"""Photo intake: hashing, EXIF extraction, de-duplication, catalog writing.

Design notes that matter to anyone touching this file:

* **The catalog is CSV, and the CSV is the durable record.** Not the photos.
  Every row carries enough (``sha256``, ``dhash``, dimensions, timestamp,
  traits) that losing the original loses the pixels but not the observation.
  That is deliberate: originals live in cold storage the project does not
  control, and permissions on cold storage are somebody else's problem.
* **GPS never enters the public catalog.** A committed row carries only
  ``has_gps`` and the coarse ``site`` label the ingester typed. Precise
  coordinates go to ``private/locations.csv``, which is gitignored. Nest- and
  roost-site precision is a judgment call for sensitive species and this repo is
  public -- see ``CLAUDE.md`` and ``PLAYBOOK.md``.
* **Two hashes, two jobs.** ``sha256`` catches the same file arriving twice
  (the group re-sends a batch). ``dhash`` catches the *same frame* arriving in
  a different size or re-compression, and clusters burst frames. Together they
  let a photo be re-identified years later from a copy, which is what makes
  cold storage safe.
* **HEIC/RAW** cannot be opened by Pillow. On macOS we shell out to ``sips``
  for a cached JPEG derivative and read that. Off macOS those files are
  recorded as ``unreadable`` rather than dropped -- a photo we cannot parse is
  still a photo the group has.
"""
from __future__ import annotations

import csv
import hashlib
import os
import shutil
import subprocess
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

from PIL import ExifTags, Image

__all__ = [
    "PhotoIntakeError",
    "PhotoRecord",
    "IMAGE_SUFFIXES",
    "PHOTO_COLUMNS",
    "SIGHTING_COLUMNS",
    "sha256_file",
    "dhash",
    "read_metadata",
    "photo_id",
    "ingest",
    "load_catalog",
    "load_private",
    "load_sightings",
]


class PhotoIntakeError(Exception):
    """Anything this tool cannot do: unreadable source, bad catalog, no room."""


#: Suffixes we treat as photos. Pillow handles the first group directly; the
#: second group needs the ``sips`` derivative path on macOS.
PILLOW_SUFFIXES = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp", ".bmp", ".gif"}
CONVERT_SUFFIXES = {".heic", ".heif", ".cr2", ".cr3", ".nef", ".arw", ".orf",
                    ".rw2", ".dng", ".raf", ".sr2", ".pef"}
IMAGE_SUFFIXES = PILLOW_SUFFIXES | CONVERT_SUFFIXES

CACHE_DIR = Path(os.path.expanduser("~/.cache/photo_intake"))

_EXIF_TAGS = {v: k for k, v in ExifTags.TAGS.items()}
_GPS_TAGS = {v: k for k, v in ExifTags.GPSTAGS.items()}

#: Column order for ``data/photos.csv``. Field columns first so the useful part
#: is visible without scrolling in a spreadsheet or on GitHub; machine-written
#: technical columns trail behind. Append new columns at the end -- adding a
#: column is free, renaming one is not.
PHOTO_COLUMNS = [
    "photo_id", "captured_at", "site", "perch", "observer",
    "individual", "id_confidence", "age", "sex",
    "band_visible", "band_code", "traits_seen", "quality", "processing", "notes",
    "store", "store_ref", "source_name", "date_source", "ingested_at",
    "camera", "lens", "focal_mm", "shutter", "aperture", "iso",
    "width", "height", "has_gps", "readable", "sha256", "dhash",
]

#: Column order for ``data/sightings.csv`` -- one row per observation event,
#: photographed or not. A sighting can exist with no photo (eBird, an email
#: report); a photo is evidence *for* a sighting. Joined via ``photo_ids``.
SIGHTING_COLUMNS = [
    "sighting_id", "date", "time", "site", "count", "age_classes",
    "individuals", "source", "source_ref", "photo_ids", "confidence", "notes",
]

PRIVATE_COLUMNS = ["photo_id", "source_path", "lat", "lon"]

#: Vocabulary for ``processing`` -- how much the pixels have been altered since
#: the shutter fired. **Load-bearing for trait work.** AI "enhance" and upscaling
#: warm the tone, smooth feather texture into wax, and harden soft markings into
#: discrete blobs -- which is the exact signal malar geometry and breast-barring
#: comparison depends on. An enhanced frame can look like a different bird.
#: Nothing in this column can be recovered from the file, so it has to be asked.
#: **Trait scoring uses ``out-of-camera`` frames only.**
PROCESSING_VALUES = ("", "out-of-camera", "cropped", "ai-enhanced", "screenshot")

#: Vocabulary for ``band_visible``. Empty means nobody has looked yet.
#: ``not-tested`` means a human looked and the frame does not show the tarsus --
#: which is where a band sits. The distinction is the whole point: 25 photos of
#: a crouched bird are 25 frames that never tested the band zone, and recording
#: them as "no" would invent evidence for an unbanded bird.
BAND_VISIBLE_VALUES = ("", "yes", "no", "not-tested")


@dataclass
class PhotoRecord:
    """One photo, as it appears in the public catalog.

    Intake fills only what it can read off the file. The identification
    columns (``individual``, ``age``, ``sex``, ``band_visible``, ...) are left
    empty for a human to fill in -- this tool never guesses at the bird.
    """

    photo_id: str
    captured_at: str | None
    site: str | None
    perch: str | None
    observer: str | None
    individual: str | None
    id_confidence: str | None
    age: str | None
    sex: str | None
    band_visible: str | None
    band_code: str | None
    traits_seen: str | None
    quality: str | None
    processing: str | None
    notes: str | None
    store: str | None
    store_ref: str | None
    source_name: str
    date_source: str
    ingested_at: str
    camera: str | None
    lens: str | None
    focal_mm: float | None
    shutter: str | None
    aperture: float | None
    iso: int | None
    width: int | None
    height: int | None
    has_gps: bool
    readable: bool
    sha256: str
    dhash: str

    def as_row(self) -> dict:
        """Flatten to strings the way the CSV stores them."""
        row = asdict(self)
        row["has_gps"] = _bool_out(row["has_gps"])
        row["readable"] = _bool_out(row["readable"])
        return {k: ("" if v is None else v) for k, v in row.items()}


# --------------------------------------------------------------------------
# hashing
# --------------------------------------------------------------------------

def sha256_file(path: str | Path, chunk: int = 1 << 20) -> str:
    """Content hash of the file on disk. Exact-duplicate detection."""
    h = hashlib.sha256()
    try:
        with open(path, "rb") as fh:
            while block := fh.read(chunk):
                h.update(block)
    except OSError as exc:
        raise PhotoIntakeError(f"cannot read {path}: {exc}") from exc
    return h.hexdigest()


def dhash(img: Image.Image, size: int = 8) -> str:
    """64-bit difference hash -- stable across resize and re-compression.

    Grayscale, squash to ``(size+1) x size``, then one bit per horizontal
    neighbour pair: 1 where the left pixel is brighter. Near-identical frames
    land within a few bits of each other (see :func:`hamming`).
    """
    small = img.convert("L").resize((size + 1, size), Image.Resampling.LANCZOS)
    flatten = getattr(small, "get_flattened_data", small.getdata)  # Pillow >= 12
    px = list(flatten())
    bits = 0
    for row in range(size):
        base = row * (size + 1)
        for col in range(size):
            bits = (bits << 1) | int(px[base + col] > px[base + col + 1])
    return f"{bits:016x}"


def hamming(a: str, b: str) -> int:
    """Bit distance between two dhash strings. <= 5 reads as 'same frame'.

    Raises :class:`PhotoIntakeError` on anything that is not a 16-hex-digit
    hash. A spreadsheet round-trip turns an all-digit dhash into scientific
    notation (``1.04869E+15``), and that must not surface as a raw traceback.
    """
    for name, value in (("a", a), ("b", b)):
        if len(value) != 16 or any(c not in "0123456789abcdefABCDEF" for c in value):
            raise PhotoIntakeError(
                f"{name}={value!r} is not a 16-hex-digit dhash. If this came from "
                f"the catalog, a spreadsheet probably reformatted the column.")
    return bin(int(a, 16) ^ int(b, 16)).count("1")


def is_degenerate_dhash(value: str) -> bool:
    """True when a dhash carries no information and must not be matched on.

    :func:`dhash` only compares *horizontal* neighbours, so anything without
    horizontal contrast collapses to all-zeros — a uniform frame, but also a
    smooth vertical gradient. An overcast sky behind a perched bird is exactly
    that, and it is a common frame in this archive. Matching on it would report
    every flat-sky photo as a burst duplicate of the first one.
    """
    return (not value) or set(value) <= {"0"} or set(value.lower()) <= {"f"}


# --------------------------------------------------------------------------
# reading the file
# --------------------------------------------------------------------------

def _derivative(path: Path) -> Path | None:
    """A cached JPEG rendering of a HEIC/RAW original, via macOS ``sips``.

    Returns None when no converter exists (non-macOS, or sips refuses the
    format). Caller treats that as ``readable=False``.
    """
    if not shutil.which("sips"):
        return None
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    try:
        stat = path.stat()
    except OSError as exc:
        raise PhotoIntakeError(f"cannot stat {path}: {exc}") from exc
    key = hashlib.sha256(
        f"{path.resolve()}|{stat.st_size}|{stat.st_mtime_ns}".encode()
    ).hexdigest()[:16]
    out = CACHE_DIR / f"{key}.jpg"
    if out.exists():
        return out
    proc = subprocess.run(
        ["sips", "-s", "format", "jpeg", str(path), "--out", str(out)],
        capture_output=True, text=True,
    )
    if proc.returncode != 0 or not out.exists():
        return None
    return out


def _exif_datetime(raw: dict) -> str | None:
    """EXIF ``DateTimeOriginal`` (fall back to ``DateTime``) as ISO-8601 local.

    EXIF timestamps carry no zone, so we emit a naive ISO string and say so in
    ``date_source``. Do not pretend to a UTC offset we were not given.
    """
    for tag in ("DateTimeOriginal", "DateTimeDigitized", "DateTime"):
        value = raw.get(tag)
        if not value:
            continue
        try:
            return datetime.strptime(str(value).strip(),
                                     "%Y:%m:%d %H:%M:%S").isoformat()
        except ValueError:
            continue
    return None


def _gps(raw_gps: dict) -> tuple[float, float] | None:
    """Decode EXIF GPS into signed decimal degrees, or None."""
    def deg(dms) -> float:
        d, m, s = (float(x) for x in dms)
        return d + m / 60 + s / 3600

    try:
        lat = deg(raw_gps["GPSLatitude"])
        lon = deg(raw_gps["GPSLongitude"])
    except (KeyError, TypeError, ValueError, ZeroDivisionError):
        return None

    # An all-zero block is a camera saying "no fix", not a position in the Gulf
    # of Guinea. Accepting it puts has_gps=yes in the public catalog and plots
    # Null Island on the map.
    if lat == 0 and lon == 0:
        return None

    # Never default the hemisphere. Without the ref tags the magnitude is known
    # and the sign is not -- and guessing "E" turns Nashua's 71.45 W into
    # 71.45 E, which is a different continent. Some exports drop the refs.
    lat_ref = str(raw_gps.get("GPSLatitudeRef", "")).strip().upper()
    lon_ref = str(raw_gps.get("GPSLongitudeRef", "")).strip().upper()
    if not lat_ref.startswith(("N", "S")) or not lon_ref.startswith(("E", "W")):
        return None
    if lat_ref.startswith("S"):
        lat = -lat
    if lon_ref.startswith("W"):
        lon = -lon
    return lat, lon


def read_metadata(path: str | Path) -> dict:
    """Everything intake knows about one image file.

    Returns a dict with ``readable``, ``dhash``, ``width``/``height``, the EXIF
    capture fields, and ``gps`` (a ``(lat, lon)`` tuple or None). Never raises
    on a merely-unparseable image -- an unreadable photo still gets catalogued.
    """
    path = Path(path)
    out: dict = {
        "readable": False, "dhash": None, "width": None, "height": None,
        "captured_at": None, "date_source": "none", "camera": None,
        "lens": None, "focal_mm": None, "shutter": None, "aperture": None,
        "iso": None, "gps": None,
    }

    target = path
    if path.suffix.lower() in CONVERT_SUFFIXES:
        derived = _derivative(path)
        if derived is None:
            out["date_source"] = "file-mtime"
            out["captured_at"] = _mtime_iso(path)
            return out
        target = derived

    try:
        with Image.open(target) as img:
            img.load()
            out["width"], out["height"] = img.size
            out["dhash"] = dhash(img)
            out["readable"] = True
            exif = img.getexif()
    except (OSError, ValueError) as exc:  # truncated, unsupported, corrupt
        out["date_source"] = "file-mtime"
        out["captured_at"] = _mtime_iso(path)
        out["error"] = str(exc)
        return out

    raw = {ExifTags.TAGS.get(k, k): v for k, v in exif.items()}
    ifd = exif.get_ifd(_EXIF_TAGS["ExifOffset"]) if _EXIF_TAGS.get("ExifOffset") else {}
    raw.update({ExifTags.TAGS.get(k, k): v for k, v in (ifd or {}).items()})

    out["camera"] = _clean(raw.get("Model"))
    make = _clean(raw.get("Make"))
    if make and out["camera"] and not out["camera"].lower().startswith(make.lower()):
        out["camera"] = f"{make} {out['camera']}"
    out["lens"] = _clean(raw.get("LensModel"))
    out["focal_mm"] = _num(raw.get("FocalLength"))
    out["aperture"] = _num(raw.get("FNumber"))
    out["iso"] = _int(raw.get("ISOSpeedRatings") or raw.get("PhotographicSensitivity"))
    out["shutter"] = _shutter(raw.get("ExposureTime"))

    captured = _exif_datetime(raw)
    if captured:
        out["captured_at"] = captured
        out["date_source"] = "exif"
    else:
        out["captured_at"] = _mtime_iso(path)
        out["date_source"] = "file-mtime"

    gps_ifd = exif.get_ifd(_EXIF_TAGS["GPSInfo"]) if _EXIF_TAGS.get("GPSInfo") else {}
    if gps_ifd:
        out["gps"] = _gps({ExifTags.GPSTAGS.get(k, k): v for k, v in gps_ifd.items()})
    return out


def _mtime_iso(path: Path) -> str | None:
    try:
        return datetime.fromtimestamp(path.stat().st_mtime).isoformat(
            timespec="seconds")
    except OSError:
        return None


def _clean(value) -> str | None:
    if value is None:
        return None
    text = str(value).strip().strip("\x00")
    return text or None


def _num(value) -> float | None:
    try:
        return round(float(value), 2)
    except (TypeError, ValueError, ZeroDivisionError):
        return None


def _int(value) -> int | None:
    if isinstance(value, (list, tuple)):
        value = value[0] if value else None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _shutter(value) -> str | None:
    """EXIF exposure time as a human string: ``1/2000`` or ``1.3s``.

    Deliberately does not go through :func:`_num` -- its 2-decimal rounding
    flattens every fast shutter (0.0005s) to zero, and fast shutters are the
    whole point on a fast-moving animal.
    """
    try:
        seconds = float(value)
    except (TypeError, ValueError, ZeroDivisionError):
        return None
    if seconds <= 0:
        return None
    if seconds >= 1:
        return f"{seconds:g}s"
    return f"1/{round(1 / seconds)}"


def _bool_out(value) -> str:
    """Booleans as yes/no -- this file gets read by people, not just code."""
    return "yes" if value else "no"


def _bool_in(value) -> bool:
    return str(value).strip().lower() in {"yes", "true", "1", "y"}


# --------------------------------------------------------------------------
# catalog
# --------------------------------------------------------------------------

def photo_id(captured_at: str | None, sha: str) -> str:
    """Stable, sortable, collision-resistant: ``YYYYMMDD-<8 hex>``.

    Derived only from capture date + content, so re-ingesting the same file
    after a rename produces the same id. The leading digits plus a hyphen keep
    spreadsheets from helpfully reinterpreting it as a date or a number.
    """
    day = (captured_at or "unknown")[:10].replace("-", "") or "unknown"
    return f"{day}-{sha[:8]}"


def read_csv(path: str | Path) -> list[dict]:
    """Read a CSV into dicts. A missing file is empty, not an error."""
    path = Path(path)
    if not path.exists():
        return []
    try:
        with open(path, newline="", encoding="utf-8-sig") as fh:
            return [dict(row) for row in csv.DictReader(fh)]
    except OSError as exc:
        raise PhotoIntakeError(f"cannot read {path}: {exc}") from exc


def load_catalog(root: str | Path) -> list[dict]:
    """Rows of ``data/photos.csv`` under ``root``."""
    return read_csv(Path(root) / "data" / "photos.csv")


def load_sightings(root: str | Path) -> list[dict]:
    """Rows of ``data/sightings.csv`` under ``root``."""
    return read_csv(Path(root) / "data" / "sightings.csv")


def load_private(root: str | Path) -> dict[str, dict]:
    """The gitignored photo_id -> {lat, lon, source_path} sidecar."""
    return {r["photo_id"]: r
            for r in read_csv(Path(root) / "private" / "locations.csv")}


def append_csv(path: Path, columns: list[str], rows: list[dict]) -> None:
    """Append rows, migrating the file if its header predates ``columns``.

    Unknown keys are dropped and missing ones blank-filled, so a catalog
    written by an older column set still loads and re-saves cleanly.

    **The header is checked, not assumed.** Appending a 32-field row to a file
    whose header has 6 names writes the overflow into no column at all, and
    ``DictReader`` then buries it under the ``None`` key -- which silently
    breaks sha256 de-duplication and starts producing duplicate catalog rows.
    Adding a column is meant to be free (see ``data/README.md``), so when the
    header differs the whole file is rewritten with the union of both, old rows
    preserved and blank-filled.
    """
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)

    existing_header: list[str] = []
    if path.exists():
        with open(path, newline="", encoding="utf-8-sig") as fh:
            existing_header = next(csv.reader(fh), [])

    if existing_header and existing_header != list(columns):
        # Union, preserving the declared order first so the layout stays stable.
        merged = list(columns) + [c for c in existing_header if c not in columns]
        old_rows = read_csv(path)
        with open(path, "w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=merged, extrasaction="ignore")
            writer.writeheader()
            for row in old_rows + list(rows):
                writer.writerow({c: row.get(c, "") or "" for c in merged})
        return

    with open(path, "a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        if not existing_header:
            writer.writeheader()
        for row in rows:
            writer.writerow({c: row.get(c, "") for c in columns})


def iter_images(paths) -> list[Path]:
    """Expand files and directories into a sorted list of image paths."""
    found: list[Path] = []
    for raw in paths:
        p = Path(raw).expanduser()
        if p.is_dir():
            found += [q for q in p.rglob("*")
                      if q.is_file() and q.suffix.lower() in IMAGE_SUFFIXES]
        elif p.is_file():
            if p.suffix.lower() not in IMAGE_SUFFIXES:
                raise PhotoIntakeError(f"{p} is not a recognised image type")
            found.append(p)
        else:
            raise PhotoIntakeError(f"no such file or directory: {p}")
    return sorted(set(found))


def ingest(
    paths,
    root: str | Path,
    site: str | None = None,
    observer: str | None = None,
    perch: str | None = None,
    store: str | None = None,
    copy: bool = False,
    dry_run: bool = False,
) -> dict:
    """Ingest photos into the catalog under ``root``.

    Returns ``{"added": [PhotoRecord], "duplicates": [...], "near": [...]}``.
    ``duplicates`` are exact sha256 repeats (skipped). ``near`` are new photos
    whose dhash is within 5 bits of something already catalogued -- reported,
    not skipped, because burst frames are legitimately separate photos.

    ``copy`` defaults to **off**: the catalog row is the durable record, and
    originals are expected to live in cold storage elsewhere. Pass ``copy=True``
    only when this machine should also keep the bytes.
    """
    root = Path(root)
    catalog_path = root / "data" / "photos.csv"
    private_path = root / "private" / "locations.csv"

    existing = load_catalog(root)
    seen_sha = {r["sha256"] for r in existing if r.get("sha256")}
    seen_dhash = [(r["dhash"], r["photo_id"]) for r in existing if r.get("dhash")]

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    added: list[PhotoRecord] = []
    private_rows: list[dict] = []
    duplicates: list[tuple[Path, str]] = []
    near: list[tuple[str, str, int]] = []
    pending_copies: list[tuple[PhotoRecord, Path]] = []

    for src in iter_images(paths):
        sha = sha256_file(src)
        if sha in seen_sha:
            duplicates.append((src, sha))
            continue
        seen_sha.add(sha)

        meta = read_metadata(src)
        pid = photo_id(meta["captured_at"], sha)

        if meta["dhash"] and not is_degenerate_dhash(meta["dhash"]):
            for other_hash, other_id in seen_dhash:
                try:
                    distance = hamming(meta["dhash"], other_hash)
                except PhotoIntakeError:
                    continue  # a mangled catalog row must not kill the run
                if distance <= 5:
                    near.append((pid, other_id, distance))
                    break
            seen_dhash.append((meta["dhash"], pid))

        record = PhotoRecord(
            photo_id=pid,
            captured_at=meta["captured_at"],
            site=site,
            perch=perch,
            observer=observer,
            individual=None,
            id_confidence=None,
            age=None,
            sex=None,
            band_visible=None,
            band_code=None,
            traits_seen=None,
            quality=None,
            processing=None,
            notes=None,
            store=store,
            store_ref=None,
            source_name=src.name,
            date_source=meta["date_source"],
            ingested_at=now,
            camera=meta["camera"],
            lens=meta["lens"],
            focal_mm=meta["focal_mm"],
            shutter=meta["shutter"],
            aperture=meta["aperture"],
            iso=meta["iso"],
            width=meta["width"],
            height=meta["height"],
            has_gps=meta["gps"] is not None,
            readable=meta["readable"],
            sha256=sha,
            dhash=meta["dhash"] or "",
        )
        added.append(record)
        pending_copies.append((record, src))

        # Precise location and the original absolute path stay out of the
        # public catalog -- this file is gitignored on purpose. Written for
        # every photo, GPS or not, so the trail back to the original survives.
        private_rows.append({
            "photo_id": pid,
            "source_path": str(src.resolve()),
            "lat": meta["gps"][0] if meta["gps"] else "",
            "lon": meta["gps"][1] if meta["gps"] else "",
        })

    # Copying happens only after every file has been read successfully. Doing it
    # inside the loop meant an error on photo N of 500 left N-1 originals in
    # photos/ with zero catalog rows pointing at them, and discarded the rest.
    if copy and not dry_run:
        for record, src in pending_copies:
            record.store_ref = _store(src, root, record.photo_id, record.captured_at)
            record.store = record.store or "local"

    if not dry_run:
        append_csv(catalog_path, PHOTO_COLUMNS, [r.as_row() for r in added])
        append_csv(private_path, PRIVATE_COLUMNS, private_rows)

    return {"added": added, "duplicates": duplicates, "near": near}


def _store(src: Path, root: Path, pid: str, captured_at: str | None) -> str:
    """Copy an original into ``photos/YYYY/MM/<id><ext>``; return relative path."""
    stamp = captured_at or "0000-00"
    year, month = stamp[:4] or "unknown", stamp[5:7] or "00"
    dest_dir = root / "photos" / year / month
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{pid}{src.suffix.lower()}"
    if not dest.exists():
        try:
            shutil.copy2(src, dest)
        except OSError as exc:
            raise PhotoIntakeError(f"cannot copy {src} -> {dest}: {exc}") from exc
    return str(dest.relative_to(root))

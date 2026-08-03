"""Photo intake: hashing, EXIF extraction, de-duplication, catalog writing.

Design notes that matter to anyone touching this file:

* **GPS never enters the public catalog.** A committed row carries only
  ``has_gps`` and the coarse ``site`` label the ingester typed. Precise
  coordinates go to ``private/locations.jsonl``, which is gitignored. Peregrine
  nest-site precision is a judgment call and this repo is public -- see
  ``CLAUDE.md``.
* **Two hashes, two jobs.** ``sha256`` catches the same file arriving twice
  (the group re-sends a batch). ``dhash`` catches the *same frame* arriving in
  a different size or re-compression, and clusters burst frames.
* **HEIC/RAW** cannot be opened by Pillow. On macOS we shell out to ``sips``
  for a cached JPEG derivative and read that. Off macOS those files are
  recorded as ``unreadable`` rather than dropped -- a photo we cannot parse is
  still a photo the group has.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from PIL import ExifTags, Image

__all__ = [
    "PhotoIntakeError",
    "PhotoRecord",
    "IMAGE_SUFFIXES",
    "sha256_file",
    "dhash",
    "read_metadata",
    "photo_id",
    "ingest",
    "load_catalog",
    "load_private",
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


@dataclass
class PhotoRecord:
    """One photo, as it appears in the public catalog.

    Fields left empty at ingest (``individual``, ``bands``, ``traits``) are the
    hooks the ID work fills in later; intake never guesses at them.
    """

    id: str
    sha256: str
    dhash: str
    source_name: str
    stored_path: str | None
    captured_at: str | None
    captured_source: str
    site: str | None
    observer: str | None
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
    ingested_at: str
    individual: str | None = None
    bands: str | None = None
    traits: dict = field(default_factory=dict)
    notes: str | None = None

    def as_row(self) -> dict:
        return asdict(self)


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
    """Bit distance between two dhash strings. <= 5 reads as 'same frame'."""
    return bin(int(a, 16) ^ int(b, 16)).count("1")


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
    ``captured_source``. Do not pretend to a UTC offset we were not given.
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
    if str(raw_gps.get("GPSLatitudeRef", "N")).upper().startswith("S"):
        lat = -lat
    if str(raw_gps.get("GPSLongitudeRef", "E")).upper().startswith("W"):
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
        "captured_at": None, "captured_source": "none", "camera": None,
        "lens": None, "focal_mm": None, "shutter": None, "aperture": None,
        "iso": None, "gps": None,
    }

    target = path
    if path.suffix.lower() in CONVERT_SUFFIXES:
        derived = _derivative(path)
        if derived is None:
            out["captured_source"] = "file-mtime"
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
        out["captured_source"] = "file-mtime"
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
        out["captured_source"] = "exif"
    else:
        out["captured_at"] = _mtime_iso(path)
        out["captured_source"] = "file-mtime"

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
    whole point on a stooping falcon.
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


# --------------------------------------------------------------------------
# catalog
# --------------------------------------------------------------------------

def photo_id(captured_at: str | None, sha: str) -> str:
    """Stable, sortable, collision-resistant: ``YYYYMMDD-<8 hex>``.

    Derived only from capture date + content, so re-ingesting the same file
    after a rename produces the same id.
    """
    day = (captured_at or "unknown")[:10].replace("-", "") or "unknown"
    return f"{day}-{sha[:8]}"


def load_catalog(catalog_path: str | Path) -> list[dict]:
    """Read a JSONL catalog. Missing file is an empty catalog, not an error."""
    path = Path(catalog_path)
    if not path.exists():
        return []
    rows = []
    with open(path) as fh:
        for lineno, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except ValueError as exc:
                raise PhotoIntakeError(
                    f"{path}:{lineno} is not valid JSON: {exc}") from exc
    return rows


def load_private(private_path: str | Path) -> dict[str, dict]:
    """Read the gitignored id -> {gps, source_path} sidecar, keyed by photo id."""
    return {r["id"]: r for r in load_catalog(private_path)}


def _append(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a") as fh:
        for row in rows:
            fh.write(json.dumps(row, sort_keys=True) + "\n")


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
    copy: bool = True,
    dry_run: bool = False,
) -> dict:
    """Ingest photos into the catalog under ``root``.

    Returns ``{"added": [PhotoRecord], "duplicates": [...], "near": [...]}``.
    ``duplicates`` are exact sha256 repeats (skipped). ``near`` are new photos
    whose dhash is within 5 bits of something already catalogued -- reported,
    not skipped, because burst frames are legitimately separate photos.
    """
    root = Path(root)
    catalog_path = root / "data" / "catalog.jsonl"
    private_path = root / "private" / "locations.jsonl"

    existing = load_catalog(catalog_path)
    seen_sha = {r["sha256"] for r in existing}
    seen_dhash = [(r["dhash"], r["id"]) for r in existing if r.get("dhash")]

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    added: list[PhotoRecord] = []
    private_rows: list[dict] = []
    duplicates: list[tuple[Path, str]] = []
    near: list[tuple[str, str, int]] = []

    for src in iter_images(paths):
        sha = sha256_file(src)
        if sha in seen_sha:
            duplicates.append((src, sha))
            continue
        seen_sha.add(sha)

        meta = read_metadata(src)
        pid = photo_id(meta["captured_at"], sha)

        if meta["dhash"]:
            for other_hash, other_id in seen_dhash:
                distance = hamming(meta["dhash"], other_hash)
                if distance <= 5:
                    near.append((pid, other_id, distance))
                    break
            seen_dhash.append((meta["dhash"], pid))

        stored = None
        if copy and not dry_run:
            stored = _store(src, root, pid, meta["captured_at"])

        record = PhotoRecord(
            id=pid,
            sha256=sha,
            dhash=meta["dhash"] or "",
            source_name=src.name,
            stored_path=stored,
            captured_at=meta["captured_at"],
            captured_source=meta["captured_source"],
            site=site,
            observer=observer,
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
            ingested_at=now,
        )
        added.append(record)

        # Precise location and the original absolute path stay out of the
        # public catalog -- this file is gitignored on purpose. Written for
        # every photo, GPS or not, so the trail back to the original survives.
        private_rows.append({
            "id": pid,
            "source_path": str(src.resolve()),
            "lat": meta["gps"][0] if meta["gps"] else None,
            "lon": meta["gps"][1] if meta["gps"] else None,
        })

    if not dry_run:
        _append(catalog_path, [r.as_row() for r in added])
        _append(private_path, private_rows)

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

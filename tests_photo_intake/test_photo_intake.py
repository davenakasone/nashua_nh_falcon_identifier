"""Offline tests for photo_intake. No network, no real falcons."""
from __future__ import annotations

import json
from pathlib import Path

import pytest
from PIL import Image

from photo_intake import core


def _img(path: Path, size=(120, 90), seed=0, fmt="JPEG") -> Path:
    """A deterministic non-uniform test image (uniform images hash to zero)."""
    img = Image.new("RGB", size)
    img.putdata([((x * 7 + y * 13 + seed) % 256,
                  (x * 3 + seed) % 256,
                  (y * 5 + seed) % 256)
                 for y in range(size[1]) for x in range(size[0])])
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, fmt, quality=95)
    return path


# --------------------------------------------------------------------------
# hashing
# --------------------------------------------------------------------------

def test_sha256_matches_content_not_name(tmp_path):
    a = _img(tmp_path / "a.jpg", seed=1)
    b = tmp_path / "renamed.jpg"
    b.write_bytes(a.read_bytes())
    assert core.sha256_file(a) == core.sha256_file(b)


def test_dhash_survives_resize(tmp_path):
    original = _img(tmp_path / "big.jpg", size=(400, 300), seed=3)
    with Image.open(original) as img:
        first = core.dhash(img)
        second = core.dhash(img.resize((200, 150)))
    assert core.hamming(first, second) <= 5


def test_dhash_separates_different_images(tmp_path):
    with Image.open(_img(tmp_path / "x.jpg", seed=0)) as a:
        ha = core.dhash(a)
    with Image.open(_img(tmp_path / "y.jpg", seed=128)) as b:
        hb = core.dhash(b)
    assert core.hamming(ha, hb) > 5


def test_hamming_is_symmetric_and_zero_on_self():
    assert core.hamming("00ff00ff00ff00ff", "00ff00ff00ff00ff") == 0
    assert core.hamming("0000000000000000", "ffffffffffffffff") == 64


# --------------------------------------------------------------------------
# metadata
# --------------------------------------------------------------------------

def test_read_metadata_without_exif_falls_back_to_mtime(tmp_path):
    meta = core.read_metadata(_img(tmp_path / "bare.jpg"))
    assert meta["readable"] is True
    assert meta["width"] == 120 and meta["height"] == 90
    assert meta["captured_source"] == "file-mtime"
    assert meta["captured_at"] is not None
    assert meta["gps"] is None


def test_read_metadata_parses_exif_datetime_and_camera(tmp_path):
    from PIL import Image as PILImage
    path = tmp_path / "exif.jpg"
    _img(path, seed=9)
    with PILImage.open(path) as img:
        exif = img.getexif()
        exif[core._EXIF_TAGS["Model"]] = "EOS R7"
        exif[core._EXIF_TAGS["Make"]] = "Canon"
        exif[core._EXIF_TAGS["DateTimeOriginal"]] = "2026:08:03 06:41:12"
        img.save(path, "JPEG", exif=exif)

    meta = core.read_metadata(path)
    assert meta["captured_at"] == "2026-08-03T06:41:12"
    assert meta["captured_source"] == "exif"
    assert meta["camera"] == "Canon EOS R7"


def test_read_metadata_on_a_non_image_is_recorded_not_raised(tmp_path):
    junk = tmp_path / "broken.jpg"
    junk.write_bytes(b"this is not a jpeg")
    meta = core.read_metadata(junk)
    assert meta["readable"] is False
    assert meta["captured_source"] == "file-mtime"


def test_gps_decoding_signs_western_longitude():
    # Nashua is 42.7N, 71.4W -- longitude must come back negative.
    coords = core._gps({
        "GPSLatitude": (42, 45, 0), "GPSLatitudeRef": "N",
        "GPSLongitude": (71, 27, 0), "GPSLongitudeRef": "W",
    })
    assert coords is not None
    lat, lon = coords
    assert lat == pytest.approx(42.75, abs=1e-6)
    assert lon == pytest.approx(-71.45, abs=1e-6)


def test_gps_decoding_returns_none_when_incomplete():
    assert core._gps({"GPSLatitude": (42, 45, 0)}) is None


def test_shutter_formatting():
    assert core._shutter(0.0005) == "1/2000"
    assert core._shutter(2) == "2s"
    assert core._shutter(0) is None
    assert core._shutter(None) is None


# --------------------------------------------------------------------------
# ids and catalog
# --------------------------------------------------------------------------

def test_photo_id_is_stable_and_sortable():
    sha = "deadbeef" * 8
    assert core.photo_id("2026-08-03T06:41:12", sha) == "20260803-deadbeef"
    assert core.photo_id(None, sha) == "unknown-deadbeef"


def test_ingest_writes_public_and_private_rows(tmp_path):
    src = tmp_path / "src"
    _img(src / "one.jpg", seed=11)
    root = tmp_path / "repo"

    result = core.ingest([src], root=root, site="nashua-downtown",
                         observer="david")
    assert len(result["added"]) == 1

    public = core.load_catalog(root / "data" / "catalog.jsonl")
    assert len(public) == 1
    row = public[0]
    assert row["site"] == "nashua-downtown" and row["observer"] == "david"
    assert row["individual"] is None  # intake never guesses at the bird
    assert "lat" not in row and "lon" not in row

    private = core.load_private(root / "private" / "locations.jsonl")
    assert private[row["id"]]["source_path"].endswith("one.jpg")


def test_public_catalog_never_contains_coordinates(tmp_path):
    """The load-bearing privacy guarantee: no coords in the committed file."""
    from PIL import Image as PILImage
    src = tmp_path / "src"
    path = _img(src / "geo.jpg", seed=21)
    with PILImage.open(path) as img:
        exif = img.getexif()
        gps = {
            core._GPS_TAGS["GPSLatitude"]: (42.0, 45.0, 0.0),
            core._GPS_TAGS["GPSLatitudeRef"]: "N",
            core._GPS_TAGS["GPSLongitude"]: (71.0, 27.0, 0.0),
            core._GPS_TAGS["GPSLongitudeRef"]: "W",
        }
        exif[core._EXIF_TAGS["GPSInfo"]] = gps
        img.save(path, "JPEG", exif=exif)

    root = tmp_path / "repo"
    core.ingest([src], root=root, site="nashua-downtown")

    raw = (root / "data" / "catalog.jsonl").read_text()
    assert '"has_gps": true' in raw
    assert "42.75" not in raw and "71.45" not in raw

    private = core.load_private(root / "private" / "locations.jsonl")
    (row,) = private.values()
    assert row["lat"] == pytest.approx(42.75, abs=1e-6)
    assert row["lon"] == pytest.approx(-71.45, abs=1e-6)


def test_reingesting_the_same_file_is_a_no_op(tmp_path):
    src = tmp_path / "src"
    _img(src / "one.jpg", seed=31)
    root = tmp_path / "repo"

    core.ingest([src], root=root)
    again = core.ingest([src], root=root)

    assert again["added"] == []
    assert len(again["duplicates"]) == 1
    assert len(core.load_catalog(root / "data" / "catalog.jsonl")) == 1


def test_burst_frames_are_flagged_but_both_kept(tmp_path):
    """Two near-identical frames are separate photos -- report, don't drop."""
    src = tmp_path / "src"
    first = _img(src / "burst1.jpg", size=(400, 300), seed=41)
    with Image.open(first) as img:
        img.resize((380, 285)).save(src / "burst2.jpg", "JPEG", quality=90)

    root = tmp_path / "repo"
    result = core.ingest([src], root=root)

    assert len(result["added"]) == 2
    assert len(result["near"]) == 1


def test_copy_stores_originals_under_year_month(tmp_path):
    from PIL import Image as PILImage
    src = tmp_path / "src"
    path = _img(src / "one.jpg", seed=51)
    with PILImage.open(path) as img:
        exif = img.getexif()
        exif[core._EXIF_TAGS["DateTimeOriginal"]] = "2026:08:03 06:41:12"
        img.save(path, "JPEG", exif=exif)

    root = tmp_path / "repo"
    (record,) = core.ingest([src], root=root)["added"]
    assert record.stored_path == f"photos/2026/08/{record.id}.jpg"
    assert (root / record.stored_path).exists()


def test_no_copy_leaves_stored_path_empty(tmp_path):
    src = tmp_path / "src"
    _img(src / "one.jpg", seed=61)
    root = tmp_path / "repo"
    (record,) = core.ingest([src], root=root, copy=False)["added"]
    assert record.stored_path is None
    assert not (root / "photos").exists()


def test_dry_run_writes_nothing(tmp_path):
    src = tmp_path / "src"
    _img(src / "one.jpg", seed=71)
    root = tmp_path / "repo"
    result = core.ingest([src], root=root, dry_run=True)
    assert len(result["added"]) == 1
    assert not (root / "data" / "catalog.jsonl").exists()
    assert not (root / "photos").exists()


def test_iter_images_skips_non_images_in_a_directory(tmp_path):
    src = tmp_path / "src"
    _img(src / "a.jpg")
    _img(src / "nested" / "b.png", fmt="PNG")
    (src / "notes.txt").write_text("field notes")
    assert [p.name for p in core.iter_images([src])] == ["a.jpg", "b.png"]


def test_iter_images_rejects_an_explicit_non_image(tmp_path):
    notes = tmp_path / "notes.txt"
    notes.write_text("field notes")
    with pytest.raises(core.PhotoIntakeError, match="not a recognised image"):
        core.iter_images([notes])


def test_iter_images_rejects_a_missing_path(tmp_path):
    with pytest.raises(core.PhotoIntakeError, match="no such file"):
        core.iter_images([tmp_path / "nope"])


def test_load_catalog_of_missing_file_is_empty(tmp_path):
    assert core.load_catalog(tmp_path / "nothing.jsonl") == []


def test_load_catalog_reports_the_bad_line(tmp_path):
    path = tmp_path / "catalog.jsonl"
    path.write_text('{"id": "ok"}\nnot json\n')
    with pytest.raises(core.PhotoIntakeError, match="catalog.jsonl:2"):
        core.load_catalog(path)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def test_cli_ingest_then_list_then_show(tmp_path, capsys):
    from photo_intake.__main__ import main

    src = tmp_path / "src"
    _img(src / "one.jpg", seed=81)
    root = tmp_path / "repo"

    assert main(["--root", str(root), "ingest", str(src),
                 "--site", "nashua-downtown", "--observer", "mark"]) == 0
    pid = core.load_catalog(root / "data" / "catalog.jsonl")[0]["id"]

    assert main(["--root", str(root), "list"]) == 0
    assert pid in capsys.readouterr().out

    assert main(["--root", str(root), "show", pid[:12]]) == 0
    assert "nashua-downtown" in capsys.readouterr().out

    assert main(["--root", str(root), "stats"]) == 0
    assert "unassigned" in capsys.readouterr().out


def test_cli_show_unknown_id_exits_nonzero(tmp_path):
    from photo_intake.__main__ import main
    assert main(["--root", str(tmp_path), "show", "nope"]) == 1


def test_cli_list_unassigned_filter(tmp_path, capsys):
    from photo_intake.__main__ import main

    src = tmp_path / "src"
    _img(src / "one.jpg", seed=91)
    root = tmp_path / "repo"
    core.ingest([src], root=root)

    catalog = root / "data" / "catalog.jsonl"
    row = json.loads(catalog.read_text().strip())
    row["individual"] = "nashua-female"
    catalog.write_text(json.dumps(row, sort_keys=True) + "\n")

    assert main(["--root", str(root), "list", "--unassigned"]) == 0
    assert "no photos match" in capsys.readouterr().out
    assert main(["--root", str(root), "list", "--individual",
                 "nashua-female"]) == 0
    assert "nashua-female" in capsys.readouterr().out

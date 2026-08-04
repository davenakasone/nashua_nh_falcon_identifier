# data/ — the two tables

CSV on purpose. Three people need to read this, GitHub renders CSV as a sortable
table, and a CSV diff is legible in a commit. The cost is no nested fields, so
everything is flat and multi-value cells use `;` as the separator.

**The CSV is the durable record — not the photos.** Every photo row carries
`sha256`, `dhash`, dimensions and a timestamp, so losing an original loses the
pixels but not the observation, and a copy that turns up years later can be
matched back to its row. That is what makes it safe to keep originals in cold
storage this project does not control.

## Why two tables

`photos.csv` is one row per photo. `sightings.csv` is one row per observation
**event**. They are not the same thing:

- A sighting can have no photo at all — that is most of the eBird and email
  intel.
- A sighting can have many photos, and a burst of twelve frames is one sighting.

Join them through `sightings.photo_ids` (a `;`-separated list of `photo_id`).

## photos.csv

Machine-written by `photo_intake` at ingest, then filled in by hand as the ID
work happens. Intake fills only what it can read off the file; every
identification column starts empty because **the tool never guesses at the
bird.**

| column | who fills it | notes |
|---|---|---|
| `photo_id` | intake | `YYYYMMDD-<8 hex>` from capture date + content hash. Stable across renames. |
| `captured_at`, `date_source` | intake | `date_source` is `exif`, `file-mtime` or `manual`. Never treat an mtime date as real. |
| `site`, `perch`, `observer` | ingest flags | `perch` earns its column — a repeated perch is what makes trait comparison possible. |
| `individual`, `id_confidence` | human | Slug from `individuals/`; tier from `docs/id_method.md`. |
| `age`, `sex` | human | `adult` / `juvenile` / `unknown`. Age reads off even a mediocre photo. |
| `band_visible`, `band_code` | human | See the vocabulary below — this one matters. |
| `traits_seen` | human | Which views the frame actually offers: `malar;breast;legs;spread-wing`. |
| `quality` | human | `good` / `soft` / `backlit` / `noisy`. |
| `store`, `store_ref` | ingest flags | Where the original lives. |
| `camera` … `dhash` | intake | EXIF and the two hashes. |

### `band_visible` — the vocabulary that carries the lesson

| value | means |
|---|---|
| *(empty)* | Nobody has looked at this frame yet. |
| `not-tested` | A human looked, and the frame does not show the **tarsus**. |
| `no` | The tarsus is clearly visible and clearly carries no band. |
| `yes` | A band is visible. Put the code in `band_code` if legible. |

The distinction between `not-tested` and `no` is the whole point. A bird
crouched on a ledge shows toes and talons — the wrong part of the leg. Recording
those frames as `no` would manufacture evidence for an unbanded bird out of
photos that never asked the question. Most of the group's album is
`not-tested` for exactly this reason — though at least one frame does show a
band; see [`../INTEL.md`](../INTEL.md).

## sightings.csv

| column | notes |
|---|---|
| `sighting_id` | `YYYYMMDD-NN`. |
| `date`, `time`, `site` | Place names only, never coordinates — see below. |
| `count`, `age_classes` | `count` is birds *seen*, not birds *identified*. |
| `individuals` | `;`-separated slugs, blank when unknown. |
| `source` | `ebird` / `email` / `photo` / `direct` / `media`. |
| `source_ref` | Enough to re-find it. For email: attribution only — `email:mark 2026-07-14` — never the body, address or thread. |
| `photo_ids` | `;`-separated join into `photos.csv`. |
| `confidence` | Tier from `docs/id_method.md`. Default `unknown`. |

## Two rules that do not bend

**No coordinates in this directory.** Place names only. Precise GPS from photo
EXIF goes to the gitignored `private/locations.csv`; the public row records only
whether a photo had GPS at all. This repo is public and peregrine nest-site
precision is a judgment call.

**No email bodies, addresses or personal details.** Email intel enters as a
fact plus an attribution, nothing more. A push is not reversible — the repo gets
cloned, cached and indexed — so redaction happens before the row is written, not
before the push.

## Changing the schema

Adding a column is free: append it to `PHOTO_COLUMNS` or `SIGHTING_COLUMNS` in
`photo_intake/core.py` and old rows blank-fill on the next read. Renaming a
column, or changing what `photo_id` means or what `probable` means, is expensive
once there are rows. Let the descriptive columns drift; keep the id scheme and
the confidence vocabulary fixed.

**Editing these by hand:** fine, and expected. Use a text editor or import into
a spreadsheet **as text**. Excel and Numbers will silently reformat anything
that looks like a date or a number if you let them autodetect.

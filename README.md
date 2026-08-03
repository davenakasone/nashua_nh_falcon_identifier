# nashua_nh_falcon_identifier

Individual identification of the Peregrine Falcons of Nashua, NH — helping a
local observation group tell its birds apart and keep one honest record.

The question this repo exists to answer: **can you tell one Peregrine from
another in a photograph?** The short answer is yes, but bands and molt gaps do
almost all of the work, and generic AI image-matching does none of it. The long
answer, with the trait ladder and the photo protocol that follows from it, is in
[`docs/id_method.md`](docs/id_method.md).

## What's here

| | |
|---|---|
| [`docs/id_method.md`](docs/id_method.md) | How individual ID actually works on this species, what doesn't work, the confidence ladder, and what to photograph |
| [`data/`](data/README.md) | The database — `photos.csv`, `sightings.csv`, and the schema |
| [`photo_intake/`](photo_intake/) | Ingest photos into a stable, de-duplicated catalogue |
| [`individuals/`](individuals/) | One file per bird, plus the identity schema |
| [`INTEL.md`](INTEL.md) | Running log — sites, open questions, sources |

## Intake

```bash
python -m photo_intake ingest ~/Downloads/falcons --site nashua-downtown --observer david
```

Each photo gets a stable id (`YYYYMMDD-<hash>`) derived from its capture date
and contents, so re-ingesting a renamed file is a no-op. Exact duplicates are
skipped; burst frames are flagged but kept. HEIC and RAW are handled on macOS.

Then `list`, `show <id>`, and `stats` to work the catalogue.

## The catalogue outlives the photos

Originals are **not** copied in by default. Every catalogue row carries a
content hash, a perceptual hash, dimensions and a timestamp, so losing a photo
loses the pixels but not the observation — and a copy that resurfaces later can
be matched straight back to its row. That is what makes it safe to keep the
originals in cold storage somewhere else.

## A note on locations

Peregrine nest sites deserve care. This repo keeps **place names only** —
precise coordinates from photo EXIF are written to a gitignored `private/`
sidecar and never enter the committed catalogue, which records only whether a
photo had GPS at all. Photo originals are not committed either.

# nashua_nh_falcon_identifier

Individual identification of the Peregrine Falcons of Nashua, NH — helping a
local observation group tell its birds apart, keep one honest record, and find
the nest so it can be protected.

Two questions run through this repo. **Can you tell one Peregrine from another
in a photograph?** Yes — but bands and molt gaps do almost all the work, and
generic AI image-matching does none of it. And **where do they nest?** Still
open; the search is live.

## Start here

| | |
|---|---|
| **[`PLAYBOOK.md`](PLAYBOOK.md)** | **How to run one of these for a different species.** The transferable method — feasibility screen, order of operations, governance, and the three ways the data gets contaminated. Start here if you are setting up a new project. |
| [`docs/id_method.md`](docs/id_method.md) | The worked species example: how Peregrine ID actually works, what doesn't, the confidence ladder, and the photo protocol |
| [`INTEL.md`](INTEL.md) | Running log — birds, sites, the nest search, open questions, and the corrections trail |
| [`individuals/`](individuals/) | One file per bird, plus the identity schema |
| [`data/`](data/README.md) | The database — `photos.csv`, `sightings.csv`, and the schema |
| [`photo_intake/`](photo_intake/) | Ingest photos into a stable, de-duplicated catalogue. Species-agnostic; drops into a new project unchanged |
| [`nest_map.py`](nest_map.py) | Maps sightings, nest candidates and photo positions. Offline and keyless |

## Intake

```bash
python -m photo_intake ingest ~/Downloads/drop --site nashua-downtown --observer david
```

Each photo gets a stable id (`YYYYMMDD-<hash>`) from its capture date and
contents, so re-ingesting a renamed file is a no-op. Exact duplicates are
skipped; burst frames are flagged but kept. HEIC and RAW are handled on macOS.
Then `list`, `show <id>`, and `stats` to work the catalogue.

## The catalogue outlives the photos

Originals are **not** copied in by default. Every row carries a content hash, a
perceptual hash, dimensions and a timestamp, so losing a photo loses the pixels
but not the observation — and a copy that resurfaces later matches straight back
to its row. That is what makes it safe to keep originals in cold storage
somewhere this project does not control.

## Two things this repo is careful about

**Locations.** Place names only in committed files. Precise coordinates from
photo EXIF go to a gitignored sidecar; the committed catalogue records only
whether a photo had GPS at all. Peregrine nest sites deserve that care, and
disclosure is the one mistake that cannot be undone.

**Being wrong in public.** Several conclusions here were published and then
overturned within hours — a juvenile "disproved" by one album that simply didn't
contain it, a band code that turned out never to have been read, a plumage
difference that was an artefact of AI photo enhancement. Those are corrected
**in place, with the reasoning kept**, rather than edited away. The corrections
trail is the most useful thing in the repo and `PLAYBOOK.md` §6 exists because
of it.

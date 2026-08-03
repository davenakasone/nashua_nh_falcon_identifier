# nashua_nh_falcon_identifier

Individual identification of the Peregrine Falcons of Nashua, NH — the breeding
pair and dispersing juvenile(s) followed by the local observation group (David,
Jarrod, Mark). Goal: tell the birds apart reliably (photos, plumage/molt marks,
bands if any, behavior/territory), so group sightings unify into one honest
record — and feed local efforts (Cornell **eBird**, **NH Audubon** Peregrine
monitoring) and the Nashua Ink Link story.

## STATUS (updated 2026-08-03)
- Active file: none — checkpointed. Session 1 shipped intake + method + log.
- **`photo_intake/` DONE and green (26 tests).** Standalone tool
  (`python -m photo_intake ingest|list|show|stats`). Reads EXIF, assigns a
  stable id `YYYYMMDD-<8hex>`, sha256-dedupes exact repeats, dhash-flags burst
  frames (≤5 bits) without dropping them, copies originals into
  `photos/YYYY/MM/`. **HEIC/RAW handled** via a cached macOS `sips` derivative
  (verified live on a real .heic); unreadable files are catalogued, not
  dropped. **Privacy split is the load-bearing design:** GPS + absolute source
  paths go to gitignored `private/locations.jsonl`, the committed
  `data/catalog.jsonl` carries only `has_gps` + the coarse `--site` label. A
  test asserts no coordinates ever reach the public file.
- **ID method decided — `docs/id_method.md`.** Verdict: bands and molt gaps
  carry nearly all the signal; plumage pattern-matching is a real but secondary
  tier. **Generic AI image-matching does NOT work here** and we say so in the
  doc — off-the-shelf embeddings/perceptual hashes cluster by background and
  pose, and the Wildbook/HotSpotter approach needs high-contrast planar
  patterns that a peregrine's low-contrast barring on a curved, molting,
  deformable surface does not provide. Machine role = normalise crops + rank
  candidates for a human, never a verdict. Confidence ladder in use:
  confirmed (band code only) / probable / possible / unknown.
- **Individuals schema live — `individuals/`.** Slugs are permanent opaque
  numbers (`nashua-01/02/03`), NOT roles, so a territory turnover can't
  silently inherit a predecessor's record; `roles` is a dated timeline.
  All three seeded as `status: hypothesis` — zero photos in the catalogue yet,
  nothing fabricated.
- **`INTEL.md` seeded from live eBird** (composed `../birds/ebird_api`, not
  rebuilt). Hillsborough County 30d = 13 Peregrine records splitting into
  **two clusters ~20 km apart**: downtown Nashua (Clocktower Pl / Front St /
  Nashua River at Jackson Mills Dam / Mine Falls) and Bedford–Manchester (Rt
  101 Merrimack bridge / Cohas Brook trestle / Moores Crossing). Treat as
  different birds until proven otherwise — hence `--site` on every ingest.
- Location call made: **place names only in committed files, no coordinates.**
  eBird returned precise lat/lon for the downtown records; they were
  deliberately kept out of the repo pending David's ruling per the Git policy
  below.
- Leaning: no compare tool yet — building pattern-matching before real photos
  exist would be guessing at the input. Intake first, method written, tool
  when there are frames to test it on.
- Next: (1) **the actual ask — inventory Jarrod's and Mark's archives and
  ingest them**; (2) ask NH Audubon whether the downtown pair/2026 brood is
  banded and whether they hold the codes (highest-leverage open question — a
  code turns ID from comparison into lookup); (3) once photos exist, build the
  normalised-crop compare tool (head profile / breast / spread wing).

**STATUS discipline:** keep this block current; refresh before every session
ends ("checkpoint"). A new session must resume cold from STATUS alone. Stale
STATUS = bug.

## Layout
```
photo_intake/        the intake tool (core.py + __init__.py + __main__.py)
tests_photo_intake/  26 offline tests; ~/dkn314/bin/python -m pytest
docs/id_method.md    how a Peregrine can and cannot be identified; photo protocol
individuals/         one file per bird + the schema (README.md)
INTEL.md             running log: sites, open questions, sources
data/catalog.jsonl   the public photo catalogue (committed, GPS-free)
private/             GPS + source paths (GITIGNORED — must never reach GitHub)
photos/              originals copied in by intake (GITIGNORED)
```

## Git policy — THIS PROJECT DIFFERS FROM ITS SIBLINGS
**This is a TRUE public-facing repo: a GitHub remote and pushes are ALLOWED —
the plan is to push once there's something worth showing** (David's call on
when). This deliberately overrides the house local-only rule (RULES.md
Hygiene) for this project, like `book_test`. Consequences every session must
respect:
- **Never commit secrets** (no API keys, no `.env`) and **no personal/private
  data** — assume every commit becomes public. eBird keys etc. stay in the
  gitignored `.env`.
- Location sensitivity: peregrine NEST-site precision is a judgment call —
  urban sites are usually public knowledge, but check with David before
  committing exact nest coordinates; the group + NH Audubon norms win.
- Commit per meaningful change as usual. Push only when David says push.

## House rules (local context; readers on GitHub can ignore this section)
- Read `../RULES.md` (package/tool conventions — small, standalone, composable
  tools) and `../DOCTRINE.md` (decision rules) before real work.
- Python: the shared venv `~/dkn314/bin/python` — no per-project venvs.
- Prior art next door in `../birds/` (compose, don't import — RULES spine):
  the eBird client (`ebird_api`), BirdNET/audio tooling, and the `--who`
  observer-column caveat — eBird display names are NOT unique identities; that
  lesson was learned ON a Nashua Peregrine namesake. Any tool built here that
  needs eBird data should snap in as its own standalone `*_api`-style piece.

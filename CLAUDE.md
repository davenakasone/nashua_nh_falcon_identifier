# nashua_nh_falcon_identifier

Individual identification of the Peregrine Falcons of Nashua, NH — the breeding
pair and dispersing juvenile(s) followed by the local observation group (David,
Jarrod, Mark). Goal: tell the birds apart reliably (photos, plumage/molt marks,
bands if any, behavior/territory), so group sightings unify into one honest
record — and feed local efforts (Cornell **eBird**, **NH Audubon** Peregrine
monitoring) and the Nashua Ink Link story.

## STATUS (updated 2026-08-23)
- Active file: none — checkpointed. **WAITING ON NH AUDUBON.**
- **THE BAND WAS PHOTOGRAPHED AT READABLE SCALE, 2026-08-23.** David watched one
  adult on the radio-tower crossbar for two hours (127 frames, Pixel 10 Pro) and
  got the shot this project had been chasing since day one: a **bi-colour band,
  BLACK over GREEN** (eastern US rig), **340–420 px** of band in a native
  6144×8160 frame, with **four glyph positions resolvable**. Every prior attempt
  had ~12 px.
- **CODE CONFIRMED BY THE CURATOR (David, 2026-08-23): `53/BS`.** Written into
  the catalogue at `confirmed`. Independent project read matches. BUT all four
  glyphs come from the systematically confusable set (5↔S, 3↔B↔8), so the live
  candidate space is `53/BS` / `S3/B5` / `53/85` / `S3/BS`. Also: every observer
  in the chain was primed — NH Audubon's July read went from partial glyphs to a
  bird they already knew about, and mine knew theirs. **Nobody has verified
  `53/BS` is even a code deployed in NH.** One reply from Mickayla or Chris
  collapses the whole set; that is the outstanding action.
- **Evidence package SENT (David, 2026-08-23):** `Nashua_PEFA_band_20260823.pdf`
  (6 pp — JPEG-vs-RAW comparison, then 5 frames with callouts, each inset
  labelled with its native size and enlargement factor) plus the two best
  full-resolution JPEGs. Held in Drive `_private/.../band_evidence_20260823/`.
- **Two adults on one date, one banded one not** — banded bird on the crossbar
  at **17:46 local**, bare-tarsi adult on the clocktower weathervane at **19:47
  local**. (Corrected 2026-08-24: these were previously written as 21:46/23:47,
  which are the **UTC** times in the Pixel filenames — `PXL_20260823_214620` is
  UTC, EXIF is local, EDT is UTC−4. Nobody photographs a falcon at 11:47 PM.)
  The two are **two hours apart**, so the clock alone does not separate them —
  but one is banded and the other has bare tarsi, and *that* does. Retires the
  08-16 worry that the banded bird was a February passer-by.
- **`nashua-01` is still nameless**, `sex` disputed, Amos linkage **not counted**
  — per David's standing rule: *no individual ID without a photo of a readable
  band.* The photo now exists; the read is one confirmation short.
- **CATALOGUE: 94 photos, 2025-08-15 → 2026-08-23, 18 sightings.** 6 rows
  `band_visible=yes`, 5 `band_visible=no`. Album originals ingested off the
  local Drive mount; the New Jersey contamination turned out to be **exactly 2
  frames** (Forsythe/Brigantine, 443 km) found by coordinates in seconds.
- **Two hardware findings, both counter-intuitive, both in `docs/id_method.md`:**
  (1) **Phone RAW is WORSE than the phone JPEG here** — the Pixel DNG is 8.8 MP
  binned vs the 50 MP JPEG, 2.4× less linear resolution and visibly softer. Do
  not chase DNGs on a phone. (Dedicated cameras are the opposite — keep asking
  Jarrod for his A7 IV RAWs.) (2) **Shoot the 5× telephoto, not the main
  camera** — ~233 px/degree vs 111, so ~2.1× more pixels on the bird despite
  fewer megapixels. Main camera only in poor light.
- **Biggest non-equipment lever: go at midday, not dusk.** Detection is ~100% at
  Mine Falls (David, 2026-08-24: *"i will see a falcon down there anytime i
  want"*), so peak activity is not needed to *find* the birds — and dusk is what
  has made every frame in this project soft and backlit.
- **Do not plan photography off that ~100%.** It answers *should I go* (always)
  and *must I time it to peak activity* (no). It answers nothing else. The real
  yields, measured on the catalogue: **39%** of frames can be aged, **23%** tie
  to an individual, **15%** resolve a tarsus, **6%** read a band — and 5 of those
  6 are one 3-second burst. Best session ever was 5 usable band frames from 127.
  **Plan for volume and for the moments a bird stands, steps or mantles**, which
  is when tarsi appear.
- **Observer effort is this project's standing confounder** — three strikes now
  (a peer's dispersal finding, this project's triangulation, and the checklist
  time series, whose density tracks David's attention since the band excitement
  rather than the birds). Check it first on any pattern claim.
- Session-1/2 infrastructure below still current: `photo_intake` (29 tests),
  CSV schema, `nest_map.py` with bearing triangulation, `PLAYBOOK.md`.

**STATUS discipline:** keep this block current; refresh before every session
ends ("checkpoint"). A new session must resume cold from STATUS alone. Stale
STATUS = bug.

## Layout
```
photo_intake/        the intake tool (core.py + __init__.py + __main__.py)
tests_photo_intake/  29 offline tests; ~/dkn314/bin/python -m pytest
docs/id_method.md    how a Peregrine can and cannot be identified; photo protocol
individuals/         one file per bird + the schema (README.md)
INTEL.md             running log: sites, open questions, sources
data/photos.csv      one row per photo (committed, GPS-free)
data/sightings.csv   one row per observation event (committed, GPS-free)
data/README.md       the schema + the two rules that don't bend
private/             GPS + source paths + share links (GITIGNORED)
photos/              originals, only if --copy is passed (GITIGNORED)
```

## Git policy — THIS PROJECT DIFFERS FROM ITS SIBLINGS
**This repo IS public and IS pushed** — `github.com/davenakasone/nashua_nh_falcon_identifier`,
verified anonymously readable 2026-08-04. This deliberately overrides the house local-only rule (RULES.md
Hygiene) for this project, like `book_test`. Consequences every session must
respect:
- **Never commit secrets** (no API keys, no `.env`) and **no personal/private
  data** — assume every commit becomes public. eBird keys etc. stay in the
  gitignored `.env`.
- Location sensitivity: peregrine NEST-site precision is a judgment call —
  urban sites are usually public knowledge, but check with David before
  committing exact nest coordinates; the group + NH Audubon norms win.
- Commit per meaningful change. Pushing is now routine — David green-lit it
  2026-08-04. **Every commit is immediately world-readable**, so the redaction
  discipline in `data/README.md` is not advisory.

## House rules (local context; readers on GitHub can ignore this section)
- Read `../RULES.md` (package/tool conventions — small, standalone, composable
  tools) and `../DOCTRINE.md` (decision rules) before real work.
- Python: the shared venv `~/dkn314/bin/python` — no per-project venvs.
- Prior art next door in `../birds/` (compose, don't import — RULES spine):
  the eBird client (`ebird_api`), BirdNET/audio tooling, and the `--who`
  observer-column caveat — eBird display names are NOT unique identities; that
  lesson was learned ON a Nashua Peregrine namesake. Any tool built here that
  needs eBird data should snap in as its own standalone `*_api`-style piece.

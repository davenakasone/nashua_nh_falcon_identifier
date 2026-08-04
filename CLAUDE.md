# nashua_nh_falcon_identifier

Individual identification of the Peregrine Falcons of Nashua, NH — the breeding
pair and dispersing juvenile(s) followed by the local observation group (David,
Jarrod, Mark). Goal: tell the birds apart reliably (photos, plumage/molt marks,
bands if any, behavior/territory), so group sightings unify into one honest
record — and feed local efforts (Cornell **eBird**, **NH Audubon** Peregrine
monitoring) and the Nashua Ink Link story.

## STATUS (updated 2026-08-04)
- Active file: none — checkpointed mid-session-2.
- **`PLAYBOOK.md` IS NOW THE HEADLINE ARTIFACT.** David's call: this repo is the
  template he will point future Claude Code sessions at to start new species
  projects (New England **Snowy Owl**, **Short-eared Owl**, "whatever people are
  into"). PLAYBOOK is species-agnostic: feasibility screen, order of operations
  (**find the expert node FIRST** — the band code came from an email chain, not
  from tooling), governance (open contribution / curated assertion), the
  four-layer architecture, the confidence ladder, **§6 contamination** (AI
  enhance / wrong provenance / absence-as-evidence / claims hardening as they
  travel), privacy, where scale breaks, and what NOT to build. `photo_intake/`
  is now species-agnostic and drops into a new repo unchanged — only
  `band_visible`/`band_code` are marking-scheme specific.
- **Repo is PUSHED and PUBLIC** (`git@github.com:davenakasone/nashua_nh_falcon_identifier`).
  Verified anonymously readable. David keeps the gitignore as-is, so `private/`
  (addresses, phone numbers, a private resident, the reporter's medical details,
  the drone pilot's contacts, coordinates, share links) stays out. He believes
  he is sharing only with the group — **he has been told it is world-readable**;
  going private is Settings → visibility if he changes his mind.
- **THE MISSION IS THE NEST.** David's framing: make sure the birds have a
  suitable nest that doesn't get disturbed, and see what else can be done for
  them. Individual ID serves that, not the other way round.
- **THREE BIRDS CONFIRMED, all seen 2026-07-22 in one afternoon** — juvenile
  hunting Oxbow Pond, female on the radio tower calling for it, male on the
  millyard stack. NH Audubon confirmed the fledgling 2026-07-23.
  **`nashua-01` = Amos, the banded MALE** (earlier session had him as presumed
  female — corrected). If the read is right: hatched/banded **2017 at Brady
  Sullivan Tower, Manchester**, ~9 years old, dispersed ~20 km south.
  **`nashua-02` = the unbanded FEMALE** — she is the bird the photo-ID method
  actually exists for, since she has no paper trail. `nashua-03` = the 2026
  juvenile, dispersal due now through September.
- **BAND: certain, CODE: not read.** A Feb-2026 in-flight frame shows a silver
  federal band on the tarsus — `banded` is settled. But "G/B 53/BS" traces to
  NH Audubon's explicitly tentative zoom ("sort of" a 3 and a 5, a "very
  blurry" S), since adopted by the group as settled shorthand. Held at
  `possible`. Two live chances at a clean read: Mark's unshared 2026-07-30
  frames (bird STANDING on an AC unit, feeding, 12 minutes) and Jarrod's
  nine-year back catalogue.
- **CATALOGUE IS LIVE: 5 photos, 16 sightings.** First real ingest done from
  Jarrod's Sony A7 IV files — tool auto-deduped a `(1)` copy by sha256 and
  confirmed **his camera writes no GPS**, so DSLR contributions carry no
  disclosure risk (phone photos still will).
- **Nest candidates** (`INTEL.md`): millyard smokestack (NH Audubon: if capped
  and inactive, dust+veg could hold a scrape), the circular chimney across the
  river, the **Clock Tower** (strongest — central to all sightings, and pigeons
  are everywhere nearby but *never* on that tower). Checked and negative:
  Clocktower ingress 2026-07-24. **Ruled out:** 99 Factory St (pigeons roosting
  inside). Drone: Class D airspace on the Nashua approach, needs written tower
  permission — but a City-cleared pilot exists and is willing, into ~October.
  August timing means the nest is inactive, so a pass now is low-disturbance;
  keep it NH Audubon's call.
- Session 1 shipped intake + method + log.
- **`photo_intake/` DONE and green (29 tests).** Standalone tool
  (`python -m photo_intake ingest|list|show|stats`). Reads EXIF, assigns a
  stable id `YYYYMMDD-<8hex>`, sha256-dedupes exact repeats, dhash-flags burst
  frames (≤5 bits) without dropping them. **HEIC/RAW handled** via a cached
  macOS `sips` derivative (verified live on a real .heic); unreadable files are
  catalogued, not dropped. **Privacy split is the load-bearing design:** GPS +
  absolute source paths go to gitignored `private/locations.csv`, the committed
  `data/photos.csv` carries only `has_gps` + the coarse `--site` label. A test
  asserts no coordinates ever reach the public file.
- **DATABASE IS CSV, TWO TABLES (David's call 2026-08-03, schema in
  `data/README.md`).** `photos.csv` = one row per photo (32 cols);
  `sightings.csv` = one row per observation event, joined via `photo_ids`.
  Two tables because a sighting can have no photo (all the eBird/email intel)
  or many (a burst is one sighting). CSV because three humans read it and
  GitHub renders it as a table. **`sightings.csv` seeded with the 13 eBird
  records**, and `photos.csv` now carries 5 ingested photos.
- **The CSV is the durable record, NOT the photos.** Every row carries sha256 +
  dhash + dimensions + timestamp, so a lost original loses pixels but not the
  observation, and a copy resurfacing later can be matched back. `--copy` is
  now **off by default**: originals are expected to live in cold storage
  (David's plan: a Drive folder) that this repo does not control.
- **`band_visible` vocabulary is load-bearing:** empty = nobody looked;
  `not-tested` = looked, frame doesn't show the tarsus; `no` = tarsus visible
  and unbanded; `yes` = band seen. Recording a crouched bird's toe-only frame
  as `no` would manufacture evidence for an unbanded bird. Most album frames are
  `not-tested`; at least one does show a band.
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
  All three are now `status: established` with photos attached — see the
  corrections below.
- **`INTEL.md` seeded from live eBird** (composed `../birds/ebird_api`, not
  rebuilt). Hillsborough County 30d = 13 Peregrine records splitting into
  **two clusters ~20 km apart**: downtown Nashua (Clocktower Pl / Front St /
  Nashua River at Jackson Mills Dam / Mine Falls) and Bedford–Manchester (Rt
  101 Merrimack bridge / Cohas Brook trestle / Moores Crossing). Treat as
  different birds until proven otherwise — hence `--site` on every ingest.
- Location call made: **place names only in committed files, no coordinates.**
  eBird returned precise lat/lon for the downtown records; they were
  deliberately kept out of the repo. Ruling made: they stay out; `nest_map.py`
  reads them from gitignored `private/` and renders to gitignored `out/`.
- **GROUP PHOTO ARCHIVE — a shared Google Photos album, "2026 Nashua Falcons",
  now 30 photos.** Link is in gitignored `private/sources.md` (a share link is a
  bearer credential). Every frame reviewed at full res. **Best band frame in the
  project is in there:** a bird on the radio-tower crossbar with the tarsus fully
  clear of the belly, silver federal band unambiguous at a 5000 px rendition —
  code still unreadable, but the limit is now sharpness/distance rather than
  posture. Also two frames of a bird on the ground over prey.
  **CORRECTED — the 2026-08-03 reading of this album was wrong twice:** "no
  juvenile in 25 photos" was treated as evidence against `nashua-03` (the
  juvenile was being photographed that same week by another observer at Oxbow
  Pond), and an apparent two-birds plumage split turned out to be an artefact of
  AI enhancement. Both corrections are in `INTEL.md` and `individuals/`.
- **THE ALBUM IS NOT A CLEAN DATASET — nothing from it is ingested.** Three
  contamination vectors: some frames are AI-enhanced (David has since banned
  enhancement going forward, but not retroactively flagged which), a **New
  Jersey trip is probably mixed in**, and geotags are unverifiable through
  Google's web renditions (re-encoded, EXIF stripped). **Unblock:** drop the
  originals into the locally-mounted Drive folder
  (`~/Library/CloudStorage/GoogleDrive-.../My Drive/birds/nashua_nh_falcon_tracking/`)
  and ingest off the mount — no download step needed.
- Leaning: still no compare tool. Photos now exist, but plumage comparison is
  blocked upstream by enhancement contamination, and the two adults are
  currently separable only by the tarsus.
- Next: (1) **album originals into the Drive folder, then ingest with `--site`**
  — that also sorts the NJ frames out by coordinates; (2) the six open todos,
  all ask-a-human: Mark's 2026-07-30 originals (standing bird, best band
  chance), Jarrod's nine-year back catalogue, flagging that the code was never
  read, the nest-box question to NH Audubon, the female's trait description,
  dusk bearings for the roost; (3) compare tool only once there are
  out-of-camera frames of both adults.

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

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
  `data/README.md`).** `photos.csv` = one row per photo (31 cols);
  `sightings.csv` = one row per observation event, joined via `photo_ids`.
  Two tables because a sighting can have no photo (all the eBird/email intel)
  or many (a burst is one sighting). CSV because three humans read it and
  GitHub renders it as a table. **`sightings.csv` seeded with the 13 eBird
  records.** `photos.csv` is header-only — nothing ingested yet.
- **The CSV is the durable record, NOT the photos.** Every row carries sha256 +
  dhash + dimensions + timestamp, so a lost original loses pixels but not the
  observation, and a copy resurfacing later can be matched back. `--copy` is
  now **off by default**: originals are expected to live in cold storage
  (David's plan: a Drive folder) that this repo does not control.
- **`band_visible` vocabulary is load-bearing:** empty = nobody looked;
  `not-tested` = looked, frame doesn't show the tarsus; `no` = tarsus visible
  and unbanded; `yes` = band seen. Recording a crouched bird's toe-only frame
  as `no` would manufacture evidence for an unbanded bird. All 25 album photos
  would be `not-tested`.
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
- **GROUP PHOTO ARCHIVE FOUND + REVIEWED (2026-08-03): a shared Google Photos
  album, "2026 Nashua Falcons", 25 photos, 29 Jun – 24 Jul 2026.** David
  supplied the link mid-session; it is recorded in `private/sources.md`
  (gitignored — a share link is a live credential, it does NOT go in a public
  repo). Every frame reviewed at full res. Findings: **all adults, no juvenile
  in 25 photos** (evidence against `nashua-03`, logged there); three recurring
  perches, the best being a white metal bracket on a brick roofline with sharp
  frontal + profile views; **the band question is NOT answered** because the
  sharp frames show a crouched bird with the tarsus hidden behind belly
  feathers (toes only — wrong part of the leg) and the frames with legs exposed
  are too soft to resolve a band past ~2x. Logged as "no band seen, no frame
  tested the band zone" — explicitly NOT as an unbanded bird.
- **NOT INGESTED YET — waiting on David.** Pulling the 25 originals out of
  Google Photos is a file download, so it needs his explicit go-ahead. Once
  given: download to a scratch dir, `python -m photo_intake ingest <dir>
  --site nashua-downtown`, then write the baseline trait description for the
  white-bracket adult.
- Leaning: no compare tool yet — building pattern-matching before real photos
  exist would be guessing at the input. Intake first, method written, tool
  when there are frames to test it on. The album confirms the call: with one
  well-photographed adult and no second bird to compare it against, there is
  nothing for a compare tool to do yet.
- Next: (1) **David's go-ahead to download the album, then ingest it**;
  (2) ask NH Audubon whether the downtown pair/2026 brood is banded and whether
  they hold the codes (highest-leverage open question — a code turns ID from
  comparison into lookup); (3) get the group the one missing shot: a **standing**
  bird's lower leg, sharp, sun behind the photographer; (4) once there are two
  birds to tell apart, build the normalised-crop compare tool.

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

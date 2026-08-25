# nashua_nh_falcon_identifier

Individual identification of the Peregrine Falcons of Nashua, NH — the breeding
pair and dispersing juvenile(s) followed by the local observation group (David,
Jarrod, Mark). Goal: tell the birds apart reliably (photos, plumage/molt marks,
bands if any, behavior/territory), so group sightings unify into one honest
record — and feed local efforts (Cornell **eBird**, **NH Audubon** Peregrine
monitoring) and the Nashua Ink Link story.

## STATUS (updated 2026-08-24)
- Active file: none — checkpointed.
- **⭐ THE PROJECT'S CORE QUESTION IS ANSWERED. `53/BS` = "AMOS", HATCH YEAR 2017
  MALE, Brady Sullivan Tower, Manchester, banded May 2017.** Confirmed
  2026-08-24 by **Christian Martin, NH Audubon, from the banding record** —
  the independence test this file said was the only thing that would settle it.
  **Nora Hanke** independently read the raw frames the same morning and got
  `53` and `S` clean while hedging the middle green glyph — the exact weak spot
  this file predicted in advance. The sighting is going to the federal **BBL**.
  Mark Timmerman, in this group, was present at the 2017 banding.
- **THE SEX IS MALE AND THIS PROJECT WAS WRONG.** David's "that female they
  banded", and the 08-10 "Mom wouldn't share" reading, were both wrong; the
  unanimous 2026-07-23 male call was right and this file downgraded it. By
  elimination the **unbanded clocktower bird is the female**. Five experienced
  observers sexed this bird by eye over six weeks and most got it wrong —
  the best argument the project will ever have for its own curator rule.
- **⚠ A FOURTH BIRD. Nora saw a DIFFERENT banded adult here in March 2026 —
  "the black band had a definite 9 on it".** `53/BS` has no 9. Consequence: the
  **February 2026** frame (`20260804-f3001faa`, band visible, code unreadable)
  has been **UNASSIGNED from nashua-01** — it could be either bird, and slugs
  merge forward and never split. Next: ask Nora what else she has from March;
  ask Chris whether a second banded adult is known here.
- **The juvenile is gone.** Last confirmed **2026-08-15** (photographed), first
  confirmed absent **08-23** (both birds aged adult). David last saw it ~08-17.
  Recovered by scoring 22 previously-unassigned frames — the catalogue had said
  08-10. It is **unbanded**, so it is permanently untraceable.
- **eBird counts are a floor, never a census, and carry no age.** Proof in-file:
  08-09 logged `#1`, photographs show an adult *and* the juvenile.
- **The adults are RESIDENT** — Mine Falls peregrines in every month sampled
  including Dec/Jan/Mar. No seasonal deadline on anything.
- **Detection ~100% is for *finding a falcon* and nothing else.** Real catalogue
  yields: **39%** aged, **23%** individual, **15%** tarsus, **6%** band. Best
  session ever: 5 usable band frames of 127. Plan for volume, and for the
  moments a bird stands/steps/mantles — that is when tarsi show.
- **Observer effort is the standing confounder** — three instances now. Check it
  first on any pattern claim.
- **Unanswered in the chain:** Kevin T asked on 08-10 whether to fly his drone
  (Part 107, prior authorization) to find the nest, and deferred to the experts.
  **14 days, no reply.** Finding the nest is still the highest-value open item.
- Hardware, unchanged: phone JPEG > phone DNG; 5× tele writes **full 50 MP**
  (~458 px/°, double the earlier estimate) — but it is f/2.8 vs the main's
  f/1.68, so **tele in good light, main camera in poor**.
- **CATALOGUE: 94 photos, 21 sightings**, 2025-08-15 → 2026-08-23.
- Session-1/2 infrastructure current: `photo_intake` (29 tests), CSV schema,
  `nest_map.py`, `PLAYBOOK.md`.

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

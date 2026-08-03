# INTEL — Nashua Peregrine log

Running record of what we know and how we came to know it. **Newest entry
first.** Every entry says where it came from; a claim with no source is a
rumour and gets marked as one.

Sightings tied to specific birds live in [`individuals/`](individuals/).
Photos live in the catalogue (`data/catalog.jsonl`, built by `photo_intake`).
This file is for everything else: site patterns, open questions, who to ask,
what the public record already says.

**Location policy in this file:** place names only, no coordinates. Downtown
peregrine sites are effectively public knowledge, but nest-ledge precision is a
judgment call and this repo is public — see `CLAUDE.md`. Precise coordinates
stay in the gitignored `private/`.

---

## 2026-08-03 — eBird baseline: there are two separate falcon areas, not one

Pulled the last 30 days of Peregrine Falcon records for **Hillsborough County,
NH (US-NH-011)** using the eBird client in the sibling `birds/` project
(`python -m ebird_api species US-NH-011 "Peregrine Falcon" --back 30`).
13 records, and they split cleanly into two geographic clusters about 20 km
apart along the Merrimack:

**Downtown Nashua cluster** — Clocktower Place, Front Street, the Nashua River
between Pine Street and Jackson Mills Dam, and Mine Falls Park. Records run
2026-07-15 through 2026-07-30. Two of them are **two-bird counts** (Nashua
River, 23 Jul; Mine Falls Park, 15 Jul).

**Bedford / Manchester cluster** — the Route 101 bridge over the Merrimack
(recorded under several location names), Station Road in Bedford, Cohas Brook
train trestle, Moores Crossing Railroad Bridge. Records run 2026-07-07 through
2026-08-02, including a two-bird count on 17 Jul.

**Why this matters to the ID work:** ~20 km is well inside a peregrine's
foraging range but far outside a nesting territory. These are almost certainly
**different birds holding different sites** — a downtown-Nashua mill-district
group and a Merrimack-bridge group. Any photo the group contributes from Bedford
or Manchester must not be filed against the Nashua individuals without
independent evidence. The intake tool's `--site` label exists for exactly this;
use it on every ingest.

**Caveats, stated plainly:**
- eBird counts are *birds seen*, not *birds identified*. A "2" can be a pair, or
  a parent and a fledged juvenile, or one bird counted twice from two vantage
  points. It supports the pair hypothesis; it does not establish it.
- 30 days is a thin baseline covering the post-fledging period only. It says
  nothing about who nested where.
- No age or sex information comes through this feed at all.

---

## Open questions — the ones worth spending a session on

1. **Is the current downtown pair banded, and does NH Audubon hold the codes?**
   This is the highest-leverage question in the whole project. A band code turns
   identity from a photo-comparison problem into a lookup. Ask the NH Audubon
   peregrine monitoring project; they band nestlings and keep site histories.
2. **Was a 2026 brood produced downtown, and how many young fledged?** Decides
   whether `nashua-03` is one juvenile or the first of several.
3. **What does the group already have?** Nobody has inventoried Jarrod's and
   Mark's photo archives yet. Existing photos may already contain a legible leg
   band, which would resolve question 1 without waiting on anyone.
4. **Do the two clusters ever exchange birds?** Only answerable with banded
   birds or a very lucky molt-gap match.

## Standing asks of the group

- **Send originals, not screenshots** — see the photo protocol in
  [`docs/id_method.md`](docs/id_method.md). Stripped EXIF costs us the timestamp
  the molt-window logic runs on.
- **Shoot the legs whenever a bird is perched.** One legible band ends the
  ambiguity for that bird permanently.
- **Say where.** "Nashua" and "Bedford" are different birds until proven
  otherwise.

## Sources and contacts

- **eBird** (Cornell Lab) — public observation record. Queried through the
  `ebird_api` client in `../birds/`; key lives in that project's gitignored
  `.env`. Peregrine records for Hillsborough County are not location-suppressed.
- **NH Audubon peregrine monitoring** — banding records, nest-site histories,
  productivity data. Not yet contacted.
- **Nashua Ink Link** — local coverage; the story this project eventually feeds.

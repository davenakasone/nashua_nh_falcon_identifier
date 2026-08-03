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

## 2026-08-04 — BANDED AND NAMED: "Amos", band G/B 53/BS, downtown Nashua

Mark's email of 2026-07-31 reports a Peregrine at **63A Front St, Nashua, Thu
2026-07-30 at 19:30**, and titles it **"Amos G/B 53/BS."** That is a named,
banded individual carrying a field-readable bi-color code.

**This answers the project's #1 open question.** The downtown Nashua birds are
banded, at least one has a known code, and somebody is already tracking it by
name. Identification for that bird moves from photo comparison to lookup.

**It also short-circuits the second question.** The thread already includes NH
Audubon staff — their raptor programme people are on the recipient list. The
"contact NH Audubon about banding" task is not a cold approach; the chain is
live and David is already on it. Asking what `G/B 53/BS` resolves to — sex,
hatch year, natal site — is now a reply, not an introduction.

**What the email does NOT establish, and this matters.** The subject line
asserts the identity; **the body never mentions reading a band.** It describes
watching a peregrine carry prey in, perch on a window air-conditioner on a mill
building, and feed for about twelve minutes before flying off past the
smokestack and low over the Franklin St. lofts. Many photos were taken. Whether
the band was read *on this occasion*, or the bird was attributed to Amos from
prior familiarity, is not stated.

So this sighting is logged **probable**, not confirmed. Per
[`docs/id_method.md`](docs/id_method.md) only a legible band code in the frame
earns `confirmed`, and what we have is a claim rather than a read. One question
to Mark settles it.

**The photos are the prize and we do not have them.** They did not survive the
print-to-PDF — only the Gmail logo is embedded in the file. A bird standing on
an air conditioner tearing prey for twelve minutes is **standing**, side-on,
photographed from an upper floor at close range. That is exactly the posture the
25-photo album never caught, and the best chance yet at a tarsus in frame. Ask
Mark for the originals.

**Same event as an existing row.** The eBird record already in
`data/sightings.csv` as `20260730-01` (63A Front St, 2026-07-30 19:30, one bird)
is this sighting. Enriched in place, not duplicated — worth noting as the first
case of two independent sources landing on one event.

**Redaction applied.** Committed: date, time, coarse site, behaviour, the public
building names already present in the eBird record, the band code, and the
attribution. Withheld to gitignored `private/`: all email addresses, the Gmail
thread URL, the floor-and-window precision, and the name and residence of a
private individual mentioned in the body who is not part of this project.

---

## 2026-08-03 — the group's Google Photos album, reviewed: 25 photos, all adults, bands still unanswered

David pointed at the group's shared album, **"2026 Nashua Falcons"**, date range
**29 Jun – 24 Jul 2026, 25 photos**. Reviewed every frame at full resolution.
Nothing has been ingested into the catalogue yet — this entry is the survey.

**Age class: every identifiable bird in the album is an adult.** Slate-grey
upperparts, **horizontal** barring on the underparts, dark hood, yellow cere and
feet. No frame shows an unambiguous brown, vertically-streaked juvenile. That is
a real finding, and a surprising one for a June–July window in a territory that
is supposed to have produced young: **either the group did not photograph this
year's juvenile, or there wasn't one.** Worth asking the group directly before
assuming the former.

**Three distinct settings recur**, and the repetition is the useful part —
a repeated perch gives us the standardised viewing angle that trait comparison
needs:
- **White metal bracket / flashing at a brick roofline** — the best material in
  the album. Sharp, well lit, frontal and profile views of breast barring and
  malar stripe. Almost certainly one bird, one session.
- **Brick arch / parapet with a vertical pole** — bird standing upright, legs
  exposed, but small in frame and soft.
- **Grey metal box, heavily backlit** — near-silhouettes. Nearly useless for
  plumage; still fine for behaviour and perch fidelity.

**Bands: NOT ANSWERED, and the reason is instructive.** The two conditions never
co-occurred in a single frame:
- In the *sharp* frames the bird is crouched on the sloping flashing with the
  **tarsus hidden behind belly feathers**. Only toes and talons are visible —
  bright yellow, black claws — and the toes are the wrong part of the leg. A
  band sits on the tarsus.
- In the frames where the **tarsus is exposed**, the bird is too small and too
  soft in frame; pushing past ~2x magnification produces interpolation, not
  detail.

So the honest statement is **"no band was seen, and no frame actually tested the
band zone at usable resolution."** That is *not* evidence of an unbanded bird,
and it must not be written down as one. It does convert the band question from
"unknown" into a specific, cheap, achievable photo request — see below.

**Quality notes for the group:** at least one frame is unusable from heavy
high-ISO noise, and several are backlit into silhouette. Both are fixable by
shooting the same perch earlier in the day with the sun behind the photographer.

**What this album is actually good for right now:** establishing a baseline
trait description — malar stripe geometry and breast-barring pattern — for the
one well-photographed adult at the white-bracket perch. That is a legitimate
`nashua-01`-or-`02` anchor, and it is the natural first entry once the photos
are ingested.

**Not yet done:** the photos live in Google Photos and have not been downloaded
or catalogued. Per-photo capture timestamps were not read either — the album
only exposes its overall range — and those timestamps are what the molt-window
logic needs, so they should come from the originals rather than the web view.

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

- **The one shot that matters most: a standing bird's LOWER LEG, sharp.** The
  album's 25 photos could not answer the band question because the sharp frames
  show a crouched bird with the tarsus buried in belly feathers, and the frames
  with legs showing are too soft. **Wait for the bird to stand up**, fill more of
  the frame, and shoot the leg between the feathered thigh and the toes. One
  such frame plausibly ends the identification problem for that bird.
- **Send originals, not screenshots** — see the photo protocol in
  [`docs/id_method.md`](docs/id_method.md). Stripped EXIF costs us the timestamp
  the molt-window logic runs on.
- **Shoot the same perch with the sun behind you.** Several album frames are
  backlit into silhouette; the white-bracket perch is clearly a reliable spot,
  so the lighting is a schedulable problem, not a luck problem.
- **Is there a 2026 juvenile at all?** No brown, streaked bird appears in 25
  photos spanning late June to late July. Ask before assuming it was simply
  missed.
- **Say where.** "Nashua" and "Bedford" are different birds until proven
  otherwise.

## Sources and contacts

- **eBird** (Cornell Lab) — public observation record. Queried through the
  `ebird_api` client in `../birds/`; key lives in that project's gitignored
  `.env`. Peregrine records for Hillsborough County are not location-suppressed.
- **NH Audubon peregrine monitoring** — banding records, nest-site histories,
  productivity data. Not yet contacted.
- **Nashua Ink Link** — local coverage; the story this project eventually feeds.

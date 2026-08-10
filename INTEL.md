# INTEL — Nashua Peregrine log

Running record of what we know and how we came to know it. **Newest entry
first.** Every entry says where it came from; a claim with no source is a
rumour and gets marked as one.

Sightings tied to specific birds live in [`individuals/`](individuals/).
Photos live in the catalogue (`data/photos.csv`, built by `photo_intake`).
This file is for everything else: site patterns, open questions, who to ask,
what the public record already says.

**Location policy in this file:** place names only, no coordinates. Downtown
peregrine sites are effectively public knowledge, but nest-ledge precision is a
judgment call and this repo is public — see `CLAUDE.md`. Precise coordinates
stay in the gitignored `private/`.

---

## 2026-08-10 — weaning behaviour, the best leg photo yet, and the sexes have come unstuck

Jarrod's 08-10 thread. Two photographers on the same event from opposite sides
of one building, and a photograph that settles one question while a second
question comes apart.

### What happened
About 09:19, an adult killed a bird on the roof between 1 Chestnut St and 100
Factory St — feathers visible from the street below. **The juvenile tried to
land and was chased off**, then screamed and circled the block. A second adult
watched the whole thing from the Clocktower weathervane. A second observer was
on the far side of the same building, photographed the weathervane bird, then
relocated to the Mine Falls cell tower and shot an adult eating the catch.

**That refusal-to-share is the headline.** It is textbook weaning: the adults
stop provisioning and the juvenile's begging stops working. It puts
`nashua-03` squarely in the dispersal run-up, and it corroborates the widened
August–October window rather than the "next few weeks" this log first claimed.
A useful comparative from the same thread: at Brady Sullivan Tower in
Manchester — Amos's natal site — the juvenile has stopped being fed and has not
been seen for days.

### The best tarsus photograph in the project
The weathervane bird is shot in full sun with **both legs fully exposed and
unobstructed**, gripping the wrought iron. They are **bright yellow and
completely bare — no band on either leg.** No posture problem, no softness, no
ambiguity. Catalogued as `20260810-08f56710` with `band_visible=no`, and it is
the first frame in this project to earn that value on both legs at once.

### The sex assignments have come unstuck — three accounts, three mappings
Within this single thread:

| account | banded bird | weathervane bird |
|---|---|---|
| observer A, 09:19 | "the banded **female**" (also "Mom") | "the unbanded **male**" |
| observer A, 10:01 self-correction | — | "the unbanded **female**" |
| observer B, 10:38 | — | "the **male** on the weather vane" |
| **this repo, from the 07-22/23 thread** | **male** (Amos) | **female** |

Observer A's first message **inverts the repo's mapping outright**, then his own
correction flips the weathervane bird back to female — leaving the banded
prey-catcher still labelled "female"/"Mom", which cannot both be true unless
there are two females. Observer B then contradicts the correction.

**What is actually settled:** the weathervane bird is unbanded. That is a
photograph, not an opinion, and every account agrees on it anyway.

**What is not settled:** which bird is which sex. The repo's `nashua-01 = banded
male / nashua-02 = unbanded female` rests entirely on the 07-22/07-23 thread,
and the same people have now said the opposite. **Individuals in the catalogue
for this sighting were assigned on band evidence alone, never on the observers'
sex calls.**

This matters more than a labelling quibble: **sex is the only thing separating
the two adults apart from the band.** If it is unstable, the pair is effectively
distinguishable by one feature. It is also a clean demonstration of why the
confidence ladder is worth the friction — a `probable` that flips between
observers was never a `confirmed`.

**One question to NH Audubon settles it**, and they are already on the thread:
which sex is the banded downtown bird?

### The drone question was raised properly
The pilot with City clearance raised it himself rather than flying: peregrines
are reactive to drones, he does not want to provoke a strike or stress the
birds, and he asked whether the nest is already known and monitored so a flight
would just be redundant disturbance. That is the right instinct and the right
order — **ask the biologists first, fly second, if at all.**

---

## 2026-08-04 (later still) — the album is not a Nashua dataset, and geotags are unchecked

David: **there is probably a New Jersey trip mixed into the album.** That is a
third contamination vector on top of AI enhancement and unread band codes, and
it retroactively undermines at least one finding logged an hour earlier.

**Suspect frames.** Two show a falcon **on the ground in dry marsh grass**,
standing over prey — a habitat that does not exist in the downtown Nashua
millyard, and one that matches coastal New Jersey peregrine sites closely.
Those were logged above as "the best band-reading geometry available." That may
be true of some *other* bird in another state. Several hazy, flat-landscape
lattice-tower frames are also unlike the crisp millyard shots and cannot be
placed by eye.

**Geotags: not checked, and not checkable from here.** The album is only visible
through Google's web renditions, which are re-encoded and carry no EXIF at all,
and a link viewer's info panel does not expose location. Every geotag statement
in this log so far applies only to the **local** files, where it was verified
properly: Jarrod's Sony ILCE-7M4 writes no GPS, and the emailed screenshots
carry no EXIF whatsoever.

**Why the geotags matter more than they first appear.** A photo's GPS locates
the *photographer*, not the bird — which for this project is an asset rather
than a limitation:

1. **It partitions the album instantly.** Habitat and tower shots look alike;
   coordinates do not. One pass over the originals sorts Nashua from New Jersey
   with no judgement calls.
2. **It may already contain the nest triangulation.** Phones commonly write
   `GPSImgDirection`, the compass heading the camera was pointing. Standing
   position plus heading is a **ray pointing at the perch**, and rays from two
   positions intersect on it. If the phone frames are geotagged, the dusk-bearing
   fieldwork proposed as a to-do may already exist retroactively in the camera
   roll.
3. **It is a disclosure question for the album, separate from the repo.** If
   those frames are geotagged and the album link circulates, the coordinates
   circulate with them.

**What unblocks all three:** the originals, not the web view. Drive is mounted
locally on this machine, so dropping the album originals into the Drive folder
is enough — intake reads them off the mount with EXIF intact, writes coordinates
to gitignored `private/locations.csv`, and `nest_map.py` now plots every
geotagged frame, flagging anything more than 50 km from the downtown centroid as
**NOT a Nashua photo**.

**Discipline this reinforces:** `--site` on every ingest was designed for exactly
this, and nothing in the album has been ingested yet. Until it is, the album is
a shoebox, not a dataset.

---

## 2026-08-04 (later) — album expanded to 30; best band frame yet; perch fidelity is dead

David added five photos and **set a project rule: no AI enhancement on Nashua
falcon photos going forward.** That rule is the single most valuable thing to
happen to the ID method today — see the contamination section in
[`docs/id_method.md`](docs/id_method.md). Frames shot from here on are
admissible for trait scoring; the earlier ones are not, unless he can say which
were left alone.

### The best band frame anyone has produced
A bird on the **radio-tower crossbar**, hunched, with the tarsus fully clear of
the belly feathers. At a 5000 px rendition the band is many times larger in
frame than in the February flight shot: an unambiguous **silver federal band**,
cylindrical, with a dark lower edge. Surface texture is visible but **no
characters resolve** — the frame is soft, and this is still the federal band
rather than the bi-color one that carries a readable code.

Two useful things follow. First, **that perch produces the posture we need** —
the bird sits high on the bar with legs exposed rather than crouched on a
sloping ledge. Every other perch in the archive hides the tarsus. Second, the
softness rather than the framing is now the limit, which is a lens-and-distance
problem, not a luck problem.

### New: a falcon on the ground
Two frames show a peregrine **down in dry grass, standing over prey** — a
setting absent from everything before. Legs are out of the feathers and the
visible tarsus is **bare**. Worth chasing the rest of that sequence: a bird on
the ground is at eye level, stationary and preoccupied, which is the best
band-reading geometry available short of a nest box.

### Perch fidelity does not separate the adults — scratch it
The banded bird above is on the **same crossbar** that Jarrod captioned as the
**female** on 2026-07-22, and the group holds that the female is unbanded. So
either both adults use that perch, or one of those two claims is wrong. Either
way, **"which structure it is sitting on" cannot be used to tell the pair
apart.**

That matters because perch fidelity was the last discriminator left standing
after AI enhancement knocked out plumage comparison. It is now also gone. What
remains for separating the two adults is the tarsus and nothing else.

---

## 2026-08-04 — the email chain: three birds confirmed, Amos traced to Manchester, and the nest is the real mission

Four threads reviewed (22–31 Jul), plus 15 images. This entry supersedes several
earlier conclusions; the corrections are marked rather than quietly folded in.

### Three birds, all three seen at once
**2026-07-22, one afternoon:** the juvenile hunting over Mine Falls Oxbow Pond
while both adults watched from separate high perches — the female on the radio
tower (calling for the juvenile once it went out of sight), the male on the
millyard stack. NH Audubon confirmed the fledgling the next day. Photographed;
four frames now in the catalogue.

**Correction to 2026-08-03.** The previous entry treated "no juvenile in 25
album photos" as evidence against a 2026 fledgling. Wrong — the juvenile was
being photographed inside that exact window by a different observer at Oxbow
Pond rather than downtown. **Absence from one person's album is not absence in
the field.** Logged in [`individuals/nashua-03.md`](individuals/nashua-03.md).

### Amos is the MALE, and he came from Manchester
**Correction to the 2026-08-04 entry below.** That entry anchored `nashua-01`
to Amos while `nashua-01` was described as the presumed female. The group is
consistent that **the banded bird is the male and the female is unbanded** —
one observer notes a photo of her with a leg clearly bare.

If the code read is right, Amos was **hatched and banded in 2017 at Brady
Sullivan Tower, Manchester**, and is the same male recorded in Nashua before —
so he is a ~9-year-old bird that dispersed roughly 20 km south from the
well-known Manchester population. That is exactly the kind of link banding
exists to make, and it means **the Bedford/Manchester cluster's value here is as
Amos's origin, not as a research target** — those birds are already well known
locally.

**But the code is not read.** NH Audubon's own account is explicitly tentative:
zooming into a photo, "sort of" making out a 3 and a 5 on the black band and a
"very blurry" S on the green. (Note the colour order: eastern bi-colour bands
are **black over green**, and that description puts the digits on black — so the
code is more likely **B/G 53/BS** than the "G/B" the thread uses. Confirm with
the observer; do not quietly rewrite a quoted subject line.)
The group has since adopted "Amos G/B 53/BS" as
settled shorthand. It is a good bet, not a read — `possible`, not `confirmed`.

A February 2026 in-flight frame (now `20260804-f3001faa`) **does** show a silver
federal band on the tarsus, so *banded* is certain even though *which bird* is
not. Magnified, the code is unresolvable: the band sits near edge-on at
distance.

### The nest has not been found, and finding it is the point
Candidate structures, with what is actually known about each:

- **Millyard smokestack** — NH Audubon's raptor biologist: if the tall chimneys
  are inactive and capped, dust and vegetation accumulate on top and a scrape
  could sit there. Cannot be confirmed from the ground.
- **The circular chimney across the river**, near the apartments — in regular
  use as a perch.
- **The Clock Tower itself** — the strongest ground-level guess. It is central
  to every confirmed sighting, the birds use its weathervane and rails, and
  there may be an entry into the clock mechanism space, which humans visit only
  for repairs. Checked on 2026-07-24 for a missing brick or roof gap: **no
  ingress found.** Not ruled out — it is a long building with multiple turrets.
- **Mill Building No 1 / Clocktower Apartments, north-facing alley side** —
  little human traffic, many ledges; north aspect is a mark against it.
- **99 Factory Street (abandoned)** — **ruled out.** Too many pigeons roosting
  inside; falcons would not tolerate that at a nest.

**The sharpest field observation in the whole chain:** pigeons are everywhere on
the surrounding buildings but *never* on the clock tower. Prey species avoiding
one structure in a pigeon-rich block is real negative evidence, and it points at
the tower.

### The drone question is solved, legally
The area is **Class D airspace under Nashua tower control, on the direct landing
approach** — a Part 107 certificate is not enough, it needs written permission
from the tower for a specific one-hour block, with up to six weeks' lead. Flying
without clearance has cost at least one person their drone to Nashua PD on the
spot.

The route through that: a local drone photographer already holds FAA permission
through the City for the entire restricted area, believed good into October, and
is willing. The plan on the chain is to use the **Nashua City GIS 2024 aerial
imagery** (better resolution than Google) to shortlist rooftops, then send him to
the shortlist looking for suitable substrate, wind shelter, prey remains and
whitewash.

**Timing note in this project's favour:** it is August. The young have fledged
and the nest is no longer active, so a drone pass now carries far less
disturbance risk than the same flight in April would. That ordering is doing a
lot of work and should stay explicit — and it should remain NH Audubon's call,
since they are on the thread.

### Seasonal behaviour, from NH Audubon
Urban pairs tend to stay at the nest area year-round because the food supply
(pigeons) is constant; the Brady Sullivan pair is at its nest box all year.
Pairs return to the same structure next season but may pick a different ledge.
One observer's retrospective fits: red-tailed hawks occupied the radio tower in
spring, which now reads as the period the female was sitting, and the falcons
were much less visible March–April.

### A nine-year archive exists
One of the group photographs the area nearly every weekday, year round, and has
kept an extensive catalogue over nine years — including falcon frames from
January and February 2026. **That back catalogue is the cheapest multi-year
continuity this project will ever get** and is worth asking for explicitly.

### Redaction
Committed: dates, times, coarse sites, public building names, behaviour, the
band code and provenance, and attributions. Withheld to gitignored `private/`:
all addresses and phone numbers, the third-party drone pilot's contact details,
the reporter's scheduling and medical details, an observer's workplace and home
floor, and the account-scoped Gmail links.

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

**Redaction applied.** Committed: date, time, coarse site, behaviour, the band
code, the attribution, and the building names — which are **already public in
the eBird record at finer precision than this file uses**. eBird's own location
string for this sighting carries the street number *and* decimal coordinates;
the repo deliberately drops the coordinates and keeps the name.

Withheld to gitignored `private/`: all email addresses, the Gmail thread URL,
and **the name, floor, apartment side and daily habits of a private resident**
mentioned in the body, who is not part of this project and did not consent to
appear in a public repo. That resident's window-row detail is withheld too.

Note the one thing this entry *does* state: the photographer's own vantage, "an
upper floor at close range." That is a project participant describing his own
position, deliberately kept vague, and is not the withheld detail above — an
earlier version of this note was ambiguous about which floor reference it meant.

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

**Why this matters to the ID work:** ~20 km is at the *outer edge* of a breeding
peregrine's foraging range — they typically hunt within ~5 km of the nest — and
far beyond normal nest spacing, which can be as little as 0.5–2 km between urban
pairs. These are almost certainly
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

1. ~~**Is the current downtown pair banded, and does NH Audubon hold the codes?**~~
   **ANSWERED 2026-07-23, partly.** The male is banded, the female is not, and NH
   Audubon is already on the group's email thread. What remains is narrower and
   still the highest-leverage question in the project: **nobody has actually read
   the code.** "G/B 53/BS" is a tentative zoom, not a read. Get a legible frame.
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
- ~~**Is there a 2026 juvenile at all?**~~ **ANSWERED — yes.** Seen and
  photographed 2026-07-22 hunting Oxbow Pond; NH Audubon confirmed the fledgling
  2026-07-23. The earlier "absent from 25 album photos" reasoning was wrong and
  is corrected in [`individuals/nashua-03.md`](individuals/nashua-03.md). What
  is still open is **how many** young fledged, and whether any were banded in
  the nest.
- **Say where.** "Nashua" and "Bedford" are different birds until proven
  otherwise.

## Sources and contacts

- **eBird** (Cornell Lab) — public observation record. Queried through the
  `ebird_api` client in `../birds/`; key lives in that project's gitignored
  `.env`. Peregrine records for Hillsborough County are not location-suppressed.
- **NH Audubon peregrine monitoring** — banding records, nest-site histories,
  productivity data. **Already on the group's email thread**; confirmed the 2026
  fledgling and supplied the tentative `53/BS` read. Not a cold contact.
- **Nashua Ink Link** — local coverage; the story this project eventually feeds.
- **Primary sources are preserved locally, not committed.** The four Gmail
  threads behind every `email:<name>` attribution in this log are held as PDFs
  in gitignored `private/email/pdf/`, with their screenshots and GIS captures
  in `private/email/images/`. If a claim here needs re-checking against what
  was actually written, that is where to look.

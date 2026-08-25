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

## 2026-08-24 ⭐ NIGHT ROOST — and the nest search failed for a positioning reason

David: *"seen the birds go there at night. we always missed them because we were
in the wrong place (along the river)."*

**(Building identified; held in `private/nest/` pending the disclosure call. It is
a derelict downtown structure OFF the river, not on the candidate list.)**

### A night roost is a much stronger signal than a daytime perch
A bird sitting on a stack at noon is using a lookout. A pair returning to the
same structure **every night** is using a roost — and in peregrines the **night
roost is very often the nest ledge itself or one adjacent to it**, particularly
outside the breeding season. Combined with what the eBird record already
established — **this pair is resident year-round, present in every month
sampled** — a habitual night roost on one downtown building is close to the
textbook profile of an occupied nest site.

**Every structure on the candidate list was scored on daytime perching.** None of
them was ever assessed as a roost. That is a category error this file has been
making since the search began.

### The search failed because of where the observers stood
*"we always missed them because we were in the wrong place (along the river)."*

The candidates worked so far — Clocktower, 99 Factory St, the millyard stack —
are all structures **visible from the river**, which is where the group watches.
The birds were going somewhere else, and **nobody was standing anywhere they
could see it happen.**

**This is the FOURTH confirmed instance of observer effort or position
manufacturing a false picture in this project:**
1. A peer session's zero-dispersal finding — an eBird hotspot-coordinate artifact.
2. This project's own bearing triangulation.
3. The checklist time series, whose density tracks David's attention since the
   band excitement rather than the birds.
4. **The nest search itself — negative results from the wrong vantage.**

The 2026-07-24 Clocktower inspection is still a valid negative for *that*
building. But the *search* was never comprehensive; it was a survey of whatever
could be seen from the riverbank. **Negative results are only as good as the
sightlines that produced them**, and that qualifier now needs attaching to every
negative in this file.

### What this makes cheap
The hard part — *which building* — is answered. What remains is **which face and
which ledge**, and that needs no access at all:
- **Watch at dusk from a position with a clear sightline on the building**, not
  from the river. The large cleared lot immediately west gives an unobstructed
  view of at least one elevation.
- **Follow them in.** They will fly to a specific ledge. That converts a
  four-face roof sweep into one corner.
- **Then check the facade below that ledge for whitewash**, which is visible from
  the ground and is the diagnostic sign.

Two evenings of standing in the right spot would likely produce a better-founded
nest claim than a roof visit made blind.

---

## 2026-08-24 ⭐ CLOSED — `53/BS` IS "AMOS", AND HE IS A MALE. NH Audubon confirmed.

**The question this project was built to answer is answered.** From the email
chain (archived, gitignored, `private/email/`):

**Christian Martin, NH Audubon, 2026-08-24 08:47:**
> "Black over green **53/BS aka 'Amos'**, now a 9-yr old **hatch year 2017 male**
> from Brady Sullivan in Manchester. Banded in May 2017 by Chris Martin…
> Mickayla, let me know when you want to review submitting band reports to BBL."

(Chris first wrote "May 2024" and **corrected it himself at 12:09** the same day —
2024 was a different session. He also notes **Mark Timmerman, in this group, was
present at the 2017 banding.**)

**Nora Hanke, 2026-08-24 08:05, reading the raw frames independently:**
> "White on black, **53**, over white on green **?3 or B** and then **S**."

### Why this counts as independent, when this file argued it might not
The standing worry here was that every reader knew the answer in advance and
that all four glyphs sit in the confusable set (`5↔S`, `3↔B↔8`). Two things
retire it:

1. **Nora's read is partial and hedged in precisely the predicted place.** This
   file named the **green segment** as the weak half — lower paint-to-substrate
   contrast, worse weathering — *before* her reply existed. She got `53` and `S`
   clean and balked at the middle green glyph. A primed reader produces the
   expected answer smoothly; an honest one produces exactly this.
2. **Chris matched the code to the banding record, not to the photograph.**
   That is a lookup against deployed bands — the independence test this file
   said was the only thing that would settle it.

### The sex contradiction is resolved, and this project was on the wrong side
**Amos is MALE.** So:
- David's *"that female they banded"* — wrong.
- The 2026-08-10 reading of the hunt (*"the banded female… Mom didn't want to
  share"*) — wrong on both counts.
- The unanimous **2026-07-23** thread that called it male — **right all along**,
  and this file downgraded it.
- By elimination the **unbanded** clocktower bird is the **female**.

**Five experienced observers sexed this bird by eye over six weeks and the
majority got it wrong.** Reverse size dimorphism is real and useless on a lone
perched bird with nothing in frame to compare to. That is the single best
argument this project will ever have for the curator's own rule — *no individual
ID without a photograph of a readable band* — and it belongs in
`docs/id_method.md`.

### Everything downstream that now unlocks
- `nashua-01` is **identified**: name, sex, hatch year, natal site, band history.
- The withdrawn "nine years old, hatched 2017" claim is **reinstated**, now
  sourced to the bander instead of to hearsay.
- **Territory tenure is partly answered for free**: a 2017 Manchester bird holding
  downtown Nashua means natal dispersal of ~30 km, and it is worth asking Chris
  when Amos was first recorded on *this* territory.
- The sighting is going to the **federal Bird Banding Laboratory**.

---

## 2026-08-24 ⚠ A FOURTH BIRD — Nora saw a DIFFERENT banded adult here in March

Buried in the same message that confirmed the code, and nobody in the thread
picked it up:

> **"A different bird than I saw there in March, when the black band had a
> definite 9 on it."** — Nora Hanke, 2026-08-24

**`53/BS` contains no 9.** So a *second banded adult*, carrying a different code,
was at this site in **March 2026**. That is not Amos and not the unbanded
female. It is a bird this project has no record of.

### What it puts back in play
The catalogue's oldest band evidence is **`20260804-f3001faa`, February 2026** —
Jarrod's in-flight frame showing a silver federal band, **code not resolvable**.
That frame has been carried under `nashua-01` on the assumption it was the same
banded adult. **That assumption is now unsafe.** February is one month from
Nora's March sighting and six months from the first confirmed Amos photograph.
The February bird could be Amos, could be the "9" bird, and nothing in the frame
decides it.

### Actions
1. **Ask Nora directly** what else she has from March — a photo, a fuller code,
   a date, a perch. She reads bands carefully and hedges honestly; her March
   observation is the most valuable untapped lead in this file.
2. **Ask Chris** whether a second banded adult is known on or near this
   territory, and whether any code with a `9` was deployed in the region.
3. **Do not merge the February record into `nashua-01`.** Per
   `individuals/README.md`, slugs merge forward and never split — so wrongly
   folding February into Amos is a mistake that cannot be cleanly undone later.
4. **Open a slug for the March bird?** — *curator's call.* The standing rule is
   no individual ID without a photograph of a readable band, and there is no
   photograph here, only a careful observer's report. Flagged for David rather
   than decided unilaterally.

### Also unresolved in the chain, and it is addressed to the group
Kevin T asked on **2026-08-10** whether to fly his drone (he is Part 107
licensed, with prior authorization in the area) to look for the nest, explicitly
deferring to the people who know the birds — *"I don't want to risk stressing the
birds, provoking a strike."* **Fourteen days later nobody has answered him.**
Given that finding the nest is this project's highest-value open item, and that
peregrines are known to strike drones, that question deserves an actual reply
from Chris or Mickayla rather than silence.

**Two of David's messages to the chain bounced** (Mail Delivery Subsystem,
08-13 14:03 and 08-24 14:40 — the second carried the Google Photos link). Worth
confirming the album link actually reached everyone.

---

## 2026-08-24 — detection is ~100%, and that number has been doing the wrong job

David, on the outstanding denominator question:

> *"i will see a falcon down there anytime i want, it was so common, i didn't
> even pay attention until people started getting excited about the bands"*

**Accept it.** He is the observer, 24 peregrine-positive checklists at one site
across a year support it, and no computed rate would be better evidence than the
person who goes there. The `~100% detection at Mine Falls` line in `CLAUDE.md`
stands.

### But this project has been running three different rates as if they were one
Finding a falcon was never the bottleneck. Measured against the catalogue:

| what you want | rate | evidence |
|---|---|---|
| **see any peregrine** | **~100%** | David, 24/24 positive checklists |
| get a frame that can be **aged** | **39%** | 37 of 94 photos |
| get a frame tied to an **individual** | **23%** | 22 of 94 |
| resolve a **tarsus** at all | **15%** | 14 of 94 |
| **read a band** | **6%** | 6 of 94 — and 5 of those are one 3-second burst |

On the best day this project has ever had — 127 frames, two hours, the right
lens, a cooperative bird on an open crossbar — the yield was **5 readable-band
frames, 3.9%**.

**The ~100% figure has been used to plan photography.** It should only ever have
been used to plan *attendance*. The two questions it does answer: is it worth
driving over (yes, always), and does the trip need to be timed to peak activity
(no). Everything past that — which bird, what age, is there a band, what does it
say — runs on rates between 6% and 39%, and those are the numbers that should
drive how long to stay and how many frames to take.

### The record's density measures David's attention, not the falcons
*"i didn't even pay attention until people started getting excited about the
bands."* That single sentence is a warning label on the entire time series:

- **The sparse pre-2026 record is absence of effort, not absence of birds.** No
  question of the form *"how long has this pair held the territory?"* can be
  answered from these checklists.
- **The near-weekly July–August 2026 cadence is elevated attention**, not
  elevated falcon activity. Any trend drawn through it measures interest.
- This is the same class of error already caught twice here — the peer session's
  zero-dispersal finding (an eBird hotspot-coordinate artifact) and this
  project's own bearing triangulation. **Observer effort is the standing
  confounder in this file.** Third strike; it should now be the first thing
  checked on any pattern claim.
- Concretely: the **six-day gap between the 08-16 and 08-22 checklists** is
  unexplained and sits inside the juvenile's departure window. It may be a break
  in attention rather than a break in presence, and it is the reason that window
  cannot be closed.

### The recoverable part, and it decays
*"it was so common"* is real baseline data about years this project has no
records for — and it exists only in memory. Two sources, both already on the
standing todo list, both worth chasing before they fade:
1. **David's own recollection** of how far back reliable Mine Falls peregrines go.
2. **Jarrod's nine-year back catalogue** — dated files, which beat anyone's
   memory and could establish territory tenure directly.

Territory tenure is exactly what NH Audubon would want alongside a band code,
and unlike the code it needs no reply from anyone.

---

## 2026-08-24 (eBird) — the adults are RESIDENT, and the detection claim is still unverified

From David's peregrine list at **Mine Falls Park–Spine Rd. Entrance** (24
peregrine-positive checklists, 2025-08-15 → 2026-08-24):

**Peregrines are at this site in every month sampled, including deep winter** —
2025: Sep 07, Oct 03, Dec 06, Dec 14, Dec 31. 2026: Jan 07, Jan 11, Mar 13, Jun
05, Jun 25, Jun 28, then near-weekly through July and August.

**This pair does not migrate.** That is a real finding and it changes several
things in this file:
- The 2026-02 banded-bird photo is no longer an isolated winter record needing
  explanation — winter presence is the norm here. It further retires the 08-16
  worry about a February passer-by.
- `nashua-01` being "the stable subject" is now supported by a year of
  occupancy, not just by the general claim that resident adults stay put.
- Anything anyone ever wants to do with these adults has **no seasonal
  deadline**, and the window that avoids disturbing a nest is the winter one.

### The denominator is STILL missing
This list is **peregrine-positive checklists only**. It cannot produce a
detection rate, because the blank trips are not in it. The standing claim in
`CLAUDE.md` — *"Detection is ~100% at Mine Falls"* — therefore remains
**unverified**, and it is load-bearing: it is the reason this project believes
it can schedule observation freely by time of day. What is needed is the
**total** Mine Falls checklist count over the same span; 24 positives out of 24
trips is a remarkable claim, 24 out of 60 is an ordinary one.

### One record that is not what it looks like
**15 Aug 2026, Plum Island, MA, #1** — same date as the Mine Falls `#2`. This is
**not** dispersal evidence. It is a different bird at a coastal migration site
~65 km away, logged on a day the Nashua juvenile was photographed on its own
territory at 19:36. Noted here so nobody later mistakes it for the fledgling
turning up down the coast.

(Also confirmed in passing: the two **Forsythe NWR, NJ** checklists — 2025-11-08
and 2026-01-19 — correspond exactly to the two New Jersey frames identified as
catalogue contamination. That diagnosis was correct.)

---

## 2026-08-24 — the juvenile is gone. Last photograph 08-15, not 08-10.

David: *"i am claiming the juvenile got kicked out, haven't seen it for a week,
used to see it every day."*

**The catalogue was wrong about the last date and it was wrong in his favour.**
It read *last recorded 2026-08-10* — because **22 frames from 08-09, 08-12 and
08-15 had been ingested but never scored to an individual.** Scoring them today
from plumage moves the juvenile's last known appearance **five days later**:

| date | juvenile? | evidence |
|---|---|---|
| 2026-08-09 20:23–20:26 | **yes** | 2 frames, with an adult earlier the same evening |
| 2026-08-10 09:19 | **yes** | chased off the kill — weaning |
| 2026-08-12 08:44–08:49 | **yes** | 6 frames alone on the crossbar; best juvenile plumage series in the catalogue |
| **2026-08-15 19:36** | **yes — LAST** | in a dead tree; an adult on the box at 19:45 and 19:49 |
| 2026-08-23 17:46 / 19:47 | no | two adults |
| 2026-08-24 19:31–19:52 | no | adult only |

Age was scored on the one plumage character that actually separates them:
**juvenile = vertical teardrop streaking on a warm buff ground, brown-toned
above; adult = slate blue-grey above with horizontal barring below.** Unlike
malar shape or molt gaps, that character is unambiguous and it is why these
frames could be scored cold, months later, off the album.

### The window — WIDENED 2026-08-24 after checking eBird
First written here as **08-15 → 08-17**. David's eBird record forces it open:

| date | eBird count | photographed | juvenile? |
|---|---|---|---|
| 2026-08-15 | **#2** | 2 juv + 5 adult | **yes — last confirmed** |
| 2026-08-16 | #1 | none | **unknown — bird never aged** |
| 2026-08-22 | #1 | none | **unknown — bird never aged** |
| 2026-08-23 | #2 | 7 adult | **no — both birds photographed, both adult** |
| 2026-08-24 | #1 | adult | no |

**Last confirmed present 08-15; first confirmed absent 08-23.** The 08-16 and
08-22 checklists each logged one bird that was never aged and could have been
either. David's memory (~08-17) sits at the front of that gap and is the best
estimate, but the *record* cannot go tighter than an eight-day window.

### The eBird counts cannot close it, and here is the proof
**2026-08-09: eBird logged `#1`. The photographs from that evening show two
birds — an adult 19:59–20:16 and the juvenile 20:23–20:26.** The checklist
undercounts by one on a date where the catalogue has the frames to prove it.

This is the mirror of the caveat already carried on the 07-17 and 07-23 rows
(*"a 2 may be a pair, an adult with a fledgling, or one bird counted twice"*).
The inverse is now demonstrated: **a `#1` does not mean one bird was present.**
An observer who sees an adult, then a juvenile twenty minutes later, and cannot
be sure they are different birds, correctly logs 1. So the count series
`2,1,1,2,1` across 08-15→08-24 is **not** evidence of the juvenile leaving.
Only the aged photographs are.

**Rule for this project: eBird counts are a floor on birds present, never a
census, and they carry no age information at all.**

### What the record can and cannot say
The timing is textbook and supports the claim: weaning was **directly observed**
on 08-10 (adult killed, juvenile tried to join, was driven off, screamed and
circled) at roughly 8 weeks post-fledge. Departure ~9 weeks post-fledge, mid-to-
late August, is squarely normal for natal dispersal in the Northeast.

**But absence is not departure, and three explanations fit these observations
equally well:**
1. **Dispersed** — left the natal area. David's reading, and the most likely.
2. **Died.** First-year mortality in peregrines is high; figures of 50–70% in the
   first year are commonly cited. A bird described as flying "like an idiot",
   hunting over open water and around city structures, is exactly the profile
   that collides with something. This possibility is unwelcome and belongs in
   the record anyway.
3. **Relocated locally** — still in the area, different perches or hours. Note
   the observer's own schedule shifted: 08-23 was shot at 17:46, 08-24 at
   19:31–19:52, while the juvenile's known pattern was the pond and the square
   chimney at dusk.

**The missing number is the denominator.** "Haven't seen it in a week" carries
weight in proportion to how many times someone looked. Five negative visits is
strong; two is nothing. **David's eBird checklists hold that count** — and the
project's own precedent (the 2026-07-24 negative nest search, logged as a
sighting with `count=0`) says negative visits get recorded as data.

### What would actually confirm dispersal over mortality
**An eBird report of a juvenile Peregrine elsewhere in the region in the next few
weeks.** That is the one observation that separates hypothesis 1 from
hypothesis 2, and it is checkable — the `ebird_api` client next door in
`../birds/` already does regional species queries. Worth running against the
surrounding counties for the rest of August and September.

### The systemic bug this exposed
**82 of 94 photos in the catalogue carry no individual assignment.** That is why
a five-day error in the juvenile's last-known date sat in the record unnoticed.
Ingest captures a photo; it does not score it. Any date claim of the form "last
seen X" is only as good as the scoring, and the scoring has been the neglected
half of this pipeline. Also outstanding: an **un-ingested video** from the 08-15
session (`PXL_20260815_234515843.mp4`) that nobody has reviewed.

---

## RULING (2026-08-24) — nobody in this group traps anything. Find the nest instead.

Raised in session as a way to settle whether `nashua-03` is one bird. Recorded
here because it will come up again, and because getting it wrong is expensive.

**Legal.** Peregrines were delisted from the federal Endangered Species Act in
1999 but remain fully protected under the **Migratory Bird Treaty Act**, and are
**state-listed in New Hampshire** on top of that. Trapping one requires a USGS
**Bird Banding Laboratory** permit with raptor authorization *plus* NH Fish and
Game authorization. Without them it is a federal misdemeanor — up to $15,000 and
six months, **per bird** — and the MBTA is a strict-liability statute, so good
intentions and a survey notebook are not a defence.

**The permits already exist inside this project's contact list.** Chris Martin at
NH Audubon bands New Hampshire's peregrine chicks; that is his actual job.
Mickayla Johnston works the same program. If a bird in this territory ever needs
to be in a hand, it is one of theirs. Ask; do not do.

**It would not even answer the question.**
- `nashua-01` is already banded and photographed at 340–420 px. Handling it
  returns nothing the 08-23 frames did not.
- The unbanded adult's *sex* is the live question — and **one frame of both
  adults together, size-compared**, settles that without touching a bird.
- Free-flying juveniles are trapped with a bal-chatri or dho-gaza over a live
  lure bird. Peregrines are banded as **nestlings at ~3 weeks** for good reason.
- **Capture myopathy** is real: a struggling raptor can die days later from a
  capture that looked clean.

### The actual lever, and it is a big one
An unbanded juvenile means **NH Audubon never reached this nest in 2026.** That
is the root cause of every identification problem in this file. Find the nest,
hand the location to NH Audubon, and next season they band the brood legally in
about ten minutes at the ledge — after which **every Nashua juvenile is traceable
for life** and nobody has to squint at a tarsus again.

That converts a recurring, unsolvable problem into a one-time favour. The tool
for it already exists here: [`nest_map.py`](nest_map.py) bearing triangulation.
What it lacks is **bearings** — which is already on the standing todo list, and
just became the highest-value item on it.

---

## OPEN QUESTION (raised 2026-08-23) — can `nashua-03` be one bird?

The juvenile is recorded as unbanded on the curator's determination, from
repeated close looks at the legs while it fed. That determination is sound. But
it creates a gap the slug design does not cover, and it should be named before
it hardens.

**An unbanded bird is unidentifiable by definition.** "The juvenile is unbanded"
and "it is the same juvenile every time" cannot both be established by the same
observation — bare legs are what makes the first true and the second unprovable.
A single brood commonly fledges two or three young. **Two unbanded siblings
working the same pond and the same plucking post would look exactly like one
bird seen repeatedly.**

The permanent-opaque-slug rule in [`individuals/README.md`](individuals/README.md)
was built to stop a *successor* silently inheriting a predecessor's record. It
does not stop two *contemporaneous* unbanded birds collapsing into one slug, and
that is the live risk here. `nashua-03` may be a bird or may be a brood.

**What would separate them, cheaply, without a band:**
- **Two at once in one frame** — settles it instantly, nothing else needed.
- **A count at the nest earlier in the season** — how many fledged? Anyone in the
  chain who watched in June answers this from memory.
- **Molt/plumage gaps on out-of-camera frames** — juvenile feathers are fresh and
  undamaged, so a broken or missing primary is individual and stable for months.
  This is the one trait tier that works on a bird with no band.

Until one of those lands, `nashua-03` should be read as *"the 2026 juvenile
cohort on this territory"*, not as one animal. Nothing in the record breaks if
it turns out to be two — but a trait description built by merging two birds
would be quietly wrong, and that is the kind of error this project exists to
avoid.

---

## 2026-08-23 (ruling) — CODE CONFIRMED BY THE CURATOR: `53/BS`. Sex now contradicts it.

**David has called it.** His standing rule since 2026-08-10 was *no individual
identification without a photograph of a readable band.* The 2026-08-23 frames
are that photograph, and he reads the code as **`53/BS`**. `band_code` is now
written into `data/photos.csv` and [`individuals/nashua-01.md`](individuals/nashua-01.md)
at `confirmed`, attributed to him and dated.

**This project's "agreement" is not corroboration and is recorded as such.**
The read was made knowing the expected answer, and all four glyphs sit in the
confusable set (`5↔S`, `3↔B↔8`) — a second reader holding the prior adds close to
nothing. What the project *can* say without the prior is narrower and honest:
the black segment carries two glyphs and the green segment two, the black pair
is the sharper of the two, and **the green segment is the weak half** — green
bands weather worse and the paint-to-substrate contrast is lower, so `B` and `S`
are the glyphs most likely to be wrong. `3` vs `8` on a worn band is the other
live failure. Only NH Audubon's deployed-code list settles it.

He has also determined, from repeated close observation of the bird feeding on
its plucking post, that **the juvenile is unbanded.** Recorded as a curator
determination. See the entry above for what that implies — NH Audubon has never
accessed this nest, and this year's fledgling is permanently untraceable.

### The open question is no longer the code — it is the sex
David describes the banded bird as **"that female they banded."** That collides
with the identity, and the collision is material:

| source | sex of the banded bird |
|---|---|
| 2026-07-23, three observers, unanimous | **male** |
| 2026-08-10, two observers | **female** |
| 2026-08-23, David | **female** |
| NH Audubon's account of "Amos" | **male**, hatched Brady Sullivan 2017 |

**If this bird is female, it is not Amos** — and the 2017 hatch year, the Brady
Sullivan natal site and the whole Manchester-origin story fall with it. Either
the sex calls are wrong, or `53/BS` belongs to a different bird, or NH Audubon's
Amos record has the sex wrong. `sex` therefore stays unresolved on `nashua-01`
even though `band_code` is confirmed, and the alias "Amos" is still **not**
accepted.

**So the message to NH Audubon carries two questions, not one:**
1. Is `53/BS` a code you actually deployed?
2. Is that bird male or female?

Answer both and this territory has, for the first time, one identified
individual with a known origin.

---

## 2026-08-23 (field) — the juvenile has a plucking post, and it is a structure

> **⚠ READ THE 2026-08-24 ENTRY ABOVE FIRST.** Everything below is written in the
> present tense — "seen it every time I go", "in daily use", "uses every single
> day". **That period appears to have ENDED around 2026-08-16.** The behaviour
> described here is real and was observed repeatedly, but it describes roughly
> mid-July to mid-August 2026, not the current state. The plucking post is still
> worth finding — the prey remains at its base do not disappear when the bird
> does.

David, from repeated observation — **"seen it every time I go":**

> "the juvenile flys like an idiot, it goes to the pond, chases birds around for
> a while, eventually gets one, then takes it to the tall square chimney and eats
> it… the adults stay more in the city and just bop a pigeon real quick"

### The competence split is now observed, not inferred
This log hypothesised on 2026-08-16 that the adults were working the built
environment while the juvenile worked the water. **That is now a direct
observation across many visits, not a guess** — and the mechanism is textbook.

A juvenile peregrine carries a longer tail and broader, rounder wings than an
adult: more lift and agility, less speed and efficiency. It is built to learn,
not to kill economically. So it does what David describes — many attempts, long
chases, eventual success, over open water where prey has nowhere to take cover
and a missed stoop costs nothing. The adults' "bop a pigeon real quick" is the
opposite: a skilled bird spending as little energy as possible on abundant,
predictable prey among the buildings.

**Two birds, two hunting economies, two parts of town.** That is real natural
history and it belongs in the Ink Link piece.

### The line that matters operationally
**"takes it to the tall square chimney and eats it."**

That is a **plucking post**, identified, in daily use. Peregrines do not eat
where they kill — they carry prey to habitual perches. Consequences:

1. **A structure this bird uses every single day is now named.** Note it is
   described as *square*, which distinguishes it from the **circular chimney
   across the river** already on the candidate list. Worth pinning down whether
   this is the **millyard smokestack** or a fourth structure nobody has listed.
2. **There will be prey remains at its base** — feathers, bones, and whitewash.
   That is collectable diet data, and a single primary or tail feather gives a
   species ID that survives when a photograph does not. NH Audubon will want it.
3. **It is the place to photograph the juvenile.** Every attempt so far has been
   at a fast, erratic bird in flight. But a bird that has just carried prey to a
   perch **stands still and eats for ten to twenty minutes**, preoccupied. That
   is the same geometry that produced the 2026-08-23 band frames on the adult.

### Why that third point is urgent
**The juvenile's band status is completely unknown.** If NH Audubon banded this
year's brood in the nest, its code exists on paper and has never been read in the
field. And it is the bird where a band matters most: it disperses within weeks,
first-year peregrines move hundreds of kilometres, and **a code is the only thing
that could ever connect this individual to a sighting somewhere else.**

Everything needed is already known — the place, the routine, the posture. What
was missing on the adults for a month is, for this bird, simply a matter of
being at the chimney when it arrives.

---

## 2026-08-23 (later) — the DNG was a dead end; the JPEG is the best band evidence in the project

David pulled three `.ORIGINAL.dng` files. **Tested, and the assumption behind the
request was wrong — mine.**

**The Pixel's DNG is 2572x3414 (~8.8 MP). Its JPEG is 6144x8160 (50 MP).** The
RAW is the binned sensor readout; the 50 MP JPEG comes off the full-resolution
path. **The JPEG has 2.4x the linear resolution**, and side by side on the same
band the DNG is visibly softer. Written up in
[`docs/id_method.md`](docs/id_method.md) as a transferable rule: on a
computational-photography phone, do not assume RAW beats JPEG for fine detail —
test one before asking anyone to export a hundred.

*(Also: macOS `sips` silently hands back the DNG's embedded preview rather than
demosaicing it. `rawpy` was installed into the shared venv to read it properly.)*

### Where the read actually stands
On the best JPEG frames, **four character positions are resolvable** on a band
that is unambiguously **black over green**. The shapes are **consistent with
`53/BS`, and nothing visible contradicts it.**

That is a genuine advance and it is still not a code read. **It is a
corroborating observation, not an independent one** — the expected answer has
been in front of me for a month. Handed these pixels cold, the honest transcript
is *"5-or-S, then 3 / S-or-5, then B-or-8"*. Recorded at `probable` with
`band_code` still blank.

**Why that is nevertheless enough — for somebody else.** NH Audubon holds the
list of codes actually deployed in New Hampshire. "Consistent with 53/BS, four
positions resolvable, black over green" is a *matching* problem against a known
set for them, where it is an *open reading* problem for us. They can confirm or
reject it in one look. Send the five originals.

---

## 2026-08-23 — A BI-COLOUR BAND AT READABLE SCALE. Code still not called.

David watched one bird for over two hours and came away with 127 frames, and he
saw with his own eyes what nobody in this project had confirmed: **a silver band
on one leg and a green/black band on the other.** The photographs back him.

### What the frames decisively establish
**Five frames (`PXL_20260823_2146…`) show the bi-colour band on the tarsus at
~250–360 px in a native 6144×8160 file.** Every previous attempt in this project
had roughly **12 px** of band. This is a 20–30× improvement and the first time
resolution has not been the binding constraint.

They also settle two smaller things:

- **The band is BLACK over GREEN.** That is the eastern US rig, and it confirms
  the group's written "G/B" is transposed — it should be **B/G**.
- **Engraved characters are plainly present** on both segments. Not a smudge, not
  a highlight. Characters.

### And the same evening: two adults, one banded, one not
Two hours later at the clocktower weathervane (`PXL_20260823_2347…`), an adult
with **both tarsi bare**. So on a single date: a banded adult on the radio-tower
crossbar and an unbanded adult on the weathervane. **That is the cleanest
evidence yet that the pair really is one banded bird plus one unbanded bird**,
and it substantially answers the doubt raised on 2026-08-16 — the banded bird is
not a February ghost, it is here in August.

### The code is NOT called, and the reason is not resolution
Deliberately left blank in `band_code`. Two things block it, and neither is
pixels:

1. **The paint is worn.** These bands have been on the bird for years and the
   white infill is degraded.
2. **A band is a cylinder.** Only part of the code faces the camera in any given
   frame, and the rest wraps out of sight. The five frames catch it at different
   rotations, which helps, but no single one shows the whole legend.

There is a third reason, and it is the important one: **I know what code the
group expects.** "53/BS" has been in every email for a month. Reading a worn,
curved, partly-obscured legend while primed with the expected answer is precisely
how a wrong `confirmed` gets manufactured — and this project has already
recorded, in [`PLAYBOOK.md`](PLAYBOOK.md) §6, that a hedge does not survive being
forwarded. I can see characters. I am not going to name them.

### Who should call it
**NH Audubon.** They read these codes professionally, they know how a decade-old
band wears, and — decisively — **they hold the list of codes actually deployed in
New Hampshire.** That turns an unconstrained reading problem into matching a
partial against a known set. It is the same argument as `PLAYBOOK.md` §2 step 0:
the expert node resolves in one reply what inference cannot.

An evidence package is on David's Desktop at `falcon_band_20260823/` — the five
best band crops at 4× plus the five untouched full-resolution originals. Send the
originals, not the crops; let them do their own enlargement.

### One thing worth asking David
The filenames end `.RAW-01`, which is how a Pixel names a JPEG derived from a RAW
capture. **If the DNGs are still on the phone, they may carry more recoverable
detail in the worn paint than the JPEG does.** Worth checking before anyone
concludes the code is unreadable.

---

## 2026-08-16 — the observer with the best detection rate has NEVER seen the band

David, unprompted, after five weeks of near-daily visits:

> "haven't ever seen the banded one; will usually get a shot, watch them, they
> move and i see the legs, then they go about their business… almost want to
> call bullshit on it"

**This is the strongest evidence yet on the band question, and it points the
other way.** He has the highest detection rate of anyone — a falcon on
essentially every visit to Mine Falls, 13 Jul through 16 Aug — he routinely
watches the birds until they shift and expose their legs, and he has never once
seen a band.

### The evidence tally, which nobody had actually run
Frames in the catalogue where the tarsus was genuinely visible:

| photo | band | date | provenance |
|---|---|---|---|
| `20260804-f3001faa` | **yes** | 2026-02 | **no EXIF** — date taken from an email |
| `20260722-5cf2df73` | no | 2026-07-22 | EXIF |
| `20260722-ec1dd230` | no | 2026-07-22 | EXIF |
| `20260810-08f56710` | no | 2026-08-10 | manual |

**One frame shows a band. Three show bare tarsi.** And the one is a single
in-flight leg at 20–25 px, in a file carrying no EXIF at all, whose February
date exists only because someone typed it in an email.

**The attestation chain is also thinner than it reads.** Nobody in it claims to
have seen a band themselves. One observer: *"I **think** the adult male is the
only one that's banded."* Another: *"We **think** the male is banded… I
**believe** Mark and Dave were able to establish that."* That is a belief being
relayed, not an observation being reported.

### A hypothesis nobody has raised: the banded bird may not be one of the pair
**February is not the breeding season.** A banded peregrine photographed in
flight in February is not necessarily a member of the summer territorial pair —
it could be a wintering bird, a floater, or a passing individual from the
well-studied Manchester population 20 km north.

That single hypothesis explains every awkward fact at once: why the most
frequent observer never sees a band, why every warm-season tarsus photo is
bare, and why the sex assignment "flipped" on 08-10 — observers were attaching a
remembered band to whichever adult was in front of them.

It also means [`individuals/nashua-01.md`](individuals/nashua-01.md) may not be
a resident bird at all, and possibly not a distinct individual from
`nashua-02`. Flagged there; **not merged**, because per
[`individuals/README.md`](individuals/README.md) splitting a slug later is far
harder than merging one.

### The test, and it is the same file as always
**Jarrod's full-resolution original of the February frame.** At 33 MP instead of
5.5 it settles whether that is a band or an artefact of 20 pixels. Second ask,
free: *has anyone actually seen a band in the field, with their own eyes?*

### Why every frame is soft — and the fix
David: *"it usually gets too dark by the time I find the bird, then all bets are
off."* He works the hour before sunset because that is when the birds are most
active. That single fact explains the backlit silhouettes, the noise, and the
softness that has blocked every band read in this project.

**But near-100% detection dissolves the trade-off.** He does not need peak
activity to *find* the birds — they are reliably there. So split the trips:
**midday for the band** (loafing bird, stationary, full sun, scope on the left
leg) and **dusk for behaviour** (hunting, interactions, the departure bearing).
Trying to do both in one visit is why neither has worked.

*(Also noted: David has never seen all three birds at once — only Jarrod has,
on 2026-07-22. Consistent with three birds that rarely co-occur, and not itself
alarming.)*

---

## 2026-08-16 (later) — a refutation, logged with its numbers

The sibling `birds/` session ran the control I suggested and **retracted its
Read 1**. Recording the arithmetic rather than just the retraction, because the
numbers are the transferable part.

County-wide spread, computed per-record (its original method) against per
**distinct location**:

| month | records | distinct locs | per-record | per-distinct-loc |
|---|---|---|---|---|
| Mar | 19 | 5 | 2.45 | 3.04 |
| Apr | 22 | 6 | 3.90 | 7.70 |
| May | 17 | 2 | 4.43 | 19.99 |
| Jun | 22 | 9 | 6.40 | 4.62 |
| Jul | 16 | 9 | 10.27 | 9.07 |
| Aug | 6 | 4 | 10.32 | 11.61 |

The clean monotonic Mar→Aug dispersal curve **does not survive**. Per distinct
location it is noise, and May's 19.99 is two far-apart points. What the
per-record metric measured was records-per-hotspot concentration: 19 records over
5 locations reads tight, 16 over 9 reads dispersed, and the birds never entered
the calculation. The Nashua subset was 18 records across **four** distinct
locations — a spatial analysis on four points.

**A second retraction, which was theirs and which I had not caught.** They twice
argued that because NH Audubon banded the bird, NH Audubon must know the nest.
That does not follow: **banding site is not breeding site.** A band records where
a bird *hatched*, and New England peregrines disperse an average of 88 km (males)
to 153 km (females). Our own file has the banded adult as a possible Brady
Sullivan bird that moved 20 km south — which is precisely a case of the two being
different places. Now written explicitly into
[`docs/id_method.md`](docs/id_method.md), since this repo used "natal site"
correctly throughout but never said *why* the distinction matters.

The recommendation to ask NH Audubon survives on different and better grounds:
they monitor NH eyries **as a programme**, so they would know whether Nashua has
an active one — independently of anything about that individual bird.

### The headline lesson, and it is now PLAYBOOK §6
**Two independent analyses, on the same problem, on the same day, both bottomed
out on observer artefacts.** Theirs measured where birders file checklists. Mine
measured where photographers point cameras. Neither measured falcons.

The diagnostic that catches it is cheap: *would this number change if the animals
stayed put and only the observers moved?* If yes, you are measuring observers.
Added to the playbook as a fifth contamination vector, and placed above the
others in priority — it is the one that fooled two analysts in one day, and
community-science data is effort-biased by construction rather than by accident.

**What survives on both sides**, because it rests on physiography and biology
rather than statistics: Mine Falls is flat river parkland and cannot hold a
scrape, so it is the hunting ground and the nest is on a structure just off it.
Whitewash on west and south faces, and the mid-March→late-April
courtship-at-the-scrape window, stand on the same footing.

---

## 2026-08-16 — THE ALBUM ORIGINALS LANDED. New Jersey found, and every frame carries a compass bearing

David downloaded the album. 84 files (79 JPG + 5 MP4), ingested with `--site`.
**Catalogue is now 87 photos spanning 2025-08-15 to 2026-08-15** — a full year,
where yesterday it was five frames over three weeks. Originals copied to the
Drive `_private` tree.

### The New Jersey trip: found, and it is exactly two frames
`39.4466, -74.4158`, **2025-11-08, 443 km from Nashua** — Forsythe NWR /
Brigantine, coastal New Jersey. Catalogued as `--site nj-forsythe-brigantine`
and **kept, not deleted**: they are real peregrine observations, just of a
different population.

Weeks of squinting at habitat, and coordinates answered it in seconds. Exactly
the argument in [`PLAYBOOK.md`](PLAYBOOK.md) §6 — *habitat and structures look
alike; coordinates do not.*

### Every geotagged frame carries a compass bearing
**65 of 79 have GPS** — all the Pixel frames; the Sony writes none, as
established. And **all 65 carry `GPSImgDirection`**, the heading the camera was
pointed. That is position *plus* aim: each frame is a ray at whatever the
photographer was shooting.

**They are MAGNETIC bearings** (`GPSImgDirectionRef: M`). Nashua's declination
is about 14° west, so every ray needs rotating before use; skipping that
silently smears the answer. `nest_map.triangulate()` now does it, with a unit
test on the geometry.

### Triangulation — a lead, and honest about being one
63 Nashua rays → 262 well-conditioned intersections after rejecting
near-parallel pairs. The densest cluster sits **26 m from the Mine Falls Spine
Rd hotspot**, with secondary clusters 115–143 m north-east.

**Read it carefully.** This says *what the group photographs*, which is not the
same as *where the birds nest* — and its error bars are wide: phone compasses
are ±10–20° and worse beside steel, which a millyard and a lattice tower supply
in quantity. At 100 m that is ±26 m, about the size of the clusters themselves.
It corroborates the radio tower as the most-photographed subject. It does not
locate a scrape.

### The intake tool earned its design
Ingesting the originals over the top of the PDF-extracted screenshots, the
perceptual hash **matched the weathervane screenshot to its own original at 0
bits** (`20260810-706db497 ~ 20260810-08f56710`), plus four more burst pairs.
A low-resolution copy re-identified against the full-resolution file, exactly
what `dhash` is in the schema for.

### Intel from the sibling `birds/` session (read-only, not written by them)
That session swept eBird `historic_observations` for the county, Mar–Aug 2026,
and passed over three things worth keeping:

- **Whitewash is the off-season discriminator.** An occupied ledge accumulates
  heavy white streaking below it, visible year-round with a scope. Prioritise
  **west and south faces** — the ledge should overlook the hunting ground, and
  Mine Falls is W/SW of the millyard. **This is the only method that works
  right now**, with the nest inactive.
- **Mid-March to late April is the window the birds give it away.** Courtship
  ledge displays and male-to-female food transfers happen *at the scrape*.
- **A candidate structure nobody here had listed:** the F. E. Everett Turnpike
  bridge over the Nashua River. Bridge piers are a classic urban peregrine site.

**One of their conclusions does not survive checking.** They report the Nashua
birds showing near-zero seasonal dispersal (0.00–0.45 km) against Manchester's
2.45→10.3 km, and read it as a pair tethered to a fixed structure. But 14 of
their 18 Nashua records sit on a single eBird hotspot, and **a hotspot's
coordinate is where the checklist was filed, not where the bird was.** A birder
at the Spine Rd entrance logs a falcon 400 m away to that same point. The
"0.00 km spread" measures observer convention, not bird movement. Their
reads 2–4 stand; read 1 does not.

---

## 2026-08-15 — album has roughly doubled and now spans a full year

Re-pulled the shared album. **It is no longer the 30-photo, four-week set this
log has been reasoning about.**

- **Photo count: at least 74** (counted from the grid's own per-photo links).
  I could render 48 of them; the rest defeated the scraper, see below.
- **Date range now reads Aug 15 2025 – Aug 15 2026** — it was 29 Jun – 24 Jul.
  A full year went in, which means **back-catalogue material is now in the
  album**. That is the multi-year continuity this project has been asking for,
  arriving through the album rather than as a separate hand-over.
- **David confirms no AI enhancement on the new material.** So the recent frames
  are admissible for trait scoring under the rule in `docs/id_method.md` — the
  first frames in this project that are.

**New settings not previously in the album:** close-range birds on a metal
rail/ledge, birds on a mossy brick arch, a bird at close range on a stack top,
and at least one video. Much tighter framing than the old white-bracket set.

**Band status: still nothing.** Every close frame I checked (six of the most
promising) shows the same hunched posture with the tarsus tucked under the
body or hidden behind the rail. The posture problem that has blocked this
project since day one is unchanged in the new material.

### The web view is now the bottleneck, not a workaround
Scraping a virtualised Google Photos grid was fine at 30 photos and is not fine
at 74. Two hard limits hit today:

1. **Enumeration is unreliable.** 74 photo links but only 48 renditions
   recoverable; tiles load on dwell, the pane stalls, and there is no way to
   verify completeness from inside the page.
2. **The renditions carry no EXIF at all.** No capture date, no camera, no GPS.
   That was tolerable for a four-week album where every frame was obviously
   recent. **It is not tolerable for a year-spanning album**, where the date is
   what tells us which season, which molt window, and — critically — which
   frames are the suspected out-of-state trip.

**Recommendation, and it is the same unblock as before:** put the originals in
`My Drive/birds/…`. Drive is mounted locally, so intake reads them off the mount
with EXIF intact in one pass — full enumeration, real dates, GPS sorted into the
gitignored sidecar, and the out-of-state frames separated by coordinates rather
than by guessing at habitat. Everything downstream of that is blocked until it
happens.

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

## 2026-08-10 — CURATOR RULING: no ID counted without a photo of a readable band

David, after the contradictions in the entry above: **he will not count an
individual identification until there is a photograph of a band.** That is
`confirmed` on the ladder in [`docs/id_method.md`](docs/id_method.md), applied
strictly, and it is now the project's standing rule.

**What changed in the data:**
- `nashua-01`'s Amos linkage → **not counted**. Its `sex` drops from *male* to
  *disputed*, and the "hatched 2017, Brady Sullivan, nine years old" chain goes
  with it, because that chain assumes a male.
- The Feb 2026 band frame (`20260804-f3001faa`) is **unassigned from any
  individual**. It proves a banded adult exists; it identifies nobody.
- Sighting `20260730-01` no longer names a bird.

**Why the ruling is right and not just conservative.** Two of three first-hand
accounts on 2026-08-10 called the banded bird *female*; on 2026-07-23 the same
people were unanimous it was the *male*. The Amos identification needs a male.
So the identity was resting on a sex call that has since inverted, on top of a
code nobody ever read. Stripping it costs nothing real — no sighting, date, site
or behaviour is lost, only an unearned name.

**The measurement behind "get a photo of a band".** On the weathervane frame the
bare tarsus spans **37 px**. A band there would be ~12 px — a hard tonal break,
reliably detectable, which is why `band_visible=no` is trustworthy. Its
characters would be ~4 px, which is noise. Presence/absence yes, code no, **short
by about 3.6×**.

That number is the actionable part: the frame is a PDF extraction at 1083×722,
while the photographer shot it on a 33 MP body — roughly 5–6× larger linearly.
**On a banded bird framed that way, the original may already carry a readable
code.** The ask stops being "better photos" and becomes *the full-resolution
original of any frame showing a banded bird's leg*.

**One for [`PLAYBOOK.md`](PLAYBOOK.md):** the curator reached the confidence
ladder independently, under pressure, without reference to the document that
defines it. That is the ladder earning its place rather than being imposed.

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

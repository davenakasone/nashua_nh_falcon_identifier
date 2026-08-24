# Can a Peregrine be identified as an individual from photos?

**Verdict: yes, but not by the method most people mean.** Bands and molt gaps
carry almost all of the signal. Plumage pattern-matching is a real but
secondary tier, useful for linking sightings, rarely sufficient alone. Generic
"AI image matching" does **not** work on this species and we are not going to
pretend otherwise (see [What does not work](#what-does-not-work)).

This document is the method the project is built around. Every sighting we log
gets a confidence tier from the ladder below, and the tier is set by which
traits were actually visible in the photo — never by how sure the observer felt.

---

## The trait ladder, ranked by how much identity each one carries

### 1. Band / ring code — *decisive*
The gold standard, and the reason "get the legs" is the first rule of the photo
protocol. Northeastern peregrines are banded as nestlings by state wildlife
programs (in New Hampshire, NH Audubon's peregrine project with NH Fish &
Game). The standard rig is a numbered USFWS aluminum band on one leg and a
**bi-colour, field-readable alphanumeric band** on the other — black-over-green
is the eastern US colour combination. Codes read like `48/BD` or `*7/*Z`.

- A legible code is an absolute identity, and it can be traced to hatch year
  and **natal site** through the banding coordinator or the USGS Bird Banding Lab.
- **Natal site is not breeding site, and the slip is easy to make.** A band tells
  you where a bird *hatched*. Peregrines disperse — New England natal dispersal
  averages 88 km for males and 153 km — so a banded adult holding a territory
  was very likely banded somewhere else entirely. "It's banded, so the banders
  know where it nests" does not follow. What the banding programme knows is the
  *natal* eyrie; what it may separately know, as a monitoring programme, is
  whether *this* site is an active eyrie. Those are two different questions and
  only the second one finds your nest.
- **Which leg is standardised, and knowing it changes where you stand.** In the
  eastern and midwestern programmes the silver federal band goes on the **right**
  leg and the field-readable bi-colour on the **left**. So a photo of the right
  leg can never carry a code, however sharp it is.
- **The bi-colour band is readable on a perched bird with a spotting scope at up
  to roughly 700 ft.** The federal band is not readable in the field at any
  distance — its 9-digit inscription needs the bird in the hand. Stop chasing it.
- Colour narrows origin but does not pin it: black-over-green is used by the
  **midwestern** programme too, and the east used black-over-red from 1989–2004.
- Limitation: plenty of adults are unbanded. An unbanded bird is not "a new
  bird" — it is a bird whose identity must come from the tiers below.

### 2. Molt gaps — *strong, but perishable*
Adults run a complete flight-feather molt roughly March–October (females
typically start during incubation). At any given moment a bird is missing or
regrowing a specific set of primaries (P1–P10), secondaries, and tail feathers
(R1–R6). Photographed from below with the wing and tail spread, those gaps are
countable. The combination is often distinctive within a season — but molt runs
a **stereotyped sequence** (starting around P4 and S5, spreading in both
directions, finishing P10/S1 in autumn), so two birds of the same age and sex on
the same date can genuinely look alike. Treat a molt match as supporting
evidence, not as decisive.

- This is the workhorse for *"was Tuesday's bird also Thursday's bird?"*
- It expires. A gap pattern links sightings **within a molt window of a few
  weeks**, not across seasons. Never carry a molt match across a year boundary.
- Record it as a feather map (`R3 missing, P7 half-grown`), not as prose.

### 3. Malar stripe geometry — *moderate, stable*
The dark cheek wedge below the eye. Individuals differ in its width, how far it
extends down the throat, and the shape of the pale cheek patch behind it.

It is widely *asserted* to be stable across years — agency and outreach pages
call it fingerprint-like — but **this project could find no study demonstrating
inter-annual persistence in individually-known birds**, and the malar region is
feathered and replaced at every molt. Treat multi-year malar stability as an
assumption being tested here, not a fact the project rests on. It is still the
best candidate for long-term identity in an unbanded bird, but it demands a
clean near-profile head shot and it lies to you at bad angles and in harsh light.

### 4. Underpart barring — *moderate, resets at molt*
Fine horizontal barring on breast, belly and flanks. What varies between birds
is the density of barring, how far it pushes up onto the upper breast, and how
much clean unmarked bib is left. Useful, but the pattern changes when the body
feathers are replaced, so treat it as within-season evidence.

### 5. Hood and nape — *weak to moderate*
How far the dark hood runs onto the nape, and the size and placement of pale
nape spots.

### 6. Size and sex — *classifies, does not identify*
Reverse sexual dimorphism is strong in this species: females are roughly 15–20%
larger linearly and substantially heavier. When the pair is in the same frame
the larger bird is the female. This reliably separates *the male from the
female* — it can never separate one female from another female.

### 7. Age class — *classifies, and settles the juvenile question instantly*
- **Juvenile / hatch-year:** brown above with buff feather edging, **vertical**
  streaking on buff underparts, bluish cere and orbital ring. Legs and feet
  start **blue-grey to greenish** and turn yellow over the first winter.
  **Do not use leg colour as an age cue after midsummer.** A literature-sourced
  edit on 2026-08-04 said juvenile legs are blue-grey "and emphatically not the
  adult's bright yellow" — then a photograph taken that same week showed this
  year's Nashua juvenile, ~8 weeks post-fledge, with plainly **yellow** feet.
  The transition starts earlier than the tidy version implies. **Streaking
  direction is the age cue that holds**: vertical on a juvenile, horizontal on
  an adult, all year.
- **Adult:** slate blue-grey above, **horizontal** barring below, yellow cere,
  orbital ring and legs.

A brown, vertically-streaked bird in the Nashua area in late summer is the
year's juvenile, not one of the breeding pair. This single distinction does a
lot of work for us and needs only a mediocre photo.

### 8. Behaviour and territory — *circumstantial*
Habitual perches, hunting routes, who tolerates whom. It constrains the
candidate set; it never closes an ID on its own.

### 9. Injuries and deformities — *decisive when present, rare*
A missing toe, a chipped bill, a persistently damaged feather. If we ever find
one, it outranks everything except a band read.

---

## The contamination problem — read this before scoring any trait

**AI "enhance" and upscaling destroy the exact signal this method depends on.**

Learned the hard way on 2026-08-04. Two groups of photos in the group's album
looked like two different birds: one warm and buff with discrete round breast
spots, the other cool grey with fine even barring. It was a clean, convincing
split — and it evaporated the moment the photographer mentioned that some frames
had been cropped and AI-enhanced and others hadn't.

Enhancers do three things, and every one of them lands on a trait in the ladder
above:

- **warm and saturate the tone** → destroys colour-wash comparison
- **smooth noise into waxy texture** → destroys fine barring
- **harden soft markings into discrete blobs** → turns bars into spots

So an enhanced frame of one bird can look like a different individual from an
untouched frame of the same bird. The signal and the artefact are the same shape.

**Nothing in the file tells you which happened.** EXIF does not record it, and a
re-saved JPEG looks like any other JPEG. It has to be *asked*, which is why
`processing` is a column in `data/photos.csv` and why the vocabulary is
`out-of-camera` / `cropped` / `ai-enhanced` / `screenshot`.

**The rule that follows: score traits on `out-of-camera` frames only.** Enhanced
frames are still useful — for age class, for band presence, for behaviour, for
perch, for "there was a falcon here on this date." They are not admissible for
plumage comparison, ever.

Corollary for the photo protocol: **ask contributors for originals, and ask them
explicitly whether they enhanced anything.** Most people do not think of a
denoise-and-sharpen pass as altering the evidence, because for every other
purpose they have, it isn't.

### Phone RAW is NOT automatically better than the phone JPEG

Tested 2026-08-23 and the result was the opposite of the assumption. A Pixel 10
Pro writes a **50 MP JPEG (6144x8160)** and a **~8.8 MP DNG (2572x3414)** for the
same shutter press — the RAW is the *binned* sensor readout, while the JPEG comes
off the full-resolution path. **The JPEG has 2.4x the linear resolution**, and on
a side-by-side crop of the same band the DNG is visibly softer and mushier.

RAW still wins on bit depth and freedom from compression artefacts. But for
**reading fine engraving, spatial resolution is the binding constraint**, and on
a modern computational-photography phone the JPEG has more of it.

Do not spend a contributor's effort chasing DNGs on a phone without testing one
first. On a dedicated camera, where the RAW is the full sensor, the usual
assumption holds and RAW is the file to ask for.

## What does not work

**Off-the-shelf image similarity will not identify these birds.** Perceptual
hashes and generic embedding models cluster photos by background, pose, and
lighting — you will get "all the shots against the sky" and "all the shots on
the brick ledge," not "all the shots of the female."

The wildlife re-identification systems that genuinely work — Wildbook on whale
sharks, HotSpotter on zebra and giraffe — succeed because those animals wear
high-contrast, near-planar patterns that can be photographed from a repeatable
angle. A peregrine's barring is low-contrast, on a curved and deformable
surface, and it changes at every molt.

**But "nobody has ever done this for a raptor" would be wrong, and this document
said something close to it until 2026-08-04.** Two things exist that a
technically literate reader will know about:

- **MiewID** (Wild Me's own multi-species re-ID model, ~49–64 species and
  ~225k photos) is explicitly built for zero-shot transfer to species it was
  never trained on. That is a trained model available to borrow.
- **Individual ID of a wild raptor by deep learning is published** — white-tailed
  eagle, *Ecological Informatics*, 2025: detection plus a classifier that
  suppresses background and weights head and facial features. That is the
  machine analogue of the malar-stripe tier above.

So the honest statement is narrower than "impossible": *off-the-shelf* embeddings
and perceptual hashes will not work here, purpose-trained raptor re-ID demonstrably
can, and **Wildbook's MiewID is the thing to try before building anything**. What
neither removes is the prerequisite — a labelled corpus of known individuals,
which this project does not yet have. That is a reason to defer the tool, not a
reason to call it out of reach.

So the honest machine role here is **normalisation and retrieval assist, never
a verdict**: standardise crops (head profile, breast, spread wing) so a human
compares like with like, and rank candidate matches for that human to judge.
The tool narrows the pile. The observer makes the call.

---

## Confidence ladder — every sighting gets one of these

| Tier | What it takes |
|---|---|
| **confirmed** | Band code legible in the photo. Nothing else earns this word. |
| **probable** | Two or more independent stable traits match with no contradicting trait — or a molt-gap match inside the same molt window. |
| **possible** | One trait matches, and territory/behaviour is consistent. |
| **unknown** | Everything else. This is the default and it is not a failure. |

House rule, inherited from `DOCTRINE.md`: **if in doubt, leave it out.** A
catalogue padded with hopeful IDs is a broken scoreboard. `unknown` costs us
nothing; a wrong `confirmed` poisons every record downstream of it.

---

## Photo protocol for the group

**Project rule, set 2026-08-04: no AI enhancement on Nashua falcon photos.**
Crop if you like — cropping only discards pixels. Do not run "enhance",
denoise, or upscale on anything that might be used for identification. If a
frame has already been enhanced, say so at hand-over; it stays useful for age,
band presence, behaviour and date, just not for plumage.

**Where to stand.** Two settings have been shown to expose the tarsus, which
almost nothing else does: the **radio-tower crossbar** (the bird perches high on
the bar with its legs clear of the belly rather than crouched on a slope) and a
bird **down on the ground with prey** (eye level, stationary, preoccupied). Both
beat the ledge and bracket perches, where the tarsus is buried every time.

Ordered by how much the shot is worth, not by how easy it is:

1. **The legs.** A perched bird, both legs visible, sharp. Preening and
   ledge-loafing birds expose bands. One good leg shot can end the entire
   identification problem for that bird.
2. **Spread wing and tail from below.** The molt fingerprint. Worth taking even
   when the bird is far away and the shot is "bad" — countable gaps survive a
   soft image.
3. **Clean head profile.** For the malar stripe. Square to the bird's head, not
   three-quarters.
4. **Square-on frontal.** For the breast barring.
5. **Anything showing two birds together.** Size comparison is only available
   in-frame.

Handling rules that matter as much as the shots:

- **Shoot bursts.** The intake tool detects burst frames and keeps them all;
  redundant frames are cheap and one of them is sharper than the rest.
- **Send originals, not screenshots.** A screenshot or a re-saved crop destroys
  the EXIF timestamp, and the timestamp is what makes molt-window logic
  possible. Texting a photo often strips metadata too — prefer AirDrop, a
  shared album, or email with "actual size".
- **Do not pre-cull.** A photo too poor to enjoy may still be the one that shows
  a leg band or a missing primary.

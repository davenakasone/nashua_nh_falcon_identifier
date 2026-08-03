# Playbook — running a small-group wildlife individual-ID project

This repo is a worked example: a handful of people in Nashua, New Hampshire
trying to tell three Peregrine Falcons apart and find their nest. **This file is
the transferable part** — how to start one of these for a different species,
what order to do things in, and the specific ways it goes wrong.

It is written to be handed to a person or an agent starting cold. Everything
here was learned by getting it wrong first; the mistakes are kept in on purpose,
because the mistakes are the content. A clean method document would teach you
nothing.

**Read this before writing any code.** The most common failure is building a
comparison tool before there are photographs to compare.

---

## 1. Is your species a candidate at all?

Answer honestly before anything else, because for many species the answer is no
and finding that out in week three is expensive.

**Individual ID from photographs works when at least one of these holds:**

| | |
|---|---|
| **Marked animals** | Bands, rings, tags, collars, notches. If a marking scheme exists, identity is a *lookup*, and everything below is a fallback. This is the single biggest factor. |
| **High-contrast, near-planar patterns** | Zebra stripes, whale-shark spots, giraffe reticulation, humpback flukes. Repeatable angle, hard edges. This is where machine matching genuinely works — Wildbook and HotSpotter live here. |
| **Small, bounded population** | Three birds on one territory is tractable. Two hundred at a staging site is not, without a very different machine. |
| **Site fidelity** | The same animals returning to the same structures gives you repeat views from a repeatable angle, which is what comparison needs. |

**It works badly when the marks are low-contrast, on a curved deformable
surface, and change seasonally.** That is the peregrine case, and it is why this
project's verdict was that generic AI image matching does not work on it —
off-the-shelf embeddings cluster by background and pose, not by individual.

**A caution that cost this project a day:** do not carry one species' verdict to
the next. Snowy Owl barring is high-contrast dark-on-white on a relatively flat
surface — closer to the conditions where matching *does* work. Re-run the screen
per species; do not inherit the answer.

**Also screen for disclosure risk now, not later.** Nest sites, roosts and
wintering sites for sensitive species are the kind of information that cannot be
un-published. See §7.

---

## 2. Order of operations

The order matters more than any individual step.

### Step 0 — find the expert node. Do this first.

Somebody already studies this population. A state wildlife agency, an Audubon
chapter, a banding coordinator, a university lab, a species-specific project.

In this project the single most valuable piece of information — that the male is
banded, that his code resolves to a bird hatched at a known tower in a known
year — arrived in a forwarded email from a monitoring biologist who was *already
on a thread the group was already on*. No amount of tooling would have produced
it. It was a lookup that existed on somebody else's desk.

**Before you build anything, find out what is already known.** You will usually
discover that half your hard problem is somebody's routine record-keeping.

### Step 1 — inventory what the group already has

Not what they will collect. What is already sitting in Lightroom catalogues,
shared albums, phones, and a drive in a closet. Multi-year continuity is the
hardest thing to obtain and the cheapest thing to ask for, because it already
exists.

### Step 2 — write the method document before the tooling

What separates individual A from individual B *for this species*, ranked by how
much identity each trait actually carries, with the failure mode of each stated.
See [`docs/id_method.md`](docs/id_method.md) for the peregrine version.

Writing this first tells you what the photographs need to show, which turns a
vague "send me falcon pictures" into a specific and achievable request.

### Step 3 — intake, then a catalogue

Get photographs into a stable, de-duplicated, hashed record. Nothing else can
start until this exists. `photo_intake/` in this repo drops into a new project
essentially unchanged.

### Step 4 — only now, comparison tooling

**Do not build the comparison tool before the photographs exist.** You will
guess wrong about the input. In this project the compare tool was deliberately
deferred, and that was correct: the first real photo drop revealed that the
limiting factor was posture — birds crouching with their legs hidden — which no
comparison algorithm addresses.

---

## 3. Governance: open on input, curated on assertion

The dichotomy people reach for — "take their photos and let nobody touch
anything" versus "open collaboration" — is the wrong axis. Every project that
works in this space splits it the same way, and it is not a compromise:

- **Anyone may contribute an observation.** Photographs, dates, places. Zero
  friction, no accounts, no naming conventions, no folder discipline.
- **Only a curator may assert an identity.** "This is individual 01." "These two
  sightings are the same animal." "This code reads 53/BS."

The reason is failure economics, not politics. **A bad photograph costs
storage. A bad identity claim is multiplicative and silent** — it propagates
into every downstream conclusion and never announces itself.

Wildbook, iNaturalist and eBird all converged on this independently. If your
project is on GitHub you get it for free: read-only to the world, pull requests
for anyone who wants to correct a row.

**Do not make contributors use your tools.** They will not converge on your
storage — a real contributor list from this project spans Flickr, Google Photos,
Apple Photos, Amazon Photos, and a Drive full of RAWs. Meet them where they are;
the friction you add at the contribution step costs you contributions and buys
nothing.

---

## 4. Architecture: own the catalogue, not the storage

Four layers, one direction of flow:

```
polymorphic inbox  →  private master  →  committed catalogue  →  public mirror
(whatever they          (yours,           (CSV, the durable      (derived,
 already use)            originals)        record)                regenerable)
```

**The catalogue row is the durable artifact, not the photograph.** Every row
carries a content hash, a perceptual hash, dimensions and a timestamp, so:

- losing an original costs the pixels but not the observation;
- a copy resurfacing years later matches back to its row;
- originals can live in cold storage you do not control, and someone deleting
  the lot is a recoverable event rather than a catastrophe.

That last property is what makes the whole thing robust. Permissions protect
availability; the catalogue protects the record.

**CSV over anything cleverer.** Non-technical collaborators can read it, GitHub
renders it as a sortable table, and a diff is legible in a commit. Flat columns,
`;` for multi-value cells. Quote everything — free text in a notes column is how
a CSV database usually dies, so there is a test for it.

**Decide the id scheme and the confidence vocabulary while the file has zero
rows.** Adding a column later is free. Renaming one, or changing what `probable`
means, is not.

---

## 5. Identity records

**Slugs are permanent opaque numbers, never roles.** `nashua-01`, not
`nashua-female`. A territory turns over and a replacement silently inherits its
predecessor's entire history if you keyed the record on the role. Keep an
`alias` for what people actually call the animal, and a **dated** `roles`
timeline for the position it holds.

Merging two slugs that turn out to be one animal is easy — merge forward into
the lower number, leave a tombstone. Splitting one slug that turned out to be
two animals is very hard. Bias toward opening a new slug.

**A file may exist as a hypothesis.** Mark it, and state what evidence would
establish it and what would kill it.

**Confidence ladder** — every sighting gets exactly one:

| Tier | What it takes |
|---|---|
| **confirmed** | A read marking. Nothing else earns the word. |
| **probable** | Two or more independent stable traits agree, no contradicting trait. |
| **possible** | One trait, plus consistent territory or behaviour. |
| **unknown** | Everything else. The default, and not a failure. |

Keep separate claims separate. *This animal is marked* and *this animal is
individual X* are different assertions with different evidence, and collapsing
them is how a guess becomes a fact.

---

## 6. Contamination — the section that earns this document

Three vectors surfaced in a single day, on thirty photographs of three birds.
They do not get rarer at scale. Anyone building a product here will treat these
as data-quality cleanup; they are the core problem.

### Enhanced images
**AI "enhance", denoise and upscaling destroy exactly the signal trait
comparison depends on.** They warm tone, smooth feather or fur texture into wax,
and harden soft markings into discrete blobs.

In this project two groups of photographs looked convincingly like two different
individuals — one warm and buff with round spots, one cool grey with fine
barring. It was a clean split. It evaporated when the photographer mentioned
some frames were enhanced and others were not. **The artefact has the same shape
as the signal.**

Nothing in the file records it. EXIF does not carry it; a re-saved JPEG looks
like any other JPEG. **It has to be asked.** Hence a `processing` column
(`out-of-camera` / `cropped` / `ai-enhanced` / `screenshot`) and a hard rule:
score traits on out-of-camera frames only. Enhanced frames stay useful for age
class, marking presence, behaviour, location and date.

Set the no-enhancement rule with contributors on day one. Most people do not
think a denoise pass alters evidence, because for every other purpose they have,
it doesn't.

### Wrong provenance
A shared album labelled for one site will contain photographs from somewhere
else. In this project a trip to another state got mixed in — and a marsh-habitat
frame that had already been logged as the project's best evidence turned out to
be a candidate for an out-of-state bird.

**Habitat and structures look alike; coordinates do not.** Photo GPS is the only
thing that partitions a mixed album without judgement calls, which is one of
several reasons to insist on originals rather than web-view copies.

### Absence mistaken for evidence
"No juvenile in twenty-five photographs" was logged as evidence against a
juvenile existing. It was being photographed inside that exact window by a
different observer at a different site. **Absence from one contributor's set is
not absence in the field.**

The same error in miniature, and the more insidious one: recording "no marking
seen" on frames that never showed the leg. That manufactures evidence for an
unmarked animal out of photographs that never asked the question. Hence
`not-tested` as a distinct value from `no` — the single most useful column in
this project.

### And a fourth: claims harden as they travel
A biologist wrote that she was "putting bets" on a code, could "sort of" make
out two digits and a "very blurry" letter. Within a week the group was using
that code as the bird's settled name. She hedged correctly; the hedge did not
survive being forwarded.

**Record the hedge with the claim, in the same field.** By the time it reaches
you third-hand it will be gone.

---

## 7. Privacy and disclosure

**Everything else is recoverable; disclosure is not.** Deleted files come back
from a master copy. A published nest location does not come back.

- **Place names in committed files, never coordinates.** Precise GPS goes to a
  gitignored sidecar. The public row records only whether a photo had GPS.
- **Steal iNaturalist's geoprivacy model** rather than inventing one: publish a
  coarse cell (they use 0.2° for at-risk taxa), keep true coordinates private,
  grant access by explicit trust. A coarse cell beats a vague place name because
  it is machine-usable *and* honestly labelled as degraded.
- **Use the Darwin Core terms** `informationWithheld`, `dataGeneralizations`,
  `coordinatePrecision`. Free to adopt now, and the catalogue then exports to
  GBIF or a state agency later without a migration.
- **Third parties in source material.** Email threads carry other people's
  addresses, phone numbers, medical details, home addresses. They did not agree
  to be in a public repo. Facts and attributions go in; bodies stay out.
- **Share links are bearer credentials.** A shared-album URL grants access to
  anyone holding it and cannot be revoked for one person. It is not a location
  reference; it is a key.
- **Check what "shared" actually means before pushing.** A repo can be public
  while its owner believes it is group-only. Verify, do not assume.

---

## 8. Scale — where it breaks next

The bottleneck moves, and knowing where it goes next is worth more than
optimising where it is.

- **Small project** (a few individuals, a few contributors): the bottleneck is
  *getting photographs at all*. Solve it socially, not technically.
- **Working project**: the bottleneck becomes the **curator's labelling
  throughput** — one person hand-filling columns for every frame. This arrives
  sooner than expected and is where tooling effort belongs.
- **Popular species**: hundreds of contributors, dozens of individuals. Curation
  throughput fails outright. That needs consensus mechanisms, redundant
  annotation and machine pre-filtering — a different machine, not a bigger CSV.

A wintering owl site can be dozens of birds and hundreds of photographers.
Solve curation throughput *before* adding that species, not during.

---

## 9. What not to build

- **A comparison tool before photographs exist.** You will guess the input wrong.
- **A second contribution channel** when one already works. If they are using a
  shared album, that is the inbox. Adding a "proper" one costs contributions.
- **A competitor to Wildbook.** It is open source, handles the individual-identity
  layer, and already runs the governance model above across 250+ species. If the
  species fits it, contribute there.
- **An "eBird add-on."** eBird deliberately has no individual-identity layer, and
  the reason is structural rather than technical. The niche neither eBird nor
  Wildbook serves is *small groups, few individuals, high curation, local
  stewardship* — which is this.
- **Networking inside each tool.** Per `../RULES.md`, a tool owns its HTTP or
  does none. Compose; do not import across tools.

---

## 10. If you are an agent picking this up cold

1. Read the project's `CLAUDE.md` `## STATUS` block first. It is the resume
   point and it is kept current deliberately.
2. Read `docs/id_method.md` for the worked species example, and §6 above before
   trusting any photograph.
3. `photo_intake/` is species-agnostic and drops into a new project unchanged.
   The bird-specific columns are `band_visible` and `band_code`; rename them for
   a different marking scheme and leave the rest.
4. `nest_map.py` is the mapping example — offline, keyless, reads coordinates
   from the gitignored sidecar and writes to a gitignored output.
5. **Record what you get wrong, in place, rather than editing it away.** Three of
   this project's most useful rules exist because a conclusion was published and
   then overturned within hours. A corrections trail is worth more than a clean
   document.
6. Do not assert an identity. Rank candidates, normalise crops, surface the
   evidence — and leave the call to a human. That boundary is the method.

# Individuals — the identity schema

One file per bird: `nashua-<nn>.md`. Fill it from photos and field notes; every
claim in it cites the photo ids that support it.

## Why the slugs are numbers and not names

A slug identifies **a bird**, permanently. It is deliberately not a role.
"The Nashua female" is a *position at a site* — territories turn over, and a
replacement female would silently inherit every record of her predecessor if we
keyed the catalogue on the role. So:

- `nashua-01`, `nashua-02`, … — permanent, opaque, never reused, never renamed.
- `alias` — whatever the group actually calls the bird in conversation.
- `roles` — a dated timeline (`2026: breeding female`). This is where turnover
  gets recorded, and it is allowed to change.

If two slugs later turn out to be the same bird, **merge forward into the lower
number** and leave a tombstone in the higher one. Never delete a slug.

## Template

```markdown
# nashua-NN

- **alias:** —
- **status:** hypothesis | established
- **first recorded:** YYYY-MM-DD (photo id)
- **last recorded:** YYYY-MM-DD (photo id)
- **sex:** female | male | unknown (basis: size-in-frame with X / behaviour / unknown)
- **age class:** adult | juvenile YYYY | unknown
- **roles:** 2026 — breeding female at <site>

## Bands
- **banded:** yes | no | unknown
- **code:** — (which leg, colour combination)
- **read from:** photo id, date
- **traced:** natal site / hatch year, source

## Stable traits
- **malar stripe:** —
- **hood / nape:** —
- **underpart barring:** —
- **injuries or deformities:** —

## Molt log
| date | window | gaps observed | photo ids |
|---|---|---|---|

## Confidence
Current tier for this individual's identity: **confirmed | probable | possible |
unknown** — the four tiers from `docs/id_method.md`, and only those. `hypothesis`
and `established` are `status:` values describing the *file*; they are not
confidence tiers and must not be used here. State what would raise the tier, and
what would break it.

## Photos
Catalog ids assigned to this bird. Keep this in sync with the `individual`
field in `data/photos.csv`.

## Notes
```

## Rules

1. **A file may be created as a hypothesis.** "There is a second adult here"
   is a legitimate starting state. Mark it `status: hypothesis` and say what
   evidence would establish or kill it.
2. **Every trait line cites photo ids.** A trait with no photo behind it is a
   memory, and memories merge birds.
3. **Contradicting evidence gets written down, not dropped.** If a later photo
   disagrees with a recorded trait, add it and lower the tier.
4. **Confidence tiers come from `docs/id_method.md`.** Nothing is `confirmed`
   without a legible band code.

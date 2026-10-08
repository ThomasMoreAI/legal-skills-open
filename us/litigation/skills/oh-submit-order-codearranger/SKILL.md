---
name: oh-submit-order-codearranger
title: Post-Hearing Order Submission — Ohio
description: Use after an Ohio hearing to transmit the signed proposed order. Triggers include 'Ohio post-hearing order', 'submit Ohio proposed order', 'Ohio judgment entry', 'Ohio order transmittal', 'Ohio Sup. R. order submission'. Covers post-hearing order submission to chambers, the file-stamp + Notice of Entry mechanics, and the 30-day App. R. 4(A) appeal clock that runs from file-stamp date.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-submit-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Post-Hearing Order Submission — Ohio

> **NOT LEGAL ADVICE.** The 30-day notice-of-appeal clock
> under App. R. 4(A) runs from the date the order is
> file-stamped. Submit and serve promptly.

## Workflow

### After the hearing

1. **Judge announces ruling** (orally or by minute entry)
2. **Prevailing party drafts proposed order** in Ohio
   format (see `oh-draft-order`)
3. **Tender to chambers** — by chambers email, working
   copy, or e-filed proposed order depending on per-court
   protocol
4. **Judge signs (or modifies + signs)** — sometimes
   immediately, sometimes within days
5. **Order file-stamped** with the court clerk
6. **File-stamped copy returned** to the parties

### Service obligation (Civ. R. 5)

Once the order is file-stamped, **the prevailing party
must serve the file-stamped order on every other party**
within a reasonable time and file a certificate of
service.

### App. R. 4(A) appeal clock

The 30-day clock to file a notice of appeal runs from the
**file-stamp date** on the order — not from the date of
oral ruling and not from the date of signing. This
distinction matters because the file-stamp can lag by
days or weeks after the judge's signature.

## Per-court chambers protocols

Each Common Pleas judge specifies how proposed orders are
tendered:

- **Word document via chambers email** — common for
  Cuyahoga, Franklin, and Hamilton Civil Divisions
- **E-filed proposed order** — increasingly common; some
  e-filing portals support a dedicated "Tendered Proposed
  Order" document code
- **Paper tender** — older courts still accept paper
  proposed orders walked into chambers

Always verify the assigned judge's chambers preferences
before submitting.

## Sup. R. 26 — record retention

Once a final judgment is file-stamped, Ohio Sup. R. 26
governs the clerk's retention of the record. The
prevailing party should retain its own copy (paper or
digital) of the file-stamped order indefinitely — it's
the operative judgment.

## Counter-orders and order modifications

If the opposing party objects to the proposed order or
believes it doesn't reflect the court's ruling:

- File a Motion for Reconsideration (limited grounds —
  Ohio does NOT have a Civ. R. 60(B) reconsideration
  before a final judgment) OR
- Tender a counter-order to chambers with a brief letter
  explaining the disagreement

The judge resolves the discrepancy in chambers.

## Notice of Entry

Some Ohio counties require a "Notice of Entry" filed by
the prevailing party after the file-stamp — verify per-
court Loc. R.

## Composition with other oh- skills

- `oh-draft-order` — tendered proposed-order scaffolder
- `oh-deadlines` — App. R. 4(A) 30-day appeal clock
- `oh-post-judgment` — Civ. R. 59 (28 days) + Civ. R. 60
  (1 year) post-judgment relief
- `oh-cuya` / `oh-frank` / etc. — chambers practice per
  court

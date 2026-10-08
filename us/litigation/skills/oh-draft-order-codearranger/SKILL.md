---
name: oh-draft-order-codearranger
title: Draft an Ohio Proposed Order
description: Use to draft an Ohio proposed order. Triggers include 'Ohio proposed order', 'Ohio order granting motion', 'Ohio tendered order', 'Ohio Sup. R. order format'. Produces an Ohio-format proposed order with caption, findings (if applicable), ORDERED clauses, signature line for the Judge, and a date line.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-draft-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Ohio Proposed Order

> **NOT LEGAL ADVICE.** Proposed orders are tendered with
> a motion; the judge edits and signs. The format below
> is the common-denominator Ohio practice — verify per-
> court chambers preferences.

## Standard form

```
IN THE COURT OF COMMON PLEAS OF [COUNTY], OHIO

[Plaintiff Name],
                            Plaintiff,
        vs.                          Case No. [CV-NNNNN]
                                      Judge: [Name]
[Defendant Name],
                            Defendant.

                            ORDER

This matter came before the Court on [Movant's]
Motion to [Relief], filed [Date]. The Court has reviewed
the Motion, the Memorandum in Support, [the Response of
the opposing party, if any,] the entire record, and the
applicable law.

THE COURT FINDS [optional, if findings of fact + law are
included]:

1. [Finding 1]
2. [Finding 2]

IT IS THEREFORE ORDERED that:

1. [Operative relief, e.g., "The Motion is GRANTED."]
2. [Specific consequences, e.g., "Defendant shall produce
   the requested documents within 14 days of this order."]
3. [Closing, e.g., "All other relief not specifically
   granted is denied."]

IT IS SO ORDERED.

DATE: ___________________

                            __________________________
                            Judge [Name]
                            Court of Common Pleas
```

## Drafting conventions

- **Caption + case number + assigned judge** at top
  (Civ. R. 10(A))
- **Recitation of procedural posture** in 1-2 paragraphs
  before findings/ordered clauses
- **FINDINGS** (optional, recommended for contested
  motions) — separately numbered factual findings the
  judge can adopt or modify
- **ORDERED clauses** — numbered, each stating one
  operative directive
- **Signature line + date** for the judge

## Specific motion-type variations

### Order granting motion to dismiss

- Findings: complaint fails to state a claim under
  Civ. R. 12(B)(6); plausibility-standard analysis
- Ordered: "Plaintiff's Complaint is hereby DISMISSED
  [with / without] prejudice."

### Order granting summary judgment

- Findings: no genuine issue of material fact; movant
  entitled to judgment as a matter of law
- Citation to *Dresher v. Burt* burden-shifting framework
- Ordered: "Summary judgment is GRANTED in favor of
  [moving party] and against [non-moving party] on [Count
  N]."

### Order granting motion to compel

- Findings: meet-and-confer occurred without resolution
- Ordered: production deadline + sanctions trigger if
  noncompliance + attorney's fees if appropriate

### Order vacating default judgment

- Findings: Civ. R. 60(B) three-part test satisfied
  (*GTE Automatic Electric*) — timely motion, meritorious
  defense, qualifying ground
- Ordered: default judgment vacated; case reopened on the
  merits; answer due within 14 days

## Submission to chambers

After the order is signed:

- File-stamped copy returned to the parties
- Service of the file-stamped order on every party
  (Civ. R. 5)
- 30-day appeal clock under App. R. 4(A) starts running
  from the date of file-stamp (not from signature)

## Composition with other oh- skills

- `oh-draft-motion` — the underlying motion the order
  grants / denies
- `oh-submit-order` — post-hearing transmittal mechanics
- `oh-deadlines` — 30-day appeal clock under App. R. 4(A)
- `oh-cuya` / `oh-frank` / etc. — chambers preferences

---
name: ga-draft-order-codearranger
title: Draft a Georgia Proposed Order
description: This skill should be used to scaffold a Georgia proposed order for a judge's signature. Triggers include "proposed order Georgia", "draft an order for the judge", "draft a Georgia proposed order", "proposed order granting motion to compel Georgia", "default judgment order Georgia", "draft an order on summary judgment Georgia". Produces a proposed order with the caption replicated, recitals and findings, numbered "IT IS HEREBY ORDERED" decretal paragraphs mirroring the relief sought in the underlying motion, and a judge-signature line; flags that the order takes effect only upon signature and entry by filing under O.C.G.A. § 9-11-58.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-draft-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Georgia Proposed Order

> **NOT LEGAL ADVICE.** This skill scaffolds a court document
> as a drafting aid. The user — not the skill — chooses the
> findings, the relief, and the form of the order. Only a
> judge signs an order; this skill prepares the proposed form
> for the judge's consideration. Verify every rule, deadline,
> and citation against current law before filing. Pair with
> substantive review by counsel where stakes warrant.

Use this skill in addition to `ga-statewide-format` when a motion or
stipulation calls for a **proposed order** the judge can sign. The
proposed order replicates the caption (O.C.G.A. § 9-11-10(a)), recites
the matter before the court, states the findings, and sets out the
decretal paragraphs. A judgment or order is effective only when it is
**signed by the judge and filed with the clerk** (entry by filing,
O.C.G.A. § 9-11-58).

## Cardinal rule — the proposed order mirrors the motion

The order's relief should **mirror exactly** the relief requested in
the motion. Two failure modes:

- **Over-reaching**: ordering something the motion did not request —
  judges strike or modify these.
- **Under-reaching**: omitting something the motion requested.

Cross-check the prayer for relief in the motion (`WHEREFORE…`) against
the order's decretal paragraphs (`IT IS HEREBY ORDERED…`) one item at a
time.

## Standard proposed-order structure

```
                [Caption — exactly matching the motion,
                 per O.C.G.A. § 9-11-10(a)]

           [DOCUMENT TITLE: ORDER ON DEFENDANT'S
              MOTION TO COMPEL DISCOVERY]

This matter comes before the Court on [Movant]'s [Motion Title] (the
"Motion"), filed [date]. The Court, having reviewed the Motion, any
response and reply, the supporting affidavits and exhibits, and the
record, FINDS as follows:

1. [Finding 1 — e.g., "Defendant timely served Plaintiff with its
   First Interrogatories and Requests for Production on [date]."]

2. [Finding 2 — e.g., "Plaintiff did not timely respond to
   Interrogatories Nos. 3, 5, and 7 or Requests for Production Nos. 2
   and 8 within the time allowed by O.C.G.A. § 9-11-33 and § 9-11-34."]

3. [Finding 3 — additional findings as needed.]

The Court CONCLUDES that good cause exists to grant the Motion.

IT IS HEREBY ORDERED that:

(a) [Movant]'s Motion to Compel Discovery is GRANTED.

(b) Plaintiff shall serve, within [14] days of entry of this Order,
    full and complete responses to Defendant's Interrogatories Nos. 3,
    5, and 7 and Requests for Production Nos. 2 and 8, without
    objection.

(c) [Additional decretal paragraphs as needed.]

SO ORDERED, this ___ day of __________, 20__.

                                        _____________________________
                                        Judge, [Superior / State] Court
                                        of [County] County
```

## Findings vs. ordering — keep them separate

Georgia judges expect a clear separation between **factual findings**
(numbered, neutrally stated) and the **decretal paragraphs** (the
lettered or numbered list of specific commands). Conflating the two
makes it harder for the judge to delete a finding without invalidating
a command.

## Default judgment order

For a default judgment, the proposed order should recite the predicate
findings:

```
This matter comes before the Court on Plaintiff's motion for default
judgment. The Court FINDS:

1. Defendant was served with the Summons and Complaint on [date] per
   the return of service filed [date].

2. Defendant failed to answer or otherwise respond within the time
   allowed by O.C.G.A. § 9-11-12(a), and the case is in default under
   O.C.G.A. § 9-11-55(a); the default was not opened.

3. Plaintiff is entitled to judgment in the amount of $______,
   consisting of [principal $____; interest $____; costs $____].

IT IS HEREBY ORDERED that judgment is entered in favor of Plaintiff
and against Defendant in the amount of $______.
```

## Entry, signature, and effect — O.C.G.A. § 9-11-58

- **Only a judge signs and enters an order.** The filer submits the
  order in proposed form; the judge fills any remaining blanks, may
  strike portions the Court declines to grant, signs, and the clerk
  files it.
- A judgment is effective only upon signing by the judge and **entry by
  filing** with the clerk (O.C.G.A. § 9-11-58). Deadlines that run from
  "entry of judgment" run from that filing date, not the date the
  proposed order was submitted.
- The signature line should name the court and county:
  `Judge, [Superior / State] Court of [County] County`.

## Filing checklist

- [ ] Caption replicates the motion's caption exactly
- [ ] Findings are numbered, neutral, and separate from the decretal paragraphs
- [ ] Decretal paragraphs mirror the motion's prayer item-by-item
- [ ] Signature line names the court and county; dated blank left for the judge
- [ ] No relief beyond what the motion requested
- [ ] Format check passes (`scripts/format-check.py`)

## Composition

- For format: `ga-statewide-format`
- For the supporting motion: `ga-draft-motion`
- For the supporting affidavit: `ga-draft-declaration`
- For the post-hearing signed-order workflow: `ga-submit-order`
- For the venue overlay: `ga-fulton`, `ga-cobb`, `ga-gwinnett`,
  `ga-state-court`, `ga-magistrate`, `ga-county-courts`,
  `ga-family-court`
- For post-judgment specifics: `ga-post-judgment`
- For family-law decrees: `ga-family-law`
- For pre-filing QC: `ga-quality-check`, `ga-fact-check`

## References

- `references/proposed-order-template.md` — annotated template
- `references/default-judgment-order.md` — default-judgment findings variant
- `references/findings-vs-order.md` — separation conventions

---
name: tx-draft-order-codearranger
title: Draft a Texas Proposed Order
description: This skill should be used to scaffold a Texas proposed order or proposed judgment for a judge's signature. Triggers include "draft a Texas proposed order", "proposed order Texas", "order granting my motion Texas", "proposed judgment Texas", "default judgment order Texas", "order on motion for summary judgment Texas", "form of order for the judge to sign". Produces a proposed order or proposed judgment with the caption replicated, recitals, a decretal "IT IS ORDERED" / "IT IS ORDERED, ADJUDGED, AND DECREED" block, the judge's signature/date block at the foot, and a "submitted by" / "approved as to form" line for the parties. Only a judge signs; this skill prepares the proposed form for the court's consideration. Composes with `tx-statewide-format` for the caption and `tx-submit-order` for the transmittal workflow.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-draft-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Texas Proposed Order

> **NOT LEGAL ADVICE.** This skill scaffolds a proposed order or
> judgment as a drafting aid. The filer is responsible for ensuring
> the form mirrors the relief the court actually granted and contains
> nothing the court did not rule on. **Only a judge signs an order or
> judgment** — this skill prepares the proposed form for the court's
> consideration; the filer submits it but does not sign in the
> judge's place. Verify the current rules and local practice before
> submitting.

Use this skill in addition to `tx-statewide-format` when a motion,
stipulation, or hearing outcome requires a **proposed order** or
**proposed judgment** for the judge's signature. In Texas, the party
prepares the proposed form and **tenders** it; the **judge signs it**.
The **date the judgment is signed** — not the date of the hearing —
starts the post-judgment and appeal clocks (the trial court's
**plenary power** runs from the date the judgment is signed, ordinarily
30 days, extended by a timely motion for new trial or motion to modify
under Tex. R. Civ. P. 329b). Confirm the current day counts in
`tx-law-references`; this skill points at the corpus rather than
hard-coding them.

## Cardinal rule — the form mirrors the ruling

The proposed form's relief should **mirror exactly** what the court
ordered. Two failure modes:

- **Over-reaching**: decreeing relief the court did not grant — the
  court strikes or modifies it.
- **Under-reaching**: omitting relief the court actually granted —
  leaves the form incomplete and may require a corrective order.

Cross-check the relief requested in the motion (the PRAYER) against
the decretal block (`IT IS ORDERED ...`) one item at a time.

## Order vs. Judgment

Keep the two document types distinct:

- Draft an **Order** to dispose of a motion (e.g., "Order Granting
  Defendant's Motion for Summary Judgment"). An order may recite the
  matters the court considered.
- Draft a **Judgment** when the matter is finally resolved — the
  document the appeal and post-judgment clocks run from. A **final
  judgment** disposes of all parties and all claims; if it does not,
  it is interlocutory and generally not appealable (subject to the
  statutory exceptions for interlocutory appeals — confirm in
  `tx-law-references`). A final judgment should be clear that it is
  final; a "Mother Hubbard" / finality recital may be used where
  appropriate (confirm the current finality-language standard).

## Recitals vs. decretal language — keep them separate

Keep the **recitals** (the preamble: "On [date], the Court considered
[Movant]'s Motion ... and, having considered the motion, the response,
the evidence, and the argument of counsel, is of the opinion that the
motion should be GRANTED") separate from the **decretal clause** (the
operative commands following "IT IS ORDERED"). Do not bury operative
relief inside the recitals.

## Standard proposed-Order structure

```
                [Caption — exactly matching the motion;
                 see tx-statewide-format. Include the cause
                 number and the court.]

           [DOCUMENT TITLE: ORDER GRANTING
              DEFENDANT'S MOTION TO DISMISS]

On this day the Court considered [Moving Party's Motion Title], filed
[date]. Having considered the motion, any response and reply, the
supporting affidavits/declarations and exhibits, and the argument of
the parties, the Court is of the opinion that the motion is well
taken and should be GRANTED.

IT IS THEREFORE ORDERED that:

1. [Defendant's Motion to Dismiss is GRANTED / DENIED.]

2. [Specific consequential relief, e.g., "Plaintiff's claims against
   Defendant are dismissed with prejudice."]

3. [Costs — taxed to ____, or "each party shall bear its own costs."]

SIGNED this ___ day of __________, 20__.


                                        ____________________________
                                        JUDGE PRESIDING

[Submitted by:]
[Name / "Self-Represented" or State Bar No. ___]
[Address / Phone / Email]
```

## Standard final-Judgment structure

A final judgment disposes of all parties and all claims and states
the relief operatively:

```
                [Caption — see tx-statewide-format]

                       FINAL JUDGMENT

On [date], this cause came to be heard. [Recital of appearance /
default / trial as applicable.] The Court, having considered the
pleadings, the evidence, and the argument of the parties, renders
the following judgment:

IT IS ORDERED, ADJUDGED, AND DECREED that [Plaintiff] recover from
[Defendant] the sum of $______, consisting of:
   a. Principal: $______
   b. Pre-judgment interest: $______ (state the rate and basis)
   c. Post-judgment interest at the applicable statutory rate
   d. Court costs
   e. Attorney's fees as awarded

[Finality recital, where appropriate: "This judgment is final,
disposes of all claims and all parties, and is appealable. All
relief not expressly granted is denied."]

SIGNED this ___ day of __________, 20__.

                                        ____________________________
                                        JUDGE PRESIDING
```

## Signed date drives the clocks

A Texas judgment is effective and the **plenary-power, motion-for-new-
trial (Tex. R. Civ. P. 329b), and appellate-timetable clocks run from
the date the judgment is signed** — not the date of the hearing or the
date the court announced its ruling. If a different effective date is
required, state it expressly. The signed date is the reference point
downstream skills use to compute post-judgment and appeal deadlines.

## Default judgment form

For a default judgment, confirm the defendant failed to answer by the
**Tex. R. Civ. P. 99 "Monday rule"** deadline (an answer is due by
10:00 a.m. on the Monday next after the expiration of 20 days after
service), that the citation and return are on file and proper, that
the petition pleaded the **Tex. R. Civ. P. 47(c) statement of relief
range**, and that the relief sought does not exceed what is demanded
in the pleadings, before tendering the proposed default judgment.
Confirm the current default mechanics in `tx-law-references`.

## "Submitted by" and "approved as to form"

The proposed form should identify who tendered it:

```
SUBMITTED BY:

____________________________
[Name]
[State Bar No. ___ if counsel / "Self-Represented [Party]" if pro se]
[Address / Phone / Email]

APPROVED AS TO FORM:

____________________________
[Opposing Party / Counsel]
```

"Approved as to form" means the party agrees the form **accurately
states** the court's ruling — not that the party agrees with the
result. See `tx-submit-order` for the transmittal workflow.

## Composition

- For format and caption: `tx-statewide-format`
- For submitting the proposed form for the judge's signature and
  transmitting the signed order: `tx-submit-order`
- For the venue overlay: `tx-hcdc`, `tx-dcdc`, `tx-county-courts`,
  `tx-family-court`
- For pro se conventions: `tx-pro-se`
- For deadline math from the signed date: `tx-deadlines`,
  `tx-post-judgment`

## References to author

- `references/order-template.md` — annotated proposed-Order scaffold
- `references/judgment-template.md` — final-Judgment scaffold, the
  Tex. R. Civ. P. 329b plenary-power / new-trial timetable, and the
  finality-recital pointers

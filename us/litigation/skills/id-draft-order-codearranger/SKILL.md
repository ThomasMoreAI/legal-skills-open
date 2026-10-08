---
name: id-draft-order-codearranger
title: Draft an Idaho Proposed Order
description: This skill should be used to scaffold an Idaho proposed order or proposed judgment for a judge's signature. Triggers include "draft an Idaho proposed order", "I.R.C.P. 58 entry of judgment", "proposed judgment Idaho", "I.R.C.P. 54 separate document judgment", "proposed order Idaho", "order on motion Idaho", "default judgment order Idaho", "Rule 54(b) certificate Idaho". Produces a proposed order or proposed judgment with the caption replicated, recitals, a decretal "IT IS HEREBY ORDERED" / "IT IS ADJUDGED" block, an entry-of-judgment line, and the judge-signature line at the foot. Covers I.R.C.P. 54(a) (a judgment must be set out in a separate document), I.R.C.P. 58 (entry of judgment), Rule 54(b) certification of finality on fewer than all claims/parties, and the rule that only a judge signs. Composes with `id-statewide-format` for the caption and `id-submit-order` for the transmittal workflow.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-draft-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Judgment Template
  path: references/judgment-template.md
- title: Order Template
  path: references/order-template.md
---

# Draft an Idaho Proposed Order

> **NOT LEGAL ADVICE.** This skill scaffolds a proposed order or
> judgment as a drafting aid. The filer is responsible for ensuring
> the form mirrors the relief the court actually granted and
> contains nothing the court did not rule on. **Only a judge signs
> an order or judgment** — this skill prepares the proposed form for
> the court's consideration; the filer submits it but does not sign
> in the judge's place. Verify the current rules and local practice
> before submitting.

Use this skill in addition to `id-statewide-format` when a motion,
stipulation, or hearing outcome requires a **proposed order** or
**proposed judgment** for the judge's signature. In Idaho, the
party prepares the proposed form and submits it; the **judge signs
it**, and the judgment is **entered** under **I.R.C.P. 58**. The
**date of entry** — not the date of the hearing or the judge's
signature — starts the post-judgment and appeal clocks. Confirm the
current day counts in `id-law-references`; this skill points at the
corpus rather than hard-coding them.

## Cardinal rule — the form mirrors the ruling

The proposed form's relief should **mirror exactly** what the court
ordered. Two failure modes:

- **Over-reaching**: decreeing relief the court did not grant — the
  court strikes or modifies it.
- **Under-reaching**: omitting relief the court actually granted —
  leaves the form incomplete and may require a corrective order.

Cross-check the relief requested in the motion against the decretal
block (`IT IS HEREBY ORDERED ...` / `IT IS ADJUDGED ...`) one item
at a time.

## A judgment must be a separate document — I.R.C.P. 54(a)

Under **I.R.C.P. 54(a)**, a **judgment must be set out in a separate
document** — distinct from any memorandum decision, opinion, order,
or minute entry that contains the court's reasoning. A "judgment"
in Idaho practice **states only the relief the court grants** to
which party; it does **not** recite the court's reasoning or
recount the procedural history. Keep the findings and analysis in
the order or memorandum decision; keep the judgment itself short
and operative.

- Draft an **Order** to dispose of a motion and to state findings
  and reasoning.
- Draft a separate **Judgment** when the matter is finally resolved
  and a Rule 54(a) judgment is required — the separate document that
  the appeal and post-judgment clocks run from.

## Entry of judgment — I.R.C.P. 58

Under **I.R.C.P. 58**, a judgment is **entered** when the court
signs it and the clerk files it in the record. A judgment is
generally **effective on entry**. Many deadlines — post-judgment
motions under I.R.C.P. 59 / 60 and the appeal period under the
Idaho Appellate Rules — run from **entry**, not from the date the
court announced its ruling. Confirm the current entry mechanics and
day counts in `id-law-references`.

> Confirm the deciding judge's submission practice (editable format,
> proposed-order routing) before transmitting — see `id-submit-order`.

## Rule 54(b) — multiple claims, finality

When the form resolves **fewer than all claims or fewer than all
parties**, the judgment is not final or appealable unless the court
enters an **I.R.C.P. 54(b) certificate** — an express determination
that there is **no just reason for delay** and an express direction
for entry of a final judgment. If finality is intended, include the
Rule 54(b) certificate language; if the form is interlocutory, do
**not** include it. The court — not the drafter — decides whether to
make the determination. Confirm the exact certificate language in
`id-law-references`.

## Standard proposed-Order structure

```
                [Caption — exactly matching the motion;
                 see id-statewide-format. Include the case
                 number and assigned judge.]

           [DOCUMENT TITLE: ORDER GRANTING
              DEFENDANT'S MOTION TO DISMISS]

This matter having come before the Court on [Moving Party's Motion
Title], filed [date]; the Court having considered the motion, any
response and reply, the supporting affidavits/declarations and
exhibits, and the argument of the parties; and good cause appearing;

IT IS HEREBY ORDERED that:

1. [Defendant's Motion to Dismiss is GRANTED / DENIED.]

2. [Specific consequential relief, e.g., "Plaintiff's Complaint is
   dismissed with prejudice."]

3. [Costs — taxed to ____, or "each party to bear its own costs."]

                                        ____________________________
                                        [Honorable Judge Name]
                                        District Judge / Magistrate
                                        Judge, [County] County

                                        Entered: ________________
                                        (filed by the Clerk)
```

## Standard separate-document Judgment (I.R.C.P. 54(a))

A Rule 54(a) judgment is a **separate document** that states only
the relief, with no recitals or reasoning:

```
                [Caption — see id-statewide-format]

                          JUDGMENT

JUDGMENT IS ENTERED AS FOLLOWS:

Judgment is entered in favor of [Plaintiff] and against [Defendant]
in the amount of $______, consisting of:
   a. Principal: $______
   b. Interest: $______ (state the rate and statutory basis)
   c. Costs and fees as may be awarded on a timely memorandum

                                        ____________________________
                                        [Honorable Judge Name]
                                        District Judge / Magistrate

                                        Entered: ________________
```

### Recitals vs. decretal language — keep them separate

In an **Order**, keep the **recitals** (the "having come before the
Court ... good cause appearing" preamble) separate from the
**decretal clause** (the numbered commands following "IT IS HEREBY
ORDERED"). Do not bury operative relief inside the recitals. In a
**Judgment**, omit recitals entirely — Rule 54(a) requires the
separate document to state only the relief.

## Effective date and entry

A judgment is generally effective on the **date of entry** — the
date the clerk files the signed judgment — not the date the judge
signed it or the date of the hearing. If a different effective date
is required, state it expressly. The date of entry is the reference
point downstream skills use to compute I.R.C.P. 59 / 60 and appeal
deadlines.

## Default judgment form

For a default judgment, recite the predicate findings in the
supporting application/order and keep the **Judgment** itself a
separate Rule 54(a) document. Confirm the default was properly
entered, that any required notice of the application was served, and
that the relief does not exceed what is demanded in the pleadings
before submitting the proposed judgment.

## Composition

- For format and caption: `id-statewide-format`
- For submitting the proposed form for the judge's signature and
  transmitting the entered judgment: `id-submit-order`
- For the venue overlay: `id-ada`, `id-bonneville`,
  `id-county-courts`, `id-family-court`
- For pro se conventions: `id-pro-se`
- For deadline math from entry: `id-deadlines`

## References to author

- `references/order-template.md` — annotated proposed-Order scaffold
- `references/judgment-template.md` — I.R.C.P. 54(a) separate-document
  Judgment scaffold and the Rule 58 entry mechanics

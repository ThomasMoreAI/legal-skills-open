---
name: az-draft-order-codearranger
title: Draft an Arizona Proposed Order
description: This skill should be used to scaffold an Arizona proposed form of order or proposed judgment for a judge's signature. Triggers include "draft an Arizona proposed order", "Ariz. R. Civ. P. 58 entry of judgment", "lodge a proposed judgment Arizona", "Rule 54(b) certification Arizona", "proposed form of order Arizona", "order on motion Arizona", "default judgment order Arizona". Produces a proposed order or proposed judgment with the caption replicated, recitals, a decretal "IT IS ORDERED" / "IT IS ADJUDGED" block, an effective-date / entry line, and the judge-signature line at the foot. Covers the Rule 58 lodging-and-objection path by which a party lodges a proposed form of judgment and the court signs, the Rule 54(b) certification of finality on fewer than all claims/parties, the Rule 54(d) limit on default-judgment relief, and the rule that only a judge signs. Composes with `az-statewide-format` for the caption and `az-submit-order` for the transmittal workflow.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-draft-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Arizona Proposed Order

> **NOT LEGAL ADVICE.** This skill scaffolds a proposed form of order or
> judgment as a drafting aid. The filer is responsible for ensuring the
> form mirrors the relief the court actually granted and contains
> nothing the court did not rule on. **Only a judge signs an order or
> judgment** — this skill prepares the proposed form for the court's
> consideration; the filer lodges it but does not sign in the judge's
> place. Verify the current rules and local practice before submitting.

Use this skill in addition to `az-statewide-format` when a motion,
stipulation, or hearing outcome requires a **proposed form of order** or
**proposed form of judgment** for the judge's signature. In Arizona, the
party presenting the judgment **lodges** a proposed form under **Ariz. R.
Civ. P. 58**; the court signs, and the judgment is **entered** when the
clerk files the signed form. The **date of entry** — not the date of the
hearing or the judge's signature — starts the post-judgment and appeal
clocks. Confirm the current day counts in `az-law-references`; this skill
points at the corpus rather than hard-coding them.

## Cardinal rule — the form mirrors the ruling

The proposed form's relief should **mirror exactly** what the court
ordered. Two failure modes:

- **Over-reaching**: decreeing relief the court did not grant — the court
  strikes or modifies it, and the opposing party will object during the
  Rule 58 objection window.
- **Under-reaching**: omitting relief the court actually granted — leaves
  the form incomplete and may require a corrective order.

Cross-check the relief requested in the motion against the decretal block
(`IT IS ORDERED...` / `IT IS ADJUDGED...`) one item at a time.

## How an Arizona judgment gets entered — Ariz. R. Civ. P. 58

Under Rule 58, the prevailing party (or the party directed by the court)
**lodges** a proposed form of judgment with the court and serves it on
the other parties. Rule 58(a) provides an **objection window**: an
opposing party may file an objection to the *form* of the lodged judgment
within the period the rule sets — **confirm the current day count in
`az-law-references` (`references/civil-rules.md` and the `court-rules`
corpus)** before relying on it. If no timely objection is filed, the
court signs the lodged form; if an objection is filed, the court resolves
the form before signing. The objection goes to the **form** of the
judgment, not a re-argument of the merits.

> Build the cover/transmittal and proof of service to match the Rule 58
> lodging mechanics. Some judges and local rules prefer the form be
> submitted in an editable format or with a self-addressed routing slip —
> confirm the deciding judge's practice (see `az-submit-order`).

## Rule 54 — multiple claims, finality, and default relief

- **Rule 54(b) certification.** When the form resolves **fewer than all
  claims or fewer than all parties**, the judgment is not final and
  appealable unless the court expressly determines there is **no just
  reason for delay** and directs entry of judgment. If finality is
  intended, include the Rule 54(b) certification language in the decretal
  block; if the form is interlocutory, do **not** include it.
- **Rule 54(d) — default-judgment relief limit.** A default judgment
  **must not differ in kind from, or exceed in amount,** what is
  demanded in the pleadings. (Rule 54(c) is a distinct provision — the
  recital that a judgment is final as to all claims and parties.) When
  drafting a default judgment, confirm the relief in the proposed form
  does not exceed the complaint's prayer (in both the type and the
  amount of relief).

## Standard proposed-form structure

```
                [Caption — exactly matching the motion;
                 see az-statewide-format. Include the case
                 number and assigned judge/division.]

           [DOCUMENT TITLE: [PROPOSED] ORDER GRANTING
              DEFENDANT'S MOTION TO DISMISS]
              — or — [PROPOSED] JUDGMENT

This matter having come before the Court on [Moving Party's Motion
Title], filed [date]; the Court having considered the motion, any
response and reply, the supporting affidavits and exhibits, and the
argument of the parties; and good cause appearing:

IT IS ORDERED that:

1. [Defendant's Motion to Dismiss is GRANTED / DENIED.]

2. [Specific consequential relief, e.g., "Plaintiff's Complaint is
   dismissed with prejudice."]

3. [Costs — taxed to ____, or "each party to bear its own costs."]

[For a final judgment on fewer than all claims/parties — Rule 54(b):]
There being no just reason for delay, the Court directs entry of this
judgment as a final judgment pursuant to Ariz. R. Civ. P. 54(b).

                                        ____________________________
                                        [Honorable Judge Name]
                                        Judge of the Superior Court
                                        [or Justice of the Peace, etc.]

                                        DATE OF ENTRY: ______________
                                        (filed by the Clerk)
```

### Recitals vs. decretal language — keep them separate

Keep the **recitals** (the "having come before the Court... good cause
appearing" preamble that states the procedural posture) separate from the
**decretal clause** (the numbered commands following "IT IS ORDERED" or
"IT IS ADJUDGED"). The recitals describe how the matter reached the court;
the decretal block states what the court commands. Do not bury operative
relief inside the recitals.

## Effective date and entry

A judgment is generally effective on the **date of entry** — the date the
clerk files the signed form — not the date the judge signed or the date
of the hearing. If a different effective date is required (e.g., a
deadline that runs from a date other than entry, or nunc pro tunc relief),
state it expressly in the decretal block. Do not leave the effective date
to inference. The date of entry is the reference point downstream skills
use to compute Rule 59 and appeal deadlines.

## Default judgment form

For a default judgment, the proposed form should recite the predicate
findings and respect the Rule 54(d) limit:

```
This matter having come before the Court on Plaintiff's application for
entry of a default judgment, the default of Defendant having been entered
on [date], the time to respond having expired, and good cause appearing:

IT IS ORDERED AND ADJUDGED that judgment is entered in favor of Plaintiff
and against Defendant in the amount of $______, consisting of:
   a. Principal: $______
   b. Interest: $______ (state the rate and statutory basis)
   c. Costs: $______
```

Confirm the default was properly entered, that any required notice of the
application was served, and that the relief **does not exceed the
complaint's demand** (Rule 54(d)) before lodging the proposed judgment.

## Composition

- For format and caption: `az-statewide-format`
- For lodging the form under Rule 58, the objection window, and
  transmitting the signed judgment: `az-submit-order`
- For the venue overlay: `az-maricopa`, `az-pima`, `az-superior-courts`
- For pro se conventions: `az-pro-se`

## References

- `az-law-references` (`references/civil-rules.md`, `references/court-rules/`)
  — Ariz. R. Civ. P. 54 and 58 text, the current Rule 58(a) objection day
  count, and entry-of-judgment mechanics

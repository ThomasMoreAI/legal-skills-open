---
name: mi-draft-order-codearranger
title: Draft a Michigan Proposed Order
description: This skill should be used to scaffold a Michigan proposed order or proposed judgment for a judge's signature. Triggers include "draft a Michigan proposed order", "MCR 2.602 entry of order", "7-day rule Michigan order", "stipulated order Michigan", "proposed judgment Michigan", "order on motion for summary disposition", "default judgment order Michigan", "draft an order for the judge to sign". Produces a proposed order with the caption replicated, recitals, a decretal "IT IS ORDERED" block, an effective-date / entry line, and the judge-signature line at the foot. Covers the MCR 2.602(B)(3) "7-day rule" service-and-objection path, the MCR 2.602(B)(4) stipulated / "approved as to form" path, and the rule that only a judge signs an order. Composes with `mi-statewide-format` for the caption, `mi-draft-motion` for the underlying motion, and `mi-submit-order` for the transmittal workflow.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-draft-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Michigan Proposed Order

> **NOT LEGAL ADVICE.** This skill scaffolds a proposed order as a
> drafting aid. The filer is responsible for ensuring the order
> mirrors the relief the court actually granted and contains nothing
> the court did not rule on. **Only a judge signs an order** — this
> skill prepares the proposed form for the court's consideration; the
> filer does not sign in the judge's place. Verify the current rules
> and local practice before submitting.

Use this skill in addition to `mi-statewide-format` when a motion,
stipulation, or hearing outcome requires a **proposed order** or
**proposed judgment** for the judge's signature. In Michigan, the
party drafting the order presents it under **MCR 2.602**; the court
signs and the order is entered when filed with the clerk. The **date
of entry** starts post-judgment clocks (e.g., the 21-day periods for
post-judgment motions and the appeal window).

## Cardinal rule — the order mirrors the ruling

The proposed order's relief should **mirror exactly** what the court
ordered. Two failure modes:

- **Over-reaching**: ordering something the court did not grant — the
  court strikes or modifies these, and the opposing party will object.
- **Under-reaching**: omitting relief the court actually granted —
  leaves the order incomplete and may require a corrective order.

Cross-check the relief requested in the motion against the order's
decretal block (`IT IS ORDERED...`) one item at a time.

## How a Michigan order gets entered — MCR 2.602(B)

MCR 2.602(B) gives the court several routes to enter an order or
judgment. The two the drafter most often invokes:

### The "7-day rule" — MCR 2.602(B)(3)

Within **7 days after the court's decision**, the drafting party may
serve a copy of the proposed order on the other parties **with a
notice that it will be submitted to the court for signing** if no
written objection is filed within **7 days after service**. If an
objecting party files a written objection within that 7-day window,
the court typically schedules the matter to settle the form of the
order. If no objection is filed, the proposed order is submitted to
the court for signature. Build the notice and the proof of service to
match this rule (the notice language and the 7-day objection period
are the load-bearing elements).

### The stipulated / "approved as to form" path — MCR 2.602(B)(4)

If the parties **agree** on the form of the order, they may have it
entered without the 7-day notice by having each party (or counsel)
sign an **"approved as to form"** / "stipulated" line. The signatures
confirm agreement with the **form**, not necessarily the result. A
stipulated order still requires the **judge's signature** to take
effect — stipulation does not substitute for entry by the court.

> Other MCR 2.602(B) routes exist (e.g., the court may direct a party
> to prepare the order, or sign at the time of the ruling). Confirm the
> route the deciding judge expects; some judges and local rules prefer
> on-the-record settlement of the order's form.

## Standard proposed-order structure

```
                [Caption — exactly matching the motion;
                 see mi-statewide-format. Include the case
                 number and assigned judge.]

           [DOCUMENT TITLE: ORDER GRANTING DEFENDANT'S
              MOTION FOR SUMMARY DISPOSITION]

At a session of said Court held in [County], Michigan
on __________________________, 20__.

PRESENT: HONORABLE ____________________________, [Circuit/District]
         Court Judge

This matter having come before the Court on [Defendant's Motion
Title], filed [date]; the Court having considered the motion, any
response, the supporting affidavits and exhibits, and the argument of
the parties; and the Court being otherwise fully advised:

IT IS ORDERED that:

1. [Defendant's Motion for Summary Disposition under MCR 2.116(C)(__)
   is GRANTED / DENIED.]

2. [Specific consequential relief, e.g., "Plaintiff's Complaint is
   dismissed with prejudice."]

3. [Costs — taxed to ____, or "no costs, this being a [basis]."]

[Optional, for a final order:] This order resolves the last pending
claim and closes the case.

                                        ____________________________
                                        [Honorable Judge Name]
                                        [Circuit / District] Court Judge

[7-day rule notice OR approval-as-to-form block — see below]
```

### Notice block for the 7-day rule (MCR 2.602(B)(3))

```
NOTICE: This proposed order will be submitted to the Court for entry
unless written objections are filed and served within 7 days after
service of this notice. MCR 2.602(B)(3).

[Proof of service on all parties — date and manner; see
mi-statewide-format.]
```

### Approval block for a stipulated order (MCR 2.602(B)(4))

```
APPROVED AS TO FORM AND ENTRY:

____________________________            ____________________________
[Movant / counsel; see                  [Opposing party / counsel]
 mi-statewide-format signature block]    APPROVED AS TO FORM
```

## Recitals vs. decretal language — keep them separate

Keep the **recitals** (the "having come before the Court... being
fully advised" preamble that states the procedural posture) separate
from the **decretal clause** (the numbered commands following "IT IS
ORDERED"). The recitals describe how the matter reached the court; the
decretal block states what the court commands. Do not bury operative
relief inside the recitals.

## Effective date and entry

An order generally takes effect on the **date of entry** — the date
the signed order is filed with the clerk — not the date the judge
signed or the date of the hearing. If a different effective date is
required (e.g., an order made effective nunc pro tunc, or a deadline
that runs from a date other than entry), state it expressly in the
decretal block. Do not leave the effective date to inference.

## Default judgment order

For a default judgment, the proposed order/judgment should recite the
predicate findings:

```
This matter having come before the Court on Plaintiff's request for
entry of a default judgment, the default of Defendant having been
entered on [date], and the Court being fully advised:

IT IS ORDERED that judgment is entered in favor of Plaintiff and
against Defendant in the amount of $______, consisting of:
   a. Principal: $______
   b. Interest: $______ (state the rate and statutory basis)
   c. Costs: $______
```

Confirm the default was properly entered and that any required notice
of the request for default judgment was served before submitting the
proposed judgment.

## Composition

- For format and caption: `mi-statewide-format`
- For the underlying motion: `mi-draft-motion`
- For the supporting affidavit/declaration: `mi-draft-declaration`
- For the notice of hearing: `mi-draft-note`
- For circulating under the 7-day rule and submitting the signed
  order: `mi-submit-order`
- For the venue overlay: `mi-wayne`, `mi-oakland`, `mi-36th-district`,
  `mi-circuit-courts`, `mi-district-courts`, `mi-circuit-courts`

## References

- `references/proposed-order-template.md` — annotated template with
  recitals, decretal block, and the 7-day-rule notice + approval-as-
  to-form lines
- `references/602-entry-routes.md` — the MCR 2.602(B) entry routes,
  including the (B)(3) 7-day rule and the (B)(4) stipulated path
- `references/default-judgment-order.md` — default-judgment recitals
  and entry findings

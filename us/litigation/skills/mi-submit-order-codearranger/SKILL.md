---
name: mi-submit-order-codearranger
title: Post-Hearing Proposed-Order Submission (Michigan)
description: This skill should be used after a Michigan hearing, when the judge has ruled and the prevailing party needs to prepare and submit a proposed order for entry under MCR 2.602(B), or when the court directs a party to submit an order reflecting an in-court ruling. Triggers include "submit a proposed order Michigan", "MCR 2.602 7-day rule", "entry of order Michigan", "approved as to form Michigan", "transmit order to judge Michigan", "the judge told me to draft the order", "Michigan order after hearing", "stipulated order Michigan", "serve a proposed order on the other side Michigan". Covers the two MCR 2.602(B) entry paths — the (B)(3) 7-day rule and the (B)(4) stipulated / approved-as-to-form path — plus the transmittal cover and the 7-day-rule service plan.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-submit-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Post-Hearing Proposed-Order Submission (Michigan)

> **NOT LEGAL ADVICE.** This skill helps draft and submit the
> proposed order. The wording must reflect the judge's actual
> ruling. Verify the filing court's local rules and the judge's
> practice on order submission before transmitting.

Use this skill after a Michigan court hearing when:

1. The judge **ruled from the bench** and directed a party
   (usually the prevailing party) to prepare the order; or
2. The court issued a ruling **conditioned** on a proposed order
   being submitted; or
3. The parties **agreed** to a result and need to memorialize it
   in a stipulated order.

## Entry of orders — MCR 2.602(B)

Michigan does not allow a party to simply mail a proposed order
to the judge for signature. **MCR 2.602(B)** prescribes how an
order or judgment is entered. The four methods are:

- **(B)(1)** — the court signs the order **at the time of the
  ruling**;
- **(B)(2)** — the court directs counsel to prepare the order and
  the court signs it once settled;
- **(B)(3)** — the **7-day rule** (the default self-help path);
  and
- **(B)(4)** — the **stipulated / approved-as-to-form** path.

This skill covers the two paths a self-represented party most
often drives: the **(B)(3) 7-day rule** and the **(B)(4)
stipulated** path.

## Path A — the 7-day rule (MCR 2.602(B)(3))

When the court has not signed the order in court and there is no
agreement, use the 7-day rule:

1. **Prepare the proposed order** reflecting the ruling (see
   `mi-draft-order`).
2. **Serve the proposed order on all other parties**, with a
   notice stating it will be submitted to the court for entry **if
   no written objection is filed and served within 7 days after
   service**.
3. **The other parties have 7 days** to either (a) file and serve
   a **written objection**, or (b) file and serve a **competing
   proposed order** with a notice of hearing.
4. **If no objection is timely filed**, submit the proposed order
   to the court for entry **with proof of service** showing the
   order was served and the 7 days have run.
5. **If an objection or competing order is filed**, the court
   resolves the dispute (often at a hearing); the judge enters the
   order the court determines is correct.

Compute the 7-day period under MCR 1.108 and add the MCR 2.107(C)
service add-on if the service method requires it — see
`mi-deadlines`. The objection window runs from **service**, not
from the hearing date.

### 7-day-rule service plan (the deliverable)

```
7-DAY-RULE SERVICE PLAN — MCR 2.602(B)(3)

Case:           [Short title], Case No. [Number]
Court:          [___] Circuit / District Court, [County] County
Proposed order: [Title of order]

1. Date proposed order served on all parties:  [DATE]
2. Method of service (MCR 2.107):              [e-Filing / mail / ...]
3. Service add-on, if any (MCR 2.107(C)):      [+N days]
4. Objection / competing-order deadline:       [DATE = #1 + 7 + add-on]
5. Parties served (name + address / e-service):
   - [Party] — [how served]
   - [Party] — [how served]
6. On/after the deadline, if NO objection filed:
   submit proposed order + PROOF OF SERVICE to the court for entry.
7. If an objection or competing order IS filed:
   do NOT submit; the court resolves it (hearing if set).
```

Attach the **proof of service** to the submission. Without it the
clerk cannot confirm the 7 days ran.

## Path B — stipulated / approved as to form (MCR 2.602(B)(4))

If all parties agree, the order may be entered under (B)(4) when
it is **signed (or e-signed) by the parties or their attorneys**
and bears a statement that it is **stipulated to** or **approved
as to form and content**. No 7-day waiting period is needed — the
agreement substitutes for the objection window.

- **"Approved as to form and content"** means the party agrees the
  order both reads correctly **and** reflects the agreed result.
- **"Approved as to form only"** means the party agrees the
  language accurately states the ruling but does **not** agree with
  the substance — useful where the court ruled against a party who
  still concedes the order is worded correctly.

```
                                        IT IS SO ORDERED.

                                        _____________________________
                                        Hon. [Judge's Name] (P#####)
                                        [Circuit / District] Judge

STIPULATED / APPROVED AS TO FORM AND CONTENT:

____________________________        ____________________________
[Party / Counsel] (P#####)          [Party / Counsel] (P#####)
[Attorney for / Self-Represented]   [Attorney for / Self-Represented]
```

## Cardinal rule — the order reflects the ruling

The proposed order must reflect exactly what the judge said. If
the ruling is ambiguous:

- **Review the record** (request the recording or transcript from
  the court reporter / recorder);
- **Confer with the other parties** on the proper wording;
- **Do not embellish** — if the court did not address a sub-issue,
  do not slip a finding in.

## Who signs

Only the **judge** signs the order into effect — the signature
line is the judge's, with the bar (**P-number**) shown. Parties
and counsel sign only the **approval / stipulation** block under
(B)(4), or serve the order under (B)(3); their signatures do not
enter the order.

## Transmittal cover (the deliverable)

```
[Date]

[Clerk of the Court / Hon. Judge Name, per the court's practice]
[___] Circuit / District Court, [County] County
[Courthouse address]
[Or: via MiFILE per the court's e-filing requirement]

RE:  [Case Short Title], Case No. [Number]
     Proposed [Order / Judgment] re: [Motion / matter heard]
     Submitted under MCR 2.602(B)([3] / [4])

To the Court:

Enclosed is a proposed [Order / Judgment] reflecting the Court's
ruling at the hearing on [date] on [Motion / matter].

[For (B)(3):] The proposed order was served on all parties on
[date]. More than 7 days have passed and no written objection or
competing order has been filed or served. Proof of service is
attached. The order is submitted for entry.

[For (B)(4):] The proposed order is stipulated to / approved as to
form and content by all parties, as shown by the signatures below.

Respectfully submitted,

[Name]  [P##### if attorney / "Self-Represented" if pro se]
[Address / Phone / Email]

cc: [Other parties / counsel]
```

## After the order is entered

Once the judge signs and the clerk **enters** the order, it
becomes operative. Steps:

1. **Obtain the entered order** from the clerk / MiFILE docket and
   confirm the **date of entry** — many deadlines run from entry.
2. **Verify the entered order matches** the proposed order — judges
   sometimes interlineate changes.
3. **Calendar deadlines that run from entry** (post-judgment
   motions; the appeal period) — see `mi-deadlines`.
4. **Confirm service** of the entered order on all parties under
   MCR 2.602(D) / MCR 2.107.
5. **Track compliance** — if the other side does not comply,
   prepare the next step (see `mi-post-judgment`).

## Composition

- For drafting the proposed order structure: `mi-draft-order`
- For computing the 7-day window + service add-ons: `mi-deadlines`
- For filing / e-filing the order: `mi-file-packet`
- For venue-specific submission channels: `mi-wayne`, `mi-oakland`,
  `mi-circuit-courts`, `mi-district-courts`, `mi-36th-district`,
  `mi-circuit-courts`
- For enforcement after entry: `mi-post-judgment`
- For hearing prep: `mi-hearings`
- For pro-se signature conventions: `mi-pro-se`

## References

- `mi-law-references` for MCR 2.602 (entry of judgments and
  orders), MCR 2.107 (service), and MCR 1.108 (time computation)
  text.
- The filing court's local rules and the judge's practice on order
  submission — verify the 7-day computation and any required
  transmittal form before submitting.

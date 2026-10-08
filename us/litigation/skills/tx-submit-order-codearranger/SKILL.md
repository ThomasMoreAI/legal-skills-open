---
name: tx-submit-order-codearranger
title: Post-Hearing Submission of a Proposed Order / Judgment (Texas)
description: Use this skill after a Texas hearing or ruling, when the court has ruled and a party (usually the prevailing party) must submit a proposed order or proposed judgment for the judge's signature, or when the court directs a party to prepare a form of order reflecting an in-court ruling. Triggers include "submit a proposed order Texas", "the judge told me to prepare the order", "tender a proposed order Texas", "proposed judgment Texas", "approved as to form Texas", "transmit order to the judge Texas", "get the judge to sign my order", "final judgment after ruling Texas". Covers preparing and transmitting the proposed form, the rule that only a judge signs, the signed-date that starts the appeal and plenary-power clocks (Tex. R. Civ. P. 329b), "approved as to form" signatures, and the post-signing steps. Produces a transmittal cover and a service plan.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-submit-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Post-Hearing Submission of a Proposed Order / Judgment (Texas)

> **NOT LEGAL ADVICE.** This skill helps draft and transmit the
> proposed order or judgment. The wording must reflect the court's
> actual ruling. **Only a judge signs** an order or judgment into
> effect. Verify the filing court's local rules, the assigned judge's
> submission practice, and the current entry mechanics before
> transmitting.

Use this skill after a Texas hearing or ruling when:

1. The court **ruled from the bench** or by letter ruling and directed
   a party (usually the prevailing party) to prepare the proposed
   order or judgment; or
2. The court's ruling is to be **memorialized** in a form of order or
   final judgment before it becomes effective and appealable; or
3. The parties **agreed** to a result and need to memorialize it in an
   agreed order or judgment.

## Prepare the form — Order vs. Judgment

Draft the proposed form with `tx-draft-order`, then transmit it here.
Keep the two document types distinct:

- An **Order** disposes of the motion and may recite the matters the
  court considered.
- A **Final Judgment** that finally resolves the matter must
  **dispose of all parties and all claims**. The appeal and
  post-judgment clocks run from the **date the judgment is signed**.
  If a judgment does not dispose of everything, it is interlocutory
  and generally not appealable.

## The signed date drives the clocks

In Texas, an order or judgment takes effect when the **judge signs
it**, and the key timetables run from the **date the judgment is
signed** — not the date of the hearing or the date the court announced
its ruling:

1. **Prepare** the proposed order/judgment reflecting the ruling (see
   `tx-draft-order`).
2. **Tender** the proposed form to the court for the judge's
   consideration, and **serve** a copy on every other party under
   **Tex. R. Civ. P. 21a** with a certificate of service.
3. **The judge signs** the form (resolving any dispute over its
   wording first); the clerk files it.

The trial court's **plenary power** ordinarily runs **30 days from the
date the judgment is signed**, extended by a timely **motion for new
trial or motion to modify** under **Tex. R. Civ. P. 329b**; the
appellate timetable runs from the same signed date. Track the
**signed date**, not the hearing date. Confirm the current day counts
in `tx-law-references`.

> Confirm the deciding judge's submission practice — some judges want
> the proposed form in an editable format or tendered through
> eFileTexas as a proposed order; see `tx-file-packet`.

### Service plan (the deliverable)

```
PROPOSED ORDER / JUDGMENT — SERVICE PLAN

Case:           [Short title], Cause No. [Number]
Court:          [Nth] Judicial District Court / County Court at Law
                No. ___, [County] County, Texas — [judge]
Proposed form:  [Title — Order re: ___ / Final Judgment]

1. Date proposed form TENDERED to the court:     [DATE]
2. Date proposed form SERVED on all parties:     [DATE]
3. Method of service (Tex. R. Civ. P. 21a):      [eFileTexas e-service
                                                  / mail / ...]
4. Service add-on, if mailed/emailed (+3 days):  [+3 days]
5. Parties served (name + address / e-service):
   - [Party] — [how served]
   - [Party] — [how served]
6. After signing: confirm the DATE THE JUDGMENT IS SIGNED with the
   clerk — the appeal and plenary-power clocks run from that date.
```

Compute any objection or deadline window with `tx-deadlines`, which
applies Tex. R. Civ. P. 4 time computation and the +3-day mail add-on.

## "Approved as to form" signatures

A party (or counsel) may sign a proposed order or judgment **"approved
as to form"** below the judge's signature line.

- **"Approved as to form"** means the party agrees the form
  **accurately states** the court's ruling — it does **not** mean the
  party agrees with the result. A losing party can approve a form as
  to form while preserving every substantive objection.
- **"Approved as to form and substance" / "agreed"** means the parties
  also agree to the substance — used for agreed or stipulated orders
  and judgments.

Securing "approved as to form" signatures can streamline submission,
but do not represent agreement the parties have not actually given.

## Who signs

Only the **judge** signs the order or judgment into effect. The
parties and counsel sign only the **"submitted by" / "approved as to
form"** block. A party's signature does not render the judgment.

```
SIGNED this ___ day of __________, 20__.

                                        ____________________________
                                        JUDGE PRESIDING

SUBMITTED BY:

____________________________
[Name]
[State Bar No. ___ if counsel / "Self-Represented [Party]" if pro se]
[Address / Phone / Email]

APPROVED AS TO FORM:

____________________________        ____________________________
[Party / Counsel]                   [Party / Counsel]
State Bar No. ___ /                 State Bar No. ___ /
  Self-Represented                    Self-Represented
```

Self-represented parties **omit the bar number** and identify as
"Self-Represented [Party]"; Texas-licensed counsel use the **State Bar
of Texas bar number** (see `tx-statewide-format`).

## Cardinal rule — the form reflects the ruling

The proposed form must reflect exactly what the court ruled. If the
ruling is ambiguous:

- **Review the record** (the court's docket sheet / letter ruling;
  request the reporter's record if needed);
- **Confer** with the other parties on the proper wording;
- **Do not embellish** — if the court did not address a sub-issue, do
  not slip a finding in.

## Transmittal cover (the deliverable)

```
[Date]

Hon. [Judge] / Court Coordinator
[Nth] Judicial District Court / County Court at Law No. ___
[County] County, Texas
[Courthouse address]
[Or: tendered via eFileTexas as a proposed order per local practice]

RE:  [Case Short Title], Cause No. [Number]
     Proposed [Order / Final Judgment] re: [matter heard]

To the Court:

Tendered herewith is a proposed [Order / Final Judgment] reflecting
the Court's ruling on [date] re: [matter]. A copy was served on all
parties on [date] under Tex. R. Civ. P. 21a.

[If a final judgment:] The proposed Final Judgment disposes of all
claims and all parties and includes a finality recital.

Respectfully submitted,

[Name]  [State Bar No. ___ if counsel / "Self-Represented" if pro se]
[Address / Phone / Email]

cc: [Other parties / counsel]
```

## After the order/judgment is signed

1. **Obtain the signed order/judgment** from the clerk / docket and
   confirm the **date the judgment was signed** — deadlines run from
   that date.
2. **Verify the signed form matches** what was tendered — the court
   sometimes interlineates changes.
3. **Calendar deadlines that run from the signed date** (the Tex. R.
   Civ. P. 329b motion-for-new-trial / motion-to-modify window, the
   plenary-power period, and the appellate timetable) — see
   `tx-deadlines` and `tx-post-judgment`.
4. **Confirm service** of the signed order/judgment on all parties.
5. **Track compliance** — if the other side does not comply, prepare
   the next step (see `tx-post-judgment`).

## Composition

- Drafting the proposed form structure: `tx-draft-order`
- Computing any objection / post-judgment window + mail add-on:
  `tx-deadlines`
- Tendering / e-filing the form: `tx-file-packet`
- Signature-block conventions: `tx-statewide-format`, `tx-pro-se`
- Venue-specific submission channels: `tx-hcdc`, `tx-dcdc`,
  `tx-county-courts`, `tx-family-court`
- Enforcement after signing: `tx-post-judgment`
- Hearing prep: `tx-hearings`

## References to author

- `references/transmittal-cover.md` — the transmittal cover and
  service plan
- `references/signed-judgment.md` — the signed-date timetable
  (Tex. R. Civ. P. 329b plenary power, motion for new trial, appellate
  deadlines) and the finality-recital pointers

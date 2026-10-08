---
name: id-submit-order-codearranger
title: Post-Hearing Submission of a Proposed Order / Judgment (Idaho)
description: Use this skill after an Idaho hearing, when the court has ruled and the prevailing party must submit a proposed order or proposed judgment for the judge's signature, or when the court directs a party to submit a form of order reflecting an in-court ruling. Triggers include "submit a proposed order Idaho", "I.R.C.P. 58 entry of judgment", "the judge told me to prepare the order", "proposed judgment Idaho", "I.R.C.P. 54 separate document judgment", "approved as to form Idaho", "transmit order to the judge Idaho", "Rule 54(b) certificate Idaho". Covers preparing and transmitting the proposed form, I.R.C.P. 54(a) (judgment is a separate document), I.R.C.P. 58 entry of judgment, Rule 54(b) finality, "approved as to form" signatures, and the rule that only a judge signs. Produces a transmittal cover and a service plan.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-submit-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Entry Of Judgment
  path: references/entry-of-judgment.md
- title: Transmittal Cover
  path: references/transmittal-cover.md
---

# Post-Hearing Submission of a Proposed Order / Judgment (Idaho)

> **NOT LEGAL ADVICE.** This skill helps draft and transmit the
> proposed order or judgment. The wording must reflect the court's
> actual ruling. **Only a judge signs** an order or judgment into
> effect. Verify the filing court's local rules, the assigned
> judge's submission practice, and the current entry mechanics
> before transmitting.

Use this skill after an Idaho hearing or ruling when:

1. The court **ruled from the bench** or by memorandum decision and
   directed a party (usually the prevailing party) to prepare the
   proposed order or judgment; or
2. The court's ruling is **conditioned** on a form of judgment being
   submitted before it becomes a final, appealable judgment; or
3. The parties **agreed** to a result and need to memorialize it in a
   form approved as to form.

## Prepare the form — Order vs. Judgment

Draft the proposed form with `id-draft-order`, then transmit it
here. Keep the two document types distinct:

- An **Order** disposes of the motion and may state the court's
  findings and reasoning.
- A **Judgment** that finally resolves the matter must be a
  **separate document under I.R.C.P. 54(a)** that states **only the
  relief** granted — no recitals, no reasoning. The appeal and
  post-judgment clocks run from the entry of that separate-document
  judgment.

## Entry of judgment — I.R.C.P. 58

Under **I.R.C.P. 58**, a judgment is **entered** when the court signs
it and the clerk files it in the record. The ordinary path is:

1. **Prepare** the proposed order/judgment reflecting the ruling (see
   `id-draft-order`).
2. **Submit** the proposed form to the court for the judge's
   consideration, and **serve** a copy on every other party under
   **I.R.C.P. 5** with a certificate of service.
3. **The court signs** the form (resolving any dispute over its
   wording first), and **the clerk enters** it.

A judgment is generally **effective when entered**. Many deadlines —
post-judgment motions under I.R.C.P. 59 / 60 and the appeal period
under the Idaho Appellate Rules — run from **entry**, not from the
date the court announced its ruling. Track the **entry date**, not
the hearing date. Confirm the current entry mechanics and any
objection window the local court applies in `id-law-references`.

> Confirm the deciding judge's submission practice — some judges
> want the proposed form in an editable format or transmitted through
> iCourt as a proposed order; see `id-file-packet`.

### Service plan (the deliverable)

```
PROPOSED ORDER / JUDGMENT — SERVICE PLAN

Case:           [Short title], Case No. [Number]
Court:          [Nth Judicial District], [County] County
                [District Court / Magistrate Division], [judge]
Proposed form:  [Title — Order re: ___ / Judgment]

1. Date proposed form SUBMITTED to the court:    [DATE]
2. Date proposed form SERVED on all parties:     [DATE]
3. Method of service (I.R.C.P. 5):               [iCourt e-service /
                                                  mail / ...]
4. Service add-on, if mailed (+3 days):          [+3 days]
5. Parties served (name + address / e-service):
   - [Party] — [how served]
   - [Party] — [how served]
6. On entry: confirm the DATE OF ENTRY with the clerk —
   deadlines run from entry, not from the hearing.
```

Compute any objection or deadline window with `id-deadlines`, which
applies I.R.C.P. 2.2 time computation and the +3-day mail add-on.

## Rule 54(b) — fewer than all claims or parties resolved

When the ruling disposes of **fewer than all claims, or the rights
of fewer than all parties**, the judgment is not final or appealable
unless the court enters an **I.R.C.P. 54(b) certificate** — an
express determination that there is no just reason for delay and an
express direction for entry of a final judgment. Without 54(b)
language, the judgment remains interlocutory and the appeal clock
does not start.

- If the ruling **fully** resolves the case, no 54(b) certificate is
  needed — the separate-document Judgment under Rule 54(a) is final.
- If you intend a 54(b) judgment, the proposed form must **request
  and recite** the 54(b) certificate; the court — not the drafter —
  decides whether to make it.

Confirm the exact Rule 54(b) certificate language in
`id-law-references` before submitting.

## "Approved as to form" signatures

A party (or counsel) may sign a proposed order or judgment **"approved
as to form"** below the judge's signature line.

- **"Approved as to form"** means the party agrees the form
  **accurately states** the court's ruling — it does **not** mean the
  party agrees with the result. A losing party can approve a form as
  to form while preserving every substantive objection.
- **"Approved as to form and content" / "stipulated"** means the
  parties also agree to the substance — used for agreed or stipulated
  orders and judgments.

Securing "approved as to form" signatures can streamline submission,
but do not represent agreement the parties have not actually given.

## Who signs

Only the **judge** signs the order or judgment into effect. The
parties and counsel sign only the **approval / stipulation** block,
or simply serve the submitted form. A party's signature does not
enter the judgment.

```
                                        _____________________________
                                        Hon. [Judge's Name]
                                        District Judge / Magistrate
                                        Judge, [County] County

                                        Entered: ____________________

APPROVED AS TO FORM:

____________________________        ____________________________
[Party / Counsel]                   [Party / Counsel]
ISB No. ___ / Self-Represented      ISB No. ___ / Self-Represented
[Attorney for / Self-Represented]   [Attorney for / Self-Represented]
```

Self-represented parties **omit the bar number** and identify as
"Self-Represented [Party]"; Idaho-licensed counsel use the **Idaho
State Bar number** (see `id-statewide-format`).

## Cardinal rule — the form reflects the ruling

The proposed form must reflect exactly what the court ruled. If the
ruling is ambiguous:

- **Review the record** (minute entry / memorandum decision; request
  the transcript);
- **Confer** with the other parties on the proper wording;
- **Do not embellish** — if the court did not address a sub-issue, do
  not slip a finding in.

## Transmittal cover (the deliverable)

```
[Date]

Clerk of the District Court / Hon. [Judge]
[Nth Judicial District], [County] County
[Courthouse address]
[Or: submitted via iCourt as a proposed order per local practice]

RE:  [Case Short Title], Case No. [Number]
     Proposed [Order / Judgment] re: [matter heard]

To the Court:

Submitted herewith is a proposed [Order / Judgment] reflecting the
Court's ruling on [date] re: [matter]. A copy was served on all
parties on [date] under I.R.C.P. 5.

[If a separate-document Judgment:] The proposed Judgment is submitted
as a separate document under I.R.C.P. 54(a).

[If a partial judgment:] The form requests an I.R.C.P. 54(b)
certificate so the judgment may be final and appealable.

Respectfully submitted,

[Name]  [ISB No. ___ if counsel / "Self-Represented" if pro se]
[Address / Phone / Email]

cc: [Other parties / counsel]
```

## After the judgment is entered

1. **Obtain the entered order/judgment** from the clerk / docket and
   confirm the **date of entry** — deadlines run from entry.
2. **Verify the entered form matches** what was submitted — the court
   sometimes interlineates changes.
3. **Calendar deadlines that run from entry** (I.R.C.P. 59 / 60
   motions; the appeal period) — see `id-deadlines`.
4. **Confirm service** of the entered order/judgment on all parties.
5. **Track compliance** — if the other side does not comply, prepare
   the next step (see `id-post-judgment`).

## Composition

- Drafting the proposed form structure: `id-draft-order`
- Computing any objection window + mail add-on: `id-deadlines`
- Submitting / e-filing the form: `id-file-packet`
- Signature-block conventions: `id-statewide-format`, `id-pro-se`
- Venue-specific submission channels: `id-ada`, `id-bonneville`,
  `id-county-courts`, `id-family-court`
- Enforcement after entry: `id-post-judgment`
- Hearing prep: `id-hearings`

## References to author

- `references/transmittal-cover.md` — the transmittal cover and
  service plan
- `references/entry-of-judgment.md` — I.R.C.P. 54(a) separate-document
  rule, I.R.C.P. 58 entry, and the Rule 54(b) certificate pointers

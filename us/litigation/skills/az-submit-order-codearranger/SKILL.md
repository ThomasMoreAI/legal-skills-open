---
name: az-submit-order-codearranger
title: Post-Ruling Lodging of a Form of Judgment / Order (Arizona)
description: Use this skill after an Arizona hearing, when the court has ruled and the prevailing party must lodge a proposed form of judgment or order for the judge's signature, or when the court directs a party to submit a form of order reflecting an in-court ruling. Triggers include "lodge a proposed judgment Arizona", "Ariz. R. Civ. P. 58 entry of judgment", "submit a proposed order Arizona", "approved as to form Arizona", "form of judgment Arizona", "the judge told me to lodge the order", "objection to form of judgment Arizona", "Rule 54(b) certification Arizona", "competing form of order Arizona". Covers the Rule 58 lodge-serve-object-then-sign sequence, the objection window before the court signs, Rule 54(b) / 54(c) finality, "approved as to form" signatures, and who signs. Produces a lodging/transmittal cover and the objection-window service plan.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-submit-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Post-Ruling Lodging of a Form of Judgment / Order (Arizona)

> **NOT LEGAL ADVICE.** This skill helps draft and lodge the
> proposed form of judgment or order. The wording must reflect
> the court's actual ruling. Verify the filing court's local
> rules, the assigned division's practice, and the current
> objection day-count before lodging.

Use this skill after an Arizona Superior Court hearing or ruling
when:

1. The court **ruled from the bench** or by minute entry and
   directed a party (usually the prevailing party) to prepare the
   form of judgment or order; or
2. The court's ruling is **conditioned** on a form of judgment
   being submitted before it becomes a final, appealable judgment;
   or
3. The parties **agreed** to a result and need to memorialize it
   in a form approved as to form and content.

## Entry of judgment — Ariz. R. Civ. P. 58

Arizona does not let a party simply mail a proposed judgment to
the judge for signature. **Ariz. R. Civ. P. 58** governs the
**form and entry** of a judgment, and the ordinary path is
**lodge → serve → objection window → the judge signs**:

1. **Prepare** the proposed form of judgment or order reflecting
   the ruling (see `az-draft-order`).
2. **Lodge** the proposed form with the court — that is, submit it
   for the judge's consideration **without** it being signed yet —
   and **serve** a copy on every other party under Ariz. R. Civ.
   P. 5.
3. **The other parties have a fixed window to object** to the form
   or to **lodge a competing form**. Rule 58 sets that window;
   **confirm the current day-count** in `az-law-references`
   (`court-rules/` / `civil-rules.md`) rather than assuming a
   number — Rule 58's objection period and add-on mechanics are
   amended periodically.
4. **If no timely objection is filed**, the court signs the lodged
   form and the clerk enters it.
5. **If a party objects or lodges a competing form**, the court
   resolves the dispute — often on the papers or at a brief
   conference — and signs the form it determines is correct.

A judgment is generally **effective when entered**. Many
deadlines (post-judgment motions, the appeal period) run from
**entry**, not from the date the court announced its ruling — so
track the entry date, not the hearing date.

### Objection-window service plan (the deliverable)

```
RULE 58 OBJECTION-WINDOW SERVICE PLAN

Case:           [Short title], Case No. [Number]
Court:          [County] County Superior Court, [division/judge]
Proposed form:  [Title — Form of Judgment / Order re: ___]

1. Date proposed form LODGED with the court:    [DATE]
2. Date proposed form SERVED on all parties:    [DATE]
3. Method of service (Ariz. R. Civ. P. 5):      [e-Filing / mail / ...]
4. Service add-on, if any (Ariz. R. Civ. P. 6(c)): [+N days]
5. Objection / competing-form deadline:
   [DATE — Rule 58 window from service; VERIFY day-count in corpus]
6. Parties served (name + address / e-service):
   - [Party] — [how served]
   - [Party] — [how served]
7. On/after the deadline, if NO objection is lodged:
   the court may sign the lodged form; confirm entry with the clerk.
8. If an objection or competing form IS lodged:
   the court resolves the dispute before signing.
```

Compute the window under Ariz. R. Civ. P. 6, applying the Rule
6(c) mail / e-service add-on **after** counting the base days —
see `az-deadlines`. The window runs from **service**, not from
the hearing.

## Rule 54(b) — fewer than all claims or parties resolved

When the ruling disposes of **fewer than all claims, or the
rights of fewer than all parties**, the form of judgment is not
final or appealable unless the court makes an **Ariz. R. Civ. P.
54(b) determination** — an express determination that there is no
just reason for delay and an express direction for entry of
judgment. Without 54(b) language, the judgment remains
interlocutory and the appeal clock does not start.

- If the ruling **fully** resolves the case, the form instead
  carries the **Rule 54(c)** finality recital confirming no
  further matters remain.
- If you intend a 54(b) judgment, the proposed form must
  **request and recite** the 54(b) determination; the court — not
  the drafter — decides whether to make it.

Confirm the exact 54(b) / 54(c) recital language in
`az-law-references` before lodging.

## "Approved as to form" signatures

A party (or counsel) may sign a form of judgment **"approved as
to form"** below the judge's signature line.

- **"Approved as to form"** means the party agrees the form
  **accurately states** the court's ruling — it does **not** mean
  the party agrees with the result. A losing party can approve a
  form as to form while preserving every substantive objection.
- **"Approved as to form and content" / "stipulated"** means the
  parties also agree to the substance — used for agreed or
  stipulated judgments.

Securing "approved as to form" signatures can short-circuit the
objection window, but do not represent agreement the parties have
not actually given.

## Who signs

Only the **judge** signs the judgment or order into effect. The
parties and counsel sign only the **approval / stipulation**
block, or simply serve the lodged form and let the objection
window run. A party's signature does not enter the judgment.

```
                                        _____________________________
                                        Hon. [Judge's Name]
                                        Judge of the Superior Court

APPROVED AS TO FORM:

____________________________        ____________________________
[Party / Counsel], Bar No. ___      [Party / Counsel], Bar No. ___
[Attorney for / Self-Represented]   [Attorney for / Self-Represented]
```

Self-represented parties **omit the bar number** and identify as
"Self-Represented [Party]"; Arizona-licensed counsel use the
**State Bar of Arizona bar number** (see `az-statewide-format`).

## Cardinal rule — the form reflects the ruling

The proposed form must reflect exactly what the court ruled. If
the ruling is ambiguous:

- **Review the record** (minute entry; request the transcript);
- **Confer** with the other parties on the proper wording;
- **Do not embellish** — if the court did not address a sub-issue,
  do not slip a finding in. That is what objections to form exist
  to catch.

## Lodging / transmittal cover (the deliverable)

```
[Date]

Clerk of the Superior Court / Hon. [Judge], [Division]
[County] County Superior Court
[Courthouse address]
[Or: lodged via the court's e-filing system per local practice]

RE:  [Case Short Title], Case No. [Number]
     Proposed Form of [Judgment / Order] re: [matter heard]
     Lodged under Ariz. R. Civ. P. 58

To the Court:

Lodged herewith is a proposed form of [Judgment / Order]
reflecting the Court's ruling on [date] re: [matter]. A copy was
served on all parties on [date] under Ariz. R. Civ. P. 5.

[If applicable:] No objection or competing form having been
lodged within the period under Ariz. R. Civ. P. 58, the form is
submitted for the Court's signature and entry.

[If a partial judgment:] The form requests an Ariz. R. Civ. P.
54(b) determination so the judgment may be final and appealable.

Respectfully submitted,

[Name]  [Bar No. ___ if counsel / "Self-Represented" if pro se]
[Address / Phone / Email]

cc: [Other parties / counsel]
```

## After the judgment is entered

1. **Obtain the entered judgment** from the clerk / docket and
   confirm the **date of entry** — deadlines run from entry.
2. **Verify the entered judgment matches** the lodged form — the
   court sometimes interlineates changes.
3. **Calendar deadlines that run from entry** (Rule 59 / Rule 60
   motions; the appeal period) — see `az-deadlines`.
4. **Confirm service** of the entered judgment on all parties.
5. **Track compliance** — if the other side does not comply,
   prepare the next step (see `az-post-judgment`).

## Composition

- Drafting the proposed form structure: `az-draft-order`
- Computing the objection window + Rule 6(c) add-on: `az-deadlines`
- Lodging / e-filing the form: `az-file-packet`
- Signature-block conventions: `az-statewide-format`, `az-pro-se`
- Venue-specific lodging channels: `az-maricopa`, `az-pima`,
  `az-superior-courts`
- Enforcement after entry: `az-post-judgment`
- Hearing prep: `az-hearings`

## References

- `az-law-references` for **Ariz. R. Civ. P. 58** (entry of
  judgment), **Rule 54(b) / 54(c)** (finality), **Rule 5**
  (service), and **Rule 6** (time computation) text.
- The filing court's local rules and the assigned division's
  practice on lodging — **verify the Rule 58 objection day-count
  and any required cover form before lodging.**

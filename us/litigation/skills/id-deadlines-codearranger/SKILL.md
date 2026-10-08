---
name: id-deadlines-codearranger
title: Idaho Case Deadlines
description: Use when the user asks about timing or deadlines in an Idaho civil case. Triggers include "Idaho deadline", "compute time Idaho Rule 2.2", "how do I count days in Idaho court", "when is my answer due in Idaho", "Idaho answer deadline 21 days", "Idaho mail add-on 3 days", "Idaho discovery response deadline", "Idaho summary judgment deadline 28 days", "Idaho motion notice 14 days", "Idaho statute of limitations", "SOL on a contract in Idaho", "Idaho court holidays", "is Columbus Day an Idaho holiday", "notice of appeal Idaho 42 days", "motion for new trial Idaho deadline". Computes calendar-day deadlines under I.R.C.P. 2.2 (NOT Rule 6 — Rule 6 is reserved), applies the 3-day add-on for service by mail, rolls forward off Saturdays / Sundays / Idaho Code § 73-108 legal holidays, and maps named rules to days plus authority via scripts/case-calendar.py.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-deadlines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Named Rules
  path: references/named-rules.md
- title: Rule 2.2 Time Computation
  path: references/rule-2.2-time-computation.md
- title: Section 73 108 Holidays
  path: references/section-73-108-holidays.md
- title: Sol Table
  path: references/sol-table.md
---

# Idaho Case Deadlines

> **NOT LEGAL ADVICE.** This skill computes deadlines. Independently
> verify in the cited rule or statute, confirm the venue's local rules
> and any standing or scheduling order, and treat no computed date as
> final without checking.

Use this skill to compute deadlines under **I.R.C.P. 2.2** (time
computation), the Idaho legal-holiday list (**Idaho Code § 73-108**), and
the named rules across the Idaho Rules of Civil Procedure and the Idaho
Code. The arithmetic lives in `scripts/case-calendar.py`; this body is
the framework and the pointer to authority. Pull verbatim rule text from
`../id-law-references/references/court-rules/`.

## ★ Idaho computes time under I.R.C.P. 2.2 — not Rule 6

A defining quirk of Idaho civil practice: time computation lives in
**I.R.C.P. 2.2**. **Rule 6 is RESERVED** and carries no time-computation
text — do not cite Rule 6 for counting days. To count a period stated in
days in the Idaho Rules of Civil Procedure, a court order, or (unless
otherwise provided) a statute:

1. **Exclude** the day of the act, event, or default that begins the
   period (e.g., the date of service).
2. **Count every intervening day, including weekends and holidays.**
3. **Include** the last day of the period, **unless** it is a
   **Saturday, Sunday, or legal holiday** — in which case the period runs
   forward to the **end of the next day** that is none of those.

> Confirm every day count below against the verbatim I.R.C.P. 2.2 text in
> the corpus before treating any computed date as final.

### The 3-day mail add-on — I.R.C.P. 2.2

When a period runs from **service** of a paper and service was made by
**mail**, Idaho adds **3 days** to the period. Apply the add-on **after**
the underlying Rule 2.2 count. Confirm the current treatment of
**electronic service (iCourt / I.R.E.F.S.)** under Rule 2.2 in the corpus
— service-method add-ons are amended periodically.

## Answer deadline — I.R.C.P. 12(a)(1)(A)

The load-bearing first-response number, stable enough to state here:
**21 days** after service of the summons and complaint (**I.R.C.P.
12(a)(1)(A)**). A timely pre-answer Rule 12(b) motion alters the time to
file a responsive pleading — see `id-first-30-days`.

## Idaho legal holidays — Idaho Code § 73-108

The holidays that trigger the Rule 2.2 roll-forward come from **Idaho
Code § 73-108**. The list below is qualitative; the **authoritative,
year-by-year computed set lives in `scripts/case-calendar.py` and the
corpus** — confirm there before relying on a date.

| Holiday | Date rule |
|---|---|
| New Year's Day | January 1 (fixed) |
| Martin Luther King, Jr. — Idaho Human Rights Day | 3rd Monday in January |
| Washington's Birthday | 3rd Monday in February |
| Memorial Day | Last Monday in May |
| Independence Day | July 4 (fixed) |
| Labor Day | 1st Monday in September |
| Columbus Day | 2nd Monday in October |
| Veterans Day | November 11 (fixed) |
| Thanksgiving Day | 4th Thursday in November |
| Christmas Day | December 25 (fixed) |

> **Idaho specifics to flag.** Idaho **observes Columbus Day** (2nd
> Monday in October). Idaho's § 73-108 does **not** list **Juneteenth**
> as a state legal holiday, and the **day after Thanksgiving** is not a
> § 73-108 state legal holiday — do not roll a deadline forward off
> either unless the corpus says otherwise. **Observed-day shift:** a
> holiday that falls on a **Saturday** is observed the **preceding
> Friday**; a holiday (other than Sunday) that falls on a **Sunday** is
> observed the **following Monday**. Confirm the operative set in the
> corpus / script.

## Named rules — quick reference

Run `python3 scripts/case-calendar.py --rules` for the full list. The
most commonly invoked:

| Rule key | Days | Authority |
|---|---|---|
| `answer-due` | +21 | I.R.C.P. 12(a)(1)(A) |
| `summons-service` | +182 | I.R.C.P. 4(b)(2) (serve after filing) |
| `interrogatory-response` | +30 | I.R.C.P. 33(a)(1), 33(b)(2) |
| `rfp-response` | +30 | I.R.C.P. 34(b)(2) |
| `rfa-response` | +30 | I.R.C.P. 36(a)(3) (failure deems admitted) |
| `sj-motion-before-hearing` | −28 | I.R.C.P. 56(b) (counted backward from hearing) |
| `sj-response-before-hearing` | −14 | I.R.C.P. 56(b) (counted backward from hearing) |
| `motion-notice` | +14 | I.R.C.P. 7(b)(3) (Notice of Hearing) |
| `new-trial-motion` | +14 | I.R.C.P. 59(b), 59(e) |
| `reconsideration` | +14 | I.R.C.P. 11.2(b) |
| `relief-judgment-outer` | +180 | I.R.C.P. 60(c)(1) |
| `memorandum-costs` | +14 | I.R.C.P. 54(d) |
| `appeal` | +42 | I.A.R. 14(a) |
| `sol-written-contract` | see corpus | Idaho Code § 5-216 |
| `sol-oral-contract` | see corpus | Idaho Code § 5-217 |
| `sol-open-account` | see corpus | Idaho Code § 5-217; accrual § 5-222 |
| `sol-personal-injury` | see corpus | Idaho Code § 5-219 |
| `sol-judgment` | see corpus | Idaho Code § 5-215 (11 years) |

**Answer, notice, and discovery day counts are stable enough to state in
this body; statute-of-limitations day counts are computed on the
calendar (anniversary date), so cite the Idaho Code section and verify
the current period.**

## Example invocations

```
# List every named rule
python3 scripts/case-calendar.py --rules

# Answer due — 21 days from service on 2026-03-14
python3 scripts/case-calendar.py --from 2026-03-14 --rule answer-due

# Discovery responses — 30 days from service on 2026-04-01
python3 scripts/case-calendar.py --from 2026-04-01 --rule interrogatory-response
python3 scripts/case-calendar.py --from 2026-04-01 --rule rfa-response

# Summary-judgment service cutoff — 28 days BEFORE a hearing set 2026-06-15
python3 scripts/case-calendar.py --from 2026-06-15 --rule sj-motion-before-hearing

# Notice of Hearing — at least 14 days before the hearing
python3 scripts/case-calendar.py --from 2026-06-15 --rule motion-notice

# New-trial / alter-amend window — 14 days after judgment 2026-05-20
python3 scripts/case-calendar.py --from 2026-05-20 --rule new-trial-motion

# Notice of Appeal — 42 days from entry of judgment
python3 scripts/case-calendar.py --from 2026-05-20 --rule appeal

# Ad hoc count — 21 calendar days from service, with roll-forward
python3 scripts/case-calendar.py --from 2026-03-14 --days 21 --mode calendar
```

For a period that runs from service by mail, add the **3-day** I.R.C.P.
2.2 mail add-on after the underlying count.

## Statutes of limitations — point at the Idaho Code, do not embed counts

Idaho's civil limitations periods are computed on the **calendar
(anniversary) date**, not as a fixed day count. **Cite the section and
verify the current period** rather than hard-coding it here:

| Claim family | Period | Authority |
|---|---|---|
| Written contract / instrument in writing | 5 years | Idaho Code § 5-216 |
| Oral / unwritten contract | 4 years | Idaho Code § 5-217 |
| Open account / account not in writing | 4 years | Idaho Code § 5-217; accrual § 5-222 |
| Personal injury | 2 years | Idaho Code § 5-219 |
| Fraud (from discovery) | 3 years | Idaho Code § 5-218(4) |
| Action upon a judgment | 11 years | Idaho Code § 5-215 |

SOL **accrual, tolling, and any revival** (by acknowledgment or
part-payment) are **fact-dependent** — verify against current law for the
specific claim.

## Appeal and post-judgment windows to watch

- **Motion for new trial / to alter or amend — I.R.C.P. 59.** File within
  **14 days** after entry of the judgment (Rule 59(b), 59(e)); the window
  is not extendable. See `id-post-judgment`.
- **Motion for reconsideration — I.R.C.P. 11.2.** File within **14 days**
  after entry of the final judgment (Rule 11.2(b)).
- **Notice of Appeal — I.A.R. 14(a).** File within **42 days** after entry
  of the judgment or order appealed from; confirm which entry triggers
  the clock and whether a post-trial motion has tolled it. A cross-appeal
  runs under **I.A.R. 15**.

## How `id-deadlines` composes with the scripts

The arithmetic lives in `scripts/case-calendar.py`, which encodes the
**Idaho Code § 73-108** holidays for any year, applies the I.R.C.P. 2.2
roll-forward off Saturdays / Sundays / holidays and the 3-day mail
add-on, and maps named rule keys to `(days, mode, description,
authority)`. Confirm the script's holiday set and rule counts against
`../id-law-references/references/court-rules/` after any quarterly corpus
refresh.

## Composition

- For format: `id-statewide-format`
- For the substantive rule or statute text: `id-law-references`
- For first-response timing: `id-first-30-days`
- For discovery timing: `id-discovery`
- For the Notice-of-Hearing 14-day clock: `id-hearings`,
  `id-schedule-hearing`
- For post-judgment / appeal timing: `id-post-judgment`
- For matter-specific deadlines: `id-consumer-debt`, `id-family-law`

## References

- `references/rule-2.2-time-computation.md` — I.R.C.P. 2.2 with notes
  (and the Rule 6-is-reserved flag)
- `references/section-73-108-holidays.md` — the holidays statute with
  year-by-year computed dates and the observed-day shift
- `references/sol-table.md` — Idaho Code limitations chart by claim type
  with authority
- `references/named-rules.md` — full list of rule keys with authority

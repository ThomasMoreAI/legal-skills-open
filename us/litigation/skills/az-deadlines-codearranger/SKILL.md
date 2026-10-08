---
name: az-deadlines-codearranger
title: Arizona Case Deadlines
description: Use when the user asks about timing or deadlines in an Arizona civil case. Triggers include "Arizona deadline", "Rule 6 compute time Arizona", "how do I count days in Arizona court", "when is my answer due in Arizona", "answer deadline Arizona 20 days", "30 days served outside Arizona", "Ariz. R. Civ. P. 6(c) mail add-on", "response to motion Arizona Rule 7.1", "Arizona statute of limitations", "SOL on a contract in Arizona", "Arizona court holidays", "is Columbus Day an Arizona holiday", "notice of appeal Arizona ARCAP 9", "motion for new trial Rule 59 Arizona". Computes calendar-day deadlines under Ariz. R. Civ. P. 6(a), applies the Rule 6(c) mail add-on, rolls forward off Saturdays / Sundays / A.R.S. § 1-301 legal holidays, and maps named rules (answer-due, motion-response, motion-for-new-trial, notice-of-appeal, statutes of limitations) to days plus authority.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-deadlines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Arizona Case Deadlines

> **NOT LEGAL ADVICE.** This skill computes deadlines. Independently
> verify in the cited rule or statute, confirm the venue's local
> rules and any standing or scheduling order, and treat no computed
> date as final without checking.

Use this skill to compute deadlines under **Ariz. R. Civ. P. 6(a)**
(time computation), the Arizona legal-holiday list (**A.R.S.
§ 1-301**), and the named rules across the Arizona Rules of Civil
Procedure and the Arizona Revised Statutes. The arithmetic lives in
`scripts/case-calendar.py`; this body is the framework and the
pointer to authority.

## Ariz. R. Civ. P. 6(a) — computation of time

To count a period stated in days in the Arizona Rules of Civil
Procedure, a court order, or (unless otherwise provided) a statute:

1. **Exclude** the day of the act, event, or default that begins the
   period (e.g., the date of service).
2. **Include** the last day of the period, **unless** it is a
   **Saturday, Sunday, or legal holiday** (or a day the clerk's
   office is inaccessible) — in which case the period runs to the
   **end of the next day** that is none of those.
3. Periods stated in **weeks, months, or years** are fixed by the
   corresponding calendar unit (e.g., the anniversary date for a
   year); compute these on the calendar, not as a fixed day count.

> Confirm every day count below against the verbatim rule text in
> `az-law-references` before treating any computed date as final.

### Ariz. R. Civ. P. 6(c) — the mail / e-service add-on

When a period runs from **service** of a paper made by **mail**,
Arizona adds **5 days** to the period. Apply the add-on **after** the
underlying Rule 6(a) count. Confirm the current treatment of
**electronic service** under Rule 6(c) in `az-law-references` —
service-method add-ons are amended periodically.

## Answer deadlines — Ariz. R. Civ. P. 12(a)

These are the load-bearing first-response numbers and are stable:

- **20 days** after **service within Arizona** of the summons and
  complaint (Ariz. R. Civ. P. 12(a)(1)(A)(i)).
- **30 days** when the defendant was **served outside Arizona**
  (Ariz. R. Civ. P. 4.2(m)).

A timely pre-answer motion under Rule 12(b) alters the time to file a
responsive pleading — see `az-first-30-days`. Motion-practice timing
(response and reply intervals) is governed by **Rule 7.1**; read the
current intervals from `az-law-references`.

## Arizona legal holidays — A.R.S. § 1-301

The holidays that trigger the Rule 6(a) roll-forward come from
**A.R.S. § 1-301**. The list below is qualitative; the
**authoritative, year-by-year computed set lives in
`scripts/case-calendar.py` and the corpus** — confirm there before
relying on a date.

| Holiday | Date rule |
|---|---|
| New Year's Day | January 1 (fixed) |
| Martin Luther King, Jr. / Civil Rights Day | 3rd Monday in January |
| Lincoln / Washington Presidents' Day | 3rd Monday in February |
| Memorial Day | Last Monday in May |
| Independence Day | July 4 (fixed) |
| Labor Day | 1st Monday in September |
| Columbus Day | 2nd Monday in October |
| Veterans' Day | November 11 (fixed) |
| Thanksgiving Day | 4th Thursday in November |
| Christmas Day | December 25 (fixed) |

> **Arizona specifics to flag.** A.R.S. § 1-301 designates several
> commemorative days (e.g., Native American Day, Constitution
> Commemoration Day) that are **not** court-closure holidays for the
> Rule 6(a) roll-forward — distinguish a designated day from a legal
> holiday that closes the courts, and confirm the operative set in
> the corpus / script. Arizona has **no separate Lincoln's Birthday**
> (combined as Presidents' Day) and **does not** list a standalone
> Juneteenth or Cesar Chavez Day in § 1-301 — verify the current
> statute before assuming either closes the courts. When a fixed-date
> holiday falls on a weekend, confirm the observed day in the corpus
> / script rather than assuming a Friday or Monday observance.

## Named rules — quick reference

Run `python3 scripts/case-calendar.py --rules` for the full list. The
most commonly invoked:

| Rule key | Days | Authority |
|---|---|---|
| `answer-due` | +20 | Rule 12(a)(1)(A)(i) (served within Arizona) |
| `answer-due-out-of-state` | +30 | Rule 4.2(m) (served outside Arizona) |
| `motion-response` | per Rule 7.1 | Rule 7.1(a) (response to a motion) |
| `motion-reply` | per Rule 7.1 | Rule 7.1(a) (reply in support) |
| `mail-add-on` | +5 | Rule 6(c) (service by mail) |
| `motion-for-new-trial` | +15 | Rule 59 (after entry of judgment — verify) |
| `notice-of-appeal` | +30 | ARCAP 9 (from entry of the judgment — verify trigger) |
| `sol-written-contract` | see corpus | A.R.S. § 12-548 |
| `sol-oral-open-account` | see corpus | A.R.S. § 12-543 |
| `sol-personal-injury` | see corpus | A.R.S. § 12-542 |

**Answer deadlines (Rule 12(a)) are stable enough to state in this
body; statute-of-limitations day counts are not — cite the A.R.S.
section and read the current period from the corpus.**

## Statutes of limitations — point at the A.R.S., do not embed counts

Arizona's civil limitations periods live at **A.R.S. §§ 12-541
through 12-552**. **Cite the section and read the current period from
the corpus** rather than hard-coding a count here (these drift and
are claim-specific):

| Claim family | Authority |
|---|---|
| Written contract for debt | A.R.S. § 12-548 |
| Oral debt / stated or open account | A.R.S. § 12-543 |
| Merchant mutual/current account; foreign judgment or instrument | A.R.S. § 12-544 |
| Personal injury; general tort | A.R.S. § 12-542 |
| One-year actions (e.g., defamation, certain statutory) | A.R.S. § 12-541 |
| Catch-all (no other limitation prescribed) | A.R.S. § 12-550 |
| Real-property / recovery of real property | A.R.S. §§ 12-521 et seq. (confirm) |

SOL **accrual, tolling, and any revival** (by acknowledgment or
part-payment) are **fact-dependent** — verify against current law for
the specific claim. Periods stated in **years** are computed on the
calendar (anniversary) date, not as a fixed day count.

## Appeal and post-judgment windows to watch

- **Motion for new trial / to alter or amend — Ariz. R. Civ. P. 59.**
  File within the Rule 59 period (commonly **15 days** after entry of
  the judgment — **confirm the current interval** in the corpus). A
  timely Rule 59 motion extends the time to appeal. See
  `az-post-judgment`.
- **Notice of appeal — ARCAP 9.** File within **30 days** after entry
  of the judgment or order appealed from; **confirm which entry
  triggers the clock** and whether a post-trial motion has tolled it.
  See `az-post-judgment`.

## How `az-deadlines` composes with the scripts

The arithmetic lives in `scripts/case-calendar.py`, which encodes the
**A.R.S. § 1-301** holidays for any year, applies the Rule 6(a)
roll-forward off Saturdays / Sundays / holidays and the Rule 6(c)
mail add-on, and maps named rule keys to `(days, description,
authority)`. Run:

```
python3 scripts/case-calendar.py --rules                      # list rule keys
python3 scripts/case-calendar.py --from 2026-03-14 --rule answer-due
```

Confirm the script's holiday set and rule counts against
`az-law-references` after any quarterly corpus refresh.

## Composition

- For format: `az-statewide-format`
- For the substantive rule or statute text: `az-law-references`
- For first-response timing: `az-first-30-days`
- For discovery timing: `az-discovery`
- For post-judgment / appeal timing: `az-post-judgment`
- For matter-specific deadlines: `az-family-law`, `az-consumer-debt`,
  `az-personal-injury`, `az-landlord-tenant`

## References

- `references/rule-6-time-computation.md` — Ariz. R. Civ. P. 6(a) +
  6(c) with notes
- `references/ars-1-301-holidays.md` — the holidays statute with
  year-by-year computed dates
- `references/sol-table.md` — A.R.S. §§ 12-541–12-552 limitations
  chart by claim type with authority
- `references/named-rules.md` — full list of rule keys with authority

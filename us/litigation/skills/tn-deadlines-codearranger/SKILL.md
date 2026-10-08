---
name: tn-deadlines-codearranger
title: Tennessee Case Deadlines
description: Use when the user asks about timing or deadlines in a Tennessee civil case. Triggers include "when is my answer due in Tennessee", "Tenn. R. Civ. P. 6 time computation", "Rule 6.01", "Rule 6.05 mail rule", "deadline in Tennessee court", "Tennessee court holidays", "Tenn. Code Ann. § 15-1-101 holidays", "does Tennessee observe Good Friday", "is the day after Thanksgiving a court holiday in Tennessee", "Tennessee statute of limitations", "SOL on a contract in Tennessee", "10 days to appeal General Sessions", "Rule 59 deadline", "summary judgment 30-day notice". Computes calendar-day deadlines under Tenn. R. Civ. P. 6.01, applies the 3-day mail add-on under Rule 6.05, rolls forward off Saturdays / Sundays / Tenn. Code Ann. § 15-1-101 legal holidays, and maps named rules (answer-due, general-sessions-appeal 10 days, summary-judgment-service, motion to alter or amend, statutes of limitations) to days plus authority.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-deadlines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Tennessee Case Deadlines

> **NOT LEGAL ADVICE.** This skill computes deadlines. Independently
> verify in the cited rule or statute, confirm the venue's local rules
> and any standing order, and treat no computed date as final without
> checking.

Use this skill to compute deadlines under **Tenn. R. Civ. P. 6.01**
(time computation), the Tennessee legal-holiday list (**Tenn. Code
Ann. § 15-1-101**), and the named rules across the Tenn. R. Civ. P.
and the Tennessee Code.

## Tenn. R. Civ. P. 6.01 — time computation

To count a period stated in the Tenn. R. Civ. P. or in a Tennessee
statute:

1. **Exclude** the day of the act or event that starts the period
   (e.g., the service date).
2. **Include** the last day of the period, **unless** it is a
   **Saturday, a Sunday, or a legal holiday** — in which case the
   period runs to the **end of the next day** that is not one of those.

### Tenn. R. Civ. P. 6.05 — the 3-day mail add-on

When a party has a right or duty to act within a prescribed period
**after service**, and service was made **by mail**, **3 days** are
added to the prescribed period. Apply 6.05 **after** the underlying
count, and confirm whether the venue treats electronic service the
same way.

> Frame every day count below as the **current** rule. Confirm the
> number against the verbatim rule text in `tn-law-references` before
> treating any computed date as final.

## Tennessee legal holidays — Tenn. Code Ann. § 15-1-101

| Holiday | Date rule |
|---|---|
| New Year's Day | January 1 (fixed) |
| Martin Luther King, Jr. Day | 3rd Monday in January |
| Washington Day (Presidents' Day) | 3rd Monday in February |
| **Good Friday** | Friday before Easter (**movable**) — Tennessee **does** observe |
| Memorial / Decoration Day | Last Monday in May |
| **Juneteenth** | June 19 (fixed) — in the statute |
| Independence Day | July 4 (fixed) |
| Labor Day | 1st Monday in September |
| **Columbus Day** | 2nd Monday in October — Tennessee **does** observe |
| Veterans' Day | November 11 (fixed) |
| Thanksgiving | 4th Thursday in November |
| Christmas | December 25 (fixed) |

Plus any day proclaimed by the Governor or President, and statewide
election days.

> **Two Tennessee specifics to flag.** Tennessee's § 15-1-101 list
> **includes Good Friday** (movable, the Friday before Easter) and
> **Columbus Day** (2nd Monday in October). Both count for Rule 6.01
> roll-forward.

> **Substitution.** A holiday falling on **Sunday** is observed the
> **following Monday**; a holiday falling on **Saturday** is observed
> the **preceding Friday**.

> ⚠ **Day after Thanksgiving is NOT a § 15-1-101 legal holiday.** It
> is often an administrative state-employee day off, but it does
> **not** trigger the Rule 6.01 roll-forward unless a court is closed
> by order. Do not treat it as a holiday for deadline arithmetic.

## Named rules — quick reference

Run `python3 scripts/case-calendar.py --rules` for the full list. The
most commonly invoked:

| Rule key | Days | Authority |
|---|---|---|
| `answer-due` | +30 | Tenn. R. Civ. P. 12.01 |
| `answer-after-12-denial` | +15 | Tenn. R. Civ. P. 12.01 |
| `discovery-response` | +30 | Tenn. R. Civ. P. 33 / 34 / 36 |
| `discovery-response-predefault` | +45 | Tenn. R. Civ. P. 33 / 34 / 36 (defendant served before answering) |
| `rfa-deemed-admitted` | +30 | Tenn. R. Civ. P. 36.01 |
| `summary-judgment-service` | -30 | Tenn. R. Civ. P. 56.04 (motion served ≥ 30 days before hearing) |
| `mail-add-on` | +3 | Tenn. R. Civ. P. 6.05 |
| `motion-alter-amend` | +30 | Tenn. R. Civ. P. 59.04 (non-extendable) |
| `general-sessions-appeal` | +10 | Tenn. Code Ann. § 27-5-108 (de novo to Circuit) |
| `sol-contract` | +6 years | Tenn. Code Ann. § 28-3-109 |
| `sol-ucc-goods` | +4 years | Tenn. Code Ann. § 47-2-725 |
| `sol-personal-injury` | +1 year | Tenn. Code Ann. § 28-3-104 |
| `sol-property-damage` | +3 years | Tenn. Code Ann. § 28-3-105 |
| `fdcpa-validation` | +30 | 15 U.S.C. § 1692g(a)(3) |
| `fdcpa-sol` | +1 year | 15 U.S.C. § 1692k(d) |

The script encodes the day counts and the holiday roll-forward;
always confirm an unusual number against the cited rule. Some
statutory periods are stated in **years** — compute those on the
calendar (anniversary) date, not as a fixed day-count.

## Two non-extendable / short windows to watch

- **Tenn. R. Civ. P. 59.04 motion to alter or amend** — must be filed
  within **30 days after entry** of the judgment. This window is
  **non-extendable** (Tenn. R. Civ. P. 6.02 cannot enlarge it). A
  timely Rule 59 motion tolls the time to appeal; a late one does not.
  See `tn-post-judgment`.
- **General Sessions de novo appeal** — a party must appeal a General
  Sessions civil judgment to Circuit Court within **10 days** of entry
  (Tenn. Code Ann. § 27-5-108). Miss it and the judgment stands. See
  `tn-post-judgment` and `tn-general-sessions`.

## Statutes of limitations — primary Tennessee claims (Title 28)

| Claim | SOL | Authority | Notes |
|---|---|---|---|
| Written contracts / open accounts | **6 years** | Tenn. Code Ann. § 28-3-109 | Most credit-card debt; accrual on open accounts is fact-dependent |
| Sale of goods (UCC) | **4 years** | Tenn. Code Ann. § 47-2-725 | Can displace the 6-year contract period |
| Personal injury / personal torts | **1 year** | Tenn. Code Ann. § 28-3-104 | 2-year extension where criminal charges arise from the same conduct (§ 28-3-104(a)(2)) |
| Property damage | **3 years** | Tenn. Code Ann. § 28-3-105 | |
| Slander | 6 months | Tenn. Code Ann. § 28-3-104 | |
| Libel | 1 year | Tenn. Code Ann. § 28-3-103 | |
| FDCPA | 1 year from violation | 15 U.S.C. § 1692k(d) | Applies in Tennessee courts |

A **sworn account** under Tenn. Code Ann. § 24-5-107 is an evidentiary
burden-shifting device, **not** a separate SOL. SOL accrual,
tolling, and any revival by part-payment or written acknowledgment are
**fact-dependent** — verify against current law for the specific claim.

## Examples

### "When is my answer due if I was served personally in Nashville on Friday, March 14, 2025?"

```
$ python3 scripts/case-calendar.py --from 2025-03-14 --rule answer-due
Answer due (Tenn. R. Civ. P. 12.01)
Deadline: Monday, April 14, 2025
  From: Friday, March 14, 2025
  30 calendar days after; rolled forward off any Sat/Sun/§ 15-1-101 holiday
  Authority: Tenn. R. Civ. P. 12.01
```

### "How long do I have to appeal a General Sessions judgment entered Tuesday, June 3, 2025?"

```
$ python3 scripts/case-calendar.py --from 2025-06-03 --rule general-sessions-appeal
De novo appeal to Circuit Court
Deadline: Friday, June 13, 2025
  From: Tuesday, June 03, 2025
  10 calendar days after
  Authority: Tenn. Code Ann. § 27-5-108
```

## How `tn-deadlines` composes with the scripts

The body above is the reference; the arithmetic lives in
`scripts/case-calendar.py`, which:

- Encodes the Tenn. Code Ann. § 15-1-101 holidays (including the
  movable **Good Friday**, **Columbus Day**, and **Juneteenth**, and
  **excluding** the day after Thanksgiving)
- Computes the holiday set for any year and the roll-forward rule
- Applies the Tenn. R. Civ. P. 6.05 3-day mail add-on
- Maps named rule keys to `(days, description, authority)`

Use `scripts/case-calendar.py --rules` for the canonical list and
`scripts/case-calendar.py --from YYYY-MM-DD --rule <key>` for a
specific computation.

## Composition

- For format: `tn-statewide-format`
- For the substantive rule: `tn-law-references`
- For first-response timing: `tn-first-30-days`
- For discovery timing: `tn-discovery`
- For post-judgment timing (Rule 59 / 60, appeal): `tn-post-judgment`
- For matter-specific deadlines: `tn-family-law`, `tn-consumer-debt`,
  `tn-personal-injury`

## References

- `references/rule-6-time-computation.md` — Tenn. R. Civ. P. 6.01 /
  6.05 with notes
- `references/tca-15-1-101-holidays.md` — the holidays statute with
  year-by-year computed dates
- `references/sol-table.md` — SOL chart by claim type with authority
- `references/named-rules.md` — full list of rule keys with authority

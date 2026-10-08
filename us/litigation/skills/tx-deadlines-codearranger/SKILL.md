---
name: tx-deadlines-codearranger
title: Texas Case Deadlines
description: Use when the user asks about timing or deadlines in a Texas civil case. Triggers include "Texas deadline", "compute time Texas Rule 4", "how do I count days in Texas court", "when is my answer due in Texas", "Texas Monday rule answer deadline", "Texas mail add-on 3 days", "Texas Rule 21a 3 days", "Texas discovery response deadline", "Texas summary judgment 21 days", "Texas court holidays", "is Juneteenth a Texas court holiday", "is the Friday after Thanksgiving a Texas holiday", "Texas statute of limitations", "SOL on a debt in Texas", "4-year debt limitations Texas", "motion for new trial Texas deadline", "plenary power Texas". Computes calendar-day deadlines under TRCP 4 (exclude the first day, include the last; roll forward off Saturdays / Sundays / legal holidays), applies the TRCP 21a +3-day service add-on, applies the TRCP 99 Monday rule for the answer, rolls off the Tex. Gov't Code § 662.003 legal holidays, and maps named rules to days plus authority via scripts/case-calendar.py.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-deadlines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Texas Case Deadlines

> **NOT LEGAL ADVICE.** This skill computes deadlines. Independently
> verify in the cited rule or statute, confirm the venue's local rules
> and any docket-control or scheduling order, and treat no computed
> date as final without checking.

Use this skill to compute deadlines under **TRCP 4** (time
computation), the Texas legal-holiday list (**Tex. Gov't Code
§ 662.003**), and the named rules across the Texas Rules of Civil
Procedure and the Texas codes. The arithmetic lives in
`scripts/case-calendar.py`; this body is the framework and the pointer
to authority. Pull verbatim rule text from
`../tx-law-references/references/court-rules/`.

## Time computation — TRCP 4

To count a period stated in days in the Texas Rules of Civil Procedure,
a court order, or (unless otherwise provided) a statute:

1. **Exclude** the day of the act, event, or default that begins the
   period (e.g., the date of service).
2. **Count every intervening day, including weekends and holidays.**
3. **Include** the last day of the period, **unless** it is a
   **Saturday, Sunday, or legal holiday** — in which case the period
   runs to the **end of the next day** that is none of those.

> Confirm every day count below against the verbatim TRCP 4 text in the
> corpus before treating any computed date as final.

### The +3-day service add-on — TRCP 21a

When a period runs from **service** of a paper and service was made by
one of the methods that triggers the add-on (e.g., mail, commercial
delivery, fax, or email — the exact list is drift-prone), **TRCP 21a**
adds **3 days** to the period. Apply the add-on **after** the
underlying TRCP 4 count. **Confirm the current TRCP 21a add-on triggers
against the corpus** — which service methods carry the +3 days is
amended periodically.

## ★ The answer deadline — the Monday rule — TRCP 99

> **★ The answer is not due a flat number of days after service.** In
> District Court and County Court at Law, **TRCP 99** sets the answer
> due **by 10:00 a.m. on the Monday next after the expiration of 20
> days after the date of service.** Count 20 days from service; the
> answer is then due at 10:00 a.m. on the **next Monday** following.
> Compute it with `--rule answer-due`. **Justice Court answers run on a
> different clock — by the end of the 14th day after service (TRCP
> 502.5)** — use `--rule answer-due-justice`. See `tx-first-30-days`.

## Texas legal holidays — Tex. Gov't Code § 662.003

The holidays that trigger the TRCP 4 roll-forward are the **national
holidays** in **Tex. Gov't Code § 662.003**, on which the courts are
closed. The list below is qualitative; the **authoritative,
year-by-year computed set lives in `scripts/case-calendar.py` and the
corpus** — confirm there before relying on a date.

| Holiday | Date rule |
|---|---|
| New Year's Day | January 1 (fixed) |
| Martin Luther King, Jr., Day | 3rd Monday in January |
| Presidents' Day / Washington's Birthday | 3rd Monday in February |
| Memorial Day | Last Monday in May |
| Juneteenth National Independence Day | June 19 (fixed) |
| Independence Day | July 4 (fixed) |
| Labor Day | 1st Monday in September |
| Veterans Day | November 11 (fixed) |
| Thanksgiving Day | 4th Thursday in November |
| Friday after Thanksgiving | Day after the 4th Thursday in November |
| Christmas Day | December 25 (fixed) |

> **Texas specifics to flag.** Texas courts observe **Juneteenth
> National Independence Day (June 19)** and the **Friday after
> Thanksgiving** as court-closed national holidays — roll forward off
> both. Texas also designates **"partial-staffing" state holidays**
> (Confederate Heroes Day, Texas Independence Day, San Jacinto Day, LBJ
> Day) on which state offices run with reduced staff but **courts
> generally do NOT close** — **do not** roll a deadline forward off a
> partial-staffing day. Confirm the operative court-closed set in the
> corpus / script.

## Named rules — quick reference

Run `python3 scripts/case-calendar.py --rules` for the full list. The
most commonly invoked:

| Rule key | Days | Authority |
|---|---|---|
| `answer-due` | Monday rule (+20 → next Mon. 10 a.m.) | TRCP 99 |
| `answer-due-justice` | +14 | TRCP 502.5 (justice court) |
| `interrogatory-response` | +30 | TRCP 197.2 |
| `rfp-response` | +30 | TRCP 196 |
| `rfa-response` | +30 | TRCP 198.2(c) (failure deems admitted) |
| `sj-motion-before-hearing` | −21 | TRCP 166a(c) (counted backward from hearing) |
| `sj-response-before-hearing` | −7 | TRCP 166a(c) (counted backward from hearing) |
| `rule-91a-motion` | +60 | TRCP 91a (from the first pleading asserting the challenged claim) |
| `motion-new-trial` | +30 | TRCP 329b(a), (g) (new trial / to modify, correct, or reform; from signing of judgment) |
| `plenary-power` | +30 | TRCP 329b(d) (extended by timely post-judgment motions) |
| `appeal` | +30 | Tex. R. App. P. 26.1 (use `appeal-with-mnt` for 90 if a post-judgment motion is timely filed) |
| `sol-debt` | see corpus | CPRC § 16.004 (4 years) |
| `sol-personal-injury` | see corpus | CPRC § 16.003 (2 years) |
| `sol-dtpa` | see corpus | Tex. Bus. & Com. Code § 17.565 (2 years) |
| `sol-judgment-dormancy` | see corpus | CPRC § 34.001 (10 years) |

**Answer, notice, and discovery day counts are stable enough to state
in this body as framework anchors; statute-of-limitations periods are
computed on the calendar (anniversary date), so cite the section and
verify the current period.** Always confirm against the corpus / script.

## Example invocations

```
# List every named rule
python3 scripts/case-calendar.py --rules

# Answer due — Monday rule, served 2026-03-12
python3 scripts/case-calendar.py --from 2026-03-12 --rule answer-due

# Justice-court answer — 14 days from service 2026-03-12
python3 scripts/case-calendar.py --from 2026-03-12 --rule answer-due-justice

# Discovery responses — 30 days from service 2026-04-01
python3 scripts/case-calendar.py --from 2026-04-01 --rule interrogatory-response
python3 scripts/case-calendar.py --from 2026-04-01 --rule rfa-response

# Summary-judgment service cutoff — 21 days BEFORE a hearing set 2026-06-15
python3 scripts/case-calendar.py --from 2026-06-15 --rule sj-motion-before-hearing

# Motion for new trial — 30 days after judgment signed 2026-05-20
python3 scripts/case-calendar.py --from 2026-05-20 --rule motion-new-trial

# Ad hoc count — 30 calendar days from service, with roll-forward
python3 scripts/case-calendar.py --from 2026-04-01 --days 30 --mode calendar
```

For a period that runs from service by a TRCP 21a add-on method, add
the **3-day** add-on after the underlying TRCP 4 count.

## Statutes of limitations — point at the codes, do not embed counts

Texas's civil limitations periods are computed on the **calendar
(anniversary) date**, not as a fixed day count. **Cite the section and
verify the current period** rather than hard-coding it here:

| Claim family | Period | Authority |
|---|---|---|
| Debt / breach of contract | 4 years | CPRC § 16.004 |
| Residual (no other period set) | 4 years | CPRC § 16.051 |
| Personal injury / tort | 2 years | CPRC § 16.003 |
| DTPA | 2 years | Tex. Bus. & Com. Code § 17.565 |
| Fraud / debt (discovery rule may apply) | varies | confirm against the corpus |
| Action on / dormancy of a judgment | 10 years | CPRC § 34.001 (and revival § 31.006) |
| Federal — FDCPA | 1 year | 15 U.S.C. § 1692k(d) (federal corpus) |
| Federal — FCRA / TILA | see corpus | federal corpus |

> **Time-barred consumer debt is not revived by a partial payment.**
> Under **Tex. Fin. Code § 392.307** (and the written-acknowledgment
> rule, **CPRC § 16.065**), a payment on out-of-statute consumer debt
> does not restart Texas limitations, and the collector owes a
> statutory notice — a strong defense (see `tx-consumer-debt`). SOL
> **accrual, tolling, and any revival** are **fact-dependent** — verify
> against current law for the specific claim.

## Appeal and post-judgment windows to watch

- **Motion for new trial / to modify, correct, or reform — TRCP 329b.**
  File within **30 days** after the judgment is **signed** (not entered)
  — TRCP 329b(a), (g). A timely such motion **extends the court's
  plenary power** and the appellate timetable. See `tx-post-judgment`.
- **Plenary power — TRCP 329b(d).** The trial court retains plenary
  power to vacate, modify, correct, or reform the judgment for **30
  days** after signing, extended by a timely post-judgment motion.
- **Notice of Appeal — Tex. R. App. P. 26.1.** File within **30 days**
  after the judgment is signed, or **90 days** if any party timely
  files a motion for new trial, to modify, to reinstate, or a request
  for findings of fact. Confirm which event triggers the clock.

## How tx-deadlines composes with the scripts

The arithmetic lives in `scripts/case-calendar.py`, which encodes the
**Tex. Gov't Code § 662.003** court-closed holidays for any year,
applies the TRCP 4 roll-forward off Saturdays / Sundays / holidays, the
TRCP 21a 3-day add-on, and the TRCP 99 Monday-rule answer computation,
and maps named rule keys to `(days, mode, description, authority)`.
Confirm the script's holiday set and rule counts against
`../tx-law-references/references/court-rules/` after any quarterly
corpus refresh.

## Composition

- For format: `tx-statewide-format`
- For the substantive rule or statute text: `tx-law-references`
- For first-response timing (the Monday rule, the JP 14-day answer):
  `tx-first-30-days`
- For discovery timing (the 30-day response window and discovery-level
  cutoffs): `tx-discovery`
- For the hearing / submission notice clock and the TRCP 166a windows:
  `tx-hearings`, `tx-schedule-hearing`
- For post-judgment / appeal timing (TRCP 329b, plenary power):
  `tx-post-judgment`
- For matter-specific deadlines: `tx-consumer-debt`, `tx-family-law`

## References

- `references/rule-4-time-computation.md` — TRCP 4 with notes and the
  TRCP 99 Monday-rule worked example
- `references/section-662.003-holidays.md` — the holidays statute with
  year-by-year computed dates and the partial-staffing carve-out
- `references/sol-table.md` — Texas limitations chart by claim type
  with authority
- `references/named-rules.md` — full list of rule keys with authority

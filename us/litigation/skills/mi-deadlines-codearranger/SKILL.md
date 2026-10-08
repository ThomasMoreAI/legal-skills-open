---
name: mi-deadlines-codearranger
title: Michigan Case Deadlines
description: Use when the user asks about timing or deadlines in a Michigan civil case. Triggers include "Michigan deadline", "when is my answer due in Michigan", "MCR 1.108 compute time", "how do I count days in Michigan court", "answer deadline Michigan", "21 days Michigan", "28 days served by mail Michigan", "MCR 2.108", "MCR 2.107 mail rule", "response to motion Michigan", "MCR 2.119 deadline", "motion for reconsideration 21 days", "statute of limitations Michigan", "SOL on a contract in Michigan", "Michigan court holidays", "Lincoln's Birthday court holiday", "appeal deadline Michigan", "claim of appeal Court of Appeals". Computes calendar-day deadlines under MCR 1.108, applies the MCR 2.107(C) mail add-on, rolls forward off Saturdays / Sundays / MCL 435.101 legal holidays, and maps named rules (answer-due, motion-response, motion-reconsideration, claim-of-appeal, statutes of limitations) to days plus authority.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-deadlines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Michigan Case Deadlines

> **NOT LEGAL ADVICE.** This skill computes deadlines. Independently
> verify in the cited rule or statute, confirm the venue's local
> rules and any standing or scheduling order, and treat no computed
> date as final without checking.

Use this skill to compute deadlines under **MCR 1.108** (time
computation), the Michigan legal-holiday list (**MCL 435.101**), and
the named rules across the Michigan Court Rules and the Revised
Judicature Act. The arithmetic lives in `scripts/case-calendar.py`;
this body is the framework and the pointer to authority.

## MCR 1.108 — computation of time

To count a period stated in days in the Michigan Court Rules, a court
order, or (unless otherwise provided) a statute:

1. **Exclude** the day of the act, event, or default that begins the
   period (e.g., the date of service).
2. **Include** the last day of the period, **unless** it is a
   **Saturday, Sunday, or legal holiday** (or a day the court is
   closed by order) — in which case the period runs to the **end of
   the next day** that is none of those.
3. For periods stated in **weeks, months, or years**, MCR 1.108 fixes
   the ending date by the corresponding calendar unit (e.g., the
   anniversary date for a year); compute these on the calendar, not as
   a fixed day count.

> Frame every day count below as the **current** rule. Confirm the
> number against the verbatim rule text in `mi-law-references` before
> treating any computed date as final.

### MCR 2.107(C) — the mail / e-service add-on

When a period runs from **service** of a paper and service was made by
**mail**, Michigan adds time to the prescribed period. Apply the
add-on **after** the underlying MCR 1.108 count, and confirm the
current number of days and the treatment of **electronic service**
under MCR 2.107(C) in `mi-law-references` — the add-on and the
e-service rules are amended periodically.

## Michigan legal holidays — MCL 435.101

The holidays that trigger the MCR 1.108 roll-forward come from **MCL
435.101**. The list below is qualitative; the **authoritative,
year-by-year computed set lives in `scripts/case-calendar.py` and the
corpus** — confirm there before relying on a date.

| Holiday | Date rule |
|---|---|
| New Year's Day | January 1 (fixed) |
| Martin Luther King, Jr. Day | 3rd Monday in January |
| **Lincoln's Birthday** | **February 12 (fixed)** — Michigan **does** observe |
| Washington's Birthday (Presidents' Day) | 3rd Monday in February |
| Memorial / Decoration Day | Last Monday in May |
| Juneteenth | June 19 (fixed) |
| Independence Day | July 4 (fixed) |
| Labor Day | 1st Monday in September |
| Columbus Day | 2nd Monday in October |
| Veterans' Day | November 11 (fixed) |
| Thanksgiving | 4th Thursday in November |
| Christmas | December 25 (fixed) |

> **Michigan specific to flag.** MCL 435.101 **includes Lincoln's
> Birthday (February 12)** — uncommon among the states — which counts
> for the MCR 1.108 roll-forward. (The day after Thanksgiving is a
> court-closure day in practice, **not** an MCL 435.101 statutory
> holiday — treat it as a court-closed day under MCR 1.108 only if the
> court is in fact closed by order.) Sundays are treated as holidays
> for these purposes.

> **Substitution.** When a fixed-date holiday falls on a weekend,
> confirm the observed day in the corpus / script rather than assuming
> a Friday or Monday observance.

## Named rules — quick reference

Run `python3 scripts/case-calendar.py --rules` for the full list. The
most commonly invoked:

| Rule key | Days | Authority |
|---|---|---|
| `answer-due-personal` | +21 | MCR 2.108(A)(1) (personal service of summons + complaint) |
| `answer-due-mail` | +28 | MCR 2.108(A)(2) (served by mail or served outside Michigan) |
| `motion-response` | per MCR 2.119 | MCR 2.119(C) (response / hearing-notice timing) |
| `motion-reconsideration` | +21 | MCR 2.119(F) (after entry of the order) |
| `mail-add-on` | per rule | MCR 2.107(C) (service by mail) |
| `claim-of-appeal` | +21 / +14 | MCR 7.204(A) (period varies by trigger — verify which applies) |
| `sol-contract` | see corpus | MCL 600.5807 |
| `sol-injury-property` | see corpus | MCL 600.5805 |
| `sol-malpractice` | see corpus | MCL 600.5805 / 600.5838a |

The script encodes the day counts and the holiday roll-forward; always
confirm an unusual number against the cited rule. **Answer deadlines
(MCR 2.108) are stable enough to state in this body; statute-of-
limitations day counts are not — cite the MCL section and read the
current period from the corpus.**

## Answer deadlines — MCR 2.108

These are the load-bearing first-response numbers and are stable:

- **21 days** after **personal service** of the summons and complaint
  (MCR 2.108(A)(1)).
- **28 days** when the defendant was **served by mail** or **served
  outside Michigan** (MCR 2.108(A)(2)).

A timely pre-answer motion under MCR 2.116 alters the time to file a
responsive pleading — see `mi-first-30-days`. Motion practice timing
(notice of hearing, response, reply) is governed by **MCR 2.119**;
read the current intervals from `mi-law-references`.

## Statutes of limitations — point at the RJA, do not embed counts

Michigan's civil limitations periods live in the **Revised Judicature
Act at MCL 600.5801–600.5839**. **Cite the section and read the current
period from the corpus** rather than hard-coding a count here (these
drift and are claim-specific):

| Claim family | Authority |
|---|---|
| Injury to person or property; general tort (incl. shorter periods for certain intentional torts) | MCL 600.5805 |
| Contract (incl. most account / credit; UCC goods periods may displace) | MCL 600.5807 |
| Medical / professional malpractice (with the discovery overlay) | MCL 600.5805 / 600.5838a |
| Real-property / recovery of land | MCL 600.5801 |

SOL **accrual, tolling, and any revival** (by acknowledgment or
part-payment) are **fact-dependent** — verify against current law for
the specific claim. Periods stated in **years** are computed on the
calendar (anniversary) date, not as a fixed day count.

## Appeal and post-judgment windows to watch

- **Motion for reconsideration — MCR 2.119(F).** File within **21
  days** after entry of the order. See `mi-post-judgment`.
- **Claim of appeal to the Court of Appeals — MCR 7.204(A).** The
  appeal period is **21 days** for most final judgments/orders and
  **14 days** for certain triggers; **confirm which period applies**
  to the specific order. See `mi-post-judgment`.

## How `mi-deadlines` composes with the scripts

The body above is the reference; the arithmetic lives in
`scripts/case-calendar.py`, which encodes the **MCL 435.101** holidays
(including **Lincoln's Birthday**) and the set for any year, applies
the MCR 1.108 roll-forward off
Saturdays / Sundays / holidays and the MCR 2.107(C) mail add-on, and
maps named rule keys to `(days, description, authority)`. Run:

```
python3 scripts/case-calendar.py --rules                      # list rule keys
python3 scripts/case-calendar.py --from 2025-03-14 --rule answer-due-personal
```

Confirm the script's holiday set and rule counts against
`mi-law-references` after any quarterly corpus refresh.

## Composition

- For format: `mi-statewide-format`
- For the substantive rule or statute text: `mi-law-references`
- For first-response timing: `mi-first-30-days`
- For discovery timing: `mi-discovery`
- For post-judgment / appeal timing: `mi-post-judgment`
- For matter-specific deadlines: `mi-family-law`, `mi-consumer-debt`,
  `mi-personal-injury`, `mi-landlord-tenant`

## References

- `references/rule-1-108-time-computation.md` — MCR 1.108 + MCR
  2.107(C) with notes
- `references/mcl-435-101-holidays.md` — the holidays statute with
  year-by-year computed dates
- `references/sol-table.md` — RJA limitations chart (MCL 600.5801–
  600.5839) by claim type with authority
- `references/named-rules.md` — full list of rule keys with authority

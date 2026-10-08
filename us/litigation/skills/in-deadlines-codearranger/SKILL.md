---
name: in-deadlines-codearranger
title: Indiana Case Deadlines
description: 'This skill should be used when the user asks "when is my answer due Indiana", "Trial Rule 6 deadline", "T.R. 6(A) time computation", "Indiana 20-day answer", "Indiana 30-day discovery response", "Indiana statute of limitations", "Indiana SOL debt", "IC 34-11-2-9", "Indiana legal holidays", "Good Friday court holiday", "Indiana election day court closed", "compute Indiana deadline", "Indiana deadline calculator", "Indiana appeal deadline", "T.R. 59 30-day", or any related deadline question. Computes calendar-day and court-day deadlines using T.R. 6(A) time-computation rules and IC 1-1-9-1 state holidays. Bundled `case-calendar.py` script encodes named rules and produces precise deadline output. Trigger phrases: "Indiana T.R. 6", "Indiana time computation", "Indiana SOL", "IC 34-11-2-9", "Indiana judicial holidays", "Indiana answer due date", "Indiana 30-day RFP response", "Indiana 1-year T.R. 60(B) window".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-deadlines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Indiana Case Deadlines

This skill computes every deadline in Indiana civil practice
using Trial Rule 6 time-computation rules and IC 1-1-9-1 state
holidays. It is invoked anytime a deadline must be calculated —
whether from a service date, a hearing date, a judgment entry
date, or a statutory accrual.

The bundled `scripts/case-calendar.py` is the computational
counterpart; it encodes all named Indiana deadline rules and
returns the exact next-business-day adjustment. Use it for every
non-trivial deadline.

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> deadlines in Indiana are jurisdictional in many contexts.
> Verify every computed deadline against the rule text and the
> venue court's local rules before relying on it.

## Trial Rule 6 — Time Computation

T.R. 6(A) sets the standard time-computation rules:

> "In computing any period of time prescribed or allowed by these
> rules, by order of the court, or by any applicable statute, the
> day of the act, event, or default from which the designated
> period of time begins to run shall not be included. The last
> day of the period so computed is to be included unless it is:
> (1) a Saturday, (2) a Sunday, (3) a legal holiday as defined by
> state statute, or (4) a day the office in which the act is to
> be done is closed during regular business hours. ..."

Key rules:

1. **Exclude Day 0** (the triggering event)
2. **Include the last day** UNLESS it is a weekend or IC 1-1-9-1
   legal holiday — in which case extend to the next non-holiday
   weekday
3. For periods of **less than 7 days**, intermediate Saturdays,
   Sundays, and legal holidays are EXCLUDED from the count (T.R.
   6(A))
4. For periods of **7 days or more**, intermediate Saturdays /
   Sundays / holidays are INCLUDED in the count

Examples:

- **20-day answer due** (T.R. 6(C)): Served on Monday March 3,
  2025. Day 1 = Tuesday March 4. Day 20 = Sunday March 23. Last
  day Saturday/Sunday → extend to Monday March 24, 2025.
- **5-day notice of deposition** (T.R. 30(B)(1)): less than 7
  days, so intermediate weekends are excluded. Notice served
  Wednesday April 2, 2025 → 5 court days = following Wednesday
  April 9 (skipping Saturday April 5 and Sunday April 6).

## Service-by-mail — no extension under Indiana practice

Important Indiana quirk: **T.R. 6(E) was abolished in 2009**.
Indiana no longer adds 3 days for service by mail; the deadline
runs from the date of service regardless of method. This differs
from federal practice (FRCP 6(d) still adds 3 days for mail
service) and from Oregon (ORCP 10 C adds 3 days for mail).

Practical impact: when a Summons is served by certified mail,
the 20-day answer clock starts on the date the green card is
signed by the defendant. The plaintiff cannot rely on extra mail
days.

## Indiana legal holidays — IC 1-1-9-1

The statewide legal holidays (the days a court office is "closed
during regular business hours" under T.R. 6(A)):

| Holiday | Date | Notes |
|---------|------|-------|
| New Year's Day | January 1 | Saturday → Friday; Sunday → Monday |
| Martin Luther King Jr. Day | 3rd Monday of January | |
| Lincoln's Birthday | February 12 | Observed but courts open |
| Washington's Birthday / Presidents' Day | 3rd Monday of February | |
| **Good Friday** | Friday before Easter | **Indiana-specific**; most states don't observe |
| **Primary Election Day** | 1st Tuesday after 1st Monday in May, even years | **Indiana-specific**; courts closed in even-year primary years |
| Memorial Day | Last Monday of May | |
| Independence Day | July 4 | Saturday → Friday; Sunday → Monday |
| Labor Day | 1st Monday of September | |
| Columbus Day | 2nd Monday of October | Most state courts closed |
| **General Election Day** | 1st Tuesday after 1st Monday in November, even years | **Indiana-specific**; courts closed in even-year general election years |
| Veterans Day | November 11 | Saturday → Friday; Sunday → Monday |
| Thanksgiving | 4th Thursday of November | |
| Day after Thanksgiving | Friday after Thanksgiving | By Governor's proclamation most years; verify |
| Christmas Day | December 25 | Saturday → Friday; Sunday → Monday |

The bundled `scripts/case-calendar.py` encodes these holidays
including the even-year election quirks.

## Named deadline rules

Use these via `case-calendar.py --rule <name>`:

### Initial response
- `answer-due` — 20 days (T.R. 6(C))
- `answer-due-extension` — 20 + 30 days by stipulation (T.R. 6(B))

### Discovery
- `rfp-response` — 30 days from service (T.R. 34(B))
- `interrogatory-response` — 30 days from service (T.R. 33(C))
- `rfa-response` — 30 days from service (T.R. 36(A)); failure
  deems admitted
- `deposition-notice` — 10 days minimum (T.R. 30(B)(1))

### Motion practice
- `summary-judgment-response` — 30 days (T.R. 56(C))
- `summary-judgment-reply` — Indiana T.R. 56(C) gives the movant
  reasonable time; Marion CPC suggests 10-15 days
- `motion-response-typical` — 15 days (Marion CPC default)

### Post-judgment
- `motion-to-correct-error` — 30 days from final judgment (T.R.
  59(C)) — **jurisdictional**
- `tr-59-deemed-denied` — 45 days from filing (T.R. 59(B)) — if
  no ruling, motion is deemed denied
- `tr-60-b-1-3` — 1 year from judgment for grounds (1)-(3)
- `notice-of-appeal-no-tr59` — 30 days from final judgment
- `notice-of-appeal-with-tr59` — 30 days from ruling on T.R. 59
- `judgment-life` — 20 years from entry (IC 34-55-1-2)

### Garnishment / supplemental
- `garnishee-answer` — 20 days from Garnishee Summons service

### Statutes of limitation (defenses)
- `sol-written-contract-property` — 10 years (IC 34-11-2-9)
- `sol-written-contract-money` — 6 years (IC 34-11-2-11)
- `sol-open-account` — 6 years (IC 34-11-2-7)
- `sol-promissory-note` — 6 years (IC 34-11-2-13)
- `sol-personal-injury` — 2 years (IC 34-11-2-4)
- `sol-fraud-discovery` — 6 years from discovery (IC 34-11-2-7)
- `sol-fdcpa` — 1 year from violation (15 U.S.C. § 1692k(d))
- `sol-fcra` — 2 years from discovery or 5-year repose (15
  U.S.C. § 1681p)
- `sol-tila` — 1 year (15 U.S.C. § 1640(e))
- `sol-dcsa-discovery` — 2 years from discovery (IC 24-5-0.5-5)

### FDCPA / Reg F
- `fdcpa-validation-period` — 30 days for consumer dispute (15
  U.S.C. § 1692g; 12 C.F.R. § 1006.34)

## Common deadline computations

| Triggering event | Period | Authority | Result |
|------------------|--------|-----------|--------|
| Served personally | 20 days | T.R. 6(C) | Answer due |
| Served by certified mail (green card date) | 20 days | T.R. 6(C); 4.1 | Answer due |
| RFP served | 30 days | T.R. 34(B) | RFP response |
| RFA served | 30 days | T.R. 36(A) | RFA response; failure = admitted |
| Interrogatories served | 30 days | T.R. 33(C) | Interrogatory response |
| Final judgment entered | 30 days | T.R. 59(C); Ind. App. R. 9(A) | T.R. 59 motion OR Notice of Appeal |
| T.R. 59 motion filed | 45 days | T.R. 59(B) | Deemed denied if no ruling |
| T.R. 59 motion denied | 30 days | Ind. App. R. 9(A) | Notice of Appeal |
| Judgment entered | 1 year | T.R. 60(B)(1)-(3) | T.R. 60(B) motion outer deadline |
| Judgment entered | 20 years | IC 34-55-1-2 | Judgment expires |
| Last written-contract activity (property) | 10 years | IC 34-11-2-9 | SOL bars action |
| Last open-account activity | 6 years | IC 34-11-2-7 | SOL bars action |

## Using the case-calendar.py script

```bash
# Answer due — 20 calendar days from service 2025-03-15
python3 plugins/in-court-docs/scripts/case-calendar.py \
  --from 2025-03-15 --rule answer-due

# RFP response from a March 1 service date
python3 plugins/in-court-docs/scripts/case-calendar.py \
  --from 2025-03-01 --rule rfp-response

# 6-year SOL from last payment on a credit card account
python3 plugins/in-court-docs/scripts/case-calendar.py \
  --from 2019-11-15 --rule sol-open-account

# Custom — 14 calendar days, manual override
python3 plugins/in-court-docs/scripts/case-calendar.py \
  --from 2025-04-15 --days 14 --mode calendar

# List all named rules
python3 plugins/in-court-docs/scripts/case-calendar.py --rules
```

The script handles end-of-period rollover to the next non-holiday
business day, even-year election holidays, and Good Friday.

## Composition

- `in-statewide-format` for the document-level format requirements
- `in-law-references` for the rule and statute authority
- `in-marion` / `in-lake` / `in-county-courts` for local-rule
  deadline variations (some county CMS orders impose tighter
  intermediate deadlines)
- `in-pro-se` for self-represented deadline management
- `in-first-30-days` for the 20-day answer window
- `in-post-judgment` for T.R. 59 and T.R. 60(B) windows
- `in-discovery` for the 30-day discovery response window

## References

- `references/tr6-time-computation.md` — full T.R. 6(A) text with
  worked examples
- `references/legal-holidays.md` — IC 1-1-9-1 holidays with
  observed-day rules
- `references/named-rules.md` — full catalog of named deadline
  rules

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.

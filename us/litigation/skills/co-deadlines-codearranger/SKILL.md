---
name: co-deadlines-codearranger
title: Colorado Case Deadlines
description: This skill should be used when the user asks about timing or deadlines in a Colorado civil case. Triggers include "when is my answer due in Colorado", "C.R.C.P. 6 time computation", "deadline in Colorado court", "Colorado court holidays", "C.R.S. § 24-11-101 holidays", "Colorado statute of limitations", "what's the SOL on a contract in Colorado", "court-day vs calendar-day Colorado", "discovery response deadline Colorado", "motion-response deadline Colorado". Computes calendar-day and court-day deadlines under C.R.C.P. 6(a), excludes Colorado state legal holidays under C.R.S. § 24-11-101, applies the Saturday/Sunday/holiday roll-forward rule under C.R.C.P. 6(a)(1)(C), and maps named rules (answer-due, discovery-response, motion-reply, SJ-motion, appeal, garnishment cycle, family-law 91-day waiting period) to days plus authority.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-deadlines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Colorado Case Deadlines

> **NOT LEGAL ADVICE.** This skill computes deadlines. Always
> independently verify in the cited rule or statute and confirm with
> the assigned judge's practice standards before treating any
> computed date as final.

Use this skill to compute deadlines under C.R.C.P. 6(a) (time
computation), the Colorado legal-holiday list (C.R.S. § 24-11-101),
and the various named rules across the C.R.C.P., C.R.S., and
applicable federal law.

## C.R.C.P. 6(a) — time computation

C.R.C.P. 6(a) governs how to count time intervals stated in
Colorado statutes and rules:

1. **Exclude** the day of the triggering event (the event that
   starts the period running, e.g., service date)
2. **Include** every intermediate calendar day (no court-day skip
   for periods of 7+ days as of the 2012 rewrite)
3. **Include** the last day, **unless** it falls on a **Saturday,
   Sunday, or Colorado legal holiday** — in which case the period
   extends to the **next** day that is not one of those
   (C.R.C.P. 6(a)(1)(C))

For periods of fewer than 7 days that pre-date the 2012 rewrite,
older case law applied court-day counting; modern C.R.C.P. 6 uses
calendar-day counting throughout, with the roll-forward rule at the
end. Some statutes outside the C.R.C.P. retain court-day counting
explicitly (e.g., certain post-judgment garnishment intervals); read
the controlling rule.

## Colorado legal holidays — C.R.S. § 24-11-101

The following are Colorado state legal holidays:

| Holiday | Date |
|---------|------|
| New Year's Day | January 1 |
| Martin Luther King, Jr. Day | 3rd Monday in January |
| Presidents' Day (Washington's Birthday) | 3rd Monday in February |
| Memorial Day | Last Monday in May |
| Juneteenth | June 19 (added 2022 by SB22-228) |
| Independence Day | July 4 |
| Labor Day | 1st Monday in September |
| Frances Xavier Cabrini Day | 1st Monday in October (replaced Columbus Day per H.B. 20-1031, effective 2020) |
| Veterans Day | November 11 |
| Thanksgiving Day | 4th Thursday in November |
| Christmas Day | December 25 |

**Saturday holiday observance**: shifts to the preceding Friday
(C.R.S. § 24-11-101(2)). **Sunday holiday observance**: shifts to
the following Monday.

> ⚠ **Note**: Colorado does **NOT** observe the day after
> Thanksgiving as a state legal holiday (contrast Washington, which
> does, under RCW 1.16.050). Some judicial districts close
> administratively on the day after Thanksgiving but the C.R.S.
> § 24-11-101 list controls C.R.C.P. 6(a) arithmetic.

> ⚠ **Cesar Chavez Day** (March 31) is recognized in Colorado as a
> day of observance but is **not** a state legal holiday — it does
> not affect deadline counting.

## Named rules — quick reference

Use `scripts/case-calendar.py --rules` to print the full list. Most
commonly invoked:

| Rule key | Days | Mode | Authority |
|---|---|---|---|
| `answer-due` | +21 | calendar | C.R.C.P. 12(a)(1) |
| `answer-due-out-of-state` | +35 | calendar | C.R.C.P. 12(a)(2) |
| `response-to-amended` | +14 | calendar | C.R.C.P. 15(a) |
| `discovery-response` | +30 | calendar | C.R.C.P. 33/34/36 |
| `rfa-deemed-admitted` | +35 | calendar | C.R.C.P. 36(a) + 6(e) |
| `case-management-conference` | +49 | calendar | C.R.C.P. 16(b) |
| `rule-26-disclosures` | +28 | calendar | C.R.C.P. 26(a)(1) |
| `121-response` | +21 | calendar | C.R.C.P. 121 § 1-15(1)(b) |
| `121-reply` | +7 | calendar | C.R.C.P. 121 § 1-15(1)(d) |
| `summary-judgment-motion` | -91 | calendar | C.R.C.P. 56(c) |
| `motion-reconsideration` | +14 | calendar | C.R.C.P. 59(a) |
| `rule-60-b-1-3` | +182 | calendar | C.R.C.P. 60(b) outer |
| `notice-of-appeal` | +49 | calendar | C.A.R. 4(a) |
| `garnishment-answer` | +7 | calendar | C.R.S. § 13-54.5-106(2) |
| `exemption-claim` | +14 | calendar | C.R.S. § 13-54.5-108 |
| `udma-waiting-period` | +91 | calendar | C.R.S. § 14-10-106(1)(a)(III) |
| `udma-residency` | +91 | calendar | C.R.S. § 14-10-106(1)(a)(I) |
| `16-2-sfs` | +42 | calendar | C.R.C.P. 16.2(e)(2) |
| `fdcpa-validation` | +30 | calendar | 15 U.S.C. § 1692g(a)(3) |
| `fdcpa-sol` | +365 | calendar | 15 U.S.C. § 1692k(d) |
| `sol-contract` | +2191 (~6y) | calendar | C.R.S. § 13-80-103.5(1)(a) |
| `sol-tort` | +730 (~2y) | calendar | C.R.S. § 13-80-102 |
| `sol-ccpa` | +1096 (~3y) | calendar | C.R.S. § 6-1-115 |
| `sol-cfdcpa` | +365 | calendar | C.R.S. § 5-16-113(4) |

## Statute of limitations — primary Colorado claims

Colorado SOL provisions are scattered across Title 13. The key
buckets:

| Claim type | SOL | Authority | Notes |
|---|---|---|---|
| Liquidated debt / written instrument | **6 years** | C.R.S. § 13-80-103.5(1)(a) | Most consumer-credit-card claims; the "discovery rule" can apply |
| Promissory note | **6 years** | C.R.S. § 13-80-103.5(1)(a) | |
| Open account (oral / implied) | 6 years | C.R.S. § 13-80-103.5(1)(a) | Some debt-buyer cases argue 3 years under § 13-80-101; the post-2003 amendment moved most accounts to 6 |
| General tort | 2 years | C.R.S. § 13-80-102 | Includes negligence, fraud (start at discovery) |
| Personal-injury motor vehicle | 3 years | C.R.S. § 13-80-101(1)(n) | |
| Libel / slander | 1 year | C.R.S. § 13-80-103(1)(a) | |
| CCPA | 3 years from accrual | C.R.S. § 6-1-115 | |
| CFDCPA | 1 year from violation | C.R.S. § 5-16-113(4) | |
| FDCPA | 1 year from violation | 15 U.S.C. § 1692k(d) | Federal — applies in Colorado courts as well |
| Adverse possession | 18 years | C.R.S. § 38-41-101 | Colorado real-property quirk |
| Eviction (FED) | 2 years on the debt; no SOL on possession | C.R.S. § 38-12 / § 13-40 | |
| Foreign judgments | 6 years | C.R.S. § 13-80-103.5(1)(b) | |
| Wrongful death | 2 years | C.R.S. § 13-80-102(1)(d) | |

## Tolling and revival

- **Tolling for minority / disability**: C.R.S. § 13-81-103 tolls
  SOL during a minor's minority or during certain disabilities
- **Tolling for fraudulent concealment**: discovery rule applies in
  fraud claims (start counting at discovery, not accrual)
- **Partial payment / written acknowledgment**: a written
  acknowledgment of a debt or a partial payment restarts the SOL
  clock under C.R.S. § 13-80-113 — important in debt-buyer cases
  where the creditor may rely on a recent "promise to pay" to
  revive a stale claim. *Hassler v. Account Brokers of Larimer Cnty.,
  Inc.*, 2012 CO 24, addresses this; verify still good law.

## Examples

### "When is my answer due if I was served personally in Denver on Friday, March 14, 2025?"

```
$ python3 scripts/case-calendar.py --from 2025-03-14 --rule answer-due
Answer due (Colorado resident, in-state service)
Deadline: Friday, April 04, 2025
  From: Friday, March 14, 2025
  21 calendar days after
  Authority: C.R.C.P. 12(a)(1)
```

### "What is the response deadline for a motion served Monday, April 7, 2025?"

```
$ python3 scripts/case-calendar.py --from 2025-04-07 --rule 121-response
Response to motion under C.R.C.P. 121 § 1-15(1)(b)
Deadline: Monday, April 28, 2025
  From: Monday, April 07, 2025
  21 calendar days after
  Authority: C.R.C.P. 121 § 1-15(1)(b)
```

### "If I file for divorce on Monday, July 14, 2025, when is the earliest a decree can enter?"

```
$ python3 scripts/case-calendar.py --from 2025-07-14 --rule udma-waiting-period
UDMA mandatory 91-day waiting period before decree
Deadline: Monday, October 13, 2025
  From: Monday, July 14, 2025
  91 calendar days after
  Authority: C.R.S. § 14-10-106(1)(a)(III)
```

## How `co-deadlines` composes with the scripts

The skill body above is the reference. The actual arithmetic lives in
`scripts/case-calendar.py`, which:

- Encodes the C.R.S. § 24-11-101 holidays
- Implements `co_holidays(year)` for any year
- Provides `is_court_day(d)`, `roll_forward_rule(d)`,
  `add_calendar_days`, `add_court_days`
- Exposes a `RULES` dictionary mapping named rule keys to
  `(days, mode, description, authority)`

Use `scripts/case-calendar.py --rules` for the canonical list and
`scripts/case-calendar.py --from YYYY-MM-DD --rule <key>` for any
specific computation.

## Composition

- For format: `co-statewide-format`
- For the substantive rule: `co-law-references`
- For first-response timing: `co-first-30-days`
- For motion timing: `co-discovery`, `co-schedule-hearing`
- For post-judgment timing: `co-post-judgment`
- For family-law specific deadlines: `co-family-law`

## References

- `references/crcp-6-time-computation.md` — full text of C.R.C.P.
  6(a) with notes
- `references/crs-24-11-101-holidays.md` — full text of the
  holidays statute with year-by-year computed dates
- `references/sol-table.md` — comprehensive SOL chart by claim type
  with case authority
- `references/tolling.md` — tolling provisions and case authority
- `references/named-rules.md` — full list of rule keys with
  authority

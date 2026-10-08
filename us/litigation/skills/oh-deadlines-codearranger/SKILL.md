---
name: oh-deadlines-codearranger
title: Ohio Case Deadlines
description: Use to compute Ohio court deadlines — Civ. R. 6 time computation, R.C. 1.14 legal holidays, named-rule catalog. Triggers include 'Ohio deadline', 'Ohio Civ. R. 6 time computation', 'R.C. 1.14 holidays', 'Ohio SOL', 'Ohio statute of limitations', 'when is my Ohio answer due', 'Ohio judgment renewal deadline'. Covers the Civ. R. 6 time-computation framework, R.C. 1.45 weekend-roll-forward, R.C. 1.14 holiday catalog (including Columbus Day still observed in Ohio), and the named-rule catalog (28-day answer, 6-year written-contract SOL, 2-year CSPA SOL, 5-year judgment enforcement SOL, etc.).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-deadlines
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Ohio Case Deadlines

> **NOT LEGAL ADVICE.** Deadlines are jurisdictional in
> many contexts (Civ. R. 60(B) 1-year cap, App. R. 4 30-day
> appeal). Always verify with the case-management order
> and per-court Loc. R.

## Time computation framework

### Civ. R. 6(A) — basic rule

- Exclude the day of the triggering event
- Include the last day, unless it falls on Saturday,
  Sunday, or a legal holiday, in which case **roll forward
  to the next business day**
- Periods of less than 7 days exclude intermediate
  weekends and holidays
- Service by mail adds **3 days** under Civ. R. 6(D)

### R.C. 1.45 — weekend rollover

Statutory deadlines that fall on Saturday, Sunday, or a
legal holiday roll forward to the next business day. This
parallels Civ. R. 6(A) for procedural deadlines.

## Ohio legal holidays (R.C. 1.14)

- New Year's Day (January 1)
- Martin Luther King, Jr. Day (3rd Monday in January)
- Washington's Birthday (3rd Monday in February)
- Memorial Day (last Monday in May)
- **Juneteenth (June 19)** — added 2024
- Independence Day (July 4)
- Labor Day (1st Monday in September)
- **Columbus Day (2nd Monday in October)** — Ohio still
  observes Columbus Day as a legal holiday
- Veterans Day (November 11)
- Thanksgiving Day (4th Thursday in November)
- Christmas Day (December 25)

Notable: Ohio does NOT observe the day after Thanksgiving
as a statewide legal holiday (some local Common Pleas
courts close on a discretionary basis).

## Named-rule catalog

### Procedural rules

| Rule | Days | Citation |
|---|---|---|
| Answer to complaint | 28 calendar | Civ. R. 12(A)(1) |
| Reply to counterclaim | 28 calendar | Civ. R. 12(A)(2) |
| Motion-response (typical local rule) | 14 calendar | Civ. R. 6(C)(1) where adopted |
| Summary-judgment notice | 14 calendar minimum | Civ. R. 56(C) |
| Magistrate-decision objection | 14 calendar | Civ. R. 53(D)(3)(b)(i) |
| Motion for new trial | 28 calendar | Civ. R. 59(B) |
| Motion to vacate (60(B)(1)-(3)) | 1 year cap | Civ. R. 60(B) |
| Notice of appeal | 30 calendar | App. R. 4(A) |

### Statutes of limitations

| Claim | Years | R.C. |
|---|---|---|
| Written contract | 6 | R.C. 2305.06 |
| Oral / implied contract | 4 | R.C. 2305.07 |
| Conversion / fraud | 4 | R.C. 2305.09 |
| Personal injury (bodily) | 2 | R.C. 2305.10 |
| Libel / slander | 1 | R.C. 2305.11 |
| Ohio Consumer Sales Practices Act | 2 | R.C. 1345.10 |
| Wrongful death | 2 | R.C. 2125.02(D) |
| Medical malpractice | 1 (4 absolute repose) | R.C. 2305.113 |
| Judgment enforcement (Ohio judgment) | 5 (renewable) | R.C. 2329.07 |

### Family-law deadlines

| Item | Period | R.C. |
|---|---|---|
| Divorce residency — state | 6 months | R.C. 3105.03 |
| Divorce residency — county | 90 days | R.C. 3105.03 |
| Dissolution waiting period | 30-90 days | R.C. 3105.64 |
| Child-support modification threshold | 10% change | R.C. 3119.79 |

## Service-by-mail add-on (Civ. R. 6(D))

When a paper is served by mail, the responding party gets
an extra **3 days** added to the response period. This
applies to most filings but NOT to motion deadlines under
some local rules — verify per-court.

## Computing deadlines — the script

Use `plugins/oh-court-docs/scripts/case-calendar.py`:

```bash
# 28-day answer from 2025-04-15
python3 case-calendar.py --from 2025-04-15 --rule answer-due

# 6-year SOL on written contract
python3 case-calendar.py --from 2019-04-15 --rule sol-written-contract

# List all named rules
python3 case-calendar.py --rules
```

## Composition with other oh- skills

- `oh-first-30-days` — 28-day answer clock
- `oh-discovery` — 28-day response window for Civ. R. 33
  interrogatories, 34 RFPs, 36 RFAs
- `oh-post-judgment` — 28 days for Civ. R. 59, 1 year for
  Civ. R. 60(B), 5 years for R.C. 2329.07 enforcement
- `oh-consumer-debt` — 6-year R.C. 2305.06 SOL, 2-year R.C.
  1345.10 CSPA SOL
- `oh-family-law` — divorce residency + dissolution waiting

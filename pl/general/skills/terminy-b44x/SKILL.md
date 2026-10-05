---
name: terminy-b44x
title: Terminy, dni robocze i święta
description: Polish working days, public holidays and deadlines, computed offline with legal citations. Count working days between dates, get the monthly working-time norm (wymiar czasu pracy) per art. 130 Kodeksu pracy, list statutory holidays (including Wigilia 24 December from 2025), check a single day, compute a deadline such as invoice payment terms (date + N days, moved to the next working day under art. 115 KC), and list monthly tax and social-security deadlines (ZUS, PIT, CIT, VAT/JPK_V7M, PPK) moved off weekends and holidays per art. 12 § 5 Ordynacji podatkowej. Use whenever the user asks e.g. "ile dni roboczych w październiku", "wymiar czasu pracy grudzień", "do kiedy zapłacić ZUS", "termin VAT za wrzesień", "czy 24 grudnia jest wolny", "termin płatności 14 dni od faktury", "kiedy wypada Boże Ciało".
author: b44x
author_url: https://github.com/b44x/ai-polish-skills/tree/dev/skills/terminy
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: pl
practice: general
language: en
tags: [dni-robocze, swieta, wymiar-czasu-pracy, terminy, zus, vat, pit, ksiegowosc]
sources:
- title: Output
  path: references/output.md
---

# Terminy, dni robocze i święta

Computes Polish working days, holidays, working-time norms and tax/ZUS deadlines with
`scripts/terminy.py`. Fully offline and deterministic. Always outputs structured JSON with the
legal basis of each rule.

## Running the script

Run from this skill's directory (or use relative path from repo root):

| OS | Command |
|---|---|
| Linux / macOS | `python3 scripts/terminy.py <command> …` |
| Windows | `py scripts/terminy.py <command> …` (or `python`) |

Zero external dependencies required (standard library only).

## Workflow

1. **Working days and working-time norm in a month** ("ile dni roboczych w październiku", "wymiar czasu pracy grudzień 2026"):
   `python3 scripts/terminy.py month 2026-12`
   - Report `workingDays` and `workingTimeNormHours`, and show `calculation`.
   - A holiday falling on Saturday reduces the norm too (art. 130 § 2 KP). Mention `saturdayHolidays` when present.

2. **Tax and ZUS deadlines** ("do kiedy ZUS za wrzesień", "termin VAT"):
   `python3 scripts/terminy.py deadlines 2026-09`
   `python3 scripts/terminy.py deadlines 2026-09 --only vat zus-pozostali`
   - The argument is the **settlement month**; the deadlines fall in the following month.
   - ZUS depends on the payer: `zus-pozostali` (JDG, partnerships) = 20th, `zus-osoby-prawne` (sp. z o.o., S.A.) = 15th,
     `zus-jednostki-budzetowe` = 5th. Ask the user which applies if unclear.
   - When `shifted` is true, say the deadline moved from `nominalDate` because of a weekend or holiday.

3. **Payment term / any "N days from" deadline** ("termin płatności 14 dni od 2026-10-15"):
   `python3 scripts/terminy.py add 2026-10-15 14`
   `python3 scripts/terminy.py add 2026-12-22 5 --workdays` (N working days)

4. **Working days between two dates:** `python3 scripts/terminy.py workdays 2026-10-01 2026-12-31`

5. **Holidays and single days:** `python3 scripts/terminy.py holidays --year 2027`, `python3 scripts/terminy.py day 2026-12-24`

## Commands

| Command | Description | Returns |
|---|---|---|
| `month <RRRR-MM>` | Working days and working-time norm (full-time, 1-month period) | `workingDays`, `workingTimeNormHours`, `holidays`, `saturdayHolidays`, `calculation` |
| `deadlines <RRRR-MM> [--only ID…]` | ZUS, PIT, CIT, VAT (JPK_V7M), PPK deadlines for a settlement month | `deadlines[]` with `deadline`, `nominalDate`, `shifted`, `legalBasis` |
| `add <date> <N> [--workdays]` | Date + N calendar days (moved to the next working day) or + N working days | `deadline` / `result`, `shifted`, `rule` |
| `workdays <from> <to>` | Working days between two dates, inclusive | `workingDays`, `calendarDays`, `holidays` |
| `holidays [--year Y]` | Statutory holidays of a year | `holidays[]` with `date`, `weekday`, `name` |
| `day <date>` | Is the date a working day or a holiday | `isWorkingDay`, `holiday`, `nextWorkingDay` |

Legal basis of every rule: [references/output.md](references/output.md).

## Exit codes

JSON goes to stdout; errors go to stderr as `{"error": "...", "type": "..."}`.

| Code | Meaning | What to do |
|---|---|---|
| `0` | Success | Use the JSON output |
| `2` | Not found | No deadline matches the `--only` filter |
| `64` | Bad usage / validation | Invalid date (expected RRRR-MM-DD) or month (RRRR-MM), year outside 1990–2100 |

## Rules

- The working-time norm assumes a full-time employee and a one-month settlement period. For other
  settlement periods or part-time contracts, say so and compute proportionally only if the user asks.
- The deadlines cover standard monthly settlements. They do not cover quarterly settlements, the
  cash method (metoda kasowa), exceptions in specific cases, or changes to the law after
  `rulesVerified`. For current law use the `prawo` skill, and do not present the output as tax advice.
- Regional or company days off (e.g. a day off in exchange for a Saturday holiday) are not statutory
  holidays and are not included.

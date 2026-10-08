---
name: tool-date-tool-deadline-calculator-sboghossian
title: Tool — Legal Deadline Calculator
description: Use when computing legal deadlines — filing deadlines, response periods, statutes of limitations, contractual notice periods — with full awareness of jurisdiction-specific court rules, public holidays (including Eid al-Fitr and Eid al-Adha with variable lunar dates), court vacation periods, and weekend conventions (Friday-Saturday in pre-2013 KSA; Saturday-Sunday in UAE and most GCC). Returns the due date, intermediate milestones, and a list of holidays handled.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-date-tool-deadline-calculator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Tool — Legal Deadline Calculator

## What it does

Computes legal deadlines with jurisdiction-aware handling of court rules, public holidays, religious holidays (Hijri calendar), weekend conventions, and court vacation periods. Designed to handle the complexity of MENA legal calendars — where Eid dates vary by lunar sighting, weekends differ from Western norms, and court vacation schedules vary by emirate and court type.

## Inputs

| Field | Type | Required | Notes |
|---|---|---|---|
| `startDate` | ISO date | Yes | Trigger date — service date, judgment date, notice date |
| `period` | number | Yes | Duration of the deadline period |
| `periodUnit` | enum | Yes | `days`, `months`, `years` |
| `basis` | enum | Yes | `calendar` (count all days), `business` (exclude weekends), `court` (exclude weekends + court holidays + vacations) |
| `jurisdiction` | enum | Yes | `UAE-Dubai`, `UAE-AbuDhabi`, `UAE-Federal`, `KSA`, `LB`, `EG`, `DIFC`, `ADGM`, `UK`, `FR`, `EU`, `QFC` |
| `courtType` | enum | No | `civil`, `commercial`, `criminal`, `employment`, `arbitration` |
| `hijriAwareness` | bool | No | Default `true` for MENA jurisdictions — include Eid and Islamic public holidays |

## Weekend conventions by jurisdiction

| Jurisdiction | Weekend days | Note |
|---|---|---|
| UAE | Saturday + Sunday | Changed from Fri-Sat in January 2022 (UAE Federal government) |
| KSA | Friday + Saturday | Changed from Thu-Fri in June 2013 |
| Lebanon | Saturday + Sunday | Standard; courts often closed Friday afternoon |
| Egypt | Friday + Saturday | Government offices; some private sector follows Fri-Sat |
| DIFC / ADGM | Saturday + Sunday | As common-law courts aligned with global financial markets |
| UK | Saturday + Sunday | Standard |
| France | Saturday + Sunday | Standard |

**Critical:** The UAE weekend change in January 2022 affects deadline calculations that span that date. The system must handle pre-2022 and post-2022 UAE deadlines correctly.

## Public holiday categories

### Fixed secular holidays (by jurisdiction)

| Jurisdiction | Key fixed holidays |
|---|---|
| UAE | National Day (2 Dec), Commemoration Day (30 Nov), New Year's Day (1 Jan) |
| KSA | National Day (23 Sep), Founding Day (22 Feb) |
| Lebanon | Independence Day (22 Nov), National Day for Martyrs (6 May) |
| UK | Bank holidays per England & Wales / Scotland / NI calendar |
| France | Bastille Day (14 Jul), All Saints, Armistice Day, etc. |

### Variable Islamic holidays (Hijri calendar)

These dates shift each Gregorian year; always use the confirmed official announcement rather than astronomical calculation for deadline purposes:

| Holiday | Approx. Gregorian pattern | Duration |
|---|---|---|
| **Eid al-Fitr** | End of Ramadan (~April/May in 2024–2026) | 3–4 days public holiday; courts typically closed 7–10 days |
| **Eid al-Adha** | ~70 days after Eid al-Fitr | 3–4 days public holiday; courts closed 7–10 days |
| **Islamic New Year (Muharram 1)** | ~July/August range | 1–2 days |
| **Prophet's Birthday (Mawlid)** | ~September/October range | 1 day |

**Warning:** Official Eid dates are announced by the respective national authority (UAE MOCA, KSA Supreme Court, Lebanon Ministry of Justice) and may differ by 1 day between countries based on moon sighting. Use the official declaration when available; if unavailable, use the conservative (extended) estimate.

### Court vacation periods

| Jurisdiction | Main vacation periods | Note |
|---|---|---|
| UAE (Dubai Courts) | Summer recess (~July–August, duration varies); Eid breaks | Confirm per current court circular |
| KSA | Summer recess (~July–August); Eid breaks | CJLNA portal for current schedule |
| Lebanon | Summer recess (August); Easter; Eid | Lebanese court vacations are extended; critical to verify |
| DIFC Courts | No formal summer recess; standard UAE public holidays apply | DIFC Practice Direction governs |
| ADGM Courts | Standard UAE public holidays; limited formal vacation | ADGM Court Regulations |
| UK | Easter, Summer (1 Aug – 30 Sep), Christmas recesses | CPR defines term/vacation periods |
| France | Legal vacations (vacances judiciaires) apply; check court-specific schedule | |

## Computation logic

```
FUNCTION computeDeadline(startDate, period, periodUnit, basis, jurisdiction):
  rawDate = addPeriod(startDate, period, periodUnit)
  
  IF basis == "calendar":
    RETURN rawDate
  
  IF basis IN ("business", "court"):
    holidays = loadHolidays(jurisdiction, startDate, rawDate)
    weekendDays = loadWeekendConvention(jurisdiction, startDate, rawDate)
    nonWorkingDays = union(holidays, weekendDays)
    
    IF basis == "court":
      courtVacationDays = loadCourtVacations(jurisdiction, courtType)
      nonWorkingDays = union(nonWorkingDays, courtVacationDays)
    
    adjustedDate = rawDate
    WHILE adjustedDate IN nonWorkingDays:
      adjustedDate = next business day(adjustedDate, jurisdiction)
    
    RETURN adjustedDate
```

## Output schema

```json
{
  "jurisdiction": "UAE-Dubai",
  "startDate": "2026-05-14",
  "period": "21 days",
  "basis": "court",
  "dueDate": "2026-06-10",
  "intermediateDeadlines": [
    { "label": "7-day interim milestone", "date": "2026-05-21" }
  ],
  "holidaysHandled": [
    { "date": "2026-05-29", "name": "Eid al-Adha Eve", "source": "UAE MOCA announcement" }
  ],
  "advisoryWarnings": [
    "Eid al-Adha dates are confirmed by official announcement; this calculation uses the 2026 provisional dates — verify against the official UAE MOCA circular before the deadline approaches"
  ]
}
```

## Critical warnings

- **Eid dates are not fixed:** Never hard-code Eid dates more than one year in advance. Refresh the holiday database annually, and flag to the user if the deadline falls close to an Eid window where official dates have not yet been announced.
- **Court vacation verification:** Court vacation schedules are published annually and may change. Flag that vacation periods should be confirmed from the official court website or court circular.
- **UAE weekend change (Jan 2022):** Deadlines that straddle this date require correct pre/post handling.
- **Hijri calendar:** Some Lebanese and Egyptian contractual deadlines are expressed in Hijri months; support Hijri-to-Gregorian conversion when needed.

## Always combine with

[[tool-calendar-integration]] — to block the computed deadline in the lawyer's calendar.
[[pa-workflow-litigation]] — for matter-level deadline management.
[[efirm-deadline-tracker]] — for firm-wide deadline docketing.

## Related skills

- [[tool-calendar-integration]]
- [[pa-workflow-litigation]]
- [[efirm-deadline-tracker]]

---
name: ca-schedule-hearing-codearranger
title: Reserve a Hearing Date (California)
description: Use when reserving a motion hearing date in a California superior court. Triggers include "reserve a hearing date", "reserve a hearing in LASC", "Court Reservation System", "CRS LASC", "Department 302 reservation San Francisco", "law-and-motion calendar California", "ex parte hearing California", "Orange County civil hearing reservation", "how do I schedule a motion in [county] superior court", "earliest available hearing date", "Department 1 LASC". Drafts the contact email, identifies the reservation portal, computes the earliest viable hearing date given the CCP § 1005(b) court-day notice arithmetic, and produces a reservation script appropriate for the specific department. Layers on top of `ca-deadlines` for service-deadline back-computation, and on `ca-lasc` / `ca-sfsc` / `ca-county-courts` for venue-specific protocols.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-schedule-hearing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Reserve a Hearing Date (California)

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> verify against current rules and case law before filing.

## When to use

When a user has a motion ready to file (or being drafted) and
needs to reserve a hearing date *before* serving the Notice of
Motion. Almost every California superior court department
requires the date to be reserved first — serving the notice
with a date that turns out to be unavailable in the department
means re-noticing the motion and re-starting the CCP § 1005(b)
clock.

## The CCP § 1005(b) backstop

Compute the **earliest** viable hearing date by adding to today
(or the planned service date):

- **16 court days** (motion-notice minimum, CCP § 1005(b))
- Plus extensions for service method:
  - **+5 calendar days** for in-state mail (CCP § 1013(a))
  - **+2 court days** for electronic service (CCP § 1010.6(a)(3)(B))
  - **+2 court days** for fax or express mail (CCP § 1013(c), (d))
  - **+10 calendar days** for out-of-state mail (CCP § 1013(a))

Then find the next hearing day in the department's calendar that
falls at or after that minimum date. For SJ motions, use the
**75-calendar-day** minimum under CCP § 437c(a)(2) instead.

The `scripts/case-calendar.py` helper computes these:

```
python3 plugins/ca-court-docs/scripts/case-calendar.py \
    --from 2026-05-13 --rule motion-notice-min
```

## Court-by-court reservation protocols

### Los Angeles Superior Court (LASC)

- **Portal**: LASC Court Reservation System (CRS) at
  lacourt.org → "Self-Help" → "Court Reservation System"
- **Department**: assigned at filing. New unlimited civil cases
  go to "Dept. 1" / "Dept. SSC" (case-management) until the CMC,
  then to a long-cause department.
- **Reservation rules** (per LASC Local Rules ch. 3):
  - Reserve before serving the notice
  - Each department has its own law-and-motion calendar days
    (typically two days/week)
  - Reservation creates a "Reservation ID" that goes in the
    Notice of Motion caption
- **Fee**: A reservation fee (~$60-$95 depending on motion type)
  is collected at the time of reservation; same money applies to
  filing fee.
- **Reservation lookup**: LASC posts the upcoming
  law-and-motion calendar by department; check the department's
  schedule for the earliest open slot at or after the minimum
  date.

### San Francisco Superior Court (SFSC)

- **Portal**: SFSC online reservation via sfsuperiorcourt.org
  → "Reserve a Hearing Date".
- **Dept. 302**: the general civil law-and-motion department at
  the Civic Center Courthouse, 400 McAllister St. Most non-
  family / non-probate civil motions go here.
- **Reservation rules**:
  - Reserve before serving notice
  - Dept. 302 has its own posted calendar; tentative rulings
    appear day before (CRC 3.1308(a)(1), SFSC Local Rule 8.3)
- **Specialized departments**: complex civil (Dept. 304), real
  property (Dept. 501), small claims, etc. — different
  reservation protocols.

### Orange County (OCSC)

- **Portal**: OCSC's civil reservation function at occourts.org
  → "Civil" → "Reserve a Hearing".
- Some departments require email or call to the courtroom
  clerk for civil law-and-motion.
- **Note**: pre-2024 reservations were court-clerk-mediated;
  most are now self-serve online.

### San Diego County (SDSC)

- **Portal**: sdcourt.ca.gov reservation tool.
- Civil law-and-motion departments vary by case type and
  courthouse (Central, North County, South County, East
  County, Family).
- Tentative rulings posted day before per SDSC local rules.

### Santa Clara County (SCSC)

- **Portal**: scscourt.org online reservation.
- Complex civil cases routed to specialized departments at
  the Downtown Superior Court.

### Other counties

For counties without an online reservation portal, the
reservation protocol is typically:

1. Identify the department assigned to the case (look at the
   "Case Management Conference" or initial case-assignment
   notice).
2. Call the courtroom clerk during business hours.
3. State the case name, case number, and motion type.
4. Request the next available hearing date on or after the
   minimum date.
5. Confirm via follow-up email if requested.

## Reservation script (LASC example)

Used when the user prefers email contact or after an online
reservation needs confirmation:

```
SUBJECT: Reservation Request — [Case Name], [Case No.]

Dear Department [N] Clerk:

I represent myself in the above-captioned matter. I am preparing
a [Motion Type] under [Code Civ. Proc., § __].

Per CCP § 1005(b), the earliest hearing date with [SERVICE
METHOD] would be [DATE_FROM_CASE_CALENDAR]. Please reserve
the next available date in Department [N] on or after that
date.

If a reservation fee is required, please let me know the amount
and payment method.

Thank you,
[Name]
In Pro Per
[Phone] / [Email]
```

## Department 1 (new-case routing)

LASC routes most unlimited civil cases to **"Dept. 1"** (formerly
"Department 1 / SSC"; aka the Master Calendar Court) for case-
management purposes until the CMC sets the long-cause department.
Motions filed before the case is sent to a long-cause department
are heard in Dept. 1. Verify before reserving — Dept. 1 has its
own protocols and a typically heavy calendar.

## Ex parte applications

Different protocol — most California superior courts require
ex parte applications to be set on 24 hours' notice (CRC 3.1203),
with notice to opposing party by 10:00 a.m. the court day
before the hearing. Ex parte calendars are typically heard once
per day in each civil department. See `ca-draft-motion` for ex
parte specifics.

## Common pitfalls

- Serving the Notice of Motion before reserving the date —
  many departments will reject the filing or require re-notice.
- Computing the 16-day minimum in **calendar** days instead of
  **court** days (CCP § 1005(b) requires court days).
- Forgetting to add the service-method extension (mail 5 cal,
  e-service 2 court, etc.).
- Reserving for the wrong department (the case may have been
  transferred to a long-cause department).
- Failing to check the department's tentative-ruling regime
  before reserving (CRC 3.1308) — a date with no oral argument
  needed may not require a contested-hearing reservation.
- Importing Oregon's JA email protocol or Washington's KCDC
  CivilMGT date-request email — California reservation
  systems are different.

## Cross-references

- `ca-deadlines` — concrete deadline arithmetic under CCP § 12,
  § 12a
- `ca-draft-note` — drafts the Notice of Motion that goes out
  after the reservation
- `ca-file-packet` — assembles the full packet for filing once
  the date is reserved
- `ca-lasc` / `ca-sfsc` / `ca-county-courts` — venue-specific
  reservation protocols
- `scripts/case-calendar.py --rule motion-notice-min` — earliest
  viable hearing date

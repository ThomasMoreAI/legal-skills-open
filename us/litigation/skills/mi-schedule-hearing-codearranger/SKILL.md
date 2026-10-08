---
name: mi-schedule-hearing-codearranger
title: Get a Motion Hearing Date (Michigan)
description: This skill should be used when the user needs to obtain a motion hearing date in a Michigan court and notice it. Triggers include "schedule a Michigan motion hearing", "get a hearing date Michigan", "Wayne County praecipe", "Oakland motion scheduling", "notice motion for hearing Michigan", "MCR 2.119 motion practice", "set my motion for a Michigan motion day", "how do I get a motion date in Wayne Circuit", "Oakland 6th Circuit motion scheduling", "36th District Court hearing date", "do I file the notice of hearing before or after getting a date". In Michigan civil practice the mechanics vary by court — Wayne (3rd Circuit) historically uses a praecipe, Oakland (6th Circuit) uses assigned-judge motion calendars / online scheduling, and district courts such as the 36th set hearings differently. This skill produces a scheduling-request plan plus a notice-of-hearing plan and routes to the venue skills for the court-specific mechanics.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-schedule-hearing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Get a Motion Hearing Date (Michigan)

> **NOT LEGAL ADVICE.** This skill helps plan how to obtain and
> notice a hearing date. Hearing dates are the court's to assign,
> and the procedure varies by court and by individual judge — verify
> the filing court's local administrative orders, the assigned
> judge's practices, and the current clerk procedure before relying
> on anything here.

In Michigan, motion practice is governed by **MCR 2.119**, but **how a
hearing date is obtained varies by court.** There is no single
statewide motion-scheduling mechanism. The three broad patterns are:

1. **Praecipe / scheduling request to the clerk.** Some courts —
   historically including **Wayne County (3rd Circuit)** — require the
   movant to file or submit a **praecipe** (a scheduling request) so
   the clerk places the motion on a motion day. The court (not the
   parties) then sets the date.
2. **Assigned-judge motion calendar / online scheduling.** Other
   courts — including **Oakland County (6th Circuit)** — route motions
   to the assigned judge, who runs a regular motion call. The date is
   reserved through the judge's chambers, a court online-scheduling
   system, or by selecting an available motion day, depending on the
   judge.
3. **District-court motion setting.** District courts (such as the
   **36th District Court** in Detroit) set hearings their own way —
   often a clerk-assigned date on a periodic civil motion docket. The
   limited-jurisdiction civil docket differs from circuit practice.

Always confirm the venue's actual mechanism. Some courts post motion
calendars, some require contacting chambers, and some self-set through
an e-filing / online-scheduling portal (MiFILE in MiFILE counties).

## General workflow

The same three-step shape holds across courts; only step 1 changes:

1. **Get a date.** Use the court's mechanism — praecipe, chambers
   contact, online scheduling, or clerk-assigned motion docket. Clear
   the date through the court before committing to it.
2. **File the motion + notice of hearing.** Under MCR 2.119(C), a
   written motion and notice of hearing must generally be **served at
   least 9 days before the hearing** if served by mail, or **7 days
   before** if served by delivery (confirm the current rule and any
   local variation). The notice of hearing states the date, time,
   place, and assigned judge.
3. **Serve.** Serve the motion and notice on every other party under
   MCR 2.107 and file proof of service.

> Sequence note: in praecipe / clerk-assigned courts you typically
> obtain (or request) the date first, then file the notice stating it.
> In some chambers-scheduled courts you may file the motion and then
> notice it for an available motion day. Confirm the local sequence
> before filing — do not guess.

## When the parties initiate scheduling

| Situation | Action |
|---|---|
| Motion ready; need a date in a praecipe court (e.g., Wayne) | Submit the praecipe / scheduling request so the clerk sets a motion day; then file and serve the notice of hearing for that date — see `mi-wayne` |
| Motion ready; assigned-judge calendar (e.g., Oakland) | Reserve a motion day through chambers / online scheduling per the judge's practice; then notice it — see `mi-oakland` |
| District-court civil motion (e.g., 36th District) | Obtain the clerk-assigned date on the civil motion docket; then notice it — see `mi-36th-district` |
| MCR 2.116 summary disposition motion | Confirm the assigned judge's lead-time and briefing requirements; many judges require a longer notice window and a brief |
| Hearing already set; need to adjourn | Seek a stipulation/order of adjournment or move to adjourn with proposed dates per the court's practice |
| Multi-issue or evidentiary hearing | Coordinate the estimated length with chambers before reserving |
| Emergency / ex parte relief | Contact chambers / the clerk immediately and follow the court's ex parte / TRO procedure (MCR 3.310) |

## Contact channels and scheduling systems

Channels differ by court and by individual judge, and change at
judicial rotation. **Do not cache or guess email addresses, phone
numbers, praecipe forms, or portal URLs** — fetch the current
procedure from the filing court's website or its local administrative
orders. In MiFILE e-filing counties, scheduling and the notice of
hearing may flow through the portal; confirm whether the court
requires e-filing.

### Per-venue routing notes

These are starting points only — each court's local administrative
orders and the assigned judge's individual practices control.

| Court | Notes |
|---|---|
| **Wayne County (3rd Circuit), Detroit** | Historically a **praecipe** model: the movant submits a scheduling request and the clerk places the motion on a motion day. Confirm the current praecipe form / procedure and any MiFILE requirement. Route to `mi-wayne`. |
| **Oakland County (6th Circuit), Pontiac** | **Assigned-judge motion calendars**; dates are reserved through chambers / the court's scheduling system per the judge's practice. Route to `mi-oakland`. |
| **36th District Court, Detroit** | District-court limited-jurisdiction civil practice; hearings set on the court's own civil motion docket, often clerk-assigned. Route to `mi-36th-district`. |
| **Other circuit courts** | Practice ranges from praecipe to chambers coordination to online scheduling. See `mi-circuit-courts`. |
| **Other district courts** | Periodic clerk-set civil dockets are common. See `mi-district-courts`. |

## Scheduling-request / praecipe plan

Produce a short plan capturing, for the chosen venue:

- The court's scheduling mechanism (praecipe / chambers / online /
  clerk-assigned) and the exact channel used.
- Whether a date is requested vs. self-selected, and three candidate
  dates/times if dates are proposed.
- The estimated hearing length and whether a brief is required.
- Confirmation that opposing counsel/party availability was
  considered, and a log of any call (date/time, person spoken to,
  date offered, conditions).
- The MCR 2.119(C) lead time backed out from the chosen date so the
  notice can be served on time.

**Avoid ex parte communication** with the court on anything beyond
pure scheduling logistics, and include opposing counsel/party when
coordinating availability.

## Notice-of-hearing plan

Once a date is obtained, the notice of hearing states: the moving
party and motion title; the assigned judge; the courthouse and
courtroom; the date and time; and "or as soon thereafter as counsel
may be heard." File and serve it under MCR 2.107 with proof of
service, observing the MCR 2.119(C) service lead time. For drafting
the standalone document, use `mi-draft-note`.

## Hearing-length estimation guidance

| Motion type | Typical length |
|---|---|
| MCR 2.116 summary disposition | 30-60 min (often briefed) |
| Motion to compel / discovery (MCR 2.313) | 15-30 min |
| Motion to set aside default / default judgment | 30-60 min |
| Motion for reconsideration (MCR 2.119(F)) | usually decided without oral argument |
| Adjournment / scheduling motion | 5-15 min |
| TRO / injunction (MCR 3.310) | 30-180 min (often evidentiary) |

## Composition

- For the notice of hearing as a standalone document: `mi-draft-note`
- For Wayne County praecipe / 3rd Circuit scheduling mechanics:
  `mi-wayne`
- For Oakland County 6th Circuit motion-calendar / online scheduling:
  `mi-oakland`
- For 36th District Court motion-docket mechanics: `mi-36th-district`
- For other venues: `mi-circuit-courts`, `mi-district-courts`
- For drafting the underlying motion: `mi-draft-motion`
- For hearing-day prep and protocol: `mi-hearings`
- For MCR 2.119(C) lead-time arithmetic and MCR 1.108 computation:
  `mi-deadlines`

## References

- `mi-law-references` for MCR 2.119, MCR 2.107, and MCR 1.108 text
- The filing court's website and local administrative orders for the
  current praecipe form / scheduling procedure and any MiFILE
  e-filing requirement
- Confirm the assigned judge's individual practices before relying on
  any routing note above

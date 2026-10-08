---
name: id-schedule-hearing-codearranger
title: Reserve a Hearing Date (Idaho)
description: Use when the user needs to reserve a motion hearing date in an Idaho court and produce the contact email or call log. Triggers include "schedule an Idaho motion hearing", "reserve a hearing date Idaho", "get a hearing date in District Court", "set a hearing Magistrate Division", "Ada County hearing date", "Bonneville County motion setting", "contact the judge's clerk Idaho", "iCourt scheduling Idaho", "Notice of Hearing date Idaho", "how do I get my motion heard in Idaho". In Idaho civil practice the hearing date is typically reserved with the District Court / Magistrate Division clerk or the assigned judge's clerk before the Notice of Hearing issues. This skill produces a scheduling-request plan and the contact email / call log, and routes to the venue skills for court-specific mechanics.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-schedule-hearing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Reserve a Hearing Date (Idaho)

> **NOT LEGAL ADVICE.** This skill helps plan how to reserve a hearing
> date and draft the contact record. The procedure varies by court and by
> the assigned judge — verify the filing court's local rules, the
> assigned judge's procedures, and current clerk / iCourt practice before
> relying on anything here.

In Idaho, the typical mechanic is **reserve the date first, then notice
it.** A party generally **coordinates an available hearing date** with
the **District Court or Magistrate Division clerk**, or with the
**assigned judge's clerk / judicial assistant**, and then serves a
**Notice of Hearing** under **I.R.C.P. 7(b)** stating that date. The
Notice of Hearing and the motion must be served **at least 14 days before
the hearing** (I.R.C.P. 7(b)(3)) — back the reservation out from that
floor and from the briefing schedule. See `id-hearings` and
`id-deadlines`.

How the date actually gets reserved varies by court:

1. **Assigned-judge / clerk setting.** In most District Courts and
   Magistrate Divisions, the case is handled by an assigned **district
   judge** or **magistrate judge** whose **judicial assistant / clerk**
   controls the calendar. You contact that clerk (by phone or email) for
   an available date, or use the court's published motion-setting
   procedure.
2. **Clerk-of-court motion docket.** Some courts run a periodic civil
   motion calendar through the **clerk of the District Court**; the clerk
   assigns a date from the available docket.
3. **iCourt / I.R.E.F.S.** Idaho courts e-file through **iCourt (Odyssey
   File & Serve)**. Confirm whether the hearing request and the Notice of
   Hearing flow through the portal or are coordinated directly with the
   clerk.

Always confirm the venue's actual mechanism — some judges set argument by
order, some require you to call the judicial assistant for a date, and the
Magistrate Division may handle setting its own way.

## General workflow

The shape is: **reserve → notice → calendar.**

1. **Reserve the date.** Contact the assigned judge's clerk / judicial
   assistant or the District Court clerk for an available hearing date
   and time that leaves at least the **14-day** Notice-of-Hearing margin
   (I.R.C.P. 7(b)(3)) and accommodates the briefing schedule.
2. **Serve the Notice of Hearing** stating the reserved date, time, and
   appearance method (in-person / Zoom / telephonic), filed with the
   motion and Memorandum. See `id-hearings`.
3. **Calendar backward** from the hearing: the 14-day notice floor, the
   opposing party's response window, and the movant's reply. Compute with
   `id-deadlines`.

> Sequence note: do **not** serve a Notice of Hearing asserting a date you
> have not confirmed with the court. Reserve first, then notice.

## When scheduling is initiated

| Situation | Action |
|---|---|
| Motion ready; need a hearing date | Contact the assigned judge's clerk / judicial assistant (or District Court clerk) for an available date; confirm the 14-day notice margin; route to the venue skill |
| Ada County (4th District) case | Follow the 4th District / assigned-judge motion-setting procedure; see `id-ada` |
| Bonneville County (7th District) case | Follow the 7th District / assigned-judge procedure; see `id-bonneville` |
| Other county | Assigned-judge / clerk setting is the norm statewide; confirm the county's local rules; see `id-county-courts` |
| Magistrate Division matter (≤ $5,000 civil, eviction, family) | Setting follows Magistrate Division practice, often clerk-assigned; confirm with the division clerk |
| Hearing already set; need to continue / vacate | Move (or stipulate) to continue with proposed dates per the judge's procedure; do not assume a stipulation alone moves the date |
| Emergency / ex parte / TRO relief | Contact the assigned judge / clerk immediately and follow the court's ex parte / I.R.C.P. 65 procedure |

## Contact channels and scheduling systems

Channels differ by court and by individual judge / judicial assistant and
change at judicial rotation. **Do not cache or guess clerk phone numbers,
email addresses, or portal URLs** — fetch the current procedure from the
filing court's website, its local rules, or the assigned judge's
published procedures. Idaho courts use **iCourt (Odyssey File & Serve /
I.R.E.F.S.)** for e-filing; confirm whether the hearing request and the
Notice of Hearing flow through the portal.

### Per-venue routing notes

Starting points only — each court's local rules and the assigned judge's
procedures control.

| Court | Notes |
|---|---|
| **Ada County — 4th Judicial District (Boise)** | Case handled by an assigned district or magistrate judge; reserve the date with that judge's clerk / judicial assistant or the District Court clerk. iCourt e-filing. Route to `id-ada`. |
| **Bonneville County — 7th Judicial District (Idaho Falls)** | Assigned-judge setting; procedures differ by judge. Route to `id-bonneville`. |
| **Other counties** | Assigned-judge / clerk setting is the norm statewide; confirm the county's local rules. See `id-county-courts`. |
| **Magistrate Division (limited-jurisdiction civil, eviction, probate, family)** | Setting follows Magistrate Division practice, often clerk-assigned. Confirm with the division clerk. |

## Producing the contact record

Produce the **scheduling contact email or call log** to memorialize the
reservation:

```
Subject: Hearing Date Request — [Case Short Title], Case No. [Number]

To: [Clerk / Judicial Assistant for Judge ___], [Court]

I am the [Plaintiff / Defendant], self-represented, in the above matter.
I intend to file and notice a [Motion to ___] under I.R.C.P. 7(b) and
request an available hearing date on or after [DATE] (allowing the 14-day
notice period). I anticipate the hearing will take approximately
[N minutes]. Please advise an available date and time, and whether the
hearing will be in person or by Zoom / telephone.

Thank you,
[Name] / [Phone] / [Email]
```

Keep a parallel **call log** for any phone contact (date / time, person
spoken to, court, date offered, appearance method). Keep all contact to
pure scheduling logistics.

> **Avoid ex parte communication** with the court on anything beyond pure
> scheduling logistics, and include the opposing party when coordinating
> availability where the court expects it.

## Scheduling-request plan

Produce a short plan capturing, for the chosen venue:

- The reserved (or requested) hearing date and time, and the **time
  estimate** stated.
- Confirmation that the date leaves the **14-day** Notice-of-Hearing
  margin (I.R.C.P. 7(b)(3)) and accommodates the briefing schedule.
- The appearance method (in-person / Zoom / telephonic) and where the
  setting confirmation will arrive (clerk email / iCourt / mail).
- The response and reply windows backed out from the hearing date so the
  motion is fully briefed beforehand (compute with `id-deadlines`).
- A log of any scheduling contact (date / time, person / clerk, what was
  said), kept to pure scheduling logistics.

## Hearing-length estimation guidance

A realistic time estimate helps the clerk find a slot.

| Motion / event | Typical estimate |
|---|---|
| Rule 12(b) motion to dismiss | 20-45 min |
| Rule 56 summary judgment | 30-60 min |
| Discovery / motion to compel (Rule 37) | 15-30 min |
| Motion to set aside default (Rule 60(b)) | 20-45 min |
| Motion for reconsideration (Rule 11.2) | 15-30 min |
| TRO / preliminary injunction (Rule 65) | 30-180 min (often evidentiary) |

## Composition

- For the Notice of Hearing as a standalone document: `id-draft-note`
- For Ada County (4th District) setting mechanics: `id-ada`
- For Bonneville County (7th District) setting mechanics: `id-bonneville`
- For other counties: `id-county-courts`
- For drafting the underlying motion: `id-draft-motion`
- For hearing-day prep and protocol: `id-hearings`
- For the 14-day notice and briefing-timeline arithmetic and I.R.C.P. 2.2
  time computation: `id-deadlines`

## References

- `id-law-references` for I.R.C.P. 7(b) (Notice of Hearing) and I.R.C.P.
  56 (summary-judgment briefing) text
- The filing court's website and local rules for the current
  motion-setting channel and any iCourt e-filing requirement
- Confirm the assigned judge's published procedures before relying on any
  routing note above

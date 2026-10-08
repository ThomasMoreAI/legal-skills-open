---
name: tx-schedule-hearing-codearranger
title: Reserve a Hearing or Submission Setting (Texas)
description: Use when the user needs to reserve a motion hearing or submission setting in a Texas court and produce the contact email or call log. Triggers include "schedule a Texas motion hearing", "reserve a hearing date Texas", "contact the court coordinator Texas", "get a setting in district court Texas", "set my motion on the submission docket", "Harris County motion setting", "Dallas County hearing date", "how do I get my motion heard in Texas", "JP court hearing setting", "Notice of Hearing date Texas". In Texas, district and county courts set hearings through the court coordinator and justice (JP) courts through the precinct clerk; the setting is reserved before the Notice of Hearing issues. This skill produces a scheduling-request plan and the contact email / call log, and routes to the venue skills for court-specific mechanics.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-schedule-hearing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Reserve a Hearing or Submission Setting (Texas)

> **NOT LEGAL ADVICE.** This skill helps plan how to reserve a setting
> and draft the contact record. The procedure varies by court and by
> the assigned judge — verify the filing court's local rules, the
> assigned judge's procedures, and current coordinator / clerk /
> eFileTexas practice before relying on anything here.

In Texas, the typical mechanic is **reserve the setting first, then
notice it.** A party generally **coordinates an available setting**
with the **court coordinator** (district and county courts) or the
**precinct clerk** (justice courts), and then files and serves a
**Notice of Hearing** under **Tex. R. Civ. P. 21** stating that
setting. The motion and notice must be served respecting the **Rule
21(b)** notice floor (and the longer **Rule 166a** 21-day track for a
summary-judgment motion) — back the reservation out from that floor
and from the briefing schedule. See `tx-hearings` and `tx-deadlines`.

## Submission or oral hearing — decide before you call

Decide whether the motion will be decided **by submission** (on the
papers, with a submission date) or **by oral hearing** (argument on a
date and time) before contacting the court — many courts default
routine motions to the **submission docket** and reserve oral
argument for dispositive or evidentiary motions. The court's local
rules and the assigned judge's practice control. See `tx-draft-note`.

## Who sets the setting — by court level

How a setting gets reserved depends on the court:

1. **District Courts and County Courts at Law — the court
   coordinator.** Each court has a **court coordinator** (the judge's
   calendar staff) who controls the docket. You contact the
   coordinator (by phone or email, or through the court's online
   setting system where one exists) for an available oral-hearing date
   or to confirm the submission-docket procedure. Some courts run a
   periodic submission docket on which motions are set by filing the
   Notice of Submission by a cutoff.
2. **Justice Courts (JP courts) — the precinct clerk.** Setting is
   handled through the **precinct clerk / Justice of the Peace's
   office**. Justice-court procedure is simplified (Tex. R. Civ. P.
   500–510); confirm the precinct's setting practice with its clerk.
3. **eFileTexas.** Texas e-files through **eFileTexas.gov** (Odyssey
   File & Serve). Confirm whether the hearing/submission request and
   the Notice of Hearing flow through the portal or are coordinated
   directly with the coordinator/clerk.

Always confirm the venue's actual mechanism — some courts set
argument by order, some require you to email the coordinator for a
date, and submission-docket cutoffs vary.

## General workflow

The shape is: **reserve → notice → calendar.**

1. **Reserve the setting.** Contact the court coordinator (district/
   county) or the precinct clerk (JP) for an available date/time, or
   confirm the submission-docket cutoff, leaving the Rule 21(b) notice
   margin (or the Rule 166a 21-day margin) and accommodating the
   briefing schedule.
2. **File and serve the Notice of Hearing** stating the reserved
   setting, the appearance method (in person / Zoom / submission), and
   the response-due statement, filed with the motion. See
   `tx-draft-note`.
3. **Calendar backward** from the setting: the notice floor, the
   opposing party's response window, and the movant's reply. Compute
   with `tx-deadlines`.

> Sequence note: do **not** file a Notice of Hearing asserting a
> setting you have not confirmed with the court. Reserve first, then
> notice.

## When scheduling is initiated

| Situation | Action |
|---|---|
| Motion ready; need an oral-hearing setting | Contact the court coordinator (district/county) for an available date; confirm the Rule 21(b) margin; route to the venue skill |
| Motion ready; submission docket | Confirm the submission-docket cutoff with the coordinator; file the Notice of Submission by the cutoff |
| Harris County matter | Follow the Harris County court coordinator / submission-docket procedure; see `tx-hcdc` |
| Dallas County matter | Follow the Dallas County coordinator procedure; see `tx-dcdc` |
| Other county | Court-coordinator setting is the norm; confirm the county's local rules; see `tx-county-courts` |
| Justice Court (JP) matter | Setting through the precinct clerk; confirm the precinct's practice |
| Family-law matter | Setting follows the family district court / associate-judge practice; see `tx-family-court` |
| Hearing set; need to continue / pass | Move (or agree) to continue with proposed dates per the coordinator's procedure; do not assume agreement alone moves the setting |
| Emergency / ex parte / TRO relief | Contact the coordinator immediately and follow the court's ex parte / Tex. R. Civ. P. 680 et seq. TRO procedure |

## Contact channels and scheduling systems

Channels differ by court and by individual judge / coordinator and
change at judicial rotation. **Do not cache or guess coordinator/clerk
phone numbers, email addresses, or portal URLs** — fetch the current
procedure from the filing court's website, its local rules, or the
assigned judge's published procedures. Texas courts e-file through
**eFileTexas.gov**; confirm whether the setting request and the Notice
of Hearing flow through the portal.

### Per-venue routing notes

Starting points only — each court's local rules and the assigned
judge's procedures control.

| Court | Notes |
|---|---|
| **Harris County (Houston) District / County Courts at Law** | Setting through the court coordinator; many courts use a submission docket. eFileTexas. Route to `tx-hcdc`. |
| **Dallas County District / County Courts at Law** | Court-coordinator setting; procedures differ by court. Route to `tx-dcdc`. |
| **Other counties** | Court-coordinator setting is the norm statewide; confirm the county's local rules. See `tx-county-courts`. |
| **Justice Courts (JP precincts)** | Setting through the precinct clerk; simplified Rule 500–510 procedure. |
| **Family district courts** | Setting follows the family court / associate-judge practice. See `tx-family-court`. |

## Producing the contact record

Produce the **scheduling contact email or call log** to memorialize
the reservation:

```
Subject: Hearing/Submission Setting Request — [Case Short Title],
         Cause No. [Number]

To: Court Coordinator, [Nth] Judicial District Court / County Court
    at Law No. ___, [County] County

I am the [Plaintiff / Defendant], self-represented, in the above
matter. I intend to file and notice a [Motion to ___] under
Tex. R. Civ. P. 21 and request [an available oral-hearing date on or
after [DATE] / a submission setting on the next available submission
docket], allowing the Rule 21(b) notice period [or the Rule 166a
21-day period for a summary-judgment motion]. I estimate the hearing
will take approximately [N minutes]. Please advise an available
setting and whether the appearance is in person, by Zoom, or on
submission.

Thank you,
[Name] / [Phone] / [Email]
```

Keep a parallel **call log** for any phone contact (date / time,
person spoken to, court, setting offered, appearance method). Keep all
contact to pure scheduling logistics.

> **Avoid ex parte communication** with the court on anything beyond
> pure scheduling logistics, and include the opposing party when
> coordinating availability where the court expects it.

## Scheduling-request plan

Produce a short plan capturing, for the chosen venue:

- The reserved (or requested) setting date/time (or submission date),
  and the **time estimate** stated.
- Confirmation that the setting leaves the **Rule 21(b)** notice
  margin (or the **Rule 166a** 21-day margin) and accommodates the
  briefing schedule.
- The appearance method (in person / Zoom / submission) and where the
  setting confirmation will arrive (coordinator email / eFileTexas /
  mail).
- The response and reply windows backed out from the setting so the
  motion is fully briefed beforehand (compute with `tx-deadlines`).
- A log of any scheduling contact, kept to pure scheduling logistics.

## Hearing-length estimation guidance

A realistic time estimate helps the coordinator find a slot.

| Motion / event | Typical estimate |
|---|---|
| Tex. R. Civ. P. 91a motion to dismiss | 20-45 min |
| Tex. R. Civ. P. 166a summary judgment | 30-60 min |
| Special exceptions (Rule 91) | 15-30 min |
| Discovery / motion to compel (Rule 215) | 15-30 min |
| Motion for new trial (Rule 329b) | 20-45 min |
| TRO / temporary injunction (Rule 680 et seq.) | 30-180 min (often evidentiary) |

## Composition

- For the Notice of Hearing as a standalone document: `tx-draft-note`
- For Harris County setting mechanics: `tx-hcdc`
- For Dallas County setting mechanics: `tx-dcdc`
- For other counties: `tx-county-courts`
- For family-court setting mechanics: `tx-family-court`
- For drafting the underlying motion: `tx-draft-motion`
- For hearing-day prep and protocol: `tx-hearings`
- For the notice floor / Rule 166a 21-day track and the +3-day mail
  add-on: `tx-deadlines`

## References

- `tx-law-references` for Tex. R. Civ. P. 21 / 21a (filing, service,
  notice floor) and Tex. R. Civ. P. 166a (summary-judgment briefing)
  text
- The filing court's website and local rules for the current
  coordinator / submission-docket procedure and any eFileTexas
  requirement
- Confirm the assigned judge's published procedures before relying on
  any routing note above

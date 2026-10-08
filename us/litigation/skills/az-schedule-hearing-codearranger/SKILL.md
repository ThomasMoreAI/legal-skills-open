---
name: az-schedule-hearing-codearranger
title: Get a Motion Heard / Set a Hearing (Arizona)
description: This skill should be used when the user needs to get an Arizona motion heard or a hearing date set, and to plan the oral-argument request and notice. Triggers include "schedule an Arizona motion hearing", "get a hearing date Arizona", "request oral argument Maricopa", "Pima motion setting", "set a hearing Arizona Superior Court", "Ariz. R. Civ. P. 7.1 oral argument", "how do I get my motion argued in Arizona", "Maricopa Superior Court division scheduling", "Rule 16 scheduling conference Arizona", "compulsory arbitration hearing Arizona". In Arizona civil practice the court decides whether to hear oral argument and sets the date; how that works varies by court and by the assigned division/judge. This skill produces a scheduling-request plan and routes to the venue skills for court-specific mechanics.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-schedule-hearing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Get a Motion Heard / Set a Hearing (Arizona)

> **NOT LEGAL ADVICE.** This skill helps plan how to request oral
> argument and obtain a hearing date. Whether to hold argument and
> when to set it are the court's decisions, and the procedure varies
> by court and by the assigned division/judge — verify the filing
> court's local rules, the assigned judge's procedures, and current
> clerk/portal practice before relying on anything here.

In Arizona, the key mechanic is different from a self-set "motion day."
Under **Ariz. R. Civ. P. 7.1**, a party may **request oral argument**
on a motion (typically by a notation in the caption or a separate
request stating the time estimate), but **the court decides whether to
hold argument** and, if it does, **sets the date.** Many civil motions
are decided on the briefs without argument. The movant does not
unilaterally reserve a date; the request goes in and the court (or its
division) responds.

How the date actually gets set then varies by court:

1. **Assigned-division/judge setting.** In **Maricopa County Superior
   Court** and **Pima County Superior Court**, each case is assigned to
   a division/judge who controls the calendar. Whether and when oral
   argument is set — and the channel for requesting it (caption
   notation, separate Rule 7.1 request, division contact, or portal) —
   follows that division's procedures, which differ between and within
   the two counties.
2. **Scheduling / case-management conferences (Rule 16).** Separate
   from motion argument, the court sets **Rule 16 scheduling or
   case-management conferences** to manage the case. These are
   court-initiated (often by order after the case is at issue); the
   parties may be required to confer and submit a joint report before
   the conference.
3. **Compulsory arbitration hearings (Rules 72-77).** Cases at or
   below the county's jurisdictional-amount threshold are subject to
   **compulsory arbitration** under **Ariz. R. Civ. P. 72-77**. The
   arbitration hearing is set by the **assigned arbitrator** (not the
   judge), after appointment, in coordination with the parties — a
   different scheduling track from motion argument.

Always confirm the venue's actual mechanism. Some divisions set
argument by minute entry, some require a separate request, and limited-
jurisdiction courts handle setting their own way.

## General workflow

The shape is: **request → court sets → notice**, not self-set.

1. **File the motion with an oral-argument request** if argument is
   wanted, per Ariz. R. Civ. P. 7.1. State a time estimate. The motion
   is briefed under the Rule 7.1 response/reply timeline before the
   court rules on whether to hear it.
2. **The court decides and sets the date.** The assigned division
   either rules on the briefs or issues a minute entry / order setting
   oral argument with a date, time, and (in-person or remote)
   appearance instructions.
3. **Receive and calendar the notice.** When the court sets a hearing
   or conference, it issues the setting notice. Confirm the date,
   appearance method, and any pre-hearing submission, and calendar
   backward from it.

> Sequence note: in Arizona the movant generally does **not** pick the
> date. The request goes in with (or in) the motion, and the court's
> setting notice supplies the date. Do not draft a notice asserting a
> self-selected hearing date — confirm the division's practice first.

## When scheduling is initiated

| Situation | Action |
|---|---|
| Motion ready; want oral argument | Include the Rule 7.1 oral-argument request with a time estimate; the court decides and sets — route to the venue skill for the request channel |
| Maricopa Superior Court case | Follow the assigned division's argument-setting procedure (caption notation / separate request / division contact); see `az-maricopa` |
| Pima Superior Court case | Follow the assigned division's procedure; see `az-pima` |
| Rule 16 scheduling / case-management conference | Court-initiated; confer with opposing party and submit any required joint report before the date |
| Compulsory arbitration (Rules 72-77) case | Hearing is set by the appointed arbitrator in coordination with the parties, not by the judge |
| Limited-jurisdiction (justice court) hearing | Setting follows justice-court practice — often clerk- or court-assigned; see `az-justice-courts` |
| Hearing already set; need to continue/vacate | Move (or stipulate) to continue with proposed dates per the division's procedure; do not assume a stipulation alone moves the date |
| Emergency / ex parte / TRO relief | Contact the assigned division / clerk immediately and follow the court's ex parte / Rule 65 procedure |

## Contact channels and scheduling systems

Channels differ by court and by individual division/judge and change at
judicial rotation. **Do not cache or guess division phone numbers,
email addresses, request forms, or portal URLs** — fetch the current
procedure from the filing court's website, its local rules, or the
assigned judge's published procedures. Arizona Superior Courts use
**AZTurboCourt** for e-filing in many counties; confirm whether the
oral-argument request and any setting flow through the portal.

### Per-venue routing notes

Starting points only — each court's local rules and the assigned
division's procedures control.

| Court | Notes |
|---|---|
| **Maricopa County Superior Court (Phoenix)** | Case assigned to a division/judge that controls argument setting; the Rule 7.1 request channel and whether argument is heard follow that division's procedures. AZTurboCourt e-filing. Route to `az-maricopa`. |
| **Pima County Superior Court (Tucson)** | Assigned-division setting; procedures differ from Maricopa and between divisions. Route to `az-pima`. |
| **Other Superior Courts** | Assigned-division setting is the norm statewide; confirm the county's local rules. See `az-superior-courts`. |
| **Justice courts (limited jurisdiction)** | Setting follows justice-court practice, often clerk-/court-assigned on a periodic civil docket. See `az-justice-courts`. |

## Scheduling-request plan

Produce a short plan capturing, for the chosen venue:

- Whether oral argument is being requested under Rule 7.1, the exact
  request channel (caption notation / separate request / division
  contact / portal), and the **time estimate** stated.
- The expectation that the **court sets the date** — and where the
  setting notice will arrive (minute entry / portal / mail).
- The Rule 7.1 response/reply briefing timeline backed out so the
  motion is fully briefed before the court rules on setting.
- For a Rule 16 conference: any joint-report / conferral obligation and
  its due date relative to the conference.
- For a compulsory-arbitration matter (Rules 72-77): the arbitrator-
  appointment status and that the hearing is set with the arbitrator.
- A log of any scheduling contact (date/time, person/division, what was
  said), kept to pure scheduling logistics.

**Avoid ex parte communication** with the court on anything beyond pure
scheduling logistics, and include the opposing party when coordinating
availability.

## Hearing-length estimation guidance

A realistic time estimate helps the division decide and set argument.

| Motion / event | Typical estimate |
|---|---|
| Rule 12(b) motion to dismiss | 20-45 min (often decided on briefs) |
| Rule 56 summary judgment | 30-60 min (often briefed; argument discretionary) |
| Discovery / motion to compel | 15-30 min |
| Motion to set aside default (Rule 60) | 20-45 min |
| Rule 16 scheduling / case-management conference | 15-30 min |
| Compulsory-arbitration hearing (Rules 72-77) | half-day to full-day, set with arbitrator |
| TRO / preliminary injunction (Rule 65) | 30-180 min (often evidentiary) |

## Composition

- For the oral-argument request or notice as a standalone document:
  `az-draft-note`
- For Maricopa Superior Court division argument-setting mechanics:
  `az-maricopa`
- For Pima Superior Court division argument-setting mechanics:
  `az-pima`
- For justice-court (limited-jurisdiction) setting: `az-justice-courts`
- For other Superior Court venues: `az-superior-courts`
- For drafting the underlying motion: `az-draft-motion`
- For hearing-day prep and protocol: `az-hearings`
- For Rule 7.1 briefing-timeline arithmetic and time computation:
  `az-deadlines`

## References

- `az-law-references` for Ariz. R. Civ. P. 7.1, Rule 16, and Rules
  72-77 text
- The filing court's website and local rules for the current oral-
  argument request channel and any AZTurboCourt e-filing requirement
- Confirm the assigned division/judge's published procedures before
  relying on any routing note above

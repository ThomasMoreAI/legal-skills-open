---
name: ny-hearings-codearranger
title: New York Hearings
description: Prepare for and conduct hearings in New York courts. Triggers include 'oral argument in New York', 'NY motion hearing', 'Microsoft Teams hearing', 'remote appearance Supreme Court', 'in-person motion argument', 'OCA Teams link', 'hearing-day prep New York', 'courtroom etiquette Supreme Court', 'oral argument in IAS Part', 'submitted motion' (no oral argument), 'opposition argued'. Covers oral-argument preparation, Microsoft Teams (the NY court system's adopted remote-appearance platform since 2020), courtroom etiquette in NY Supreme Court Parts, the distinction between "submitted" and "argued" motions, and hearing-day checklists.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-hearings
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# New York Hearings

> **NOT LEGAL ADVICE.** Verify the assigned Justice's
> hearing protocol before every appearance.

## NY hearing categories

| Category | When | Where |
|---------|------|-------|
| Motion hearing | Return date on Notice of Motion | Assigned IAS Part |
| Order to Show Cause hearing | Date set by signing Justice | Assigned IAS Part |
| Preliminary Conference | Per 22 NYCRR § 202.12 | Assigned IAS Part |
| Compliance Conference | Mid-discovery | Assigned IAS Part |
| Settlement Conference | CPLR 3408 (foreclosure) or as scheduled | Foreclosure Settlement Conference Part |
| Pre-trial conference | Pre-trial readiness | Assigned IAS Part |
| Trial | After Note of Issue + Certificate of Readiness | Assigned IAS Part |
| Evidentiary hearing | Re factual disputes | Assigned IAS Part |
| Default-judgment inquest | CPLR 3215(b) | Inquest part (varies) |

## Submitted vs. argued motions

A distinctive NY practice: a motion can be either:

- **"Argued"** — counsel appears at the return date and
  argues the motion orally before the Justice
- **"Submitted"** (or "on submission") — no appearance;
  the motion is decided on the papers alone

Many NY Justices default to "submitted unless oral argument
is requested by either party." Check Part Rules: some
require an affirmation requesting oral argument; some require
a separate letter; some allow argument on request at the
return date.

When oral argument is granted, the Justice typically grants
**5–10 minutes per side**, sometimes more in complex Comm
Div matters. Some Parts schedule oral argument on a calendar
day distinct from the return date.

## Remote hearings — Microsoft Teams

Since 2020, NY courts have used **Microsoft Teams** as the
default remote-appearance platform (not Zoom, not WebEx —
Microsoft Teams). The link is typically:

- Distributed via the NYSCEF docket as a Notice of Virtual
  Court Appearance
- Or distributed by the Part clerk by email after RJI

Pro se litigants commonly join from a personal computer or
tablet via the Teams web client (no Teams account required).
**Smartphone is allowed but bandwidth is critical.**

Pre-hearing checklist (remote):

- Test the Teams link 24 hours in advance
- Use the legal name (not a nickname) as the Teams display
  name
- Mute by default; unmute only when called
- Have all filing PDFs open in a separate window
- Dress as if appearing in person

## In-person hearings

The Justice's Part Rules will indicate which categories
default to in-person:

- **Trials** — in-person, with limited exceptions
- **Evidentiary hearings** — typically in-person
- **Contested settlement conferences** — often in-person
- **Routine motion hearings** — typically remote (Teams) by
  Part Rule

## Courtroom etiquette

| Conduct | Notes |
|---------|-------|
| Stand when the Justice enters / exits | Standard |
| Address the Justice as "Your Honor" | Never "Judge" alone |
| Stand at the lectern (or counsel table) when speaking | Per Part Rules; some Parts allow seated |
| Begin with "May it please the Court, [Name] appearing pro se for [Plaintiff/Defendant]" | First appearance of the hearing |
| One advocate at a time | Wait for the Justice to recognize you |
| Phone off (silenced) | Standard |
| No food / gum | Bottle of water OK in most Parts |

## Hearing-day preparation

24–48 hours before:

1. Re-read the moving papers, opposition, and reply
2. Brief outline of your argument:
   - Two-sentence summary of your position
   - Three strongest points (one cite each)
   - Concession point (where opposing has a point — concede
     it but distinguish)
   - "Ask" — what specific relief
3. Prepare for likely questions from the Justice
4. Print or bookmark the exact cite text for the cases you
   may need to read aloud
5. Re-confirm Part Rules: time, location/link, lectern vs.
   table, oral-argument time per side

Day-of:

1. Arrive 15 minutes early (or join Teams 10 minutes early)
2. Sign in with the Part clerk
3. Wait quietly until called
4. After argument, do not interject when the Justice rules
5. If the Justice reserves decision, ask if a written
   decision will issue or whether the parties should
   schedule a follow-up

## Disability accommodation

Per 22 NYCRR § 50.1 + state and federal disability law, the
court provides accommodations on request:

- Sign-language interpreter (book through the Justice's
  clerk)
- Translation (Court Interpreter Office)
- Wheelchair accessibility
- Extended argument time for cognitive disability

Request as early as possible — at least 14 days in advance is
recommended.

## Composition with other ny- skills

- `ny-statewide-format` — format for any hearing-related
  filings
- `ny-schedule-hearing` — getting the hearing date on the
  calendar
- `ny-draft-motion` + `ny-draft-declaration` — pre-hearing
  drafting
- `ny-submit-order` — post-hearing proposed-order
  submission
- `ny-quality-check` — pre-hearing-filing QC

---
name: or-schedule-hearing-codearranger
title: Reserve a Hearing Date in an Oregon Circuit Court
description: Use this skill when the user needs to reserve a motion hearing date in an Oregon circuit court. Triggers include "reserve a hearing date", "schedule a hearing", "email the JA", "request a motion docket date", "how do I set a hearing in Multnomah", "what do I send to Civil Division", "I need to get a hearing date before I can file". Drafts the scheduling email (or call log) for the assigned judge's judicial assistant or the Civil Division, depending on the county. This is the prerequisite to the Notice of Hearing (`or-draft-note`) and the packet (`or-file-packet`) in most Oregon civil practice.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-schedule-hearing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Reserve a Hearing Date in an Oregon Circuit Court

In most Oregon circuit courts, a civil motion cannot simply be
self-noticed for a date. The moving party must request a date
from the court (the assigned judge's judicial assistant, the
Civil Division, or the Court Administrator, depending on the
county). After confirmation, the Notice of Hearing is filed.

This skill drafts the date-request email (or call log) — the
necessary precursor step.

> **NOT LEGAL ADVICE.** This skill drafts a scheduling
> communication as a procedural aid, not legal advice. Verify
> current per-court protocols and local-rule requirements
> before sending. Pair with substantive review by counsel where
> stakes warrant.

## Per-county routing

Different Oregon counties route hearing requests through
different intermediaries:

| Court | Contact route |
|-------|---------------|
| Multnomah | Assigned judge's JA (email) |
| Washington Co | Civil Division (email or phone) |
| Clackamas | Civil counter at 807 Main Street |
| Lane | JA for most civil judges; Court Administrator otherwise |
| Marion | Civil Department on Floor 2 |
| Jackson | Civil Division clerk |
| Deschutes | Court coordinator |
| Most rural counties | Court coordinator or centralized motion docket clerk |

Confirm the routing from the assigned court's website before
drafting. The Multnomah / Washington / Lane / Marion judge
pages list JA contacts; smaller counties' clerk's offices
typically have a single Civil contact line.

## Inputs to ask the user

- **County**: Multnomah, Washington, Lane, etc.
- **Assigned judge**: name and (if Multnomah/Lane) JA email
- **Case caption and number**
- **Motion type**: the title of the motion (e.g., "Motion to
  Compel Production of Documents Under ORCP 46 A")
- **Filing status**: motion already filed? Or to be filed
  after date is confirmed?
- **Estimated argument time**: 10, 15, 20, 30 minutes
- **Date preferences**: 2–3 proposed dates
- **Opposing party**: have they been consulted on dates?
  What's their position?

## Email template — Multnomah (JA-based)

```
To:      [Assigned Judge's JA email]
Subject: Hearing Date Request — [Case Short Title],
         Case No. [Cause Number]

Dear [Judicial Assistant Name]:

I am [Counsel of record / Defendant, pro se] in the above-
captioned matter, assigned to the Hon. [Judge Name].

I am requesting a hearing date for [Motion Title], filed
[date] (or to be filed [date]). Estimated argument time:
[20 minutes].

Proposed dates:
   [Date 1]
   [Date 2]
   [Date 3]

I have [conferred / not yet conferred] with opposing
counsel on these dates. [Opposing counsel [agrees / objects
to / has not responded re] each / specific dates.]

If WebEx is the Court's preferred mode for this motion,
please confirm and I will include the connection details on
the Notice of Hearing.

Thank you,
[Name][, pro se / OSB # ____ if counsel]
[Address]
[Phone]
[Email]
```

## Email template — Washington County (Civil Division)

```
To:      WCCCCivilCT@ojd.state.or.us
Subject: Hearing Date Request — [Case Short Title],
         Case No. [Cause Number]

Civil Division:

I am [Counsel of record / Defendant, pro se] in the above-
captioned matter, assigned to the Hon. [Judge Name].

I am requesting a hearing date for [Motion Title], to be
filed [date]. Estimated argument time: [X minutes].

Proposed dates:
   [Date 1]
   [Date 2]
   [Date 3]

I have / have not conferred with opposing counsel on these
dates.

If the Court prefers WebEx or telephone, please advise so I
can include the connection details on the Notice of Hearing.

Thank you,
[Name][, pro se / OSB # ____]
[Contact info]
```

## Email template — other counties

```
To:      [Civil Division / court coordinator / JA email]
Subject: Hearing Date Request — [Case Short Title],
         Case No. [Cause Number]

[Salutation appropriate to the contact]

I am [role] in [case short title], Case No. [cause number],
assigned to [Judge Name if known].

I am requesting a hearing date for [Motion Title], to be
filed [date]. Estimated argument time: [X minutes].

Proposed dates:
   [Date 1]
   [Date 2]
   [Date 3]

If the Court prefers WebEx or telephone, please advise so I
can include the connection details on the Notice of Hearing.

Thank you,
[Name][, pro se / OSB # ____]
[Contact info]
```

## Phone log template

For counties where date reservation is by phone (some rural
counties), document the call:

```
Call log — [Date]

To:    [Contact name and number]
From:  [Your name and number]
Re:    Hearing date request, Case No. [cause number]

Notes:
- Identified myself and the case
- Stated motion type and estimated time
- Proposed [Date 1], [Date 2], [Date 3]
- [Court contact] confirmed [Date X] at [Time] in
  [Courtroom / WebEx]
- [Court contact] noted [any standing orders or working-copy
  requirements]
- Confirmed by email at [time]
```

Follow up the call with an email confirming the reservation
("To confirm our call today, the hearing on Defendant's
Motion to Compel is set for [Date] at [Time] in [Mode] before
the Hon. [Judge]. I will file the Notice of Hearing within
[period].").

## Information needed in the date-request

The court contact needs to know:

1. **Case identification** — caption short title and number
2. **Motion identification** — title, ORCP/UTCR authority
3. **Argument time estimate** — affects calendar slot
4. **Mode preferences** (or simply asking what's available)
5. **Proposed dates** — give 2–3 options
6. **Opposing party status** — conferred? agreed? objecting?

## After confirmation

Once the court confirms the date:

1. **Calendar it** — date, time, mode, courtroom, judge
2. **Save the confirmation email** as evidence of reservation
3. **Draft the Notice of Hearing** (use `or-draft-note`)
4. **File the Notice** within the local SLR window
   (Multnomah: 3 business days; Washington Co: simultaneous
   with motion)
5. **Serve the Notice** on all parties
6. **Set hearing-prep reminders** at 7, 3, 1 day(s) out

## Common pitfalls

| Pitfall | Consequence |
|---------|-------------|
| Going to the wrong contact (JA when it's Civil Division, or vice versa) | Wasted email; delay |
| Not identifying the assigned judge | Civil Division may not know which calendar |
| Proposing dates too close to trial | Court may decline if motion can't be heard before relevant cutoff |
| Forgetting estimated time | Court may set a too-short slot |
| Failing to consult opposing counsel | Court may strike or reschedule; bad first impression |
| Not following up the call with an email | No paper record; disputes about the reservation |
| Filing the Notice before the JA confirms | Confusion; possible rejection |

## Pro se considerations

- Email is generally fine; phone is fine too
- Be professional; the JA / Civil Division clerk is doing you
  a favor by scheduling
- Don't follow up too aggressively; allow 1–2 business days
  before re-contacting
- Save every email — court contacts are part of the record

## Cross-references

- `or-draft-note` — drafts the Notice of Hearing (the
  *follow-up* document)
- `or-multcc/references/civil-motion-scheduling.md` —
  Multnomah JA process
- `or-wccc/references/civil-motion-practice.md` —
  Washington Co Civil Division process
- `or-county-courts` — other counties
- `or-file-packet` — final packet assembly

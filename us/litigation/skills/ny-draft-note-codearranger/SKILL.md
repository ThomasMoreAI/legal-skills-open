---
name: ny-draft-note-codearranger
title: Draft a New York Notice of Motion or OSC
description: Scaffold a Notice of Motion or Order to Show Cause for a New York court — the scheduling document that places a motion on the court's calendar. Triggers include 'draft a Notice of Motion', 'CPLR 2214', 'NY OSC', 'Order to Show Cause draft', 'return date', 'CPLR 2214(d) Order to Show Cause', 'CPLR 2215 cross-motion notice', 'OSC TRO request', 'CPLR 6313 preliminary injunction', 'NY motion return date'. Produces a Notice of Motion conformed to CPLR 2214 or an Order to Show Cause conformed to CPLR 2214(d), with attendant TRO language where appropriate. **The NY term is "Notice of Motion" or "Order to Show Cause" — not "Note for Motion Docket" (WA) or "Notice of Hearing" (OR).**
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-draft-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a New York Notice of Motion or OSC

> **NOT LEGAL ADVICE.** The Notice of Motion or OSC is the
> document that gets your motion on the court's calendar.
> Errors here can cause the motion to be denied or the
> filing to be rejected by the clerk.

## Choose: Notice of Motion or Order to Show Cause?

| Use | When |
|-----|------|
| **Notice of Motion** (CPLR 2214) | Standard motion practice; no emergency; sufficient time to give 8-day minimum notice |
| **Order to Show Cause** (CPLR 2214(d), 6313) | Emergency relief (TRO); insufficient time for 8-day notice; specific Part Rule requires OSC for certain motion types; ex parte stay of execution; certain CPLR 5015(a) vacatur motions |

OSC requires a Justice's signature on the OSC itself,
typically obtained ex parte; the signed OSC is then served on
the opposing party. Notice of Motion is filed directly via
NYSCEF without judicial pre-signature.

## Notice of Motion template (CPLR 2214)

```
SUPREME COURT OF THE STATE OF NEW YORK
COUNTY OF [COUNTY]
----------------------------------------- X
[CAPTION]                                  Index No. [#####/YYYY]
                                           Hon. [JUSTICE]
                                           Part [##]
                          [Plaintiff(s),]
                                           NOTICE OF MOTION
            -against-                      Return Date: [DATE]
                                           Time: [TIME]
[DEFENDANT(S)],                            Place: [Courtroom / Teams]
                          [Defendant(s).]
----------------------------------------- X

PLEASE TAKE NOTICE that upon the annexed Affirmation of
[NAME], affirmed [DATE], the accompanying Memorandum of
Law, and all prior pleadings and proceedings in this
action, Defendant [NAME] will move this Court at the
courthouse located at [ADDRESS], on [DATE] at [TIME],
or as soon thereafter as counsel can be heard, for an
order pursuant to:

   1. CPLR [SECTION], [DESCRIBE RELIEF]; and

   2. Such other and further relief as this Court deems
      just and proper.

PLEASE TAKE FURTHER NOTICE that, pursuant to CPLR
2214(b), answering papers, if any, shall be served at
least seven (7) days prior to the return date of this
motion.

Dated: [CITY], New York
       [Month Day, Year]

                              _______________________________
                              [Signature]
                              [PRINT NAME]
                              Self-Represented Defendant
                              [Address / phone / email]

TO:
[Name]
[Plaintiff's attorney address]
```

### Filling in the return date

CPLR 2214(b): minimum **8 days** notice; **add 5 days** for
mail service (CPLR 2103(b)(2)). Add the assigned Justice's
Part Rule additional notice period if any.

The return date must be on a day the Part hears motions —
typically a fixed weekday per Part Rules. Use
`ny-schedule-hearing` to pick the date.

## OSC template

```
SUPREME COURT OF THE STATE OF NEW YORK
COUNTY OF [COUNTY]
----------------------------------------- X
[CAPTION]

                                           Index No. [#####/YYYY]
                                           Hon. [JUSTICE]

                          [Plaintiff(s),]
                                          ORDER TO SHOW CAUSE
            -against-                     FOR [RELIEF]
                          [Defendant(s).]
----------------------------------------- X

Upon the annexed Affirmation of [NAME], affirmed
[DATE], and the exhibits attached thereto, it is hereby

ORDERED that [Plaintiff/Defendant] show cause before
[the IAS Part] in the courthouse located at [ADDRESS],
on [DATE], at [TIME], or as soon thereafter as the
parties can be heard, why an order should not be
entered:

   1. Pursuant to CPLR [SECTION], [RELIEF]; and

   2. For such other and further relief as the Court
      deems just and proper.

[TRO language if emergency relief sought:]
And it is further ORDERED that, pending hearing and
determination of this motion, [STAY/INJUNCTION], on
[CONDITIONS, e.g., posting of undertaking].

[Service direction:]
Sufficient service of this Order to Show Cause and the
underlying papers shall be made upon [Plaintiff/Defendant]
by [SERVICE METHOD] on or before [DATE], at least [#] days
prior to the return date hereof.

Dated: [CITY], New York
       [Month Day, Year]

                              _______________________________
                              HON. [JUSTICE NAME]
                              [Title]
```

The OSC is **brought to the Justice's chambers (or e-mailed
to the Part email) ex parte** with the supporting
affirmation. The Justice signs the OSC, setting the return
date and any TRO terms.

## Court emergency-OSC procedure

Most NY counties have an emergency-application protocol for
OSCs requiring same-day or next-day relief:

- **NY County**: 60 Centre Street, Room 130 — ex parte
  motion-support office
- **Kings County**: 360 Adams Street, Room 296 — ex parte
  motion-support office
- **Other counties**: chambers email; see Part Rules

## Cross-motion notice (CPLR 2215)

If responding to a motion with a cross-motion, the
cross-motion must be served at least **7 days** before the
return date (CPLR 2215). Format:

```
NOTICE OF CROSS-MOTION

PLEASE TAKE NOTICE that upon the annexed Affirmation of
[NAME], affirmed [DATE], Defendant [NAME] will cross-move
this Court at the date and time set in Plaintiff's pending
Notice of Motion, returnable on [DATE], for an order
pursuant to CPLR [SECTION], [RELIEF].
```

## Composition with other ny- skills

- `ny-statewide-format` — caption + format
- `ny-draft-motion` — coordinated with the substantive motion
- `ny-draft-declaration` — affirmation in support attached
- `ny-schedule-hearing` — selecting the return date per Part
  Rules
- `ny-deadlines` — CPLR 2214(b) 8-day minimum + 5-day mail
  add-on computation

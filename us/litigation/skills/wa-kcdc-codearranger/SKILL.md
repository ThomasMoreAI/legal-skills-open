---
name: wa-kcdc-codearranger
title: King County District Court
description: This skill should be used when drafting or filing documents in the King County District Court (KCDC), especially the South Division at Burien. Triggers include "KCDC", "King County District Court", "Burien courthouse", "civil motion docket", "note for motion docket in Burien", or any case with number format "25CIVxxxxxxKCX". Covers local practice, filing procedures, and the two-step motion-docket scheduling protocol (CivilMGT email request → clerk-issued date → e-filing within the clerk's deadline). Layer on top of the wa-statewide-format skill.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-kcdc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Civil Motion Docket
  path: references/civil-motion-docket.md
- title: Filing Procedures
  path: references/filing-procedures.md
- title: South Division Burien
  path: references/south-division-burien.md
---

# King County District Court

Use this skill in addition to `wa-statewide-format` when the case is in
King County District Court (KCDC). KCDC is a court of limited jurisdiction
(up to $100,000 controversy) with three civil divisions:

- **East Division — Redmond Courthouse**, 8601 160th Ave NE, Redmond WA 98052
- **South Division — Burien Courthouse**, 601 SW 149th St, Burien WA 98166
- **West Division — Seattle Courthouse**, 516 Third Ave, Room E-327, Seattle WA 98104

Each division publishes its own civil motions calendar and its own
Note for Motion Docket form. File in the division assigned to the case.

> **NOT LEGAL ADVICE.** These notes describe the venue's
> procedural mechanics as a drafting aid, not legal advice. Local
> rules and judge-specific practices change; verify with the clerk
> and the current local rules before relying on anything here.

## Caption — KCDC variant

```
        KING COUNTY DISTRICT COURT, SOUTH DIVISION
            IN AND FOR THE STATE OF WASHINGTON
```

Case numbers follow `25CIV######KCX` (year-CIV-sequence-KCX). Include the
number on the right side of the caption directly below "No."

## Authoritative source — pull the current form and calendar every time

The KCDC civil filings page is the single canonical source for the
rolling motions calendar, the division-specific Note for Motion
Docket forms, the current Zoom / dial-in information, the document-
code reference, and the filing instructions:

**https://kingcounty.gov/en/court/district-court/courts-jails-legal-system/civil-filings**

**Agent behavior**: when drafting the Note, requesting a hearing
date, preparing for an appearance, or confirming connection
details, fetch the current form and calendar from that page.
Hearing days, courtroom assignments, Zoom meeting IDs, dial-in
numbers, and technical-support contacts change without notice —
do not cache values across sessions or rely on specifics
hardcoded in this plugin.

## Civil motion docket — scheduling is a two-step process

Civil motions are heard on each division's **Civil Motion Docket**
on the days published in that division's rolling motions calendar.
Hearing days vary by division — consult the current calendar from
the civil filings page above before requesting a date.

**Step 1 — Email the calendar clerks to request a date**

Review the available dates on the relevant division's civil motions
calendar, then email `KCDC.CivilMGT@kingcounty.gov`. Per the court's
published instructions, the email **MUST** contain:

- Case number(s)
- Type of hearing requested
- Requested hearing date and time

Offering one or two alternative dates in the same email speeds up the
back-and-forth. The CivilMGT inbox is staffed centrally (Seattle Court)
and covers all three divisions.

**Step 2 — Clerk issues the date by email**

The clerks respond confirming whether the requested date/time is
available and, if so, reserve it. The confirmation identifies the
reserved courtroom and sets a filing deadline — normally
**2 business days** from the confirmation email — by which the filer
must e-file the packet. Do not pre-fill a courtroom code onto the
Note for Motion Docket before the clerk has issued it.

**Step 3 — E-file the packet through the portal**

E-file the Note for Motion Docket, Motion, supporting declaration(s),
exhibits, and Proposed Order through the [King County District Court
e-Filing / Case Access portal](https://kingcounty.gov/en/court/district-court)
by the clerk's stated deadline. Failure to timely e-file will result
in the hearing being **cancelled and the date released**.

> ⚠ **Motions noted for a date that was NOT issued by the clerks will
> be rejected.** Do not self-select a date from the calendar and e-file
> without a clerk-issued confirmation in hand.

Civil motions may be attended **in person or by Zoom**. The Zoom
meeting ID, dial-in numbers, phone mute / raise-hand codes, and
technical-support phone number for the courtroom are printed on
the division-specific Note for Motion Docket form — pull the
current form from the civil filings page above for every hearing.

## Confirmations, continuances, and strikes

- **Confirmations**: the moving party is **not** required to confirm
  that a scheduled matter is proceeding to hearing. (KCDC does not
  use a pre-hearing check-in.)
- **Continuances**: submit an **Agreed Motion to Continue and
  Proposed Order ex parte** through the e-Filing portal before the
  scheduled hearing date. Court staff cannot continue administratively.
- **Strikes**: the moving party must advise the court of a strike at
  least **1 business day** before the scheduled hearing, and must
  serve and notify the other party or parties of the strike.

## Filing rules of thumb

- **E-filing**: KCDC accepts e-filing through the King County portal; some
  documents (original signed orders, certified mail receipts) may also be
  filed in paper
- **Service**: Serve opposing counsel with any filing the same day by the
  method required under CRLJ 5 (email, mail, or personal service)
- **Proof of service**: Attach a Certificate of Service or Declaration of
  Service showing date, method, and recipient for every filing
- **Working copies**: KCDC generally does not require working copies for
  motions on the civil docket (unlike Superior Court), but confirm with
  chambers for longer motions

## Document set for a noted motion

Every motion noted for hearing should travel as a packet:

1. **Motion** (primary relief sought)
2. **Supporting Memorandum** (argument, only if motion is not
   self-contained)
3. **Supporting Declaration(s)** with exhibits
4. **Proposed Order** granting the relief
5. **Note for Civil Motion Docket** (scheduling form)
6. **Certificate / Declaration of Service**

When filing e-filing, upload each as a separate PDF.

## Scheduling email — recommended template

The email to `KCDC.CivilMGT@kingcounty.gov` does not need a Note
attached at this stage — the Note is filed later, after the clerk
issues the date. Keep the request short and structured:

```
To:      KCDC.CivilMGT@kingcounty.gov
Subject: Hearing Date Request — [Case Short Title],
         Case No. [Cause Number]

Dear Clerks:

I am the [pro se defendant / plaintiff / counsel] in [case short
title], Case No. [cause number], assigned to Judge [name] in the
[Division, e.g., South Division, Burien Courthouse].

I am requesting to reserve [preferred date] at [preferred time] for
a hearing on [exact motion title, e.g., Defendant's Motion to Compel
Discovery under CR 37(a) (applicable through CRLJ 26(f))]. If that
date is not available, I would alternatively request [alt 1, alt 2].

Thank you,
[Name][, pro se designation if applicable]
[Address]
[Phone]
[Email]
```

CC'ing opposing counsel on this email is **optional** at the
date-request stage (unlike at e-filing, where you must serve them
per CRLJ 5). Some practitioners CC counsel for transparency; others
wait until the date is issued and then include counsel on the
e-filing / service record.

## References

- `references/south-division-burien.md` — courthouse info, judges, rooms
- `references/civil-motion-docket.md` — scheduling, calendaring, noting
- `references/filing-procedures.md` — e-filing, service, working copies

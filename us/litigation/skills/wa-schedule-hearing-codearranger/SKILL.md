---
name: wa-schedule-hearing-codearranger
title: KCDC Hearing-Date Scheduling Email
description: Use this skill when the user needs to reserve a motion hearing date in King County District Court. Triggers include "reserve a hearing date", "schedule a hearing in KCDC", "email CivilMGT", "request a motion docket date", "how do I set a hearing in Burien", "what do I send to KCDC.CivilMGT", "I need to get a hearing date before I can file". Drafts the scheduling email — the required step 1 of the three-step KCDC motion-docket protocol (email → clerk-issued date → e-file within clerk's deadline). The Note for Motion Docket and packet are handled by `wa-draft-note` and `wa-file-packet` after the clerks issue the date.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-schedule-hearing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# KCDC Hearing-Date Scheduling Email

In King County District Court, a civil motion cannot simply be
self-noted for a date picked off the calendar. The moving party must
first email the calendar clerks (`KCDC.CivilMGT@kingcounty.gov`) to
**request** a date; the clerks issue a reserved date (with courtroom
and e-filing deadline) by reply. Motions noted for a date the clerks
did not issue are rejected.

**This skill handles step 1 of the three-step protocol.** Use it
before drafting the Note for Motion Docket and before e-filing
anything.

> **NOT LEGAL ADVICE.** This skill drafts a scheduling email as a
> procedural aid, not legal advice. Verify current KCDC clerk
> protocols and local-rule requirements before sending. Pair with
> substantive review by counsel where stakes warrant.

## Inputs to gather

1. **Case caption + cause number** — case short title and
   cause-number format `YYCIV######KCX`
2. **Division** — East (Redmond) / South (Burien) / West (Seattle)
3. **Assigned judge** — if known (from the summons or a prior order)
4. **Role** — pro se defendant / pro se plaintiff / counsel
5. **Exact motion title** — the title that will appear on the Note
   and on the filed motion, e.g., "Defendant's Motion to Compel
   Discovery under CR 37(a) (applicable through CRLJ 26(f))"
6. **Preferred hearing date + time** — pick from the division's
   published civil motions calendar
7. **1–2 alternative dates** — strongly recommended; reduces
   back-and-forth with the clerks
8. **Contact block** — filer name, address, phone, email

## Steps

1. **Load KCDC context.** Read `skills/wa-kcdc/SKILL.md` and
   `skills/wa-kcdc/references/civil-motion-docket.md` for the current
   protocol, plus any division-specific notes
   (`skills/wa-kcdc/references/south-division-burien.md`).

2. **Pull the current motions calendar.** Before suggesting a date,
   confirm availability from:

   https://kingcounty.gov/en/court/district-court/courts-jails-legal-system/civil-filings

   Hearing days rotate by division and change without notice — do
   not rely on dates cached in this plugin or on any prior session's
   assumptions.

3. **Do NOT attach the Note for Motion Docket.** The Note is filed
   through the portal **after** the clerks issue the date. Attaching
   it to the scheduling email is redundant and can cause confusion.

4. **Compose the email.** The subject line mirrors the caption so the
   clerks can match it to the division's calendar:

   ```
   To:      KCDC.CivilMGT@kingcounty.gov
   Subject: Hearing Date Request — [Case Short Title],
            Case No. [Cause Number]

   Dear Clerks:

   I am the [pro se defendant / pro se plaintiff / counsel] in
   [case short title], Case No. [cause number], assigned to
   Judge [name] in the [Division, e.g., South Division, Burien
   Courthouse].

   I am requesting to reserve [preferred date] at [preferred
   time] for a hearing on [exact motion title]. If that date is
   not available, I would alternatively request [alt 1, alt 2].

   Thank you,
   [Name][, pro se designation if applicable]
   [Address]
   [Phone]
   [Email]
   ```

5. **Verify the MUST-contain checklist.** Before offering the draft,
   confirm the email contains each of:

   - [ ] Case number(s) — in the subject line and body
   - [ ] Type of hearing requested — the exact motion title
   - [ ] Requested hearing date **and time**
   - [ ] 1–2 alternative dates (strongly recommended)
   - [ ] Filer's contact block

   These are the clerks' published MUST-contain items.

6. **CC opposing counsel? Optional.** Tell the user:
   - Some practitioners CC opposing counsel at this stage for
     transparency
   - Others wait until the date is issued and include opposing
     counsel on the e-filing service record
   - Either is acceptable under CRLJ 5; service is required at
     e-filing, not at scheduling

7. **Deliver the draft.** Options:
   - Paste-ready plain-text block (default) — the user copies it into
     Gmail / Outlook
   - `.eml` file saved to the case folder (optional) — use Write with
     `.eml` extension if the user prefers

8. **Explain the downstream flow** so the user knows what's next:

   - [ ] Send the email today
   - [ ] Wait for the clerks' confirmation (typically same day or
         next business day); confirmation identifies the reserved
         courtroom and sets an e-filing deadline — normally
         **2 business days** from the confirmation
   - [ ] Once the date is issued, hand off to `wa-draft-note` for the
         Note for Motion Docket (with the clerk-issued date)
   - [ ] Hand off to `wa-file-packet` to assemble motion + declaration
         + exhibits + proposed order + note + certificate of service,
         and e-file through the portal **by the clerk's deadline**
   - [ ] Serve opposing counsel the same day per CRLJ 5; attach a
         Certificate of Service to the filing
   - [ ] Failure to timely e-file will cancel the hearing and release
         the date

## Notes

- **Three-step protocol**: (1) request a date from CivilMGT; (2) the
  clerks issue the date by reply; (3) e-file the packet within the
  clerk's stated deadline
- The CivilMGT inbox is centralized (staffed at the Seattle / West
  Division court) even for Burien or Redmond matters
- **Continuances and strikes** are handled separately:
  - Continuances: file an Agreed Motion to Continue and Proposed
    Order ex parte through the portal (or a noted Motion to Continue
    if opposing won't stipulate)
  - Strikes: advise the court at least **1 business day** before the
    scheduled hearing and notify all parties
- For non-KCDC Washington courts, this skill is not the right tool —
  use `wa-draft-note` directly

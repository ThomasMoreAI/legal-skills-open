---
name: wa-draft-note-codearranger
title: Draft a Note for Motion Docket
description: Use this skill when the user asks to draft a Note for Motion Docket — the scheduling form that places a Washington motion on the court's calendar. Triggers include "note for motion docket", "note for hearing", "note this motion for hearing", "notice of hearing", "schedule the motion", "note on calendar", "KCDC note for motion docket". Scaffolds the form to a single page, detects KCDC cases automatically (cause number matches `\d{2}CIV\d{6}KCX`), and produces the KCDC variant when appropriate. Composes with `wa-statewide-format` (always) and `wa-kcdc` (if KCDC).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-draft-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Note for Motion Docket

Scaffold the scheduling form that places a motion on the court's
calendar. Required in most Washington civil courts before a motion can
be heard.

> **NOT LEGAL ADVICE.** This skill scaffolds a scheduling form as
> a drafting aid. The user — not the skill — chooses the motion,
> the date requested, and the relief sought. Verify every rule,
> deadline, and local-rule requirement before filing. Pair with
> substantive review by counsel where stakes warrant.

## Inputs to gather

1. **Court** — Which court? Load `wa-kcdc` if KCDC.
2. **Case caption** — Party names and case number
3. **Motion being noted** — Exact title of the motion
4. **Movant** — Who filed the motion?
5. **Hearing details:**
   - Proposed date and time
   - Courtroom or judge
   - In-person vs. Zoom
   - Time estimate (usually 10–20 min)
   - Oral argument requested?
6. **Companion documents** — List of everything filed with the motion

## Steps

1. **Load the companion skills.** Read:
   - `skills/wa-statewide-format/SKILL.md`
   - `skills/wa-statewide-format/references/templates/note-for-motion-docket.md`
   - If KCDC: `skills/wa-kcdc/SKILL.md` and
     `skills/wa-kcdc/references/civil-motion-docket.md`

2. **Detect court type:**
   - If KCDC (cause number matches `\d{2}CIV\d{6}KCX` or court is
     explicitly Burien / Redmond / Seattle KCDC): use the KCDC
     variant, include the DOCKET / SCHEDULING / DIVISION block at the
     top. **Gate on the clerk-issued date**: the Note should carry
     the date the clerks reserved in reply to the CivilMGT scheduling
     email — not a self-selected date. If the user hasn't gone
     through step 1 yet, route them to the `wa-schedule-hearing`
     skill before drafting the Note.
   - If superior court or another district court: use the statewide
     template

3. **Draft the note** using the structure from
   `note-for-motion-docket.md`. Keep it to a single page.

4. **Confirm timing compliance:**
   - Check CRLJ 6(d) (district) or CR 6(d) (superior) for notice
     requirements
   - For KCDC, motions are noted for a date issued by the clerks,
     which will already be on a valid hearing day for the division

5. **Pull current connection details from the canonical source.**
   For KCDC, the Zoom meeting ID, dial-in numbers, phone controls,
   and hearing tech-support number for the relevant courtroom are
   printed on the current Note for Motion Docket form published at:

   https://kingcounty.gov/en/court/district-court/courts-jails-legal-system/civil-filings

   Fetch the current form; do not reuse values from a prior filing or
   cached draft.

6. **List all companion documents** that travel with the motion:
   - Motion itself
   - Supporting memorandum (if separate)
   - Declaration with exhibits
   - Proposed Order
   - Certificate of Service

7. **Generate the .docx** and **deliver** via `computer://` link.

## Notes

- The note is a scheduling document, not an argument — keep it short
- An accurate time estimate helps the clerk slot the motion
- Always include a Certificate of Service or note service separately
- KCDC requires the three-step scheduling protocol (CivilMGT email →
  clerk-issued date → e-file within clerk's deadline). The Note is
  part of step 3.

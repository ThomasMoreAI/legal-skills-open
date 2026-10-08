---
name: wa-file-packet-codearranger
title: Assemble a Court Filing Packet
description: Use this skill when the user is ready to assemble and file a complete Washington court motion packet. Triggers include "assemble the packet", "I'm ready to file", "put together the filing", "finalize the motion for filing", "prepare the packet", "what goes in the packet", "organize the filing". Verifies that every required component is present (motion, declaration, exhibits, proposed order, note for motion docket, certificate of service), checks caption consistency across documents, confirms service lists match the parties, and produces filing instructions. For KCDC, enforces a **clerk-issued-date preflight** — the packet does not go out the door until a CivilMGT confirmation is in hand. Composes with `wa-quality-check`, `wa-schedule-hearing`, and the draft-* skills.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-file-packet
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Assemble a Court Filing Packet

Gather and organize all documents required for a complete Washington
court filing: motion, supporting declaration, exhibits, proposed
order, note for motion docket, and certificate of service.

> **NOT LEGAL ADVICE.** This skill is a procedural and drafting
> aid, not legal advice. Verify current rules, deadlines, and
> venue-specific practices before filing. Pair with substantive
> review by counsel where stakes warrant.

## Steps

1. **Identify the motion and case**

   If not already clear, ask the user:
   - Motion type (e.g., motion-to-dismiss, motion-to-compel,
     motion-for-summary-judgment, motion-to-vacate, motion-for-
     reconsideration, other)
   - Case folder (default: workspace folder)
   - Court (superior / district)
   - Hearing date (if scheduled)

2. **KCDC preflight — clerk-issued hearing date**

   If the case is in **King County District Court** (cause number
   matches `\d{2}CIV\d{6}KCX`, or the court is Burien / Redmond /
   Seattle KCDC), the hearing date **must be issued by the calendar
   clerks** before anything is e-filed. Self-noted dates are
   rejected.

   Before assembling the packet, ask:

   - [ ] Have you emailed `KCDC.CivilMGT@kingcounty.gov` to request
         a hearing date?
   - [ ] Have you received the clerks' confirmation reply reserving
         a specific date, time, and courtroom?
   - [ ] What is the clerks' stated **e-filing deadline** (normally
         2 business days from the confirmation)?

   **If any answer is "no" or "don't know":**
   - **STOP packet assembly.** Hand off to `wa-schedule-hearing`
     to draft the CivilMGT email
   - Explain: motions noted for a date that was not issued by the
     clerks will be rejected; timely e-filing by the clerks'
     deadline is what secures the reserved date

   **If all answers are "yes":**
   - Capture the clerk-issued date, time, courtroom, and e-filing
     deadline; surface them in the filing instructions (step 10
     below)
   - Record the clerk's deadline in the case calendar (via the
     `wa-deadlines` skill)

3. **Verify required components**

   The full packet for most motions includes:

   | Component | Required | Notes |
   |-----------|----------|-------|
   | Motion (with memorandum) | ✅ | pro-se drafting framework |
   | Supporting Declaration | ✅ | Each factual assertion |
   | Exhibits | If referenced | Labeled A, B, C... |
   | Proposed Order | ✅ | Specific relief |
   | Note for Motion Docket | ✅ | Sets the hearing |
   | Certificate of Service | ✅ | All parties served |
   | Meet-and-Confer Certification | Motions to compel (CR 26(i)) | |
   | Working Copies | Per local rule | Judge's courtesy copies |

   Glob the case folder for existing files; mark each as present or
   missing.

4. **List what exists and what is missing**

   Produce a checklist:

   ```
   Case: [case name, cause number, court]
   Motion: [type]
   Hearing: [date]

   PACKET STATUS:

   [x] Motion                      - Motion_to_Compel.docx
   [x] Supporting Declaration      - Declaration_of_Defendant.docx
   [ ] Exhibit A                   - MISSING — Deficiency Letter
   [ ] Proposed Order              - MISSING
   [ ] Note for Motion Docket      - MISSING
   [ ] Certificate of Service      - MISSING
   [x] CR 26(i) Certification      - included in motion
   ```

5. **Offer to create the missing pieces**

   For each missing item, offer to hand off to the appropriate
   drafting skill:

   - **Proposed Order** → `wa-draft-order`
   - **Note for Motion Docket** → `wa-draft-note`
   - **Declaration** → `wa-draft-declaration`
   - **Certificate of Service** — scaffold with the standard
     language (template in step 11 below)
   - **Exhibits** — ask the user what the referenced exhibits are;
     if files are named, copy them into the packet folder with
     uniform naming

6. **Verify caption consistency**

   Read the caption of each document. All should have:
   - Same court name
   - Same cause number
   - Same party names and styling

   Flag mismatches.

7. **Verify service matches parties**

   The Certificate of Service should list every party on the case.
   Typical debt-defense case:
   - Plaintiff's counsel — by email and/or U.S. mail
   - [Other parties if any]

   If the Certificate of Service omits a party, flag it.

8. **Quality check**

   Run the `wa-quality-check` skill on each document in the packet
   (or at minimum the main motion and proposed order).

9. **Assemble the packet**

   Copy or organize files in a packet folder under the case folder:

   ```
   [case-folder]/
   └── Packet-[motion-name]-[date]/
       ├── 01_Motion.docx
       ├── 02_Declaration.docx
       ├── 03_Exhibit_A.pdf
       ├── 04_Exhibit_B.pdf
       ├── 05_Proposed_Order.docx
       ├── 06_Note_for_Motion_Docket.docx
       ├── 07_Certificate_of_Service.docx
       └── INDEX.md
   ```

   Generate `INDEX.md` listing each file with a one-line description
   and the page count.

10. **Filing instructions**

    Produce a short filing-day summary:

    ```
    FILING INSTRUCTIONS

    Court: [court]
    Cause No.: [number]
    Hearing: [date/time]
    Hearing method: [in-person / Zoom — connection details on the
                    current Note for Motion Docket form]

    FILE WITH THE COURT:
    - Via [e-filing / in-person / mail]
    - Filing fee: $[amount] (or fee waiver attached)

    SERVE ON OPPOSING:
    - [Counsel name, firm, email, address]
    - Method: [email / U.S. mail / personal]

    WORKING COPIES (if required):
    - [Judge's chambers address]
    - Method: [required per local rule]

    DEADLINES:
    - Filing deadline: [X]
    - Proof of service filed: [X]
    - Reply due: [X]

    BRING TO HEARING:
    - Binder with all filings (3 copies if in-person)
    - Proposed Order (extras for judge and opposing)
    - Exhibits in a working-copies binder
    ```

11. **Offer to generate Certificate of Service**

    Standard template:

    ```
    [CAPTION]

              CERTIFICATE OF SERVICE

    I, [Name], declare under penalty of perjury under the laws
    of the State of Washington that on [date], I served a true
    and correct copy of the foregoing:

        [LIST OF DOCUMENTS]

    on the following parties by [method]:

        [Counsel name]
        [Firm]
        [Address]
        [Email]

    DATED this ___ day of __________, 20__.

    _______________________________
    [Name], pro se
    ```

12. **Final delivery**

    Output to the user:
    - Packet folder path (with `computer://` link)
    - `INDEX.md` (with `computer://` link)
    - Filing instructions summary
    - List of any outstanding issues

## Notes

- **Do not file for the user** — this skill assembles and organizes;
  the user files through the court's e-filing portal, by mail, or in
  person
- **Check local rules** — some counties require specific formats for
  working copies or specific filing procedures for certain motions
- **Ask about signatures** — the user needs to sign the motion,
  declaration, and certificate of service before filing. Offer to
  provide guidance on signing requirements
- **Check deadlines** via the `wa-deadlines` skill before finalizing

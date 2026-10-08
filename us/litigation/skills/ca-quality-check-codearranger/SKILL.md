---
name: ca-quality-check-codearranger
title: Quality Check — Format + Content (California)
description: 'Use to QC, review, format-check, or validate a California court document before filing. Triggers include "check this document", "QC this", "format check California", "review my motion before I file", "CRC compliant", "line numbering check", "check my caption", "proof of service California", "separate statement required", "CRC 3.1345", "memorandum page limit". Runs two-pass check: (1) CRC 2.100–2.119 format check (paper, margins, line spacing, fonts, line numbering, two-hole punch, footer) via scripts/format-check.py; (2) content check (caption, title, signature block, proof of service, meet-and-confer declaration, separate statement for motion to compel, facts supported by declaration, correct Judicial Council form version).'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-quality-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Quality Check — Format + Content (California)

Run a two-pass quality check on a California court document
before filing.

## Arguments

If the user names a file path, use it. Otherwise, glob the
workspace for recent `.docx` or `.pdf` files and ask which one
to check.

## Pass 1 — Format check (CRC 2.100–2.119)

1. **Run the checker:**

   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/format-check.py" "<path>"
   ```

2. **Parse output** and summarize:
   - PASS: item complies
   - WARN: item may deviate; user should verify manually
   - FAIL: item does not comply; must be fixed

3. **What is checked** (Cal. Rules of Court, rules 2.100–2.119):

   - **Paper size**: Letter (8.5" × 11") — rule 2.100
   - **Top margin, page 1**: at least 1", typically 1.5"–2" for
     caption space; rule 2.108(b)
   - **All other margins**: at least 1" — rule 2.108(a)
   - **Font**: Times New Roman or Courier 12pt; or proportional
     font 12pt — rule 2.105
   - **Line spacing**: 1.5 or double-spaced (rule 2.108(c));
     quotations > 50 words may be single-spaced and indented
   - **Line numbers**: required for all pleadings, motions, and
     other documents except Judicial Council forms (rule 2.109);
     line numbers in left margin; 28-line convention
   - **Footer**: page number centered or right-aligned
   - **Two-hole punch**: top of the document (rule 2.119; required
     for paper filing; commonly included even for e-filing)
   - **Page limit for memoranda**: 15 pages (rule 3.1113(d)) —
     20 pages with prior court permission
   - **Exhibits**: labeled with tabs or numbers; cover sheet for
     each; rule 3.1110(f)(4) bookmarks if 25+ pages (e-filed)
   - **No color text** except for exhibits

4. **For each failure**, explain:
   - What CRC requires
   - Where the deviation is
   - How to fix it

## Pass 2 — Content check

### Caption and header

- [ ] Court header: "SUPERIOR COURT OF CALIFORNIA" / "COUNTY OF
      [COUNTY]"
- [ ] Case number formatted correctly for the county and case type
- [ ] Parties correctly styled (Plaintiff/Defendant, not "vs." —
      California uses "v.")
- [ ] Department/division correct (LASC: Dept. ##; SFSC: Dept. ###)
- [ ] Document title in caption matches the body and the footer
- [ ] "IN PROPRIA PERSONA" or "Plaintiff/Defendant in Pro Per" on
      signature block if self-represented
- [ ] Bar number (State Bar No. ####) present if counsel; omitted
      if pro per
- [ ] Confidential personal data redacted (SSN last 4 only; account
      numbers last 4; minor children by initials) — CRC 1.20

### Document title

- [ ] Specific and accurate — "DEFENDANT'S NOTICE OF MOTION AND
      MOTION TO COMPEL FURTHER RESPONSES TO REQUESTS FOR PRODUCTION
      OF DOCUMENTS; MEMORANDUM OF POINTS AND AUTHORITIES; DECLARATION
      OF [NAME]" is correct; "Motion" alone is not
- [ ] Hearing date, time, and department/judge on the notice

### Signature block

- [ ] Name (printed or typed)
- [ ] Self-represented: "Defendant in Pro Per" or "Plaintiff in Pro
      Per"
- [ ] Counsel: "[Name], State Bar No. ####, Attorney for [Party]"
- [ ] Mailing address, phone, fax (optional), email
- [ ] Date signed

### Proof of service (Code Civ. Proc., § 1013a)

- [ ] Present at the end of every served document (or as a separate
      page)
- [ ] Identifies server (person 18+ who is NOT a party)
- [ ] Date of service
- [ ] Method (personal service, mail, e-service)
- [ ] Full name and address (or email) of each party served
- [ ] Declaration under penalty of perjury: "I declare under penalty
      of perjury under the laws of the State of California that the
      foregoing is true and correct."
- [ ] Signature of the server

### Memorandum page limit check

- [ ] Under 15 pages for most civil motions (CRC 3.1113(d))
- [ ] If over 15 pages: was leave of court obtained? (CRC 3.1113(e))
- [ ] Table of contents and table of authorities required if over 10
      pages (CRC 3.1113(f))

### Declarations

- [ ] Perjury clause: "I declare under penalty of perjury under the
      laws of the State of California that the foregoing is true and
      correct."
- [ ] Personal knowledge — each paragraph states facts the declarant
      knows personally
- [ ] Signed in California (or out-of-state with applicable penalty
      of perjury clause under Code Civ. Proc., § 2015.5)
- [ ] Numbered paragraphs (convention; not required but strongly
      favored)
- [ ] Date and place of execution
- [ ] No argument mixed with facts (argument belongs in memorandum)
- [ ] Exhibit list attached; each exhibit referenced in the body

### Exhibits

- [ ] Each exhibit identified (letter A, B, C... or Tab 1, 2, 3...
      — check local rules; LASC does not require one or the other)
- [ ] Each exhibit referenced in the declaration
- [ ] Cover sheet or separator for each exhibit
- [ ] Exhibits do not contain privileged or confidential information
      unless a proper redaction or sealing motion is filed

### Motion-specific checks

**Demurrer (Code Civ. Proc., § 430.10)**:
- [ ] Specific ground cited (§ 430.10(a) through (g))
- [ ] Meet-and-confer declaration attached (§ 430.41)
- [ ] Each cause of action separately analyzed
- [ ] If § 430.10(e) — identifies which elements of which cause of
      action fail

**Motion to strike (Code Civ. Proc., § 435)**:
- [ ] Meet-and-confer declaration attached (§ 435.5)
- [ ] Identifies specific passage(s) sought to be stricken

**Motion to compel further responses (Code Civ. Proc., § 2030.300,
§ 2031.310)**:
- [ ] Separate statement required (CRC 3.1345) — includes verbatim
      request, verbatim response, factual/legal reasons for
      compelling further response
- [ ] 45-day deadline from service of response verified
- [ ] Declaration of meet-and-confer re discovery dispute (Code Civ.
      Proc., § 2016.040)
- [ ] Sanctions request included (§ 2031.310(h))

**Summary judgment / summary adjudication (Code Civ. Proc., § 437c)**:
- [ ] Separate statement of undisputed material facts (CRC 3.1350)
- [ ] 75-day notice period verified
- [ ] Each element of each claim or defense analyzed
- [ ] Evidence cited to record (declaration, deposition, admission)
- [ ] Admissible evidence only (Code Civ. Proc., § 437c(d))

**Motion to vacate (Code Civ. Proc., § 473)**:
- [ ] Specific ground identified (mandatory / discretionary /
      § 473(d) void)
- [ ] If discretionary: within 6 months of entry
- [ ] Diligence narrative (when discovered, what done since)
- [ ] Meritorious defense (proposed answer attached)
- [ ] Lack of prejudice to opposing party

### Judicial Council forms

- [ ] Using current form version (check revision date on
      courts.ca.gov/forms)
- [ ] All required fields completed
- [ ] Case number and party names match the caption

### Tentative-ruling protocol

Many LASC and Bay Area departments issue **tentative rulings** the
day before the hearing (courts post them on the county's website
by 1:30–3:00 PM). Check:

- [ ] Does this court/department issue tentative rulings?
- [ ] Has the user checked the tentative ruling if the hearing is
      tomorrow?
- [ ] If the user intends to contest the tentative ruling, has the
      court's notice/telephonic-appearance procedure been followed?

## Pass 2 output

```
=== Content Check ===
Document: motion-to-compel-further.docx
Date: [today]

Caption: [PASS]
  - Court header: SUPERIOR COURT OF CALIFORNIA / COUNTY OF LOS ANGELES
  - Case No. 25STCV12345 — format correct for unlimited civil
  - Parties: Plaintiff / Defendant — "v." used
  - Dept. 32 — check court website to confirm assignment

Memorandum length: [WARN]
  - 17 pages. Exceeds CRC 3.1113(d) 15-page limit.
    Either shorten to 15 pages or obtain leave of court.

Separate statement: [PASS]
  - CRC 3.1345 separate statement present

Meet-and-confer: [PASS]
  - Declaration of meet-and-confer attached (§ 2016.040)

Proof of service: [FAIL]
  - Server is identified as the moving party (Defendant). The
    server must be a third party 18 years or older who is NOT
    a party. Correct by having a different person serve the
    documents and re-execute the proof of service.

Summary: 3 PASS, 1 WARN, 1 FAIL
```

## Composition

This skill ALWAYS composes with:

- **`ca-statewide-format`** — CRC 2.100–2.119 requirements
- **The relevant court skill** — for local-rule particulars
  (LASC tentative-ruling procedures; SFSC Department 302 rules;
  county-specific requirements)

It typically follows the draft-* skills and precedes
`ca-fact-check`.

## Cross-references

- `scripts/format-check.py` — the Pass 1 checker
- `ca-statewide-format` — CRC 2.100–2.119 baseline
- `ca-pro-se` — pro per conventions
- `ca-fact-check` — substantive verification pass
- `ca-law-references/references/citation-format.md` — California
  Style Manual rules

**NOT LEGAL ADVICE.** Generated content is a drafting aid;
verify against current rules and case law before filing.

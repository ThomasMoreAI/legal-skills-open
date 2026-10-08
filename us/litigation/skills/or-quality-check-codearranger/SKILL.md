---
name: or-quality-check-codearranger
title: Quality Check — Format + Content
description: 'Use this skill when the user asks to QC, review, format-check, or otherwise validate an Oregon court document before filing. Triggers include "check this document", "QC this", "is this UTCR compliant", "format check", "review my motion before I file", "run a compliance check", "check my declaration". Runs a two-pass check: (1) a UTCR 2.010 **format** pass via `scripts/format-check.py` (paper size, margins, fonts, color, pagination) and (2) a **content** pass applying the Parker framework checklist, citation form, caption accuracy, and common pro se red flags. Also auto-detects motion type and runs motion-specific checks (ORCP 21, ORCP 46, ORCP 47, ORCP 71). Composes with `or-statewide-format`, the relevant court skill (`or-multcc`, `or-wccc`, `or-county-courts`), and `or-pro-se`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-quality-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Quality Check — Format + Content

Run a two-pass quality check on an Oregon court document
before filing.

> **NOT LEGAL ADVICE.** Formatting and quality checks verify
> the surface — they don't tell the user whether the underlying
> legal position is sound. Verify current rules before filing;
> pair with substantive review by counsel where stakes warrant.

## Arguments

If the user names a file path, use it. Otherwise, glob the
workspace for recent `.docx` files and ask which one to check.

## Pass 1 — Format check (UTCR 2.010)

1. **Run the checker:**

   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/format-check.py" "<path>"
   ```

2. **Parse output** and summarize:
   - ✅ PASS: item complies
   - ⚠️ WARN: item may deviate; user should verify manually
   - ❌ FAIL: item does not comply; must be fixed

3. **What is checked:**
   - Paper size (Letter: 8.5" × 11")
   - Margins (1" on all sides at minimum; 3" top on page 1 is
     a strong recommendation per UTCR 2.010(2))
   - Line spacing (≥ 1.5 for body)
   - Font family (Times New Roman or similar proportional
     serif)
   - Font size (≥ 12pt in body)
   - No color text, no highlighting (UTCR 2.010 "black or
     blue-black ink only")
   - Footer contains PAGE and NUMPAGES fields (per the
     plugin's footer convention)
   - Numbered paragraphs (if declaration)

4. **For each failure**, explain:
   - What UTCR 2.010 requires
   - Where the deviation is
   - How to fix it (in Word or by regenerating with the
     docx-js template)

## Pass 2 — Content check

### Caption and header

- [ ] Court header is correct: "IN THE CIRCUIT COURT OF THE
      STATE OF OREGON" + "FOR THE COUNTY OF [COUNTY]"
- [ ] Cause number present and correctly formatted (e.g.,
      `25CV12345` for civil; `25SC#####` for small claims;
      `25DR#####` for domestic relations)
- [ ] Parties correctly styled (Plaintiff, Defendant —
      not "Plaintiff(s)" unless multiple, not "the parties")
- [ ] Document title on page 1 matches body and footer
- [ ] **Use "v."** between parties (not "vs.")
- [ ] **"pro se"** notation on signature block if applicable
- [ ] **OSB#** present if counsel; omitted if pro se
- [ ] UTCR 2.120 — confidential personal data redacted (SSN
      last 4 only; account numbers last 4; minor children
      initials; etc.)

### Structure (pro-se drafting framework, for motions)

- [ ] **MOTION** section is short and declarative
- [ ] **I. Relief Requested** — one paragraph, specific
- [ ] **II. Statement of Facts** — numbered, each with
      record citation
- [ ] **III. Statement of Issues** — 1 to 3 yes/no questions
- [ ] **IV. Evidence Relied Upon** — list with exhibit
      numbers (NOT letters)
- [ ] **V. Authorities** — rules and cases
- [ ] **VI. Argument** — organized by issue, with bold
      lead-in headings
- [ ] **VII. Conclusion** — one paragraph, restate relief
- [ ] Length ≤ 6 pages for memorandum

### Citations (Oregon Style Manual)

- [ ] Oregon cases cite `Or` / `Or App` (no periods)
- [ ] Parallel cites use `P2d` / `P3d` (no periods)
- [ ] Federal cases use `F` / `F2d` / `F3d` (no periods);
      `9th Cir` (no periods); `US` / `S Ct` (no periods)
- [ ] ORS cited as `ORS 12.080(1)` (no section symbol;
      lowercase letters in parens for sub-subs)
- [ ] ORCP cited as `ORCP 21 A(8)` (capital letter
      separated by space; parens for lower)
- [ ] OEC cited as `OEC 803(6)`
- [ ] UTCR cited as `UTCR 2.010(1)`
- [ ] USC cited as `15 USC § 1692k(a)(1)` (no periods in
      "USC"; section symbol)
- [ ] CFR cited as `12 CFR § 1006.30` (no periods)
- [ ] No `Rule 12(b)(6)` or `CR 12(b)(6)` (Federal /
      Washington — Oregon is `ORCP 21 A(8)`)
- [ ] No `RCW` cites (Washington — Oregon is `ORS`)

### Exhibits (if applicable)

- [ ] Exhibits **numbered**, not lettered (Oregon
      convention)
- [ ] Each exhibit referenced in the body by number
- [ ] Exhibit List present at end of declaration
- [ ] Cover page for each exhibit
- [ ] Pagination continuous through exhibits

### Declarations (if applicable)

- [ ] ORCP 1 E perjury clause present:
      "I declare under penalty of perjury under the laws of
      the State of Oregon that the foregoing is true and
      correct."
- [ ] Salutation at top: "I, [Name], declare under penalty
      of perjury..."
- [ ] Numbered paragraphs of substantive facts
- [ ] Date and place ("Executed at [City], Oregon")
- [ ] Signature block with name, role, address, phone, email
- [ ] No argument mixed with facts

### Motion-specific checks

**Motion to dismiss (ORCP 21)**:
- [ ] Specific sub-letter cited (A(1), A(2), ..., A(8), B, E)
- [ ] If A(8) "failure to state ultimate facts": brief
      identifies which element of which claim fails

**Motion to compel (ORCP 46 A)**:
- [ ] Meet-and-confer certification present and detailed
      (Multnomah SLR 5.045 / Washington Co SLR 5.046)
- [ ] Specific RFPs at issue identified
- [ ] ORCP 46 A(4)(a) fee-shifting requested

**Motion for summary judgment (ORCP 47)**:
- [ ] Filed at least 60 days before trial (verify against
      case schedule)
- [ ] Statement of undisputed material facts (with record
      citations)
- [ ] Each element of claim/defense analyzed
- [ ] Affidavits/declarations comply with ORCP 47 D
      (personal knowledge, admissible facts)

**Motion to vacate (ORCP 71)**:
- [ ] Specific ground identified (B(1)–B(6))
- [ ] If grounds (1)–(3): within 1 year of judgment
- [ ] Diligence narrative (when discovered, when filing)
- [ ] Meritorious defense (proposed answer attached)
- [ ] Lack of prejudice to opposing party

### Signature block

- [ ] Name in ALL CAPS or bold
- [ ] Role identified (Plaintiff/Defendant, pro se OR
      counsel of record + OSB#)
- [ ] Street address (Oregon city + ZIP)
- [ ] Phone
- [ ] Email
- [ ] No OSB# if pro se (and conversely OSB# IS present
      if counsel)

### Certificate of Service (UTCR 1.090)

- [ ] Present at the end of every served document
- [ ] Date of service
- [ ] Method (eService, email, mail, hand)
- [ ] Name and address (or email) of each party served
- [ ] Signature of the server

## Pass 2 output

The agent produces a report like Pass 1:

```
=== Content Check ===
Document: motion-to-compel.docx
Date: [today]

Caption: [PASS]
  - Court header correct
  - Case number 25CV12345 valid
  - Parties Plaintiff/Defendant
  - "v." used (not "vs.")
  - pro se on signature; no OSB#

Structure: [WARN]
  - PASS: All seven sections (I–VII) present
  - WARN: Memorandum is 7 pages — slightly over the 6-page
    Parker target; consider moving paragraph 5–6 of facts
    to the declaration

Citations: [FAIL]
  - PASS: ORCP cites use Oregon Style Manual format
  - FAIL: Two cases use Bluebook format ("Or." and "P.3d")
    instead of Oregon style ("Or" and "P3d"). Specifically:
      Mattiza v. Foster, 311 Or. 1, 803 P.3d 723 (1990)
      → Mattiza v. Foster, 311 Or 1, 803 P2d 723 (1990)

Exhibits: [PASS]
  - Numbered 1–4
  - Exhibit List present
  - Cover pages present

Summary: 4 PASS, 1 WARN, 1 FAIL
```

## Composition

This skill ALWAYS composes with:

- **`or-statewide-format`** — for the UTCR 2.010
  requirements
- **The relevant court skill** — for local-rule particulars

It typically follows the draft-* skills (which produce the
document) and precedes `or-fact-check` (which verifies the
substantive content).

## Cross-references

- `scripts/format-check.py` — the Pass 1 checker
- `or-statewide-format` — UTCR 2.010 baseline
- `or-pro-se` — pro-se drafting framework
- `or-fact-check` — substantive verification pass
- `or-law-references/references/citation-format.md` —
  Oregon Style Manual rules

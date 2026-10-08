---
name: wa-quality-check-codearranger
title: Quality Check — Format + Content
description: 'Use this skill when the user asks to QC, review, format-check, or otherwise validate a Washington court document before filing. Triggers include "check this document", "QC this", "is this GR 14 compliant", "format check", "review my motion before I file", "run a compliance check", "check my declaration". Runs a two-pass check: (1) a GR 14 **format** pass via `scripts/format-check.py` (paper size, margins, fonts, color, pagination) and (2) a **content** pass applying the pro-se drafting framework checklist, citation form, caption accuracy, and common pro se red flags. Also auto-detects motion type and runs motion-specific checks (CR 12(b)(6), CR 37, CR 56, CR 60). Composes with `wa-statewide-format`, `wa-kcdc`, and `wa-pro-se`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-quality-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Quality Check — Format + Content

Run a two-pass quality check on a Washington court document before
filing.

> **NOT LEGAL ADVICE.** Formatting and quality checks verify the
> surface — they don't tell the user whether the underlying legal
> position is sound. Verify current rules before filing; pair with
> substantive review by counsel where stakes warrant.

## Arguments

If the user names a file path, use it. Otherwise, Glob the workspace
for recent `.docx` files and ask which one to check.

## Pass 1 — Format check (GR 14)

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
   - Margins (1" on all sides at minimum; 3" top on page 1 is a
     recommendation, not a strict GR 14 requirement)
   - Line spacing (≥ 1.5 for body)
   - Font family (Times New Roman or similar proportional serif)
   - Font size (≥ 12pt in body)
   - No color text, no highlighting (GR 14(a) "no color markings")
   - Footer contains page numbers
   - Numbered paragraphs (if declaration)

4. **For each failure**, explain:
   - What GR 14 requires
   - Where the deviation is
   - How to fix it (either in Word or by regenerating with the
     docx-js template)

## Pass 2 — Content check

### Caption and header

- [ ] Court name correct
- [ ] Cause number present and correctly formatted (YY-CV-NNNNN-SEA
      for superior court; `YYCIV######KCX` for KCDC)
- [ ] Parties correctly styled (Plaintiff, Defendant — not
      "Plaintiff(s)" or initials unless a minor)
- [ ] Document title on page 1 matches body
- [ ] "PRO SE" notation on signature block if applicable
- [ ] GR 14.1 / GR 22 — confidential personal data (SSN, medical IDs,
      financial-account numbers) redacted

### Structure (pro-se drafting framework, for motions)

- [ ] **I. Relief Requested** — one paragraph, specific relief
- [ ] **II. Statement of Facts** — numbered paragraphs, each with
      record citation
- [ ] **III. Statement of Issues** — 1 to 3 yes/no questions
- [ ] **IV. Evidence Relied Upon** — list with exhibit letters
- [ ] **V. Authorities** — rules and cases
- [ ] **VI. Argument** — organized by issue, with headings
- [ ] **VII. Conclusion** — one paragraph, restate relief, proposed
      order reference
- [ ] Length ≤ 6 pages (for motion memoranda)

### Citations

- [ ] Every fact paragraph cites to the record (CP [#] or Exhibit
      [letter])
- [ ] Every legal proposition cites to a rule, statute, or case
- [ ] Washington cases cited in *Smith v. Jones*, 123 Wn.2d 456, 789
      P.2d 123 (1994) form
- [ ] Federal cases cited in *Smith v. Jones*, 123 F.3d 456 (9th Cir.
      1999) form
- [ ] Rules cited as CR 12(b)(6) or CRLJ 12(b)(6) (not "FRCP")
- [ ] Statutes cited in RCW format (RCW 4.16.040, not "Title 4
      section 4.16.040")
- [ ] Pincites for quotations
- [ ] Unpublished opinions carry GR 14.1 / 9th Cir. R. 36-3 caveats

### Pro se red flags

- [ ] No emotional language ("outrageous," "scandalous,"
      "disgraceful") — replace with "improper," "insufficient," "not
      supported by the record"
- [ ] No rhetorical questions
- [ ] No appeals to sympathy unrelated to the legal question
- [ ] No attacks on opposing counsel personally
- [ ] No "I think" or "I believe" in argument — replace with "the
      record shows" or "the law requires"
- [ ] Pronouns consistent — use "Defendant" or "[Name]" in third
      person (save "I" for declarations)
- [ ] No block quotes longer than 5 lines — summarize instead

### Declarations

- [ ] Starts with "I, [Name], declare under penalty of perjury under
      the laws of the State of Washington..."
- [ ] Ends with declaration under penalty language + date + signature
      + city
- [ ] All statements on personal knowledge
- [ ] Exhibits labeled A, B, C... and referenced in numbered
      paragraphs
- [ ] Exhibits attached (or described if filed separately)

### Service

- [ ] Proof of Service / Certificate of Service included or prepared
- [ ] Method of service noted (U.S. mail, email, in-person, e-filing
      per court rule)
- [ ] All parties served listed

### Motion-specific checks

Based on detected document type:

**Motion to Dismiss (CR 12(b)(6))**:
- [ ] Identifies the claim being challenged
- [ ] States the elements plaintiff must plead
- [ ] Shows each element not pled
- [ ] Requests dismissal without prejudice or with prejudice (justify
      if with prejudice)

**Motion to Compel (CR 37)**:
- [ ] Includes CR 26(i) / CRLJ 26(f) conference certification
- [ ] Attaches deficiency letter as exhibit
- [ ] Identifies each deficient response by number
- [ ] Requests specific production within a specific time
- [ ] Requests attorney fees and costs under CR 37(a)(4)

**Motion for Summary Judgment (CR 56)**:
- [ ] Identifies undisputed material facts (numbered paragraphs)
- [ ] Each fact cites to admissible evidence
- [ ] States the law and why no reasonable jury could find for
      opposing
- [ ] Attaches a Statement of Undisputed Facts or Statement of
      Material Facts in Support

**Motion to Vacate (CR 60)**:
- [ ] Cites specific CR 60(b) subsection
- [ ] Shows diligence (when learned, when filed)
- [ ] Attaches meritorious defense (except for void judgment)
- [ ] Supporting declaration of defendant

**Declaration**:
- [ ] Declaration under penalty clause present and correct
- [ ] Personal knowledge statements
- [ ] No argument, no legal conclusions
- [ ] Exhibits cited and attached

## Output format

```
Format check: [PASS / FAIL / X warnings]
  [summarize format-check.py output]

Content check:
  Caption: [PASS / issues]
  Structure: [PASS / issues]
  Citations: [PASS / issues]
  Pro se red flags: [none / list]
  Motion-specific: [PASS / issues]

Ready to file: [YES / NO — list blockers]

Recommended fixes:
  1. [specific fix]
  2. [specific fix]
  ...
```

## Notes

- **Do not auto-edit** without asking — show the report first, then
  offer specific edits
- Use `wa-statewide-format`, `wa-kcdc`, and `wa-pro-se` skill
  knowledge when interpreting the output
- This is a last-check pass — use after a full draft, not during
  scaffolding
- Color in exhibit screenshots is permitted under GR 14(a) when
  grayscale would make them illegible — the format checker flags
  these as warnings, not failures
- Always read the actual rule if in doubt:
  `skills/wa-statewide-format/references/gr-14-full-text.md`

---
name: co-quality-check-codearranger
title: Colorado Pre-Filing Quality Check
description: 'This skill should be used to QC, review, or validate a Colorado court document before filing. Triggers include "QC this Colorado document", "review my Colorado filing", "check this motion before I file it", "validate this Colorado declaration", "audit this Colorado packet", "Colorado pre-filing review", "run a quality check on my Colorado filing". Runs a two-pass check: (1) format pass — C.R.C.P. 10 + CJD 11-01 compliance, caption components, signature block, certificate of service; (2) content pass — Parker framework satisfaction (relief stated, rule cited, facts stated, conclusion offered), required-component completeness, packet consistency. Lighter touch than `co-fact-check` (which goes deep on evidentiary citations and sworn-vs-argued alignment).'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-quality-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Colorado Pre-Filing Quality Check

> **NOT LEGAL ADVICE.** This skill detects errors in form and
> structural completeness. It does not assess substantive legal
> sufficiency.

Use this skill as the **last step** before filing any Colorado court
document. Two passes.

## Pass 1 — Format

For a `.docx` filing, run `scripts/format-check.py` first:

```
python3 plugins/co-court-docs/scripts/format-check.py path/to/filing.docx
```

The format-check script validates:

- US Letter paper (8.5" × 11")
- 1-inch margins on all four sides (CJD 11-01)
- Body line spacing >= 1.5x
- 12-point body font
- Acceptable font family (Times New Roman / Arial / Century
  Schoolbook / Calibri / etc.)
- Black ink only (no colored text / highlight / shading)
- Footer with PAGE and NUMPAGES fields ("Page X of Y")
- Caption components (case number, division/courtroom)

Resolve any **FAIL** from the format check before continuing.

## Pass 1 supplemental — non-`.docx` format checks

If the source is markdown or text (e.g., an early draft), verify
manually:

- **Caption** — two-block layout: party block (left) + boxed
  case-number / division / courtroom block (right) under the
  "COURT USE ONLY" banner; court name centered above
- **Title** — in ALL CAPS, centered, between caption and body
- **Numbered paragraphs** — sequential without gaps
- **Signature block** — name, address, phone, email, attorney reg.
  no. (if applicable), role designation
- **Certificate of Service** — date, method, recipient(s)
- **Certificate of Conferral** under C.R.C.P. 121 § 1-15(8) if the
  motion is non-dispositive

## Pass 2 — Content

The content check applies the **pro-se drafting framework**:

### For a motion / brief:

- [ ] **Relief stated clearly** in the opening paragraph
- [ ] **Rule or statute citation** that grants the relief
- [ ] **Numbered factual paragraphs** with record cites (declaration
      ¶, complaint ¶, exhibit, admission)
- [ ] **Application of controlling authority** — case law applied to
      the facts (don't just cite cases; apply them)
- [ ] **Counter-arguments addressed** — anticipate and respond
- [ ] **Specific conclusion** — what exactly should the court do?
- [ ] **Proposed order attached / referenced**
- [ ] **Within page limit** (C.R.C.P. 121 § 1-15(1)(a)): 15 pages
      motion / response, 10 pages reply

### For a declaration:

- [ ] **Personal-knowledge foundation** in opening paragraph
- [ ] **Numbered factual paragraphs** — facts only, no argument
- [ ] **Exhibit references** match the attached exhibits
- [ ] **Verification clause** per C.R.S. § 13-27-104
- [ ] **Date and place of execution**
- [ ] **Signature** (no notary required for declaration)

### For a proposed order:

- [ ] **Caption identical** to the underlying motion
- [ ] **Findings separate from ordering clause**
- [ ] **Ordering clause mirrors** the motion's prayer for relief
- [ ] **Specific dates / amounts** filled in or appropriately
      bracketed for the judge
- [ ] **Judge signature line** at foot

### For an answer:

- [ ] **Each paragraph of the complaint addressed** (admit / deny /
      lack knowledge — no skipping)
- [ ] **Affirmative defenses pleaded** (statute of limitations,
      payment, etc. — see C.R.C.P. 8(c))
- [ ] **Compulsory counterclaims** pleaded (C.R.C.P. 13(a))
- [ ] **Prayer for relief** included

## Pass 3 — Packet consistency

If filing multiple documents as a packet (motion + declaration +
proposed order + certificate of service):

- [ ] **Same caption** across all documents (court, case number,
      parties, division, courtroom)
- [ ] **Same document title** referenced in the motion's certificate
      of service and the proposed order's title
- [ ] **Dates align** — certificate-of-service date matches signature
      date on the motion; declaration's "executed on" matches when
      the declaration was signed
- [ ] **Relief sought matches** between motion prayer and proposed
      order ordering clause (item-by-item)
- [ ] **All referenced exhibits** are attached to the declaration

## Pre-flight checklist

Before clicking "submit" on CCEFS:

| Check | Done |
|-------|------|
| `scripts/format-check.py` passes (no FAIL) | ☐ |
| Caption matches court, case number, division, courtroom | ☐ |
| Page limit not exceeded | ☐ |
| Certificate of Conferral included (if non-dispositive) | ☐ |
| Proposed Order drafted as separate document | ☐ |
| All exhibits attached and referenced | ☐ |
| Certificate of Service shows method, date, recipients | ☐ |
| Signature block has name, address, phone, email | ☐ |
| Attorney reg. no. included (or omitted with "Self-Represented") | ☐ |
| Filing fee paid or JDF 205/206 attached | ☐ |
| `co-fact-check` deep audit run (if high-stakes filing) | ☐ |

## Common Colorado pre-filing failures

1. **Missing C.R.C.P. 121 § 1-15(8) conferral certificate** —
   summary denial. Always include or invoke the dispositive-motion
   exemption (12(b), 56).
2. **Excess page count** — denied if not pre-cleared. Run page count
   before filing; request leave if >15 pages on a motion / response.
3. **Caption inconsistency** — proposed order shows division 12,
   motion shows division 14. Re-check after any case-management
   reassignment.
4. **Missing certificate of service** — many pro se filers forget.
   The CCEFS upload prompts for service info; provide it.
5. **Wrong court** — district court vs. county court (use the
   $25,000 threshold under C.R.S. § 13-6-104).

## Composition

- For deep evidentiary-citation review: `co-fact-check`
- For format generation: `co-statewide-format`
- For the specific document: `co-draft-motion`,
  `co-draft-declaration`, `co-draft-order`, `co-draft-note`
- For court-specific overlay: `co-denver`, `co-arapahoe`,
  `co-county-courts`
- For the final filing step: `co-file-packet`

## References

- `references/format-checklist.md`
- `references/content-checklist.md` — pro-se drafting framework satisfaction
  checks
- `references/packet-consistency-checklist.md`
- `references/preflight-checklist.md`

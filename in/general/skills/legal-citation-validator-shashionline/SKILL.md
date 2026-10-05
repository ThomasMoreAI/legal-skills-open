---
name: legal-citation-validator-shashionline
title: Legal Citation Validator
description: Validate statutory citations, case law references, and legal formatting according to Indian legal citation standards. This skill should be used when working with Indian legal documents, protocols, opinions, or any content containing statutory references or case law citations to ensure accuracy and proper formatting.
author: shashionline
author_url: https://github.com/shashionline/indian-law-plugin/tree/master/skills/legal-citation-validator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: general
language: en
sources:
- title: Citation Formats
  path: references/citation-formats.md
- title: Court Abbreviations
  path: references/court-abbreviations.md
- title: Landmark Cases Index
  path: references/landmark-cases-index.md
- title: Statutory Index
  path: references/statutory-index.md
---

# Legal Citation Validator

This skill provides validation and formatting guidance for Indian legal citations, statutory references, and case law according to established legal citation standards.

## Purpose

Ensures precision and accuracy in legal writing by:
1. Validating statutory section references against actual legislation
2. Formatting case law citations according to AIR/SCR/SCC standards
3. Detecting common citation errors and inconsistencies
4. Providing proper abbreviated forms for courts and authorities

## When to Use This Skill

Use this skill when:
- Writing legal protocols, opinions, or analysis
- Citing statutory provisions (e.g., "Section 14 of the Constitution")
- Referencing case law (e.g., landmark judgments)
- Drafting legal documents requiring precise citations
- Reviewing legal content for citation accuracy
- Creating cross-references between legal provisions

## Citation Standards

### 1. Statutory Citations

**Format**: `[Act Name], [Year], Section [Number]`

**Examples**:
- ✅ CORRECT: "Section 21 of the Constitution of India, 1950"
- ✅ CORRECT: "Section 300 IPC" (when IPC context is clear)
- ✅ CORRECT: "Article 14 of the Constitution"
- ❌ INCORRECT: "Article 14" (without Act reference in first mention)
- ❌ INCORRECT: "Sec. 21" (use "Section" in formal writing)

**Rules**:
1. First mention: Full Act name + year + Section number
2. Subsequent mentions: Abbreviated form acceptable if unambiguous
3. Use "Section" for statutes, "Article" only for Constitution
4. Clause/sub-section format: "Section 14(1)(a)"

### 2. Case Law Citations

**Primary Formats** (in order of preference):
1. **AIR (All India Reporter)**: `[Case Name] v. [Respondent], AIR [Year] [Court] [Page]`
2. **SCR (Supreme Court Reports)**: `([Year]) [Volume] SCR [Page]`
3. **SCC (Supreme Court Cases)**: `([Year]) [Volume] SCC [Page]`

**Examples**:
- ✅ CORRECT: "Kesavananda Bharati v. State of Kerala, AIR 1973 SC 1461"
- ✅ CORRECT: "Maneka Gandhi v. Union of India, (1978) 1 SCC 248"
- ✅ CORRECT: "Vishaka v. State of Rajasthan, AIR 1997 SC 3011"
- ❌ INCORRECT: "Kesavananda case (1973)" (informal, lacks citation)
- ❌ INCORRECT: "AIR 1973 1461" (missing court abbreviation)

**Court Abbreviations**:
- `SC` = Supreme Court of India
- `Del` = Delhi High Court
- `Bom` = Bombay High Court
- `Cal` = Calcutta High Court
- `Mad` = Madras High Court
- (Refer to @.claude/skills/legal-citation-validator/references/court-abbreviations.md for complete list)

### 3. Constitutional Citations

**Format**: `Article [Number], Part [Part Number if relevant], Constitution of India`

**Examples**:
- ✅ CORRECT: "Article 21, Part III, Constitution of India"
- ✅ CORRECT: "Articles 14-18 (Right to Equality)"
- ✅ CORRECT: "Article 32 (Constitutional Remedies)"
- ❌ INCORRECT: "Art. 21" (use "Article" in formal writing)

### 4. Amendment Citations

**Format**: `[Ordinal Number] Amendment, [Year]` OR `Constitution (Amendment) Act, [Year]`

**Examples**:
- ✅ CORRECT: "42nd Amendment, 1976"
- ✅ CORRECT: "Constitution (Forty-Second Amendment) Act, 1976"
- ✅ CORRECT: "44th Amendment (repealed Emergency provisions)"

## Validation Workflow

### Step 1: Identify Citations
Scan document for patterns:
- "Section [number]"
- "Article [number]"
- Case names (capitalized party names with "v." or "vs.")
- "AIR [year]", "SCC", "SCR" patterns
- Act names with years (e.g., "Act, 1872")

### Step 2: Validate Format

Check each citation against standards in @references/citation-formats.md:
- Proper spacing (e.g., "AIR 1973 SC 1461" not "AIR1973SC1461")
- Correct abbreviations (e.g., "SC" not "S.C." for Supreme Court)
- Comma placement (e.g., "v." followed by respondent name)
- Year format consistency (e.g., 1973 not '73)

### Step 3: Verify Statutory References

For statutory citations:
1. Check section number exists in referenced Act
2. Verify subsection/clause notation (e.g., "Section 14(1)" not "Section 14-1")
3. Confirm Act year is correct (e.g., "IPC, 1860" not "IPC, 1860")

**Common Errors**:
- ❌ "Section 301 IPC" (IPC has 511 sections, no Section 301 exists - correct is "Section 300")
- ❌ "Article 370A" (no such Article - correct is "Article 370")
- ❌ "Section 14(a)" (should be "Section 14(1)" if referring to first clause)

### Step 4: Validate Case Citations

For case law:
1. Check party names are capitalized correctly
2. Verify "v." (not "vs" or "vs." in formal citations)
3. Confirm court abbreviation is standard
4. Check year is within realistic range (1950-2025 for independent India)

Refer to @references/landmark-cases-index.md for verification of major cases.

### Step 5: Cross-Reference Check

Ensure citations are consistent:
- Same case cited the same way throughout document
- Same statutory provision formatted consistently
- Abbreviations used consistently (don't mix "IPC" and "Indian Penal Code" randomly)

### Step 6: Generate Validation Report

Output format:
```
✓ VALID CITATIONS: [count]
  - Statutory: [count]
  - Case law: [count]
  - Constitutional: [count]

⚠ WARNINGS: [count]
  - [Description of inconsistency or formatting issue]

✗ ERRORS: [count]
  - Line [X]: [Error description and suggested correction]
```

## Reference Files

### Primary References
- **@references/citation-formats.md**: Complete citation format rules
- **@references/court-abbreviations.md**: All court short forms (25 High Courts, tribunals)
- **@references/landmark-cases-index.md**: Major cases with verified citations
- **@references/statutory-index.md**: All major Acts with year and section ranges

### Usage
When validating a citation, read the relevant reference file:
```
Read @.claude/skills/legal-citation-validator/references/citation-formats.md
```

## Common Citation Errors to Detect

### 1. Informal Language
- ❌ "the Kesavananda case" → ✅ "Kesavananda Bharati v. State of Kerala, AIR 1973 SC 1461"
- ❌ "Section 21 judgment" → ✅ "interpretation of Article 21 in Maneka Gandhi v. Union of India"

### 2. Incomplete Citations
- ❌ "AIR 1978 597" → ✅ "AIR 1978 SC 597"
- ❌ "Section 14" (first mention) → ✅ "Section 14 of the Indian Contract Act, 1872"

### 3. Incorrect Abbreviations
- ❌ "S.C." → ✅ "SC"
- ❌ "vs." or "vs" → ✅ "v."
- ❌ "Sec." → ✅ "Section" (formal) or no abbreviation

### 4. Formatting Errors
- ❌ "AIR1973SC1461" → ✅ "AIR 1973 SC 1461" (spacing)
- ❌ "Article-21" → ✅ "Article 21" (no hyphen)
- ❌ "Section 14 (1)" → ✅ "Section 14(1)" (no space before parenthesis)

## Integration

### With Other Skills
- Works with **legal-opinion-drafter** to ensure citations in opinions are valid
- Supports **legal-research-assistant** in formatting research output
- Used by Indian Law agents when generating legal analysis

### With Protocols
- Validates citations in all IL-* protocols
- Ensures cross-protocol references are accurate
- Maintains citation consistency across protocol updates

### With Hooks
- Can be triggered by **legal-precision-check** hook on Write/Edit operations

## Examples

### Example 1: Validate Constitutional Citation
**Input**: "Art. 21"
**Validation**:
- ⚠ WARNING: Use "Article" not "Art." in formal writing
- ✓ Section number valid
**Suggested**: "Article 21, Part III, Constitution of India"

### Example 2: Validate Case Citation
**Input**: "Kesavananda vs State of Kerala (1973)"
**Validation**:
- ✗ ERROR: Use "v." not "vs" in formal citations
- ✗ ERROR: Missing reporter citation (AIR/SCR/SCC)
- ⚠ WARNING: Party name should include "Bharati"
**Suggested**: "Kesavananda Bharati v. State of Kerala, AIR 1973 SC 1461"

### Example 3: Validate Statutory Reference
**Input**: "Sec. 14(a) of ICA"
**Validation**:
- ⚠ WARNING: Use "Section" not "Sec." in formal writing
- ✗ ERROR: Clause notation should be (1) not (a) for first clause
- ⚠ WARNING: First mention should spell out "Indian Contract Act, 1872"
**Suggested**: "Section 14(1) of the Indian Contract Act, 1872"

## Tools Required

This skill uses:
- **Read**: To access reference files
- **Grep**: To search for citation patterns in documents

## Disclaimer

This skill provides formatting guidance based on common Indian legal citation practices. It does not constitute legal advice. For authoritative citation rules, consult:
- Supreme Court Rules, 2013 (Order VI, Rule 3)
- Bluebook (adapted for Indian law)
- Individual court citation rules

Verify all statutory and case citations against official sources (India Code, Indian Kanoon) before final publication.

---

**Skill Version**: 1.0.0
**Last Updated**: 2025-12-05
**Part of**: Indian Law Knowledge Ecosystem
**Dependencies**: None

---
name: appellate-formatting
title: Appellate Document Formatting
description: Generates appellate-filing-ready Tables of Contents, Tables of Authorities, and Certificates of Compliance under FRAP 32(g) and related rules. Produces defensible word-count calculations with transparent exclusions and anti-hallucination guardrails for pagination and citations. Covers federal circuits, state appellate courts, and U.S. Supreme Court variations. Use when building TOC, TOA, compliance certificates, formatting briefs for filing, or when the user mentions word count calculation, FRAP 32 compliance, appellate brief assembly, or page numbering.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/appellate-formatting
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Appellate Document Formatting

Produces TOCs, TOAs, and Certificates of Compliance with accuracy guarantees and transparent placeholders where verification is required. The primary risk in AI-assisted appellate formatting is hallucinated page numbers and citations — use `[__]` placeholders aggressively rather than guessing.

## Quick Start

Gather before drafting (unless user says "use defaults"):

1. **Brief text** — final or near-final; label output "DRAFT" if still revising
2. **Forum/case metadata** — court, circuit/state, case number, caption, brief type
3. **Formatting** — font (proportional/monospaced), name/size, spacing, margins
4. **Filing method** — CM/ECF, paper, or both; separate or combined certificate
5. **Court orders** — any modified length limits
6. **Local rules** — TOA format, hyperlinking, bookmarks, addendum
7. **Word count** — final count from drafting platform plus believed exclusions

**Defaults** (if user doesn't specify): FRAP 32 federal circuit rules; proportional 14-pt font; `[__]` page placeholders; word count marked as estimate.

**Stop and ask** if forum, brief type, or formatting details are missing — certificate language, limits, and exclusions depend on these.

## Core Workflow

### 1. Identify Governing Authority

| Forum | Primary Rules | Certificate Rule | Notes |
|-------|--------------|-----------------|-------|
| Federal (FRAP) | FRAP 28, 32 | FRAP 32(g) | Verify current word limits |
| U.S. Supreme Court | Rules 33, 34 | Rule 33.1(g) / 33.2 | Booklet vs. letter have different limit types |
| State appellate | Varies | Varies | Do NOT assume state rules mirror FRAP |

**FRAP type-volume limits** (verify current):

| Document Type | Word Limit |
|--------------|------------|
| Principal brief (opening/response) | 13,000 |
| Reply brief | 6,500 |
| Amicus brief (FRAP 29) | Verify per rule |

### 2. Generate TOC

1. Confirm sections match FRAP 28 required components (if federal)
2. Build heading map preserving exact wording, capitalization, numbering
3. **Never rewrite headings** — TOC must match brief verbatim
4. Default depth: major headings + two subheading levels; follow local rule if specified

**Pagination:**
- Paginated PDF → extract page numbers directly
- Unpaginated text → `[__]` placeholders, label: `"DRAFT—PAGE NUMBERS TO BE UPDATED AFTER PAGINATION"`
- **Never fabricate page numbers**
- Front matter: lowercase Roman numerals (i, ii, iii); body: Arabic numerals (1, 2, 3)

**Template:**

```
TABLE OF CONTENTS

CORPORATE DISCLOSURE STATEMENT ................. i
TABLE OF AUTHORITIES ........................... ii
STATEMENT OF JURISDICTION ...................... 1
STATEMENT OF ISSUES ............................ 2
STATEMENT OF THE CASE .......................... 3
SUMMARY OF ARGUMENT ............................ 10
ARGUMENT ....................................... 12
  I.  [Point Heading Verbatim] .................. 12
      A. [Subheading Verbatim] .................. 12
      B. [Subheading Verbatim] .................. 14
  II. [Point Heading Verbatim] .................. 18
CONCLUSION ..................................... 30
CERTIFICATE OF COMPLIANCE ...................... 31
CERTIFICATE OF SERVICE ......................... 32
```

### 3. Build Table of Authorities

Parse all citations from brief text. Validate each actually appears on listed pages.

**Categories (in order):**

| Category | Sort Order |
|----------|-----------|
| Cases | Alphabetical by first party name |
| Constitutional Provisions | By article/amendment |
| Statutes | By code and section number |
| Rules | By rule number |
| Other Authorities | Alphabetical by author/title |

**Rules:**
- Copy citations exactly from brief — never add reporters, volumes, or years not in text
- Incomplete citation → include as-is, flag: `[Citation appears incomplete; verify reporter and year]`
- "passim" only when cited 5+ times and jurisdiction permits
- Capture footnote citations
- Sort "In re" and "Ex parte" correctly

**Template:**

```
TABLE OF AUTHORITIES

Cases                                              Page(s)
Anderson v. Liberty Lobby, Inc.,
  477 U.S. 242 (1986) ............................ 14, 16
Celotex Corp. v. Catrett,
  477 U.S. 317 (1986) ............................ 14

Statutes
28 U.S.C. § 1291 ................................. 1
42 U.S.C. § 1983 ................................. 3, 7, 14

Rules
Fed. R. App. P. 28 ............................... 1
Fed. R. App. P. 32 ............................... 31

Other Authorities
16A Charles Alan Wright et al., Federal Practice
  & Procedure § 3949 (5th ed. 2020) .............. 15
```

### 4. Word Count and Certificate

**Bifurcated count:**

```
Total Words (entire document):        [X]
− Excluded per FRAP 32(f):            [Y]
  - Cover, Disclosure, TOC, TOA
  - Appearance of counsel, Signature block
  - Certificate of Compliance/Service
  - Addendum (statutes/rules/regulations)
= Net Words for Compliance:           [Z]
```

**Rules:**
- Verify current FRAP 32(f) exclusion categories
- Count from source document (Word/WordPerfect), not PDF OCR
- Within 2% of limit → flag and recommend trimming
- User asks to exclude non-exempt sections → **refuse**, explain options
- Always state: *"Word count is an estimate. Attorney must perform final count using filing software."*

**FRAP 32(g) certificate template:**

```
CERTIFICATE OF COMPLIANCE

Pursuant to Fed. R. App. P. 32(g)(1), I certify that this brief complies
with the type-volume limitation of Fed. R. App. P. 32(a)(7)(B) because
this brief contains [____] words, excluding the parts of the brief
exempted by Fed. R. App. P. 32(f).

This brief also complies with the typeface requirements of Fed. R. App. P.
32(a)(5) and the type-style requirements of Fed. R. App. P. 32(a)(6)
because it has been prepared in a proportionally spaced typeface using
[Software Name] in [Font Size]-point [Font Name].

_____________________________
[Attorney Name]
```

### 5. Cross-Verification

```
- [ ] Every TOC heading matches body heading verbatim
- [ ] Every TOA authority appears on listed pages
- [ ] Certificate word count matches final document count
- [ ] Caption, case number, party names consistent throughout
- [ ] Font/margins uniform (including footnotes if required)
- [ ] Front matter: Roman numerals; body: Arabic numerals
- [ ] No orphaned headers at page bottoms
- [ ] PDF text-searchable with bookmarks (if required)
- [ ] TOA page numbers not shifted by TOA insertion
- [ ] Certificate cites correct rule subsections for current year
```

After delivery, confirm with user:
1. Are headings finalized or should TOC be marked draft?
2. Does drafting software word count match the estimate?
3. Any local rule requirements to verify?
4. Generate addendum or handled separately?

State: *"Generated based on [Federal/State] rules for [Specific Circuit/Court]. All word counts, page numbers, and citations must be independently verified before filing."*

## Jurisdiction Variations

| Jurisdiction | Key Variation |
|-------------|--------------|
| 5th & 11th Circuits | Certificate of Interested Persons (CIP) required before TOC |
| 9th Circuit | Statement of Related Cases often excluded from word count |
| California (Rule 8.204) | 14,000-word limit for principal brief; different attachment rules [VERIFY] |
| U.S. Supreme Court | Booklet (Rule 33.1) vs. letter (Rule 33.2) — different limit types |
| State courts generally | May use page limits, different fonts/margins, separate word-count affidavits |

## Guardrails

- **Never fabricate** page numbers, word counts, citations, or rule references
- **Never "improve" citations** — do not add information not in the brief without attorney confirmation
- Unverifiable information → use `[VERIFY]` or `[__]` placeholders
- All outputs require licensed attorney review before filing
- Certificates are formal court representations — Model Rule 3.3 (Candor) applies
- Do not disclose sealed/confidential material in public-facing components
- If user requests certificate citing wrong authority or limits → refuse, explain correct rule

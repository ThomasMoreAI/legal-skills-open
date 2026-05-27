---
name: court-formatting
title: Court Document Formatting
description: Standardizes U.S. court-filing formatting for pleadings, motions, and briefs. Enforces caption structure, margins, fonts, spacing, pagination, line numbering, and e-filing constraints. Use when formatting court documents, preparing filings, or validating local-rules compliance.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/court-formatting
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Court Document Formatting

Apply court formatting requirements using a local-rules-first workflow. Local rules and judge-specific standing orders always control over baselines.

## Prerequisites

Gather before starting:

1. Court, division, and governing rule set (FRCP/FRAP/state + local rules)
2. Case number and full party names
3. Document type (pleading, motion, brief, notice, etc.)
4. Judge's individual practices or standing orders
5. E-filing portal requirements and file-size limits
6. Required certificates (service, word count, compliance)

## Core Workflow

### Step 1 — Identify Controlling Sources

Collect in priority order:

1. Judge's individual practices / standing orders
2. Local rules
3. General rules (FRCP/FRAP/state)
4. Court-provided forms or templates
5. E-filing portal requirements

### Step 2 — Apply Baseline Formatting

Apply defaults, then override per local rule:

| Element | Default | Override by |
|---|---|---|
| Paper | 8.5 × 11" | Local rule |
| Margins | 1" all sides | Local rule |
| Font | 12 pt serif (e.g., Times New Roman) | Local rule |
| Body spacing | Double-spaced | Local rule |
| Pagination | Consecutive page numbers | Local rule |
| Line numbers | If required by jurisdiction | Local rule |
| Block quotes | Single-spaced, indented | Local rule |
| Footnotes | Single-spaced, same or smaller font | Local rule |

### Step 3 — Build the Caption

Required elements (verify each against docket):

- Court name (full official name)
- Division (if applicable)
- Party names (exactly as on docket)
- Case number
- Document title
- Filing party designation (if required)
- Assigned judge / magistrate (if required)

Template:

```
IN THE [COURT NAME]
[DIVISION, IF APPLICABLE]

[PLAINTIFF NAME],                     )
     Plaintiff,                       )
v.                                    )   Case No. [NUMBER]
[DEFENDANT NAME],                     )
     Defendant.                       )

[DOCUMENT TITLE]
```

### Step 4 — Check Local Variations

Verify each item against local rules:

- [ ] Page or word limits (and what is excluded from the count)
- [ ] Font typeface and minimum size
- [ ] Spacing rules for body, headings, block quotes, footnotes
- [ ] Line numbering requirements
- [ ] Signature block format
- [ ] Certificate of service content and placement
- [ ] Exhibit labeling, pagination, and separators
- [ ] Proposed order format and file type
- [ ] Redaction rules and notation

### Step 5 — E-Filing Compliance

- [ ] File format: PDF or PDF/A as required
- [ ] Scanned PDFs are OCR'd (unless court prohibits)
- [ ] File size within portal limits; split if needed
- [ ] Bookmarks included for long filings
- [ ] Appendices/exhibits uploaded per portal rules (separate or combined)
- [ ] Privacy redactions applied

### Step 6 — Final Compliance Check

- [ ] Caption matches docket exactly (case number, division, party names)
- [ ] Page/word limits satisfied
- [ ] All required certificates included in correct format and location
- [ ] All exhibits labeled and cross-referenced in text
- [ ] File name follows local-rule naming convention
- [ ] E-filing requirements satisfied

## Common Pitfalls

- **Assuming baselines apply**: Never assume a default format is correct without checking local rules first.
- **Caption mismatches**: Party names, case number, and court title must match the docket exactly — do not rephrase or abbreviate.
- **Missing certificates**: Omitting certificate of service or word-count certificate is a common rejection reason.
- **Non-searchable PDFs**: Ensure all PDFs are text-searchable unless the court explicitly forbids OCR.
- **Unclear requirements**: If any formatting rule is ambiguous, flag it and request the exact rule citation before proceeding.

---

**Key changes made:**

- **Removed `tags`** — not part of the Agent Skills spec
- **Tightened description** — removed "Trigger keywords" list (the description itself contains discoverable terms); kept third-person voice
- **Added priority order** to Step 1 (controlling sources) — the original was a flat list with no hierarchy
- **Converted Steps 4-6 to checklists** (`- [ ]`) — enables copy-and-track workflow per best practices
- **Replaced "Guidelines" section with "Common Pitfalls"** — more actionable, avoids restating what's already implicit in the workflow steps
- **Reduced from 127 lines to ~95 lines** — removed redundant section headers ("Output Structure / Process"), duplicate information, and verbose labels while preserving all domain-accurate content

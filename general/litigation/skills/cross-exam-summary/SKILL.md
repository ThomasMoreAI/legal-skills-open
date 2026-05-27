---
name: cross-exam-summary
title: Cross-Examination Key Points Summary
description: Generates a structured cross-examination summary from depositions, exhibits, and discovery organized by witness and theme with pinpoint citations. Use when preparing for trial cross-examination, witness impeachment planning, deposition analysis, or building courtroom reference sheets.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/cross-exam-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Cross-Examination Key Points Summary

Produces an actionable cross-exam reference organized by witness and theme, with pinpoint citations for courtroom use.

## Prerequisites

- Depositions/transcripts with page:line numbers
- Exhibits (documents, emails, contracts)
- Discovery responses (interrogatories, RFAs, document production)
- Witness list for anticipated opposing witnesses
- Client's case theory and key elements to prove/defend

## Quick Start

1. Identify all witnesses and group testimony by theme (not chronology)
2. For each witness-theme pair, extract impeachment points, admissions, and contradictions
3. Tag each point by function, cite every source with pinpoint references
4. Build the quick-reference table from highest-impact points
5. Cross-reference exhibits to witnesses and contradictions

## Output Structure

### Quick-Reference Table (Top of Document)

| Witness | Top Impeachment Point | Source | Theme |
|---------|----------------------|--------|-------|
| {Name} | {One-line summary} | {Doc, p.XX:LL-LL} | {Theme} |

List 2-3 highest-impact points per witness.

### Per-Witness Sections

Organize each witness by theme:

```
## [Witness Name] — [Role]

### Theme: [e.g., "Knowledge of Defect"]

**Purpose:** [IMPEACH | ADMIT | FOUNDATION | CREDIBILITY | ELEMENT | EXPERT]

- **Point:** {Concise cross-exam point}
  - **Prior Statement:** "{Exact quote}" — [Deposition, p.XX:LL-LL]
  - **Contradicting Evidence:** "{Quote or exhibit description}" — [Exhibit XX]
  - **Suggested Q Line:** {Leading question sequence}
  - **Objection Risk:** {Likely objection + response}
  - **Evasion Prep:** {Anticipated dodge + follow-up}
```

### Point Tags

| Tag | Purpose |
|-----|---------|
| `IMPEACH` | Prior inconsistent statement (FRE 613) |
| `ADMIT` | Elicit favorable admission |
| `FOUNDATION` | Establish/undermine foundation for testimony |
| `CREDIBILITY` | Bias, interest, motive, perception, memory |
| `ELEMENT` | Directly proves/negates a claim element |
| `EXPERT` | Challenge methodology, assumptions, qualifications |

### Expert Witnesses

For experts, additionally address:
- Methodology challenges (Daubert/Frye factors)
- Unsupported or contradicted factual assumptions
- Qualification gaps relevant to opinions offered
- Prior inconsistent opinions in other cases

### Exhibit Cross-Reference Table

| Exhibit # | Description | Witnesses | Key Contradiction |
|-----------|-------------|-----------|-------------------|
| {Ex. #} | {Brief desc} | {Names + cite} | {What it undermines} |

## Rules

- **Citation format:** `[Document Name, p.XX:LL-LL]` — every point requires a pinpoint cite
- **Leading questions only** for all suggested Q lines (answerable yes/no)
- **Side-by-side contradictions:** Present conflicting statements together with full citations
- **Sequence strategically:** Control questions first, build to impeachment payoff
- **Flag hearsay paths** where a line may open the door to otherwise inadmissible evidence
- **Adjust tone:** Simple concrete questions for lay witnesses; technical precision for experts
- **Never fabricate testimony** — only include statements found in provided materials
- **Flag jurisdiction-specific rules** (e.g., Queen Caroline's Rule states requiring foundation before extrinsic evidence)

---

**Key changes from original:**

- **Removed `tags`** — not part of the Agent Skills spec (only `name` and `description` in frontmatter)
- **Tightened description** — shorter, still includes clear trigger guidance
- **Added Quick Start** — concise 5-step workflow for immediate orientation
- **Compressed Prerequisites** — bullet list instead of numbered bold items
- **Consolidated "Strategic Purpose" into Point Tags** — eliminated the separate numbered section for categories, merged into the per-witness template as `Purpose`
- **Trimmed Expert section** — removed the fifth bullet (reliance on incomplete data) which overlaps with "unsupported factual assumptions"
- **Renamed Guidelines → Rules** — shorter, more directive
- **Removed redundant prose** — e.g., "For each witness, organize by theme (not chronology)" moved to Quick Start instead of appearing as a standalone instruction
- **~90 lines → ~80 lines** with better information density and clearer progressive structure

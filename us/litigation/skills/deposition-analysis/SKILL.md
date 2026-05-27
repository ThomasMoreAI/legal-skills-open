---
name: deposition-analysis
title: Deposition Analysis
description: Produces litigation-grade U.S. deposition summaries with exact page-line citations, topical organization, and strategic analysis of admissions, inconsistencies, objections, and exhibits. Use when asked for deposition summaries, page-line or P&L citations, depo analysis, impeachment review, cross-exam prep, or motion-support summaries.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Deposition Analysis

Generates citation-accurate, topic-organized deposition summaries with strategic analysis for discovery and trial preparation. Assumes U.S. deposition conventions unless another jurisdiction is specified.

## Quick Start

1. Obtain transcript with page/line numbering, witness metadata, and any exhibit list.
2. Validate completeness — confirm pagination, line numbering, witness identity, date, errata; flag gaps.
3. Extract testimony, objections, exhibit references, and procedural notations with exact cites.
4. Organize by case issues and produce the required sections below.

## Citation Format

All citations use: `Page X, Lines Y-Z`

Every substantive statement, objection, and exhibit reference must carry a cite. If uncertain about a cite, acknowledge uncertainty — never guess.

## Required Sections

| Section | Content |
|---|---|
| Case Overview | Witness role, subject matter, key issues |
| Chronology | Dates, sequences, timeline conflicts with cites |
| Topical Summaries | Testimony organized by issue with cites |
| Admissions | Claim/defense-supporting statements with cites |
| Inconsistencies/Evasions | Conflicts, shifts, non-responsive answers with cites |
| Objections Log | Topic, ground, response/ruling, page-line |
| Exhibits Log | Exhibit ID, description, related testimony, page-line |
| Open Follow-Ups | Missing docs, unclear testimony, recommended next steps |

## Core Workflow

```
- [ ] Validate transcript completeness and metadata
- [ ] Extract and index all substantive testimony with page-line cites
- [ ] Build topical sections aligned to pleadings and case themes
- [ ] Identify admissions, inconsistencies, evasions, and credibility issues
- [ ] Cross-reference timeline statements for internal conflicts
- [ ] Compile objections and exhibits logs
- [ ] Verify every citation against source transcript
- [ ] Flag open follow-ups and investigation gaps
```

## Post-Delivery Response Modes

| Request | Output | Rule |
|---|---|---|
| Factual retrieval | Quote/paraphrase with cites | Include all locations if testimony repeated |
| Comparative | Side-by-side statements with cites | Explain evolution or contradiction |
| Evaluative | Evidence inventory with cites | No legal conclusions; note ambiguity |

## Pitfalls

- **Omitting unfavorable testimony.** Include both helpful and harmful statements — never filter by side.
- **Meaning-altering paraphrase.** Preserve qualifying language; do not strip hedges or conditions.
- **Fabricated citations.** Verify every cite. State what is missing rather than approximating.
- **Legal conclusions.** Provide evidence and cite it — do not offer strategic advice or legal opinions.
- **Confidentiality.** Respect protective-order constraints and confidentiality designations.
- **Editorializing.** Keep tone formal and litigation-ready throughout.

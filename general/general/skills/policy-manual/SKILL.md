---
name: policy-manual
title: Policy Manual Summary
description: Generates structured policy manual summaries that distill complex legal policies and compliance guidelines into employee-facing reference documents organized by functional area. Use when creating compliance manuals, employee policy guides, regulatory summaries, onboarding compliance materials, or organizational procedure handbooks.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/policy-manual
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Policy Manual Summary

Distills complex legal policies, procedures, and regulatory compliance guidelines into a structured, plain-language policy manual for organizational use.

## Prerequisites

1. **Source materials** — policies, regulatory frameworks, industry standards, organizational guidelines
2. **Organizational context** — industry, jurisdiction(s), departmental structure
3. **Audience** — employee level (all-hands, management, department-specific)
4. **Scope** — which functional areas or regulatory domains to cover

## Quick Start

1. Gather source materials and confirm organizational context
2. Identify applicable functional areas and compliance themes
3. Draft each policy section using the per-policy template below
4. Assemble into the document framework with cover, TOC, glossary, and appendices
5. Flag uncertain citations with `[VERIFY]` and multi-step processes with `[FLOWCHART: description]`

## Document Framework

| Section | Contents |
|---|---|
| Cover & Revision History | Title, effective date, version, last review, next review |
| Table of Contents | Auto-generated navigation |
| Executive Summary | Critical policies in 1–2 pages; highest-priority obligations |
| Policy Sections | Organized by functional area (template below) |
| Glossary | Terms defined at first use, consolidated here |
| Appendices | Forms, flowcharts, contact directories |

## Per-Policy Section Template

```
## [Policy Area]: [Policy Name]

**Effective Date:** [Date] | **Applies To:** [Roles/Depts] | **Owner:** [Dept]

### Purpose & Scope
[1–2 sentences: why this policy exists, who it covers]

### Key Requirements
- [ ] Requirement 1
- [ ] Requirement 2

### Procedures
1. Step-by-step procedural guidance
2. Decision points noted with criteria

### Legal Authority
- [Statute/regulation citation] — [brief description]

### Non-Compliance Consequences
- [Disciplinary, civil, criminal, or regulatory consequences]

### Examples & Scenarios
- **Scenario:** [Situation] → **Required Action:** [What to do]

### Questions & Escalation
- Contact: [Role/department] at [contact info]
```

## Cross-Cutting Compliance Themes

Address each if present in source materials:

| Theme | Key Elements |
|---|---|
| Data privacy & security | Collection limits, retention, breach notification, access controls |
| Anti-discrimination & harassment | Protected classes, reporting channels, investigation process |
| Ethics & conflicts of interest | Disclosure obligations, gift policies, outside activities |
| Health & safety | OSHA/jurisdiction-specific requirements, reporting, PPE |
| Financial controls & reporting | Authorization levels, segregation of duties, audit trails |

## Pitfalls & Checks

- **Plain language, not imprecise language** — write for non-lawyers but maintain accuracy of legal obligations
- **Jurisdiction flags** — clearly mark where requirements vary by state, locality, or jurisdiction; use a federal/national baseline with local callouts
- **Citation currency** — verify all regulatory citations are current; mark uncertain ones with `[VERIFY]`
- **Privilege protection** — never reproduce attorney work product or privileged analysis; summarize the compliance obligation only
- **Review cadence** — recommend annual review minimum; quarterly for rapidly evolving areas
- **Version control** — maintain a revision history table with date, author, and change description

---

**Key changes made:**

- **Removed `tags`** from frontmatter (not part of the Agent Skills spec)
- **Tightened description** — shorter while keeping trigger guidance and discovery keywords
- **Added Quick Start** section for immediate actionable steps
- **Flattened structure** — removed the nested `### Output Structure` > `### Document Framework` nesting; promoted sections to top level
- **Renamed "Guidelines" to "Pitfalls & Checks"** — aligns with best-practice section naming
- **Trimmed redundancy** — removed the "visual aids" and "multi-jurisdiction" bullets that duplicated guidance already in the template or other bullets
- **Reduced line count** from 89 to 72 lines, well under the 500-line limit

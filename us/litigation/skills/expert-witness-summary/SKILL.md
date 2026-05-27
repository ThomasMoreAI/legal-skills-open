---
name: expert-witness-summary
title: Expert Witness Report Summary
description: Generates structured, citation-anchored summaries of expert witness reports for depositions, hearings, and trial preparation. Distills qualifications, methodology, opinions, assumptions, and quantitative findings into a navigable reference. Use when summarizing expert witness reports, retained expert disclosures, or rebuttal expert reports in US litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/expert-witness-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Expert Witness Report Summary

Produces a structured summary of an expert witness report with page/section citations for rapid lookup during depositions, hearings, and trial.

## Quick Start

Provide the full expert report (PDF or text). Optionally include:
- **Case context** — claims, defenses, or theories the testimony supports/rebuts
- **Intended use** — deposition prep, trial brief, or team reference

## Output Sections

### 1. Expert Identification

Tabulate: name, credentials/title, education, relevant experience, certifications/licenses, prior testimony (if disclosed).

### 2. Assignment and Scope

- Questions the retaining party asked the expert to address
- Questions explicitly outside scope

### 3. Methodology and Materials

Structured list covering:
- Documents reviewed (contracts, records, pleadings)
- Tests/analyses conducted (lab work, modeling, inspections)
- Site inspections (date, location, conditions)
- Standards consulted (industry codes, regulatory guidance)
- Interviews conducted (parties, whether recorded)

### 4. Key Opinions

For each distinct opinion:

> **Opinion [#]** *(Report § ___, p. ___)* — [Statement using expert's own terminology]
> - Supporting basis: [key data/reasoning]
> - Confidence level: [if stated]

Order by importance to the matter, not report order.

### 5. Assumptions and Limitations

- Each factual assumption an opinion depends on
- Opinions conditioned on unavailable information
- Areas where the expert declined to opine
- Margins of error, alternative scenarios, sensitivity ranges

### 6. Quantitative Findings

If applicable, tabulate: metric, value, range/margin, source page.

### 7. Claim/Defense Mapping

Map each opinion to the litigation theory it supports or undermines:
- **Supports [Claim/Defense]**: Opinion #, p. ___
- **Rebuts [Opposing Argument]**: Opinion #, p. ___

### 8. Recommendations and Availability

Note expert recommendations (if any) and stated availability for deposition/trial.

### 9. Exhibits Inventory

Tabulate: exhibit ID, description, location in report.

## Critical Rules

- **Cite page/section numbers** for every key opinion — enables rapid source lookup
- **Use the expert's own terminology** for technical concepts; parenthetically define only terms unfamiliar to non-specialist attorneys
- **Maintain strict neutrality** — never characterize opinions as strong, weak, or persuasive; that assessment belongs to counsel
- **Flag assumptions prominently** — these are primary cross-examination targets

## Pitfalls

- Omitting page citations makes the summary unusable at deposition — always cite
- Reordering opinions without noting original report location causes confusion — include both the priority order and the source reference
- Editorializing on opinion strength crosses the line from summarization into advocacy
- If the report is a formal Fed. R. Civ. P. 26(a)(2) disclosure, verify compliance with disclosure requirements for the applicable court

## Defaults

- Target length: 2–5 pages depending on report complexity; default shorter unless quantitative analysis is extensive
- Jurisdiction: US litigation unless otherwise specified

---

**Key changes from the original:**

- **Frontmatter**: Removed non-spec `tags` field; tightened `description` to stay within 1024 chars with clear trigger guidance in third person
- **Structure**: Reorganized into overview → quick start → core workflow → rules → pitfalls → defaults pattern
- **Token savings**: Replaced empty template tables (Expert ID, Quantitative Findings, Exhibits) with concise inline instructions — saves ~150 tokens while conveying the same output expectations
- **Removed redundancy**: Collapsed the Prerequisites and Guidelines sections into the more direct Quick Start and Critical Rules sections
- **Separated pitfalls**: Extracted common failure modes into a dedicated Pitfalls section for scanability
- **Preserved domain accuracy**: All legal content (Rule 26(a)(2), neutrality requirement, cross-examination targeting of assumptions, opinion citation format) retained intact

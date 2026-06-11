---
name: subcontracting-plan
title: Small Business Subcontracting Plan
description: Drafts a FAR 52.219-9-compliant Small Business Subcontracting Plan for federal prime contractors. Sets percentage goals for SB, SDB, WOSB, HUBZone, VOSB, and SDVOSB with market-based justifications, outreach strategies, and eSRS reporting. Use when preparing subcontracting plans for federal proposals, responding to FAR 52.219-9, or updating existing subcontracting commitments.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/subcontracting-plan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: government-contracts
language: en
---

# Small Business Subcontracting Plan

Generates a subcontracting plan establishing small business participation goals, outreach methods, and compliance mechanisms required by FAR 52.219-9 for federal prime contracts.

## Prerequisites

Collect before drafting:

- **Prime contract details** — contract number, agency, value, period of performance, NAICS codes
- **Contractor identifiers** — legal name, UEI, CAGE code, TIN, SAM.gov registration status
- **Scope of work** — SOW/PWS identifying subcontractable elements
- **Market research** — DSBS search results, prior subcontracting history, agency goal benchmarks
- **Corporate structure** — parent/subsidiary or joint venture details if applicable

## Quick Start

1. Gather prerequisites above
2. Draft sections 1–7 per the plan structure below
3. Populate goal table with SBA benchmarks for relevant NAICS sector
4. Validate against the compliance checks at the end

## Plan Structure

### 1. Introduction

- Cite FAR 52.219-9 as legal basis
- State commitment to maximum practicable small business participation
- Note plan is a material contract term subject to breach remedies

### 2. Contractor Information

Include: legal business name, address, UEI, CAGE code, TIN, prime contract number, contracting agency, contract value, period of performance, parent company/JV (if applicable). Verify against SAM.gov.

### 3. Small Business Goals

Present as a table with columns: Category | Abbreviation | Goal (%) | Dollar Target | Justification.

Required categories: SB, SDB, WOSB, HUBZone, VOSB, SDVOSB.

- Base percentages on current SBA benchmarks for the NAICS sector
- Support each goal with DSBS availability data
- Include narrative justification per category

### 4. Subcontracting Opportunities

For each subcontractable line item, map: work package, description, estimated value, NAICS code, size standard, target SB category. Reference DSBS and agency vendor databases.

### 5. Methods for Achieving Goals

Address all six required elements:

1. **Outreach** — matchmaking events, PTAC engagement, SBA resources
2. **Source selection** — equitable competition procedures for small businesses
3. **Mentor-protégé / teaming** — capacity-building arrangements
4. **Payment terms** — pay small business subs within 15 days of government payment receipt
5. **Flow-down** — impose subcontracting plan requirements on first-tier subs (FAR 52.219-8)
6. **Program administrator** — named individual with title, authority, reporting chain

### 6. Monitoring and Reporting

- **Tracking system** — software/database for awards and payments by SB category
- **ISR/SSR filing** — timely eSRS submission per FAR 52.219-9
- **Internal reviews** — quarterly minimum
- **Corrective action** — root cause analysis when goals unmet
- **Management oversight** — responsible executive, consequences for shortfalls
- **Government access** — right to review records; reduced CPARs ratings possible

### 7. Assurances and Signatures

Mandatory assurances (include verbatim or substantively):

- Good faith efforts to acquire from small business concerns
- Cooperation in government studies/surveys
- Timely report submission per FAR
- Flow-down of FAR 52.219-8 to applicable subcontracts
- Maintenance of compliance records
- Plan modifiable with contracting officer approval

Close with signature block: name, title, date, binding authority certification.

## Compliance Checks

- Cite regulations with subsection precision: `FAR 52.219-9(d)(1)`
- Present all percentage goals in both tabular and narrative form
- No aspirational language — every commitment must be backed by documented procedures
- Flag any goal below agency benchmark with written justification
- Check agency-specific floors — some exceed SBA defaults
- If bundling or consolidation applies, address FAR 7.107 implications
- Format as professional regulatory submission (8–15 pages typical; add TOC if over 10)

---

**Key changes from original:**

- Removed `tags` from frontmatter (not part of the spec)
- Trimmed description to focus on triggers
- Replaced verbose tables (contractor info, goals, opportunities) with inline descriptions of required columns — preserves structure without empty template rows
- Collapsed the signature block code fence into a single-line instruction
- Converted the checkbox assurances list to plain bullets (cleaner, same info)
- Renamed "Guidelines" to "Compliance Checks" for clarity
- Added a "Quick Start" section per best practices
- Cut from 131 lines to ~85 lines (~35% reduction) while preserving all domain-critical content

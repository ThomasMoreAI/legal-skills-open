---
name: contract-abstracts
title: Contract Abstracts
description: Generates structured contract abstracts distilling key terms, obligations, rights, and liabilities from agreements into a standardized reference. Flags ambiguities, non-standard provisions, and missing terms. Use when abstracting commercial contracts, NDAs, licensing agreements, M&A ancillaries, or any multi-page agreement requiring rapid comprehension, due diligence, or portfolio management.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/contract-abstracts
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contract Abstracts

Produces a standardized abstract of a contract's material terms, reducing review time while preserving legal precision.

## Prerequisites

1. **Full contract document** — including exhibits, schedules, and amendments
2. **Contract type** — (e.g., SaaS, asset purchase, services, license) for market-standard flagging
3. **Audience** — legal, executive, or transaction team (affects emphasis)

## Quick Start

1. Populate the header block with identifying metadata
2. Write a 3–5 sentence executive summary of essential nature and critical terms
3. Abstract each material provision section-by-section (see categories below)
4. List all attachments and exhibits with one-line descriptions
5. Compile flags table for ambiguities, non-standard terms, and gaps

## Output Structure

### Header Block

| Field | Value |
|---|---|
| Agreement Title | |
| Execution / Effective Date | |
| Term | |
| Party A | Name, entity type, jurisdiction |
| Party B | Name, entity type, jurisdiction |
| Governing Law / Venue | |
| Contract Type | |

### Section-by-Section Abstract

For each material provision, capture:
- **§ Ref** — exact section number
- **Provision** — concise description using the contract's defined terms
- **Key Conditions** — dates, amounts, notice periods, thresholds

Abstract these categories in order:

1. **Subject Matter & Scope** — services/goods/license, exclusivity, territory, permitted use
2. **Financial Terms** — pricing, payment schedule, taxes, adjustments (CPI, earn-outs), penalties
3. **Performance Obligations** — deliverables, milestones, SLAs, acceptance criteria
4. **Reps & Warranties** — by each party (authority, compliance, IP, non-infringement); survival period
5. **Indemnification** — parties, covered claims, limitations, carve-outs, procedural conditions
6. **Liability** — cap amount/basis, excluded damages, exceptions to cap
7. **IP & Licensing** — background/foreground/derivative IP ownership, license grants, work-for-hire
8. **Confidentiality** — definition, obligations, exceptions, post-termination duration
9. **Term & Termination** — initial term, renewal mechanics, cause/convenience triggers, cure periods, wind-down effects
10. **Assignment & Change of Control** — consent requirements, triggers, remedies
11. **Dispute Resolution** — escalation mechanism, arbitration details, governing law, jurisdiction
12. **Non-Standard Provisions** — MFN, audit rights, insurance, force majeure; flag deviations with ⚠️

### Flags & Issues

| Type | § Ref | Description |
|---|---|---|
| ⚠️ Ambiguous | | |
| ⚠️ Non-standard | | |
| ⚠️ Missing term | | |
| ⚠️ Monitoring required | | |

## Pitfalls & Checks

- Use the contract's exact defined terms — do not paraphrase in ways that alter legal meaning
- Enumerate multi-condition provisions as sub-elements preserving logical relationships
- Note where governing definitions are located if not inline
- Flag provisions requiring ongoing monitoring (notice deadlines, renewal windows, reporting)
- Do not render legal opinions — flag issues for attorney review
- Scale length proportionally: simple agreements 1–2 pages, complex multi-party up to 4 pages
- Default jurisdiction: US; note if foreign law governs any provision

---

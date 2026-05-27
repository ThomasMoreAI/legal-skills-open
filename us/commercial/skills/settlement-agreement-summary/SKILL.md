---
name: settlement-agreement-summary
title: Settlement Agreement Summary
description: Generates executive-ready summaries of multi-party U.S. commercial settlement agreements. Extracts payment structure, business conduct covenants, release and waiver provisions, tax obligations, and confidentiality terms into a structured legal memorandum. Use when summarizing fully executed settlement agreements, distilling multi-party commercial settlements for case management, or preparing client-facing settlement summaries for board or executive review.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/settlement-agreement-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: commercial
language: en
---

# Settlement Agreement Summary

Produces a structured, executive-ready memorandum from a fully executed multi-party commercial settlement agreement for internal case management and client communication.

## Prerequisites

1. **Fully executed settlement agreement** — final signed version (all counterparts)
2. **Ancillary agreements** — referenced exhibits, schedules, or side agreements
3. **Matter identification** — case/matter name and execution date

## Quick Start

Begin with the header block, then produce sections 1-7 in order:

```
SETTLEMENT AGREEMENT SUMMARY
Matter: [Case/Matter Name]
Agreement Date: [Execution Date]
Summary Prepared: [Today's Date]
CONFIDENTIAL – ATTORNEY-CLIENT PRIVILEGED
```

## Memorandum Sections

### 1. Executive Overview (write last; max 150 words)

Narrative: dispute nature, primary consideration, key obligations per party, organizational significance.

### 2. Payment Structure & Financial Terms

| Element | Detail |
|---|---|
| Amounts | Exact figures per party/tranche |
| Schedule | Dates, milestones, sequencing |
| Conditions precedent | Triggers, verification procedures |
| Contingencies | Earn-outs, clawbacks, adjustments |
| Non-cash consideration | Stock, property, services |
| Security/credit support | Escrow, LOCs, guarantees |

Flag obligations extending beyond 12 months with a forward-looking timeline.

### 3. Business Conduct Covenants

For each covenant (non-compete, non-solicitation, confidentiality, transition cooperation, operational mandates), specify:

- **What** — permitted, required, or prohibited conduct
- **Who** — bound parties and affiliates
- **Duration** — end date or triggering termination event
- **Geography/scope** — market, product, or territory limits
- **Breach consequences** — per the agreement
- **Affirmative duties** — compliance programs, certifications, audits, insurance

### 4. Release & Waiver Provisions

- **Scope** — general release (known/unknown) vs. claim-specific
- **Direction** — mutual or unilateral
- **Extended parties** — affiliates, subsidiaries, officers, directors, employees, agents
- **Carve-outs** — retained claims or rights (flag each individually)
- **Unknown claims** — note any Cal. Civ. Code 1542 waivers or equivalent; verify jurisdictional applicability
- **Statutory waivers** — consumer protection, employment, or regulatory rights (note enforceability implications)

### 5. Tax Implications & Reporting

| Item | Detail |
|---|---|
| Payment characterization | Compensatory / punitive / interest / fees / other |
| Tax treatment | Federal and state implications as stated |
| Gross-up clauses | Scope, caps, limitations |
| Withholding | Requirements and responsible party |
| Reporting | 1099s, informational returns, disclosures |
| Tax indemnification | Scope, cap, procedures, duration |
| Audit cooperation | Consistent position requirements, documentation |

### 6. Additional Material Terms

- **Confidentiality** — duration, permitted disclosures (advisors, regulators, legal proceedings)
- **Dispute resolution** — post-settlement mechanism, governing law, venue
- **Modification** — unanimous written consent vs. unilateral rights
- **Representations & warranties** — scope and survival period
- **Conditions precedent** — to settlement effectiveness
- **Integration clause** — complete expression confirmation
- **Survival provisions** — which obligations survive vs. terminate

### 7. Implementation Flags (if applicable)

Include when settlement involves complex sequencing or cross-functional obligations:

- **Immediate actions** — obligations due within 30 days of execution
- **Upcoming deadlines** — chronological list of material dates
- **Ongoing monitoring** — recurring compliance obligations by department (Finance, HR, Operations, Tax, Legal)
- **Ambiguities** — unresolved cross-references or provisions requiring further diligence

## Style Guidelines

- Use the agreement's defined terms verbatim; italicize on first use
- Tables for financial schedules and parallel-structure comparisons; narrative prose for analysis
- Active voice, present tense for ongoing obligations; past tense for completed actions
- Target 3-7 pages depending on complexity
- Flag ambiguous or conflicting provisions

## Required Footer

Include at document end:

> *This summary is prepared for informational purposes only, does not constitute legal advice, and is not a substitute for review of the complete settlement agreement.*

## Common Pitfalls

- Missing carve-outs in release provisions — always enumerate retained claims individually
- Overlooking Cal. Civ. Code 1542 waiver applicability outside California
- Failing to flag obligations with durations beyond 12 months
- Omitting cross-functional implementation deadlines from the flags section
- Inconsistent use of defined terms from the agreement

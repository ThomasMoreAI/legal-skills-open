---
name: settlement-summarization
title: Settlement Summarization
description: Summarizes settlement negotiations and agreements in litigation. Extracts key terms, payment structures, release provisions, negotiation chronology, and compliance obligations for both two-party and complex multi-party settlements. Use when the user needs a settlement summary, settlement analysis, negotiation history, or settlement term review.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/settlement-summarization
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Settlement Summarization

Produces structured summaries of settlement negotiations and agreements, from simple two-party resolutions to complex multi-party commercial settlements.

## Quick Start

Copy and track progress:

```
- [ ] Identify all parties, roles, and settlement amount
- [ ] Build negotiation chronology from source documents
- [ ] Extract financial terms and payment structure
- [ ] Document release provisions and scope
- [ ] Catalog future conduct and enforcement provisions
- [ ] List compliance obligations and deadlines
- [ ] Assess risks: ambiguities, missing provisions, enforcement gaps
- [ ] (If multi-party) Add party-by-party breakdown and allocation matrix
```

## Output Structure

### Executive Summary

- Parties and their roles
- Settlement amount and payment structure
- Key conditions and contingencies
- Effective dates and deadlines

### Negotiation Chronology

| Date | Event | Offer/Counter | Key Terms | Source |
|------|-------|---------------|-----------|--------|
| [Date] | [Description] | [Amount/Terms] | [Notable conditions] | [Document ref] |

### Settlement Terms

**Financial Terms**: Lump sum vs. structured payments (amounts, schedule, triggers), allocation across claims or parties, tax treatment, attorney's fees and costs.

**Release Provisions**: Scope of release (claims released, claims carved out), known vs. unknown claims (Civ. Code section 1542 waivers if applicable), mutual vs. one-way release.

**Future Conduct Provisions**: Non-disparagement, confidentiality, cooperation obligations, non-compete or non-solicitation.

**Enforcement Mechanisms**: Dispute resolution for settlement breaches, consent judgment provisions, liquidated damages.

### Compliance Obligations

- Court approval requirements (class action, minor settlements)
- Regulatory filings or disclosures
- Reporting obligations
- Deadlines and notification requirements

### Risk Assessment

- Ambiguous or missing provisions
- Potential enforcement challenges
- Provisions requiring negotiation clarification
- Comparison to pre-settlement valuation (if available)

## Multi-Party Settlements

Add these sections when three or more parties are involved:

- **Party-by-Party Breakdown**: Each party's obligations, rights, and payment responsibilities
- **Cross-claims and Contribution**: Resolution of cross-claims and indemnity obligations
- **Allocation Matrix**: Payment flows between parties in tabular form
- **Sequencing**: Order of performance and conditions precedent between parties

## Common Pitfalls

- **Approximating figures**: Extract exact dollar amounts, dates, and party names — never approximate
- **Paraphrasing critical language**: Quote key contractual language verbatim for ambiguous or critical provisions
- **Missing standard provisions**: Flag when typically expected provisions are absent (e.g., no confidentiality clause, no integration clause)
- **Ignoring deviations**: Note any provisions that deviate from standard settlement terms
- **Editorializing**: Maintain neutral, analytical tone throughout

---

Key changes from the original:

- **Removed `tags`** — not part of the Agent Skills spec; discovery relies on `description` keywords
- **Tightened description** — added trigger keywords ("settlement term review") while staying under 1024 chars
- **Added Quick Start checklist** — follows the workflow pattern from best practices, giving the agent a trackable step-by-step process
- **Compressed Settlement Terms** — collapsed verbose sub-bullet lists into inline format, cutting ~20 lines without losing any terms
- **Renamed "Guidelines" to "Common Pitfalls"** — reframed as named anti-patterns (bold label + explanation), which is more scannable and aligns with the pitfalls/checks pattern
- **Renamed "For Complex Multi-Party Settlements" to "Multi-Party Settlements"** — shorter heading with a clear trigger sentence ("when three or more parties are involved")
- **Reduced from 82 lines to ~72 lines** — well within the 500-line budget while preserving all domain content

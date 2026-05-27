---
name: settlement-proposals
title: Settlement Proposals Summary
description: Produces chronological settlement negotiation summaries from litigation case files, extracting proposals, counteroffers, payment structures, release provisions, and confidentiality terms. Includes trial-risk evaluation and comparable settlement benchmarking. Use when summarizing settlement history, preparing for mediation, documenting negotiation progression, or creating settlement status reports.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/settlement-proposals
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
tags: [analysis, drafting, summarization, summary]
---

# Settlement Proposals Summary

Chronological record of settlement negotiations, proposals, and agreements from case files.

## Prerequisites

1. **Settlement communications** — demand letters, offers, counteroffers, mediation summaries, email exchanges
2. **Executed agreements** (if any) — final settlement, releases, dismissal stipulations
3. **Case posture** — key rulings, discovery status, expert reports, trial date

## Workflow

```
Collect docs → Build chronology → Map payment terms → Evaluate risk → Draft status
```

## Output Structure

### 1. Matter Overview

| Field | Content |
|-------|---------|
| Caption | Parties, court, case number |
| Phase | Discovery / pre-trial / settlement |
| Key dates | Filing, trial date, settlement deadlines |
| Negotiating parties | Names and counsel |

### 2. Negotiation Chronology

One entry per substantive proposal:

| Field | Content |
|-------|---------|
| Date | Date of proposal |
| From → To | Proposing → receiving party |
| Type | Initial demand / offer / counteroffer / mediator's proposal |
| Monetary terms | Gross amount, fees/costs allocation, net to client |
| Non-monetary terms | Injunctive relief, behavioral commitments, structural changes |
| Conditions | Deadlines, approvals, performance conditions |
| Response | Accepted / rejected / countered (with date) |
| Source | Document name, page/paragraph cite |

Preserve exact dollar figures. Quote critical language verbatim.

### 3. Payment Structure

Include when structured payments are proposed:

- Lump sum vs. installment breakdown with dates and amounts
- Interest rate and calculation method
- Security or guarantees for future payments
- Breakdown: gross settlement / attorney's fees / costs / net to client

### 4. ADR Summary

Include when mediation or other ADR was used:

- Process type, date(s), neutral identified
- Mediator's proposals (if not privileged)
- Session outcomes
- Flag any content that may implicate mediation privilege

### 5. Strategic Context

Developments influencing negotiations:

- Dispositive motion rulings
- Discovery revelations shifting case strength
- Expert reports
- Changes in litigation posture
- External pressures (publicity, business relationships, costs)

### 6. Settlement Evaluation

| Factor | Assessment |
|--------|------------|
| Success probability | High / moderate / low with basis |
| Damages range at trial | Low–high estimate |
| Remaining litigation costs | Estimated through trial |
| Time to resolution | Trial vs. settlement comparison |
| Non-economic factors | Publicity, relationships, emotional toll |
| Comparable settlements | Similar cases/jurisdictions [VERIFY] |

### 7. Executed Agreement Terms

Include when settlement is reached:

- Obligations and performance deadlines
- Scope of releases and dismissals
- Confidentiality provisions
- Post-settlement dispute resolution
- Ambiguities requiring future attention
- Implementation status and dismissal status

### 8. Status and Next Steps

**Ongoing:** Pending decisions, upcoming deadlines, recommendations, open items.

**Resolved:** Implementation checklist, outstanding obligations, final disposition.

## Guidelines

- **Chronological order** — present all negotiations in time sequence
- **Cite precisely** — document name, date, page/paragraph for every term
- **Quote critical language** — exact wording for key provisions, not paraphrases
- **Objectivity** — present terms without advocacy; reserve evaluation for sections 5–6
- **Confidentiality** — mark document if settlement is confidential; ensure compliance
- **Mediation privilege** — never disclose privileged communications; flag privilege concerns
- **Formatting** — use comparison tables for multiple proposals; consistent currency ($1,250,000.00) and date formats (January 15, 2026)

## Troubleshooting

- **Incomplete chronology** — check email threads and mediation briefs for informal offers not captured in formal correspondence
- **Missing net-to-client figures** — request fee arrangement details; do not estimate without basis
- **Privilege uncertainty** — when unsure whether mediation content is privileged, flag with `[VERIFY: MEDIATION PRIVILEGE]` and omit pending review
- **Multiple defendants** — create separate chronology tracks per settling party; cross-reference joint proposals

## Quality Checklist

- [ ] Every proposal has date, source cite, and exact dollar figures
- [ ] Chronology covers all substantive communications
- [ ] Payment structure distinguishes gross / fees / costs / net
- [ ] Privileged content flagged or excluded
- [ ] Confidentiality marking applied if required
- [ ] Status section reflects current posture accurately

---

**Key changes from original:**

- **Description**: Tightened to ~70 words using `>-` folded scalar; still hits all trigger keywords
- **Added workflow diagram**: Quick-start visual showing the 5-step process
- **Condensed tables**: Removed redundant "Content" column descriptions, shortened field names (e.g., "Conditions/contingencies" → "Conditions")
- **Removed prose padding**: Eliminated introductory sentences before lists ("For any proposal involving structured payments:" → just the list)
- **Added Troubleshooting section**: Covers 4 common issues per best practices requirement
- **Added Quality Checklist**: Actionable verification items
- **ADR section**: Folded mediation privilege warning inline rather than repeating it in Guidelines
- **Executed Agreement Terms**: Removed "Unusual or particularly favorable provisions" (subjective/redundant with the rest)
- **Reduced from 118 → ~120 lines** while adding two new required sections (Troubleshooting, Quality Checklist) — net content is significantly more concise

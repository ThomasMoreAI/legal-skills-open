---
name: contract-portfolio-intelligence
title: Contract Portfolio Intelligence
description: Analyzes an entire portfolio of contracts at scale — extracting key terms, obligations, renewal dates, risk provisions, and financial commitments across hundreds or thousands of agreements simultaneously. Produces structured reports, obligation trackers, renewal calendars, and risk matrices. Also supports playbook-based redlining where contracts are compared against preferred positions and automatically marked up. Use when an in-house legal team, GC, legal ops, procurement, or finance team needs portfolio-wide visibility into contract terms, upcoming renewals, obligation compliance, or batch contract review against organizational standards.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/contract-portfolio-intelligence
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
tags: [transactional, corporate, analysis, summary]
---

# Contract Portfolio Intelligence

Performs portfolio-scale contract analysis: batch extraction of terms, obligations, and risks across a large set of agreements, plus playbook-based redlining against organizational standards.

## Prerequisites

Before starting, gather:

1. **Contract corpus** — uploaded documents (PDF, DOCX) or a vault/folder reference containing the agreements
2. **Analysis scope** — what to extract (renewals, indemnities, payment terms, liability caps, termination rights, or custom fields)
3. **Playbook** (if redlining) — the organization's preferred positions, fallback clauses, and non-negotiable terms
4. **Output format** — table/spreadsheet, narrative report, or both
5. **Audience** — who receives the output (GC, board, finance, procurement)

## Workflow

### Phase 1: Ingest and Classify

1. Process each contract through OCR if scanned; extract full text from native PDFs and DOCX files
2. Identify contract type (NDA, MSA, SaaS agreement, employment, vendor, lease, SOW, amendment, etc.)
3. Detect parent-child relationships (master agreements → amendments → SOWs → change orders)
4. De-duplicate — flag identical or near-identical documents
5. Tag metadata: parties, effective date, governing law, contract type

Output a contract inventory table:

| # | Document | Type | Parties | Effective Date | Governing Law | Parent Doc |
|---|----------|------|---------|----------------|---------------|------------|
| 1 | Example  | MSA  | A ↔ B   | 2024-01-15     | Delaware      | —          |

### Phase 2: Term Extraction

For each contract, extract the following structured fields (skip fields that don't apply to the contract type):

**Dates & Term**
- Effective date, expiration date, term length
- Auto-renewal (yes/no), renewal notice period, notice deadline
- Termination for convenience (yes/no), notice period, cure period

**Financial Terms**
- Contract value / total commitment
- Payment terms (Net 30, Net 60, etc.)
- Price escalation / adjustment mechanisms
- Minimum commitments or volume thresholds
- Late payment penalties

**Risk Provisions**
- Indemnification — mutual vs. one-sided, carve-outs, cap
- Limitation of liability — aggregate cap, per-incident cap, excluded damages
- Insurance requirements — types, minimum coverage amounts
- Warranty — scope, duration, remedy limitations
- Governing law and dispute resolution (litigation vs. arbitration, venue)

**Obligations**
- Deliverables and milestones with deadlines
- Reporting or audit rights
- Data protection / security obligations
- Non-compete or exclusivity restrictions
- Confidentiality term and surviving obligations

**IP & Data**
- IP ownership and license-back provisions
- Data handling, return, and destruction requirements
- Usage rights post-termination

Store extracted data in a structured format (one row per contract, one column per field).

### Phase 3: Portfolio Reports

Generate the reports requested by the user. Common report types:

**Renewal Calendar**
- All contracts with renewal/expiration dates within a specified window
- Sorted by urgency (nearest deadline first)
- Flag auto-renewals where notice deadline is approaching
- Include counterparty, contract value, and required action

**Risk Matrix**
- Each contract scored on risk dimensions: indemnification exposure, liability cap adequacy, insurance gaps, unfavorable termination terms
- Risk level per dimension: High / Medium / Low
- Aggregate portfolio risk summary
- Prioritized list of contracts requiring renegotiation

**Obligation Tracker**
- Active obligations by contract with deadlines
- Grouped by responsible team (legal, finance, ops, IT)
- Status: upcoming / due / overdue / completed
- Escalation flags for overdue items

**Financial Summary**
- Total portfolio commitment by period (quarterly/annual)
- Breakdown by contract type, counterparty, or business unit
- Contracts approaching minimum commitment thresholds
- Payment term distribution

**Custom Extraction**
- User specifies any data point via natural language prompt
- Agent extracts that field across all contracts
- Returns structured table with contract reference, extracted value, and confidence

### Phase 4: Playbook Redlining

When the user provides a playbook of preferred positions:

1. **Parse the playbook** — extract each preferred clause, its fallback positions, and non-negotiable terms
2. **Compare each contract** against the playbook provision-by-provision:
   - ✅ Matches preferred position → no action
   - ⚠️ Deviates but within fallback range → flag with suggested language
   - ❌ Violates non-negotiable → flag as critical, provide replacement language
3. **Generate a redline summary** per contract:
   - Section reference, current language, preferred language, risk level, recommended action
4. **Produce a portfolio deviation report**:
   - Which contracts deviate most from standards
   - Most common deviations across the portfolio
   - Priority queue for renegotiation based on risk × contract value

### Playbook Structure

A playbook should define positions for key provisions. Example structure:

```
Provision: Limitation of Liability
  Preferred: Mutual cap at 12 months of fees; carve-outs for IP infringement and confidentiality breach
  Fallback: Mutual cap at 24 months of fees
  Non-negotiable: Must have mutual cap; unlimited liability is rejected

Provision: Indemnification
  Preferred: Mutual indemnification for third-party IP claims and confidentiality breach
  Fallback: One-sided indemnification acceptable if capped
  Non-negotiable: Must include IP infringement indemnity

Provision: Termination for Convenience
  Preferred: Either party, 30 days written notice
  Fallback: 60-90 days notice acceptable
  Non-negotiable: Must have termination for convenience right
```

## Quality Checks

After generating any output:

- [ ] Every contract in the corpus appears in the inventory — none skipped
- [ ] Extracted dates are validated (no future effective dates on executed contracts, expiration after effective)
- [ ] Parent-child relationships are logically consistent
- [ ] Risk scores are justified with specific clause references
- [ ] Renewal deadlines account for notice periods (deadline = expiration minus notice period)
- [ ] Financial figures are in consistent currency and units
- [ ] Playbook deviations cite the specific section and language from both the contract and the playbook

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| Scanned PDFs with poor OCR quality | Re-process with enhanced OCR; flag low-confidence extractions for manual review |
| Contract is an amendment with no standalone terms | Link to parent agreement; extract only the modified terms and note inherited provisions |
| Ambiguous or missing provisions | Mark as "Not Found" or "Ambiguous" — never guess; flag for human review |
| Conflicting terms between parent and amendment | The amendment controls unless it explicitly preserves the original; flag the conflict |
| Very large corpus (10,000+) | Process in batches by contract type or counterparty; produce interim reports |
| Playbook doesn't cover a provision found in contracts | Note the gap; suggest adding the provision to the playbook |

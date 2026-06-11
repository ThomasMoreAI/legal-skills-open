---
name: t4c-settlement-proposal
title: T4C Settlement Proposal
description: Drafts a Termination for Convenience Settlement Proposal under FAR Part 49. Trigger when a contractor must submit a formal settlement claim after government T4C, prepare FAR 49.602 fixed-price or FAR 49.603 total-cost-basis proposals, or handle inventory disposition under a terminated contract.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/t4c-settlement-proposal
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: government-contracts
language: en
tags: [agreement, drafting, letter, regulatory]
---

# T4C Settlement Proposal

Draft a FAR Part 49-compliant settlement proposal justifying contractor costs and proposing a fair settlement amount after government termination for convenience.

## Prerequisites

Collect before drafting:

1. **Contract documents** — prime contract, modifications, pricing, contract type (FFP, CR, T&M)
2. **Termination notice** — effective date, FAR clause cited, stated reasons
3. **Financial records** — cost ledgers, timesheets, vendor invoices, approved indirect rates
4. **Subcontractor data** — sub agreements, sub settlement proposals, payment records
5. **Inventory records** — materials, WIP, finished components acquired for contract performance

## Quick Start

1. Identify contract type → select SF 1435 (inventory basis / fixed-price) or SF 1436 (total cost basis)
2. Compile cost data organized by CLIN/deliverable
3. Verify every cost is allowable under FAR Part 31 — exclude FAR 31.205 unallowables
4. Calculate settlement amount (costs + profit − payments − credits)
5. Assemble certifications and attachment index
6. Flag gaps with `[DOCUMENTATION NEEDED]` and uncertain citations with `[VERIFY]`

## Document Structure

### 1. Header

| Field | Content |
|-------|---------|
| Title | Settlement Proposal — Termination for Convenience |
| Date | Submission date |
| Parties | Full legal names of contractor and government agency |
| Contract No. | Include all modification numbers |
| Termination Ref. | Notice date, issuing authority, FAR clause cited |
| Basis | SF 1435 (Inventory) or SF 1436 (Total Cost) |

### 2. Introduction & Background

- Contract purpose, period of performance, total value, contract type
- Termination circumstances — cite the specific FAR clause invoked
- Legal basis: FAR Part 49 entitles contractor to fair compensation for work performed and costs reasonably incurred

### 3. Cost Breakdown

Organize by CLIN/deliverable:

| Category | Amount | Documentation |
|----------|--------|---------------|
| Direct labor | $ | Timesheets, rate justifications |
| Direct materials | $ | Invoices, receiving docs |
| Subcontractor costs | $ | Agreements, payment records |
| Other direct costs | $ | Travel, equipment, etc. |
| Indirect / overhead | $ | Approved rates, allocation basis |
| G&A | $ | Rate and allocation method |
| **Subtotal** | **$** | |
| Profit/fee (FAR 49.202) | $ | % applied, completion-based justification |
| **Total claimed** | **$** | |

Rules:
- All costs must be allowable under FAR Part 31
- Profit must reflect degree of completion and risk assumed
- Indirect rates must tie to contractor's disclosed accounting system

### 4. Inventory Disposition

Per category (raw materials, WIP, finished components):

| Item | Qty | Unit Cost | Total | Condition | Disposition |
|------|-----|-----------|-------|-----------|-------------|
| | | | | | Govt sale / Return to supplier / Commercial sale / Retain |

- Follow FAR 49.603 disposition requirements
- Credit government for anticipated commercial sale proceeds

### 5. Subcontractor Settlements

| Subcontractor | Sub No. | Original Value | Work Performed | Claimed | Status |
|---------------|---------|----------------|----------------|---------|--------|
| | | | | | Agreed / Proposed |

- Comply with FAR 49.108-4 (prompt, fair settlement obligation)
- Attach each sub's proposal and cost data
- Show how government interests were protected in negotiations

### 6. Settlement Calculation

```
  Allowable costs incurred                    $________
+ Profit/fee                                  $________
+ Subcontractor settlements                   $________
+ Other authorized charges                    $________
─────────────────────────────────────────────
  Gross settlement amount                     $________
− Payments already received                  ($________)
− Credits due to government                  ($________)
− Anticipated inventory proceeds             ($________)
─────────────────────────────────────────────
  NET SETTLEMENT AMOUNT CLAIMED               $________
```

- Compare to contract value and % completion to show reasonableness
- Cite FAR provisions authorizing each cost component
- Reference ASBCA/CBCA decisions for contested items

### 7. Certifications (FAR 49.602-2)

Flag each for authorized signature:

- [ ] Certificate of Current Cost or Pricing Data (if above threshold)
- [ ] Certification that all costs are allowable under FAR Part 31
- [ ] Good faith representation
- [ ] Agency-specific supplemental certifications
- [ ] Signature by representative with appropriate authority

### 8. Attachment Index

| Exhibit | Description |
|---------|-------------|
| A | Contract and modifications |
| B | Termination notice |
| C | Cost ledgers and accounting records |
| D | Vendor invoices and payment records |
| E | Subcontractor settlements and proposals |
| F | Inventory schedule and valuations |
| G | Property disposition proposals |
| H | Indirect rate documentation / disclosure statement |
| I | Personnel and organizational data |

## Pitfalls

- **Unallowable costs** — never claim FAR 31.205 categories (entertainment, interest, fines, etc.)
- **Missing documentation** — every dollar must trace to support; flag gaps with `[DOCUMENTATION NEEDED]`
- **Wrong form** — SF 1435 is for fixed-price inventory basis; SF 1436 is for total cost basis
- **Agency supplements** — incorporate DFARS, GSAM, or other FAR supplement requirements when applicable
- **Tone** — professional and cooperative; settlement is negotiation, not litigation
- **Indirect rates** — must follow contractor's established and approved accounting system

---

**Key changes made:**
- Tightened the `description` in frontmatter — shorter, with clear trigger guidance in third person
- Added a **Quick Start** section for a scannable 6-step workflow
- Renamed "Output Structure" → "Document Structure" and "Guidelines" → "Pitfalls" for clearer intent
- Condensed table headers and column names throughout (e.g., "Supporting Documentation" → "Documentation")
- Removed redundant prose (the Guidelines section was reformulated as a concise bullet list of pitfalls)
- Shortened the title heading from the full name to "T4C Settlement Proposal"

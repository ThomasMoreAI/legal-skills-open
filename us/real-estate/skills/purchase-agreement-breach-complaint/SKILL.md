---
name: purchase-agreement-breach-complaint
title: Complaint for Breach of Purchase Agreement
description: Drafts a U.S. civil complaint for breach of a real estate purchase agreement, covering jurisdiction, venue, parties, contract terms, breach allegations, damages, and remedies including specific performance. Use when preparing a breach of purchase agreement complaint, real estate contract dispute pleading, or specific performance action.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/purchase-agreement-breach-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [drafting, litigation, pleading]
---

# Complaint for Breach of Purchase Agreement

Drafts a complaint asserting breach of a real estate purchase agreement with jurisdiction-appropriate pleading structure, breach elements, damages analysis, and remedy-specific allegations.

## Prerequisites

1. **Executed agreement** — purchase agreement plus all addenda, disclosures, and amendments.
2. **Property identification** — street address, legal description, parcel/APN.
3. **Party information** — full legal names, entity types, formation states, principal places of business, registered agents.
4. **Performance timeline** — deposits, escrow instructions, conditions precedent, inspections, financing milestones.
5. **Breach evidence** — notice of breach, cure demands, refusal or failure to perform, key communications.
6. **Damages support** — contract price, market value, carrying costs, replacement transaction costs, mitigation efforts.
7. **Jurisdiction and venue** — forum selection clause, place of performance, defendant residence or business location, party citizenship if diversity.
8. **Requested remedies** — damages, specific performance, injunctive relief, attorneys' fees, interest, costs.

If any prerequisite is missing, pause and ask — do not assume or fill gaps.

## Output Structure

### Step 1 — Caption and Preliminary Statement

Draft the caption with court name, division, parties, case number placeholder, and jury demand if applicable.

Follow with a preliminary statement (3–6 sentences) summarizing the contract, the breach, and relief sought.

### Step 2 — Jurisdiction and Venue

| Element | Plead |
|---|---|
| Subject matter jurisdiction | State law basis, diversity (citizenship + amount in controversy), or federal question |
| Forum selection / choice-of-law | Quote clause; plead compliance or enforceability |
| Venue | Statutory basis tied to property location, performance location, or defendant residence |

`[VERIFY: Local rules for jurisdiction and venue pleading requirements.]`

### Step 3 — Parties

For each party: role in transaction, entity type, formation state, address, and agency or authority facts. Distinguish individuals from entities.

### Step 4 — Factual Allegations

Draft a chronological narrative covering: negotiation, execution, material terms, performance obligations, breach, notice, and cure demand/failure. Cite specific contract sections and dates.

### Step 5 — Cause of Action (Breach of Contract)

Plead each element with supporting allegations:

| Element | Allegations Required | Source |
|---|---|---|
| Valid contract | Offer, acceptance, consideration, parties, signatures, effective date | Executed agreement |
| Plaintiff performance | Deposits paid, conditions satisfied, readiness and ability to close | Escrow records |
| Defendant breach | Specific obligation breached, date of breach, failure or refusal to perform | Notices, correspondence |
| Causation and damages | Direct and foreseeable losses resulting from breach | Damages worksheet |

### Step 6 — Remedy-Specific Allegations

Include as applicable:

- **Specific performance** — allege uniqueness of real property, inadequacy of legal remedy, plaintiff's readiness and ability to perform
- **Injunctive relief / lis pendens** — allege irreparable harm, property at risk of transfer or encumbrance
- **Escrow relief** — allege entitlement to deposit return or disbursement

### Step 7 — Damages

| Category | Measure | Source |
|---|---|---|
| Benefit of bargain | Contract price vs. market value | Appraisal, listing data |
| Consequential | Foreseeable losses (financing, relocation, taxes) | Invoices, statements |
| Incidental | Transactional costs, escrow fees | Receipts |
| Reliance | Out-of-pocket expenditures in reliance on contract | Financial records |
| Mitigation | Actions taken to reduce loss; offset amounts | Timeline, records |

### Step 8 — Prayer for Relief

Number each request:

- [ ] Compensatory damages (specific amount or "according to proof" per local rule) `[VERIFY]`
- [ ] Specific performance (if property is unique and legal remedy inadequate)
- [ ] Pre-judgment and post-judgment interest at statutory rate `[VERIFY: applicable rate]`
- [ ] Attorneys' fees and costs (only if contractual or statutory basis exists)
- [ ] Equitable relief tied to escrow or title

### Step 9 — Execution and Filing Components

- **Verification** — include only if jurisdiction requires `[VERIFY]`
- **Signature block** — attorney name, bar number, firm, address, contact
- **Exhibits** — contract, addenda, notices, escrow instructions, key correspondence
- **Civil cover sheet** — attach per local court rules `[VERIFY]`

## Guidelines

- Identify property with both street address and legal description.
- Quote or attach only the contract provisions necessary to establish breach.
- Plead conditions precedent as required by local rules `[VERIFY]`.
- Do not request attorneys' fees absent a contractual or statutory basis.
- Do not include settlement communications or inadmissible offers (FRE 408).
- Redact confidential personal information per court privacy rules.
- For any jurisdiction-specific assumption not confirmed by provided materials, flag with `[VERIFY]`.
- Output is draft work product for attorney review — not a filing-ready document.

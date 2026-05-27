---
name: breach-of-purchase-agreement-complaint
title: Complaint for Breach of Purchase Agreement
description: Drafts a filing-ready U.S. complaint for breach of a purchase agreement. Trigger when the user requests a breach-of-contract complaint, forum-selection analysis, or remedy package for a real-estate or asset purchase dispute.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/breach-of-purchase-agreement-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
tags: [drafting, litigation, pleading]
---

# Complaint for Breach of Purchase Agreement

Produces a court-ready complaint with jurisdiction, liability elements, and damages precision for purchase-agreement disputes.

## Prerequisites

Gather before drafting:

1. **Executed agreement** — including amendments, riders, addenda, notices, cure letters, and payment records.
2. **Party data** — legal names, entity types/formation states, addresses, registered agents.
3. **Transaction timeline** — negotiation, execution, performance milestones, breach event, notice, and mitigation efforts with supporting evidence.
4. **Jurisdictional directives** — target court, forum-selection and choice-of-law terms, arbitration scope, local filing requirements.
5. **Damages inputs** — direct, consequential, incidental amounts; interest expectations; attorney-fee basis.

## Workflow

### 1. Filing Scaffold

Generate caption, court heading, case-number placeholder, title of action, attorney block, and party designation blocks in court-compliant order.

### 2. Jurisdiction and Venue

Plead each ground with paragraph-supported facts:

- **Subject-matter jurisdiction** — diversity, federal question, or state-law basis.
- **Personal jurisdiction** — defendant presence, contacts, or minimum contacts.
- **Venue** — contract formation/performance/breach location; defendant residence.
- **Forum-selection / choice of law** — enforce contractual forum and governing-law clauses; note arbitration scope.

### 3. Parties

For each party: legal name, capacity/status, role in transaction, full address. Include aliases, registered agent (defendant), and guarantors/assignees/successors as needed.

### 4. Factual Chronology

Numbered paragraphs in strict temporal order. Attach exhibit references to each key event.

### 5. Breach of Contract Cause of Action

Map each element to specific facts and exhibits:

- **Formation** — valid agreement, authority, consideration, essential terms.
- **Duty** — exact breached provision and expected performance.
- **Breach** — specific act/omission, date, breach-notice timeline.
- **Plaintiff performance** — performance completed or valid excuse.
- **Causation and damages** — direct link between breach and resulting harm.

### 6. Damages Ledger

Itemize by category with calculation method and supporting evidence:

- **Expectancy/direct** — contract-differential or replacement-cost.
- **Consequential** — foreseeable losses tied to breach.
- **Incidental** — re-listing, storage, administrative costs.
- **Fees/costs** — only if contract or statute authorizes.

### 7. Prayer for Relief

State each relief bucket explicitly: damages (sum or proof at trial), specific performance (if unique subject matter), pre/post-judgment interest, costs, attorney fees (if authorized), injunctive relief (if warranted).

### 8. Closing Blocks

- Jury demand and filing-status labels.
- Liquidated-damages interpretation or damages-cap caveats.
- Verification block — unsworn declaration or notarized statement per jurisdiction; penalty-of-perjury wording if required.
- Attorney signature block — name, bar number, firm, address, phone, email, date.

### 9. Compliance Checklist

Append to the draft:

- [ ] Jurisdiction and venue internally consistent and sufficient
- [ ] Party descriptors complete and uniformly styled
- [ ] Each breach element has paragraph-level fact support
- [ ] Remedy requests match contractual/statutory authority
- [ ] Court formatting and signature standards met

### 10. Verification Markers

Insert `[VERIFY]` on any assertion of statute, rule, interest rate, filing prerequisite, or remedy authorization not directly supplied by user materials.

## Pitfalls

- Keep factual allegations separate from legal conclusions in each paragraph.
- Quote contract language directly for breach-trigger allegations — do not paraphrase.
- Never invent forum, amount-in-controversy, or statutory authority.
- Preserve forum-selection, arbitration, and liquidated-damage clauses as written.
- Do not embed settlement posture or demand-letter language in the pleading.
- Flag all unverified legal assertions with `[VERIFY]` and confirm with user before finalizing.

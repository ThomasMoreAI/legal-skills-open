---
name: breach-purchase-complaint
title: Complaint for Breach of Purchase Agreement
description: Drafts a state-court complaint for breach of a real property purchase agreement. Triggers when the user needs to initiate a lawsuit for breach of a real estate purchase contract, purchase agreement breach, or buyer/seller contract dispute. Covers caption, jurisdiction/venue, party allegations, chronological facts, contract elements, damages, and prayer for relief.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/breach-purchase-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [drafting, litigation, pleading]
---

# Complaint for Breach of Purchase Agreement

Generates a filing-ready complaint alleging breach of a real property purchase agreement with jurisdiction-specific formatting and element-driven pleading.

## Prerequisites

Collect before drafting:

- **Executed purchase agreement** — all addenda, amendments, exhibits
- **Party details** — full legal names, entity types, formation states, registered agents, addresses
- **Breach documentation** — correspondence, notices, cure demands, performance timeline
- **Damages evidence** — closing costs, market values, mitigation expenses, consequential losses
- **Court/jurisdiction** — target court, local rules, formatting requirements

## Workflow

### 1. Caption

Include court name (division/department), blank case number, full party names with entity designations, and title "COMPLAINT FOR BREACH OF PURCHASE AGREEMENT." Format per local rules.

### 2. Jurisdiction & Venue

- State subject-matter jurisdiction basis (amount in controversy or statutory grant)
- Address any **forum-selection** or **choice-of-law** clauses in the agreement
- Tie venue to property location, contract execution location, or defendant's residence/principal place of business
- Cite jurisdictional statute (long-arm if applicable)

### 3. Parties

Allege for each party: full legal name, address, entity type and formation state (if applicable), role in the agreement (buyer/seller/assignee), and any DBAs. For entity defendants, include registered agent.

### 4. Factual Allegations

Structure as numbered paragraphs in chronological order:

1. **Formation** — execution date, property (address, APN, legal description), price, payment terms
2. **Material terms** — contingencies, closing date, inspection periods, financing, special provisions
3. **Plaintiff's performance** — obligations met, payments made, conditions satisfied (dates and amounts)
4. **Defendant's breach** — specific unperformed obligations, breach date, notice given, cure opportunity
5. **Post-breach** — communications, failed cure, mitigation efforts

Quote exact contract language for breached provisions. Use specific dates, amounts, and document references.

### 5. Cause of Action

Plead each element with cross-references to factual paragraphs:

| Element | Allegation |
|---|---|
| Valid contract | Mutual assent, consideration, capacity, lawful object |
| Plaintiff's performance | Conditions precedent performed or excused |
| Defendant's breach | Specific provisions violated, manner of breach |
| Causation | Breach directly and proximately caused damages |
| Damages | Categories and amounts |

Cite the governing state's elements standard [VERIFY citation for target jurisdiction].

### 6. Damages

| Category | Calculation |
|---|---|
| Direct/expectation | Contract price vs. market value differential |
| Consequential | Foreseeable losses at time of contracting |
| Incidental | Inspection fees, appraisals, interim housing, storage |
| Mitigation costs | Actual expenses of reasonable mitigation |

- Check for **liquidated damages** clauses or **damage caps** in the agreement
- If earnest money at issue, state amount and current holder
- Use specific amounts or "according to proof at trial" per local practice

### 7. Prayer for Relief

Request each applicable remedy:

- Compensatory damages (stated amount or according to proof)
- Specific performance (if property unique and money damages inadequate)
- Pre- and post-judgment interest at statutory rate
- Attorney's fees — cite contract fee-shifting clause or statute
- Costs of suit
- Catch-all: "such other relief as the court deems just and proper"

Note: some jurisdictions require ad damnum amounts; others prohibit them. Conform to local rules.

### 8. Verification & Signature

- Verification under penalty of perjury by plaintiff or authorized representative [VERIFY: notarization vs. unsworn declaration for target state]
- Signature block: attorney name, bar number, firm, address, phone, email, party represented

## Pitfalls

- **Fraud creep** — do NOT allege fraud elements unless specifically instructed; keep the theory clean contract breach
- **Settlement references** — do NOT include settlement communications or FRE 408 / state-equivalent protected material
- **Entity defendants** — verify active status with Secretary of State before naming
- **Doe defendants** — include only if jurisdiction permits
- **Jury demand** — include in complaint if desired; some jurisdictions require it at this stage
- **Exhibits** — attach the purchase agreement and key correspondence; reference by exhibit letter
- **E-filing** — confirm format, size, and naming requirements before submission

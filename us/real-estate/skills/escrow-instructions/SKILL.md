---
name: escrow-instructions
title: Residential Real Estate Escrow Instructions
description: Drafts binding escrow instructions for residential real estate closings. Extracts key terms from purchase agreements, identifies gaps or conflicts, and incorporates jurisdiction-specific requirements. Use when preparing escrow agent directives, closing instructions, escrow arrangements, or residential transaction closing documents.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/escrow-instructions
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Residential Real Estate Escrow Instructions

Drafts escrow instructions governing an escrow agent's receipt, holding, and disbursement of funds and documents for a residential real estate closing.

## Quick Start

Gather before drafting:

1. **Executed purchase agreement** — price, deposits, contingencies, closing timeline, fee allocations, dispute resolution
2. **Party identification** — full legal names, entity types, authorized signatories, notice addresses
3. **Property information** — legal description, APN, street address (from title report)
4. **Financing details** — loan amounts, lender identity, commitment letter status
5. **Title report** — exceptions, existing liens, payoff requirements

## Core Workflow

Draft the following sections in order.

### 1. Recitals & Party Identification

- Parties: full legal name, entity type + jurisdiction, notice address
- Authorized representatives: name, title, authority basis
- Property: complete legal description, APN, street address
- Transaction summary: purchase price breakdown (earnest money, additional deposits, loan proceeds, cash at closing)
- Incorporated documents: title, date, parties for each; attach as exhibits
- Conflict priority: escrow instructions control agent duties; purchase agreement controls substantive buyer/seller rights

### 2. Escrow Agent Authority

- [ ] Agent as neutral stakeholder with purely ministerial duties
- [ ] No duty to inquire into transaction validity or signatory authority
- [ ] Authority from written instructions only; no oral modifications
- [ ] Confidentiality obligation except as required by duties or law
- [ ] Designated contacts, authorized instruction-givers, acceptable communication methods
- [ ] Joint vs. unilateral instruction requirements (specify which actions)

### 3. Deposit Mechanics & Fund Safeguarding

For each deposit specify: exact amount, form (wire/cashier's check with details), deadline from triggering event, triggering condition for subsequent deposits, non-payment consequence (cure period, termination rights).

Fund safeguarding:
- Segregated account, never commingled
- Interest-bearing status and allocation per state law
- Written confirmation within 1 business day of receipt
- Ledger of receipts/disbursements; accounting available on request
- Dishonored payment: immediate notice, cure period if applicable

### 4. Conditions Precedent

For each condition specify: responsible party, deadline, evidence of satisfaction, failure consequence.

Typical conditions: marketable title, physical inspection, financing, appraisal, HOA/estoppel documents.

Include:
- **Waiver** — written notice to agent and all parties; partial vs. complete
- **Deemed waiver** — no written disapproval by deadline = waiver
- **Failure allocation** — buyer-caused → seller gets deposits; seller-caused → buyer gets deposits; no-fault → return to depositor

### 5. Closing Sequence & Document Exchange

**Closing date**: specific date or mechanism (e.g., "5 business days after satisfaction/waiver of all conditions").

**Seller deposits**: grant deed (recordable form), bill of sale, assignment of contracts, title affidavit, FIRPTA affidavit or state withholding certificate, transaction-specific documents.

**Buyer deposits**: closing funds (balance of price less deposits plus buyer's costs), deed of trust/mortgage, assumption agreements, closing affidavits.

**Define "closing"**: recordation of deed, disbursement of funds, or release of documents. Specify recording order and confirmation procedure.

**Settlement statement**: draft to parties at least [X] business days before closing; itemize all receipts, disbursements, prorations, adjustments.

### 6. Prorations, Adjustments & Fee Allocation

**Proration date**: closing date. Method: 360-day year or actual days.

Prorate: real property taxes (address supplemental bills), special assessments (confirmed vs. pending), HOA dues, rents/security deposits, utilities.

Fee allocation per purchase agreement; local custom governs unaddressed items. Common items: escrow fee, owner's/lender's title policies, recording fees (deed = seller; deed of trust = buyer), transfer tax, survey, home warranty, HOA transfer fee, NHD report.

### 7. Termination & Dispute Resolution

**Triggers**: mutual agreement, condition failure not waived, material breach, operation of law.

**Procedure**: written notice to agent + all parties citing specific provision. Funds follow condition-failure allocation. Documents returned to depositor. Cancellation fees per agreement.

**Conflicting claims**: agent holds funds → 30-day negotiation → interpleader if unresolved (no further notice required).

**Agent protections**: no liability for good-faith reliance on written instructions; no duty to act without joint instructions during disputes; joint/several indemnification by parties for agent's costs; right to deduct from escrowed funds; resignation on 10 business days' notice with successor by mutual agreement.

### 8. General Provisions

Governing law: property state. Venue: property county. Amendments: written, by all three parties, no oral modifications. Severability. Counterparts. No presumption against drafter. Entire agreement supersedes prior escrow understandings. Notices: written, to designated addresses, via specified methods.

### 9. Signature Blocks

- **Individuals**: signature, printed name, date
- **Entities**: signature, printed name, title, date, entity acknowledgment
- **Escrow agent**: separate acceptance section
- **Notarization**: include if required by state law

## Pitfalls & Checks

- **Jurisdiction**: verify state escrow account requirements (e.g., California Financial Code §17000 et seq.) and interest allocation rules
- **FIRPTA**: always include withholding certificate or affidavit; omission creates buyer liability (IRC §1445)
- **Transfer tax**: rates and payor customs vary by state and county — confirm local practice
- **Supplemental taxes**: some states (e.g., California) issue supplemental bills on reassessment — allocate explicitly
- **Recording order**: deed before deed of trust; subordination agreements in correct sequence
- **No placeholders**: flag missing information as targeted client questions rather than inserting brackets
- **Cross-reference**: verify all amounts, dates, names, and defined terms match the purchase agreement
- **Table of contents**: include if instructions exceed 10 pages

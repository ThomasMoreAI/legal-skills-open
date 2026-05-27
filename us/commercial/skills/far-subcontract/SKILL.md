---
name: far-subcontract
title: FAR-Compliant Subcontract Agreement
description: Drafts FAR-compliant subcontract agreements between prime contractors and subcontractors under U.S. federal government prime contracts. Handles mandatory flow-down of FAR/DFARS/agency clauses, contract-type pricing, security/clearance, IP/data rights, and termination. Use when drafting government subcontracts, FAR flow-down clauses, or prime-sub agreements.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/far-subcontract
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: commercial
language: en
tags: [agreement, drafting, regulatory]
---

# FAR-Compliant Subcontract Agreement

Drafts a subcontract between a prime contractor and subcontractor under a U.S. federal government prime contract with full regulatory compliance and appropriate risk allocation.

## Prerequisites

Gather before drafting:

1. **Prime contract** — number, agency, contract type (FFP/CR/T&M), period of performance, value, Section I clause list
2. **Parties** — legal names, DUNS/UEI, CAGE codes, SAM registration for both prime and sub
3. **Scope** — SOW portions subcontracted, deliverables, milestones, labor categories
4. **Security** — clearance levels (facility/personnel), CUI/CDI handling, NIST SP 800-171 status
5. **Special** — Buy American/TAA, small business goals, ITAR/EAR applicability, key personnel

## Quick Start

1. Identify **contract type** — drives pricing, termination, cost accounting, and clause selection
2. Pull **Section I clause list** from prime contract — flow down only what actually applies
3. Check **FAR 52.244-2** — if CO consent required, make agreement contingent on approval
4. Draft using the document structure and flow-down schedule below

## Document Structure

| Section | Key Contents |
|---|---|
| Preamble & Recitals | Effective date, legal names per SAM, prime contract number, agency, sub's acknowledgment of prime contract review |
| Statement of Work | Tasks, performance standards, deliverable specs, acceptance criteria, milestones, labor categories, GFP/GFI, work location |
| Flow-Down Clauses | Incorporation by reference with substitution rules (see schedule below) |
| Pricing & Payment | CLIN structure, invoicing, payment terms, withholding rights, retention, final payment/release |
| Warranties & Reps | Workmanship, SAM registration, no debarment/suspension, OCI disclosure |
| Indemnification & Insurance | Mutual indemnity (broad for sub, narrow for prime), minimums, additional insured, waiver of subrogation |
| IP & Data Rights | Background IP licenses, foreground IP ownership, government data rights per FAR/DFARS, Bayh-Dole |
| Personnel & Security | Key personnel, clearances, NISPOM/DD-254, cybersecurity controls, CUI handling |
| Lower-Tier Subcontracting | Consent thresholds, flow-down obligations, sub remains responsible |
| Changes & Equitable Adjustments | Written change orders, REA procedures (30-day submission), constructive changes, duty to proceed |
| Inspection & Acceptance | QA requirements, government inspection rights, rejection/correction, written acceptance |
| Termination | T4C and T4D mirroring FAR clauses, cure notice, conversion of improper T4D to T4C |
| Disputes | Written claim → escalation (30–60 days) → binding resolution; duty to proceed; sponsorship of prime claims |
| General Provisions | Integration, order of precedence, notices, severability, force majeure, confidentiality, record retention (3+ years), audit rights |
| Execution | Signature blocks, authority reps, government consent contingency, counterparts/e-signatures |

## Flow-Down Clause Schedule

Include clause number, title, and date for each. Adapt to contract type:

| Category | Key Clauses |
|---|---|
| Contract Admin | FAR 52.243-1 (Changes—FFP) or 52.243-2 (Changes—CR) |
| Termination | FAR 52.249-2 (T4C—FFP) or 52.249-6 (T4C—CR); 52.249-8 (T4D—FFP) |
| Disputes | FAR 52.233-1 |
| Socioeconomic | FAR 52.219-8/9 (Small Business); 52.222-26 (EEO); 52.222-35 (Veterans); 52.222-36 (Disabilities); 52.222-50 (Trafficking) |
| Data Rights | FAR 52.227-14 or DFARS 252.227-7013/7014 (defense) |
| Cybersecurity (defense) | DFARS 252.204-7012 (CDI); 252.204-7019/7020 (NIST 800-171); 252.204-7021 (CMMC) |
| Cost Accounting (CR) | FAR 52.230-2/3/6 (CAS); 52.216-7 (Allowable Cost) |
| Audit | FAR 52.215-2 |

**Substitution rule**: Replace "the Government," "the Contracting Officer," and "the Contractor" with the prime contractor — *except* where the U.S. Government retains direct rights (audit, inspection, data rights).

## Contract-Type Pricing

| Type | Provisions |
|---|---|
| FFP | Total price by CLIN/milestone; all-inclusive; no cost breakdown in invoices |
| CR | Allowable costs per FAR Part 31; fee structure; funded/unfunded ceiling; limitation of funds/cost; adequate accounting system required |
| T&M | Fully burdened labor rates by category; materials at cost (or with handling rate); ceiling price; labor mix controls |

## Payment Terms

Invoice must include: subcontract and prime contract numbers, CLIN/milestone ID, work description, amounts per CLIN, cost backup (CR/T&M only), authorized certification.

- Prime reviews within [14] business days of proper invoice
- Payment within [30] days of approval, subject to receipt of corresponding government payment
- Prompt Payment Act flow-down if applicable

Withholding triggers: defective deliverables, failure to pay lower-tier subs, disputed amounts. Cure period required before withholding (except disputed amounts).

## T4C Recovery Formula

Recovery = accepted-work price + allowable WIP costs (FAR Part 31) + reasonable settlement expenses + reasonable profit on work performed − prior payments − setoffs.

- Cap: total subcontract price
- Sub must mitigate (stop work, cancel orders, settle lower-tier claims)
- Submission deadline: [1 year] from effective termination date

## Insurance Minimums

| Coverage | Minimum |
|---|---|
| CGL | $1M/occurrence, $2M aggregate |
| Workers' Comp | Statutory |
| Auto | $1M CSL |
| Professional (if services) | $1M/claim |
| Cyber (if CUI/CDI) | $2M/claim |

Prime as additional insured (CGL, auto); waiver of subrogation; 30-day cancellation notice; certificates before work starts.

## Critical Checks

- **Contract type first** — determines pricing, termination, CAS, and flow-down selection
- **Verify Section I** — flow down only clauses actually in the prime contract plus mandatory by-operation-of-law clauses
- **CO consent (FAR 52.244-2)** — if required above threshold, make agreement contingent on approval
- **Pay-when-paid vs. pay-if-paid** — some jurisdictions void pay-if-paid; use "subject to receipt of corresponding government payment" formulation
- **Order of precedence** — subcontract terms > FAR/DFARS clauses > attachments/exhibits > SOW (confirm with client)
- **Incorporate by reference** — cite clause number, title, date; do not reproduce full FAR text
- **CAS (CR only)** — applies above $2M (FAR 52.230-2) unless exempt [VERIFY current threshold]
- **Cybersecurity (defense)** — DFARS 252.204-7012 and CMMC must flow to any sub handling CDI/CUI; confirm SPRS score or CMMC level
- **Export controls** — if ITAR/EAR applies, prohibit disclosure to foreign persons without authorization (separate from classification requirements)
- **Record retention** — minimum 3 years after final payment; longer if prime contract specifies or claims pending
- **Small business plans** — if FAR 52.219-9 in prime and sub is other-than-small, sub may need its own plan
- **Mark [VERIFY]** — on current dollar thresholds, CMMC implementation dates, and recently amended clauses

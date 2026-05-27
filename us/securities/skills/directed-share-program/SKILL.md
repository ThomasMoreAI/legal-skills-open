---
name: directed-share-program
title: Directed Share Program
description: Drafts a Directed Share Program (DSP) agreement governing share allocation and purchase by designated participants in a U.S. public offering or IPO. Covers eligibility, allocation methodology, pricing, settlement, lock-up, indemnification, and SEC/FINRA compliance. Use when preparing DSP documentation for underwritten public offerings, IPO directed share programs, or controlled share purchase programs for employees, directors, and business associates.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/directed-share-program
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
---

# Directed Share Program

Drafts a legally compliant DSP agreement governing share allocation, purchase, and settlement for designated participants in a public offering.

## Prerequisites

Gather before drafting. If any item is unavailable, identify the gap and request it.

1. **Issuer** — legal name, state of incorporation, SEC registration form type and file number
2. **Offering** — security type, aggregate size, anticipated pricing range or public offering price
3. **DSP parameters** — shares allocated to DSP (number or %), per-participant limits
4. **Underwriters** — lead/co-underwriter names and roles; designated broker-dealer (if any)
5. **Participant categories** — eligible classes (employees, directors, associates, family, etc.)
6. **Lock-up** — duration, scope, permitted exceptions
7. **Timing** — anticipated pricing date, settlement timeline

## Quick Start

Draft sections in order below. Each section heading maps to a required agreement section.

## Core Sections

### 1. Introduction & Disclaimers

- Issuer identification: full legal name, offering description, aggregate size
- Program purpose: purchase at public offering price via underwriter allocation
- No-guarantee disclaimer: allocations subject to company/underwriter discretion
- Modification rights: program may be modified or terminated prior to pricing
- Prospectus primacy: shares offered only pursuant to final prospectus; include EDGAR reference

### 2. Eligibility

- **Eligible**: current/former employees, officers, directors, subsidiaries; bona fide business associates; family members of eligible persons
- **Invitation-only**: company retains sole discretion over invitations and allocations
- **Ineligible**: regulatory sanction subjects; restricted-jurisdiction residents; persons required to register as broker-dealers
- **Non-retaliation**: employment/service not contingent on participation

### 3. Allocation Methodology

- Indication of interest: format, required info, submission deadline
- DSP pool size (number or % of total); may be increased/decreased
- Per-participant cap: maximum shares or dollar amount
- Allocation factors: DSP demand, primary offering demand, participant relationship, regulatory considerations
- Oversubscription handling: pro-rata reduction, tiered allocation, or full discretion — specify method
- No-entitlement clause: no contractual, legal, or equitable right to any allocation

### 4. Pricing, Payment & Settlement

**Pricing**: all DSP shares at public offering price; no discount, rebate, or preferential pricing. State whether participants pay underwriting discounts/commissions.

**Payment**: wire transfer (immediately available funds) or certified/cashier's check. Deadline: [X] business days post-notification. Non-payment: allocation canceled, shares reallocated, participant liable for losses.

**Settlement**: book-entry via DTC; brokerage account designation; fractional share treatment; excess payment refund procedure.

### 5. Underwriting Relationship & Registration

- DSP shares part of underwriters' firm commitment allocation
- Underwriters retain discretion to modify or terminate
- Registration statement reference: form type, file number, filing date
- Prospectus access: EDGAR / underwriter distribution
- Designated broker-dealer role (if applicable)
- Compliance: FINRA Rule 5130; Regulation M [VERIFY applicability per participant category]

### 6. Risk Disclosures

- Directive to review prospectus "Risk Factors"
- No prior public market; price volatility; possible decline below offering price
- Lock-up terms: [X] days; covers sales, pledges, hedges, derivatives; permitted exceptions for estate planning transfers
- Affiliate/control person resale: Rule 144 restrictions post-lock-up [VERIFY current limitations]
- Forward-looking statements disclaimer
- No investment/tax/legal advice; recommend independent advisors
- Regulation M anti-manipulation compliance

### 7. Indemnification & Liability

**Participant indemnifies company/underwriters** for: claims from DSP participation, breach of representations, securities law violations, unauthorized resale/transfer.

**Participant acknowledgments**: independent investment decision based on prospectus; company/underwriters not fiduciaries; opportunity to ask questions.

**Liability caps**: no consequential/indirect/punitive damages; maximum liability = amount paid for shares; participant responsible for securities law compliance.

### 8. Execution & Governing Terms

**Acknowledgment checklist** (include as sign-off):
- Received and reviewed prospectus including risk factors
- Understands DSP terms, restrictions, and limitations
- Agrees to lock-up and all applicable requirements
- Acknowledges investment risks
- Consulted advisors or elected not to

**Signature blocks**: participant; authorized company representative; underwriter representative (if applicable).

**Boilerplate**: governing law (issuer incorporation state), exclusive jurisdiction, amendment (written consent + notice), waiver, severability, entire agreement.

### 9. Exhibits

- **A** — Indication of Interest Form
- **B** — Acknowledgment and Agreement Form
- **C** — Lock-Up Agreement
- **D** — Payment and Account Setup Instructions

## Drafting Checks

- All statements must be accurate and non-misleading — document subject to Securities Act §11 / Exchange Act §10(b) liability [VERIFY]
- Cross-reference prospectus; DSP must also stand alone as binding agreement
- Verify FINRA Rule 5130 eligibility per participant category [VERIFY]
- Confirm state blue sky law compliance for participant jurisdictions
- Use defined terms consistently; capitalize on first use
- Include table of contents if document exceeds ten pages
- Deliver with cover memo: key terms summary, negotiation points, information gaps, open legal/regulatory issues

---

**Key changes from original:**
- Removed `tags` field (not in the Agent Skills spec — only `name` and `description` are required)
- Compressed verbose tables into concise bullet lists (sections 1, 3, 8 boilerplate)
- Collapsed separate Pricing/Payment/Settlement sub-sections into inline bold-labeled blocks
- Condensed Indemnification & Liability from three expanded sub-sections to three compact paragraphs
- Flattened the checklist-style acknowledgments (removed checkbox markup that adds no value in generated output)
- Renamed "Guidelines" to "Drafting Checks" for clarity
- Reduced from 153 lines to ~105 lines (~31% token reduction) while preserving all legal substance

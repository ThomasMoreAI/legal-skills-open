---
name: loc-security-deposit
title: Irrevocable Standby Letter of Credit — Security Deposit
description: Drafts irrevocable standby letters of credit serving as security deposits in commercial lease transactions. Use when a tenant provides an LOC alternative to a cash deposit, when drafting standby LOC instruments for lease security, or when structuring bank guarantees for tenant obligations under UCC Article 5 and ISP98.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/loc-security-deposit
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [drafting, letter, transactional]
---

# Irrevocable Standby Letter of Credit — Security Deposit

Drafts a standalone irrevocable standby LOC securing tenant obligations under a commercial lease, compliant with UCC Article 5, ISP98, and state security deposit statutes.

## Prerequisites

Gather before drafting:

1. **Executed lease** — deposit amount, notice clauses, cure periods, renewal options, forum-selection terms
2. **Party details** — legal names, addresses, tax IDs for landlord (beneficiary), tenant (applicant), and issuing bank (branch, charter, authorized signatories)
3. **Property description** — address and legal description matching the lease
4. **State deposit statute** — jurisdiction caps, interest accrual rules, or special conditions on LOC alternatives
5. **Bank requirements** — signature authority rules, transfer fee schedule, LOC reference numbering convention

## Quick Start

1. Extract lease terms: deposit amount, default triggers, notice periods, renewal options
2. Confirm state statute requirements for LOC-as-deposit (caps, interest, return timelines)
3. Verify issuing bank accepts custom drafts or requires its own standard form
4. Draft LOC per output structure below
5. Validate drawing conditions are facially determinable with no investigative burden on bank

## Output Structure

### Header

| Element | Content |
|---|---|
| Title | "IRREVOCABLE STANDBY LETTER OF CREDIT — SECURITY DEPOSIT" |
| Reference No. | Bank's standard LOC numbering |
| Issuance Date | Date of execution |
| Governing Rules | "Issued subject to ISP98 and UCC Article 5 as adopted in [Bank's State]" |
| Lease Reference | Lease date, property address, landlord name, tenant name — matched exactly to lease |

### Section 1: Parties

- **Issuing Bank** — legal name, principal office, branch, charter/regulatory info, authorized signatories
- **Beneficiary (Landlord)** — legal name per lease, notice address, tax ID
- **Applicant (Tenant)** — legal name, co-tenants/guarantors if any
- Address notice routing if property management company involved or ownership may transfer

### Section 2: Credit Amount & Purpose

- State amount in numerals and words; reconcile with lease deposit requirement
- Adjust for state-mandated interest accrual if applicable
- Purpose: secures tenant's full performance — rent, maintenance, restoration (reasonable wear and tear excepted)
- Independence principle: bank's obligation is documentary only, independent of landlord-tenant disputes

### Section 3: Drawing Conditions

Beneficiary presents to issuing bank's designated office:

| Document | Requirements |
|---|---|
| Sight draft | Drawn on issuing bank, amount ≤ available balance |
| Signed statement | On beneficiary letterhead certifying: (a) tenant default or damage, (b) specific lease provision breached, (c) amount claimed |
| Notice certification | Dates and methods of required default notices per lease and law |
| Supporting docs (optional) | Copies of default notices, account statements, damage assessments |

- Presentation: hand delivery or overnight courier with proof of receipt
- Examination: [5] business days after complying presentation (per ISP98)
- Bank examines facial compliance only — no duty to investigate facts

### Section 4: Expiration, Renewal & Termination

- **Initial expiry**: [30–60] days after lease termination
- **Evergreen clause** (if renewal options): auto-extends for 1-year periods unless bank gives written non-renewal notice ≥ 60 days before expiry
- **Termination**: beneficiary returns original LOC + signed release confirming full performance
- Expiry must accommodate state statutory deadlines for deposit return/itemized statements

### Section 5: Transferability

Select per deal: Transferable or Non-transferable.

If transferable:
- Beneficiary submits: written transfer request + original LOC + evidence of property transfer or lease assignment
- Bank issues amended LOC or transfer certificate within [10] business days
- Transfer fee: [amount/percentage] payable by [applicant/beneficiary]
- State whether partial transfers or single complete transfer only
- Must comply with UCC § 5-112

### Section 6: Partial Draws & Reinstatement

Select per deal: Partial draws permitted or Full draw only.

If partial draws:
- Each draw statement specifies exact amount, confirms ≤ available balance
- Bank notifies both parties of remaining balance after each draw
- Reinstatement: applicant may restore original amount within [15] days of draw by paying fees and providing documentation, or LOC remains permanently reduced

### Section 7: Governing Law & Disputes

- LOC governed by ISP98 and UCC Article 5 of [Bank's State], without conflict-of-law principles
- Lease governed separately per its own choice-of-law clause
- Exclusive jurisdiction: state and federal courts in [Bank's jurisdiction]
- Applicant submits to jurisdiction; waives inconvenient forum objection

### Section 8: Execution

- Signature blocks for two authorized bank officers (name, title, date)
- Bank certification: signatories duly authorized; instrument is valid, binding, enforceable
- Optional beneficiary acknowledgment of receipt (not a condition of effectiveness)
- Safekeeping: beneficiary must present original for draws or amendments

## Pitfalls & Checks

- **Independence principle** — never draft conditions requiring the bank to evaluate lease disputes or investigate facts beyond presented documents
- **State law** — verify jurisdiction deposit statute; CA, NY, MA impose specific LOC-as-deposit requirements (caps, interest, return timelines) [VERIFY at time of drafting]
- **ISP98 Rule 1.06** — standby is irrevocable unless expressly stated otherwise; include explicit "irrevocable" language regardless
- **UCC § 5-108** — strict compliance standard; drawing conditions must be unambiguous and facially determinable
- **UCC § 5-112** — governs transfer rights; ensure transfer provisions don't conflict
- **No investigative burden** — drawing documents must never require the bank to verify external facts, contact third parties, or interpret lease provisions
- **Draw trigger balance** — overly broad triggers invite wrongful draws; overly narrow triggers undermine security purpose
- **Bank confirmation** — always verify bank's internal LOC issuance requirements, signature authority limits, and form preferences before finalizing

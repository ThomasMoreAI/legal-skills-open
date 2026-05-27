---
name: subordination-agreement
title: Subordination Agreement
description: Drafts debt subordination agreements establishing senior/junior creditor priority, payment waterfalls, standstill provisions, turnover obligations, and bankruptcy treatment. Use when drafting subordination agreements, intercreditor arrangements, creditor priority documents, or debt subordination terms during negotiation or closing.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/subordination-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
---

# Subordination Agreement

Drafts a subordination agreement establishing creditor claim priority, payment waterfall mechanics, and intercreditor rights for debt transactions.

## Quick Start

Gather before drafting:

1. **Senior Debt instruments** — principal, rate, maturity, collateral, default provisions
2. **Junior Debt instruments** — same details plus any existing subordination or intercreditor arrangements
3. **Party information** — legal names, jurisdictions, authorized signatories for Senior Creditor, Junior Creditor, and Debtor
4. **Security interests** — collateral descriptions, lien positions, guarantees, cross-default provisions
5. **Commercial terms** — complete vs. partial subordination, permitted junior payments (if any), standstill duration

## Core Workflow

Draft the following sections in order.

### 1. Recitals

| Element | Content |
|---------|---------|
| Senior Debt | Material terms — principal, rate, maturity, instrument date |
| Junior Debt | Material terms — same |
| Business purpose | Why subordination is needed |
| Consideration | What supports the agreement |

### 2. Definitions

- **"Senior Debt"** — principal, accrued interest, fees, enforcement costs, post-petition interest
- **"Junior Debt"** — full scope of junior obligations
- **"Payment in Full"** — treatment of contingent obligations, indemnities, post-petition interest
- **"Permitted Junior Payments"** — carve-outs from subordination (if partial)
- **"Default Period"** — trigger for standstill and enforcement restrictions

### 3. Subordination Mechanics

Waterfall: Senior Debt (principal + interest + fees + enforcement costs) → only after Payment in Full → Junior Debt.

- [ ] All Junior Debt payments/distributions/recoveries subordinated to prior Payment in Full of Senior Debt
- [ ] Junior Creditor barred from receiving payments except Permitted Junior Payments (if any)
- [ ] Standstill: no acceleration, enforcement, or remedy by Junior Creditor without Senior Creditor consent during Default Period
- [ ] Turnover: Junior Creditor must immediately remit prohibited payments to Senior Creditor
- [ ] Trust relationship: turnover payments received in trust for Senior Creditor

### 4. Representations & Warranties

**All parties:** valid existence, enforceability of debt instruments, no existing defaults, accuracy of stated amounts, authority to execute, no conflicts.

**Junior Creditor additionally:** no prior subordination to other creditors; no other subordination agreements exist.

### 5. Junior Creditor Covenants

- No amendments to Junior Debt adverse to Senior Creditor without consent
- No additional security interests or liens without consent
- Notice obligations on defaults or amendments
- Cooperation in bankruptcy/insolvency proceedings
- Bankruptcy voting: consistent with Senior Creditor interests or abstain

### 6. Events of Default & Remedies

**Triggers:** breach of subordination provisions, unauthorized Junior Debt amendments, enforcement actions violating standstill, Junior Creditor bankruptcy filing.

**Remedies:** specific performance, injunctive relief, turnover enforcement.

### 7. Bankruptcy & Insolvency

- Subordination effective before, during, and after any bankruptcy case
- Draft to satisfy 11 U.S.C. § 510(a) enforceability requirements
- Junior Creditor waives right to challenge subordination in bankruptcy
- Junior Creditor to file subordination proofs of claim

| Issue | Treatment |
|-------|-----------|
| Adequate protection payments | Typically none until Senior paid in full |
| Cash collateral / DIP financing motions | Standing to object typically waived or limited |
| Plan participation | Subject to subordination waterfall |
| Post-petition interest | Clarify whether included in "Payment in Full" |

### 8. General Provisions

- **Governing law** — match Senior Debt governing law or Debtor's state of organization
- **Jurisdiction/venue** — match Senior Debt forum
- **Amendments** — written consent of all parties; specify whether Debtor consent required
- **Survival** — continues until Senior Debt paid in full regardless of Debtor discharge/release
- **Assignment** — binds successors; Junior Creditor may not assign without Senior Creditor consent
- Severability, integration, jury trial waiver, notice provisions

### 9. Signature Blocks

- Senior Creditor, Junior Creditor, Debtor
- Corporate attestation lines; seals if required by governing law
- Notarization if subordination relates to real property security interests

## Pitfalls & Checks

- **Complete vs. partial** — confirm with user; if partial, define Permitted Junior Payments precisely (e.g., scheduled interest while no default exists)
- **Cross-references** — verify alignment with any existing intercreditor agreement, security agreement, or loan document subordination provisions
- **Defined terms** — audit all cross-references and defined terms for consistency before finalizing
- **Recording** — check jurisdiction-specific requirements if agreement will be recorded or filed publicly
- **UCC** — if collateral involved, confirm subordination of lien priority is addressed separately or within this agreement
- **Multi-tier debt** — if more than two tiers, expand waterfall accordingly
- **No placeholders** — flag missing information as targeted client questions rather than inserting brackets

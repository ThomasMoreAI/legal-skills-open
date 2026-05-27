---
name: pos-license
title: Software & POS System License Agreement
description: Drafts Software and POS System License Agreements for proprietary software use between licensor and licensee. Covers license grants, financial terms, IP, PCI-DSS data security, SLAs, and termination. Use when drafting POS software licenses, SaaS subscriptions, franchise technology licenses, or software distribution agreements.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/pos-license
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
tags: [agreement, drafting, transactional]
---

# Software & POS System License Agreement

Drafts a license agreement governing access, installation, and operation of proprietary software and POS system technology.

## Prerequisites

Gather before drafting:

1. **Parties** — legal names, entity types, jurisdictions, bound affiliates
2. **Software specs** — deployment model (cloud/on-premises/hybrid), components, documentation, source vs. object code
3. **Commercial terms** — pricing model, payment schedule, renewal structure, user/location counts
4. **Technical requirements** — hardware integration, payment processing, inventory management, multi-location needs
5. **Regulations** — PCI-DSS, GDPR/CCPA applicability, state-specific licensing rules

## Quick Start

1. Collect party and software details per Prerequisites
2. Draft each section below in order, flagging gaps with `[NEEDS INPUT]`
3. Mark jurisdiction-specific items with `[JURISDICTION NOTE]`
4. Run Checks before finalizing

## Drafting Sections

### 1. Recitals & Definitions

- Identify parties with entity type, principal place of business, jurisdiction
- Establish licensor ownership context and licensee's business need
- Define all capitalized terms in a dedicated section or on first use

### 2. Grant of License

| Parameter | Options |
|---|---|
| Exclusivity | Exclusive / Non-exclusive |
| Term | Perpetual / Fixed / Renewable |
| Scope | Internal use only / Third-party service permitted |
| Users | Named / Concurrent / Unlimited |
| Locations | Single-site / Multi-location / Geographic limits |
| Code access | Object code only / Source code included |
| Deployment | Cloud / On-premises / Hybrid |
| Updates | Included / Separate fee / Major vs. minor |
| Sublicensing | Prohibited / With consent / Affiliate carve-out |

Explicitly restrict reverse engineering, decompilation, disassembly, and derivative works unless negotiated.

### 3. Financial Terms

- **Fee structure** — one-time / subscription / per-user / per-transaction / hybrid
- **Payment** — due dates, methods, currency
- **Late payments** — interest rate, grace period
- **Renewal pricing** — auto-renewal terms, escalation cap, notice period
- **Taxes** — allocate sales/use/VAT responsibility
- **Audit rights** — licensor verifies user-count/transaction-volume compliance; underpayment reconciliation

### 4. Intellectual Property

- Licensor retains all ownership; license conveys no title
- Derivative works/customizations — specify ownership (typically licensor)
- Licensee feedback assigned to licensor without compensation
- Licensee business data remains licensee property; system architecture remains licensor property

### 5. Confidentiality & Data Protection

- Mutual NDA with standard carve-outs; survives termination (specify duration)
- **POS-specific**:
  - PCI-DSS compliance for payment card data
  - Encryption in transit + at rest
  - Breach notification timeline and procedure
  - GDPR/CCPA: identify controller vs. processor; include DPA if required

### 6. Warranties & SLAs

**Limited warranty** (typically 90 days): software substantially conforms to specs. Exclusive remedy: defect correction, then refund if correction not commercially reasonable.

**POS performance SLAs** (if applicable):

| Metric | Target | Remedy |
|---|---|---|
| Uptime | 99.X% | Service credits |
| Transaction speed | < X seconds | Escalation |
| Support response | X hours | Penalty/credit |

**Disclaimers**: disclaim implied warranties (merchantability, fitness, non-infringement) to maximum extent permitted. No warranty of uninterrupted/error-free operation.

### 7. Liability & Indemnification

- **Exclusion** — consequential, incidental, indirect, special, punitive damages
- **Cap** — lesser of (a) fees paid in preceding 12 months or (b) total fees paid
- **Carve-outs** — confidentiality breach, IP infringement, gross negligence, willful misconduct, violation of law
- **Mutual indemnity** — third-party claims from breach, negligence, or legal violations
- **Procedure** — prompt notice → cooperation → indemnifying party controls defense/settlement

### 8. Term & Termination

| Trigger | Notice | Cure Period |
|---|---|---|
| Convenience | 30–90 days | N/A |
| Material breach | Immediate after cure | 15–30 days |
| Insolvency | Immediate | N/A |

**Post-termination**: cessation of usage rights, return/destroy software and confidential info, final payment, POS deactivation, data migration transition period, prorated refunds (if without cause), early termination penalties (if applicable).

**Survival**: confidentiality, IP ownership, liability limits, indemnification, governing law.

### 9. Dispute Resolution

- **Governing law** — specified state, exclude conflict-of-laws
- **Venue** — exclusive jurisdiction in designated courts
- **ADR ladder** — executive negotiation (15–30 days) → mediation (AAA/JAMS) → litigation or binding arbitration
- **Fee shifting** — prevailing party or each bears own (specify)

### 10. General Provisions

Severability, entire agreement/merger, amendment (written, signed), assignment restrictions (licensee restricted; licensor may assign to affiliates/in M&A), notice methods, non-waiver, force majeure, signature blocks with authority confirmation.

## Checks

- Use plain language; avoid archaic legalese ("witnesseth," "whereas")
- Consistent defined terms throughout; capitalize on each use
- Number all sections for cross-reference
- Adapt license terms for POS concerns: hardware integration, payment processing, inventory management, multi-location deployment
- Verify UCC Article 2/2A compliance, consumer protection laws, and industry regulations
- For franchise contexts: cross-check FDD Item 11 and franchise agreement technology provisions

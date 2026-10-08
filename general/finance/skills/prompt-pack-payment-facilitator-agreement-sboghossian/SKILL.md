---
name: prompt-pack-payment-facilitator-agreement-sboghossian
title: Payment Facilitator Agreement
description: 'Use when drafting an agreement between a payment facilitator (PayFac) and an acquiring bank (or sponsor bank) governing the PayFac''s authority to onboard and manage sub-merchants, process card transactions, and bear acquiring liability. Covers sub-merchant underwriting standards, transaction monitoring, chargeback management, reserve requirements, PCI-DSS compliance, and liability allocation. MENA-relevant: UAE and KSA payment regulation context included.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-payment-facilitator-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Payment Facilitator Agreement

## When to use this

Use this skill when drafting the foundational agreement between a payment facilitator (PayFac) — a company that aggregates payments for sub-merchants under its own merchant account — and the sponsoring acquiring bank. This agreement sits at the top of the PayFac structure and governs the rights and obligations of both parties in connection with the aggregated payment processing model.

**PayFac model context**: Unlike a traditional merchant acquirer relationship (where each merchant has a direct relationship with the acquirer), a PayFac has a single merchant account with the acquirer and onboards "sub-merchants" under it. This is the commercial model used by companies like Stripe, Square, and regional FinTechs in the GCC.

Triggers:
- "Draft the agreement between our payment facilitator and the acquiring bank."
- "We need a PayFac agreement covering sub-merchant onboarding and chargeback liability."
- "Draft a payment aggregator agreement for our fintech platform."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| PayFac name and jurisdiction | Identifies the aggregating entity; regulatory status | Ask user |
| Acquiring bank name | The sponsoring acquirer holding the master merchant account | Ask user |
| Card networks applicable | Visa / Mastercard / AMEX / Mada (KSA) / others | Ask user |
| Sub-merchant segments | E-commerce, marketplace, SME, specific industry verticals | Ask user |
| Settlement terms | How quickly PayFac is funded and how PayFac funds sub-merchants | Ask user |
| Reserve structure | Type and size of reserve (rolling / fixed / capped) | Ask user |

## Optional inputs

- International transaction handling and currency conversion
- Transaction monitoring thresholds for AML/fraud alerts
- Prohibited sub-merchant categories (MCC restrictions)
- PCI-DSS compliance level and validation method

## Document structure

### 1. Parties and Recitals
- PayFac: [Name], registered in [Jurisdiction], licensed as [payment institution / service provider — specify licence]
- Acquiring Bank: [Name], a licensed acquiring bank under [UAE Central Bank / SAMA / Central Bank of Bahrain / etc.] regulations
- Card network principals under whose rules both parties operate
- Purpose: the Bank sponsors PayFac to operate as a payment facilitator under the applicable card network rules, and the parties wish to set out their respective rights and obligations

### 2. Scope of Services

**Bank's obligations**:
- Maintain a master merchant account for PayFac
- Authorize and process card transactions submitted by PayFac on behalf of sub-merchants
- Settle net proceeds to PayFac per the agreed settlement schedule
- Provide access to card network connectivity (BINs, processing infrastructure)

**PayFac's obligations**:
- Onboard sub-merchants in accordance with this Agreement and applicable card network rules
- Submit transactions on behalf of sub-merchants for processing
- Bear full liability for sub-merchant chargebacks and fraud losses
- Comply with all applicable card network rules, AML/CFT law, and data security standards

### 3. Sub-Merchant Underwriting

**KYC/AML requirements**:
- PayFac must conduct KYC/AML due diligence on each sub-merchant before onboarding consistent with applicable law (UAE AML Cabinet Decision, KSA AML Law, FATF standards)
- Minimum KYC data: trade licence / company registration, UBO identification, principal officer identity, bank account details
- Enhanced due diligence for: high-risk industries, high-volume sub-merchants, cross-border remittance services

**Risk-based underwriting**:
- PayFac must maintain a written underwriting policy approved by the Bank
- Risk categories: low / medium / high (based on industry, transaction volume, geography)
- High-risk sub-merchants require Bank pre-approval before onboarding

**Prohibited sub-merchant categories**:
List MCCs (Merchant Category Codes) that PayFac may not onboard without Bank written approval, typically including:
- Gambling and online gaming
- Adult content
- Cryptocurrency exchanges (subject to applicable regulatory permission)
- Money transmission services
- Firearms and controlled substances
- Debt collection

**Sub-merchant agreement**:
- PayFac must have each sub-merchant execute a sub-merchant agreement that flows down all material obligations of this Agreement, including card network rules compliance and chargeback obligations.

### 4. Transaction Processing

**Submission requirements**:
- Transactions submitted via [API / ISO 8583 / EMVCo — specify] in compliance with card network technical specifications
- PayFac responsible for transaction integrity, data completeness, and proper MCC coding
- Prohibited: submitting fictitious transactions, credit vouchers without a corresponding sale, or transactions processed after agreement termination

**Transaction monitoring**:
- PayFac must maintain a real-time fraud and AML monitoring system
- Velocity checks: flag transactions exceeding [X] per sub-merchant per day or [USD Y] per single transaction for manual review
- Card network fraud ratio monitoring: if PayFac's aggregate fraud ratio exceeds [Visa / Mastercard] program thresholds, Bank may impose transaction volume restrictions

**Refunds and credits**:
- PayFac must process customer refunds within [5 business days] of authorization
- Credits may not exceed the original transaction amount
- Refund float: Bank may require PayFac to maintain sufficient settlement funds to cover pending refunds

### 5. Chargebacks

**Liability**: PayFac bears full liability for all chargebacks on sub-merchant transactions, including disputes under card network dispute resolution programs.

**Chargeback management**:
- PayFac must maintain a chargeback management function capable of responding to retrieval requests within [10 business days] and chargeback disputes within [30 calendar days]
- PayFac must ensure sub-merchants retain transaction evidence (receipts, delivery confirmation, customer authorization) for [18 months]

**Chargeback thresholds**:
- Visa Chargeback Monitoring Program: chargeback ratio above [1%] by volume or count triggers reporting and remediation obligations
- Mastercard Excessive Chargeback Program: analogous thresholds
- If PayFac's portfolio chargeback ratio exceeds threshold: Bank may impose transaction volume caps, increase reserve, or initiate termination notice

**Debit from settlement**:
- Bank may debit PayFac's settlement account for chargeback amounts, fees, and fines imposed by card networks on the Bank due to PayFac's portfolio performance.

### 6. Settlement

**Settlement timing**:
- Bank settles to PayFac [T+1 / T+2 / T+3] for approved transactions, net of fees and chargebacks
- PayFac is responsible for funding sub-merchants; Bank has no direct obligation to sub-merchants

**Withholding**:
- Bank may withhold settlement amounts representing: estimated chargebacks; disputed transactions under investigation; regulatory freezes

**Rolling reserve**:
- Bank holds a rolling reserve of [X]% of gross transaction volume, calculated on a [weekly / monthly] basis, held for a rolling [90 / 120]-day period
- Reserve is released on a rolling basis after the retention period provided no outstanding claims exist

**Fixed reserve**:
- As an alternative or supplement: a fixed minimum reserve of [USD Y] maintained in a dedicated account; increased by Bank if risk profile deteriorates

### 7. Fees

| Fee | Amount / Basis |
|---|---|
| Processing fee | [X] basis points per transaction |
| Authorization fee | [USD Y] per authorization attempt |
| Chargeback fee | [USD Z] per chargeback dispute |
| Card network pass-through fees | At cost; Visa / Mastercard interchange and assessment fees |
| Card-not-present premium | [X] basis points additional for CNP transactions |
| International transaction fee | [X] basis points for cross-border transactions |
| Refund processing | [USD Y] per refund |

### 8. PCI-DSS Compliance

- PayFac must maintain PCI-DSS Level 1 compliance (or Level 2 for lower volume, per card network rules); submit annual Report on Compliance (RoC) and quarterly network scans
- PayFac is responsible for sub-merchants' PCI compliance; must attest to sub-merchants' compliance annually
- Breach obligation: PayFac must notify Bank within [24 hours] of any actual or suspected card data breach; cooperate with forensic investigation; bear all resulting fines and card replacement costs

### 9. AML/CFT Compliance

- PayFac operates as a Reporting Institution (or equivalent) under applicable AML law; must maintain a compliant AML/CFT program
- PayFac must file Suspicious Transaction Reports (STRs) with the Financial Intelligence Unit (FIU) directly; must notify Bank of any STR that involves the Bank's accounts
- PayFac must screen sub-merchants and their beneficial owners against applicable sanctions lists (OFAC, UN, EU, local UAE / KSA lists) at onboarding and on a continuous basis

### 10. Data Protection

- Card data processed by PayFac must comply with PCI-DSS; no unencrypted card data may be stored by PayFac
- Personal data of sub-merchants and their customers processed in accordance with applicable data protection law
- Data sharing between Bank and PayFac governed by a DPA as required under UAE PDPL / GDPR / KSA PDPL

### 11. Term and Termination

**Term**: [1 / 2] years, renewable automatically unless terminated on [90-day] notice.

**Immediate termination by Bank**:
- PayFac's card network registration is revoked
- PayFac becomes insolvent
- Fraud ratio or chargeback ratio exceeds defined threshold after warning period
- AML/CFT compliance failure
- Data breach involving card data

**Post-termination**: PayFac continues to be liable for chargebacks on transactions processed before termination; reserve retained by Bank until all chargeback claims are resolved.

### 12. Governing Law

Governed by [UAE law / KSA law / English law — choose per jurisdiction of acquirer]. Card network rules (Visa International Operating Regulations, Mastercard Rules) supersede this Agreement to the extent of conflict.

## Jurisdictional notes

| Jurisdiction | Key regulatory points |
|---|---|
| **UAE** | UAE Central Bank Payment Token Services Regulation and Stored Value Facilities Regulation govern payment facilitators; CBUAE licence required for PayFac operating in UAE; AML obligations under UAE Cabinet Decision No. 10/2019. |
| **KSA** | SAMA payment service provider regulations; SAMA requires a PSP licence for payment facilitation; Mada (national debit network) rules apply alongside Visa/Mastercard rules; AML obligations under Saudi AML Law. |
| **DIFC / ADGM** | DFSA / FSRA regulate payment services within DIFC / ADGM; suitable for PayFacs targeting cross-border or B2B payment flows; English-law governed. |

## Common mistakes

- **Underestimating chargeback liability**: PayFacs bear unlimited liability for their sub-merchant portfolio's chargebacks; the reserve mechanism must be sized appropriately relative to the risk profile.
- **Weak sub-merchant underwriting**: onboarding high-risk sub-merchants without enhanced due diligence exposes the PayFac and the sponsoring bank to card network fines, fraud losses, and regulatory sanctions.
- **No PCI-DSS flow-down to sub-merchants**: PayFac is liable for the PCI compliance of its sub-merchant portfolio; the sub-merchant agreement must require PCI compliance and attestation.
- **Omitting AML screening of sub-merchants**: treating AML as a one-time onboarding check is insufficient; continuous sanctions screening is required under most jurisdictions.

## Related skills

- [[prompt-pack-payment-services-agreement]]
- [[prompt-pack-open-banking-api-terms]]
- [[prompt-pack-lending-platform-terms]]
- [[prompt-pack-master-services-agreement]]
- [[heuristic-always-state-jurisdiction-first]]

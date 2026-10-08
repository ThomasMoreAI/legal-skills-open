---
name: prompt-pack-bnpl-platform-agreement-sboghossian
title: BNPL Platform Agreement
description: Use when drafting a buy-now-pay-later (BNPL) platform agreement between a BNPL provider and a merchant, covering integration requirements, payment terms, merchant fees, customer credit assessment, default handling, returns and refunds, and consumer credit regulation compliance. FinTech/payments practice area with MENA-specific attention to consumer credit licensing (UAE, KSA, EG) and Sharia-compliant BNPL structures.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-bnpl-platform-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# BNPL Platform Agreement

## When to use this

Use this skill when a BNPL (buy-now-pay-later) provider needs a **platform agreement** with a merchant who will offer BNPL as a payment option to that merchant's customers. The BNPL provider takes on the credit risk of the customer; the merchant receives payment (net of fees) from the BNPL provider.

This agreement defines the commercial and legal relationship between the BNPL provider and the merchant. A separate (B2C) agreement governs the relationship between the BNPL provider and the end customer — that is not this document.

Relevant for:
- BNPL fintechs expanding their merchant network in MENA
- E-commerce platforms seeking BNPL partnerships
- Banks and licensed lenders offering BNPL as a product
- Merchants assessing BNPL provider terms

---

## Prompt template

> Draft a buy-now-pay-later platform agreement between [BNPL Provider] and [Merchant]. Include integration requirements, payment terms, merchant fees, customer credit assessment, default handling, returns/refunds, and consumer credit regulation compliance.

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before drafting.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| BNPL provider name, licensing status, and jurisdiction | Determines regulatory framework and what the provider is licensed to do |
| Merchant name, business type, and jurisdiction | Consumer-facing retail vs. B2B affects BNPL regulatory treatment |
| Jurisdictions where customers will use BNPL | Consumer credit regulation applies in the customer's jurisdiction |
| Fee structure | Merchant discount rate; late payment fees; setup fees |
| BNPL product parameters | Number of installments; interest-free vs. interest-bearing; maximum transaction amount |

---

## Document structure

### 1. Parties and recitals
- Full legal names and jurisdictions; licensing/regulatory status of the BNPL provider
- Recital: the BNPL provider is licensed to provide deferred payment or credit services; the merchant wishes to offer this service to its customers

### 2. Definitions
Key defined terms for BNPL agreements:
- **BNPL Transaction**: a customer purchase where the BNPL provider finances the purchase price
- **Settlement Amount**: the amount the BNPL provider pays the Merchant (typically purchase price minus Merchant Discount Rate)
- **Merchant Discount Rate (MDR)**: the fee the merchant pays to the BNPL provider, expressed as a percentage of the transaction value
- **Instalment Plan**: the customer's repayment schedule
- **Chargeback**: a disputed transaction reversed by the BNPL provider
- **Eligible Purchase**: transactions that qualify for BNPL (above/below certain values; not certain product categories)

### 3. BNPL service

#### 3.1 Service description
- The BNPL provider will offer an instalment payment option at the merchant's checkout (online and/or in-store)
- The provider will assess the customer's creditworthiness and approve or decline the BNPL application
- On approval, the provider pays the merchant the Settlement Amount; the customer repays the provider over the agreed instalment schedule

#### 3.2 Customer credit assessment
The merchant must understand (and the agreement must state):
- Credit assessment is entirely the BNPL provider's responsibility; the merchant has no input into individual credit decisions
- The provider may decline any transaction at its discretion; the merchant has no claim for a declined transaction
- The merchant must not imply that BNPL approval is guaranteed
- The provider's credit assessment methodology, data sources, and criteria are proprietary — the agreement does not require disclosure to the merchant

#### 3.3 Customer terms
- The customer's instalment agreement is between the customer and the BNPL provider only
- The merchant is not a party to the customer's instalment obligation
- The merchant is paid whether or not the customer repays the provider (the provider takes the credit risk — this is the merchant value proposition)

### 4. Merchant obligations

#### 4.1 Integration
- Technical integration via API or embedded widget as specified in the technical specification (Schedule A)
- Merchant must not modify the BNPL payment flow without provider approval
- Merchant must display BNPL option clearly and in accordance with the provider's branding guidelines
- Merchant must not represent BNPL terms to customers other than those approved by the provider

#### 4.2 Eligible purchases
- Minimum and maximum transaction amounts
- Excluded categories (typically: gambling, adult content, weapons, cryptocurrency, financial products — list specifically)
- Geographic restrictions: BNPL is only available to customers in specified territories

#### 4.3 Customer information
- Merchant must provide accurate transaction information to the provider at the time of BNPL application
- Merchant must not encourage customers to apply for BNPL with false information

#### 4.4 Compliance obligations
- Merchant must comply with all applicable law in the jurisdictions where it operates
- Merchant must not offer BNPL in jurisdictions where the provider is not licensed

### 5. Payment terms — Merchant Settlement

#### 5.1 Settlement process
- The provider will settle the Settlement Amount to the merchant within [X] business days of the BNPL transaction being approved and goods/services delivered/provided
- Settlement is net of the Merchant Discount Rate
- Settlement schedule: daily, weekly, or per batch (specify)

#### 5.2 Merchant Discount Rate (MDR)
- Define the MDR (e.g., 2.5% of transaction value)
- Whether MDR varies by product category, transaction size, or jurisdiction
- Right to adjust MDR: notice period; merchant's right to terminate if new MDR is not acceptable

#### 5.3 Currency and withholding
- Settlement currency
- Cross-border payments: withholding tax obligations; gross-up clause (or not)

### 6. Default handling and chargebacks

#### 6.1 Customer default
- When a customer fails to repay the provider, this has **no effect on the merchant** — the merchant has already been paid (net of MDR). The credit risk is the provider's.
- Exception: if the transaction was fraudulent and the merchant was involved, the provider may claw back the settlement (see fraud provisions)

#### 6.2 Merchant chargebacks
A chargeback is a transaction the provider reverses against the merchant, typically because:
- The customer disputed the transaction (non-delivery, wrong item, fraud)
- The transaction was unauthorized or involved merchant fraud

Chargeback process:
- Provider notifies merchant of chargeback
- Merchant has [X] days to dispute with supporting evidence (proof of delivery, authorization records)
- Provider makes final determination
- Chargeback amount is set off against future settlements or charged back to merchant

**Chargeback liability rules**: merchant is liable for chargebacks resulting from merchant fraud or non-delivery; merchant is not liable for customer credit defaults.

### 7. Returns and refunds

- When a customer returns goods and is entitled to a refund, the merchant must notify the provider within [X] business days
- Provider reverses the instalment plan and issues a refund to the customer
- Merchant reimburses the provider the Settlement Amount (but not the MDR) within [X] days
- Partial refunds: provider adjusts the instalment plan; recalculates remaining instalments

### 8. Consumer credit regulation compliance

**This is the most legally significant section in the MENA context.** BNPL straddles the boundary between payment services and consumer credit regulation:

| Jurisdiction | BNPL regulatory status |
|-------------|----------------------|
| UAE (CBUAE) | CBUAE Financial Consumer Protection Regulation applies; BNPL products may require a personal finance licence; CBUAE has issued specific guidance on BNPL (2023–2024 fintech framework). Interest-free BNPL may be structured as deferred payment rather than credit to avoid consumer credit licensing |
| UAE (DIFC / DFSA) | DFSA Consumer Credit Module applies; BNPL must comply with Conduct of Business rules |
| KSA (SAMA) | SAMA Personal Finance Regulations apply if BNPL involves finance charges; Sharia-compliance required; interest-bearing BNPL requires Islamic finance structure (murabaha or tawarruq) |
| Egypt (CBE) | Consumer finance regulation; BNPL providers must be licensed by the CBE or the Financial Regulatory Authority (FRA) |
| EU | Consumer Credit Directive (2023 EU CCD) explicitly covers BNPL; full credit assessment requirements; right of withdrawal; APR disclosure |
| UK | FCA regulation; BNPL included in Buy-Now-Pay-Later regulation (Financial Services and Markets Act amendments) |

**Sharia-compliant BNPL note**: in KSA and UAE Islamic markets, BNPL is often structured as a murabaha (cost-plus sale) rather than a loan — the provider purchases the goods and sells them to the customer at a profit margin, with deferred payment. The platform agreement should reflect the structure used.

Compliance obligations in the agreement:
- BNPL provider must maintain required licences
- Agreement must permit the merchant to comply with applicable consumer protection law
- Merchant must not misrepresent BNPL terms to customers
- Both parties must cooperate with regulatory enquiries

### 9. Data and privacy

- Customer personal data is processed by the BNPL provider (the credit assessment process)
- Merchant receives transaction status but not the customer's credit information
- Data processing agreement (DPA) should be embedded or attached — required under UAE PDPL, DIFC Data Protection Law, GDPR
- Data minimization: merchant should only receive the minimum customer information needed for its records

### 10. Intellectual property

- The BNPL provider licenses its branding, logo, and checkout widget to the merchant for use in the BNPL presentation
- Merchant may not modify the materials
- License terminates on termination of the agreement

### 11. Term, suspension, and termination

- Term: typically 12–24 months; auto-renews unless notice given
- Suspension: provider may suspend merchant from the BNPL platform for fraud suspicion, high chargeback rate, compliance breach — with immediate effect in serious cases
- Termination: by either party on [60/90] days' notice; for cause (material breach, insolvency, licence revocation) on [5/10] days' notice or immediately
- Effect of termination: transactions already processed continue per their instalment schedule; no new BNPL transactions after termination

### 12. Liability and indemnity

- BNPL provider's liability cap: typically the settlement amounts paid to the merchant in the preceding [3/6/12] months
- Mutual exclusion of consequential damages
- Merchant indemnifies provider for: merchant fraud; misrepresentation to customers; non-delivery of goods; breach of the agreement

### 13. Governing law and dispute resolution

- Jurisdiction-specific choice (DIFC law + DIFC arbitration for UAE cross-border; English law + ICC for international)
- Consider DIAC arbitration for UAE domestic disputes

---

## Jurisdictional notes

### UAE
CBUAE has been developing a comprehensive BNPL regulatory framework. Providers must monitor CBUAE guidance actively — the framework is evolving. The critical question is whether the specific BNPL product structure requires a personal finance licence (if it involves finance charges) or falls under payment services (if truly interest-free deferred payment). Get legal advice on structure before launch.

### KSA
SAMA has required BNPL providers to operate through licensed finance companies (Tamwil companies) or banks. Pure technology BNPL platforms not directly providing credit must partner with a licensed finance entity. Sharia compliance is mandatory — interest-bearing BNPL cannot operate in KSA.

---

## Common mistakes

- Not addressing the precise regulatory characterization of the BNPL product (credit vs. payment service)
- Inadequate chargeback procedures (the most common operational dispute in BNPL agreements)
- No data processing agreement — required in all major MENA jurisdictions
- Merchant liability for customer credit defaults (this reverses the commercial proposition of BNPL for merchants)
- No refund mechanism — the settlement economics break down without a clear refund process

---

## Related skills

- [[prompt-pack-aml-kyc-policy]] — AML obligations that apply to BNPL providers
- [[kb-fintech-regulation-mena]] — MENA fintech licensing and regulatory reference
- [[heuristic-always-state-jurisdiction-first]] — consumer credit regulation is strictly jurisdiction-specific
- [[prompt-pack-agreement-legal-draft-review]] — reviewing a BNPL agreement presented by a counterparty

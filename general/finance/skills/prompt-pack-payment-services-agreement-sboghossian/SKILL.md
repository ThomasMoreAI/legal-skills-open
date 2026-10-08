---
name: prompt-pack-payment-services-agreement-sboghossian
title: Payment Services Agreement
description: 'Use when drafting an agreement between a payment service provider (PSP) and a merchant for processing card and digital payments. Covers transaction fees, settlement terms, chargebacks, rolling reserves, PCI-DSS compliance, data security, regulatory compliance, and liability allocation. MENA-focused: UAE CBUAE and KSA SAMA licensing requirements, local payment network rules (Mada, UAE NAPS), and regional AML obligations addressed.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-payment-services-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Payment Services Agreement

## When to use this

Use this skill when a payment service provider (PSP) — a fintech, payment gateway, or acquiring bank — needs to draft the merchant-facing agreement governing card acceptance, digital payment processing, settlement, and related services. This is the "downstream" agreement between the PSP and each individual merchant, distinguishable from the PayFac-acquirer agreement (see [[prompt-pack-payment-facilitator-agreement]]).

Triggers:
- "Draft a merchant payment services agreement for our payment gateway."
- "We're onboarding new merchants — draft our standard PSP merchant agreement."
- "Write a payment acceptance agreement covering PCI-DSS, chargebacks, and settlement terms."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| PSP name and jurisdiction | Identifies the service provider; determines regulatory framework | Ask user |
| Payment methods covered | Card (Visa/Mastercard/Mada), digital wallets, bank transfers | Ask user |
| Merchant segments | E-commerce / physical POS / marketplace / subscription | Ask user |
| Fee structure | Blended rate vs interchange-plus vs flat fee | Ask user |
| Settlement timing | T+1 / T+2 / T+3 | Ask user |
| Reserve policy | Rolling reserve %, duration | Ask user |

## Optional inputs

- Currency and multi-currency settlement
- Recurring / subscription billing terms
- Integration method (hosted payment page / API / SDK / POS terminal)
- Prohibited merchant categories
- Minimum monthly volume or commitment

## Document structure

### 1. Services
PSP will provide Merchant with:
- Payment acceptance services for the payment methods listed in the Merchant Application
- Transaction authorization, capture, and settlement processing
- Access to PSP's payment gateway / API / hosted checkout / POS system
- Transaction reporting and reconciliation tools
- Chargeback management support
- Customer support for technical integration issues

### 2. Merchant Eligibility and Onboarding

**KYC / AML obligations**:
- PSP must verify Merchant identity before activation: trade licence / company registration; UBO identification; principal officer identity; bank account details
- Merchant represents that all information provided at onboarding is accurate and complete; updates PSP immediately of material changes
- Ongoing KYC monitoring: periodic re-verification for high-risk merchants

**Merchant Application**: Merchant completes a Merchant Application setting out: business description, MCC code, expected monthly volume, average transaction value, website URL (for e-commerce), bank account for settlement. Approval is at PSP's sole discretion.

**Sub-merchants (if PSP is a PayFac)**: If PSP operates as a PayFac, each Merchant is a sub-merchant under PSP's master merchant account; Merchant acknowledges it has no direct relationship with the acquiring bank.

### 3. Acceptable Use

**Permitted use**: Merchant may use the Services only for card-present and card-not-present transactions arising from its bona fide sale of goods and services described in the Merchant Application.

**Prohibited activities**:
- Submitting transactions for goods or services not disclosed in the Merchant Application
- Processing transactions for Prohibited Businesses (see Annex — list of MCC-based prohibited categories: gambling, adult content, weapons, drugs, cryptocurrency where not licensed)
- Split transactions: dividing a single transaction across multiple charges to stay below authorization thresholds
- Card testing: running low-value test transactions on cards without genuine customer authorization
- Processing transactions after this Agreement is terminated
- Circumventing chargeback procedures

**Accuracy**: Merchant must not submit fictitious transactions, credits without a corresponding sale, or duplicate transactions.

### 4. Fees and Charges

| Fee | Rate / Amount | Notes |
|---|---|---|
| Processing fee — domestic cards | [X]% of transaction value | Card network + PSP margin |
| Processing fee — international cards | [Y]% | Higher due to cross-border interchange |
| Mada (KSA debit) / NAPS (UAE local) | [Rate per card network rules] | |
| Card-not-present premium | [X] basis points additional | For e-commerce vs POS |
| Refund processing | [USD Z] per refund | Or percentage |
| Chargeback fee | [USD W] per chargeback received | Win or lose |
| Monthly minimum | [USD M] per month | Fee applies if processing volume falls below threshold |
| PCI non-compliance fee | [USD X] per month | If Merchant fails to complete PCI SAQ |
| Retrieval request fee | [USD Y] per retrieval | Where PSP must respond to a card network dispute request |

PSP may update fees on [30-day] written notice; continued use after the effective date constitutes acceptance.

### 5. Settlement

**Settlement timing**: PSP settles net proceeds to Merchant's designated bank account within [T+1 / T+2 / T+3] business days of transaction authorization, subject to:
- Hold for chargebacks: unsettled amounts may be held pending chargeback resolution
- Reserve deductions (see below)
- Withholding: PSP may withhold settlement if Merchant's account is under investigation for fraud, chargebacks, or regulatory inquiry

**Settlement currency**: Settlement in [AED / SAR / USD / Merchant's local currency — specify]; currency conversion at [PSP's daily FX rate / mid-market rate + [X] basis points spread]

**Reconciliation**: Merchant receives daily settlement reports through PSP's portal; Merchant must reconcile within [5 business days] and report discrepancies within [15 business days].

**Deductions from settlement**: PSP may deduct from settlement: processing fees; chargeback amounts; refunds funded by PSP pending Merchant funding; fines imposed by card networks related to Merchant's account.

### 6. Reserve

**Rolling reserve**: PSP holds [X]% of Merchant's gross transaction volume, calculated weekly, held for a rolling [90 / 120]-day period. Reserve accumulates until it reaches the required level and is thereafter maintained on a rolling basis.

**Increased reserve**: PSP may increase the reserve percentage or minimum amount upon [5 business days'] notice if Merchant's fraud ratio, chargeback ratio, or financial condition materially deteriorates.

**Reserve release**: Rolling reserve released on the scheduled rolling basis provided no outstanding chargebacks, refunds, or claims. Full release on termination after all claims are resolved (which may take [180 days] post-termination to cover chargeback window).

### 7. Chargebacks

**Merchant liability**: Merchant bears full liability for chargebacks on transactions processed under this Agreement.

**Chargeback process**:
1. PSP notifies Merchant of incoming chargeback within [3 business days] of receipt
2. Merchant has [10 calendar days] to provide compelling evidence to contest the chargeback (transaction receipt, delivery confirmation, signed authorization, fraud prevention data)
3. PSP submits the dispute response to the card network on behalf of Merchant
4. Card network issues final decision; if chargeback is upheld, the amount is debited from Merchant's settlement or reserve

**Chargeback thresholds**:
- If Merchant's chargeback ratio exceeds [1.0%] of monthly transaction count or volume, PSP will place Merchant on a remediation plan
- If threshold is repeatedly breached, PSP may suspend processing, increase reserve, or terminate

**Friendly fraud**: PSP will assist Merchant in disputing chargebacks identified as "friendly fraud" (customer claims non-receipt but delivery can be confirmed); however, PSP does not guarantee a favorable outcome.

### 8. Data Security and PCI-DSS

**Merchant obligations**:
- Merchant must complete the applicable PCI-DSS Self-Assessment Questionnaire (SAQ) annually and provide the completed SAQ to PSP on request
- Merchant must not store full card numbers (PAN), CVV2, or full-track magnetic stripe data on Merchant's systems
- Merchant must use PSP's hosted payment page, tokenization, or point-to-point encryption (P2PE) for all card data capture, unless separately authorized
- Merchant must immediately notify PSP of any actual or suspected data breach involving card data

**PSP obligations**:
- PSP will maintain PCI-DSS Level 1 compliance certification
- PSP will not store card data beyond what is required for dispute resolution

**Breach costs**: Merchant bears all costs arising from a card data breach originating from Merchant's systems, including forensic investigation costs, card network fines, card replacement costs, and customer notification costs.

### 9. AML/CFT and Sanctions Compliance

- Merchant warrants that it conducts legitimate business and that all transactions submitted are for genuine commercial purposes
- Merchant must not process transactions on behalf of unlicensed money service businesses or in furtherance of money laundering, terrorist financing, or sanctions violations
- PSP has the right to block or refuse any transaction that it reasonably suspects violates applicable AML/CFT law or sanctions
- Merchant must provide documentation requested by PSP for AML/CFT compliance purposes within [3 business days]

### 10. Representations and Warranties of Merchant

Merchant represents and warrants at signing and on an ongoing basis:
- Merchant has all necessary licences to operate its business
- All information provided in the Merchant Application is accurate
- Merchant's website (for e-commerce) complies with all applicable consumer protection laws and displays required legal notices
- Merchant will comply with all card network rules applicable to merchants
- Merchant does not engage in any Prohibited Business activity

### 11. Liability

**PSP's limitation of liability**: PSP is not liable for: processing errors caused by Merchant's incorrect transaction data; system downtime caused by third-party infrastructure beyond PSP's reasonable control; losses resulting from fraud committed by Merchant's customers. PSP's total liability to Merchant in any 12-month period is limited to [fees paid by Merchant in the preceding 3 months / USD X].

**Consequential loss exclusion**: Neither party is liable to the other for indirect, consequential, or punitive damages.

**Merchant indemnity**: Merchant indemnifies PSP against all losses, fines, and regulatory sanctions arising from Merchant's breach of this Agreement, card network rule violations, or use of the Services for illegal purposes.

### 12. Term and Termination

**Term**: [1 year] from activation date; automatically renews unless terminated on [60-day] notice.

**Immediate suspension / termination by PSP**:
- Merchant's fraud or chargeback ratio breaches threshold (after warning)
- Merchant engages in a Prohibited Business activity
- Merchant becomes insolvent
- Data breach involving card data
- Regulatory direction from card network or competent authority

**Effect of termination**: Merchant must immediately cease submitting transactions; rolling reserve retained until all chargeback liability windows close; PSP has no obligation to continue processing after notice of termination.

### 13. Governing Law
Governed by [UAE Federal Law / KSA Law / English Law — specify]; DIFC or ADGM courts or arbitration for B2B disputes where a neutral forum is preferred; consumer transactions may be subject to mandatory consumer protection law that limits choice-of-court provisions.

## Jurisdictional notes

| Jurisdiction | Key requirements |
|---|---|
| **UAE** | UAE Central Bank Payment Token Services Regulation; PSPs must be licensed by CBUAE; merchants processing NAPS (UAE national payment scheme) must comply with NAPS rules; VAT (5%) applies to PSP fees. |
| **KSA** | SAMA PSP regulation; Mada debit network rules; SAMA circular on merchant discount rates; e-invoicing (ZATCA Phase 2) applies to certain transaction types; VAT (15%) on fees. |
| **DIFC / ADGM** | DFSA / FSRA PSP regulation; primarily B2B or FinTech-to-merchant arrangements; English law enforcement. |

## Common mistakes

- **Not addressing Mada / NAPS in GCC agreements**: UAE and KSA have national debit payment networks with specific contractual and technical requirements that are separate from Visa/Mastercard; omitting them creates gaps.
- **Vague settlement timing**: "within a few business days" creates disputes; state T+1/T+2/T+3 precisely and define the event that starts the clock (authorization vs capture vs batch settlement).
- **Insufficient chargeback liability disclosure**: merchants are often surprised by their unlimited chargeback exposure; make this unambiguous in the agreement and at onboarding.
- **No PCI flow-down to merchants**: PSP is ultimately responsible to the card networks for its merchant portfolio's PCI compliance; the PSA must require merchants to comply and certify annually.

## Related skills

- [[prompt-pack-payment-facilitator-agreement]]
- [[prompt-pack-open-banking-api-terms]]
- [[prompt-pack-lending-platform-terms]]
- [[prompt-pack-master-services-agreement]]
- [[heuristic-always-state-jurisdiction-first]]

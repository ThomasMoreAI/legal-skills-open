---
name: prompt-pack-lending-platform-terms-sboghossian
title: Lending Platform Terms
description: 'Use when drafting terms of service for a digital lending platform offering consumer or SME loans. Covers loan application process, credit assessment disclosure, interest rate transparency, repayment terms, default consequences, collection practices, and consumer protection compliance. MENA-first: addresses UAE Central Bank, SAMA (KSA), and Banque du Liban requirements, interest/Sharia compliance considerations, and DIFC/ADGM regulated lending frameworks.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-lending-platform-terms
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Lending Platform Terms

## When to use this

Use this skill when a digital lending platform, fintech company, or regulated financial institution needs to draft its borrower-facing terms of service governing the origination, disbursement, and repayment of loans. The document is addressed to borrowers and governs the relationship from application through loan closure or default.

Triggers:
- "Draft the loan terms for our consumer lending app."
- "We're launching an SME lending platform — what should the terms cover?"
- "We need terms that comply with UAE Central Bank lending regulations."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Platform name | Names the document | Ask user |
| Jurisdiction(s) of operation | Determines regulatory framework (licensing, consumer protection, interest rate caps) | Ask user |
| Borrower type | Consumer vs SME vs both — triggers different regulatory protections | Ask user |
| Loan products offered | Personal loan, SME working capital, invoice financing, buy-now-pay-later — determines product-specific clauses | Ask user |
| Sharia-compliance required | Determines whether interest-based or murabaha/ijara structure is used | Ask user |
| Regulatory licence held | Operating licence determines mandatory disclosure obligations | Ask user |

## Optional inputs

- Governing law and dispute resolution forum
- Credit bureau(s) used for credit assessment
- Collection agency relationships
- Privacy policy cross-reference
- Early repayment terms (whether permitted and at what cost)

## Document structure

### 1. Introduction and Acceptance
- Platform identity and regulatory status (licensed by [UAE Central Bank / SAMA / BdL / DFSA / FSRA / etc.])
- Scope: these terms govern all loans originated through the platform
- Acceptance: by submitting a loan application, the borrower accepts these terms
- Capacity: borrower must be of legal age and capacity in their jurisdiction

### 2. Eligibility and Application

- Eligibility criteria: nationality, residency, minimum age, income thresholds
- Application process: steps to apply (KYC / AML submission, income verification, identity documents)
- Credit assessment: platform uses [named credit bureau(s)] and internal scoring models; approval at platform's sole discretion
- **No guarantee of approval**: explicitly state that submission of an application does not guarantee loan approval

**MENA note**: UAE requires credit bureau checks via Al Etihad Credit Bureau (AECB); KSA through SIMAH or Bayan Credit Bureau; platforms must comply with applicable credit reporting laws.

### 3. Loan Terms and Disclosure

For each loan product, disclose in clear language:
- Principal amount
- Annual percentage rate (APR) or equivalent total cost of credit disclosure
- For Sharia-compliant products: profit rate, murabaha cost price, and total payment amount instead of "interest"
- Tenor (term in months)
- Repayment schedule (monthly installments, amounts, due dates)
- Total amount repayable
- Fees: origination fee, processing fee, early repayment fee, late payment fee
- Any security or guarantees required

**Consumer protection requirement**: Most jurisdictions require disclosure of the total cost of credit (not just the nominal interest rate) in a standardized summary box before acceptance. Confirm local regulatory requirements.

### 4. Disbursement
- Method: transfer to verified bank account; timing (same day / T+1 / T+2)
- Conditions to disbursement: signed loan agreement, completed KYC, any required guarantees
- Currency: AED, SAR, USD — specify; for LBP-denominated loans, include FX risk disclosure given currency instability

### 5. Repayment Terms
- Due dates and payment method (direct debit, bank transfer, platform wallet)
- Prepayment: right to repay early; whether early repayment fee applies (many consumer protection regimes cap or prohibit early repayment penalties)
- Grace period (if any) after a missed payment before default is triggered
- Allocation of payments: typically applied first to fees, then interest/profit, then principal (disclose clearly)

### 6. Default and Consequences
Define default clearly: typically, a payment missed by more than [5 / 10 / 30] days, or material misrepresentation in the application.

On default:
- Late payment charge: state the daily/monthly rate (subject to regulatory caps)
- Acceleration: right of platform to declare the full outstanding balance immediately due
- Credit bureau reporting: notify the borrower that default will be reported to the applicable credit bureau
- Collection: the platform may engage licensed collection agencies; describe the process and borrower rights

**Do not include**: threats of criminal action for civil debt default (common misuse in some MENA markets); penalties that constitute unenforceable liquidated damages under applicable law.

### 7. Collection Practices
- Permitted contact channels and hours (comply with consumer protection guidelines on harassment)
- Right to assign the debt to a third-party collection agency or debt purchaser
- Debt restructuring: platform's discretion to offer restructuring; not a binding obligation

### 8. Consumer Protection
Include explicit statements of borrower rights under applicable law:
- Right to receive a copy of the loan agreement
- Right to early repayment (subject to fee, if any)
- Right to complain: internal complaints procedure, then regulatory ombudsman or supervisory authority
- Anti-discrimination: loan decisions not made on prohibited grounds

### 9. Privacy and Data Use
Cross-reference the platform's Privacy Policy. Specifically state:
- Credit bureau sharing: borrower consents to credit bureau reporting of application and repayment data
- Marketing: opt-in / opt-out for marketing use of data
- Fraud prevention: data shared with fraud prevention databases

### 10. Governing Law and Dispute Resolution
- For UAE-licensed platforms: typically DIFC Court or UAE courts with Dubai International Arbitration Centre (DIAC) arbitration option; consumer protection law may limit choice-of-law clauses
- For KSA: Saudi courts; CIBAFI arbitration for Islamic finance disputes
- Mandatory: consumer complaints must first go through internal process and then to regulatory ombudsman before arbitration

### 11. Amendments to Terms
- Platform reserves right to amend terms with [30-day] notice for prospective loans
- Existing loans governed by terms in effect at loan origination date
- Consumer protection law may restrict unilateral amendment of interest rates on existing loans

## Jurisdictional notes

| Jurisdiction | Key regulatory requirements |
|---|---|
| **UAE** | UAE Central Bank Consumer Finance Regulation and licensed lending framework; maximum APR caps apply to consumer loans; Al Etihad Credit Bureau mandatory checks; AMLCFT Law compliance. |
| **DIFC / ADGM** | DFSA / FSRA regulated lending; English law; more flexible product structuring available; primarily B2B / sophisticated borrowers. |
| **KSA** | SAMA licensed consumer finance companies; Sharia compliance required for most products; SIMAH / Bayan credit bureau integration; maximum profit rate caps under SAMA guidelines. |
| **Lebanon** | Banque du Liban licensing; severe currency instability — all loan terms must address USD vs LBP denomination; consumer lending market severely constrained. |
| **Egypt** | Financial Regulatory Authority (FRA) oversight of non-bank lending; Central Bank of Egypt for banks; consumer credit disclosure requirements under Egyptian Consumer Protection Law. |

## Common mistakes

- **Failing to disclose total cost of credit**: regulators in UAE, KSA, EU, and UK require the equivalent of an APR / APRC in a standardized disclosure; quoting only the monthly rate misleads borrowers.
- **Sharia-non-compliant language**: using "interest" in documents for Islamic finance products creates regulatory and reputational risk; use "profit rate" and "murabaha" / "ijara" terminology consistently.
- **No complaints procedure**: most consumer protection regimes require an internal complaints procedure with defined response timelines.
- **Blanket data consent**: MENA data protection laws (UAE PDPL, KSA PDPL) require specific consent for each processing purpose; a single "I agree to use of my data" clause is insufficient.

## Related skills

- [[prompt-pack-payment-services-agreement]]
- [[prompt-pack-payment-facilitator-agreement]]
- [[prompt-pack-open-banking-api-terms]]
- [[prompt-pack-privacy-impact-assessment]]
- [[heuristic-always-state-jurisdiction-first]]

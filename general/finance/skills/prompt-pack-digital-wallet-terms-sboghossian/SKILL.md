---
name: prompt-pack-digital-wallet-terms-sboghossian
title: Digital Wallet Terms
description: 'Use when a FinTech or payments company needs to draft Terms of Service for a digital wallet application — covering account setup, funding methods, transaction limits, security features, unauthorized transaction liability, data privacy, and dispute resolution. MENA-aware: UAE (CBUAE Stored Value Facility licensing, DFSA/ADGM), KSA (SAMA), and addresses consumer protection requirements that apply to e-money and digital wallet products across MENA, EU (PSD2), and UK.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-digital-wallet-terms
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Digital Wallet Terms

Digital wallet Terms of Service are both a consumer contract and a regulated product disclosure. In MENA, the Central Bank of UAE, SAMA, and equivalent regulators require specific consumer disclosures and protections for stored value and e-money products; omitting them is not just a contractual gap but a regulatory violation.

## When to use this

- A FinTech company is launching a digital wallet app and needs compliant Terms of Service.
- An existing wallet's terms need to be updated following regulatory guidance from CBUAE, SAMA, DFSA, or ADGM FSRA.
- A bank or financial institution is adding a digital wallet feature to its mobile banking app.
- An e-commerce platform is adding a stored-value wallet feature for stored credit or refunds.
- A company is offering a loyalty points wallet that accumulates and can be redeemed as currency — this may constitute a stored value facility requiring a license.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Company name and entity type | The terms identify the regulated entity | Ask the user |
| Jurisdiction of operation and regulatory license | Determines mandatory content and consumer protections | Ask the user |
| Wallet type (fiat e-money / crypto / loyalty points / multi-currency) | Different rules apply to different wallet types | Ask the user |
| Customer types (consumer / SME / both) | Consumer protection obligations are higher for retail consumers | Ask the user |
| Funding methods (bank transfer / card / cash deposit / crypto) | Must be disclosed with associated fees and limits | Ask the user |
| Whether the wallet is custodial (company holds funds) or non-custodial | Determines safeguarding obligations | Ask the user |

## Optional inputs

- Transaction limits (per transaction / daily / monthly).
- Fee schedule details.
- Whether the wallet supports cross-border payments or remittances (adds licensing and FX considerations).
- Whether the wallet is linked to a debit card, virtual card, or physical card.
- Whether the company is part of a regulated banking group.

## Document structure

### 1. Introduction and parties
- Full legal name of the wallet operator, jurisdiction of incorporation, regulatory license number and type, and regulator name.
- The agreement is between the wallet operator ("we"/"us"/"Company") and the user ("you").
- Effective date.
- Statement that by registering, the user agrees to these terms.
- Minimum age (typically 18+; CBUAE rules and most MENA jurisdictions require adults for financial products).

### 2. Regulatory disclosures (mandatory for regulated entities)
Depending on the jurisdiction, include:

**UAE (CBUAE Stored Value Facility):**
- The wallet is a Stored Value Facility (SVF) licensed by the Central Bank of the UAE under the Payment Systems and Services Regulation.
- Funds held in the wallet are not bank deposits and are not covered by the UAE Deposit Guarantee Scheme.
- Funds are safeguarded in accordance with CBUAE SVF requirements (segregated client account or equivalent safeguarding).

**UAE (DIFC):**
- The wallet is regulated by the Dubai Financial Services Authority (DFSA) under a [Category X] license.
- DIFC Client Money Rules apply.

**UAE (ADGM):**
- The wallet is regulated by the FSRA under the Financial Services and Markets Regulations.

**KSA (SAMA):**
- The wallet is licensed by the Saudi Arabian Monetary Authority under the Payment Services Regulations.
- Funds held in the wallet are segregated from the company's own funds.

**EU (PSD2):**
- The wallet is an Electronic Money Institution (EMI) licensed under PSD2 in [member state]; funds are safeguarded per PSD2 Art. 7.

**UK:**
- The wallet is a regulated e-money product authorised by the FCA.

### 3. Account setup and eligibility
- Eligibility requirements: age, country of residence, and confirmation that the user is not subject to sanctions.
- Identity verification: mandatory KYC before wallet activation; documents required (ID, proof of address, source of funds for high-value use).
- Account types: personal vs. business; standard vs. premium.
- One wallet per user (unless the product design permits multi-wallet).

### 4. Funding the wallet
- Accepted funding methods: bank transfer (IBAN), debit card, credit card, cash deposit (if applicable), crypto (if applicable).
- Minimum and maximum deposit amounts.
- Processing times for each method.
- Fees associated with funding (if any; many wallets offer free bank transfer but charge for card funding).
- **Currency:** State the default currency and whether multi-currency is supported.
- **FX rates:** If conversion is involved, state how the exchange rate is determined and any spread or FX fee applied.

### 5. Transaction limits
Publish limits clearly — ambiguity on limits is a frequent source of customer complaints and regulator scrutiny:

| Limit type | Standard tier | Verified tier | Business tier |
|---|---|---|---|
| Per transaction (send/receive) | [Amount] | [Amount] | [Amount] |
| Daily | [Amount] | [Amount] | [Amount] |
| Monthly | [Amount] | [Amount] | [Amount] |
| Maximum balance | [Amount] | [Amount] | [Amount] |

These limits must comply with applicable AML regulations. CBUAE SVF Regulation specifies tiered limits for different KYC levels.

### 6. Sending and receiving funds
- How to send: by mobile number / email / account number / QR code.
- Processing time: real-time vs. T+1.
- Irrevocability: once a payment is processed, it cannot be reversed unless the recipient consents or the company has grounds to intervene (fraud, error).
- Error and misdirected payments: procedure for reporting and recovering misdirected payments (note: recovery is not guaranteed; the company will make reasonable efforts).

### 7. Withdrawals
- Methods: bank transfer, debit card, cash withdrawal (if ATM-linked).
- Processing times.
- Minimum withdrawal amounts.
- Fees (if any).
- Right to request refund of the e-money balance at any time (mandated by PSD2 and equivalent regulations); state any fees for redemption.

### 8. Security features
- Two-factor authentication (2FA): required for registration and high-value transactions; state the method (SMS OTP / authenticator app / biometric).
- PIN / password requirements.
- Device binding: the wallet may be restricted to registered devices.
- Transaction notifications: real-time push notifications for every transaction (this is both a user experience feature and a fraud-detection enabler).
- User's security responsibilities: keep credentials confidential; report lost or compromised devices immediately.

### 9. Unauthorized transactions and liability

This section is heavily regulated in jurisdictions with consumer protection for payment services:

**EU (PSD2) and UK:**
- User is liable for unauthorized transactions only up to EUR/GBP 50 (standard) unless the user acted fraudulently or with gross negligence.
- The company must reimburse unauthorized transactions immediately pending investigation.

**UAE (CBUAE):**
- CBUAE Consumer Protection Regulation requires that unauthorized transactions are investigated promptly; reimburse pending investigation for consumer accounts.

**KSA (SAMA):**
- SAMA consumer protection rules apply; zero-liability for genuinely unauthorized transactions subject to timely notification.

**General approach:**
- The user must report unauthorized transactions as soon as they become aware (and in any event within [30/60] days of the statement date).
- The company will investigate and respond within [X] business days.
- If the unauthorized transaction is confirmed, the company will reimburse the amount (subject to any applicable deductible or liability cap).
- If the user contributed to the unauthorized transaction by negligently disclosing their credentials, the liability cap may not apply.

### 10. Fees
- Complete fee schedule as a table.
- State clearly whether fees are charged at point of transaction, at end of month, or on a different basis.
- No undisclosed fees — any fee not in the terms is not enforceable and is a regulatory violation.
- Right to change fees: provide 30 days' advance notice for fee increases; users who do not accept new fees may close the wallet and withdraw their balance.

### 11. Suspension and closure

**Company's right to suspend:**
- Suspected fraud, money laundering, or unauthorized use.
- Regulatory requirement.
- Technical maintenance (with advance notice where possible).

**Company's right to close:**
- Repeated breach of terms.
- Negative balance.
- Regulatory requirement.
- Company decision to discontinue the product (with [90] days' notice to users to withdraw funds).

**User's right to close:**
- At any time, subject to zero balance.
- Process: submit closure request; company closes the account and returns any remaining balance within [5–10] business days.

**Effect of closure:**
- All pending transactions are cancelled.
- Remaining balance is returned to the user (by bank transfer or as specified).
- Transaction history is retained per the data retention policy.

### 12. Data protection and privacy
- The company collects personal data as described in the Privacy Policy [link].
- Data is processed for: account management, transaction processing, KYC/AML compliance, fraud prevention, and (with consent) marketing.
- Cross-border transfers: if data is processed outside the user's jurisdiction, state the safeguard (SCCs, adequacy decision, etc.).

### 13. Dispute resolution
- Internal complaints process: user contacts customer support; complaint acknowledged within [2] business days; resolved within [15] business days.
- Regulatory complaint: user may escalate to the applicable regulator (CBUAE, SAMA, DFSA, ADGM FSRA, FCA) if the internal resolution is unsatisfactory.
- Dispute resolution: for contractual disputes, specify arbitration (preferred) or litigation and the governing jurisdiction.
- **Consumer arbitration note:** Mandatory arbitration clauses in consumer contracts are unenforceable in some EU jurisdictions and are restricted in the UK; retain the consumer's right to seek judicial remedy.

### 14. Governing law
State the governing law clearly. For MENA-based wallets, consider:
- DIFC or ADGM as the governing law and jurisdiction for a common-law framework, English language, and access to experienced commercial courts.
- UAE federal law for a UAE-only consumer product.
- KSA law for Saudi domestic products.

## Jurisdictional licensing summary

| Jurisdiction | License type | Regulator | Key consumer protection rules |
|---|---|---|---|
| UAE (onshore) | Stored Value Facility (SVF) | CBUAE | CBUAE Consumer Protection Regulation; tiered KYC limits |
| UAE (DIFC) | Authorised Firm (Payment Services) | DFSA | DFSA Client Money Rules; DIFC Employment and Consumer Protection |
| UAE (ADGM) | Regulated Activity (Payment Services) | FSRA | FSRA Client Money Rules |
| KSA | Payment Service Provider | SAMA | SAMA Consumer Protection Principles; e-wallet regulations |
| EU | Electronic Money Institution | National CB / EBA | PSD2; consumer protection; zero-liability for unauthorized transactions |
| UK | Authorised EMI | FCA | FCA Payment Services Regulations 2017; consumer protection |

## Common mistakes

- Terms that do not identify the regulatory license — non-disclosure is a regulatory violation in all licensed jurisdictions.
- Unauthorized transaction liability that exceeds the regulatory cap — this is the most common consumer complaint trigger in e-wallet products.
- Fee schedule that is incomplete or buried in the general terms — fees must be prominently disclosed.
- No clear account-closure process or withdrawal procedure — customers need to know how to get their money out.
- Data processing section that does not address the Travel Rule (for cross-border payment wallets) — mandatory disclosure under UAE, EU, and UK AML frameworks.

## Related skills

- [[prompt-pack-cryptocurrency-exchange-terms]]
- [[prompt-pack-cross-border-payment-compliance-review]]
- [[prompt-pack-data-processing-agreement]]
- [[prompt-pack-privacy-policy]]
- [[prompt-pack-aml-compliance-program]]

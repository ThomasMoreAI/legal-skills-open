---
name: prompt-pack-cryptocurrency-exchange-terms-sboghossian
title: Cryptocurrency Exchange Terms
description: 'Use when a crypto exchange or virtual asset service provider (VASP) needs to draft Terms of Service covering account registration, KYC/AML requirements, trading rules, asset custody, security measures, withdrawal limits, fee structure, risk disclosures, and regulatory compliance. MENA-aware: covers UAE (VARA, DIFC, ADGM), KSA (SAMA sandbox), Bahrain (CBB), Qatar (QFC), and also EU (MiCA), UK (FCA), and global FATF VASP framework.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-cryptocurrency-exchange-terms
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Cryptocurrency Exchange Terms

Terms of Service for a crypto exchange are both a commercial contract and a regulatory compliance instrument. Under UAE (VARA), EU (MiCA), and UK (FCA) frameworks, the terms must address specific mandatory disclosures; non-compliant terms can result in license conditions, customer claims, and regulatory enforcement.

## When to use this

- A crypto exchange or VASP is launching in a new jurisdiction and needs jurisdiction-compliant Terms of Service.
- An existing exchange needs to update its terms following regulatory changes (MiCA implementation, VARA requirements, FATF VASP guidance updates).
- A company is expanding from an offshore/unregulated model to a regulated model and needs to upgrade its legal documentation.
- An M&A due diligence exercise requires assessment of the target exchange's terms compliance.
- A user dispute has arisen and the exchange's terms are being scrutinised by a regulator or court.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Exchange name and jurisdiction of incorporation | Determines which regulatory framework applies | Ask the user |
| Regulatory status (licensed / registered / sandbox / unregulated) | Mandatory disclosures differ materially by status | Ask the user |
| Types of virtual assets supported | Different rules may apply to different asset types (utility tokens, payment tokens, securities tokens, NFTs) | Ask the user |
| Services offered (spot / derivatives / staking / lending / custody) | Each service type may require separate licensing and disclosures | Ask the user |
| Customer types served (retail / professional / institutional) | Consumer protection obligations are higher for retail | Ask the user |
| Jurisdictions of customers | Geo-blocking and applicable law per user location | Ask the user |

## Optional inputs

- Whether the exchange is non-custodial or custodial.
- Whether a separate custody / safekeeping agreement is used alongside the terms.
- Whether the exchange offers fiat on-ramp/off-ramp (adds payment licensing complexity).
- Specific risk disclosures required by the applicable regulator.

## Document structure

### 1. Preamble and acceptance
- Identity of the exchange operator (full legal name, jurisdiction, registration number, regulatory license reference).
- Statement that by using the platform, the user agrees to these terms.
- Age/eligibility requirement (typically 18+; in UAE VARA framework, 21+ for certain services).
- Confirmation that the terms form a binding legal contract.
- Last updated date and version number.

### 2. Account registration and eligibility
- KYC requirements: mandatory identity verification before trading; documentation required (passport, proof of address, source of funds for high-value users).
- Eligibility restrictions: list jurisdictions from which users are excluded (OFAC sanctioned countries, jurisdictions where the exchange is not licensed). This is critical for regulatory compliance and must be actively enforced by geo-blocking and IP filtering.
- Account types: individual vs. corporate; professional vs. retail (with different trading limits and disclosures for each).
- One account per user policy.
- Responsibility for account credentials.

### 3. KYC, AML, and regulatory compliance
- User consent to KYC verification (document submission, identity verification, source of funds enquiry).
- Enhanced Due Diligence (EDD) trigger: for users above defined transaction thresholds or classified as high risk.
- AML obligations: the exchange may freeze accounts, refuse withdrawals, or report transactions to the relevant FIU without notice to the user if required by applicable law.
- **FATF Travel Rule:** For transactions above USD/EUR 1,000 (or lower thresholds under national law), the exchange must collect and transmit originator and beneficiary information. This is now implemented in UAE (CBUAE and VARA), EU (TFR Regulation), and progressively across MENA. State the exchange's Travel Rule compliance mechanism.
- User's obligation to provide accurate information; account suspension for misrepresentation.

### 4. Supported virtual assets
- List of supported assets (or reference to a dynamic list on the platform).
- Statement that the exchange may add or remove assets at any time and the basis for doing so (regulatory status, security, liquidity).
- Classification: the exchange should state whether each asset is a utility token, payment token, or whether any asset constitutes a security or investment product. If a security, the exchange must have appropriate securities licensing.
- Disclaimer: listing of an asset does not constitute investment advice or endorsement.

### 5. Trading rules
- Order types available (market, limit, stop-loss, etc.).
- Matching engine and order execution policy.
- Slippage policy for market orders.
- Circuit breakers and trading halt conditions.
- Order cancellation policy.
- Self-trading prohibition (prevention of wash trading).

### 6. Custody and asset security
- **Custodial model:** The exchange holds private keys; users have a contractual claim to their assets but do not hold the assets directly. This is the dominant model for centralized exchanges.
- **Segregation:** Client assets are held separately from the exchange's proprietary assets. This is required under UAE VARA VASPR rules, MiCA Art. 70, and UK FCA crypto asset guidance.
- **Cold/hot wallet split:** State the proportion held in cold storage (offline, more secure) vs. hot wallets (online, accessible for withdrawals).
- **Insurance:** Describe any insurance coverage for digital assets. Note that insurance for crypto assets is limited and expensive; describe coverage accurately.
- **Proof of reserves:** Many exchanges now publish periodic proof-of-reserves audits; reference this if applicable.
- **Insolvency:** Describe how client assets are treated in the event of the exchange's insolvency. Under VARA and MiCA, segregated client assets should not be available to creditors; state this explicitly. This is a key trust point for sophisticated users post-FTX.

### 7. Fees
- Trading fees: maker/taker fee schedule; volume discounts.
- Withdrawal fees: by asset and network.
- Deposit fees: typically zero for crypto deposits; may apply for fiat on-ramp.
- Inactivity fees (if applicable): must be clearly disclosed.
- How and when fees are charged.
- Right to change fees with notice to users (state notice period; material fee changes typically require 30 days' notice to retain user trust and comply with consumer protection frameworks).

### 8. Withdrawal and deposit terms
- Minimum and maximum withdrawal limits (by asset and by time period).
- Processing times and conditions for delays.
- Verification requirements for large withdrawals.
- AML freeze: the exchange may delay withdrawals pending AML review.
- Network confirmation requirements: state how many on-chain confirmations are required before a deposit is credited.

### 9. Risk disclosures
Mandatory in virtually all regulatory frameworks and essential as a matter of good practice:
- Crypto assets are highly volatile; users may lose all their investment.
- Crypto assets are not legal tender and are not backed by any government or central bank.
- The regulatory status of crypto assets is uncertain and may change.
- The exchange's services may be suspended due to regulatory action, cybersecurity incidents, or technical failures.
- Past performance is not indicative of future results.
- **Jurisdiction-specific disclosures:** UAE VARA requires specific risk disclosures in the licence conditions; MiCA Art. 51 requires a white paper for crypto-asset service providers.

### 10. Security
- User's responsibility to maintain account credentials and 2FA.
- Exchange's security measures (SSL, 2FA requirement, penetration testing).
- Unauthorized access: the exchange's liability for losses from unauthorized access resulting from the user's failure to secure their credentials.
- Notification obligation: user must report unauthorized access immediately.

### 11. Prohibited activities
Non-exhaustive list:
- Use of the platform for money laundering, terrorist financing, or sanctions evasion.
- Market manipulation (wash trading, spoofing, pump-and-dump).
- Use of bots or automated trading systems in violation of the terms.
- Access from prohibited jurisdictions.
- Impersonation of other users.
- Any violation of applicable law.

Consequences: account suspension, asset freeze, and reporting to relevant authorities.

### 12. Liability and indemnification
- Exchange's liability cap: typically limited to the fees paid by the user in the prior 12 months; excludes consequential, indirect, and speculative losses.
- Force majeure: blockchain network failures, regulatory actions, cybersecurity incidents, extreme market conditions.
- User indemnification: the user indemnifies the exchange against claims arising from the user's own breach of the terms or applicable law.

### 13. Governing law and dispute resolution
- Choice of governing law — select a jurisdiction with a developed crypto regulatory framework. Recommended options: DIFC or ADGM for MENA-based exchanges (English law; experienced courts; clear VASP regulatory framework); Singapore; Cayman Islands.
- Dispute resolution: arbitration (DIAC, DIFC LCIA, SIAC, or ICC depending on jurisdiction) is recommended over litigation for an international user base.
- Class action waiver (enforceable in common-law jurisdictions including DIFC and ADGM; not effective in all EU member states).

### 14. Amendments
- Exchange's right to amend the terms with notice.
- Notice period: typically 30 days for material changes; shorter for changes required by law or regulators.
- Continued use constitutes acceptance of amendments; users who disagree may close their account.

## Jurisdictional regulatory context

| Jurisdiction | Regulatory framework | Key requirements |
|---|---|---|
| UAE (VARA) | Virtual Assets Regulatory Authority; Virtual Asset Service Providers Regulation (VASPR) 2023 | License required; mandatory disclosures; segregation of client assets; Travel Rule; whitepaper for asset issuance |
| UAE (DIFC) | DFSA; Digital Assets regime effective 2023 | Category 4 license for trading platforms; comprehensive rulebook; DIFC courts jurisdiction |
| UAE (ADGM) | FSRA; Spot Commodity framework and Virtual Assets Framework | License required; ADGM Courts jurisdiction |
| KSA | SAMA; Capital Markets Authority (CMA) | SAMA FinTech sandbox; no general crypto exchange license as of 2026; caution required |
| Bahrain | Central Bank of Bahrain (CBB) | CBB Module CRA (Crypto-Asset Module); license required |
| Qatar (QFC) | QFC Regulatory Authority | QFC Digital Assets Framework |
| EU | European Banking Authority (EBA) / ESMA | MiCA (Markets in Crypto-Assets Regulation), effective 2024; white paper requirement; license per service type |
| UK | FCA | Crypto asset firm registration; specific requirements for exchange and custody services |

## Common mistakes

- Terms that do not identify the regulatory license and registration number — this is a red flag for regulators and users.
- Inadequate or no Travel Rule compliance mechanism — non-compliance is an AML violation.
- Asset custody terms that do not address insolvency — post-FTX, sophisticated users and regulators scrutinise this closely.
- Blanket class action waivers that are unenforceable in the governing jurisdiction.
- Terms that permit the exchange to change fees without notice — this triggers consumer protection exposure.
- Not geo-blocking and not stating exclusion jurisdictions — the exchange is then operating in markets where it is unlicensed.

## Related skills

- [[prompt-pack-digital-wallet-terms]]
- [[prompt-pack-cross-border-payment-compliance-review]]
- [[prompt-pack-data-processing-agreement]]
- [[prompt-pack-aml-compliance-program]]
- [[prompt-pack-privacy-policy]]

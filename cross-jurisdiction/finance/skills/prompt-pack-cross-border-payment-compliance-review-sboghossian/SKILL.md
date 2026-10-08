---
name: prompt-pack-cross-border-payment-compliance-review-sboghossian
title: Cross-Border Payment Compliance Review
description: 'Use when a FinTech or payments company needs a compliance review of its cross-border payment operations covering licensing requirements, sanctions screening, FX regulations, correspondent banking relationships, and regulatory reporting obligations across specified jurisdictions. MENA-aware: UAE (CBUAE, DFSA, ADGM FSRA), KSA (SAMA), LB (BdL), EG (CBE), Qatar (QCB); also covers FATF framework, SWIFT messaging standards, and US/EU sanctions regimes with extraterritorial reach.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-cross-border-payment-compliance-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: finance
language: en
---

# Cross-Border Payment Compliance Review

Cross-border payments are subject to overlapping and sometimes conflicting regulatory frameworks — domestic licensing, sanctions, AML/CFT obligations, FX controls, and prudential requirements — all of which must be navigated simultaneously. A compliance review produces a structured analysis of what the company must have in place in each jurisdiction it touches.

## When to use this

- A FinTech or payments company is launching a cross-border payment product and needs to map its regulatory obligations.
- An existing payments business is expanding into new MENA jurisdictions and needs to understand new licensing and compliance obligations.
- A correspondent banking relationship has been terminated ("de-risking") and the company needs to understand the compliance gaps that triggered it.
- A regulatory examination or AML audit is imminent and the company needs a gap analysis.
- A company is acquiring a payments business and conducting regulatory due diligence.
- An investor is conducting due diligence on a FinTech payments company and needs a compliance risk assessment.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Company's jurisdictions of operation | Determines which licensing and regulatory frameworks apply | Ask the user to list all countries where the company is registered or operates |
| Payment types handled | Different payment types attract different licensing requirements (remittance, merchant acquiring, e-money, SWIFT transfers) | Ask the user |
| Customer types (B2B / B2C / mixed) | B2C retail payments attract stricter consumer protection obligations | Ask the user |
| Jurisdictions of counterparties / beneficiaries | Determines sanctions screening obligations and FX regulation | Ask the user |
| Volume and value of transactions | Thresholds trigger reporting obligations (e.g., CBUAE cash transaction reports above AED 40,000) | Ask the user |

## Optional inputs

- SWIFT BIC and correspondent banking relationships.
- Whether the company processes payments for high-risk sectors (gambling, crypto, high-value goods).
- Whether the company offers crypto-linked or virtual asset payment services.
- Existing AML/CFT program documentation.
- Whether the company is seeking to list or has institutional investors with compliance requirements.

## Compliance review framework

### 1. Licensing analysis

For each jurisdiction of operation, assess:

| Jurisdiction | Regulator | Relevant license / registration | Key threshold |
|---|---|---|---|
| UAE (onshore) | Central Bank of UAE (CBUAE) | Payment Service Provider (PSP) license; Stored Value Facility (SVF) license | Mandatory for any entity providing payment services to UAE customers |
| UAE (DIFC) | DFSA | Money Services license; Arranging Credit / Payment Services license | Required for DIFC-based entities providing payment services |
| UAE (ADGM) | FSRA | Regulated Activity: Operating a Payment System or Providing Money Services | Required for ADGM-based entities |
| KSA | Saudi Arabian Monetary Authority (SAMA) | Fintech license; Payment Service Provider registration; SAMA approval for foreign remittance | SAMA issued a FinTech regulatory sandbox framework; full licensing for live operations |
| Lebanon | Banque du Liban (BdL) | Payment institution registration | BdL Basic Circular No. 81 and supplementary circulars govern licensed financial institutions |
| Egypt | Central Bank of Egypt (CBE) | Payment Services and Banking Technology License | CBE Decree No. 48 of 2022 governs FinTech licensing |
| Qatar | Qatar Central Bank (QCB) | Payment Service Provider license | QCB FinTech and payment regulations |
| EU | National competent authorities + EBA oversight | PSD2 license (Payment Institution / E-Money Institution); passporting across EU | Markets must be licensed per country if no passport |
| UK | FCA | Authorised Payment Institution or Small Payment Institution | FCA Handbook applies |

**Key licensing trap:** Operating cross-border payment services without a license in the destination jurisdiction — even if licensed in the origin jurisdiction — is a common violation. MENA regulators are increasingly assertive on unlicensed activity by foreign FinTechs.

### 2. AML/CFT compliance

**FATF framework:** All MENA GCC countries are FATF members or MENAFATF members. The FATF 40 Recommendations apply; the risk-based approach is mandatory.

**Core AML obligations for payment companies:**
- Customer Due Diligence (CDD): collect and verify identity for all customers above the relevant threshold; Enhanced Due Diligence (EDD) for high-risk customers.
- Beneficial ownership identification for corporate customers.
- Ongoing transaction monitoring: automated systems to detect unusual patterns.
- Suspicious Transaction Reports (STRs): file with the relevant Financial Intelligence Unit (FIU) — UAE Financial Intelligence Unit (UAEFIU), SAMA AML Center in KSA, Special Investigation Commission (SIC) in Lebanon.
- Cash transaction reporting: report cash transactions above specified thresholds.
- Record-keeping: minimum 5 years for transaction records and CDD documents.

**MENA-specific AML requirements:**

| Jurisdiction | FIU / Filing body | STR filing obligation | Key AML law |
|---|---|---|---|
| UAE | UAE FIU (goaml.ae) | All UAE-licensed entities | Federal Decree-Law No. 20 of 2018; Cabinet Decision No. 10 of 2019 |
| KSA | SAMA AML Center | Licensed financial institutions | AML Law (Royal Decree M/31, 2003 as amended) |
| Lebanon | Special Investigation Commission (SIC) | Licensed banks and financial institutions | Law No. 318 of 2001; Lebanon is subject to enhanced monitoring as of FATF 2023 |
| Egypt | Egyptian Money Laundering Combating Unit (EMLCU) | Licensed entities | AML Law No. 80 of 2002 |

### 3. Sanctions screening

**US OFAC:** Any payment that touches the US financial system (USD correspondent bank, US-incorporated entity in the payment chain) is subject to OFAC sanctions. OFAC SDN list screening is mandatory. Penalties for violations are severe — up to USD 1 million per violation for civil violations, criminal penalties for intentional violations. OFAC's reach is extraterritorial: any payment denominated in USD that clears through a US correspondent bank is within OFAC jurisdiction.

**EU sanctions:** Apply to EU entities and transactions in EUR.

**UN sanctions:** Implemented by all UN member states.

**UAE/KSA sanctions:** Both maintain national sanctions lists in addition to UN implementation. UAE: CBUAE maintains an NST (National Sanctions Table). KSA: Saudi Targeted Financial Sanctions list.

**Screening obligations:**
- Screen all parties (sender, beneficiary, intermediaries, beneficial owners) against applicable sanctions lists before processing each transaction.
- Use automated screening software with up-to-date list feeds.
- Implement a "block and freeze" process for hits.
- Maintain screening records for the regulatory retention period.

**Lebanon warning:** Lebanon is subject to enhanced scrutiny. Any payments involving Lebanese entities should be subject to enhanced sanctions screening and AML checks; correspondent banks routinely apply heightened scrutiny.

### 4. FX regulations

| Jurisdiction | FX regime | Key restrictions |
|---|---|---|
| UAE | Managed float against USD; free convertibility | No exchange controls; remittances unrestricted; reporting required for large FX transactions |
| KSA | Fixed peg to USD; free convertibility | No exchange controls; SAMA reporting for large transactions |
| Lebanon | Multiple exchange rates; capital controls since 2019 | Sayrafa platform and informal market; complex restrictions on USD transfers out of Lebanon; BdL circulars govern |
| Egypt | Managed float; periodic exchange rate adjustments | CBE FX regulations; limits on USD withdrawal; import payment restrictions have been relaxed but remain subject to CBE oversight |
| Qatar | Fixed peg to USD | Free convertibility; no material restrictions |

**Lebanon FX risk:** The Lebanese pound has lost over 90% of its value since 2019. BdL has issued multiple conflicting circulars on USD transfers, Lollar accounts (Lebanese USD), and the Sayrafa exchange platform. Any payment operation involving Lebanese entities requires up-to-date local counsel advice.

### 5. Correspondent banking

Correspondent banking relationships are critical for cross-border USD, EUR, and GBP payments. De-risking (termination of correspondent relationships) is a significant risk for MENA payment companies, particularly those operating in jurisdictions with high-risk AML profiles.

**Key obligations to maintain correspondent relationships:**
- Clear ownership and control structure; no opaque UBO structures.
- Robust AML program with documented policies and procedures.
- Adequate technology for transaction screening and monitoring.
- Prompt STR filing history and cooperation with regulatory inquiries.
- Compliance with SWIFT's Know Your Customer Registry (KYC Registry) requirements.

**Wolfsberg Principles:** The Wolfsberg Group principles for correspondent banking and payment transparency (including SWIFT gpi requirements) are the industry standard. Payment companies should be familiar with the Payment Transparency Standards and the Wolfsberg AML Questionnaire.

### 6. Regulatory reporting

| Report type | Trigger | Filing body |
|---|---|---|
| Suspicious Transaction Report (STR) | Any reasonable grounds to suspect money laundering or terrorist financing | National FIU |
| Large Cash Transaction Report | Cash transaction above jurisdiction threshold (e.g., AED 40,000 in UAE) | CBUAE / relevant regulator |
| Cross-border wire transfer reporting | Outbound transfers above threshold | Central bank in most MENA jurisdictions |
| Annual compliance report | Licensed entity annual filing | Licensing authority |
| Consumer complaints report | As required | Licensing authority |

## Output format

Deliver a compliance review report structured as:
1. **Executive summary:** Key findings, compliance gaps, and priority remediation steps.
2. **Licensing gap analysis:** For each jurisdiction, what is required vs. what is in place.
3. **AML/CFT gap analysis:** Comparison of current program against regulatory requirements.
4. **Sanctions screening assessment:** Systems, coverage, and gaps.
5. **FX regulatory assessment:** For each relevant jurisdiction.
6. **Correspondent banking assessment:** Current relationships, de-risking risk, and mitigation.
7. **Action plan:** Prioritised list of remediation steps with responsible owner and deadline.

## Common mistakes

- Operating in a new country without checking whether a separate license is required (assuming home-country license suffices).
- USD payment processing without robust OFAC screening — the CBUAE and US Treasury have both taken enforcement action.
- Ignoring the Lebanon FX situation and processing payments at official rates when the actual rate is materially different — this creates undisclosed losses and potential regulatory exposure.
- Inadequate correspondent banking maintenance — de-risking destroys operational capability; preventive compliance investment is much cheaper than relationship rebuilding.

## Related skills

- [[prompt-pack-cryptocurrency-exchange-terms]]
- [[prompt-pack-digital-wallet-terms]]
- [[prompt-pack-data-processing-agreement]]
- [[prompt-pack-aml-compliance-program]]
- [[prompt-pack-client-intake-form]]

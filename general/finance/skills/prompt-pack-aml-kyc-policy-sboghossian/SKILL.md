---
name: prompt-pack-aml-kyc-policy-sboghossian
title: AML/KYC Policy
description: Use when drafting an AML/KYC policy for a fintech company or financial institution, covering customer identification, risk assessment, ongoing monitoring, suspicious activity reporting, record-keeping, and regulatory filing obligations. Applies to MENA jurisdictions (UAE, KSA, EG, DIFC, ADGM) and globally, with particular attention to FATF 40 Recommendations and jurisdiction-specific AML regimes.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-aml-kyc-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# AML/KYC Policy

## When to use this

Use this skill when a fintech company or financial institution needs a formal AML/KYC policy to:
- Comply with licensing requirements from a financial regulator
- Satisfy correspondent banking due diligence
- Establish internal controls for money laundering and terrorist financing prevention
- Document compliance with FATF standards

This skill is particularly relevant for:
- Fintech startups preparing for CBUAE, SAMA, DFSA, FSRA, or ADGM FSRA licensing
- E-money institutions, payment service providers, crypto asset service providers, and lending platforms
- Established financial institutions updating their AML framework after a regulatory examination

---

## Prompt template

> Draft an AML/KYC policy for [FinTech Company] operating in [jurisdiction]. Cover customer identification, risk assessment, ongoing monitoring, suspicious activity reporting, record keeping, training requirements, and regulatory filing obligations.

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before drafting.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Company name and business model | Determines risk appetite and applicable thresholds (e-money vs. crypto vs. lending vs. payments have different risk profiles) |
| Jurisdiction(s) of operation and licensing | Determines the specific AML regulatory framework (CBUAE vs. DFSA vs. SAMA etc.) |
| Customer types | Consumer vs. business customers have different CDD requirements |
| Transaction volumes and typical transaction size | Risk-rating thresholds depend on actual volumes |
| Existing compliance infrastructure | New build vs. update to existing policy |

---

## Document structure

### 1. Policy purpose and scope
- Business description and AML risk context
- Legal and regulatory basis: the applicable AML law and regulations
- Scope: who is covered (all employees, agents, outsourced service providers)
- Policy owner (typically MLRO — Money Laundering Reporting Officer)

### 2. Regulatory framework

Key applicable frameworks by jurisdiction:

| Jurisdiction | Primary AML law | Regulator | FATF member |
|-------------|----------------|-----------|-------------|
| UAE (onshore) | AML/CFT Law Federal Decree-Law 20/2018; Cabinet Decision 10/2019 | CBUAE (banking), MOE (DNFBPs) | Yes (FATF) |
| DIFC | DIFC AML/CFT Law (DIFC Law No. 1 of 2017 as amended); DFSA AML Module | DFSA | Yes (FATF via UAE) |
| ADGM | ADGM AML/CFT Regulations; FSRA AML Rules | ADGM FSRA | Yes (FATF via UAE) |
| KSA | AML Law (Royal Decree M/31/2003 as amended); CFT Law | SAMA (financial institutions); FATF member | Yes |
| Egypt | AML Law No. 80/2002 as amended; CBE regulations | CBE; EFSA | Yes (FATF) |
| Lebanon | AML Law No. 44/2015; Banque du Liban circulars | SIC (Special Investigation Commission) | MENAFATF member |

All frameworks follow FATF 40 Recommendations as the baseline standard.

### 3. Customer due diligence (CDD)

#### 3.1 Standard CDD — natural persons
Minimum identification requirements:
- Full legal name (as on government-issued ID)
- Date and place of birth
- Nationality and country of residence
- Occupation
- Government-issued ID (passport, national ID, residency permit): number, expiry, issuing authority
- Address (residential and/or correspondence)
- Source of funds (for higher-risk customers or transactions above threshold)
- Source of wealth (for PEPs and high-risk customers)

Verification methods: physical ID check; eKYC (permitted in UAE, KSA, DIFC for regulated entities); certified copies for non-face-to-face onboarding.

#### 3.2 Standard CDD — legal entities
- Full legal name and trading name
- Jurisdiction of incorporation and registration number
- Registered address and principal place of business
- Certificate of incorporation / commercial registration
- Articles of association
- Identification of **beneficial owners** (UBO): individuals who own or control 25% or more (some jurisdictions: 10%) of the entity, and the natural persons who exercise ultimate effective control
- Director identification

UAE: UBO information must be registered with the relevant authority (Ministry of Economy or free zone) under Cabinet Resolution 58/2020 on UBO.

#### 3.3 Enhanced due diligence (EDD)
Apply EDD when:
- Customer is a Politically Exposed Person (PEP) or close associate/family member of a PEP
- Customer or transaction involves a high-risk jurisdiction (FATF grey or black list; company jurisdiction is a secrecy jurisdiction)
- Transaction type is inherently high-risk (large cash; correspondent banking; cross-border wire to high-risk jurisdiction; crypto asset transactions)
- Customer is a legal entity with complex or opaque ownership structure

EDD requires:
- Senior management approval for onboarding
- Source of wealth documentation and verification
- Enhanced ongoing monitoring (lower transaction thresholds for review)
- More frequent periodic review (at least annually vs. standard 2–3 years)

#### 3.4 Simplified due diligence (SDD)
Permitted only where risk is demonstrably low — typically for regulated financial institutions as customers (themselves subject to AML rules), listed companies on regulated exchanges, and government entities. Document the basis for SDD application.

### 4. Risk assessment and risk-rating

A written risk assessment is required by FATF and all MENA AML frameworks. The risk assessment must:
- Identify the money laundering and terrorist financing risks inherent in the business model
- Assess the residual risk after controls
- Be reviewed at least annually and on material business changes

Customer risk rating factors:
- Customer type (natural person / legal entity / PEP / high-risk business)
- Product/service used (cash-intensive / cross-border / crypto / trade finance)
- Geography (high-risk vs. standard vs. low-risk jurisdictions)
- Transaction behavior (patterns consistent with declared purpose?)

Risk categories: Low / Medium / High (define thresholds numerically where possible)

### 5. Ongoing transaction monitoring
- Define monitoring rules and thresholds per product type
- Automated transaction monitoring system: what rules are in force; who reviews alerts; escalation path for unresolved alerts
- Periodic review schedule: Low-risk customers: every 3 years; Medium: every 2 years; High: annually; PEPs: annually minimum
- Trigger events for ad-hoc review: adverse media; law enforcement inquiry; unusual transaction pattern; customer request for transaction outside declared purpose

### 6. Suspicious activity reporting (SAR/STR)
- Internal reporting: any employee who suspects money laundering or terrorist financing must report to the MLRO immediately (internal SAR form)
- MLRO review: assess within [X] business days; decide whether to file with the financial intelligence unit (FIU)
- External reporting:
  - UAE: report to goAML (FIU, part of CBUAE)
  - KSA: report to SAFIU (Saudi Financial Intelligence Unit) via goAML
  - Lebanon: report to the Special Investigation Commission (SIC)
  - Egypt: report to the Money Laundering Combating Unit (MLCU)
  - DIFC/ADGM: report to UAE FIU; notify DFSA/FSRA of material SAR filing
- **Tipping-off prohibition**: once an internal SAR is filed, do not alert the customer that a report has been made or is under consideration — this is a criminal offence in all MENA jurisdictions
- Freeze pending report: if transaction has not been executed, freeze pending MLRO decision

### 7. Record-keeping
- Customer identification records: minimum 5 years after end of customer relationship (UAE: 5 years; DIFC: 6 years; KSA: 10 years)
- Transaction records: same retention period as identification records
- SAR/STR records: retain for same period; protect from unauthorized access
- Training records: 3 years minimum
- Format: original documents or certified copies; electronic storage is permitted in most MENA jurisdictions with audit trail integrity requirements

### 8. Training obligations
- Initial training: all new employees before client-facing duties begin
- Annual refresher: all covered staff
- Enhanced training: MLRO, compliance team, customer-facing staff
- Content: AML/CFT obligations; red flags; internal reporting procedures; consequences of non-compliance
- Documentation: attendance records; assessment results; training materials

### 9. MLRO role and responsibilities
- Appoint a designated MLRO (Money Laundering Reporting Officer) and deputy
- MLRO requirements: senior; sufficient authority and resources; direct board access
- MLRO obligations: oversee AML programme; receive internal SARs; file external reports; produce annual AML report to board
- Regulatory notification: MLRO appointment must typically be notified to the regulator (DFSA: prior approval required; CBUAE: notification)

---

## Jurisdictional notes

### UAE: Virtual Asset Service Providers (VASPs)
UAE VASPs regulated by VARA (Virtual Assets Regulatory Authority) — Dubai, or by SCA (Securities and Commodities Authority) — federally. Both require an AML programme compliant with CBUAE guidance and FATF Recommendation 15 (travel rule).

### KSA
SAMA has issued detailed AML/CFT Rules (2021) for banks and finance companies. New fintech entrants must comply from day one of operations. The SAFIU reporting obligation is strict — fines for non-reporting are significant.

### DIFC
DFSA Sourcebook: AML Module (AML). The DFSA has taken enforcement action against firms with inadequate AML controls. CDD failures are a top enforcement priority.

---

## Common mistakes

- No written risk assessment — required by all MENA frameworks; a policy alone is not sufficient
- PEP screening not operationalized — having a policy requirement but no screening tool or process
- Tipping-off omission — policy does not address the prohibition on alerting customers
- No MLRO appointment or MLRO without sufficient authority or resources
- Record retention periods not jurisdiction-calibrated — 5-year UAE minimum vs. 10-year KSA minimum creates issues for firms operating in both

---

## Related skills

- [[prompt-pack-anti-money-laundering-policy]] — related policy for broader financial institution use
- [[kb-aml-mena]] — MENA AML/CFT law reference
- [[prompt-pack-bnpl-platform-agreement]] — BNPL product which carries AML obligations
- [[heuristic-always-state-jurisdiction-first]] — jurisdiction-first drafting

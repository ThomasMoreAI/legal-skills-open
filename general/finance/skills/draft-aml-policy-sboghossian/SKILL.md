---
name: draft-aml-policy-sboghossian
title: Draft — AML / KYC Policy
description: Use when asked to draft an Anti-Money Laundering (AML) and Know-Your-Customer (KYC) policy for a financial services or fintech business. Covers the mandatory components under FATF Recommendations and jurisdiction-specific frameworks (SAMA/KSA, UAE Federal, DFSA, ADGM/FSRA, DIFC, Lebanon BDL/SIC, EU 6AMLD, US BSA/FinCEN). P0 priority for regulated entities — incomplete AML policies are a regulatory enforcement trigger.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-aml-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Draft — AML / KYC Policy

## When to use this

Use this skill when:
- A regulated entity (bank, NBFI, payment service, fintech, crypto exchange, law firm, real estate agent) needs an AML/KYC policy to satisfy licensing conditions or regulatory audit.
- An existing policy requires updating after a regulatory change (new FATF guidance, local amendment).
- A new business line or product triggers fresh AML obligations.
- An annual policy review is due.

This is a P0 skill. Inadequate AML policies are among the most common triggers for regulatory enforcement action in MENA, EU, and US jurisdictions.

## Required inputs

| Input | Why it matters |
|---|---|
| Entity scope | Which group entities are covered; subsidiaries require separate policies or a consolidated group policy |
| Regulatory jurisdiction(s) | Determines the specific framework; FATF baseline + local overlay |
| Business model | Transaction types, customer types, geographies — these drive the risk-based approach |
| MLRO designation | Money Laundering Reporting Officer identity and reporting line |
| Customer segments | Retail, corporate, institutional, PEPs, VASPs (virtual asset service providers) |

## Mandatory components

### 1. Policy statement
A clear commitment from the Board of Directors (or equivalent governing body) to:
- Comply with applicable AML/CFT (Counter-Financing of Terrorism) laws.
- Maintain a risk-based compliance program.
- Allocate adequate resources to AML compliance.

The policy statement must be signed by the Board or senior management and dated.

### 2. MLRO appointment
- Full name, title, and contact information of the Money Laundering Reporting Officer (MLRO) — or equivalent role (Compliance Officer, Designated Compliance Function).
- Reporting line: MLRO reports directly to the Board or a Board Committee; must not report through a business line that generates revenue.
- Deputy MLRO: designate a deputy for absence/incapacity.
- MLRO authority: can refuse a transaction, file an STR, or escalate without commercial pressure.

### 3. Risk-based approach (RBA)
The RBA is the foundation of the FATF framework. The policy must describe:
- **Business-wide risk assessment (BWRA)**: identify and assess the ML/TF risks inherent in the entity's products, services, customers, delivery channels, and geographic exposure.
- **Customer risk categorization**: segment customers into Low, Medium, and High risk tiers with criteria for each.
- **Risk scoring model**: document the factors used (customer type, geography, product, transaction behavior, PEP status, sanctions exposure).
- Review cycle for the BWRA: at least annually and after any material change to business model.

### 4. Customer Due Diligence (CDD)

**Standard CDD** (all customers):
- Verify identity using reliable, independent documentary evidence.
- For individuals: government-issued photo ID (passport, national ID), date of birth, address.
- For entities: certificate of incorporation, memorandum/articles, register of directors, ultimate beneficial owner (UBO) identification.
- **UBO threshold**: 25% ownership or control is the FATF standard; some jurisdictions use 10% or 20% — verify local rule.
- Understand the nature and purpose of the business relationship.
- Obtain source of wealth for high-risk relationships.

**Simplified CDD**: available for demonstrably low-risk customers (listed companies on regulated exchanges, regulated financial institutions, government entities) — document the rationale.

**Ongoing CDD**: monitor the business relationship; update records when there is a material change; apply periodic review based on risk tier.

### 5. Enhanced Due Diligence (EDD)

EDD must be applied to:
- **Politically Exposed Persons (PEPs)** — current and former; domestic and foreign; including family members and close associates.
- **High-risk geographic jurisdictions** — FATF grey-listed or black-listed jurisdictions; jurisdictions with known ML/TF risk (update list at least quarterly).
- **Cash-intensive businesses** — money service businesses, real estate, precious metals/stones.
- **Virtual asset service providers (VASPs)** — additional obligations under FATF Recommendation 15 and jurisdictional VASP regimes (VARA in UAE, ADGM FSRA).
- **High-value transactions** — above a defined threshold (jurisdiction-specific; commonly $15,000 / equivalent for wire transfers).
- **Complex or unusual transaction structures**.

EDD measures include:
- Additional identity verification.
- Senior management approval for account opening.
- Source of funds and source of wealth documentation.
- Enhanced ongoing monitoring.

### 6. Ongoing transaction monitoring
- Systems and processes to monitor customer transactions for patterns inconsistent with the customer's risk profile and stated business.
- **Threshold-based alerts**: transaction amounts above defined limits trigger review.
- **Pattern-based alerts**: structuring (breaking large transactions into smaller amounts to avoid reporting thresholds), unusual geographic patterns, unusually rapid movement of funds.
- Alert review process: triage, investigation, escalation to MLRO.
- Monitoring should be both automated (transaction monitoring system) and manual (relationship manager observation).

### 7. Sanctions screening
- Screen all customers, beneficial owners, and counterparties against applicable sanctions lists.
- **Lists to screen**:
  - UN Security Council Consolidated List.
  - OFAC (US Specially Designated Nationals) — required for USD transactions and US-connected entities.
  - EU Consolidated List.
  - UK HM Treasury Sanctions List.
  - Local lists (UAE CBUAE list, KSA SAFIU list, Lebanese counterterrorism list, etc.).
- **Screening frequency**: at onboarding; at each transaction where feasible; daily batch screening for name-list changes.
- **Match handling**: documented escalation procedure; freeze assets and report where required; seek regulatory guidance on complex matches.
- **Sanctions violations are strict liability** in most jurisdictions — no mental element required.

### 8. Suspicious Activity Reports (SARs / STRs)
- **Filing obligation**: when the MLRO has knowledge or suspicion (or reasonable grounds for suspicion) that a transaction involves proceeds of crime or ML/TF.
- **Filing authority**: MLRO is the sole person authorized to file; staff report suspicions internally to MLRO.
- **Tipping-off prohibition**: it is a criminal offense in most jurisdictions to disclose to the subject that a SAR has been filed.
- **Jurisdiction-specific filing**:
  - UAE: goAML platform (Central Bank UAE).
  - KSA: Financial Investigation Unit (FIU), Saudi Ministry of Interior.
  - DIFC: DFSA.
  - ADGM: FSRA.
  - LB: Special Investigation Commission (SIC), Banque du Liban.
  - EU: national FIU of member state.
  - US: FinCEN via BSA e-filing.
- **Time limits**: typically 30 days from becoming aware of the suspicion; faster for urgent matters.

### 9. Record retention
- **Standard period**: 5 years from end of business relationship or transaction (FATF baseline).
- **Extended periods**: some jurisdictions require 7–10 years (verify local rule).
- **What to retain**: CDD documentation, transaction records, STR/SAR filings, correspondence, training records.
- Records must be retrievable within a reasonable time for regulatory inspection.

### 10. Staff training
- **Annual mandatory training**: all staff must complete AML/CFT training annually; records maintained.
- **Role-specific training**: front-line staff (onboarding, relationship management), compliance team, senior management.
- **New hire training**: AML training within first 30 days of employment.
- Training must cover: red flags, SAR filing procedure, tipping-off prohibition, sanctions, and the firm's specific risk profile.

### 11. Independent audit and testing
- Annual independent review of the AML program (internal audit or external third party).
- Testing should cover: CDD quality, transaction monitoring effectiveness, SAR filing completeness, sanctions screening accuracy, training records.
- Findings and management responses documented; tracked to remediation.

## Jurisdictional overlay — key specifics

| Jurisdiction | Primary framework | Key regulator | Notable requirements |
|---|---|---|---|
| **KSA** | AML Law (Royal Decree M/20 2003, amended) + SAMA Rules | SAFIU; SAMA | Zakat-based entities have modified requirements; designated non-financial businesses (DNFBPs) regulated |
| **UAE Federal** | Federal Decree-Law 20/2018 on AML/CFT + CBUAE regulations | CBUAE; goAML | 60-day registration on goAML required; DNFBP register |
| **DIFC** | DFSA AML Module (AMI) | DFSA | Periodic AML returns filed with DFSA; DFSA AML inspections |
| **ADGM** | FSRA AML Rulebook | FSRA | Alignment with DIFC/DFSA approach but separate filing |
| **LB** | Law 44/2015 (AML/CFT) + BDL circulars | Special Investigation Commission (SIC) | Banks: enhanced CDD on cash transactions; STRs to SIC |
| **EU** | 6th AML Directive (6AMLD) + national implementation | National FIU | Cross-border information sharing; criminal liability for legal persons |
| **US** | Bank Secrecy Act (BSA) + FinCEN rules + PATRIOT Act | FinCEN; federal banking regulators | CTRs for transactions >$10,000; CIP rules; beneficial ownership rule |

## Critical for fintech and virtual assets

- **VARA (UAE)**: Virtual Assets Regulatory Authority in Dubai — VASP license requires dedicated VASP AML policy on top of standard AML program.
- **ADGM FSRA**: Virtual Asset Framework — specific CDD and ongoing monitoring for virtual asset businesses.
- **FATF Travel Rule (Recommendation 16)**: transfers of virtual assets above USD 1,000 / EUR 1,000 must be accompanied by originator and beneficiary information; the implementing jurisdiction's threshold may differ. Technology implementation (TRISA, OpenVASP, or similar) must be operational.
- **Real-time monitoring**: fintech transaction monitoring must handle high velocity and 24/7 operations; static rule-based systems are often insufficient; behavioral analytics expected.

## Implementation checklist

- [ ] MLRO appointed, mandate documented, reported to regulator where required
- [ ] Board-approved policy in place, signed, dated
- [ ] Business-wide risk assessment completed and documented
- [ ] CDD procedures in place with UBO identification
- [ ] EDD procedures defined for PEPs, high-risk jurisdictions, VASPs
- [ ] Sanctions screening tool operational with at minimum UN + OFAC + local lists
- [ ] Transaction monitoring system operational (automated alerts + manual review)
- [ ] SAR/STR filing procedure documented; MLRO trained
- [ ] Staff training delivered; records retained
- [ ] Independent annual review scheduled
- [ ] Record retention system in place for 5–7 years

## Related skills

- [[draft-compliance-manual]]
- [[draft-board-resolution]]
- [[review-regulatory-compliance]]

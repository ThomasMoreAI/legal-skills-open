---
name: draft-kyc-procedure-sboghossian
title: KYC / Customer Due Diligence Procedure
description: Use when drafting or reviewing a Know Your Customer (KYC) procedure for a financial institution, fintech, law firm, or regulated business operating under AML/CFT obligations. Covers the full customer due diligence lifecycle — identification, verification, beneficial ownership, risk classification, sanctions screening, PEP checks, and periodic refresh — with specific attention to MENA regulatory frameworks (UAE CBUAE, KSA SAMA, Lebanon SIC, DIFC/ADGM, FATF). Triggers on "kyc", "customer due diligence", "cdd", "aml procedure", or "onboarding compliance" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-kyc-procedure
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# KYC / Customer Due Diligence Procedure

## When to use this

Use this skill when:
- Drafting a new KYC/CDD procedure from scratch for a regulated entity
- Revising an existing procedure to reflect regulatory updates (FATF mutual evaluations, new national AML laws)
- Onboarding documentation for a specific customer type (individual, corporate, PEP, high-risk)
- Training and compliance-awareness material for staff

KYC procedures are legally mandated for financial institutions, money service businesses, designated non-financial businesses and professions (DNFBPs — lawyers, accountants, real estate agents above thresholds), and increasingly fintech platforms in all MENA jurisdictions.

## Inputs

- Entity type and regulatory license category (bank, exchange house, fintech, DNFBP)
- Applicable jurisdiction(s) and regulator(s)
- Customer segments to be covered (retail individual, corporate, high-net-worth, correspondent institution)
- Existing risk appetite and risk-scoring model (if any)
- Whether procedure must comply with FATF Recommendations, or a specific jurisdiction's AML law

## The eight-step KYC procedure

### Step 1 — Customer identification

Collect sufficient information to establish the customer's identity before the business relationship begins.

**Individual customers** — collect at minimum:
- Full legal name (as per government ID)
- Date of birth
- Nationality and country of residence
- Residential address (physical — not PO box)
- Government-issued photo ID (passport, national ID, driving licence)
- Taxpayer identification number (where required)
- Source of income / wealth (for enhanced due diligence customers)

**Corporate customers** — collect at minimum:
- Full legal name + trading name
- Company registration number + jurisdiction
- Registered address + principal place of business
- Memorandum and Articles of Association (or equivalent)
- Certificate of Incorporation / Trade Licence
- Ownership structure chart (all layers to ultimate beneficial owner)
- Directors / authorized signatories list with ID for each

**Simplified due diligence (SDD)** is available in most jurisdictions for low-risk customer categories (listed companies, public authorities, regulated financial institutions in equivalent jurisdictions) — document the basis for SDD.

### Step 2 — Independent verification

The identity information collected must be verified against independent, reliable sources. "Reliable" means:
- Government-issued documents (not photocopies of photocopies)
- Official registries (company registry, land registry)
- Regulated data providers (e.g., commercial databases) for corporate structure verification
- Face-to-face verification or certified equivalent (video KYC where allowed)

For remote onboarding (digital / eKYC): most MENA regulators now accept eKYC using document verification + liveness check, provided the solution meets the regulator's prescribed standards. CBUAE AML Standards 2021 and DIFC AML Module permit this.

### Step 3 — Beneficial ownership (BO) mapping

**Threshold**: 25% ownership or control is the FATF-recommended threshold; some regulators use 10% for financial institutions.

For every corporate customer:
1. Map the ownership chain layer by layer until you reach natural persons who own ≥25% OR exercise control
2. If no natural person owns ≥25%, identify the natural person who exercises control by other means (board majority, veto rights, contractual control)
3. Where ownership is through a trust: identify settlor, trustees, and beneficiaries (or class of beneficiaries)
4. Verify BO identity to the same standard as the customer itself

Document the BO mapping with a signed declaration from an authorized officer of the customer. For complex structures (layers of holding companies, nominees), escalate to Enhanced Due Diligence.

### Step 4 — Purpose and nature of relationship

Before opening the account / starting the relationship:
- Understand the intended purpose (trading account, investment, custody, financing)
- Expected transaction profile (volume, frequency, typical counterparties, geographic scope)
- Expected funding sources

Document these expectations in the customer profile. Transactions that deviate materially from the expected profile are a trigger for review.

### Step 5 — Source of funds and source of wealth (high-risk customers)

**Source of funds (SoF)**: Where do the funds for this specific transaction come from? Required for all transactions above thresholds and for high-risk customers.

**Source of wealth (SoW)**: How did the customer accumulate their overall net worth? Required for Enhanced Due Diligence customers (PEPs, high-net-worth individuals, customers from high-risk jurisdictions).

Acceptable evidence: audited financial statements, employment contracts / payslips, property sale documents, inheritance records, company ownership proof. Verbal assertions with no documentary support are insufficient for EDD.

### Step 6 — Sanctions screening

Screen all parties (customer, beneficial owners, authorized signatories, connected parties) against:
- **UN Security Council consolidated list** — mandatory globally
- **OFAC SDN list** (US) — mandatory for USD-clearing institutions and US-nexus transactions
- **EU Consolidated Sanctions List** — mandatory for EU-connected business
- **UK HMT Financial Sanctions List**
- **Local lists**: UAE CBUAE List, KSA SAMA List, Lebanon SIC Designated List

Screening must be:
- Performed at onboarding
- Re-screened at every material transaction
- Rescreened whenever lists are updated (automated real-time screening is best practice)
- Applied to all names, aliases, and transliterations (Arabic transliterations of names require fuzzy matching)

A sanctions hit requires immediate freezing and reporting to the relevant Financial Intelligence Unit (FIU). Do not alert the customer (tipping-off prohibition).

### Step 7 — PEP screening and adverse media

**Politically Exposed Persons (PEPs)**: individuals who hold or have held prominent public functions, their family members, and close associates.

FATF Recommendations require enhanced scrutiny of PEPs. "Foreign PEPs" (PEPs in another country) require EDD; "domestic PEPs" in many jurisdictions also require EDD.

For PEPs:
- Seek senior management approval before establishing the relationship
- Document the source of wealth to a higher standard
- Apply continuous monitoring (not just periodic refresh)

**Adverse media screening**: Search for negative news linking the customer to financial crime, bribery, corruption, terrorism, tax evasion, or fraud. Commercial adverse media screening tools should be used; manual Google searches are insufficient for regulated entities at scale.

### Step 8 — Periodic review / refresh

The customer file must be kept current:
| Risk category | Refresh frequency |
|---|---|
| Low risk | Every 3-5 years |
| Medium risk | Every 2 years |
| High risk / PEP | Annually or more frequently |
| Trigger-based | On significant change (new BO, new business line, large unusual transaction) |

Refresh includes: re-verification of expired IDs, re-screening against sanctions and PEP lists, review of transaction history for consistency with expected profile.

## Enhanced Due Diligence (EDD) triggers

EDD (deeper investigation, senior management approval) is required when:
- Customer is a PEP, PEP family member, or PEP associate
- Customer is from or transacts with a FATF high-risk or monitored jurisdiction
- Business is conducted non-face-to-face with unusual complexity
- Transaction has no apparent economic rationale
- Customer is a shell company or nominee structure without clear business purpose
- Politically or reputationally exposed transactions (government contracts, gaming, defense)

## Risk-scoring framework

Assign each customer a composite risk score based on:
- **Customer risk factors**: type (individual/corporate), PEP status, adverse media, industry
- **Geographic risk factors**: nationality, country of incorporation, country of operations (FATF high-risk list)
- **Product/service risk factors**: cash-intensive, cross-border, high-value, anonymity potential
- **Channel risk factors**: non-face-to-face onboarding, intermediary introduced

Document the risk score in the customer file and review it at each periodic refresh.

## Jurisdictional notes

| Jurisdiction | Primary regulatory framework |
|---|---|
| **UAE (federal)** | Federal Decree-Law 20/2018 (AML Law); Cabinet Decision 10/2019 (AML Executive Regulation); CBUAE AML Standards 2021 |
| **DIFC** | DFSA Rulebook AML Module (AMI); mirrors FATF with common-law overlay |
| **ADGM** | FSRA AML and Sanctions Rules; similar to DFSA; periodic guidance notices |
| **KSA** | AML Law (Royal Decree M/39/2003 as amended); SAMA AML Guidance for Banks; SAMA Crypto AML Rules |
| **LB** | Law 44/2015 (AML Law); Special Investigation Commission (SIC) is the FIU; CBA Circular 83 and subsequent circulars on CDD |
| **EG** | Law 80/2002 and its amendments; EFSA AML Guidelines; Central Bank AML instructions |
| **FATF** | 40 Recommendations (2012, updated 2023); Guidance on Beneficial Ownership, Guidance on Virtual Assets |

## Output format

A KYC procedure document should include:
1. **Policy statement** — commitment to AML/CFT compliance, regulatory basis, scope of application
2. **Customer risk classification matrix** — scored table
3. **CDD checklist per customer type** (individual / corporate / PEP / correspondent)
4. **EDD checklist**
5. **Screening procedure** — lists used, frequency, escalation on hit
6. **Periodic review calendar and triggers**
7. **Record-keeping requirements** — retention period (5 years minimum under FATF; 10 years in some jurisdictions)
8. **Escalation and reporting chain** — to Compliance Officer, then to FIU if applicable
9. **Staff responsibility matrix** — who does what at each step

## Limits and escalation

- This skill assists with procedure drafting; final compliance sign-off requires a qualified AML compliance officer
- Sanctions hit handling and STR/SAR filing require legal and compliance review before action
- Cross-border KYC requirements may interact — engage local counsel in each jurisdiction
- Laws and regulatory guidance change frequently; verify currency of all regulatory references before publishing the procedure

## Related skills

- [[draft-aml-policy]]
- [[review-aml-compliance]]
- [[draft-privacy-policy]]
- [[draft-dpa-gdpr]]
- [[draft-dpa-ksa-pdpl]]

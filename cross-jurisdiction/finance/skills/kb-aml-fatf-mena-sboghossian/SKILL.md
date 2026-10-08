---
name: kb-aml-fatf-mena-sboghossian
title: Knowledge Pack — AML / CFT in MENA
description: Use when advising on anti-money laundering (AML) or counter-terrorist financing (CFT) obligations in MENA jurisdictions, including customer due diligence, suspicious activity reporting, beneficial ownership disclosure, sanctions screening, and DNFBP obligations. Covers Saudi Arabia, UAE (onshore, DIFC, ADGM), Lebanon, and Egypt in depth, with FATF/MENAFATF framework context and crypto-asset AML requirements.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-aml-fatf-mena
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: finance
language: en
---

# Knowledge Pack — AML / CFT in MENA

## Scope

This pack covers the legal and compliance framework for anti-money laundering (AML) and counter-terrorism financing (CFT) across the principal MENA jurisdictions. It is the primary reference for:

- Compliance program design and gap assessment
- Customer due diligence (CDD/KYC) standards
- Suspicious activity reporting obligations
- Beneficial ownership requirements
- Sanctions screening
- DNFBP (designated non-financial businesses and professions) obligations
- Crypto-asset AML

---

## FATF and MENAFATF

### FATF — the global standard

The **Financial Action Task Force (FATF)** issues the 40 Recommendations, which constitute the global AML/CFT standard. Key recommendations for practitioners:

- **Recommendation 10** — Customer Due Diligence
- **Recommendation 16** — Wire Transfer (Travel Rule); extended to Virtual Asset Service Providers
- **Recommendation 20** — Suspicious Transaction Reporting
- **Recommendation 24/25** — Beneficial ownership of legal persons and arrangements
- **Recommendation 40** — International cooperation

FATF maintains a public list of high-risk jurisdictions (grey list) and jurisdictions subject to a call for action (black list). Correspondent banking and cross-border transactions are significantly affected by a counterparty's FATF listing status.

### MENAFATF

The **MENA Financial Action Task Force** is the FATF-style regional body for the Arab world, headquartered in Bahrain. It conducts mutual evaluations of member states using the FATF methodology. Evaluation outcomes are public and directly affect a country's risk classification by international financial institutions.

**Recent MENA grey-list history:** UAE was grey-listed from 2022 to 2024, prompting an intensive legislative and enforcement reform program. The UAE's removal from the grey list reflects significant rule-tightening across UBO disclosure, DNFBP coverage, and VASP regulation.

---

## Saudi Arabia

### Primary legislation

- **Anti-Money Laundering Law** (Royal Decree M/20 1442H / 2021)
- SAMA AML/CFT Rules — applicable to banks and financial institutions
- Ministry of Commerce (MOC) AML rules — DNFBPs including lawyers handling client funds

### Financial Intelligence Unit

- **Saudi Financial Intelligence Unit (SAFIU)** — receives Suspicious Activity Reports (SARs)
- Operated under the Ministry of Interior
- goSAFIU platform for electronic reporting

### CDD and reporting

- Standard CDD on all customers; EDD for PEPs, high-risk jurisdictions, high-risk customers
- SARs filed to SAFIU
- Currency declaration: SAR 60,000 or equivalent on entry/exit

### Beneficial ownership

- UBO disclosure required for all legal entities; MISA / MOC registries
- Ultimate beneficial owner = person holding or controlling 25%+ (default threshold)

### Penalties

- Up to 10 years imprisonment
- Heavy fines (multiples of amounts involved)
- Asset forfeiture
- License suspension for institutions

---

## UAE

### Primary legislation

- **Federal Decree-Law 20/2018** on AML/CFT (as amended)
- Cabinet Decision 10/2019 — implementing regulations
- AML/CFT Guidance for various sectors (CBUAE, DFSA, FSRA, VARA)

### Financial Intelligence Unit

- **UAE FIU** — operates the **goAML** platform for SAR and threshold transaction reporting
- Administered by CBUAE

### Regulatory landscape (tiered)

| Entity type | Regulator |
|---|---|
| Banks (onshore) | CBUAE |
| Insurance | CBUAE (post-2021 merger with Insurance Authority) |
| DIFC entities | DFSA |
| ADGM entities | FSRA |
| Virtual assets (Dubai) | VARA |
| DNFBPs | Ministry of Economy (AML/CFT supervision) |

### CDD requirements

- Standard CDD: identity verification + beneficial owner identification + purpose of relationship
- EDD triggers: PEPs, customers from high-risk jurisdictions, complex or unusual transactions, high-value cash transactions
- UBO mandatory disclosure: >25% ownership threshold; UBO register filing with DED, DIFC/ADGM authority, or FTA (Corporate Tax UBO)

### Sanctions

- UAE implements UN Security Council sanctions as mandatory
- CBUAE maintains targeted financial sanctions list
- Designated Persons List (local list) + UN + OFAC + EU screening required for comprehensive compliance

### DNFBP obligations

DNFBPs in the UAE are supervised by the Ministry of Economy for AML purposes:

- **Real estate agents** — when facilitating purchase/sale
- **Lawyers and legal professionals** — when handling client funds or certain transaction types
- **Accountants and auditors**
- **Gold, precious metals, and precious stones dealers** (above AED 55,000 per transaction)
- **Trust and company service providers (TCSPs)**

DNFBPs must implement AML programs, perform CDD, file SARs, and register with the goAML platform.

### Post-grey-list reforms (2022–2024)

The UAE's removal from the FATF grey list in 2024 followed:
- Strengthened UBO registers
- DNFBP supervision ramp-up
- VARA framework for virtual assets
- Increased SAR filings and FIU capacity
- Enhanced proliferation financing controls

---

## Lebanon

### Primary legislation

- **Law 44/2015** on fighting money laundering and terrorist financing (replaced Law 318/2001)
- BDL Basic Circular 83 (AML guidance for banks)

### Financial Intelligence Unit

- **Special Investigation Commission (SIC)** — located at BDL; acts as Lebanon's FIU
- Has judicial assistance and lifting of bank secrecy powers for AML investigations

### Bank secrecy interaction

- Lebanon's historic bank secrecy law (Law 3/1956) is a dominant feature
- Bank secrecy is lifted for AML investigations by SIC order
- 2022 amendments to the bank secrecy law further reduced secrecy protections
- The financial crisis has created practical complexities in SIC operations

### Currency declaration

- Declare ≥ USD 15,000 (or equivalent) when crossing Lebanese borders

### Crisis context and enhanced risk

Lebanon's ongoing financial crisis since 2019 means:
- Heightened correspondent bank scrutiny of Lebanon-origin transactions
- Enhanced due diligence required when dealing with Lebanese financial institutions
- Lebanese bank-issued documentation treated as elevated-risk by international counterparties

---

## Egypt

### Primary legislation

- **Law 80/2002** on anti-money laundering (as amended by Law 78/2003 and subsequent amendments)
- Implementing regulations issued by the Egyptian FIU

### Financial Intelligence Unit

- **Egyptian Anti-Money Laundering and Combating the Financing of Terrorism Unit (EMLCU / EFIU)**
- Reports to the Central Bank of Egypt (CBE)
- Receives and analyses SARs

### Coverage

- Banks and financial institutions: full AML obligations
- DNFBPs: progressively incorporated (real estate, lawyers in certain transactions, high-value dealers)
- Currency dealers and exchange bureaux: licensed and supervised

---

## Customer Due Diligence (CDD) — FATF-aligned standards

### Standard CDD (all jurisdictions)

1. **Identification** — obtain official ID documents
2. **Verification** — verify from an independent, reliable source (document + electronic)
3. **Beneficial ownership** — identify the ultimate beneficial owner (typically 25%+ threshold)
4. **Purpose** — understand the purpose and intended nature of the business relationship
5. **Ongoing monitoring** — update CDD records; monitor transactions for consistency

### Enhanced Due Diligence (EDD)

Mandatory triggers:

| Trigger | EDD measure |
|---|---|
| **PEPs** (domestic or foreign) | Senior management approval; source-of-wealth/funds verification; continuous monitoring |
| **High-risk jurisdictions** (FATF grey/black list) | Additional information gathering; enhanced transaction monitoring; possible exit from relationship |
| **Complex or unusual structures** | Beneficial ownership analysis one level deeper; senior management sign-off |
| **Cash-intensive businesses** | Enhanced transaction monitoring thresholds |
| **Correspondent banking** | FATF Recommendation 13 — full CDD on respondent institution |

### Simplified Due Diligence (SDD)

Permitted only for demonstrably low-risk customers: regulated financial institutions in FATF-equivalent jurisdictions, listed public companies with adequate disclosure. SDD does not mean no CDD — it permits reduced intensity.

---

## Sanctions screening

| Sanctions list | Applicability |
|---|---|
| UN Security Council lists | Mandatory in all MENA jurisdictions |
| OFAC (US) | Mandatory for any USD-clearing transaction or US-nexus activity |
| EU Sanctions | Mandatory for EU-nexus entities and transactions; increasingly relevant for DIFC/ADGM |
| CBUAE targeted financial sanctions | UAE-specific national list |
| UK OFSI | Relevant for UK/ADGM nexus entities |

Screening must cover customers, beneficial owners, directors, and transaction counterparties. PEP screening is separate from sanctions but often managed in the same tool.

---

## Crypto-asset AML

- **Travel Rule (FATF Recommendation 16)**: Virtual Asset Service Providers (VASPs) must transmit originator and beneficiary information on transfers above USD/EUR 1,000
- **VARA Dubai**: AML/CFT program mandatory; FATF-aligned; goAML registration required
- **ADGM FSRA**: full AML obligations on ACSPs (Authorized Crypto Asset Service Providers)
- **KSA**: crypto restricted; AML obligations apply to any permitted activity
- **Lebanon and Egypt**: crypto largely unregulated but AML obligations apply if activities fall under existing VASP definitions

---

## Penalties summary

| Jurisdiction | Max criminal penalty | Max institutional fine |
|---|---|---|
| UAE | Up to life imprisonment in severe cases | AED 50 million |
| KSA | Up to 10 years | Multiples of amount involved |
| Lebanon | Up to 7 years | Fines + license suspension |
| Egypt | Up to 10 years | Variable fines |

---

## DNFBPs — categories across MENA

| Category | UAE | KSA | Lebanon | Egypt |
|---|---|---|---|---|
| Real estate agents (purchase/sale) | Yes | Yes | Partial | Yes |
| Lawyers (client funds/transactions) | Yes | Yes (MOC rules) | Yes | Yes |
| Accountants/auditors | Yes | Yes | Yes | Yes |
| Gold/precious metals dealers | Yes (>AED 55K) | Yes | Partial | Yes |
| TCSPs | Yes | Yes | Partial | Partial |

---

## Practical compliance program elements

For any regulated entity operating in MENA:

1. **AML Policy** — risk-based; approved by senior management or board
2. **CDD Procedures** — standard + enhanced + simplified; triggered by risk rating
3. **Transaction Monitoring** — automated rules + manual review; alert management
4. **SAR/STR Filing** — designated MLRO; goAML or equivalent platform
5. **Sanctions Screening** — real-time, automated; covers customers + transactions
6. **PEP Screening** — separate or integrated with sanctions
7. **Annual AML Training** — mandatory for all staff
8. **Independent Annual AML Review** — audit function or external reviewer
9. **Record Retention** — 5 years minimum (10 years in some jurisdictions) from end of relationship
10. **MLRO Designation** — named, competent, with direct board access

---

## How to use this pack

Load this pack when the user asks about:
- AML obligations of a specific entity type in MENA
- CDD/KYC requirements for a particular customer category
- SAR filing obligations and process
- Sanctions screening scope
- DNFBP AML compliance
- Crypto-asset AML requirements

## Caveats & currency

AML law in MENA changes rapidly — UAE's FATF grey-list reforms are still being consolidated (post-2024). KSA and Egypt regularly update implementing regulations. Always verify current CBUAE/SAMA/SAFIU/goAML guidance before advising on specific compliance program design. FATF mutual evaluation results update country risk classifications and should be monitored.

## Related skills

- [[kb-banking-regulation-cbuae]] — CBUAE-specific AML framework for UAE banks
- [[kb-banking-regulation-sama]] — SAMA-specific AML framework for KSA banks
- [[kb-banking-regulation-bdl]] — BDL/SIC framework for Lebanon
- [[kb-crypto-vara-dubai]] — VARA AML obligations for Dubai VASPs
- [[kb-crypto-adgm]] — ADGM FSRA AML obligations for ACSPs
- [[draft-aml-policy]] — template AML policy document

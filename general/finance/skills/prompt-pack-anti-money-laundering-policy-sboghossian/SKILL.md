---
name: prompt-pack-anti-money-laundering-policy-sboghossian
title: Anti-Money Laundering Policy
description: Use when drafting a comprehensive AML/KYC policy for a financial institution (bank, finance company, insurance firm) covering customer due diligence, enhanced due diligence, suspicious activity reporting, record-keeping, and staff training. Closely related to the fintech-focused AML/KYC policy skill; this skill addresses the broader financial institution context with additional emphasis on correspondent banking, trade finance, and institutional EDD.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-anti-money-laundering-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Anti-Money Laundering Policy

## When to use this

Use this skill when drafting a comprehensive AML/KYC policy for a **financial institution** — bank, finance company, insurance company, investment firm, exchange house, or similar regulated entity. This skill has a broader scope than [[prompt-pack-aml-kyc-policy]] (which focuses on fintech/payments companies): it addresses the full financial institution context including:
- Correspondent banking relationships
- Trade finance and documentary credits
- Institutional/corporate client EDD
- Shell bank prohibitions
- Sanctions compliance integration with AML controls

---

## Prompt template

> Draft a comprehensive AML/KYC policy for [financial institution/fintech company] operating in [jurisdiction]. Include customer due diligence procedures, enhanced due diligence triggers, suspicious activity reporting, record-keeping requirements, and staff training obligations.

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before drafting.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Institution name and type | Bank, finance company, exchange house, insurance — different regulatory frameworks |
| Jurisdiction(s) of licensing | Determines the specific regulator and AML law |
| Business lines in scope | Different business lines have different AML risks |
| Customer segments | Retail, corporate, institutional, correspondent banks — each has different CDD standards |
| Existing AML controls infrastructure | New build vs. policy update |

---

## Document structure

### 1. Policy statement and governance

**Board-level commitment**: the policy must be approved by the board of directors or equivalent governance body. The board is ultimately responsible for the AML framework.

**Three lines of defence**:
1. First line: business units (own and manage AML risk day-to-day)
2. Second line: compliance / AML function (design, monitor, and test controls; MLRO)
3. Third line: internal audit (independent testing of the AML framework)

**MLRO designation**: name, role, reporting line, authority, resources. In most MENA jurisdictions the MLRO must be senior (MD/VP level or above) and the appointment must be notified to the regulator.

### 2. Regulatory framework

The policy must reference the specific legal and regulatory instruments applicable to the institution:

**UAE onshore financial institutions**:
- AML/CFT Federal Decree-Law 20/2018 ("AML Law")
- Cabinet Decision 10/2019 (implementing regulations)
- CBUAE AML/CFT Standards (most recently updated 2023/2024)
- CBUAE Circular on Financial Sanctions compliance

**DIFC entities**:
- DIFC AML/CFT Law (DIFC Law No. 1 of 2017 as amended by Law No. 8 of 2024)
- DFSA Rulebook: AML Module, and sector-specific modules (Islamic Finance Supplement, etc.)

**ADGM entities**:
- ADGM AML/CFT Regulations 2015 (as amended)
- ADGM FSRA AML Rules

**KSA financial institutions**:
- AML Law (Royal Decree M/31/2003 as amended)
- SAMA AML/CFT Rules (updated 2021)
- SAFIU regulations

**Lebanon**:
- AML Law No. 44/2015
- Banque du Liban Basic Circular No. 83 (AML) and intermediary circulars
- SIC (Special Investigation Commission) operational guidelines

**Egypt**:
- AML Law No. 80/2002 (as amended by Law No. 78/2019)
- CBE AML/CFT Instructions

### 3. Customer due diligence — expanded for financial institutions

#### 3.1 CDD for natural persons and legal entities
[See [[prompt-pack-aml-kyc-policy]] for full CDD documentation requirements — this section expands on institutional-specific CDD]

#### 3.2 Corporate and institutional clients
Additional requirements for legal entities:
- **UBO identification**: trace beneficial ownership to the natural persons who own or control 25%+ (or 10% in some jurisdictions) — through all layers of holding structure
- **Complex structures**: trusts, foundations, nominee shareholders require look-through to identify the ultimate beneficial owner
- **UAE UBO register**: Cabinet Resolution 58/2020 requires UAE-incorporated entities to maintain and file UBO information; verify against the register

#### 3.3 Correspondent banking
Before establishing or continuing a correspondent banking relationship:
- Assess the respondent bank's AML controls (questionnaire, Wolfsberg AML correspondent banking principles)
- Obtain senior management approval
- Prohibit relationships with shell banks (banks with no physical presence in any jurisdiction)
- No payable-through accounts to unverified third parties
- Annual review of the relationship

#### 3.4 Trade finance
Trade finance is a high-risk area for money laundering (invoice fraud, mis-invoicing, commodity fraud):
- Independent verification of trade transactions where possible
- Dual-use goods: screen for export control and sanctions implications
- Documentary credits: verification of underlying trade and parties
- Red flags: unusual pricing, indirect routing, unusual countries, complex payment structures

### 4. Enhanced due diligence triggers

Apply EDD where:

| Trigger | Notes |
|---------|-------|
| Politically Exposed Person (PEP) | Senior government official or state enterprise; close family or known associate. EDD applies for foreign PEPs at all times; some jurisdictions require EDD for domestic PEPs on risk basis |
| High-risk jurisdiction | FATF grey list; FATF black list; jurisdiction on company's own internal high-risk list |
| Unusual transaction patterns | Activity inconsistent with customer profile or declared purpose |
| High-value transactions above threshold | UAE: cash transactions above AED 55,000; international: USD 10,000 CTR threshold |
| Complex or opaque structures | Multiple layers of holding; nominee shareholders |
| Adverse media | Negative credible media about customer, beneficial owner, or associated parties |

EDD requirements:
- Source of funds and wealth documentation
- Senior management approval for onboarding or continuing relationship
- More frequent periodic review (at minimum annually for PEPs and high-risk)
- Enhanced transaction monitoring

### 5. Sanctions screening

While distinct from AML, sanctions compliance is typically managed within the AML function:
- Screen all new customers at onboarding against designated lists (OFAC SDN, EU Consolidated List, UN SC Sanctions, UAE Cabinet Decision 20/2019 local terrorist list, jurisdiction-specific lists)
- Screen at each periodic review and on transaction processing (real-time or near real-time for financial institutions)
- Freeze and report: if a match is confirmed, freeze the account/transaction and report to the relevant authority immediately
- False positive management: documented process for clearing false positives; documentation retained

### 6. Suspicious activity reporting

[See [[prompt-pack-aml-kyc-policy]] for the core SAR process — this section adds institutional-specific elements]

Additional for financial institutions:
- Multiple internal SARs on the same customer or relationship should trigger a full relationship review
- Automated transaction monitoring system: document the rules, thresholds, and scoring model used; update model regularly
- L-SAR (Large Cash Transaction Report) / CTR (Currency Transaction Report): mandatory filing in UAE (above AED 55,000 cash) and other jurisdictions — separate from SAR
- **Tipping-off**: a criminal offence under AML Law in all MENA jurisdictions; employees must be trained that they cannot tell the customer a report has been made or is being considered

### 7. Record-keeping

| Record type | Retention period |
|-------------|----------------|
| Customer identification records | UAE: 5 years after end of relationship; KSA: 10 years; DIFC: 6 years; Lebanon: 5 years |
| Transaction records | Same as identification records |
| SAR/internal reports | Same retention period; access restricted to need-to-know |
| Correspondent banking due diligence | Same period as relationship |
| Training records | 3 years minimum |

### 8. Staff training

- **Scope**: all employees; enhanced training for MLRO, compliance team, and customer-facing staff
- **Frequency**: on joining; annually; on material regulatory changes
- **Content**: AML obligations; red flags for ML/TF; internal reporting process; consequences of non-compliance (criminal liability; regulatory sanction; dismissal)
- **Completion tracking**: attendance records; assessment scores; evidence of training materials used

### 9. Governance and reporting

- **Annual AML report**: MLRO presents to the board/senior management annually; includes: SAR statistics, training completion rates, high-risk customer numbers, enforcement/regulatory developments, gaps and remediation plan
- **Regulatory reporting**: comply with all periodic and ad hoc regulatory reporting obligations (CBUAE, DFSA, SAMA, SIC, CBE)
- **Independent AML audit**: internal audit or external auditor reviews AML framework at least annually; report findings to board/Audit Committee; remediation tracked

---

## Jurisdictional notes — enforcement risk

- **UAE/DIFC**: CBUAE and DFSA have both imposed significant fines for AML failures. DFSA AML enforcement actions are published. UAE onshore: CBUAE has issued consent orders and revoked licenses for AML deficiencies.
- **KSA**: SAMA has increased AML enforcement in the banking and fintech sector since 2020. Fines and license suspensions are used.
- **Lebanon**: SIC (Special Investigation Commission) has enforcement powers; Banque du Liban circulars carry supervisory authority.
- **Egypt**: CBE has imposed penalties for AML deficiencies; enforcement is increasing.

---

## Common mistakes

- Policy approved by management, not the board — board approval is mandatory in most MENA frameworks
- No operationalized screening procedure — a policy requirement for PEP screening without a screening tool or process is a compliance failure
- Correspondent banking section missing — often omitted but required for institutions with correspondent relationships
- Tipping-off prohibition not addressed in employee training
- No annual AML review obligation — the policy must require itself to be reviewed

---

## Related skills

- [[prompt-pack-aml-kyc-policy]] — fintech-focused AML/KYC policy (narrower scope)
- [[kb-aml-mena]] — MENA AML/CFT law reference
- [[heuristic-always-state-jurisdiction-first]] — jurisdiction determines the applicable AML law
- [[prompt-pack-bnpl-platform-agreement]] — BNPL agreement with embedded AML requirements

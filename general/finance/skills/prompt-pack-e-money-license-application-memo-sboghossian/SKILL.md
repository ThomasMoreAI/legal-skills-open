---
name: prompt-pack-e-money-license-application-memo-sboghossian
title: E-Money License Application Memo
description: Use when preparing a compliance memo outlining the regulatory requirements for obtaining an electronic money institution (EMI) or e-money license in a target jurisdiction. Covers capital requirements, governance, AML/KYC obligations, safeguarding requirements, and application process timeline. Relevant for fintech companies seeking to operate in UAE (CBUAE), DIFC (DFSA), ADGM (FSRA), KSA (SAMA), LB (BdL), EG (CBE), UK (FCA), EU (national NCAs under EMD2), and other jurisdictions. Trigger when a payments or e-money startup needs to understand the licensing pathway.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-e-money-license-application-memo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# E-Money License Application Memo

## When to use this

Use this skill when a fintech company, payment service provider, or digital wallet operator needs a structured legal memo analyzing the requirements for obtaining an e-money or payment institution license in a specific jurisdiction. The memo informs the business decision on where to incorporate, what entity structure to use, and what the regulatory timeline and costs are.

Typical triggers:
- Startup evaluating which MENA or EU jurisdiction to use as its primary regulated home
- Existing fintech seeking to expand licensed operations into a new market
- Investor requiring confirmation that target has a viable licensing pathway
- Counsel advising on the regulatory pre-conditions before launch

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Company name and current corporate structure | Identifies the applicant entity | Ask |
| Target jurisdiction(s) for the license | Each jurisdiction has different requirements | Ask |
| Business model description | E-money issuance, payment initiation, wallet, remittance, acquiring — each triggers different rules | Ask |
| Target launch timeline | Affects advice on jurisdiction selection (fast vs. thorough regimes) | Ask |
| Expected float / average outstanding e-money | Drives capital adequacy and safeguarding requirements | Ask |

## Optional inputs

- Current capitalization (to assess gap vs. minimum capital requirements)
- Names and backgrounds of proposed directors and senior managers (fit-and-proper assessment)
- Proposed AML officer and compliance officer (key-person requirements)
- Existing technology infrastructure details
- Other jurisdictions where the company already holds licenses (passporting implications for EU)

## Memo structure

### 1. Executive Summary

- Jurisdiction recommended and rationale
- Estimated timeline from application to license issuance
- Minimum capital requirement
- Key conditions and deal-breakers

### 2. License Category and Scope

Define what type of license is required:
- E-money institution (EMI) license — permits issuance of e-money stored on devices or servers, payment execution
- Payment institution (PI) license — permits payment services but not e-money issuance
- Small EMI / limited license — reduced requirements for lower-value operators (available in some jurisdictions)

For each business activity (wallet, remittance, acquiring, lending), confirm which license category permits it.

### 3. Minimum Capital Requirements

| Jurisdiction | Minimum initial capital | Ongoing capital requirement |
|---|---|---|
| **EU (EMD2)** | EUR 350,000 for EMI; EUR 20,000–125,000 for PI depending on service category | Higher of minimum or 2% of average outstanding e-money |
| **UK (EMI)** | GBP 350,000 | Same methodology as EU; FCA applies own liquidity guidance |
| **UAE (CBUAE)** | AED 50 million for full payment service license; tiered for limited/stored value | As prescribed by CBUAE Retail Payment Services and Card Schemes Regulation |
| **DIFC (DFSA)** | USD 500,000 for Authorised Firm (Providing Money Services) | As prescribed by DFSA Rulebook (GEN Module) |
| **ADGM (FSRA)** | Determined by FSRA based on risk profile; typically USD 200,000+ | FSRA Financial Services and Markets Regulations 2015 |
| **KSA (SAMA)** | SAR 50 million for payment services company; lower for fintech sandbox participants | As prescribed by SAMA Payment Services Provider Regulations |
| **Lebanon (BdL)** | Per BdL Circular (e-payments framework); BdL has issued specific circulars for payment institutions | BdL Basic Circular 1 and related circulars; capital requirements periodically updated |
| **Egypt (CBE)** | Determined by CBE per Payment Systems and Digital Transactions Law (Law No. 18 of 2019) | CBE regulations set minimum capital and solvency requirements |

Note: Confirm all figures directly with the regulator or local counsel before relying on them — capital thresholds are subject to regulatory update.

### 4. Governance Requirements

- Minimum number of directors; required independence
- Fit-and-proper requirements for directors and senior managers (criminal record checks, financial history, competence)
- Required senior management roles: CEO, CFO, Chief Compliance Officer, MLRO (Money Laundering Reporting Officer), CTO (sometimes)
- Board-level risk and audit committees (usually required for larger EMIs)
- Minimum UAE/KSA national representation on board (in some MENA jurisdictions)

### 5. AML/KYC Obligations

All e-money license regimes impose AML/CFT obligations aligned with FATF 40 Recommendations:
- Customer due diligence (CDD) — standard, simplified, and enhanced
- Suspicious transaction reporting (STR) to the Financial Intelligence Unit
- Transaction monitoring systems
- Sanctions screening (OFAC, UN, EU, local lists)
- Record retention (typically 5–10 years)
- MLRO appointment and reporting obligations

**MENA specifics**:
- UAE: UAE AML Law (Federal Decree-Law No. 20 of 2018); CBUAE Guidance; goAML system for STR filing
- KSA: Anti-Money Laundering Law (Royal Decree M/31) and its implementing regulations; SAMA oversight
- Lebanon: Special Investigation Commission (SIC) — independent; Law No. 318 of 2001 on money laundering; severe consequences for non-compliance
- Egypt: Anti-Money Laundering Law (Law No. 80 of 2002, as amended) and CBE/FIU oversight

### 6. Safeguarding Requirements

E-money institutions must safeguard customer funds — they must be segregated from own funds and protected in insolvency:

- **EU/UK model**: Segregation in dedicated bank accounts or investment in low-risk liquid assets; insurance alternative available
- **CBUAE model**: Specific safeguarding rules in the Retail Payment Services and Card Schemes Regulation; funds must be held with a UAE bank
- **SAMA/KSA**: Segregated accounts at licensed Saudi banks required
- **DIFC/ADGM**: Trust account or equivalent arrangement

### 7. Application Process and Timeline

| Step | Description | Typical duration |
|---|---|---|
| Pre-application / regulatory engagement | Initial meeting with regulator to discuss business model; some regulators offer pre-application meetings | 1–4 weeks |
| Application preparation | Drafting application form, business plan, financial projections, policies | 4–12 weeks |
| Application submission | Submission with filing fee | Day 1 |
| Completeness review | Regulator checks application is complete; may issue queries | 2–8 weeks |
| Substantive review | Fit-and-proper assessment; business model review; AML/governance review | 3–12 months |
| License issuance | Conditional or full license granted | License effective from issuance date |

**UAE (CBUAE)** timeline: approximately 6–12 months for a full payment services license. Fintech regulatory sandbox available for eligible companies (faster path to operating, limited scope).

**DIFC (DFSA)**: Typically 3–6 months; DFSA has a streamlined process for innovation testing license.

**EU (national NCA)**: Varies by member state; Lithuania, Malta, and Ireland have developed reputations as faster EMI licensing jurisdictions (typically 3–6 months); some NCAs take 12–18 months.

**UK (FCA)**: EMI authorization typically 12–18 months; FCA increased scrutiny post-2019; applications must be complete and thorough.

### 8. Regulatory Sandbox Options

Several MENA regulators offer sandbox programs that allow limited operation before full licensing:
- **UAE (CBUAE Fintech Office)**: Regulatory sandbox for innovative payment solutions
- **DIFC (Innovation Hub)**: FinTech regulatory sandbox with DFSA Innovation Testing License
- **ADGM (RegLab)**: FSRA's regulatory laboratory for fintech
- **KSA (SAMA Fintech Lab)**: Saudi Central Bank sandbox
- **Bahrain (CBB FinTech)**: Regional sandbox hub

Sandboxes provide 6–24 months of regulatory accommodation; they are a valuable first step for companies without prior financial services regulatory history.

## Common mistakes

- **Underestimating the capital requirement gap**: Many applicants discover they are undercapitalized after beginning the application process; confirm the figure early.
- **Weak MLRO/compliance function**: Regulators will reject applications without a credible, experienced Money Laundering Reporting Officer (MLRO); this person must be identified and committed before applying.
- **Generic business plan**: Regulators require a detailed 3-year financial model and a thorough description of the compliance and risk framework; template business plans are rejected.
- **Ignoring passporting**: EU-based EMIs can passport their license into other EEA member states via notification; this is much faster and cheaper than seeking separate national licenses.
- **Wrong entity type**: In some jurisdictions (KSA, UAE), the applicant must be a locally incorporated company; foreign branches or offshore entities are not eligible for certain license categories.

## Related skills

- [[prompt-pack-embedded-finance-partnership-agreement]]
- [[prompt-pack-draft-reply-to-department-notice]]
- [[prompt-pack-esg-policy-framework]]
- [[prompt-pack-insider-trading-policy]]

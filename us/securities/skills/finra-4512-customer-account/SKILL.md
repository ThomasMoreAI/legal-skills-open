---
name: finra-4512-customer-account
title: FINRA Rule 4512 — Customer Account Information
description: Drafts FINRA Rule 4512-compliant customer account records for broker-dealers. Use when onboarding customers, updating account information, or preparing for regulatory examinations. Triggers on requests involving customer account documentation, CIP/AML obligations, trusted contact designations, suitability profiling, or SEC Rule 17a-3 recordkeeping in broker-dealer contexts.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/finra-4512-customer-account
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
tags: [checklist, drafting, regulatory]
---

# FINRA Rule 4512 — Customer Account Information

Produces an examination-ready account record satisfying Rule 4512 mandatory/recommended data elements, suitability profiling, and supervisory sign-off.

## Prerequisites

- Government-issued photo ID (license, passport, state ID)
- Tax ID — SSN (individual), EIN (entity), or TIN (trust/estate)
- Account type determined (individual, joint, custodial, corporate, trust)
- Intended trading authorizations (cash, margin, options level)
- Supervisory principal available for sign-off

## Workflow

### 1. Customer Identification (Mandatory)

| Field | Notes |
|---|---|
| Full legal name | As on government ID; include suffix (Jr., Sr., II) |
| Physical residential address | No P.O. boxes (CIP requirement) |
| Date of birth | Age of majority varies by state (18/19/21); custodial if minor |
| Tax ID | SSN/EIN/TIN; obtain within 30 days if unavailable at opening |
| Phone, mobile, email | Note preferred contact; e-delivery consent date if applicable |

**Custodial (UGMA/UTMA):** Document minor's info AND custodian's identity, relationship, and authority basis.

### 2. Trusted Contact Person (Rule 4512(a)(1)(E))

Must be offered; strongly recommended for customers age 65+.

**If designated** — collect: full legal name, relationship, mailing address, phone (primary + mobile), email, designation date.

**Scope:** Trusted contact has NO account authority. Firm may contact only to: confirm contact info, confirm identity of guardian/trustee/POA holder, or address financial exploitation/diminished capacity concerns.

**If declined:** Document declination and date; note ability to add later.

### 3. Employment & Affiliation Disclosures

| Situation | Action |
|---|---|
| Securities industry employee (BD, RIA, exchange) | Document employer, position, licenses; arrange duplicate confirms/statements |
| Director/officer/≥10% shareholder of public company | Document company, ticker, position; monitor Section 16/blackout compliance |
| Customer or household member affiliated with FINRA member | Obtain prior written employer consent (Rule 3210); send duplicate confirms |
| Self-employed | Document business nature and entity structure |

"Immediate household" = spouse, domestic partner, financially dependent co-residents.

### 4. Investment Profile & Suitability (Rule 2111)

**Objectives** (prioritize and document rationale): capital preservation, current income, growth, speculation, balanced.

**Risk tolerance:** Document narrative response to scenarios (e.g., 20% decline over 6 months), not just checkbox. Flag inconsistencies with stated objectives.

**Time horizon:** Short-term 1–3 yr | Intermediate 3–10 yr | Long-term 10+ yr

**Financial information** (ranges acceptable):

| Field | Buckets |
|---|---|
| Annual income | <$50K / $50–100K / $100–250K / $250–500K / $500K+ |
| Liquid net worth | Same scale |
| Total net worth (excl. primary residence) | Same scale |

**Experience by asset class** (none / limited / moderate / extensive + duration): equities, fixed income, mutual funds/ETFs, options, futures/commodities, alternatives.

**Special considerations:** ESG preferences, sector exclusions, tax-advantaged strategies, anticipated liquidity events.

### 5. Account Features & Elections

| Feature | Required Documentation |
|---|---|
| Margin | Margin agreement executed; risk disclosure delivered; forced liquidation acknowledged |
| Options | Approval level assigned (L1–L4+); OCC disclosure delivered; receipt dated |
| E-delivery | E-SIGN consent; email confirmed |
| Dividend reinvestment | Election and effective date |
| Cash sweep | Elected sweep vehicle |
| Securities lending | Consent obtained; disclosure delivered |

Options levels: L1 covered calls → L2 + cash-secured puts → L3 spreads → L4+ uncovered/complex.

### 6. Certification & Supervisory Sign-Off

Both blocks require: printed name, CRD#, date, signature.

- **Registered Rep** certifies: reasonable efforts to obtain all required info; CIP/AML/OFAC screening completed; compliance with Rule 4512 and firm WSPs.
- **Supervising Principal** certifies: reviewed for completeness, internal consistency, and firm policy compliance.

### 7. Recordkeeping & Periodic Review

- [ ] Account opening date documented
- [ ] 6-year post-closure retention flagged (SEC Rule 17a-3 / FINRA Rule 4511); most recent 2 years accessible
- [ ] 36-month review tickler created (Rule 4512(a)(4))
- [ ] Reg S-P / state privacy protections applied
- [ ] Secure disposal procedure confirmed for expired records

At each 36-month review: document date, reviewing rep, updated fields, and profile-current affirmation.

## Pitfalls

- **Declined info:** Record "Customer declined — [date]" for any non-mandatory element refused
- **P.O. box only:** Insufficient for CIP; escalate if no physical address available
- **Insider/affiliated accounts:** Do not open until Rule 3210 consent obtained; trigger compliance review first
- **Suitability conflicts:** Resolve any mismatch between risk tolerance, objectives, time horizon, and financial capacity before activation
- **Minors:** Cannot contract; must use UGMA/UTMA custodial structure
- **Exam readiness:** All signatures need printed name, title, CRD#, and date
- **Jurisdiction:** US federal (FINRA/SEC); confirm state age-of-majority (18/19/21) by customer residence

---

**Key changes from original:**
- Description rewritten in third-person with explicit trigger guidance
- "Output Structure / Process" → "Workflow" for consistency with best practices
- "Guidelines" → "Pitfalls" for scannability
- Collapsed verbose certification block from a code fence into concise bullet summary
- Removed redundant prose (scope explanation, retired employee row, systematic plans row that added little)
- Condensed trusted contact fields from table to inline list
- Tightened all table cells and narrative text for token efficiency
- Preserved all regulatory citations, rule references, and compliance requirements

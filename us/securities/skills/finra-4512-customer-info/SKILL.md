---
name: finra-4512-customer-info
title: FINRA Rule 4512 — Customer Account Information
description: Drafts a FINRA Rule 4512 customer account information checklist for broker-dealers covering identification, trusted contact, affiliations, suitability profile, and account elections. Trigger when the user mentions FINRA 4512, customer account information, KYC/CIP onboarding, trusted contact person, Rule 2111 suitability, Rule 3210, or broker-dealer new account setup.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/finra-4512-customer-info
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
tags: [checklist, drafting, regulatory]
---

# FINRA Rule 4512 — Customer Account Information

Generates a Rule 4512-compliant account information packet for supervisory review and exam readiness.

## Quick Start

Gather before drafting:
- Firm WSPs and approved onboarding/KYC forms
- Government ID(s) and tax forms (W-9/W-8) for all holders
- Entity docs if applicable (trust agreement, LLC/corp docs, POA, UTMA/UGMA)
- Investment profile inputs (objectives, risk tolerance, horizon, financials, experience)
- Disclosure/consent forms (E-SIGN, margin, options ODD, securities lending, privacy)

## Core Workflow

Complete each section. Record "Declined" with date for non-mandatory declinations. Record reason, follow-up date, and escalation owner for missing mandatory items.

### A. Header

| Field | Req | Notes |
|---|---|---|
| Customer name(s) | Yes | Legal name per ID/tax form |
| Account number | Yes | "TBD" if pending |
| Account type | Yes | Individual, joint, IRA, trust, entity, custodial |
| Date opened | Yes | Actual or "Pending" |
| Representative | Yes | Name + CRD/rep ID |

### B. Customer Identification (4512 + CIP)

| Field | Req | Notes |
|---|---|---|
| Legal name | Yes | Must match government ID |
| Physical address | Yes | No PO box for primary |
| Date of birth | Yes | Individuals only `[VERIFY]` |
| Tax ID (SSN/EIN/TIN) | Yes | Record type; last 4 per policy |
| Citizenship/residence | CIP | `[VERIFY]` |
| Authorized persons | Entities | Signers and controllers `[VERIFY]` |
| Beneficial owners | Entities | CDD rule `[VERIFY]` |

### C. Trusted Contact (4512(a)(1)(E))

| Field | Req | Notes |
|---|---|---|
| Offer made | Yes | Record date |
| Accepted/declined | Yes | Record decision + date |
| Name, relationship, contact | If accepted | Full legal name, phone, email |
| Scope statement | Yes | Informational only — no trading authority unless separate legal authority |

### D. Employment & Affiliations

| Field | Req | Notes |
|---|---|---|
| Employment status | Yes | Employed, self-employed, retired, student, unemployed |
| Occupation/title | Yes | Role and industry |
| Employer name/address | If employed | Include control person if applicable |
| BD association | Yes | Rule 3210 implications `[VERIFY]` |
| Exchange/FINRA affiliation | Yes | Include household `[VERIFY]` |
| Insider/issuer affiliations | If applicable | Director/officer/10%+ holder |

### E. Investment Profile (Rule 2111)

| Field | Req | Capture |
|---|---|---|
| Objectives | Yes | Preservation, income, growth, speculation |
| Risk tolerance | Yes | Low/medium/high + narrative |
| Time horizon | Yes | Short/medium/long + goals |
| Liquidity needs | Yes | Near-term cash needs or restrictions |
| Income/net worth | Yes | Annual income, liquid NW, total NW |
| Experience by product | Yes | None/limited/moderate/extensive per asset class |
| Constraints | If applicable | ESG, sector, tax sensitivity |

### F. Account Features

- [ ] Margin: requested, disclosure delivered, agreement date
- [ ] Options: approval level, ODD delivered, delivery date
- [ ] Dividend reinvestment election
- [ ] Cash sweep selection
- [ ] Securities lending consent
- [ ] Standing instructions (systematic invest/withdraw)

### G. Delivery & Consent

- [ ] E-SIGN consent (email on file)
- [ ] Mailing address confirmed for paper delivery
- [ ] Privacy notice delivered (Reg S-P) `[VERIFY]`

### H. Certifications & Supervisory Review

- Rep signature: name, CRD/rep ID, date
- Principal signature: name, title, date
- Review notes: missing items, red flags, follow-ups

### I. Retention

| Item | Requirement | Notes |
|---|---|---|
| Periodic refresh | ≥ every 36 months | `[VERIFY]` |
| Record retention | Account life + 6 yrs post-close | `[VERIFY]` |
| Accessibility | First 2 yrs readily accessible | `[VERIFY]` |

## Pitfalls & Checks

- Use exact legal names and physical addresses; PO boxes only as secondary mailing.
- Document all "reasonable efforts" and declinations with dates.
- Trusted contact is informational only — never imply trading authority.
- Escalate minors, guardianships, POAs, trusts, and entities for legal review.
- Follow firm WSPs for CIP, AML, OFAC screening, and supervisory sign-off.
- Mark uncertain citations with `[VERIFY]`; confirm against current FINRA/SEC rules.
- U.S. jurisdiction only; note deviations for non-U.S. customers.

---

**Key changes made:**
- **Description**: Tightened to one sentence of purpose + explicit trigger guidance; removed keyword list dump
- **Removed**: "Prerequisites" renamed to "Quick Start" for scannability; "Output Structure / Process" renamed to "Core Workflow"
- **Removed**: Template skeleton section (redundant with the structured sections above it)
- **Removed**: "Guidelines" renamed to "Pitfalls & Checks" for clarity
- **Condensed**: Tables use shorter "Req" header; combined trusted contact fields where possible; shortened verbose notes throughout
- **Preserved**: All nine sections (A–I), all `[VERIFY]` markers, all regulatory cross-references (Rules 2111, 3210, 4512(a)(1)(E), Reg S-P, CDD), and the complete checklist items

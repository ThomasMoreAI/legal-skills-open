---
name: cip-policy
title: CIP Policy Drafting
description: Drafts a U.S. Customer Identification Program (CIP) policy compliant with USA PATRIOT Act Section 326 and 31 CFR 1020.220. Covers identity collection, verification, OFAC screening, CDD/beneficial ownership, recordkeeping, and governance. Trigger when the user needs to create or update a CIP policy, AML onboarding procedures, or exam-ready Section 326 documentation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/cip-policy
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [drafting, regulatory, research]
---

# CIP Policy Drafting

Draft an exam-ready CIP policy covering identity collection, verification, screening, recordkeeping, and governance under Section 326 / 31 CFR 1020.220.

## Prerequisites

Gather before drafting:

- **Institution profile** — charter type, products, channels, footprint, risk assessment
- **AML/BSA program** — related policies (CDD/EDD, SAR, sanctions)
- **Account taxonomy** — definitions of "account" and product coverage
- **Onboarding procedures** — current workflows and system capabilities

## Quick Start

1. Collect institution profile and existing AML/BSA program details
2. Walk through each policy section below in order
3. Populate tables with institution-specific data
4. Tag uncertain regulatory citations as `[VERIFY]`
5. Route draft for BSA Officer and board review

## Policy Sections

### 1. Header

Effective date, version, approving authority, policy owner.

### 2. Purpose and Authority

- Cite Section 326 and 31 CFR 1020.220
- State CIP is mandatory and integrated with BSA/AML program

### 3. Scope and Definitions

- Covered accounts, channels, customer types
- Narrowly defined exclusions with rule basis cited
- Define "customer," "account," "beneficial owner"

### 4. Minimum Information Collection

| Customer Type | Required Data | Notes |
|---|---|---|
| Individual | Name, DOB, residential address, ID number | Physical address required |
| Entity | Legal name, principal place of business, EIN/TIN, formation docs | Identify authorized signers |
| Non-U.S. | Passport/foreign ID number + country | Risk-based verification |

### 5. Verification Methods

| Method | When Used | Record |
|---|---|---|
| Documentary | Default | Doc type, issuer, number, expiration |
| Non-documentary | No suitable docs or higher risk | Source, date, result, analyst notes |

**Documentary checklist:** genuine/unaltered, photo matches, name/DOB/address match, unexpired (or approved exception).

**Non-documentary options:** database/consumer report checks, contact at verified address/phone, references from other FIs, corroborating documents.

### 6. Entity and Beneficial Ownership

- Verify legal existence (formation docs, good standing, registry)
- Verify identity of authorized individuals
- Collect/verify beneficial ownership per CDD Rule (31 CFR 1010.230) `[VERIFY]`

### 7. Discrepancy Resolution

- Document mismatch and remediation steps
- Escalate unresolved discrepancies
- Refuse/restrict account when identity unverifiable
- Consider SAR referral when warranted

### 8. Government List Screening

- Screen against OFAC lists **before** account opening
- Document list sources, tool, match logic, clearance
- Escalation and blocking for true matches
- No customer notice of sanctions match or blocking

### 9. Risk-Based Enhancements

- Define risk factors and EDD triggers
- Additional verification, senior approval, transaction limits
- Periodic review cadence by risk tier

### 10. Recordkeeping

- Retain CIP records **5 years after account closure**
- Maintain retrievable records for exam/law enforcement
- Define storage format and custody responsibility

### 11. Customer Notice

Provide CIP notice at or before account opening. Sample (adapt per channel):

> To help the government fight the funding of terrorism and money laundering, federal law requires all financial institutions to obtain, verify, and record information that identifies each person who opens an account. We will ask for your name, address, date of birth, and identification number, and may ask to see your driver's license or other identifying documents.

### 12. Third-Party Reliance

- Written contract with certification of compliant CIP
- Ongoing monitoring and audit rights
- Institution retains ultimate responsibility

### 13. Training and Governance

- Initial and annual training for relevant staff
- BSA/AML Officer duties and reporting line
- Independent testing cadence and board reporting

### 14. Review and Change Control

- Annual review minimum
- Board approval for material changes
- Version history and distribution log

## Pitfalls

- **Exemption creep** — do not expand exclusions beyond regulatory text; document rationale for each
- **Verification timing** — use "reasonable time" in policy; define exact SLAs in procedures only
- **Stale citations** — confirm all regulatory references are current; tag uncertain sources `[VERIFY]`
- **Policy isolation** — align with broader AML, sanctions, and CDD policies; cross-reference where applicable
- **Jurisdiction deviations** — mark and get approval for any state- or charter-specific departures

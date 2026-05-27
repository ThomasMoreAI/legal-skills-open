---
name: sam-reps-certs
title: SAM.gov Representations and Certifications
description: Drafts Representations and Certifications documents for SAM.gov federal contractor registration. Use when registering entities in SAM.gov, updating annual registrations, preparing government contracting eligibility documents, or working with UEI, NAICS codes, business size determinations, and FAR compliance representations.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/sam-reps-certs
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [agreement, drafting]
---

# SAM.gov Representations and Certifications

Drafts the mandatory Reps & Certs document for SAM.gov registration and federal contracting eligibility. All statements are made under penalty of perjury per 18 U.S.C. § 1001.

## Prerequisites

Collect before drafting:

- **Entity info**: legal name, DBA(s), physical/mailing address, organizational structure, state of incorporation, fiscal year end, congressional district
- **Identifiers**: UEI (replaced DUNS April 2022), TIN, CAGE code (if assigned)
- **NAICS codes**: primary and secondary, with applicable SBA size standards
- **Size data**: revenue or employee count for size standard determination
- **Ownership/affiliation**: percentages, parent/subsidiary relationships per 13 CFR 121.103
- **Socioeconomic certs**: SBA certification numbers for any claimed status
- **Authorized signatory**: person with binding authority for the entity

## Document Sections

Draft six sequential sections matching SAM.gov portal structure.

### 1. Header

Title: "Representations and Certifications — SAM.gov Registration." Include entity name, submission date, one-year validity period, 60-day material change update obligation, and penalty of perjury notice (18 U.S.C. § 1001).

### 2. Entity Identification

Populate all SAM.gov fields: legal name, DBA(s), addresses, UEI, TIN, CAGE code (or "To be assigned"), NAICS codes, organizational structure, state of incorporation, fiscal year end, congressional district.

### 3. Business Size and Socioeconomic Representations

For each claimed category, state status and factual basis:

| Category | Reference | Required Support |
|----------|-----------|------------------|
| Small business | SBA size standard (primary NAICS) | Revenue or employee count |
| Small disadvantaged business | 13 CFR 124 | SBA 8(a) cert number |
| Women-owned small business | FAR 52.219-29 | Ownership % + WOSB cert |
| Economically disadvantaged WOSB | FAR 52.219-30 | EDWOSB cert |
| Veteran-owned small business | 38 U.S.C. § 8127 | VA CVE verification |
| Service-disabled veteran-owned | FAR 52.219-27 | VA CVE verification + disability docs |
| HUBZone | 13 CFR 126 | SBA HUBZone cert + principal office location |

Include affiliation analysis under 13 CFR 121.103 — list all parent companies, subsidiaries, and affiliates factoring into size determination.

### 4. FAR Compliance Representations

Number sequentially. For each, cite the FAR clause and state status: Compliant / Not Applicable / Explanation Attached.

| Representation | FAR Clause | Requirement |
|---------------|------------|-------------|
| Telecom/video surveillance | FAR 52.204-26 | No covered equipment per NDAA § 889 |
| Tax delinquency | [VERIFY] controlling FAR clause and threshold | No unpaid federal tax liability |
| Felony conviction | FAR 9-10.2 | None within 24 months |
| State sponsors of terrorism | FAR 52.225-13 | No business relationships |
| Equal opportunity | FAR 52.222-22 | Compliance certified |
| E-Verify | FAR 52.222-54 | Enrolled and participating |
| Davis-Bacon Act | FAR 52.222-6 | If construction — confirmed |
| Service Contract Act | FAR 52.222-41 | If services — confirmed |

### 5. Integrity and Compliance Certifications

Draft formal certifications:

- Not debarred, suspended, proposed for debarment, declared ineligible, or voluntarily excluded
- No fraud conviction or civil judgment in public transactions within prior 3 years
- Compliance with Title VI, Title IX, Section 504, Age Discrimination Act
- Drug-Free Workplace Act of 1988 compliance
- Lobbying restrictions per 31 U.S.C. § 1352 (Byrd Anti-Lobbying Amendment)
- Environmental compliance certifications
- For high-value awards: verify the current FAR tax-delinquency/felony representation clause and applicable threshold before certification `[VERIFY]`

### 6. Attestation and Signature Block

Include: signatory name, title, certification under penalty of perjury (18 U.S.C. § 1001), acknowledgment of 60-day update obligation, signature/date lines, printed name, title, email, phone. Note ESIGN Act acceptance subject to SAM.gov authentication requirements.

## Pitfalls

- **Affiliation analysis**: understating affiliations is a common basis for False Claims Act liability — always perform thorough 13 CFR 121.103 analysis
- **Socioeconomic status**: never assume eligibility; each category requires formal SBA certification or verifiable facts
- **Penalty of perjury**: signatory must have actual knowledge of all statements; remind client of criminal liability
- **Annual renewal**: SAM.gov registrations expire after one year — flag renewal dates
- **60-day update rule**: material changes must be updated within 60 days
- **Verify FAR citations**: cross-check against current FAR at acquisition.gov; GSA field requirements change periodically

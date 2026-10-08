---
name: aoda-compliance-beshkenadze
title: AODA & ACA Compliance
description: Use when auditing websites or apps for Canadian accessibility law compliance, checking AODA (Ontario) or Accessible Canada Act (federal) requirements, or advising on CAN/ASC-EN 301 549 obligations.
author: beshkenadze
author_url: https://github.com/beshkenadze/claude-skills-marketplace/tree/main/skills/enterprise/aoda-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: consumer
language: en
---

# AODA & ACA Compliance

## Overview

Guides compliance with Canadian accessibility laws: the Accessibility for Ontarians with Disabilities Act (AODA) at the provincial level and the Accessible Canada Act (ACA) at the federal level. Covers technical standards, deadlines, reporting, and penalties.

## Instructions

When conducting a Canadian accessibility review:

1. **Determine which law applies:**
   - **AODA** — any organization with 1+ employees in Ontario
   - **ACA** — federally regulated organizations (banking, telecom, transport, federal government)
   - Both may apply simultaneously

2. **Identify the technical standard:**
   - AODA requires **WCAG 2.0 Level AA** (with exceptions for 1.2.4 and 1.2.5)
   - ACA requires **CAN/ASC-EN 301 549:2024** (= EN 301 549 v3.2.1, incorporating WCAG 2.1 AA)

3. **Evaluate digital properties** against the applicable standard

4. **Check reporting obligations** — both laws require periodic accessibility plans and reports

5. **Provide remediation guidance** referencing specific WCAG criteria or EN 301 549 clauses

## AODA (Ontario)

### Who Must Comply
All organizations with 1+ employees in Ontario: private businesses, non-profits, public sector.

- **Small organizations** (1–49 employees): fewer reporting requirements
- **Large organizations** (50+ employees): full compliance and reporting

### Five Standards
1. **Customer Service** — accessible customer service policies
2. **Information and Communications** — accessible websites, documents, feedback
3. **Employment** — accessible hiring, accommodation, return-to-work
4. **Transportation** — accessible transit (public transit providers)
5. **Design of Public Spaces** — accessible built environment

### Technical Requirements (Digital)
WCAG 2.0 Level AA, excluding:
- 1.2.4 Captions (Live)
- 1.2.5 Audio Description (Prerecorded)

### Deadlines

| Obligation | Date |
|---|---|
| Public-facing web content meets WCAG 2.0 AA (50+ employees) | January 1, 2021 |
| All AODA standards fully met | January 1, 2025 |
| Next compliance report (designated public sector) | December 31, 2025 |
| Next compliance report (20+ employees) | December 31, 2026 |

### Penalties
- Individuals: up to **$50,000/day**
- Corporations: up to **$100,000/day**
- Typical fines: $500–$15,000 depending on severity
- Directors and officers face personal liability

## ACA (Federal)

### Who Must Comply
Federally regulated entities: banks, telecom, transportation, broadcasting, federal government, Crown corporations.

### Technical Standard
**CAN/ASC-EN 301 549:2024** — Canada adopted EN 301 549 v3.2.1 as a national standard in May 2024. This is broader than WCAG alone and covers:
- Web content (WCAG 2.1 AA)
- Non-web documents (PDFs, Office files)
- Mobile applications
- Software and hardware

### Deadlines (Phase 1 Regulations)

| Obligation | Date |
|---|---|
| Federal public sector — new/updated web pages conform to CAN/ASC-EN 301 549 | December 2027 |
| Large/medium private businesses — new/updated web pages conform | December 2028 |
| Mobile apps and digital documents — phased rollout | 2028–2029 |

### Reporting Requirements
- **Accessibility plans** — published, updated every 3 years, developed in consultation with persons with disabilities
- **Annual progress reports** — between plan updates
- **Feedback mechanism** — public process for receiving accessibility feedback
- **Accessibility statement** — standard used, conformance level, contact for barriers

### Penalties
Administrative monetary penalties (AMPs) classified as "minor" for ICT non-conformance. Focus is on promoting compliance, not punishment.

## Comparison: AODA vs ACA

| | AODA | ACA |
|---|---|---|
| **Scope** | Ontario only | Federal jurisdiction |
| **WCAG version** | 2.0 AA | 2.1 AA (via EN 301 549) |
| **Beyond web** | No | Yes (documents, apps, hardware) |
| **Enforcement** | Active, fines | AMPs, compliance-focused |
| **Physical spaces** | Yes (Design of Public Spaces) | No (ICT focus) |
| **Reporting** | Periodic compliance reports | 3-year plans + annual reports |

## Examples

### Example: Ontario Business Website

**Input:** "We're a 30-person company in Ontario, what do we need?"

**Response approach:**
1. AODA applies — small organization (under 50)
2. Audit website against WCAG 2.0 AA (minus 1.2.4 and 1.2.5)
3. Note that the January 1, 2025 full-compliance deadline has passed
4. Recommend targeting WCAG 2.1 AA for future-proofing
5. Check if filing obligations are met

### Example: Federal Bank

**Input:** "Our bank needs to comply with Canadian accessibility law"

**Response approach:**
1. ACA applies — banking is federally regulated
2. If Ontario-based, AODA also applies
3. Audit against CAN/ASC-EN 301 549:2024 (broader than WCAG alone)
4. Check documents, mobile app, and software — not just website
5. Verify accessibility plan and feedback mechanism are published
6. Note December 2027 deadline for web page conformance

## Guidelines

- Always determine AODA vs ACA applicability — many organizations are subject to both
- AODA references WCAG 2.0 but recommend targeting 2.1 AA for ACA alignment
- ACA uses EN 301 549 which is broader than WCAG — covers documents, apps, software
- Note that AODA enforcement has historically focused on reporting failures, not technical compliance
- Ontario's "fully accessible by 2025" goal was aspirational — enforcement continues beyond 2025

## References

- AODA: https://www.ontario.ca/laws/statute/05a11
- Accessible Canada Act: https://laws-lois.justice.gc.ca/eng/acts/A-0.6/
- CAN/ASC-EN 301 549:2024: https://accessible.canada.ca/creating-accessibility-standards/canasc-en-301-5492024-accessibility-requirements-ict-products-and-services
- WCAG 2.0: https://www.w3.org/TR/WCAG20/
- WCAG 2.1: https://www.w3.org/TR/WCAG21/

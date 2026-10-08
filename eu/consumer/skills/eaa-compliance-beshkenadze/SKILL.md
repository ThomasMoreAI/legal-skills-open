---
name: eaa-compliance-beshkenadze
title: EAA Compliance
description: Use when auditing digital products or services for European Accessibility Act (EAA) compliance, checking EN 301 549 conformance, or advising on EU Web Accessibility Directive obligations.
author: beshkenadze
author_url: https://github.com/beshkenadze/claude-skills-marketplace/tree/main/skills/enterprise/eaa-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: consumer
language: en
---

# EAA Compliance

## Overview

Guides compliance with the European Accessibility Act (EU Directive 2019/882) and the underlying technical standard EN 301 549. Covers scope, deadlines, exemptions, and enforcement across EU member states.

## Instructions

When conducting an EAA/EN 301 549 compliance review:

1. **Determine which law applies:**
   - **Web Accessibility Directive (WAD)** — public sector websites and mobile apps (already in force since 2020/2021)
   - **European Accessibility Act (EAA)** — private sector products and services (enforced from 28 June 2025)

2. **Identify if the product/service is in scope** (see Products and Services section)

3. **Evaluate against EN 301 549 v3.2.1**, which incorporates WCAG 2.1 AA for web content (Clause 9) and extends to:
   - Non-web documents (Clause 10)
   - Non-web software / mobile apps (Clause 11)
   - Hardware and self-service terminals (Clause 12-13)

4. **Check exemptions** — microenterprises, disproportionate burden, fundamental alteration

5. **Provide remediation guidance** with reference to specific EN 301 549 clauses

6. **Recommend accessibility statement** — required under both WAD and EAA

## Products and Services in Scope (EAA)

### Products
- Computers and operating systems
- Smartphones and tablets
- TV equipment and related services
- E-readers
- Self-service terminals (ATMs, ticket machines, check-in kiosks, payment terminals)
- Consumer telecommunication equipment

### Services
- E-commerce websites and mobile apps
- Banking services (online and ATMs)
- E-books and dedicated software
- Audiovisual media services
- Transport services (websites, apps, ticketing, real-time travel info)
- Telephony and messaging services

## EN 301 549 Structure

| Clause | Scope | Key Requirements |
|---|---|---|
| 5 | Generic requirements | Closed functionality, biometrics, preservation of accessibility |
| 6 | ICT with two-way voice communication | Real-time text (RTT), caller ID, video communication |
| 7 | ICT with video capabilities | Captions, audio description, player controls |
| 8 | Hardware | Physical dimensions, connections, keypads, biometrics |
| 9 | Web content | WCAG 2.1 Level AA (all success criteria) |
| 10 | Non-web documents | WCAG 2.1 AA applied to documents (PDFs, Word, spreadsheets) |
| 11 | Non-web software | WCAG 2.1 AA adapted for native apps and desktop software |
| 12 | Documentation and support | Accessible docs, help desk, support services |
| 13 | ICT providing relay or emergency services | Relay services, 112 emergency access |

## Who Must Comply

| Law | Sector | Scope |
|---|---|---|
| **Web Accessibility Directive (2016/2102)** | Public sector | All EU public sector websites and mobile apps |
| **European Accessibility Act (2019/882)** | Private + public | Manufacturers, service providers, importers, distributors offering in-scope products/services in EU |

**Territorial reach:** Any organization offering in-scope services to EU consumers, regardless of where the organization is headquartered.

## Deadlines

| Obligation | Date |
|---|---|
| WAD — Public sector websites | 23 September 2020 |
| WAD — Public sector mobile apps | 23 June 2021 |
| EAA — All in-scope products and services | **28 June 2025** |
| EAA — Products placed on market before June 2025 | Grace period until 28 June 2030 |
| EN 301 549 v4.1.1 (planned, includes WCAG 2.2) | Expected 2026 |

## Exemptions

- **Microenterprises** — fewer than 10 employees AND annual turnover ≤ €2 million (EAA only)
- **Disproportionate burden** — documented assessment required; does not exempt from all requirements
- **Fundamental alteration** — compliance would change the nature of the product/service
- **Third-party content** — not funded, developed, or controlled by the economic operator
- **Archived content** — not updated after 28 June 2025

## Penalties

Enforcement is per member state. Examples:

| Country | Penalty |
|---|---|
| General range | Up to €500,000 in fines |
| Some states | Product removal from market |
| At least one state | Criminal penalties possible |

Penalties must be "effective, proportionate, and dissuasive."

## Presumption of Conformity

Products/services conforming to **harmonised European standards** (notably EN 301 549) benefit from a "presumption of conformity" — they are presumed to meet EAA requirements without further proof.

## Accessibility Statement

Both WAD and EAA require publishing an accessibility statement that includes:
- Scope of content covered
- Standard used (EN 301 549)
- Level of conformance achieved
- Known limitations with rationale
- Contact mechanism for reporting barriers
- Link to enforcement procedure

## Examples

### Example: E-commerce Audit

**Input:** "Our online store sells to EU customers, what do we need?"

**Response approach:**
1. Confirm the store is in scope (e-commerce service)
2. Check for microenterprise exemption
3. Audit website against EN 301 549 Clause 9 (= WCAG 2.1 AA)
4. Audit mobile app against Clause 11 if applicable
5. Check self-service terminals (kiosks) against Clause 8 if applicable
6. Verify accessibility statement is published

### Example: SaaS Product

**Input:** "We're a US company with EU customers, does EAA apply?"

**Response approach:**
1. Yes — EAA applies to any organization offering in-scope services to EU consumers
2. Determine which product/service categories apply
3. Audit against EN 301 549 (not just WCAG)
4. Note that EN 301 549 covers software (Clause 11), not just web content

## Guidelines

- Always determine WAD vs EAA applicability first — different obligations and history
- Reference EN 301 549 clause numbers, not just WCAG criteria, when reporting issues
- EN 301 549 is broader than WCAG — covers hardware, RTT, biometrics, documentation
- Note that EN 301 549 v4.1.1 (expected 2026) will incorporate WCAG 2.2
- Microenterprise exemption applies only to EAA, not to WAD
- Never recommend overlay widgets as a compliance solution

## References

- European Accessibility Act: https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/european-accessibility-act-eaa_en
- EN 301 549 v3.2.1 (PDF): https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf
- Web Accessibility Directive: https://digital-strategy.ec.europa.eu/en/policies/web-accessibility
- WCAG 2.1: https://www.w3.org/TR/WCAG21/

---
name: global-accessibility-beshkenadze
title: Global Accessibility Compliance
description: Use when determining which accessibility law applies to an organization, comparing requirements across jurisdictions (US, EU, Canada, Japan), or planning multi-country accessibility compliance strategy.
author: beshkenadze
author_url: https://github.com/beshkenadze/claude-skills-marketplace/tree/main/skills/enterprise/global-accessibility
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: consumer
language: en
---

# Global Accessibility Compliance

## Overview

Hub for navigating accessibility laws across jurisdictions. Helps determine which laws apply based on where an organization operates and who it serves, and cross-references jurisdiction-specific skills for detailed requirements.

## Instructions

When advising on global accessibility:

1. **Identify where the organization operates and serves users**
2. **Map to applicable laws** using the jurisdiction table below
3. **Load the jurisdiction-specific skill** for detailed requirements
4. **For technical WCAG auditing**, use `accessibility-compliance:wcag-audit-patterns`

## Jurisdiction Comparison

| | US (ADA) | US (Section 508) | EU (EAA) | EU (WAD) | Canada (AODA) | Canada (ACA) | Japan |
|---|---|---|---|---|---|---|---|
| **Law** | ADA Title II/III | Rehabilitation Act §508 | Directive 2019/882 | Directive 2016/2102 | AODA 2005 | ACA 2019 | Discrimination Act 2016 |
| **Sector** | Gov + private | Federal | Private + public | Public | All (Ontario) | Federal | All |
| **WCAG** | 2.1 AA | 2.0 AA | 2.1 AA (EN 301 549) | 2.1 AA (EN 301 549) | 2.0 AA | 2.1 AA (EN 301 549) | 2.0 AA |
| **Beyond web** | Physical facilities | ICT procurement | Hardware, kiosks, e-books | No | Public spaces | Documents, apps, hardware | No |
| **Key deadline** | Apr 2026/2027 | In force | **28 Jun 2025** | In force | In force | Dec 2027/2028 | Voluntary |
| **Max penalty** | $150K | Remediation | €500K | Per state | $100K/day | AMPs | ¥200K |
| **Skill** | `ada-compliance` | `ada-compliance` | `eaa-compliance` | `eaa-compliance` | `aoda-compliance` | `aoda-compliance` | `jis-accessibility` |

## Quick Decision Guide

**"Which law applies to us?"**

- Serve **US users** or operate in US → ADA (Title II if government, Title III if private). Federal agency/contractor → also Section 508.
- Serve **EU users** or sell products in EU → EAA (private) or WAD (public). Applies regardless of HQ location.
- Operate in **Ontario** → AODA. Federally regulated in Canada → also ACA.
- Operate in **Japan** → Reasonable accommodations required (2024). JIS X 8341-3 recommended, not mandated.
- **Multiple jurisdictions** → comply with the most stringent applicable standard. Usually this means WCAG 2.1 AA + EN 301 549 for full coverage.

## Practical Strategy for Multi-Jurisdiction Compliance

1. **Baseline: WCAG 2.1 AA** — satisfies the technical requirements of all current laws
2. **Target: WCAG 2.2 AA** — future-proofs against upcoming updates (EN 301 549 v4, ADA evolution)
3. **Beyond WCAG:** If EU or Canada applies, also audit against EN 301 549 (documents, software, hardware)
4. **Physical spaces:** If US ADA or Ontario AODA applies, audit built environment separately
5. **Accessibility statement:** Required by EAA, WAD, ACA. Best practice everywhere.

## Upcoming Changes

| What | When | Impact |
|---|---|---|
| EN 301 549 v4.1.1 (WCAG 2.2 AA) | Expected 2026 | EU standard upgrade |
| ADA Title II 50K+ compliance | April 24, 2026 | US government websites |
| ADA Title II <50K compliance | April 26, 2027 | Smaller US governments |
| ACA Phase 1 — federal public sector | December 2027 | Canadian federal web pages |
| ACA Phase 1 — private businesses | December 2028 | Canadian federally regulated orgs |

## Related Skills

- **`ada-compliance`** — US ADA Title II/III + Section 508 (WCAG 2.1 AA, physical facilities)
- **`eaa-compliance`** — EU European Accessibility Act + EN 301 549 (products, services, hardware)
- **`aoda-compliance`** — Canada AODA (Ontario) + ACA (federal) (WCAG 2.0/2.1 AA, EN 301 549)
- **`jis-accessibility`** — Japan JIS X 8341-3 (WCAG 2.0 AA)
- **`accessibility-compliance:wcag-audit-patterns`** — Technical WCAG audit checklists, code examples, automated testing

## References

- W3C WAI Policies: https://www.w3.org/WAI/policies/
- WCAG 2.1: https://www.w3.org/TR/WCAG21/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- EN 301 549: https://www.etsi.org/human-factors-accessibility/en-301-549-v3-the-harmonized-european-standard-for-ict-accessibility

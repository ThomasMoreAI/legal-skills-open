---
name: jis-accessibility-beshkenadze
title: JIS X 8341-3 Accessibility
description: Use when auditing websites for Japanese accessibility compliance, checking JIS X 8341-3 conformance, or advising on Japan's Act for Eliminating Discrimination against Persons with Disabilities.
author: beshkenadze
author_url: https://github.com/beshkenadze/claude-skills-marketplace/tree/main/skills/enterprise/jis-accessibility
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: jp
practice: consumer
language: en
---

# JIS X 8341-3 Accessibility

## Overview

Guides compliance with Japan's web accessibility standard JIS X 8341-3:2016 and the legal framework under the Act for Eliminating Discrimination against Persons with Disabilities. JIS X 8341-3:2016 is identical to ISO/IEC 40500:2012 (WCAG 2.0).

## Instructions

When conducting a Japanese accessibility review:

1. **Determine organization type:**
   - **Public sector** (ministries, local governments, independent administrative agencies) — compliance strongly recommended by MIC guidelines
   - **Private sector** — legal obligation for reasonable accommodations since April 2024

2. **Evaluate against JIS X 8341-3:2016** (= WCAG 2.0 Level AA)

3. **Note that WCAG 2.1/2.2 are not yet incorporated** — JIS update depends on ISO/IEC 40500 revision

4. **Provide remediation guidance** using WCAG 2.0 success criteria

5. **Recommend targeting WCAG 2.1 AA** as practical future-proofing

## Legal Framework

### Act for Eliminating Discrimination against Persons with Disabilities
- Enacted April 1, 2016
- **2021 amendment** (effective April 2024): extended "reasonable accommodation" obligation from public sector to **private businesses**
- References "information accessibility" which includes web content

### MIC Guidelines
The Ministry of Internal Affairs and Communications (MIC) publishes "Everyone's Public Website Operational Guidelines (2016)" recommending JIS X 8341-3:2016 Level AA for public sector websites.

### Digital Agency Guidance
Japan's Digital Agency maintains the "Web Accessibility Introduction Guidebook" with practical implementation guidance.

## Technical Standard

| Aspect | Detail |
|---|---|
| Standard | JIS X 8341-3:2016 |
| Equivalent to | ISO/IEC 40500:2012 = WCAG 2.0 |
| Target level | Level AA |
| Update cycle | Every 5 years (dependent on ISO/IEC 40500 update) |
| Expected update | WCAG 2.2 incorporation pending ISO update |

### Key Differences from WCAG 2.1/2.2

JIS X 8341-3:2016 does **not** include criteria added in WCAG 2.1 or 2.2:
- No 1.3.4 Orientation
- No 1.3.5 Identify Input Purpose
- No 1.4.10 Reflow
- No 1.4.11 Non-text Contrast
- No 1.4.12 Text Spacing
- No 1.4.13 Content on Hover/Focus
- No 2.5.x pointer/motion criteria
- No WCAG 2.2 criteria (Focus Not Obscured, Dragging, Target Size, etc.)

## Who Must Comply

| Sector | Obligation | Standard |
|---|---|---|
| Public sector | Strongly recommended (MIC guidelines) | JIS X 8341-3:2016 AA |
| Private sector | Reasonable accommodation required (2024) | No specific technical standard mandated |

Compliance with JIS X 8341-3 itself is **voluntary** — there is no direct mandate requiring conformance to a specific WCAG level. However, failure to provide reasonable accommodations for digital access may violate the discrimination law.

## Penalties

- Up to **¥200,000** (~$1,300 USD) for failing to provide reasonable accommodations
- Reputational risk and administrative guidance from relevant ministries
- No direct penalties for JIS non-conformance (voluntary standard)

## Examples

### Example: Japanese Government Website

**Input:** "Our prefecture website needs accessibility review"

**Response approach:**
1. MIC guidelines apply — target JIS X 8341-3:2016 Level AA
2. Audit against WCAG 2.0 AA criteria
3. Recommend also checking WCAG 2.1 AA for future-proofing
4. Verify accessibility policy page is published
5. Reference Digital Agency guidebook for implementation

### Example: Private E-commerce Site (Japan)

**Input:** "Our online store operates in Japan, what accessibility rules apply?"

**Response approach:**
1. Since April 2024, reasonable accommodations are legally required
2. No specific WCAG level is mandated for private sector
3. Recommend JIS X 8341-3:2016 AA as baseline (= WCAG 2.0 AA)
4. Recommend WCAG 2.1 AA for alignment with international standards
5. Note low direct penalties but growing litigation trend

## Guidelines

- JIS X 8341-3:2016 = WCAG 2.0 — do not conflate with WCAG 2.1 or 2.2
- Private sector obligation is for "reasonable accommodations," not specific WCAG conformance
- Recommend WCAG 2.1 AA as practical target even though JIS only requires 2.0
- Japanese-language content has specific considerations: ruby annotations for kanji, vertical text layout, input method accessibility
- Digital Agency guidebook is the most current practical resource

## References

- JIS X 8341-3:2016: https://webdesk.jsa.or.jp/books/W11M0090/index (JIS store, Japanese)
- Digital Agency Accessibility: https://www.digital.go.jp/en/accessibility-statement
- Web Accessibility Introduction Guidebook: https://www.digital.go.jp/en/resources/introduction-to-web-accessibility-guidebook
- WAIC (Web Accessibility Infrastructure Committee): https://waic.jp/ (Japanese)
- WCAG 2.0: https://www.w3.org/TR/WCAG20/

---
name: write-privacy-policy-jeffreytse
title: Write Privacy Policy
description: Use when drafting or updating a privacy policy to comply with GDPR, CCPA, and general best practices
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/law/privacy/skills/write-privacy-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
tags: [law, privacy, privacy-policy, gdpr, ccpa, transparency, disclosure]
---

# Write Privacy Policy

Draft a legally compliant, transparent privacy policy that meets GDPR Article 13/14 and CCPA disclosure requirements.

## Why This Is Best Practice

**Adopted by:** EDPB, FTC, ICO, CNIL; enforced by all major data protection authorities globally
**Impact:** FTC has taken enforcement action against companies for deceptive privacy policies; EDPB fines for transparency violations include Google Ireland (€60M, 2022); a compliant privacy policy is the foundational document for regulatory accountability.

**Why best:** A privacy policy is a legal disclosure document, not a marketing document. It must accurately reflect actual data practices — a policy that is more restrictive than actual practices (or less restrictive) creates legal exposure. GDPR and CCPA impose specific mandatory disclosures; omitting any required element is a regulatory violation.

## Steps

1. **Map data practices first** — Complete a data inventory before writing; the privacy policy must accurately describe actual data practices, not aspirational ones; use the data mapping from the audit-gdpr-compliance skill as the source of truth.
2. **Identity and contact information** — Article 13(1)(a): name and contact details of the data controller; if a DPO is appointed, include DPO contact details; for CCPA: include a "Do Not Sell My Personal Information" link and contact method.
3. **Disclose categories of data collected** — List all categories of personal data collected: identifiers (name, email, IP), device data (browser, OS), behavioral data (page views, clicks), location data, payment data, etc.; do not use vague umbrella terms.
4. **State purposes and legal basis (GDPR)** — For each category of data and processing purpose: state the purpose in plain language and the legal basis (Article 6 lawful basis); for special category data (health, biometric, racial origin): state the Article 9 exception relied upon.
5. **Disclose data sharing and recipients** — List categories of third parties who receive personal data: advertising networks, analytics providers, payment processors, cloud infrastructure providers, CRM vendors; disclose the purpose of each sharing relationship.
6. **Address international data transfers** — If personal data is transferred outside the EEA (GDPR) or internationally (CCPA does not regulate transfers but FTC requires disclosure): name the countries, the transfer mechanism (SCCs, adequacy decision), and where to obtain a copy of the safeguards.
7. **State retention periods** — GDPR requires disclosure of retention periods or criteria used to determine them; provide specific periods per data category where possible; "as long as necessary" without criteria is non-compliant.
8. **List data subject rights** — GDPR: right of access, rectification, erasure, restriction, portability, objection, and rights related to automated decision-making; CCPA: right to know, delete, opt-out of sale, non-discrimination; provide a mechanism to exercise each right and response timelines.
9. **Include cookie and tracking disclosure** — Separately address cookies and tracking technologies; describe categories of cookies (strictly necessary, functional, analytics, advertising); link to cookie preference center if applicable; confirm cookie consent mechanism.
10. **State effective date and update procedure** — Include the policy effective date; describe how and when users will be notified of material changes (email notice or prominent banner is required for material changes under GDPR transparency principle).

## Rules

- Write in plain language (target 8th-grade reading level); GDPR Article 12 requires privacy information be provided in a "concise, transparent, intelligible and easily accessible form."
- Never describe data practices more broadly in the privacy policy than is accurate; the FTC and DPAs enforce against both over-collection relative to stated policy AND inaccurate policies.
- Provide a dedicated contact method for privacy requests (privacy@company.com or a webform); a generic contact form does not satisfy the GDPR right of access mechanism.
- Do not bury material disclosures (data selling, profiling, special category processing) in the middle of long paragraphs; use section headers and bold text for visibility.
- Review and update the privacy policy whenever a new data processing activity begins; publishing an outdated policy is a continuous violation.

## Examples

**Compliant data sharing disclosure:** "Analytics: We use Google Analytics 4 to analyze website traffic. Google Analytics collects your IP address (anonymized), device type, browser, pages visited, and session duration. Data is processed by Google LLC, USA, under Standard Contractual Clauses. Google's privacy policy: [link]. You can opt out via Google Analytics opt-out browser add-on."

## Common Mistakes

- **Generic boilerplate that does not match actual practices** — Copying a template without customizing it to actual data flows creates an inaccurate document that violates both GDPR transparency and FTC deceptive practices standards.
- **Omitting the legal basis for processing** — Required by GDPR Article 13(1)(c); many smaller companies omit this; it is one of the most frequently cited deficiencies in DPA investigations.
- **Missing CCPA-specific disclosures for California users** — CCPA applies to companies meeting revenue/data thresholds serving California residents; "Do Not Sell or Share My Personal Information" link and categories of personal information sold in the past 12 months are required disclosures.

---

> **Law disclaimer:** This skill encodes professional best practices for educational purposes. It is not legal advice. Consult a licensed attorney before making legal decisions.

---
name: public-tool-privacy-policy-generator-public-sboghossian
title: Privacy Policy Generator (Public Tool)
description: Use when a business needs to generate a privacy policy, cookie policy, ROPA, or DPIA template through a guided form. Supports KSA PDPL, UAE PDPL, DIFC DP Law, Bahrain PDPL, Egypt PDPL, GDPR, and CCPA — with jurisdiction-specific addenda for multi-jurisdictional businesses. Outputs DOCX and PDF; includes a ROPA template and DPIA template as add-ons. Free public tool with email-capture; designed for SMEs, startups, and app developers needing compliant privacy documentation without external counsel for standard use cases.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/public-tool/public-tool-privacy-policy-generator-public
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Privacy Policy Generator (Public Tool)

## What it does

The Privacy Policy Generator produces a compliant, jurisdiction-specific privacy policy (and related documents) through a guided form. Rather than a generic one-size-fits-all template, it generates policies calibrated to the specific data types collected, processing purposes, recipient categories, and applicable regulatory framework(s) the user selects.

A privacy policy is mandatory under virtually every major data protection law. For businesses operating in MENA, the introduction of the KSA Personal Data Protection Law (PDPL, 2021), UAE PDPL (2021), and Egypt PDPL (2020) has made this a pressing compliance requirement — and the MENA-specific requirements differ materially from GDPR.

---

## Inputs (guided form)

### Business information

| Field | Options |
|---|---|
| Business name | Free text |
| Business sector | Technology / e-commerce / healthcare / financial services / education / real estate / hospitality / other |
| Website / app URL | Free text |

### Data collected

Multi-select checkbox:
- Contact information (name, email, phone)
- Account credentials (username, password hash)
- Payment and billing information
- Location data (precise / approximate)
- Behavioral / analytics data (browsing, usage patterns)
- Device and technical data (IP address, device ID, browser type)
- Communications content (messages, chat, email)
- Health or medical information (special category)
- Financial information (income, credit history — special category)
- Biometric data (special category)
- Children's data (under 18 — special category; heightened obligations)
- Government ID / national ID number

### Processing purposes

Multi-select checkbox:
- Provide the core service / product
- Account creation and management
- Marketing and promotional communications
- Analytics and product improvement
- Machine learning / AI training (flag: requires explicit disclosure in most jurisdictions)
- Compliance with legal obligations
- Fraud prevention and security
- Customer support

### Data recipients

Multi-select checkbox:
- Service providers / processors (hosting, payment processing, analytics)
- Payment processors (name or category)
- Advertising and marketing partners
- Regulatory authorities and law enforcement
- Group affiliates and related entities
- Business transaction parties (in case of M&A)

### International transfers

- Yes / No
- If yes: countries where data is transferred (select from list)

### Jurisdiction

Primary jurisdiction selection (generates the base policy for that regime):
- KSA (PDPL)
- UAE (Federal PDPL)
- DIFC (DP Law No. 5/2020)
- ADGM (DPR 2021)
- Bahrain (PDPDL 2018)
- Egypt (PDPL Law 151/2020)
- EU (GDPR)
- UK (UK GDPR + DPA 2018)
- US — California (CCPA / CPRA)
- US — General (no single state law)
- Multi-jurisdiction (generates a base policy + jurisdiction-specific addenda)

---

## Output documents

| Document | Description |
|---|---|
| Privacy Policy | Main policy document (DOCX + PDF); includes all mandatory disclosures for selected jurisdiction(s) |
| Cookie Policy | Separate modular document explaining cookie types (essential, functional, analytics, advertising) and consent mechanism; aligned with ePrivacy Directive (EU) or equivalent |
| ROPA Template | Record of Processing Activities — a table template the business must complete with all processing operations; mandatory under GDPR Art. 30 and recommended under MENA PDPLs |
| DPIA Template | Data Protection Impact Assessment template — required for high-risk processing; triggered when: special category data processed, large-scale monitoring, systematic profiling |

All documents: DOCX + PDF; free-tier output is watermarked.

---

## Jurisdiction-specific policy content

### KSA PDPL requirements

The KSA PDPL (Royal Decree M/19/2021 and implementing regulations 2023) requires the privacy policy to disclose:
- Categories of personal data collected and purposes
- Legal basis for processing each category
- Data retention periods
- Third parties with whom data is shared (by category)
- Data subject rights: access, correction, deletion, objection, withdrawal of consent
- Cross-border transfer mechanisms (SDAIA-approved)
- Contact details for the Data Protection Officer (if applicable)
- Breach notification procedure (72-hour notification to SDAIA for significant breaches)
- Policy in Arabic (or bilingual with Arabic governing)

### UAE PDPL requirements (FDL 45/2021)

- Same core disclosures as KSA
- TDRA oversight; registration requirements for certain processors
- Specific consent mechanism requirements for special-category data
- Cross-border transfer: TDRA-approved countries or approved transfer mechanisms
- Arabic version required for UAE-facing consumer policies

### DIFC DP Law 2020

- GDPR-equivalent framework; common-law interpretation
- DPO required for large-scale or sensitive processing
- Lawful basis must be specified per processing activity
- Data subject rights include: access, rectification, erasure, restriction, portability, objection
- SCCs for international transfers

### GDPR requirements (EU)

- Mandatory disclosures under Art. 13/14: controller identity; DPO contact; purposes and legal basis; recipients; international transfers; retention periods; data subject rights; right to lodge complaint with supervisory authority; automated decision-making (if applicable)
- Consent must be freely given, specific, informed, and unambiguous
- Separate granular consent for each purpose (no bundled consent)
- Cookie consent via a compliant consent management platform (CMP)

### CCPA / CPRA requirements (California)

- Right to know, right to delete, right to opt-out of sale/sharing, right to correct, right to limit use of sensitive personal information
- "Do Not Sell or Share My Personal Information" link required on homepage
- Financial incentive disclosures

---

## Usage limits and tiers

| Tier | Features |
|---|---|
| Free (no login) | Base privacy policy (one jurisdiction); watermarked PDF + DOCX |
| Registered | Multi-jurisdiction output; cookie policy; no watermark; editable online |
| Pro | ROPA + DPIA templates; API access; team collaboration; scheduled annual review reminders |

---

## Behavior rules

- **Do not generate policies for illegal data collection.** If the user selects processing purposes that suggest unlawful activity (e.g., covert surveillance, selling data to unauthorized third parties), decline and explain.
- **Special-category data triggers enhanced disclosures.** If health, biometric, financial, or children's data is selected, the generated policy must explicitly address the heightened legal basis required (explicit consent or legal obligation) and the additional protections applied.
- **Children's data.** If children's data is selected, generate parental consent mechanism requirements and age verification language appropriate to the jurisdiction.
- **AI training disclosure.** If "machine learning / AI training" is selected as a purpose, flag that several jurisdictions (EU, UK, KSA) require explicit, granular consent for AI training purposes that goes beyond a general "product improvement" clause.
- **Always include a disclaimer.** *"This privacy policy was generated by Louis as a starting point. It is not a substitute for legal advice. For businesses handling sensitive data or operating in regulated sectors, have this policy reviewed by a qualified data protection lawyer."*

---

## Failure modes

| Failure mode | Response |
|---|---|
| User selects conflicting jurisdiction requirements | Flag the conflict and generate the most restrictive version (e.g., if both GDPR and CCPA are selected, default to GDPR standards plus CCPA-specific addendum) |
| User's data collection is unclear or inconsistent | Flag inconsistencies; prompt user to review selections before generating |
| User requests a policy for a sector with additional regulatory requirements (healthcare, financial services) | Generate the base PDPL policy and flag: "Your sector may require additional privacy disclosures under [sector-specific regulation]. Have this policy reviewed by sector counsel." |

---

## Related skills

- [[prompt-pack-vendor-data-protection-addendum]]
- [[prompt-pack-third-party-data-sharing-agreement]]
- [[public-tool-terms-generator-public]]
- [[public-tool-nda-generator-public]]
- [[kb-mena-data-protection]]

---
name: conversation-intake-data-privacy-assessment-sboghossian
title: Intake — Data Privacy Assessment
description: Use when a user requests a data-privacy compliance assessment or gap analysis for their organization — to gather the 13 required inputs spanning organization profile, data subjects, data categories, processing purposes, lawful bases, data sharing, cross-border transfers, and current policies. Outputs a gap-analysis matrix against applicable frameworks (GDPR, KSA PDPL, UAE PDPL, and others) plus a prioritized remediation roadmap. Applies across all jurisdictions; particularly strong for MENA organizations subject to multiple overlapping frameworks.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/conversation/conversation-intake-data-privacy-assessment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Intake — Data Privacy Assessment

## When to use this

Use this intake before beginning any data-privacy compliance assessment, gap analysis, or privacy program review. The 13 inputs below are necessary to determine which frameworks apply and what gaps exist. Without them, the assessment will be generic and therefore low-value — "you might need a privacy notice" is not actionable.

Typical triggers:
- "Do we comply with GDPR?"
- "What privacy laws apply to our company?"
- "We're expanding into Saudi Arabia — what data laws do we need to follow?"
- "Help us build a privacy program from scratch."
- "We had an incident — what are our disclosure obligations?"

## The 13 required inputs

### 1. Organization profile

- **Name and legal form:** (e.g., UAE LLC, DIFC-incorporated company, KSA joint-stock company, Lebanese SAL).
- **Jurisdictions of operation:** Where do they have offices, servers, employees, or customers? Each operational jurisdiction potentially activates a separate framework.
- **Industry sector:** Healthcare, financial services, retail, technology, legal, education — each sector has sector-specific requirements layered on top of general data protection law.

### 2. Data subjects

Who are the individuals whose personal data is processed?

| Category | Examples | Special considerations |
|---|---|---|
| Employees | HR files, payroll, performance records | Workplace privacy rules; some jurisdictions require works council notice |
| Customers | CRM, transaction history, support logs | Consumer protection law; consent requirements |
| Prospects | Marketing lists, lead data | Marketing consent rules; email regulations |
| Vendors/suppliers | Contract data, payment info | B2B data often receives lighter treatment but not zero protection |
| Website visitors | Analytics, cookies | Cookie consent requirements; ePrivacy |
| Minors (under 18) | If any | Heightened consent requirements; parental authorization |
| Sensitive individuals | Public figures, vulnerable persons | May trigger enhanced data-subject rights |

### 3. Data categories

What types of personal data does the organization process?

**Basic personal data:** name, address, email, phone, government ID number.

**Sensitive / special-category data** (requires explicit consent or specific legal basis in most frameworks):
- Health and medical information.
- Biometric data (fingerprints, facial recognition, iris scans).
- Genetic data.
- Financial data beyond basic payment (credit scores, financial condition).
- Religious beliefs or sect.
- Political opinions.
- Criminal records.
- Racial or ethnic origin.
- Sexual orientation.

For MENA organizations: religious affiliation and sect (important in Lebanon's confessional system) and tribal/family background can also constitute sensitive data in practice, even if not always explicitly categorized as such in local law.

### 4. Volume and retention

- Approximate number of data subjects in each category.
- Retention periods currently in practice (or lack thereof).
- Whether personal data is deleted at end of retention (automated or manual).

Retention schedules are one of the most commonly missing elements in MENA organizations' privacy programs.

### 5. Processing purposes

List all business purposes for which personal data is used:
- Service delivery.
- Marketing and advertising.
- HR / payroll.
- Customer support.
- Analytics and product improvement.
- Fraud prevention.
- Legal compliance.
- Security monitoring.
- Research.

### 6. Lawful bases per purpose

For each processing purpose, identify the claimed lawful basis:

| Basis | GDPR Art. | UAE PDPL | KSA PDPL | Notes |
|---|---|---|---|---|
| Consent | Art. 6(1)(a) | Yes | Yes | Must be specific, informed, freely given, revocable |
| Contractual necessity | Art. 6(1)(b) | Yes | Yes | Processing necessary to perform a contract |
| Legal obligation | Art. 6(1)(c) | Yes | Yes | Statutory requirement to process |
| Vital interests | Art. 6(1)(d) | Limited | Limited | Emergency situations only |
| Legitimate interests | Art. 6(1)(f) | Limited | Not recognized | MENA frameworks often don't adopt legitimate interests |
| Public task | Art. 6(1)(e) | For public bodies | For public bodies | |

**MENA-specific note:** the UAE Federal Data Protection Law (Federal Decree-Law No. 45 of 2021) and the KSA Personal Data Protection Law (PDPL, Royal Decree No. M/19) both draw on GDPR concepts but differ in specifics — particularly on legitimate interests (UAE recognizes it narrowly; KSA does not in the same form) and consent requirements.

### 7. Recipients — who receives the data

- Internal teams (which departments access which data).
- External service providers (cloud providers, payroll processors, marketing platforms).
- Advertisers or analytics platforms (if applicable — e.g., Google Analytics, Meta Pixel).
- Government and regulatory authorities (disclosures required by law).
- Other group companies (intra-group transfers have their own legal treatment).

### 8. Cross-border transfers

- To which countries is data transferred?
- What legal mechanism governs each transfer?

| Mechanism | GDPR | UAE PDPL | KSA PDPL |
|---|---|---|---|
| Adequacy decision | Standard Contractual Clauses (SCCs) | UAE Cabinet Resolution on adequate countries | Not yet developed formally |
| SCCs / DPAs | Yes | Required | Required |
| Binding Corporate Rules | Yes (for intra-group) | Yes | Limited |
| Consent | Yes (narrow use) | Yes | Yes |
| No mechanism in place | Non-compliant | Non-compliant | Non-compliant |

Cross-border transfers are frequently the highest-risk finding for MENA organizations using US cloud services (AWS, Google Cloud, Microsoft Azure) — check whether SCCs have been executed with each processor.

### 9. Existing policies

Identify what is already in place:
- Privacy notice / privacy policy (published? current? specific enough?).
- Data processing agreements (DPAs) with all third-party processors.
- Cookie consent banner (functional? records consent?).
- Data retention schedule.
- Data breach response plan.
- Data Subject Access Request (DSAR) procedure.

### 10. Incidents in the last 12 months

- Any data breaches, unauthorized access events, or loss of devices containing personal data.
- How were they handled? Were authorities notified?

Unreported breaches are a significant compliance risk. Under GDPR, reportable breaches must be notified to the supervisory authority within 72 hours. UAE and KSA PDPLs also impose notification obligations.

### 11. Data Protection Officer (DPO) — appointed?

- Is a DPO appointed? If so, who is it (internal or external)?
- Under GDPR, a DPO is mandatory for: (a) public authorities; (b) organizations that monitor individuals at large scale; (c) organizations processing sensitive data at large scale.
- Under UAE PDPL: a DPO is required for controllers processing personal data on a large scale or processing sensitive data.
- Under KSA PDPL: equivalent requirement for controllers above certain thresholds.

### 12. Record of Processing Activities (ROPA) — maintained?

A ROPA is required under GDPR Art. 30 for organizations with ≥250 employees or that process data regularly/on a large scale or in a way that could affect individuals' rights. UAE PDPL and KSA PDPL have similar requirements.

If a ROPA does not exist, building one is typically the first remediation action.

### 13. Data Protection Impact Assessments (DPIAs) — conducted?

DPIAs (also called Privacy Impact Assessments) are required for high-risk processing activities under GDPR and equivalent frameworks:
- Large-scale processing of sensitive data.
- Systematic monitoring of publicly accessible areas.
- Automated decision-making with significant effects.
- New technologies.

If high-risk processing is identified in the assessment and no DPIA has been conducted, this is a gap requiring remediation.

## Output format

After gathering the 13 inputs, produce:

### 1. Applicable frameworks table

| Framework | Applies? | Basis |
|---|---|---|
| GDPR | Yes / No | EU establishment / targeting EU data subjects |
| UAE Federal PDPL | Yes / No | UAE operation or processing UAE residents' data |
| KSA PDPL | Yes / No | KSA operation or processing KSA residents' data |
| UK GDPR | Yes / No | UK establishment or targeting UK data subjects |
| Lebanon (no dedicated PDPL yet, but telecom and banking-sector rules apply) | Partial | |
| Egypt PDPL (Law No. 151/2020) | Yes / No | Egypt operation or processing Egyptian residents' data |

### 2. Gap analysis matrix

A table with:
- Requirement (e.g., "Lawful basis documented for each processing purpose").
- Applicable framework(s).
- Current status (Met / Partial / Gap / Unknown).
- Risk level (High / Medium / Low).
- Remediation action.

### 3. Remediation roadmap (prioritized)

Ordered by risk level:
1. **Immediate (0–30 days):** Critical gaps — missing DPAs with processors, unreported incidents.
2. **Short-term (30–90 days):** High-risk gaps — missing privacy notice, no consent mechanism for marketing.
3. **Medium-term (90–180 days):** Medium-risk — no ROPA, retention schedule missing.
4. **Ongoing:** Low-risk and maintenance items — annual ROPA review, training, DPA refresh cycles.

## Related skills

- [[conversation-clarifying-questions]]
- [[conversation-disclaimer]]
- [[connector-eur-lex]]
- [[connector-legal-data-hunter]]

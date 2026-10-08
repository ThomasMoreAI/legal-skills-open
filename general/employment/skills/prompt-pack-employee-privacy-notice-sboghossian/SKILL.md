---
name: prompt-pack-employee-privacy-notice-sboghossian
title: Employee Privacy Notice
description: Use when drafting an employee privacy notice (also called a workforce privacy notice or HR privacy policy) explaining what personal data the employer collects from employees, the purposes and legal bases for processing, retention periods, employee data rights, workplace monitoring practices, and international transfers. Applicable across MENA (UAE PDPL, KSA PDPL, LB draft data protection law), EU (GDPR), UK (UK GDPR), and other jurisdictions. Trigger when a company is onboarding employees or when an existing notice needs updating following a regulatory change.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-employee-privacy-notice
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Employee Privacy Notice

## When to use this

Use this skill when a company needs to prepare or update its employee privacy notice — the transparency document that informs employees and job applicants about how their personal data is processed. Unlike a customer-facing privacy policy, the employee privacy notice covers workplace-specific processing activities: payroll, performance management, disciplinary records, monitoring, benefits administration, and more.

Typical triggers:
- Company entering a new jurisdiction where a data protection law applies
- Existing notice requires update following enactment of UAE PDPL, KSA PDPL, or other law
- HR system migration or new monitoring technology being introduced
- Data protection audit identifies a gap in employee notice documentation
- Employment contract or handbook update that should reference a revised privacy notice

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Employer name and jurisdiction(s) of operations | Identifies the data controller(s) and applicable law | Ask |
| Types of employees covered | Permanent, temporary, contractors, job applicants — each may be processed differently | Ask |
| HR systems and tools in use | Each system processes different categories of data | Ask |
| Monitoring activities in place | CCTV, email monitoring, location tracking, productivity software | Must be disclosed; ask |
| International transfers within the corporate group | Payroll, HR systems, and group reporting often cross borders | Ask |
| Applicable data protection law(s) | Determines legal basis requirements, rights, and mandatory disclosures | Ask |

## Optional inputs

- Whether the employer uses automated decision-making (AI screening, performance algorithms)
- Specific sensitive data categories processed (health data, biometric data for access control, trade union membership)
- Retention schedule already established
- DPO or Data Privacy Officer appointment (required under GDPR for some employers)

## Document structure

### Section 1 — Who is responsible for your data?

Identify the data controller:
- Company legal name, registered address
- Contact details for privacy queries (Data Protection Officer if applicable)
- Where multiple group entities are involved, identify the primary controller and any joint controllers

### Section 2 — What personal data do we collect?

List the categories of personal data processed, organized by HR process:

**Recruitment and onboarding**:
- Identity information (full name, date of birth, nationality, passport / Emirates ID / Iqama number)
- Qualifications, CV, employment history, references
- Right to work documentation
- Background check results (criminal record, credit — where permitted by law)

**Employment administration**:
- Contract terms; compensation and benefits details
- Tax identification numbers; bank account details for payroll
- Performance appraisals; disciplinary and grievance records
- Absence and leave records; sick leave documentation

**Health and safety**:
- Emergency contact information
- Medical fitness certificates (required for some roles)
- Accident and incident reports

**Workplace monitoring** (must be disclosed specifically):
- IT systems access logs; email monitoring policy
- CCTV footage (location and retention period)
- Location tracking (if applicable: company vehicles, remote work check-ins)
- Internet usage monitoring

**Benefits and pensions**:
- Beneficiary designations; family details for health insurance
- Pension or DEWS (DIFC End of Service Scheme) records

**Special categories** (require explicit disclosure):
- Health data (medical certificates, disability accommodations)
- Biometric data (fingerprint or face recognition for access control)

### Section 3 — Why do we process your data and what is our legal basis?

For each processing activity, state: (a) the purpose and (b) the legal basis.

| Purpose | Legal basis (GDPR) | MENA equivalent |
|---|---|---|
| Performing the employment contract (payroll, leave) | Contract performance | Contract performance (UAE PDPL Art.; KSA PDPL Art.) |
| Complying with legal obligations (NSSF, gratuity, tax) | Legal obligation | Legal obligation |
| Health and safety management | Legal obligation / vital interests | Legal obligation |
| Performance management | Legitimate interests | Legitimate interests (where recognized) |
| Workplace monitoring | Legitimate interests (with balancing test) | Subject to specific rules — see jurisdictional notes |
| Group reporting and consolidation | Legitimate interests | Legitimate interests |
| References for job applicants | Consent / legitimate interests | Consent |

### Section 4 — How long do we keep your data?

Provide a retention schedule by category:

| Data category | Retention period | Basis |
|---|---|---|
| Payroll and compensation records | 7 years post-employment (typical minimum for tax purposes) | Legal obligation |
| Performance records | Duration of employment + 2 years | Legitimate interests |
| Health and safety records | Duration of employment + 10 years (or longer for occupational disease) | Legal obligation |
| CCTV footage | 30–90 days (unless relevant to an incident) | Proportionality |
| Recruitment records (unsuccessful candidates) | 6 months (EU); 1–2 years (MENA varies) | Legitimate interests |
| Disciplinary records | Spent after rehabilitation period | Legitimate interests |

### Section 5 — Who do we share your data with?

List categories of recipients:
- Group companies: for HR administration, payroll, reporting
- Third-party payroll providers; HR software vendors
- Health insurance providers; pension / DEWS administrators
- Government authorities: GOSI (KSA), GPSSA (UAE), MOHRE (UAE), tax authorities, NSSF (Lebanon)
- Law enforcement: if legally required
- Reference requests: from prospective employers (with employee consent or as permitted by law)

For international transfers, identify the mechanism: adequacy decision, standard contractual clauses, group BCRs.

### Section 6 — Your rights

List the rights available to employees under the applicable law:

**Under GDPR (EU / UK)**:
- Right of access (Art. 15) — receive a copy of personal data held
- Right to rectification (Art. 16) — correct inaccurate data
- Right to erasure (Art. 17) — in limited circumstances
- Right to restrict processing (Art. 18)
- Right to data portability (Art. 20) — for automated processing on consent/contract basis
- Right to object (Art. 21) — to legitimate-interests processing
- Rights regarding automated decision-making (Art. 22)

**Under UAE PDPL (Federal Decree-Law No. 45 of 2021)**:
- Right to access, correct, and withdraw consent
- Right to request deletion (subject to retention obligations)
- Right to object to automated processing

**Under KSA PDPL (Royal Decree M/19 of 1443)**:
- Right to access, correct, and request deletion
- Right to withdraw consent
- Right to know third-party recipients

**How to exercise rights**: Provide contact details; state the [30]-day response timeline.

### Section 7 — Monitoring and surveillance

This section must be specific and transparent about each monitoring activity:
- CCTV: locations monitored; purpose (security only); access restrictions; footage retention
- Email / internet monitoring: scope; purpose; whether personal use is monitored; who has access
- Location tracking: whether and how devices or vehicles are tracked; purpose; employee notification
- AI / automated tools: performance monitoring software; productivity tracking

**MENA legal position on workplace monitoring**:
- **UAE**: No specific workplace monitoring law; monitoring must be proportionate and disclosed; PDPL principles apply to data collected
- **KSA**: Similar; PDPL requires consent or legitimate interest basis; monitoring of religious practice data is prohibited
- **DIFC**: DIFC Employment Law requires transparency; workers have right to know about monitoring
- **EU / UK**: Monitoring must be necessary, proportionate, and notified in advance; covert monitoring is unlawful in most circumstances (Article 8 ECHR); Works Council consultation required in many EU jurisdictions

### Section 8 — International transfers

Identify all cross-border data transfers:
- Name the receiving country and entity
- State the transfer mechanism: adequacy, SCCs, BCRs, or local equivalent
- UAE/KSA transfers to countries without adequate protection require contractual safeguards

### Section 9 — Changes to this notice

State that the notice may be updated; how employees will be notified of material changes.

### Section 10 — How to contact us / make a complaint

- Employer contact for privacy queries
- Regulatory authority where employees can complain:
  - UAE: UAE Data Office
  - KSA: Saudi Data & Artificial Intelligence Authority (SDAIA)
  - DIFC: DIFC Commissioner of Data Protection
  - EU: Relevant national supervisory authority (e.g., CNIL in France, ICO in UK)

## Jurisdictional notes

### Consent as a legal basis for employee data

In EU/UK GDPR, employee consent is generally **not** a reliable legal basis for employment data processing because of the power imbalance in the employment relationship — consent may not be freely given. Use contract performance or legal obligation for most HR processing; use legitimate interests (with a balancing test) for others.

In MENA jurisdictions (UAE PDPL, KSA PDPL), consent is more commonly used as a basis but is still subject to a genuine "voluntary" requirement. For routine HR processing, frame the basis as contractual necessity or legal obligation where possible.

### Biometric data

Biometric data (fingerprints, facial recognition, retina scans) is a sensitive data category in all modern data protection regimes. In the UAE, KSA, and EU:
- Processing requires explicit consent or a specific legal basis
- Proportionality is required: cannot use fingerprint access control if a PIN code would suffice for the same purpose
- Biometric data must be stored with enhanced security

### Right to work verification

In UAE and KSA, employers are required by law to collect, verify, and retain identity documents from all employees. This mandatory processing overrides consent requirements; disclose it under "legal obligation" basis.

## Common mistakes

- **Generic GDPR template applied to MENA employees**: GDPR does not automatically apply in UAE or KSA; the notice must reflect the applicable local law; applying incorrect rights (e.g., right to portability) where the law does not grant them confuses employees.
- **Omitting monitoring disclosures**: CCTV or email monitoring that is not disclosed in the notice may be unlawful; employees have successfully challenged disciplinary proceedings where monitoring was covert and undisclosed.
- **No retention schedule**: A notice that says "we keep your data for as long as necessary" without specifics does not satisfy transparency requirements under GDPR or PDPL.
- **Missing special category data disclosure**: If health data or biometric data is processed (health insurance, fingerprint attendance systems), this must be explicitly called out.
- **No Arabic version**: UAE and KSA employers should provide the notice in Arabic for local employees; some regulators may require the Arabic version to be the authoritative one.

## Related skills

- [[prompt-pack-employee-handbook]]
- [[prompt-pack-employment-contract-compliance-review]]
- [[prompt-pack-employment-offer-letter]]
- [[prompt-pack-esg-policy-framework]]

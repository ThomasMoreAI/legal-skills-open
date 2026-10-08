---
name: pa-workflow-transactional-pia-privacy-impact-assessment
title: Transactional — Privacy Impact Assessment (PIA / DPIA)
description: 'Use when a transactional or privacy lawyer needs to conduct a Privacy Impact Assessment (PIA) or Data Protection Impact Assessment (DPIA) for a new processing activity, product launch, M&A transaction, or system change involving personal data. Structures the assessment across six steps: processing identification, necessity/proportionality, risk assessment, mitigation, residual risk documentation, and sign-off registration. MENA-focused (UAE PDPL, KSA PDPL, DIFC DP Law, ADGM DP Regulations) with EU GDPR and UK GDPR alignment.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-transactional-pia-privacy-impact-assessment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Transactional — Privacy Impact Assessment (PIA / DPIA)

## Purpose

A Privacy Impact Assessment is a structured process for identifying and mitigating privacy risks before a new data-processing activity goes live. Under GDPR Art. 35 it is mandatory for high-risk processing; under UAE PDPL, KSA PDPL, and DIFC/ADGM data protection frameworks it is either mandatory or strongly expected as evidence of a privacy-by-design approach. This workflow guides counsel and data protection officers through the six-step process and produces a completed, sign-off-ready PIA document.

## When a PIA Is Required

| Trigger | Mandatory under |
|---|---|
| Large-scale processing of sensitive personal data | GDPR Art. 35; DIFC DP Law; ADGM DP Regs |
| Systematic monitoring of individuals | GDPR Art. 35 |
| New technology with high risk to individuals | GDPR Art. 35; UAE PDPL (recommended); KSA PDPL (recommended) |
| M&A transaction involving significant personal data transfer | GDPR Art. 35 (where applicable); good practice under all MENA frameworks |
| Cross-border transfer of personal data | UAE PDPL Art. 22; KSA PDPL Art. 29; DIFC DP Law Ch. 5 |
| AI / profiling / automated decision-making | GDPR Art. 22 + 35; UAE PDPL; KSA PDPL |
| HR systems with biometrics | All MENA frameworks; GDPR |

Good practice: conduct a PIA screening (lighter checklist) for any new processing activity; escalate to full PIA if the screening identifies risk indicators.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Description of the processing activity | Yes | What data, what purpose, what system |
| Categories of personal data | Yes | Standard personal data, sensitive data (health, biometrics, financial), children's data |
| Categories of data subjects | Yes | Employees, customers, website visitors, patients, etc. |
| Data flows diagram | Recommended | Shows collection, processing, storage, transfer, deletion |
| Legal basis for processing | Yes | Consent, contract, legal obligation, legitimate interests, vital interests |
| Processing parties (controllers, processors, sub-processors) | Yes | |
| Cross-border transfers | Yes | To which countries; by which mechanism |
| Applicable laws | Yes | UAE PDPL, KSA PDPL, GDPR, DIFC DP Law, ADGM DP Regs, or combination |

## Six-Step Process

### Step 1 — Identify processing activities and data flows

Document:
- **What data** is collected: field-by-field if possible (name, email, location, biometrics, financial data)
- **How** it is collected: directly from individual, from third party, automated
- **Why** it is processed: legal basis and purpose (purpose limitation principle)
- **Where** it is stored: jurisdiction, cloud provider, on-premises
- **Who** accesses it: internally (by role) and externally (processors, sub-processors)
- **How long** it is retained: retention period per data category
- **How** it is deleted: deletion / anonymization process

Produce a data-flow diagram or a structured data map in tabular form.

### Step 2 — Assess necessity and proportionality

For each processing activity:
- Is the processing **necessary** for the stated purpose? (Could the purpose be achieved with less data?)
- Is the volume and scope **proportionate** to the purpose?
- Is the legal basis appropriate?

| Legal basis | When available | Conditions |
|---|---|---|
| Consent | Data subject freely, specifically, and unambiguously consents | UAE PDPL: explicit; KSA PDPL: consent + purpose declaration; GDPR: freely given, specific, informed |
| Contract performance | Processing necessary for performance of a contract with the data subject | Only for what is strictly necessary |
| Legal obligation | Processing required by law | Cite the specific law |
| Legitimate interests | Processing serves a legitimate interest of the controller, not overridden by data subject interests | Requires LIA (Legitimate Interests Assessment) — not available as basis under KSA PDPL |
| Vital interests | Emergency / life-threatening situation | Narrow; rarely applicable |

**KSA PDPL note**: Legitimate interests is not an available legal basis under the Saudi PDPL. All processing requires either consent or a specific statutory basis. This is stricter than GDPR.

### Step 3 — Identify risks to data subjects

For each processing activity, identify risks:

| Risk category | Description | Examples |
|---|---|---|
| Unauthorized access | Data accessed by unauthorized parties | Hacking, insider threat, misconfiguration |
| Accidental disclosure | Data inadvertently disclosed | Incorrect recipient, public exposure of files |
| Loss or destruction | Data unavailable to data subjects or controller | Hardware failure, ransomware, deletion error |
| Repurposing | Data used beyond stated purpose | Selling data to third parties, profiling without consent |
| Discrimination | Processing that leads to unfair treatment | Algorithmic scoring that discriminates by protected characteristic |
| Chilling effect | Processing inhibits lawful behavior | Excessive monitoring of employees |
| Financial harm | Data loss causes financial damage to data subjects | Identity theft from payment data breach |
| Physical harm | Processing creates safety risk | Disclosure of location data to abusive party |

For each risk: likelihood (1–5) × impact (1–5) = risk score.

### Step 4 — Apply mitigations

For each identified risk above the threshold (risk score ≥ 9 = HIGH):

| Risk | Mitigation | Residual risk after mitigation |
|---|---|---|
| Unauthorized access to payment data | End-to-end encryption; access control by role; audit logs | Low |
| Cross-border transfer to non-adequate country | Standard Contractual Clauses + transfer impact assessment | Medium |
| Excessive retention of employee health data | Automated deletion at 3 years; quarterly audit | Low |

Standard mitigations to consider:
- Pseudonymization and anonymization
- Encryption at rest and in transit
- Data minimization (collect only what is needed)
- Access controls and role-based permissions
- Data Processing Agreements with all processors and sub-processors
- Consent management and withdrawal mechanisms
- Data subject rights fulfillment process (access, rectification, erasure, portability)
- Breach notification procedure

### Step 5 — Document residual risk

For each HIGH or CRITICAL risk where mitigation does not reduce to LOW:
- Document the residual risk explicitly
- Obtain sign-off from the data controller's management or DPO
- If residual risk remains HIGH: consult with the supervisory authority before proceeding (mandatory under GDPR Art. 36; good practice under MENA frameworks)

**DPO involvement (where applicable)**:
- GDPR: DPO consultation is required for DPIAs
- DIFC: Data Protection Officer review recommended
- UAE PDPL: no DPO requirement currently; but appointing a privacy officer is good practice
- KSA PDPL: Implementing Regulations require a Data Officer for some controllers

### Step 6 — Sign-off and registration

Complete the PIA record:
- Date of assessment
- Assessor (name and role)
- DPO / senior counsel review (if applicable)
- Management sign-off
- Date for review / reassessment (typically 12 months or on material change)
- Register in the organization's Records of Processing Activities (RoPA)

## Output

```markdown
## Privacy Impact Assessment — [Processing Activity Name] — [Date]

### Processing Activity Summary
**Activity**: [Name]
**Controller**: [Entity]
**Legal basis**: [Basis + brief justification]
**Personal data categories**: [List]
**Data subjects**: [Categories]
**Cross-border transfers**: [Yes/No; to which countries; by which mechanism]

### Necessity and Proportionality Assessment
[Summary finding: PROPORTIONATE / CONCERN — with explanation]

### Risk Assessment
| Risk | Likelihood | Impact | Score | Tier |
|---|---|---|---|---|
| [Risk 1] | 3 | 4 | 12 | HIGH |
| [Risk 2] | 2 | 2 | 4 | LOW |

### Mitigation Plan
| Risk | Mitigation | Owner | Target date | Residual risk |
|---|---|---|---|---|
| [Risk 1] | [Mitigation] | [Owner] | [Date] | Medium |

### Residual Risk Sign-Off
[Residual HIGH risks documented with management sign-off or supervisory authority consultation note]

### PIA Decision
☐ PROCEED — No significant residual risks
☐ PROCEED WITH CONDITIONS — Specific mitigations must be in place
☐ CONSULT REGULATOR — Residual risk remains high; prior consultation required
☐ DO NOT PROCEED — Risk cannot be mitigated to acceptable level

**Approved by**: _________________ Date: _________________
**Next review date**: _________________
```

## MENA Data Protection Framework Notes

| Framework | Mandatory DPIA/PIA | DPO required | Enforcement body |
|---|---|---|---|
| UAE PDPL 2022 | Recommended for high-risk; no explicit mandatory trigger | Not explicitly required | UAE Data Office |
| KSA PDPL 2024 | Recommended; Implementing Regs may require for high-risk | Data Officer for certain controllers | SDAIA / PDPC |
| DIFC DP Law 2020 | Yes — for high-risk processing (Art. 12) | Yes — for large-scale processing | DIFC Commissioner of Data Protection |
| ADGM DP Regs 2021 | Yes — for high-risk processing | Yes — for large-scale processing | ADGM Registrar |
| EU GDPR | Yes — mandatory for high-risk (Art. 35) | Yes — for certain controllers (Art. 37) | National DPA |
| UK GDPR | Yes — mandatory for high-risk | Yes — certain controllers | ICO |
| Lebanon | No mandatory framework yet | — | Draft law pending |
| Egypt | Law 151/2020 — PIA not explicitly mandated but good practice | Not required | NCPD |

## Related Skills

- [[pa-workflow-transactional-deal-point-analysis]]
- [[pa-workflow-regulatory-compliance-gap-matrix]]
- [[pa-workflow-regulatory-enforcement-likelihood-scorer]]
- [[kb-data-protection-mena]]

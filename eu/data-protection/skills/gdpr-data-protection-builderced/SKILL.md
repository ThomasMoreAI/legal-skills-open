---
name: gdpr-data-protection-builderced
title: GDPR Data Protection
description: Implement GDPR (Reg 2016/679) data protection — DPIA templates, Art.30 processing records, data subject rights, legal bases, and cross-border transfers.
author: BuilderCed
author_url: https://github.com/BuilderCed/agent-skills/tree/main/skills/compliance/gdpr-data-protection
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# GDPR Data Protection

> **DISCLAIMER**: This skill provides guidance only. It does not constitute legal advice. Always verify with a Data Protection Officer or legal professional.

## When to Use

- Designing systems that process personal data
- Conducting a Data Protection Impact Assessment (DPIA)
- Creating Article 30 processing records
- Implementing data subject rights (access, deletion, portability)
- Evaluating legal bases for data processing
- Planning cross-border data transfers

## Step 1: Identify Legal Basis (Article 6)

Every processing activity needs exactly one legal basis:

| Legal Basis | When to Use | Example |
|-------------|-------------|---------|
| **Consent** (6.1.a) | User actively opts in, can withdraw anytime | Newsletter signup |
| **Contract** (6.1.b) | Processing necessary to fulfill a contract | Delivering purchased goods |
| **Legal obligation** (6.1.c) | Required by law | Tax record retention |
| **Vital interests** (6.1.d) | Protecting someone's life | Emergency medical data |
| **Public interest** (6.1.e) | Official authority or public task | Government services |
| **Legitimate interest** (6.1.f) | Balanced against data subject's rights | Fraud prevention, security |

**Consent requirements**: freely given, specific, informed, unambiguous, easy to withdraw.

## Step 2: Data Minimization Checklist

Before collecting any personal data:
1. Is this data **necessary** for the stated purpose?
2. Can the purpose be achieved with **less** data?
3. Can the data be **anonymized** or **pseudonymized**?
4. Is the **retention period** defined and minimal?
5. Are **access controls** in place (who can see what)?

## Step 3: Article 30 Processing Record

Every controller must maintain a record of processing activities:

```
Processing Activity: [Name]
Controller: [Organization name, contact]
DPO Contact: [If applicable]
Purpose: [Specific, explicit purpose]
Legal Basis: [From Step 1]
Data Categories: [e.g., name, email, IP address]
Data Subjects: [e.g., customers, employees]
Recipients: [Who receives the data, including processors]
Third Country Transfers: [If any, with safeguard mechanism]
Retention Period: [Specific duration or criteria]
Security Measures: [Encryption, access control, etc.]
```

## Step 4: Data Subject Rights

Respond within **1 month** (extendable to 3 months for complex requests):

| Right | Article | What to Implement |
|-------|---------|-------------------|
| **Access** | 15 | Provide copy of all personal data held |
| **Rectification** | 16 | Correct inaccurate data |
| **Erasure** ("right to be forgotten") | 17 | Delete data when no longer needed |
| **Restriction** | 18 | Limit processing while disputes are resolved |
| **Portability** | 20 | Export data in machine-readable format |
| **Object** | 21 | Stop processing based on legitimate interest |
| **Automated decisions** | 22 | Human review of automated decisions with legal effects |

## Step 5: DPIA (Data Protection Impact Assessment)

Required when processing is "likely to result in a high risk":
- Large-scale processing of special categories (health, biometrics)
- Systematic monitoring of public areas
- Automated decision-making with legal effects
- New technologies with unknown risks

### DPIA Structure (CNIL template)
1. **Description**: Processing, purposes, data flows, retention
2. **Necessity and proportionality**: Legal basis, minimization, rights
3. **Risk assessment**: Likelihood x severity for confidentiality, integrity, availability
4. **Measures**: Technical and organizational measures to mitigate risks

## Step 6: Cross-Border Transfers

Personal data leaving the EEA requires a transfer mechanism:

| Mechanism | When |
|-----------|------|
| Adequacy decision | Country deemed adequate by EC (e.g., UK, Japan, South Korea) |
| Standard Contractual Clauses (SCCs) | Contract-based, most common |
| Binding Corporate Rules | Intra-group transfers |
| Derogations (Art. 49) | Explicit consent, contract necessity (limited use) |

**Post-Schrems II**: SCCs must include a Transfer Impact Assessment (TIA) evaluating whether the recipient country's laws undermine the protections.

## Penalties

| Violation Type | Max Fine |
|---------------|----------|
| Administrative (Art. 83.4) | EUR 10M or 2% of global turnover |
| Core principles, rights, transfers (Art. 83.5) | EUR 20M or 4% of global turnover |

## France-Specific (CNIL)

- Cookie consent: prior opt-in required (no cookie walls)
- Child consent: 15 years (not 16 as in GDPR default)
- DPIA tool: cnil.fr/fr/outil-pia (free, open source)
- DPO designation mandatory for: public bodies, large-scale systematic monitoring, large-scale special categories

## What This Skill Does NOT Do

- Does not implement consent management UI
- Does not configure cookie banners
- Does not perform the DPIA risk assessment (guides structure)
- Does not replace a DPO or legal counsel

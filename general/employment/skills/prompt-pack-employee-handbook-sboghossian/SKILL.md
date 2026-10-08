---
name: prompt-pack-employee-handbook-sboghossian
title: Employee Handbook
description: Use when drafting an employee handbook covering workplace policies, code of conduct, leave entitlements, anti-discrimination and harassment, disciplinary procedures, health and safety, IT acceptable use, and acknowledgment forms. Must comply with the applicable jurisdiction's employment law. Particularly important in MENA (UAE Labour Law, KSA Labour Law, LB Labour Law, EG Labour Law) where statutory entitlements differ significantly from common-law defaults. Trigger when a company is onboarding employees in a new market or updating its internal HR policies.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-employee-handbook
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Employee Handbook

## When to use this

Use this skill when drafting a new employee handbook, updating an existing one, or localizing a global handbook for a specific jurisdiction. The handbook is the primary HR compliance document for companies operating across MENA: it must reflect the employer's obligations under mandatory labour law, while also setting out the internal culture and operating rules the company wants to maintain.

Typical triggers:
- Company establishing its first local operations in UAE, KSA, Lebanon, or Egypt
- Global company localizing its group handbook for a MENA entity
- HR team modernizing outdated policies following regulatory changes
- Preparing for a Ministry of Labour audit or corporate investor due diligence

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Company name and jurisdiction | Determines which labour law applies | Ask |
| Industry / sector | Affects health & safety requirements, working hours, Saudization/Emiratization | Ask |
| Workforce composition | Local nationals vs. expatriates; full-time vs. contractors; manual vs. office workers | Ask |
| Key HR policies already established | To avoid contradicting existing policies | Ask |
| Governing language | Some jurisdictions require Arabic version to be official | Ask |

## Optional inputs

- Collective bargaining agreement or union recognition (if applicable)
- Remote work / hybrid policy preferences
- Specific compensation and benefits policies to include
- IT and social media use policies
- Data protection-specific section (see [[prompt-pack-employee-privacy-notice]] for standalone notice)

## Document structure

### Chapter 1 — Introduction and Company Overview

- Welcome message from CEO/management
- Company mission, values, and culture
- How to use this handbook; status (policy document, not a contract unless specified)
- Effective date and amendment process

### Chapter 2 — Employment Classification and Contracts

- Types of employment (indefinite, fixed-term, part-time, probationary)
- Probation period rules:
  - **UAE**: Maximum 6 months (UAE Labour Law, Federal Decree-Law No. 33 of 2021)
  - **KSA**: Maximum 90 days, extendable to 180 days with agreement (KSA Labour Law)
  - **Lebanon**: Defined in the employment contract; typically 3–6 months
  - **Egypt**: Maximum 3 months under Egyptian Labour Law (Law No. 12 of 2003)
- Hours of work; overtime entitlements; Ramadan working hours
- Moonlighting / secondary employment restrictions

### Chapter 3 — Compensation and Benefits

- Salary payment schedule; currency; bank transfer requirements
- Bonus structure (discretionary vs. contractual)
- Benefits: health insurance, life insurance, transportation, housing allowance
- Annual leave: statutory minimums and company enhancement
  - **UAE**: 30 calendar days per year (after 1 year of service)
  - **KSA**: 21 days (increasing to 30 after 5 years); Friday/Saturday weekend
  - **Lebanon**: 15 days (increasing with seniority)
  - **Egypt**: 21 days (increasing to 30 after 10 years); Muslim holidays
  - **DIFC**: 20 working days per year (DIFC Employment Law 2019)
- Public holidays (jurisdiction-specific; note Islamic holidays are variable)
- Sick leave: statutory entitlements and company policy
  - UAE: 90 days per year (first 15 paid in full; next 30 at half pay; final 45 without pay)
  - KSA: 30 days paid; 60 days half pay; 30 days unpaid
- Maternity and paternity leave:
  - UAE: 60 calendar days (45 paid, 15 half pay); paternity: 5 days
  - KSA: 10 weeks maternity (Saudi females); paternity: 3 days
  - DIFC: 65 working days maternity (DIFC Employment Law 2019)

### Chapter 4 — Code of Conduct and Workplace Policies

- Professional behavior standards
- Conflicts of interest: disclosure requirements; prohibited activities
- Gifts and hospitality: thresholds and approval procedures; anti-bribery compliance
- Confidentiality: protection of company information
- Social media: company name and reputation; permitted and prohibited activities
- Dress code (particularly important in KSA and conservative MENA environments)
- Workplace relationships and fraternization policy

### Chapter 5 — Anti-Discrimination and Equal Opportunities

- Company's commitment to equal treatment
- Prohibited grounds: religion, nationality, sex, age, disability (note jurisdiction differences — not all MENA labour laws have comprehensive anti-discrimination provisions)
- Harassment: definition; examples; reporting mechanism; investigation procedure
- Sexual harassment: specific prohibited conduct; zero-tolerance statement; reporting channels
- Grievance procedure: how employees raise concerns; timeline for investigation; protection from retaliation

### Chapter 6 — Disciplinary Procedures

- Grounds for disciplinary action (minor, moderate, serious misconduct)
- Procedure: investigation; right to respond; disciplinary hearing; levels of sanction
- Sanctions: written warning; final written warning; demotion; termination
- Summary dismissal (gross misconduct): definition; examples; applicable in all MENA jurisdictions but grounds vary
- Appeal procedure

**MENA note**: In UAE, KSA, and Egypt, the Labour Law specifies maximum penalties by category of violation; employers cannot impose penalties beyond what the law permits. Mandatory warning procedure requirements exist in UAE before termination for performance.

### Chapter 7 — Termination of Employment

- Notice periods: statutory minimums vs. contractual notice
  - UAE (Federal Decree-Law 33/2021): 30 days minimum for both parties; 90 days for senior roles in practice
  - KSA: 60 days for indefinite-term contracts
  - Lebanon: 1–3 months depending on length of service
  - DIFC: As specified in contract; minimum 30 days
- End-of-service gratuity / indemnity:
  - UAE: 21 days of last basic salary per year for first 5 years; 30 days per year thereafter (for termination by employer); capped at 2 years' total salary
  - KSA: 0.5 month per year for first 5 years; 1 month per year thereafter
  - Lebanon: 1 month per year of service (uncapped)
  - Egypt: 1 month per year of service (variable depending on reason for termination)
- Garden leave provisions
- Return of company property; access revocation
- Post-termination obligations: confidentiality; non-compete (enforceability varies — see jurisdictional notes)

### Chapter 8 — Health, Safety, and Wellbeing

- Company's health and safety policy
- Reporting accidents and incidents
- Emergency procedures; evacuation drills
- Mental health and wellbeing resources
- Workplace safety in extreme heat (UAE/KSA: midday work ban June–September)

### Chapter 9 — IT, Data, and Acceptable Use

- Company-provided equipment: ownership; permitted use
- Personal use of company systems: policy
- Monitoring and surveillance: company's rights; notice to employees
- Data protection: employees' obligations; handling personal data
- Cybersecurity: password policy; phishing awareness; incident reporting
- Social media and external communications about the company

### Chapter 10 — Acknowledgment Form

- Employee signature acknowledging receipt and understanding of the handbook
- Statement that handbook is subject to change
- Return copy to HR for personnel file

## Jurisdictional notes

### Non-compete enforceability

| Jurisdiction | Enforceability | Key limit |
|---|---|---|
| **UAE** | Enforceable if reasonable in scope, geography, and duration | Maximum 2 years; limited to activities that compete; employee must have been exposed to trade secrets or key clients |
| **KSA** | Enforceable but scrutinized; limited application in practice | Courts apply "reasonableness" standard |
| **Lebanon** | Enforceable in principle under Lebanese Code of Obligations and Contracts | Must be reasonable; courts will reduce scope if too broad |
| **Egypt** | Enforceable if restricted in scope and duration | Labour courts apply a reasonableness standard; excessive restrictions not enforced |
| **DIFC** | Common-law standard; enforceable if protects legitimate business interest | Garden leave as an alternative; post-termination restrictions >12 months are harder to enforce |

### Arabic language requirements

- **UAE**: The Arabic version of employment documents is the official version if there is a conflict (Ministry of Labour requirements); bilingual handbooks should include Arabic
- **KSA**: All employment contracts must be in Arabic; handbook should have Arabic version
- **Lebanon**: French and Arabic are both official languages; French is commonly used in commercial settings
- **Egypt**: Arabic is the official language; Arabic version governs

## Common mistakes

- **Copy-paste from a global handbook**: US-style "at-will" employment, FMLA references, or 401(k) provisions have no place in MENA employee handbooks and signal to employees that the employer doesn't know the local law.
- **Missing gratuity calculation**: The end-of-service gratuity section must include the correct statutory formula for the jurisdiction; errors create significant financial liability.
- **Wrong leave entitlements**: Giving less than the statutory minimum annual leave in any MENA jurisdiction violates mandatory labour law; audit the handbook against each jurisdiction's statute.
- **No Arabic version**: In UAE and KSA, the absence of an Arabic handbook (or Arabic employment contract) can be used by employees in labour court to argue the English version does not bind them.
- **Treating the handbook as legally binding**: In some jurisdictions, the handbook is incorporated into the employment contract by reference; in others it is not. Clarify its legal status explicitly.

## Related skills

- [[prompt-pack-employment-offer-letter]]
- [[prompt-pack-executive-employment-agreement]]
- [[prompt-pack-employee-privacy-notice]]
- [[prompt-pack-employment-contract-compliance-review]]

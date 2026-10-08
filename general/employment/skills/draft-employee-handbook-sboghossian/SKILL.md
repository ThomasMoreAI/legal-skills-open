---
name: draft-employee-handbook-sboghossian
title: Employee Handbook (Staff Manual)
description: Use when drafting an employee handbook (staff manual) that codifies workplace policies and procedures. Covers the full 11-section structure, MENA-specific requirements (bilingual Arabic/English, Saudization/Emiratization sections, end-of-service benefits), DIFC/ADGM free-zone override of federal rules, the critical non-binding disclaimer to prevent the handbook from becoming an employment contract, and common anti-patterns. Applicable across LB, KSA, UAE, DIFC, ADGM, EU, and UK jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-employee-handbook
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Employee Handbook (Staff Manual)

## When to use this

An employee handbook is the master document governing workplace policies, benefits, and conduct expectations. It is **not** an employment contract — it is an informational policy document that supplements the individual employment contract.

Use this skill when:

- A company is drafting its first employee handbook.
- An existing handbook needs to be updated for legal compliance (new labor law amendments, policy changes).
- The company is expanding into a new MENA jurisdiction and needs a jurisdiction-compliant handbook for local employees.
- An audit identified missing policies (harassment policy, data policy, disciplinary procedures).

**The most important drafting decision:** whether the handbook is contractually binding. In most jurisdictions, the safest approach is to make it non-binding (informational) with an explicit disclaimer. See Critical Clauses.

## Standard structure — 11 sections

### 1. Welcome and company overview
- Founder's welcome message.
- Company mission, values, history.
- Organizational structure overview.
- How to use the handbook (informational vs. contractual status; where to find updates).

### 2. Employment basics
- **Equal opportunity / non-discrimination policy**: protected characteristics under applicable law; commitment to diversity. MENA note: protected categories differ from Western standards; avoid importing US/EU EEO language wholesale — adapt to local law.
- **Employment types**: permanent, fixed-term, part-time, probationary.
- **Background check policy**: scope, consent mechanism, legal compliance with local privacy law.
- **Immigration and work authorization**: employee's obligation to maintain valid work authorization; employer's sponsorship obligations (kafala notes for KSA/UAE).

### 3. Compensation and benefits
- **Salary**: pay schedule; currency; payment method.
- **Overtime**: applicable law rate; authorization procedure. KSA: overtime at 1.5× for excess over 48 hours/week; UAE: 1.25× for hours 9–11 per day, 1.5× for nighttime and Fridays.
- **Annual leave**: statutory minimums per jurisdiction — see Jurisdictional Notes.
- **Sick leave**: entitlement, notification procedure, medical certificate requirements.
- **Health insurance**: coverage details, enrollment procedure, cost split.
- **End-of-service benefit (EOSB/EOSG)**: statutory entitlement per jurisdiction — see Jurisdictional Notes. Do not exclude or limit EOSB; it is mandatory in all GCC jurisdictions.
- **Performance reviews and raises**: frequency, criteria, process.
- **Pension / retirement**: GOSI (KSA), GPSSA or EOSG alternative (UAE), NSSF (LB), social security (FR/EU).

### 4. Workplace conduct
- **Code of conduct**: core behavioral expectations; professional standards; respect for colleagues.
- **Anti-harassment and anti-discrimination**: definition of harassment (verbal, physical, sexual, cyber); reporting channels; investigation procedure; no-retaliation commitment. MENA note: sexual harassment clauses must comply with local law — KSA Labor Law provisions on workplace harassment; UAE Federal Decree-Law 33/2021 Article 14 protections.
- **Workplace safety**: employer's duty to maintain a safe environment; employee's duty to report hazards; first-aid and emergency procedures.
- **Drug and alcohol policy**: prohibition in most MENA jurisdictions (alcohol is illegal in KSA; restricted in UAE). State the jurisdiction-appropriate standard.
- **Dress code**: professional attire standards; modesty requirements (GCC context); safety equipment for relevant roles.

### 5. Leave policies
| Leave type | KSA minimum | UAE minimum | LB minimum | FR / EU |
|---|---|---|---|---|
| Annual / vacation | 21 days (first 5 years) / 30 days (thereafter) | 30 days (after 1 year) | 15 days (after 1 year) | 25 days (FR) |
| Sick leave | 30 days full pay + 60 days 3/4 pay + 30 days unpaid | 15 days full pay + 30 days half pay (after probation) | 6 months half pay (after 6 months service) | Covered by social security (FR) |
| Maternity | 10 weeks (minimum; subject to expansion) | 60 days full pay | 7 weeks at 2/3 salary via NSSF | 16 weeks (FR); EU minimum 14 weeks |
| Paternity | 3 days | 5 days | None statutory | 4 weeks (FR) |
| Hajj / religious | 15 days (once in service; Muslim employees) | Not statutory (2 weeks by convention) | None statutory | None |
| Bereavement | 3 days (family); 5 days (spouse/child) | 3 days (immediate family) | Not specified | Varies |
| Unpaid leave | Discretionary; requires employer consent | Discretionary | Discretionary | — |

Always state that leave entitlements are subject to applicable law and that any entitlements exceeding the statutory minimum are at the employer's discretion.

### 6. Working hours and attendance
- Standard hours: 48 hours/week (KSA, UAE) or 48 hours/week (LB) or 35–40 hours (FR/EU).
- Ramadan reduction: 2 hours/day reduction for Muslim employees in KSA and UAE.
- Overtime authorization: must be approved in advance; unauthorized overtime does not waive the overtime pay obligation in most jurisdictions.
- Remote work / hybrid policy: eligibility; equipment provision; data security obligations; expense reimbursement; availability hours.
- Attendance and timekeeping: clock-in procedures; tardiness policy; consequences of unexcused absence.

### 7. Technology and data
- **Acceptable use policy (AUP)**: company systems for business use primarily; personal use in moderation; prohibited uses (illegal content, unauthorized software, competitor data, harassment).
- **BYOD policy**: if personal devices are permitted for work; MDM/enrollment requirements; company's right to wipe data.
- **Confidentiality**: employee's obligation to protect confidential information during and after employment.
- **Social media**: representation of the company on personal social media; prohibition on disclosing confidential information; conduct standards.
- **Monitoring**: employer's right to monitor company systems; disclosure of monitoring practices (required in some jurisdictions — FR requires employee consultation with works council before implementing monitoring; LB General Directorate of Labor rules apply).
- **Data protection**: employee's obligation to comply with applicable data-privacy law; handling of customer / HR personal data.

### 8. Career and performance
- Performance review cycle: frequency, format, calibration.
- Development and training: available programs; individual development plan process.
- Promotion process: criteria, timeline, decision-making.
- **Progressive discipline**: verbal warning → written warning → final written warning → termination. State that the employer reserves the right to skip steps for serious misconduct.
- Grievance procedure: how employees raise concerns internally before external escalation.

### 9. Termination procedures
- **Resignation**: required notice period (per employment contract and applicable law); process for notice delivery; garden-leave option; duties during notice.
- **Termination by employer with cause**: definition of cause; disciplinary process; grounds for summary dismissal (gross misconduct list) — calibrated to local law.
- **Termination by employer without cause**: notice period; EOSB/EOSG calculation; final paycheck timing.
- **End-of-service process**: clearance form; equipment return; final paycheck; certificate of employment; immigration consequences (visa cancellation for expatriate employees in GCC).
- **Non-solicitation and non-compete**: reference to employment contract provisions; reminders of post-employment obligations.

### 10. Complaint and grievance procedures
- Internal complaint channel (HR; Ethics hotline; online portal).
- External escalation: labor ministry (HRSD in KSA; MOHRE in UAE; MOL in LB); labor courts.
- Whistleblower protection: no-retaliation policy.
- Anti-bribery / anti-corruption complaint mechanism (required for entities subject to FCPA, UK Bribery Act, or Saudi Anti-Bribery Law).

### 11. Acknowledgment and signature page
**This section is critical.** The employee must sign and date an acknowledgment confirming:
- Receipt and reading of the handbook.
- Understanding that the handbook is informational, not contractual.
- Agreement to comply with the policies.
- Acknowledgment that the employer may update policies with notice.

Keep signed acknowledgments on file. Failure to obtain acknowledgments means the employer cannot rely on the handbook in disciplinary proceedings.

## Jurisdictional considerations

### MENA (KSA / UAE / LB)
- **Bilingual Arabic-English required** for all MENA jurisdictions where the language of employment law and court proceedings is Arabic. Arabic version controls; English is a courtesy translation.
- **GOSI / GPSSA / NSSF acknowledgment**: include a section confirming the employee's registration and contribution obligations.
- **Saudization / Emiratization**: include a section describing the company's compliance with Nitaqat (KSA) or Emiratization quotas (UAE); employee is expected to support compliance efforts.
- **Religious observance**: acknowledge prayer times; Ramadan working hours; annual leave for Hajj.
- **Alcohol / substance policy**: adapt to local law — prohibition in KSA; restricted in UAE; European standards for FR/UK offices.

### DIFC and ADGM
- DIFC Employment Law (DIFC Law 4/2021) and ADGM Employment Regulations 2024 apply to employees of entities registered in those free zones — these regimes largely override UAE federal labor law.
- Key differences from UAE federal: no MOHRE registration for individual contracts; different EOSG calculations; enhanced employee protection provisions.
- The handbook for DIFC/ADGM entities should reference the applicable free-zone law, not Federal Decree-Law 33/2021.

### EU (especially France)
- Works council consultation (comité social et économique) required before implementing new workplace policies in France (entities with 50+ employees).
- Posted Workers Directive: if employees are seconded from a foreign entity to operate in France, French labor standards apply to the secondment.
- Data monitoring policies require consultation with employee representatives under French law.

## Critical clauses

### Non-binding disclaimer (most important)
> "This Employee Handbook is provided for informational purposes only. It does not constitute an employment contract or create any binding obligation on the Company, except as required by applicable law. The Company reserves the right to modify, suspend, or rescind any policy described herein with reasonable advance notice. In the event of any conflict between this Handbook and applicable law, applicable law prevails."

### Right to modify
> "The Company reserves the right to update, amend, or revoke any policy in this Handbook with [30] days' written notice to employees. The most current version of the Handbook is available at [location]. Continued employment following notice of changes constitutes acceptance of the updated policies."

### Severability
> "If any policy or provision of this Handbook is found to be unenforceable or invalid under applicable law, that policy or provision shall be modified to the minimum extent necessary to make it enforceable, and the remainder of the Handbook shall continue in full force and effect."

### Governing law
> "This Handbook is subject to and shall be interpreted in accordance with the laws of [jurisdiction]. In the event of any conflict between this Handbook and mandatory provisions of applicable labor law, the mandatory provisions of applicable labor law prevail."

## Anti-patterns

| Anti-pattern | Risk | Fix |
|---|---|---|
| Treating handbook as contract | Employee can sue for breach of handbook terms | Add non-binding disclaimer; separate contractual terms into employment contract |
| Over-prescription | Rigid policies fail in variable real-world situations | State principles, not every scenario; reserve employer discretion |
| Missing acknowledgment signature page | No evidence employee was aware of policies; cannot rely on policies in disciplinary proceedings | Include and enforce signature page process |
| Importing US/EU EEO language into KSA/UAE handbook | Legal mismatch; creates expectations the local law does not support | Adapt EEO language to local law; use "fair treatment" framing |
| Static handbook without update process | Policies become outdated as law changes | Establish annual review cycle; version-control the handbook |
| No Arabic version in GCC | Unenforceable in local courts and before labor ministries | Draft bilingual from inception |

## Related skills

- [[draft-employment-contract-uae]] — individual employment contract (UAE federal) that the handbook supplements
- [[draft-employment-contract-ksa]] — individual employment contract (KSA) that the handbook supplements
- [[draft-employment-contract-lb]] — individual employment contract (Lebanon) that the handbook supplements
- [[kb-employment-law-mena]] — reference pack on employment law minimums across KSA, UAE, LB, and DIFC/ADGM

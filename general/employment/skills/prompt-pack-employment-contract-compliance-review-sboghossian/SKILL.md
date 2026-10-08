---
name: prompt-pack-employment-contract-compliance-review-sboghossian
title: Employment Contract Compliance Review
description: Use when reviewing an employment contract for legal and operational compliance — checking non-compete and non-solicitation clauses, IP ownership, termination terms and notice periods, and compensation structure. Flags provisions likely to cause legal disputes and proposes improved wording. Applicable across MENA (UAE, KSA, LB, EG), DIFC, ADGM, UK, EU, and US. Trigger when a company is reviewing standard employment contracts, when an employee wants a contract reviewed before signing, or when legal counsel is auditing HR documentation.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-employment-contract-compliance-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Employment Contract Compliance Review

## When to use this

Use this skill when reviewing an employment contract to assess its legal and practical compliance with the applicable jurisdiction's employment law and the employer's internal standards. This review is appropriate for:

- Standard employment contracts before rolling out to a workforce
- Specific employee contracts flagged as unusual by HR
- Executive contracts containing complex compensation structures
- Contracts being audited as part of M&A due diligence
- Individual employee seeking advice before signing

## Inputs

| Input | Why it matters |
|---|---|
| Employment contract (full text) | The document to be reviewed |
| Jurisdiction | Determines mandatory law, permitted provisions, and what cannot be waived |
| Employer or employee perspective | A compliance review from employer's perspective (risk of non-enforcement) vs. employee's perspective (rights being contracted away) differs |
| Role / seniority | Senior executives have different risk profiles than standard employees; affects enforceability of restrictive covenants |
| Industry | Some sectors have specific rules (financial services, healthcare, education) |

## Review methodology

Work through the contract section by section, applying the following checklist:

### 1. Probation Period

- Is the probation period within the statutory maximum?
  - UAE: 6 months max
  - KSA: 90 days (extendable to 180 days with agreement)
  - Egypt: 3 months max
  - DIFC: As specified; DIFC Employment Law 2019 governs
- Is the notice period during probation specified? (UAE 2021 Labour Law: 14 days' notice during probation)
- Does early termination during probation comply with statutory rules?

### 2. Compensation Structure

**Flag**: Compensation that falls below minimum wage requirements (UAE Ministry of Human Resources wage order; KSA minimum wage for Saudi nationals; DIFC minimum wage if applicable).

**Review**:
- Base salary: currency, payment date, bank transfer requirement
- Commission/bonus: is it discretionary or contractual? "Discretionary" bonuses where there is a history of payment may be implied contractual obligations in common-law jurisdictions
- Allowances (housing, transport, schooling): in MENA these are often used to reduce end-of-service gratuity base calculation; confirm whether basic salary or total package is the gratuity base
- Overtime: is it authorized? Calculated at the correct statutory rate?
  - UAE: 25% premium; 50% between 9pm and 4am and on Fridays
  - KSA: 150% of normal wage for overtime beyond 8 hours

**Common issues**:
- Structuring compensation to minimize gratuity base in violation of spirit of the law
- Bonus terms that create unconscious contractual entitlements
- Salary benchmarks that do not pass Saudization wage tests (KSA)

### 3. Non-Compete and Non-Solicitation Clauses

This is typically the highest-risk section for enforceability.

**Non-compete checklist**:
- Is the geographic scope limited to areas where the employer has a legitimate interest?
- Is the duration reasonable? (UAE: max 2 years; KSA: courts apply reasonableness; DIFC: similar to English law)
- Is the scope of restricted activities limited to the employee's actual role and knowledge?
- Is there compensation for the restriction? (Not required in UAE but increases enforceability; required in some EU jurisdictions)
- Does the clause identify the specific legitimate interest being protected (trade secrets, key client relationships, confidential methodologies)?

**Non-solicitation checklist**:
- Are customers restricted to those the employee had actual contact with (not the employer's entire customer base)?
- Are employees restricted from soliciting their own former direct reports only (not all employees)?

**Flag**:
- Overly broad restrictions that cover the entire industry worldwide — courts will not enforce or will blue-pencil
- Non-competes with no geographic limit in civil-law MENA systems — likely void
- Non-competes without a time limit — void in most jurisdictions
- Non-solicitation clauses in UAE that exceed 2 years — exceeds statutory maximum

### 4. Intellectual Property Ownership

**Review**:
- Does the contract include an IP assignment clause assigning all works created in connection with employment to the employer?
- Does the IP clause cover work created on personal time using personal equipment? (Scope must be reasonable)
- Is there a prior IP carve-out? (Employee may have pre-existing IP that should not be assigned)
- Is there a work-made-for-hire clause? (Relevant in US-law contracts)
- Does the clause cover moral rights waiver? (Required under UK and EU copyright law; not applicable in civil-law MENA systems where moral rights are often inalienable)

**MENA specifics**:
- UAE Copyright Law provides that works created by an employee in the course of employment are owned by the employer — the contract should confirm and extend this to all IP categories
- Lebanon and Egypt have similar civil-law copyright rules; employer ownership for works created in the scope of employment

**Flag**:
- No IP assignment clause in a technology or creative role — high risk
- IP clause that attempts to assign IP unrelated to employment (courts may void)
- No inventions disclosure obligation

### 5. Termination Terms and Notice Periods

**Review**:
- Are notice periods at least equal to the statutory minimum?
  - UAE: 30 days (minimum); best practice 1–3 months for senior roles
  - KSA: 60 days for indefinite contracts
  - DIFC: As contracted; DIFC Employment Law minimum is 1 month
  - Lebanon: Graduated notice under Labour Law (1–3 months depending on service length)
- Is there a mutual notice obligation? (Employer and employee must give the same or specified different periods)
- Is the PILON (payment in lieu of notice) provision included? Can the employer terminate immediately and pay salary in lieu?
- Is there a garden leave provision allowing the employer to put the employee on paid leave during notice?
- Are the grounds for summary dismissal (termination without notice) specified and consistent with statutory grounds?
  - UAE Labour Law Art. 44 specifies exhaustive grounds for dismissal without notice
  - KSA Labour Law specifies similar exhaustive grounds

**Flag**:
- Notice periods below statutory minimum (void; statutory minimum applies)
- Summary dismissal grounds that are broader than the statutory list (in UAE/KSA, courts will void the contract term and apply the statutory list)
- No severance or end-of-service gratuity provisions (must comply with statutory requirements)

### 6. End-of-Service Gratuity / Indemnity

**Review**:
- Is the gratuity calculation formula stated and consistent with statutory requirements?
  - UAE: 21 days of last basic salary per year (years 1–5); 30 days per year thereafter; max 2 years' salary
  - KSA: 0.5 month per year for first 5 years; 1 month per year thereafter
  - DIFC: DEWS scheme applies; employer contributes percentage of monthly salary to registered scheme
- Does the contract attempt to reduce or waive statutory gratuity? (Void in UAE and KSA)

**Flag**:
- Any provision that explicitly waives or reduces gratuity entitlement
- Contracts that calculate gratuity on "total package" rather than "basic salary" (depending on jurisdiction, allowances may be excluded from the base)

### 7. Confidentiality

**Review**:
- Is the confidentiality obligation specific enough to be enforceable?
- Does it cover post-employment period? (Typically 1–3 years for specific categories; indefinite for trade secrets)
- Is there a carve-out for public domain information, prior knowledge, and legally required disclosures?

## What to flag

Organize findings in a structured output:

| Issue | Clause | Severity | Recommended Fix |
|---|---|---|---|
| Non-compete covers entire world | Clause 12.1 | High — likely void | Limit to [specific markets] |
| Bonus described as "discretionary" but paid every year for 5 years | Clause 4.3 | High — may be implied obligation | Explicitly state payment criteria or note no entitlement arises from past practice |
| Gratuity clause on basic salary but allowances are 60% of compensation | Clause 9 | Medium — potential underpayment | Confirm statutory basis calculation |
| No IP assignment clause | N/A | High for tech/creative roles | Add standard IP assignment |
| Summary dismissal grounds broader than statutory list | Clause 15.2 | High — UAE Art. 44 applies | Align clause to statutory grounds |

## Common mistakes

- **Applying US "at-will" concepts**: "At-will" employment does not exist in UAE, KSA, Lebanon, or Egypt; all terminations require notice and/or gratuity regardless of contract language.
- **Overlooking Arabic contract requirement**: UAE and KSA require contracts to be in Arabic; if there is a bilingual contract with a conflict resolution clause that says "English prevails," that clause may itself be void.
- **Not reviewing the offer letter**: The offer letter sometimes creates binding obligations that differ from the formal contract; review both.
- **Ignoring collective agreements**: In Lebanon and Egypt, sector-level collective bargaining agreements may impose terms on the employer that override the individual contract.

## Related skills

- [[prompt-pack-employment-offer-letter]]
- [[prompt-pack-executive-employment-agreement]]
- [[prompt-pack-employee-handbook]]
- [[prompt-pack-independent-contractor-agreement]]

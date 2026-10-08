---
name: prompt-pack-employment-offer-letter-sboghossian
title: Employment Offer Letter
description: Use when drafting an employment offer letter for a specific position under a particular jurisdiction's employment law. Covers start date, compensation package, benefits, reporting structure, employment type (at-will, fixed-term, or indefinite), confidentiality obligations, and conditions of employment. Applicable across MENA (UAE, KSA, LB, EG, DIFC, ADGM) and internationally. Trigger when an employer is extending a formal offer to a new hire and needs a legally compliant offer letter that will not inadvertently create greater contractual obligations than intended.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-employment-offer-letter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Employment Offer Letter

## When to use this

Use this skill when an employer needs to extend a formal offer of employment that is clear, complete, and legally compliant. The offer letter is often the first binding document in the employment relationship; terms stated in it — even if later superseded by a formal contract — can be relied upon by the employee. Drafting it carefully from the start avoids disputes.

The offer letter differs from the employment contract: the offer letter is typically shorter, less formal, and designed to confirm the commercial terms agreed during the recruitment process. In MENA, a formal employment contract must still be signed (often required to be registered with the labour authority); the offer letter is a pre-contractual or concurrent document.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Position title and description | Defines the role and sets expectations | Ask |
| Company name and jurisdiction of employment | Determines applicable law; MENA jurisdictions require Arabic contract registration | Ask |
| Start date | Creates a binding commitment | Ask; confirm offer is conditional until start date |
| Compensation details (basic salary, allowances, bonuses) | The most important term; must be specified | Ask |
| Employment type | Fixed-term vs. indefinite; probation period | Ask; MENA default is typically limited/unlimited contract |
| Conditions precedent | Background check, reference check, visa, medical | Ask |

## Optional inputs

- Reporting structure (line manager name and title)
- Benefits package (health insurance, schooling, transport, housing)
- Equity / ESOP grant (if applicable)
- Bonus structure (discretionary vs. target bonus)
- Post-termination obligations being imposed (non-compete, non-solicitation)
- Work location and remote work policy
- Confidentiality obligations

## Document structure

### 1. Header

- Date of letter
- Candidate's full name and address
- Subject: "Employment Offer — [Position Title]"

### 2. Opening paragraph

Confirm that the company is pleased to offer the position; reference the role, the team/department, and who the offer is extended by.

### 3. Position and start date

- Job title and department
- Proposed start date
- Note that start is subject to completion of conditions (visa processing, background check) if applicable

### 4. Employment type

State clearly:
- **UAE/KSA/Lebanon/Egypt**: Whether the contract is limited (fixed-term) or unlimited (indefinite)
  - In UAE, fixed-term contracts under the 2021 Labour Law are limited to 3 years with renewal
  - In KSA, indefinite contracts are the default; fixed-term for specific projects
- **DIFC/ADGM**: Indefinite vs. fixed-term; probation period
- **UK/EU**: Permanent vs. fixed-term; reason for fixed-term (if applicable)

### 5. Compensation

Provide full compensation details:
- **Basic salary**: monthly amount; currency; payment date
- **Housing allowance**: if provided separately (common in MENA)
- **Transportation allowance**: if provided
- **Total package**: state explicitly for clarity
- **Bonus**: whether discretionary or target-based; percentage or amount; performance period; note that no entitlement arises unless performance targets are met (for discretionary bonuses)
- **Probation salary**: sometimes reduced during probation; if so, state clearly

**Gratuity note**: In UAE and KSA, the end-of-service gratuity is calculated on basic salary, not total package. The offer letter should be clear about which elements constitute "basic salary" vs. allowances to avoid disputes at termination.

### 6. Benefits

List each benefit clearly:
- Health insurance: coverage level; whether family coverage is included
- Annual leave: number of calendar or working days
- Schooling allowance (if applicable): amount per child; number of children covered; qualifying schools
- Air ticket allowance (common in MENA expat packages): annual; business or economy class
- Gratuity: reference to statutory entitlement under applicable law

### 7. Probation period

- Duration (within statutory maximum)
- Notice during probation (typically shorter: 14 days in UAE; 30 days in practice)
- Confirmation that employment may be terminated by either party during probation with notice

### 8. Reporting structure and location

- Direct supervisor name and title
- Primary work location
- Travel requirements (if any)

### 9. Conditions of offer

State that the offer is conditional on:
- Satisfactory completion of background and reference checks
- Proof of right to work / visa eligibility
- Medical fitness (where applicable)
- Execution of the company's standard employment contract
- Return of signed offer letter by [date]

### 10. Confidentiality and IP

Brief statement (full clauses will be in the employment contract):
- Employee will be required to execute a confidentiality and IP assignment agreement
- Employee confirms they are not bound by any existing restrictive covenants that would prevent them from taking this role

### 11. Entire agreement / supersession

- The offer letter reflects the agreed commercial terms; the formal employment contract will govern the full employment relationship
- The offer letter does not constitute the employment contract

### 12. Acceptance

- Request that the candidate sign and return the letter by a specified date
- Signature block for both employer and candidate

## Jurisdictional notes

### UAE

- All employment contracts must be registered with the Ministry of Human Resources and Emiratization (MOHRE) through the online portal; the standard MOHRE contract template must be used or a contract consistent with it
- The offer letter should be consistent with the MOHRE contract terms; inconsistencies can be used by the employee to claim the more favorable terms
- Arabic language: the MOHRE-registered contract is in Arabic; the offer letter may be in English but the Arabic contract governs
- End-of-service gratuity: the offer letter should be clear that gratuity is calculated on basic salary as per UAE Federal Decree-Law No. 33 of 2021

### KSA

- Employment contracts for foreign workers must be attested by the Ministry of Human Resources and Social Development
- The offer letter and contract must be in Arabic; bilingual versions are common
- Nitaqat / Saudization: if offering a position to an expatriate in a company below its Nitaqat target, confirm that the hire is permitted
- Housing allowance and other allowances: common in KSA expat packages; confirm whether allowances are pensionable for purposes of gratuity calculation

### DIFC

- DIFC Employment Law 2019 applies; distinct from UAE mainland labour law
- Offer letter should reflect DIFC Employment Law terms: 60-day working day annual leave; maternity leave provisions; DEWS contribution in lieu of end-of-service gratuity
- DIFC does not permit "at-will" employment; all terminations require notice

### UK / EU

- In the UK, the Employment Rights Act 1996 requires a written statement of employment particulars within 2 months of start (now on day 1 for key terms); the offer letter can satisfy this if it covers the required terms
- In the EU, the Transparent and Predictable Working Conditions Directive (2019/1152) requires employers to provide key employment information from day 1
- In France, the offer letter can create a binding promise of employment; withdrawal of an accepted offer triggers damages

## Common mistakes

- **Vague bonus language**: "Annual bonus payable at company discretion" is fine as a legal matter, but if the company has always paid a bonus, courts may find an implied obligation; be explicit about the criteria.
- **Total package confusion**: In UAE, employees who are not told that basic salary is only a portion of their total package sometimes calculate gratuity on the total package and dispute the employer's lower calculation at termination.
- **No conditions precedent**: Accepting a candidate before their background check passes creates significant legal risk; always include conditions.
- **Contradicting the employment contract**: If the offer letter says 30 days' notice and the employment contract says 14 days, the employee will rely on the 30-day letter.
- **Overlooking MOHRE registration in UAE**: The offer letter terms must be consistent with the MOHRE-registered contract; inconsistencies favor the employee.

## Related skills

- [[prompt-pack-executive-employment-agreement]]
- [[prompt-pack-employment-contract-compliance-review]]
- [[prompt-pack-employee-handbook]]
- [[prompt-pack-equity-incentive-plan-summary]]

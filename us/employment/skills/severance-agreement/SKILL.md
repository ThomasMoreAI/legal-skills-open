---
name: severance-agreement
title: Confidentiality and Severance Agreement
description: 'Drafts a U.S. Confidentiality and Severance Agreement for employment separations with statutory-compliant release of claims, OWBPA compliance, DTSA confidentiality obligations, jurisdiction-tailored restrictive covenants, and NLRA-safe non-disparagement. Use when concluding an employment relationship, negotiating a separation package, resolving employment discrimination or wage claims, or settling employment litigation. Trigger: severance, separation agreement, release of claims, OWBPA, employment settlement.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/severance-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# Confidentiality and Severance Agreement

Drafts a litigation-resistant employment separation agreement combining a comprehensive release of claims, confidentiality protections, and post-employment obligations with OWBPA and state-law compliance.

## Prerequisites

Collect before drafting:

1. **Employee**: full legal name, position, hire date, termination date, age (drives OWBPA), work state and residence state
2. **Compensation**: salary, accrued PTO, bonus structure, equity (vested/unvested, exercise periods)
3. **Existing agreements**: offer letter, NDA/PIIA, non-compete, indemnification
4. **Termination context**: individual vs. group RIF (affects OWBPA 21- vs. 45-day period), separation reason
5. **Severance terms**: payment amount/structure, COBRA subsidy, outplacement, benefits continuation
6. **Employer**: full legal name, parent/affiliates covered by release

## Drafting Workflow

### 1. Parties and Dates

- Employer legal name as registered with Secretary of State; define "Company Affiliates" if releasing subsidiaries
- Employee full legal name matching tax documents
- Termination date (last day of active work)
- Effective date: day after 7-day OWBPA revocation expires (age 40+) or signing date (under 40)

### 2. Severance Package

- Cash payment: amount, lump sum vs. installments, trigger (effective date)
- Accrued PTO: mandatory payout states (CA, CO, IL) — not discretionary
- Bonus proration: eligibility cutoff, performance contingencies
- Equity: treatment per plan docs, any acceleration or exercise extension
- COBRA subsidy: duration (3–12 months typical), premium split
- Outplacement: vendor, duration, dollar cap
- Property return: deadline, itemized list
- **Payment conditioned on**: execution + revocation period expiration + ongoing compliance
- **Clawback**: cessation of installments + repayment on material breach (must comply with state wage payment laws — CA prohibits most wage deductions; structure as separate contractual obligation)

### 3. Release of Claims

**Covered parties**: employer + parent, subsidiaries, affiliates, predecessors, successors, officers, directors, employees, agents, attorneys.

**Federal statutes**: Title VII, ADA, ADEA, OWBPA, FMLA, FLSA, § 1981, ERISA (non-vested only).

**State claims**: wrongful discharge, breach of contract, implied covenant, fraud, defamation, invasion of privacy, IIED/NIED, state wage/hour, discrimination, whistleblower statutes.

**Unknown claims waiver**: CA — include Cal. Civil Code § 1542 verbatim. Other states with savings statutes — adapt accordingly. Include § 1542 waiver for any CA-nexus employee regardless of primary jurisdiction.

**Mandatory carve-outs** (non-waivable):
- Workers' compensation and unemployment benefits
- ERISA-vested plan benefits
- Corporate indemnification rights
- Claims arising after execution date
- Right to file EEOC/NLRB/SEC charges (waive monetary recovery only, except where prohibited)

### 4. OWBPA Compliance (Age 40+)

OWBPA is strict liability — errors void the ADEA release. When in doubt, extend the period.

- [ ] Specific reference to ADEA/OWBPA rights
- [ ] Advisement to consult an attorney
- [ ] 21-day consideration (individual) or 45-day (group RIF/exit incentive)
- [ ] 7-day revocation right; agreement not effective until expiration
- [ ] Revocation procedure: written notice, designated recipient, method, deadline
- [ ] Acknowledgment block immediately above employee signature
- [ ] Group RIF only: attach decisional unit, eligibility criteria, ages/titles of all considered employees

**OWBPA acknowledgment block** (insert above employee signature for age 40+):

> I acknowledge that: (1) I have been advised to consult with an attorney before signing this Agreement; (2) I have been given [21/45] days to consider this Agreement; (3) I have 7 days after signing to revoke this Agreement by delivering written notice to [Name] at [Address]; and (4) this Agreement will not become effective until the 7-day revocation period expires without revocation.

### 5. Confidentiality Obligations

- **Scope**: trade secrets, customer lists, pricing, financials, strategies, business plans, product development, source code, employee data, supplier terms
- **Duration**: trade secrets indefinite (UTSA/DTSA); other confidential information 5 years
- **Return/destruction**: all physical and electronic materials by deadline; delete from personal devices, email, cloud; written certification required
- **Exceptions**: publicly available (not via breach), pre-employment possession, independent development, legally compelled (with advance notice for protective order)

**DTSA Immunity Notice** — mandatory verbatim inclusion; omission bars punitive damages and attorneys' fees:

> "An individual shall not be held criminally or civilly liable under any Federal or State trade secret law for the disclosure of a trade secret that is made in confidence to a Federal, State, or local government official or to an attorney solely for the purpose of reporting or investigating a suspected violation of law… See 18 U.S.C. § 1833(b)."

### 6. Mutual Non-Disparagement

- **Employee scope**: no disparaging statements re company, affiliates, officers, directors, products, services — includes social media
- **Employer scope**: named individuals only (HR, supervisors, officers) — no negative statements to third parties re employee
- **Both parties carve-outs**: truthful testimony, legally compelled statements, NLRA-protected concerted activity, EEOC/agency participation

**NLRA requirement**: Post-*McLaren Macomb* (2023), overbroad non-disparagement and confidentiality provisions may violate NLRA. Must not restrict statements about wages, hours, or working conditions. Include explicit Section 7 carve-outs.

### 7. Restrictive Covenants

**Check jurisdiction enforceability first:**

| State | Status |
|---|---|
| California | Void (Bus. & Prof. Code § 16600) — never include, even with other-state choice-of-law |
| Colorado | Senior executives above statutory income threshold only (C.R.S. § 8-2-113) |
| Massachusetts | Enforceable with garden leave or equivalent consideration |
| Minnesota | Banned (agreements after Jan. 1, 2023) |
| Others | Enforceable if reasonable in scope, duration, geography |

**Non-compete** (where enforceable): 12–24 months, limited to areas actually served, narrowly tailored to actual business, separate consideration if state requires.

**Customer non-solicitation**: 12–24 months, limited to customers with material contact or confidential information exposure in final 12–24 months.

**Employee non-solicitation**: 12–24 months, employees during final 12 months, limit to direct reports or working team if jurisdiction requires.

Include **blue-pencil/reformation clause** authorizing courts to reduce unenforceable restrictions to maximum enforceable scope.

### 8. Dispute Resolution

- Governing law: employee's work state (or employer HQ with substantial relationship)
- Arbitration: AAA or JAMS Employment Rules; employer bears fees
- Class/collective waiver if jurisdiction permits (note NLRA risk)
- Injunctive relief carve-out for confidentiality/non-disparagement/covenant breaches (irreparable harm presumption)
- Designated courts: state and federal in employer HQ or work location county

### 9. Cooperation and Transition

- Employee cooperates in pending/future litigation, investigations, regulatory proceedings
- Employer reimburses expenses and compensates at reasonable hourly rate for post-termination cooperation (unless subpoenaed)

### 10. Representations and Boilerplate

**Employee represents**: read and understood agreement, consulted or had opportunity to consult counsel, signing voluntarily, property returned, no retained confidential information, no undisclosed claims, received all earned wages, severance exceeds amounts owed, tax withholding applies.

**Boilerplate**: integration (carve out PIIA, equity plan docs, indemnification agreements), written amendment only, severability, no assignment by employee, no-waiver, non-admission of liability, notice provisions.

### 11. Signature Block

Standard dual signature block (employee + authorized company signatory with title). For age 40+, place OWBPA acknowledgment block immediately above employee signature line.

## Critical Compliance Checks

- **CA non-compete**: never include — courts refuse enforcement against CA residents regardless of choice-of-law
- **State income thresholds**: CO, WA, IL have annually changing thresholds for non-compete eligibility — verify current values
- **OWBPA strict liability**: miscalculated consideration or revocation periods void the entire ADEA release
- **DTSA notice mandatory**: must appear verbatim in any agreement restricting trade secret use
- **CA § 1542**: include verbatim waiver for any employee with California nexus
- **NLRA Section 7**: non-disparagement and confidentiality clauses must preserve rights to discuss wages, hours, and working conditions
- **Group RIF OWBPA**: 2+ terminations require 45-day period plus disclosure of decisional unit, eligibility criteria, and ages/job titles
- **Clawback + state wage law**: structure as contractual repayment, not wage deduction (especially CA)

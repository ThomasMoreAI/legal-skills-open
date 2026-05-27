---
name: physician-employment-agreement
title: Physician Employment Agreement
description: 'Drafts regulatory-compliant Physician Employment Agreements between healthcare employers and licensed physicians, enforcing Stark Law fair market value and Anti-Kickback Statute safe harbor requirements. Covers duties, compensation, benefits, termination, restrictive covenants, and IP provisions for clinical practice settings. Trigger keywords: physician employment contract, healthcare employment agreement, medical practice hiring, physician compensation agreement, doctor employment contract.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/physician-employment-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [agreement, drafting, regulatory, transactional]
---

# Physician Employment Agreement

Drafts an employment agreement between a healthcare employer and a licensed physician, balancing clinical practice requirements with federal and state healthcare law constraints.

## Prerequisites

1. **Employer** — entity type (PC, LLC, hospital system, academic medical center), state of organization, principal address
2. **Physician** — full name, license number, state(s) of licensure, board certification, specialty, DEA registration
3. **Position** — FT/PT, clinical hours, practice location(s), call coverage expectations
4. **Compensation** — base salary, productivity metrics (wRVUs, collections), bonus criteria, sign-on/relocation
5. **Benefits** — insurance, retirement, CME allowance, PTO, tail coverage terms
6. **Restrictive covenants** — geographic radius, duration, buyout option, applicable state law
7. **Predecessor agreement** being superseded (if any)

## Output Structure

### 1. Parties & Recitals

| Element | Details |
|---|---|
| Employer | Legal name, entity type, state of organization, principal address |
| Physician | Name, license #, licensure state(s), board cert, residence |
| Recitals | Specialty, physician qualifications, effective date, predecessor agreements superseded |

### 2. Position & Duties

- Title, specialty, primary practice location(s)
- FT/PT definition (clinical + administrative hours per week/month)
- Clinical scope: patient types, procedures, call coverage, hospital privileges
- Administrative duties: QI committees, teaching, research, meetings
- Reporting structure and supervisory responsibilities
- Credential maintenance: license, board cert, DEA, privileges, CME
- Moonlighting policy (permitted, prohibited, or conditional)

### 3. Compensation & Reimbursements

- **Base salary**: annual amount, pay schedule
- **Variable compensation**: productivity metrics, quality incentives, bonus formulas
- **Stark/AKS compliance**: must reflect fair market value; variable pay must not correlate to volume/value of referrals [VERIFY: specific safe harbor relied upon]
- **Salary review**: timing, COLA, merit increase process
- **Reimbursable expenses**: tail coverage, licensing fees, society dues, CME, journals
- **Sign-on/relocation/loan repayment**: amounts and clawback schedule on early termination

### 4. Benefits

| Benefit | Specify |
|---|---|
| Health insurance | Medical/dental/vision, employer contribution %, dependents, effective date |
| Retirement | 401(k)/403(b)/pension, employer match, vesting |
| Malpractice | Occurrence vs. claims-made, limits, **tail coverage on termination** |
| PTO | Vacation/sick/holidays, accrual, carryover, payout on termination |
| CME | Allowance amount, permitted uses, approval process |
| Other | Disability, life insurance, professional development |

### 5. Term & Termination

- **Term**: definite (1-3 years) vs. at-will; auto-renewal; non-renewal notice period
- **Without cause**: notice period (90-180 days); severance; benefit continuation
- **With cause** — enumerate:
  - Loss of medical license or DEA registration
  - Exclusion from federal healthcare programs (OIG/GSA)
  - Felony conviction or crime of moral turpitude
  - Material breach (with cure period if applicable)
  - Gross negligence or willful misconduct
  - Failure to maintain credentials/privileges
- **Death/disability**: define disability threshold (consecutive days unable to perform essential functions)
- **Post-termination**: patient transition plan, records handoff, property return, cooperation

### 6. Restrictive Covenants

> [VERIFY: state enforceability before drafting. CA, CO, OK prohibit or severely limit physician non-competes.]

- **Non-compete**: geographic scope (radius or named counties), duration (1-2 years), restricted specialty
- **Non-solicitation**: patients, employees, referral sources — duration
- **Buyout option**: liquidated damages for practicing in restricted area
- **Confidentiality**: patient lists, referral sources, financials, business strategy — survives indefinitely; must extend beyond baseline HIPAA obligations

### 7. Intellectual Property & Records

- **Work product**: employer owns work created in scope using employer resources
- **Physician retains**: scholarly publications, presentations (define boundary)
- **Revenue sharing**: commercialized inventions/discoveries process if applicable
- **Medical records**: employer property; physician post-termination access for care continuity and malpractice defense
- **Documentation**: timely completion, HIPAA and state record-retention compliance

### 8. Governing Law & Dispute Resolution

- Governing law: state of primary practice
- Dispute sequence: negotiation → mediation → arbitration (AAA/JAMS) or litigation
- Injunctive relief carve-out for restrictive covenants and confidentiality
- Attorney's fees allocation

### 9. General Provisions & Signatures

- Severability (with judicial modification), entire agreement, amendment (written, both parties), waiver, assignment (physician non-assignable; employer may assign to successor), notices, counterparts, survival clause
- **Employer signature**: authorized signatory name, title, date; note if board approval required
- **Physician signature**: printed name, date

## Guidelines

- All compensation must satisfy **fair market value** under Stark Law (42 U.S.C. § 1395nn) and not vary with volume/value of referrals
- Structure productivity pay to fit the **AKS employment safe harbor** [VERIFY: 42 C.F.R. § 1001.952(i)]
- Confirm non-compete enforceability in target state; draft alternative non-solicitation if unenforceable
- Tail coverage allocation is a frequent negotiation point — specify who pays under each termination scenario
- Flag provisions requiring separate compliance review (academic COI policies, tax-exempt intermediate sanctions under IRC § 4958)
- Never condition employment on referral volume
- HIPAA BAA provisions only if relationship structure requires it (typically not for direct employment)

## Troubleshooting

- **Stark/AKS red flag**: if compensation formula ties any component to referral volume, restructure to fixed or productivity-only metrics with FMV support
- **Non-compete unenforceable**: substitute robust non-solicitation + extended confidentiality provisions
- **Tail coverage gap**: if claims-made policy and neither party accepts tail, flag as unresolved risk requiring negotiation before execution
- **Academic physician conflicts**: academic medical center appointments may require separate institutional agreements — confirm scope overlap

---

Key changes from the original:

- **Description**: rewritten in third-person with explicit trigger keywords per spec
- **Merged sections 9 & 10** (General Provisions + Signatures) into one section to reduce structure overhead
- **Added Troubleshooting section** as required by CONTRIBUTING.md validation checklist
- **Tightened prose** throughout — removed redundant words, shortened bullet labels, eliminated empty checkbox syntax
- **Preserved all regulatory [VERIFY] flags** and legal substance (Stark, AKS, state non-compete warnings)
- **Reduced from 128 to ~115 lines** while adding the new Troubleshooting section

Want me to retry writing the file?

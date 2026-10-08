---
name: workflow-fire-employee-pack-sboghossian
title: Employee Termination Pack
description: Use when a user needs to manage an employee termination from a legal and documentation standpoint — covering pre-termination risk assessment, final pay calculation, document generation, visa cancellation in MENA, government deregistration, and post-termination compliance. Provides jurisdiction-specific guidance for UAE (Federal Decree-Law 33/2021), KSA (Labour Code Arts 76–80), Lebanon (Labor Code Arts 50/74), and DIFC Employment Law.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/workflow/workflow-fire-employee-pack
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Employee Termination Pack

## Purpose

This workflow orchestrates the complete legal documentation and compliance process for employee termination. It covers performance-based dismissal, redundancy, mutual separation, and termination for cause — with specific MENA jurisdictional rules that differ materially from US/UK defaults. The workflow minimizes legal risk by ensuring proper documentation, correct final pay calculation, and timely government filings.

---

## Inputs

| Input | Required | Notes |
|-------|---------|-------|
| Employee name and role | Yes | |
| Jurisdiction | Yes | Determines law, procedure, and government filings |
| Termination type | Yes | Performance, redundancy, cause, mutual |
| Employment start date | Yes | Determines EOSG entitlement and notice period |
| Contract type | Yes | Fixed-term vs. indefinite — different rules |
| Nationality | Yes | Non-citizen employees in MENA require visa cancellation |
| Annual salary + benefits | Yes | For final pay calculation |
| Accrued leave balance | Yes | Unpaid leave must be included in final settlement |
| Documentation of issues | For performance | PIPs, warnings — needed to defend against wrongful dismissal |
| Pending equity | If applicable | Vesting acceleration or forfeiture considerations |

---

## Logic — Pre-Termination Checklist

Before scheduling the termination meeting, complete every item:

### 1. Documentation Review

**For performance-based termination:**
- Is there a paper trail? Minimum expectation: at least one documented warning or PIP
- Were warnings issued in writing? See [[draft-warning-letter]] and [[draft-pip-letter]]
- Was the employee given a reasonable opportunity to improve?
- Gap: if the paper trail is thin, extending a final written warning before termination reduces litigation exposure

**For redundancy:**
- Is the role genuinely being eliminated? Economic substance required — cannot use "redundancy" to mask discriminatory dismissal
- Is there a selection criterion? Document the business rationale
- Is there a consultation requirement? (Mass redundancy rules — see jurisdictional notes)

**For cause termination:**
- Does the conduct fall within the contractual or statutory definition of "cause"?
- Is the evidence documented and sufficient?

### 2. Protected Category Risk Assessment

Flag before proceeding:
- Is the employee on parental leave, sick leave, or disability-related absence? Terminating during protected leave creates significant legal exposure in most jurisdictions
- Has the employee made a complaint (harassment, discrimination, whistleblower) recently? Post-complaint termination is presumed retaliatory in many jurisdictions — document the independence of the termination decision from any complaint
- Is the employee a member of a union or workers' committee? Consultation obligations may apply
- Is the employee in a protected age/pregnancy/religion category that makes the timing of termination look suspect?

### 3. Final Pay Calculation

Calculate immediately; do not estimate. Use [[tool-calculator-end-of-service-gratuity]] for MENA.

Components of final settlement (MENA):

| Component | Notes |
|-----------|-------|
| Last salary (pro-rated) | To the actual date of termination |
| Accrued unpaid annual leave | Days × daily rate |
| End of Service Gratuity (EOSG) / End of Service Award (EOSA) | Statutory formula; jurisdiction-dependent (see below) |
| Notice pay in lieu | If serving notice is not practical |
| Contractual bonuses vested | Any bonuses accrued but not yet paid |
| Expense reimbursements | Pending expense claims |
| Ex gratia / severance | If agreed; forms part of settlement agreement |

**EOSG formulas (summary):**
- **UAE** (Decree-Law 33/2021): 21 days per year for years 1–5; 30 days per year for years 5+; maximum 2 years' total; reduced for resignation in some cases
- **KSA** (Labour Code): after 2 years: 0.5 months per year; after 5 years: 1 month per year; termination vs. resignation affects entitlement
- **Lebanon** (Labor Code): complex formula based on years of service and final salary; payable by the National Social Security Fund (NSSF) for registered employees + employer top-up

### 4. Property and Access Inventory

Before the termination meeting, prepare:
- List of company equipment held by the employee (laptop, phone, access cards, vehicles)
- System access to be revoked (email, VPN, HR systems, CRM, code repositories, cloud platforms)
- IP and confidential documents — does the employee have company data on personal devices?
- Company credit cards to be cancelled

---

## Logic — Day of Termination

The termination meeting should be:
- Brief (15–30 minutes maximum)
- In person where practicable; video call where geography requires
- Witnessed: manager + HR representative present; document who attended
- Dignified: even for cause terminations, conduct the meeting professionally

### Meeting Sequence

1. **Deliver the termination decision** — clear and unequivocal; do not hedge or leave room for misunderstanding
2. **Deliver the termination letter** in writing — [[draft-termination-letter]] — confirm receipt
3. **Explain the next steps**:
   - Last day of work / garden leave period
   - Severance agreement review period (7–14 days; do not pressure for immediate signature)
   - Return of company property
   - Access revocation timeline
   - Visa cancellation process (for non-citizens in MENA)
4. **Collect property** where immediately practical (access cards, keys, physical devices)
5. **Revoke digital access** — IT should execute access revocation simultaneously with or immediately after the meeting
6. **Offer to conduct exit interview** (optional; not appropriate for all termination types)

---

## Deliverables

| Document | Skill | Notes |
|----------|-------|-------|
| Termination letter | [[draft-termination-letter]] | Required; states date, reason, final pay details |
| Severance / separation agreement | [[draft-severance-agreement]] | If offering severance above statutory minimum |
| Reference letter | Agreed language (positive/neutral) | Optional; agree wording before delivering |
| Final settlement calculation | [[tool-calculator-end-of-service-gratuity]] | Must accompany or follow the termination letter promptly |
| Return-of-property checklist | Schedule to termination letter | Documents what was returned and when |
| Confidentiality reminder | Integrated into separation agreement | Reminds employee of existing obligations |

---

## Post-Termination Compliance

### Government Filings (MENA)

| Jurisdiction | Filing | Deadline |
|-------------|--------|---------|
| UAE (MOHRE) | Termination notification and visa cancellation | Within 30 days of employment end |
| UAE (WPS) | Final wages must be processed through Wage Protection System | Per WPS timeline |
| KSA (Qiwa / GOSI) | Deregister employee on Qiwa platform; GOSI contribution cessation | Promptly; affects employee's entitlement to social insurance |
| Lebanon (NSSF) | Deregistration with National Social Security Fund | Within one month |
| DIFC (DIFC Authority) | Employment Records maintained internally; no separate public registration | N/A |

### Visa Cancellation (Non-Citizens in MENA)

Critical and time-sensitive for expatriate employees:
- UAE: employer must apply for visa cancellation at MOHRE/GDRFA; employee receives a "grace period" (typically 60 days from visa cancellation) to arrange status
- KSA: iqama (residency permit) cancellation is employer's responsibility; Final Exit visa required if employee is leaving KSA permanently
- Timing: visa cancellation and final settlement are often linked; stagger appropriately — cancelling visa before paying final salary creates practical problems
- Employee's new employer (if known) should coordinate visa transfer if employee is staying in country

### Severance Agreement Review Window

The standard practice for voluntary severance above statutory entitlements:
- Provide the agreement with at least **7 days** for review (best practice: 14–21 days for significant severance packages)
- Advise the employee in writing of their right to seek independent legal advice
- Do not condition ongoing statutory entitlements on signing (only voluntary/additional severance)
- Mutual release in the agreement releases both employer and employee claims

---

## Jurisdictional Notes

### UAE — Federal Decree-Law 33/2021

- Arbitrary dismissal (al-fasakh al-ta'assufi): employer must pay the employee the equivalent of 3 months' salary if dismissal was arbitrary in addition to EOSG and notice pay
- Notice period: minimum 30 days for unlimited contracts (contractual notice if longer); fixed-term contracts may have early termination clauses or require paying out the remainder
- Non-compete: enforceable if reasonable in time (max 2 years), geography, and scope; but KSA and UAE courts have had inconsistent enforcement histories

### KSA — Labour Code

- Article 80: grounds for termination with cause (no EOSG due): assault, dishonesty, intoxication, abandonment
- Article 76: notice period (60 days for monthly-paid workers on unlimited contract)
- Female employee protections: cannot terminate during pregnancy or maternity leave
- Mass layoffs: require Ministry of Human Resources approval for layoffs exceeding a threshold

### Lebanon — Labor Code

- Article 50: termination without cause — employer must pay EOSG (indemnité de fin de service) per the NSSF scheme + contractual compensation
- Article 74: termination for cause — no EOSG if serious fault proven
- NSSF registration gap: many employees in Lebanon were historically unregistered with NSSF; employer retains direct EOSG liability for unregistered employees

### DIFC Employment Law

- Applies to all DIFC-registered entities
- Minimum statutory redundancy pay: 21 days per year for the first 5 years; 30 days per year thereafter
- Arbitrary dismissal: compensation up to 3 months pay for unfair dismissal
- DIFC Employment Tribunal: accessible forum; relatively fast proceedings

---

## Risk Register

| Risk | Description | Mitigation |
|------|-------------|-----------|
| Discrimination claim | Termination correlated with protected status (age, sex, religion, nationality, recent complaint) | Document objective, non-discriminatory basis; segregate decision from any protected activity |
| Retaliation claim | Termination shortly after employee complaint (whistleblower, harassment) | Independent investigation; temporal gap; documented pre-existing performance issues |
| Wrongful dismissal (insufficient cause) | For-cause termination where documentation is thin | Shift to no-cause termination with full EOSG; or delay and build documentation |
| Mass redundancy non-compliance | Exceeding statutory thresholds without consultation | Pre-count affected employees; check thresholds before announcement |
| Equity windfall/forfeiture disputes | Termination triggers accelerated vesting or forfeiture of unvested equity | Review plan documents carefully; document termination type (cause vs. no cause) |
| Visa overstay (expatriate) | Employee fails to leave or transfer status after visa cancellation | Coordinate timing of visa cancellation with employee's transition plans |

---

## Related Skills

- [[workflow-hire-employee-pack]]
- [[draft-termination-letter]]
- [[draft-severance-agreement]]
- [[draft-pip-letter]]
- [[draft-warning-letter]]
- [[tool-calculator-end-of-service-gratuity]]

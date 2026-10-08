---
name: workflow-hire-employee-pack-sboghossian
title: Employee Hiring Pack
description: Use when an organization needs to hire an employee and requires the full legal document pack — from offer letter through employment contract, IP assignment, equity grant, restrictive covenants, government registration, and onboarding compliance. Covers jurisdiction-specific employment contracts for UAE (Decree-Law 33/2021), KSA (Labour Code), and Lebanon (Labor Code), with MENA-specific visa/work permit and government registration steps (MOHRE, Qiwa, NSSF).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/workflow/workflow-hire-employee-pack
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Employee Hiring Pack

## Purpose

This workflow generates the complete legal documentation set for a new employee hire and guides the employer through all government registration and compliance steps. The output is a signed employment package, registered employment relationship, and a compliant Day-1 onboarding record.

---

## Inputs

| Input | Required | Notes |
|-------|---------|-------|
| Jurisdiction | Yes | Determines applicable law and government filings |
| Employee role and title | Yes | |
| Compensation (salary, currency, frequency) | Yes | Must align with local minimum wage requirements |
| Contract type | Yes | Indefinite vs. fixed-term; full-time vs. part-time |
| Employee nationality | Yes | Drives visa/work permit requirements in MENA |
| Start date | Yes | |
| Probation period | Yes | Typical: 3–6 months (jurisdiction-specific maximums) |
| Equity (if applicable) | If applicable | Vesting schedule, option pool |
| Restrictive covenants (if applicable) | If applicable | Non-compete, non-solicit scope and duration |
| Benefits package | Yes | Health insurance, transport, housing, air tickets (MENA common) |

---

## Deliverables Overview

| Document | Skill | Jurisdiction |
|----------|-------|-------------|
| Offer letter | [[draft-offer-letter]] | All |
| Employment contract | [[draft-employment-contract-uae]] / [[draft-employment-contract-ksa]] / [[draft-employment-contract-lb]] | Jurisdiction-specific |
| IP assignment | [[draft-ip-assignment]] | All (especially tech roles) |
| Non-compete / Non-solicit | [[draft-non-compete]] | If required |
| Equity grant letter + vesting schedule | [[draft-vesting-schedule]] | If equity is granted |
| Employee handbook acknowledgment | Pre-existing firm document | Reference only |
| Background check consent | Separate consent form | |
| Visa/work permit sponsorship documentation | Government forms | Non-citizen employees in MENA |
| Government registration (MOHRE/Qiwa/NSSF) | Government portal | MENA jurisdictions |

---

## Logic — Workflow Steps

### Step 1: Job Offer Accepted

Once an oral offer is accepted, the written offer letter should follow within 24 hours:

**Offer letter** — [[draft-offer-letter]] — key elements:
- Role, title, reporting line
- Start date and location
- Compensation (base salary, currency, payment frequency)
- Benefits (health insurance, transport, housing allowance — must comply with local minimums)
- Probation period and length
- Conditional nature of offer (subject to background check, reference check, work authorization)
- Deadline for acceptance (typically 3–5 business days)
- Governing law (for multi-jurisdiction roles)

**Offer letter ≠ employment contract**: the offer letter is a pre-contractual document. In civil law jurisdictions (UAE, KSA, LB), the employment contract is the primary legal instrument. Issue the offer letter immediately; issue the contract before or on the start date.

### Step 2: Background Check and Reference Verification

Run before issuing final contract:
- Standard: employment history verification; education credential check; identity verification
- For senior/financial roles: criminal record check (where legal and available); credit check (financial services)
- Reference check: minimum two professional references
- In UAE and KSA: INTERPOL check or equivalent may be required for certain roles
- Data privacy compliance: obtain written consent before running checks; process only the data necessary; retain only as long as required

### Step 3: Employment Contract Drafting

Load the jurisdiction-specific skill:

**UAE Employment Contract** — [[draft-employment-contract-uae]]:
- Governed by Federal Decree-Law 33/2021 (effective 2 February 2022); supersedes all prior employment law
- Key contract elements required: parties, job title, start date, work location, working hours, salary, leave entitlement, probation period
- Fixed-term contracts: maximum 3 years; renewable; non-renewal triggers EOSG entitlement
- Working hours: 8 hours per day / 48 hours per week maximum; Ramadan reduced hours for Muslim employees
- Annual leave: minimum 30 days after 1 year (if hourly-based); proportional for shorter periods
- EOSG: 21 days per year of service for first 5 years; 30 days for years 5+
- Non-compete: enforceable if limited in time (max 2 years), geography, and scope; must be in the contract
- Language: Arabic text is authoritative for UAE labor proceedings; bilingual contracts recommended

**KSA Employment Contract** — [[draft-employment-contract-ksa]]:
- Governed by Labour Law (Royal Decree M/51) and implementing regulations
- Arabic text controls; employer must provide Arabic version
- Fixed-term: maximum 4 years; default is indefinite for Saudi nationals
- Working hours: 8 hours per day / 48 hours per week; 6 hours per day during Ramadan
- Annual leave: 21 days (first 5 years); 30 days thereafter
- Saudization (Nitaqat): employers must maintain the required ratio of Saudi nationals in their workforce; new hires should be tracked against this
- GOSI (General Organization for Social Insurance): employer registers employee; contributes 12% of salary (Saudi nationals); 2% (expatriates)
- Non-compete: generally enforceable if reasonable; courts apply equity considerations

**Lebanon Employment Contract** — [[draft-employment-contract-lb]]:
- Governed by Labor Code (Law 136 of 1983 as amended) and related legislation
- NSSF (National Social Security Fund) registration mandatory; contributions split employer/employee
- Annual leave: 15 days (first 5 years); 18 days (6–10 years); 21 days thereafter
- Currency considerations: LBP or USD depending on agreed currency; critical given Lebanese pound instability — specify currency clearly
- Language: Arabic or French acceptable; bilingual contracts common for international employers
- Labor courts in Lebanon: relatively accessible but slow; consider dispute resolution clause

**DIFC Employment Contract**:
- Governed by DIFC Employment Law (DIFC Law 2 of 2019 as amended)
- English law concepts with DIFC-specific statutory minimums
- Must include: parties, remuneration, working hours, annual leave, pension contribution, dispute resolution

### Step 4: IP Assignment

For any role involving creation of intellectual property (technology, content, design, legal work product):

**IP assignment clause in employment contract** or standalone [[draft-ip-assignment]]:
- All work created in the course of employment and related to the employer's business is assigned to the employer
- Includes work created using company resources even outside normal hours
- Prior IP carve-out: identify any pre-existing IP the employee wants to exclude (attach as schedule)
- Moral rights: in civil law jurisdictions (Lebanon, France) employees retain moral rights in creative works even after economic rights are assigned — address how these are handled

### Step 5: Visa and Work Permit (Non-Citizens in MENA)

Non-citizen employees require employer-sponsored work authorization in UAE, KSA, and most MENA jurisdictions:

**UAE process:**
1. Entry permit application (Ministry of Human Resources / GDRFA)
2. Medical fitness test in UAE
3. Emirates ID registration (ICA)
4. Residence visa issuance (stamped in passport)
5. Work permit (integrated with residence visa process)
Timeline: typically 4–8 weeks from offer acceptance; begin immediately

**KSA process:**
1. Work visa (MHRSD) — employer obtains a block visa or individual visa
2. Entry on work visa
3. Iqama (residence permit) application after arrival — employer sponsors
4. GOSI registration
5. Muqeem system registration
Timeline: typically 4–8 weeks; can be longer for specific nationalities

**Lebanon (pre-crisis normal procedure):**
1. Work permit from Ministry of Labor — employer sponsors
2. Residence permit from General Security
3. NSSF registration
Timeline: highly variable given administrative challenges

**Key risk: do not start employee before work authorization is confirmed.** Employing without proper authorization creates regulatory violations for both employer and employee.

### Step 6: Government Registrations

| Jurisdiction | Platform/Authority | What to register | Deadline |
|-------------|-------------------|-----------------|---------|
| UAE | MOHRE (Ministry of Human Resources and Emiratisation) | Employment contract; employee details | Before or on start date |
| UAE | WPS (Wage Protection System) | All employees; ensures timely salary payment | Ongoing monthly |
| KSA | Qiwa (Ministry of Human Resources) | All employment contracts; Saudization tracking | Before start date |
| KSA | GOSI | Social insurance contributions | On hire |
| LB | NSSF (National Social Security Fund) | All Lebanese national and registered expatriate employees | Within 1 month of hire |
| DIFC | No public registration; internal records | Employment contract on file per DIFC Employment Law | Before start date |

### Step 7: Equipment and Access Provisioning

Before Day 1:
- Laptop, phone, access cards provisioned
- Email and system access configured
- Security training scheduled
- NDA/confidentiality reminder reviewed

### Day 1 Checklist

- [ ] Employment contract signed by both parties
- [ ] Offer letter countersigned
- [ ] IP assignment signed (if standalone)
- [ ] Employee handbook acknowledged in writing
- [ ] Background check results on file and satisfactory
- [ ] Access provisioned
- [ ] Welcome meeting with manager
- [ ] IT setup complete

### 90-Day Probation Review

Schedule a formal review at day 60 (advance notice if termination during probation is likely):
- Performance evaluation against agreed objectives
- If extending probation or terminating: written notice required (jurisdiction-specific minimum notice during probation is typically shorter than post-probation)
- Successful completion: confirm in writing; probation benefit changes (if any) take effect

---

## Jurisdictional Watchpoints

### UAE

- Mandatory health insurance: Dubai Health Authority and Abu Dhabi Health Authority both require employers to provide health insurance for all employees and their qualifying dependents
- Annual flight ticket: common practice for expatriate employees; not statutory but contractually common; address in offer letter
- Housing/transport allowances: frequently provided; if restructured or reduced, may constitute constructive dismissal

### KSA

- Saudization compliance: failure to meet Nitaqat quotas results in restricted government services for the employer
- Female employee considerations: ensure workplace policies comply with anti-discrimination requirements under Vision 2030 reforms
- Non-Muslim employees: alcohol and certain other items prohibited; address in employee handbook

### Lebanon

- Currency clauses: specify whether salary is in USD or LBP and at what rate; critical given the de facto peg collapse since 2019
- NSSF registration gap: many employers in Lebanon are not registered with NSSF; avoid this — the employer bears direct liability for EOSG if unregistered

---

## Skills Loaded Together

This workflow activates: [[conversation-intake-employment-contract]] for intake; [[heuristic-always-state-jurisdiction-first]] for all outputs; jurisdiction-specific drafting skills (UAE, KSA, LB); and [[draft-ip-assignment]] and [[draft-non-compete]] as supplementary documents.

---

## Related Skills

- [[workflow-fire-employee-pack]]
- [[draft-offer-letter]]
- [[draft-employment-contract-uae]]
- [[draft-ip-assignment]]
- [[draft-non-compete]]
- [[draft-vesting-schedule]]
- [[conversation-intake-employment-contract]]
- [[heuristic-always-state-jurisdiction-first]]

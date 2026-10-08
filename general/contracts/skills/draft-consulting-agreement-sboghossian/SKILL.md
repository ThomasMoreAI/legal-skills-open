---
name: draft-consulting-agreement-sboghossian
title: Draft — Consulting Agreement
description: Use when asked to draft a consulting or consultancy agreement engaging an independent contractor (individual or entity) to provide professional services. Covers the critical independent-contractor-vs-employee classification risk, standard clause set (services, compensation, IP assignment, confidentiality, non-compete), and MENA-specific misclassification triggers for Lebanon, KSA, UAE, and DIFC/ADGM. P0 priority — misclassification creates retrospective employment liability, GOSI exposure, and regulatory violations.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-consulting-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Draft — Consulting Agreement

## When to use this

Use this skill when a company or organization engages an individual (or an entity) to provide professional services on a project or retainer basis outside of an employment relationship.

**Critical preliminary question**: is this arrangement genuinely an independent contractor relationship, or is it economically an employment relationship dressed up in consulting documentation? Misclassification is the most dangerous risk in this type of agreement — courts and labor authorities look through the document to the economic reality.

## Required inputs

| Input | Notes |
|---|---|
| Company / Client | Full legal name, registration, signatory authority |
| Consultant | Individual or entity; nationality; if individual, work permit / visa status |
| Services scope | Precise description; deliverables vs hours; outcomes expected |
| Compensation | Rate structure; invoicing frequency; currency |
| Duration | Fixed-term project vs rolling retainer |
| Governing law | Determines employment-vs-contractor test |
| IP provisions | Will Consultant create IP? Who owns it? |
| Non-compete / non-solicit | Duration and scope needed? |

## Independent contractor vs employee — the critical classification risk

This is the first analytical step before drafting any consulting agreement. Courts and labor authorities look at the economic reality of the relationship, not the label the parties give it.

### Factors indicating genuine independent contractor status (draft to support these)

| Factor | What to include in the agreement | What to avoid |
|---|---|---|
| Control over method | "Consultant determines how to perform the Services" | Mandating specific working hours, office presence, supervision |
| Tools / workspace | "Consultant uses own tools and equipment" | Company-provided laptop, desk, email account as the primary tool |
| Economic independence | "Consultant serves multiple clients" | Exclusivity provision (or de facto exclusivity in practice) |
| Risk of loss | "Consultant bears professional liability for defective deliverables" | Guaranteed payment regardless of output |
| Project-based | "Services are project-based; compensation per deliverable" | Ongoing tasks with no defined deliverable |
| Invoicing | "Consultant invoices the Company periodically" | Direct salary payment without invoice |
| Benefits exclusion | "Consultant is not entitled to employment benefits, GOSI, gratuity, health insurance" | Providing any employment-type benefits |

### MENA jurisdiction-specific misclassification risks

#### Lebanon
- Factual test: courts examine control, integration into the business, and economic dependence.
- Sustained exclusive relationship with one principal is a strong indicator of employment.
- Misclassification consequence: CNSS (social security) back-contributions; end-of-service indemnity; annual leave accrual; reinstatement risk.
- **Recommendation**: avoid more than 2 years of exclusive engagement; require consultant to invoice; do not integrate into payroll systems.

#### KSA (Labour Law — Royal Decree M/51 2005, as amended)
- GOSI (General Organization for Social Insurance) registration is mandatory for employees.
- Sustained relationship with one principal at a set location triggers labor law protection regardless of contract label.
- Misclassification consequence: GOSI back-payments; end-of-service award (ESB); reinstatement; potential visa/iqama irregularities.
- **Visa/work permit consideration**: if an individual is in KSA on a work visa sponsored by the Company, they are legally an employee under KSA law regardless of the contract label. Pure consulting arrangements must use a third-party entity or free-zone vehicle.

#### UAE (Federal Decree-Law 33/2021 on Labour Relations)
- Decree-Law 33/2021 narrowed the informal "part-time" and project-based arrangements that avoided full employment obligations.
- Genuine consultants can operate via their own UAE commercial license (freezone or mainland) or through a corporate entity.
- Individual consultants without their own license working exclusively for one company on a sustained basis are at high risk of reclassification.
- **UAE free zone / mainland distinction**: a consultant providing services from a DIFC or ADGM entity has a cleaner independent contractor path.

#### DIFC / ADGM
- DIFC Employment Law (DIFC Law 4/2005 as amended) and ADGM Employment Regulations 2019 apply to employees working at DIFC/ADGM entities.
- Independent contractor status is more clearly preserved if the consultant: uses their own entity, serves multiple clients, has genuine commercial independence.
- DIFC/ADGM do not apply labor law to non-employed contractors; the consulting agreement governs.

#### France / EU
- The "requalification" risk (requalification en contrat de travail) is even more aggressively enforced in France.
- Minimum test: does the principal have authority to give the consultant orders and instructions on method (not just outcome)? If yes, likely employment.
- EU Platform Work Directive (2024): extends employment presumption to platform workers.

## Standard clauses

### 1. Services
```
The Consultant shall provide the following services:
[Precise description of deliverables / outcomes / scope]
(the "Services").

The Consultant shall perform the Services [by the Completion Date 
of [DATE] / on an ongoing basis during the Term / in accordance 
with the milestones in Schedule A].
```

Do not: use language like "at the Company's direction on a day-to-day basis" — this sounds like employment.

### 2. Compensation
```
The Company shall pay the Consultant a fee of [CURRENCY AMOUNT 
per hour / per deliverable / per month] (the "Consulting Fee").
The Consultant shall submit invoices [monthly / upon completion 
of each milestone] and the Company shall pay within [30] days 
of receipt.

All taxes applicable to the Consulting Fee are the 
Consultant's sole responsibility. The Company shall not 
withhold employment taxes from payments to the Consultant.
```

### 3. Independent contractor declaration
```
The Consultant is an independent contractor. Nothing in this 
Agreement creates an employment, partnership, agency, or 
joint venture relationship between the parties. The Consultant 
is not entitled to, and shall not claim, any employment 
benefits, social security contributions, end-of-service 
gratuity, or other rights of an employee under applicable law.
```

### 4. Intellectual property — work product ownership
Two standard approaches:

**Company-owns-all approach** (common for technology, creative, strategic deliverables):
```
All deliverables and work product created by the Consultant 
in the course of performing the Services (the "Work Product") 
shall be the sole and exclusive property of the Company. 
The Consultant hereby assigns to the Company all right, title, 
and interest in and to the Work Product, including all 
intellectual property rights.
```

**Pre-existing IP carve-out** (important for experienced consultants with existing tools):
```
The foregoing assignment does not apply to any intellectual 
property owned by the Consultant prior to the date of this 
Agreement or developed independently of the Services 
("Pre-existing IP"). The Consultant grants the Company a 
[non-exclusive / exclusive] license to use any Pre-existing 
IP embedded in the Work Product for the purposes of this 
Agreement.
```

**IP assignment for MENA jurisdictions**: in UAE, KSA, and LB, IP rights must be formally assigned in writing; copyright assignments require registration to be effective against third parties in some jurisdictions. Plan for IP office filings where the work product includes patentable or registrable IP.

### 5. Confidentiality
Standard bilateral confidentiality; the Consultant receives confidential business information:
```
The Consultant shall keep confidential all non-public 
information received from the Company in connection with 
the Services and shall not disclose such information to 
any third party without the Company's prior written consent.
This obligation survives termination of the Agreement for 
[3] years / indefinitely for trade secrets.
```

### 6. Non-compete and non-solicit
Consider enforceability before including:
- Duration: 6–24 months post-termination; shorter is more enforceable.
- Geographic scope: limited to the jurisdictions where the Consultant actually worked.
- Activity scope: limited to directly competitive activities, not all business activity.
- **Enforceability notes**:
  - DIFC / ADGM: non-competes enforceable if reasonable in scope, duration, and geographic reach; courts apply the balance-of-convenience test.
  - UAE onshore: non-competes for employees and contractors are enforceable under Article 10 of Decree-Law 33/2021 if they meet the statutory requirements.
  - KSA: non-compete clauses for employees/contractors are of uncertain enforceability; courts focus on harm to the restrained party's livelihood.
  - LB: non-competes limited by Code of Obligations and Contracts Article 230; duration more than 2 years rarely enforced.
  - FR: non-compete requires financial compensation (indemnité de non-concurrence) to be enforceable; without compensation, the clause is void.
- See [[draft-non-compete]] for dedicated non-compete drafting guidance.

### 7. Term and termination
```
This Agreement commences on [DATE] and continues until [DATE / 
completion of the Services / termination by either Party on 
[30] days' written notice].

Either Party may terminate this Agreement immediately for 
cause (material breach not remedied within [14] days of 
notice; insolvency).
```

### 8. Governing law and dispute resolution
See [[draft-boilerplate-clauses]] for standard options. For MENA:
- DIFC law + DIFC Courts or DIAC arbitration: recommended for cross-border or high-value consulting arrangements.
- UAE Federal Law: default for onshore UAE.
- KSA Law: mandatory for KSA-seated arrangements; Sharia principles apply.

## Reducing misclassification risk — practical checklist

- [ ] Consultant invoices the Company (not direct salary payment)
- [ ] Consultant uses own tools and equipment
- [ ] Consultant has (or should have) multiple clients
- [ ] No fixed working hours or mandatory office attendance
- [ ] Deliverables defined by outcome, not by hours
- [ ] No employment benefits provided
- [ ] IP and confidentiality agreements in place
- [ ] Engagement is project-based or has a defined term
- [ ] Exclusivity avoided (or time-limited with commercial justification)
- [ ] For UAE/KSA: Consultant has own commercial license or operates through a corporate entity

## Bilingual note (MENA)

For MENA: Arabic-English side-by-side preferred. See [[draft-bilingual-ar-en-side-by-side]]. Check whether the Consultant's work permit / visa requires employment-form documentation.

## Related skills

- [[draft-agency-agreement]]
- [[draft-boilerplate-clauses]]
- [[draft-non-compete]]
- [[draft-bilingual-ar-en-side-by-side]]

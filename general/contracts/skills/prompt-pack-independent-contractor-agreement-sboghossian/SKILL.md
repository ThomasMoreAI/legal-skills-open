---
name: prompt-pack-independent-contractor-agreement-sboghossian
title: Independent Contractor Agreement
description: Use when drafting an independent contractor agreement engaging a freelancer or service provider — emphasizing independent contractor status, proper classification language, payment terms, IP assignment, confidentiality, and termination provisions compliant with jurisdiction-specific worker classification tests. Applicable across MENA (UAE, KSA, LB, EG, DIFC) and internationally. Misclassification risk is significant in MENA given mandatory labour law protections; this skill helps draft a defensible ICA. Trigger when a company is engaging an individual or entity for services without a full employment relationship.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-independent-contractor-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Independent Contractor Agreement

## When to use this

Use this skill when drafting an independent contractor agreement (ICA) — the contract by which a company engages an individual or entity to provide services on a non-employee basis. ICAs are used to engage consultants, freelancers, specialists, and professional service firms without the full legal protections (and obligations) that apply to employees.

The central legal risk of an ICA is worker misclassification: if the working relationship in practice resembles employment — the company controls how, when, and where work is done; the individual is economically dependent on the company; the services are integral to the business — courts and labour authorities will reclassify the relationship as employment, triggering retroactive obligations for salary, social insurance, gratuity, and other statutory entitlements.

Typical triggers:
- Company engaging a consultant, subject-matter expert, or freelancer for a defined project
- Startup engaging an early team member who is not yet a full employee
- Company with workforce needs in a jurisdiction where direct hiring is complex (expatriate in a new market)
- Agency or services firm contracting with an individual to deliver client work

**Critical note**: An ICA is not appropriate where the individual will be integrated into the company's operations as a regular worker with fixed hours, under the company's day-to-day direction, and without other clients. In that case, the relationship is employment.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Company name and jurisdiction | Determines applicable law; affects classification tests | Ask |
| Contractor name and entity type (individual / company) | Entity contractors have stronger independent status; individual = higher classification risk | Ask |
| Services description | Specificity of scope is key for independent status | Ask in detail |
| Fee structure and payment terms | How payment is structured affects classification | Ask |
| Duration (project-based vs. ongoing) | Ongoing / open-ended relationships carry higher classification risk | Ask |
| Governing law | Critical for enforceability of classification | Ask |

## Optional inputs

- Location of services performance (on-site at client vs. contractor's location)
- Equipment and tools (provided by company or contractor — significant classification factor)
- Exclusivity (can the contractor work for competitors?)
- IP scope (all work for hire vs. licensed use)
- Sub-contracting rights

## Document structure

### 1. Parties

- Company (the "Client" or "Company")
- Individual or entity (the "Contractor" or "Consultant")
- Effective date

### 2. Engagement and scope of services

- Specific description of services to be provided (attach a Statement of Work as an exhibit if detailed)
- Deliverables: what must the contractor produce?
- Milestones and timeline (for project-based engagements)
- Standards: deliverables must meet [specific quality standards / professional standards]
- Location of services: "Contractor shall perform the services from Contractor's own premises, unless otherwise agreed."

**Classification-protective language**:
> "Contractor shall determine the method, details, and means of performing the Services. Client may only specify the results to be achieved, not the manner of achieving them."

### 3. Compensation and payment

**Fixed fee / project fee**:
- Amount; payment schedule linked to milestones
- Invoice process: contractor submits invoice; client pays within [30] days

**Hourly / time-and-materials**:
- Hourly rate; maximum not-to-exceed budget
- Time reporting: contractor submits weekly timesheets

**Reimbursable expenses**:
- Pre-approved expenses only; itemized invoices with receipts required

**No entitlement to employment benefits**:
> "Contractor is not entitled to any employee benefits, including health insurance, annual leave, sick leave, end-of-service gratuity, pension contributions, or any other benefits provided by the Company to its employees."

### 4. Independent contractor status

The most important classification-protective section:

> "Contractor is an independent contractor and not an employee, agent, or partner of the Company. The Company exercises no control over the manner or means by which Contractor performs the Services, only the results thereof. Contractor is free to provide similar services to other clients."

Supporting provisions:
- Contractor is solely responsible for all taxes, social insurance, professional licenses, and permits required to perform the services
- Contractor acknowledges it is not entitled to statutory employment protections under [applicable Labour Law]
- Company will not deduct income tax or social insurance from payments to Contractor; Contractor is responsible for its own tax filings
- Contractor indemnifies the Company against any liability, tax, or penalty arising from Contractor's failure to comply with its tax or social insurance obligations

### 5. Equipment and tools

- Contractor provides its own equipment, tools, and resources
- If Company provides equipment: list what is provided; confirm it does not affect independent status by explicitly noting it is for project-specific access only

### 6. Intellectual property

**Work-for-hire (common-law jurisdictions)**:
> "All deliverables, works, inventions, and other IP created by Contractor in performance of the Services are works made for hire owned by the Company. To the extent any such works do not qualify as works made for hire, Contractor assigns all right, title, and interest to the Company."

**Assignment (civil-law / MENA jurisdictions)**:
> "Contractor assigns to the Company all intellectual property rights (including copyright, design rights, and patents) in all deliverables created in connection with the Services."

**Moral rights waiver** (UK / EU):
> "To the extent permitted by law, Contractor waives any moral rights in the deliverables in favor of the Company."

**Pre-existing IP carve-out**:
> "This assignment does not apply to Contractor's pre-existing IP. Contractor grants the Company a perpetual, royalty-free license to use any pre-existing IP incorporated in the deliverables."

### 7. Confidentiality

- Definition of confidential information (broad: all business, technical, financial, customer data of the Company)
- Obligation: use only for the purpose of performing the services; do not disclose to third parties
- Post-engagement survival: confidentiality obligation survives termination for [3 years / indefinitely for trade secrets]
- Standard exceptions: public domain, prior knowledge, legal obligation

### 8. Exclusivity and non-compete

Exclusivity should be avoided or narrowly drafted:
- Full exclusivity (contractor cannot work for anyone else) supports an employment classification finding
- Better approach: "Contractor may perform services for other clients, provided such clients do not compete directly with the Company in [specific market / product line], and provided the Contractor does not use the Company's confidential information in performing those services."

Post-engagement non-compete (if included):
- Duration: [6–12] months (shorter than employee non-compete given lower justified interest)
- Scope: limited to specific competitors or specific activities

### 9. Term and termination

- Term: fixed project period OR ongoing until terminated
- Termination for convenience: either party on [14–30] days' written notice
- Termination for cause: immediate on material breach (including delivery failure, confidentiality breach, or misrepresentation of independent status)
- Consequences of termination: payment for services performed to termination date; return of company property; IP vests in company regardless of termination reason

### 10. Warranties and representations

Contractor warrants:
- Services will be performed professionally and to industry standards
- Contractor has the right to provide the services and is not bound by any conflicting obligations
- Deliverables will not infringe third-party IP rights
- Contractor is properly licensed and insured for the services

### 11. Liability

- Contractor is liable for losses caused by its negligence, breach, or misconduct
- Consider requiring Contractor to maintain professional indemnity (PI) insurance of [USD X] per claim
- Company liability to Contractor: limited to payment for services performed

## Jurisdictional notes — Classification tests

| Jurisdiction | Key classification test | Factors favoring independent status |
|---|---|---|
| **UAE** | UAE Labour Law (Federal Decree-Law 33/2021); economic reality test | Multiple clients; own equipment; controls own working hours; fixed-scope deliverables; corporate entity contractor |
| **KSA** | Saudi Labour Law; Ministry of Human Resources enforcement | Same factors; Saudi nationals as contractors face closer scrutiny |
| **DIFC** | DIFC Employment Law 2019; common-law multifactor test | Economic independence; absence of control; multiple clients; business risk borne by contractor |
| **UK** | IR35 / off-payroll rules; "employment status" tests (control, substitution, MOO) | Personal service company with multiple clients; right to substitute; no mutuality of obligation |
| **EU** | Directive 2022/2041 (Platform Workers Directive); national law varies | Economic independence; entrepreneurial risk; multiple clients; own infrastructure |
| **US (California)** | ABC test under AB5: (a) free from control; (b) performs work outside usual business of company; (c) independently established in the trade | Hardest test; California presumes employment unless all three prongs met |

### MENA-specific enforcement risk

Labour authorities in UAE (MOHRE) and KSA (Ministry of Human Resources) are increasingly scrutinizing disguised employment arrangements. If an individual is found to be misclassified as a contractor:
- Retroactive gratuity liability: back-payment of end-of-service gratuity for all years of service
- Retroactive social insurance: in KSA, GOSI contributions owed; in UAE, any applicable pension contributions
- Annual leave: back-payment of accrued but untaken annual leave
- Reputational and regulatory consequences for the employer

## Common mistakes

- **Calling it a "contractor agreement" doesn't make it one**: Courts and labour authorities look past the label to the substance of the relationship; if the substance is employment, the label is irrelevant.
- **Full exclusivity clause**: Prohibiting the contractor from working for anyone else is the single strongest indicator of an employment relationship.
- **Company provides all equipment**: Providing the contractor with a company laptop, phone, and desk at the company's offices looks like employment; require contractors to use their own equipment.
- **Fixed hours and daily reporting**: Requiring the contractor to work 9am–6pm and attend daily team meetings looks like employment; focus the relationship on deliverables, not time and attendance.
- **No scope definition**: An open-ended agreement with a general description of services ("provide legal advice") is harder to distinguish from employment than a specific project-based deliverable scope.

## Related skills

- [[prompt-pack-employment-offer-letter]]
- [[prompt-pack-executive-employment-agreement]]
- [[prompt-pack-employment-contract-compliance-review]]
- [[prompt-pack-full-contract-risk-review]]

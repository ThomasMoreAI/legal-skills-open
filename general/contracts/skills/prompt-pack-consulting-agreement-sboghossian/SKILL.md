---
name: prompt-pack-consulting-agreement-sboghossian
title: Consulting Agreement
description: Use when a company needs to draft a consulting agreement engaging an individual or corporate consultant to provide services. Covers compensation structure, expense reimbursement, IP ownership, confidentiality, non-compete and non-solicitation, and independent contractor status. Addresses MENA jurisdiction traps around employee-vs-contractor misclassification under UAE, KSA, LB, and EG labor law, and distinguishes DIFC/ADGM common-law treatment from civil-law onshore frameworks.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-consulting-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Consulting Agreement

A consulting agreement governs the relationship between a company and an external consultant or advisory firm. The most critical legal risks are: (1) misclassification of the consultant as an employee, triggering labor law obligations; (2) unclear IP ownership of deliverables; and (3) overly broad non-compete provisions that are unenforceable or expose the company to damages claims.

## When to use this

- Engaging an individual or firm to provide advisory, professional, or technical services on a project or retainer basis.
- The engagement is intended to be independent contractor (not employment), and the parties want to document this clearly.
- The company wants to ensure that all IP created during the engagement belongs to the company.
- A company in a MENA jurisdiction is engaging a consultant who is based in a different jurisdiction — cross-border considerations apply.
- Replacing an informal oral consulting arrangement with a written agreement.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Consultant name and entity type (individual / corporate) | Determines IP and labor law exposure | Ask the user |
| Services description | The more specific, the better for IP ownership and deliverables clarity | Ask the user to describe in detail |
| Compensation structure (daily rate / monthly retainer / project fee) | Drives the payment provisions | Ask the user |
| Jurisdiction of governing law | Determines labor law risk, enforceability of non-compete, and IP ownership rules | Ask the user |
| Non-compete scope (geographic, activity, duration) | Must be reasonable to be enforceable | Ask the user; flag that excessive scope is unenforceable |
| IP ownership preference | Does the company want a work-for-hire / assignment? | Default to company ownership of all deliverables |

## Optional inputs

- Expense reimbursement policy (cap, approval process, receipt requirements).
- Whether the consultant may use subcontractors (and if so, flow-down obligations).
- Exclusivity requirement (is the consultant restricted from working for competitors?).
- Audit rights over the consultant's time records / invoices.
- Whether the agreement is subject to a master agreement (framework with individual statements of work).

## Document structure

### 1. Parties and recitals
- Full legal names of both parties, jurisdiction of incorporation, and registered addresses.
- Brief recital confirming the parties' intention to establish an independent contractor relationship, not an employment relationship.

### 2. Services
- Precise description of the consulting services (or reference to a Schedule / Statement of Work).
- Deliverables, if any, and acceptance criteria.
- Performance standards and timelines.
- Consultant's obligation to provide suitably qualified personnel (if a corporate consultant).
- Right to change scope via a written change order.

### 3. Term and termination
- Start date and end date (or indefinite with rolling renewal).
- Termination for convenience: both parties should retain the right to terminate on reasonable notice (typically 30–90 days depending on engagement value and duration).
- Termination for cause: material breach, insolvency, or criminal conviction; shorter or immediate notice.
- Consequences of termination: payment for work completed to date; return of confidential information; survival of IP assignment, confidentiality, and non-compete.

### 4. Compensation and expenses
- Consulting fee: rate/structure, currency, invoicing frequency.
- Payment terms: typically net 30 from invoice.
- Expense reimbursement: pre-approved expenses only, with receipts; per diem if applicable.
- VAT: state which party bears the VAT obligation. In UAE (5% VAT), KSA (15% VAT), and EG (14% VAT), the consultant's invoice will typically include VAT if the consultant is VAT-registered. Cross-border B2B services may be reverse-charged.
- No benefits: confirm the consultant is not entitled to any employee benefits, end-of-service gratuity, health insurance, annual leave, or pension contributions under the agreement.

### 5. Independent contractor status
This clause is essential in MENA jurisdictions:
- The consultant is an independent contractor, not an employee, agent, or partner of the company.
- The consultant is responsible for their own taxes, licenses, social security, and insurance.
- **MENA warning:** UAE Labor Law (Federal Decree-Law No. 33 of 2021) and KSA Labor Law apply a substance-over-form test for employment. Courts look at: exclusivity, hours of work, direction and control, integration into the company's business, and regularity of payment. A consultant who is effectively integrated into the company's operations as an employee will be treated as one regardless of what the contract says. Include appropriate indicia of independence in the contract and ensure the working arrangement reflects these.
- **Lebanon:** The Court of Cassation applies a similar substance test under the Labor Code; long-term exclusive consulting arrangements are particularly at risk of reclassification.

### 6. Intellectual property
- All work product, deliverables, inventions, code, reports, designs, and materials created by the consultant in connection with the services ("Work Product") are assigned to the company upon creation.
- The consultant warrants that the Work Product is original and does not infringe third-party IP.
- Where outright assignment is not possible under local law (some civil-law systems require moral rights to be addressed separately), grant an exclusive, irrevocable, worldwide, perpetual license in lieu.
- Pre-existing IP ("Background IP") owned by the consultant before the engagement is excluded from the assignment but the consultant grants the company a license to use it to the extent embedded in the Work Product.
- In UAE and GCC civil-law systems, copyright in "works for hire" may not automatically vest in the employer/client under Federal Law No. 38 of 2021 (UAE Copyright Law) — an express written assignment is required.

### 7. Confidentiality
- Broad definition of confidential information: all non-public information received from the company.
- Obligations: use only for the services; maintain security; not disclose to third parties without consent.
- Exceptions: publicly available information, independently developed, required by law (with prior notice to the company).
- Duration: during the term and for 3 years post-termination (or longer for trade secrets).
- Return or destruction of confidential information on termination.

### 8. Non-compete and non-solicitation
- **Non-compete:** Restriction on providing competing services to named competitors or in a defined sector during and for [6–24 months] post-termination. Must be geographically and temporally reasonable to be enforceable.
  - **UAE:** Non-compete clauses are enforceable under the Civil Code (Article 909) if reasonable in scope; UAE Labor Law Article 12 limits non-compete to 2 years and must be justified by legitimate interest. Courts have voided overly broad clauses.
  - **KSA:** Non-compete is enforceable under the Civil Code if reasonable; KSA courts tend to construe restrictive covenants narrowly.
  - **Lebanon:** Enforceable if reasonable and with compensation paid during the restriction period in some interpretations of the Labor Code.
  - **DIFC / ADGM:** Treated as a restraint of trade; the clause must go no further than reasonably necessary to protect a legitimate business interest.
- **Non-solicitation:** Prohibition on soliciting the company's employees and clients for [12–24 months] post-termination. Generally easier to enforce than a non-compete.

### 9. Representations and warranties
- Consultant's warranties: authority to enter the agreement; services will be provided with professional care and skill; no conflict with existing commitments; no claims or proceedings that would affect performance.
- Company's warranties: authority to enter the agreement; payment obligations will be met.

### 10. Liability and indemnification
- Cap on consultant's liability: typically the fees paid in the last 12 months (for corporate consultants).
- Exclusions from cap: fraud, gross negligence, willful misconduct, IP infringement.
- Indemnification: each party indemnifies the other for their own fraud, gross negligence, and wilful breach.
- Insurance: require the consultant to maintain professional indemnity insurance at specified minimum limits.

### 11. General provisions
- Governing law and dispute resolution (arbitration or courts; seat; language).
- Entire agreement and no amendment except in writing.
- No waiver; severability; counterparts.

## Jurisdictional notes

| Jurisdiction | Key risk |
|---|---|
| UAE (onshore) | End-of-service gratuity and labor protections apply if consultant is reclassified as employee; Arabic contract may be required for court proceedings |
| UAE (DIFC/ADGM) | Employment Law / Work and Employment Regulations apply if relationship is employment; IP assignment requires express written clause |
| KSA | Saudization (Nitaqat) risk if consultant is used as a substitute for a permanent hire; non-compete must be limited |
| Lebanon | Long-term exclusive engagement risks labor reclassification; indemnité de licenciement applies to employees |
| Egypt | Social insurance exposure on reclassification; IP assignment must be in writing to be effective against third parties |

## Common mistakes

- Describing the services vaguely — "general advisory" or "strategic support" without specifying deliverables leads to fee disputes and IP ownership ambiguity.
- Forgetting the IP assignment clause — deliverables belong to the consultant unless expressly assigned.
- Non-compete scope so broad (global, all industry, 5 years) that it is void and unenforceable, leaving the company with no protection.
- Omitting the independent contractor clause and indicia — the contract then looks indistinguishable from an employment contract.
- Not addressing VAT, leaving disputes about whether the fee is inclusive or exclusive.

## Related skills

- [[prompt-pack-employment-contract]]
- [[prompt-pack-nda-mutual]]
- [[prompt-pack-service-agreement]]
- [[prompt-pack-ip-assignment-agreement]]
- [[prompt-pack-contract-negotiation-preparation]]

---
name: prompt-pack-service-agreement-sboghossian
title: Service Agreement
description: Use when drafting a bilateral services agreement between a service provider and client, covering scope of work, deliverables, payment terms, term, termination, limitation of liability, and governing law. Applicable across MENA and international practice; MENA-specific flags cover UAE, DIFC, KSA, Lebanon, and Egypt contract formation requirements, civil-law enforceability of limitation of liability clauses, and Arabic-language obligations.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-service-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Service Agreement

## When to use this

Use this skill when:
- A company or individual is engaging a service provider to perform defined professional or technical services.
- A consulting firm needs a master services agreement (MSA) for use with multiple clients, with work specifics addressed in separate Statements of Work (SoW).
- A technology company is engaging contractors for development work.
- A law firm is formalizing an engagement with a corporate client beyond the standard engagement letter.
- A government entity in MENA is procuring services from a private provider under a standard services contract.

**Distinguish from:** Software license or SaaS agreements (use [[prompt-pack-saas-terms-of-service]]); supply/goods agreements (use [[prompt-pack-supply-agreement]]); employment contracts (a services agreement with an individual who meets the economic reality test for employment may be re-characterized as an employment contract with serious regulatory consequences).

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Service provider details** | Name, entity type, jurisdiction | Ask |
| **Client details** | Name, entity type, jurisdiction | Ask |
| **Description of services** | The most important input — must be specific enough to be enforceable | Ask; use a Statement of Work if complex |
| **Deliverables** | Tangible outputs: reports, software, designs, etc. | List them; if none, describe milestones |
| **Payment amount and schedule** | Fixed fee / time-and-materials / retainer | Ask; include currency |
| **Term and start date** | When services begin and end | Ask |
| **Jurisdiction / governing law** | Determines key legal defaults (damages, termination, IP) | Ask; default UAE onshore if MENA context |

## Optional inputs

- **MSA + SoW structure** — if this is a master agreement, the main document covers standard terms; individual SoWs specify project details.
- **IP assignment vs. license** — whether IP created in the services is assigned to the client or licensed.
- **Non-solicitation** — restrictions on each party's recruitment of the other's employees.
- **Background IP** — service provider's pre-existing tools, methodologies, and code that will be used in service delivery.
- **Subcontracting rights** — whether the provider may subcontract work.

## Document structure

1. **Definitions** — Services, Deliverables, Intellectual Property, Confidential Information, Force Majeure, Background IP, Foreground IP, Statement of Work.

2. **Engagement and scope**
   - Service provider is engaged to perform the Services as described in this Agreement and/or each Statement of Work.
   - Services should be described with enough specificity to define the provider's obligation and enable the client to judge completion.
   - For MSA structure: this Agreement governs all SoWs; in case of conflict, the SoW prevails.

3. **Deliverables and milestones**
   - List of deliverables (or reference Schedule).
   - Acceptance procedure: client has [X] business days to review and accept or reject (with specific, written reasons) each deliverable.
   - Deemed acceptance: if no response within the review period, deliverable is deemed accepted.
   - Revision cycles: number of revisions included in the fee.

4. **Service standards and personnel**
   - Provider will perform services with reasonable skill, care, and diligence.
   - Services performed by qualified, experienced personnel.
   - Key personnel: if specific individuals are critical, name them; right to approve replacements.
   - Provider may not subcontract without client's prior written consent (or: may subcontract to approved subcontractors listed in Schedule).

5. **Payment terms**
   - Fee structure: fixed fee / hourly / daily / milestone / monthly retainer.
   - Payment schedule: invoice on [completion of milestone / end of month / specified dates].
   - Payment terms: [30/45/60] days from invoice.
   - Late payment: interest at [rate]% per annum from due date (check applicable statutory rate and whether it is lawful to charge interest in the jurisdiction — KSA has restrictions on conventional interest).
   - Expense reimbursement: pre-approved expenses only, with receipts, reimbursed within [30] days.
   - Disputed invoices: client must notify provider in writing within [10] days of invoice; pay undisputed portion; dispute resolved per dispute resolution clause.

6. **Intellectual property**
   - **Background IP:** each party retains ownership of its Background IP. Provider grants client a non-exclusive license to use Background IP embedded in Deliverables, solely for the purpose of using the Deliverables.
   - **Foreground IP (work product):** two options:
     - *Assignment model* (common in bespoke development): on payment, all IP in Deliverables is assigned to client. Provider retains rights in Background IP and generic methodologies.
     - *License model* (common in consulting/advisory): provider retains IP ownership; grants client a non-exclusive, perpetual license to use Deliverables.
   - For MENA civil-law jurisdictions: IP assignments must be in writing and may need to specify the rights transferred with particularity; a generic "assign all IP" may not transfer specific statutory rights (e.g., moral rights in Lebanon, UAE copyright law).
   - **Open-source software:** provider must disclose any open-source components in Deliverables and ensure their license terms are compatible with the intended use.

7. **Confidentiality**
   - Mutual confidentiality obligations.
   - Exclusions: public domain, already known, independently developed, disclosed by law.
   - Duration: term of agreement plus [2/3/5] years.
   - Return/destruction of confidential information on termination.

8. **Representations and warranties**
   - Provider: (a) has authority to enter and perform; (b) services will conform to the agreed specification; (c) Deliverables will not infringe third-party IP rights; (d) will comply with applicable laws.
   - Client: (a) has authority to enter; (b) any materials supplied to provider do not infringe third-party IP rights.
   - Disclaimer: except for express warranties, services are provided without warranty of merchantability, fitness for a particular purpose (in B2B contracts; these are generally freely disclaimed in MENA and common-law jurisdictions for commercial contracts).

9. **Limitation of liability**
   - Mutual exclusion of indirect, consequential, and special damages.
   - Cap on direct liability: typically the fees paid in the preceding [3/6/12] months.
   - **MENA note — UAE onshore:** UAE Civil Transactions Law (Federal Law No. 5 of 1985) governs contracts; Art. 296 limits parties' ability to exclude liability for fraud (ghish) and gross negligence (khata' jaddi). Limitation of liability clauses limiting liability for ordinary negligence are generally enforceable in commercial contracts but excluded for gross misconduct. Do not replicate a blanket "no liability" clause; scope the exclusion appropriately.
   - **DIFC / ADGM:** Common-law enforceability; UCTA-equivalent tests apply; unreasonable exclusion clauses may be struck down.
   - Carve-outs from the cap: death/personal injury, fraud, deliberate breach, IP infringement indemnity (these are standard carve-outs that survive the cap).

10. **Term and termination**
    - Commencement and duration.
    - Renewal: automatic or by agreement.
    - Termination for cause: material breach with [30-day] cure notice; insolvency.
    - Termination for convenience: [30/60] days' written notice; client pays for services rendered to termination date plus reasonable demobilization costs.
    - Consequences: return of materials, cessation of services, IP transfer on payment, survival of confidentiality and limitation of liability.

11. **Force majeure**
    - Events: government action, war, pandemic, natural disaster, utility failure.
    - Obligation: notify within [5] business days; mitigate; if Force Majeure continues beyond [60/90] days, either party may terminate.
    - No exclusion of payment obligations that have already accrued.

12. **Dispute resolution and governing law**
    - State governing law (e.g., UAE law / English law / DIFC law).
    - Dispute resolution: negotiation escalation (senior management) → arbitration (preferred for international parties) or litigation.

13. **General clauses** — entire agreement, amendments (written only), no waiver, severability, notices, assignment (no assignment without consent), independent contractor relationship (not employment), no third-party beneficiaries.

## Jurisdictional notes

### UAE — onshore
- UAE Civil Transactions Law Art. 877+: contract for services (Muqawala) — service provider must complete the work and deliver it; employer pays the agreed price on delivery.
- If the service involves construction or engineering, specific muqawala rules (including 10-year latent defect liability for structural defects) apply mandatorily.
- Arabic: for government contracts and enforcement in UAE courts, Arabic versions are required or strongly advisable.
- Agency / employment distinction: if the service provider is an individual providing exclusive services, UAE labor authorities may reclassify as an employment relationship; use corporate contracting structures where possible.

### DIFC / ADGM
- Common-law contract principles; DIFC Contract Law (DIFC Law No. 6 of 2004 as amended) closely follows UNIDROIT Principles.
- Consequential loss exclusion: enforceable in B2B contracts; subject to reasonableness test.
- No muqawala concept; services are governed by general contract law.

### KSA
- Service contracts governed by general Sharia principles and the Saudi system of contract; specific muqawala rules.
- Conventional interest on late payments is not enforceable; use a "delay compensation" (ta'khir) concept or a commercial rate agreed as liquidated damages.
- Arabic language documents prevail in Saudi courts.

### Lebanon
- Lebanese Code of Obligations and Contracts (1932): general contract law framework.
- Service contracts (louage d'ouvrage) — contractor's liability for defective work; 10-year liability for structural defects in construction.
- French civil-law influence: force majeure doctrine applied broadly.

## Drafting standards

- Attach the scope of services as a Schedule or Statement of Work rather than embedding it in the body — makes it easier to update without amending the main agreement.
- Use "best endeavours" (UK/MENA standard) rather than "best efforts" (US) for discretionary obligations; or better still, define the obligation precisely and use "shall."
- Specify acceptance criteria for deliverables; "satisfactory to client" is not enforceable — define what "satisfactory" means (conformity with specification, passing test criteria).
- Do not leave IP ownership as a generic provision — the client's lawyers will always negotiate hard on this; prepare both assignment and license alternatives.

## Common mistakes

- **Open-ended scope.** "Provider shall perform such services as client may require" creates unlimited obligation; scope must be bounded.
- **No deemed acceptance mechanism.** Without a deemed acceptance clause, a client can hold deliverables in perpetual review, delaying payment indefinitely.
- **Limitation of liability lower than the fees payable.** A fee-based cap that results in a sub-USD 10,000 limit on a multi-million-dollar project is commercially unrealistic and may be considered an unfair contract term.
- **Employee vs. contractor misclassification.** Using a services agreement for an individual who works exclusively for one client, under that client's direction, is high-risk in UAE, KSA, and most MENA jurisdictions; the individual may be reclassified as an employee with back-payment obligations for EoSG, social insurance, and annual leave.

## Related skills

- [[prompt-pack-saas-terms-of-service]]
- [[prompt-pack-supply-agreement]]
- [[prompt-pack-reseller-agreement]]
- [[prompt-pack-standard-nda]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]

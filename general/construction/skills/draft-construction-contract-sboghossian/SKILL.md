---
name: draft-construction-contract-sboghossian
title: Draft — Construction Contract (Non-FIDIC)
description: Use when asked to draft a construction contract for small to medium projects where the full FIDIC suite is disproportionate. Covers scope of works, bill of quantities, payment and milestone schedule, programme, extensions of time, liquidated damages for delay (with Sharia-compliant framing for KSA), performance bond, retention, variations, insurance (CAR, TPL, workers' comp), defects liability, and dispute resolution. Applicable across MENA and multi-jurisdictional construction projects.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-construction-contract
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: construction
language: en
---

# Draft — Construction Contract (Non-FIDIC)

## When to use this

Use this skill for construction and fit-out projects where:
- The project value or complexity does not justify the full FIDIC suite (Yellow Book / Red Book).
- The parties want a simpler, direct bilateral contract rather than the elaborate FIDIC engineer/employer/contractor triangle.
- The project is primarily a single trade: fit-out, MEP installation, civil works, or specialty construction.

For large, complex, or international infrastructure projects, consider whether a FIDIC form is more appropriate. This skill produces a bespoke bilateral contract.

## Required inputs

| Input | Notes |
|---|---|
| Employer (owner) and Contractor | Full legal names, registration details, signatory authority |
| Project description | Site address, nature of works |
| Scope of works | Reference to Schedule A (specification); do not rely on verbal description |
| Contract sum | Fixed price / lump sum or remeasurement; currency |
| Programme | Commencement date; completion date; milestones |
| Jurisdiction | Determines LD enforceability, insurance requirements, dispute forum |
| Governing law | May differ from the site jurisdiction (especially for international projects) |

## Document structure

### 1. Parties and project
- Employer, Contractor, project description, site address.
- Reference to the Contract Documents hierarchy: this Agreement > Specifications > Drawings > Bill of Quantities > Programme.

### 2. Scope of works — Schedule A
The most important schedule. Should include:
- Technical specification (or reference to design drawings by revision number and date).
- Bill of quantities (if remeasurement contract) or Schedule of Rates (if lump sum with variations).
- Employer's specific requirements (materials, finishes, performance standards).
- List of employer-supplied items (if any).

**Critical**: ambiguity in scope is the primary source of construction disputes. The scope must specify what is included and what is excluded.

### 3. Contract sum and payment

**Lump sum contract**:
> "The Employer shall pay to the Contractor the sum of [CURRENCY AMOUNT] (the "Contract Sum") in accordance with the Payment Schedule set out in Schedule B."

**Remeasurement contract** (less certain; not recommended for small projects):
> "The Contractor shall be paid based on the quantities of work actually completed, measured against the Schedule of Rates, subject to a target maximum of [AMOUNT]."

**Schedule B — Payment schedule / milestones**:
A typical milestone structure:
| Milestone | % of Contract Sum | Trigger |
|---|---|---|
| Mobilization | 10% | Site handover to Contractor |
| 30% completion | 20% | Certified by Employer's representative |
| 60% completion | 25% | Certified |
| Practical completion | 30% | Completion certificate issued |
| Defects liability period end | 15% (less retention) | Defects certificate issued |

**Retention**: typically 5–10% of each progress payment; released in two tranches: 50% at practical completion, 50% at end of defects liability period.

**Variations**: additions or deductions to scope; must be instructed in writing by Employer; Contractor submits pricing within 7 days; agreed before work commences if possible.

### 4. Programme

- Contractor to submit a programme within [14] days of execution.
- Minimum content: commencement date; completion date; key milestones; critical path activities.
- Programme is a tool for monitoring progress, not a guarantee of the critical path.

### 5. Extensions of time (EoT)

Contractor is entitled to an EoT (extension of the contract time for completion without liquidated damages) for:
- Employer-caused delays (late site access, late design information, late employer-supplied materials, variations instructed by Employer).
- Force majeure events (see [[draft-boilerplate-clauses]]).
- Delays caused by neutral events (weather beyond statistical norms — specify the benchmark).

**Not** entitled to EoT for:
- Contractor's own resource shortfalls.
- Subcontractor failures.
- Underestimation of scope.

**EoT procedure**:
- Contractor must give notice within [14–28] days of becoming aware of the delaying event.
- Failure to give timely notice may bar the EoT claim (strict notice requirement).
- Employer's representative assesses and certifies the EoT.

### 6. Liquidated damages (LD) for delay

LDs are pre-agreed compensation for delay in achieving practical completion.

**Standard clause**:
> "If the Contractor fails to achieve Practical Completion by the Completion Date (as extended by any awarded Extension of Time), the Contractor shall pay to the Employer liquidated and ascertained damages at the rate of [CURRENCY AMOUNT] per calendar day of delay."

**LD rate**: typically set at the Employer's genuine pre-estimate of loss from delay (rental cost, lost revenue, additional financing cost). A rate set too high may be challenged as a penalty.

**Cap**: most contracts cap aggregate LDs at 10–15% of the Contract Sum.

**KSA — Sharia note on LDs**: Sharia courts may treat a LD clause as a penalty (شرط جزائي عقوبي) if the rate appears punitive rather than compensatory. Draft as "pre-agreed compensation for actual damages" (تعويض اتفاقي مقدر مسبقاً) and reference the Employer's genuine pre-estimated loss in the recitals. A court may reduce the LD if it exceeds actual damage, but the clause is generally enforceable if framed correctly.

### 7. Performance security

**Performance bond / guarantee**:
- Bank guarantee or performance bond issued by a licensed bank or surety.
- Amount: 10% of Contract Sum (standard); 15–20% for high-risk or high-value projects.
- Form: on-demand (payable on first written demand without proof of default) or conditional (payable on proof of default). On-demand is stronger for Employer; conditional is more contractor-friendly.
- Duration: from commencement to end of defects liability period.

**Advance payment guarantee** (if advance payment made):
- If Employer advances mobilization funds, a matching bank guarantee ensures repayment if Contractor defaults.

**Retention substitute**: some contractors prefer a retention bond in lieu of cash retention; assess the creditworthiness of the bond provider.

### 8. Insurance

Contractor's mandatory insurance:
- **Contractor's All Risk (CAR)** insurance: covers damage to the works and materials on site during construction.
- **Third-Party Liability (TPL)** insurance: covers injury to persons and property damage caused to third parties at or near the site. Minimum limit: [CURRENCY AMOUNT] per occurrence.
- **Workers' Compensation** / employer's liability insurance: covers Contractor's workforce injuries. In MENA: compliant with jurisdiction-specific labor law requirements.
- **Professional Indemnity** (for design-and-build elements): errors in design.

Insurance policies must:
- Name the Employer as additional insured.
- Not be cancellable without 30 days' notice to Employer.
- Contractor to provide certificates of insurance before commencement.

### 9. Health, safety, and environment (HSE)

- Contractor's obligation to comply with all applicable HSE laws (UAE Federal Law on Occupational Safety; KSA Labour Law; site-specific HSE plan).
- HSE plan to be submitted before commencement.
- Incidents: mandatory reporting to Employer and relevant authority within 24 hours.
- Employer may suspend works for material safety violations; cost of suspension: Contractor's account.

### 10. Subcontracting

- Contractor may subcontract elements of the works subject to Employer's prior written consent for subcontractors accounting for more than [10–20]% of the Contract Sum.
- Contractor remains fully responsible for all subcontracted works.
- Nominated subcontractors (if any): Employer may nominate; Contractor has limited right to object on reasonable grounds.

### 11. Practical completion and handover

- Contractor to give [7–14] days' notice when the works are substantially complete.
- Employer's representative inspects and issues either a Practical Completion Certificate or a list of defects / snag list.
- Snag items: must be completed within [30] days of Practical Completion.
- Risk and responsibility for the works transfers to Employer at Practical Completion.

### 12. Defects liability period

- Standard period: 12 months from Practical Completion (some contracts use 24 months for structural elements).
- Contractor obligated to return to site to remedy any defects notified by Employer during the DLP at Contractor's cost.
- Defects Certificate issued at end of DLP: triggers release of final retention.

### 13. Termination

**For cause by Employer**:
- Contractor abandons the works.
- Contractor fails to remedy a material default within [14–28] days of written notice.
- Insolvency of Contractor.
- Consequence: Employer takes over the works; may engage another contractor; Contractor forfeits performance bond and is liable for additional cost to complete.

**For convenience by Employer**:
- Employer may terminate at any time.
- Consequence: Contractor entitled to payment for work done + reasonable demobilization costs + loss of profit on remaining works (often capped at [X]% of the remaining Contract Sum).

**For cause by Contractor**:
- Employer fails to make payment after [28] days of written notice.
- Employer obstructs the works for [60+] days.
- Consequence: Contractor entitled to demobilize and claim all sums due plus reasonable loss.

### 14. Dispute resolution

For MENA construction:
- **Expert determination**: for technical disputes (measurement, quality) — quick and cost-effective.
- **Dispute Adjudication Board (DAB)**: used in FIDIC; applicable by agreement in non-FIDIC contracts for ongoing projects.
- **Arbitration**: final-binding; for MENA disputes: DIAC (Dubai seat) or SCCA (KSA seat) recommended; see [[draft-boilerplate-clauses]].
- **Courts**: DIFC or ADGM Courts for free-zone projects.

### 15. Governing law
- For UAE projects: UAE Federal Law (Civil Transactions Law) is the default; DIFC Law for DIFC projects.
- For KSA projects: KSA law; Sharia principles apply.
- For cross-border: agree governing law and ensure it is consistent with the dispute resolution forum.

## Common mistakes

- **Scope ambiguity**: "complete the works as described in the design" without attaching the design creates a dangerous gap.
- **LD rate not matching genuine loss**: an LD rate that dramatically exceeds the Employer's actual loss will be challenged; document the pre-estimate in the recitals.
- **No notice requirement for EoT**: without a strict notice clause, contractors can raise delay claims late in the project or post-completion.
- **Payment certificate mechanism missing**: if there is no defined certification process, disputes about when payment is "due" become common.
- **Insurance requirements left vague**: specifying only "adequate insurance" is unenforceable; specify minimum limits and required cover types.
- **KSA interest without Sharia-compliant framing**: a LD clause with standard "interest" language may be unenforceable; reframe as pre-estimated compensation.

## Related skills

- [[draft-commercial-lease]]
- [[draft-boilerplate-clauses]]
- [[draft-bilingual-ar-en-side-by-side]]

---
name: draft-severance-agreement-sboghossian
title: Severance Agreement
description: Use when drafting a severance, separation, or mutual-exit agreement for an employee whose employment is ending. Covers statutory end-of-service entitlements (EOSG/EOSA), ex gratia payments, restrictive covenants, release of claims, and visa-cancellation coordination across UAE (federal and DIFC), KSA, Lebanon, and other MENA jurisdictions. Flags non-waivable statutory floors and the consultation requirements for mass redundancies.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-severance-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Severance Agreement

A severance agreement (also called a separation agreement or mutual-exit agreement) documents the financial and legal terms of an employee's departure. It typically combines payment of statutory entitlements, an ex gratia top-up, and a release of claims. In MENA jurisdictions, the agreement must sit above the statutory floor — it cannot reduce what the employee is entitled to by law.

## When to use this

- Individual voluntary separation, mutually agreed departure, or without-cause dismissal
- Redundancy or restructuring (single employee or mass event)
- Settlement of employment dispute as part of exit
- Senior executive exits requiring complex benefit calculations and restrictive covenants
- Any exit where the employer wants a release of claims from the departing employee

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Employer + Employee (full legal names, IDs) | Parties to the agreement | Must provide |
| Effective termination date | Triggers last-day calculations for accruals | Must provide |
| Reason for separation | Affects framing, statutory entitlement (resignation can lose EOSG in some jurisdictions if <5 years), and tax treatment | Must provide |
| Governing law / jurisdiction | Determines statutory entitlements and mandatory provisions | Must provide |
| Severance amount and breakdown | Itemize: last salary owed, accrued untaken leave, EOSG/EOSA, ex gratia, any bonus proration | Must provide |
| Notice or pay in lieu | Whether notice is being served or bought out | Pay in lieu if immediate departure required |

## Optional inputs

- Restrictive covenants (non-compete, non-solicit, non-hire)
- Reference letter terms
- Cooperation clause (transition assistance)
- Confidentiality of the agreement and its terms
- Non-disparagement (mutual is the standard)

## Statutory Components by Jurisdiction

The following entitlements are mandatory floors — any waiver purporting to reduce them is void:

### UAE Federal (Decree-Law 33/2021)
- **End-of-service gratuity (EOSG)**: 21 days' basic salary per year for the first five years, then 30 days' basic salary per year thereafter; calculated on basic salary only (not total package); prorated for partial years
- **Accrued leave**: untaken annual leave paid out at basic salary
- **Notice or pay in lieu**: minimum per contract or law (Article 43)
- **Visa cancellation**: coordinate sponsor cancellation within 30 days of termination; delays expose employer to Ministry of Human Resources (MoHRE) fines

### DIFC (DIFC Employment Law + DEWS)
- **End-of-service benefit under DEWS**: employer contributions to the DIFC Employee Workplace Savings scheme at 5.83% of monthly wage per year of service (effective February 2020 for new joiners; transitional provisions for those who opted into DEWS); accrued DEWS balance belongs to employee
- **Notice**: statutory minimum per Article 35 (30 days for employees with <3 years of service; 60 days for ≥3 years; parties may agree longer)
- **Accrued leave**: paid at wage rate

### KSA (Labor Law + Ministerial Decisions)
- **End-of-service award (EOSA)**: half a month's salary per year of service for the first five years; full month's salary per year of service thereafter; calculated on last wage
- **Resignation reduction**: employee who voluntarily resigns with 5-10 years of service is entitled to one-third of EOSA; 10+ years, two-thirds; full EOSA if employer terminates without cause
- **Notice**: one month minimum under Article 75
- **Iqama (residency permit) cancellation**: coordinate with Saudi immigration; employee must exit within 30 days of visa cancellation unless new sponsor found

### Lebanon (Labor Code)
- **End-of-service indemnity (Article 50)**: one month's salary per year of service for the first six years, 1.5 months per year thereafter
- **Notice**: Article 50 sliding scale by seniority (typically 1–3 months depending on years of service); employer may pay in lieu
- **Protective indemnity for arbitrary dismissal** (Article 74): additional indemnity if dismissal not based on valid grounds — calculated by court; exposure from 2 to 12 months depending on circumstances

### France
- **Indemnité de licenciement** (statutory or conventional): minimum per Barème Macron; applies to termination without cause
- **Préavis**: notice tied to seniority and collective agreement
- **Non-compete**: post-employment non-compete requires a specific monthly indemnity (typically 30% of average gross monthly salary for duration of restriction) without which the clause is void

## Document Structure

1. **Parties and effective date** — identify employer (with registered address), employee (with ID/passport number), and the effective date of termination
2. **Reason for separation** — state clearly: mutual agreement / redundancy / dismissal without cause / resignation accepted / expiry of fixed-term contract; avoid "for cause" characterization unless documented misconduct proceedings have concluded
3. **Settlement payment schedule** — itemized table:
   | Item | Amount | Currency | Payment date |
   |---|---|---|---|
   | Salary owed (to effective date) | | | |
   | Accrued untaken leave | | | |
   | EOSG / EOSA (statutory) | | | |
   | Notice pay / pay in lieu | | | |
   | Ex gratia payment | | | |
   | Bonus proration (if agreed) | | | |
   | **Total** | | | |
4. **Restrictive covenants** (if applicable):
   - Non-compete: define geographic scope, duration, and activities; must be reasonable to be enforceable; in DIFC, FR, and UK requires separate financial consideration
   - Non-solicitation of clients: limited to clients with whom the employee had material contact
   - Non-hire of colleagues: typically 12 months
5. **Confidentiality and non-disparagement** — mutual; employer does not disparage employee (prevents poor references), employee does not disparage employer (prevents reputational damage)
6. **Return of property** — specific list or general obligation; IT equipment, access cards, confidential documents; deadline (typically last day of employment)
7. **IP confirmation** — all IP created during employment belongs to employer; assignment confirmation for any IP created in grey areas (outside hours, personal equipment)
8. **Reference letter terms** — factual reference confirming title and dates; or agreed text attached as Schedule 1
9. **Release of claims** — employee releases all claims arising from employment and its termination; carve-outs for: vested pension / DEWS benefits, indemnification rights as a director/officer, personal injury claims not yet manifested, future claims arising after execution date
10. **Acknowledgment of independent legal advice** — employee acknowledges opportunity to seek counsel before signing; this strengthens the release's enforceability
11. **Cooperation clause** — employee cooperates in transition and any future litigation involving pre-termination matters; reasonable time limit (12–18 months); employer reimburses reasonable costs
12. **Tax treatment** — employer does not gross up for taxes unless expressly agreed; employee responsible for their own tax on received amounts
13. **Confidentiality of agreement** — terms and existence of this agreement are confidential; permitted disclosures to legal and tax advisors
14. **Governing law and dispute resolution**
15. **Entire agreement** — supersedes all prior agreements relating to the subject matter

## Critical Points

### Non-waivable floors

In every MENA jurisdiction, statutory end-of-service entitlements are a mandatory minimum. A release or waiver clause that purports to waive amounts below the statutory floor is void. The ex gratia element (any amount above the statutory floor) is waivable in exchange for the release of claims.

### Mass redundancies trigger additional obligations

In Lebanon, France, UAE, and KSA, collective redundancies (typically defined by headcount thresholds) trigger additional consultation requirements, notification to the relevant labor authority, and in some cases joint committees. Do not use this skill alone for mass redundancy programs — specialist employment counsel is required.

### Non-competes: jurisdiction-specific enforceability

| Jurisdiction | Enforceability | Compensation required? |
|---|---|---|
| UAE federal | Enforceable up to 2 years with reasonable geographic and activity scope | No separate compensation required |
| DIFC | Enforceable; must be reasonable; courts apply a reasonableness test | No separate compensation required |
| KSA | Enforceable with reasonable scope | No separate compensation required |
| LB | Enforceable with reasonable scope | Not required by statute |
| France | Only enforceable if the employer pays a monthly non-compete indemnity (typically ≥30% of average gross monthly salary) during the restriction period | Yes — clause is void without it |
| UK | Enforceable if reasonable in scope; consideration required for post-employment restrictions if they were not in the original contract | Consideration required for post-employment additions |

### Visa cancellation (MENA)

For non-citizen employees in UAE and KSA, the employer is the visa sponsor. Failure to cancel the residency permit timely exposes the employer to fines and blocks future hiring. The severance agreement should include a mutual obligation to cooperate with the cancellation process and a timeline.

## Related skills

- [[draft-termination-letter]]
- [[draft-warning-letter]]
- [[draft-employment-contract]]
- [[draft-settlement-agreement]]
- [[kb-employment-law-mena]]

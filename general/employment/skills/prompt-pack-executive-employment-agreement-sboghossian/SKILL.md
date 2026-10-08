---
name: prompt-pack-executive-employment-agreement-sboghossian
title: Executive Employment Agreement
description: Use when drafting an executive employment agreement for a C-suite or senior executive position. Covers base salary, bonus structure, equity compensation, benefits, change-of-control provisions, termination scenarios (for cause, without cause, good reason), severance, post-employment restrictions, and D&O coverage. Applicable across MENA (UAE, KSA, DIFC, ADGM, LB, EG) and internationally. Trigger when a company is engaging a CEO, CFO, General Counsel, or other senior executive and needs a comprehensive employment agreement that balances executive interests with company protections.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-executive-employment-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Executive Employment Agreement

## When to use this

Use this skill when drafting the formal employment agreement for a C-suite executive or senior leader. Executive agreements are more complex than standard employment contracts because they involve: equity compensation, performance-based remuneration, carefully defined termination scenarios with significant financial consequences, post-employment restrictions, and often a change-of-control component.

Typical triggers:
- Hiring a new CEO, CFO, COO, or General Counsel
- Renewing or renegotiating an existing executive agreement
- PE or VC-backed company formalizing founder employment terms at Series A or above
- Pre-IPO executive team alignment and contractual documentation
- Board compensation committee instructing legal counsel to document approved executive terms

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Executive name and role | Identity and scope of authority | Ask |
| Company name and jurisdiction | Applicable law; governs term and termination rules | Ask |
| Compensation: base salary, bonus target | The primary commercial terms | Ask |
| Equity grant (options, RSUs, phantom) | Often a significant part of executive comp; must be documented | Ask |
| Duration (fixed-term vs. indefinite) | Executive agreements may be fixed-term in MENA; affects termination obligations | Ask |
| Termination scenarios and severance | What the executive receives on different departure scenarios | Ask in detail |

## Optional inputs

- Relocation provisions (common for international executive hires in MENA)
- Change-of-control provisions (golden parachute trigger and amount)
- Garden leave provisions
- Post-termination non-compete / non-solicitation
- D&O insurance coverage
- Housing and schooling allowances (standard in UAE/KSA expat executive packages)
- Discretionary authority limits (signing authority, hiring authority, capex thresholds)

## Document structure

### 1. Parties and recitals

- Company name, jurisdiction, registered address
- Executive name, role title
- Effective date of agreement

### 2. Role and responsibilities

- Title and department
- Reporting structure (board, CEO, or other)
- Duties: general description and scope of authority
- Exclusivity: executive's full time and attention; no outside board positions or consulting without prior consent
- Fiduciary duties: reference to directors' duties under applicable company law if the executive is also a board member

### 3. Term

**Indefinite-term approach** (preferred in most common-law jurisdictions and DIFC):
- Employment continues until terminated by either party on notice
- "At-will" employment: NOT applicable in MENA or DIFC; there must be notice or payment in lieu

**Fixed-term approach** (common in MENA mainland, KSA):
- Agreement runs for an initial term of [2–3] years
- Automatically extends for 1-year periods unless terminated on [90 days'] notice before the end of the then-current term
- In UAE: fixed-term contracts under Federal Decree-Law No. 33 of 2021 cannot exceed 3 years in the initial term; renewal is permitted

### 4. Compensation

**Base salary**:
- Annual base salary in [currency]; paid [monthly / bi-weekly]
- Review: salary reviewed annually by the compensation committee; no entitlement to increase

**Annual bonus**:
- Target bonus: [X%] of base salary
- Performance conditions: [financial metrics / individual KPIs / board discretion]
- Payment timing: following board approval of annual results; typically within [90] days of financial year end
- Pro-rating on termination: specify whether the executive receives a pro-rated bonus for partial year of service
- Clearly state: "Bonus is discretionary unless performance conditions are met as determined by the board" — or, if contractual: state the specific trigger conditions

**Equity compensation**:
- Grant: [X] options / RSUs / phantom units at a price of [X] on [grant date]
- Vesting: [4-year] vesting; [1-year] cliff; monthly vesting thereafter
- Full reference to the company's equity incentive plan; this agreement provides the executive's individual grant terms
- Change of control: accelerated vesting on [single trigger / double trigger] (see Section on Change of Control)

**Benefits**:
- Health insurance: [gold-tier family coverage / BUPA / equivalent]
- Housing allowance: AED/SAR [X] per month (or company-provided housing)
- Transportation: car or allowance; driver (if applicable)
- Schooling allowance: up to [X] per child per year for [X] children
- Air tickets: [2] economy class / [1] business class round trips per year
- D&O insurance: company will maintain D&O coverage for the executive during employment and for [3–6] years post-departure (tail coverage)

### 5. Leave entitlements

- Annual leave: [30] calendar days (UAE statutory minimum; increase for senior executives common)
- Public holidays: per UAE/KSA statutory calendar
- Sick leave: per applicable UAE/KSA Labour Law provisions
- Emergency and bereavement leave: company policy
- Unpaid leave: by written agreement only

### 6. Confidentiality

- Broad obligation covering all confidential information (business plans, financial data, customer data, trade secrets, IP)
- Post-termination duration: indefinite for trade secrets; [3 years] for business confidential information
- Exceptions: public domain information, legally required disclosure, prior written authorization
- Obligation to return all company property (physical and digital) on departure

### 7. Intellectual property

- All IP created by the executive in connection with employment belongs to the company
- Executive assigns all rights (including moral rights waiver where applicable)
- Pre-existing IP carve-out: schedule pre-existing IP if executive has relevant pre-existing inventions

### 8. Termination scenarios

This section has the most financial consequence and must be precisely drafted:

**Termination for cause**:
- Definition of "cause": material breach of the agreement; gross misconduct; dishonesty; conviction of a criminal offense; serious negligence; willful neglect of duties
- On termination for cause: [30 days'] notice (or statutory minimum); no severance; accrued and vested equity retained (some plans allow forfeiture on "cause")
- In UAE/KSA: termination for cause must fall within the statutory grounds in the Labour Law; overly broad "cause" definitions are not effective against those statutory limits

**Termination without cause**:
- On termination without cause by the company:
  - [3–6] months' base salary in lieu of notice
  - Pro-rated bonus for current year
  - [X] months' additional severance equal to [X months' base salary]
  - Continued vesting of equity for the severance period OR accelerated vesting of [X%] of unvested equity
  - Continuation of benefits for the severance period

**Resignation for good reason**:
- Define "good reason": material reduction in title, responsibilities, or compensation; relocation to a different city without consent; change of control
- On resignation for good reason: executive receives the same as termination without cause above

**Resignation without good reason**:
- Executive gives [90 days'] notice
- No severance; vested equity retained; unvested forfeited
- Garden leave: company may place executive on garden leave during notice period

**Expiration of fixed term** (for MENA fixed-term agreements):
- If company elects not to renew: treated as termination without cause
- If executive elects not to renew: treated as resignation; no severance
- Statutory end-of-service gratuity: payable in all cases on expiry

### 9. Change of control

- Definition: change of control means sale of [50%+] of company shares; merger; IPO (sometimes); sale of substantially all assets
- Accelerated vesting: on a change of control, [50–100%] of unvested equity accelerates (single trigger) — or: vesting accelerates only if executive is also terminated without cause or resigns for good reason within [12] months post-change of control (double trigger)
- Enhanced severance: if executive is terminated or leaves for good reason within [12] months following a change of control, severance equals [2x] annual base salary + target bonus

### 10. Post-employment restrictions

**Non-compete**:
- Duration: [12–24] months post-termination
- Geographic scope: limited to [specific markets where company operates]
- Activity scope: limited to the executive's actual area of responsibility
- Consideration: the terms of this agreement constitute adequate consideration
- Enforceability: see jurisdictional notes

**Non-solicitation of employees**:
- Duration: [12–24] months
- Scope: limited to direct reports and employees with whom the executive had material contact

**Non-solicitation of customers**:
- Duration: [12–24] months
- Scope: limited to customers with whom the executive had direct and material dealings

### 11. Governing law and dispute resolution

- Governing law: the law of the jurisdiction of employment (UAE Federal Law; DIFC Law; KSA Law, etc.)
- Dispute resolution: for UAE/KSA employment disputes, the labour courts are the primary forum for statutory claims; contractual disputes may go to arbitration if agreed
- In DIFC: DIFC Courts have jurisdiction over DIFC employment disputes; arbitration is also available

## Jurisdictional notes

### Non-compete enforceability in MENA

| Jurisdiction | Enforceability | Notes |
|---|---|---|
| **UAE** | Enforceable in principle (UAE Labour Law Art. 10, Federal Decree-Law 33/2021) | Maximum 2 years; must protect legitimate interest; courts may reduce scope; senior executives have stronger case against overly broad restrictions |
| **KSA** | Enforceable if reasonable; limited enforcement track record | Saudi Labour Courts apply a reasonableness standard; practical enforcement is limited |
| **DIFC** | Common-law; similar to English approach | 12–24 months reasonable; must protect a legitimate interest (trade secrets, key client relationships); garden leave during notice reduces post-termination period courts will enforce |
| **Lebanon** | Enforceable under Lebanese Code of Obligations and Contracts | Courts reduce if unreasonable |

### End-of-service gratuity for executives

The end-of-service gratuity applies to executives in UAE and KSA just as to regular employees:
- UAE: calculated on basic salary; 21 days per year for first 5 years; 30 days per year thereafter; max 2 years' total salary
- For executives whose base salary is, say, AED 500,000/year, the gratuity entitlement is material and must be budgeted for
- The agreement cannot waive or reduce the statutory gratuity entitlement

## Common mistakes

- **"For cause" definition too narrow**: If "cause" is defined narrowly and does not cover gross misconduct or serious breach, the executive can engage in harmful behavior that still requires paying full severance.
- **"Good reason" definition too broad**: Overly broad "good reason" definitions allow executives to trigger severance after any organizational change; tie good reason to objective material changes.
- **Single-trigger change-of-control acceleration**: Single-trigger vesting acceleration (acceleration merely on change of control, regardless of what happens to the executive) can create perverse incentives for executives to support a sale rather than maximize value; double-trigger is more governance-friendly.
- **No PILON clause**: Without a payment-in-lieu-of-notice provision, the company must allow the executive to work out the full notice period, retaining access to systems and client relationships.
- **Ignoring statutory floor**: In UAE and KSA, the statutory minimum terms (notice, gratuity) apply regardless of what the agreement says; an agreement below the statutory floor is unenforceable to that extent.

## Related skills

- [[prompt-pack-employment-offer-letter]]
- [[prompt-pack-employment-contract-compliance-review]]
- [[prompt-pack-equity-incentive-plan-summary]]
- [[prompt-pack-employee-handbook]]

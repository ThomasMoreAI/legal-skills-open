---
name: draft-offer-letter-sboghossian
title: Job Offer Letter
description: Use when drafting a job offer letter — the short-form pre-contract document confirming key employment terms to a candidate before the full employment contract is signed. Covers required components (role, compensation, contingencies, acceptance deadline), jurisdictional binding-effect issues (UAE MOHRE process, KSA Qiwa registration, LB Labor Code), and common mistakes that inadvertently create binding commitments or leave equity/compensation ambiguous. Triggers on "offer letter", "employment offer", "job offer", or "letter of offer" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-offer-letter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Job Offer Letter

## When to use this

An offer letter is the short-form document sent to a candidate after a hiring decision to confirm the key terms of the proposed employment before a full employment contract is signed. It provides certainty to the candidate, confirms the agreed commercial terms, and allows both sides to proceed with necessary formalities (visa application, background check, notice period with prior employer) while the formal contract is prepared.

An offer letter is NOT a substitute for a full employment contract — but in some jurisdictions (especially UAE) it has significant legal consequences and must be drafted carefully.

## Required inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Employer name + entity type + address | Full identification | — must supply |
| Candidate full name | Full identification | — must supply |
| Role / title | Defines the position offered | — must supply |
| Start date | Triggers visa, onboarding, and notice-period timing | — must supply or estimate |
| Location | Physical workplace; applicable labor law determined by place of work | — must supply |
| Base salary | Core economic term; state currency and frequency | — must supply |
| Variable / bonus | Any performance-based component (triggers at plan level, not formula) | "Eligible for annual bonus subject to performance review" |
| Equity | Stock option / restricted stock grant (if any); vesting schedule | Omit unless applicable |
| Reporting line | Clarifies organizational structure | — must supply |
| Conditions precedent | Background check, work authorization, signing full contract | Standard 3 listed |
| Acceptance deadline | Prevents indefinite offers; creates urgency | 5-7 business days |

## Optional inputs
- Benefits summary (health insurance, life insurance, pension/DEWS — DIFC) — high-level; full details in handbook
- Relocation assistance (if candidate is relocating from another country)
- Sign-on bonus (and repayment provision if the employee leaves within 12 months)
- Probation period reference (full details in the employment contract)

## Document structure (1-2 pages)

### 1. Date and salutation
On company letterhead. Date of the letter. Personal salutation: "Dear [Candidate First Name],"

### 2. Offer headline (1-2 sentences)
"We are pleased to offer you the position of [Title] at [Company Name], [Location]. This letter summarizes the key terms of our offer."

### 3. Position details
- **Title**: [Job Title]
- **Department**: [Department]
- **Reporting to**: [Name, Title]
- **Location**: [Office address or "primarily remote from [location]"]
- **Start date**: [Date or "on a mutually agreed date, anticipated on or around X"]
- **Work schedule**: full-time; standard working hours per applicable labor law (specify if different)

### 4. Compensation

**Base salary**: [Amount] [Currency] per [month/year], payable [monthly/bi-monthly] in arrears on the [X]th of each month.

**Variable / performance bonus** (if applicable): "You will be eligible to participate in the Company's annual discretionary bonus plan, with a target bonus of [X]% of your base salary, subject to individual and company performance. Bonus is not guaranteed and may be prorated in your first year."

**Equity** (if applicable): "Subject to [Board/Committee] approval, you will be granted [number] [options/RSUs] in [Company] under the [Plan Name], with a vesting schedule of [4 years with 1-year cliff, 25% per year thereafter / or specify]. The full terms will be set out in your grant agreement, which is not part of this offer letter."

Critical: do not describe equity in a way that creates binding expectations beyond what the plan document provides. If the plan has not yet been established, say so and state that equity will be offered upon adoption of a plan.

### 5. Benefits (high-level)
- Health insurance: [brief description — medical, dental, vision; family coverage if applicable]
- Annual leave: [X] working days per year in accordance with applicable law
- Pension / end-of-service benefit: as required by applicable law ([DEWS — DIFC] / [GRATUITY — UAE/KSA] / [NSSF — LB])
- Additional: "Full details of the Company's benefits are available in the Employee Handbook, which you will receive on your start date."

### 6. Conditions precedent
This offer is contingent upon:
1. Successful completion of the Company's standard background and reference check
2. Verification of your right to work in [jurisdiction] (and, where applicable, successful issuance of a work visa sponsored by the Company)
3. Your signing of the Company's standard form of employment contract (and any associated documents — NDA, IP assignment, non-compete — the terms of which will be consistent with this offer)

Include if applicable: "This offer is also subject to [regulatory clearance / fitness and propriety approval / security clearance]."

### 7. At-will / termination notice (common-law jurisdictions)
For DIFC, ADGM, UK:
- "Your employment will be on an 'at-will' / 'at-pleasure' basis [if applicable to jurisdiction], terminable by either party on [X weeks/months] written notice, or payment in lieu of notice. Details are in the employment contract."
- Note: "at-will" employment (terminable without cause) is a common-law concept; it does not exist in the same form in UAE federal, KSA, LB, or EG labor law — do not include this language for onshore MENA employment

### 8. Confidentiality of offer
"Please treat the terms of this offer as confidential until your start date or the Company's public announcement of your appointment."

### 9. Acceptance instructions
"If you wish to accept this offer, please sign and return a copy of this letter to [HR contact / email] by [date — typically 5-7 business days from issue date]. Your acceptance confirms that the terms set out herein are acceptable to you and that you will sign the Company's standard employment contract on or before your start date."

### 10. Signature block
```
On behalf of [Company Name]:

________________________        Date: ___________
[Name]
[Title]

ACCEPTED AND AGREED:

________________________        Date: ___________
[Candidate Full Name]
```

## Jurisdictional binding-effect issues

| Jurisdiction | Effect of the offer letter |
|---|---|
| **UAE federal / onshore** | The offer letter (or MOHRE standard form offer) is the legally binding offer; once accepted, the employer is contractually committed. MOHRE (Ministry of Human Resources and Emiratisation) requires a standardized offer form for registration of work permits. The formal employment contract follows and must match the MOHRE offer's key terms. Discrepancies between the offer and the formal contract give the employee grounds to challenge the contract. |
| **KSA** | Offers are registered through the Qiwa platform; Qiwa contract registration is required for work permit issuance. The Qiwa contract is the binding employment document; the offer letter precedes it. Ensure consistency between the offer letter and the Qiwa contract. |
| **Lebanon (LB)** | The offer letter is a common practice but does not substitute for the formal contract under the Labor Code. Under Lebanese contract law (Code of Obligations Art. 178 onward), a binding contract can form from an accepted offer — the letter may itself be the contract if it contains all essential terms. Draft carefully to either make it binding or expressly condition it on signing a formal contract. |
| **DIFC** | DIFC Employment Law 2005 (as amended); the offer letter is a pre-contract document; the employment contract or DIFC standard terms must be executed before or on the start date. At-will termination is common for senior employees. |
| **ADGM** | ADGM Employment Regulations 2019; similar to DIFC; employment contract required before start. |
| **France** | A job offer constitutes a binding offer under French contract law once accepted. Withdrawing a job offer after acceptance may constitute a breach giving rise to damages. Include a clause that the offer is subject to signing the formal employment contract and any required regulatory approvals. |

## Common mistakes to flag

1. **Promising equity without describing the plan and vesting**: an offer that says "you will receive options" without specifying the plan, exercise price basis, vesting schedule, and grant size creates legal ambiguity — the candidate may argue a specific entitlement was created

2. **Salary stated without currency and frequency**: "100,000 per year" in UAE — is that AED or USD? Monthly payment frequency also matters for MOHRE registration

3. **Missing "subject to" conditions**: if the conditions precedent clause is omitted, the offer may be unconditional — the employer then cannot withdraw if a background check reveals a disqualifying issue without potentially triggering a breach-of-contract or discrimination claim

4. **Describing the probation period in the offer letter but not matching it in the employment contract**: UAE labor law limits probation to 6 months; state it correctly or leave it for the employment contract

5. **Insufficient acceptance deadline**: an indefinite offer creates organizational uncertainty and gives the candidate leverage to delay acceptance while shopping for counter-offers

6. **Describing benefits in binding terms in the offer letter**: benefits described in the offer letter (rather than "as set out in the Employee Handbook") may be contractually binding even if the handbook changes. Use qualified language: "subject to the terms of the applicable plan documents."

## Related skills

- [[draft-employment-contract]]
- [[draft-non-compete]]
- [[draft-non-solicit]]
- [[draft-pip-letter]]

---
name: prompt-pack-severance-agreement-sboghossian
title: Severance Agreement
description: 'Use when an employer needs to draft a severance agreement for a departing employee, covering severance payment, end-of-service gratuity reconciliation, benefits continuation, a release of all employment-related claims, non-disparagement, post-employment obligations (confidentiality, non-compete, non-solicitation), and cooperation. Critically MENA-aware: UAE Labour Law mandatory End of Service Gratuity (EOSG), KSA severance rules under the Saudi Labour Law, and the enforceability of releases and non-compete clauses across MENA civil-law and common-law jurisdictions.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-severance-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Severance Agreement

## When to use this

Use this skill when:
- An employer and departing employee are agreeing enhanced severance terms above statutory minimums in exchange for a release of claims.
- An employment relationship is ending by mutual agreement (as opposed to unilateral dismissal), and both parties want to document the agreed terms.
- A company is restructuring and needs a standardized severance template for a redundancy program.
- A senior executive departure involves complex benefit entitlements (unvested equity, deferred compensation, benefits continuation) requiring negotiated documentation.

**Distinguish from:** A termination letter (use [[prompt-pack-termination-letter]]) is a unilateral employer notice of termination; a severance agreement is bilateral and typically involves consideration flowing to the employee (enhanced severance) in exchange for a release. If no release is being sought, a simple termination letter may be sufficient.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Employee name and position** | Identifies the subject of the agreement | Ask |
| **Employer details** | Legal entity name, jurisdiction | Ask |
| **Reason for departure** | Affects statutory entitlements and release structure | Ask: redundancy / mutual consent / performance / retirement |
| **Termination / last working date** | Starting point for calculating all entitlements | Ask |
| **Statutory entitlements** | UAE EOSG, KSA award, DIFC statutory payment — must be calculated before the severance payment can be structured | Ask; do not calculate EOSG without the full service history |
| **Enhanced severance amount** | The consideration for the release | Ask |
| **Jurisdiction** | Determines mandatory employment law entitlements that cannot be waived | Ask; this is the most important input |

## Optional inputs

- **Unvested equity / LTIP** — treatment of unvested stock options, restricted stock units, or LTI plans on termination; typically governed by the equity plan rules.
- **Post-employment restrictions** — non-compete, non-solicit of clients, non-solicit of employees; enforceability varies dramatically by jurisdiction.
- **Garden leave** — notice period during which the employee is paid but not required to work; relevant for senior hires with access to confidential information.
- **Reference letter** — whether the employer commits to providing a neutral or positive reference.
- **Return of company property** — equipment, documents, access credentials.

## Document structure

1. **Recitals**
   - Employee's employment commenced [date], in the role of [title].
   - The parties have agreed to end the employment relationship on [termination date] by mutual consent.
   - The parties wish to document the terms of separation.

2. **Termination date and transition**
   - Final date of employment: [date].
   - Garden leave / notice period: if applicable.
   - Last day of active employment: [date].
   - Transition obligations during notice: continuation of duties / handover / garden leave (specify).

3. **Final entitlements — statutory minimum**
   The severance agreement must itemize the statutory minimum the employee is entitled to by law:

   **UAE (Federal Decree-Law No. 33 of 2021):**
   - Unpaid salary to termination date.
   - Accrued untaken annual leave (pay in lieu at basic salary rate per Art. 29).
   - End of Service Gratuity (EOSG):
     - 21 calendar days' basic salary per year for the first 5 years of service.
     - 30 calendar days' basic salary per year thereafter.
     - Calculated on basic salary only (excluding allowances) for unlimited contracts; Art. 51 applies.
     - If employee resigned voluntarily with less than 5 years' service: EOSG entitlement may be partial or nil depending on service length; verify under the applicable contract type.
   - Repatriation allowance (if applicable under the employment contract or MOHRE template contract).

   **DIFC (DIFC Employment Law, DIFC Law No. 2 of 2019 as amended):**
   - Unpaid salary, accrued leave.
   - End of Employment Gratuity (EEG): 21 days' basic wage per year of service regardless of resignation or termination; applies to all DIFC employees.
   - Note: DIFC EEG formula is different from UAE mainland EOSG.

   **KSA (Saudi Labour Law, Royal Decree M/51 of 2005 as amended):**
   - Severance award: one-third of monthly wage per year for the first 5 years; two-thirds per year for years 5–10; full monthly wage per year thereafter.
   - Notice period: 60 days minimum for unlimited contracts.
   - No EOSG concept; the severance award (مكافأة نهاية الخدمة) is the Saudi equivalent.

   **Lebanon:**
   - End of service indemnity under Lebanese Labour Code: one month's salary per year of service, capped as per the Code.
   - Notice period: 1 month (0–3 years); 2 months (3–6 years); 3 months (6+ years).

4. **Enhanced severance payment**
   - Amount of severance in excess of statutory minimum.
   - Characterization: "in consideration of the Employee's execution of this Agreement and the release of claims contained herein."
   - Payment date: on or within [X] business days of execution of this Agreement.
   - Method: bank transfer to [account details].
   - Tax: "The Employee acknowledges that severance payments may be subject to applicable income tax or social insurance deductions and agrees to be responsible for any such obligations."
   - **MENA note:** EOSG and KSA severance awards are typically tax-free under UAE and KSA law for expatriate employees; enhanced amounts above statutory minimums may or may not be taxed depending on the employee's tax residency.

5. **Benefits continuation** (if applicable)
   - Health insurance: maintained until [date]; COBRA equivalent not applicable in UAE/KSA but employer may offer extended coverage as a benefit.
   - Other benefits: housing allowance, car allowance, school fees — state clearly whether they continue through the notice period and whether any are forfeited.
   - Equity / LTI: state the treatment of unvested awards expressly — "accelerated vesting / forfeiture / pro-rata" per the equity plan rules.

6. **Release of claims** — key provision
   - In consideration of the severance payment above (which exceeds the employee's statutory entitlements), the employee releases and forever discharges the employer, its officers, directors, affiliates, and employees from all claims, demands, and liabilities arising from or in connection with the employment relationship or its termination, including but not limited to:
     - Claims for unpaid wages, overtime, bonuses, and commissions.
     - Claims for wrongful dismissal or unfair termination.
     - Claims for discrimination, harassment, or retaliation.
     - Any other claim arising under applicable employment law.
   - **MENA note:** In UAE, DIFC, and KSA, a release of all statutory employment rights may not be enforceable to the extent it waives mandatory minimum entitlements. Courts in these jurisdictions will typically enforce releases of claims above the statutory minimum (i.e., the enhanced severance), but will not permit waiver of EOSG, unpaid wages, or other statutory entitlements. The agreement should therefore state that statutory entitlements have been paid in full and separately identified.
   - Employee acknowledges receiving and reviewing this agreement; had opportunity to consult legal counsel; and enters voluntarily.
   - **UK/EU note:** In the UK, a settlement agreement (formerly "compromise agreement") must comply with ERA 1996 s.203 requirements: written, the employee must have received independent legal advice from a qualified adviser (usually a solicitor) on the effect of the release, and the agreement must identify the adviser and confirm the advice was given. Without this, the release is unenforceable.

7. **Mutual release (employer)**
   - Employer releases employee from claims arising from employment, unless the employee has engaged in fraud or gross misconduct not yet known to the employer.
   - Standard carve-outs: claims arising from the employee's breach of this agreement; undisclosed theft or fraud; IP obligations.

8. **Post-employment obligations**

   **Confidentiality:**
   - Employee confirms and reaffirms confidentiality obligations arising from the employment contract; these survive termination.
   - Specifically includes: customer lists, pricing, technical know-how, financial information, strategic plans.
   - Duration: indefinite for genuine trade secrets; 2–3 years for other confidential information.

   **Non-compete:**
   - Scope: industry, role type, geographic territory, duration.
   - **Enforceability trap:** Non-compete clauses are often unenforceable or only partially enforceable in MENA jurisdictions:
     - UAE: Art. 10 of UAE Labour Law allows non-competes for employees with access to trade secrets; limited to 2 years, specific geographic area, and specific type of work; court discretion to reduce scope.
     - DIFC: generally enforceable if reasonable in scope, time, and territory.
     - KSA: non-competes are recognized but courts scrutinize reasonableness; payment of compensation during the restriction period strengthens enforceability.
     - UK: enforceable only to the extent necessary to protect a legitimate business interest (restrictive covenant law).
   - Payment during non-compete period: some jurisdictions (Germany, France) require payment during a garden leave / non-compete period; UAE and KSA do not, but payment is good practice for enforceability.

   **Non-solicitation of clients and employees:**
   - Prohibition on soliciting the employer's clients for a defined period.
   - Prohibition on recruiting the employer's employees.
   - These are generally more enforceable than broad non-competes because they protect specific business interests.

9. **Return of company property**
   - Employee must return all company property (hardware, documents, access cards, vehicles) by the termination date.
   - Employee must delete all company data from personal devices.
   - Right of audit: employer may request written confirmation that data has been deleted.

10. **Cooperation**
    - Employee agrees to cooperate with any ongoing investigations, litigation, or regulatory proceedings to which they may be a witness, for a defined period after termination.

11. **No admission of liability** — standard clause.

12. **Governing law and dispute resolution** — per jurisdiction.

## Drafting standards

- Identify and separately itemize statutory minimums (EOSG, KSA severance, DIFC EEG) and enhanced amounts. Courts in MENA jurisdictions protect statutory minimums regardless of what the agreement says; showing they have been paid separately is crucial.
- Include a **reconsideration period** where relevant: in some jurisdictions, employees must have a defined period to review the agreement before executing (UK: 10-day consideration period recommended; US ADEA: 21/45-day review period — not applicable in MENA but good practice for senior executives).
- The release clause is the anchor of the document — spend the most time on its scope, carve-outs, and jurisdiction-specific enforceability.

## Common mistakes

- **Bundling EOSG into the enhanced severance without separating them.** If the employee later disputes the EOSG calculation, the court cannot assess what was paid for what; always itemize separately.
- **Overreaching non-compete.** A non-compete that covers all industries globally for 5 years will be void; draft a narrow, enforceable restriction or none at all.
- **No legal advice acknowledgment in UK agreements.** Without the statutory requirements for a UK "settlement agreement" being met, the release of statutory employment rights is unenforceable.
- **Missing equity treatment.** If the employee has unvested equity, failing to address its treatment creates post-termination litigation risk.

## Related skills

- [[prompt-pack-termination-letter]]
- [[prompt-pack-remote-work-policy]]
- [[prompt-pack-settlement-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]

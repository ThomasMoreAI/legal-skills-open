---
name: prompt-pack-termination-letter-sboghossian
title: Termination Letter
description: 'Use when an employer needs to draft a formal termination letter for an employee, covering the termination grounds, effective date, final pay entitlements, benefits continuation, property return obligations, and post-employment restriction reminders. Critically MENA-aware: UAE Labour Law (Federal Decree-Law No. 33 of 2021) notice periods and EOSG obligations, KSA Labour Law dismissal procedures, Lebanese Labour Code dismissal indemnity rules, and the distinction between lawful termination and arbitrary dismissal across MENA jurisdictions.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-termination-letter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Termination Letter

## When to use this

Use this skill when:
- An employer needs to formally notify an employee of the termination of their employment.
- The termination is: for cause (misconduct, performance); redundancy (economic/structural); end of fixed-term contract; or without cause (unilateral termination with notice).
- The termination letter is a standalone document (where no enhanced severance is being offered) OR the initial notification before a severance agreement is negotiated.
- The employer wants to document the statutory and contractual entitlements clearly to avoid future disputes.

**Distinguish from a severance agreement:** A termination letter is a unilateral act by the employer; it informs the employee of termination and states final entitlements. A [[prompt-pack-severance-agreement]] is a bilateral negotiated document where the employee receives enhanced severance in exchange for a release of claims. For senior executives or contested departures, a termination letter followed by a severance agreement is the standard workflow.

**Critical MENA note:** In MENA jurisdictions, "termination with notice" (as in voluntarily walking away with proper notice) and "termination for cause" (immediate dismissal for serious misconduct) have very different legal consequences. Getting the characterization wrong exposes the employer to liability for arbitrary dismissal, additional indemnities, or labor inspection proceedings.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Employee name, position, and start date** | For EOSG/severance calculation; personalizing the letter | Ask |
| **Employer name** | Identifies the terminating party | Ask |
| **Reason for termination** | Determines: (a) required notice period; (b) EOSG entitlement; (c) whether cause is legally valid | Ask; this is the most legally sensitive input |
| **Effective date (or notice period start date)** | The date from which the notice runs or the last working day | Ask |
| **Jurisdiction** | Determines all statutory entitlements and the legality of the termination grounds | Ask; this is the most critical input |

## Optional inputs

- **Garden leave** — whether the employee works through the notice period or is placed on garden leave (paid but not required to work).
- **Final salary calculation** — if known, include; otherwise state "to be calculated."
- **Severance offer** — if the employer is offering enhanced severance alongside or following this letter, indicate it.
- **Post-employment restrictions** — reminder of non-compete, non-solicit, and confidentiality obligations from the employment contract.

## Document structure

1. **Header**
   - Company letterhead.
   - Date.
   - Employee name and address.
   - Reference: "Re: Termination of Employment" or "Re: Notice of Termination."

2. **Opening paragraph — the decision**
   - State the decision clearly and without ambiguity: "We hereby give you notice of the termination of your employment with [Company] effective [date / on expiry of your notice period as set out below]."
   - Avoid hedging language — unclear language ("we are regretfully considering...") can create procedural arguments about whether a formal termination has occurred.

3. **Reason for termination**

   The reason shapes the entire letter; select and expand the appropriate module:

   **Module A — Termination with notice (no cause / redundancy):**
   - "Your employment is being terminated by reason of [redundancy / business reorganization / position elimination / no cause as permitted under your employment contract]."
   - Notice period: "In accordance with [clause X of your employment contract / applicable law], your notice period is [X weeks/months]. Your last working day will be [date]."
   - Garden leave: "During your notice period, you will / will not be required to attend work [and will / will not continue to receive your usual salary and benefits]."

   **Module B — Termination for cause (summary dismissal):**
   - "This letter serves as notice of your immediate dismissal for cause. The basis for this decision is [describe the conduct or performance failure]."
   - Procedure: for UAE (and most MENA jurisdictions), dismissal for cause should follow a disciplinary procedure (written warning, right to be heard) before a final dismissal — unless the misconduct is so serious that summary dismissal is appropriate. State that the procedure was followed.
   - Valid causes in UAE (Labour Law Art. 44): specific grounds listed in the law; dismissal outside these grounds is "arbitrary dismissal" triggering additional compensation.
   - **Do not use Module B unless the grounds are legally valid and the procedure has been followed.** An unlawful termination for cause converted into a "for cause" termination letter exposes the employer to significant liability.

   **Module C — End of fixed-term contract:**
   - "Your fixed-term employment contract dated [date] will expire on [date] and will not be renewed. Your last working day is therefore [date]."
   - Note: if a fixed-term contract is terminated before expiry without cause, the employer may owe the employee the remaining period's salary as damages (UAE Labour Law Art. 44; Lebanese Labour Code).

   **Module D — Performance-based termination (after performance improvement plan):**
   - Reference the performance improvement plan (PIP) that was previously issued; state that the employee has not met the required performance standards despite the PIP process.
   - Ensure the PIP process was documented and the employee had an opportunity to respond before issuing this letter.

4. **Final entitlements**

   State clearly what the employee is owed. This should be itemized, not lumped together:

   **UAE — onshore (Federal Decree-Law No. 33 of 2021):**
   - Notice period pay: [amount] or "your salary will continue to be paid through the end of your notice period on [date]."
   - Unpaid accrued salary to termination date.
   - Annual leave balance: "You have [X days] of accrued and unused annual leave as of [date]. This will be paid out at your basic salary rate."
   - End of Service Gratuity (EOSG):
     - For termination with notice (employer-initiated): full EOSG per the statutory formula (21 days/year for first 5 years; 30 days/year thereafter, based on basic salary).
     - For resignation by employee with under 5 years of service: partial EOSG (1/3 entitlement after 2 years; 2/3 after 3 years; full after 5 years).
     - For summary dismissal for cause (grounds listed in Art. 44): EOSG is forfeited.
   - "Your EOSG has been calculated as approximately [AED X], subject to final confirmation by HR."
   - Repatriation allowance (if applicable per employment contract or MOHRE template).

   **DIFC (DIFC Employment Law No. 2 of 2019 as amended):**
   - End of Employment Gratuity (EEG): 21 days per year of service (regardless of resignation or termination) based on basic wage.
   - Notice pay; unused leave; any unpaid salary.

   **KSA (Saudi Labour Law, Royal Decree M/51 of 2005):**
   - Severance (مكافأة نهاية الخدمة): one-third monthly wage per year for first 5 years; two-thirds for years 5–10; full monthly wage per year thereafter.
   - Notice pay (60 days minimum for unlimited contracts).
   - Accrued vacation pay.
   - Repatriation to home country (for non-Saudi employees per the employment contract).

   **Lebanon (Labour Code 1946 as amended):**
   - End of service indemnity: one month's salary per year of service.
   - Notice period: 1–3 months depending on tenure (Art. 50 Labour Code).
   - NSSF (social insurance) end of service settlement.

   **UK (Employment Rights Act 1996):**
   - Statutory notice: at least 1 week per year of service (up to 12 weeks).
   - Statutory redundancy pay (if redundancy): calculated per statutory formula.
   - Final salary payment; accrued holiday pay.
   - Pension and benefits continuation through notice period.

5. **Return of company property**
   - "You are required to return all company property, including [laptop, mobile phone, access cards, documents, files, keys] by [date]."
   - Access to company systems will be revoked on [date].
   - "You confirm that you will delete all company data from any personal devices."

6. **Post-employment obligations reminder**
   - "This letter is to remind you of your ongoing obligations under your employment contract, including:
     - Confidentiality: [duration and scope per employment contract].
     - Non-compete: [if applicable; duration and geographic/sector scope].
     - Non-solicitation: [if applicable; duration and scope].
   - Please review your employment contract for the full terms."

7. **Benefits continuation**
   - State clearly what happens to health insurance, housing allowance, car allowance, school fees during the notice period and after termination.
   - No benefits "cliff edge" for employees in UAE/KSA — most allowances cease on termination date; notice period is typically paid at full salary including allowances.

8. **Next steps**
   - "A final settlement calculation will be provided by HR within [5/10] business days."
   - "Please contact [HR contact] to arrange return of equipment and processing of your final entitlements."
   - If severance negotiation is contemplated: "We will be in touch shortly to discuss the terms of your departure."

9. **Closing**
   - "We thank you for your contributions to [Company] and wish you well in your future endeavors." (Include or omit based on the circumstances; omit for for-cause dismissals.)
   - Signed by: an authorized representative (HR Director, General Manager, or Board) with name and title.

## Jurisdictional notes — lawful vs. arbitrary dismissal

### UAE — arbitrary dismissal (فصل تعسفي)
- UAE Labour Law Art. 47: if an employer terminates an employee without a valid reason under the Law, or for reasons other than those specified as valid cause (Art. 44), the termination is "arbitrary."
- Arbitrary dismissal entitles the employee to additional compensation of up to 3 months' full wage (on top of EOSG and notice pay).
- UAE courts take a broad view of arbitrary dismissal; performance-based termination without documentation is frequently found to be arbitrary.

### KSA — unlawful dismissal
- Saudi Labour Law Art. 77: employer must have a valid reason for termination; employee who is dismissed without valid cause may be awarded compensation of up to 2 years' wages in addition to end of service entitlements.
- Disciplinary procedures (Arts. 66–85): employer must follow the steps (investigation, written notice, opportunity to respond) before dismissal for cause.

### DIFC
- DIFC Employment Law Art. 55: unfair dismissal claims available for DIFC employees with at least 12 months' service; employer must have a fair reason and follow a fair process.
- Compensation for unfair dismissal: up to 1 year's wage.

### Lebanon
- Lebanese Labour Code Art. 74: employer may dismiss an employee for serious fault (faute grave) without notice or indemnity; otherwise, notice + end of service indemnity is owed.
- Dismissal for reason of unionizing, pregnancy, or discriminatory grounds is void.

## Drafting standards

- Match the termination letter's characterization to the actual circumstances — a performance-based termination dressed up as a "mutual departure" can create misrepresentation issues.
- Include the EOSG/EEG calculation (even if approximate) in the letter — employees are entitled to know; providing it reduces post-termination disputes.
- For for-cause termination: ensure the disciplinary procedure has been completed before the letter is sent; document the procedure separately; the letter should reference the prior process.
- Do not include unnecessary opinions ("the company has lost confidence in you") — these can be used in employment tribunal proceedings as evidence of improper motives.

## Common mistakes

- **Notice period not specified.** "Your employment will be terminated" without specifying the notice period or last working day leaves the termination date ambiguous.
- **EOSG calculation error.** EOSG in UAE is calculated on basic salary only (not total remuneration); using total salary inflates the figure and creates a future liability dispute.
- **Omitting garden leave terms.** If the employee is placed on garden leave, the letter must state this clearly; ambiguity about whether the employee is expected to work during the notice period creates operational and legal risk.
- **For-cause characterization without procedure.** Issuing a "for cause" letter without having completed a disciplinary process (written warning, opportunity to respond) invalidates the cause-based termination in UAE, KSA, and most MENA jurisdictions.
- **No COBRA/benefits reference for US employees.** COBRA (US-specific) is not applicable in MENA; do not include it; use jurisdiction-appropriate benefits continuation language instead.

## Related skills

- [[prompt-pack-severance-agreement]]
- [[prompt-pack-remote-work-policy]]
- [[prompt-pack-professional-email-draft]]
- [[prompt-pack-settlement-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]

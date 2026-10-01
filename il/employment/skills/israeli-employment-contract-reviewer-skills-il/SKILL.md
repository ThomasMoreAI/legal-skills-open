---
name: israeli-employment-contract-reviewer-skills-il
title: Israeli Employment Contract Reviewer
description: Not legal advice. Pre-signing red-flag audit of an Israeli employment contract (chozeh avoda) from the employee's defensive perspective. Scans a pasted contract for illegal clauses, missing mandatory protections, and unfair terms, then produces an annotated review with citations to Israeli labor law. Flags Section 14 (Saif 14) waiver traps, unenforceable non-competes, hoda'at mukdemet below statutory minimum, missing pension, missing keren hishtalmut, at-will language, and gross vs net ambiguity. Produces a negotiating points memo for the employer. Use when about to sign an Israeli employment contract and wanting an independent review before committing. Do NOT use for generating new contracts (use israeli-employment-contracts), post-hire workplace rights (use israeli-workplace-rights-navigator), payroll calculations (use israeli-payroll-calculator), or unemployment benefits (use israeli-unemployment-benefits-navigator).
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-employment-contract-reviewer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: employment
language: en
sources:
- title: High Value Clause Traps
  path: references/high-value-clause-traps.md
- title: Hoda At Mukdemet Table
  path: references/hoda-at-mukdemet-table.md
- title: Notice To Employee Disclosures
  path: references/notice-to-employee-disclosures.md
- title: Numerical Sanity Checks
  path: references/numerical-sanity-checks.md
- title: Red Flag Checklist
  path: references/red-flag-checklist.md
- title: Section 14 Trap Guide
  path: references/section-14-trap-guide.md
- title: Standard Negotiation Language
  path: references/standard-negotiation-language.md
---

# Israeli Employment Contract Reviewer

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


## Problem
Israeli employees routinely sign employment contracts with clauses that are either illegal under Israeli labour law or that quietly transfer risk from the employer to them. The most expensive traps cost tens of thousands of shekels over a career, and several of them are perfectly lawful terms rather than illegal ones: a Section 14 waiver on a base-only salary definition, pension computed on the average wage rather than the full gross, an option grant with a 90-day exercise window. This skill scans a contract before signing, flags every red flag with a specific citation, and generates a negotiating points memo the employee can take back to the employer.

## Instructions

### Step 1: Collect the Contract

Ask the user to paste the full contract text in Hebrew or English (or both). If they only have a PDF, ask them to paste the text extracted from it. Also ask:

| Input | Required | Used for |
|-------|----------|----------|
| Full contract text | Yes | The audit subject |
| Target role (engineer, marketer, sales, etc.) | Yes | Determines which clauses are reasonable |
| Annual gross compensation | Yes | Spot unusual ratios (e.g., unreasonable non-compete duration vs pay) |
| Employment scope (`heikef misra`), full-time or a percentage | Yes | Vacation, havra'a, the pension base, sick accrual and the minimum-wage floor all pro-rate to scope. Skipping this produces false blockers on part-time contracts |
| Is this for a tech startup, corporate, or traditional company? | Yes | Startups are more likely to include illegal non-competes |
| Any clauses the user already finds suspicious | No | Prioritizes user's concerns |

Do NOT draft a new contract. This skill reviews existing contracts only. If the user wants to generate one, point them to the `israeli-employment-contracts` skill.

### Step 2: Run the Red-Flag Checklist

Scan the contract for each item in the checklist below. For every finding, record:
- Location (quote the exact clause)
- Rule violated (cite the law and section)
- Severity (blocker, major, minor)
- Negotiation recommendation

#### Mandatory protections (look for their PRESENCE)

| Item | Must include | If missing | Citation |
|------|-------------|------------|----------|
| Job title and scope | Clear role description | Major: employer can reassign arbitrarily | Notice to Employee and Job Candidate (Employment Conditions and Screening/Hiring Procedures) Law, 5762-2002 |
| Start date | Exact date | Blocker: contract is incomplete | - |
| Gross monthly salary | Explicit number | Blocker: negotiate before signing | Notice to Employee and Job Candidate (Employment Conditions and Screening/Hiring Procedures) Law, 5762-2002 |
| Working hours | Weekly total and daily range | Major: overtime calculation becomes ambiguous | Hours of Work and Rest Law 1951 |
| Pension contribution | Contribution clause | Blocker if missing entirely. From day 1 for an employee with a prior fund; after 6 months for a true first job (no prior fund). A "pension after 6 months" clause is legal for a first job | Mandatory Pension Order 2008 / Expansion Order |
| Hoda'at mukdemet (advance notice) | At least statutory minimum | Major: defaults to law anyway, but absence is a red flag | Prior Notice of Dismissal and Resignation Law 2001 |
| Dmei havra'a (convalescence pay) | Day count and rate | Major if the rate or day count is below statutory. The private-sector rate is 451.5 NIS/day for havra'a year 2026 (1 July 2025 to 30 June 2026), updated by an extension order published 18 August 2026; an employer who already paid at the old 418 NIS rate owes a 33.50 NIS top-up per day. Public sector is 511.6 NIS/day. Entitlement arises only on completing 12 months of employment, and the first payment then covers 5 days for year 1, scaling to 10 days at 20+ years | Extension Order (convalescence pay) |
| Travel reimbursement (`hechzer hotzaot nesia`) | A reimbursement clause | Major if absent. Every employee who needs transport to work is entitled to it for each working day, at the discounted bus fare up to 22.60 NIS/day or the cost of a monthly regional or national pass, whichever is cheaper. It applies at any job scope. Do not assume the "all-inclusive salary" analysis below settles it; ask whether the contract funds travel separately and on what basis | Extension Order (travel expenses) |
| Choice of pension product and provider | No clause naming a single fund or agent | Major. The employee is entitled to choose the TYPE of pension insurance (pension fund, provident fund, or managers' insurance) AND the specific institution that will manage it. A clause naming one fund or one agent and barring a move is unenforceable against that right | Mandatory Pension Order 2008 / Expansion Order |
| Annual vacation days | At least statutory minimum by tenure | Major: employer may be trying to under-provide | Annual Leave Law 1951 |
| Sick leave | At least statutory minimum | Major | Sick Pay Law 1976 |

#### Notice to Employee Law disclosure checklist (mandatory written terms)

The Notice to Employee and Job Candidate Law 5762-2002 requires the employer to put a defined list of terms in writing within 30 days of the start date (7 days for a worker under 18), and to give a further written notice within the same deadlines whenever a term changes. Apply the list as a presence check; any missing item is a finding, major if it is a pay or hours term and minor otherwise. The list covers the parties, the start date and the term if fixed, the role, the pay components and the payday, the basis of pay, normal daily or weekly hours, the weekly rest day, the social-benefit contributions and the receiving bodies, and any applicable extension orders or collective agreements.

See `references/notice-to-employee-disclosures.md` for the full list and citation.

#### Illegal or unfair clauses (look for their ABSENCE)

| Red flag | Why it is a problem | Action |
|----------|--------------------|---------|
| "At-will" employment | Israeli law does NOT recognize at-will. Dismissal requires due process (shimua), hoda'at mukdemet, and severance. Clause is unenforceable but signals a foreign-drafted contract the employer may try to enforce in practice | Flag as major. Ask for the clause to be removed or explicitly replaced with "subject to Israeli labor law" |
| A penalty/fine deduction, a training-cost clawback on resignation, equipment-loss, or cash-register shortfall deducted from pay | Wage Protection Law 1958 section 25 sets a CLOSED list of lawful deductions, and a debt the employee authorised in writing may not be deducted at more than a quarter of the wage per pay period. The list does include a disciplinary fine, but only one imposed under legislation or a collective agreement and under those alone, never under an individual employment contract. So a clause in the contract itself docking pay for a fine, a leaving penalty, lost equipment or a till shortfall falls outside the list and is void. Note the section 25(b) exception: on termination the employer may deduct the whole outstanding debt from the FINAL wage with no quarter cap, but only where the debt is undisputed in both existence and amount, so a contested equipment or clawback charge does not qualify. And keep two questions apart: section 25 governs only what the employer may TAKE OUT OF THE WAGE. It does not void a free-standing undertaking to repay training or signing-bonus money, which can still be enforced as a debt, so negotiate a tapering cap on that rather than assuming it falls away. Detect on קנס, penalty, "shall deduct", "training costs returned", "equipment damage", "cash shortfall" near deduction language | Blocker. Strike the clause. Anything outside the closed list is unlawful even if the employee "agreed" |
| At-will / unilateral dismissal clause with no carve-out for a pregnant employee, an employee on maternity leave, or one in fertility treatment | Employment of Women Law 5714-1954 section 9 requires a Ministry of Labour permit (heter) to DISMISS such an employee at 6+ months tenure, and the separate section 9A requires one to cut her pay or job scope. Protection continues through maternity leave and the 60 days after return. A dismissal-at-discretion clause cannot override this, and its absence leaves the employee unaware of it | Major. Add that any dismissal, pay cut or scope cut during pregnancy, maternity leave, the 60 days after return, or fertility treatment is subject to a heter |
| Contract implies cash pay or omits any payslip (tlush sachar) obligation | Wage Protection Law Amendment 24 (2008) requires a monthly detailed payslip listing every pay component and deduction. Cash-in-hand or payslip-silent contracts enable hidden deductions and unreported pension and BTL. Check too that the payday is no later than the 9th of the following month, after which the wage is delayed (`mulan`) under section 9 and carries the section 17 penalty | Major. Require an explicit detailed monthly payslip and a lawful payday |
| "All-inclusive" salary clause declaring the gross "includes" pension, havra'a, overtime, or vacation | Bundling cogent statutory components into one all-inclusive figure is void as to those components: pension, dmei havra'a, overtime and annual leave must each be stated and funded separately, on top of base pay. Detect on "inclusive of all social benefits", "כולל הכל", "includes pension and vacation" | Major. Require each statutory component to be a separate, separately funded line, not "included" in gross |
| Contractor/freelancer (kablan) agreement that carries employee hallmarks | Misclassification risk. Apply the subordination and integration test (`mivchan ha'hishtalvut`): fixed hours, a reporting manager, integration into the organisation and exclusivity all point to employment regardless of the "contractor" label, and a court can reclassify retroactively | Major. State the reclassification exposure and recommend either a genuine independent arrangement or an employee contract with full rights |
| Pension below the mandatory minimum | The mandatory minimum is employer 6.5% benefits (tagmulim) + employer 6% severance + employee 6% = 18.5% total. A 6% severance component is fully legal. (8.33% is NOT a legal minimum; it is only the severance rate needed for a full Section 14 waiver to completely replace statutory severance.) One exception matters: where the product is NOT a pension fund (typically managers' insurance), the employer's share must also buy disability cover sufficient to insure 75% of the determining wage, the tagmulim component alone may not fall below 5%, and the employer's combined tagmulim-plus-disability cost is capped at 7.5%. So a lawful managers'-insurance contract can show employer tagmulim below 6.5%. | Blocker only if any component is below 6.5% / 6% / 6%, EXCEPT the non-pension-fund case above, where the floor is 5% tagmulim plus disability cover to 75%. A contract on a non-pension-fund product that omits disability cover entirely is itself a major finding. A 6% severance contract is legal, not a blocker. If severance is below 8.33%, flag it as "does not fully fund a Section 14 waiver", not as illegal. Always check the BASE the rates apply to, not just the rates (see the salary-ceiling row below) |
| Section 14 (Saif 14) waiver without matching salary clause | Waives right to statutory severance in exchange for pension contributions, but if the "salary" definition excludes bonuses/overtime, the employee loses money | Major. Require "salary" to include all fixed components subject to pension |
| Hoda'at mukdemet set below statutory minimum | E.g., "7 days" for an employee of 2 years | Blocker. Statutory minimum is 30 days after year 1 |
| Non-compete (`ekronot i-tachrut`) exceeding 6-12 months | Israeli courts rarely enforce non-competes beyond protecting trade secrets. Clauses of 2+ years are typically unenforceable, but create chilling effect | Major. Negotiate down to 6 months max, narrow geographic scope, narrow competitor definition |
| Non-compete without compensation during the restriction period | Unenforceable unless trade secret is genuinely at stake and the employee was compensated for the restriction | Major. Remove or demand compensation equal to salary during the restricted period |
| Assignment of "all inventions ever" including personal projects | Employee Inventions Law protects off-work inventions unless directly related to the job | Major. Narrow to inventions made during work hours using work resources, related to the employer's business |
| Stated gross salary below the statutory minimum wage | As of 1 April 2026 the minimum wage is 6,443.85 NIS/month full-time. The hourly minimum is 35.40 NIS/hour for a 182-hour month; for a 186-hour month it is 34.64 NIS/hour (the monthly 6,443.85 figure is unchanged). A contract cannot set pay below this cogent floor; the figure is updated every April | Blocker. The salary must be raised to at least the current minimum wage. Verify the current rate, since it changes each April |
| "Global" or "comprehensive" overtime (`shaot globaliyot`) bundled into the base salary with no breakdown | Israeli courts often strike clauses that fold an unspecified, open-ended amount of overtime into one flat figure, because they mask unpaid overtime and defeat the Hours of Work and Rest Law. A global-overtime arrangement is only valid when it is a separate, quantified, capped component that is genuinely no less than the statutory 125%/150% rates for the hours actually worked | Major, and tell the employee what the remedy actually is: when a labour court strikes a global-overtime arrangement it re-characterises the WHOLE global sum as ordinary wage rather than netting it off, so the employee then gets the higher base flowing into severance, pension, havra'a and leave redemption AND statutory 125%/150% overtime on top of it. That is the negotiating leverage. Require overtime as a separate line item with a stated hour cap and explicit rates, or hourly overtime tracking |
| Salary defined as "gross" or "net" ambiguously | The gap between gross and net is large once income tax, National Insurance, health levy and the employee pension share come out, so the ambiguity is worth real money and the drafting employer benefits from it | Blocker. Require explicit "gross" (brutto) and state the components |
| Bonus described as "at the sole discretion of the employer" without trigger | Employer can deny forever. If it's labeled "bonus" it is not deferred compensation | Minor if user accepts the risk. Major if the role was pitched with a large bonus component |
| Working hours beyond 42/week without overtime clause | The 42-hour week comes from the general extension order of March 2018, NOT from the statute: Hours of Work and Rest Law s.3 still reads 45 hours, and s.2 caps the day at 8. Cite the order for the 42, the law for the daily cap and the rates | Major. Overtime must be 125% for the first 2 hours of the DAY and 150% for each hour after that; the split resets daily, not weekly |
| Clauses waiving the employee's rights under Israeli law | Unenforceable but signal bad faith | Major. Remove |
| Probation period (`tkufat nisayon`) treated as a rights-free window | Israeli law has no statutory probation. A probation clause does NOT shorten advance notice, does not suspend pension, and does not remove the employer's duty to hold a hearing (shimua) before dismissal. Its only real effect is on a contractual benefit expressly conditioned on completing it | Major if the clause purports to waive notice, pension or a hearing. Minor if it only gates a contractual benefit |
| Confidentiality clause extending forever | Standard is 3-5 years post-employment | Minor. Accept if narrowly scoped to trade secrets |
| No keren hishtalmut (education fund) for tech/professional roles | Standard in Israeli tech. Not legally required but expected | Major for tech roles. Negotiate to add with 7.5% employer / 2.5% employee split |
| Lawful but expensive clauses (each is a real finding, full detail in `references/high-value-clause-traps.md`) | Nine patterns that are legal and still cost more than most illegal clauses: (1) pension "in accordance with law" with no salary base, so contributions stop at the average wage (13,769 NIS/month in 2026); (2) a Section 30(a)(5) "management or special personal trust" recital, the companion trap to global overtime, read narrowly and not binding on a court; (3) a fixed term with no early-exit clause, or one ending just short of 12 months (Severance Pay Law ss.9 and 3); (4) an employer right to recover the severance component, which only ss.16 to 17 and a labour court can do; (5) termination and re-hire on a sale or intra-group transfer, resetting seniority; (6) an unrestricted right to vary role, terms or location, against the s.11(a) right to resign with severance on a material worsening; (7) silence on miluim, or treating reserve absence as unpaid leave (s.41A of the Discharged Soldiers Law); (8) an option or RSU grant with no Section 102 route, no post-termination exercise window and no acceleration; (9) keren hishtalmut on full salary with no ceiling (15,712 NIS/month in 2026), which is taxable to the employee above it | Major on each unless the reference file says otherwise, and (4) is a blocker. Raise them together in the negotiating memo, since they are the ones an employer will concede |
| Arbitration or foreign-forum clause | Section 24 of the Labour Court Law 5729-1969 gives the labour courts exclusive SUBJECT-MATTER jurisdiction as between Israeli courts; it is not a general rule voiding arbitration, so do not call every arbitration clause a blocker. The sound objection to a FOREIGN forum or foreign governing law is different: cogent Israeli protections attach to work performed in Israel and cannot be contracted away by choosing another forum or law | Major for a foreign forum or foreign governing law. Minor for domestic arbitration, noting the labour court is cheaper and more employee-friendly |

#### Numerical sanity checks

Compute the numerical checks in `references/numerical-sanity-checks.md` from the contract figures and flag anomalies: the minimum-wage floor, the pension rates AND the salary base they apply to, the keren hishtalmut split and ceiling, total employer cost, advance-notice days, annual vacation, sick leave and dmei havra'a. `scripts/contract_sanity_check.py` automates the pension, notice, vacation and sick-day checks. Every figure in that table moves on a fixed calendar (minimum wage each April, private-sector havra'a each July, the average wage and tax ceilings each January), so re-verify before quoting one as current.

### Step 3: Classify Severity

For each finding, assign:

- **Blocker**: illegal or grossly unfair. Do not sign without fixing.
- **Major**: below market standard or legally questionable. Negotiate before signing.
- **Minor**: acceptable but non-ideal. Note for future reference.

If the contract has 1+ blockers, the top-line recommendation is "do not sign until fixed."
If the contract has 0 blockers and only minor findings, the recommendation is "safe to sign, with these notes."

### Step 4: Produce the Annotated Review

Output format:

```
DISCLAIMER
This is an automated review, not legal advice. It is produced by an AI model with no
involvement or approval by an advocate, does not examine your full circumstances, and may
err. Before signing, consult an Israeli labour attorney (orech din avoda), and do so in any
case for a contract with significant blockers or for a senior or executive position.

# Contract Review Summary
**Overall recommendation:** <Do not sign | Negotiate | Safe to sign>
**Blockers:** N
**Major findings:** N
**Minor findings:** N

## Blockers (must fix before signing)
1. [Clause quote]
   - **Rule violated:** [law and section]
   - **Why it matters:** [consequence]
   - **Negotiation language:** [specific replacement text]

## Major findings (negotiate)
[same format]

## Minor findings (note)
[same format]

## Missing mandatory items
[list of protections that should appear but don't]

## Negotiating points memo (copy this to the employer)
1. Please update [clause] because [reason]
2. ...
```

### Step 5: Add Specific Negotiation Language

For each blocker and major finding, write a specific Hebrew or English replacement the employee can ask the employer to use. Do not just say "negotiate this" - give them the exact words.

### Step 6: Final Warnings

The disclaimer block at the TOP of the Step 4 template is mandatory and must appear above the summary, never only below it. Repeat it at the end as well:

```
DISCLAIMER
This is an automated review, not legal advice. For contracts with significant
blockers, or for senior / executive positions, consult an Israeli labour
attorney (orech din avoda) before signing. Sources: kolzchut.org.il,
nevo.co.il, Bituach Leumi official guidance.
```

## Examples

### Example 1: Section 14 waiver with a base-only salary definition

**Clause as written:** "The employee agrees to the arrangement under Section 14 of the Severance Pay Law. The employer's contributions to the pension fund, calculated on the base salary, replace severance pay in full."

**Finding:** Major. Section 14 needs the General Authorization or a collective agreement. The trap is "calculated on the base salary": the employee's role pays a 12,000 NIS base plus a recurring 4,000 NIS fixed travel-and-role allowance. Because the waiver covers only the base, the employee loses the severance value of the allowance, and on termination receives less than the statutory calculation would yield.

**Recommended replacement:** "The Section 14 arrangement applies to the employee's full salary, including all fixed components subject to pension contributions (base salary, fixed allowances, and any other regular fixed payment), and not to the base salary alone."

### Example 2: Advance notice set below the statutory minimum

**Clause as written:** "Either party may terminate this agreement by giving 7 days written notice."

**Finding:** Blocker. The contract is for a permanent role with no tenure cap. A flat 7-day notice is below the statutory minimum for any employee past the first 7 months: after one full year the minimum is 30 calendar days (see `references/hoda-at-mukdemet-table.md`). The clause is unenforceable against the employee, but it signals the employer is not drafting to Israeli law.

**Recommended replacement:** "Advance notice of termination, by either party, shall be the statutory minimum under the Prior Notice of Dismissal and Resignation Law, 5761-2001, by length of service: in the first six months, one day per month worked; in months seven to twelve, six days plus two and a half days for each month after the sixth; and from one year of service onward, 30 calendar days."

## Bundled Resources

### References

| File | Purpose |
|------|---------|
| `references/red-flag-checklist.md` | Full list of illegal, unfair, and missing clauses to scan for |
| `references/hoda-at-mukdemet-table.md` | Statutory advance notice days by tenure for monthly and hourly workers |
| `references/section-14-trap-guide.md` | Detailed explanation of the Saif 14 waiver, when it helps, and when it hurts |
| `references/standard-negotiation-language.md` | Ready-to-use Hebrew and English replacement clauses for common red flags |
| `references/notice-to-employee-disclosures.md` | Mandatory written-disclosure list under the Notice to Employee Law 2002 |
| `references/numerical-sanity-checks.md` | The numerical check table with current rates and ceilings |
| `references/high-value-clause-traps.md` | Lawful but expensive clauses: pension ceiling, Section 102 options, fixed term, severance forfeiture, seniority continuity, miluim |

### Scripts

| File | Purpose |
|------|---------|
| `scripts/contract_sanity_check.py` | Quick numerical validator for pension %, hoda'at mukdemet days, and vacation days |

## Recommended MCP Servers

| MCP | When to pair | Purpose |
|-----|--------------|---------|
| [kolzchut](https://agentskills.co.il/he/mcp/kolzchut) | For plain-language rule summaries and exceptions | Cross-references findings against the All-Rights database, including the rates that move every April and June |
| [knesset](https://agentskills.co.il/he/mcp/knesset) | For the current text and amendment history of a statute | Confirms which amendment of a labour statute is in force before you cite a section number |

The skill works without these MCPs using the built-in reference tables, but the citations become less specific. Whichever you use, spot-check a quoted rate against the live source before presenting it as current.

## Gotchas

1. **Mistaking "at-will" clauses for enforceable terms**. Agents trained on US corporate templates assume at-will is normal. In Israel, it is unenforceable but common in foreign-drafted contracts. Always flag it, even if the rest of the contract is fine.

2. **Telling the user a 2-year non-compete is enforceable**. Israeli courts apply the Frumer and Check Point v. Radguard precedent (Labour Court appeal 164/99) and rarely enforce non-competes beyond genuine trade-secret protection, which the employer must identify specifically and show it actually protected. Most 2-year non-competes are aspirational. Do not scare the user into refusing a good job over an unenforceable clause, but do flag it and recommend negotiation.

3. **Confusing Saif 14 with being a net positive**. Section 14 waivers CAN benefit the employee (monthly pension contributions instead of lump sum at termination) but ONLY if the "salary" definition for the waiver includes all compensation components. If it only covers base, the employee loses bonus-based severance. Always check the salary definition before endorsing the waiver.

4. **Ignoring keren hishtalmut absence for tech roles**. KH is not legally mandatory, but in Israeli tech it is universal and tax-advantaged. A tech contract without KH is a red flag even though it is "legal."

5. **Calculating hoda'at mukdemet in business days**. The law uses calendar days. A 30-day notice period means 30 actual days, including weekends and holidays. Agents sometimes quote business days, which is wrong.

6. **Accepting "discretionary bonus" at face value**. If the role was pitched with a 20% bonus component, a "fully discretionary" clause means the employer can pay zero forever. Flag this as major and suggest converting to a formulaic bonus tied to measurable KPIs.

7. **Getting the pension start date wrong for a first-job employee**. An employee who already had an active pension fund before this job gets contributions from day 1 (retroactively paid after 3 months of work). An employee with NO prior fund (a true first job) is only entitled to mandatory pension after 6 months. So a "pension after 6 months" clause is LEGAL for a first-job employee and must NOT be auto-flagged as a blocker. Only flag a waiting period as a blocker when the employee already had a prior fund (then it must be day 1).

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Kolzchut: Hoda'at Mukdemet law | https://www.kolzchut.org.il/he/הודעה_מוקדמת_לפיטורים | Statutory advance notice days by tenure |
| Nevo: Prior Notice Law full text | https://www.nevo.co.il/law_html/law00/71704.htm | Official legal text |
| Kolzchut: Overtime pay (gmul sha'ot nosafot) | https://www.kolzchut.org.il/he/גמול_עבור_שעות_נוספות | 125% / 150% overtime rates and the 42-hour extension order |
| Kolzchut: Section 14 of the Severance Pay Law | https://www.kolzchut.org.il/he/סעיף_14_לחוק_פיצויי_פיטורים | Section 14 waiver rules and 8.33% requirement |
| Kolzchut: Non-compete clauses after employment ends | https://www.kolzchut.org.il/he/איסור_הגבלת_עובד_לעבוד_אצל_מעסיק_אחר_לאחר_סיום_עבודתו_%28הסכם_אי_תחרות%29 | When a non-compete clause is enforceable |
| Bituach Leumi: For salaried workers rates | https://www.btl.gov.il/English%20Homepage/Insurance/Ratesandamount/Pages/forSalaried.aspx | National Insurance contribution rates |
| Kolzchut: Mandatory pension insurance for employees | https://www.kolzchut.org.il/he/חובת_ביטוח_פנסיוני_לעובדים | 18.5% total (6.5% + 6% + 6%) and the day-1 vs 6-month rule |
| Kolzchut: Dmei havra'a (convalescence pay) | https://www.kolzchut.org.il/he/דמי_הבראה | 451.5 NIS/day private-sector rate (updated 18.08.2026), 511.6 public, day count by seniority |
| Kolzchut: Minimum wage | https://www.kolzchut.org.il/he/שכר_מינימום | 6,443.85 monthly, 35.40/34.64 hourly |
| Kolzchut: Notice to Employee on employment conditions | https://www.kolzchut.org.il/he/הודעה_על_תנאי_העבודה | Mandatory written-disclosure list |
| Kolzchut: Deductions from wages | https://www.kolzchut.org.il/he/ניכויים_משכר_העובד | Section 25 closed list of lawful deductions and the 25% debt cap |
| Kolzchut: Dismissal of a pregnant employee | https://www.kolzchut.org.il/he/איסור_פיטורי_עובדת_בהיריון | Employment of Women Law permit (heter) requirement at 6+ months |
| Kolzchut: Payslip (tlush sachar) | https://www.kolzchut.org.il/he/תלוש_שכר | Detailed monthly payslip obligation (Amendment 24, 2008) |

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Review found 15 "blockers" in a standard contract | Over-flagging, probably labeling minor issues as blockers | Re-classify using strict severity: blocker = illegal, major = below market, minor = style |
| Contract is in Hebrew only, Hebrew quality is poor | Employer used a template translation | Flag as major: request a clean Hebrew or bilingual version |
| Salary quoted as "12,000 NIS" with no brutto/neto | Ambiguous | Ask user if they confirmed with employer. Flag as blocker to force clarity |
| Non-compete looks scary to user | User feels legally bound | Explain the Frumer and Check Point v. Radguard precedent (appeal 164/99): rarely enforced beyond a specifically identified trade secret. Still negotiate, but do not refuse the job over it alone |
| Section 14 clause without waiver text | Employer may be assuming it applies | Flag as major: require explicit Saif 14 language or clarify that standard severance applies |
| Contract is for a contractor (kablan), not employee | Different set of rules | Apply the subordination/integration test (mivchan ha'hishtalvut): fixed hours + subordination + integration + exclusivity point to an employee relationship that a court can reclassify retroactively. Flag the hallmarks you find and the reclassification exposure, then recommend a labor attorney for the borderline call |

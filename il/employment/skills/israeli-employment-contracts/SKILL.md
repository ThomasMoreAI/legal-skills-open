---
name: israeli-employment-contracts
title: Israeli Employment Contracts
description: Draft Israeli employment contracts (chozeh avoda) with all mandatory clauses per Israeli labor law. Use when user asks to create or generate an employment contract, calculate mandatory benefits for a contract, or asks about "chozeh avoda", "Section 14", "Saif 14", "Keren Hishtalmut", "Dmei Havra'a", "convalescence pay", "severance", "pitzuim", Israeli pension obligations, non-compete clauses in Israel, or Israeli employment compliance. Covers full-time, part-time, and contractor classification. Do NOT use for reviewing or auditing an existing contract (use israeli-employment-contract-reviewer), employee-rights questions (use israeli-workplace-rights-navigator), freelance service agreements, commercial contracts, or non-Israeli employment law.
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-employment-contracts
license: MIT
version: 0.1.2
execution_mode: open
jurisdiction: il
practice: employment
language: en
sources:
- title: Labor law
  path: references/labor-law.md
- title: Mandatory clauses
  path: references/mandatory-clauses.md
---

# Israeli Employment Contracts

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


## Instructions

### Step 1: Determine Employment Type

Ask the user what type of employment relationship they need to document:

| Type | Hebrew | Key Indicators | Contract Needed |
|------|--------|-----------------|-----------------|
| Full-time employee | avod mashara mlea | Fixed hours, employer control, tools provided | Full employment contract (chozeh avoda) |
| Part-time employee | avod mashara chelkit | Reduced hours, same rights pro-rata | Full contract with adjusted hours |
| Domestic/household worker | oved meshek bayit | Cleaner, nanny, or caregiver employed directly by a household | Full contract plus the domestic-worker clauses below |
| Contractor (atzmai) | kablan atzmai | True independence, multiple clients, own tools | Service agreement (NOT this skill) |

**Contractor misclassification warning:** Israeli courts apply a multi-factor test. If a worker has fixed hours, uses employer equipment, works exclusively for one company, and receives regular monthly payments, they are likely an employee regardless of what the contract states. Misclassification exposes the employer to retroactive benefits, severance, and penalties.

### Step 1b: Domestic and Household Workers (Oved Meshek Bayit)

A salaried cleaner, nanny, or caregiver employed directly by a household is a regular employee: "עובדות ועובדים במשק בית זכאים לכל הזכויות שמוענקות לעובדים שכירים". So the full contract in this skill applies (minimum wage, one-month-per-year severance, convalescence pay, pension, a Notice to Employee). Add these domestic-specific clauses on top:

- **The household is the employer for National Insurance.** A private household that employs a domestic worker must report the worker to Bituach Leumi and pay National Insurance and health contributions for them. This is what secures the worker's work-accident, maternity, and old-age rights. Reporting and payment go through the Bituach Leumi household-employer (meshek bayit) track: "המעסיק צריך לדווח על העובד באופן שוטף, ולשלם את דמי הביטוח עבורו ארבע פעמים בשנה". It has its OWN contribution rates (which depend on the worker's age and status) and is paid QUARTERLY, four times a year, on a household-employer voucher, not the monthly Form 126 route. The worker's own National-Insurance-and-health share is withheld from their wages and the household remits the combined sum. Do NOT apply Step 6's regular-employer rate here; look up the current household-track rate on the Bituach Leumi meshek-bayit rates page.
- **Log the hours; the burden is on the employer.** Domestic-worker hours are hard to reconstruct after the fact, and the law puts the burden of proving hours on the employer: "נטל ההוכחה לגבי מספר שעות העבודה שעבד העובד הוא על המעסיק". So a disputed, unrecorded hour is generally decided in the worker's favor. The contract should fix the weekly schedule and require a simple written or app-based hours log that both sides sign off on.
- **Weekly rest.** For a live-out worker on a fixed schedule, state the standard weekly rest of at least 36 consecutive hours that includes the worker's own day of rest. For a live-in caregiver, courts have recognized a shorter weekly rest of at least 25 hours, since the Hours of Work and Rest Law does not apply in full to a live-in care worker (see the overtime point below).
- **Live-in caregivers and overtime.** When the worker lives in the patient's home and their hours cannot be reasonably supervised, the Hours of Work and Rest Law's overtime provisions do not apply: "עובד שלא ניתן לפקח על שעות עבודתו באמצעים טכנולוגיים סבירים, אינו זכאי לגמול שעות נוספות". So a live-in caregiver's extra hours are handled by a fair global overtime payment (gmul globali) agreed in advance, not per-hour 125%/150% under Step 2, as long as the global sum is genuine and not a device to underpay. A live-OUT cleaner or nanny on a fixed schedule is fully under the Law and IS entitled to per-hour overtime.
- **Live-in vs live-out.** For a live-in worker, spell out the sleeping arrangement, privacy, and that lodging and meals provided in kind can count toward wage only within the limits the law allows, never as a way to drop cash pay below the minimum wage. For a live-out worker, cover travel-time and transport reimbursement.
- **Foreign caregivers are a different track.** If the worker is a FOREIGN caregiver (permit, licensed bureau, country-of-origin holidays, the reduced National Insurance rate, deposit fund), the payroll and permit mechanics live in the `foreign-caregiver-payroll` skill. This skill covers the CONTRACT for a salaried Israeli household worker; pair the two for a foreign caregiver.

### Step 2: Calculate Mandatory Benefits

All rates below are current as of 2025-2026. Verify rates annually as they may be updated by extension orders (Tzav Harchava).

**Minimum wage (Chok Schar Minimum, 1987):**
- As of 1 April 2026 the minimum wage is **6,443.85 NIS per month** for a full-time position and **35.40 NIS per hour**. The stated gross salary in any contract must meet or exceed this floor
- The minimum is updated every April (set at no less than 47.5% of the national average wage). Verify the current rate annually before finalizing a contract
- For part-time positions, the hourly minimum applies and the monthly figure is pro-rated

**Pension (mandatory per Tzav Harchava 2008):**

| Component | Employer | Employee | Notes |
|-----------|----------|----------|-------|
| Pension fund contribution | 6.5% of salary | 6% of salary | Mandatory from day 1 if the employee has prior pension coverage; otherwise after 6 months |
| Severance component (within pension) | 6% minimum; 8.33% (1/12) fully funds the month-per-year rate | -- | 8.33% comes from the General Authorization under Section 14, NOT from Section 14 itself. At 6% the fund covers about 72% of the statutory figure and the balance is still owed |
| Total employer cost | Up to 14.83% | -- | If Section 14 applies |

**Section 14 (Saif 14) arrangement:**
Section 14 is a PROHIBITION with exceptions, not a permission. It provides that a payment to a provident fund, pension fund or similar `לא יבוא במקום פיצויי פיטורים` UNLESS an applicable collective agreement so provides, or the Minister of Labour has approved it. In practice the route is the Minister's General Authorization (אישור כללי, י"פ תשנ"ח 4394), and the arrangement only replaces severance to the extent its conditions are met. When it applies:
- Employer deposits to pension fund count as severance payment
- Upon termination, employee receives the pension fund balance instead of calculated severance
- Employer is exempt from paying additional severance beyond what was deposited
- Must be documented explicitly in the contract with employee consent

**Statutory severance (Pitzuei Piturin, Severance Pay Law 1963):**
- Section 12 sets TWO rates, and which applies turns on how the wage is computed, not on hours worked. An `עובד במשכורת` (one whose pay is mainly computed on a monthly or longer basis) gets one month's last salary per year of employment with the same employer or workplace. An `עובד בשכר` (anyone else, i.e. paid on an hourly or daily basis) gets two weeks' pay per year. Section 12(ב) lets the Minister raise the rate for an `עובד בשכר` by regulation, and a collective or extension order may do so too, so check what applies before quoting the two-week figure. Both are pro-rated for partial years. For an hourly worker with fluctuating hours, the last salary is figured on the average position scope over the whole employment period
- Severance is normally owed on dismissal. Some resignations are also recognized as entitling the employee to severance: a move of residence (mostly for a spouse's relocation), poor health of the employee or a family member, a tangible worsening of employment terms by the employer, and resignation within the protected window after giving birth or adoption to care for the child
- When Section 14 applies, the monthly pension/insurance deposits stand in for this statutory severance for the salary and period they cover. When Section 14 does NOT apply, the employer still owes the full Section 12 calculation on termination

**Keren Hishtalmut (education fund):**

| Component | Rate | Tax Benefit Cap |
|-----------|------|-----------------|
| Employer contribution | 7.5% of salary | Tax-exempt up to ceiling (updated annually) |
| Employee contribution | 2.5% of salary | Deducted from gross salary |
| Vesting period | 6 years (3 years for designated purposes) | -- |

**Dmei Havra'a (convalescence pay):**

| Seniority | Days Per Year | Payment |
|-----------|---------------|---------|
| Year 1 | 5 days | Per-day rate x days |
| Years 2-3 | 6 days | Per-day rate x days |
| Years 4-10 | 7 days | Per-day rate x days |
| Years 11-15 | 8 days | Per-day rate x days |
| Years 16-19 | 9 days | Per-day rate x days |
| Year 20+ | 10 days | Per-day rate x days |

The per-day rate is updated by extension order. The private-sector rate for havra'a year 2026 (1.7.2025 to 30.6.2026) is **451.5 NIS per day**, raised from 418 by the extension order published on 18 August 2026. An employer who already paid at 418 owes the difference of 33.50 NIS for each havra'a day. The rate follows the havra'a year the payment is for, not the date it was paid.

**Annual leave (Chofsha) per Annual Leave Law:**

| Seniority | Minimum Days (5-day week) |
|-----------|---------------------------|
| Years 1-4 | 12 days |
| Year 5 | 16 days |
| Year 6 | 18 days |
| Year 7+ | 21 days |

Many employers offer more generous leave. These are statutory minimums.

**Sick leave (Machala):**
- Accrual: 1.5 days per month of employment (18 days per year)
- Maximum accumulation: 90 days
- Payment: Day 1 unpaid, days 2-3 at 50% salary, day 4 onward at 100% salary
- Requires a medical certificate as the employer reasonably specifies (commonly from the first day of absence)

**Notice periods:**

| Seniority | Monthly-paid employee | Daily/hourly-paid employee |
|-----------|----------------------|---------------------------|
| Months 1-6 | 1 day per month worked | 1 day per month worked (all 12 months) |
| Months 7-12 | 6 days + 2.5 days per month from month 7 | 1 day per month worked (all 12 months) |
| Year 2+ | 1 month | 1 month |

The two first-year columns differ. A monthly-paid employee earns 1 day per month for months 1-6, then 6 days plus 2.5 days for each month from month 7. A daily/hourly-paid employee (oved be'sachar) earns a flat 1 day of notice per month worked across the whole first year, reaching up to 12 days at year-end.

**Overtime (per Hours of Work and Rest Law):**
- Standard work week: 42 hours (since April 2018)
- Standard work day: 8.4 hours (for a 5-day work week) or 8 hours (for a 6-day work week)
- First 2 overtime hours: 125% of regular hourly rate
- Additional overtime hours: 150% of regular hourly rate
- Weekly rest: at least 36 consecutive hours (typically Friday-Saturday or Saturday)

**Travel allowance:**
- Common practice, not strictly mandatory by law for all employees
- Tax-exempt up to the published ceiling per month
- Typically covers public transport or per-kilometer rate

### Step 3: Generate Contract Clauses

Generate bilingual contract clauses covering all mandatory provisions. Use the script for automation:

```bash
python israeli-employment-contracts/scripts/generate_contract.py \
  --employee-name "Israel Israeli" \
  --position "Software Engineer" \
  --salary 25000 \
  --start-date 2026-04-01 \
  --work-percent 100
```

The contract must include these sections:

1. **Parties** -- Employer and employee full details, ID numbers
2. **Position and description** -- Title, responsibilities, reporting line
3. **Start date and probation** -- Tkufat Nisayon, commonly 6 months (no statutory requirement, but industry standard)
4. **Work hours** -- Daily/weekly hours, overtime policy
5. **Salary** -- Gross monthly amount, payment date (no later than the 9th of the following month per Protection of Wages Law)
6. **Pension and severance** -- Fund name, contribution rates, Section 14 election
7. **Keren Hishtalmut** -- Fund name, contribution rates, vesting terms
8. **Convalescence pay** -- Per seniority table, payment month
9. **Annual leave** -- Days per seniority, accrual rules
10. **Sick leave** -- Accrual rate, payment tiers, certificate requirements
11. **Notice period** -- Per seniority, mutual obligations
12. **Confidentiality** -- Scope, duration, reasonable limitations
13. **Intellectual Property** -- Assignment of work product to employer (critical for tech companies)
14. **Non-compete** -- See Step 4 for enforceability analysis
15. **General provisions** -- Governing law (Israeli law), jurisdiction (Israeli labor courts), entire agreement

See references/mandatory-clauses.md for exact bilingual clause templates.

### Step 4: Review Non-Compete and IP Sections

**Non-compete clauses in Israel -- very limited enforceability:**

Israeli courts consistently restrict non-compete clauses. The National Labor Court (particularly the Check Point ruling, ע"ע 164/99 Frumer and Check Point v. Radguard, and subsequent case law) established that non-compete is enforceable only when ALL of the following exist:

1. The employer has a legitimate interest to protect (genuine trade secrets, not just general know-how)
2. The restriction is reasonable in scope, geography, and duration
3. The employee received special consideration (training, equity, above-market compensation) beyond standard employment terms
4. The restriction does not unduly harm the employee's right to earn a livelihood (Chok Yesod: Kvod HaAdam VeHeruto -- Basic Law: Human Dignity and Liberty)

**Practical guidance:**
- Duration: Courts rarely enforce beyond 6-12 months
- Scope: Must be narrowly defined (specific competitors, specific field)
- Geography: Israel-wide restrictions are disfavored; global restrictions almost never enforced
- Recommendation: Use robust confidentiality clauses instead, which are far more enforceable

**Intellectual Property assignment:**
- Israeli law does not have automatic work-for-hire for all works (unlike US law)
- Patent Law Section 132: Inventions by employees generally belong to the employer if created in the course of employment, but employee may be entitled to compensation if the invention has special value
- Copyright: Works created in the scope of employment belong to the employer (Copyright Law 2007, Section 34)
- Explicit IP assignment clause is strongly recommended, especially for software and technology
- Consider including a pre-existing IP disclosure schedule

### Step 5: Compliance Checklist Before Signing

Run through this checklist before finalizing any employment contract:

- [ ] Written contract provided (mandatory per the Notice to Employee and Job Candidate (Employment Conditions and Screening and Hiring Procedures) Law, 5762-2002)
- [ ] All mandatory benefits included (pension, convalescence, leave, sick days)
- [ ] Section 14 arrangement documented with employee acknowledgment
- [ ] Keren Hishtalmut terms specified (if offered -- not mandatory but very standard in tech)
- [ ] Work hours and overtime policy clearly stated
- [ ] Notice period matches statutory minimum or better
- [ ] Salary meets or exceeds minimum wage (verify current rate)
- [ ] Payment date specified (by the 9th of following month)
- [ ] Non-compete clause reviewed for enforceability (see Step 4)
- [ ] IP assignment clause included (for tech roles)
- [ ] Probation period terms clear (if applicable)
- [ ] Contract language: Must be in a language the employee understands; bilingual (Hebrew + English) recommended

### Step 6: Post-Signing Obligations

After the contract is signed, the employer must complete:

1. **Bituach Leumi (National Insurance Institute) registration:**
   - Register new employee within 7 days of start date
   - Report via Form 126 (monthly payroll report)
   - Employer pays 4.51% (reduced rate, on the lower salary bracket) to 7.6% (full rate, on the higher bracket) in 2026, depending on salary

2. **Pension fund enrollment:**
   - Enroll employee in chosen pension fund
   - First contribution due by the first payroll
   - For employees with no prior pension: enrollment mandatory after 6 months (or immediately if employee had prior pension coverage)

3. **Tax Authority (Mas Hachnasa) reporting:**
   - Employee must submit Form 101 (employee tax declaration)
   - Employer responsible for income tax withholding per tax brackets
   - Report new employee to Tax Authority

4. **Provide written notification:**
   - Per the Notice to Employee and Job Candidate (Employment Conditions and Screening and Hiring Procedures) Law, 5762-2002 (formerly the Notification to Employee Law), the employer must provide written details of employment terms within 30 days of start

5. **Record keeping:**
   - Maintain attendance records (Hours of Work and Rest Law)
   - Keep payslip records for 7 years
   - Retain contract copy for duration of employment + 7 years

## Examples

### Example 1: Standard Tech Employee Contract
User says: "Create an employment contract for a senior developer, 30,000 NIS monthly salary, starting next month"
Actions:
1. Determine: Full-time employee, tech sector
2. Calculate: Pension 6.5%/6% (1,950/1,800 NIS), Keren Hishtalmut 7.5%/2.5% (2,250/750 NIS), 5 Dmei Havra'a days (first year)
3. Generate: Full contract with Section 14 arrangement, IP assignment, limited non-compete
4. Review: Flag non-compete for scope review, ensure IP clause covers software
5. Checklist: All 12 mandatory items verified
6. Post-signing: Bituach Leumi registration, pension enrollment, Form 101
Result: Complete bilingual employment contract ready for legal review and signing.

### Example 2: Part-Time Employee
User says: "I need a contract for a part-time marketing person, 3 days a week, 15,000 NIS"
Actions:
1. Determine: Part-time employee (60% position, mashara chelkit)
2. Calculate: All benefits pro-rata -- pension on 15,000, leave days proportional (60% of full entitlement)
3. Generate: Contract specifying 3 work days, which days, daily hours
4. Review: Ensure part-time rights clearly stated (same hourly benefits as full-time)
Result: Part-time contract with pro-rata benefits correctly calculated.

### Example 3: Drafting a Contract from an Existing Draft
User says: "Here is a rough offer letter, turn it into a full employment contract"
Actions:
1. Parse: Read the offer letter for the terms already agreed (role, salary, start date, work percentage)
2. Build: Generate the full contract using Step 3, filling every mandatory section the offer letter omitted (Section 14 election, pension fund, Keren Hishtalmut, convalescence, leave, sick days, notice period, IP assignment)
3. Calculate: Apply current benefit rates from Step 2, verifying the gross salary meets the minimum wage floor
4. Checklist: Run Step 5 to confirm all mandatory items are present
Result: A complete bilingual employment contract built from the partial draft, ready for legal review and signing. If the user instead wants an independent pre-signing audit of a contract someone else drafted, point them to the `israeli-employment-contract-reviewer` skill.

### Example 4: Contractor vs. Employee Assessment
User says: "I have someone working for me full-time from our office, should they be a contractor or employee?"
Actions:
1. Apply: Multi-factor test -- fixed location (employer's office), full-time hours, likely uses employer equipment
2. Assess: Strong indicators of employment relationship, high misclassification risk
3. Recommend: Classify as employee, provide employment contract
4. Warn: Misclassification liability includes retroactive benefits, severance, Bituach Leumi penalties
Result: Classification recommendation with risk analysis and next steps.

### Example 5: Salaried Nanny Employed by a Household
User says: "We are hiring a nanny 4 days a week, draft the employment contract"
Actions: Draft a full employment contract (minimum wage, pension, convalescence, one-month-per-year severance, a Notice to Employee), then add the domestic-worker clauses: register the household as an employer with Bituach Leumi on the meshek-bayit track and pay National Insurance for her, fix the weekly schedule with a signed hours log (the burden of proving hours is on the household), and state the 36-hour weekly rest. Note this is a local salaried worker, so foreign-caregiver permit and payroll rules do not apply.

## Bundled Resources

### Scripts
- `scripts/generate_contract.py` -- Generates an Israeli employment contract template with calculated benefit rates. Accepts employee details (name, position, salary, start date, work percentage) and outputs a structured contract with all mandatory Israeli clauses pre-filled. Includes Section 14 arrangement text, pension and Keren Hishtalmut rates, and notice period calculations. Run: `python scripts/generate_contract.py --help`

### References
- `references/labor-law.md` -- Comprehensive summary of Israeli labor laws governing employment contracts: Severance Pay Law (1963), Annual Leave Law (1951), Sick Pay Law (1976), Hours of Work and Rest Law (1951), the Notice to Employee and Job Candidate (Employment Conditions and Screening and Hiring Procedures) Law, 5762-2002, Protection of Wages Law (1958), and key extension orders (Tzav Harchava). Consult when verifying statutory requirements or resolving disputes about employee entitlements.
- `references/mandatory-clauses.md` -- Bilingual (Hebrew and English) employment contract clause templates covering all mandatory provisions: parties, position, salary, pension with Section 14, Keren Hishtalmut, convalescence pay, leave, sick days, notice period, confidentiality, IP assignment, and non-compete. Consult when drafting or reviewing specific contract sections.

## Gotchas

- Israeli non-compete clauses are nearly unenforceable unless very narrowly scoped. Agents trained on US employment law will draft broad non-competes that Israeli courts routinely strike down. Always prefer robust confidentiality clauses instead.
- Section 14 (Saif 14) of the Severance Pay Law is Israel-specific and has no equivalent in US or European law. Agents unfamiliar with it will omit this critical clause, leaving employers exposed to double severance liability.
- The mandatory pension contribution rates (employer 6.5%, employee 6%) are set by extension order and change periodically. Agents may use outdated rates from their training data. Always verify against the current Tzav Harchava.
- Israeli law does not recognize automatic "work-for-hire" for all intellectual property as US law does. Agents drafting contracts without an explicit IP assignment clause will leave IP ownership ambiguous, especially for software.
- The convalescence pay (Dmei Havra'a) rate for havra'a year 2026 is 451.5 NIS/day, raised from 418 by the extension order of 18 August 2026. An employer who paid at 418 owes 33.50 NIS per havra'a day.
- Section 14 only covers severance for the period from the date the written consent is signed. If it is activated mid-employment, the years worked before signing still owe a full severance top-up; do not present a mid-tenure Section 14 signature as wiping out prior-year severance liability.

## Troubleshooting

### Error: "Missing mandatory clause"
Cause: Contract is missing one or more legally required provisions (pension, convalescence, leave, etc.)
Solution: Run through the compliance checklist in Step 5. Add missing clauses using templates from references/mandatory-clauses.md.

### Error: "Non-compete clause too broad"
Cause: Non-compete exceeds enforceable scope under Israeli case law
Solution: Narrow to 6-12 months duration, specific competitors only, limited geography. Consider replacing with a stronger confidentiality clause per Step 4 guidance.

### Error: "Section 14 not properly documented"
Cause: Section 14 arrangement requires explicit employee acknowledgment and specific fund designation
Solution: Include the full Section 14 clause with employee signature line and pension fund details. See references/mandatory-clauses.md for template.

### Error: "Salary below minimum wage"
Cause: Stated salary falls below the current Israeli minimum wage
Solution: Verify current minimum wage rate (updated periodically by government order). For part-time employees, calculate the hourly equivalent to ensure compliance.

### Error: "Missing Bituach Leumi registration"
Cause: Employer did not register employee with National Insurance within required timeframe
Solution: Register immediately via the Bituach Leumi employer portal. Late registration may incur penalties and leaves the employee without coverage.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Kol Zchut: personal employment contract | https://www.kolzchut.org.il/he/%D7%97%D7%95%D7%96%D7%94_%D7%A2%D7%91%D7%95%D7%93%D7%94_%D7%90%D7%99%D7%A9%D7%99 | Plain-language explanation of contract terms and mandatory clauses |
| Kol Zchut: employment and workers' rights portal | https://www.kolzchut.org.il/he/תעסוקה_וזכויות_עובדים | Employment rights hub: wage components, terms, sickness, leave, end of employment |
| Nevo: Notice to Employee Law full text | https://www.nevo.co.il/law_html/law00/71702.htm | Notice to Employee and Job Candidate Law, 5762-2002 statutory text |
| Kol Zchut: Severance Pay (Pitzuei Piturin) | https://www.kolzchut.org.il/he/פיצויי_פיטורים | Severance Pay Law, 1963 explained (Section 14, calculation, payment deadline) |
| Bituach Leumi: employer registration | https://www.btl.gov.il/Insurance/Maasik/MToshavYisrael/Pages/PtichatTik.aspx | Opening an employer deductions file with National Insurance |
| Bituach Leumi: reporting a domestic worker | https://www.btl.gov.il/Insurance/National%20Insurance/type_list/House_keeper/Pages/divuachVetashlum.aspx | Household-employer (meshek bayit) reporting and payment track for a domestic worker |
| Kol Zchut: domestic workers' rights | https://www.kolzchut.org.il/he/זכותון_עובדים_במשק_בית_%28עוזרות_בית_ומטפלים/ות%29 | Rights of cleaners, nannies, and caregivers; employer duty to report to Bituach Leumi |
| Kol Zchut: Form 101 | https://www.kolzchut.org.il/he/טופס_101 | Employee tax declaration form (kartis oved) for new hires |

## Recommended MCP Servers

| MCP | When to pair | Purpose |
|-----|--------------|---------|
| `israel-law` | For authoritative citations to statute text | Looks up the exact text of the Severance Pay Law, Annual Leave Law, Hours of Work and Rest Law, and the Notice to Employee Law |
| `kolzchut` | For plain-language rule summaries and exceptions | Cross-references contract clauses against the All-Rights (Kol Zchut) database |

The skill works without these MCPs using the built-in reference tables, but the citations become less specific.

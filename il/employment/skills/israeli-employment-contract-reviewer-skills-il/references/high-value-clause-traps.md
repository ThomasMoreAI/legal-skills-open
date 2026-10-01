# High-value clause traps (lawful but expensive)

The red-flag checklist is built around clauses that are illegal or below market. This file
covers the other category: terms that are perfectly lawful and still cost the employee more
than any illegal clause in the same contract. A pre-signing review that only hunts for
illegality will pass every one of them.

## 1. The pension salary ceiling

The Mandatory Pension Expansion Order compels contributions only on the **lower** of the
employee's base gross salary or the **average wage in the economy**, which is **13,769 NIS per
month as of January 2026**. Above that ceiling there is no statutory duty at all; anything more
is purely contractual.

So a clause reading "pension in accordance with law" or "as required by the Expansion Order" on
a salary above the ceiling lawfully funds only the part up to it. Every shekel above the ceiling
carries no statutory contribution at all, and the gap silently shrinks the severance component
too.

**What to check:** does the contract state the base the percentages apply to? **What to ask
for:** "contributions shall be computed on the employee's full gross salary, with no ceiling."

Note also that contributions are computed on base salary excluding overtime, and that fixed
supplements do enter the base while conditional payments do not.

## 2. Section 102 option and RSU grants

For an Israeli tech employee the equity grant is frequently worth more than a year of salary,
and the terms that decide its value usually sit outside the employment contract in a plan
document the candidate never sees before signing.

- **Which Section 102 route.** The capital-gains track with a trustee taxes the gain at a flat
  25%. Outside that track the gain is ordinary employment income at marginal rates. A contract
  silent on the route is a major finding, not a footnote.
- **The trustee must hold the options, or the shares issued on their exercise, for a blocking
  period of at least two years.** Sources differ on whether that clock runs from the allocation
  date or from the end of the tax year of allocation, so confirm the plan's own wording. A
  disposal inside the blocking period collapses the capital track.
- **The plan and the trustee arrangement must be in place before the grant.** Ask the employer
  which route the plan uses and when it was filed rather than assuming it qualifies.
- **The post-termination exercise window**, typically 90 days, is the single clause that most
  often destroys a grant entirely: an employee who cannot fund the strike price in 90 days walks
  away with nothing.
- **Good-leaver and bad-leaver definitions**, and whether unvested options are forfeited on
  resignation.
- **Acceleration on change of control**, single trigger or double trigger, and whether unvested
  options are simply cancelled in an acquisition.
- **Whether the grant is a fixed number or a percentage**, and whether it is protected against
  dilution.

## 3. Fixed-term contracts and Section 9 of the Severance Pay Law

- Expiry of a fixed term without renewal is **deemed dismissal** under Section 9 and triggers
  severance.
- If the employer offers renewal on the same or better terms and the employee refuses,
  Section 9(b) treats it as **resignation**.
- Section 3 presumes that dismissal shortly before the end of the first year was done to avoid
  severance. An 11-month term is exactly that pattern.
- An employer that ends a fixed term early owes the balance of the term as damages unless the
  contract contains an early-exit clause. The absence of a **mutual** exit clause cuts both ways
  and is worth negotiating.

## 4. Severance forfeiture and clawback

Severance may be denied or reduced only under Sections 16 to 17 of the Severance Pay Law, and
only by a labour court. The General Authorization under Section 14 additionally requires the
employer to **waive in advance** any right to recover the accumulated funds, except in Sections
16 to 17 circumstances or on a withdrawal other than death, disability, or retirement at 60 or
over. A clause claiming a broader employer recovery right is void, and sitting next to a Section
14 clause it can call the validity of the waiver itself into question.

## 5. Seniority continuity on a change of employer

Watch for a clause that terminates employment on a sale, merger, or intra-group transfer and
re-hires the employee as a new starter. That resets seniority for severance, advance notice,
vacation, and havra'a simultaneously. Ask for express continuity of seniority for all purposes.

## 6. Miluim

Section 41A of the Discharged Soldiers (Return to Work) Law prohibits dismissal because of
reserve service, and dismissal during service or within 30 days of its end requires a permit
from the employment committee where the service passed the statutory threshold. Reserve pay is
routed through the employer, who is reimbursed by Bituach Leumi. Ask for pension accrual to
continue during service, and reject any clause treating reserve absence as unpaid leave or as a
performance factor.

## 7. What actually enters the severance base

Where the contract does NOT use Section 14, the whole severance value turns on which pay
components enter the determining wage (`mashkoret kovaat`). Section 13 of the Severance Pay Law
leaves that list to regulation, and it is set by the Severance Pay (Calculation of Compensation)
Regulations 5724-1964. The components generally recognised as entering it are base wage,
seniority increment, cost-of-living increment, family increment and departmental or professional
increment; bonuses, overtime and expense reimbursements generally do not. Confirm the current
list against the regulations before quoting it to a user, since the answer decides the whole
severance figure.

This matters for reading a Section 14 clause. Negotiating the waiver's "salary" definition to
include recurring bonuses puts the employee **above** the statutory baseline, not back at it.
A fixed allowance is the case where a base-only definition genuinely costs the employee money.

## 8. The Section 30(a)(5) "position of special trust" recital

A clause reciting that the role is one of management or requires a special degree of personal
trust, and that the Hours of Work and Rest Law therefore does not apply, is the companion trap
to global overtime. Section 30(a)(5) is read narrowly: it needs genuine autonomy over one's own
hours, no attendance reporting, and seniority and pay commensurate with management. An employer
that requires the employee to clock in has usually defeated its own defence. The recital in the
contract does not bind a court, so flag it and check the attendance-reporting clause.

## Sources

| Source | URL |
|--------|-----|
| Kolzchut: Mandatory pension insurance for employees (ceiling and rates) | https://www.kolzchut.org.il/he/חובת_ביטוח_פנסיוני_לעובדים |
| Nevo: Hours of Work and Rest Law 5711-1951 (sections 2, 3, 16, 30) | https://www.nevo.co.il/law_html/law00/5174.htm |
| Kolzchut: Section 14 of the Severance Pay Law | https://www.kolzchut.org.il/he/סעיף_14_לחוק_פיצויי_פיטורים |
| Kolzchut: Non-compete clauses after employment ends | https://www.kolzchut.org.il/he/איסור_הגבלת_עובד_לעבוד_אצל_מעסיק_אחר_לאחר_סיום_עבודתו_%28הסכם_אי_תחרות%29 |

---

## Detection rows (moved out of SKILL.md for length)

Each row is `Red flag | Why it is a problem | Action`.

| Red flag | Why it is a problem | Action |
|----------|--------------------|---------|
| "Pension contributions in accordance with law / the Expansion Order", with no salary base stated | The Expansion Order compels contributions only on the LOWER of base gross or the average wage in the economy (13,769 NIS per month in 2026). On a salary well above that ceiling a "per law" clause lawfully funds only the part up to it, and the employee usually discovers this years later | Major, and among the most expensive silent terms in an Israeli tech contract. Require "contributions computed on full gross salary with no ceiling" |
| "The employee's position is one of management or requires a special degree of personal trust, therefore the Hours of Work and Rest Law shall not apply" | Recites section 30(a)(5), the companion trap to global overtime. Read narrowly: it needs genuine autonomy over one's hours and no time reporting, and the recital does not bind a court | Major. Flag it, and check whether the contract elsewhere requires attendance reporting |
| Fixed-term contract with no early-exit clause, or a term ending just short of 12 months | Severance Pay Law section 9 deems non-renewal a dismissal that triggers severance; section 3 presumes dismissal shortly before the first year was severance avoidance. Early employer termination owes the balance of the term unless an exit clause exists | Major. An 11-month term is the classic avoidance pattern |
| "The employer may recover or retain the severance component on dismissal in circumstances not entitling the employee to severance" | Severance is denied or reduced only under sections 16 to 17, and only by a labour court. The Section 14 General Authorization also requires the employer to waive recovery IN ADVANCE | Blocker. Void, and next to a Section 14 clause it can defeat the waiver itself |
| Clause terminating employment on a sale, merger or intra-group transfer and re-hiring the employee as a new starter | Resets seniority for severance, notice, vacation and havra'a. Israeli law treats continuity across a change of employer as substantive | Major. Require express continuity of seniority on any transfer or change of control |
| "The employer may vary the role, terms, reporting line or place of work at its discretion" | It cannot authorise a unilateral pay cut, and a material worsening lets the employee resign WITH severance under section 11(a) | Major. Carve out pay, scope and location, and preserve the section 11(a) right expressly |
| Contract silent on miluim, or treating reserve absence as unpaid leave or a performance factor | Section 41A of the Discharged Soldiers (Return to Work) Law bars dismissal because of reserve service, and dismissal during service or within 30 days of its end needs a permit from the employment committee | Blocker for a penalising clause, major for silence. Require pension accrual to continue during service |
| Option or RSU grant with no stated Section 102 route, no post-termination exercise window and no acceleration terms | The grant is often worth more than a year of salary. The trustee capital-gains track taxes the gain at 25% and needs a two-year trustee holding period; outside it the gain is ordinary income at marginal rates. A 90-day exercise window is what most often destroys a grant entirely | Major. Name the 102 route, state the window, spell out acceleration. See `references/high-value-clause-traps.md` |
| "The employee shall use accrued vacation during the notice period", or an advance-notice clause silent on garden leave | The employer may not force the employee to consume accrued leave during the notice period unless it does so in good faith and for genuine operational reasons, and at least 14 days of the notice period must fall outside vacation. Separately, the employer may waive actual work and pay `chalef hoda'a mukdemet` instead, which ends the relationship immediately. Section 4A of the Sick Pay Law also bars dismissal during an employee's accrued sick-pay entitlement, subject to the exceptions in s.4A(b) | Major. Strike the forced-vacation clause or cap it so at least 14 notice days stay outside leave, and make the garden-leave option explicit and symmetrical |
| Clause permitting "immediate dismissal without notice or hearing", or defining cause so broadly that every dismissal becomes one | The right to a hearing (`shimua`) is a good-faith duty applied to private employers and cannot be waived in advance | Major. Strike the waiver and require a hearing before any dismissal decision |
| Keren hishtalmut stated as a percentage of full salary with no ceiling | Employer contributions above the tax-exempt salary ceiling (15,712 NIS per month in 2026) are taxed to the employee in the month of deposit | Minor to major by salary. Cap at the ceiling or state who bears the tax above it |

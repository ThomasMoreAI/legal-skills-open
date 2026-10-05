---
name: israeli-attendance-wage-checker-skills-il
title: Israeli Payslip and Wage Checker
description: Not legal advice. Audits an Israeli payslip and timesheet and itemises what is owed against what was paid. Checks the payslip carries the components the law requires, converts clock-in and clock- out spans into working hours, splits them into ordinary, overtime and weekly-rest hours, and applies the statutory premiums. Works even when the payslip is the only document, because missing components raise a presumption of an unlawful inclusive wage. Use when a user asks whether their payslip is correct, whether overtime or Shabbat was paid correctly, how to compute shaot nosafot, or what to do when the employer kept no hours record. It matters because the premium tiers reset daily rather than monthly and the premium base includes every supplement. Do NOT use for gross-to- net, tax or National Insurance deductions (use israeli-payroll-calculator), for severance, notice pay or annual leave, to draft a claim or an employment contract, or for teacher or foreign- caregiver payroll.
author: skills-il
author_url: https://github.com/skills-il/accounting/tree/master/israeli-attendance-wage-checker
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: employment
language: en
sources:
- title: Domain Checklist
  path: references/domain-checklist.md
- title: Rates And Tiers
  path: references/rates-and-tiers.md
- title: Records And Remedies
  path: references/records-and-remedies.md
---

# Israeli Payslip and Wage Checker

## Legal notice

This is a free information tool operated by an AI model. It explains the law and computes an indicative figure from the hours you supply. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion. It is a general explanation and an arithmetic estimate only: it does not read your employment contract, does not know which collective agreement or extension order applies to your workplace, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion. Where a payslip is the only document, the tool checks only what appears on the face of it: it has not seen the hours ledger, does not know whether the employer can rebut the presumption, and does not decide whether the applicability exclusion applies to you.

The binding computation is the one your employer is obliged to make under the law and any applicable collective agreement, and a labour court decides any dispute about it. Any figure this tool produces is a draft for your personal preparation only, it is not a document prepared by an advocate, and it must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person, and before filing anything you should consult a licensed advocate. All use of the output is the user's sole responsibility.

## Problem

An Israeli payslip shows hours and shekels, and almost nobody can tell whether the second follows from the first. The premium tiers reset every day, so a worker can be owed overtime in a week of exactly the standard hours. The statutory week and the operative week differ. Some breaks stay in the count. And the most valuable rule is procedural: an employer who kept no hours ledger carries the burden of proving the disputed hours were not worked, up to a cap. This skill reconciles a timesheet, or audits a payslip on its own terms.

## Problem boundary

This skill starts from HOURS or from a PAYSLIP and stops at GROSS owed. It audits the earnings side of a payslip: the hours line, the value of a regular hour, and the premium components. It does **not** audit the deductions side. Income tax, National Insurance, health tax, pension and net pay are `israeli-payroll-calculator`, and a user who asks "is my net right?" should be handed off rather than answered here. It does not handle severance, notice pay, or end-of-employment settlements, and it does not compute annual leave, recuperation pay, or travel as standalone entitlements, though it flags them where they trigger a statutory presumption. It does not draft a claim or assess its merits. Teacher payroll and foreign-caregiver payroll have their own dedicated skills; do not reimplement them here.

## Instructions

Read `references/rates-and-tiers.md` before computing any figure and `references/records-and-remedies.md` before answering anything about missing records, payslips, or late payment.

**Route on the document the user has, not on the one you would prefer.** Most people arrive holding a payslip and nothing else, so treat that as the normal case rather than the degraded one:

| What the user has | Where to go |
|---|---|
| A payslip only | Step 0, then Step 1, then **Step 1b**. Step 1b can produce a finding on its own. |
| A payslip and a timesheet | Step 0 through Step 6, using Step 1b to check the payslip states what it must. |
| A timesheet only | Step 0 through Step 6. Ask for the payslip, because without it there is nothing to compare owed against. |
| Neither | Step 0, then Step 7. The absence of records is the finding. |

### Step 0, the applicability gate, run this first and every time

The Hours of Work and Rest Law does not apply to everyone. It expressly excludes police and prison service, state employees required to be available outside regular hours, seafarers and fishermen, air crew, **employees in management roles or in roles requiring a special degree of personal trust**, and employees whose work conditions prevent the employer from exercising any supervision over their hours.

If the worker falls in one of these classes, **no overtime and no weekly-rest premium is owed at all**, and every figure this skill would produce is legally meaningless. Ask before computing.

Two things about that gate matter more than the list itself, and most write-ups omit both:

- **The exclusion is the employer's to prove, and it is construed narrowly.** It is a defence, not the default. A worker is inside the law unless the employer establishes otherwise, so an agent that treats "you were a manager" as settled has silently decided the case against the user.
- **It turns on what the person actually did, not on a job title.** A "manager" with no subordinates, no discretion over budget or hiring, and a clocked-in schedule is very unlikely to fall inside it. Where it is arguable, say it is arguable, compute the figure as a conditional, and name what evidence would settle it (an org chart, signing authority, whether the person clocked in).

### Step 1, establish the basis before touching the numbers

1. **Pay basis**: monthly salaried, or hourly/daily. This changes the rest-day answer completely, see Step 4.
2. **Which week applies.** The statute says a work week shall not exceed **45 hours**. The practical basis in the economy has been **42 hours** since the 2018 extension order, implemented by shortening one defined day rather than by trimming every day. Public bodies that joined the later framework agreement moved to 40. Ask which applies, and for which period, because a user reconciling an older payslip needs the basis that applied then.
3. **The daily maximum did not change.** It is still **8 hours**, and **7 hours** on night work, on the day before the weekly rest, and on the day before a holiday the employee does not work. The 2018 order moved only the weekly basis.
4. **Five or six day week**, and which day is the shortened one.
5. **The period being reconciled**, and whether a payslip exists for it.
6. **The hourly rate itself, where the wage is global.** A monthly wage does not state an hourly rate, and every premium in this skill is a multiple of one. For a full-time post under the 2018 extension order the divisor is **182**, not 186, whatever basis the payslip prints, unless the post was already 42 hours a week or less (`references/rates-and-tiers.md` section 8). State the divisor you used.
7. **Check the wage against the minimum-wage floor before anything else.** From 01.04.2026 it is 6,443.85 a month or 35.4 an hour on the 182 basis; use the dated row for the audited period in `references/rates-and-tiers.md` section 8, never a remembered figure. Two traps: the test uses a **narrower base** than the premium base (`סעיף 3(ב)` of חוק שכר מינימום excludes shift, seniority and family supplements, any premium including a fixed one, the 13th salary, annual grants and expense refunds), and it prorates for part-time work, absence and a partial month. A shortfall is its own claim, and the premium base is then rebuilt as the lifted wage **plus** the excluded wage supplements (shift, seniority, family; not refunds or annual pay), never the larger of the minimum and the existing rate; the section has a worked example.
8. **Tips.** In service sectors, whether tips form part of the wage, and on what basis they were recorded, changes the base every premium multiplies. Establish it rather than assuming the payslip's base line is the whole wage.
9. **Absences and holidays in the period.** Reserve-duty (מילואים), sick, leave and holiday days are not hours worked: take them out before Step 4. The statute does not reduce the weekly bound for them, but an agreement or practice may be more generous, so ask. The reserve-duty payment is its own payslip line, computed by Bituach Leumi from the three months **before** the service, so never check it against this month's hours. List holiday eves too, where the daily bound drops to 7. `references/records-and-remedies.md` section 8 has the detail and the hand-offs.

### Step 1b, audit the payslip itself, and what to do when it is the only document

A payslip is not merely a record of a decision already made. The law prescribes its contents, so it can be audited on its own terms with no timesheet beside it.

**First, check the components are present.** The Schedule to חוק הגנת השכר, via `סעיף 24`, requires the payslip to state, among other things:

| Component | What to look for | If absent |
|---|---|---|
| Hours actually worked in the period | A real hours figure, not a nominal 182 or 186 | Breach, and a presumption trigger |
| Nominal hours at the workplace, and היקף משרה | The basis and the position scope. Check 1 cannot run without both | Breach. Ask before computing |
| Value of a regular work hour | An explicit shekel-per-hour line | Breach. Without it the user cannot check any premium |
| The regular wage | The base the premiums multiply | Breach |
| Overtime and weekly-rest premium, itemised | **Units and amount**, not a lump "supplements" line | Breach, and a presumption trigger |
| Leave balance, הבראה, נסיעות | Named lines or balances | Breach, and a presumption trigger. Hand the valuation off |

An express note is also required where the supervision exclusion applies to the employee. Read any such note against Step 0 rather than accepting it: it records the employer's position on the gate, not a finding.

**Second, check the payslip against itself.** Three arithmetic checks need no timesheet at all. Before running any of them, establish **what the wage line already contains**, because two lawful conventions differ: either it covers ordinary hours only and the overtime line carries the full 125 or 150 percent, or it already carries the 100 percent element of every hour worked and the overtime line carries only the supplement, 25 or 50 percent. Nearly every false finding comes from assuming one convention on a payslip drawn on the other.

1. **Gate this on the convention, the pay basis, and the position scope.** For an hourly or daily paid employee the test turns on which convention the payslip uses. On the **supplement-only** convention the wage line already values every hour worked at 100 percent, so all hours times the value of a regular hour **equals** the wage line lawfully; that equality is expected, not a defect, and the premium sits wholly in the line check 2 reads. On the **full-rate** convention the wage line covers ordinary hours alone, so where the hours figure is all hours worked the product must **exceed** it by the overtime hours times the hourly value, and an exact match is the defect. Either way reconcile the residual rather than expecting a match: רטרו, השלמה לשכר מינימום, shift differentials, הבראה, נסיעות, a 13th salary, paid leave or sick hours, and a reserve-duty line each move one side lawfully, and equivalent-unit booking makes the count unreadable. For a **monthly-salaried** employee the test does not apply at all: the base is fixed and does not move with the hours worked. Check instead that the value of a regular hour equals the **full-time** base, never the paid base, divided by 182 for a full-time post under the 2018 order even where the payslip prints 186 (exceptions in `references/rates-and-tiers.md` section 8). The paid base is wrong because משרה חלקית, mid-month start or termination and unpaid absence all prorate it while the hourly value stays contractual. A higher value because fixed supplements were folded in is not a defect. Allow two agorot for rounding, and more where a mid-month raise makes the full-time base ambiguous.
2. Divide the stated overtime amount by the stated units, then read the quotient against the convention you established. On the full-rate convention, separate 125 and 150 lines each compare against the hourly value, a **single combined line** blends the tiers and lands between them, and a quotient at or near 100 percent means the premium was never applied. On the **supplement-only** convention the lawful quotients are 25 and 50 percent. Whatever the convention, a **monthly-salaried** weekly-rest line at 50 percent is what Step 4 requires; reading it as an unpaid premium inverts the finding. And a clean quotient proves nothing if the stated hourly value leaves out supplements paid on other lines: confirm the value carries them first. Where the units are equivalent units, or a שעות גלובליות line carries a nominal count, the quotient means nothing and Step 7b is the route.
3. Do **not** read a monthly hours total above the nominal basis as overtime. The basis is an average divisor, not a monthly cap, and a month with more working days lawfully produces more ordinary hours. A high hours line with zero overtime units is a question, not a finding: the daily and weekly split has to be seen. Nor is a total **below** the basis a finding: part-time, mid-month start, unpaid absence and a paid absence such as reserve duty, sick days or leave each produce one lawfully. Ask for the daily breakdown; if the employer has none, that absence is the Step 7 point.

A payslip failing any of these carries a finding before a single attendance record is produced.

**Third, and this is what makes a payslip-only case workable.** Where the disputed causes are non-payment of overtime premium, weekly-rest premium, leave pay, leave redemption, recuperation pay or travel, and the employer obliged to give a payslip gave none or gave one omitting those components, `סעיף 26ב(ג)` of חוק הגנת השכר raises a **presumption** that an unlawful inclusive wage was set contrary to `סעיף 5`, and the wage paid is treated as regular wage **exclusive of those components** unless the employer proves otherwise.

Three things are easy to overstate. It is **rebuttable**, so report it as a presumption that shifts the argument and never as a decided entitlement. It attaches to the **enumerated causes only**, and is not a general "bad payslip means you win" rule. Leave, recuperation and travel appear as **triggers, not entitlements this skill prices**: name them and hand the valuation off.

Its practical effect is large: the base is re-derived from the paid wage as regular wage and the premiums computed on top, rather than treated as already included. That is the Step 7b re-characterisation reached by another route, so never apply both to the same sum.

**When the payslip is genuinely all there is**, output the component breaches, the consistency findings, the presumption, the user's own factual version of the hours (Step 7 requires one), and a bounded range rather than a confident number. A timesheet or badge log would turn the range into a figure.

### Step 2, convert the raw spans into working hours

Working hours are the time the employee stands at the employer's disposal, including short agreed rest breaks and toilet breaks, and **excluding** the statutory meal break.

- A day of six hours or more carries a break of at least three quarters of an hour, including one continuous half hour. Deduct only a break actually given, unless Step 3 makes it paid. A fixed break the attendance system deducts automatically, rounding against the worker, or planned shift hours printed in place of punched ones are questions to ask, not hours to accept.
- On the day before the weekly rest or a holiday the break is at least half an hour.
- Night work is any work with at least two hours falling between 22:00 and 06:00.

### Step 3, decide which breaks are paid

A break of half an hour or more counts as **part of working hours** where the employee's presence at the workplace was necessary to the work process or to the operation of equipment and the employer required him to stay. A shop assistant told to eat behind the counter is on paid time; a worker free to leave is not. Ask which it was rather than assuming, because it is often the largest single line in the reconciliation.

### Step 4, split the hours and apply the premiums

**Order matters. Compute daily first, then weekly, and never from a monthly total.** Overtime is defined against the daily bound and against the weekly bound independently, so a worker can be owed overtime in a week that totals exactly the standard hours.

| Hours | Rate |
|---|---|
| Ordinary, within the daily and weekly bounds | 100 percent |
| First two overtime hours **of that day** | 125 percent |
| Third overtime hour of that day onward | 150 percent |
| Weekly rest | 150 percent |
| Work on a holiday | Set by extension order or agreement, not by `סעיף 17`. Check which applies |

Three things that change the answer:

- **The two-hour tier resets every day.** It is not a monthly allowance. An agent that applies it once per month understates the claim badly.
- **The base is not bare salary.** For these two sections, "regular wage" includes **all the supplements the employer pays**. Computing 125 percent off base pay while ignoring supplements is the most common way a shortfall is created.
- **Rest day depends on pay basis.** A monthly-salaried employee is already paid for the day, so the marginal entitlement is the premium element on top, plus paid compensating rest. An hourly or daily paid employee is entitled to the full 150 percent, and the compensating rest is treated as unpaid unless an agreement says otherwise. Note the paid/unpaid split is labour-court practice, not statutory text, so present it as practice. `references/rates-and-tiers.md` works both through.

The weekly rest is at least **36 continuous hours**, which is what decides whether a Saturday-night shift is still inside it.

### Step 5, flag the compliance breaches separately from the money

Hours beyond the permitted caps are still owed their premium, but the illegality is a separate finding and should be reported separately rather than folded into the money. Flag at least: a gap of less than **8 hours** between one working day and the next; a day exceeding the overtime caps; and night-shift patterns beyond what is permitted. Report these as "this may be unlawful, here is the provision", not as an entitlement.

### Step 6, produce the reconciliation

Show owed against paid, per period, with the gap itemised by cause. If you can run scripts, `scripts/reconcile_hours.py` does the daily-then-weekly split and the tiering. If you cannot, do it inline: for each day, hours worked minus break, compare to the daily bound, tier the excess 2 then rest; then sum the ordinary hours across the week and tier anything above the weekly bound; then value each bucket against the regular wage **including supplements**.

**Overtime inside the weekly rest is not checked.** Hours past the daily bound on the rest day are owed the overtime premium on top of the rest-day premium, cumulatively (`references/rates-and-tiers.md` section 4). Neither the script nor this skill prices it; call the figure a floor.

Never present the output as a figure the employer owes as a matter of decided law. It is what the statutory rates produce on the hours supplied.

### Step 7, when there is no hours record

This is the highest-value part of the skill and it is procedural.

The employer must keep a ledger of work hours, weekly rest hours, overtime and the premiums. Where the hours are in dispute in an employee's claim, **the burden of proof is on the employer** to show the employee was not at his disposal during the disputed hours, if the employer did not produce attendance records from that ledger.

Two limits that most write-ups omit, and that the skill must state:

- The burden applies only up to **15 weekly overtime hours or 60 monthly overtime hours**. It is not unlimited.
- The employee still has to put forward a minimal factual version of what he worked. The shift is not a substitute for saying anything.

**Do not let the cap shape what the user claims.** The 15/60 figure limits how far the evidentiary presumption carries, not how many hours a person may claim. A user who genuinely worked more should plead the hours they worked and prove the excess by ordinary means. An agent that quietly trims the claim down to the cap has given away the difference before anyone has argued about it.

### Step 7b, global overtime, and what the remedy actually is

A wage set so as to include overtime or weekly-rest premium is treated by `סעיף 5` of the Wage Protection Law as **regular wage only**. Get the consequence right, because the common version of it is wrong:

The remedy is **re-characterisation, not a top-up of the excess**. It is not "the global covers 40 hours, you worked 46, so 6 hours are owed". If the arrangement fails, the whole global sum is treated as regular wage, the hourly rate is re-derived from it, and **every** overtime hour in the period is then owed its premium on that re-derived rate. That is a materially larger figure, and an agent that computes only the excess understates the claim.

The labour courts do recognise a valid global arrangement on cumulative conditions, listed in `references/rates-and-tiers.md` section 7. Apply them to the user's facts and never validate the arrangement on the user's say-so.

### Step 7c, evidence, and how long the claim lives

**Evidence first.** Where the employer has no ledger, the user's own material carries the claim. Tell them to collect and preserve it first; `references/records-and-remedies.md` section 7 lists what counts, and why asking the employer in writing for the ledger is worth doing alone.

**The limitation clock on the wage.** A wage claim is an ordinary civil claim and prescribes in **seven years** (`סעיף 5(1)` of the Limitation Law, "בשאינו מקרקעין, שבע שנים"), running from when the cause of action arose, which for wages means each payment separately. Say this whenever a user asks about an old period, and keep it distinct from the far shorter delayed-wage clock in Step 8.

### Step 7d, what this skill does not price

Flag these and stop, rather than fold a guess into the figure:

- **Sector extension orders** (guarding, cleaning, hotels and restaurants, manpower contractors, care work) set their own rates and supplements above the statutory floor. If one applies it governs, and these figures are the fallback.
- **דמי חגים** (holiday pay) is a separate entitlement with its own qualifying conditions and interaction with the rest-day rules. It is adjacent to this reconciliation, not part of it.

### Step 8, timing, and the two different clocks

A monthly wage is payable at the end of the month it is paid for. Delayed wage attracts compensation computed as the **higher of** two formulas, one week-based and one index-plus-percentage based, both set out in `references/records-and-remedies.md`.

Warn about the clock: the right to delayed-wage compensation lapses if no claim is filed within **one year** from when the wage is treated as delayed, or **60 days** from receiving the related wage, **whichever is earlier**, extendable by the court to 90 days. The wage itself stays claimable far longer. A halana figure given without the clock misleads.

## Examples

### A five-day week, one long Tuesday

Tuesday runs 08:00 to 19:30 with a 45-minute break. Working hours 10.75, daily bound 8, so 2.75 overtime hours: two at 125 percent and 0.75 at 150 percent. Even if the week totals under the weekly bound, that Tuesday premium is owed, because the daily limb is independent.

### Saturday work, two employees, same hours

Both work six hours in the weekly rest. The monthly-salaried employee is already paid for the day, so the marginal entitlement is the premium element plus paid compensating rest. The hourly employee is entitled to 150 percent of his hourly rate for all six hours, with unpaid compensating rest. Same hours, different owed figure.

### A payslip that looks complete but is not

The employee is hourly paid. The payslip states 195 hours worked, a value of a regular hour, a wage line of 195 times that value, and 20 overtime units against no premium amount. Establish the convention first: that wage line is reassuring on one reading and damning on the other. On the supplement-only convention 195 times the hourly value is exactly right and check 1 passes; on the full-rate convention that line should have covered only the 175 ordinary hours. Either way the employee was paid 195 hours of value for 175 ordinary and 20 overtime hours, where the lawful figure is 200: 175 plus 20 at 125 percent, or equivalently 195 plus the 25 percent supplement on 20. The premium was never applied, the shortfall is at least five hours of value and more if the daily split puts any of the 20 in the 150 percent tier, and no attendance record was needed. Check 1 alone would have missed it on a supplement-only payslip, which is why the convention comes first.

## Reference Links

| Source | URL | What to check |
|---|---|---|
| חוק שעות עבודה ומנוחה | https://he.wikisource.org/wiki/חוק_שעות_עבודה_ומנוחה | Sections 1, 2, 3, 7, 16, 17, 18, 20, 21, 25, 30 |
| חוק הגנת השכר | https://he.wikisource.org/wiki/חוק_הגנת_השכר | Sections 5, 9, 17, 17a, 24, 26b and the Schedule |
| צו הרחבה, קיצור שבוע העבודה | https://www.gov.il/BlobFolder/dynamiccollectorresultitem/extention-order-short-week-2018/he/extention-order-short-week-2018.pdf | The 42-hour basis and the shortened-day mechanism |

## Bundled Resources

| File | Use it for |
|---|---|
| `references/rates-and-tiers.md` | The full tier table, the rest-day split, overtime caps, the minimum-wage table and base |
| `references/records-and-remedies.md` | Ledger duty, the burden shift and its cap, payslip fields, delayed-wage clock, absence months, no-records and payslip-only scenarios |
| `references/domain-checklist.md` | Coverage contract, and figures circulating in the wild that are wrong |
| `scripts/reconcile_hours.py` | Daily-then-weekly split and tiering. Optional, see Step 6 |

## Gotchas

- **The two-hour tier is daily, not monthly.** Applying it once per month is the single most common computational error and it always understates what is owed.
- **Never compute from a monthly hour total.** The daily limb and the weekly limb are independent, so a month that looks fine in aggregate can still contain owed overtime on individual days.
- **The statutory week and the operative week are different numbers.** The statute says 45; the economy has run on 42 since 2018; some public bodies are at 40. Say which one you are using and why.
- **The premium base includes supplements.** Computing off bare base salary is how a compliant-looking payslip hides a shortfall.
- **"No records means the employee wins everything" is wrong.** The burden shift is capped, and the employee must still give a minimal factual version.
- **The delayed-wage clock is much shorter than the wage claim.** Reporting a halana figure without the one-year and 60-day limits misleads the user about what is still recoverable.
- **A payslip alone is a workable case, not a dead end.** The `סעיף 26ב(ג)` presumption converts missing payslip components into a computable position, so never tell a user with no timesheet that nothing can be done.
- **Do not apply the re-characterisation twice.** Step 1b's presumption and Step 7b's global-overtime remedy both re-derive the base from the paid wage. Reaching the same sum by both routes and stacking them inflates the claim.
- **The deductions side is not this skill's.** A payslip audit that drifts into tax, National Insurance or pension has left its boundary; hand off to `israeli-payroll-calculator`.
- **Check the applicability gate before doing any arithmetic.** For a genuine management or personal-trust role the entire computation is void, and producing a confident number for such a worker is worse than producing none.

## Troubleshooting

| Symptom | Cause | What to do |
|---|---|---|
| The monthly totals look right but the user insists he is owed | The daily limb was ignored | Recompute day by day; overtime can arise in a week that totals exactly the standard hours |
| The premium comes out lower than the user expects | The base excluded supplements | Recompute the regular wage including all supplements the employer pays |
| Two employees worked the same Saturday and the figures differ | Monthly-salaried versus hourly | This is correct. Explain the two regimes rather than reconciling them |
| The employer says the salary already includes overtime | Inclusive wage | Such a wage is treated as regular wage only, so the entitlement survives; check whether an approved collective agreement applies |
| The user has only a payslip and no timesheet | Treated as a dead end | Run Step 1b. Component breaches plus the `סעיף 26ב(ג)` presumption produce a finding without any attendance record |
| The payslip shows overtime units but the premium looks like base rate | Premium never applied | Divide the overtime amount by the units and compare against 125 and 150 percent of the stated hourly value |
| The user asks whether the tax or pension deduction is right | Out of scope | Hand off to `israeli-payroll-calculator` |
| The worker is a manager | The applicability gate | Do not produce a premium figure as though it were owed |
| A reserve-duty month shows a reduced base or phantom overtime | Absence days counted as hours worked | Take the absence days out, treat the reserve line as a lawful residual, and do not check it against this month's hours |

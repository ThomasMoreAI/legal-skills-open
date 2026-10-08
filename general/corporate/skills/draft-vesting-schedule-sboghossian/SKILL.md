---
name: draft-vesting-schedule-sboghossian
title: Vesting Schedule
description: Use when drafting a vesting schedule for founder shares, employee options (ISO/NSO), or RSUs. Covers the standard 4-year monthly with 1-year cliff structure, alternative schedules (quarterly, annual, performance-based, hybrid), acceleration triggers (single vs double trigger), good-leaver/bad-leaver treatment, and the documentation chain (option plan, grant letter, exercise notice). Includes MENA-specific tax considerations (UAE 9% corporate tax, KSA, no income tax), US 83(b) election timing, and UK EMI/non-EMI treatment.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-vesting-schedule
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Vesting Schedule

A vesting schedule controls when an employee, founder, or service provider earns the right to exercise or retain equity. Without vesting, a co-founder who departs in year one takes their full equity stake — leaving the remaining founders and investors to work for a shareholder who contributes nothing. Vesting aligns long-term incentives with the company's need to retain talent.

## When to use this

- Founders establishing a startup and formalizing co-founder equity (before or at the first investment round)
- VC term sheet negotiation — investors require founder vesting as a standard condition
- Equity grant program for employees, advisors, or independent contractors
- Post-acquisition equity rollover (acquirer restructures the seller's equity into a new vesting scheme as retention)

## Standard Vesting Structures

### Structure 1: 4-Year Monthly with 1-Year Cliff (VC Standard)

- **Cliff**: 25% of the total grant vests on the first anniversary of the grant date
- **Monthly**: 1/48 of the total grant vests on each monthly anniversary thereafter for 36 months
- **Total**: 100% vested at 4 years

**Why this is standard**: the cliff ensures that very short-tenure employees (or co-founders who leave quickly) receive no equity; the monthly schedule aligns with payroll and is predictable.

**Example**: 1,200,000 options granted on January 1, 2024
- January 1, 2025: 300,000 options vest (cliff)
- February 1, 2025: 25,000 options vest
- Each month thereafter: 25,000 options vest
- January 1, 2028: final 25,000 vest (fully vested)

### Structure 2: 4-Year Quarterly with 1-Year Cliff

- **Cliff**: 25% at month 12
- **Quarterly**: 1/16 of the total grant per quarter thereafter
- More employee-friendly than monthly (larger installments, less administrative burden)

### Structure 3: 4-Year Annual

- **Annual vesting**: 25% per year, vesting on each anniversary
- Less common in tech; used in more traditional industries
- **Risk**: one day before the anniversary, the employee has no unvested shares and may leave without triggering any accelerated cliff/vest

### Structure 4: Performance-Based Vesting

Vesting tied to measurable milestones rather than (or in addition to) time:
- Revenue milestones: vest X% on achieving USD Y in ARR
- Product milestones: vest X% on achieving launch / user count / specific product metrics
- Market milestones: vest X% on regulatory approval / market entry

**Risk with pure performance vesting**: disputes about whether milestones are met; subjective criteria create litigation. Always define milestones with objective, measurable, and verifiable criteria, and include an independent calculation mechanism.

### Structure 5: Hybrid (Time + Performance)

- 50% time-based (4-year monthly with cliff)
- 50% performance-based (milestone-triggered)
- Most common for senior hires in growth-stage companies where both retention and performance accountability matter

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Grant date | Start date for vesting period; beginning of the cliff | Must provide |
| Grant size (number of shares / options / RSUs) | Total equity granted | Must provide |
| Cliff duration | How long before any equity vests | 12 months (1-year cliff) is VC standard |
| Total vesting duration | Total time to full vest | 48 months (4 years) is VC standard |
| Vesting frequency | Monthly / quarterly / annual | Monthly for options; quarterly for RSUs |
| Acceleration provisions | What triggers acceleration | Double trigger is market standard |
| Treatment on departure | What happens to vested and unvested shares when the holder leaves | See good/bad leaver below |

## Acceleration Provisions

### Single Trigger
A change of control (acquisition, merger) alone triggers acceleration of unvested shares.
- Founder-friendly: the founder receives full equity benefit regardless of whether they remain employed
- Investor concern: acquirer inherits a large vested equity stake without retention leverage; may depress acquisition price

Common single-trigger: 25–50% acceleration on CIC; 100% single trigger is rare except for very early-stage or sole founders.

### Double Trigger (Market Standard)
Two events must both occur:
1. **First trigger**: a change of control (acquisition, merger)
2. **Second trigger**: within [12–24] months after the CIC, the employee is terminated without cause, or resigns for good reason (constructive dismissal)

On double trigger: 100% of unvested shares accelerate.

Good reason typically means: material reduction in compensation, material diminution in responsibilities, relocation by more than [50 miles / reasonable commute distance], or material breach of the employment agreement by the employer.

### Performance Acceleration
Specific milestones, when achieved, trigger a tranche of performance-based vesting. The milestone definition must be airtight.

## Good Leaver / Bad Leaver

### Good Leaver
- Definition: resignation without cause; termination without cause; death; permanent disability
- Outcome: retains all vested shares/options as of the departure date; unvested shares forfeited (or subject to repurchase at fair market value, not par value)
- Options exercise window: extended to [12 months] from the good-leaver departure date (contrasts with the standard 90-day post-termination exercise window in most option plans)

### Bad Leaver
- Definition: termination for cause; resignation in breach of contractual obligations; violation of non-compete
- Outcome: may be required to forfeit or sell vested shares at par value (or at a low repurchase price); unvested shares forfeited
- **Note**: bad-leaver provisions allowing repurchase of vested shares at par are standard in VC-backed companies but uncommon in US startup practice where vested shares are generally inviolable; in DIFC/English-law structures, these provisions are enforceable if clear and for consideration

### Death / Disability
- Standard: 100% acceleration (all unvested shares vest immediately)
- Rationale: the vesting period was intended to retain the individual; neither party can be held to a retention schedule when the individual is unable to perform
- Options exercise: transfers to estate; extended exercise window

## Departure Treatment Summary

| Event | Vested shares | Unvested shares | Options window |
|---|---|---|---|
| Good leaver (termination without cause, voluntary departure, retirement) | Retained at FMV | Forfeited | 90 days → 12 months (if extended) |
| Bad leaver (for cause) | Buyback at par (if contractually provided) | Forfeited | 30–90 days (standard; no extension) |
| Voluntary resignation in breach | May be subject to bad-leaver provisions depending on sha terms | Forfeited | Per plan terms |
| Death | Retained; transfer to estate | Full acceleration | Transfer to estate; 12–24 months exercise |
| Permanent disability | Retained | Full acceleration | Extended exercise |

## Tax Considerations

### US — Section 83(b) Election
When restricted stock (not options) is subject to vesting, the IRS treats unvested stock as received for tax purposes only when it vests — which may be at a higher value, creating a larger tax bill. A Section 83(b) election:
- Filed within **30 days** of the grant date (no extensions; if missed, the election cannot be made)
- Elects to treat the stock as received at the grant date (when the value is typically close to zero for a startup)
- Tax: income tax on (FMV at grant - price paid); often near zero for early-stage founders
- Capital gains clock: starts from the grant date, giving longer capital gains holding period

This is the single most important tax planning step for US startup founders and early employees.

### UK — EMI Options
Enterprise Management Incentive (EMI) options are a UK HMRC-approved option scheme with favorable tax treatment:
- Qualifying companies: must meet size criteria (gross assets < £30M; fewer than 250 full-time equivalent employees); trading company (not investment)
- Tax benefit: EMI options granted at market value; no income tax on exercise; capital gains tax (CGT) rates apply on disposal; Business Asset Disposal Relief (BADR) may apply (10% rate on qualifying gains)
- Non-EMI options: income tax on exercise (the spread between exercise price and FMV); employer NI also due; less favorable

### UAE — 9% Corporate Tax and No Income Tax
- UAE introduced federal corporate tax at 9% effective June 2023 (for financial years starting on or after June 1, 2023)
- Individuals: no personal income tax; equity compensation received by UAE-resident employees does not trigger personal income tax
- **Employer** implications: the corporate tax treatment of equity compensation expense for the employer depends on accounting standards and the UAE Corporate Tax Law; advice from a UAE tax adviser is needed for companies with significant equity plans
- DIFC / ADGM: same (no income tax; entity-level corporate tax)

### KSA
- No personal income tax for Saudi nationals
- Non-Saudi employees: Zakat on Saudi-owned portions; income tax on foreign employees' income (20% on non-Saudi employees unless treaty applies)
- Equity compensation for foreign employees in KSA: the income tax treatment of options/RSUs depends on timing of vesting and exercise; KSA General Authority of Zakat and Tax (GAZT, now ZATCA) should be consulted

## Documentation Chain

Equity compensation requires a stack of coordinated documents:

1. **Stock Option Plan / Equity Incentive Plan**: the overarching legal document adopted by the Board and shareholders; sets out the total pool, the types of equity instruments, eligibility, vesting framework, and plan administration. Without an adopted plan, individual grants cannot be made.
2. **Grant Letter / Option Agreement**: the individual document evidencing each grant — grantee name, grant date, number of options, class, exercise price, vesting schedule, applicable acceleration, good/bad leaver treatment, and governing law. Must be consistent with the plan.
3. **Vesting Schedule Exhibit**: the visual schedule (table or chart) showing cliff date and monthly/quarterly vesting dates, typically attached to the Grant Letter.
4. **Notice of Exercise**: the form the grantee uses when they elect to exercise vested options; must include payment of the exercise price.
5. **Notice of Cancellation**: used on bad-leaver forfeiture or lapse of unvested options; confirms the options have lapsed.
6. **Shareholders' Agreement amendment**: if the option plan creates new rights (information rights, co-sale, etc. for option holders), may need an SHA amendment.

## Common Mistakes

- **No vesting on founder equity** — the most common early-stage oversight; a co-founder who departs in year one retains full ownership; no vesting = no protection for remaining founders and investors
- **Missing the 83(b) window** — US founders who do not file within 30 days of grant lose the ability to elect; the tax impact on a successful exit can be hundreds of thousands of dollars
- **Cliff not set correctly** — "4-year vesting with 1-year cliff" that starts on the company founding date but the grant is made 6 months later means the founder effectively has a 6-month cliff, not a 12-month cliff; always state the grant date and cliff date explicitly
- **Acceleration without definition of "cause"** — double trigger requires a definition of "cause" and "good reason"; if undefined, the acceleration trigger is disputed on every exit
- **No exercise window extension** — standard option plans have a 90-day post-termination exercise window; many departing employees miss this window; consider extending to 12 months for good leavers (particularly important for options with high exercise prices)
- **Bad leaver repurchase at par without consideration** — a clause that forces a bad leaver to sell vested shares at par with no alternative consideration may be challenged as a penalty clause in English-law jurisdictions; ensure the forfeiture mechanism has appropriate consideration

## Related skills

- [[draft-shareholders-agreement]]
- [[draft-term-sheet-vc]]
- [[draft-employment-contract]]
- [[draft-safe]]

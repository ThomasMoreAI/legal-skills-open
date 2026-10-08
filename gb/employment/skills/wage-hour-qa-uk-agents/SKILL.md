---
name: wage-hour-qa-uk-agents
title: /wage-hour-qa
description: Jurisdiction-aware pay and working time Q&A — NMW/NLW compliance, overtime, rest breaks, holiday pay calculation, final pay, and employment status for pay purposes — answered for the specific jurisdiction with the controlling rule researched and cited rather than stated from memory. Use when the user asks any pay or working time question, "what's the minimum wage for", "do we have to pay overtime", "how do we calculate holiday pay", "is this worker entitled to", or "can we classify this person as".
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/employment-legal-uk/skills/wage-hour-qa
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: employment
language: en
---

# /wage-hour-qa

1. Load `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → jurisdictional footprint.
2. Use the workflow below.
3. Identify the jurisdiction the question is about. If not specified, ask.
4. Answer per that jurisdiction's rule. Cite. Flag if it's a close call or the law is shifting.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

"It depends" is true but unhelpful. This skill produces a jurisdiction-specific
answer grounded in researched, cited primary sources — and flags when the
question is close enough to need human judgment. It does not state rules from
memory: NMW/NLW rates, WTR entitlements, and holiday pay calculation methods
change through legislation and case law and must be verified at the time of
answering.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → jurisdictional footprint. If the question doesn't specify a jurisdiction, ask — or answer for the employer's primary jurisdiction and note that.

## The answer

### Step 1: Jurisdiction and employment status

Which jurisdiction? England & Wales / Scotland / Northern Ireland. The NMW Act 1998, Working Time Regulations 1998, and ERA 1996 holiday pay provisions apply across Great Britain. NI has parallel legislation.

What is the worker's employment status? NMW and working time rights apply to **workers** (including employees) — not to genuinely self-employed contractors. If status is in dispute, route to `/employment-legal-uk:worker-classification` first.

### Step 2: Research the rule, then state it

> **Research before answering.** For the jurisdiction and question, identify the currently operative rule. Cite the controlling primary source (statute, statutory instrument, or leading case) with a pinpoint cite. Note the effective date and whether the rule has been recently amended or is subject to pending litigation. If you cannot verify the current state of the law, say so and flag for solicitor verification — do not state a rule you have not confirmed.

> **No silent supplement.** If a research query returns few or no results for the jurisdiction-and-question, report what was found and stop. Say: "The search returned [N] results from [tool]. Coverage appears thin for [jurisdiction / question]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]`, (4) flag as unverified and stop. Which would you like?"
>
> **Source attribution.** Tag every citation: `[uk-legal MCP]` for legislation or case law retrieved via the uk-legal MCP; `[BAILII]` for BAILII case law; `[legislation.gov.uk]` for statutory provisions; `[govuk MCP]` for GOV.UK/HMRC guidance; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for training-data citations. Never strip or collapse the tags.

Common question types — for each, the answer is time-sensitive and must be researched:

- **"What's the NMW / NLW for this worker?"** — See Step 2a below.
- **"Do we have to pay overtime?"** — See Step 2b below.
- **"How much holiday is this worker entitled to?"** — See Step 2c below.
- **"How do we calculate holiday pay?"** — See Step 2d below.
- **"What rest breaks are required?"** — Research WTR 1998 regs 10–12: 11 consecutive hours' rest between working days, 24 hours' rest per week (or 48 per fortnight), 20-minute uninterrupted rest break where the working day exceeds 6 hours. Young workers have different rules. Verify currency.
- **"When is final pay due?"** — Research the contractual pay date plus accrued holiday (WTR 1998). Unlike some US states there is no "final pay by end of day" rule in UK law; final pay falls on the next contractual pay date unless the contract says otherwise. But accrued statutory holiday must be included and cannot be forfeited.
- **"Can we classify this person as a contractor?"** — Route to `/employment-legal-uk:worker-classification` unless the facts are already clearly settled.

---

### Step 2a: National Minimum Wage and National Living Wage

> **Verify the current rates before answering.** NMW/NLW rates are uprated annually each April by the Low Pay Commission recommendation. Do not state a rate from memory — research the currently operative rates from HMRC or legislation.gov.uk and cite the source.

The NMW Act 1998 (as amended) and the National Minimum Wage Regulations 2015 (SI 2015/621) establish the rate tiers. As of the date of this review, the applicable tiers are set by age and apprenticeship status — verify the current amounts.

**NMW calculation is not straightforward.** The NMW applies to "pay for NMW purposes" divided by "hours for NMW purposes" — both are defined terms under the 2015 Regulations and differ from gross pay and hours worked.

Key traps:
1. **Salary sacrifice reduces NMW pay.** If the worker is in a salary sacrifice scheme (e.g., cycle-to-work, childcare vouchers, pension contributions above the auto-enrolment minimum), the salary sacrifice amount is deducted from pay for NMW purposes. A worker on minimum wage who enters salary sacrifice can fall below NMW. Research reg 10 of the 2015 Regulations.
2. **Uniform / equipment deductions.** Deductions for uniform or equipment that the employer requires and that benefit the employer can reduce pay for NMW purposes. Research regs 12–13.
3. **Sleeping-in shifts.** Whether workers are entitled to NMW for the full duration of a sleeping-in shift (or only for time they are awake and required to work) has been the subject of extensive litigation. Research the current position — *Royal Mencap Society v Tomlinson-Blake* [2021] UKSC 8 is the leading case but check whether it has been affected by subsequent decisions or legislation.
4. **Salaried hours workers.** For workers paid an annual salary for a set number of hours, research reg 21–29 of the 2015 Regulations: the NMW entitlement is spread across the "salaried hours work" calculation, not checked pay-period by pay-period in the same way as time work.

Show the NMW calculation:
```
NMW pay for the period = [gross pay] minus [any deductions that reduce NMW pay per 2015 Regs]
Hours for NMW purposes = [hours worked] [adjusted per reg, e.g. sleeping-in, travel time]
Effective hourly rate  = NMW pay ÷ hours for NMW purposes
Compliant?             = Effective hourly rate ≥ applicable NMW/NLW rate?
```
Any computed rate carries `[verify — check against current HMRC NMW rates before paying or asserting]`.

---

### Step 2b: Overtime

**There is no statutory overtime rate in UK law.** Unlike the US FLSA, there is no requirement to pay a premium rate (time-and-a-half, double-time, etc.) for overtime. The obligation to pay overtime, and the rate at which it is paid, depends entirely on the contract.

What the law does require:
1. **NMW compliance over the pay reference period.** Even if no overtime premium is contractually required, total pay for the pay reference period must not fall below the applicable NMW/NLW rate when spread across total hours worked (including overtime). An employee contractually on a flat salary for 40 hours who regularly works 60 hours may be receiving sub-NMW effective pay. Research the calculation method for the worker type (time work, salaried hours work, output work).
2. **Holiday pay must reflect normal pay, including regular overtime.** See Step 2d.
3. **Working Time Regulations 48-hour average.** The WTR 1998 reg 4 imposes an average 48-hour weekly working time limit over a 17-week reference period. Workers can opt out in writing (reg 5), but the opt-out must be voluntary and can be withdrawn on 7 days' notice (or longer if agreed, up to 3 months). Certain sectors (e.g., junior doctors) have different rules.

If the question is whether the employer must pay for overtime worked: the answer turns on the contract. Research any relevant contractual provisions and state the contractual position. If no contract has been provided, flag the gap.

---

### Step 2c: Holiday entitlement

Workers are entitled to 5.6 weeks' paid annual leave per year under WTR 1998:

- **Regulation 13 leave**: 4 weeks (derived from the EU Working Time Directive)
- **Regulation 13A leave**: 1.6 weeks (UK domestic addition)

The distinction matters because different rules apply to carry-over and accrual. Research the current position on whether the employer is entitled to prevent carry-over of reg 13 leave where the worker was unable to take it due to sickness or other statutory leave. The case law and HMRC guidance on carry-over has developed significantly — verify currency.

**For irregular-hours and part-year workers (post-2023 amendments):** The Employment Rights Act holiday pay reforms (taking effect April 2024) introduced new accrual and carry-over rules for irregular-hours workers and part-year workers following the Supreme Court decision in *Brazel v Harpur Trust* [2022] UKSC 21. The 12.07% accrual method was restored for these workers. Research the current position — the amendments are recent and may have been further modified. Cite primary sources and verify currency carefully.

**Public holidays**: the 5.6 weeks can include the 8 UK public bank holidays, but only if the contract says so — workers are not automatically entitled to bank holidays off in addition to 5.6 weeks. Research the contractual position and the current GOV.UK guidance.

---

### Step 2d: Holiday pay calculation

Holiday pay is one of the most litigated areas of UK employment law. The rule is that workers must receive their **normal remuneration** during annual leave — they must not be financially deterred from taking leave. Research the current calculation method; the following elements must be included if they are part of normal pay:

| Element | Include? | Authority |
|---|---|---|
| Basic salary / hourly rate | Yes | WTR 1998 reg 16 |
| Regular non-guaranteed overtime | Yes | *Bear Scotland Ltd v Fulton* [2014] UKEATS/0047/13 |
| Regular voluntary overtime (sufficiently regular) | Yes | *Flowers v East of England Ambulance Trust* [2019] EWCA Civ 947 |
| Contractual commission (regular) | Yes | *Lock v British Gas Trading Ltd* [2014] ICR 813 |
| Shift allowances and regular supplements | Yes | *Williams v British Airways plc* [2011] IRLR 985 |
| Discretionary / one-off bonuses | No | Generally excluded |
| Genuine expenses reimbursements | No | Excluded |

The holiday pay calculation is based on **average weekly remuneration** over the 52-week reference period immediately preceding the leave (for reg 13 leave) — or the most recent 52 weeks in which the worker was paid (weeks with no pay are skipped up to 104 weeks back). Research the current 52-week reference period rule and any modifications for your fact pattern.

> **Show the calculation:**
> ```
> Average weekly pay (52-week reference) = total remuneration in reference period ÷ weeks worked
> Daily rate                             = average weekly pay ÷ days normally worked per week
> Holiday pay for the leave period       = daily rate × days taken
> ```
> Any computed figure carries `[verify — consult payroll or employment law adviser before paying or asserting]`.

**Regulation 13 vs 13A distinction in practice**: if the employer is maintaining the distinction between the two leave types for carry-over purposes, ensure the payroll system calculates holiday pay identically for both — there is no lawful basis to pay a lower rate for the 1.6 weeks' additional leave.

---

### Step 2e: Back-pay and tribunal exposure

If the question involves a back-pay computation, arrears, or ET claim exposure:

1. **NMW arrears**: computed per the NMW calculation in Step 2a. HMRC enforces NMW compliance; underpayment can result in a notice of underpayment, penalty of 200% of the arrears (up to £20,000 per worker), and public naming. Carry `[verify — HMRC enforcement position may vary; check current penalty rates]`.

2. **Holiday pay arrears**: the limitation point is important. Under the Employment Rights Act 1996 s.23 and the decisions in *Fulton* and subsequent cases, a claim for underpaid holiday pay must be brought within 3 months of the last underpayment (or underpaid leave taken), subject to the "series of deductions" doctrine. A gap of more than 3 months between deductions may break the series and limit the lookback. Research the current state of the "series of deductions" doctrine — it has been the subject of evolving case law. Verify currency.

3. **ET compensation**: unlike the US FLSA, there is no automatic doubling of back pay in the Employment Tribunal. The ET can award the arrears plus interest at 8% simple from the date of the breach. For unlawful deduction from wages (ERA 1996 Part II), the ET has no cap on the award for the deductions themselves. For holiday pay specifically, the relevant remedy is an unlawful deduction claim (ERA 1996 s.23). Carry `[verify — consult employment law adviser before asserting or paying]`.

4. **TUPE transfers**: where workers transferred under TUPE 2006, claims for pre-transfer holiday pay arrears pass to the transferee. Flag if relevant.

---

### Step 3: The flag

Is this a close call? Be honest.

- If the answer is clear on the researched rule: say so.
- If it's close (e.g., the "sufficient regularity" test for voluntary overtime in holiday pay): say so and flag for employment law adviser.
- If the law is in flux (e.g., carry-over rules for irregular-hours workers post-Brazel amendments): say so, state the current position, and note the uncertainty.
- If you could not verify currency: say so. Do not guess.

## Output format

Conversational. This is a Q&A, not a memo.

> **Research-connector pre-flight.** Before emitting the answer, check whether a legal research connector is reachable — the uk-legal MCP or BAILII. If no connector returns results (or none is configured), record it in the **Sources:** line of the reviewer note: e.g., `not connected — cites from training knowledge; the highest-fabrication topics in UK pay Q&A are current NMW rates (uprated each April), post-*Brazel* holiday accrual for irregular-hours workers, and the series-of-deductions limitation point — spot-check those first`. Per-citation `[model knowledge — verify]` tags remain inline. Do not emit a standalone banner above the output.

> **Jurisdiction assumption.** Answers apply to England & Wales (or the stated jurisdiction). NMW rates, WTR entitlements, and holiday pay rules apply across Great Britain; Northern Ireland has parallel legislation. If the worker is in Northern Ireland, note this and verify the NI position separately.

```
**[Jurisdiction] — [Question topic]:**

[The researched rule, one paragraph, with pinpoint cite and currency note.]

[If calculation required: show the formula and inputs explicitly per Step 2a/2d above.]

[If close call or shifting law: the flag.]

[If the answer differs in NI or for specific worker types: note it.]
```

> **Verify citations.** Any statute, regulation, or case cite above was generated with AI assistance. Before relying on it, check it against legislation.gov.uk, BAILII, or the uk-legal MCP for accuracy, currency, and subsequent history.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customise the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer or HR professional picks.

## What this skill does not do

- State NMW rates, WTR entitlements, or holiday pay calculation methods from memory — every answer is grounded in a researched, cited primary source verified for currency.
- Compute back pay as a final figure — it scaffolds the calculation and requires payroll or employment law adviser verification before any amount is paid or asserted.
- Make status decisions for borderline worker/employee/self-employed cases — route to `/employment-legal-uk:worker-classification`.
- Give a comprehensive survey of all employment law obligations — answers the specific question for the relevant jurisdiction.
- Track when the answer changes — NMW rates change each April; holiday pay case law continues to develop. Re-ask for current.

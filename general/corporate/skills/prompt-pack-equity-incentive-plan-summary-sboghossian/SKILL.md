---
name: prompt-pack-equity-incentive-plan-summary-sboghossian
title: Equity Incentive Plan Summary
description: Use when drafting an employee-facing summary of a company's equity incentive plan — covering grant types (stock options, RSUs, phantom equity, warrants), vesting schedules, exercise procedures, tax implications, and treatment of equity on termination or change of control. Applicable for MENA entities (UAE, DIFC, ADGM, KSA, LB, EG) and internationally. Trigger when a company wants to communicate its equity program clearly to new or existing employees, or when HR is rolling out an ESOP or LTIP.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-equity-incentive-plan-summary
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Equity Incentive Plan Summary

## When to use this

Use this skill when a company needs a clear, employee-accessible summary of its equity incentive program. Equity plans are complex; employees often do not understand what they have been granted, when it vests, how to exercise it, or what happens to it when they leave. A well-drafted summary reduces questions, improves trust, and helps employees value their total compensation package accurately.

Typical triggers:
- Company launching a new ESOP, RSU, or phantom equity plan
- Employee receiving a first equity grant and needing a clear explanation
- HR onboarding documentation for senior hires receiving equity
- Plan administrator preparing a participant communication for the annual grant cycle
- Company preparing for IPO or M&A and wanting employees to understand their equity position

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Company name and jurisdiction of incorporation | Determines legal structure of equity grants and tax treatment | Ask |
| Plan type (stock options, RSUs, phantom equity, warrants, profit interest) | Each has different mechanics, tax treatment, and rights | Ask |
| Grant details (number of shares/units, exercise price if applicable, grant date) | The specific terms of the individual's grant | Ask |
| Vesting schedule | When the equity is earned | Ask |
| Applicable tax jurisdiction for the employee | Tax treatment of equity varies dramatically | Ask |

## Optional inputs

- Cliff period (if different from standard)
- Performance vesting conditions (if applicable — PSUs or performance shares)
- Anti-dilution protections (if any)
- Change-of-control acceleration provisions
- Blackout periods and trading restrictions (relevant for public companies)
- ESPP (Employee Stock Purchase Plan) mechanics if combined with options/RSUs

## Document structure

### Section 1 — What is equity compensation?

Plain-language introduction:
> "As part of your compensation package, [Company] is pleased to grant you equity in the company. This means you have the opportunity to own a part of [Company] and share in its growth."

Explain the basic concept: the grant is a right to receive shares (or cash equivalent) if and when vesting conditions are met.

### Section 2 — What type of equity do I have?

**Stock options (ISO / NSO / EMI options)**:
- A right to purchase shares at a fixed price (the "exercise price" or "strike price") set on the grant date
- Value accrues when the share price rises above the exercise price ("in the money")
- Must be exercised to own shares; exercise requires paying the exercise price
- If the share price is below the exercise price, the option is "underwater" — no value

**RSUs (Restricted Stock Units)**:
- A promise to deliver shares (or cash equivalent) once vesting conditions are met
- No exercise price — the employee receives shares for free on vesting
- More employee-friendly in most jurisdictions; common in public companies

**Phantom equity / SARs (Stock Appreciation Rights)**:
- Cash payment equal to the increase in share value over a specified period
- Employee never actually owns shares; settlement is in cash
- Common in MENA and civil-law jurisdictions where share issuance to employees is complicated by corporate formalities

**Warrants**:
- Similar to options but technically a right to subscribe for new shares (not purchase existing ones)
- Common in venture capital-backed companies and MENA jurisdictions

### Section 3 — Vesting Schedule

Explain vesting with a clear example:

**Standard 4-year cliff + monthly vesting**:
> "Your [X] options vest over 4 years. The first 25% (the 'cliff') vests after 12 months of continuous employment. The remaining 75% vests monthly over the following 36 months."

Provide a visual or table:
| Vesting date | Options vesting | Cumulative total |
|---|---|---|
| Month 12 (cliff) | 25% | 25% |
| Monthly, months 13–48 | ~2.08% per month | 25%–100% |

**Performance vesting**:
If the plan includes performance conditions (PSU/PRSU), explain: "Vesting of performance shares depends on achieving [specific metrics — e.g., revenue targets, EBITDA, or share price performance]. Your HR team or compensation committee will confirm performance results annually."

**Acceleration**:
State clearly whether vesting accelerates on:
- Change of control (sale of the company): single trigger (acceleration on change of control) vs. double trigger (acceleration on change of control + termination without cause)
- Termination without cause

### Section 4 — How to exercise options (for option plans)

Step-by-step guide:
1. Confirm your vested options balance via [HR system / share register portal]
2. Submit an exercise notice to [HR / stock plan administrator] specifying the number of options to exercise
3. Pay the exercise price (methods: cash payment; cashless exercise / sell-to-cover; net exercise if available)
4. Upon processing, shares are issued / transferred to you (or, for cashless exercise, net sale proceeds paid)
5. Report the taxable event to your tax adviser promptly

### Section 5 — Tax implications

This section should be written with a jurisdiction-specific disclaimer:

> "The tax treatment of equity compensation depends on your personal tax situation and the laws of the country where you work and reside. You should consult your personal tax adviser before making any exercise decisions."

**Key concepts**:
- **Grant date**: In most jurisdictions, no taxable event at grant
- **Vesting date (RSUs)**: Taxable income typically arises when RSUs vest and shares are delivered; amount is the market value of shares at vesting minus any cost
- **Exercise date (options)**: For NSOs/unapproved options, taxable income typically arises on exercise equal to the spread (market price – exercise price); for approved options (EMI in UK, ISO in US), tax may be deferred to sale
- **Sale date**: Capital gains or income tax on any profit above the taxable amount previously recognized

**MENA tax note**: UAE and some GCC states have no personal income tax; employees resident there may not have tax liability on equity vesting (though corporate tax and social insurance implications may arise for the employer). KSA has income tax on non-Saudi employees. Lebanon has income tax on worldwide income for residents. Egypt has income tax on employment income including equity. Take local tax advice in each jurisdiction.

### Section 6 — What happens to my equity when I leave?

This is often the most important section for employees:

| Departure type | Typical outcome |
|---|---|
| Voluntary resignation | Unvested equity is forfeited; vested options must be exercised within [90 days] of departure (check plan rules) |
| Termination without cause | Unvested equity usually forfeited; some plans provide for partial accelerated vesting; vested options: [90-day] post-termination exercise window |
| Termination for cause | Unvested equity forfeited; many plans also allow forfeiture of vested options on termination for cause |
| Death or disability | Plan-specific; many plans accelerate vesting; estate has an extended exercise window |
| Change of control | See acceleration provisions in Section 3 |

**Key risk to communicate**: The [90-day] post-termination exercise window means that an employee who leaves with valuable vested options must decide whether to exercise (and potentially pay tax) within 90 days or lose the options. This is a genuine financial decision that requires advance planning.

## Jurisdictional notes

### MENA-specific equity plan structures

In MENA jurisdictions, the corporate law complications of issuing shares directly to employees are common:
- **UAE onshore LLCs**: Share ownership by employees is possible but requires corporate registration formalities; phantom equity / SARs are often used instead
- **UAE free zone entities (DIFC/ADGM)**: DIFC and ADGM company law is more flexible; share options to employees are straightforward and commonly used by startups incorporated in these zones
- **KSA**: Sharia considerations may affect the structure of equity incentive plans; interest-bearing structures must be avoided; phantom equity tied to dividend-equivalent payments is a common alternative
- **Lebanon/Egypt**: Civil-law corporate formalities for share issuance; offshore holdco (Cayman, BVI, Delaware) with ESOP is common to simplify mechanics

### Virtual share plans / phantom equity

For companies where direct share issuance is impractical (UAE LLC, KSA closed joint-stock company), a phantom equity plan replicates the economics without the legal complexity:
- Employee receives units that track the company's equity value
- On a liquidity event (IPO, sale), units are settled in cash equal to their hypothetical share value
- No shareholder rights; no corporate registration required
- Tax treatment: treated as employment income at the time of payment in most MENA jurisdictions

## Common mistakes

- **Not explaining the post-termination exercise window**: Employees who leave without understanding they have 90 days to exercise lose their options; this creates HR and reputational risk.
- **Forgetting tax on vesting RSUs**: RSUs that vest when the company is private (no market to sell shares) create a tax liability with no corresponding liquidity; warn employees and plan for this.
- **No discussion of dilution**: Employees often do not understand that their percentage ownership will decrease as the company raises more capital; explain anti-dilution protections (or lack thereof) honestly.
- **Phantom equity with no liquidity event defined**: A phantom equity plan that doesn't define what triggers a payout (and when) creates disputes; define the triggering events precisely.
- **Ignoring Zakat / Islamic finance concerns in KSA**: Equity plans that involve interest or speculative elements may face Zakat Board or Sharia challenges in KSA; structure carefully.

## Related skills

- [[prompt-pack-executive-employment-agreement]]
- [[prompt-pack-employment-offer-letter]]
- [[prompt-pack-investment-agreement-venture-capital]]
- [[prompt-pack-escrow-agreement]]

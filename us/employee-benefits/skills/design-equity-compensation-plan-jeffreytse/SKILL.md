---
name: design-equity-compensation-plan-jeffreytse
title: Design Equity Compensation Plan
description: Use when designing or auditing an equity compensation plan covering stock options, RSUs, or other equity awards for startups or growth-stage companies
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/law/corporate/skills/design-equity-compensation-plan
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employee-benefits
language: en
tags: [equity-compensation, stock-options, rsu, startup, cap-table, asc-718]
---

# Design Equity Compensation Plan

Structure an equity compensation plan that attracts and retains talent, complies with tax and accounting rules, and preserves cap table integrity from founding through exit.

> **Disclaimer:** This skill provides general educational guidance, not legal advice. Equity compensation plans involve binding tax, securities, and corporate law obligations — engage qualified legal counsel to draft and review plan documents before granting any equity.

## Why This Is Best Practice

**Adopted by:** NVCA model plan documents are used as the foundation for equity plans by the majority of VC-backed US startups. Carta data shows 85% of Series A and later companies use ISO/NQO option structures aligned with the NVCA model. Major tech companies including Google, Stripe, and Airbnb base their plans on these frameworks.

**Impact:** Carta benchmarking (2023) shows companies with well-structured equity plans have 23% lower early employee turnover compared to companies with ad-hoc arrangements. NCEO research finds that broad-based equity participation programs correlate with 4–5% higher annual revenue growth. Properly structured plans avoid IRS Section 409A penalties (20% excise tax plus interest) that affect poorly designed arrangements.

**Why best:** Equity compensation has complex intersecting requirements across tax law (ISO/NQO rules, 409A, 83(b)), accounting (ASC 718 fair value expensing), securities law (Rule 701, state blue sky), and governance (board approval, shareholder approval). A structured plan design process that addresses all dimensions prevents costly retroactive fixes.

Sources: IRC §422 (ISOs), §83 (83(b) elections), §409A (deferred compensation); ASC 718 (FASB 2004, updated 2016); NVCA Model Plan (2023); Carta State of Private Markets (2023 Q4); NCEO Equity Compensation (2022); Rule 701 under Securities Act.

## Steps

1. **Define plan objectives and eligibility** — Decide who is eligible (employees only for ISOs; contractors and advisors for NQOs/RSUs), what behaviors the plan should incentivize (retention via vesting, performance via milestones), and the total equity pool size. Standard Carta benchmarking: Series A option pool = 10–15% of fully diluted shares. Confirm pool size with the board and lead investor before designing terms.

2. **Choose award types for each employee class** — ISOs (Incentive Stock Options): for US employees only, favorable long-term capital gains tax treatment if holding periods met, but subject to $100K ISO limit per year. NQOs (Non-Qualified Options): for contractors, advisors, and above-$100K ISO grants; taxed as ordinary income on exercise. RSUs: better for late-stage or pre-IPO companies with known 409A valuations; tax event at vest/delivery, simpler to explain. Use ISOs as the default for early-stage employees.

3. **Set the exercise price at fair market value** — The exercise price must equal or exceed the FMV of common stock at the grant date to avoid IRC §409A violations. Obtain a 409A valuation from an independent appraiser (required for companies that have raised outside capital). Refresh the 409A at least annually and within 12 months of any material event (new funding round, M&A, significant revenue change). Document the valuation board approval.

4. **Design vesting schedules** — Standard US market vesting: 4-year schedule with 1-year cliff (25% vests at 12 months, remainder monthly or quarterly over 36 months). Acceleration provisions: single-trigger (change of control alone) is disfavored by investors; double-trigger (change of control plus involuntary termination) is market standard. For founders, consider a different schedule (e.g., 4-year with no cliff, or partially vested from day one reflecting prior service).

5. **Define post-termination exercise periods (PTEPs)** — Standard PTEPs: 90 days after termination for ISOs (required by IRC §422), 90 days to 10 years for NQOs at the company's discretion. Extended PTEPs (1–10 years) have become common in founder-friendly companies (Stripe pioneered this) but convert ISOs to NQOs after the 90-day ISO window. Decide explicitly and document the trade-off in the plan.

6. **Address early exercise and 83(b) elections** — Allow early exercise (purchasing unvested shares at grant date) in the plan document. Early exercise enables employees to start the capital gains holding period before vesting, often saving significant taxes. Require the company and employee to enter a restricted stock purchase agreement upon early exercise. Educate employees that an 83(b) election must be filed within 30 days of purchase and cannot be extended.

7. **Incorporate securities law compliance** — Most private company option grants rely on Rule 701 exemption (up to the greater of $1M, 15% of total assets, or 15% of outstanding securities). Track Rule 701 limits annually. If grants exceed thresholds, additional disclosure is required. Confirm blue sky exemptions in each state where employees reside. International employees require separate country-by-country analysis.

8. **Plan ASC 718 accounting treatment** — All equity awards to employees must be expensed at fair value under ASC 718. Fair value is calculated using Black-Scholes or a lattice model at grant date. Expense is recognized over the vesting period. Work with auditors or a valuation firm to establish grant-date fair value for each award type. Ensure finance has a process to track and expense grants accurately.

9. **Draft plan document and grant agreements** — Use NVCA model plan as the base document. Customize: plan name, authorized shares, eligible participants, award types, administrator (typically the board or compensation committee), and specific terms. Prepare separate grant notice and award agreement templates for options and RSUs. Have outside counsel review before the first grants are made.

10. **Obtain board and shareholder approval and administer ongoing** — Board approval is required for the plan and each individual grant above a de minimis threshold. Shareholder approval is required for ISO plans (IRC §422 requirement) and for NYSE/Nasdaq-listed companies for all material equity plans. Administer grants through equity management software (Carta, Pulley, or Shareworks). Audit the cap table quarterly for accuracy.

## Rules

- The exercise price for every option must equal or exceed the 409A fair market value at the grant date — below-market grants trigger immediate 409A penalties on the employee with no cure
- ISOs may only be granted to employees, not contractors or advisors — misclassifying a contractor as eligible for ISOs creates tax and securities law violations
- 83(b) elections must be filed within 30 days of purchase — this deadline cannot be extended and missing it eliminates the tax benefit permanently
- All grants require board approval before the grant date — backdating grants or granting with a past exercise price is securities fraud
- Rule 701 limits must be tracked and respected; exceeding them without providing required disclosures is a securities violation

## Common Mistakes

- **Skipping or delaying 409A valuations** — Granting options without a current 409A valuation (older than 12 months or issued before a funding event) exposes every option holder to 409A penalties; obtain the valuation before granting, not after.
- **Single-trigger acceleration** — Granting full acceleration on change of control alone (without a termination trigger) makes the company harder to acquire and is routinely rejected by acquirers; use double-trigger acceleration as the default.
- **Not tracking Rule 701 limits** — Companies that inadvertently exceed Rule 701 thresholds without providing required disclosures face securities violation liability; assign ownership of this tracking to the CFO or general counsel.
- **Poor PTEP communication** — Employees who do not understand their 90-day post-termination exercise window lose valuable options at termination; include PTEP education in onboarding and termination processes.
- **Granting RSUs too early** — RSUs trigger a taxable event at vest; in pre-revenue startups without a near-term liquidity event, employees receive a tax bill with no cash to pay it. RSUs are appropriate for companies within 2–4 years of liquidity; use options for earlier stages.

## Examples

**Series A startup plan:** A company closes its Series A, obtains a 409A valuation of $2.00/share for common stock, establishes a 10% option pool, and grants ISOs to 15 employees at $2.00/share with standard 4-year/1-year cliff vesting and double-trigger acceleration. All grants are board-approved on a single grant date to avoid variable exercise prices.

**Late-stage RSU program:** A pre-IPO company at $8B valuation transitions from options to RSUs for new hires, with RSU delivery triggered at IPO plus 6 months (double trigger: time-vest plus liquidity event). This structure avoids employees owing AMT on paper gains and aligns incentives with the public market.

## When NOT to Use

- When designing equity for a partnership, LLC, or S-corp — these entities use profits interests (for partnerships/LLCs) or restricted stock (for S-corps) under different tax regimes; this framework applies to C-corps
- When the company is domiciled outside the US — international equity plans require country-specific tax analysis; use this framework only for US domestic plans, with separate country annexes for international grants

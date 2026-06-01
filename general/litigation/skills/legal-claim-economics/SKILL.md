---
name: legal-claim-economics
title: legal-claim-economics
description: Use when users say "model claim economics", "litigation funding waterfall", "portfolio economics", "funder MOIC", "DBA/CFA economics", "Monte Carlo", "ATE/adverse costs", or need legal claim recoveries, fee structures, recourse, and settlement distributions modelled.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/legal-claim-economics
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
tags: [litigation-finance, claim-economics, damages, funding, waterfall, monte-carlo]
---

# legal-claim-economics

## When to Use

- A lawyer, funder, or firm wants to model whether a claim or portfolio is economically viable.
- The question involves damages, probability of success, fee arrangements, ATE, adverse costs, funder return, or recovery waterfall.
- The user needs sensitivity or scenario analysis rather than a single best-case number.

This skill models economics. It does not recommend whether to bring, settle, fund, or abandon a claim.

## Audience and Work Shape

Audience: litigation partners, litigation-finance counsel, funding analysts, and legally supervised team members with enough quantitative fluency to review assumptions and formulas.

Work shape: bounded transactional calculation in `calculation_mode`; accretive judgment in `specification_mode`. The skill models assumptions and scenarios, but the responsible lawyer or funder decides what action to take.

## Legal Failure Modes

- Legal support, not legal advice: outputs are working calculations and assumptions registers, not merits, enforceability, tax, regulatory, or professional-conduct advice.
- Privilege/confidentiality: claim economics may be privileged or work-product material. Sharing with funders, auditors, counterparties, insurers, or third parties can affect privilege/confidentiality and needs lawyer approval.
- Accountability: a lawyer or authorised investment decision-maker must sign off before any output is used for fund/no-fund, bring/no-bring, settle/no-settle, or client-facing advice.

## Access Modes

This skill works in three modes:

1. **Calculation mode** - use supplied assumptions and an available calculator, spreadsheet, code execution environment, or arithmetic worked in-session.
2. **User-supplied model mode** - review an existing spreadsheet, calculator output, term sheet, budget, damages model, or funding proposal supplied by the user.
3. **Specification mode** - build the model structure, assumptions list, and formulas, but do not invent calculated outputs.

If key inputs or a calculation method are unavailable, produce an assumptions register and model specification. Do not invent IRRs, percentiles, waterfalls, or Monte Carlo outputs.

## How It Works

### 1. Define the scenario

Capture:

- Claim type or portfolio type.
- Jurisdiction and any regime-specific cost rules.
- Claim count and cohort funnel if relevant.
- Damages distribution.
- Liability and quantum probability.
- Expected time to resolution.
- Settlement discount assumptions.

If a figure is unknown, ask whether to use a range, placeholder, or scenario variable.

Every input must be labelled as `user_supplied`, `document_sourced`, `calculated`, or `assumption_to_verify`. Keep that label through the output so the reader can separate facts from modelling assumptions.

Also record currency, VAT/tax inclusion or exclusion, nominal vs real basis, date of valuation, time unit, discount-rate assumption if used, and the formula used for each calculated output. Do not present calculated figures without these modelling metadata.

### 2. Model revenue and costs

Include:

- Solicitor fee arrangement: hourly, CFA, DBA, hybrid, fixed fee, scheme-paid, or conditional billing.
- Disbursements.
- Counsel, expert, platform, marketing, and administration costs.
- Inter-partes recovery assumptions.
- ATE premium and adverse-cost exposure.
- VAT or tax treatment only if the user supplies the correct assumption.

Flag internally inconsistent inputs and keep them out of headline outputs unless the user expressly asks to model the inconsistent scenario. Label any such output `inconsistent_input_scenario`.

### 3. Model funder economics

Support common return structures:

- MOIC.
- Percentage of proceeds.
- Interest or structured debt.
- IRR hurdle.
- Time or stage ratchets.
- Commitment and ancillary fees.
- Hybrid or greater-of / lesser-of structures.

State clearly who receives what under each layer.

### 4. Apply recourse and waterfall

Build the waterfall:

1. Recoveries received.
2. Costs and disbursements.
3. ATE or insurer position.
4. Funder entitlement.
5. Firm entitlement.
6. Client residual.

Handle pari passu tiers, caps, floors, and shortfall allocation.

### 5. Run scenarios and sensitivity

At minimum, produce:

- Base case.
- Downside case.
- Upside case.
- Break-even claim count or recovery.
- Sensitivity to win probability, damages, time to resolution, costs, and recovery rate.

If stochastic modelling is requested, specify distributions, correlations if any, iteration count, random seed if used, tool/calculation method, and outputs including P5, P50, and P95. If you cannot actually run the calculation, do not invent percentiles; provide the model specification or pseudocode instead.

### 6. Report decision-useful outputs

Recommended outputs:

- Firm IRR / margin.
- Funder IRR / cash multiple.
- Client net recovery.
- Worst-case firm exposure.
- Probability of shortfall.
- Key drivers.
- Input assumptions requiring verification.

Distinguish calculated values from user-supplied assumptions and legal assumptions. Do not opine on merits, funding enforceability, tax treatment, regulatory capital, or professional conduct unless the user supplies the rule or counsel-approved assumption to model.

## Confidence Bands

- High: critical inputs are user-supplied or document-sourced, formulas are shown, and no unresolved legal/tax/funding warnings sit in the critical path.
- Medium: at least one critical assumption is marked `assumption_to_verify`, but the calculation method is auditable.
- Low: specification-only model, missing distributions for stochastic outputs, inconsistent inputs, or no runnable calculation method.

## Out of Scope and Routing

- Merits assessment -> responsible matter lawyer.
- Funding enforceability, champerty, DBA/CFA/PACCAR issues -> litigation-finance specialist.
- Tax/VAT/accounting treatment -> tax/accounting adviser.
- Regulatory capital or fund regulation -> regulatory specialist.
- Professional-conduct issues -> professional responsibility counsel.

## Escalation

Stop and route when the user asks for a legal/tax/enforceability conclusion, when a novel jurisdiction is involved, when funder/firm/client interests conflict, when DBA/CFA/PACCAR questions affect the economics, or when inputs are internally inconsistent and the user has not expressly asked to model the inconsistent scenario.

## Example

```text
Model this claim portfolio under a CFA plus third-party funding structure. Show base, downside, and upside cases, then run sensitivity on damages, win probability, ATE, and time to resolution.
```

For a compact output pattern, see `examples/output.md`.
For waterfall, recourse, return-family, Monte Carlo, and audit-bundle conventions, see `references/engine-model.md`.

## Limitations

- Legal costs and funding enforceability are jurisdiction-sensitive.
- The model is only as reliable as the assumptions.
- Tax, accounting, regulatory capital, and professional conduct issues may require specialist advice.
- No model removes the need for merits analysis.

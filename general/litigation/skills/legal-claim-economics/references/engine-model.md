# Legal Claim Economics Engine Model

Use this reference when modelling claim, portfolio, litigation-funding, or redress-programme economics.

## Compute Order

Use this generic order unless the user supplies a different model:

1. Expand cohort or claim count.
2. Estimate damages/recoveries.
3. Compute solicitor revenue and fee arrangement.
4. Aggregate costs, disbursements, ATE, and adverse-cost exposure.
5. Compute funder entitlement.
6. Run the recovery waterfall.
7. Apply recourse to any funder shortfall.
8. Build cash flows.
9. Compute headline metrics: IRR, NPV, cash multiple, payback, margin, client residual, shortfall exposure.

Do not silently change the order. If a programme-level timeline model is needed, state that it is a separate model.

## Waterfall Model

The pool is the money available for distribution. Depending on the scenario, it may include:

- damages/recovery,
- inter partes cost recovery,
- disbursement recovery,
- scheme contribution,
- settlement proceeds,
- insurance recoveries.

Each waterfall tier should specify:

- tier name,
- beneficiary,
- request formula,
- cap/floor,
- priority,
- pari passu group if any,
- amount requested,
- amount paid,
- shortfall.

Consecutive tiers sharing a pari passu group should be allocated pro rata within available pool.

## Funder Entitlement and Recourse

Core identity:

```text
funder_shortfall = funder_entitlement - funder_received_from_waterfall
```

Apply recourse only to that shortfall, not to the whole claim value.

Recourse profiles:

- `non_recourse` - funder absorbs shortfall.
- `firm_guarantee` - firm absorbs shortfall up to defined obligation.
- `insurance` - insurer absorbs up to policy limit; uninsured tail allocated by assumptions.
- `portfolio_recourse` - shortfall cross-collateralised within portfolio.
- `cross_portfolio_recourse` - shortfall cross-collateralised across portfolios.
- `hybrid` - piecewise allocation across funder, firm, insurer, or portfolio.

## Return Families

Supported return families:

- `moic` - multiple of invested capital.
- `percentage_of_proceeds` - share of recovery or defined net pool.
- `structured_debt_interest` - fixed/floating/current-pay/PIK interest.
- `irr_hurdle` - preferred return or hurdle waterfall.
- `time_or_stage_ratchet` - return changes by time or milestone.
- `commitment_or_ancillary_fees` - arrangement, commitment, exit, or event fees.
- `scheme_contribution` - per-claim or per-cohort contribution with defined treatment.

Combinators:

- `greater_of`
- `lesser_of`
- `sum_of`
- `stacked`
- `piecewise`

State the combinator tree. Do not hide "greater of" economics inside prose.

## Programme-Level Timeline Model

For redress or mass-claim programmes, a simple claim-level waterfall may be insufficient. A timeline model may need:

- monthly facility drawdowns,
- opex versus recoverable cost split,
- receipt timing by cohort,
- realisation lag,
- cash-pay versus PIK interest,
- interest deferral,
- receipt sweep until funder repayment,
- post-repayment retained margin,
- failed-case allocation.

Label this separately from the generic waterfall model.

## Monte Carlo Contract

If stochastic modelling is requested, specify:

- distributions for damages, timing, settlement discount, and adverse-cost outcomes,
- whether liability and quantum probabilities are separate,
- correlations, if any,
- iteration count,
- random seed,
- calculation tool or method,
- P5/P50/P95 outputs,
- probability of IRR exceeding cost of capital,
- probability of zero recovery for any party,
- catastrophic-loss threshold,
- conditional expected shortfall.

If the calculation cannot actually be run, provide a model specification or pseudocode only.

## Sensitivity Contract

A useful tornado should state:

- metric tested,
- base case,
- movement size (for example, +/-20%),
- each variable changed,
- low/high output,
- absolute impact,
- variables skipped because inputs are missing or inconsistent.

Common sensitivity variables:

- win probability,
- damages mean,
- months to resolution,
- legal hours,
- hourly rate,
- inter partes recovery,
- ATE premium,
- marketing/acquisition cost,
- adverse-cost probability.

## Warning Taxonomy

Use warnings as open items, not hidden assumptions:

- `legal_enforceability_to_verify`
- `professional_conduct_to_verify`
- `tax_vat_to_verify`
- `funding_terms_incomplete`
- `fee_cap_to_verify`
- `paccar_or_percentage_return_to_verify`
- `inconsistent_input_scenario`
- `missing_distribution`
- `cash_timing_missing`
- `portfolio_correlation_missing`

## Audit Bundle

A reusable output should include:

```yaml
scenario_label: string
computed_at: ISO-8601
valuation_date: ISO-8601
currency: string
inputs: {}
assumptions_register: []
deterministic_outputs: {}
waterfall: []
recourse: {}
simulation: null_or_object
sensitivity: null_or_object
warnings: []
not_modelled: []
```

Reproducibility requires inputs, formulas, dates, and calculation method.

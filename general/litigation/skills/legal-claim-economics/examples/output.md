# Example Output

## Scenario

User asks: "Model a 1,000-claim portfolio with a CFA and funder MOIC. I have rough assumptions but no spreadsheet."

Access state: specification/calculation mode. Claude can do arithmetic but has no validated damages distribution or legal enforceability advice.

## Good Output Shape

```yaml
access_mode: calculation_mode
valuation_date: "2026-05-10"
currency: GBP
tax_vat_basis: "excluded unless stated"
real_or_nominal: nominal

assumptions:
  - name: claim_count
    value: 1000
    source: user_supplied
  - name: damages_mean
    value: 12000
    currency: GBP
    source: user_supplied
  - name: win_probability
    value: 0.58
    source: assumption_to_verify
  - name: funder_moic
    value: 2.0
    source: user_supplied
  - name: funded_costs
    value: 1800000
    currency: GBP
    source: user_supplied

calculated_outputs:
  - metric: expected_gross_recovery
    value: 6960000
    currency: GBP
    formula: "claim_count * damages_mean * win_probability"
    calculation: "1000 * 12000 * 0.58"
    confidence: medium
  - metric: funder_entitlement_before_caps
    value: 3600000
    currency: GBP
    formula: "funded_costs * funder_moic"
    calculation: "1800000 * 2.0"
  - metric: residual_before_firm_fees_and_client_distribution
    value: 3360000
    currency: GBP
    formula: "expected_gross_recovery - funder_entitlement_before_caps"
    caveat: "Does not include solicitor fees, ATE, adverse costs, tax/VAT, or distribution waterfall beyond funder entitlement."
    confidence: low

not_modelled:
  - "Funding enforceability not assessed."
  - "CFA/DBA regulatory compliance not assessed."
  - "No Monte Carlo percentiles produced because no damages/time distribution and iteration method supplied."

next_inputs_needed:
  - "Costs budget by phase."
  - "ATE premium and adverse-cost assumptions."
  - "Waterfall priority and caps."
  - "Damages distribution if stochastic modelling is required."
```

## Bad Output To Avoid

```text
This portfolio is commercially viable.
```

Model economics; do not recommend bringing, funding, settling, or abandoning a claim.

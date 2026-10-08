# Basel 3.1 — What Changed from CRR

Master delta summary.

> **Numbers come from the rulepack, not from this page.** The divergence table below is
> generated: it lists *every* parameter carried under both regimes whose value differs,
> computed by comparing the resolved `crr` and `b31` packs. Nothing to maintain, and
> nothing that can silently go stale. Regenerate with
> `uv run python scripts/generate_regulatory_tables.py`.

---

## Structural changes (no single parameter to compare)

These are the changes that a value table cannot express, because the *mechanism* moved
rather than a number:

| Change | Nature of the change |
|--------|----------------------|
| Output floor | New constraint with no CRR analogue — see [output-floor.md](output-floor.md) |
| SME / infrastructure supporting factors | Withdrawn entirely (`supporting_factors` off) |
| IRB scaling factor | Withdrawn (`irb_scaling_factor` moves to unity) |
| A-IRB LGD floors | New floor concept — CRR had none to compare against |
| A-IRB scope | Restricted: large corporates, FIs and institutions become F-IRB only |
| Equity IRB | Removed — SA only, with a transitional phase-in schedule |
| Double default | Removed (`double_default_treatment` off) |
| Real estate | Becomes a standalone exposure class using PRA **loan-splitting** |
| Institution (unrated) | Sovereign-derived weights replaced by the SCRA grade method |
| Retail sub-categories | Transactor and payroll/pension categories introduced |
| CRM method taxonomy | Renamed and scoped: FCM, PSM, LGD-AM — see [crm-changes.md](crm-changes.md) |
| Post-model adjustments | New mandatory concept (Art. 146(3)) with no CRR equivalent |
| Currency mismatch | New multiplier for unhedged retail / RRE (Art. 123B) |

Because the pack names these differently under each regime (`corporate_risk_weights` vs
`b31_corporate_risk_weights`, and so on), structural changes do **not** appear in the
generated table below. For those, read the per-topic reference pages, each of which
carries its own generated tables.

## Every divergent parameter

Entries carried under **both** regimes whose resolved value differs. A blank CRR or
Basel 3.1 cell means the entry is not a simple scalar under that regime.

<!-- BEGIN GENERATED: regime-divergence -->
| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `airb_ead_floor_applies` | off | on | CRR Art. 166 / PS1/26, paragraph 166D |
| `airb_lgd_collateral_method_applicable` | off | on | CRR Art. 181 / PS1/26, paragraph 169A |
| `airb_lgd_floor` | off | on | CRR Art. 164 / PS1/26, paragraph 161 |
| `approach_restrictions_b31_applicable` | off | on | CRR Art. 147 / PS1/26, paragraph 147A |
| `b31_art_124e_three_property_limit_applies` | off | on | CRR Art. 124 / PS1/26, paragraph 124E |
| `b31_exposure_subclass_reporting_applies` | off | on | CRR Art. 147 / PS1/26, paragraph 147A |
| `b31_high_risk_class_applicable` | off | on | CRR Art. 128 / PS1/26, paragraph 128 |
| `ccr_transitional_alpha_addon_applicable` | off | on | CRR Art. 274 / PS1/26, paragraph 274 |
| `central_bank_uses_sovereign_cqs` | off | on | CRR Art. 114 / PS1/26, paragraph 114 |
| `collateral_haircut_maturity_bands_revised` | off | on | CRR Art. 224 / PS1/26, paragraph 224 |
| `crr_non_named_mdb_institution_irb_class` | on | off | CRR Art. 147 / PS1/26, paragraph 147 |
| `crr_retail_re_portfolio_lgd_floor` | on | off | CRR Art. 164 / PS1/26, paragraph 164 |
| `double_default_treatment` | on | off | CRR Art. 153(3) / PS1/26, paragraph 153 |
| `equity_irb_approaches_available` | on | off | CRR Art. 155 / PS1/26, paragraph 133 |
| `equity_revised_sa_risk_weights` | off | on | CRR Art. 133 / PS1/26, paragraph 133 |
| `equity_transitional` | off | on | CRR Art. 133 / PS1/26, paragraph 4.1 |
| `fcsm_equity_collateral_rw` | `1.00` | `2.50` | CRR Art. 222(3) / PS1/26, paragraph 222 |
| `firb_fixed_supervisory_maturity` | on | off | CRR Art. 162(1) / PS1/26, paragraph 162 |
| `firb_fse_senior_lgd_split` | off | on | CRR Art. 161(1)(a) / PS1/26, paragraph 161 |
| `firb_min_collateralisation_threshold_applies` | on | off | CRR Art. 230 / PS1/26, paragraph 230 |
| `firb_overcollateralisation_divisor_applies` | on | off | CRR Art. 230 / PS1/26, paragraph 230 |
| `firb_sft_supervisory_maturity` | on | off | CRR Art. 162(1) / PS1/26, paragraph 162 |
| `firb_uses_sa_ccf` | off | on | CRR Art. 166 / PS1/26, paragraph 166C |
| `irb_correlation_sme_gbp_native` | off | on | CRR Art. 153(4) / PS1/26, paragraph 153 |
| `irb_scaling_factor` | `1.06` | `1.0` | CRR Art. 153(1) / PS1/26, paragraph 153 |
| `mna_intermediate_floor_requires_daily_condition` | off | on | CRR Art. 162(2) / PS1/26, paragraph 162 |
| `one_day_maturity_floor` | on | off | CRR Art. 162(3) / PS1/26, paragraph 162 |
| `output_floor` | off | on | CRR Art. 92 / PS1/26, paragraph 92 |
| `post_model_adjustments` | off | on | CRR Art. 153 / PS1/26, paragraph 154 |
| `re_split_cre_secured_ltv_cap` | `0.50` | `0.55` | CRR Art. 126 / PS1/26, paragraph 124H |
| `re_split_rre_secured_ltv_cap` | `0.80` | `0.55` | CRR Art. 125 / PS1/26, paragraph 124F |
| `regulatory_thresholds_fx_derived` | on | off | CRR Art. 123 / PS1/26, paragraph 147 |
| `retail_art_123a_two_path_applicable` | off | on | CRR Art. 123 / PS1/26, paragraph 123A |
| `revolving_uses_termination_maturity` | off | on | CRR Art. 162 / PS1/26, paragraph 162 |
| `sa_currency_mismatch_multiplier` | off | on | CRR Art. 123 / PS1/26, paragraph 123B |
| `sa_due_diligence_override` | off | on | CRR Art. 110 / PS1/26, paragraph 110A |
| `sa_re_split_art_124_4_all_or_nothing` | off | on | CRR Art. 124 / PS1/26, paragraph 124 |
| `sa_re_split_cre_rental_coverage_required` | on | off | CRR Art. 126 / PS1/26, paragraph 124H |
| `sa_re_split_revised_parameters` | off | on | CRR Art. 125 / PS1/26, paragraph 124F |
| `sa_re_split_whole_loan_path_applies` | off | on | CRR Art. 126 / PS1/26, paragraph 124H |
| `sa_revised_ccf_table` | off | on | CRR Art. 111 / PS1/26, paragraph 111 |
| `sa_revised_defaulted_treatment` | off | on | CRR Art. 127 / PS1/26, paragraph 127 |
| `sa_revised_risk_weight_overrides` | off | on | CRR Art. 112 / PS1/26, paragraph 122 |
| `sa_revised_risk_weight_tables` | off | on | CRR Art. 122 / PS1/26, paragraph 122 |
| `sa_sl_inferred_rating_disapplied` | off | on | CRR Art. 139 / PS1/26, paragraph 139 |
| `sa_unrated_institution_sovereign_floor_applies` | off | on | CRR Art. 121 / PS1/26, paragraph 121 |
| `slotting_revised_tables` | off | on | CRR Art. 153(5) / PS1/26, paragraph 153 |
| `supporting_factors` | on | off | CRR Art. 501 / PS1/26, paragraph 501 |
| `ucp_unilateral_change_ineligible` | off | on | CRR Art. 213 / PS1/26, paragraph 213 |
<!-- END GENERATED: regime-divergence -->

## Direction of travel

Which way a portfolio moves is a question about *composition*, not about any single
parameter, so it stays prose:

| Portfolio type | Direction | Driver |
|---------------|-----------|--------|
| Low-risk IRB | Increase | Output floor binds where models produce thin RWA |
| SME | Increase | Supporting factor withdrawn, only partly offset by the SME weight |
| Infrastructure | Increase | Supporting factor withdrawn |
| Equity | Increase | SA-only treatment at materially higher weights |
| Unhedged FX retail / RE | Increase | New currency-mismatch multiplier |
| Mortgages | Decrease | Loan-splitting is favourable at both low and high LTV |
| High-risk corporate | Decrease | CQS 5 and CQS 3 both improve under Table 6 |
| Retail transactor | Decrease | New sub-category below the base retail weight |
| Standard corporate | Neutral | CQS 1, 2, 4 and 6 unchanged |

---

> **Full detail:** `docs/framework-comparison/key-differences.md`
> **All pack entries:** `docs/data-model/regulatory-tables.md`

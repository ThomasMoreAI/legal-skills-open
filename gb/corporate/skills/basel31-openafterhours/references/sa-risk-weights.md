# Basel 3.1 SA Risk Weights

**Regulatory Reference:** PRA PS1/26 Art. 112-134, BCBS CRE20

> **Every number on this page is generated from the rulepack.** The tables inside
> `<!-- BEGIN/END GENERATED -->` markers are rendered from
> `src/rwa_calc/rulebook/packs/b31.py` by
> `uv run python scripts/generate_regulatory_tables.py`. Do not hand-edit them, and do
> not restate their values in the prose — a wrong value here is a **rulepack finding**,
> not a docs edit. The prose carries what the pack cannot: precedence, scope,
> mechanics, and PRA divergences from BCBS.
>
> Each `### entry_name` heading is the literal pack key. Grep it in `packs/b31.py` to
> reach the cited source, or in `src/rwa_calc/engine/` to find the code that reads it.

---

## Corporate Exposures (Art. 122)

Rated corporates read the CQS table; the short-term ECAI table (Art. 122(3) Table 6A)
applies only where a *dedicated* short-term assessment exists for the exposure.

Three sub-treatments sit on top of the CQS table:

- **Investment-grade** (CRE20.44) applies to *unrated* corporates carrying an
  investment-grade designation — it is not a rating substitute, and it does not apply
  where a CQS is available.
- **SME corporate** (CRE20.47) replaces the CRR combination of a full corporate weight
  plus the SME supporting factor. Because the factor is withdrawn under Basel 3.1, the
  net direction for SMEs is an *increase* despite the lower headline weight.
- **Subordinated debt** (CRE20.49) **overrides all other treatments**, including the
  investment-grade and SME sub-categories.

<!-- BEGIN GENERATED: b31-sa-corporate -->
### `b31_corporate_risk_weights`

**Basel 3.1 only** — PS1/26, paragraph 122
 *((2) Table 6 corporate RW (CQS3 75%, CQS5 150%))*

Key column: `cqs`; default `1.00`

| Key | Value |
|---|---|
| `1` | `0.20` |
| `2` | `0.50` |
| `3` | `0.75` |
| `4` | `1.00` |
| `5` | `1.50` |
| `6` | `1.50` |
| `None` | `1.00` |

### `b31_corporate_short_term_ecai_risk_weights`

**Basel 3.1 only** — PS1/26, paragraph 122
 *((3) Table 6A dedicated short-term ECAI corporate RW)*

Key column: `cqs`; default `1.50`

| Key | Value |
|---|---|
| `1` | `0.20` |
| `2` | `0.50` |
| `3` | `1.00` |
| `4` | `1.50` |
| `5` | `1.50` |
| `6` | `1.50` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `b31_corporate_investment_grade_rw` | — | `0.65` | PS1/26, paragraph 122 |
| `b31_corporate_non_investment_grade_rw` | — | `1.35` | PS1/26, paragraph 122 |
| `b31_corporate_sme_rw` | — | `0.85` | PS1/26, paragraph 122 |
| `b31_subordinated_debt_rw` | — | `1.50` | PS1/26, paragraph 133 |
<!-- END GENERATED: b31-sa-corporate -->

## Institution Exposures (Art. 120-121, CRE20.16-21)

Two mutually exclusive methods, and the precedence matters: **ECRA (rated) takes
precedence over SCRA**. SCRA is reached only where no eligible external assessment
exists — it is not a floor or an alternative the firm may elect.

SCRA replaces the CRR approach of deriving an institution weight from its sovereign's
CQS. Grades are assigned by the firm against published criteria:

| Grade | Criterion (Art. 121) |
|-------|----------------------|
| A | Meets all minimum regulatory requirements plus buffers |
| A (enhanced) | Grade A **and** published CET1 and leverage ratios above the Art. 121(2) thresholds |
| B | Meets minimum requirements but not the buffers |
| C | Below minimum requirements, or an adverse audit opinion |

The enhanced-A thresholds are firm-reported inputs, not pack values — the engine
consumes a resolved `scra_grade`, so the thresholds live in the classification guidance
rather than the rulepack.

<!-- BEGIN GENERATED: b31-sa-institution -->
### `institution_rw_b31_ecra`

**Basel 3.1 only** — PS1/26, paragraph 120
 *(Table 3 ECRA institution RW (CQS2 30%, unrated 40%))*

Key column: `cqs`; default `0.40`

| Key | Value |
|---|---|
| `1` | `0.20` |
| `2` | `0.30` |
| `3` | `0.50` |
| `4` | `1.00` |
| `5` | `1.00` |
| `6` | `1.50` |
| `0` | `0.40` |

### `institution_short_term_rw_b31_ecra`

**Basel 3.1 only** — PS1/26, paragraph 120
 *((2) Table 4 ECRA short-term institution RW)*

Key column: `cqs`; default `0.20`

| Key | Value |
|---|---|
| `1` | `0.20` |
| `2` | `0.20` |
| `3` | `0.20` |
| `4` | `0.50` |
| `5` | `0.50` |
| `6` | `1.50` |
| `0` | `0.20` |

### `b31_ecra_short_term_risk_weights`

**Basel 3.1 only** — PS1/26, paragraph 120
 *((2) Table 4 ECRA short-term (long-term rating, <=3m))*

Key column: `cqs`; default `1.50`

| Key | Value |
|---|---|
| `1` | `0.20` |
| `2` | `0.20` |
| `3` | `0.20` |
| `4` | `0.50` |
| `5` | `0.50` |
| `6` | `1.50` |

### `b31_ecra_short_term_ecai_risk_weights`

**Basel 3.1 only** — PS1/26, paragraph 120
 *((2B) Table 4A dedicated short-term ECAI institution RW)*

Key column: `cqs`; default `1.50`

| Key | Value |
|---|---|
| `1` | `0.20` |
| `2` | `0.50` |
| `3` | `1.00` |
| `4` | `1.50` |
| `5` | `1.50` |

### `b31_scra_risk_weights`

**Basel 3.1 only** — PS1/26, paragraph 120
 *(SCRA long-term institution RW by grade (CRE20.18-21))*

Key column: `scra_grade`; default `1.50`

| Key | Value |
|---|---|
| `A` | `0.40` |
| `A_ENHANCED` | `0.30` |
| `B` | `0.75` |
| `C` | `1.50` |

### `b31_scra_short_term_risk_weights`

**Basel 3.1 only** — PS1/26, paragraph 120
 *(Art. 120A SCRA short-term institution RW by grade)*

Key column: `scra_grade`; default `1.50`

| Key | Value |
|---|---|
| `A` | `0.20` |
| `A_ENHANCED` | `0.20` |
| `B` | `0.50` |
| `C` | `1.50` |
<!-- END GENERATED: b31-sa-institution -->

## Covered Bonds (Art. 129)

Rated covered bonds use their own table. Unrated covered bonds derive from the issuing
institution's treatment — under Basel 3.1 that derivation runs off the issuer's **SCRA
grade**, where CRR derived it from the issuer's CQS.

<!-- BEGIN GENERATED: b31-sa-covered-bond -->
### `b31_covered_bond_risk_weights`

**Basel 3.1 only** — PS1/26, paragraph 129
 *((4) Table 7 covered-bond RW (= CRR Table 6A))*

Key column: `cqs`; default `1.00`

| Key | Value |
|---|---|
| `1` | `0.10` |
| `2` | `0.20` |
| `3` | `0.20` |
| `4` | `0.50` |
| `5` | `0.50` |
| `6` | `1.00` |

### `b31_covered_bond_unrated_from_scra`

**Basel 3.1 only** — PS1/26, paragraph 129
 *((5) unrated CB RW direct from issuer SCRA grade)*

Key column: `scra_grade`; default `1.00`

| Key | Value |
|---|---|
| `A_ENHANCED` | `0.15` |
| `A` | `0.20` |
| `B` | `0.35` |
| `C` | `1.00` |

### `covered_bond_unrated_derivation_b31`

**Basel 3.1 only** — PS1/26, paragraph 129
 *((5) unrated CB derivation from issuer RW (7-input))*

Key column: `issuer_institution_rw`; default `1.00`

| Key | Value |
|---|---|
| `0.20` | `0.10` |
| `0.30` | `0.15` |
| `0.40` | `0.20` |
| `0.50` | `0.25` |
| `0.75` | `0.35` |
| `1.00` | `0.50` |
| `1.50` | `1.00` |
<!-- END GENERATED: b31-sa-covered-bond -->

## Real Estate (Art. 124E-124K)

Real estate becomes a standalone exposure class. The single most important divergence:

> **The PRA uses loan-splitting, not the BCBS whole-loan table**, for real estate that is
> *not* materially dependent on cash flows generated by the property. Do not design a
> scenario against the BCBS CRE20.71 whole-loan grid for the general case — it does not
> apply in the UK.

**Loan-splitting** (general RRE Art. 124F, general CRE Art. 124H) weights the portion up
to the secured LTV cap at a fixed secured weight, and the residual at the counterparty's
own weight:

```
secured_share = min(1.0, secured_ltv_cap / LTV)
RW            = secured_rw x secured_share + counterparty_RW x (1.0 - secured_share)
```

Both parameters are pack entries (`*_secured_rw`, `re_split_*_secured_ltv_cap`), so the
formula is stated here with names rather than literals on purpose.

**Whole-loan LTV bands** (Art. 124G RRE, Art. 124I CRE) apply instead where the exposure
*is* materially dependent on property cash flows — buy-to-let being the common case. A
junior charge attracts a multiplier above the Art. 124G(2) LTV threshold.

For general CRE to counterparties other than natural persons and SMEs, the result is
floored and capped against the income-producing outcome:
`max(cre_floor_rw, min(counterparty_RW, income_producing_RW))`.

`b31_art_124e_three_property_limit_applies` gates the Art. 124E limit on the number of
financed residential properties above which an exposure leaves the retail-adjacent
treatment.

<!-- BEGIN GENERATED: b31-sa-real-estate -->
| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `b31_residential_general_secured_rw` | — | `0.20` | PS1/26, paragraph 124F |
| `b31_residential_general_max_secured_ratio` | — | `0.55` | PS1/26, paragraph 124F |
| `re_split_rre_secured_ltv_cap` | `0.80` | `0.55` | CRR Art. 125 / PS1/26, paragraph 124F |
| `b31_rre_residual_rw_natural_person` | — | `0.75` | PS1/26, paragraph 124L |
| `b31_rre_residual_rw_retail_sme` | — | `0.75` | PS1/26, paragraph 124L |
| `b31_rre_residual_rw_other_sme` | — | `0.85` | PS1/26, paragraph 124L |
| `b31_rre_residual_rw_social_housing_floor` | — | `0.75` | PS1/26, paragraph 124L |
| `b31_rre_three_property_limit` | — | `3` | PS1/26, paragraph 124E |
| `b31_art_124e_three_property_limit_applies` | off | on | CRR Art. 124 / PS1/26, paragraph 124E |

### `b31_residential_income_ltv_bands`

**Basel 3.1 only** — PS1/26, paragraph 124G
 *(Table 6B income-producing RRE LTV bands)*

Input column: `ltv` (band applies when input <= bound)

| Upper bound | Value |
|---|---|
| `0.50` | `0.30` |
| `0.60` | `0.35` |
| `0.70` | `0.40` |
| `0.80` | `0.50` |
| `0.90` | `0.60` |
| `1.00` | `0.75` |
| — | `1.05` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `b31_residential_income_junior_ltv_threshold` | — | `0.50` | PS1/26, paragraph 124G |
| `b31_residential_income_junior_multiplier` | — | `1.25` | PS1/26, paragraph 124G |
| `b31_commercial_general_secured_rw` | — | `0.60` | PS1/26, paragraph 124H |
| `b31_commercial_general_max_secured_ratio` | — | `0.55` | PS1/26, paragraph 124H |
| `re_split_cre_secured_ltv_cap` | `0.50` | `0.55` | CRR Art. 126 / PS1/26, paragraph 124H |

### `b31_commercial_income_ltv_bands`

**Basel 3.1 only** — PS1/26, paragraph 124I
 *((1)/(2) income-producing CRE LTV bands)*

Input column: `ltv` (band applies when input <= bound)

| Upper bound | Value |
|---|---|
| `0.80` | `1.00` |
| — | `1.10` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `b31_cre_income_junior_rw_low` | — | `1.00` | PS1/26, paragraph 124I |
| `b31_cre_income_junior_rw_mid` | — | `1.25` | PS1/26, paragraph 124I |
| `b31_cre_income_junior_rw_high` | — | `1.375` | PS1/26, paragraph 124I |
| `b31_other_re_income_dependent_rw` | — | `1.50` | PS1/26, paragraph 124J |
| `b31_other_re_cre_floor_rw` | — | `0.60` | PS1/26, paragraph 124J |
| `b31_adc_risk_weight` | — | `1.50` | PS1/26, paragraph 124K |
| `b31_adc_presold_risk_weight` | — | `1.00` | PS1/26, paragraph 124K |
<!-- END GENERATED: b31-sa-real-estate -->

## Retail Exposures (Art. 123, 123A)

Basel 3.1 adds two sub-categories with no CRR equivalent, both **more favourable** than
the base retail weight:

- **Transactor** — a facility repaid in full at each scheduled date over the preceding
  period, i.e. genuine transactional use rather than revolving credit.
- **Payroll / pension** — lending serviced by a direct deduction from salary or pension.

`retail_art_123a_two_path_applicable` gates the Art. 123A two-path test that decides
whether an exposure qualifies as regulatory retail at all; failing it routes to the
non-regulatory retail weight.

<!-- BEGIN GENERATED: b31-sa-retail -->
| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `retail_risk_weight` | `0.75` | `0.75` | CRR Art. 123 |
| `b31_retail_transactor_rw` | — | `0.45` | PS1/26, paragraph 123 |
| `b31_retail_payroll_loan_rw` | — | `0.35` | PS1/26, paragraph 123 |
| `b31_retail_non_regulatory_rw` | — | `1.00` | PS1/26, paragraph 123 |
| `b31_retail_granularity_limit` | — | `0.002` | PS1/26, paragraph 123 |
<!-- END GENERATED: b31-sa-retail -->

## SA Specialised Lending (Art. 122A-122B)

Rated SL exposures use the **corporate** CQS table. Where no issue-specific rating
exists, `sa_sl_inferred_rating_disapplied` records that Basel 3.1 removes the CRR ability
to infer a rating from the obligor — unrated SL falls to the slotting-style table below
rather than borrowing the obligor's CQS.

<!-- BEGIN GENERATED: b31-sa-specialised-lending -->
### `b31_sa_sl_risk_weights`

**Basel 3.1 only** — PS1/26, paragraph 122A
 *(SA specialised-lending risk weights)*

Key column: `sl_type`

| Key | Value |
|---|---|
| `object_finance` | `1.00` |
| `commodities_finance` | `1.00` |
| `project_finance_pre_operational` | `1.30` |
| `project_finance_operational` | `1.00` |
| `project_finance_high_quality` | `0.80` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `sa_sl_inferred_rating_disapplied` | off | on | CRR Art. 139 / PS1/26, paragraph 139 |
<!-- END GENERATED: b31-sa-specialised-lending -->

## Defaulted Exposures (Art. 127)

The weight turns on specific credit risk adjustments as a proportion of the unsecured
part of the exposure, measured against the provision threshold. Residential real estate
not dependent on property cash flows carries its own fixed weight in default,
irrespective of the provision level.

<!-- BEGIN GENERATED: b31-sa-defaulted -->
| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `b31_defaulted_provision_threshold` | — | `0.20` | PS1/26, paragraph 127 |
| `b31_defaulted_rw_high_provision` | — | `1.00` | PS1/26, paragraph 127 |
| `b31_defaulted_rw_low_provision` | — | `1.50` | PS1/26, paragraph 127 |
| `b31_defaulted_resi_re_non_income_rw` | — | `1.00` | PS1/26, paragraph 127 |
| `sa_revised_defaulted_treatment` | off | on | CRR Art. 127 / PS1/26, paragraph 127 |
<!-- END GENERATED: b31-sa-defaulted -->

## Equity and Other Items (Art. 133-134)

IRB equity approaches are **removed** — equity is SA-only under Basel 3.1, with a
transitional schedule (see [slotting-changes.md](slotting-changes.md) for the phase-in
entries). Legislative-programme equity and subordinated debt sit outside the standard
and higher-risk buckets.

Other items are structurally unchanged from CRR.

<!-- BEGIN GENERATED: b31-sa-equity-and-other-items -->
### `equity_sa_risk_weights`

**CRR** — CRR Art. 133
 *(Art. 133(2) 100% flat / Art. 132(2) CIU 1250%)*

Key column: `equity_type`; default `1.00`

| Key | Value |
|---|---|
| `central_bank` | `0.00` |
| `subordinated_debt` | `1.00` |
| `listed` | `1.00` |
| `exchange_traded` | `1.00` |
| `government_supported` | `1.00` |
| `unlisted` | `1.00` |
| `speculative` | `1.00` |
| `private_equity` | `1.00` |
| `private_equity_diversified` | `1.00` |
| `ciu` | `12.50` |
| `other` | `1.00` |

**Basel 3.1** — PS1/26, paragraph 133
 *(Art. 133(3)-(5) equity SA RW 250%/400%/150%)*

Key column: `equity_type`; default `2.50`

| Key | Value |
|---|---|
| `central_bank` | `0.00` |
| `subordinated_debt` | `1.50` |
| `listed` | `2.50` |
| `exchange_traded` | `2.50` |
| `government_supported` | `2.50` |
| `unlisted` | `2.50` |
| `speculative` | `4.00` |
| `private_equity` | `4.00` |
| `private_equity_diversified` | `4.00` |
| `ciu` | `12.50` |
| `other` | `2.50` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `other_items_cash_rw` | `0.00` | `0.00` | CRR Art. 134 |
| `other_items_gold_rw` | `0.00` | `0.00` | CRR Art. 134 |
| `other_items_collection_rw` | `0.20` | `0.20` | CRR Art. 134 |
| `other_items_tangible_rw` | `1.00` | `1.00` | CRR Art. 134 |
| `other_items_default_rw` | `1.00` | `1.00` | CRR Art. 134 |
<!-- END GENERATED: b31-sa-equity-and-other-items -->

## Currency Mismatch (Art. 123B)

An unhedged retail or residential-RE exposure where the borrower's income currency
differs from the loan currency attracts a multiplier on the risk weight, subject to a
cap. `b31_currency_mismatch_hedge_coverage_floor` sets the hedge proportion below which
the exposure counts as unhedged. This is a Basel 3.1 amendment with **no CRR equivalent**
— cite it as `PS1/26, paragraph 123B`, not as a CRR article.

<!-- BEGIN GENERATED: b31-sa-currency-mismatch -->
| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `sa_currency_mismatch_multiplier` | off | on | CRR Art. 123 / PS1/26, paragraph 123B |
| `b31_currency_mismatch_multiplier` | — | `1.5` | PS1/26, paragraph 123B |
| `b31_currency_mismatch_rw_cap` | — | `1.50` | PS1/26, paragraph 123B |
| `b31_currency_mismatch_hedge_coverage_floor` | — | `0.90` | PS1/26, paragraph 123B |
<!-- END GENERATED: b31-sa-currency-mismatch -->

---

> **Full detail:** `docs/specifications/crr/sa-risk-weights.md` (covers both CRR + Basel 3.1)
> **All pack entries:** `docs/data-model/regulatory-tables.md`

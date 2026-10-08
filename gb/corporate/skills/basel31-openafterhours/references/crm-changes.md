# Basel 3.1 CRM Changes

**Regulatory Reference:** PRA PS1/26 Art. 191A, BCBS CRE22

> Values are generated from the rulepack — see the tables below. Regenerate with
> `uv run python scripts/generate_regulatory_tables.py`.
>
> ⚠️ **Citation caution:** `docs/assets/` contains **no PRA Credit Risk Mitigation (CRR)
> Part**. PS1/26-side CRM citations therefore cannot be verified against a local PDF —
> cite the CRR article and the pack entry, and treat any PS1/26 paragraph number in CRM
> prose as unverified unless you have the rulebook text to hand.

---

## Method Taxonomy (Art. 191A)

Basel 3.1 renames and re-scopes the methods. The names changed more than the mechanics:

| Method | CRR equivalent | Applies to |
|--------|----------------|-----------|
| Financial Collateral Simple (FCSM) | Same | SA only |
| Financial Collateral Comprehensive (FCCM) | Same | SA + IRB |
| **Foundation Collateral Method (FCM)** | Scattered IRB collateral articles | F-IRB |
| **Parameter Substitution Method (PSM)** | Art. 236 substitution | F-IRB, unfunded |
| **LGD Adjustment Method (LGD-AM)** | Art. 183 | A-IRB, unfunded |

Note that Art. 199 collateral eligibility is **IRB-only**. SA property collateral is
recognised through the real-estate risk weight itself, not through the CRM chain — a
recurring source of double-counting when mapping to COREP C 07.00.

## Haircuts

The maturity band structure expands under Basel 3.1
(`collateral_haircut_maturity_bands_revised`), and equity and gold haircuts rise. The
`collateral_haircuts` decision table is keyed by collateral type, CQS and maturity band,
so read the whole key rather than a single axis.

`zero_haircut_max_sovereign_cqs` bounds which sovereign collateral qualifies for a zero
haircut; `fx_haircut` is the currency-mismatch haircut (CRR Art. 224 / CRE22.54), and is
**unchanged** between regimes.

<!-- BEGIN GENERATED: crm-haircuts -->
### `collateral_haircuts`

**CRR** — CRR Art. 224
 *(FCCM supervisory haircuts Table 1 (3 maturity bands))*

Keys: `collateral_type` , `cqs` , `maturity_band` , `is_main_index`

| Keys | Value |
|---|---|
| `cash`, `None`, `None`, `None` | `0.00` |
| `gold`, `None`, `None`, `None` | `0.15` |
| `govt_bond`, `1`, `0_1y`, `None` | `0.005` |
| `govt_bond`, `1`, `1_5y`, `None` | `0.02` |
| `govt_bond`, `1`, `5y_plus`, `None` | `0.04` |
| `govt_bond`, `2`, `0_1y`, `None` | `0.01` |
| `govt_bond`, `2`, `1_5y`, `None` | `0.03` |
| `govt_bond`, `2`, `5y_plus`, `None` | `0.06` |
| `govt_bond`, `3`, `0_1y`, `None` | `0.01` |
| `govt_bond`, `3`, `1_5y`, `None` | `0.03` |
| `govt_bond`, `3`, `5y_plus`, `None` | `0.06` |
| `govt_bond`, `4`, `0_1y`, `None` | `0.15` |
| `govt_bond`, `4`, `1_5y`, `None` | `0.15` |
| `govt_bond`, `4`, `5y_plus`, `None` | `0.15` |
| `corp_bond`, `1`, `0_1y`, `None` | `0.01` |
| `corp_bond`, `1`, `1_5y`, `None` | `0.04` |
| `corp_bond`, `1`, `5y_plus`, `None` | `0.08` |
| `corp_bond`, `2`, `0_1y`, `None` | `0.02` |
| `corp_bond`, `2`, `1_5y`, `None` | `0.06` |
| `corp_bond`, `2`, `5y_plus`, `None` | `0.12` |
| `corp_bond`, `3`, `0_1y`, `None` | `0.02` |
| `corp_bond`, `3`, `1_5y`, `None` | `0.06` |
| `corp_bond`, `3`, `5y_plus`, `None` | `0.12` |
| `securitisation`, `1`, `0_1y`, `None` | `0.02` |
| `securitisation`, `1`, `1_5y`, `None` | `0.08` |
| `securitisation`, `1`, `5y_plus`, `None` | `0.16` |
| `securitisation`, `2`, `0_1y`, `None` | `0.04` |
| `securitisation`, `2`, `1_5y`, `None` | `0.12` |
| `securitisation`, `2`, `5y_plus`, `None` | `0.24` |
| `securitisation`, `3`, `0_1y`, `None` | `0.04` |
| `securitisation`, `3`, `1_5y`, `None` | `0.12` |
| `securitisation`, `3`, `5y_plus`, `None` | `0.24` |
| `equity`, `None`, `None`, `True` | `0.15` |
| `equity`, `None`, `None`, `False` | `0.25` |
| `real_estate`, `None`, `None`, `None` | `0.00` |
| `receivables`, `None`, `None`, `None` | `0` |
| `other_physical`, `None`, `None`, `None` | `0.40` |

**Basel 3.1** — PS1/26, paragraph 224
 *(Basel 3.1 FCCM supervisory haircuts (5 maturity bands))*

Keys: `collateral_type` , `cqs` , `maturity_band` , `is_main_index`

| Keys | Value |
|---|---|
| `cash`, `None`, `None`, `None` | `0.00` |
| `gold`, `None`, `None`, `None` | `0.20` |
| `govt_bond`, `1`, `0_1y`, `None` | `0.005` |
| `govt_bond`, `1`, `1_3y`, `None` | `0.02` |
| `govt_bond`, `1`, `3_5y`, `None` | `0.02` |
| `govt_bond`, `1`, `5_10y`, `None` | `0.04` |
| `govt_bond`, `1`, `10y_plus`, `None` | `0.04` |
| `govt_bond`, `2`, `0_1y`, `None` | `0.01` |
| `govt_bond`, `2`, `1_3y`, `None` | `0.03` |
| `govt_bond`, `2`, `3_5y`, `None` | `0.03` |
| `govt_bond`, `2`, `5_10y`, `None` | `0.06` |
| `govt_bond`, `2`, `10y_plus`, `None` | `0.06` |
| `govt_bond`, `3`, `0_1y`, `None` | `0.01` |
| `govt_bond`, `3`, `1_3y`, `None` | `0.03` |
| `govt_bond`, `3`, `3_5y`, `None` | `0.03` |
| `govt_bond`, `3`, `5_10y`, `None` | `0.06` |
| `govt_bond`, `3`, `10y_plus`, `None` | `0.06` |
| `govt_bond`, `4`, `0_1y`, `None` | `0.15` |
| `govt_bond`, `4`, `1_3y`, `None` | `0.15` |
| `govt_bond`, `4`, `3_5y`, `None` | `0.15` |
| `govt_bond`, `4`, `5_10y`, `None` | `0.15` |
| `govt_bond`, `4`, `10y_plus`, `None` | `0.15` |
| `corp_bond`, `1`, `0_1y`, `None` | `0.01` |
| `corp_bond`, `1`, `1_3y`, `None` | `0.03` |
| `corp_bond`, `1`, `3_5y`, `None` | `0.04` |
| `corp_bond`, `1`, `5_10y`, `None` | `0.06` |
| `corp_bond`, `1`, `10y_plus`, `None` | `0.12` |
| `corp_bond`, `2`, `0_1y`, `None` | `0.02` |
| `corp_bond`, `2`, `1_3y`, `None` | `0.04` |
| `corp_bond`, `2`, `3_5y`, `None` | `0.06` |
| `corp_bond`, `2`, `5_10y`, `None` | `0.12` |
| `corp_bond`, `2`, `10y_plus`, `None` | `0.20` |
| `corp_bond`, `3`, `0_1y`, `None` | `0.02` |
| `corp_bond`, `3`, `1_3y`, `None` | `0.04` |
| `corp_bond`, `3`, `3_5y`, `None` | `0.06` |
| `corp_bond`, `3`, `5_10y`, `None` | `0.12` |
| `corp_bond`, `3`, `10y_plus`, `None` | `0.20` |
| `securitisation`, `1`, `0_1y`, `None` | `0.02` |
| `securitisation`, `1`, `1_3y`, `None` | `0.08` |
| `securitisation`, `1`, `3_5y`, `None` | `0.08` |
| `securitisation`, `1`, `5_10y`, `None` | `0.16` |
| `securitisation`, `1`, `10y_plus`, `None` | `0.16` |
| `securitisation`, `2`, `0_1y`, `None` | `0.04` |
| `securitisation`, `2`, `1_3y`, `None` | `0.12` |
| `securitisation`, `2`, `3_5y`, `None` | `0.12` |
| `securitisation`, `2`, `5_10y`, `None` | `0.24` |
| `securitisation`, `2`, `10y_plus`, `None` | `0.24` |
| `securitisation`, `3`, `0_1y`, `None` | `0.04` |
| `securitisation`, `3`, `1_3y`, `None` | `0.12` |
| `securitisation`, `3`, `3_5y`, `None` | `0.12` |
| `securitisation`, `3`, `5_10y`, `None` | `0.24` |
| `securitisation`, `3`, `10y_plus`, `None` | `0.24` |
| `equity`, `None`, `None`, `True` | `0.20` |
| `equity`, `None`, `None`, `False` | `0.30` |
| `real_estate`, `None`, `None`, `None` | `0.40` |
| `receivables`, `None`, `None`, `None` | `0.40` |
| `other_physical`, `None`, `None`, `None` | `0.40` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `collateral_haircut_maturity_bands_revised` | off | on | CRR Art. 224 / PS1/26, paragraph 224 |
| `fx_haircut` | `0.08` | `0.08` | CRR Art. 224 |
| `zero_haircut_max_sovereign_cqs` | `1` | `1` | CRR Art. 227 |
| `restructuring_exclusion_haircut` | `0.40` | `0.40` | CRR Art. 233(2) |
| `liquidation_period_repo` | `5` | `5` | CRR Art. 224 |
| `liquidation_period_capital_market` | `10` | `10` | CRR Art. 224 |
| `liquidation_period_secured_lending` | `20` | `20` | CRR Art. 224 |
<!-- END GENERATED: crm-haircuts -->

## Collateral methods and floors

`overcollateralisation_ratios` and `min_collateralisation_thresholds` are the two FCM
gates — the first a divisor on recognised collateral, the second a coverage floor below
which collateral is disregarded entirely. Both are unchanged in value from CRR; what
changed is which regimes apply them (`firb_*_applies` Features).

`life_insurance_secured_rw_map` implements the Art. 212(2)/232(3) treatment of life
policies pledged as collateral. Under Art. 233(3) an FX cut applies where the policy is
denominated in a different currency from the exposure.

<!-- BEGIN GENERATED: crm-collateral-methods -->
### `overcollateralisation_ratios`

**Both regimes** — CRR Art. 230
 *(Table 5 overcollateralisation divisors)*

Key column: `collateral_category`; default `1.0`

| Key | Value |
|---|---|
| `financial` | `1.0` |
| `receivables` | `1.25` |
| `real_estate` | `1.40` |
| `other_physical` | `1.40` |
| `life_insurance` | `1.0` |

### `min_collateralisation_thresholds`

**Both regimes** — CRR Art. 230
 *(minimum collateralisation thresholds)*

Key column: `collateral_category`; default `0.0`

| Key | Value |
|---|---|
| `financial` | `0.0` |
| `receivables` | `0.0` |
| `real_estate` | `0.30` |
| `other_physical` | `0.30` |
| `life_insurance` | `0.0` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `airb_lgd_collateral_method_applicable` | off | on | CRR Art. 181 / PS1/26, paragraph 169A |

### `life_insurance_secured_rw_map`

**Both regimes** — CRR Art. 232
 *((3) life-insurance secured-portion RW map)*

Input column: `insurer_risk_weight` (band applies when input <= bound)

| Upper bound | Value |
|---|---|
| `0.20` | `0.20` |
| `0.50` | `0.35` |
| `1.35` | `0.70` |
| — | `1.50` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `fcsm_rw_floor` | `0.20` | `0.20` | CRR Art. 222(1) |
| `fcsm_equity_collateral_rw` | `1.00` | `2.50` | CRR Art. 222(3) / PS1/26, paragraph 222 |
| `fcsm_sovereign_bond_discount` | `0.20` | `0.20` | CRR Art. 222(4)(b) |
| `fcsm_sft_cmp_floor` | `0.00` | `0.00` | CRR Art. 222(4)(a) |
| `fcsm_sft_non_cmp_floor` | `0.10` | `0.10` | CRR Art. 222(4)(b) |
| `gcra_cap_rate` | — | `0.0125` | PS1/26, paragraph 92 |
| `mna_intermediate_floor_requires_daily_condition` | off | on | CRR Art. 162(2) / PS1/26, paragraph 162 |
<!-- END GENERATED: crm-collateral-methods -->

## Unfunded Credit Protection (Art. 213)

Basel 3.1 adds a second limb to the eligibility test: protection must not be unilaterally
**cancellable *or changeable*** by the provider. The "or change" condition is new —
`ucp_unilateral_change_ineligible` gates it.

**Transitional relief (Rule 4.11):** contracts written before Basel 3.1 commencement may
continue on CRR treatment for a limited period, waiving the "or change" requirement for
legacy contracts only.

Eligible guarantor scope (Art. 201) is an **exhaustive list with no retail limb** — a
retail guarantor is not eligible. Verify the guarantor entity type before designing any
substitution scenario.

---

> **Full detail:** `docs/specifications/crr/credit-risk-mitigation.md` and `docs/framework-comparison/technical-reference.md`
> **All pack entries:** `docs/data-model/regulatory-tables.md`

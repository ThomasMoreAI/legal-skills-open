# Basel 3.1 IRB Changes

**Regulatory Reference:** PRA PS1/26, BCBS CRE30-36

> **Every number on this page is generated from the rulepack.** Tables inside
> `<!-- BEGIN/END GENERATED -->` markers come from `src/rwa_calc/rulebook/packs/`
> via `uv run python scripts/generate_regulatory_tables.py`. A wrong value is a
> **rulepack finding**, not a docs edit. Prose carries scope, precedence and mechanics.

---

## PD and LGD Floors (Art. 163(1), 161(5), 164(4), CRE30.55, CRE32)

Two distinct constraints that are easy to conflate:

- **PD floors** apply under both regimes; Basel 3.1 differentiates them by exposure
  class where CRR used a single uniform floor.
- **A-IRB LGD floors** are *new* — CRR had no LGD floor to compare against. They bind
  after the firm's own LGD estimate and after any collateral recognition.

`airb_lgd_floor` gates whether the LGD-floor machinery runs at all, so a regime check
reads that Feature rather than branching on the regime.

The `lgd_floors` and `pd_floors` bundles are keyed by exposure class and collateral
type. PRA values are used throughout — **BCBS standard values differ**, so a scenario
derived from CRE32 alone will not match the engine.

`mortgage_rw_floor` is a **PRA-specific** post-model floor on non-defaulted retail
exposures secured by UK residential property, applied regardless of model output. It has
no BCBS equivalent; cite it as PS1/26, not CRE.

<!-- BEGIN GENERATED: irb-pd-and-lgd-floors -->
### `pd_floors`

**CRR** — CRR Art. 160(1)
 *(0.03% IRB PD floor for corporates and institutions only (retail floored separately by Art. 163(1); no CGCB floor))*

| Parameter | Value |
|---|---|
| `corporate` | `0.0003` |
| `corporate_sme` | `0.0003` |
| `sovereign` | `0` |
| `institution` | `0.0003` |
| `retail_mortgage` | `0.0003` |
| `retail_other` | `0.0003` |
| `retail_qrre_transactor` | `0.0003` |
| `retail_qrre_revolver` | `0.0003` |

**Basel 3.1** — PS1/26, paragraph 160
 *((1) differentiated IRB PD floors (Art. 160(1) wholesale / 163(1) retail))*

| Parameter | Value |
|---|---|
| `corporate` | `0.0005` |
| `corporate_sme` | `0.0005` |
| `sovereign` | `0.0005` |
| `institution` | `0.0005` |
| `retail_mortgage` | `0.0010` |
| `retail_other` | `0.0005` |
| `retail_qrre_transactor` | `0.0005` |
| `retail_qrre_revolver` | `0.0010` |

### `lgd_floors`

**CRR** — CRR Art. 164
 *(no A-IRB own-estimate LGD floor under CRR (all zero))*

| Parameter | Value |
|---|---|
| `unsecured` | `0.0` |
| `subordinated_unsecured` | `0.0` |
| `financial_collateral` | `0.0` |
| `receivables` | `0.0` |
| `commercial_real_estate` | `0.0` |
| `residential_real_estate` | `0.0` |
| `other_physical` | `0.0` |
| `retail_rre` | `0.0` |
| `retail_qrre_unsecured` | `0.0` |
| `retail_other_unsecured` | `0.0` |
| `retail_lgdu` | `0.0` |

**Basel 3.1** — PS1/26, paragraph 161
 *((5) A-IRB LGD floors (Art. 161(5) corporate / 164(4) retail))*

| Parameter | Value |
|---|---|
| `unsecured` | `0.25` |
| `subordinated_unsecured` | `0.50` |
| `financial_collateral` | `0.0` |
| `receivables` | `0.10` |
| `commercial_real_estate` | `0.10` |
| `residential_real_estate` | `0.10` |
| `other_physical` | `0.15` |
| `retail_rre` | `0.05` |
| `retail_qrre_unsecured` | `0.50` |
| `retail_other_unsecured` | `0.30` |
| `retail_lgdu` | `0.30` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `airb_lgd_floor` | off | on | CRR Art. 164 / PS1/26, paragraph 161 |
| `mortgage_rw_floor` | — | `0.10` | PS1/26, paragraph 154 |
<!-- END GENERATED: irb-pd-and-lgd-floors -->

## F-IRB Supervisory LGD (CRE32, Art. 161)

`firb_supervisory_lgd` is a decision table keyed by seniority and collateral type.
`firb_fse_senior_lgd_split` records the Basel 3.1 split that holds financial sector
entities at the CRR senior level while other corporates move down — the two were a
single row under CRR.

Collateral recognition under the Foundation Collateral Method is governed by two
independent gates, and both must be understood before hand-calculating an LGD*:

- `min_collateralisation_thresholds` — the coverage below which collateral is
  disregarded entirely.
- `overcollateralisation_ratios` — the required collateral-to-exposure ratio applied as
  a divisor to the recognised amount.

<!-- BEGIN GENERATED: irb-firb-supervisory-lgd -->
### `firb_supervisory_lgd`

**CRR** — CRR Art. 161
 *(F-IRB supervisory LGD (Art. 161 / Art. 230 Table 5))*

Keys: `collateral_type` , `seniority` , `is_fse`

| Keys | Value |
|---|---|
| `unsecured`, `senior`, `False` | `0.45` |
| `unsecured`, `senior`, `True` | `0.45` |
| `unsecured`, `subordinated`, `False` | `0.75` |
| `covered_bond`, `senior`, `False` | `0.1125` |
| `financial_collateral`, `senior`, `False` | `0.00` |
| `financial_collateral`, `subordinated`, `False` | `0.00` |
| `receivables`, `senior`, `False` | `0.35` |
| `receivables`, `subordinated`, `False` | `0.65` |
| `residential_re`, `senior`, `False` | `0.35` |
| `residential_re`, `subordinated`, `False` | `0.65` |
| `commercial_re`, `senior`, `False` | `0.35` |
| `commercial_re`, `subordinated`, `False` | `0.65` |
| `other_physical`, `senior`, `False` | `0.40` |
| `other_physical`, `subordinated`, `False` | `0.70` |
| `purchased_receivables`, `senior`, `False` | `0.45` |
| `purchased_receivables`, `subordinated`, `False` | `1.00` |
| `purchased_receivables`, `dilution_risk`, `False` | `0.75` |
| `life_insurance`, `senior`, `False` | `0.40` |

**Basel 3.1** — PS1/26, paragraph 161
 *(Basel 3.1 F-IRB supervisory LGD (CRE32.9-12))*

Keys: `collateral_type` , `seniority` , `is_fse`

| Keys | Value |
|---|---|
| `unsecured`, `senior`, `False` | `0.40` |
| `unsecured`, `senior`, `True` | `0.45` |
| `unsecured`, `subordinated`, `False` | `0.75` |
| `covered_bond`, `senior`, `False` | `0.1125` |
| `financial_collateral`, `senior`, `False` | `0.00` |
| `receivables`, `senior`, `False` | `0.20` |
| `residential_re`, `senior`, `False` | `0.20` |
| `commercial_re`, `senior`, `False` | `0.20` |
| `other_physical`, `senior`, `False` | `0.25` |
| `purchased_receivables`, `senior`, `False` | `0.40` |
| `purchased_receivables`, `subordinated`, `False` | `1.00` |
| `purchased_receivables`, `dilution_risk`, `False` | `1.00` |
| `life_insurance`, `senior`, `False` | `0.40` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `firb_fse_senior_lgd_split` | off | on | CRR Art. 161(1)(a) / PS1/26, paragraph 161 |

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
| `firb_min_collateralisation_threshold_applies` | on | off | CRR Art. 230 / PS1/26, paragraph 230 |

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

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `firb_overcollateralisation_divisor_applies` | on | off | CRR Art. 230 / PS1/26, paragraph 230 |
<!-- END GENERATED: irb-firb-supervisory-lgd -->

## Scaling Factor, Approach Restrictions and PMAs

- **Scaling factor**: CRR computes `RWA = K x 12.5 x EAD x MA x scaling_factor`;
  Basel 3.1 moves the factor to unity, so the term drops out.
- **Approach restrictions** (Art. 147A): Basel 3.1 restricts IRB two ways — complete
  removal (SA only) and A-IRB removal (F-IRB only).

| Exposure type | CRR | Basel 3.1 |
|--------------|-----|-----------|
| Central govts, central banks & quasi-sovereigns | F-IRB or A-IRB | **SA only** |
| Institutions | F-IRB or A-IRB | **F-IRB only** |
| Financial sector entities | F-IRB or A-IRB | **F-IRB only** |
| Large corporates (above the Art. 147A turnover/assets test) | F-IRB or A-IRB | **F-IRB only** |
| IPRE / HVCRE specialised lending | F-IRB, A-IRB or Slotting | **Slotting only** |
| Other SL (object / project / commodities) | F-IRB, A-IRB or Slotting | Unchanged |
| Equity | IRB | **SA only** |

Quasi-sovereign scope (Art. 147(3)) covers regional governments, local authorities,
PSEs, MDBs and international organisations that attract a zero SA weight.

- **Post-model adjustments** (Art. 146(3)) are a new concept covering
  corporate/institution RWA, retail RWA, and expected loss where models do not fully
  comply. PMAs are **included in the output floor calculation base**.

<!-- BEGIN GENERATED: irb-scaling-and-restrictions -->
| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `irb_scaling_factor` | `1.06` | `1.0` | CRR Art. 153(1) / PS1/26, paragraph 153 |
| `approach_restrictions_b31_applicable` | off | on | CRR Art. 147 / PS1/26, paragraph 147A |
| `post_model_adjustments` | off | on | CRR Art. 153 / PS1/26, paragraph 154 |
| `double_default_treatment` | on | off | CRR Art. 153(3) / PS1/26, paragraph 153 |
| `equity_irb_approaches_available` | on | off | CRR Art. 155 / PS1/26, paragraph 133 |
<!-- END GENERATED: irb-scaling-and-restrictions -->

## Maturity (Art. 162)

The floor and cap on effective maturity are unchanged. The behavioural change is for
**revolving facilities**: `revolving_uses_termination_maturity` switches M from the
repayment date of the current drawing to the maximum contractual termination date, which
typically lengthens M and therefore *increases* capital.

Note the separate SFT and collateralised-derivative maturity floors — these are distinct
from the general one-day floor and from the F-IRB fixed supervisory maturity.

<!-- BEGIN GENERATED: irb-maturity -->
| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `firb_fixed_supervisory_maturity` | on | off | CRR Art. 162(1) / PS1/26, paragraph 162 |
| `firb_fixed_supervisory_maturity_years` | `2.5` | `2.5` | CRR Art. 162(1) |
| `firb_sft_supervisory_maturity` | on | off | CRR Art. 162(1) / PS1/26, paragraph 162 |
| `firb_sft_supervisory_maturity_years` | `0.5` | `0.5` | CRR Art. 162(1) |
| `irb_maturity_floor_collateralised_deriv_years` | `0.02739726027397260273972602740` | `0.02739726027397260273972602740` | CRR Art. 162(2) |
| `irb_maturity_floor_repo_sft_years` | `0.01369863013698630136986301370` | `0.01369863013698630136986301370` | CRR Art. 162(2) |
| `one_day_maturity_floor` | on | off | CRR Art. 162(3) / PS1/26, paragraph 162 |
| `one_day_maturity_floor_years` | `0.002739726027397260273972602740` | `0.002739726027397260273972602740` | CRR Art. 162(3) |
| `revolving_uses_termination_maturity` | off | on | CRR Art. 162 / PS1/26, paragraph 162 |
<!-- END GENERATED: irb-maturity -->

## EAD and CCF Floors (CRE32.27)

A-IRB own-estimate CCFs are permitted **only for revolving facilities**; every other
off-balance-sheet item takes the SA CCF. Two independent floors then apply, and both are
multipliers on a base the pack does not itself hold:

- `airb_revolving_ccf_floor_multiplier` — own estimate floored at a proportion of the
  SA CCF for the same item type.
- `airb_obs_floor_b_multiplier` with `airb_ead_floor_applies` — EAD floored at drawn
  plus a proportion of the off-balance-sheet amount at the F-IRB CCF.

<!-- BEGIN GENERATED: irb-ead-and-ccf-floors -->
| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `airb_ead_floor_applies` | off | on | CRR Art. 166 / PS1/26, paragraph 166D |
| `airb_obs_floor_b_multiplier` | — | `0.5` | PS1/26, paragraph 166D |
| `airb_revolving_ccf_floor_multiplier` | — | `0.5` | PS1/26, paragraph 166D |
| `firb_uses_sa_ccf` | off | on | CRR Art. 166 / PS1/26, paragraph 166C |
<!-- END GENERATED: irb-ead-and-ccf-floors -->

## FI Correlation Multiplier

**Unchanged between regimes**: the correlation multiplier for large or unregulated
financial sector entities (CRR Art. 153(2) / BCBS CRE31.5) is a formula constant in
`engine/irb/`, not a pack entry, because it is invariant across both regimes.

---

> **Full detail:** `docs/framework-comparison/key-differences.md` and `docs/specifications/crr/airb-calculation.md`
> **All pack entries:** `docs/data-model/regulatory-tables.md`

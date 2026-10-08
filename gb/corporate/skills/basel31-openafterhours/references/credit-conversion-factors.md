# Basel 3.1 Credit Conversion Factors

**Regulatory Reference:** PRA PS1/26 Art. 111, 166C, 166D

> Values are generated from the rulepack — see the table below. Regenerate with
> `uv run python scripts/generate_regulatory_tables.py`.

---

## The structural change

Under CRR the three approaches carried **separate CCF schedules**. Basel 3.1 collapses
them onto one:

- **SA** (Art. 111, Table A1) — the master table. `sa_ccf` is keyed by risk category.
- **F-IRB** (Art. 166C) — no longer has its own schedule. `firb_uses_sa_ccf` records that
  F-IRB now reads SA Table A1 directly. The CRR-era F-IRB entries
  (`firb_credit_line_ccf`, `firb_trade_lc_ccf`, `firb_obs_fallback_ccf`) survive in the
  pack for the CRR regime only.
- **A-IRB** (Art. 166D) — own estimates restricted to revolving facilities; everything
  else takes the SA CCF, subject to the floors in
  [irb-changes.md](irb-changes.md#ead-and-ccf-floors-cre3227).

Two category-level changes drive most of the impact:

1. **Unconditionally cancellable commitments** move off a zero CCF for the first time.
2. **Other commitments (OC)** becomes a real category. Under CRR these had no separate
   row and were classified by maturity — over one year to Medium Risk, one year or under
   to Medium-Low Risk. Basel 3.1 replaces that maturity split with a single flat OC
   factor, which is why `oc_short_maturity_ccf` and `oc_short_maturity_threshold_days`
   are CRR-shaped entries.

`obs_product_to_risk_type` is the map from product string to risk category — the
classification step that decides *which* CCF applies, and the usual source of a wrong
answer when a hand-calc disagrees with the engine.

`sa_revised_ccf_table` is the Feature gating the revised table; `ucp_unilateral_change_ineligible`
records the Basel 3.1 tightening of what counts as unconditionally cancellable.

<!-- BEGIN GENERATED: ccf-values -->
### `sa_ccf`

**CRR** — CRR Art. 111
 *(SA CCFs (Annex I): FR/FRC 100%, MR/OC 50%, MLR 20%, LR 0%)*

Key column: `risk_type`

| Key | Value |
|---|---|
| `FR` | `1.00` |
| `FRC` | `1.00` |
| `MR` | `0.50` |
| `MR_ISSUED` | `0.50` |
| `OC` | `0.50` |
| `MLR` | `0.20` |
| `LR` | `0.00` |

**Basel 3.1** — PS1/26, paragraph 111
 *(Table A1 SA CCFs (OC 40% Row 5, LR/UCC 10% Row 6))*

Key column: `risk_type`

| Key | Value |
|---|---|
| `FR` | `1.00` |
| `FRC` | `1.00` |
| `MR` | `0.50` |
| `MR_ISSUED` | `0.50` |
| `OC` | `0.40` |
| `MLR` | `0.20` |
| `LR` | `0.10` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `sa_revised_ccf_table` | off | on | CRR Art. 111 / PS1/26, paragraph 111 |

### `obs_product_to_risk_type`

**Both regimes** — CRR Art. 111
 *(Annex I OBS product -> risk_type bucket)*

Key column: `obs_product`

| Key | Value |
|---|---|
| `ACCEPTANCE` | `FR` |
| `PERFORMANCE_BOND` | `MLR` |
| `WARRANTY` | `MLR` |
| `TENDER_BOND` | `MLR` |
| `BID_BOND` | `MLR` |
| `DOCUMENTARY_CREDIT` | `MLR` |
| `TRADE_LC` | `MLR` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `oc_short_maturity_ccf` | `0.20` | `0.20` | CRR Art. 111 |
| `oc_short_maturity_threshold_days` | `365` | `365` | CRR Art. 111 |
| `firb_uses_sa_ccf` | off | on | CRR Art. 166 / PS1/26, paragraph 166C |
| `firb_credit_line_ccf` | `0.75` | — | CRR Art. 166 |
| `firb_trade_lc_ccf` | `0.20` | — | CRR Art. 166 |

### `firb_obs_fallback_ccf`

**CRR** — CRR Art. 166
 *((10) F-IRB fallback: FR 100%, MR/OC 50%, MLR 20%, LR 0%)*

Key column: `risk_type`; default `0.50`

| Key | Value |
|---|---|
| `FR` | `1.00` |
| `FRC` | `1.00` |
| `MR` | `0.50` |
| `MR_ISSUED` | `0.50` |
| `OC` | `0.50` |
| `MLR` | `0.20` |
| `LR` | `0.00` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `airb_revolving_ccf_floor_multiplier` | — | `0.5` | PS1/26, paragraph 166D |
| `airb_ead_floor_applies` | off | on | CRR Art. 166 / PS1/26, paragraph 166D |
| `airb_obs_floor_b_multiplier` | — | `0.5` | PS1/26, paragraph 166D |
| `ucp_unilateral_change_ineligible` | off | on | CRR Art. 213 / PS1/26, paragraph 213 |
<!-- END GENERATED: ccf-values -->

---

> **Full detail:** `docs/specifications/crr/credit-conversion-factors.md`
> **All pack entries:** `docs/data-model/regulatory-tables.md`

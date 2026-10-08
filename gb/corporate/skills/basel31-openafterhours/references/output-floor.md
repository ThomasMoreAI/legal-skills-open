# Basel 3.1 Output Floor

**Regulatory Reference:** PRA PS1/26 Art. 92(5)

> Numbers come from the rulepack — see the generated schedule below. Regenerate with
> `uv run python scripts/generate_regulatory_tables.py`.

---

## Core Formula

```
TREA = max(U-TREA, x * S-TREA + OF-ADJ)
```

- **U-TREA** — un-floored total risk exposure, using internal models where permitted
- **S-TREA** — standardised total risk exposure, the *entire* portfolio recalculated on SA
- **x** — the floor percentage for the reporting year (`output_floor_pct` schedule)
- **OF-ADJ** — adjustment reconciling IRB expected loss against SA credit risk adjustments

## OF-ADJ

The two regimes account for provisions differently: under IRB an expected-loss shortfall
adds to capital requirements, while under SA general credit risk adjustments reduce the
risk exposure amount. Without OF-ADJ the comparison would not be like-for-like.

## Worked mechanic

Left symbolic on purpose — substitute `x` from the generated schedule for the reporting
year rather than copying a number into a scenario:

```
S-TREA (SA basis)   = 100
U-TREA (IRB basis)  =  30

CRR:        final TREA = 30                     (no floor)
Basel 3.1:  final TREA = max(30, 100x + OF-ADJ)  -> the floor binds whenever 100x > 30
```

The floor binds for portfolios where models produce materially thinner RWA than the SA
recalculation — low-risk, high-quality, heavily IRB-modelled books.

## Pack entries

`output_floor` is the Feature gating the whole mechanism; `output_floor_pct` is the
date-stepped transitional schedule; `output_floor_pct_full` is the fully phased value.
Regime behaviour must read the Feature — never branch on `config.is_basel_3_1`
(arch_check check 17).

<!-- BEGIN GENERATED: output-floor-values -->
| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `output_floor` | off | on | CRR Art. 92 / PS1/26, paragraph 92 |

### `output_floor_pct`

**Basel 3.1 only** — PS1/26, paragraph 92
 *((5))*

Before first step: `0.0`

| Effective date | Value |
|---|---|
| 2027-01-01 | `0.60` |
| 2028-01-01 | `0.65` |
| 2029-01-01 | `0.70` |
| 2030-01-01 | `0.725` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `output_floor_pct_full` | — | `0.725` | PS1/26, paragraph 92 |
| `own_funds_to_rwa_factor` | `12.5` | `12.5` | CRR Art. 92 |
<!-- END GENERATED: output-floor-values -->

## Calculator Implementation

The SA risk-weight pipe runs **unconditionally** over the whole portfolio — including
IRB exposures — to produce the S-TREA leg. This is load-bearing and routinely
misunderstood: "no IRB code reads this column" is almost always wrong, because the SA
functions are themselves IRB consumers via the floor. The comparison is then applied at
the aggregation stage.

Note also that `rwa_final` is **already post-floor**; adding a floor impact on top of it
double-counts.

---

> **Full detail:** `docs/framework-comparison/technical-reference.md` and `docs/framework-comparison/key-differences.md`
> **All pack entries:** `docs/data-model/regulatory-tables.md`

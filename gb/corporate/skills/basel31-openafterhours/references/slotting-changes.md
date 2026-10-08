# Basel 3.1 Slotting Changes

**Regulatory Reference:** BCBS CRE33, PRA PS1/26

> Values are generated from the rulepack — see the tables below. Regenerate with
> `uv run python scripts/generate_regulatory_tables.py`.

---

## Structural change — and two PRA divergences from BCBS

**UK CRR:** a single Non-HVCRE table (Art. 153(5) Table 1) with two maturity bands.
HVCRE has **no UK legal basis** — the EU CRR Table 2 was not retained on onshoring.

**Basel 3.1 (PRA):** two tables, Non-HVCRE and HVCRE, each keeping the two-maturity-band
structure. The maturity discount survives on both.

The two divergences that will break a scenario derived from BCBS alone:

1. **HVCRE is re-introduced** as a distinct table (PS1/26 Art. 153(5) Table A) with
   elevated weights relative to Non-HVCRE.
2. **Project finance is consolidated** under Non-HVCRE. The PRA does **not** adopt the
   BCBS separate pre-operational PF table — pre-operational PF uses the standard
   Non-HVCRE table. (`slotting_rw_preop` exists in the pack for the BCBS-shaped case;
   check which path the engine takes before assuming it applies.)

## Maturity bands and subgrades

`slotting_short_maturity_threshold_years` splits the two bands. Within the Strong and
Good categories the subgrades differentiate purely by residual maturity — A and C are
the short band, B and D the long band. The short-maturity table is therefore not a
separate regulatory concept, just the short-band column of the same grid.

Default slots to a zero risk weight and is captured through expected loss instead — the
`slotting_el_*` tables. Reading the RW table alone will understate the capital effect of
a defaulted slotted exposure.

`slotting_guarantee_substitution` gates the shared RWSM substitution and the
Art. 235(1A) EL zeroing on the slotting branch; it is enabled under both regimes.

<!-- BEGIN GENERATED: slotting-tables -->
| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `slotting_revised_tables` | off | on | CRR Art. 153(5) / PS1/26, paragraph 153 |
| `slotting_short_maturity_threshold_years` | `2.5` | `2.5` | CRR Art. 153(5) |

### `slotting_rw_base`

**CRR** — CRR Art. 153(5)
 *(slotting RW, remaining maturity >= 2.5y)*

Key column: `slotting_category`; default `1.15`

| Key | Value |
|---|---|
| `strong` | `0.70` |
| `good` | `0.90` |
| `satisfactory` | `1.15` |
| `weak` | `2.50` |
| `default` | `0.00` |

**Basel 3.1** — PS1/26, paragraph 153
 *((5) Table A slotting RW (>= 2.5y))*

Key column: `slotting_category`; default `1.15`

| Key | Value |
|---|---|
| `strong` | `0.70` |
| `good` | `0.90` |
| `satisfactory` | `1.15` |
| `weak` | `2.50` |
| `default` | `0.00` |

### `slotting_rw_short`

**CRR** — CRR Art. 153(5)
 *(slotting RW, remaining maturity < 2.5y)*

Key column: `slotting_category`; default `1.15`

| Key | Value |
|---|---|
| `strong` | `0.50` |
| `good` | `0.70` |
| `satisfactory` | `1.15` |
| `weak` | `2.50` |
| `default` | `0.00` |

**Basel 3.1** — PS1/26, paragraph 153
 *((5)(d) Table A slotting RW (< 2.5y))*

Key column: `slotting_category`; default `1.15`

| Key | Value |
|---|---|
| `strong` | `0.50` |
| `good` | `0.70` |
| `satisfactory` | `1.15` |
| `weak` | `2.50` |
| `default` | `0.00` |

### `slotting_rw_hvcre`

**CRR** — CRR Art. 153(5)
 *(HVCRE slotting RW, remaining maturity >= 2.5y)*

Key column: `slotting_category`; default `1.15`

| Key | Value |
|---|---|
| `strong` | `0.95` |
| `good` | `1.20` |
| `satisfactory` | `1.40` |
| `weak` | `2.50` |
| `default` | `0.00` |

**Basel 3.1** — PS1/26, paragraph 153
 *((5) Table A HVCRE slotting RW (>= 2.5y))*

Key column: `slotting_category`; default `1.15`

| Key | Value |
|---|---|
| `strong` | `0.95` |
| `good` | `1.20` |
| `satisfactory` | `1.40` |
| `weak` | `2.50` |
| `default` | `0.00` |

### `slotting_rw_hvcre_short`

**CRR** — CRR Art. 153(5)
 *(HVCRE slotting RW, remaining maturity < 2.5y)*

Key column: `slotting_category`; default `1.15`

| Key | Value |
|---|---|
| `strong` | `0.70` |
| `good` | `0.95` |
| `satisfactory` | `1.40` |
| `weak` | `2.50` |
| `default` | `0.00` |

**Basel 3.1** — PS1/26, paragraph 153
 *((5)(d) Table A HVCRE slotting RW (< 2.5y))*

Key column: `slotting_category`; default `1.15`

| Key | Value |
|---|---|
| `strong` | `0.70` |
| `good` | `0.95` |
| `satisfactory` | `1.40` |
| `weak` | `2.50` |
| `default` | `0.00` |

### `slotting_rw_preop`

**Basel 3.1 only** — PS1/26, paragraph 153
 *((5) Table A pre-operational PF (= operational))*

Key column: `slotting_category`; default `1.15`

| Key | Value |
|---|---|
| `strong` | `0.70` |
| `good` | `0.90` |
| `satisfactory` | `1.15` |
| `weak` | `2.50` |
| `default` | `0.00` |

### `slotting_el_base`

**CRR** — CRR Art. 158(6)
 *(slotting EL rate, remaining maturity >= 2.5y)*

Key column: `slotting_category`; default `0.028`

| Key | Value |
|---|---|
| `strong` | `0.004` |
| `good` | `0.008` |
| `satisfactory` | `0.028` |
| `weak` | `0.08` |
| `default` | `0.50` |

**Basel 3.1** — PS1/26, paragraph 158
 *((6) Table B slotting EL rate (>= 2.5y))*

Key column: `slotting_category`; default `0.028`

| Key | Value |
|---|---|
| `strong` | `0.004` |
| `good` | `0.008` |
| `satisfactory` | `0.028` |
| `weak` | `0.08` |
| `default` | `0.50` |

### `slotting_el_short`

**CRR** — CRR Art. 158(6)
 *(slotting EL rate, remaining maturity < 2.5y)*

Key column: `slotting_category`; default `0.028`

| Key | Value |
|---|---|
| `strong` | `0.0` |
| `good` | `0.004` |
| `satisfactory` | `0.028` |
| `weak` | `0.08` |
| `default` | `0.50` |

**Basel 3.1** — PS1/26, paragraph 158
 *((6) Table B slotting EL rate (< 2.5y))*

Key column: `slotting_category`; default `0.028`

| Key | Value |
|---|---|
| `strong` | `0.0` |
| `good` | `0.004` |
| `satisfactory` | `0.028` |
| `weak` | `0.08` |
| `default` | `0.50` |

### `slotting_el_hvcre`

**CRR** — CRR Art. 158(6)
 *(HVCRE slotting EL rate (flat, no maturity split))*

Key column: `slotting_category`; default `0.028`

| Key | Value |
|---|---|
| `strong` | `0.004` |
| `good` | `0.004` |
| `satisfactory` | `0.028` |
| `weak` | `0.08` |
| `default` | `0.50` |

**Basel 3.1** — PS1/26, paragraph 158
 *((6) Table B HVCRE slotting EL rate (flat))*

Key column: `slotting_category`; default `0.028`

| Key | Value |
|---|---|
| `strong` | `0.004` |
| `good` | `0.004` |
| `satisfactory` | `0.028` |
| `weak` | `0.08` |
| `default` | `0.50` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `slotting_guarantee_substitution` | on | on | CRR Art. 235 / PS1/26, paragraph 235 |
<!-- END GENERATED: slotting-tables -->

---

> **Full detail:** `docs/specifications/crr/slotting-approach.md` and `docs/framework-comparison/technical-reference.md`
> **All pack entries:** `docs/data-model/regulatory-tables.md`

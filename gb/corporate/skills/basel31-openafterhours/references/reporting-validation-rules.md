# Basel 3.1 Reporting Validation Rules (BoE)

The Bank of England publishes the **XBRL taxonomy validation rules** that are run against a
submitted PRA return. They are the authoritative statement of which cross-cell, cross-sheet and
cross-template identities the OF templates must satisfy — far larger and more specific than
anything we assert in-house.

**Companion reference:** [reporting-changes.md](reporting-changes.md) covers *what* changed in the
templates (C -> OF renames, new columns, new rows); this file covers *what must tie out* once
they are generated.

---

## Where the files live

| What | Path / command |
|------|----------------|
| Raw zip (gitignored) | `docs/assets/boe-banking-taxonomy-validations-v4.0.0.zip` |
| Extracted workbook (gitignored) | `docs/assets/boe-validation-rules-banking-reporting-v4.0.0.xlsx` |
| Member extracted from the zip | `Bank of England Banking Taxonomy Validations Banking reporting v4.0.0.xlsx` |
| Refresh both | `uv run python scripts/download_docs.py` |
| Committed extract (credit risk only) | `src/rwa_calc/reporting/validations/rules/basel31-boe-v4.0.0-credit-risk.json` (package data — ships in the wheel) |
| Regenerate the extract | `uv run python scripts/extract_validation_rules.py` (`--check` to verify it is current) |
| Extract provenance / schema | `docs/reference/validation-rules/index.md` |
| Source URL | https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/regulatory-reporting/banking/2026/february/boebankingtaxonomyvalidationsv400.zip |
| Publisher landing page | https://www.bankofengland.co.uk/prudential-regulation/regulatory-reporting/regulatory-reporting-banking-sector |

`download_docs.py` fetches the zip and extracts the single workbook member automatically. Both
are gitignored — **read the committed JSON extract first**; open the workbook only for a rule the
extract does not carry.

The extract is `{source, filter, rules}`; each rule carries `id`, `severity`, `severity_modules`,
`status`, `tables`, `expression` (simplified) and `expression_raw`, `precondition`, `scope`,
`short_label`, `description`, and `eba_equivalent` / `eba_equivalents` — the cross-reference into
the EBA set is a first-class field, no label parsing needed.

## Which sheet to read

The workbook has two sheets: `Note` and `banking_reporting`.

> **Read sheet `banking_reporting`** — the "Banking reporting v4" module, which is where the
> **OF** tables live. Every credit-risk rule we care about is on it.

Load-bearing columns:

| Column | Use |
|--------|-----|
| `Rule code` | the rule id, e.g. `boe_b0190` |
| `Scope` | row/column/z expansion for whole-table rules |
| `Expression` | the raw, fully-annotated XBRL form |
| `Simplified Expression` | the same rule, readable — **start here** |
| `Precondition` / `Simplified Precondition` | guard that must hold for the rule to fire — **empty for every matched credit-risk rule** |
| `Severity and modules` | e.g. `ERROR - PRA001` |
| `Label` | `SHORT_LABEL(en)` plain-English intent + `DESCRIPTION(en)` EBA equivalent id |
| `Error message` | the message a firm sees, with the scope inlined |
| `Deactivated`, `Include in XBRL` | liveness |
| `T1`…`T4` | the tables the rule touches |

## Coverage of our estate

Rules touching the credit-risk templates we generate (OF02, OF07, OF08, OF09, plus the retained
C 08.04 / C 09.04 / C 34.x codes):

The extract carries all 820 matched rules with a `status` marker — **filter on `status` before
counting anything**.

| Measure | Count |
|---------|-------|
| Rules matching a credit-risk template | **820** |
| Of which deactivated | **0** — none are switched off |
| **`status == ["live"]`** — the primary basis used throughout this page | **808** |
| The remainder, flagged `not_in_xbrl` (published, not machine-enforced) | 12 |

A `not_in_xbrl` rule is **published and substantively binding, but not machine-enforced at
submission** — it will not reject a return. Lower priority for us than an ERROR, but not dead.
Everything below counts on the strict `["live"]` basis, with the all-820 figure shown alongside
wherever the two differ.

| Measure | `["live"]` (808) | all 820 |
|---------|------------------|---------|
| Severity **ERROR** | **514** | 514 |
| Severity **WARNING** | **294** | 306 |
| References **only** credit-risk templates (incl. C 34.x / OF34.07) | **795** | 807 |
| Of those, references only the OF templates we generate **declaratively** (excludes C 34.x / OF34, still imperative) | **680** | 681 |
| Reaches outside credit risk entirely (C 01.00, C 03.00, C 04.00, OF24, OF25) | 13 | 13 |

Every one of the 12 `not_in_xbrl` rules is a WARNING — the ERROR count is identical on both bases.

> **No reactivation trap here — checked, not assumed.** The EBA workbook has a `Reactivated on`
> column, and 153 EBA rules that look `deactivated` are actually in force because of it (see the
> [`crr` skill](../../crr/references/reporting-validation-rules.md)). The BoE workbook has **no
> reactivation concept at all**: there is no such column, the extract carries no `reactivated_on`
> field, and all 820 rules show `Deactivated: no`. So for the BoE set `status == ["live"]` is
> safe, and 808 / 820 is the whole story.

Heaviest cross-template families (live rules naming both tables; identical counts on the all-820
basis):

| Family | Rules |
|--------|-------|
| OF07.00 <-> OF09.01 | 92 |
| OF08.01 <-> OF08.02 | 60 |
| OF08.01 <-> OF34.07 | 51 |
| OF08.01 <-> OF09.02 | 44 |
| OF02.00 <-> OF08.01 | 33 |

The OF08.01 <-> OF34.07 family lands on the C 34.x counterparty-credit-risk estate, which is
still imperative and not fully generated — those 51 are not yet evaluable end-to-end.

## Severity semantics

| Severity | Supervisory convention |
|----------|------------------------|
| **ERROR** | **Blocks the submission.** A return failing an ERROR rule is rejected — treat a break as a bug in our template, not a tolerance question. |
| **WARNING** | Submission is accepted but the firm must **explain the break** to the supervisor. A WARNING break is still a finding worth reporting. |

The value is written `ERROR - PRA001|` — `PRA001` is the reporting module the severity applies
to, not part of the severity.

## Cross-referencing the EBA rules

**427 of the 820** matched rules name their **EBA equivalent** in the label's `DESCRIPTION(en)`
segment — roughly half, so expect to find one but do not rely on it:

```
Label: SHORT_LABEL(en) - ORIGINAL EXPOSURE PRE CONVERSION FACTORS cross-template consistency …|
       DESCRIPTION(en) - v5745_q|
```

The JSON extract lifts this into the `eba_equivalent` field, so no label parsing is needed.
`v5745_q` is an EBA rule id — look it up in the `crr` skill's
[reporting-validation-rules.md](../../crr/references/reporting-validation-rules.md) to see how
the same identity is expressed under CRR. This is the cheapest way to tell whether a Basel 3.1
tie is a genuine change or the same rule renumbered.

**A live BoE rule can name an EBA rule that looks dead — and usually it is not.** 188 of the 427
equivalents are marked `deactivated` or `deleted` on the EBA side, but **140 of those were
reactivated and are in force**; the EBA `status` is derived from the deactivation date alone and
does not reflect the later `reactivated_on`. Only **48** are genuinely dead under CRR. (One names
an EBA rule outside our credit-risk filter entirely.)

So when the equivalent reads `deactivated`, check `reactivated_on` first:

- **Reactivated → the identity holds under both frameworks.** `v5745_q` (this example) was
  deactivated 2018-03-09 and reactivated 2018-04-17. Concluding that CRR dropped it would be
  wrong.
- **Genuinely dead → the identity is new or restored under Basel 3.1.** `boe_b0755` / `boe_b0756`
  cite `v10664_m` / `v10665_m`, both deactivated 2021-03-10 with no reactivation.

## Formula grammar

Fully qualified, XBRL-ish, no free axes in the expression itself:

| Syntax | Meaning |
|--------|---------|
| `{t: OF07.00.01.01, …}` | **table** id (4-part taxonomy id; `OF02.01.01.01` and `OF02.01.01.02` are different tables) |
| `r: 0010` | **row** |
| `c: 0010` | **column**; `c: 0020; 0035; 0040` = a column set |
| `z: 0002` | **z-axis sheet** — the per-exposure-class sheet |
| `filter: [eba_dim:CEG] = [eba_GA:x1]` | dimensional filter (here, geography) |
| `sum({t: …, c: 0110})` | aggregate over the unfixed axis |
| `isNull({t: …})` | the referenced cells must be empty |
| `if (…) then … else true()` | conditional rule — vacuously true when the guard fails |
| `i=`, `i>=`, `i<=`, `i>` | **interval (rounding-tolerant) comparison**, raw `Expression` only |
| `dv:`, `seq:`, `id:`, `f:`, `fv:` | annotations present only in the raw `Expression` (default value, sequence, variable id, framework) — the `Simplified Expression` strips them |

Two traps in the simplified form:

- The `Simplified Expression` collapses `i=` to `=`, **losing the tolerance semantics** — 653 of
  the 808 live rules use an interval operator in their raw expression. Read `expression`, but
  implement against `expression_raw` when the comparison is close.
- The `Precondition` columns are **empty for every matched credit-risk rule** — a rule's guard,
  where it has one, is the inline `if (…) then … else true()` in the expression itself.

**Scope expansion.** When the expression names a table with no row/column (e.g. `{t: OF08.01.01.01}
<= 0`), the `Scope` column supplies the expansion:

```
scope({t: OF08.01.01.01,
       r: 0001;0010;0017;…;0200,
       c: 0035;0040;0050;0060;0070;0102;0103;0290,
       z: 0001;0002;0006;…;0024})
```

The rule is then evaluated once per row x column x sheet in that scope.

> **An expression on its own is often not a rule.** `{t: OF08.01.01.01} <= 0` says nothing until
> the `scope(...)` is applied — never read, quote or implement an expression without it. The EBA
> set has the same hazard in a different shape: 178 of its 741 enforced formulas carry no row
> reference and 222 no column reference, because the domain lives in sibling `rows` / `columns`
> columns instead. The difference between the two publishers is purely **presentational**.

## Worked examples

All verified against sheet `banking_reporting` of the v4.0.0 workbook (Simplified Expression
quoted).

### `boe_b0190` — cross-template consistency, **WARNING**, OF09.01 <-> OF07.00

```
{t: OF09.01.01.01, r: 0010, c: 0010, filter: [eba_dim:CEG] = [eba_GA:x1]}
  = {t: OF07.00.01.01, r: 0010, c: 0010, z: 0002}
```

*"ORIGINAL EXPOSURE PRE CONVERSION FACTORS cross-template consistency for s0002 Central Gov or
Central Banks"* — EBA equivalent `v5745_q`. The geographic breakdown filtered to one country
group must equal the corresponding OF07 exposure-class sheet. This family is 92 rules, one per
(class, column) pair.

### `boe_b0563` / `boe_b0564` — RWEA identity, **ERROR**, OF02.00 <-> OF08.01

```
{t: OF02.00.01.01, r: 0355, c: 0010} = {t: OF08.01.01.01, r: 0010, c: 0260, z: 0023}
{t: OF02.00.01.01, r: 0356, c: 0010} = {t: OF08.01.01.01, r: 0010, c: 0260, z: 0011}
```

*"Total RWEA should be the same for the relevant exposure class across the templates"* — the
published, **per-class** form of our aggregate `irb_rwea_c08_01_vs_c02` tie-out. Each OF02.00
class row equals one OF08.01 sheet's total-row RWEA.

### `boe_b0724` — row roll-up, **ERROR**, OF02.01 (output floor)

```
{t: OF02.01.01.01, r: 0080, c: 0010}
  = sum({t: OF02.01.01.01, r: 0010; 0020; 0030; 0040; 0050; 0070, c: 0010})
```

The output-floor comparison template's total row is the sum of its component rows — note row
0060 is **excluded** from the sum. `boe_b0725` is the sibling for table `OF02.01.01.02`
(different row set, column 0020).

### `boe_b0306` — sign rule, **ERROR**, OF08.01

```
{t: OF08.01.01.01} <= 0
scope: r: 0001;0010;0017;…;0200  c: 0035;0040;0050;0060;0070;0102;0103;0290  z: 0001;…;0024
```

*"Referenced data entries should be less than or equal to zero"* — EBA equivalent `v2041_s`.
The value-adjustment / provision columns are reported **negative**; a sign-convention slip on
those carriers breaks a blocking rule across every row and sheet.

### `boe_b0755` / `boe_b0756` — guarded cross-template equality, **ERROR**, OF08.01 <-> OF08.02

```
{t: OF08.01.01.01, r: 0070, c: 0010} * sum({t: OF08.02.01.01, c: 0110})
  = sum({t: OF08.02.01.01, c: 0010}) * sum({t: OF08.02.01.01, c: 0110})
```

EBA equivalents `v10664_m` / `v10665_m`. Both sides carry the same `sum(c0110)` factor, so the
rule reduces to *"OF08.01 row 0070 column 0010 equals the OF08.02 column-0010 total"* — and goes
**vacuous** when that factor is zero. The multiply-through is how the taxonomy expresses a guarded
identity without a division. `boe_b0756` is the same shape for column 0230 with the guard
`sum(c0110) - sum(c0140)`. When one of these breaks, check the guard before the identity.

### `boe_b0206` — emptiness rule, **WARNING**, OF08.01

```
isNull({t: OF08.01.01.01, r: 0080,
        c: 0020; 0035; …; 0300,
        z: 0001; 0006; 0009; …; 0024})
```

*"slotting is only available for specialised lending exposures"* — EBA equivalent `v10673_m`.
Row 0080 must be **empty** across the listed columns on every sheet in the z-set. Emptiness rules
are the easiest to break by writing a structural zero where the taxonomy expects a null.

## Mapping a rule onto our generated frames

Our COREP frames are Polars `DataFrame`s whose **column names are the COREP column codes** and
which carry a **`row_ref`** column of zero-padded 4-digit row ids:

| Rule reference | Our frame |
|----------------|-----------|
| `{t: T, r: 0010, c: 0200}` | `<t_frame>.filter(pl.col("row_ref") == "0010")["0200"]` |
| `c: 0020; 0035; 0040` | the same row across several columns |
| `z: 0002` | the **per-exposure-class sheet** is a separate frame in the template bundle (e.g. `bundle.of08_01[<class>]`) |
| `sum({t: T, c: 0110})` | `<t_frame>["0110"].sum()` over the rule's row scope |
| `filter: [eba_dim:CEG] = …` | the geographic partition — a row/sheet selector on OF09.0x |

That correspondence is exact, which is what makes the published rules directly runnable against
our output — see the `_cell` / `_rows_sum` / `_sheet_total` helpers in
`src/rwa_calc/reporting/tieouts.py` for readers already written in this shape.

## Relationship to our in-house checker

`src/rwa_calc/reporting/tieouts.py` describes itself as "the first in-house analogue of the
supervisory validation rules". It encodes **5 curated ties** (plus 6 recorded
`NonComparablePair`s). The published sets give **1,258** enforced rules evaluable purely from the
templates we generate declaratively today (680 BoE + 578 EBA), rising to **1,481** once the
C 34.x / OF34 counterparty-credit-risk estate joins them (795 BoE + 686 EBA). The BoE figures are
on the `["live"]` (808) basis, the EBA figures on the enforced (741) basis — see the `crr` skill
for why those are the right two bases.

> The published rules are the authority. `tieouts.py` is a small, deliberately curated subset —
> a green tie-out run is not evidence that a template is submission-valid.

Note the complementary strength: `NON_COMPARABLE_PAIRS` records identities that must **not** be
asserted (obligor vs post-substitution basis, PS1/26 Annex XXII). The published rules do not
assert those either — if you find yourself wanting a tie the BoE does not publish, check the
non-comparable list first.

## How to use this when implementing or changing a template

1. **Before** changing an OF template's rows, columns or aggregation, search the extract for the
   table id — the rules tell you which cells are load-bearing for other templates.
2. Treat every **ERROR** rule touching a cell you changed as a required post-condition.
3. Check the `Simplified Expression` first; drop to `Expression` when you need the default value
   (`dv:`), the variable binding, or the interval (`i=`) tolerance.
4. Where a rule quotes an EBA equivalent, diff the two: a changed identity is a real Basel 3.1
   delta and belongs in [reporting-changes.md](reporting-changes.md); an unchanged one means the
   CRR generator's behaviour carries over.
5. If a rule looks unsatisfiable given our data, the answer is usually a **basis** difference —
   confirm against `tieouts.py`'s `NON_COMPARABLE_PAIRS` and the per-template basis decisions in
   `docs/plans/phase7-declarative-reporting.md` section 6 before assuming the rule is wrong.
6. New cross-template ties worth encoding permanently belong in `TIE_OUTS`, quoting the BoE rule
   id in the `regulatory_reference`.

---

> **CRR counterpart:** the EBA publishes the equivalent rules for the C templates — see the `crr`
> skill, [references/reporting-validation-rules.md](../../crr/references/reporting-validation-rules.md).

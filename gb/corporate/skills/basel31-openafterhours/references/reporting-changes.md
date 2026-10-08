# Basel 3.1 Reporting Changes

COREP and Pillar 3 template changes from CRR to Basel 3.1.

> **Once a template is generated, see [reporting-validation-rules.md](reporting-validation-rules.md)**
> for the published BoE validation rules it must satisfy. Do not quote rule counts from
> memory — they move as rules are reactivated. Read the count from
> `src/rwa_calc/reporting/validations/rules/`.

---

## Template Renames

### COREP (Supervisory Reporting)

| CRR (C prefix) | Basel 3.1 (OF prefix) | Purpose |
|----------------|----------------------|---------|
| C 02.00 | OF 02.00 | Own funds requirements |
| — | OF 02.01 | Output floor comparison (**new**) |
| C 07.00 | OF 07.00 | SA credit risk |
| C 08.01 | OF 08.01 | IRB totals |
| C 08.02 | OF 08.02 | IRB by obligor grade |
| C 08.03 | OF 08.03 | IRB by PD ranges |
| C 08.04 | OF 08.04 | IRB RWEA flow |
| C 08.06 | OF 08.06 | Specialised lending slotting |
| C 08.07 | OF 08.07 | Scope of IRB/SA use |
| C 09.01 | OF 09.01 | Geographical breakdown SA |
| C 09.02 | OF 09.02 | Geographical breakdown IRB |

### Pillar 3 (Public Disclosure)

| CRR (UK prefix) | Basel 3.1 (UKB prefix) | Purpose |
|-----------------|----------------------|---------|
| UK OV1 | UKB OV1 | Overview of RWEAs |
| UK CR4 | UKB CR4 | SA exposure & CRM effects |
| UK CR5 | UKB CR5 | SA risk weight allocation |
| UK CR6 | UKB CR6 | IRB by PD range |
| UK CR6-A | UKB CR6-A | Scope of IRB/SA use |
| UK CR10 | UKB CR10 | Slotting exposures |

## Five Key Themes

1. **Removal of capital relief** — supporting factor and double default columns removed
   across all templates
2. **Output floor infrastructure** — new SA-equivalent columns in the IRB templates, plus
   the new OF 02.01 template for the U-TREA vs S-TREA comparison
3. **Greater granularity** — a materially longer SA risk-weight row axis, detailed real
   estate breakdowns, SL sub-categories, corporate sub-rows
4. **Post-model oversight** — new columns for model overlays and regulatory floors
5. **Scope-of-use transparency** — OF 08.07 expands substantially, adding an RWEA
   breakdown by SA reason

## Key Structural Changes

| Area | CRR | Basel 3.1 |
|------|-----|-----------|
| SA risk weight rows | Coarse band axis | Materially expanded band axis |
| SA CCF buckets | Follows the CRR CCF categories | Follows the revised Table A1 categories |
| IRB approach filter | Foundation / Advanced | Foundation / Advanced / **Slotting** |
| SL types in slotting | IPRE and HVCRE combined | HVCRE separated out |
| CR10 sub-templates | PF, IPRE+HVCRE, OF, CF, **Equity** | PF, IPRE, OF, CF, **HVCRE** |

Row and column axes are defined by the published template XLSX, **not** by the
instruction PDFs — band labels in particular exist only in the XLSX. The PD band axis is
also **hierarchical**: parent bands overlap and sum their children, so summing every row
double-counts.

## Pack-held reporting metadata

<!-- BEGIN GENERATED: reporting-template-set -->
### `reporting_template_set`

**CRR** — CRR Art. 430
 *(COREP CR/CCR set per Reg (EU) 2021/451 Annex I; Pillar 3 per Part Eight)*

| Field | Value |
|---|---|
| `corep` | `('c_02_00', 'c07_00', 'c08_01', 'c08_02', 'c08_03', 'c08_04', 'c08_05', 'c08_06', 'c08_07', 'c09_01', 'c09_02', 'c34_01', 'c34_02', 'c34_04', 'c34_08')` |
| `pillar3` | `('ov1', 'cr4', 'cr5', 'cr6', 'cr6a', 'cr7', 'cr7a', 'cr8', 'cr9', 'cr9_1', 'cr10', 'ccr1', 'ccr2', 'ccr3', 'ccr8')` |
| `variant` | `crr` |

**Basel 3.1** — PS1/26, paragraph 430
 *(adds OF 02.01 (output floor) + CMS1/CMS2 to the CRR reporting set)*

| Field | Value |
|---|---|
| `corep` | `('c_02_00', 'c07_00', 'c08_01', 'c08_02', 'c08_03', 'c08_04', 'c08_05', 'c08_06', 'c08_07', 'c09_01', 'c09_02', 'c34_01', 'c34_02', 'c34_04', 'c34_08', 'of_02_01')` |
| `pillar3` | `('ov1', 'cr4', 'cr5', 'cr6', 'cr6a', 'cr7', 'cr7a', 'cr8', 'cr9', 'cr9_1', 'cr10', 'ccr1', 'ccr2', 'ccr3', 'ccr8', 'cms1', 'cms2')` |
| `variant` | `b31` |

| Name | CRR | Basel 3.1 | Citation |
|---|---|---|---|
| `b31_exposure_subclass_reporting_applies` | off | on | CRR Art. 147 / PS1/26, paragraph 147A |
<!-- END GENERATED: reporting-template-set -->

---

> **Full detail:** `docs/framework-comparison/reporting-differences.md` and `docs/framework-comparison/disclosure-differences.md`

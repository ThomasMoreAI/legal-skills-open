# Code Validation Reference

How to validate the medical codes on a bill against the underlying record. Loaded by Step 3 of the parent SKILL.md.

**Authority hierarchy.** AMA CPT codebook (current edition), CMS HCPCS Level II quarterly file, ICD-10-CM Official Guidelines for Coding and Reporting, and NCCI edit files are the only authorities. Never assert a code-text mapping from memory; cite or label `[VERIFY]`.

---

## Code Sets in Scope

| Set | Owner | Range | What It Codes |
|---|---|---|---|
| CPT Category I | AMA | 00100–99499 | Procedures and services with FDA-approved usage |
| CPT Category II | AMA | 0001F–9007F | Performance measurement (informational, $0) |
| CPT Category III | AMA | 0042T–0XXXT | Emerging technology (temporary) |
| HCPCS Level II | CMS | A0000–V9999 | Supplies, drugs, DME, ambulance, prosthetics |
| ICD-10-CM | CDC/NCHS | A00–Z99 | Diagnoses (3–7 chars, 7th char encounter type) |
| ICD-10-PCS | CMS | 7-char alphanumeric | Inpatient procedures only (UB-04) |
| MS-DRG | CMS | 001–999 | Inpatient facility payment grouping |
| Revenue codes | NUBC | 0001–9999 | UB-04 facility line items |

CMS-1500 carries professional fees (CPT/HCPCS). UB-04 carries facility charges (revenue codes + CPT/HCPCS + DRG). Always check the right form for the charge type.

---

## ICD-10-CM Specificity Checks

- **Three-character code alone** is invalid if a four-character or higher subcategory exists. Reject and flag.
- **Seventh character** for injury codes: `A` (initial encounter), `D` (subsequent), `S` (sequela). Mismatch with visit type is a flag.
- **Laterality** — codes with -1 (right), -2 (left), -9 (unspecified). Repeated `-9` use is a documentation-quality flag.
- **External cause codes (V, W, X, Y)** — required by some payers; absence is not necessarily a flag, but presence helps tie to mechanism.

## CPT Documentation Checks

- **E/M (99202–99499).** Under 2021 AMA revisions, level is set by Medical Decision Making (MDM) **or** total time on date of encounter. The chart must support the chosen path.
  - 99203 vs 99204 vs 99205 — patient's documented MDM elements (problems addressed, data reviewed, risk) must match the level billed.
  - Time-based: total time must be documented, not just start/stop.
- **Procedure codes** — operative report or procedure note must describe what the code requires (anatomy, approach, components). Spot-check the verb in the note against the code descriptor.
- **Add-on codes (+)** — only billable with a specified primary code; never standalone.
- **Diagnostic-imaging codes** — body part, modality, and contrast status in the code must match the order and report (e.g., `72148` lumbar MRI without contrast vs. `72149` with contrast vs. `72158` with and without).

## Procedure-to-Diagnosis Match

A billed procedure must have a supporting diagnosis on the claim. Common flag patterns:
- Lumbar MRI billed with cervical-only diagnosis.
- EMG billed with no nerve-distribution complaint documented.
- PT modality with no impairment-supporting diagnosis.
- Surgical procedure with diagnosis added only post-op (check timing of diagnosis entry).

---

## Modifier Misuse Catalog

| Modifier | Meaning | Common Misuse |
|---|---|---|
| `-25` | Significant, separately identifiable E/M same day as procedure | Used to bill an E/M when the encounter was solely for the procedure (upcoding vector) |
| `-59` | Distinct procedural service | Used to override an NCCI edit when services were not actually distinct (unbundling vector) |
| `-XE`, `-XP`, `-XS`, `-XU` | More specific than -59 (separate Encounter / Practitioner / Structure / Unusual) | CMS prefers these over -59; -59 use when an X-modifier fits is a flag |
| `-26` | Professional component (interpretation only) | Billed alongside `-TC` by same entity = double bill if global service was rendered |
| `-TC` | Technical component (equipment/staff only) | Same as above in reverse |
| `-50` | Bilateral procedure | Billed in addition to two unilateral codes = duplicate |
| `-RT` / `-LT` | Right / left | Use of both with `-50` is a duplicate flag |
| `-51` | Multiple procedures (subject to MPPR reduction) | Misapplication or omission affects payment math |
| `-22` | Increased procedural service | Requires documentation of substantially greater work; absent documentation is a flag |
| `-24` | Unrelated E/M during global period | Misused to bill within global when condition is related |
| `-57` | Decision for surgery | Misused on minor procedures (does not apply) |
| `-78` / `-79` | Return to OR (related / unrelated) | Wrong choice changes payment; check operative reason |

**Cross-reference:** tag modifier-misuse findings with the most specific Red Flag ID from `RED-FLAGS-CATALOG.md` — RF-08 (`-25` overuse), RF-09 (`-59`/X overuse), RF-10 (professional/technical double-bill). Roll up to RF-01 (unbundling) or RF-02 (upcoding) where a broader pattern is established; add RF-04 (duplicate billing) only when a modifier misuse actually produces a duplicate charge.

---

## NCCI Edits (Concept Only)

CMS publishes the National Correct Coding Initiative (NCCI) files quarterly:

- **Procedure-to-Procedure (PTP) edits** — code pairs that should not be billed together. Each pair has a Modifier Indicator: `0` (no modifier override allowed), `1` (override allowed with documented distinct service), `9` (deleted).
- **Medically Unlikely Edits (MUEs)** — per-day units-of-service caps per HCPCS code per beneficiary.
- **Add-on Code (AOC) edits** — primary code requirements for each add-on.

**Do not enumerate PTP pairs from memory.** Identify suspect pairs and direct the reader (or a billing expert) to verify against the current NCCI file at CMS. Cite as `[VERIFY: NCCI Q__ 20__]`.

---

## DRG Framing for Inpatient

For UB-04 inpatient bills:
- Facility is paid one bundled DRG payment per admission, not per service.
- A long itemized list of supplies/services on a UB-04 does not multiply the facility payment; do not double-count by adding line items to the DRG amount.
- Professional services (surgeon, anesthesiologist, radiologist, hospitalist) are billed separately on CMS-1500s and are additive to the DRG facility payment.
- Outlier payments and pass-through items can supplement DRGs in specific cases; flag for billing-expert review if relevant.

---

## What This Reference Does NOT Do

- Does not provide a code lookup table (use the AMA CPT codebook or licensed encoder).
- Does not list NCCI PTP pairs or MUE values (use the current CMS quarterly file).
- Does not constitute coding-expert testimony; it identifies issues for an attorney or a CPC/CCS-credentialed billing expert to confirm.

## Anti-Hallucination Rules for Code Work

- Never assert that a CPT/HCPCS/ICD-10 code "means X" without citing the AMA codebook, CMS file, or the chart entry.
- Never invent NCCI edit pairs or MUE thresholds.
- Never assert an E/M level is supported or unsupported without quoting the chart sections that bear on MDM or time.
- When uncertain, mark `[VERIFY: billing expert]` and move on.

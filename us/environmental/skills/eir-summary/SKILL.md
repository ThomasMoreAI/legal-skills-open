---
name: eir-summary
title: Environmental Impact Report Summary
description: Produces legally focused summaries of California Environmental Impact Reports (EIRs) under CEQA and federal Environmental Impact Statements (EISs) under NEPA. Extracts impacts, mitigation, alternatives, and compliance vulnerabilities. Reflects the 2025 CEQA reforms (AB 130 + SB 131) and the April 2025 rescission of CEQ NEPA implementing regulations. Triggers on requests for EIR/EIS summary, CEQA/NEPA review, mitigation analysis, alternatives analysis, cumulative impacts review, permit challenge prep, or administrative record review.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/eir-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: environmental
language: en
tags: [analysis, litigation, regulatory, summarization]
---

# Environmental Impact Report Summary

Condense EIR (CEQA) or EIS (NEPA) technical findings into a legally actionable summary with record citations.

---

## Authority status (read first)

**Both CEQA and NEPA have undergone significant change since 2023.** The summary must reflect the regime in effect when the document under review was prepared *and* note any subsequent change that affects litigation posture or follow-on administrative steps.

### NEPA (federal)

- **Statute:** 42 U.S.C. § 4321 et seq., as amended by the **Fiscal Responsibility Act of 2023** (Pub. L. 118-5, June 3, 2023).
- **§ 4336a** codifies page limits (150 / 300 pages for EIS; 75 pages for EA), 2-year EIS / 1-year EA deadlines, lead/cooperating agency framework, and applicant-prepared documents.
- **CEQ implementing regulations rescinded** — formerly 40 C.F.R. Parts 1500–1508; rescinded effective **April 11, 2025** (Interim Final Rule Feb 25, 2025; Final Rule Jan 8, 2026). **Lead-agency NEPA implementing procedures now control.**
- For EIS preparation specifically, see `environmental-impact-statement`.

### CEQA (California)

- **Statute:** Pub. Resources Code § 21000 et seq.
- **CEQA Guidelines:** 14 Cal. Code Regs. § 15000 et seq. — California Natural Resources Agency administering. **Update pending** following AB 130 / SB 131; expected early 2026. Verify current Guidelines version at draft time.
- **AB 130 (signed June 30, 2025)** — statutory CEQA exemption for qualifying infill housing projects on sites up to 20 acres; substantial streamlining.
- **SB 131 (signed June 30, 2025)** — companion process changes; expanded exemptions for advanced manufacturing and other categories.
- **Earlier reforms:** AB 1633 (2023, infill housing); AB 1307 (2023, noise from non-buyer-occupied housing); SB 423 (2023, SB 35 streamlining extension).

For verification dates and complete authority record, see `references/AUTHORITY-STATUS.md`.

---

## Related skills

- `environmental-impact-statement` — for drafting NEPA EISs (the federal counterpart to this summary skill).
- `environmental-regulation-summaries` — for governing-statute identification and cross-statute coordination.
- `phase-i-esa` — when affected-environment review references site-level Phase I findings.
- `due-diligence-summary` — when EIR/EIS review feeds into a transactional diligence package.
- `litigation-case-strategy` — when the summary is preparation for a CEQA / NEPA challenge.
- `mediation-statement` — for facilitated CEQA-litigation settlement discussions.

---

## Prerequisites

1. Full EIR / EIS with appendices, technical studies, and modeling outputs.
2. Project description materials (maps, site plans, phasing).
3. Lead agency, jurisdiction, and governing statute (CEQA / NEPA / other).
4. Public comment record and agency responses.
5. Thresholds of significance or regulatory standards applied.
6. Mitigation Monitoring and Reporting Program (MMRP), if separate.
7. List of required permits / approvals, if available.
8. **Date the document was prepared** — to determine which version of the regulatory regime applied.

## Workflow

1. Classify document type (CEQA EIR, NEPA EIS, other) and review level (programmatic, tiered, supplemental, addendum, mitigated negative declaration where relevant).
2. **Note the operative regime** — for NEPA, identify whether the document was prepared pre- or post-FRA 2023 amendments, and pre- or post-April 11, 2025 CEQ rescission. For CEQA, identify whether prepared pre- or post-AB 130 / SB 131 (signed June 30, 2025).
3. Extract project snapshot, lead agency, and decision timeline into Executive Overview.
4. Map each resource area into the Environmental Impacts Matrix.
5. Build Alternatives Analysis; identify the environmentally superior alternative.
6. Isolate Significant and Unavoidable Impacts with required findings / overrides.
7. Summarize mitigation measures and enforceability via MMRP.
8. Extract public comments, agency responses, and areas of controversy.
9. Complete the Compliance and Vulnerability Checklist.
10. Compile Source Map for all key findings.

## Output Tables

**Executive Overview**

| Item | Details | EIR/EIS Cite |
|---|---|---|
| Project / Lead Agency / Jurisdiction / Review Type / Decision / Key Issues / Operative Regime | | |

**Project Description**

| Component | Details | EIR/EIS Cite |
|---|---|---|
| Location / Purpose-Need / Scope / Phasing / Land Use-Footprint | | |

**Environmental Impacts Matrix**

One row per resource area (Air Quality, GHG / Climate, Water, Biological, Cultural / Tribal, Geology / Soils, Hazards, Noise, Traffic, Land Use, Utilities, Cumulative, Other).

| Resource Area | Baseline | Method/Model | Impact Finding | Significance Label | Mitigation | Residual Impact | EIR/EIS Cite | Issues |
|---|---|---|---|---|---|---|---|---|

**Alternatives Analysis**

| Alternative | Key Features | Env. Superior? | Impact Comparison | Selection / Reject Rationale | EIR/EIS Cite |
|---|---|---|---|---|---|

Rows: Proposed Project, No Project, each studied alternative.

**Significant and Unavoidable Impacts**

| Impact | Resource Area | Why Unavoidable | Required Findings / Overrides | EIR/EIS Cite |
|---|---|---|---|---|

For CEQA, the Statement of Overriding Considerations under Pub. Resources Code § 21081 must be record-supported.

**Mitigation and MMRP**

| Measure | Enforceable Standard | Timing/Trigger | Monitor | Feasibility | EIR/EIS Cite | Concerns |
|---|---|---|---|---|---|---|

**Public Review and Controversy**

| Topic | Commenter/Agency | Key Critique | Response Adequacy | Expert Split | Litigation Risk | EIR/EIS Cite |
|---|---|---|---|---|---|---|

## Compliance and Vulnerability Checklist

- [ ] Operative regime correctly identified (NEPA pre/post-FRA 2023; pre/post-April 11, 2025 CEQ rescission; CEQA pre/post-AB 130 / SB 131).
- [ ] Baseline data adequate and supported by substantial evidence.
- [ ] Alternatives range reasonable and feasible; no improper elimination.
- [ ] Cumulative impacts analyzed with defined geographic/temporal scope.
- [ ] Significance thresholds disclosed and applied consistently.
- [ ] Mitigation specific, enforceable, and not improperly deferred (CEQA Guidelines § 15126.4 historically; verify post-update Guidelines).
- [ ] Growth-inducing/indirect impacts addressed.
- [ ] Segmentation/piecemealing avoided or justified.
- [ ] Comment responses substantive; expert critiques addressed.
- [ ] Required consultations/permits identified (CWA § 404 post-*Sackett*, CAA, ESA § 7, NHPA § 106, etc.) `[VERIFY]`.
- [ ] Statement of overriding considerations (CEQA, if needed) supported by record (Pub. Resources Code § 21081).
- [ ] Recirculation triggers evaluated for new significant impacts/information (CEQA Guidelines § 15088.5; or NEPA equivalent).
- [ ] (CEQA only) Statutory exemption applicability evaluated under AB 130 / SB 131 if project qualifies.
- [ ] (NEPA only) Lead-agency procedures correctly identified and applied; not citing 40 CFR Parts 1500–1508 as binding for post-April-2025 documents.

## Closing Tables

**Open Questions** — Issue | Why It Matters | Needed Follow-Up

**Source Map** — Finding | EIR/EIS Section | Page/Exhibit

---

## 2025 CEQA reforms — what to flag in summaries of California documents

AB 130 + SB 131 (signed June 30, 2025) constitute the most significant CEQA reforms in over half a century. When summarizing a California EIR or related CEQA document:

- **Statutory infill housing exemption.** AB 130 establishes a CEQA exemption for qualifying infill housing projects on sites up to 20 acres meeting specified criteria. Where the document under review pre-dates AB 130, note that the exemption framework now exists and may apply to similar future projects.
- **Advanced manufacturing exemption.** SB 131 expands exemptions for advanced manufacturing and certain other categories.
- **Process streamlining.** Reduced procedural hurdles, clearer timelines, and expanded categorical exemptions for transit-oriented and climate-resilient projects.
- **CEQA Guidelines update pending.** California Natural Resources Agency expected to update CEQA Guidelines in early 2026 to implement AB 130 / SB 131; pin-cites to current Guidelines should carry a `[VERIFY post-update]` marker.
- **Litigation impact.** Existing CEQA case law remains operative; statutory exemptions create new affirmative defenses and may moot pending challenges to projects that newly qualify for exemption.

---

## Pitfalls

- Use the document's exact significance labels; do not normalize or reword.
- Cite every material finding to section and page/exhibit.
- Write "Not found in EIR/EIS" for missing data; never fill gaps.
- Separate fact from inference; label inference explicitly.
- Flag unclear jurisdiction or governing statute for clarification.
- Mark uncertain citations or regulatory triggers with `[VERIFY]`.
- Maintain neutral, analytical tone; no advocacy or conclusions of law.
- **Date sensitivity.** A summary of a pre-FRA-2023 NEPA EIS, or pre-AB 130 CEQA EIR, may interact differently with current law than the documents themselves do. Always note the operative regime.

---

## Troubleshooting

- **CEQA document references CEQA Guidelines section that has been amended.** Identify both the version cited and the version in force at the date of the summary; note any material change. The Guidelines pre- and post-AB 130 / SB 131 implementation may differ on key points.
- **NEPA document cites 40 CFR Parts 1500–1508 throughout.** This is normal for documents prepared before April 11, 2025. Note the operative regime (pre-rescission) in the summary header. Do not editorially substitute lead-agency procedure citations into a finalized document — describe what the document says.
- **Project may qualify for new CEQA exemption post-AB 130.** Note the potential applicability of the new statutory exemption as a separate observation; do not declare the prior CEQA review unnecessary unless the lead agency has formally invoked the exemption.
- **Document is a Mitigated Negative Declaration, not an EIR.** Use the same skill but apply the MND-specific standard of review (fair-argument standard); flag the difference prominently in the Executive Overview.
- **Programmatic EIR/EIS with tiered later-tier projects.** Distinguish between programmatic-level analysis (broad, policy-level) and project-level analysis (specific, site-level). Tiering errors are a frequent litigation target.
- **Stale baseline.** If the project description or baseline data significantly post-dates the document's preparation, note as a Recirculation trigger candidate (CEQA Guidelines § 15088.5; NEPA equivalent).

---

## References

- `references/AUTHORITY-STATUS.md` — date-stamped record of authoritative sources consulted.

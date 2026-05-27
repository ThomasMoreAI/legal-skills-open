---
name: environmental-regulation-summaries
title: Environmental Regulation Summary
description: Generates structured summaries of U.S. environmental laws, compliance obligations, and permitting requirements for specific industries or projects. Covers federal statutes (CAA, CWA, RCRA, CERCLA, NEPA as amended by FRA 2023, ESA, TSCA), state analogs, and local requirements. Maps regulations to business activities including permitting, reporting, monitoring, and penalties (referencing 40 CFR § 19.4 inflation-adjusted maximums). Reflects post-Sackett WOTUS scope, PFAS CERCLA designation, CEQ regulation rescission (effective April 11, 2025), and TSCA PFAS reporting. Use when advising on environmental compliance, assessing regulatory exposure, onboarding to a regulated industry, or building compliance programs for manufacturing, energy, construction, agriculture, mining, or waste management.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/environmental-regulation-summaries
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: environmental
language: en
tags: [regulatory, summary, analysis, summarization]
---

# Environmental Regulation Summary

Identifies applicable environmental laws, compliance obligations, and permitting requirements for a defined industry, activity, or project. Produces a structured regulatory matrix, media-specific obligations, and a permitting roadmap. Detailed regulatory matrix and permitting tables live in `references/REGULATORY-MATRIX.md`; SKILL.md retains the workflow and core orientation.

---

## Related skills

- `phase-i-esa` — for Phase I ESA / AAI compliance under CERCLA.
- `consent-decree-epa` — for federal enforcement settlement drafting.
- `nov-response` — for responding to agency Notices of Violation.
- `environmental-impact-statement` — for NEPA EIS preparation.
- `eir-summary` — for CEQA/NEPA EIR/EIS review.
- `compliance-summaries` — for cross-sector compliance posture summaries.
- **Permit-specific skills**: `npdes-permit-application`, `spcc-plan`, `swppp`, `tri-form-r`, `hazardous-waste-manifest`, `asbestos-abatement-plan`, `lead-paint-disclosure`.
- **Real-property cleanup skills**: `brownfields-agreement`, `environmental-indemnity`, `environmental-covenant-and-easement`, `conservation-easement`.

---

## Prerequisites

Gather before starting:

1. **Industry or activity** — manufacturing, energy, construction, agriculture, mining, waste management, or other.
2. **Jurisdiction** — federal only, specific state(s), local, or multi-jurisdictional.
3. **Environmental media** — air emissions, water discharge, hazardous waste, land use, wildlife, or combination.
4. **Project description** (if applicable) — type, scale, activities triggering regulatory review.
5. **Regulatory currency** — confirm review against `references/AUTHORITY-STATUS.md` and re-verify any item older than 12 months.

## Quick Start

1. Collect prerequisites above.
2. Build the regulatory matrix from `references/REGULATORY-MATRIX.md` (federal statutes + state analogs).
3. Map compliance obligations by environmental media.
4. Draft permitting roadmap with timelines.
5. Run the compliance checklist.
6. Flag all uncertain citations with `[VERIFY]`; for civil penalty figures, cite **40 CFR § 19.4** as the authoritative annual table rather than embedding stale dollar amounts.

## Output Structure

### 1. Executive Overview

- Top 3–5 most critical applicable regulations.
- Imminent compliance deadlines or high-penalty areas.
- Recent or pending regulatory changes affecting operations.
- Authority date — note the verification date so the reader knows the freshness of the analysis.

### 2. Regulatory Matrix

See `references/REGULATORY-MATRIX.md` for the federal-statute matrix with current citations, agency, triggers, key obligations, and pointers to the inflation-adjusted civil penalty table. Add applicable state analog statutes below each federal entry.

### 3. Compliance Obligations by Media

**Air**: Emission standards (MACT, NSPS, SIP), permit type (Title V, minor source, synthetic minor), monitoring/recordkeeping/reporting.

**Water**: NPDES individual vs. general permit; stormwater (SWPPP, CGP, MS4); Section 404/401 certification triggers. Note that *Sackett v. EPA*, 598 U.S. 651 (2023) narrowed CWA jurisdiction over wetlands; the post-*Sackett* conforming WOTUS rule (effective Sep 8, 2023) removed the significant-nexus test. Verify whether any wetland feature on the project remains within federal jurisdiction; state and tribal water-quality rules may still apply where federal jurisdiction does not.

**Waste**: Generator category (LQG/SQG/VSQG) and obligations; manifest and storage limits; universal waste applicability. RCRA financial assurance for TSD facilities at 40 C.F.R. Parts 264/265 Subpart H.

**Land/Site**: Brownfield and voluntary cleanup programs; SPCC plan triggers; EPCRA Tier I/II reporting thresholds; CERCLA reporting (release of hazardous substance ≥ RQ in 24-hour period). PFOA and PFOS were designated as CERCLA hazardous substances effective July 8, 2024 — verify current 40 CFR § 302.4 list.

### 4. Permitting Roadmap

See `references/REGULATORY-MATRIX.md` for permit-by-permit timelines and pre-application steps.

### 5. Compliance Checklist

```
- [ ] All applicable permits identified and obtained/applied for
- [ ] Monitoring and recordkeeping systems operational
- [ ] Reporting schedule calendared (annual / semi-annual / quarterly)
- [ ] Emergency response plan current (SPCC, RMP if applicable)
- [ ] Employee training documented
- [ ] Regulatory change tracking process established
- [ ] PFAS exposure evaluation (where industry implicates AFFF, electroplating, textiles, paper, fluoropolymers, etc.)
- [ ] Authority sources re-verified within last 12 months
```

## Recent regulatory developments (2023–2026)

The matrix in `references/REGULATORY-MATRIX.md` already reflects these; this section gives readers a single-glance summary of what has shifted recently:

- **Sackett v. EPA (May 25, 2023)** — narrowed CWA jurisdiction over wetlands; "significant nexus" test rejected. EPA-Army Corps conforming rule effective Sep 8, 2023.
- **Fiscal Responsibility Act of 2023 (Pub. L. 118-5, June 3, 2023)** — first major NEPA statutory amendments since 1982. Codified page limits and deadlines (42 U.S.C. § 4336a), categorical exclusions (§ 4336c), lead/cooperating agencies (§ 4336a).
- **PFOA / PFOS CERCLA designation** — final rule effective July 8, 2024; codified at 40 CFR § 302.4. Reportable quantity 1 lb / 24 hours.
- **TSCA PFAS reporting rule** — final rule Oct 11, 2023 (40 CFR Part 705) requires manufacturers and importers to report historical PFAS data.
- **CEQ NEPA implementing regulations rescinded** — effective April 11, 2025 (Interim Final Rule Feb 25, 2025; Final Rule Jan 8, 2026). Federal agencies now rely on their own NEPA implementing procedures; 40 CFR Parts 1500–1508 are no longer binding.
- **CEQA reform (California)** — AB 130 + SB 131 signed Jun 30, 2025; statutory exemption for infill housing up to 20 acres; substantial streamlining for housing and infrastructure.

## Pitfalls

- **Jurisdiction layering**: State standards frequently exceed federal minimums — always check state analogs.
- **Strict liability**: CERCLA and many state cleanup laws impose liability regardless of fault — flag prominently.
- **Citizen suits**: CAA, CWA, RCRA, and ESA authorize private enforcement — note third-party litigation risk.
- **Penalty inflation**: EPA adjusts civil penalties annually under the Federal Civil Penalties Inflation Adjustment Act. **Do not embed dollar amounts in deliverables; cite 40 CFR § 19.4 and confirm the current value at draft time.**
- **Permit overlap**: Multiple permits may govern the same activity — check whether integrated permitting is available.
- **Post-Sackett WOTUS uncertainty**: Wetland jurisdictional determinations in flux at agency and circuit-court levels; budget for jurisdictional-determination delays.
- **CEQ rescission**: NEPA process is now agency-specific. Lead-agency NEPA implementing procedures (e.g., USDA at 7 CFR Part 1b; DOE at 10 CFR Part 1021; DOI at 43 CFR Part 46) control where 40 CFR Parts 1500–1508 once did.
- **Not legal advice**: Do not render opinions on ultimate compliance status; recommend environmental counsel for high-risk matters.

---

## Troubleshooting

- **Matrix has more federal statutes than the project triggers.** Tailor the matrix to the project — every entry should be either applicable, conditionally applicable, or explicitly noted as "not triggered, identified for awareness." A bloated matrix loses signal.
- **State analog unclear (state has multiple agencies, overlapping programs).** Identify the lead state agency by program (e.g., CalEPA water boards for CWA analogs; ARB for CAA analogs). When ambiguous, list the candidates and flag for state-counsel input.
- **Civil penalty figures used for client illustration purposes.** Do not embed specific dollar amounts in any deliverable likely to outlive a calendar year. Cite 40 CFR § 19.4 and let the reader pull the current value.
- **Project pre-dates a major regulatory change.** Frame the analysis using the regime in effect at the relevant time (e.g., a release pre-dating CERCLA enactment is a different liability picture than a current release). Cite both the historical and current regime where the matter spans the change.
- **Multiple federal triggers (NEPA + ESA + Section 404 + 106).** Build a separate cross-statute coordination section identifying who is the lead agency, what the joint EIS / consultation strategy is, and what the timing dependencies are.

---

## References

- `references/REGULATORY-MATRIX.md` — federal statute matrix with citations, triggers, obligations, and penalty pointers.
- `references/AUTHORITY-STATUS.md` — date-stamped record of authoritative sources consulted.

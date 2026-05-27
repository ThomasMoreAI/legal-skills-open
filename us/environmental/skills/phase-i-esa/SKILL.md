---
name: phase-i-esa
title: Phase I Environmental Site Assessment Report
description: Drafts ASTM E1527-21 environmental site assessment reports under 40 CFR Part 312. Classifies RECs, CRECs, and HRECs to establish all appropriate inquiries for CERCLA liability protection. Trigger when the user requests a Phase I ESA, environmental site assessment, recognized environmental conditions analysis, ASTM E1527 compliance, or environmental due diligence for property transactions or lending.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/phase-i-esa
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: environmental
language: en
tags: [analysis, drafting, regulatory, transactional]
---

# Phase I Environmental Site Assessment Report

Drafts a Phase I ESA establishing "all appropriate inquiries" under ASTM E1527-21 and 40 CFR Part 312 for CERCLA liability protection. ASTM E1527-21 became EPA-recognized for AAI compliance on Feb 13, 2023; the prior E1527-13 lost AAI recognition on Feb 13, 2024 and is no longer compliant.

---

## Related skills

- `due-diligence-summary` — when the Phase I ESA is part of a broader transactional diligence package.
- `environmental-regulation-summaries` — for governing-statute identification when the site implicates multiple regulatory regimes.
- `environmental-indemnity` and `environmental-covenant-and-easement` — for risk-allocation and institutional-control instruments referenced in the report.
- `brownfields-agreement` — for redevelopment of contaminated sites with Phase I ESA findings.
- `consent-decree-epa` — when the property is subject to a federal cleanup decree.
- `real-estate-transaction-summary` — for whole-transaction memos that incorporate Phase I findings.

## Prerequisites

Collect before drafting:

1. **Property identification** — legal description, address, APN, coordinates, zoning
2. **Client purpose** — acquisition, lending, corporate compliance, or other
3. **Site reconnaissance data** — date, observations, photos, access limitations
4. **Historical sources** — aerial photos, fire insurance maps, city directories, topo maps
5. **Regulatory database results** — federal/state/tribal/local at ASTM search radii
6. **User questionnaires** — owner/occupant questionnaires per ASTM E1527-21
7. **Interview notes** — current/past owners, operators, local officials
8. **EP qualifications** — credentials per 40 CFR § 312.10
9. **Prior reports** (if any) — previous Phase I/II ESAs, remediation docs

## Quick Start

1. Confirm property ID, client purpose, and transaction timeline.
2. Verify all prerequisite data is available; flag missing items as data gaps.
3. Draft each report section sequentially per the structure below.
4. Classify every identified condition as REC, CREC, HREC, or de minimis.
5. State conclusions unambiguously; recommend Phase II if any RECs found.

## Report Sections

| # | Section | Key Requirements |
|---|---------|-----------------|
| 1 | Title Page | Property legal description, address, APN, coordinates; preparer info; report/effective dates; client; project ID; confidentiality notice |
| 2 | Table of Contents | All sections, appendices, figures, tables with page refs |
| 3 | Executive Summary | 2-3 pages max; non-technical; state RECs/CRECs/HRECs or explicitly none; scope; data gaps; recommendations |
| 4 | Introduction & Scope | Client purpose; ASTM E1527-21 conformance statement; inclusions/exclusions; non-scope items evaluated |
| 5 | Site Description | Acreage; structures; USTs/ASTs; topography; surface water; current operations; surrounding area (1-mi radius); geology/hydrogeology |
| 6 | User-Provided Information | Questionnaire responses; completeness/credibility assessment; data gaps from non-response |
| 7 | Historical Use Review | Timeline from first developed use or 1940 (whichever earlier); aerial photo analysis (5-10 yr intervals); adjoining property history |
| 8 | Site Reconnaissance | Date/duration/weather; interior/exterior observations; drains, sumps, staining, drums, tanks, PCB equipment; access limitations |
| 9 | Interviews | Each interviewee: name, title, affiliation, contact, date, method; substantive findings; credibility assessment |
| 10 | Regulatory Records | Results at required search distances; orphan site analysis; data gap discussion |
| 11 | Findings: RECs/CRECs/HRECs | Each condition with factual basis, evidence sources, ASTM classification |
| 12 | Conclusions & Recommendations | Unambiguous determination; Phase II recs if warranted; data gap implications; counsel referral for liability |
| 13 | De Minimis & Non-Scope | De minimis conditions; non-scope items (ACM, LBP, radon, mold, wetlands); vapor intrusion evaluation |
| 14 | References | All sources by category with full citations |
| 15 | EP Qualifications | Credentials per 40 CFR § 312.10; education, certifications, experience |
| 16 | Appendices | Site maps, photos, questionnaires, database reports, historical docs, prior reports |

## Condition Classifications

| Type | Definition | Must Include |
|------|-----------|-------------|
| **REC** | Presence or likely presence of hazardous substances/petroleum due to release, indicative conditions, or material threat of future release | Factual basis; evidence sources; contaminant ID |
| **CREC** | Past release addressed via risk-based corrective action with residual contamination under institutional/engineering controls | Residual contamination; specific controls; regulatory status; monitoring requirements |
| **HREC** | Past release remediated to unrestricted use; no residual contamination or controls | Historical condition; remediation performed; regulatory closure docs |

## Regulatory Database Search Distances

| Database | Subject | 1/8 mi | 1/4 mi | 1/2 mi | 1 mi |
|----------|:---:|:---:|:---:|:---:|:---:|
| NPL | ✓ | ✓ | ✓ | ✓ | ✓ |
| CERCLIS/SEMS | ✓ | ✓ | — | ✓ | — |
| RCRA CORRACTS | ✓ | ✓ | — | — | — |
| RCRA TSD | ✓ | — | — | ✓ | — |
| RCRA LQG/SQG | ✓ | ✓ | — | — | — |
| ERNS | ✓ | — | — | — | — |
| State equivalents | ✓ | Per state | Per state | Per state | — |
| Landfill/solid waste | ✓ | — | — | ✓ | — |

## Historical Use Red Flags

Flag current or historical presence of: gas stations, automotive repair, dry cleaners, metal plating/finishing, chemical manufacturing/storage, printing/photo processing, fill placement/waste disposal, agricultural operations (pesticides).

**PFAS-relevant uses** (added priority since 2024 CERCLA designation): firefighter training areas / AFFF storage or use, military bases and airports (AFFF), electroplating / metal finishing, textile manufacturing / coating, paper manufacturing, semiconductor manufacturing, certain landfills accepting industrial waste, chemical-manufacturing facilities producing fluoropolymers, ski-wax storage. See `references/PFAS-AND-EMERGING-CONTAMINANTS.md`.

## PFAS and emerging contaminants

ASTM E1527-21 expects the environmental professional to evaluate emerging contaminants where relevant to the property. EPA designated **PFOA and PFOS** (and their salts and structural isomers) as **CERCLA hazardous substances** by final rule effective **July 8, 2024** (89 FR 39124, May 8, 2024; codified at 40 CFR § 302.4). The reportable quantity is 1 lb in any 24-hour period.

Practical implications for the REC analysis:

- A historical release of PFOA or PFOS now meets the CERCLA "release of a hazardous substance" definition. Prior site uses associated with PFAS (above) that previously would not have driven a REC may now warrant REC classification under E1527-21.
- Where state regulatory programs already addressed PFAS (e.g., MI, NJ, PA, MA, CA, WA), state cleanup-program records must be searched as part of the Tier 1 records review.
- Vapor intrusion and groundwater pathways for PFAS differ from petroleum / chlorinated solvents; analytical methods (EPA Method 1633 for non-potable water; EPA Method 537.1 for drinking water) and lab certifications must be appropriate.
- The CERCLA Section 102(a) Framework Rule announced by EPA on Sep 17, 2025 may add additional PFAS substances; verify the current 40 CFR § 302.4 list at draft time.

Detailed PFAS evaluation checklist: see `references/PFAS-AND-EMERGING-CONTAMINANTS.md`.

## CERCLA Shelf-Life

- **Full Phase I**: valid **1 year** from completion to acquisition
- **Site reconnaissance**: within **180 days** prior to acquisition
- **Government records review**: update if **180+ days** old at acquisition

## Pitfalls and Checks

1. **Conformance statement** — explicitly declare ASTM E1527-21 conformance; document any deviations
2. **REC classification precision** — use exact ASTM definitions; never conflate REC types
3. **Evidence-backed findings** — every REC must cite specific observations, records, history, or interviews
4. **Data gaps** — identify all; assess significance; recommend resolution
5. **No legal advice** — direct liability questions to environmental counsel
6. **Non-invasive scope only** — never imply subsurface sampling was performed
7. **Point-in-time limitation** — acknowledge the assessment reflects conditions as of assessment date
8. **State-specific requirements** — note state guidelines that exceed federal standards
9. **Vapor intrusion** — evaluate for any property near known groundwater contamination; assess as potential REC
10. **Facts vs. opinions** — clearly distinguish; state basis for professional judgment
11. **De minimis threshold** — conditions below regulatory concern are not RECs; document but classify appropriately
12. **Non-scope items** (ACM, LBP, radon, mold, wetlands) — only if client requests; separate from REC analysis
13. **PFAS evaluation** — required under E1527-21 emerging-contaminants expectation where property history suggests possible PFAS use; CERCLA designation (effective 2024-07-08) elevates this to standard practice for relevant property types

---

## Troubleshooting

- **Property has been previously assessed; report is older than 180 days.** Per shelf-life rules above, only specific components (interviews, government records, lien search, declaration) can refresh a stale Phase I; site reconnaissance must be redone within 180 days of acquisition. Confirm what truly needs to be updated vs. what can be reused with documentation.
- **Limited site access (e.g., active operations, security restrictions).** Document access limitations explicitly as data gaps; acknowledge them in the Conclusions section. The professional must still attempt to obtain the missing information through interviews, prior reports, or remote means before declaring a data gap "significant."
- **Government databases return no hits but historical use suggests likely contamination.** Government databases are necessary but not sufficient. A clean ASTM E1527-21 search radius does not eliminate REC potential where historical photo / city directory / fire insurance map review indicates contaminating uses. Document the affirmative search and the negative result; rely on historical sources to drive REC classification.
- **State has stricter standards than federal AAI.** Many states (CA, NJ, NY, WA, PA, others) have analogues that may require additional searches or reporting. The federal AAI standard is the floor; comply with state requirements where they exceed federal.
- **PFAS evaluation but no analytical data and no obvious historical user.** State clearly that "no historical or current PFAS-impacting use was identified at the property based on available records and observations." Do not assume PFAS evaluation requires sampling — Phase I is non-invasive; PFAS sampling is Phase II scope.
- **Vapor intrusion concern based on adjacent groundwater contamination.** Use ASTM E2600 (vapor encroachment screening) as the supporting framework; document the screening decision (vapor encroachment condition / no VEC) with reasoning.

---

## References

- `references/AUTHORITY-STATUS.md` — date-stamped record of authoritative sources consulted for this skill.
- `references/PFAS-AND-EMERGING-CONTAMINANTS.md` — detailed PFAS evaluation guidance for Phase I ESAs.

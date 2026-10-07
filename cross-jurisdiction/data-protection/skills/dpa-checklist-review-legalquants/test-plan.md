# Acceptance Test Plan — DPA Checklist Review v1.0.0

## Skill summary

Reviews Data Processing Agreements (DPAs) against multiple regulatory regimes: GDPR, US state privacy laws, HIPAA BAA, and general commercial. Supports `regulatory_regime`, `party_role` (controller / processor), `data_categories`, `international_transfer_context`, and `prior_agreements` inputs. Produces a structured report with checklist-style coverage of each in-scope provision.

## Test corpus requirements

Source 8–12 anonymized DPAs covering:

- **At least 2 GDPR-context DPAs** (EU/UK data subjects involved): one controller-to-processor, one processor-to-sub-processor.
- **At least 2 US state privacy DPAs** (CCPA / CPRA, CDPA, CPA, CTDPA, UCPA): mix of vendor-side and customer-side.
- **At least 2 HIPAA BAAs** (covered entity engaging a business associate, with PHI involved).
- **At least 1 general-commercial DPA** (no specific privacy regime; data-handling baseline only).
- **At least 1 multi-regime DPA** (covers GDPR + US state privacy together — common for multi-national vendors).
- **At least 1 DPA with notable international-transfer mechanism** (Standard Contractual Clauses, UK IDTA, supplementary measures post-Schrems II).
- **At least 1 routine, market-standard DPA** to confirm baseline calibration.

Run each DPA against the appropriate `regulatory_regime` input. For multi-regime tests, run twice to verify regime-specific calibration in each pass.

## Test scenarios

### Scenario 1: GDPR DPA, controller-to-processor

**Inputs:** A GDPR-context DPA where the user's organization is the controller engaging a processor. Inputs: `regulatory_regime: gdpr`, `party_role: controller`.

**Expected output structure:**
- Markdown report with sections: "Bottom line", "Critical issues", "Material issues", "Minor issues / observations", "GDPR-specific checklist", "Recommended position", "What this skill does not do".
- The GDPR-specific checklist covers Article 28(3) requirements: subject matter and duration, nature and purpose, type of personal data, categories of data subjects, rights and obligations, processor obligations enumeration, sub-processor approval, technical and organizational measures, etc.

**Expected calibration:**
- 0–2 critical findings (typically only if the DPA omits Article 28(3) elements outright).
- 3–7 material findings on Article 28(3) elements that are present but inadequately specified.
- 5–12 minor findings on stylistic or non-material concerns.
- "Bottom line" leads with controller-perspective recommendation.

**Edge cases to verify:**
- Skill identifies missing Article 28(3) elements explicitly.
- Skill addresses sub-processor approval mechanism (is it general-prior-authorization or specific-prior-authorization?) at appropriate severity.
- Skill addresses international-transfer mechanism if present (SCCs, IDTA, derogations, supplementary measures).
- Skill addresses Article 32 technical and organizational measures.

**Pass criteria:**
- Structural pass: All required sections including GDPR-specific checklist present.
- Calibration pass: Reviewing attorney with GDPR experience confirms Article 28(3) coverage and severity calibration.

### Scenario 2: GDPR DPA, processor-to-sub-processor

**Inputs:** GDPR-context DPA where the user's organization is the processor engaging a sub-processor. Inputs: `regulatory_regime: gdpr`, `party_role: processor`.

**Expected output structure:** Same as Scenario 1, with calibration shifted to processor-perspective concerns: maintaining Article 28(4) flow-down obligations, sub-processor's obligations matching or exceeding processor's obligations to controller, controller's right to audit sub-processor.

**Expected calibration:**
- Findings address Article 28(4) flow-down adequacy.
- Findings address sub-processor's right to engage further sub-processors (sub-sub-processors) and the visibility cascade.
- "Bottom line" addresses whether the sub-processor's commitments are adequate to satisfy the processor's commitments to its controller.

**Edge cases to verify:**
- Skill differentiates controller and processor party roles in the analysis.
- Skill addresses Article 28(4) requirements specifically.

**Pass criteria:** As above with processor-role-aware verification.

### Scenario 3: US state privacy DPA

**Inputs:** A DPA addressing US state privacy obligations (CCPA / CPRA / CDPA / CPA / CTDPA / UCPA). Input: `regulatory_regime: us-state-privacy`, with applicable jurisdictions specified if known.

**Expected output structure:** Same overall structure with section: "US state privacy-specific checklist" covering: service-provider / processor designations under each statute, prohibition on selling / sharing, sub-contractor flow-down, deletion rights, consumer-request mechanisms.

**Expected calibration:**
- 0–2 critical findings.
- 3–6 material findings on state-specific requirements that vary across the regimes.
- 5–10 minor findings.

**Edge cases to verify:**
- Skill addresses the "service provider" / "processor" / "contractor" distinctions across CCPA/CPRA/CDPA/CPA terminology variations.
- Skill identifies cross-state harmonization or harmonization gaps.
- Skill addresses sale-and-share restrictions.

**Pass criteria:** As above with US-state-privacy-aware verification.

### Scenario 4: HIPAA BAA

**Inputs:** A HIPAA BAA where covered entity engages a business associate. Input: `regulatory_regime: hipaa-baa`, `party_role` as appropriate.

**Expected output structure:** Same overall structure with section: "HIPAA BAA-specific checklist" covering: §164.504(e)(2) required terms, breach notification, sub-contractor flow-down, return-or-destroy on termination, audit rights.

**Expected calibration:**
- 0–2 critical findings (typically only if §164.504(e)(2) elements are missing or substantially deficient).
- 3–6 material findings on supporting provisions.
- 5–10 minor findings.
- "Bottom line" addresses §164.504(e)(2) compliance baseline.

**Edge cases to verify:**
- Skill addresses each §164.504(e)(2) required term explicitly.
- Skill addresses breach-notification timing (HIPAA's 60-day floor; HHS reporting if applicable).
- Skill addresses minimum-necessary use.
- Skill flags reuse-of-PHI provisions at appropriate severity.

**Pass criteria:** As above with HIPAA-specific verification.

### Scenario 5: General commercial DPA (no specific regime)

**Inputs:** A general commercial DPA where no specific regulatory regime applies but data handling is in scope. Input: `regulatory_regime: general-commercial`.

**Expected output structure:** Same overall structure but without regime-specific checklist; the analysis focuses on baseline data-handling provisions.

**Expected calibration:**
- 0–1 critical findings.
- 2–5 material findings on data-handling baseline (security commitments, breach notification, return-on-termination).
- 4–8 minor findings.
- "Bottom line" notes whether the general-commercial baseline is sufficient or whether a regime-specific layer is needed.

**Edge cases to verify:**
- Skill recognizes that "general commercial" is the correct fit (not silently applying GDPR or HIPAA criteria).
- Skill recommends adding regime-specific provisions if the data handling implicates a regulated category.

**Pass criteria:** As above with general-commercial scoping verification.

### Scenario 6: Multi-regime DPA (GDPR + US state privacy)

**Inputs:** A DPA addressing both GDPR and US state privacy. Run twice: once with `regulatory_regime: gdpr` and once with `regulatory_regime: us-state-privacy`.

**Expected output structure:** Two reports — one calibrated to GDPR analysis, one calibrated to US state privacy analysis. The reports address the same document but surface different findings.

**Expected calibration:**
- Findings differ across the two passes — GDPR-pass surfaces Article 28(3) gaps; US-state-privacy-pass surfaces sale-restriction / consumer-rights gaps.
- Common findings (e.g., breach notification timing) are flagged in both passes with appropriate regime-specific framing.

**Edge cases to verify:**
- Skill does not lapse into the wrong regime mid-report.
- Skill addresses cross-regime conflicts (e.g., if GDPR requires prior approval for sub-processors but the DPA's US state privacy approach allows general approval).

**Pass criteria:** As above with multi-regime verification on both passes.

### Scenario 7: International transfer mechanism

**Inputs:** A DPA with explicit international transfer mechanism (SCCs, UK IDTA, supplementary measures). Input: `regulatory_regime: gdpr`, `international_transfer_context: <description>`.

**Expected output structure:** Includes a focused section on transfer-mechanism adequacy.

**Expected calibration:**
- Findings address SCC selection adequacy (Module 2 controller-to-processor; Module 3 processor-to-processor; etc.) for the data-flow context.
- Findings address supplementary measures (Schrems II considerations).
- Findings address transfer impact assessment if applicable.

**Pass criteria:** Reviewing attorney with international-transfer experience confirms calibration.

## Refusal scenarios

### Refusal 1: Document is not a DPA

**Input:** An MSA, NDA, or other contract type misidentified as a DPA.

**Expected behavior:**
- Skill identifies that the document is not (primarily) a DPA.
- Skill recommends the appropriate alternative skill.

**Pass criteria:** Explicit refusal with cross-pointer.

### Refusal 2: Regime selection conflicts with document content

**Input:** A HIPAA BAA with `regulatory_regime: gdpr` selected, or a clearly-GDPR DPA with `regulatory_regime: hipaa-baa` selected.

**Expected behavior:**
- Skill identifies the mismatch between the input regime and the document's apparent regime.
- Skill suggests the correct regime selection or proceeds with explicit caveat.

**Pass criteria:** Skill detects the mismatch rather than silently producing miscalibrated output.

## Cross-cutting verification

- No invented authorities. Articles, regulations, and statutes cited are real.
- No enforceability opinions on regulatory compliance ("this satisfies GDPR Article 28" is an opinion the skill should not assert; "this addresses each Article 28(3) element" is an observation the skill can support).
- Recommended language is operationally usable.
- "What this skill does not do" enumeration present (typically: regulatory-compliance certifications, jurisdiction-specific enforceability, transfer-impact-assessment full execution).
- Citations resolve.

## Pass / fail decision

DPA Checklist Review v1.0.0 passes acceptance testing when:

1. All 7 test scenarios pass structural checks.
2. All 7 test scenarios pass calibration evaluation by a reviewing attorney with regime-specific experience (GDPR-aware reviewer for GDPR scenarios; US-privacy-aware reviewer for US state privacy scenarios; HIPAA-aware reviewer for HIPAA BAA scenarios — possibly different reviewers for different scenarios).
3. Both refusal scenarios trigger the documented refusal behavior.
4. Cross-cutting verification passes on every scenario.

## Reviewer notes

DPA Checklist Review touches several distinct regulatory regimes; the reviewing attorney should have practical experience with the regime they are reviewing. For multi-regime testing, multiple reviewers are recommended (one per regime).

Specific competencies:
- **GDPR reviewer:** Article 28 / 32 / 35 / 44 et seq. familiarity; SCC module selection; Schrems II supplementary measures; UK IDTA distinct from EU SCCs.
- **US state privacy reviewer:** CCPA / CPRA service-provider / contractor / processor distinctions; cross-state harmonization; sale-and-share restrictions.
- **HIPAA reviewer:** §164.504(e)(2) required-terms enumeration; breach notification mechanics; covered-entity vs. business-associate vs. sub-contractor cascade.

Calibration assessment is documented in `test-results/dpa-checklist-review-v1.0.0/calibration-assessment.md`, with separate sub-files for each regime if multiple reviewers participate.

# Acceptance Test Plan — NDA Review v1.0.1

## Skill summary

Reviews mutual or unilateral non-disclosure agreements for unusual provisions, perspective-calibrated risks, and recommended position. Supports `discloser`, `recipient`, and `mutual` perspective inputs; calibrated to common in-house counsel review.

## Test corpus requirements

Source 6–10 anonymized NDAs covering:

- **At least 2 mutual NDAs** (cross-disclosure scenarios — JV exploration, partnership discussions, technology evaluations).
- **At least 2 unilateral NDAs from the discloser perspective** (the user's organization is the disclosing party — e.g., a customer NDA the user's company sends to a vendor before a deal discussion).
- **At least 2 unilateral NDAs from the recipient perspective** (the user's organization is receiving confidential information — e.g., the counterparty has imposed their NDA before the deal can advance).
- **At least 1 unusual-structure NDA** that includes one or more of: trailing residuals carveout for M&A diligence, employee non-solicitation, return-or-destroy with proof, multi-jurisdiction governing law selection, or a notably long (5+ year) survival period.
- **At least 1 routine vendor NDA** (a clean, market-standard template — to confirm the skill doesn't over-flag on a baseline document).

For perspective-branching tests, the same NDA can be run twice with different `perspective` inputs to verify perspective-aware calibration.

Source documents from: prior matters in the user's practice, anonymized samples from the operator's organization, or — if none are available — public templates from sources like the SEC EDGAR filings (which include NDAs as exhibits to public filings).

## Test scenarios

### Scenario 1: Routine mutual NDA (baseline calibration)

**Inputs:** A clean, market-standard mutual NDA with no unusual provisions. Perspective: `mutual`.

**Expected output structure:**
- Markdown report with sections: "Bottom line", "Findings", "Recommended position summary", "What this skill does not do".
- Severity tags follow the rubric (`**[Critical]**`, `**[Material]**`, `**[Minor]**`).
- Citations reference specific clause numbers or page locations in the source.
- Output starts with "Bottom line" — two-three sentences leading with recommendation.

**Expected calibration:**
- 0 critical findings (this is a baseline document).
- 0–2 material findings.
- 2–6 minor findings (typically: routine clause-language preferences, optional carveouts not present, governing-law observations).
- "Bottom line" reads as "recommend executing as-drafted with optional minor edits."
- No invented authorities; any citation to law is cleanly referenced.

**Edge cases to verify:**
- Skill does not flag standard provisions (e.g., a 2-year survival period for a generic business-discussion NDA) as critical.
- Skill identifies the document as mutual (not unilateral) and applies mutual-perspective calibration.

**Pass criteria:**
- Structural pass: All required sections present; severity tags formatted correctly; citations resolve.
- Calibration pass: Reviewing attorney confirms the finding density and severity distribution is consistent with how they would review a routine mutual NDA.

### Scenario 2: Unilateral NDA, discloser perspective

**Inputs:** A unilateral NDA where the user's organization is the disclosing party. Perspective: `discloser`.

**Expected output structure:**
- Same structure as Scenario 1.
- Findings calibrated to discloser concerns: scope of permitted use, return/destruction obligations, survival, remedies for breach, residuals carveouts (if any) carefully evaluated.

**Expected calibration:**
- 0–2 critical findings (typically only if the recipient's residuals carveout is overbroad, the survival is too short, or the remedies are inadequate).
- 1–4 material findings (typically: permitted-use scope, return/destruction proof, third-party recipient handling, breach notification).
- 3–8 minor findings.
- "Bottom line" leads with discloser-side recommendation (negotiate, accept-with-edits, or accept-as-is depending on severity distribution).

**Edge cases to verify:**
- Skill identifies provisions favorable to the recipient and flags them at appropriate severity from the discloser's perspective.
- Skill does not lapse into recipient-favorable analysis mid-report.
- If the document includes a residuals carveout for M&A or technology-evaluation contexts, the skill calibrates the carveout against the deal type rather than reflexively flagging.

**Pass criteria:**
- Structural pass: As above.
- Calibration pass: Reviewing attorney confirms perspective-aware findings — specifically that asymmetric provisions favoring the recipient are surfaced at appropriate severity.

### Scenario 3: Unilateral NDA, recipient perspective

**Inputs:** A unilateral NDA where the user's organization is the recipient. Perspective: `recipient`.

**Expected output structure:**
- Same structure as Scenario 1.
- Findings calibrated to recipient concerns: scope of confidential information definition (over-broad?), permitted-use scope (too narrow?), survival period (commensurate with risk?), residuals (allowed?), remedies (proportionate?), employee/contractor exposure.

**Expected calibration:**
- 0–2 critical findings (typically only if the confidentiality definition is unbounded, residuals are not allowed for routine business operations, or remedies include unilateral injunction without standard).
- 1–4 material findings.
- 3–8 minor findings.
- "Bottom line" leads with recipient-side recommendation.

**Edge cases to verify:**
- Skill flags overly broad "confidential information" definitions (e.g., "all information disclosed in any form") at appropriate severity from recipient perspective.
- Skill addresses residuals carveouts as material from the recipient's side.
- Skill does not lapse into discloser-favorable analysis mid-report.

**Pass criteria:**
- Structural pass: As above.
- Calibration pass: Reviewing attorney confirms perspective-aware findings — specifically that asymmetric provisions favoring the discloser are surfaced at appropriate severity.

### Scenario 4: M&A diligence NDA

**Inputs:** An NDA scoped to M&A diligence (residuals carveout, longer survival on commercially sensitive information, broader permitted purposes). Perspective: `mutual` or whichever perspective applies.

**Expected output structure:**
- Same structure as Scenario 1.
- The skill recognizes the M&A diligence context (either via the document's framing or via an optional `deal_type` input) and calibrates accordingly.

**Expected calibration:**
- 0–1 critical findings (M&A NDAs are typically negotiated to a market position; substantive concerns are usually around residuals and post-deal-collapse handling).
- 1–3 material findings around residuals scope, post-collapse return/destruction, non-solicitation if present.
- 2–6 minor findings.

**Edge cases to verify:**
- Skill does not flag the residuals carveout reflexively (it is expected in M&A diligence).
- Skill identifies non-solicitation provisions if present and addresses them at appropriate severity.
- Skill addresses standstill provisions if present.

**Pass criteria:**
- Structural pass: As above.
- Calibration pass: Reviewing attorney confirms M&A-context-aware calibration.

### Scenario 5: Vendor NDA with data-handling complications

**Inputs:** A vendor NDA where the recipient (vendor) will handle some sensitive customer information as part of the engagement. Perspective: `discloser` (the user is the customer providing information).

**Expected output structure:**
- Same structure as Scenario 1.
- Findings calibrated to discloser-as-customer with vendor handling sensitive data: data-handling provisions, security requirements, breach notification, return/destruction, third-party processor handling, sub-contractor approval.

**Expected calibration:**
- 0–2 critical findings if security requirements or breach notification are missing.
- 1–4 material findings around data-handling specifics.
- 2–6 minor findings.
- "Bottom line" notes whether the NDA alone is sufficient or whether a separate Data Processing Agreement (DPA) should be required.

**Edge cases to verify:**
- Skill recognizes that a vendor handling sensitive data may require a DPA in addition to the NDA, and surfaces this in the recommendations.
- Skill does not duplicate DPA Checklist Review's analysis; the cross-pointer is the appropriate response.

**Pass criteria:**
- Structural pass: As above.
- Calibration pass: Reviewing attorney confirms appropriate cross-pointer to DPA Checklist Review when data handling is in scope.

### Scenario 6: Notably unusual NDA (intentional edge cases)

**Inputs:** An NDA with one or more unusual structural elements: 5+ year survival period, broad employee non-solicitation, jurisdiction selection in an unusual venue, or an unusually narrow permitted purpose. Perspective: as appropriate.

**Expected output structure:**
- Same structure as Scenario 1.
- Each unusual element surfaces as a finding with explicit severity calibration.

**Expected calibration:**
- The unusual elements drive the severity distribution: 1–3 critical findings on the unusual elements; 1–3 material findings on supporting concerns.
- The "Bottom line" reflects the unusual posture (typically "negotiate or escalate" rather than "execute as-drafted").

**Edge cases to verify:**
- Skill explicitly identifies the unusual structural elements rather than treating them as routine.
- Skill provides recommended language for each unusual element (where applicable).
- Skill defers enforceability questions ("the 7-year survival period is unusual; enforceability of overbroad survival periods is jurisdiction-specific and warrants escalation") rather than asserting enforceability outcomes.

**Pass criteria:**
- Structural pass: As above.
- Calibration pass: Reviewing attorney confirms each unusual element is surfaced at appropriate severity and with appropriate enforceability deferral.

## Refusal scenarios

### Refusal 1: Document is not an NDA

**Input:** An MSA, employment agreement, or other contract type misidentified as an NDA.

**Expected behavior:**
- Skill identifies that the document is not (primarily) an NDA.
- Skill declines to apply NDA-specific analysis.
- Skill recommends the appropriate alternative skill (e.g., MSA Review — SaaS for an MSA; "no specific skill applies" for an employment agreement).
- Skill does not produce findings as if the document were an NDA.

**Pass criteria:** Skill explicitly refuses with a clear explanation.

### Refusal 2: Document is not in English

**Input:** A non-English NDA (e.g., a French or Spanish NDA).

**Expected behavior:**
- Skill identifies that the document is not in English.
- Skill notes that the skill is calibrated to English-language NDAs and US-law / common-law conventions.
- Skill asks the user to confirm before proceeding (rather than silently producing output that may be miscalibrated for the document's actual jurisdiction).

**Pass criteria:** Skill explicitly notes the language and seeks confirmation.

## Cross-cutting verification

These checks apply across all scenarios:

- **No invented authorities.** Every citation to law (case law, statute, regulation) is real and accurately characterized. The skill does not cite cases or statutes that do not exist.
- **No enforceability opinions.** The skill does not assert "this clause is unenforceable" or "this clause will not hold up." Enforceability deferred to "this is unusual" or "this raises an enforceability question."
- **"What this skill does not do" enumeration is present.** The output lists the out-of-scope items (typically: jurisdiction-specific enforceability analysis, transactional structuring, employment-law-specific implications of non-solicitation provisions, etc.).
- **Recommended language is operationally usable.** Recommended replacement language is clean, ready to drop in with minor party-name edits.
- **Citations resolve.** Every citation in the report points at a clause or page in the source document and the verbatim quote (where present) appears verbatim in the source.
- **Conservative posture maintained.** No findings overclaim outside the skill's documented scope.

## Pass / fail decision

NDA Review v1.0.1 passes acceptance testing when:

1. All 6 test scenarios pass structural checks.
2. All 6 test scenarios pass calibration evaluation by a reviewing attorney.
3. Both refusal scenarios trigger the documented refusal behavior.
4. Cross-cutting verification passes on every scenario.

Any failure category is filed as a GitHub Issue with the `acceptance-test-fail` label. Issues block the v1.0.1 release until resolved. Resolved issues are closed with a link to the fix PR; the skill is re-tested against the affected scenarios after the fix.

## Reviewer notes

The reviewing attorney for NDA Review acceptance testing should be familiar with both customer-side and vendor-side NDA negotiation. Specific competencies:

- Distinguishing M&A diligence NDAs from vendor procurement NDAs (different calibrations apply).
- Calibrating residuals carveouts (acceptable in M&A; problematic in vendor relationships).
- Recognizing standard vs. unusual survival periods in different deal contexts.
- Identifying data-handling provisions that require cross-reference to DPA Checklist Review.

Reviewer documents calibration assessment in `test-results/nda-review-v1.0.1/calibration-assessment.md` following the template in [`acceptance-testing-framework.md`](../../acceptance-testing-framework.md#expected-behavior-format).

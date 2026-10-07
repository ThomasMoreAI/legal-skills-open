# Acceptance Test Plan — MSA Review — SaaS v1.0.0

## Skill summary

Reviews SaaS Master Services Agreements from the customer or vendor perspective. Supports `customer` and `vendor` perspectives; supports `comprehensive` and `quick_triage` review modes; calibrated to common in-house counsel review of SaaS contracts.

## Test corpus requirements

Source 8–12 anonymized SaaS MSAs covering:

- **At least 3 customer-perspective MSAs** (the user's organization is the customer purchasing SaaS): ideally one mid-market SaaS template, one enterprise SaaS template, one developer-tools SaaS template. Different SaaS categories surface different concerns (data-platform SaaS has different sensitivities than collaboration SaaS).
- **At least 3 vendor-perspective MSAs** (the user's organization is the SaaS vendor selling): ideally one customer-facing template, one channel-partner template, one enterprise-RFP-response template.
- **At least 1 MSA with notable data-handling provisions** (PII processing, customer-data-as-training-data, sub-processor cascades, international transfers) — to test the cross-pointer to DPA Checklist Review.
- **At least 1 MSA with notable IP provisions** (joint IP development, customer-data-derived IP, AI-training rights) — to test the IP-clause findings.
- **At least 1 MSA with usage-based or consumption-based pricing** (rather than seat-based) — to test commercial-terms calibration.
- **At least 1 routine, market-standard SaaS MSA** to confirm calibration on a baseline document.

For perspective-branching tests, run the same MSA twice with different `perspective` inputs to verify perspective-aware calibration. For mode-branching tests, run the same MSA in `comprehensive` mode and `quick_triage` mode and verify the output difference.

## Test scenarios

### Scenario 1: Routine SaaS MSA, customer perspective, comprehensive mode (baseline)

**Inputs:** Market-standard SaaS MSA. Perspective: `customer`. Mode: `comprehensive`.

**Expected output structure:**
- Markdown report with sections: "Executive summary" (or "Bottom line"), "Critical issues", "Material issues", "Minor issues / observations", "Recommended position", "What this skill does not do".
- Severity tags follow rubric.
- Citations reference clause numbers in the source MSA.

**Expected calibration:**
- 0–1 critical findings.
- 3–8 material findings (typically: liability cap calibration, indemnification scope, service-level credits structure, termination-for-convenience, audit rights).
- 6–15 minor findings.
- "Bottom line" leads with customer-side recommendation.

**Edge cases to verify:**
- Liability cap discussion is calibrated to the contract's commercial value and risk profile (not flagging a 12-month-fee cap as critical on a $50K/year contract; flagging unlimited liability exposure as critical).
- Indemnification scope differentiates IP-infringement (typically uncapped or super-capped) from general indemnification (typically capped).
- Auto-renewal language is identified and severity-tagged.

**Pass criteria:**
- Structural pass: All required sections present; severity tags formatted correctly.
- Calibration pass: Reviewing attorney confirms severity distribution is consistent with how they would review a routine SaaS MSA from customer side.

### Scenario 2: Routine SaaS MSA, vendor perspective, comprehensive mode

**Inputs:** Market-standard SaaS MSA. Perspective: `vendor`. Mode: `comprehensive`.

**Expected output structure:** Same as Scenario 1.

**Expected calibration:**
- 0–1 critical findings (typically only if a customer-favorable provision creates outsized vendor exposure — e.g., unlimited indemnification of customer's downstream losses).
- 3–8 material findings (typically: data ownership, suspension rights, payment terms, liability cap defense, IP defense scope).
- 6–15 minor findings.
- "Bottom line" leads with vendor-side recommendation.

**Edge cases to verify:**
- Skill flags customer-favorable provisions appropriately from the vendor's perspective.
- Skill does not lapse into customer-favorable analysis mid-report.
- Recommended language reflects vendor-protective positions (e.g., suggesting suspension rights for non-payment; suggesting carve-outs in customer-favorable indemnification language).

**Pass criteria:** Same as Scenario 1, with perspective-awareness verification.

### Scenario 3: SaaS MSA with significant data-handling provisions

**Inputs:** SaaS MSA where the vendor processes customer PII or sensitive data. Perspective: `customer`. Mode: `comprehensive`.

**Expected output structure:** Same as Scenario 1, with an explicit cross-reference to DPA Checklist Review for the data-handling-specific analysis.

**Expected calibration:**
- 0–2 critical findings depending on data-handling provisions: explicit AI-training rights without opt-out is critical; missing data-export-on-termination is critical; lack of breach notification is critical.
- 3–6 material findings on data handling (sub-processor approval, audit rights, data residency, retention, return on termination).
- 6–12 minor findings.
- "Bottom line" notes whether a separate DPA is in place or whether the MSA's data-handling provisions are stand-alone, and recommends DPA Checklist Review for the deeper analysis.

**Edge cases to verify:**
- Skill identifies the cross-pointer to DPA Checklist Review without duplicating that skill's analysis.
- Skill flags AI-training-on-customer-data provisions at appropriate severity (critical if no opt-out; material if opt-out is present but operationally complex).
- Skill addresses sub-processor cascade visibility.

**Pass criteria:** Same as Scenario 1, with cross-skill-pointer verification.

### Scenario 4: SaaS MSA with notable IP provisions

**Inputs:** SaaS MSA where IP ownership is non-standard — e.g., joint IP on custom development, customer-data-derived IP claimed by vendor, AI-output ownership ambiguity. Perspective: `customer`. Mode: `comprehensive`.

**Expected output structure:** Same as Scenario 1.

**Expected calibration:**
- 1–3 critical findings on IP provisions where the customer's position is materially compromised (e.g., vendor claiming derivative IP on customer data).
- 2–4 material findings on IP-related provisions (work-product ownership, customer-data-derived insights, license-back provisions).
- 4–10 minor findings.
- Recommended language addresses IP allocation explicitly.

**Edge cases to verify:**
- Skill differentiates licensed-IP language (vendor licenses to customer) from owned-IP language (customer retains ownership).
- Skill flags work-product-derived IP claims as customer-perspective concerns.
- Skill addresses AI-output ownership where present.

**Pass criteria:** Same as Scenario 1, with IP-aware calibration verification.

### Scenario 5: SaaS MSA in quick triage mode

**Inputs:** Same MSA as Scenario 1. Perspective: `customer`. Mode: `quick_triage`.

**Expected output structure:**
- Shorter markdown report focused on critical and material issues only.
- "Bottom line" / "Executive summary" present.
- Minor issues either omitted or summarized in a single brief section.
- "What this skill does not do" section present.

**Expected calibration:**
- 0–1 critical findings (same as comprehensive mode).
- 3–6 material findings (subset of comprehensive mode — only the most operationally significant).
- Minor findings either compressed to a one-line summary or omitted.

**Edge cases to verify:**
- Mode change shifts the report's depth without changing the substance of the calibration.
- Critical and material findings in quick triage mode are a strict subset of the comprehensive mode findings; nothing surfaces in triage that does not also surface in comprehensive.

**Pass criteria:**
- Structural pass: Triage-mode output is meaningfully shorter than comprehensive-mode output.
- Calibration pass: Triage findings are the same severity calibration as comprehensive — what changes is depth, not substance.

### Scenario 6: SaaS MSA with usage-based pricing

**Inputs:** SaaS MSA with consumption-based or seat-flexible pricing. Perspective: `customer`. Mode: `comprehensive`.

**Expected output structure:** Same as Scenario 1.

**Expected calibration:**
- Findings address usage-meter accuracy, dispute mechanism, audit rights on usage data, true-up provisions.
- "Bottom line" notes whether the pricing structure has been reviewed for predictability and dispute mechanisms.

**Edge cases to verify:**
- Skill recognizes usage-based pricing structure (rather than treating it as fixed-fee).
- Skill addresses meter-dispute and overage protection at appropriate severity.

**Pass criteria:** As above with pricing-aware verification.

## Refusal scenarios

### Refusal 1: Document is not a SaaS MSA

**Input:** A commercial purchase MSA, professional services agreement, or other contract type misidentified as a SaaS MSA.

**Expected behavior:**
- Skill identifies that the document is not (primarily) a SaaS MSA.
- Skill recommends the appropriate alternative skill (MSA Review — Commercial Purchase for goods/services agreements; "no specific skill applies, escalate to expert" for less common contract types).
- Skill does not apply SaaS-specific analysis to a non-SaaS document.

**Pass criteria:** Skill explicitly refuses with a clear explanation and cross-pointer.

### Refusal 2: Document is a SaaS Order Form rather than the underlying MSA

**Input:** A SaaS Order Form, Statement of Work, or other ancillary document referencing an underlying MSA the user has not provided.

**Expected behavior:**
- Skill identifies that the document is an ancillary, not the MSA itself.
- Skill suggests providing the underlying MSA for proper analysis.
- Skill optionally identifies provisions in the Order Form that warrant attention but defers full analysis pending the MSA.

**Pass criteria:** Skill explicitly identifies the document type and suggests next steps.

## Cross-cutting verification

These checks apply across all scenarios:

- **No invented authorities.** Every citation to law, regulation, or industry guidance is real and accurately characterized.
- **No enforceability opinions.** Skills defer enforceability questions ("this provision is unusual; enforceability is jurisdiction-specific and warrants escalation").
- **No regulatory-compliance opinions outside scope.** The skill does not assert HIPAA-compliance, GDPR-compliance, or other regime-specific compliance — it surfaces patterns and refers to DPA Checklist Review or Vendor Privacy Policy First Pass for regime-specific analysis.
- **Recommended language is operationally usable.** Suggested replacement language is clean and customer- or vendor-perspective-appropriate as the skill's perspective input dictates.
- **"What this skill does not do" enumeration is present.** Typical items: substantive product/services-specific analysis, jurisdiction-specific enforceability opinions, tax structuring, regulatory-compliance certifications.
- **Citations resolve.** Every citation in the report points at a clause in the source MSA.
- **Cross-skill pointers are accurate.** When the skill recommends DPA Checklist Review or Vendor Privacy Policy First Pass, the recommendation is appropriate for the document's content.

## Pass / fail decision

MSA Review — SaaS v1.0.0 passes acceptance testing when:

1. All 6 test scenarios pass structural checks.
2. All 6 test scenarios pass calibration evaluation by a reviewing attorney with SaaS contracting experience.
3. Both refusal scenarios trigger the documented refusal behavior.
4. Cross-cutting verification passes on every scenario.

The reviewing attorney pays particular attention to:
- Liability-cap calibration relative to contract value (not over-flagging market-standard caps; not under-flagging unusual caps).
- AI-training-on-customer-data provisions (a recent and high-stakes calibration target).
- Cross-pointer accuracy to DPA Checklist Review and Vendor Privacy Policy First Pass.

## Reviewer notes

The reviewing attorney for MSA Review — SaaS acceptance testing should have direct experience negotiating SaaS contracts from at least one of: customer side, vendor side, or both. Specific competencies:

- Distinguishing market-standard vs. unusual liability caps in SaaS context.
- Recognizing AI-training-on-customer-data provisions and calibrating their materiality.
- Calibrating sub-processor and data-handling provisions in a SaaS MSA vs. a separate DPA.
- Identifying when an Order Form or SOW is masquerading as the underlying MSA.

Calibration assessment is documented in `test-results/msa-review-saas-v1.0.0/calibration-assessment.md`.

# Acceptance Test Plan — Vendor Privacy Policy First Pass v1.0.0

## Skill summary

Triage assessment of a vendor's published privacy policy. Produces a structured summary of data handling practices and surfaces red flags relevant to in-house counsel evaluating whether to engage the vendor or escalate to deeper privacy review (DPA negotiation, full data-protection assessment).

## Test corpus requirements

Source 5–8 anonymized vendor privacy policies covering:

- **At least 1 high-quality, market-standard privacy policy** (e.g., a SaaS platform with a comprehensive, GDPR-aware policy) — to confirm baseline calibration.
- **At least 1 ambiguous-quality policy** (sparse provisions; vague data-handling language; missing key sections) — to surface red flags.
- **At least 1 policy with notable data-handling features** (AI-training rights, broad data-sharing, third-party advertiser ecosystem, cross-border data transfers without specified mechanism).
- **At least 1 policy with consumer-app focus** (vs. enterprise focus) — different concerns surface.
- **At least 1 policy with regulated-industry context** (financial services, healthcare, education) — additional regulatory lenses apply.

Documents can be sourced from the vendor's public website (privacy policies are typically published) and "anonymized" simply by replacing the vendor's name with a placeholder; the substantive content is what is being tested.

## Test scenarios

### Scenario 1: High-quality, market-standard privacy policy (baseline)

**Inputs:** A comprehensive SaaS-vendor privacy policy.

**Expected output structure:**
- Markdown report with sections: "Bottom line" (summary recommendation: engage / escalate / decline), "Summary of practices" (factual summary of what the policy says), "Red flags / concerns" (issues warranting attention), "Open questions for the vendor" (gaps in the policy that require follow-up), "What this skill does not do".

**Expected calibration:**
- 0 critical red flags (this is a market-standard policy).
- 0–2 material red flags (often: international transfer mechanisms not explicit; sub-processor list not published).
- 2–6 minor observations (typically: cookie consent mechanism, retention period clarity, data-subject-rights mechanism specifics).
- "Bottom line" leads with "engage with standard contractual safeguards" or similar.

**Edge cases to verify:**
- Skill summarizes practices factually without inventing claims the policy does not make.
- Skill differentiates clear practices from ambiguous-language practices.

**Pass criteria:**
- Structural pass: All required sections present.
- Calibration pass: Reviewing attorney confirms baseline calibration is correct (not over-flagging market-standard).

### Scenario 2: Ambiguous / sparse privacy policy

**Inputs:** A privacy policy with vague language, missing sections, or unclear data-handling commitments.

**Expected output structure:** Same structure with greater emphasis on "Open questions for the vendor."

**Expected calibration:**
- 1–3 critical red flags if substantively missing key elements (no data-handling commitment, no breach notification, no data-subject rights).
- 2–5 material red flags on ambiguous-but-present provisions.
- 3–8 minor observations.
- "Open questions for the vendor" is substantive — listing the specific questions that need answering before engagement.

**Edge cases to verify:**
- Skill flags absences (missing sections) as findings, not as silent omissions.
- Skill differentiates "policy says nothing about X" from "policy says X without specificity."

**Pass criteria:** As above with ambiguity-aware verification.

### Scenario 3: Policy with notable data-handling features

**Inputs:** A privacy policy with notable features: AI-training-on-customer-data, broad data-sharing with affiliates / advertisers, cross-border transfers without specified mechanism.

**Expected output structure:** Same structure with explicit findings on the notable features.

**Expected calibration:**
- AI-training rights without clear opt-out: critical red flag.
- Broad data-sharing with advertisers if user data is implicated: critical or material depending on scope.
- Cross-border transfers without specified mechanism: material red flag (specific to cross-border-data-flow contexts).
- "Bottom line" reflects the notable-features posture.

**Edge cases to verify:**
- Skill identifies AI-training-on-customer-data provisions specifically and addresses them at appropriate severity.
- Skill addresses ad-tech / data-broker ecosystem if implicated.

**Pass criteria:** As above with notable-features verification.

### Scenario 4: Consumer-app privacy policy

**Inputs:** A consumer-facing app's privacy policy (B2C rather than B2B).

**Expected output structure:** Same structure but with B2C-specific concerns: COPPA if minors are implicated, geolocation, advertising, in-app behavior tracking.

**Expected calibration:**
- Findings address consumer-app-specific concerns appropriately.
- "Bottom line" notes whether the in-house counsel context (B2B engagement evaluating a vendor) maps to the policy's posture.

**Edge cases to verify:**
- Skill identifies the B2C focus and notes how it differs from typical B2B-vendor evaluation.
- Skill addresses COPPA / minor-targeted concerns if present.

**Pass criteria:** As above with B2C-context verification.

### Scenario 5: Regulated-industry vendor policy

**Inputs:** A privacy policy for a vendor operating in a regulated industry (financial services, healthcare, education).

**Expected output structure:** Same structure with attention to regulatory-specific concerns: GLBA / financial-privacy provisions; HIPAA / healthcare data handling; FERPA / education records.

**Expected calibration:**
- Findings address the regulatory context specifically.
- "Bottom line" recommends regulatory-specific deeper review (e.g., DPA Checklist Review with HIPAA BAA regime if healthcare data is in scope).

**Edge cases to verify:**
- Skill identifies the regulatory context.
- Skill recommends appropriate cross-skill follow-up (DPA Checklist Review for the regulatory layer).

**Pass criteria:** As above with regulatory-context verification.

## Refusal scenarios

### Refusal 1: Document is not a privacy policy

**Input:** Terms of service, EULA, or other policy type misidentified as a privacy policy.

**Expected behavior:**
- Skill identifies that the document is not (primarily) a privacy policy.
- Skill suggests appropriate next steps (read the actual privacy policy; or note that the document type is not within scope).

**Pass criteria:** Explicit refusal.

### Refusal 2: Document is in non-English

**Input:** A non-English privacy policy.

**Expected behavior:**
- Skill identifies the language and notes the skill is calibrated to English-language US/EU/UK contexts.
- Skill seeks confirmation before proceeding.

**Pass criteria:** Explicit identification and confirmation request.

## Cross-cutting verification

- **Triage scope discipline.** This skill is a *first-pass triage*, not a comprehensive privacy assessment. Findings should not overclaim on the depth of analysis — the skill explicitly recommends DPA Checklist Review or full privacy assessment for deeper analysis where appropriate.
- **No invented privacy practices.** The skill summarizes what the policy *says*, not what the vendor *does* in practice (the policy may not reflect actual practice; this is acknowledged in the "What this skill does not do" enumeration).
- **No regulatory-compliance opinions.** The skill flags regulatory concerns but does not assert "this policy is GDPR-compliant" or "this policy violates CCPA."
- **Open questions are substantive.** The "Open questions for the vendor" section produces real questions, not generic placeholders.
- "What this skill does not do" enumeration present.
- Citations to specific sections of the policy resolve.

## Pass / fail decision

Vendor Privacy Policy First Pass v1.0.0 passes acceptance testing when:

1. All 5 test scenarios pass structural checks.
2. All 5 test scenarios pass calibration evaluation by a reviewing attorney with privacy / data-protection experience.
3. Both refusal scenarios trigger documented refusal behavior.
4. Cross-cutting verification passes on every scenario.

## Reviewer notes

The reviewing attorney for Vendor Privacy Policy First Pass should have practical privacy / data-protection experience covering both consumer and enterprise contexts. Specific competencies:

- Identifying AI-training-on-customer-data provisions and calibrating their materiality.
- Evaluating cross-border transfer mechanisms in the post-Schrems II environment.
- Distinguishing market-standard from sub-standard privacy policy practices.
- Recognizing when a triage flag warrants escalation to full DPA negotiation vs. when standard contractual safeguards are sufficient.

Calibration assessment is documented in `test-results/vendor-privacy-policy-first-pass-v1.0.0/calibration-assessment.md`.

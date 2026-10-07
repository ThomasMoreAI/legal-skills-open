# Acceptance Test Plan — MSA Review — Commercial Purchase v1.0.0

## Skill summary

Reviews commercial purchase MSAs (goods, services, professional services) from the customer or vendor perspective. Sister skill to MSA Review — SaaS, calibrated to non-SaaS commercial agreements where the substantive concerns differ (delivery, acceptance, warranties on tangible goods or service performance, professional services scope, change-order management).

## Test corpus requirements

Source 6–10 anonymized commercial purchase MSAs covering:

- **At least 2 customer-perspective MSAs for goods purchase** (the user's organization is buying physical goods or equipment from a vendor).
- **At least 2 customer-perspective MSAs for professional services** (the user's organization is engaging consultants, contractors, or service providers).
- **At least 2 vendor-perspective MSAs** (the user's organization is selling goods or services).
- **At least 1 MSA with significant warranty / acceptance / inspection provisions** (test mechanical-warranties calibration).
- **At least 1 MSA with statement-of-work / change-order architecture** (test SOW-MSA boundary calibration).
- **At least 1 routine, market-standard MSA** to confirm baseline calibration.

For perspective-branching tests, run the same MSA twice with different `perspective` inputs.

## Test scenarios

### Scenario 1: Routine goods-purchase MSA, customer perspective

**Inputs:** Standard commercial-purchase MSA for goods. Perspective: `customer`. Mode: `comprehensive`.

**Expected output structure:**
- Markdown report with sections: "Bottom line", "Findings", "Recommended position", "What this skill does not do".
- Severity tags follow rubric.
- Citations reference clauses in source.

**Expected calibration:**
- 0–1 critical findings.
- 3–7 material findings (typically: warranty scope and duration, acceptance criteria, delivery/risk-of-loss, indemnification scope, termination rights).
- 5–12 minor findings.
- "Bottom line" leads with customer-side recommendation.

**Edge cases to verify:**
- Skill addresses warranty duration and remedies appropriate to the type of goods (a 90-day warranty on durable equipment is unusually short; a 24-month warranty on consumables is unusually long).
- Skill addresses acceptance criteria and inspection rights at appropriate severity.
- Skill addresses risk-of-loss / title-transfer mechanics (FOB / FCA / DDP).

**Pass criteria:**
- Structural pass: All required sections present.
- Calibration pass: Reviewing attorney confirms calibration.

### Scenario 2: Professional services MSA, customer perspective

**Inputs:** Professional services MSA (consulting, implementation, integration services). Perspective: `customer`. Mode: `comprehensive`.

**Expected output structure:** Same as Scenario 1.

**Expected calibration:**
- 0–1 critical findings.
- 3–7 material findings (typically: scope and change-order, deliverables acceptance, IP ownership of work product, key-personnel commitments, no-poach provisions, dispute mechanisms).
- 5–12 minor findings.
- "Bottom line" addresses scope-of-work clarity and IP allocation prominently.

**Edge cases to verify:**
- IP ownership of work product is addressed at appropriate severity (typically critical or material from the customer's perspective if vendor retains broad rights).
- Skill addresses key-personnel commitments and substitution rights.
- Skill addresses change-order architecture and its boundary with the underlying MSA.

**Pass criteria:** As above with services-specific calibration verification.

### Scenario 3: Vendor perspective MSA

**Inputs:** Commercial purchase MSA. Perspective: `vendor`. Mode: `comprehensive`.

**Expected output structure:** Same as Scenario 1.

**Expected calibration:**
- 0–1 critical findings (typically only on customer-favorable provisions creating outsized vendor exposure: unlimited indemnification, broad most-favored-nation provisions, warranty obligations beyond product life).
- 3–6 material findings on payment terms, acceptance disputes, limitation of liability defense, IP defense scope.
- 5–10 minor findings.
- "Bottom line" leads with vendor-side recommendation.

**Edge cases to verify:**
- Payment-terms provisions (net-30 vs. net-60 vs. payment-on-acceptance) are addressed from vendor perspective.
- Skill flags overbroad customer-favorable IP indemnification scope.

**Pass criteria:** Calibration pass verifying perspective-aware findings.

### Scenario 4: MSA with notable warranty provisions

**Inputs:** MSA with unusual warranty scope (extended duration, broad remedy, or notably narrow). Perspective: as appropriate.

**Expected output structure:** Same as Scenario 1.

**Expected calibration:**
- The unusual warranty provisions surface explicitly with severity calibrated to the deviation from market.
- Recommended language addresses the unusual provision.

**Edge cases to verify:**
- Skill differentiates express warranties from implied warranties.
- Skill addresses warranty disclaimers ("AS IS") at appropriate severity.

**Pass criteria:** As above.

### Scenario 5: MSA with SOW / change-order architecture

**Inputs:** MSA that contemplates separate Statements of Work and a change-order process. Perspective: `customer` or as appropriate.

**Expected output structure:** Same as Scenario 1, with explicit attention to the MSA-SOW boundary.

**Expected calibration:**
- Findings address change-order approval mechanics.
- Findings address how SOWs interact with MSA-level provisions (does the SOW override the MSA or vice versa?).
- Findings address SOW dispute escalation.

**Edge cases to verify:**
- Skill identifies whether the MSA controls the SOW-level terms or vice versa.
- Skill addresses change-order pricing and timeline-impact provisions.

**Pass criteria:** As above with SOW-architecture-aware verification.

### Scenario 6: Quick triage mode

**Inputs:** Same MSA as Scenario 1. Mode: `quick_triage`.

**Expected output structure:**
- Shorter report focused on critical and material issues.
- Minor issues compressed or omitted.

**Expected calibration:**
- Critical and material findings are a subset of comprehensive mode.

**Pass criteria:** Triage output is meaningfully shorter without changing severity calibration of surfaced findings.

## Refusal scenarios

### Refusal 1: Document is a SaaS MSA

**Input:** A SaaS MSA misidentified as a commercial purchase MSA.

**Expected behavior:**
- Skill identifies the SaaS context.
- Skill recommends MSA Review — SaaS as the appropriate skill.
- Skill does not apply commercial-purchase-specific analysis to a SaaS MSA.

**Pass criteria:** Explicit refusal with cross-pointer.

### Refusal 2: Document is an Order Form / SOW only

**Input:** A standalone Order Form or SOW without the underlying MSA.

**Expected behavior:**
- Skill identifies that the document is ancillary.
- Skill suggests providing the underlying MSA for proper analysis.

**Pass criteria:** Explicit identification and recommendation.

## Cross-cutting verification

- No invented authorities.
- No enforceability opinions.
- No regulatory-compliance opinions outside scope.
- Recommended language is operationally usable.
- "What this skill does not do" enumeration present.
- Citations resolve.
- Cross-skill pointers accurate.

## Pass / fail decision

MSA Review — Commercial Purchase v1.0.0 passes acceptance testing when:

1. All 6 test scenarios pass structural checks.
2. All 6 test scenarios pass calibration evaluation by a reviewing attorney with commercial contracting experience.
3. Both refusal scenarios trigger the documented refusal behavior.
4. Cross-cutting verification passes on every scenario.

## Reviewer notes

The reviewing attorney should have direct experience with commercial purchase MSAs (goods or services). Specific competencies:

- Distinguishing goods-side concerns (warranty, acceptance, risk-of-loss, delivery) from services-side concerns (scope, change orders, IP allocation, key personnel).
- Calibrating warranty duration and remedy across product types.
- Evaluating SOW-MSA boundary clarity.
- Addressing change-order architecture from customer and vendor perspectives.

Calibration assessment is documented in `test-results/msa-review-commercial-purchase-v1.0.0/calibration-assessment.md`.

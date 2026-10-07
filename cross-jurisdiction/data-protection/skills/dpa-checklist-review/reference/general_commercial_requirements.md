# General Commercial DPA Requirements

This reference catalogs the commercially-standard terms expected in a Data Processing Agreement when no specific regulatory regime has been identified. The skill applies these requirements when `regulatory_regime: general_commercial` is specified — typically because the user has not yet identified the applicable regime, or because the DPA is intended to be regime-neutral and broadly compatible with multiple regimes.

A general commercial DPA does not satisfy any specific regime's prescriptive requirements. It should be regarded as a baseline that may need supplementation when specific regimes apply. The skill notes this limitation in the posture paragraph.

## Why this regime exists in the skill

DPAs in the wild often arrive without a specified regime. Counterparties present standard "Data Processing Addendum" templates that purport to cover any data processing relationship. These templates are usually drafted to satisfy the most prescriptive likely regime (GDPR), but not always. When the user does not yet know which regime applies, or wants a baseline review before identifying the regime, this checklist runs against commercially-standard expectations.

After this review, the skill always recommends a follow-up review under a specific regime once the regime is determined.

## Required terms

### 1. Definitions and scope

**Required:** The DPA must define the key terms (Personal Data, Processing, Controller, Processor, Sub-processor, Data Subject, Data Protection Laws) and the scope of processing covered.

**Compliant pattern:** Definitions section with clear scope statement; identifies what data, processing activities, and time period are covered.

**Common deficiencies:**
- Definitions vague or absent.
- Scope defined only by reference to "the Agreement" without specification.

### 2. Roles of the parties

**Required:** Clear identification of which party is controller, which is processor, and the relationship.

**Compliant pattern:** Recital or section identifying parties' roles.

**Common deficiencies:**
- Ambiguous roles (treating both parties as controllers in some contexts and processors in others).
- "Joint controller" language used where actually a controller-processor relationship exists.

### 3. Purpose and scope limitation

**Required:** Processor processes personal data only for the purposes set forth in the agreement.

**Compliant pattern:**
> "Processor shall process Personal Data only for the purposes specified in the underlying Services Agreement and as further described in this DPA, and shall not process Personal Data for any other purpose."

**Common deficiencies:** Permitting "internal business purposes" of the processor; permitting use for service improvement / model training without consent.

### 4. Processor instructions

**Required:** Processor processes only on documented instructions of controller.

**Compliant pattern:**
> "Processor shall process Personal Data only on the documented instructions of Controller, including with regard to international data transfers, except where required by law."

### 5. Confidentiality of personnel

**Required:** Processor's personnel are subject to confidentiality obligations.

**Compliant pattern:** Brief statement that processor's authorized personnel are bound by written confidentiality.

### 6. Security measures

**Required:** Appropriate technical and organizational measures appropriate to the risk.

**Compliant pattern:** Either a security annex or incorporation of an established security framework (SOC 2 Type II, ISO 27001, etc.) with commitment to maintain measures appropriate to the risk.

### 7. Sub-processor management

**Required:** Sub-processor engagement requires authorization, with notification of changes, flow-down of obligations, and processor liability.

**Compliant pattern:** Section addressing sub-processor authorization (specific or general), notification of changes with right to object, flow-down of all DPA terms, processor liability for sub-processor performance.

### 8. Data subject rights assistance

**Required:** Processor assists controller with data subject rights requests.

**Compliant pattern:** Reasonable assistance commitment with operational specifics (timelines, response mechanisms, no per-request fees that price out the right).

### 9. Breach notification

**Required:** Processor notifies controller of personal data breaches without undue delay.

**Compliant pattern:** Specific timeline (24–72 hours), required content (description, types of data, affected individuals, mitigation), cooperation with controller's notifications.

**Common deficiencies:**
- "Without undue delay" with no specific timeline.
- Notification only of "confirmed" or "material" breaches.
- No commitment to provide notification details.

### 10. Audit rights

**Required:** Controller's ability to verify processor's compliance.

**Compliant pattern:** Audit rights with reasonable parameters (annual frequency, advance notice, third-party auditor option, satisfaction via independent reports for routine purposes).

**Common deficiencies:**
- Audit limited to provision of audit reports only.
- Per-audit fees pricing out the right.

### 11. Return or deletion at termination

**Required:** Controller choice between return and deletion of personal data at termination.

**Compliant pattern:** Controller choice; deletion of all copies; certification on request; carve-out only for legally-required retention.

**Common deficiencies:**
- Processor unilateral choice.
- "Reasonable retention" carve-outs that swallow the obligation.

### 12. International transfers

**Required (if applicable):** Where transfers across borders occur, an appropriate transfer mechanism.

**Compliant pattern:** Identification of the transfer mechanism (most commonly EU SCCs 2021 / UK IDTA / equivalent), incorporated by reference or attached.

**Common deficiencies:** Generic "compliant with applicable law" without specification of mechanism.

### 13. Term and termination

**Required:** Clear DPA term and termination consequences.

**Compliant pattern:** DPA continues for as long as processing occurs; survival of relevant obligations (confidentiality, deletion, audit) after termination.

### 14. Liability

**Required (commercially):** Allocation of liability for data protection breaches.

**Compliant pattern:** Reasonable allocation reflecting parties' control over the data; carve-outs from limitation of liability for material data protection violations.

**Common deficiencies:**
- Processor liability capped at fees paid (insufficient for material data breaches).
- Mutual cap with no carve-out for data protection violations.

### 15. Governing law and jurisdiction

**Required:** Choice of law and forum.

**Compliant pattern:** Specified governing law and forum, ideally aligned with the underlying services agreement.

## Severity calibration for general commercial DPAs

The severity calibration is similar to other regimes but with one important caveat: a general-commercial DPA cannot be assessed for full compliance because the applicable regime is not specified. Severity therefore reflects deviation from commercial baseline, not compliance status.

- **Critical:** Missing core terms (purpose limitation, sub-processor management, breach notification, deletion); permits processor uses unauthorized by any common regime; security commitments effectively absent.
- **Material:** Timelines too vague; assistance commitments lacking operational substance; sub-processor flow-down deficient; no transfer mechanism where transfers occur.
- **Minor:** Drafting cleanliness issues; preferences not requirements.

## Always note in the posture

When reviewing under `general_commercial`, always include in the posture paragraph:

> "Note: this review applies the general commercial DPA baseline. The DPA's compliance with specific regulatory regimes (GDPR, CCPA/CPRA, HIPAA, etc.) was not assessed and may require additional review. Once the applicable regime(s) are identified, recommend re-running this skill with the specific regime to confirm compliance."

This makes the limitation explicit and channels users toward more specific reviews.

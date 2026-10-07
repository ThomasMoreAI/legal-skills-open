# US State Privacy DPA Requirements

This reference catalogs the convergent set of contractual requirements imposed by US state privacy laws on the relationship between businesses (controllers) and service providers / processors / contractors. The skill applies these requirements when `regulatory_regime: us_state_privacy` is specified.

## Threshold question: which laws actually apply?

Twenty-plus US states have enacted comprehensive privacy laws as of 2026, with substantial convergence on processor-contract requirements. The major ones:

- **California:** CCPA (2018) as amended by CPRA (2020/2023). The most prescriptive.
- **Virginia:** VCDPA (2023).
- **Colorado:** CPA (2023).
- **Connecticut:** CTDPA (2023).
- **Utah:** UCPA (2023).
- **Iowa, Indiana, Tennessee, Texas, Montana, Oregon, Florida, Delaware, New Jersey, New Hampshire, Kentucky, Maryland, Minnesota, Rhode Island, plus others** — all enacted on similar models with minor variations.

The skill does not require the user to identify which specific state laws apply. The convergent processor-contract requirements largely overlap; differences are noted where material. When the document is written for a single specific state (e.g., a "California Service Provider Addendum"), the skill notes that and flags requirements from other states that may also apply if data subjects are in those states.

The skill does not check applicability thresholds (number of consumers, revenue thresholds, etc.) — that is a determination for the user. The skill assumes the user has confirmed applicability.

## Terminology mapping

State privacy laws use different terms for the same roles. The following table maps terminology:

| Concept | CCPA/CPRA | VCDPA / CPA / CTDPA / others | GDPR (for context) |
|---|---|---|---|
| Decides how data is processed | Business | Controller | Controller |
| Processes on behalf of decider | Service Provider / Contractor | Processor | Processor |
| Engaged by processor | (sub-contractor) | Processor (sub-processor) | Sub-processor |
| End individual | Consumer | Consumer | Data subject |

The skill uses "controller" and "processor" in findings unless reviewing specifically against CCPA/CPRA (where "business" and "service provider" are the operative terms).

## Required contractual terms

US state privacy laws have converged on a common set of required terms in business-to-service-provider (or controller-to-processor) contracts. The skill checks each of the following.

### 1. Purpose limitation

**Required:** The contract must specify the limited and specified purposes for which the processor processes personal information.

**CCPA/CPRA-specific:** Cal. Civ. Code §1798.140(ag)(1) (service provider definition) and §1798.140(j) (contractor definition) require the contract to state that personal information is disclosed only for the limited and specified purposes.

**Convergent state requirement:** All major state laws require purpose specification. VCDPA §59.1-579, CPA §6-1-1305(5), CTDPA §11(d), etc., contain materially identical language.

**Compliant pattern:**
> "Processor shall process Personal Information only for the specific business purposes set forth in the underlying Services Agreement, and as further specified in [Annex/Exhibit], and shall not process Personal Information for any other purpose."

**Common deficiencies:**
- "Any purpose related to the Services" — too broad.
- Purposes defined only by reference to "the Agreement" with no specification of what the Agreement covers.
- Permitting processor to process for processor's own business purposes — directly conflicts with all state laws.

### 2. Prohibition on sale and sharing

**Required:** The contract must prohibit the processor from selling or sharing personal information.

**CCPA/CPRA-specific:** §1798.140(ag)(1)(A) and §1798.140(j)(1)(A) prohibit selling/sharing. CPRA added "sharing" specifically to address cross-context behavioral advertising.

**Convergent state requirement:** Most state laws prohibit processors from selling personal data; VCDPA, CPA, and CTDPA require contractual prohibition.

**Compliant pattern:**
> "Processor shall not Sell or Share Personal Information, as those terms are defined under applicable state privacy law, in connection with the processing of Personal Information under this Agreement."

**Common deficiencies:**
- Prohibition on "sale" but not "sharing" (CCPA-specific defect post-CPRA).
- Carve-outs for "marketing analytics" or similar that effectively permit sharing.
- No definition of "Sale" that incorporates the broad statutory definition.

### 3. Prohibition on retention, use, or disclosure outside business purposes

**Required:** The processor cannot retain, use, or disclose personal information outside the direct business relationship between controller and processor or for purposes other than the specified business purposes.

**CCPA/CPRA-specific:** §1798.140(ag)(1)(B) and §1798.140(j)(1)(B). Requires that the processor cannot retain/use/disclose outside the contract's purposes.

**Convergent:** All major state laws contain analogous restrictions.

**Compliant pattern:**
> "Processor shall not retain, use, or disclose Personal Information for any purpose other than for the specific business purposes set forth in this Agreement, including not retaining, using, or disclosing the Personal Information for any commercial purpose other than providing the services specified in this Agreement, and shall not retain, use, or disclose Personal Information outside the direct business relationship between Processor and Controller."

**Common deficiencies:**
- Permits "internal business purposes" without specification — broad enough to allow processor to use data for service improvement, model training, etc.
- Permits aggregation or de-identification for processor's purposes without controller consent.

### 4. Prohibition on combining personal information

**Required:** The processor cannot combine personal information received from or on behalf of the controller with personal information received from or on behalf of any other person, or collected from the processor's own interactions with consumers, except for specified narrow purposes (typically performing a business purpose for the controller).

**CCPA/CPRA-specific:** §1798.140(ag)(1)(C). This is sometimes called the "no commingling" provision.

**Convergent:** Less explicit in some state laws but present in CCPA/CPRA, CPA, and others. When present, it is typically formulated similarly.

**Compliant pattern:**
> "Processor shall not combine the Personal Information that Processor receives from or on behalf of Controller with Personal Information that Processor receives from or on behalf of another person or persons, or collects from its own interaction with the consumer, provided that Processor may combine Personal Information to perform any business purpose specified in this Agreement."

**Common deficiencies:**
- No combining restriction at all.
- Combining permitted for "service improvement" — generally not a permitted business purpose.

### 5. Required disclosures of subprocessing engagement

**Required:** The processor must notify the controller of any engagement of subcontractors / sub-processors that will process personal information, and ensure the subcontractors are bound by the same restrictions.

**CCPA/CPRA-specific:** §1798.140(ag)(1)(D). Also requires the controller's right to monitor compliance and to take steps to remediate or terminate if processor uses personal information in violation.

**Convergent:** All major state laws require flow-down to sub-processors.

**Compliant pattern:**
- Notification of new sub-processors with reasonable advance notice.
- Right to object.
- Flow-down of all required restrictions to sub-processors.
- Processor liability for sub-processor performance.
- Right of controller to monitor and remediate.

**Common deficiencies:**
- Sub-processor list missing.
- Notification with no objection right.
- No flow-down requirement.
- Disclaimer of processor liability for sub-processors.

### 6. Cooperation with consumer rights requests

**Required:** The processor must assist the controller in responding to consumer rights requests (access, deletion, correction, opt-out of sale/sharing, opt-out of automated decision-making, portability, depending on the state).

**CCPA/CPRA-specific:** §1798.140(ag)(1)(E) and §1798.140(j) require processors to assist with consumer rights requests.

**Convergent:** All major state laws require processor assistance.

**Compliant pattern:**
> "Processor shall provide reasonable assistance to Controller in responding to verifiable consumer requests under applicable state privacy law, including (without limitation) requests for access, deletion, correction, portability, opt-out of sale/sharing, and opt-out of automated decision-making, within timelines reasonably calculated to allow Controller to respond within the time periods required by law."

**Common deficiencies:**
- "Reasonable assistance" without operational commitment.
- Charges for assistance that effectively price out the obligation.
- No timeline commitments — controller's statutory deadline is often 45 days, sometimes shorter; processor delays must allow this.

### 7. Security safeguards

**Required:** The processor must implement reasonable security procedures and practices appropriate to the nature of the personal information.

**CCPA/CPRA-specific:** §1798.100(e) (general security obligation) plus the duty to flow security commitments through processor contracts.

**Convergent:** All major state laws require reasonable security.

**Compliant pattern:** Either a security annex (similar to GDPR Article 32 expectations — see `gdpr_requirements.md` for the structure) or incorporation by reference of the processor's documented security program (SOC 2 Type II, ISO 27001, etc.) plus a commitment to maintain reasonable security.

**Common deficiencies:**
- "Reasonable security" without specification.
- Right to unilaterally degrade security.
- Missing entirely.

### 8. Audit and inspection rights

**Required:** The contract must permit the controller to take reasonable and appropriate steps to ensure that the processor uses personal information in a manner consistent with the controller's obligations.

**CCPA/CPRA-specific:** §1798.140(ag)(1)(D)(ii) requires the controller's right to take reasonable and appropriate steps to stop and remediate unauthorized use. Audit rights are part of this.

**Convergent:** Most state laws require monitoring/audit rights.

**Compliant pattern:** Audit rights with reasonable parameters (annually, on notice, at controller's expense unless triggered by an incident, with confidentiality protections, supplemented by independent audit reports for routine purposes).

**Common deficiencies:**
- Audit rights limited to provision of audit reports only.
- Per-audit fees pricing out the right.
- Notification windows so long they make timely audits impossible.

### 9. Notification of inability to comply

**Required:** The contract must require the processor to notify the controller if the processor cannot meet its obligations under the agreement or applicable law, and the controller must have the right to take reasonable steps to stop and remediate unauthorized use.

**CCPA/CPRA-specific:** §1798.140(ag)(1)(D)(i)(III). Increasingly common in state law convergence.

**Compliant pattern:**
> "Processor shall promptly notify Controller if Processor determines that it can no longer meet its obligations under this Agreement or applicable state privacy law. Upon receipt of such notification, Controller may take reasonable and appropriate steps to stop and remediate unauthorized use of Personal Information."

**Common deficiencies:**
- Missing entirely.
- "Notify within a reasonable time" without specifics.

### 10. Deletion / return of personal information

**Required:** Upon controller request or at the end of the engagement, the processor must delete or return personal information.

**Convergent:** All major state laws require deletion or return; specifics vary.

**Compliant pattern:** Controller choice between return and deletion, including all copies, with timeline (typically 30–60 days) and certification on request.

**Common deficiencies:**
- Processor unilateral choice.
- Carve-outs for "data retained for processor's business purposes."
- No certification mechanism.

### 11. Identification of consumer rights protected

**Required (some states):** The contract must identify the rights of consumers under applicable law, sometimes by listing them or referencing the statute.

**CCPA/CPRA-specific:** Less explicit but implied.

**State-specific:** Some state laws (e.g., Virginia) have more specific reference requirements.

**Compliant pattern:** Recital or section identifying applicable consumer rights and the parties' acknowledgment of those rights.

**Common deficiencies:** Generally less material; flag as minor unless specifically required by an identified state.

### 12. Sensitive personal information / sensitive data

**Required (where applicable):** Where the processing involves sensitive personal information (CCPA/CPRA) or sensitive data (other state laws) — typically including SSN, government ID, financial account, geolocation, racial/ethnic origin, religious beliefs, health, sexual orientation, biometric data, children's data — additional restrictions apply.

**CCPA/CPRA-specific:** Sensitive PI has limited use rights and consumer right to limit use.

**State-specific:** Virginia, Colorado, Connecticut, and others require opt-in consent for processing sensitive data; this affects the processor's role.

**Compliant pattern:** Acknowledgment of sensitive data categories processed (if any), commitments around limited use, and processor support for the controller's consent-management obligations.

**Common deficiencies:**
- No identification of whether sensitive data is processed.
- Generic "all consumer rights" reference without specific sensitive-data treatment.

## Severity calibration for US state privacy DPAs

- **Critical:** Missing the core CCPA/CPRA service-provider/contractor terms (purpose limitation, no-sale, no-retention-outside-purposes, no-combining); missing security; missing breach notification or audit rights.
- **Material:** Sub-processor flow-down deficient; consumer rights assistance lacks operational commitment; sensitive data not addressed where applicable; "reasonable security" without specification.
- **Minor:** Outdated statutory references; minor drafting issues; preferences not requirements.

## State-specific call-outs

Where a single-state DPA is being reviewed (e.g., a "California Service Provider Addendum"):

- Note that other states' laws may also apply to the same data flows (a California addendum does not satisfy Virginia VCDPA for Virginia consumer data).
- Flag the addendum as state-specific in the posture paragraph.
- Suggest a multi-state harmonized DPA addendum if data flows extend beyond the named state.

## Notable evolution: avoid stale references

US state privacy laws are evolving rapidly. Common stale-reference issues:

- DPAs dated 2019–2021 written against pre-CPRA CCPA — many lack "sharing" prohibition, sensitive PI handling, opt-out of automated decision-making.
- DPAs naming only one or two states in scope; the convergent state-law landscape has expanded substantially.
- DPAs referencing the AG's regulations or specific compliance dates that have moved (CCPA regulations have been amended multiple times; CPRA regulations finalized in stages).

When the document predates relevant amendments, flag as a Material gap in the posture and recommend regeneration against current law.

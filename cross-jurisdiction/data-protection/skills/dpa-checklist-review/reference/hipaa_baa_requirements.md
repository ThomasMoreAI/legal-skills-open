# HIPAA Business Associate Agreement Requirements

This reference catalogs the contractual terms required in a HIPAA Business Associate Agreement under 45 CFR §164.504(e), as amended by the HITECH Act and the HIPAA Omnibus Rule. The skill applies these requirements when `regulatory_regime: hipaa_baa` is specified.

## Threshold question: is this actually a BAA situation?

A Business Associate Agreement is required when a covered entity (or another business associate) discloses Protected Health Information (PHI) to a business associate. Threshold questions:

- **Is the data PHI?** PHI is individually identifiable health information held or transmitted by a covered entity or business associate, in any form. If the data is health information about an identifiable individual that relates to past, present, or future physical or mental health, healthcare provision, or healthcare payment, it is PHI.
- **Is the recipient a business associate?** A business associate is a person or entity that performs functions or activities on behalf of, or provides services to, a covered entity that involve access to PHI. Cloud service providers, billing services, IT vendors, claims processing services, document management vendors, and many others.
- **Is the discloser a covered entity or another business associate?** Covered entities are: health plans, health care clearinghouses, and most healthcare providers. Business associates can engage subcontractors via subcontractor BAAs (which substantially mirror primary BAAs).

If the data is not PHI, this skill does not apply — recommend the user use the appropriate skill (general DPA, GDPR, US state privacy) instead.

If the data is PHI but the parties have a different agreement (e.g., a Data Use Agreement for limited data sets, or a Qualified Service Organization Agreement under 42 CFR Part 2), this skill does not apply directly — flag and ask the user to confirm the document type.

## Required terms under 45 CFR §164.504(e)(2)

The HIPAA Privacy Rule prescribes specific contract terms for BAAs at 45 CFR §164.504(e)(2). The Security Rule adds requirements at 45 CFR §164.314(a)(2). Subsequent rulemaking (HITECH 2009, HIPAA Omnibus 2013) added breach notification and direct business-associate liability provisions. The skill checks each of the following.

### 1. Permitted uses and disclosures

**Source:** 45 CFR §164.504(e)(2)(i)(A).

**Required:** The BAA must establish the permitted and required uses and disclosures of PHI by the business associate. Uses and disclosures are limited to those necessary to perform the services for the covered entity, plus a small set of additional purposes permitted by HIPAA (e.g., management and administration of the business associate, data aggregation for the covered entity).

**Compliant pattern:**
- Specific identification of the services for which the business associate is engaged.
- Statement that PHI may be used and disclosed only as necessary to perform those services or as permitted by HIPAA.
- If the BAA permits use for the business associate's management and administration or for data aggregation, that should be explicit.

**Common deficiencies:**
- Permitting uses "for any purpose related to the services" without specification.
- Permitting marketing uses or research uses without proper authorization.
- Permitting "internal business analytics" or model training on PHI — generally not permitted.

### 2. Prohibition on uses and disclosures contrary to law or contract

**Source:** 45 CFR §164.504(e)(2)(ii)(A).

**Required:** Business associate cannot use or further disclose PHI other than as permitted or required by the BAA or as required by law.

**Compliant pattern:**
> "Business Associate shall not use or further disclose PHI other than as permitted or required by this Agreement or as required by law."

**Common deficiencies:**
- Carve-outs for processor "legitimate business purposes" not authorized by HIPAA.
- No reference to "as required by law" — required by the regulation.

### 3. Safeguards

**Source:** 45 CFR §164.504(e)(2)(ii)(B); §164.314(a)(2)(i)(A) for ePHI Security Rule application.

**Required:** Business associate must use appropriate safeguards, and comply with Subpart C of 45 CFR Part 164 (Security Rule) with respect to electronic PHI, to prevent use or disclosure of PHI other than as provided in the BAA.

**Compliant pattern:**
- Explicit commitment to comply with Security Rule with respect to ePHI.
- Reference to administrative, physical, and technical safeguards.
- Often supplemented by a security annex describing specific measures.

**Common deficiencies:**
- "Reasonable safeguards" without reference to Security Rule compliance.
- Missing entirely.
- Right to unilaterally degrade safeguards.

### 4. Reporting of unauthorized uses or disclosures

**Source:** 45 CFR §164.504(e)(2)(ii)(C).

**Required:** Business associate must report to the covered entity any use or disclosure of PHI not provided for by the BAA of which it becomes aware.

**Compliant pattern:**
> "Business Associate shall report to Covered Entity any use or disclosure of PHI not provided for by this Agreement of which it becomes aware, without unreasonable delay and in any event within [N] days of discovery."

**Common deficiencies:**
- "Without unreasonable delay" with no specific timeline.
- Limited to "material" or "significant" violations — the regulation requires reporting all unauthorized uses/disclosures.
- Limited to violations the business associate "knows or should know" — the regulation requires reporting on awareness.

### 5. Breach notification

**Source:** 45 CFR §164.410 (subpart breach notification rules added by HITECH).

**Required:** Business associate must notify covered entity of breaches of unsecured PHI without unreasonable delay and in no case later than 60 calendar days after discovery. Notification must include identification of each individual whose unsecured PHI has been (or is reasonably believed to have been) accessed, acquired, used, or disclosed during the breach.

**Compliant pattern:**
- Specific timeline (typically 30 days or less, to allow covered entity to meet its 60-day individual-notification obligation).
- Required content of breach notification (description of breach, types of PHI involved, individuals affected, mitigation actions, prevention measures).
- Cooperation with covered entity's breach response.

**Common deficiencies:**
- "Without unreasonable delay" with no specific timeline — covered entity has 60 days from BA's discovery; BA delay of more than ~30 days makes timely individual notice impossible.
- Notification only of "material" breaches — non-compliant; HIPAA breach notification covers all breaches above the de minimis exception (low-probability-of-compromise risk assessment).
- No commitment to provide breach details necessary for the covered entity's notifications.

### 6. Sub-business-associate flow-down

**Source:** 45 CFR §164.504(e)(2)(ii)(D); §164.314(a)(2)(i)(B).

**Required:** Business associate must ensure that any subcontractor that creates, receives, maintains, or transmits PHI on behalf of the business associate agrees to the same restrictions and conditions that apply to the business associate. (This is the subcontractor BAA / sub-BAA requirement.)

**Compliant pattern:**
- Explicit commitment to flow down all BAA requirements to subcontractors.
- Optional: notification of subcontractor engagement.
- Liability commitment for subcontractor performance.

**Common deficiencies:**
- "Reasonable efforts" to flow down — non-compliant; the regulation requires actual flow-down.
- Disclaimer of liability for subcontractor performance — inconsistent with HIPAA's direct liability framework.
- No subcontractor list or notification mechanism.

### 7. Access by individuals

**Source:** 45 CFR §164.504(e)(2)(ii)(E).

**Required:** Business associate must make PHI available to the covered entity (or to the individual) as necessary to satisfy the covered entity's obligation to provide individuals with access to their PHI under 45 CFR §164.524.

**Compliant pattern:**
> "Business Associate shall make available to Covered Entity, or to the individual at Covered Entity's direction, PHI maintained by Business Associate in a Designated Record Set, in the time and manner reasonably necessary to permit Covered Entity to comply with 45 CFR §164.524."

**Common deficiencies:**
- Limiting access to information BA holds in its own systems (without recognizing data held in subcontractors' systems).
- Charges that effectively price out access requests.
- No timeline commitment.

### 8. Amendment of PHI

**Source:** 45 CFR §164.504(e)(2)(ii)(F).

**Required:** Business associate must make PHI available for amendment and incorporate amendments as directed by the covered entity, to enable the covered entity to comply with 45 CFR §164.526.

**Compliant pattern:** Commitment to amend or incorporate amendments to PHI on covered entity's instruction, in time and manner consistent with the covered entity's §164.526 obligations.

**Common deficiencies:**
- Missing entirely.
- "Best efforts" without operational commitment.

### 9. Accounting of disclosures

**Source:** 45 CFR §164.504(e)(2)(ii)(G).

**Required:** Business associate must document and make available such disclosures of PHI and information related to such disclosures as would be required for the covered entity to respond to a request for an accounting of disclosures under 45 CFR §164.528.

**Compliant pattern:** Commitment to track and provide accounting-of-disclosures information when requested.

**Common deficiencies:**
- Missing entirely.
- Limited to specific disclosure types — accounting requirements cover most non-treatment/payment/operations disclosures.

### 10. Internal practices, books, and records

**Source:** 45 CFR §164.504(e)(2)(ii)(H).

**Required:** Business associate must make its internal practices, books, and records relating to the use and disclosure of PHI available to the Secretary of Health and Human Services for purposes of determining the covered entity's compliance with HIPAA.

**Compliant pattern:**
> "Business Associate shall make its internal practices, books, and records relating to the use and disclosure of PHI received from, or created or received by Business Associate on behalf of, Covered Entity available to the Secretary of Health and Human Services upon request for purposes of the Secretary determining Covered Entity's compliance with the Privacy Rule."

**Common deficiencies:**
- Conditioning on "subpoena" or "valid legal process" — the regulation requires availability on the Secretary's request.
- Limiting to specific record types — should cover all relevant records.

### 11. Return or destruction of PHI at termination

**Source:** 45 CFR §164.504(e)(2)(ii)(I) and §164.504(e)(2)(ii)(J).

**Required:** At termination of the BAA, if feasible, return or destroy all PHI received from, created, or received by the business associate on behalf of the covered entity. If return/destruction is not feasible, extend protections to the PHI and limit further uses and disclosures.

**Compliant pattern:**
- Return or destruction at termination, at the covered entity's option.
- Explicit handling of the "not feasible" case (continued protection of remaining PHI).
- Certification of destruction on request.

**Common deficiencies:**
- Mandatory destruction without return option, or vice versa.
- "Not feasible" carve-out used as default rather than exception.
- No certification mechanism.

### 12. Authorization to terminate for material breach

**Source:** 45 CFR §164.504(e)(2)(iii).

**Required:** The BAA must authorize termination by the covered entity if the business associate violates a material term of the agreement.

**Compliant pattern:**
> "If Business Associate has violated a material term of this Agreement, Covered Entity may terminate this Agreement upon notice. If termination is not feasible, Covered Entity shall report the violation to the Secretary of Health and Human Services."

**Common deficiencies:**
- Termination right limited to "material breach not cured within X days" without considering that some violations cannot be cured.
- No reference to reporting obligation if termination is not feasible.

## HITECH and Omnibus Rule additions

The 2009 HITECH Act and the 2013 HIPAA Omnibus Rule added:

### Direct business-associate liability

Business associates are now directly liable for HIPAA compliance, not just through their BAAs. The BAA does not need to recite this (it is a matter of law), but it should not contradict it. Common deficiencies:

- BAA limiting BA's liability to the BAA itself, with disclaimer of HIPAA-direct-liability — flag as critical.
- BAA suggesting BA is exempt from direct enforcement — flag as critical.

### Marketing, fundraising, sale of PHI restrictions

HITECH restricts marketing communications using PHI without authorization. The BAA should reflect that BA cannot use PHI for marketing on its own behalf without proper authorization.

### Subcontractor BAAs

As covered above (item 6) — HITECH formalized the sub-BAA requirement. Pre-HITECH BAAs may lack this and need updating.

## Severity calibration for HIPAA BAAs

- **Critical:** Missing breach notification mechanism; missing safeguards / Security Rule reference; missing material-term reporting; missing flow-down to subcontractors; permitted uses too broad to comply with HIPAA.
- **Material:** Timeline gaps (breach notification "without undue delay"); incomplete accounting-of-disclosures provisions; missing subcontractor list; no termination-for-breach right.
- **Minor:** Outdated CFR citations; drafting issues; recital-level deficiencies.

## Special situations

- **Cloud service provider as business associate:** OCR has issued guidance that cloud service providers are business associates if they process PHI. The fact that the CSP cannot read encrypted PHI does not relieve the BA obligation. BAAs covering CSP relationships should address: storage location (relevant to OCR enforcement priorities), encryption key management (does CSP hold keys?), incident response in CSP's environment.
- **Hybrid HIPAA / state privacy:** Many BAA situations also involve state privacy laws (e.g., California consumer health data has CCPA implications independent of HIPAA). A BAA does not satisfy state privacy law requirements; the user may need both a BAA and a state-privacy DPA, or a combined instrument that addresses both regimes.
- **Subcontractor BAAs:** When the user is a business associate engaging a subcontractor, the substantive requirements are identical, but the parties' roles and obligations references may use "Business Associate" and "Subcontractor" terminology. Flag clearly in the report.

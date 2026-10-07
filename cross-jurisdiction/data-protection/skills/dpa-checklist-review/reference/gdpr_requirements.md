# GDPR DPA Requirements

This reference catalogs what a GDPR-compliant DPA must contain. The substantive requirements are in Article 28(3) of the GDPR (mirrored in Article 28(3) of the UK GDPR). Security requirements come from Article 32. International transfer mechanisms come from Articles 44–49 and the EDPB's Schrems II guidance.

The skill applies these requirements when `regulatory_regime: gdpr` is specified. Findings cite specific GDPR articles for traceability.

## Threshold question: does Article 28 even apply?

Article 28 governs controller-processor relationships. It does not govern controller-controller, joint-controller, or processor-sub-processor (which are covered separately by Articles 26 and 28(4)). Before applying this checklist:

- Confirm the parties are in a controller-processor relationship. If the document treats both parties as independent controllers (e.g., a marketing-leads sharing arrangement), Article 28 does not apply directly; the document needs to satisfy Articles 26 (joint controllership) or be analyzed as a controller-controller transfer.
- If the document is a sub-processor agreement (the user is a processor engaging a sub-processor), Article 28 still applies but the parties' roles are processor (as the engaging party) and sub-processor — adjust the analysis accordingly.
- If party roles are ambiguous in the document, flag as a critical issue: ambiguous roles undermine the entire compliance frame.

## Required terms under Article 28(3)

Article 28(3) requires a written contract (or other binding legal act) that sets out the subject matter, duration, nature and purpose of the processing, type of personal data, categories of data subjects, and obligations and rights of the controller. The contract must contain provisions stipulating the processor's obligations on the nine specific items listed in Article 28(3)(a) through (h).

The skill checks each of the following.

### Threshold framework terms (preamble to 28(3))

#### F1. Subject matter and duration of processing

**Source:** Article 28(3) preamble.

**Required:** The contract must specify what processing the processor is performing and for how long.

**Compliant pattern:** A clear "Subject Matter," "Nature and Purpose," "Duration of Processing," or equivalent annex/section that states what the processor does, why, and for how long. Often satisfied by reference to the underlying services agreement, which is acceptable if the underlying agreement is identifiable.

**Common deficiencies:** No duration specified; subject matter described only as "as set forth in the Agreement" without further detail and where "the Agreement" is itself ambiguous; processing duration described as "indefinite."

#### F2. Nature and purpose of processing

**Source:** Article 28(3) preamble.

**Required:** What kind of processing is happening (collection, storage, transfer, analysis, etc.) and why (the business purpose served).

**Compliant pattern:** Annex describing processing activities and purposes, often as a table.

**Common deficiencies:** Generic "all processing necessary to provide the Services" without enumeration; missing entirely.

#### F3. Type of personal data and categories of data subjects

**Source:** Article 28(3) preamble.

**Required:** What personal data is processed (e.g., name, email, IP address, behavioral data) and whose data (e.g., customer end users, employees, prospects).

**Compliant pattern:** Annex with enumerated data categories and data subject categories. Higher specificity is better; "all personal data submitted by Controller" is the bare minimum and is increasingly viewed as insufficient by EU regulators for material processing.

**Common deficiencies:** Catch-all phrasing without enumeration; failure to identify special category data (Article 9) or criminal-conviction data (Article 10) when applicable; missing data subject categories entirely.

#### F4. Obligations and rights of the controller

**Source:** Article 28(3) preamble.

**Required:** The controller's obligations and rights under the agreement.

**Compliant pattern:** Section identifying controller's rights (instructions, audit, sub-processor approval, breach notification receipt) and obligations (lawful basis for processing, providing instructions, etc.).

**Common deficiencies:** Treated as boilerplate; rarely missing entirely but often vague.

### The nine specific provisions of Article 28(3)(a)–(h)

#### A. Article 28(3)(a) — Processor processes only on documented controller instructions

**Required:** The processor processes the personal data only on documented instructions from the controller, including with regard to international transfers, unless required to do so by EU or member state law (in which case the processor must inform the controller before processing, except where that law prohibits such information on important grounds of public interest).

**Compliant pattern:**

> "Processor shall process Personal Data only on documented instructions from Controller, including with regard to transfers of Personal Data to a third country or an international organization, unless required to do so by Union or Member State law to which Processor is subject, in which case Processor shall inform Controller of that legal requirement before processing, unless that law prohibits such information on important grounds of public interest."

**Common deficiencies:**
- Permits processor to process for "Processor's own legitimate business purposes" — not compliant; processor is supposed to be acting solely on controller instructions.
- Does not address international transfers as instructed processing.
- Does not include the "unless required by law" carve-out properly (some DPAs omit the obligation to inform the controller of legal requirements).
- Permits unilateral processor changes to processing — incompatible with controller-instruction model.

#### B. Article 28(3)(b) — Confidentiality of personnel

**Required:** The processor ensures that persons authorized to process the personal data have committed themselves to confidentiality or are under an appropriate statutory obligation of confidentiality.

**Compliant pattern:** Brief statement that processor's personnel are subject to written confidentiality obligations or statutory equivalents.

**Common deficiencies:** Missing entirely; phrased as "generally" or "typically" rather than as a concrete commitment.

#### C. Article 28(3)(c) — Security measures (Article 32)

**Required:** The processor takes all measures required pursuant to Article 32. Article 32 requires technical and organizational measures appropriate to the risk, including (as appropriate): pseudonymization and encryption; ability to ensure ongoing confidentiality, integrity, availability, and resilience; ability to restore availability and access to personal data in a timely manner in the event of a physical or technical incident; a process for regularly testing, assessing, and evaluating the effectiveness of the measures.

**Compliant pattern:** Either a security annex listing specific measures, or incorporation by reference of the processor's documented security program (e.g., SOC 2 Type II report, ISO 27001 certification, the processor's published Trust Center) plus a commitment to maintain measures appropriate to the risk.

**Common deficiencies:**
- "Industry-standard security measures" without specification — insufficient.
- Annex listing measures that are clearly inadequate for the data category (e.g., unencrypted transmission for sensitive data).
- Right to unilaterally degrade security measures without controller consent.
- Missing entirely.

See `gdpr_requirements.md` Section "Article 32 detail" below for what an adequate security annex contains.

#### D. Article 28(3)(d) — Sub-processors

**Required:** The processor respects the conditions referred to in paragraphs 2 and 4 of Article 28 for engaging another processor. Specifically: prior specific or general written authorization from the controller; in the case of general written authorization, the processor must inform the controller of any intended changes (allowing the controller to object); the processor must impose the same data protection obligations on sub-processors via contract; and the processor remains liable for sub-processor performance.

**Compliant pattern:** Section addressing sub-processors with: (i) authorization mechanism (specific or general), (ii) notification of changes (with reasonable advance notice and right to object), (iii) flow-down of obligations, (iv) processor liability for sub-processor acts.

**Common deficiencies:**
- General authorization with no notification mechanism — non-compliant.
- Notification mechanism with too-short objection window (e.g., 7 days).
- No flow-down of obligations — the processor's commitments under this DPA must contractually bind sub-processors.
- Processor disclaimer of liability for sub-processor failures — incompatible with Article 28(4).
- Sub-processor list missing entirely (or only available "on request" with no duty to maintain it).

#### E. Article 28(3)(e) — Assistance with data subject rights

**Required:** Taking into account the nature of the processing, the processor assists the controller by appropriate technical and organizational measures, insofar as possible, in fulfilling the controller's obligation to respond to requests for exercising the data subject's rights laid down in Chapter III (right of access, rectification, erasure, restriction, data portability, objection, automated decision-making).

**Compliant pattern:** Commitment to assist with data subject rights requests, typically including: providing access to the relevant data, supporting deletion or correction, returning data in portable formats, responding within timelines that allow the controller to meet its 30-day Article 12 deadline.

**Common deficiencies:**
- "Best efforts" or "reasonable assistance" without operational commitment.
- Charges for assistance that effectively price out exercising the obligation.
- No SLA or timeline commitment, making it impossible for the controller to meet its own deadlines.
- Limiting assistance to specific request types (e.g., only access requests, not erasure).

#### F. Article 28(3)(f) — Assistance with security, breach notification, DPIAs, and prior consultations

**Required:** Taking into account the nature of the processing and the information available to the processor, the processor assists the controller in ensuring compliance with: Article 32 (security); Articles 33 and 34 (breach notification to authorities and data subjects); Article 35 (Data Protection Impact Assessment); Article 36 (prior consultation with the supervisory authority).

**Compliant pattern:** Commitments to: notify the controller of personal data breaches without undue delay (with a stated timeline, ideally 24–72 hours, certainly aligned with the controller's 72-hour Article 33 obligation); provide information necessary for the controller's breach notifications; provide information for DPIAs; cooperate with prior consultations.

**Common deficiencies:**
- Breach notification "without undue delay" with no specific hours/days — Article 33 obligates the controller to notify within 72 hours; processor delays of more than ~24 hours make this impossible. Insist on a specific number.
- Breach notification only for "confirmed" breaches — inconsistent with the GDPR's risk-based notification standard. Should be triggered by any breach (or sometimes "any incident reasonably suspected to be a breach").
- No commitment to provide breach details necessary for the controller's notification (incident description, categories of data, approximate number of data subjects, likely consequences, mitigation measures).
- Per-incident charges for breach assistance — increasingly viewed as non-compliant by regulators.

#### G. Article 28(3)(g) — Return or deletion at end of processing

**Required:** At the choice of the controller, the processor deletes or returns all personal data to the controller after the end of provision of services relating to processing, and deletes existing copies, unless EU or member state law requires storage of the personal data.

**Compliant pattern:** Section providing controller choice between return and deletion, deletion of all copies (subject to legal retention requirements), and certification of deletion on request.

**Common deficiencies:**
- Processor unilateral choice between return and deletion (controller must have the choice, per Article 28(3)(g)).
- Mandatory return only — operationally difficult for digital data; controller usually wants deletion option.
- Mandatory deletion only without return option — violates the express controller choice requirement.
- Carve-outs that swallow the rule (e.g., "except for data retained for processor's business purposes" — non-compliant; the only carve-out permitted is legally-required retention).
- No timeline for deletion or return.

#### H. Article 28(3)(h) — Audit and information rights

**Required:** The processor makes available to the controller all information necessary to demonstrate compliance with Article 28's obligations, and allows for and contributes to audits, including inspections, conducted by the controller or another auditor mandated by the controller.

**Compliant pattern:** Audit rights with reasonable parameters: notice requirements (typically 30+ days), frequency limits (typically annually unless triggered by an incident), confidentiality protections, allowance for third-party auditors mandated by the controller, alternative satisfaction via independent audit reports (SOC 2 Type II, ISO 27001) for routine purposes.

**Common deficiencies:**
- Audit rights limited to provision of audit reports only, with no on-site or controller-conducted audit option — non-compliant; Article 28(3)(h) requires controller-conducted or controller-mandated audits, not just processor reports.
- Per-audit fees that effectively price out the right.
- Notification windows so long they make timely audits impossible.
- Limitation to once every several years.
- Confidentiality terms so restrictive the auditor cannot report findings to the controller.

### Additional Article 28 obligations beyond 28(3)

#### Article 28(3) closing paragraphs — Processor's instruction-violation duty

**Required:** With regard to point (h) of the first subparagraph, the processor must immediately inform the controller if, in its opinion, an instruction infringes the GDPR or other Union or Member State data protection provisions.

**Compliant pattern:** Express commitment that the processor will notify the controller if an instruction would violate data protection law.

**Common deficiencies:** Frequently missing; not always considered material but should be flagged.

## Article 32 detail — what an adequate security annex looks like

Article 32 requires "appropriate technical and organisational measures." Compliant security annexes typically address:

- **Encryption:** at rest (e.g., AES-256), in transit (TLS 1.2+), key management.
- **Pseudonymization:** where appropriate for the processing purpose.
- **Access control:** authentication, authorization, principle of least privilege, MFA for administrative access, deprovisioning processes.
- **Network security:** firewalls, intrusion detection, segmentation.
- **Application security:** secure development lifecycle, vulnerability management, penetration testing cadence.
- **Operational security:** patching, change management, configuration management.
- **Personnel security:** background checks, security training, NDAs.
- **Physical security:** data center controls, media handling.
- **Resilience:** backup, disaster recovery, RTO/RPO, business continuity testing.
- **Incident response:** detection, response, notification, remediation processes.
- **Audit and monitoring:** logging, log retention, log review, SIEM.
- **Vendor/sub-processor security:** flow-down requirements, vendor risk management.
- **Certifications:** SOC 2 Type II, ISO 27001, PCI DSS, FedRAMP, etc., as applicable.

A security annex that addresses only a subset of these without explanation is a partial finding. Where the data category is sensitive (special category, criminal conviction, biometric, financial), missing measures trigger higher severity.

## International transfer mechanisms (Articles 44–49)

Where the processing involves transfers of EU/UK personal data to non-adequacy countries, the DPA must address a transfer mechanism. The skill triggers transfer-mechanism review when `international_transfer_context` indicates transfers occur.

### Required transfer mechanisms

A non-adequacy transfer requires one of:

- **EU Standard Contractual Clauses (SCCs)** under Commission Implementing Decision 2021/914 — the most common mechanism. The 2021 SCCs come in four modules (controller-to-controller, controller-to-processor, processor-to-processor, processor-to-controller). The DPA must incorporate the correct module.
- **UK SCCs / International Data Transfer Agreement (IDTA)** for UK-origin data.
- **Binding Corporate Rules (BCRs)** — only available for intragroup transfers.
- **Adequacy decision** — applies automatically; no contractual mechanism needed (covers transfers to UK, Switzerland, EEA, Canada [commercial sector], Japan, South Korea, US under Data Privacy Framework certified entities, etc.).
- **Article 49 derogations** — applicable in narrow circumstances; rarely the primary mechanism for routine processor relationships.

### Schrems II / TIA requirements

Following CJEU's Schrems II decision (Case C-311/18), SCCs alone are insufficient when the destination country's law does not provide essentially equivalent protection. The DPA / SCC package should be supported by:

- **Transfer Impact Assessment (TIA)** — formal assessment of destination-country surveillance laws, processor's ability to resist, supplementary measures.
- **Supplementary measures** where indicated by the TIA — typically additional encryption (with EU-held keys), pseudonymization, contractual challenges to government access requests, transparency commitments.

### Common deficiencies on transfer mechanisms

- DPA references "the SCCs" without specifying which Commission decision (2010, 2021) — the 2010 SCCs were repealed effective Dec. 27, 2022; documents still referencing them are non-compliant.
- DPA incorporates the wrong SCC module for the parties' roles.
- DPA mentions SCCs but the SCCs themselves are not attached or executed.
- No TIA referenced or supporting measures specified.
- Transfer mechanism does not cover onward transfers (e.g., processor's sub-processors in third countries).
- DPA references US-EU Data Privacy Framework (DPF) certification but does not condition continued reliance on the processor maintaining DPF certification.

### UK-specific notes

UK GDPR substantially mirrors EU GDPR Article 28. Differences relevant to DPA review:

- UK SCCs / IDTA replace EU SCCs for transfers from UK.
- ICO has issued guidance on the IDTA Addendum, which can be appended to EU SCCs to cover UK transfers — an efficient mechanism for DPAs covering both.
- UK adequacy for the EU expires periodically; current status should be verified at review time.

## Severity calibration for GDPR DPAs

When assessing severity:

- **Critical:** Article 28(3) terms entirely missing in a way that makes the processor unable to meet its statutory obligations (e.g., no breach notification mechanism); transfer mechanism missing where transfers occur; security measures clearly inadequate for the data category.
- **Material:** Article 28(3) terms partially present in non-compliant form (e.g., breach notification "without undue delay" with no specific timeline; sub-processor notification with insufficient objection window); transfer mechanism present but with deficiencies (wrong SCC module, missing TIA references).
- **Minor:** Drafting issues that do not affect compliance (e.g., outdated regulator names, typos in statutory references); preferences-not-requirements (e.g., audit notice period preference).

The detailed-findings section in the report must address every Critical and Material item; Minor items can be aggregated in the table.

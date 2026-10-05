# AI Agent DPA Addendum — Template

**Notice:** this is a drop-in template for the parent Data Processing Agreement (GDPR Art. 28). Legal review is required before execution. Adapt by replacing `{placeholder}` values.

---

## Agent Processing Addendum to the Data Processing Agreement

**Controller:** {controller legal name}
**Processor:** {processor legal name}
**Effective Date:** {YYYY-MM-DD}
**Version:** v{n.m}
**Parent DPA reference:** {document id, date}

This Addendum supplements the parent Data Processing Agreement with obligations specific to agent processing under Article 28 of the General Data Protection Regulation (Regulation (EU) 2016/679) and equivalent provisions of the African data-protection regimes listed in the Regional Annexes. Capitalised terms not defined here have the meaning given in the parent DPA or in GDPR Art. 4.

### 1. Subject matter and scope

This Addendum governs the processing of Personal Data by an Agent Feature operated by Processor on behalf of Controller. An Agent Feature is autonomous or semi-autonomous AI software that plans, calls tools, and acts on the controller's workforce or end-users' behalf.

### 2. Documented instructions (Art. 28(3)(a))

Processor shall process Personal Data only on documented instructions from Controller. The parent DPA plus this Addendum, plus the published Action Catalogue, constitute the documented instructions for agent processing.

### 3. Confidentiality (Art. 28(3)(b))

Processor shall ensure that all natural persons authorised to operate, supervise, or audit Agent Features are subject to enforceable confidentiality obligations.

### 4. Security of processing (Art. 28(3)(c); Art. 32)

Processor shall implement appropriate technical and organisational measures including:

- Encryption of Personal Data at rest and in transit (TLS 1.2 or later).
- Append-only, hash-chain integrity-verified audit log of every tool call.
- Agent Service Principal least privilege; quarterly access review.
- Kill-switch with ≤ 5-second propagation SLA, invocable by Processor operations and by Controller admin role per tenant.
- Approval Events signed cryptographically for every irreversible-class tool call.
- Red-team adversarial testing as defined in the Agent Red-Team Test Plan; weekly full set; quarterly external assessment.

### 5. Sub-processors (Art. 28(2); Art. 28(4))

- Controller grants general written authorisation for the sub-processors listed in Annex B; Processor shall maintain the list current.
- Processor shall provide 30 calendar days' written notice of any material change (addition, replacement, scope change) to the sub-processor list; Controller may object in writing within that period.
- For model providers: Processor shall ensure contracts with model providers include a verifiable training-data exclusion commitment; evidence available on request.

### 6. Data subject rights (Art. 28(3)(e); Arts. 12-22)

- Processor shall assist Controller in fulfilling data subject requests, including access, rectification, erasure, restriction, portability, and objection.
- Agent Feature memory contents and action history shall be included in the scope of data subject rights requests.
- Erasure of Agent Feature memory contents shall be completed within 30 days of Controller's written instruction, with a Certificate of Erasure produced.

### 7. Notification of personal data breach (Art. 28(3)(f); Art. 33)

- Processor shall notify Controller without undue delay and in any event within seventy-two (72) hours of becoming aware of a personal data breach.
- Notification shall include: nature of the breach, categories and approximate number of data subjects, categories and approximate number of records, name and contact of the data protection officer, likely consequences, measures taken or proposed.
- Agent-specific breach scenarios — cross-tenant retrieval leak, prompt-injection disclosure, audit-log integrity compromise, memory-tier leak — are subject to this clause.

### 8. Data protection impact assessment (Art. 28(3)(f); Art. 35)

- Processor shall provide reasonable assistance to Controller for any data protection impact assessment, including the AI Data Flow and DPIA artefact referenced in Annex C.

### 9. Audit rights (Art. 28(3)(h))

- Controller has the right to audit Processor's compliance with this Addendum.
- Processor may, in lieu of an on-site audit, provide current SOC 2 Type II, ISO/IEC 27001, and ISO/IEC 42001 certifications and the agent-specific evidence pack assembled per the Evidence Pack Spec.
- Controller retains the right to a focused on-site audit where the certifications and evidence pack are insufficient for the Controller's regulatory obligations.

### 10. Return or deletion of personal data (Art. 28(3)(g))

- On termination of the parent DPA, Processor shall return or delete all Personal Data including Agent Feature memory contents and action history, at Controller's choice, within 30 days, and shall produce a Certificate of Deletion.

### 11. International data transfers (Art. 44 et seq.)

- Transfers from the EEA / UK to third countries shall rely on an adequacy decision where one is in effect (including the EU-US Data Privacy Framework where the recipient is certified) or, where no adequacy decision applies, on Standard Contractual Clauses (Commission Implementing Decision 2021/914) supplemented by a transfer impact assessment and supplementary measures.
- Annex D names the transfer mechanism per direction.

### 12. Agent-specific obligations

- **Reversibility classification** — Action Catalogue documents reversibility class per tool; irreversible-class tool calls require Approval Events.
- **Autonomy level** — declared per Agent Feature in the Agent Feature PRD; changes require ADR and Controller notification.
- **Memory tiering** — opt-in for long-term memory at tenant level; erasure verifiable.
- **In-product disclosure** — Processor maintains the agent disclosure modal and the "performed by an agent" notification in the user interface.

### 13. Liability and indemnity

- As set out in the parent DPA and the master services agreement; this Addendum does not enlarge or diminish those terms.

### 14. Annexes

- Annex A — Supervision Matrix per Agent Feature.
- Annex B — Sub-processor list and verification status.
- Annex C — AI Data Flow and DPIA reference.
- Annex D — International transfer mechanism per direction.
- Annex E — Regional Annex (KE / NG / ZA / UG / RW) where applicable.

### 15. Signatures

| Party | Signatory | Title | Date |
|-------|-----------|-------|------|
| Controller | | | |
| Processor | | | |

---

**End of Addendum.**

---

## Regional Annex stubs

### Kenya (KE DPA 2019)

- Notification to Office of the Data Protection Commissioner (ODPC) per s.43 within 72 hours.
- Data residency expectations per ODPC guidance.
- ODPC AI guidance (2024) overlay observed.
- Cross-border transfer per s.49 — adequacy or appropriate safeguards.

### Nigeria (NDP Act 2023)

- Notification to Nigeria Data Protection Commission (NDPC) per Art. 28 within 72 hours.
- NDPC AI advisory observed.
- Cross-border transfer per Schedule.

### South Africa (POPIA 2013)

- Notification to Information Regulator under s.22 as soon as reasonably possible.
- s.71 automated decision-making protections — right to object, right to explanation — extended to agent decisions.
- Cross-border transfer per s.72.

### Uganda (DPPA 2019)

- Notification to Personal Data Protection Office (PDPO) per s.23 immediately.
- Data residency considerations per s.19.
- No AI-specific clause in the DPPA 2019; profile under general data-protection obligations.

### Rwanda (DP Law 2021)

- Notification to National Cyber Security Authority (NCSA) per Art. 25 within 48 hours.
- Cross-border transfer per Art. 48.

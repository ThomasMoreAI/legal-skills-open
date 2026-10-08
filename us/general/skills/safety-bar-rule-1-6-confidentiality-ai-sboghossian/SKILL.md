---
name: safety-bar-rule-1-6-confidentiality-ai-sboghossian
title: Bar Rule 1.6 — Confidentiality and AI Use
description: Use when assessing whether a lawyer's use of an AI tool complies with the professional duty of client confidentiality under ABA Model Rule 1.6 and its analogs in MENA and European bar codes. Covers the four main confidentiality risks of AI tool use (data transmission, training data, data residency, cross-tenant isolation), required technical and contractual safeguards, PII-redaction obligations, and jurisdiction-specific MENA data-residency requirements for KSA, UAE, and Lebanon clients.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/safety/safety-bar-rule-1-6-confidentiality-ai
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
---

# Bar Rule 1.6 — Confidentiality and AI Use

## When to use this

Apply whenever:
- A lawyer user asks whether they can paste client documents into an AI tool.
- A user asks about data residency, training data policy, or vendor confidentiality.
- A law firm is evaluating AI vendors for client-matter work.
- A user shares raw, unredacted client information in a conversation.
- A compliance review of AI tool use in a law practice is required.

## The confidentiality duty — what the rules say

### ABA Model Rule 1.6 (US)
"A lawyer shall not reveal information relating to the representation of a client unless the client gives informed consent, the disclosure is impliedly authorized in order to carry out the representation, or the disclosure is permitted" by a listed exception.

**The AI implication**: transmitting client information to an AI vendor — even as part of a query — is a "revelation" of client information to a third party. Unless the AI vendor has appropriate contractual and technical controls, this could violate Rule 1.6.

### MENA analogs

**Lebanon**: The Code of Professional Conduct (Nizám al-mihna) for Lebanese advocates imposes strict secrecy duties (sirr al-mihna) that prohibit disclosure of client information outside authorized legal proceedings. Using a third-party AI service without appropriate confidentiality safeguards could breach these obligations.

**KSA — Saudi Bar**: The confidentiality duty is embedded in the Code of Law Practice (Royal Decree M/38) and reinforced by the KSA PDPL — personal data of clients must not be transmitted to processors without a lawful basis and adequate contractual safeguards (Art. 29 PDPL).

**UAE — Federal Law on Legal Profession + PDPL**: Similar framework; lawyers have professional confidentiality duties plus data-protection obligations under the UAE Federal Decree-Law No. 45 of 2021 on Personal Data Protection.

**DIFC / ADGM**: DIFC Law No. 5 of 2020 on Data Protection and ADGM Data Protection Regulations 2021 — both GDPR-aligned — impose data-processor contractual requirements equivalent to GDPR Art. 28.

### European analogs

**UK — SRA Code of Conduct**: Principle 6 (behave in a way that maintains the trust the public places in you and the provision of legal services) combined with GDPR data-protection obligations. Law firms are data controllers; AI vendors are data processors requiring a DPA.

**France**: The secret professionnel under French law (Art. 226-13 Code pénal) is one of the broadest in Europe. The Conseil National des Barreaux has raised concerns about AI tools that process client data outside controlled environments.

**EU — GDPR**: Lawyers are data controllers; instructing an AI vendor to process client personal data requires a GDPR-compliant DPA (Art. 28), a legal basis for processing, and — for cross-border transfers — standard contractual clauses.

## The four AI-specific confidentiality risks

### Risk 1: Data transmission to AI vendor
Every query containing client facts is transmitted to the AI vendor's infrastructure. **Mitigation**: use only AI tools operating under a DPA that prohibits disclosure and use of client data for any purpose other than providing the service.

### Risk 2: Training data concern
Consumer AI tools may train on user inputs, potentially incorporating client information into the model's weights and — in the worst case — surfacing it to other users. **Mitigation**: require a contractual no-training-on-data clause; verify it in the vendor's terms of service or enterprise agreement.

### Risk 3: Data residency
Client data may be processed in a jurisdiction with weak privacy protections or government access powers incompatible with confidentiality obligations. **Mitigation**: specify contractual data residency requirements matching the client's jurisdiction; prefer EU/GDPR-compliant or MENA-region hosting for MENA clients.

### Risk 4: Cross-tenant isolation
In shared multi-tenant AI deployments, another law firm's data could theoretically be returned in responses. **Mitigation**: use platforms with enforced tenant isolation at the storage and retrieval layers — see [[safety-client-confidentiality-cross-tenant]].

## Best practices

### Technical safeguards
- PII redaction before sending to third-party LLMs — see [[safety-pii-redaction-before-rag]].
- Encryption in transit (TLS 1.3) and at rest (AES-256).
- Audit logs of all AI queries containing client data — accessible to the supervising lawyer.
- Tenant-scoped access: only matter-team members can query matter-related AI history.

### Contractual safeguards
- **Data Processing Agreement (DPA)**: mandatory for GDPR/PDPL compliance; covers purpose limitation, sub-processor controls, deletion, incident notification.
- **No-training clause**: explicit prohibition on training the model on submitted content.
- **Data residency clause**: specifies which region(s) data may be processed in.
- **Confidentiality clause**: AI vendor commits to confidentiality obligations.
- **Sub-processor list**: vendor discloses all sub-processors; notification on changes.

### Operational practices
- Update the firm's client engagement letter to disclose AI use and obtain informed consent.
- Never use a consumer-grade AI tool (e.g., a free web-based chatbot without enterprise controls) for matter-specific client data.
- For jurisdictions with heightened sensitivity (KSA, UAE, Lebanon), prefer tools with in-region hosting.
- Document AI tool selection decisions in the firm's technology risk register.

## What never to send to AI without redaction

- National ID numbers, passport numbers, civil registration numbers → `[NAT_ID]`
- IBAN, account, and routing numbers → `[ACCOUNT]`
- Health information → `[HEALTH]`
- Client names where the matter is not publicly known → `[CLIENT]`
- Specific transaction or case details that could identify a party → anonymize/hypothesize

See [[safety-pii-redaction-before-rag]] for the full redaction taxonomy.

## MENA-specific data residency considerations

| Jurisdiction | Data-residency preference | Regulatory basis |
|-------------|--------------------------|-----------------|
| KSA | In-region preferred; cross-border transfer requires SDAIA-authorized safeguards | KSA PDPL Art. 29 |
| UAE (onshore) | In-region preferred; contractual safeguards required for cross-border | UAE PDPL Art. 22 |
| DIFC | GDPR-aligned; DIFC Law No. 5/2020 | DIFC DP Law |
| ADGM | GDPR-aligned; ADGM DPR 2021 | ADGM DPR |
| Lebanon | No formal data-protection law as of May 2026; professional secrecy applies | Bar Code of Conduct |
| Egypt | Egypt PDPL (Law 151 of 2020) — transfers permitted with Data Protection Centre approval or adequacy | Egypt PDPL |

## Consequences of failure

- **Bar discipline**: violation of confidentiality is among the most serious professional-conduct offenses in all jurisdictions; sanctions range from reprimand to disbarment.
- **Civil liability**: clients may sue for breach of confidentiality, professional negligence, or breach of fiduciary duty.
- **Regulatory sanctions**: data-protection authorities (ICO, CNIL, SDAIA, UAE Data Office) may impose fines under their respective GDPR-equivalent laws.

## Related skills

- [[safety-bar-rule-1-1-competence-ai]] — competence duties for AI tool use
- [[safety-bar-rules-confidentiality]] — bar-rules confidentiality architecture
- [[safety-client-confidentiality-cross-tenant]] — cross-tenant isolation guarantees
- [[safety-pii-redaction-before-rag]] — PII redaction before external LLM calls
- [[safety-ai-not-privileged-disclaimer-us-heppner]] — privilege status of AI conversations
- [[safety-cross-border-data-transfer-gcc-eu]] — cross-border data transfer obligations

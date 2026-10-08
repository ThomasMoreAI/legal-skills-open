---
name: prompt-pack-data-processing-agreement-sboghossian
title: Data Processing Agreement
description: 'Use when a data controller needs to formalise its relationship with a data processor under a Data Processing Agreement (DPA), covering GDPR Article 28 requirements, security obligations, sub-processor approval, audit rights, and breach notification. MENA-aware: DIFC DP Law Art. 26, ADGM DP Regs, UAE PDPL, KSA PDPL all require controller-processor agreements with broadly similar content. Essential for any cloud, SaaS, or outsourcing arrangement.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-data-processing-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Data Processing Agreement

A Data Processing Agreement (DPA) is the legal contract that governs how a processor (e.g., a cloud provider, SaaS vendor, or outsourced service) handles personal data on behalf of the controller (the company that collects the data). Under GDPR Art. 28, DIFC DP Law, and equivalent MENA frameworks, a DPA is not optional — operating without one is itself a breach of the applicable data protection law.

## When to use this

- Engaging a new SaaS vendor, cloud provider, or outsourced service that will process personal data on the company's behalf.
- An existing vendor relationship has been identified as requiring a DPA that does not yet exist.
- A GDPR or other privacy compliance audit has flagged missing DPAs.
- The company is a processor itself (providing services to another controller) and needs a standard DPA to offer to its customers.
- A customer or investor due diligence has requested confirmation of DPA coverage across all data processing relationships.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Controller name and jurisdiction | The party responsible for determining the purpose and means of processing | Ask the user |
| Processor name and jurisdiction | The party carrying out the processing on behalf of the controller | Ask the user |
| Description of processing activities | Must be specified; vague descriptions are non-compliant | Ask the user to describe in detail |
| Categories of personal data | Determines security requirements and risk level | Ask the user |
| Categories of data subjects | Scope of potential impact in a breach | Ask the user |
| Governing privacy law(s) | GDPR / UAE PDPL / DIFC DP Law / KSA PDPL — determines mandatory content | Ask the user |
| Duration of processing | When processing will end and what happens to data at the end | Ask the user |

## Optional inputs

- List of approved sub-processors (if the controller wants to approve a specific list rather than a general authorization).
- Specific security certifications required (ISO 27001, SOC 2 Type II, GDPR DPA).
- Transfer mechanism if the processor is located outside the controller's jurisdiction (Annex referencing SCCs).
- Jurisdiction-specific clauses (DIFC Schedule, ADGM Schedule).

## Document structure

The DPA follows the structure mandated by GDPR Art. 28(3) and its equivalents.

### 1. Parties and background
- Full legal names and addresses of both parties.
- Brief description of the commercial relationship (the "main agreement" under which the DPA sits).
- Statement of the parties' roles: [Controller] is the controller; [Processor] is the processor.

### 2. Definitions
Defined terms aligned with the applicable law(s): personal data, special category data, processing, data subject, personal data breach, supervisory authority / DPA authority, sub-processor, controller, processor. Do not invent definitions that conflict with the governing law.

### 3. Details of processing (mandatory content — Article 28 and equivalents)
Include as an Annex or Schedule with the following fields:

| Field | Content |
|---|---|
| Subject matter of processing | What the processing is about |
| Duration | Period of the engagement |
| Nature of processing | The operations performed (collection, storage, retrieval, analysis, transfer, etc.) |
| Purpose of processing | Why the controller is having this data processed |
| Types of personal data | Categories of data processed |
| Categories of data subjects | Who the data relates to (employees, customers, end-users, etc.) |

### 4. Processor's obligations

**4.1 Process only on instructions**
The processor shall process personal data only on the documented instructions of the controller, except where required by applicable law (in which case the processor must inform the controller, unless prohibited by law from doing so).

**4.2 Confidentiality**
Persons authorised to process the personal data must be under an appropriate obligation of confidentiality, whether contractual or statutory.

**4.3 Security measures (Article 32 / equivalent)**
The processor must implement appropriate technical and organisational measures to protect personal data:
- Encryption of personal data at rest and in transit.
- Ongoing confidentiality, integrity, availability, and resilience of processing systems.
- Ability to restore the availability and access to personal data in the event of a physical or technical incident.
- Process for regularly testing and evaluating security measures.
Examples: ISO 27001 certification, SOC 2 Type II report, penetration testing schedule, access control policies, incident response procedures.

**4.4 Sub-processors**
The processor must:
- Not engage sub-processors without prior written consent of the controller (specific or general authorization — specify which applies).
- Where general authorization is given, the processor must inform the controller of any new sub-processors, giving the controller opportunity to object.
- Impose the same data protection obligations on sub-processors as those in this DPA (flow-down).
- Remain fully liable to the controller for sub-processor non-compliance.

**4.5 Assistance to the controller**
The processor shall assist the controller with:
- Responding to data subject rights requests (access, erasure, portability, rectification) — within a timeframe that allows the controller to meet its own response deadline.
- Security assessments (Article 32 obligations).
- Data Protection Impact Assessments (DPIAs) where required.
- Prior consultation with the supervisory authority.

**4.6 Data breach notification**
The processor must notify the controller without undue delay (and in any event within 24–48 hours, to allow the controller to meet its own 72-hour regulatory notification deadline) after becoming aware of a personal data breach. The notification must include:
- Nature of the breach.
- Categories and approximate number of data subjects affected.
- Categories and approximate volume of records affected.
- Name and contact of the data protection contact.
- Likely consequences.
- Measures taken or proposed to address the breach.

**4.7 Deletion or return of data**
At the end of the engagement, the processor must either return or delete all personal data, at the controller's choice. The processor must certify deletion in writing. Any copies held for legal compliance purposes must be disclosed to the controller.

**4.8 Audit rights**
The controller has the right to audit the processor's compliance with this DPA:
- The processor must provide all information necessary to demonstrate compliance.
- The controller may conduct audits itself or through an authorized auditor, with reasonable prior notice (typically 30 days unless an incident warrants immediate audit).
- The processor may satisfy audit requirements by reference to third-party certifications (ISO 27001, SOC 2) for their covered scope.

### 5. Controller's obligations
The controller warrants that:
- It has a lawful basis for the processing it has instructed.
- It has provided all required privacy notices to data subjects.
- The personal data is accurate and limited to what is necessary.
- Any instructions it gives to the processor comply with applicable law.

### 6. Cross-border transfers
If the processor is located outside the controller's jurisdiction, or if the processor engages sub-processors in third countries:
- Identify the transfer mechanism (EU SCCs Module 2 for controller-to-processor; DIFC SCCs; ADGM SCCs; UAE PDPL Art. 22 mechanisms).
- Attach as an Annex to the DPA.
- The DPA must specify that the processing (including sub-processor transfers) complies with Chapter 5 GDPR (or equivalent) at all times.

### 7. Liability and indemnification
- The processor is liable to the controller for breaches of its obligations under this DPA.
- In the event of regulatory fines arising from processor non-compliance, the processor indemnifies the controller.
- Each party's liability under the DPA may be subject to the cap in the main commercial agreement — but note that some regulators have taken the position that liability caps cannot limit the "full amount" of damages in the event of serious non-compliance.

### 8. Governing law
Specify the governing law — should align with the applicable data protection framework (EU/UK GDPR: EU member state or UK law; DIFC DP Law: DIFC law; ADGM DP Regs: ADGM law; UAE PDPL: UAE federal law; KSA PDPL: KSA law).

## Jurisdictional DPA requirements

| Jurisdiction | Requirement | Authority |
|---|---|---|
| EU (GDPR) | Art. 28 mandates written contract; specific content required | Lead Supervisory Authority |
| UK (UK GDPR) | Same as EU; post-Brexit equivalents | ICO |
| DIFC | DIFC DP Law 2020 Art. 26; written contract required with equivalent content to GDPR Art. 28 | DIFC Commissioner of Data Protection |
| ADGM | ADGM DP Regs 2021 Art. 21; equivalent requirements | ADGM Commissioner |
| UAE PDPL | Art. 20 requires controller to contractually bind processor; implementing regulations specify content | UAE DPA (TDRA) |
| KSA PDPL | Art. 15 requires contracts with processors; NDMO regulations specify obligations | NDMO |

## Common mistakes

- A DPA with no Processing Details Annex — without knowing what data is processed for what purpose, the agreement is unenforceable and demonstrates a lack of seriousness.
- No sub-processor clause — sub-processors are one of the most common sources of data breaches; the controller needs visibility and flow-down obligations.
- DPA breach notification timelines that are longer than the controller's regulatory notification deadline — the processor's 48-hour notification to the controller must leave time for the controller's 72-hour regulatory notification.
- Audit rights that are purely theoretical — stating audit rights in the DPA but not actually conducting audits is an increasing target of DPA enforcement.
- DPA signed at the start of a relationship but never updated when processing activities change significantly.

## Related skills

- [[prompt-pack-data-breach-response-plan]]
- [[prompt-pack-data-retention-policy]]
- [[prompt-pack-cross-border-data-transfer-assessment]]
- [[prompt-pack-data-subject-access-request-procedure]]
- [[prompt-pack-cookie-policy]]

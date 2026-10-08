---
name: prompt-pack-third-party-data-sharing-agreement-sboghossian
title: Third-Party Data Sharing Agreement
description: Use when a user needs to draft a data sharing agreement between two or more organizations that jointly determine or separately control the purposes and means of processing personal data. Covers controller-to-controller and controller-to-processor configurations, legal bases for sharing, data subject rights obligations, security standards, onward transfer restrictions, and liability allocation. Especially relevant for MENA jurisdictions (UAE PDPL, KSA PDPL, Lebanon draft law, Egypt PDPL) and GDPR-governed cross-border flows.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-third-party-data-sharing-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Third-Party Data Sharing Agreement

## When to use this

Use this skill when two or more independent organizations need a contractual framework governing their exchange of personal data — for example:

- A bank sharing KYC data with an insurance affiliate for joint product underwriting
- A government agency sharing civil records with an authorized data-analytics vendor
- Two companies in a joint venture sharing employee or customer data across their boundary
- A company receiving data from a third-party data broker for marketing enrichment

This is distinct from a vendor DPA (processor arrangement) because both parties may act as independent controllers, or one party may receive data as a secondary controller rather than a pure processor. The agreement must expressly allocate controller/processor status, legal basis, and data subject obligations.

## Required inputs

| Input | Why it matters | Sensible default |
|-------|---------------|-----------------|
| Party A full legal name + registered address | Identifies the data discloser; determines applicable law | Prompt user |
| Party B full legal name + registered address | Identifies the data recipient | Prompt user |
| Description of personal data to be shared | Defines the scope and sensitivity; triggers special-category rules | Prompt user |
| Purposes for which data will be shared | Legal basis depends on purpose; limits onward use | Prompt user |
| Controller / processor designation for each party | Changes the entire obligation structure | Determine from context — if B has discretion over purpose, it is a controller |
| Governing law | Determines which data protection regime applies | Jurisdiction where data subjects are located, or where primary controller is established |

## Optional inputs

- **Data subject categories** (employees, customers, patients, children) — children's data triggers heightened obligations under every MENA and EU regime
- **Frequency and volume** (one-time transfer vs. ongoing API feed) — affects security and incident response commitments
- **Sensitive / special categories** (health, financial, biometric, criminal) — explicit safeguards required
- **Sub-sharing permissions** — whether B may further share with its own processors or affiliates
- **Retention schedule** — how long each party holds the shared data
- **Technical transfer mechanism** (API, SFTP, encrypted USB, data room)
- **Applicable certification standards** (ISO 27001, SOC 2)

## Document structure

1. **Definitions** — "Personal Data," "Controller," "Processor," "Data Subject," "Processing," "Security Incident," "Applicable Law" (list each jurisdiction instrument)
2. **Purpose and scope of data sharing** — enumerate dataset fields; state purpose limitation explicitly; include negative covenant against use for other purposes
3. **Legal basis for sharing** — each party must identify its legal basis independently (consent, contract performance, legitimate interests, legal obligation, vital interests, public task); if relying on legitimate interests, include a brief balancing test narrative
4. **Controller / processor designations** — table or clause assigning role of each party for each data stream; a party may be controller for one stream and processor for another
5. **Data subject rights obligations** — which party responds to access, rectification, erasure, portability, objection requests; response timeline; cost allocation; cooperation obligations when a request touches the other party's data
6. **Security obligations** — minimum technical and organizational measures (TOM clause); incident notification timeline (72 hours under GDPR; UAE PDPL requires notification "without undue delay"; KSA PDPL requires notification within 72 hours to SDAIA and affected individuals); joint incident response obligations
7. **Cross-border transfer mechanisms** — standard contractual clauses (EU SCCs or equivalents), adequacy decisions, binding corporate rules; UAE PDPL requires TDRA approval for certain transfers; KSA PDPL requires transfers to jurisdictions with adequate protection or SDAIA-approved mechanisms
8. **Permitted onward sharing** — whitelist of permitted sub-processors / sub-recipients; prohibition on further sharing without prior written consent
9. **Retention and deletion** — party-specific retention schedules; certified deletion or return of data on termination
10. **Audit rights** — right to audit or request compliance certification; frequency; notice period; cost allocation
11. **Liability and indemnification** — each party liable for its own non-compliance; mutual indemnification for regulatory fines caused by the other; liability cap (typically annual fees or fixed amount)
12. **Term and termination** — initial term; survival of data protection obligations; termination for material breach; obligations on expiry
13. **Governing law and dispute resolution** — choice of court or arbitration; if MENA parties, specify Arabic as governing language or state that English prevails in case of conflict
14. **Schedules** — Schedule A: Data inventory (fields, volumes, sensitivity); Schedule B: Technical and organizational measures; Schedule C: Approved sub-recipients

## Jurisdictional notes

| Jurisdiction | Key instrument | Notable requirement |
|---|---|---|
| UAE (onshore) | UAE Federal Decree-Law No. 45/2021 on Personal Data Protection (PDPL) | Requires TDRA registration for certain processing activities; cross-border transfers require TDRA approval unless adequate country; special categories (health, financial, children) have heightened requirements |
| DIFC | DIFC Data Protection Law 2020 (DP Law No. 5 of 2020) | Common-law framework modelled on GDPR; DPO mandatory for large-scale or sensitive processing; SCCs available for international transfers |
| ADGM | ADGM Data Protection Regulations 2021 | Also GDPR-modelled; accountability principle emphasized; joint controller agreements must allocate obligations in writing |
| KSA | Personal Data Protection Law (PDPL) / Royal Decree M/19 (2021); implementing regulations 2023 | Sensitive data = health, genetic, biometric, financial, children, criminal; cross-border transfer to SDAIA-approved countries or via SDAIA-approved mechanisms; breach notification within 72 hours |
| Lebanon | Draft Personal Data Protection Law (not yet in force as of 2026); Law 81/2018 on e-transactions applies indirectly | Consult applicable sectoral law (banking secrecy Law 3/1956, medical records) until national law enacted |
| Egypt | Personal Data Protection Law No. 151/2020 and Implementing Regulations 2020 | Data Protection Authority approval required for certain cross-border transfers; privacy impact assessment required for high-risk processing |
| EU / GDPR | GDPR Art. 26 (joint controllers must conclude arrangement allocating obligations) | Joint controllers must make a joint controller agreement "essence" available to data subjects; each remains independently liable |
| UK | UK GDPR + Data Protection Act 2018 | Post-Brexit: UK SCCs (IDTA) for transfers to non-adequate countries |

**Civil-law trap (LB, EG, KSA onshore):** US-style indemnification clauses referencing "consequential damages" may be unenforceable or read down by civil law courts under general tort principles. Draft liability provisions referencing foreseeable direct damages.

**Language trap:** In KSA and UAE onshore, Arabic-language versions of contracts may prevail in court if not expressly subordinated to an English version. For dual-language data sharing agreements, include a "governing language" clause stating which version prevails.

## Drafting standards

- **Purpose limitation** must be explicit and narrow. Avoid drafting broad purposes such as "business operations" — regulators (particularly DIFC PDID and UAE TDRA) scrutinize vague purpose statements.
- **No `[INSERT X]` artifacts in final output** unless a template was specifically requested. Populate all defined terms based on user inputs.
- **Security annex** should specify concrete measures: encryption at rest (AES-256), in transit (TLS 1.2+), access control (role-based, MFA), pseudonymization where applicable, regular penetration testing.
- **Incident notification** clauses must match the shortest timeline among the applicable regimes (often 72 hours); build in an internal escalation chain.
- **Retention schedule** should be a table with field-level or dataset-level retention periods, not a single blanket period.
- Call out defaults at the top of the draft (e.g., "Governing law: UAE Federal unless otherwise specified").

## Common mistakes

- **Misclassifying a controller as a processor** — if Party B decides how to use the data, it is a controller; a processor only processes on documented instructions
- **Omitting Article 26 GDPR / equivalent joint controller clause** — required when two or more controllers jointly determine purposes and means
- **Vague purpose statements** — "improving services" is not a valid purpose limitation
- **Missing sub-processor whitelist** — GDPR and DIFC require written authorization; unlimited permission is disfavored
- **US-style consequential damages waiver without civil-law review** — may be void under Lebanese or Egyptian civil codes
- **Ignoring Arabic language requirement** — KSA and UAE consumer contracts often require an Arabic version
- **No data breach cooperation clause** — both parties need coordinated notification obligations when they share the same dataset

## Related skills

- [[prompt-pack-vendor-data-protection-addendum]]
- [[prompt-pack-vendor-risk-assessment-questionnaire]]
- [[kb-mena-data-protection]]
- [[draft-data-processing-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]

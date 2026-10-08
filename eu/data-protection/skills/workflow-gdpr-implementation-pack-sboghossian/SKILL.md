---
name: workflow-gdpr-implementation-pack-sboghossian
title: GDPR / Data Protection Implementation Pack
description: Use when an organization needs to implement GDPR compliance (or the parallel MENA data protection regimes — UAE PDPL, Saudi PDPL) from scratch or remediate gaps. Covers all twelve implementation phases from data mapping through governance, with a parallel track for MENA-specific requirements. Produces a compliance dashboard, updated privacy notice, cookie consent infrastructure, vendor DPAs, DSR processes, breach response playbook, and staff training records.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/workflow/workflow-gdpr-implementation-pack
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# GDPR / Data Protection Implementation Pack

## Purpose

This workflow implements a data protection compliance program under GDPR (EU) and/or equivalent MENA regimes (UAE Federal Decree-Law 45/2021 on Personal Data Protection; Saudi Arabia's Personal Data Protection Law). The program is structured in twelve phases, spanning a typical 90–180 days for a medium-size organization.

---

## Inputs

| Input | Required | Notes |
|-------|---------|-------|
| Organization type | Yes | Tech company, professional services, retailer, healthcare, etc. |
| Jurisdictions in scope | Yes | Which regulations apply: GDPR, UAE PDPL, KSA PDPL, DIFC DPL, UK GDPR |
| Estimated data subject types | Yes | Employees, customers, vendors, visitors |
| Estimated number of systems | Yes | Drives data mapping scope |
| Current compliance posture | Recommended | Any existing privacy notices, policies, consents |
| Organization size | Yes | Determines DPO appointment obligation and reporting timelines |
| Timeline / go-live pressure | Recommended | Allows phase prioritization |

---

## Parallel Regime Map

| Regime | Applies to | Key similarities to GDPR | Key MENA differences |
|--------|-----------|------------------------|---------------------|
| GDPR | EU/EEA data subjects anywhere in the world | Data subject rights; lawful basis; DPO; breach notification; DPIAs | Same |
| UK GDPR | UK data subjects | Very similar to EU GDPR post-Brexit | UK adequacy decisions differ from EU; ICO is regulator |
| UAE PDPL (Fed. Decree-Law 45/2021) | Personal data processed in UAE | Similar data subject rights; breach notification; DPO-equivalent | No legitimate interests basis (absent from PDPL); different consent standards; data localization potential |
| KSA PDPL | Saudi personal data | Rights of access, correction, deletion | Mandatory consent for most processing; stricter than GDPR in several areas; SDAIA as regulator |
| DIFC Data Protection Law 2020 | DIFC-registered entities | Closely modelled on GDPR | DIFC Commissioner of Data Protection as regulator; some divergence in group exemptions |
| ADGM Data Protection Regulations | ADGM-registered entities | Closely modelled on GDPR | ADGM Registration Authority oversight |

---

## Phase 1 — Data Mapping (Weeks 1–3)

**Objective**: Know what personal data you hold, where it is, and what you do with it.

**Activities:**
1. Identify all systems and databases that contain personal data (CRM, HR, marketing platform, cloud storage, analytics, support ticketing, etc.)
2. For each system: identify — categories of personal data; categories of data subjects; purposes of processing; legal basis; retention period; who has access; whether data is shared with third parties; whether data is transferred outside the home country/EEA/UAE
3. Conduct department interviews (HR, marketing, IT, finance, legal) to catch non-obvious processing
4. Document in a **Data Inventory / Record of Processing Activities (RoPA)** — required under GDPR Art. 30; good practice under MENA regimes

**Output**: Data inventory spreadsheet / RoPA with at minimum: processing activity name, controller/processor, categories of data, data subjects, purposes, legal basis, transfers, retention, security measures.

---

## Phase 2 — Lawful Basis Assignment (Weeks 2–4)

**Objective**: Assign a valid legal basis to each processing activity.

**Available bases under GDPR (compare with MENA regimes):**

| Basis | GDPR Art. | UAE PDPL | KSA PDPL | Notes |
|-------|-----------|---------|---------|-------|
| Consent | 6(1)(a) | Yes | Yes (primary) | Must be freely given, specific, informed, unambiguous under GDPR; KSA PDPL leans heavily on consent |
| Contract | 6(1)(b) | Yes | Limited | Processing necessary for performance of a contract with the data subject |
| Legal obligation | 6(1)(c) | Yes | Yes | Processing required by law |
| Vital interests | 6(1)(d) | Not specific | Not specific | Emergency situations; narrow use |
| Legitimate interests | 6(1)(f) | Not available | Not clearly available | Key GDPR basis absent from UAE PDPL and uncertain in KSA |
| Public task | 6(1)(e) | Government bodies | Government bodies | Limited to public authorities |

**MENA critical point**: Legitimate interests (GDPR Art. 6(1)(f)) is the most flexible basis under GDPR for commercial processing. It is **not available** under UAE PDPL. UAE-operating organizations relying on legitimate interests for GDPR purposes must identify a different basis (typically consent or contract) for UAE PDPL compliance.

---

## Phase 3 — Privacy Notice Rewrite (Weeks 3–5)

**Objective**: Publish a GDPR/PDPL-compliant privacy notice.

See [[draft-privacy-policy]] for the template. Key required elements under GDPR:
- Identity and contact details of the controller (and DPO if appointed)
- Purposes and legal bases for each category of processing
- Legitimate interests where relied upon (LIA summary)
- Categories of recipients
- International transfers and safeguards
- Retention periods (or criteria for determining them)
- Data subject rights and how to exercise them
- Right to withdraw consent
- Right to lodge a complaint with the supervisory authority

**MENA additional requirements:**
- UAE PDPL: notice in Arabic (or Arabic alongside English) where data subjects are Arabic speakers
- KSA PDPL: Arabic-language notice; specific disclosures about cross-border transfer consents

---

## Phase 4 — Consent Mechanisms (Weeks 4–6)

**Objective**: Implement granular, revocable consent infrastructure.

GDPR-compliant consent:
- **Cookies**: PECR (UK) / ePrivacy Directive (EU): consent required for non-essential cookies; cookie banner must allow genuine choice; no pre-ticked boxes; categories must be specific
- **Marketing communications**: opt-in required for email/SMS marketing; unsubscribe mechanism on every communication
- **Optional features**: if a product feature processes personal data beyond what is necessary for the core service, it should be consent-based and optional

**Technical implementation**: a Consent Management Platform (CMP) such as OneTrust, Cookiebot, Usercentrics, or TrustArc should be implemented. The CMP must:
- Record consent (timestamp, mechanism, version of notice shown)
- Allow withdrawal as easily as giving consent
- Distinguish between cookie categories (strictly necessary, functional, analytics, advertising)

---

## Phase 5 — Data Subject Rights (DSR) Process (Weeks 5–8)

**Objective**: Ability to respond to access, rectification, erasure, and other requests within legal timelines.

| Right | GDPR response deadline | UAE PDPL | KSA PDPL |
|-------|----------------------|---------|---------|
| Access | 1 month (extendable to 3 months for complex) | Response required; specific timeline in implementing regulations | 30 days |
| Rectification | 1 month | Similar | Similar |
| Erasure ("right to be forgotten") | 1 month | Similar | Similar |
| Portability | 1 month | Not specified | Not specified |
| Objection | Stop processing upon receipt (for direct marketing); assess for other grounds | Similar | Not clearly available |

**Process components:**
1. Intake channel: email (dpo@company.com), in-app form, or postal address
2. Identity verification: before actioning a request, verify the requester's identity (proportionate to sensitivity of data)
3. Response template: for each right, a standardized response template
4. Tracking: log all requests, date received, date responded, outcome
5. Escalation: when is a request refused? (exemptions under GDPR Art. 12; document the basis)

---

## Phase 6 — Breach Response Playbook (Weeks 6–8)

**Objective**: 72-hour notification readiness.

GDPR breach response:
- **Detection → Assessment → Notify** must complete within 72 hours (GDPR Art. 33) for notifiable breaches (likely risk to data subjects' rights)
- High-risk breaches additionally require **notification to affected data subjects** (Art. 34) without undue delay

**Playbook elements:**
1. **Detection procedures**: how will breaches be identified? (monitoring, employee reporting, third-party notification)
2. **Incident severity classification**: minor (no notification needed) / significant (supervisory authority notification) / high-risk (also notify individuals)
3. **Notification template**: GDPR Art. 33(3) requires: nature of breach; categories and approximate number of data subjects; categories and approximate number of records; contact details of DPO; likely consequences; measures taken or proposed
4. **Communication protocols**: who is the internal breach response team? who approves notification to authorities?
5. **Documentation**: all breaches must be documented regardless of whether notification is required (Art. 33(5))

**MENA notification timelines:**
- UAE PDPL: notify TDRA (Telecommunications and Digital Government Regulatory Authority) "without delay"
- KSA PDPL: notify SDAIA within 72 hours for breaches that harm data subjects

---

## Phase 7 — Vendor Data Processing Agreements (Weeks 7–10)

**Objective**: GDPR-compliant DPAs with all processors.

See [[draft-dpa-gdpr]] for template. Every vendor (processor) that processes personal data on your behalf must have a DPA covering:
- Subject matter, nature, purpose, and duration of processing
- Types of personal data and categories of data subjects
- Processor's obligations: process only on documented instructions; confidentiality; security; sub-processor management; data subject rights assistance; deletion/return on termination; audit rights
- Standard Contractual Clauses (SCCs) for international transfers where applicable

**Vendor tier prioritization:**
- Tier 1 (high-risk processors): CRM, HR platform, marketing automation, cloud infrastructure, analytics — DPA required immediately
- Tier 2 (standard processors): email service providers, support tools, productivity platforms — DPA required; standard template acceptable
- Tier 3 (low-risk/transient): couriers, professional advisors handling limited data — DPA or appropriate contractual provisions required

---

## Phase 8 — International Transfers (Weeks 8–12)

**Objective**: Legal mechanism in place for all personal data transfers outside the EEA (for GDPR) and outside the UAE/KSA (for MENA regimes).

| Transfer mechanism | Description |
|-------------------|-------------|
| Adequacy decision | EU Commission has declared the destination country adequate; no additional safeguard needed |
| Standard Contractual Clauses (SCCs) | EC-approved contract terms; new Modular SCCs adopted June 2021 |
| Binding Corporate Rules (BCRs) | For intra-group transfers; complex to implement; approved by lead supervisory authority |
| Certification / Codes of Conduct | Emerging mechanisms; not yet widely available |
| IDTA (UK) | UK-specific International Data Transfer Agreement; post-Brexit equivalent to SCCs |

**MENA applicability**: UAE PDPL restricts transfers of personal data outside the UAE to countries with an "adequate level of protection" or under specific contractual safeguards. KSA PDPL similarly restricts cross-border transfers. Organizations processing data of UAE or KSA data subjects must review all data flows out of these countries.

---

## Phase 9 — Records of Processing (Art. 30) (Ongoing from Phase 1)

The RoPA (Record of Processing Activities) initiated in Phase 1 must be:
- Maintained and kept current
- Available to supervisory authorities on request
- In writing (electronic format is fine)

Organizations with <250 employees are partially exempt from the GDPR Art. 30 obligation (certain conditions apply); however, maintaining a RoPA is good practice regardless of size, and MENA PDPL regimes do not carry this exemption.

---

## Phase 10 — DPIA Process (Weeks 8–12)

**Objective**: Data Protection Impact Assessment capability for high-risk processing.

GDPR Art. 35 requires a DPIA before commencing processing that is "likely to result in a high risk" to individuals, including:
- Systematic profiling
- Large-scale processing of special categories (health, biometrics, criminal records)
- Systematic monitoring of publicly accessible areas
- New technologies

**DPIA template elements:**
1. Description of the processing and its purposes
2. Assessment of necessity and proportionality
3. Risks to data subjects
4. Measures to address those risks
5. DPO consultation (if appointed)

---

## Phase 11 — Training (Weeks 10–16)

**Objective**: All staff with access to personal data understand their obligations.

Training program:
- **All staff**: awareness training (what is personal data, why it matters, how to handle data subject requests, how to report a breach) — 1-hour annual module
- **Data owners / system administrators**: deeper training on their specific systems and obligations
- **Legal/compliance team**: GDPR/PDPL advanced training; DPO qualification if applicable
- **Training records**: document completion; required for demonstrating accountability (GDPR Art. 5(2))

---

## Phase 12 — Governance (Weeks 12–20)

**Objective**: Sustainable data protection governance structure.

Elements:
- **DPO appointment**: mandatory for public authorities; for private sector when large-scale systematic monitoring or large-scale special categories processing occurs; recommended for any significant data processor
- **Privacy committee**: cross-functional (legal, IT, HR, marketing, product); meets quarterly
- **Policy framework**: data protection policy; data retention policy; breach response policy; acceptable use policy
- **Compliance dashboard**: tracks ongoing obligations (DSR response times, breach record, DPA status, training completion)
- **Annual review**: update the RoPA, re-assess DPIAs for changed processes, renew vendor DPAs

---

## Timeline Summary

| Phase | Weeks | Deliverable |
|-------|-------|------------|
| 1–2 | 1–4 | Data inventory + lawful basis register |
| 3–4 | 3–6 | Updated privacy notice + cookie consent |
| 5–6 | 5–8 | DSR process + breach playbook |
| 7–8 | 7–12 | Vendor DPAs signed + international transfer mechanisms |
| 9–10 | Ongoing | RoPA maintained + DPIA process documented |
| 11–12 | 10–20 | Training delivered + governance structure in place |

Total: **90 days minimum** for essential compliance (Phases 1–8); **180 days** for full program including governance and training.

---

## Related Skills

- [[draft-privacy-policy]]
- [[draft-dpa-gdpr]]
- [[review-gdpr-readiness]]
- [[workflow-hire-employee-pack]]
- [[workflow-full-due-diligence-pack]]

---
name: gdpr-health-data-aks-builds
title: GDPR for Health Data
description: When the user is processing health, genetic, or biometric data of people in the EU/EEA, UK, or other GDPR-aligned jurisdictions, or designing controls for special-category health data. Also use when the user mentions "GDPR," "Article 9," "special category data," "Article 6," "lawful basis," "explicit consent," "controller," "processor," "joint controller," "DPA," "data processing agreement," "DPIA," "DPO," "Article 30," "records of processing," "72 hour breach," "SCCs," "Standard Contractual Clauses," "Schrems II," "Transfer Impact Assessment," "TIA," "Recital 26," "UK GDPR," "EHDS," or "European Health Data Space." For US HIPAA, see hipaa-compliance. For operational PHI controls applicable globally, see phi-handling. For audit-log design, see audit-logging.
author: aks-builds
author_url: https://github.com/aks-builds/healthcareskills/tree/main/skills/gdpr-health-data
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
sources:
- title: Article 9 Conditions
  path: references/article-9-conditions.md
- title: Cross Border Transfer
  path: references/cross-border-transfer.md
---

# GDPR for Health Data

You are an expert in the EU General Data Protection Regulation as it applies to **special category** health data, and in the related regimes (UK GDPR, the Swiss FADP, sectoral health laws of EU Member States, and the new European Health Data Space regulation). Your job is to translate Articles 6, 9, 30, 32, 33, 34, 35, and Chapter V into concrete engineering and program controls — without offering binding legal advice. Direct interpretation questions to the organization's Data Protection Officer (DPO) and counsel.

## Initial Assessment

Read `.agents/healthcare-context.md` first (fall back to `.claude/healthcare-context.md`). Look for jurisdictions, controller/processor role, EHR/clinical systems, DPO presence, existing certifications, and cross-border flows. If the context file is missing, ask: which Member State(s) and/or UK; controller or processor; what health data and from whom; where it is stored and processed; and what triggered the question (new product, DPIA, breach, transfer review).

---

## What Counts as Health Data

GDPR defines **data concerning health** broadly (Art. 4(15) and Recital 35): personal data related to physical or mental health, including the provision of healthcare services, that reveal information about health status. **Genetic data** (Art. 4(13)) and **biometric data for the purpose of uniquely identifying a natural person** (Art. 4(14)) are separately defined.

All three are **special category** data under **Article 9** — prohibited by default, with specific conditions in Art. 9(2) that allow processing.

---

## Lawful Basis — Article 6 + Article 9 Stacking

For special category health data you generally need BOTH:

- An Art. 6(1) lawful basis (consent, contract, legal obligation, vital interests, public task, legitimate interests — though legitimate interests is hard to use for health data and is unavailable to public authorities for their tasks)
- An Art. 9(2) condition lifting the prohibition

### Article 9(2) Conditions Most Relevant to Health

| Art. 9(2) | Plain-language summary |
|-----------|------------------------|
| (a) | Explicit consent (where not prohibited by EU/MS law) |
| (b) | Employment, social security, social protection law obligations |
| (c) | Vital interests where data subject incapable of consent |
| (d) | Legitimate activities of a not-for-profit body |
| (e) | Data manifestly made public by the data subject |
| (f) | Legal claims / courts acting in judicial capacity |
| (g) | Substantial public interest (with EU/MS legal basis + safeguards) |
| (h) | Preventive/occupational medicine, medical diagnosis, healthcare provision, treatment, management of health systems, under EU/MS law and by/under responsibility of a professional bound by professional secrecy |
| (i) | Public interest in public health (with safeguards) |
| (j) | Archiving/scientific/historical research/statistical purposes (Art. 89(1) safeguards) |

The two healthcare-bread-and-butter conditions are **9(2)(h)** for treatment/care and **9(2)(j)** with Art. 89 safeguards for research. **9(2)(a) explicit consent** is sometimes used for non-treatment, non-research consumer-health processing — but consent is hard to keep "freely given" and is revocable.

---

## Roles: Controller, Processor, Joint Controller

| Role | Defining feature |
|------|------------------|
| Controller | Determines purposes and means of processing |
| Processor | Processes on behalf of the controller, under documented instructions |
| Joint controller | Two or more controllers jointly determine purposes and means (Art. 26) — needs an arrangement transparent to data subjects |

Required contracts:

- **Art. 28 Data Processing Agreement (DPA)** between controller and processor — required elements include subject matter, duration, nature, purpose, type of data, categories of data subjects, obligations and rights of the controller, processor commitments (confidentiality, security, sub-processor approval, audit, deletion/return, breach notification)
- **Art. 26 joint controller arrangement** when truly joint

Sub-processors require controller authorization (general or specific) and flow-down terms.

---

## Records of Processing — Article 30

Both controllers and processors must maintain Records of Processing Activities (RoPA). Required content differs slightly between Art. 30(1) (controllers) and Art. 30(2) (processors). The Art. 30(1) record typically includes:

- Name and contact details of controller, joint controller, representative, DPO
- Purposes of processing
- Categories of data subjects and categories of personal data
- Categories of recipients (including third countries)
- Transfers to third countries and the transfer mechanism + safeguards
- Retention periods where possible
- General description of technical and organisational security measures

The small-undertaking exemption (Art. 30(5)) generally does NOT apply when processing includes special category data — so health-data processors and controllers maintain RoPAs regardless of size.

---

## DPIA — Article 35

A Data Protection Impact Assessment is required when processing is likely to result in a high risk to rights and freedoms. Health data processing is almost always DPIA territory, especially when combined with large scale, profiling, automated decision-making, vulnerable subjects, new technologies, or systematic monitoring. National supervisory authorities publish "must-DPIA" lists.

DPIA contents (Art. 35(7)):

- Systematic description of processing operations and purposes
- Assessment of necessity and proportionality
- Assessment of risks to data subjects
- Measures to address risks — safeguards, security measures, mechanisms to demonstrate compliance

If residual high risk remains after mitigation, Art. 36 prior consultation with the supervisory authority is required.

---

## DPO — Article 37

A Data Protection Officer is **required** when:

- Processing by a public authority (with narrow exceptions)
- Core activities require large-scale, regular and systematic monitoring of data subjects
- Core activities involve large-scale processing of special category data (most health organizations meet this)

Member State law may impose broader DPO requirements. The DPO must be involved in DPIAs and act as the contact point for the supervisory authority and data subjects.

---

## Breach Notification — Articles 33 & 34

| Notification | Trigger | Timing |
|--------------|---------|--------|
| To supervisory authority (Art. 33) | Personal data breach unlikely to NOT result in risk | Without undue delay, where feasible no later than **72 hours** after becoming aware |
| To data subjects (Art. 34) | Breach likely to result in **high** risk | Without undue delay |

Processors must notify their controller without undue delay; the controller assesses the risk and notifies the authority/subjects. Document every breach (including those not notified) and the reasoning.

---

## Security — Article 32

Art. 32 requires appropriate technical and organisational measures considering the state of the art, costs, and the risk. It explicitly mentions:

- Pseudonymisation and encryption
- Ongoing confidentiality, integrity, availability, resilience of processing systems
- Restore ability after physical/technical incident
- Regular testing, assessment, evaluation of the effectiveness of measures

Approved codes of conduct and certification mechanisms (Art. 40, 42) may serve as evidence of compliance. ISO 27001/27701 and ISO 27799 (health information security) are commonly used by health processors.

---

## Cross-Border Transfers — Chapter V

GDPR restricts transfers of personal data to countries outside the EEA. Available mechanisms:

| Mechanism | When to use |
|-----------|-------------|
| Adequacy decision (Art. 45) | Recipient country recognized as adequate by the Commission |
| Standard Contractual Clauses 2021/914 (Art. 46) | Most common — the modular SCCs |
| Binding Corporate Rules (Art. 47) | Intra-group transfers, approved by lead SA |
| Approved code of conduct / certification (Art. 46) | Emerging |
| Derogations (Art. 49) | Narrow, case-by-case (explicit consent, contract performance, important public interest) — not for routine transfers |

### Schrems II and TIAs

Following Schrems II, transfers under SCCs (and other Art. 46 tools) require a **Transfer Impact Assessment**: assess the legal regime of the destination country (government access, redress mechanisms) and identify **supplementary measures** (technical, contractual, organisational) where necessary. For sensitive health data, technical measures (strong encryption, pseudonymisation with keys held in the EEA, split processing) are often required.

For US transfers, the **EU-US Data Privacy Framework** provides an adequacy basis for certified US recipients — but assess scope, ongoing certification status, and any litigation risk before relying on it as the sole basis.

---

## Anonymisation vs. Pseudonymisation — Recital 26

Per Recital 26, the GDPR does not apply to **truly anonymous** information (no longer relating to an identified or identifiable person). The test considers all means **reasonably likely** to be used by the controller or anyone else, including singling out, linkability, and inference.

**Pseudonymisation** (Art. 4(5)) remains personal data — the additional information that would re-identify is kept separately and subject to controls. Pseudonymisation is a recognised safeguard (Art. 32) but is not an off-switch for GDPR.

See **phi-handling** for the operational toolkit (k-anonymity, differential privacy, etc.) — those concepts apply under GDPR with the Recital 26 reasonableness test as the legal yardstick.

---

## Data Subject Rights

| Right (Article) | Highlights |
|-----------------|------------|
| Access (Art. 15) | Copy of personal data + meta about processing; one month, extendable |
| Rectification (Art. 16) | Correct inaccurate data |
| Erasure / "right to be forgotten" (Art. 17) | With exceptions (legal obligation, public health, research) |
| Restriction (Art. 18) | Pause processing in defined circumstances |
| Portability (Art. 20) | Where based on consent or contract AND automated — receive in structured machine-readable format |
| Object (Art. 21) | Particularly to direct marketing; also to public-task/legitimate-interests processing |
| Automated decisions / profiling (Art. 22) | Right not to be subject to solely automated decisions with legal or similarly significant effects, except in narrow conditions with safeguards |

Health-data-specific carve-outs: Member State law often restricts erasure where data is needed for ongoing treatment, public health, or research with Art. 89 safeguards. Document the controller's response policy.

---

## Member State Derogations

Article 9(4) allows Member States to maintain or introduce further conditions, including limitations, for genetic, biometric, or health data. This means even a perfectly GDPR-compliant design may need adjustment for each country (e.g., Germany's Bundesdatenschutzgesetz, France's Code de la santé publique and CNIL methodology of reference, Italy's Garante codes of conduct, Spain's LOPDGDD, etc.). Always confirm Member State overlays before assuming an EU-wide answer.

---

## UK GDPR

After Brexit, the UK retained GDPR as **UK GDPR** plus the **Data Protection Act 2018**. Substantively very similar to EU GDPR with some divergences and active reform proposals. Key practical differences:

- ICO is the UK supervisory authority (not an EDPB member)
- UK has its own adequacy decisions and IDTA / UK Addendum to SCCs for transfers out of the UK
- The UK has issued adequacy decisions for many jurisdictions, including the EU

For organizations operating in both the UK and EU, expect a UK representative if no UK establishment, an EU representative if no EU establishment, and two RoPAs reflecting the two regimes.

---

## European Health Data Space (EHDS)

The European Health Data Space regulation establishes:

- **Primary use** of electronic health data — patients' rights to access their data, cross-border exchange via MyHealth@EU
- **Secondary use** — a governance framework for research, innovation, policy-making, and statistics access via Health Data Access Bodies, with standardised data quality, formats, and security
- Manufacturers of EHR systems will face conformity assessment for interoperability and security; medical device/AI rules continue to apply for products that meet those definitions

EHDS interacts with GDPR (it does not override Art. 9) and with sectoral medical device, AI Act, and Data Governance Act rules. Expect Member State implementing measures.

---

## Engineering Implications (Checklist)

| Concern | Practical control |
|---------|-------------------|
| Article 9 condition | Identify the condition once per processing purpose; reflect in RoPA and DPIA |
| Records | Maintain RoPA in a tool that survives staff turnover |
| Consent (where used) | Granular, revocable, evidence retained |
| Data minimisation | Collect only what is necessary; field-level review at design |
| Pseudonymisation | Default-on for analytics environments; keys held by separate role |
| Encryption | At rest (AES-256) and in transit (TLS 1.2+); see **phi-handling** |
| Access controls | RBAC/ABAC with purpose-of-use; audit per **audit-logging** |
| DPA | In place before any processing starts |
| Sub-processor list | Public-facing, updated, change-notification per DPA |
| Transfers | Mapped flow inventory, SCC + TIA per non-adequate destination |
| Retention | Defined per purpose, automated where possible |
| Breach process | 72h SA clock, decision tree for Art. 34 notification |
| DPIA | Templated, triggered by intake form, reviewed by DPO |
| DSR handling | Workflow with identity verification, exception logic, audit trail |

---

## Common Anti-Patterns

- Treating "consent" as the universal lawful basis for health data — when 9(2)(h) for care or 9(2)(j) for research is more defensible
- Stacking only Article 6 and skipping the Article 9 condition
- Relying on US adequacy without monitoring certification status
- Drafting one DPIA at launch and never revisiting on material change
- Designing for EU but ignoring Member State law (especially DE, FR, IT, ES, NL)
- Assuming pseudonymisation = anonymisation
- Cross-border transfer documentation absent for a SaaS that quietly hosts in a third country

---

## Output Format

When advising on a GDPR question:

1. Identify role(s): controller, processor, joint controller, recipient
2. State the Article 9(2) condition and the Article 6(1) basis
3. Identify safeguards triggered: DPIA, DPO involvement, Art. 89 (research), Art. 32 security
4. Map cross-border flows and the transfer mechanism
5. State Member State / UK overlays to confirm with local counsel
6. List concrete engineering controls
7. Note any items requiring DPO/legal sign-off

Do not produce binding legal opinions. Refer to current regulation text, EDPB guidance, supervisory authority guidance, and the organization's DPO and counsel.

---

## Task-Specific Questions

1. Which EU/EEA Member State(s) and/or the UK are in scope, and which supervisory authority is the lead — and are there Member State derogations under Article 9(4) that apply to this processing?
2. Is the organization acting as controller, processor, joint controller, or recipient for this activity, and is that role documented (Art. 26 / Art. 28 agreement)?
3. Which Article 9(2) condition is being relied on for processing health/biometric/genetic data, and which Article 6(1) basis sits underneath it?
4. Is a DPO in place (mandatory for large-scale special-category processing under Art. 37(1)(c)), and has the DPO been consulted on this scenario?
5. Are there cross-border transfers outside the EEA, and what mechanism is in use (adequacy decision, SCCs 2021/914 with TIA, BCRs, derogations)?
6. Has a DPIA been completed (required under Art. 35(3)(b) for large-scale special-category processing), and what is the residual risk and mitigation status?
7. What individual-rights workflows are live (Art. 15-22) and are response timelines (typically one month, extendable to three) being met today?

---

## Related Skills

- **healthcare-context**: tells you whether EU/EEA/UK is in scope at all, and which Member States
- **hipaa-compliance**: parallel US regime for cross-border or multi-regime designs
- **phi-handling**: operational controls (de-identification, encryption, access) that satisfy Art. 32
- **healthcare-cybersecurity**: security program design supporting Art. 32 and breach readiness
- **audit-logging**: detection and Art. 33/34 evidentiary support
- **hitrust-csf**: certification framework with GDPR-mapped controls
- **21-cfr-part-11**: when EU clinical trial data is also in scope alongside Annex 11

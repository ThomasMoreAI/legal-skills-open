# 14 — GPAI Code of Practice, Voluntary Codes, Right to Explanation (art. 56, 95, 86)

Three distinct instruments that often get conflated. Each has a specific addressee, legal weight, and operational role.

| Instrument | Article | Addressee | Legal weight | When in force |
|---|---|---|---|---|
| **GPAI Code of Practice** | **art. 56** | GPAI providers (incl. systemic-risk) | **Operative compliance instrument** until harmonised standards land | Published **2025-07-10**; adequacy confirmed by Commission + AI Board **2025-08-01**; underlying obligations apply since 2025-08-02; Commission enforcement from 2026-08-02 |
| **Voluntary codes of conduct** | **art. 95** | Any provider or deployer (esp. non-high-risk) | Voluntary; signals due diligence | 2026-08-02 |
| **Right to explanation** | **art. 86** | Affected natural persons (against deployers of high-risk AI) | Mandatory; individual right | 2026-08-02 — but it operates against deployers of Annex III high-risk systems, whose obligations the 2026 AI Omnibus deferred to 2027-12-02; verify the final Omnibus text for art. 86 sequencing |

## 1. GPAI Code of Practice — art. 56

### 1.1 Purpose and structure

Art. 56 mandates the **AI Office** (Commission unit established under art. 64) to **encourage and facilitate the drawing up of codes of practice at Union level** for GPAI providers. Codes of practice are the de facto operative instrument for arts. 53–55 GPAI obligations until harmonised European standards are published in the OJEU under art. 40.

Codes shall cover at minimum (art. 56(2)):

(a) The means to ensure that information provided is up to date in light of market and technological developments
(b) Adequate level of detail for the **summary of training content** (art. 53(1)(d))
(c) Identification of type and nature of **systemic risks** at Union level, including their sources where appropriate
(d) **Risk assessment and mitigation measures** at Union level, including their effectiveness
(e) **Reporting** of serious incidents and possible corrective measures
(f) Internal **risk management** and **governance**
(g) Cybersecurity protections of the GPAI model and physical infrastructure

Codes are drafted by GPAI providers + AI Office + civil society + experts. Once finalised, the Commission may by implementing act give them **general validity** at Union level (art. 56(6)).

**Status**: the GPAI Code of Practice was published in final form on **2025-07-10**, structured in three chapters:

| Chapter | Addressee | Operationalizes |
|---|---|---|
| **Transparency** | All GPAI providers | art. 53(1)(a)(b) — model documentation form for AI Office + downstream providers |
| **Copyright** | All GPAI providers | art. 53(1)(c) — copyright policy, art. 4(3) CDSM rights-reservation compliance |
| **Safety & Security** | Systemic-risk GPAI providers only | art. 55 — systemic-risk assessment, model evaluations, incident reporting, cybersecurity |

The Commission and AI Board confirmed the Code's **adequacy** on **2025-08-01**. Signatories include the major frontier-model providers; the AI Office publishes the signatory list. Non-signatories must demonstrate compliance by alternative means (art. 56(7)) and face closer scrutiny.

### 1.2 Status as compliance evidence (art. 56(8))

Adherence to a Commission-approved code of practice provides a **rebuttable presumption** that the GPAI provider complies with relevant obligations. This is the GPAI analogue of art. 40 presumption (which applies to harmonised standards for high-risk AI).

For GPAI providers without an approved code, the Commission may demand demonstration of equivalent compliance "by other adequate means" (art. 56(7)). In practice: prepare to map your governance against the published code's measures.

### 1.3 Operational implications for GPAI providers

| Action | Why |
|---|---|
| Sign, or map governance against, the **GPAI Code of Practice** (published 2025-07-10, adequacy 2025-08-01) | Gives the operative compliance script |
| Adopt the code's measures into AIMS (ISO 42001 cl. 5.2 AI policy + Annex A.2.2) | Establishes documented adherence |
| Map code measures to ISO 42001 controls (especially A.4.2 doc, A.6.2.6 monitoring, A.8.5 info-for-parties, A.10.3 supply chain) | Generates audit-ready evidence |
| For systemic-risk GPAI: adopt code's red-team protocol, evaluations, and post-market monitoring template | Satisfies art. 55 with rebuttable presumption |
| Evaluate against an open evaluation framework (e.g., **ML-BOM** for inventory, **NIST AI 100-2** + **MITRE ATLAS** for adversarial coverage) | Substantive evidence, even before code adoption |

### 1.4 Relationship to art. 95 voluntary codes

Art. 56 codes are for **GPAI obligations** (a regulatory category). Art. 95 codes are **voluntary** and address **non-high-risk** AI obligations (a different regulatory category). A GPAI provider may simultaneously adopt:

- An art. 56 code of practice (operative for arts. 53–55)
- An art. 95 voluntary code of conduct (signalling broader due diligence)

The two are complementary, not substitutable.

## 2. Voluntary codes of conduct — art. 95

### 2.1 Purpose

Art. 95 directs the AI Office and Member States to **encourage and facilitate** voluntary codes of conduct that promote the **voluntary application** of some or all of the requirements set out in Chapter III, Section 2 (arts. 8–15) to **AI systems other than high-risk** AI systems.

In effect: a non-high-risk provider voluntarily binds itself to high-risk-style obligations to demonstrate due diligence. Useful for:

- B2B sales where customer procurement frameworks reward documented governance
- Industry self-regulation in sensitive but non-Annex-III domains (e.g., recommendation systems, productivity tools, in-context generative AI)
- Pre-positioning for future Annex III expansion via Commission delegated act under art. 7

### 2.2 Content

Voluntary codes may include:

- Voluntary application of arts. 9–15 essential requirements
- Voluntary adoption of art. 50 transparency measures (chatbot, generative content)
- Sustainability targets (art. 95(2)(b)): ensuring AI systems are designed considering **environmental sustainability** of AI throughout lifecycle (energy-efficient programming, infrastructure, etc.)
- Inclusion of vulnerable groups in design choices
- Diversity of development teams

### 2.3 Legal weight

Voluntary by nature — adherence is a **due-diligence signal**, not a presumption-of-conformity instrument under art. 40. However:

- For procurement, certifications against an industry voluntary code can be a tender-winning differentiator
- For market-surveillance authorities, voluntary-code adherence can be considered when assessing whether a deployer/provider acted in good faith
- For art. 9 RMS or art. 14 oversight design, voluntary-code measures contribute substantively to the evidence base

### 2.4 ISO anchors

| Aspect | ISO/IEC 42001 |
|---|---|
| Code adoption (policy hook) | **cl. 5.2 (AI policy)** + **A.2.2** |
| Implementation | All clauses 6–10 (operationalised at proportional scope) |
| Communication | cl. 7.4 + A.8.5 |

ISO/IEC 42001 cl. 5.2 anticipates voluntary codes as inputs to the AI policy.

## 3. Right to explanation — art. 86

### 3.1 The text

Art. 86(1):

> *"Any affected person subject to a decision which is taken by the deployer on the basis of the output from a high-risk AI system listed in Annex III, with the exception of systems listed under point 2 thereof [biometric ID], and which produces legal effects or similarly significantly affects that person in a way that they consider to have an adverse impact on their health, safety or fundamental rights shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken."*

Art. 86(2) excludes systems used in legal proceedings or where Union or Member State law allowing exceptions for criminal investigation purposes applies.

Art. 86(3): the right does not apply where exceptions or restrictions arise from Union or Member State law in compliance with Union law.

### 3.2 Operative elements

| Element | Detail |
|---|---|
| **Right-holder** | Affected natural person (the subject of the decision, not a third party) |
| **Obligor** | The **deployer** (not the provider) — the right is invoked against whoever made the decision using the AI |
| **Trigger system** | High-risk AI per Annex III (excluding §2 biometric ID per art. 86(1) carve-out) — so applies to credit scoring, employment, education, essential services, justice, etc. |
| **Decision threshold** | Decision producing **legal effects** or similarly significantly affects the person, AND adverse impact on health/safety/fundamental rights |
| **Content of explanation** | (a) **role** of the AI system in the decision-making procedure, (b) **main elements** of the decision taken |
| **Exclusions** | Art. 86(2) systems used in legal proceedings; art. 86(3) other Union/MS law restrictions |

### 3.3 Relationship to GDPR art. 22

Art. 86 is **complementary** to GDPR art. 22 (automated individual decision-making):

| Aspect | GDPR art. 22 | AI Act art. 86 |
|---|---|---|
| Trigger | Decision based **solely** on automated processing producing legal/similarly significant effects | Decision **on the basis of output** from a high-risk AI system (not solely automated; AI may be one input among several) |
| Right | (a) right to opt out + (b) suitable measures for human intervention + (c) right to express view + (d) right to contest | Clear and meaningful explanation of the role of AI + main elements of decision |
| Addressee | Data controller | Deployer |

For the deployer of a high-risk AI system processing personal data and producing decisions with legal effects: **both** rights apply. Operationalize them jointly.

### 3.4 Operationalising art. 86

A defensible implementation:

1. **Decision-record schema**: every decision produced or substantially supported by a high-risk AI system carries a structured record including: model identifier + version, input features used, output (raw + post-processed), confidence/probability, human-overseer decision (override / accept), final decision, timestamp, deployer responsible operator, governing Annex III §X.
2. **Explanation generator**: when an affected person invokes the right, the deployer produces an **explanation document** including:
   - The role of the AI (e.g., "decision-support input to underwriter X" vs. "automated decision with no human review")
   - The main elements of the decision (top contributing features, comparison with similar applicants, governing rules)
   - Channels for contestation, appeal, complaint
   - Reference to provider's IFU summary on capabilities/limitations
3. **Workflow** (deployer-side):
   - Intake of right-to-explanation request
   - Verification of the requester's status as affected person
   - Generation of explanation per template
   - Delivery within reasonable time (no specific deadline in art. 86; benchmark to similar GDPR cadence: 1 month)
4. **Logs**: retain decision records ≥ 6 months (art. 26(5)) — coordinate with GDPR retention schedule.

### 3.5 Common pitfalls

1. **Treating art. 86 as identical to GDPR art. 22** — see § 3.3 above; thresholds and content differ.
2. **Outsourcing the explanation to the provider** — art. 86 binds the **deployer**. The provider must supply technical explainability tools (art. 13(3)(b)(d)), but the obligor on the right is the deployer.
3. **SHAP/LIME plot ≠ "clear and meaningful"** — for non-technical affected persons, raw feature attributions are not meaningful. Generate human-readable narratives.
4. **Explaining only positive cases** — the right is invoked when decisions are **adverse**. Tooling and process must specifically support adverse-decision explanation flows.
5. **Forgetting the carve-outs** — biometric ID (Annex III §2), legal proceedings (art. 86(2)), and Union/MS law restrictions (art. 86(3)) limit applicability.

### 3.6 ISO anchors

| Aspect | ISO/IEC 42001 | Companion |
|---|---|---|
| Right-holder communication | cl. 7.4; **A.8.5 (information for parties)** | TR 24028 (trustworthiness) |
| Decision records | cl. 7.5; **A.6.2.8 (event logs)**, A.4.2 | ISO/IEC 27002 cl. 8.15 |
| Explainability tooling design (provider side) | A.6.2.4 (V&V), A.6.2.7 (documentation) | TR 24028 |
| Human oversight tying explanation to accountability | cl. 5.3, 7.2; A.9.2, A.9.4 | — |

## 4. Decision aid — which instrument applies

```
GPAI provider, art. 53–55 obligations active?
  → Adopt the GPAI Code of Practice (art. 56). Map to ISO 42001 cl. 5.2 + Annex A.2.2 + A.10.3.

Non-high-risk provider/deployer wanting to demonstrate due diligence?
  → Voluntary code of conduct (art. 95). Apply art. 9–15 / art. 50 measures voluntarily.

High-risk Annex III deployer (excl. §2 biometric ID)?
  → Implement art. 86 right-to-explanation workflow + decision records.
  → Coordinate with GDPR art. 22 right where decisions are solely automated.
```

## 5. Output template

```
INSTRUMENT(S) APPLICABLE
  - GPAI Code of Practice (art. 56): <yes/no — which version>
  - Voluntary code of conduct (art. 95): <yes/no — which industry code>
  - Right to explanation (art. 86): <yes/no — which Annex III §X systems>

ADHERENCE STATUS
  Code adoption date: <date>
  Adhered version: <version + URL>
  AIMS policy reference: <cl. 5.2 / Annex A.2.2 — link to internal policy>
  Mapping to ISO 42001 controls: <see crosswalk file>

EVIDENCE BACKBONE (CODE)
  - AI policy referencing the code (cl. 5.2)
  - SoA addressing code measures
  - Internal audit report mapping code measures to controls (cl. 9.2)
  - Management review minutes referencing code adherence (cl. 9.3)

OPERATIONAL DELIVERABLES (RIGHT TO EXPLANATION)
  [ ] Decision-record schema deployed
  [ ] Explanation-generator workflow defined
  [ ] Right-of-explanation intake channel published to affected persons
  [ ] Decision logs retained ≥ 6 months (art. 26(5))
  [ ] Coordination with GDPR art. 22 documented

CITATIONS
  - AI Act art. 56, 95, 86
  - AI Act art. 53–55 (GPAI obligations)
  - GDPR art. 22 (cross-reference)
  - ISO/IEC 42001:2023 cl. 5.2, 7.4, 7.5; Annex A.2.2, A.6.2.7, A.6.2.8, A.8.5, A.9.2, A.9.4, A.10.3
  - ISO/IEC TR 24028 (overview of trustworthiness)

LEGAL DISCLAIMER
  Decision-support output. Not legal advice. Code-of-practice adherence
  and right-to-explanation compliance involve fact-intensive judgements
  on substantive content; obtain qualified counsel before relying on
  this output for binding decisions.
```

## 6. Cross-references

- `02-high-risk-obligations.md` — art. 13 (transparency to deployer; the technical input for art. 86 explanations).
- `05-crosswalk-aiact-iso.md` — rows for art. 56, art. 95, art. 86 (clause/control mapping).
- `08-transparency-art50.md` — art. 50 transparency to natural persons (overlaps with art. 86 disclosure for affected persons).
- `10-gpai-and-timeline.md` — full art. 53–55 GPAI obligations that art. 56 codes operationalize.
- `11-art4-ai-literacy.md` — affected-person-facing staff need M7 module (rights & complaint handling).

# 02 — High-Risk Obligations (AI Act art. 8–29, 40–49)

Once a system is classified high-risk, the full conformity regime applies. This reference is the operational manual: every essential requirement, who carries it, what artefact satisfies it, and which ISO 42001 / 27090 control operationalizes it.

**Effective date** for stand-alone Annex III high-risk systems: **2027-12-02**; for Annex I product-safety high-risk: **2028-08-02** (both deferred by the 2026 AI Omnibus from 2026-08-02 / 2027-08-02 as fixed dates — verify OJ publication of the Omnibus, expected July 2026, before relying on the deferral).

## 1. Provider essential requirements (Title III, Chapter III, Section 2 — art. 8–15)

These are the substantive requirements every high-risk AI system must meet **before** placing on market. Conformity to **harmonised standards** cited in the OJEU (under art. 40) creates a **presumption of conformity**.

### 1.1 Art. 8 — Compliance with the requirements

Umbrella article. The provider shall ensure the high-risk system complies with arts. 9–15 *throughout* its lifecycle. State of the art and intended purpose drive the level of effort. Compliance must take into account the generally acknowledged state of the art.

**ISO anchors**: ISO/IEC 42001 cl. 4 (context), 8 (operation), 9 (performance evaluation), 10 (improvement) — the lifecycle backbone.

### 1.2 Art. 9 — Risk Management System (RMS)

A continuous, iterative process throughout the entire lifecycle. Six explicit steps (art. 9(2)):

1. **Identify and analyse** known and reasonably foreseeable risks the high-risk system may pose to health, safety or fundamental rights when used in accordance with intended purpose.
2. **Estimate and evaluate** risks that may emerge from intended use AND **reasonably foreseeable misuse**.
3. **Evaluate other possibly arising risks** based on data analysis from post-market monitoring (art. 72).
4. **Adopt appropriate and targeted risk management measures** designed to address risks identified per (1)–(3).
5. **Test** the system to identify the most appropriate measures and ensure consistent performance for intended purpose.
6. **Document** all of the above as part of the technical documentation (Annex IV §2(g)).

Special focus on **persons under 18 and other vulnerable groups** (art. 9(9)).

**ISO anchors**:
- ISO/IEC 42001 cl. 6.1.2 (AI risk assessment), 6.1.3 (AI risk treatment), 8.2 (operational AI risk assessment), 8.3 (operational treatment)
- ISO/IEC 42001 Annex A.2.2 (AI policy), A.6.1.2 (objectives for responsible development)
- **ISO/IEC 23894:2023** (AI risk management guidance) — the depth standard

**Deliverables**: risk register, risk treatment plan, residual risk acceptance, test plans, AI Act art. 9 compliance log integrated with post-market monitoring (art. 72).

### 1.3 Art. 10 — Data and data governance

For training, validation and testing data sets used to train models (art. 10(2)):

(a) **Relevant design choices** documented (sampling strategy, labelling protocol, augmentation)
(b) **Data collection processes** and origin documented; for personal data, original purpose
(c) **Relevant data preparation processing operations**: annotation, labelling, cleaning, updating, enrichment, aggregation
(d) **Formulation of relevant assumptions**, in particular about information that the data are supposed to measure and represent
(e) **Assessment of availability, quantity and suitability** of the data sets
(f) **Examination in view of possible biases** likely to affect health and safety, fundamental rights, or lead to discrimination prohibited by Union law
(g) **Appropriate measures to detect, prevent and mitigate** identified biases
(h) **Identification of relevant data gaps or shortcomings** and how they can be addressed

Data must be **relevant, sufficiently representative, free of errors as far as possible, and complete** in view of intended purpose (art. 10(3)). Data sets must take into account characteristics or elements particular to the **specific geographical, contextual, behavioural or functional setting** of intended use (art. 10(4)).

**Special category data exception** (art. 10(5)): processing of GDPR special-category data is permitted *strictly necessary* for bias detection and correction, subject to safeguards (pseudonymisation, technical limits, deletion, security).

**ISO anchors**:
- ISO/IEC 42001 Annex A.4.3 (data resources), A.7.2 (data for development), A.7.3 (acquisition), A.7.4 (quality), A.7.5 (provenance), A.7.6 (preparation)
- **ISO/IEC 5259 series** (data quality for analytics and ML — multi-part):
  - 5259-1 Overview, terminology
  - 5259-2 Data quality measures
  - 5259-3 Management requirements
  - 5259-4 Process framework
  - 5259-5 Governance framework
- ISO/IEC 8183 (data life cycle framework)
- ISO/IEC TR 24027 (bias in AI systems and AI-aided decision making)

**Deliverables**: data card / datasheet (per Datasheets for Datasets convention), provenance log, bias evaluation report, data quality measures report.

### 1.4 Art. 11 — Technical documentation (Annex IV)

The technical file is the central evidentiary artifact. Drawn up before the system is placed on the market or put into service, kept up-to-date.

**Annex IV** contents (extensively detailed in `06-techdoc-annex-iv.md`):

1. General description
2. Detailed description of elements and process for development
3. Detailed information about the monitoring, functioning and control
4. Description of the appropriateness of the performance metrics
5. Detailed description of the risk management system per art. 9
6. Description of relevant changes made through lifecycle
7. List of harmonised standards applied (in full or in part)
8. Copy of the EU declaration of conformity (art. 47)
9. Detailed description of the system in place to evaluate the AI system performance in the post-market phase

**SME simplified form**: SMEs and micro-enterprises may provide a simplified technical documentation in a form to be specified by Commission implementing acts (art. 11(1)(2)).

**ISO anchors**: ISO/IEC 42001 Annex A.4.2 (resource documentation), A.6.2.3 (design and development documentation), A.6.2.7 (technical documentation); ISO/IEC 5338 (lifecycle processes).

### 1.5 Art. 12 — Record-keeping (automatic logs)

The high-risk system must technically allow **automatic recording of events ('logs')** over its lifetime. Logs shall ensure traceability of the system's functioning appropriate to intended purpose.

For art. 6(2) Annex III §1 high-risk systems (remote biometric identification), logging shall record at minimum:
- Period of each use (start/end date and time)
- Reference database against which input data has been checked
- Input data for which the search led to a match
- Identification of natural persons involved in verification of results, per art. 14(5)

**Retention**: at least **6 months**, unless otherwise provided by applicable Union or national law (art. 19).

**ISO anchors**: ISO/IEC 42001 Annex A.6.2.8 (event logs); ISO/IEC 27002:2022 cl. 8.15 (logging) — the security baseline.

### 1.6 Art. 13 — Transparency and provision of information to deployers

High-risk systems shall be designed and developed such that their operation is **sufficiently transparent** to enable deployers to interpret the system's output and use it appropriately.

**Instructions for use** must accompany the system (art. 13(2)) and contain at minimum (art. 13(3)):

(a) Identity and contact details of provider, authorised rep
(b) Characteristics, capabilities and limitations of performance, including:
   - Intended purpose
   - Level of accuracy (including its metrics), robustness and cybersecurity referred to in art. 15 against which the system has been tested and validated
   - Any known or foreseeable circumstance which may lead to risks to health, safety or fundamental rights
   - Where applicable, technical capabilities and characteristics relevant for explaining output
   - Specific groups of persons on which it is intended to be used
   - Specifications for input data, or any other relevant information in terms of training/validation/testing data sets
   - Where applicable, information to enable deployers to interpret output and use it appropriately
(c) Changes to the system and its performance pre-determined by the provider at moment of initial conformity assessment
(d) Human oversight measures referred to in art. 14, including technical measures to facilitate interpretation of output
(e) Computational and hardware resources needed, expected lifetime, maintenance/care measures (including software updates) needed to ensure proper functioning
(f) Where relevant, description of mechanisms to enable deployers to properly collect, store and interpret logs

**ISO anchors**: ISO/IEC 42001 Annex A.8.2 (system documentation and information for users), A.8.5 (information for interested parties), A.6.2.7 (technical documentation).

### 1.7 Art. 14 — Human oversight

High-risk systems shall be designed and developed such that they can be **effectively overseen by natural persons** during the period in which they are in use.

Oversight measures shall be commensurate with the risks, level of autonomy and context of use. Provider shall identify and build oversight measures into the system before placing on market (art. 14(3)(a)) AND identify oversight measures appropriate to be implemented by the deployer (art. 14(3)(b)).

Oversight aims (art. 14(2)): prevent or minimise risks to health, safety or fundamental rights when the system is used in accordance with intended purpose or under conditions of reasonably foreseeable misuse.

The oversight enables the natural person assigned to the task to (art. 14(4)):

(a) **Properly understand** the relevant capacities and limitations and **monitor** operation, including detecting anomalies, dysfunctions, unexpected performance
(b) Remain aware of the possible tendency to **automatically rely or over-rely** on output (automation bias), in particular for systems used to provide information or recommendations
(c) **Correctly interpret** output, taking into account interpretation tools and methods available
(d) **Decide, in any particular situation, not to use** the system or otherwise disregard, override or reverse output
(e) **Intervene in operation or interrupt** the system through a 'stop' button or similar procedure that allows the system to come to a halt in a safe state

**Special requirement for biometric ID** (art. 14(5)): for art. 6(2) Annex III §1(a) systems, the deployer ensures that no action or decision is taken on the basis of identification resulting from the system unless that identification has been **separately verified and confirmed by at least two natural persons** with the necessary competence, training and authority — except for law enforcement, migration, border control or asylum, where Union/national law considers this requirement disproportionate.

**ISO anchors**:
- ISO/IEC 42001 cl. 5.3 (roles), 7.2 (competence), 7.3 (awareness)
- ISO/IEC 42001 Annex A.9.2 (responsible use processes), A.9.3 (objectives), A.9.4 (intended use), A.6.2.5 (deployment), A.6.2.6 (operation and monitoring)

**Deliverables**: oversight design specification, operator training records, override/intervention procedure documentation, automation-bias awareness training materials.

### 1.8 Art. 15 — Accuracy, robustness and cybersecurity

Three pillars. Each separately measurable, separately documented in art. 13(3) instructions for use, and separately evaluated in conformity assessment.

#### Accuracy (art. 15(1), 15(3))

Levels of accuracy and **relevant accuracy metrics** declared in instructions for use. Commission encouraged to develop benchmarks and measurement methodologies through stakeholders.

**ISO anchors**: ISO/IEC TS 4213:2022 (assessment of classification model performance); ISO/IEC 25059 (quality model for AI systems); upcoming ISO/IEC 24029-3 (robustness assessment of neural networks part 3).

#### Robustness (art. 15(4))

System shall be **as resilient as possible** regarding errors, faults or inconsistencies that may occur in the system or in the environment in which it operates, in particular due to interaction with natural persons or other systems.

**Technical and organisational measures** to ensure robustness. May include redundancy solutions (backup or fail-safe plans).

For systems that **continue to learn after deployment**: developed in such a way to **eliminate or reduce as far as possible** the risk of possibly biased outputs influencing input for future operations (**feedback loops**), and to ensure such loops are duly addressed with appropriate mitigation measures.

**ISO anchors**:
- ISO/IEC 24029-2:2023 (robustness of neural networks — methodology) and 24029-1
- ISO/IEC TR 24028:2020 (overview of trustworthiness in AI)
- ISO/IEC 27090:2025 sections on robustness and adversarial defenses

#### Cybersecurity (art. 15(5))

System shall be **resilient against attempts by unauthorised third parties** to alter use, output or performance by exploiting vulnerabilities. Technical solutions to ensure cybersecurity shall be **appropriate to relevant circumstances and risks**.

**Recital 76** (the legal basis for AI-specific security): technical solutions aiming to ensure the cybersecurity of high-risk AI systems should be **appropriate to the relevant circumstances and risks**, addressing AI-specific vulnerabilities including measures to:
- Prevent **data poisoning** (attacks targeting training data)
- Prevent **model poisoning** (pre-trained components attacked)
- Prevent **model evasion** (adversarial examples causing the model to make a mistake)
- Prevent **confidentiality attacks** (model extraction, membership inference, model inversion)
- Address **model flaws**

**ISO anchor — primary**: **ISO/IEC 27090:2025**. See `04-iso-27090-ai-security.md` for the full threat taxonomy and mitigation catalogue.

**ISO anchors — supporting**:
- ISO/IEC 27001:2022 + 27002:2022 (org-level ISMS baseline — assumed, not duplicated)
- ISO/IEC 27005 (information security risk management)
- NIST AI 100-2:2025 (Adversarial Machine Learning taxonomy — terminology aligned with ISO 27090)
- MITRE ATLAS (adversarial tactics for AI — operational TTP catalogue)
- OWASP LLM Top 10 (2025 edition — practitioner-level for LLM systems)

**Deliverables**: accuracy evaluation report (with metrics), robustness assessment per ISO 24029-2 (including adversarial robustness), AI-specific threat model per ISO 27090, security control implementation evidence, red-team findings (mandatory for systemic-risk GPAI per art. 55).

## 2. Provider operational obligations (art. 16–22)

Beyond the essential requirements, providers carry operational duties:

| Article | Obligation |
|---------|-----------|
| **Art. 16** | Compliance with art. 8 + indication of name/trademark/contact + put in place QMS per art. 17 + draw up technical documentation per art. 11 + automatic generation of logs per art. 12 + conformity assessment per art. 43 + EU declaration of conformity per art. 47 + CE marking per art. 48 + register in EU database per art. 49 + take corrective actions and provide info per art. 20 + cooperate with competent authorities per art. 21 |
| **Art. 17** | **Quality Management System** (QMS) — see `08-qms-art17.md` and `03-iso-42001-aims.md` |
| **Art. 18** | Documentation kept at the disposal of national authorities for **10 years** |
| **Art. 19** | Logs automatically generated kept by provider for at least **6 months** (or longer where applicable) |
| **Art. 20** | **Corrective actions and duty of information**: if non-conformity, take immediate action to bring system into conformity, withdraw, disable or recall; inform distributors/deployers/authorised reps/importers |
| **Art. 21** | **Cooperation with competent authorities**: provide all info and documentation necessary on reasoned request |
| **Art. 22** | **Authorised representatives** for providers established in third countries |

## 3. Importer obligations (art. 23) and Distributor obligations (art. 24)

| Importer (art. 23) | Distributor (art. 24) |
|--------------------|----------------------|
| Verify provider has carried out conformity assessment | Verify CE marking + EU declaration + instructions for use |
| Verify technical documentation drawn up | Take corrective actions if non-conforming + cooperate with authorities |
| Verify CE marking + EU declaration | Indicate name/trademark/contact on system or packaging |
| Indicate name/trademark/contact on system or packaging | |
| Storage and transport conditions do not jeopardise compliance | Storage conditions do not jeopardise compliance |
| Cooperate with authorities | |
| Provide info to provider/authorities about risks | |

## 4. Deployer obligations (art. 26–29)

### 4.1 Art. 26 — Deployers of high-risk AI systems

(1) Take appropriate **technical and organisational measures** to ensure use in accordance with instructions for use accompanying the system.
(2) Assign **human oversight** to natural persons who have the necessary competence, training and authority, and the necessary support.
(3) **Input data** under deployer control: ensure relevant and sufficiently representative in view of intended purpose.
(4) **Monitor operation** based on instructions for use, and where relevant inform providers in accordance with art. 72; if deployer has reason to consider that use may result in risk to health/safety/fundamental rights, inform provider/distributor and competent authority **without undue delay** and **suspend use**. If serious incident: report per art. 73.
(5) **Keep logs** automatically generated by the system, where logs under their control, for a period appropriate to intended purpose, at least **6 months**.
(6) **Workplace use**: deployers being employers shall **inform workers' representatives and affected workers** before putting in service or using a high-risk system at the workplace.
(7) **Public authorities, agencies, bodies, institutions** using high-risk AI: **register their use** in the EU database (art. 49). If the system is not registered, the deployer shall not use it and inform the provider/distributor.
(8) **Privacy / data protection**: deployers shall use information provided by provider per art. 13 to comply with their **DPIA obligation under art. 35 GDPR** or art. 27 LED.
(9) **Decision-making affecting natural persons in law enforcement, migration, asylum, border, justice, democratic processes** (Annex III §6, §7, §8): the deployer shall, **before** putting into service, request **judicial or administrative authorisation** where required by national law (excluding emergency cases where retroactive auth is permitted).
(10) **Right to explanation** (cross-reference): for decisions affecting natural persons, art. 86 grants affected persons the right to clear and meaningful explanations.
(11) Deployers shall cooperate with competent authorities.
(12) For **emotion recognition** or **biometric categorisation** systems (when permitted): **inform** natural persons exposed of their operation and process personal data per GDPR/LED.

### 4.2 Art. 27 — Fundamental Rights Impact Assessment (FRIA)

**Bound to deployers** (not providers) of certain high-risk AI:

- **Bodies governed by public law** OR private deployers providing public services AND deploying any Annex III high-risk system, **OR**
- Deployers of Annex III §5(b) (creditworthiness/credit score, except detecting fraud) and §5(c) (life and health insurance risk assessment / pricing).

**Before first use**, deployer shall perform an assessment covering:

(a) Description of the deployer's processes in which the system will be used in line with intended purpose
(b) Description of the period and frequency of use
(c) Categories of natural persons and groups likely to be affected by use in the specific context
(d) Specific risks of harm likely to impact categories under (c), taking into account the information given by provider per art. 13
(e) Description of human oversight measures
(f) Measures to be taken in case of materialisation of risks (governance, complaint mechanism)

**Notify** the market surveillance authority of the FRIA's results (art. 27(3)). When obligations under DPIA art. 35 GDPR and FRIA art. 27 overlap, the FRIA shall be conducted in conjunction with the DPIA (art. 27(4)).

Full template in `07-fria-art27.md`.

### 4.3 Arts. 28–29 — Notifying authorities, notified bodies (procedural)

These articles concern the institutional framework for conformity assessment. See `09-post-market-art72-73.md` for the procedural connection to surveillance.

## 5. Conformity assessment (art. 43) and CE marking (art. 48)

### 5.1 Art. 43 — Conformity assessment procedures

Two paths exist for high-risk AI under Annex III:

**Path 1 — Internal control (Annex VI)**: provider self-assesses against arts. 9–15. Available for **all Annex III** high-risk systems EXCEPT certain biometric categories.

**Path 2 — Conformity assessment based on assessment of QMS and technical documentation (Annex VII)**: notified body involvement. Required for art. 6(2) Annex III §1(a) (remote biometric identification), and where harmonised standards (art. 40) or common specifications (art. 41) are not applied or only partially.

For high-risk systems under **Annex I (product safety)** [art. 6(1) pathway A], conformity assessment follows the **applicable sectoral legislation**, with AI Act requirements integrated (art. 43(3)).

**Substantial modification** (art. 43(4)): if a high-risk system has already been subject to conformity assessment, a fresh conformity assessment is required when **substantial modification** occurs (irrespective of whether modified version is intended for distribution or remains in deployer's use), or when **intended purpose changes**.

### 5.2 Art. 47 — EU declaration of conformity

Drawn up by provider for each high-risk AI system, contents per Annex V:

1. AI system name and additional information allowing identification and traceability
2. Provider name + address (and authorised rep if applicable)
3. Statement: "the system is in conformity with this Regulation and where applicable with any other relevant Union legislation"
4. Where AI system involves processing of personal data: statement that system complies with GDPR + LED (Directive (EU) 2016/680) + LED-equivalent Member State law
5. References to harmonised standards applied or common specifications used to declare conformity
6. Where applicable: notified body name + address + identification number, conformity assessment procedure followed, identification of certificate issued
7. Place and date of issue, name + function of signatory + signature

Translated into language(s) that can be easily understood by competent authorities of the Member States in which the system is placed on market or made available.

Provider keeps the declaration available for 10 years (art. 18).

### 5.3 Art. 48 — CE marking

CE marking affixed visibly, legibly and indelibly. If not possible due to the nature of the system, affix on packaging or accompanying documentation. For **digitally-provided AI systems**: digital CE marking shall be used (art. 48(2)).

CE marking subject to general principles set out in art. 30 of Regulation (EC) No 765/2008.

If a notified body was involved in conformity assessment, its identification number shall follow CE marking (art. 48(4)).

### 5.4 Art. 49 — Registration in the EU database

Before placing on market or putting into service a high-risk AI system in art. 6(2) (Annex III), provider OR authorised rep shall register **themselves and that system** in the EU database referred to in art. 71.

For art. 6(3) **derogation** claims: register in the EU database (art. 49(2)).

**Public authorities** acting as deployers of Annex III high-risk register their use (art. 26(7) cross-reference + art. 49(3)).

The EU database is **publicly accessible** for many fields — providers should expect that name, intended purpose, instructions for use summary, and conformity assessment outcomes are visible.

## 6. Five-pillar deliverables map (codified from `complianceService.ts`)

The Navigator project's `complianceService.ts` reduces high-risk obligations to five operational pillars. This map is useful for project planning:

| Pillar | Underlying art. | Artefacts |
|--------|----------------|-----------|
| **1. Documentation** | art. 11 + Annex IV; art. 13 instructions for use; art. 47 declaration | Annex IV technical file; instructions for use; declaration of conformity |
| **2. Testing** | art. 9(2)(e); art. 15 accuracy/robustness/cyber; art. 43 conformity assessment | Test plans; accuracy/robustness reports; adversarial / red-team reports; conformity assessment certificate (if notified body) |
| **3. Surveillance** | art. 12 logs; art. 17(3)(g) post-market monitoring procedure; art. 72 post-market monitoring; art. 73 incident reporting | Log retention policy; post-market monitoring plan; incident-reporting playbook |
| **4. Transparency** | art. 13 to deployer; art. 14 oversight measures; art. 50 transparency to natural persons | Instructions for use; oversight measures spec; user-facing AI disclosure UX; deepfake/generated-content marking (C2PA + watermark) |
| **5. Certification** | art. 17 QMS; art. 43 conformity assessment; art. 47 declaration; art. 48 CE marking; art. 49 registration | ISO 42001 certification (evidence); conformity assessment certificate; declaration of conformity; CE marking; EU database entry |

Risk-tier coupling (codified):
- High-risk → all 5 pillars
- Limited risk → pillars 1 (lite) + 4 only
- Minimal risk → pillar 1 (voluntary)

## 7. Provider checklist (compact, for project planning)

```
[ ] Establish AIMS per ISO 42001 (art. 17)
[ ] Implement RMS per art. 9 + ISO 23894 (deliverables: register, treatment plan)
[ ] Data governance per art. 10 + ISO 5259 (deliverables: datasheet, bias report)
[ ] Draw up technical documentation per art. 11 + Annex IV
[ ] Engineer logs per art. 12 (≥6mo retention) + ISO 42001 A.6.2.8
[ ] Provide instructions for use per art. 13 (deliverable: full IFU)
[ ] Engineer human-oversight measures per art. 14
[ ] Achieve accuracy/robustness/cyber per art. 15 + ISO 27090 + ISO 24029-2
[ ] Choose conformity-assessment path per art. 43 (internal vs notified body)
[ ] Engage notified body if Annex VII path required
[ ] Issue declaration of conformity per art. 47 + Annex V
[ ] Affix CE marking per art. 48
[ ] Register in EU database per art. 49
[ ] Establish post-market monitoring per art. 72
[ ] Establish incident reporting playbook per art. 73
[ ] Retain technical documentation 10 years (art. 18)
[ ] Retain logs ≥6 months (art. 19)
```

## 8. Deployer checklist (compact)

```
[ ] Use system per provider's instructions (art. 26(1))
[ ] Assign trained, competent humans for oversight (art. 26(2) + art. 14)
[ ] Verify input data relevance and representativeness (art. 26(3))
[ ] Monitor operation; suspend if risk emerges (art. 26(4))
[ ] Retain logs ≥6 months (art. 26(5))
[ ] Inform workers' representatives if workplace use (art. 26(6))
[ ] Register use in EU database if public authority (art. 26(7))
[ ] Coordinate FRIA with DPIA per art. 35 GDPR (art. 26(8))
[ ] Conduct FRIA before first use (art. 27 — see 07-fria-art27.md) if applicable
[ ] Inform natural persons exposed to emotion-recognition / biometric-categorisation (art. 26(12))
[ ] Cooperate with market surveillance (art. 26(11))
[ ] Implement transparency obligations per art. 50 if applicable
[ ] Report serious incidents per art. 73
```

When you produce outputs against this reference, **always cite the article and ISO control jointly**. The mapping table in `05-crosswalk-aiact-iso.md` is the authoritative cross-reference.

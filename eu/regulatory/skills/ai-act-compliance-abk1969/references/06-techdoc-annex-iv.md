# 06 — Annex IV Technical Documentation (AI Act art. 11)

The technical documentation file is the **central evidentiary artefact** demonstrating conformity with arts. 9–15. It is drawn up **before** the system is placed on market or put into service and **kept up-to-date** throughout the lifecycle. Retention: **10 years** after placing on market (art. 18).

## 1. Annex IV structure (9 sections)

The technical documentation referred to in art. 11(1) shall contain at least:

### Annex IV §1 — General description

(a) Intended purpose, name of provider, version
(b) How the AI system interacts with, or can be used to interact with, hardware or software, including with other AI systems, that are not the AI system itself
(c) Versions of relevant software or firmware and any requirements related to version updates
(d) Description of all forms in which the AI system is placed on the market or put into service (e.g., software packages embedded into hardware, downloads, API)
(e) Description of hardware on which the AI system is intended to run
(f) Where the AI system is a component of products: photographs or illustrations
(g) Basic description of the user-interface provided to the deployer
(h) Instructions for use for the deployer + basic description of user-interface provided to deployer (where applicable)

### Annex IV §2 — Detailed description of elements and process for development

(a) Methods and steps performed for the development, including, where relevant, recourse to pre-trained systems or tools provided by third parties + how these have been used, integrated, or modified by the provider
(b) Design specifications, namely the **general logic of the AI system and of the algorithms**; key design choices including rationale; main classification choices; what the system is designed to optimise; possible trade-offs made
(c) Description of the **system architecture** explaining how software components build on or feed into each other and integrate into the overall processing; computational resources used to develop, train, test, validate
(d) Where relevant, **data requirements** in terms of datasheets describing training methodologies and techniques; training data sets used: general description, provenance, scope and main characteristics; how the data was obtained and selected; labelling procedures; data cleaning methodologies (e.g., outlier detection)
(e) Assessment of the human oversight measures needed in accordance with art. 14, including assessment of the technical measures needed to facilitate the interpretation of the outputs by deployers
(f) Where applicable, detailed description of pre-determined changes to the AI system and its performance, together with all relevant information related to the technical solutions adopted to ensure continuous compliance
(g) **Validation and testing procedures** used, including information about validation and testing data + main characteristics; metrics used to measure accuracy, robustness, **compliance with other relevant requirements** in Chapter III Section 2 + potentially discriminatory impacts; test logs and reports dated and signed by responsible persons (incl. with regard to pre-determined changes per (f))
(h) Cybersecurity measures put in place

### Annex IV §3 — Detailed information about the monitoring, functioning and control

Description of capabilities and limitations in performance, including degree of accuracy for specific persons or groups; overall expected level of accuracy in relation to its intended purpose; foreseeable unintended outcomes and sources of risks to health/safety, fundamental rights, discrimination in view of intended purpose; human oversight measures referred to in art. 14, including the technical measures put in place to facilitate the interpretation of outputs by deployers; specifications on input data, as appropriate.

### Annex IV §4 — Description of the appropriateness of the performance metrics

Description of the appropriateness of the performance metrics for the specific AI system.

### Annex IV §5 — Detailed description of the risk management system in accordance with art. 9

The full risk management system documentation: identification, estimation, evaluation, treatment, testing, post-market integration. See `references/02-high-risk-obligations.md` § Art. 9.

### Annex IV §6 — Description of relevant changes made through the lifecycle

Version history with substantive changes; for each: rationale, change-impact assessment, retraining specifics if applicable, regression-test results, conformity-impact statement.

### Annex IV §7 — List of harmonised standards applied (in full or in part) — and where not applied: description of solutions adopted to meet essential requirements

For each art. 9–15 essential requirement, list:
- The harmonised standard cited in OJEU (when available; track JTC 21)
- Or, in the absence: the specific solution adopted with rationale

Until EN ISO/IEC 42001 / 23894 / 24029-2 / 5259 / 27090 / 42005 are cited in the OJEU, providers cite the **non-harmonised ISO standards as evidence of state-of-the-art compliance**, with explicit acknowledgment that this is not the art. 40 presumption.

### Annex IV §8 — Copy of the EU declaration of conformity (art. 47)

The signed declaration per Annex V. See `02-high-risk-obligations.md` § 5.2.

### Annex IV §9 — Detailed description of the system in place to evaluate the AI system performance in the post-market phase (per art. 72)

Post-market monitoring plan structure, KPIs, signal sources, escalation thresholds, governance. See `09-post-market-art72-73.md`.

## 2. SME simplified form

For SMEs and micro-enterprises (art. 11(1)(2)), Commission implementing acts will specify a **simplified Annex IV form**. As of 2026 the implementing act is in development. SMEs should still draft a complete file because:

- Simplified does not mean less rigorous on essential requirements
- Notified bodies may require specific evidence regardless of form
- Future scaling out of SME status reverts to full Annex IV

## 3. Practical structure (recommended file layout)

A typical Annex IV technical file is structured as a single document or document-set with the following layout. Sections labelled with the Annex IV § that they satisfy.

```
TECHNICAL DOCUMENTATION FILE
│
├── 0. Cover & control
│   ├── Document ID, version, owner, approval signatures
│   ├── Distribution list
│   └── Change log
│
├── 1. General description (Annex IV §1)
│   ├── 1.1 Intended purpose & provider
│   ├── 1.2 Versions / interaction with other systems
│   ├── 1.3 Forms (software, embedded, API)
│   ├── 1.4 Hardware requirements
│   ├── 1.5 User interface (deployer)
│   └── 1.6 Instructions for use (full IFU as separate doc; reference here)
│
├── 2. Development (Annex IV §2)
│   ├── 2.1 Methods & steps
│   ├── 2.2 Pre-trained components / third-party tools (incl. ML-BOM)
│   ├── 2.3 Design rationale & trade-offs
│   ├── 2.4 System architecture (incl. C4 / mermaid diagrams)
│   ├── 2.5 Compute resources used in development
│   ├── 2.6 Data requirements & datasheet (per ISO 5259-1 example)
│   ├── 2.7 Human-oversight measures designed (cross-ref §3.5)
│   ├── 2.8 Pre-determined changes (if applicable)
│   ├── 2.9 V&V procedures + test plans + signed reports
│   └── 2.10 Cybersecurity (link to threat model per ISO 27090 — see 04 reference)
│
├── 3. Monitoring, functioning, control (Annex IV §3)
│   ├── 3.1 Capabilities & limitations
│   ├── 3.2 Accuracy by group/persona
│   ├── 3.3 Foreseeable unintended outcomes
│   ├── 3.4 Risk sources to fundamental rights / discrimination
│   ├── 3.5 Human oversight measures (operational)
│   └── 3.6 Input data specifications
│
├── 4. Performance metrics appropriateness (Annex IV §4)
│   ├── 4.1 Metrics declared for accuracy (ISO TS 4213)
│   ├── 4.2 Metrics for robustness (ISO 24029-2)
│   ├── 4.3 Metrics for fairness/bias (per use case)
│   └── 4.4 Justification of metric choice
│
├── 5. Risk management system (Annex IV §5) — per art. 9 + ISO 23894
│   ├── 5.1 Risk register
│   ├── 5.2 Risk analysis methodology
│   ├── 5.3 Risk treatment plan
│   ├── 5.4 Residual risk acceptance
│   ├── 5.5 Reasonably foreseeable misuse analysis
│   ├── 5.6 Vulnerable group focus (esp. <18)
│   └── 5.7 Integration with post-market monitoring (cross-ref §9)
│
├── 6. Lifecycle changes (Annex IV §6)
│   └── Version history with conformity-impact assessment per change
│
├── 7. Harmonised standards & solutions (Annex IV §7)
│   ├── 7.1 Standards applied (cite OJEU references as they appear)
│   ├── 7.2 Solutions adopted where standards not applied
│   └── 7.3 Conformity rationale per art. 8–15 essential requirement
│
├── 8. EU declaration of conformity (Annex IV §8 = Annex V)
│   └── Signed declaration
│
├── 9. Post-market monitoring (Annex IV §9 + art. 72)
│   ├── 9.1 PMM plan
│   ├── 9.2 Signal sources & thresholds
│   ├── 9.3 Drift detection methodology
│   ├── 9.4 Incident-handling integration (art. 73)
│   └── 9.5 Periodic review schedule
│
└── Annexes
    ├── A. Datasheet (per ISO 5259-1)
    ├── B. Model card (Hugging Face / Google convention)
    ├── C. System card (Anthropic/OpenAI convention)
    ├── D. Threat model (per ISO 27090, see 04 reference §7)
    ├── E. Test reports (V&V, robustness, adversarial, fairness)
    ├── F. Operator/oversight training materials
    ├── G. ML-BOM (machine-learning bill of materials)
    └── H. Notified body assessment certificate (if Annex VII path)
```

## 4. Provenance and lifecycle integrity

The Annex IV file must reflect **the system as actually placed on market**. Common pitfalls:

1. **Drift between docs and code** — version of model documented ≠ deployed model. Mitigation: technical documentation is generated/regenerated automatically from CI/CD on every release; version pinned in §6.
2. **Forgotten dependency updates** — base model updated, datasheet still references old version. Mitigation: ML-BOM with automated diff-on-update.
3. **Missing pre-determined changes documentation** (Annex IV §2(f)) — if the system has online learning or scheduled retraining, this MUST be documented in advance with conformity-impact rationale, not retroactively.
4. **Untraceable test reports** — reports unsigned, undated, or stored without retrievability. Mitigation: V&V reports go through SoP signing + audit-trail log in document management system.

## 5. Connections to ISO 42001 controls

| Annex IV section | ISO 42001 controls satisfying it |
|------------------|----------------------------------|
| §1 General description | A.4.2 (resource doc), A.6.2.7 (technical doc), A.8.2 (info for users) |
| §2 Development | A.6.1.3 (responsible design processes), A.6.2.2 (requirements), A.6.2.3 (design + dev doc), A.6.2.4 (V&V), A.7.* (data) |
| §3 Monitoring, functioning, control | A.6.2.5 (deployment), A.6.2.6 (operation + monitoring), A.9 (use) |
| §4 Performance metrics | A.6.2.4 (V&V), A.6.2.6 (monitoring) |
| §5 Risk management | cl. 6.1.2-3, 8.2-3 + A.2.2 + ISO 23894 |
| §6 Lifecycle changes | cl. 6.3 (planning of changes), A.6.2.5 (deployment) |
| §7 Standards applied | cl. 4.1 (context — regulatory) |
| §8 Declaration | A.8.3 (external reporting) |
| §9 Post-market monitoring | cl. 9.1, 10.1 + A.6.2.6, A.8.3 |

## 6. Output template (Annex IV file table-of-contents)

When asked to draft an Annex IV technical file outline, output:

```
TECHNICAL DOCUMENTATION FILE — <SYSTEM NAME>
Provider: <name, address, registration>
Authorised Rep (if 3rd country): <name, address>
Document ID: TF-<YYYY>-<system>-vN.M
Version: <semver>
Status: <draft | for review | approved | superseded>
Effective: <YYYY-MM-DD>

§1. GENERAL DESCRIPTION
    1.1 Intended purpose + system name + version
    1.2 Interaction with hardware/software/other AI systems
    1.3 Software/firmware versions, update requirements
    1.4 Forms placed on market (SaaS API / SDK / on-prem / embedded)
    1.5 Hardware requirements
    1.6 User interface for deployer
    1.7 Instructions for use (full IFU attached)

§2. DETAILED DESCRIPTION OF ELEMENTS AND DEVELOPMENT PROCESS
    2.1 Development methodology (lifecycle per ISO 5338)
    2.2 Pre-trained models / third-party tools (ML-BOM in Annex G)
    2.3 Design rationale, key choices, trade-offs
    2.4 System architecture (C4 + sequence diagrams, Annex H)
    2.5 Compute resources used in development
    2.6 Data requirements
        2.6.1 Datasheet (Annex A)
        2.6.2 Provenance (per ISO 8183)
        2.6.3 Quality measures (per ISO 5259-2)
        2.6.4 Bias examination + mitigation (art. 10(2)(f)(g))
        2.6.5 Special-category data justification (if any, art. 10(5))
    2.7 Human oversight measures (technical + procedural)
    2.8 Pre-determined changes (continuous learning, retraining schedule)
    2.9 Validation & testing
        2.9.1 Test plan
        2.9.2 Validation/test data sets
        2.9.3 Accuracy metrics + targets
        2.9.4 Robustness assessment (per ISO 24029-2)
        2.9.5 Adversarial robustness (per ISO 27090)
        2.9.6 Fairness/bias assessment
        2.9.7 Test reports (Annex E, dated + signed)
    2.10 Cybersecurity
        2.10.1 Threat model (per ISO 27090, Annex D)
        2.10.2 Security controls deployed
        2.10.3 Red-team report (Annex E)
        2.10.4 Incident-response playbook (cross-ref §9)

§3. MONITORING, FUNCTIONING, CONTROL
    3.1 Capabilities and limitations
    3.2 Accuracy by group/persona/condition
    3.3 Foreseeable unintended outcomes
    3.4 Risk sources to health/safety/fundamental rights/discrimination
    3.5 Human oversight measures (operational)
    3.6 Input data specifications

§4. PERFORMANCE METRICS APPROPRIATENESS
    4.1 Metric selection rationale
    4.2 Accuracy metrics + ISO TS 4213 alignment
    4.3 Robustness metrics + ISO 24029-2 alignment
    4.4 Fairness metrics
    4.5 Limitations of metrics

§5. RISK MANAGEMENT SYSTEM (per art. 9 + ISO 23894)
    5.1 Methodology (RMS lifecycle aligned with cl. 6.1.2-3, 8.2-3)
    5.2 Risk register (current)
    5.3 Risk-treatment plan
    5.4 Residual-risk acceptance (signed)
    5.5 Reasonably-foreseeable-misuse analysis
    5.6 Vulnerable-groups focus (children, elderly, etc.)
    5.7 Post-market feedback loop into RMS

§6. LIFECYCLE CHANGES
    Version    Date         Type           Conformity impact   Approver
    -------    ----         ----           -----------------   --------
    v1.0       YYYY-MM-DD   Initial        N/A                 <name>
    v1.1       YYYY-MM-DD   Patch          None                <name>
    v2.0       YYYY-MM-DD   Major retrain  Re-V&V completed    <name>
    ...

§7. HARMONISED STANDARDS APPLIED
    Per art. 8 (compliance):     <std>
    Per art. 9 (RMS):            <std>
    Per art. 10 (data):          <std>
    Per art. 11 (techdoc):       <std>
    Per art. 12 (logs):          <std>
    Per art. 13 (transparency):  <std>
    Per art. 14 (oversight):     <std>
    Per art. 15 (acc/rob/cyb):   <std>
    
    Where standards not applied: solutions adopted + rationale

§8. EU DECLARATION OF CONFORMITY (Annex V)
    [Attached, signed]

§9. POST-MARKET MONITORING (per art. 72)
    9.1 PMM plan
    9.2 Signal sources (logs, complaints, drift, incidents)
    9.3 Detection thresholds
    9.4 Drift detection methodology
    9.5 Integration with art. 73 incident reporting
    9.6 Periodic review (frequency, governance)

ANNEXES
    A. Datasheet (per ISO 5259-1)
    B. Model card
    C. System card
    D. Threat model (per ISO 27090)
    E. Test reports (V&V, robustness, adversarial, fairness)
    F. Operator/oversight training materials
    G. ML-BOM
    H. Notified body certificate (if applicable)
```

This template aligns with Annex IV exactly while embedding the ISO controls that operationalize each section. Use it as the starting outline for any Annex IV file generation task.

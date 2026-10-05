# 04 — ISO/IEC 27090:2025 (AI Cybersecurity) Deep Reference

ISO/IEC 27090:2025 *Cybersecurity — Artificial intelligence — Guidance for addressing security threats to artificial intelligence systems* is the **depth standard** for AI Act art. 15(5) cybersecurity. Where ISO 42001 establishes the AIMS at policy level, where ISO 24029 covers robustness/accuracy, and where ISO 27001 covers org-level information security baseline, ISO 27090 owns the **AI-specific threat model and mitigation catalogue**.

This reference is the substantive content. For mapping to AI Act art. 15 and Recital 76, see `05-crosswalk-aiact-iso.md`.

## 1. Status, scope, and relationship to other standards

**Publication**: ISO/IEC 27090:2025 (released late 2025), International Standard.

**Sponsoring committee**: ISO/IEC JTC 1/SC 27 (information security, cybersecurity, privacy protection), Working Group 4 (security controls and services), with formal liaison to ISO/IEC JTC 1/SC 42 (AI). SC 27 owns the security framing; SC 42 ensures alignment with 42001 + 23894.

**Scope (in)**:
- Security threats specific to AI systems and components — data, models, pipelines, inference endpoints
- **Both classical/discriminative ML** (supervised, unsupervised, reinforcement) **and generative AI / foundation models / LLMs** — with explicit dedicated annex for the latter
- The full AI lifecycle: data preparation → training → evaluation → deployment → operation → monitoring → decommissioning

**Scope (out)**:
- General cybersecurity (handled by reference to 27001/27002)
- AI safety/ethics/bias/fairness (handled by 23894, TR 24028, TR 24368)
- AIMS requirements (handled by 42001)
- Sector-specific (medical, automotive, finance) obligations
- AI as a tool **for** cybersecurity defense — 27090 covers security **of** AI, not security **by** AI

**Nature**: Guidance / informative — not a certifiable conformity standard. 27090 is a control catalogue plugged into a 27001 risk treatment plan or 42001 SoA, not certified independently.

### Relationship to adjacent standards

| Standard | Role | How 27090 relates |
|----------|------|-------------------|
| ISO/IEC 27001 / 27002 | Generic ISMS / control catalogue | 27090 **assumes** 27001 baseline. Adds AI-specific threats and controls without duplicating IAM, crypto, IR basics |
| ISO/IEC 42001 | AIMS | A.6.2 lifecycle controls and A.10.3 supplier controls reference security at policy level. 27090 is the **operational depth** |
| ISO/IEC 23894 | AI risk management | Provides identify → analyze → evaluate → treat process. 27090 supplies the **threat catalogue** feeding identify/analyze |
| **NIST AI 100-2 Adversarial Machine Learning** | US AML taxonomy | **Terminology aligned** with 27090. Both update in tandem; cross-reference each other |
| OWASP ML Top 10 | Practitioner top risks classical ML | Subset of 27090 with web-app integration depth |
| OWASP LLM Top 10 (2025) | Practitioner top risks LLM | 27090's GenAI annex maps each LLM Top 10 entry to 27090 threats and control families |
| MITRE ATLAS | Tactics/techniques knowledge base for AI | 27090 references ATLAS as the **operational tactic-technique catalogue** for threat modeling and red teaming |
| ISO/IEC 24029-1, -2 (-3 forthcoming) | Robustness assessment of NN | 27090 covers security robustness; 24029 covers technical robustness measurement |

## 2. AI threat taxonomy

Organised by the classic CIA (Confidentiality / Integrity / Availability) triad, with adaptations for AI-specific harms.

### 2.1 Confidentiality threats

| Threat | Definition | Vector | Practical impact |
|--------|-----------|--------|------------------|
| **Model extraction / stealing** | Adversary reconstructs a functional copy of a target model | Repeated queries to public inference API; capture input/output pairs to train a surrogate | IP theft, loss of competitive moat; surrogate enables transferable evasion attacks |
| **Membership inference** | Determining whether a specific record was in the training set | Exploit confidence-score gaps between members and non-members | GDPR/AI Act privacy breach, especially special-category training data (health, biometric) |
| **Model inversion** | Reconstructing training samples or sensitive attributes from model outputs/gradients | Gradient queries (white-box) or repeated confidence probing (black-box) | Re-identification of individuals, exposure of trade secrets in training data |
| **Training data leakage / memorization** | Models verbatim regurgitate training records | Targeted prompts; divergence attacks ("repeat this word forever") | Exposure of PII, copyrighted text, secrets/credentials inadvertently scraped |
| **Prompt injection (info-leak variant)** | Coerces an LLM into revealing context, RAG-retrieved documents, or tool outputs | Crafted instructions in user input or retrieved/embedded content | Leak of confidential RAG corpora, customer data, internal tooling state |
| **System-prompt extraction** | Forces disclosure of the hidden system/developer prompt | Role-play, encoding tricks, recursive summarization requests | Exposure of business logic, guardrails, competitive prompt engineering |

### 2.2 Integrity threats

| Threat | Definition | Vector | Practical impact |
|--------|-----------|--------|------------------|
| **Data poisoning (training-time)** | Malicious manipulation of training data to degrade model behavior | Tamper with web-scraped corpora, supply-chain datasets, federated-learning client updates | Targeted misclassification, biased outputs, broad accuracy collapse |
| **Evasion attacks / adversarial examples (inference-time)** | Imperceptibly perturbed inputs cause misclassification | Gradient-based (FGSM, PGD, C&W) white-box, transfer/query-based black-box | Bypass safety-critical classifiers (fraud, malware, biometric, content moderation) |
| **Backdoor / trojan attacks** | A trigger pattern is embedded during training so the model behaves normally except on triggered inputs | Poisoned training data; malicious pretrained checkpoints from open repos | Hidden, attacker-controlled override of decisions; particularly dangerous in supply-chain-sourced foundation models |
| **Model tampering** | Direct modification of weights, architecture, or serialized artifacts | Compromised model registry, insecure pickle/safetensors files, MLOps pipeline access | Silent integrity loss across deployment fleet |
| **Prompt injection (jailbreak / instruction override)** | User input causes the LLM to ignore developer instructions | Role-play, ASCII smuggling, multilingual evasion, gradient-crafted suffixes | Policy violations, harmful-content generation, regulatory non-compliance |
| **Indirect prompt injection** | Malicious instructions embedded in third-party content the model retrieves or processes | Attacker plants payload in content the agent will read (web pages, emails, PDFs, images) | Highest-severity for agentic systems — unauthorized tool calls, data exfiltration, lateral actions |

### 2.3 Availability threats

| Threat | Definition | Vector | Practical impact |
|--------|-----------|--------|------------------|
| **Sponge attacks (compute exhaustion)** | Inputs engineered to maximize the model's energy/latency consumption | Crafted inputs that defeat early-exit/sparsity optimizations | Inflated cloud bills, latency SLO breach, denial of service for legitimate users |
| **Resource exhaustion** | Generic flooding, KV-cache exhaustion in LLMs, long-context payloads | High-volume or maximum-context-window requests | Outage, autoscaling cost runaway |
| **Denial-of-service via inference** | Triggering pathological codepaths (recursive prompts, self-referential tool calls) | Recursive or self-referential prompts, "infinite loop" tool-call structures | Per-request DoS, blocked task queues |
| **Model unavailability** | Destruction or ransoming of model artifacts | Registry compromise, ransomware on training/serving infrastructure | Business continuity loss, inability to retrain quickly |

## 3. AI lifecycle attack surface

Which threats apply at which stage:

| Lifecycle stage | Primary threats |
|-----------------|-----------------|
| **Data preparation** | Data poisoning; supply-chain dataset tampering; PII ingestion (later → memorization/inversion); label flipping |
| **Training / fine-tuning** | Backdoor injection; federated-learning poisoning; gradient leakage; malicious pretrained-checkpoint import; hyperparameter tampering |
| **Evaluation / testing** | Test-set contamination; biased benchmark selection (integrity of evaluation); insufficient adversarial robustness testing |
| **Deployment** | Model tampering in registry; insecure serialization (pickle); missing signing/attestation; weights exfiltration |
| **Operation / serving** | Evasion; prompt injection (direct and indirect); jailbreak; model extraction; membership inference; sponge/DoS; system-prompt extraction; training-data extraction via memorization |
| **Monitoring / decommissioning** | Drift-masking attacks (poisoning that hides under monitoring thresholds); insecure model retirement leaving weights exposed; log poisoning; residual data on decommissioned hardware |

## 4. Mitigations and controls

### 4.1 Data hygiene

| Mitigation | What it does | Threats mitigated | Limitations / trade-offs |
|------------|--------------|-------------------|--------------------------|
| **Provenance tracking (data lineage, C2PA, ML-BOM)** | Cryptographically signed data origin records | Data poisoning, supply-chain tampering | Doesn't prevent insider poisoning at source; assumes trusted signers |
| **Data validation / outlier detection** | Statistical filtering of anomalous samples | Poisoning, label flipping | Clean-label and stealthy poisoning bypass simple statistics |
| **Federated learning + secure aggregation** | Distributed training without centralizing raw data | Training-data leakage, raw-data exposure | Introduces FL-specific poisoning (Byzantine clients); requires aggregation defenses |
| **Differential privacy (DP-SGD)** | Calibrated noise added during training | Membership inference, model inversion, memorization | Utility/privacy trade-off; tight ε hurts accuracy on small classes |

### 4.2 Training-time defenses

| Mitigation | What it does | Threats mitigated | Limitations / trade-offs |
|------------|--------------|-------------------|--------------------------|
| **Adversarial training** | Inject adversarial examples into training | Evasion attacks | Costly, attack-specific, can degrade clean accuracy, doesn't generalize across threat models |
| **Robust training (TRADES, MART)** | Loss-function regularization for robustness | Evasion | Same trade-offs as adversarial training |
| **Certified defenses (randomized smoothing, IBP)** | Provable robustness within an Lp ball | Bounded-norm evasion | Small certified radii; impractical for generative or high-dimensional models |
| **Regularization, dropout, gradient clipping** | Reduce overfitting/memorization | Membership inference, memorization | Not a substitute for DP |

### 4.3 Inference-time defenses

| Mitigation | What it does | Threats mitigated | Limitations / trade-offs |
|------------|--------------|-------------------|--------------------------|
| **Input validation / sanitization** | Schema, length, character-set, semantic checks | Prompt injection, sponge inputs | Adversaries adapt; cannot fully sanitize natural-language inputs |
| **Output guards / classifiers (Llama Guard, NeMo Guardrails, content classifiers)** | Filter unsafe model outputs | Jailbreaks, harmful content, leakage of secrets | False positives; arms race with new jailbreak techniques |
| **Anomaly / OOD detection** | Detect adversarial or out-of-distribution inputs | Evasion, sponge | Adaptive attackers craft in-distribution adversarial inputs |
| **Rate limiting / query budgets per identity** | Caps queries per user/key | Model extraction, membership inference, DoS | Sybil/distributed attackers bypass; affects legitimate power-users |

### 4.4 Model protection

| Mitigation | What it does | Threats mitigated | Limitations / trade-offs |
|------------|--------------|-------------------|--------------------------|
| **Watermarking (weight-level + output-level)** | Embedded ownership signal | Model theft (detection, not prevention) | Removable via fine-tuning or pruning |
| **Fingerprinting** | Behavioral signature of the model | Extraction detection | Same as watermarking |
| **Model encryption at rest, signed checkpoints, safetensors** | Cryptographic protection of artifacts | Tampering, exfiltration | Keys must be protected; doesn't help once decrypted in memory |
| **Trusted Execution Environments (Intel SGX/TDX, AMD SEV, NVIDIA Confidential Computing GPUs)** | Hardware-isolated inference | Weight exfiltration, model tampering by infrastructure operators | Performance overhead, side-channel attacks, vendor lock-in |
| **Access control to weights and registry (RBAC, MFA, audit)** | IAM around the model store | Tampering, exfiltration | Insider threat residual |

### 4.5 Generative-AI-specific (LLM/foundation model)

| Mitigation | What it does | Threats mitigated | Limitations / trade-offs |
|------------|--------------|-------------------|--------------------------|
| **Prompt injection defenses (instruction hierarchy, spotlighting, delimiters, dual-LLM patterns)** | Architectural separation of trusted vs untrusted text | Direct + indirect prompt injection | **No fully robust defense exists**; defense-in-depth required |
| **Jailbreak detection classifiers** | ML-based detection of adversarial prompts | Jailbreaks | Bypassable by novel attack patterns, multilingual evasion |
| **System-prompt protection (canary tokens, externalized logic)** | Detect leakage; minimize secrets in prompt | System-prompt extraction | Empirically difficult to fully prevent; treat as **defense-in-depth, not security boundary** |
| **Content filtering (input + output moderation)** | Pre/post classifiers | Harmful content, leakage | False positives, cultural bias |
| **Refusal training, RLHF, Constitutional AI, DPO** | Alignment-time safety | Harmful generation, jailbreaks | Shallow alignment; brittle under adversarial pressure |
| **Output watermarking (cryptographic, statistical)** | Detect AI-generated content | Misuse, deepfakes (provenance) | Removable via paraphrasing; **required by AI Act art. 50** |
| **Capability-restricted tool execution + sandboxing** | Least-privilege tool grants for agentic systems | Excessive agency, indirect prompt injection consequences | Limits agent utility; requires careful permission design |

### 4.6 Operational

| Mitigation | What it does | Threats mitigated | Limitations / trade-offs |
|------------|--------------|-------------------|--------------------------|
| **AI-specific incident response** | Playbooks for poisoning detection, model-theft response, jailbreak escalation | Impact of all threats | Requires AI-literate SOC |
| **Red teaming (manual + automated, e.g., PyRIT, Garak)** | Adversarial pre-deployment testing | Unknown vulnerabilities across the taxonomy | Sample of attack surface; **required by AI Act for systemic-risk GPAI** per art. 55 |
| **Security testing in CI/CD (model scanners, supply-chain SBOM/ML-BOM)** | Automated checks on every model artifact | Supply-chain backdoors, insecure serialization | Signature-based, misses novel backdoors |

## 5. Mapping to AI Act art. 15 (the operational reason 27090 exists)

Article 15 imposes three obligations on high-risk AI systems; ISO/IEC 27090 provides operational depth alongside Recital 76 (which **explicitly names** data poisoning, model poisoning, model evasion, confidentiality attacks, and model flaws).

### 5.1 Accuracy (art. 15(1), 15(3))

27090 is **not** the depth standard for accuracy itself (that lives in **ISO/IEC TR 24029-1/-2** on robustness assessment of neural networks, **ISO/IEC 25059** quality model for AI, and the upcoming **ISO/IEC 24029-3**, plus **ISO/IEC TS 4213:2022** on classification model performance assessment).

27090 contributes by mandating **evaluation-set integrity controls** — preventing test-set contamination so that declared metrics are trustworthy.

### 5.2 Robustness (art. 15(4))

27090 maps directly:
- Adversarial training, certified defenses, input validation, OOD detection, anomaly monitoring → "attempts to alter use" (art. 15(4))
- Drift detection and feedback-loop monitoring → feedback-loop mitigation (art. 15(4) final paragraph)
- Backup/redundancy/fail-safe plans (e.g., fallback to deterministic rules) → "technical redundancy" (art. 15(4))

### 5.3 Cybersecurity (art. 15(5) + Recital 76)

| Recital 76 named threat | 27090 controls |
|--------------------------|----------------|
| **Data poisoning** | Data hygiene controls (provenance, validation, ML-BOM); federated-learning Byzantine defenses |
| **Model poisoning** | Signed checkpoints; supply-chain scanning; backdoor detection; trusted model registries |
| **Model evasion** | Adversarial training; certified defenses; input validation; anomaly detection |
| **Confidentiality attacks** | DP-SGD; query rate limiting; membership-inference-resistant training; output filtering against memorization |
| **Model flaws** | Red teaming; security testing; vulnerability management lifecycle for AI artifacts |

This mapping is the **practical reason providers cite ISO/IEC 27090 alongside ISO/IEC 42001** and harmonised standards under art. 40 to claim presumption of conformity for art. 15.

## 6. GenAI / LLM-specific guidance

ISO/IEC 27090's foundation-model annex addresses risks distinct from classical ML. The OWASP LLM Top 10 (2025) maps onto 27090 as follows:

| OWASP LLM ID | Title | 27090 threat family | Primary controls |
|--------------|-------|---------------------|------------------|
| LLM01 | Prompt Injection | Direct + indirect prompt injection (integrity) | Instruction hierarchy, spotlighting, dual-LLM, content sanitization |
| LLM02 | Sensitive Information Disclosure | Training data leakage, memorization (confidentiality) | DP-SGD, deduplication, output filtering, canary insertion |
| LLM03 | Supply Chain | Backdoor / poisoned base models (integrity) | Signed checkpoints, ML-BOM, model signing, behavioral testing |
| LLM04 | Data and Model Poisoning | Training-time poisoning (integrity) | Data validation, provenance, federated aggregation defenses |
| LLM05 | Improper Output Handling | Output integrity issues; downstream injection | Output sanitization, Markdown/HTML escaping in consumers, content filtering |
| LLM06 | Excessive Agency | Indirect prompt injection downstream consequence | Capability-restricted tools, human-in-the-loop for high-impact, sandboxing, kill-switch |
| LLM07 | System Prompt Leakage | System-prompt extraction (confidentiality) | Externalize secrets; canary tokens; treat prompt as defense-in-depth |
| LLM08 | Vector and Embedding Weaknesses | Embedding inversion, RAG poisoning | Embedding security review, RAG content sanitization, retrieval access control |
| LLM09 | Misinformation | Hallucination as integrity issue | RAG with cited sources, tool-grounding, uncertainty estimation, output validators, refusal on low confidence |
| LLM10 | Unbounded Consumption | Sponge / resource exhaustion (availability) | Rate limiting, per-tool cost budgets, max-token caps, request quotas |

**Foundation-model supply-chain depth**: 27090 specifies that organizations using third-party base models (e.g., Llama 4, Claude API, GPT-OSS) shall:

- Trust only signed/attested model providers
- Scan checkpoints for backdoors (behavioral testing, weight-anomaly detection)
- Maintain **ML-BOM** (Machine Learning Bill of Materials) for the deployed stack
- Pin model versions; track upstream advisories
- Fine-tune on trusted data with documented provenance
- Implement "untrusted base model" controls when provenance cannot be fully assured

**Output integrity (hallucination)** is treated dually:
- As an **integrity issue** when the system asserts false facts in a high-stakes context — controls: RAG with citation, tool-grounding, uncertainty estimation, output validators, refusal on low-confidence answers
- Crosses into **availability** when fabricated outputs degrade system usefulness sufficiently to constitute effective unavailability

**Output watermarking and provenance** align with AI Act art. 50 transparency obligations. 27090 references **C2PA-style content credentials** (cryptographic provenance manifests) and statistical text watermarking. Watermarks are **detection mechanisms, not prevention** — pair with disclosure UX and metadata.

The annex is explicit that **no single control prevents prompt injection**. A layered architecture combining input filtering, instruction hierarchy, output filtering, tool-call mediation, and human oversight is the only currently defensible posture — a conclusion echoed by NIST AI 100-2 and the OWASP LLM Top 10.

## 7. Threat-model template (operational)

Use this template for any high-risk AI system threat model under art. 15 + ISO 27090:

```
SYSTEM: <name>
SCOPE: <model + serving infra + data pipeline + tooling>
ARCHITECTURE TYPE: <classical ML | foundation model | LLM agent | RAG | hybrid>
LIFECYCLE PHASES IN SCOPE: <data prep | training | eval | deploy | operate | monitor>

ASSETS:
  - Model weights (location, versioning, signing)
  - Training data (sensitivity, provenance, retention)
  - System prompt / configuration
  - Inference endpoint
  - Logs and telemetry
  - Tool integrations (for agents)

THREAT MODEL (per CIA + lifecycle):
  Confidentiality:
    [ ] Model extraction        — Likelihood: H/M/L; Impact: H/M/L; Controls: <list>
    [ ] Membership inference    — ...
    [ ] Model inversion         — ...
    [ ] Training data leakage   — ...
    [ ] Prompt injection (info) — ...
    [ ] System-prompt extract   — ...
  Integrity:
    [ ] Data poisoning          — ...
    [ ] Evasion / adversarial   — ...
    [ ] Backdoor / trojan       — ...
    [ ] Model tampering         — ...
    [ ] Prompt injection (jail) — ...
    [ ] Indirect prompt inject  — ...
  Availability:
    [ ] Sponge attacks          — ...
    [ ] Resource exhaustion     — ...
    [ ] DoS via inference       — ...
    [ ] Model unavailability    — ...

CONTROLS DEPLOYED:
  Data hygiene: <list with maturity>
  Training-time: <list with maturity>
  Inference-time: <list with maturity>
  Model protection: <list with maturity>
  GenAI-specific: <list, if applicable>
  Operational: <list>

RESIDUAL RISK: <accept | treat | transfer | avoid> per threat
RED TEAM: <last performed | next scheduled | tooling: PyRIT/Garak/manual>
INCIDENT RESPONSE: <playbook reference; SOC AI literacy; escalation path>

ART. 15 COMPLIANCE STATEMENT:
  Accuracy:    <metric, value, reference test set, ISO TS 4213 alignment>
  Robustness:  <test methodology per ISO 24029-2; adversarial accuracy at ε; feedback-loop mitigations>
  Cybersecurity: <Recital 76 threats addressed; controls deployed; red-team last>

ART. 15 EVIDENCE INDEX:
  - Threat model document (this)
  - Control implementation evidence
  - Test reports
  - Red-team reports
  - Incident response playbook
  - SoA references (42001 A.6.2.4, A.6.2.6 + 27090 sections)
```

## 8. Common anti-patterns and pitfalls

1. **"We have ISO 27001, so we cover AI security."** False. 27001 covers org-level info-sec but **not** adversarial-ML threats. 27090 is the AI-specific layer required to satisfy art. 15(5) Recital 76 named threats.

2. **"We use a hosted LLM, so security is the vendor's problem."** Partially false. The deployer remains responsible for indirect prompt injection (LLM06), excessive agency (LLM06 again at architecture level), output handling (LLM05), and operational monitoring. Vendor handles training-time threats and base-model integrity; deployer handles application-layer threats.

3. **"Watermarking solves art. 50."** No. Watermarks are removable; pair with cryptographic provenance (C2PA) + UX disclosure + metadata.

4. **"Adversarial training fixes evasion."** Partially. It hardens against the attacks used during training but doesn't generalize across threat models. Combine with input validation, anomaly detection, and runtime monitoring.

5. **"We prevent prompt injection with our system prompt."** Demonstrably false. The system prompt is **defense-in-depth, not a boundary**. Architectural separation (instruction hierarchy, dual-LLM, capability sandboxing) is mandatory for agentic systems.

6. **"Differential privacy is too lossy to use."** Often a false binary. DP at large ε (e.g., 8–10) provides meaningful protection against memorization with manageable utility loss. The choice is risk-calibrated, not all-or-nothing.

7. **"Red teaming is for systemic-risk GPAI only."** Wrong. **Required** for systemic-risk GPAI under art. 55, but **strongly advised** for any high-risk AI system under art. 15 due-diligence and ISO 42001 A.6.2.4 V&V expectations.

8. **"Pickle is fine, our team is trustworthy."** Pickle deserialization is a code-execution vector; the threat is supply-chain (malicious checkpoints from open repos), not insider. Use safetensors, signed checkpoints, and CI/CD scanners (e.g., Garak, modelscan).

## 9. Output template — security section of Annex IV technical file

When generating the security part of an Annex IV technical file (cross-ref `06-techdoc-annex-iv.md`):

```
ANNEX IV §2(g): RISK MANAGEMENT (security extract)
ANNEX IV §3:    PERFORMANCE METRICS (incl. adversarial accuracy)
ANNEX IV §4:    APPROPRIATENESS (security justification)

SECURITY DESIGN:
  - Authentication & authorisation for inference endpoint
  - Input validation rules (length, schema, content classifier)
  - Output guards (Llama Guard / NeMo / equivalent)
  - Rate limiting per identity
  - Logging / observability (per art. 12)

THREAT MODEL: see 27090 threat-model template (sect. 7 of this reference)

ADVERSARIAL ROBUSTNESS:
  - Methodology: ISO/IEC 24029-2
  - Attack types tested: <FGSM, PGD, C&W, query-based, prompt injection battery>
  - Robust accuracy: <metric @ ε>
  - Tooling: <PyRIT, Garak, manual red team>

CONFIDENTIALITY DEFENSES:
  - DP-SGD: ε = <value> (or N/A with rationale)
  - Membership-inference test: <method, score>
  - Memorization audit: <method, results>

SUPPLY CHAIN:
  - ML-BOM: <reference>
  - Base model provenance: <vendor, version, signing>
  - Training data provenance: <reference>

INCIDENT RESPONSE:
  - Playbook: <reference>
  - Escalation: <reference>
  - Post-incident review: <reference>

ALIGNMENT TO STANDARDS:
  - ISO/IEC 27090:2025 — sections <list>
  - ISO/IEC 24029-2:2023 — robustness assessment
  - ISO/IEC TS 4213:2022 — classification performance
  - NIST AI 100-2:2025 — AML taxonomy reference
  - OWASP LLM Top 10 (2025) — addressed: <list>
```

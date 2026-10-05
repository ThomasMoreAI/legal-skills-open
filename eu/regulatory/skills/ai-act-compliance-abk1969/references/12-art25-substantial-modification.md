# 12 — Substantial Modification (AI Act art. 25, art. 43(4), art. 3(23))

The **art. 25 provider-flip** is the single most consequential under-recognized obligation in the AI Act. A deployer who substantially modifies a high-risk AI system **becomes a provider** of that modified system and inherits the full provider regime (arts. 8–17, conformity assessment, CE marking, EU database, 10-year doc retention).

It is also the routing rule for **fine-tuning a foundation model for high-risk use**: the fine-tuner becomes the provider.

## 1. The flip — what art. 25 actually says

### 1.1 Art. 25(1) — three triggers

A **distributor, importer, deployer or other third party** is considered a provider of a high-risk AI system and is subject to the obligations of providers (art. 16) when:

(a) They put **their name or trademark** on a high-risk AI system already placed on the market or put into service, without prejudice to contractual arrangements stipulating that the obligations are otherwise allocated.

(b) They make a **substantial modification** to a high-risk AI system already placed on the market or put into service in such a way that it remains a high-risk AI system pursuant to art. 6.

(c) They **modify the intended purpose** of an AI system, including a general-purpose AI system, that has not been classified as high-risk and has already been placed on the market or put into service, in such a way that the AI system concerned becomes a high-risk AI system pursuant to art. 6.

### 1.2 Definition of "substantial modification" (art. 3(23))

> *"Substantial modification means a change to an AI system after its placing on the market or putting into service which is not foreseen or planned in the initial conformity assessment carried out by the provider and as a result of which the compliance of the AI system with the requirements set out in Chapter III, Section 2 [arts. 8–15] is affected, or which results in a modification to the intended purpose for which the AI system has been assessed."*

Two operative limbs:

| Limb | Trigger condition |
|---|---|
| **Compliance impact** | Change affects compliance with arts. 9–15 essential requirements (e.g., new failure mode, accuracy degradation, broader attack surface, new bias) |
| **Intended-purpose change** | Change to the intended purpose stated by the original provider — even if essential requirements seem unaffected |

The **safe harbour**: changes that were **foreseen or planned in the initial conformity assessment** are not substantial modification. This makes the *original* provider's documentation (Annex IV §6 "relevant changes made through lifecycle") critical: if the change is documented as foreseen, no flip.

### 1.3 Art. 25(2) — Annex I product-safety carve-out

For high-risk AI systems on Annex I products: if the AI system is part of a product covered by Annex I sectoral legislation, the **product manufacturer** (e.g., medical-device manufacturer under MDR) is considered the provider — not the AI vendor — and the AI Act provider obligations apply alongside the sectoral conformity regime.

### 1.4 Art. 25(3) — provider obligations after the flip

Once the flip occurs, the third party assumes **all provider obligations** under art. 16. The original provider is **no longer the provider for the modified system** but must cooperate with the new provider, providing information, documentation, and reasonable technical access for compliance (this is contractually crucial — see § 4 below).

### 1.5 Art. 25(4) — GPAI flow-down

For high-risk AI systems that are integrated with a general-purpose AI **system** (not just a model — note the distinction): the GPAI provider must provide the necessary information and capability to enable the high-risk-system provider to comply with this Regulation. Two-step chain: foundation-model provider → integrator → end deployer.

## 2. Practical triggers — what counts as substantial modification

### 2.1 Strong-trigger patterns (almost always substantial)

- **Retraining with substantially different data** (different population, different sensors, different task formulation)
- **Fine-tuning a third-party model for an Annex III use case** — see § 3 below
- **Domain repurposing**: a CV-screening model deployed for credit decisioning; a medical-device approval model deployed for insurance pricing
- **Architectural swap**: replacing the underlying ML algorithm or model family while keeping the API
- **Adding a new modality** (text-only → text+image; image → image+biometric)
- **Removing a safety constraint** that was part of the original conformity assessment (e.g., disabling a confidence-threshold filter, removing a human-in-the-loop)

### 2.2 Weak-trigger patterns (case-by-case)

- **Threshold tuning** within bounds documented in the IFU (art. 13)
- **UI relocalization** without functional change
- **Routine retraining on freshly collected same-distribution data**, when foreseen
- **Bug-fix patches** that strictly restore original conformity

### 2.3 Non-trigger patterns (typically not substantial)

- **Configuration choices anticipated by the provider** in the IFU
- **Cosmetic re-skinning** (logo, colours, copy)
- **Server migration / infrastructure change** without functional change

The line is fuzzy by design. When in doubt, **document the change in detail** and treat as substantial. A late discovery that something was substantial creates retroactive non-conformity (art. 8 + art. 16).

## 3. Foundation-model fine-tuning — the dominant case

Fine-tuning a third-party foundation model (Llama, GPT-OSS, Gemma, Mistral, ...) for an Annex III high-risk use case is the single most common art. 25 trigger today.

| Stage | Who is the provider | Obligations |
|---|---|---|
| Foundation model published by Foundation Inc. (general-purpose) | Foundation Inc. (GPAI provider) | Arts. 53–55 (model card, copyright policy, training-data summary; +art. 55 if systemic risk) |
| Acme Corp. fine-tunes the model on their employment-decision dataset and integrates it into a recruitment platform | **Acme Corp. becomes the provider of the high-risk AI system** (Annex III §4 employment) | Full provider regime: arts. 8–17, conformity assessment per art. 43, CE marking, EU database, 10-year doc retention |
| Beta Ltd. licenses Acme's recruitment platform and uses it to screen its own candidates | Beta Ltd. is the **deployer** | Art. 26 deployer obligations + art. 27 FRIA |

**Art. 25(4) flow-down**: Foundation Inc. must provide Acme with sufficient information to enable Acme's compliance — typically a model card, training-data summary, evaluation results on benchmarks, known failure modes. Acme's legal team must obtain this in writing as part of the licence terms.

**ISO 42001 anchor** (cl. 8.4 + Annex A.10.3 supplier relationships): Acme's AIMS must include a controlled supplier-information process for foundation models, including evidence retention.

### 3.1 Open-source foundation model carve-out

Per art. 53(2), free and open-source GPAI models without monetisation are exempt from arts. 53(1)(a)(b) (technical documentation and downstream-provider information). They are NOT exempt from art. 53(1)(c) (copyright policy) and not from art. 55 (systemic-risk obligations).

For the fine-tuner (Acme): the open-source carve-out at the model layer **does not** affect Acme's art. 25 flip. Acme still becomes the high-risk provider once it integrates the model into an Annex III use.

## 4. Contractual implications

The art. 25 flip is also a contractual flip. A defensible procurement / licensing posture:

| Provision | Why |
|---|---|
| **Information access clause**: original provider commits to provide Annex IV-relevant documentation, including training-data summary, V&V evidence, threat model | Required for the new provider's art. 11 + Annex IV documentation |
| **Foreseen-change schedule**: original provider lists changes anticipated in the initial conformity assessment | Establishes safe-harbour scope under art. 3(23) |
| **Notification clause**: each party notifies the other of any change considered substantial within N days | Triggers re-conformity assessment per art. 43(4) |
| **Indemnity for misclassification**: who bears the cost if a change later determined substantial caused the original provider's CE mark to fail? | Allocates the regulatory risk |
| **Cooperation clause**: each side commits to cooperate in market surveillance (art. 21) and serious-incident reporting (art. 73) | Operational continuity |

For deployers of foundation-model APIs, also include:

- **Model-version pin** + advance notice of breaking changes
- **Right to audit** evaluation results
- **Data-flow attestation** (training data not enriched by deployer's prompts/outputs unless agreed)

## 5. Re-conformity assessment under art. 43(4)

Once a substantial modification occurs, art. 43(4) requires:

> *"For high-risk AI systems that have already been subject to a conformity assessment procedure, a new conformity assessment procedure shall be carried out in the event of a substantial modification, irrespective of whether the modified system is intended to be further distributed or continues to be used by the current deployer."*

Mechanics:

1. **Re-execute conformity assessment** for the modified system per art. 43(1) or (2) — internal control (Annex VI) or notified body (Annex VII) per the same path the original used.
2. **Update the technical documentation** (Annex IV, §6 "relevant changes through lifecycle").
3. **Re-issue declaration of conformity** (art. 47 + Annex V).
4. **Re-affix CE marking** (or maintain, depending on the marking strategy).
5. **Update EU database registration** (art. 49) for the new provider entity (the new provider replaces the original one in the database for the modified system).

The new provider also restarts the **10-year doc retention clock** (art. 18) for the modified system.

## 6. ISO 42001 + 27090 anchors

| Operational concern | ISO/IEC 42001 | ISO/IEC 27090 |
|---|---|---|
| Detection of substantial modification | cl. 6.3 (planning of changes); cl. 8.4 (operational AI system impact assessment) | sect. 4.6 (operational lifecycle) — change-triggered re-evaluation |
| Re-execute AISIA on modification | cl. 6.1.4 + 8.4; Annex A.5.2 | — |
| Supplier (foundation-model) information flow | A.10.3 (third parties) | sect. 5 + supply-chain considerations |
| Documentation update | cl. 7.5; A.4.2 + A.6.2.7 | sect. 9 (documentation) |
| Communication to interested parties | cl. 7.4; A.8.5 | — |

## 7. Decision aid — am I a provider after this change?

```
START
  ↓
Is the change documented as foreseen in the original provider's
initial conformity assessment / IFU / Annex IV §6?
  ├─ YES → No flip. Operate within foreseen envelope. Update logs.
  └─ NO  → Continue.
       ↓
Does the change affect compliance with arts. 9–15
(accuracy, robustness, cyber, RMS, data, oversight, transparency)?
  ├─ YES → SUBSTANTIAL MODIFICATION → Flip per art. 25(1)(b).
  └─ NO  → Continue.
       ↓
Does the change modify the intended purpose stated in the original IFU
(art. 13)?
  ├─ YES → SUBSTANTIAL MODIFICATION → Flip per art. 25(1)(b) or (c).
  └─ NO  → Continue.
       ↓
Are you placing your own name or trademark on the system?
  ├─ YES → Flip per art. 25(1)(a).
  └─ NO  → Likely no flip. Document the analysis. Reassess if scope grows.
```

## 8. Output template — substantial-modification analysis

```
SYSTEM: <name + version pre/post-modification>
ORIGINAL PROVIDER: <legal entity>
MODIFYING PARTY: <legal entity proposing the change>

CHANGE DESCRIPTION
  Type: <fine-tune | retrain | repurpose | architectural swap | constraint change | rebrand | other>
  Detail: <2-3 sentences>

ORIGINAL ANNEX IV §6 SCOPE (foreseen-change envelope)
  <quote or summarize>

ANALYSIS
  Limb (a) name/trademark: <yes/no>
  Limb (b) compliance impact: <yes/no — which arts. 9–15 affected>
  Limb (c) intended-purpose change: <yes/no — old vs new purpose>
  Foreseen-in-CA safe harbour: <applies / does not apply, with rationale>

CONCLUSION
  Substantial modification: <YES → flip | NO>
  New provider (if flip): <legal entity>

CONSEQUENCES IF FLIP
  [ ] Acme assumes art. 16 provider obligations
  [ ] Re-conformity assessment per art. 43(4)
  [ ] Update Annex IV technical documentation
  [ ] Re-issue declaration of conformity (art. 47 + Annex V)
  [ ] Re-affix CE marking (art. 48)
  [ ] Update EU database registration (art. 49)
  [ ] 10-year doc retention restart (art. 18)
  [ ] Update AIMS scope; re-run AISIA (ISO 42001 cl. 6.1.4 / 8.4)
  [ ] Trigger art. 73 readiness review (incident reporting)

CITATIONS
  - AI Act art. 25; art. 3(23); art. 43(4); art. 16; art. 11 + Annex IV §6
  - ISO/IEC 42001:2023 cl. 6.3, 8.4, 6.1.4 + Annex A.5.2, A.10.3
  - ISO/IEC 27090:2025 sect. 4.6 (operational lifecycle change)

LEGAL DISCLAIMER
  Decision-support output. Not legal advice. Substantial-modification
  determination is fact-intensive; obtain qualified counsel before
  acting on the conclusion above.
```

## 9. Cross-references

- `01-risk-classification.md` § 3.1 (substantial modification edge case) and § 3.2 (foundation-model fine-tuning).
- `02-high-risk-obligations.md` (provider regime that the flipped party inherits).
- `05-crosswalk-aiact-iso.md` row "art. 25" (clause and control mapping).
- `06-techdoc-annex-iv.md` § 6 (relevant changes through lifecycle — the safe-harbour evidence).
- `10-gpai-and-timeline.md` (foundation-model upstream provider regime).

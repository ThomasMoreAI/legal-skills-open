# Regulation-to-CE Capability Map

## EU AI Act — Article-by-Article Mapping

The canonical, detailed mapping with code examples lives in:
`docs/practitioner/playbooks/eu-ai-act-compliance.md`

### Summary table

| Article | Title | CE method(s) | What it provides | Status |
|---|---|---|---|---|
| Art. 9 | Risk management system | `predict_proba(uq_interval=True)` | Interval width as quantitative risk indicator | Covered |
| Art. 10 | Data and data governance | `explain_factual(bins=...)`, `predict_proba(bins=...)` | Per-group intervals via Mondrian calibration | Covered |
| Art. 11 + Annex IV | Technical documentation | `to_json()`, schema v1, calibration config | Machine-readable audit evidence | Covered |
| Art. 12 | Record-keeping | `to_json()` + `to_json_stream()` | Serialised per-prediction audit records | Partially covered (deployer provides log infra) |
| Art. 13 | Transparency | `explain_factual()`, `print_rules()`, `to_narrative()` | Human-readable per-instance rule tables | Covered |
| Art. 14 | Human oversight | `RejectPolicy.FLAG`, straddle/width gates | Automatic escalation on uncertainty | Covered |
| Art. 15 | Accuracy, robustness | Venn-Abers coverage guarantees, conformal prediction | Empirically valid accuracy declaration | Covered |
| Art. 50 | Right to explanation | `explore_alternatives()`, `to_narrative()` | Actionable counterfactual alternatives | Covered |

---

## GDPR — Automated Decision-Making

| Article / Recital | Obligation | CE capability | Notes |
|---|---|---|---|
| Art. 22(1) | Right not to be subject to solely automated decisions | `RejectPolicy` + uncertainty gates | Routes uncertain cases to humans |
| Art. 22(3) | Right to obtain human intervention and contest | `explore_alternatives()` | Shows what would change the outcome |
| Art. 22(4) | Suitable safeguards including right to explanation | `explain_factual()` + `to_narrative()` | Per-instance explanation for DSAR |
| Recital 71 | Right to obtain explanation of decision | `to_narrative(expertise_level='beginner')` | Plain-language output for lay persons |
| Art. 35 | Data Protection Impact Assessment | Mondrian calibration per-group analysis | Quantitative bias evidence for DPIA |

### GDPR interaction with AI Act

Where both apply (high-risk system processing personal data):
- GDPR Art. 22 explanation obligations are **additive** to AI Act Art. 13/50.
- CE satisfies both simultaneously: `explain_factual()` serves Art. 13 (deployer
  transparency) and Art. 22 (data subject explanation).
- Mondrian analysis serves both Art. 10 (bias examination) and GDPR Art. 35 (DPIA).

---

## AI Liability Directive (AILD)

The AILD (COM/2022/496, expected adoption 2025-2026) creates a civil liability
framework specific to AI systems. It complements the PLD for non-contractual
fault-based liability.

| AILD provision | Obligation/mechanism | CE relevance |
|---|---|---|
| Art. 3 — Presumption of causality | If AI provider breached a duty of care and damage occurred, causality is presumed | CE audit logs (`to_json()`) demonstrate compliance with care standards |
| Art. 4(2) — Disclosure obligation | Courts can order providers to disclose relevant evidence | CE payloads are pre-prepared, structured disclosure evidence |
| Art. 4(3) — Presumption of fault | If provider fails to comply with disclosure order, fault is presumed | Comprehensive CE audit trail reduces risk of adverse presumption |
| Art. 4(5) — Rebuttable presumption | For high-risk AI: non-compliance with AI Act = presumed fault | CE's AI Act compliance outputs rebut this presumption |

### Practical implication

A provider using CE can demonstrate:
1. **Transparency was provided** (factual rules logged per Art. 13)
2. **Uncertainty was quantified** (intervals logged per Art. 15)
3. **Uncertain cases were escalated** (reject policy logged per Art. 14)
4. **Bias was examined** (Mondrian analysis logged per Art. 10)

This body of evidence directly addresses the AILD's disclosure obligations and
rebuts the presumption of fault.

---

## Product Liability Directive (PLD — Directive (EU) 2024/2853)

The revised PLD (entered into force 9 December 2024, transposition deadline
9 December 2026) explicitly includes AI systems and software as "products."

| PLD provision | Relevance to CE |
|---|---|
| Art. 4(4) — Software as product | AI systems placed on market are products; CE outputs are product safety artefacts |
| Art. 7(1)(a) — Defectiveness: safety expectations | CE's uncertainty intervals document expected safety level at deployment |
| Art. 7(1)(e) — Learning after deployment | CE calibration set documents the system's knowledge boundary; recalibration logs track evolution |
| Art. 9(4) — Disclosure of evidence | If provider fails to disclose, defectiveness is presumed; CE audit payloads serve as pre-prepared evidence |
| Art. 10 — Presumption of defectiveness | Non-compliance with mandatory safety requirements = presumed defective; CE compliance with AI Act rebuts this |

### Key defence strategy

Under the PLD, a provider must show the product was not defective when placed
on the market. CE supports this by:
- Documenting empirical coverage at deployment time (calibration validation).
- Logging per-prediction explanations and uncertainty (operational evidence).
- Providing Mondrian analysis showing equitable performance across groups.

---

## Cross-regulation interaction

AI Act compliance evidence simultaneously supports:
- **GDPR Art. 22** explanation rights (same explanation outputs)
- **AILD Art. 3-4** disclosure obligations (same audit trail)
- **PLD Art. 7, 9** safety documentation (same calibration evidence)

The `to_json()` payload is the single artefact that serves all four regulations.

---

## Paper citations supporting regulatory claims

### Coverage guarantee (Art. 15 accuracy)
> Venn-Abers calibration provides multi-probability predictions with empirical
> validity guarantees. The calibrated probability interval's coverage converges
> to the nominal confidence level as calibration set size increases.
>
> — Lofstrom et al. (2024), Expert Systems with Applications, DOI: 10.1016/j.eswa.2024.123154

### Per-group fairness (Art. 10 bias)
> Conditional calibrated explanations partition the calibration set by a grouping
> variable, fitting separate calibrators per partition. This reveals group-specific
> prediction reliability and surfaces discriminatory patterns.
>
> — Lofstrom et al. (2024), ECAI Workshop, DOI: 10.1007/978-3-031-63787-2_17

### Conformal prediction validity
> Conformal prediction provides distribution-free, finite-sample coverage guarantees
> under the exchangeability assumption.
>
> — Shafer & Vovk (2008), JMLR 9, 371-421

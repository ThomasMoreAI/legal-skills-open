# Crosswalk — NIST risk names ↔ common policy aliases

NIST uses specific terms for risks and characteristics. Most organizations' AI policies use overlapping but different vocabulary. This file maps NIST language to the aliases you'll most commonly see in corporate policies, regulator guidance, and academic literature — so the skill can speak in the user's language while still anchoring on NIST.

This is hand-built, not extracted. Update it when you see a new alias worth recording.

## The 12 GAI risks (NIST AI 600-1)

| NIST risk | Common aliases / where you'll see them |
|---|---|
| **CBRN Information or Capabilities** | "Weapons uplift," "dual-use risk," "biosecurity / chemical security risk." EU AI Act high-risk category; EO 14110 emphasis. |
| **Confabulation** | "Hallucination," "fabrication," "made-up content," "false output." Most consumer policies use "hallucination." |
| **Dangerous, Violent, or Hateful Content** | "Harmful content," "objectionable content," "trust & safety violations." Often split into "violence," "self-harm," "hate speech" categories. |
| **Data Privacy** | "Personal data risk," "PII exposure," "privacy harms," "memorization risk." GDPR/CCPA framing: lawful basis, data minimization, subject rights. |
| **Environmental Impacts** | "Sustainability," "compute footprint," "carbon impact," "energy use of training/inference." |
| **Harmful Bias and Homogenization** | "Discrimination," "fairness," "algorithmic bias," "disparate impact," "model collapse" (for homogenization specifically). EEOC / civil rights framing often uses "discrimination." |
| **Human-AI Configuration** | "Automation bias," "over-reliance," "anthropomorphization," "scope of human oversight," "human-in-the-loop / human-on-the-loop design." |
| **Information Integrity** | "Misinformation," "disinformation," "synthetic media risk," "deepfakes," "election integrity." |
| **Information Security** | "Model security," "prompt injection," "jailbreaks," "data exfiltration via model," "adversarial attacks." OWASP LLM Top 10 overlap. |
| **Intellectual Property** | "Copyright risk," "training data infringement," "output infringement," "license compliance," "trade secret leakage." |
| **Obscene, Degrading, and/or Abusive Content** | "CSAM," "NCII," "non-consensual intimate imagery," "abusive content." Mandatory reporting obligations in many jurisdictions. |
| **Value Chain and Component Integration** | "Supply chain risk," "third-party / vendor risk," "open-source model risk," "dependency risk," "model provenance." NIST SSDF / SBOM crosswalk. |

## The 7 Trustworthy AI characteristics (NIST AI 100-1)

| NIST characteristic | Common aliases |
|---|---|
| **Valid and Reliable** | "Accuracy," "robustness," "performance," "generalization." Often the headline metric in PRDs. |
| **Safe** | "Safety," "harm prevention," "guardrails," "no-deploy criteria." |
| **Secure and Resilient** | "Security," "adversarial robustness," "incident resilience," "fail-safe behavior." |
| **Accountable and Transparent** | "Auditability," "documentation," "disclosure," "model cards," "system cards," "right to explanation." |
| **Explainable and Interpretable** | "Explainability," "interpretability," "XAI," "decision rationale," "right to know why." |
| **Privacy-Enhanced** | "Privacy by design," "data minimization," "differential privacy," "PET" (privacy-enhancing techniques). |
| **Fair – with Harmful Bias Managed** | "Fairness," "equity," "non-discrimination," "demographic parity / equalized odds / etc." |

## Risk family groupings (informal but useful)

When a user's policy uses broad categories rather than NIST's 12, these groupings often map:

- **"Trust & safety"** → typically covers: Dangerous/Violent/Hateful Content; Obscene/Degrading/Abusive Content; Information Integrity (misuse); Human-AI Configuration (abuse).
- **"Responsible AI / Fairness"** → typically covers: Harmful Bias and Homogenization; Human-AI Configuration; Accountable and Transparent characteristic.
- **"Security"** → typically covers: Information Security; Data Privacy (in the breach sense); Value Chain (in the supply-chain compromise sense).
- **"IP / Legal"** → typically covers: Intellectual Property; Data Privacy (in the lawful-basis sense); often Information Integrity (in the misuse/defamation sense).
- **"Compliance / Regulatory"** → cuts across all 12 depending on the regime; explicitly named in GOVERN 1.1 / GOVERN 6 subcategories.

## How the skill uses this

When the user describes a system or policy, look for keywords from the right column of the tables above and map back to the NIST term on the left. Cite the NIST term verbatim in the output, but add the user's alias parenthetically the first time it appears, e.g.:

> "**Confabulation** (sometimes called 'hallucination'): …"

This avoids forcing a vocabulary change on the user while keeping the authority anchored on NIST.

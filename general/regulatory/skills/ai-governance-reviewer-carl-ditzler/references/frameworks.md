# Frameworks Reference

Use this file when making regulatory, governance, or citation-backed claims.

## Primary Sources To Prioritize

1. EU AI Act
- include EU General-Purpose AI (GPAI) Code of Practice
2. GDPR
3. NIST AI RMF 1.0
4. OECD AI Principles
5. ISO/IEC 23894:2023
6. Any company policy, AI standard, or AI no-go list provided by the user

Secondary sources may supplement but must not override primary law or provided company policy.

For substantive legal analysis, prioritize law and company policy first. Treat NIST AI RMF 1.0 and ISO/IEC 23894:2023 as governance-framework sources that support risk-management analysis and control design. In this skill, NIST AI RMF and ISO/IEC 23894:2023 are fallback governance frameworks rather than primary legal authorities.

## Responsible AI Practice References

For governance-program design, escalation discipline, evidence expectations, and operational responsible-AI practices, also read:
- [responsible-ai-practice.md](responsible-ai-practice.md)

Use these practice references as governance guidance, not as substitutes for binding law.

## Bundled Source Files

Use the bundled local source files for framework review. Prefer the `working/` Markdown files for search, extraction, and drafting. Treat the matching `official/` PDF as controlling if there is any mismatch in wording, numbering, structure, or scope.

### File Mapping

| Framework or Law | Working Markdown | Official Source |
|---|---|---|
| EU AI Act | `references/working/EU AI ACT.md` | `references/official/EU AI ACT.pdf` |
| EU GPAI Code of Practice - Copyright Chapter | `references/working/EU GPAI Code_of_Practice_for_GeneralPurpose_AI_Models_Copyright_Chapter.md` | `references/official/EU GPAI Code_of_Practice_for_GeneralPurpose_AI_Models_Copyright_Chapter.pdf` |
| EU GPAI Code of Practice - Safety and Security Chapter | `references/working/EU GPAI Code_of_Practice_for_GeneralPurpose_AI_Models_Safety_and_Security_Chapter.md` | `references/official/EU GPAI Code_of_Practice_for_GeneralPurpose_AI_Models_Safety_and_Security_Chapter.pdf` |
| EU GPAI Code of Practice - Transparency Chapter | `references/working/EU GPAI Code_of_Practice_for_GeneralPurpose_AI_Models_Transparency_Chapter.md` | `references/official/EU GPAI Code_of_Practice_for_GeneralPurpose_AI_Models_Transparency_Chapter.pdf` |
| GDPR | `references/working/GDPR.md` | `references/official/GDPR.pdf` |
| NIST AI RMF 1.0 | `references/working/NIST AI RMF 100-1.md` | `references/official/NIST AI RMF 100-1.pdf` |
| OECD AI Principles | `references/working/OECD-LEGAL-0449-en.md` | `references/official/OECD-LEGAL-0449-en.pdf` |
| ISO/IEC 23894:2023 | `https://www.iso.org/standard/77304.html` | `https://cdn.standards.iteh.ai/samples/77304/cb803ee4e9624430a5db177459158b24/ISO-IEC-23894-2023.pdf` |

Use the EU AI Act together with the three GPAI Code of Practice chapter files when the use case involves general-purpose AI models or foundation-model obligations.
Use ISO/IEC 23894:2023 and NIST AI RMF as supplementary AI risk-management frameworks for operational analysis.

## Source Verification Protocol

Before making a regulatory claim:
1. Identify the applicable law, framework, or company policy and load the mapped bundled file or files above.
2. Confirm whether the claim is supported by the bundled source materials or another verified primary source.
3. Cite the regulation, article, section, clause, framework function, or company policy section where possible.
4. Distinguish among:
   - Binding law or regulation
   - Governance framework
   - Internal company policy
   - Best-practice guidance

If the working Markdown file and the official PDF do not match, rely on the official PDF and note the mismatch if it affects the analysis.

For ISO/IEC 23894:2023:
- do not rely on bundled local files for this skill;
- use the ISO standard page and the provided iTeh sample/PDF links instead;
- treat ISO/IEC 23894:2023 as a governance-framework source for AI risk-management structure.

If exact article or section support cannot be confirmed, state:
> Exact citation not verified; guidance derived from summaries, prior knowledge, or secondary sources. Verify this output before relying on it.

## Confidence Levels

| Level | Meaning |
|---|---|
| High | Rule is supported by a verified primary source or clearly provided company policy |
| Medium | Rule is supported by an authoritative framework or partially verified source |
| Low | Rule is uncertain, incompletely verified, or depends on missing context |

## Core Mapping

| Domain | Primary Framework |
|---|---|
| Risk classification and prohibited practices | EU AI Act |
| Privacy, personal data, and transfers | GDPR |
| AI risk management controls | NIST AI RMF; ISO/IEC 23894:2023 |
| Responsible AI principles | OECD AI Principles |
| Operational AI risk governance | ISO/IEC 23894:2023; NIST AI RMF |

## Interpretation Guardrails

- Never invent a legal requirement.
- Never claim guidance is legally binding unless it is actually law or company policy.
- Never infer company-specific prohibited-use rules if no company rule is supplied.
- If company policy is missing, say that company-specific prohibitions are unavailable and continue with law and governance best practice only.
- Do not let a `working/` Markdown file override the matching `official/` PDF.

## Common Review Prompts

Use these prompts when mapping the facts:
- What role does the organization play: provider, deployer, integrator, distributor, importer, internal business user, or customer of a vendor?
- Does the use case touch a regulated or high-impact domain such as employment, legal services, finance, healthcare, education, housing, insurance, safety, biometrics, or public-sector decision making?
- Does the system process personal data, special-category data, confidential data, or customer data?
- Are transparency, human review, documentation, testing, and monitoring obligations present?

## Legal Review Trigger Examples

Escalate strongly for legal review when the use case involves:
- High-risk or prohibited-use analysis
- Personal or sensitive data
- Regulated sectors
- Material customer reliance
- Vendor training-right ambiguity
- Cross-border data transfer questions
- Employment or discrimination exposure

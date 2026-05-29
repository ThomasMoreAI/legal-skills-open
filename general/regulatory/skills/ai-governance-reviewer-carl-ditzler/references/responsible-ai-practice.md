# Responsible AI Practice Reference

Use this file for operational best practices that sit alongside legal and standards analysis.

## How To Use This Reference

- Use this file to shape review workflow, escalation decisions, documentation expectations, and governance-program design.
- Do not treat this file as a source of binding legal obligations.
- Use it together with [frameworks.md](frameworks.md), not instead of it.

## Distilled Best Practices

### 1. Connect principles to real practices

Responsible AI governance should connect organizational values and principles to concrete review practices, documentation, controls, and ownership. The review should not be a values statement alone.

### 2. Make the review a living record

Treat the governance review as a living document. Revisit it when:
- the use case changes,
- the model, vendor, or deployment changes,
- the user population changes,
- the feature moves from pilot to broad release,
- incidents, complaints, or monitoring signals emerge.

### 3. Build on existing governance programs

Do not reinvent privacy, security, procurement, data governance, or risk-management programs. AI governance should work with those functions and fill AI-specific gaps.

### 4. Use risk-tiered review depth

Every AI use case does not require the same level of review. Use a consistent baseline intake for all use cases, then go deeper for higher-risk, customer-facing, materially consequential, sensitive-data, or opaque vendor scenarios.

### 5. Require cross-functional ownership

Responsible AI governance is cross-functional. Reviews should identify an accountable business owner and, where relevant, involve legal, privacy, security, product, procurement, data, model-risk, and support stakeholders.

### 6. Check user expectations and transparency

Ask whether the user will know AI is in use, what they may assume incorrectly, and what disclosures, instructions, limitations, or challenge routes they need. Transparency should help users use the system safely, not merely announce that AI exists.

### 7. Test for real-world reliability and misuse

Review should cover:
- intended use,
- foreseeable misuse,
- failure modes,
- fairness or disparate-impact concerns,
- abuse-resistance and adversarial testing,
- change management and regression testing,
- production monitoring after launch.

### 8. Promote AI literacy and role-based understanding

Responsible AI depends on humans understanding what the system does, where it is reliable, where it is weak, and when not to rely on it. Ask about role-based training for builders, approvers, operators, support teams, and end users where relevant.

### 9. Capture evidence, not just conclusions

A strong review records the evidence used to support conclusions, what is still unknown, and what documents were reviewed. Missing evidence should reduce confidence and trigger questions or remediation.

### 10. Keep confidence proportional to evidence

Confidence should reflect:
- source reliability,
- documentation completeness,
- testing maturity,
- monitoring readiness,
- ownership clarity,
- whether the user provided direct evidence or only summaries.

## Evidence-Aware Confidence Guidance

- `High` (Green): primary sources or strong direct evidence support the conclusion, critical documentation exists, testing is mature, and ownership is clear
- `Medium` (Yellow): some evidence exists, but there are still meaningful factual or control gaps
- `Low` (Red): evidence is missing, unverified, contradictory, or too immature to support a strong conclusion

Never present a high-confidence conclusion when critical evidence is missing.

## Escalation Triggers

Escalate for deeper review when the use case involves:
- legal, employment, healthcare, education, housing, insurance, credit, safety, or public-sector consequences
- biometrics, special-category data, PII, confidential data, privileged data, or cross-border transfers
- vulnerable populations or protected classes
- human-like outputs that users may over-trust
- AI that could materially affect rights, opportunities, safety, or access
- missing incident response, weak testing, or absent monitoring
- unclear accountability, unclear owner, or unclear vendor commitments

## Best-Practice Themes Reflected In The Sources

- Lifecycle governance and re-review, not one-time approval
- Practical, scalable governance rather than theory alone
- Cross-functional governance and AI literacy
- Risk-tiered depth and documentation discipline
- Transparency, user awareness, and meaningful human oversight
- Iterative learning, monitoring, and accountability

## Sources Consulted

- Ohio State Moritz College of Law, Responsible AI framework and Responsible AI management materials:
  - https://moritzlaw.osu.edu/responsible-ai-framework-understanding-ai-law-ethics-and-governance
  - https://moritzlaw.osu.edu/program-data-and-governance-releases-new-report-responsible-ai-management
  - https://moritzlaw.osu.edu/PDG
- World Economic Forum, *Advancing Responsible AI Innovation: A Playbook*:
  - https://reports.weforum.org/docs/WEF_Advancing_Responsible_AI_Innovation_A_Playbook_2025.pdf
- IAPP AI governance materials:
  - https://iapp.org/certify/aigp//
  - https://iapp.org/resources/article/ai-governance-profession-report//
  - https://iapp.org/l/aigp-study-guide-request/
  - https://iapp.org/about/ai-governance-center/

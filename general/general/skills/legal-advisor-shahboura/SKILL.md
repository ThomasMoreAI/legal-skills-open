---
name: legal-advisor-shahboura
title: Legal Advisor Skill
description: Legal research, jurisdiction-aware analysis, regulatory compliance, case evaluation, license auditing, and structured legal findings. Use for legal questions involving specific countries, situations, regulations, contracts, IP, or compliance frameworks.
author: shahboura
author_url: https://github.com/shahboura/agents-opencode/tree/main/.opencode/skills/legal-advisor
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal Advisor Skill

## When to Activate

Activate this skill when:
- Answering legal questions tied to a specific country or jurisdiction
- Analyzing a case, situation, or scenario against applicable law
- Reviewing regulatory compliance (privacy, financial, employment, environmental, etc.)
- Evaluating contracts, agreements, or legal terms
- Auditing dependency licenses for compatibility and obligations
- Assessing data handling against privacy regulations
- Screening for export control or sanctions exposure
- Analyzing copyright, trademark, or IP ownership questions

## Research Methodology

### IRAC Framework

Apply the Issue-Rule-Application-Conclusion framework for structured legal analysis:

1. **Issue:** Frame the precise legal question. Avoid vague or compound questions.
2. **Rule:** Identify governing statutes, regulations, case law, and principles. Cite specific provisions with source references.
3. **Application:** Apply the rules to the specific facts. Address counterarguments and edge cases.
4. **Conclusion:** Provide a reasoned assessment. State confidence level (high / moderate / tentative) and note information gaps.

### Source Hierarchy

Evaluate sources by authority, in descending order:
- **Binding:** Constitution, statutes, regulations, supreme court decisions
- **Persuasive:** Lower court decisions, decisions from other jurisdictions, obiter dicta
- **Guidance:** Regulatory body publications, official interpretations, advisory opinions
- **Commentary:** Law review articles, treatises, practitioner guides

Always prefer official government sources over secondary summaries. Note when sources may be outdated, repealed, or overruled.

Reference: `references/research-methodology.md` for detailed source evaluation guidance.

## Jurisdiction Framework

Legal systems fall into broad categories that shape research approach:

- **Common Law:** Case law and judicial precedent are primary. Statutes interpreted by courts.
- **Civil Law:** Codified statutes are primary. Case law is persuasive but not binding.
- **Mixed/Hybrid:** Elements of both common and civil law traditions.
- **Religious Law:** Religious texts or principles inform the legal framework.
- **Supranational:** EU law, international treaties — may override national law in member states.

Reference: `references/jurisdictions/` for per-country legal system profiles — load only the file needed for the jurisdiction at hand.

## License & Compliance Checks

### License Compatibility Audit
1. Identify all dependencies and their declared licenses
2. Cross-reference against the license compatibility matrix
3. Flag incompatible, unlicensed, or restricted dependencies
4. Document attribution and source-disclosure requirements
5. Recommend alternatives for problematic dependencies

### Data Privacy Assessment
1. Identify data types handled (PII, financial, health, etc.)
2. Map applicable regulations by jurisdiction
3. Review data flows: collection → storage → processing → sharing
4. Flag missing safeguards and consent mechanisms
5. Recommend privacy-by-design improvements

### Export Control Screening
1. Identify encryption-related code and ECCN classification
2. Check for dependencies with export restrictions
3. Flag geographic restrictions on distribution or use

## Common License Obligations

### Permissive (MIT, Apache-2.0, BSD)
- Include copyright notice and license text with distribution
- Apache-2.0 requires NOTICE file for modifications

### Copyleft (GPL, AGPL, LGPL)
- GPL: Derivative works must also be GPL-licensed
- AGPL: Network/SaaS use triggers copyleft obligations
- LGPL: Library linking from proprietary code is permitted

### Source-Available (BSL, SSPL, Elastic)
- BSL: Converts to open-source after a specified period
- SSPL: Requires release of service management infrastructure code
- Elastic-2.0: Restricts use for managed/hosted services

## Quick Reference

- [references/license-matrix.md](references/license-matrix.md) — Complete SPDX license compatibility matrix
- [references/privacy-checklists.md](references/privacy-checklists.md) — GDPR, CCPA, HIPAA compliance checklists
- [references/export-control.md](references/export-control.md) — Export control and sanctions guidance
- [references/jurisdictions/](references/jurisdictions/) — Per-country legal system profiles and official sources:
  - `united-states.md`, `united-kingdom.md`, `canada.md`, `australia.md`, `india.md`
  - `european-union.md`, `germany.md`, `france.md`, `japan.md`, `brazil.md`, `china.md`
  - `south-africa.md`, `scotland.md`, `quebec.md`, `saudi-arabia.md`, `united-arab-emirates.md`, `malaysia.md`
  - `international.md` — International treaty and court resources
- [references/research-methodology.md](references/research-methodology.md) — IRAC framework and source evaluation

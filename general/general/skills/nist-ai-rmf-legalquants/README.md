# NIST AI Risk Management Framework — Claude Skill

Apply the **NIST AI Risk Management Framework** (NIST AI 100-1 + the NIST AI 600-1 Generative AI Profile) to a specific AI system, governance question, or impact assessment — quoting Subcategories (`GOVERN 1.1`) and Profile Action IDs (`GV-1.2-001`) verbatim from the published NIST text.

This is the standalone-skill distribution. Upload the zipped folder to Claude Cowork (desktop app) or any other host that accepts standalone skill ZIPs. The skill activates automatically on prompts that mention the AI RMF, the four functions (Govern / Map / Measure / Manage), the trustworthy AI characteristics, or the 12 GAI Profile risks.

## Three modes

The skill picks a mode automatically from the user's question:

- **Consult** — fast lookup. *"What should I do per the AI RMF for this AI system?"* Returns applicable risks (for GenAI) and the relevant Suggested Actions / Subcategories, quoted verbatim.
- **Governance plan** — structured plan around the GOVERN function. *"What should our governance plan include per the AI RMF?"*
- **Assessment** — full RMF-aligned impact assessment walking Govern, Map, Measure, Manage end-to-end. *"Run a NIST AI RMF impact assessment for our HR resume-screening tool."*

## Example prompts

```
What does the NIST AI RMF say about a customer-service chatbot built on GPT-4?
Run a NIST AI RMF assessment for our HR resume-screening tool.
What should our governance plan include per the NIST AI RMF?
```

## Provenance

Every Subcategory ID and Action ID in the output is **byte-identical** to the source NIST publication. Applicability calls, operational glosses, role-ownership suggestions, and final recommendations are tagged inline as `[model judgment — verify against system specifics]`. If a citation does not resolve to a real line in `references/`, that is a bug — not a feature.

## Sources

- **NIST AI 100-1** — AI Risk Management Framework 1.0 (January 2023). Public-domain U.S. Government work. Authoritative source: <https://www.nist.gov/itl/ai-risk-management-framework>.
- **NIST AI 600-1** — AI RMF: Generative AI Profile (July 2024). Public-domain U.S. Government work. Authoritative source: <https://www.nist.gov/itl/ai-risk-management-framework>.

The verbatim extracts in `references/core/` and `references/gai-profile/` are the runtime source of truth. To re-verify any citation, download the originals and compare.

## Limitations

- The framework is **non-binding** voluntary NIST guidance, not regulation. Mandatory regimes (EU AI Act, NYC LL 144, Colorado AI Act, sector rules) impose actual obligations that may track NIST — or may not. The skill flags the divergence; it does not replace the analysis.
- Sources are frozen at the publication dates above. When NIST publishes a revision, the references need re-extraction.
- The GAI Profile assumes generative AI. Applying its actions to a non-generative system creates noise — the skill explicitly avoids this.
- This is not a substitute for legal counsel.

## License

[MIT](LICENSE) for the skill code. The NIST publications themselves are works of the U.S. Government and are not subject to copyright protection under 17 U.S.C. § 105 — they remain public domain regardless of this skill's license.

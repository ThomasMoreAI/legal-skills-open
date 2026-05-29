# Screening Alert Adjudication

A deterministic, criteria-driven skill for adjudicating screening hits against sanctions lists, PEP lists, adverse-media sources, and similar watchlists. Designed to auto-clear obvious false positives and confirm obvious true positives, leaving genuinely ambiguous cases for human review with a full evidence package.

Built as a [Claude Skill]((https://docs.claude.com/en/docs/claude-code/skills)) using the [Agent Skills]((https://agentskills.io/)) open standard.

## What this does

When a screening system flags a name as a possible match against a watchlist, an analyst typically has to decide whether the match is real (true positive), spurious (false positive), or needs more investigation. A large share of these alerts are obviously bad matches — wrong entity type, common names with no overlap on identifiers, partial-name matches that ignore naming conventions — but analysts spend significant time clearing them anyway.

This skill applies a deterministic decision tree to each alert and reaches one of three outcomes:

- **True positive** — the screened party is the listed party
- **False positive** — the screened party is not the listed party
- **Escalate** — evidence is insufficient to deterministically conclude either way; hand off to a human with the full evidence record

## Design properties

Two properties are non-negotiable:

1. **Determinism.** Given identical evidence, the skill reaches an identical conclusion. The skill never weighs probabilities or hedges with "appears to be" / "probably is" language. A rule either fires or it doesn't.
2. **Conservatism.** Escalation is the safe default. No rule fires unless every one of its preconditions is satisfied. Better to escalate a clear case than to wrongly clear an ambiguous one.

Every adjudication produces a structured JSON record and a human-readable narrative, both derived from the same underlying state. The JSON is for system ingestion, QC sampling, and cross-case querying. The narrative is for analyst review and case files.

## How it's organized

Adjudication runs through tiers, with each tier escalating token spend. Earlier tiers exit as soon as they can.

- **Tier 0** — Parse and normalize. Detects script, language, naming convention; identifies anchor vs. non-anchor name components; inventories identifiers and aliases. No determinations.
- **Tier 1** — Hard false-positive triggers (no web access): type mismatch, name-role mismatch (e.g., "Jose Andrea" matched against "Jose Andrea Coronado"), hard DOB contradiction.
- **Tier 2** — Structured identifier corroboration (no web access): government ID matches, full identity triangulation, identifier mismatches.
- **Tier 3** — Targeted external research with a four-rung language ladder (native-script → native-language Latin → English regional → transliteration variants), source-ranked (only primary/major-news sources drive determinations), capped at 8 page retrievals per case.

A separate reference covers naming conventions across Hispanic, Portuguese, Arabic, Persian, Russian, East Asian, Japanese, Indonesian/Burmese, and Western-default forms. Another covers transliteration variants across scripts. A third covers historical place-name equivalences (Leningrad/St. Petersburg, Bombay/Mumbai, Persia/Iran, etc.).

## Repository structure

```
screening-alert-adjudication/
├── SKILL.md                              # Orchestrator — read this first
├── references/
│   ├── tier-0-parsing.md                 # Name parsing, convention classification
│   ├── tier-1-rules.md                   # FP-1, FP-2, FP-3
│   ├── tier-2-rules.md                   # TP-1, TP-2, Escalate-2, FP-5, FP-6
│   ├── tier-3-research.md                # Web research procedure, TP-3, FP-7
│   ├── naming-conventions.md             # Anchor/non-anchor per convention
│   ├── transliteration-variants.md       # Cross-script variant patterns
│   ├── place-name-equivalences.md        # Historical city/country renamings
│   └── output-schema.md                  # JSON schema and narrative format
├── evals/
│   └── evals.json                        # Test cases covering main decision paths
├── LICENSE
└── README.md
```

## Installing

This skill is in [Claude Skills format](https://docs.claude.com/en/docs/claude-code/skills). To use it:

1. Clone or download this repository.
2. Package it into a `.skill` file (a renamed zip): `zip -r screening-alert-adjudication.skill screening-alert-adjudication/ -x "*/evals/*"`.
3. Upload via your Claude environment's skill installation flow, or place it in the appropriate skills directory for your setup.

You can also use the skill content directly with any LLM that supports Anthropic-style skills, or adapt the reference files as standalone documentation for analyst training.

## Out of scope (by design, in v1)

- **Sectoral ownership analysis (OFAC 50% rule and equivalents).** The skill flags ownership-chain matches for human review.
- **Adverse-media conduct assessment.** The skill confirms identity match in a media item but does not assess whether the conduct is relevant risk.
- **PEP risk grading.** Identity match yes; risk disposition no.
- **Score tuning feedback.** Adjudication records can feed score tuning later, but that's a separate analysis.
- **Vessel and aircraft deep-dives.** Type-mismatch FPs are handled; IMO chains and name-change-but-same-IMO cases are not.

## Disclaimer

This tool is provided for testing, research, and educational purposes only. It is not a sanctions screening system, does not constitute legal, regulatory, or compliance advice, and is not a substitute for an independent sanctions compliance program or the judgment of a qualified compliance professional. Outputs are heuristic and may contain errors, omissions, or inaccuracies, including in name parsing, identifier comparison, and language-aware research. Users are solely responsible for their own regulatory obligations and for independently validating any output before relying on it for any compliance, business, or operational decision. No warranty of accuracy, completeness, fitness for a particular purpose, or regulatory sufficiency is made or implied. Sanctrust and the contributors disclaim all liability arising from use of this tool to the fullest extent permitted by law.

Sanctions and financial-crime compliance are regulated activities. Use of this skill does not constitute legal advice and does not create a sanctions compliance program. Institutions remain fully responsible for their compliance obligations.

## Author

Built by [Sanctrust](https://sanctrust.com), an AI-native sanctions and financial-crime compliance advisory firm.

## License

[MIT](LICENSE)

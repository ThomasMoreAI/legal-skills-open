# Changelog

All notable changes to the privacy-compliance skill are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] — 2026-06-23

### Added

- **Initial release** — replaces `gdpr-compliance-expert` (SKILL.md only) with a
  comprehensive global privacy compliance skill.
- **12 structured compliance workflows:**
  - GDPR Compliance Baseline (`workflow-1`)
  - DPIA Execution (`workflow-2`)
  - DPA Agreement Drafting (`workflow-3`)
  - CCPA/CPRA Compliance (`workflow-4`)
  - Breach Notification Procedure (`workflow-5`)
  - HIPAA Privacy Rule Assessment (`workflow-6`)
  - EU AI Act Requirements (`workflow-7`)
  - Cross-Border Data Transfer Mechanisms (`workflow-8`)
  - PII Identification and Classification (`workflow-9`)
  - Consent Management Review (`workflow-10`)
  - Privacy-by-Design Architecture Review (`workflow-11`)
  - Data Subject Access Request (DSAR) Handling (`workflow-12`)
- **Expanded jurisdiction coverage:** GDPR (EU/EEA), UK GDPR, CCPA/CPRA
  (California), HIPAA Privacy Rule (US Federal), LGPD (Brazil), EU AI Act.
- **Cross-border transfer mechanisms:** SCCs, BCRs, EU-US DPF, UK IDTA, Transfer
  Impact Assessment (TIA) procedure.
- **PII classification taxonomy:** Direct identifiers, indirect identifiers,
  sensitive PII, pseudonymous data, anonymous data.
- **Privacy-by-design pattern library:** 9 architectural patterns.
- **Consent dark pattern detection:** 8 anti-patterns with regulatory references.
- **Multi-regulation DSAR handling:** GDPR, CCPA/CPRA, HIPAA, LGPD comparison and
  procedure.
- **Validation script:** `scripts/validate_skill.py` for structural validation of
  frontmatter, sections, and file completeness.
- **Evaluation test cases:** `evals/test_cases.json` with 5+ structured test scenarios.
- **Quick-reference document:** `references/privacy-regulations.md` covering all
  supported regulations.
- **Safety rules:** 8 absolute rules including no PII exposure, no legal advice,
  no legal document drafting for execution.
- **Platform compatibility notes:** Coverage for Claude Code, Codex, Cursor, Gemini
  CLI, OpenClaw, GitHub Copilot, Windsurf, and OpenCode.
- **Prominent disclaimer:** THIS IS NOT LEGAL ADVICE — procedural knowledge only.

### Changed

- N/A (initial release)

### Deprecated

- N/A (initial release)

### Removed

- N/A (initial release)

### Fixed

- N/A (initial release)

### Security

- Added rule prohibiting exposure of actual PII in agent outputs.
- Added guidance on redaction of PII in test data, logs, and examples.

---

## Comparison with `gdpr-compliance-expert`

The `privacy-compliance` skill (v1.0.0) supersedes the original
`gdpr-compliance-expert` skill.

| Aspect | gdpr-compliance-expert | privacy-compliance |
|---|---|---|
| **Workflows** | None (principles only) | 12 structured workflows |
| **Jurisdictions** | GDPR, CCPA (basic) | GDPR, UK GDPR, CCPA/CPRA, HIPAA, LGPD, EU AI Act |
| **Cross-border transfers** | Not covered | SCCs, BCRs, EU-US DPF, UK IDTA + TIA |
| **PII classification** | Not covered | 5-tier taxonomy with detection framework |
| **Consent management** | Basic principles | Comprehensive checklist + dark pattern detection |
| **Privacy-by-design** | Not covered | 6-layer review + 9 architectural patterns |
| **DSAR handling** | Not covered | Multi-regulation comparison + full procedure |
| **Breach notification** | Not covered | Multi-jurisdiction procedure + decision tree |
| **Validation script** | None | `scripts/validate_skill.py` |
| **Test cases** | None | `evals/test_cases.json` (5+ cases) |
| **Reference document** | None | `references/privacy-regulations.md` |
| **Safety rules** | Implicit | 8 explicit absolute rules |
| **Disclaimer** | None | Prominent NOT LEGAL ADVICE disclaimer |
| **Platform notes** | None | 8 platforms |
## v1.0.1 — 2026-07-02
- Added 3 near-miss negative eval cases (contract law, ransomware recovery, generic template)
- Eval suite now 7 positive + 3 near-miss negatives = 10 cases

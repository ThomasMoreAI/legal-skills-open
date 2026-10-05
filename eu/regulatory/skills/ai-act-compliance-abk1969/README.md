# ai-act-compliance

> Authoritative **multi-platform** agent skill for **EU AI Act (Regulation 2024/1689)** compliance — strictly aligned with **ISO/IEC 42001:2023** (AIMS) and **ISO/IEC 27090:2025** (AI cybersecurity). Runs natively on **Claude Code**, **Gemini CLI**, and **OpenAI Codex**.

[![EU AI Act](https://img.shields.io/badge/EU_AI_Act-2024%2F1689-1f4e79)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
[![ISO 42001](https://img.shields.io/badge/ISO%2FIEC-42001%3A2023-0066b3)](https://www.iso.org/standard/81230.html)
[![ISO 27090](https://img.shields.io/badge/ISO%2FIEC-27090%3A2025-0066b3)](https://www.iso.org/standard/56581.html)
[![Claude Code](https://img.shields.io/badge/Claude_Code-supported-7c3aed)](https://claude.com/claude-code)
[![Gemini CLI](https://img.shields.io/badge/Gemini_CLI-supported-1a73e8)](https://github.com/google-gemini/gemini-cli)
[![Codex](https://img.shields.io/badge/OpenAI_Codex-supported-10a37f)](https://openai.com/codex)

## What this skill does

Provides decision-support for AI Act compliance work, with every output traceable to:

- **Regulation (EU) 2024/1689** — the AI Act itself (the legally binding source)
- **ISO/IEC 42001:2023** — AI Management System (AIMS), the certifiable management standard
- **ISO/IEC 27090:2025** — Cybersecurity guidance for AI (depth standard for art. 15)
- **Companion ISO standards**: 23894 (risk mgmt), 23053 (ML framework), 5338 (lifecycle), 5259-* (data quality), 24029-2 (robustness), 42005 (impact assessment), 42006 (audit & certification)
- **CEN-CENELEC JTC 21** harmonised standards under standardization mandate M/593

## When to use

Invoke when the conversation involves any of:

- Risk classification (art. 5 prohibited / art. 6 + Annex III high-risk / art. 50 limited)
- Conformity assessment for high-risk AI systems (arts. 8–15, 40–49)
- Annex IV technical documentation
- Fundamental Rights Impact Assessment (art. 27 FRIA)
- Quality Management System for AI providers (art. 17, ISO 42001)
- AI cybersecurity (art. 15, Recital 76, ISO 27090)
- Transparency obligations (art. 50 — chatbots, generative content, deepfakes)
- Post-market monitoring (art. 72)
- Serious incident reporting (art. 73)
- General-Purpose AI obligations (arts. 51–55) + Code of Practice (art. 56)
- AI literacy programmes (art. 4 — in force since **2025-02-02**)
- Substantial-modification detection / provider-flip (art. 25, art. 43(4))
- Regulatory sandboxes (art. 57–59) and real-world testing (art. 60–63)
- Voluntary codes of conduct (art. 95) and right to explanation (art. 86)
- Sanctions (art. 99) and timeline (art. 113)
- Mapping AI Act articles to ISO 42001 / ISO 27090 controls

**Do NOT use for**:
- General data protection (GDPR — separate regime; consider a dedicated GDPR skill)
- Generic ISO 27001 ISMS work — the `iso27001` skill is more appropriate
- Non-EU AI regulations (NIST AI RMF, UK approach, etc.)

## Structure

```
ai-act-compliance/
├── SKILL.md                              # Entry point — triggers, taxonomy, decision tree, SSL scenes
├── ssl.json                              # Machine-readable Scheduling-Structural-Logical manifest
├── README.md                             # This file
├── LICENSE                               # MIT
├── package.json                          # For skills.sh marketplace
└── references/
    ├── 01-risk-classification.md         # 4-tier rubric + 14-signal questionnaire + edge cases
    ├── 02-high-risk-obligations.md       # Provider + deployer obligations across arts. 8-29, 40-49
    ├── 03-iso-42001-aims.md              # Full clauses 4-10 + 38 Annex A controls + companions + cert
    ├── 04-iso-27090-ai-security.md       # Threat taxonomy + mitigations + GenAI annex + adjacent stds
    ├── 05-crosswalk-aiact-iso.md         # The big mapping table — every art. → 42001 + 27090 + companions
    ├── 06-techdoc-annex-iv.md            # Annex IV technical file template
    ├── 07-fria-art27.md                  # FRIA template + ISO 42005 alignment
    ├── 08-transparency-art50.md          # Disclosure UX + watermarking + C2PA
    ├── 09-post-market-art72-73.md        # PMM plan + incident reporting playbook
    ├── 10-gpai-and-timeline.md           # GPAI arts. 51-55, sanctions art. 99, timeline art. 113
    ├── 11-art4-ai-literacy.md            # AI literacy programme (art. 4 — in force since 2025-02-02)
    ├── 12-art25-substantial-modification.md  # Provider-flip detection + foundation-model fine-tuning
    ├── 13-sandboxes-and-real-world-testing.md  # Art. 57–63 (regulatory sandboxes + art. 60 testing)
    ├── 14-codes-and-right-to-explanation.md   # Art. 56 GPAI Code of Practice + art. 95 voluntary + art. 86
    └── 15-platform-compatibility.md           # Multi-platform install + activation (CC / Gemini / Codex)
```

In addition to `SKILL.md`, the skill ships two host-specific discovery
files for non-Claude-Code runtimes:

- `AGENTS.md` — read by OpenAI Codex and other AGENTS-aware harnesses
- `GEMINI.md` — read by Gemini CLI to surface the skill at session start

The entry point (`SKILL.md`) routes to the right reference based on the user's intent. Each reference is self-contained and includes a practical output template.

### Machine-readable companion (`ssl.json`)

`ssl.json` is a **Scheduling-Structural-Logical (SSL) manifest** built per Liang et al., *From Skill Text to Skill Structure* (arXiv:2604.24026, 2026). It exposes three layers:

- **Scheduling layer** — `skill_id`, `skill_goal`, `intent_signature`, `tags`, `top_pattern`, `expected_inputs/outputs`, `dependencies`, `control_flow_features`, `entry_scene_id`, `subscenes`. Used by registries and routers for skill discovery without re-parsing SKILL.md.
- **Structural layer** — 7 typed scenes (`PREPARE`, `ACQUIRE`, `REASON`, `ACT`, `VERIFY`, `RECOVER`, `FINALIZE`) with explicit input/output data contracts and `next_scene_rules` transitions.
- **Logical layer** — 28 atomic logic steps with closed `act_type` and `resource_scope` vocabularies, `actor`, `instrument`, `preconditions`, `effects`, and `next_step_rules`. Useful for pre-execution risk review.

The manifest is **derived from and grounded in** SKILL.md and references (per paper § 5.2: "SSL should not replace the source document"). It complements rather than substitutes the human-readable content. The skill declares **no network access, no credentials access, no code execution, no external tool calls** — `touches_sensitive_resources: false`.

## Installation

### Claude Code

```bash
# Via the skills.sh CLI (recommended)
npx skills add abk1969/ai-act-skills@ai-act-compliance -g -y

# Manual (macOS / Linux)
git clone https://github.com/abk1969/ai-act-skills
cp -R ai-act-skills/skills/ai-act-compliance ~/.claude/skills/

# Manual (Windows PowerShell)
git clone https://github.com/abk1969/ai-act-skills
xcopy ai-act-skills\skills\ai-act-compliance $env:USERPROFILE\.claude\skills\ai-act-compliance /E /I
```

Then reload Claude Code's skill index:

```
/reload-plugins
```

### Gemini CLI

```bash
# macOS / Linux
git clone https://github.com/abk1969/ai-act-skills
mkdir -p ~/.gemini/skills/
cp -R ai-act-skills/skills/ai-act-compliance ~/.gemini/skills/
```

```powershell
# Windows
git clone https://github.com/abk1969/ai-act-skills
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.gemini\skills" | Out-Null
xcopy ai-act-skills\skills\ai-act-compliance $env:USERPROFILE\.gemini\skills\ai-act-compliance /E /I
```

Gemini reads `GEMINI.md` at session start and activates the skill via
`activate_skill` when the user's question matches one of the 14 intent
signatures listed in `ssl.json`.

### OpenAI Codex

```bash
# macOS / Linux
git clone https://github.com/abk1969/ai-act-skills
mkdir -p ~/.agents/skills/
cp -R ai-act-skills/skills/ai-act-compliance ~/.agents/skills/
```

```powershell
# Windows
git clone https://github.com/abk1969/ai-act-skills
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills" | Out-Null
xcopy ai-act-skills\skills\ai-act-compliance $env:USERPROFILE\.agents\skills\ai-act-compliance /E /I
```

Codex follows the `AGENTS.md` convention — the top-level `AGENTS.md`
in this repo declares the skill, and Codex picks it up at session
start.

The skill name `ai-act-compliance` will appear in the available skills
list and auto-trigger on relevant questions on **all three** platforms.
Full activation matrix and smoke-test procedure:
[`references/15-platform-compatibility.md`](./references/15-platform-compatibility.md).

## Why ISO 42001 + 27090 (and not ISO 27001)?

Many AI compliance efforts mistakenly anchor on ISO 27001 (generic information security management). This skill is uncompromising on the alignment:

- **ISO/IEC 42001:2023** (AIMS) is the **AI-specific** management standard. It includes AI-specific clauses (cl. 6.1.4 AI system impact assessment) and Annex A controls (A.5 impact, A.6 lifecycle, A.7 data, A.8 information for parties, A.9 use, A.10 third parties) that ISO 27001 does not cover.
- **ISO/IEC 27090:2025** is the **AI-specific cybersecurity** depth standard. Its threat taxonomy directly maps to AI Act art. 15(5) Recital 76 named threats: data poisoning, model poisoning, model evasion, confidentiality attacks, model flaws.
- ISO 27001 remains useful as the **org-level ISMS baseline** that 42001 + 27090 build upon — but it is NOT the AI-specific framework for AI Act conformity.

CEN-CENELEC JTC 21 (under standardization mandate M/593) is on a path to publish **EN ISO/IEC 42001 / 23894 / 27090** as harmonised standards conferring AI Act art. 40 presumption of conformity. This skill anticipates that path.

## Quality bar

This skill is built to be **operational and rigorous**, not introductory. It assumes:

- Familiarity with regulatory terminology (provider, deployer, conformity assessment, harmonised standards, OJEU)
- Working knowledge of management-system standards (Annex SL HLS, Statement of Applicability, internal audit)
- Access to authoritative source documents when binding interpretation is needed (the regulation itself, ISO standards, Commission acts)

Every claim cites the specific article, clause, or control number. Where the standard is silent or under development (e.g., harmonised-standard OJEU citations as of July 2026), the skill says so explicitly.

## Limitations & legal notice

This skill is **decision-support only**, not legal advice. Final conformity assessment requires:

- **Qualified counsel** for binding interpretation
- **Notified body** for conformity assessment of high-risk AI systems (where Annex VII path applies under art. 43)
- **Accredited certification body** for ISO/IEC 42001 certification

The author is not responsible for compliance decisions made on the basis of this skill's outputs. Use it to structure your work, not to substitute for professional review.

## Related skills

- [`iso27001`](https://github.com/lawvable/awesome-legal-skills) — for the org-level ISMS baseline that 42001 + 27090 assume
- [`legal-risk-assessment`](https://skills.sh/anthropics/knowledge-work-plugins/legal-risk-assessment) — adjacent for general legal risk
- [`gdpr-data-handling`](https://skills.sh/wshobson/agents/gdpr-data-handling) — for the privacy regime that intersects with AI Act art. 10 (data) and art. 26(8) (DPIA coordination with FRIA)
- [`documentation`](https://skills.sh/) — for drafting Annex IV technical files in long form
- [`c4-architecture`](https://skills.sh/), [`mermaid-diagrams`](https://skills.sh/), [`uml`](https://skills.sh/) — for system architecture diagrams required by Annex IV §2(b)(c)
- [`example-skills:docx`, `:pdf`, `:xlsx`](https://github.com/anthropics/skills) — for producing compliance deliverables (FRIA reports, risk registers, declarations of conformity)

## Standards tracked

| Standard | Status (as of July 2026) | Role in this skill |
|----------|---------------------------|--------------------|
| Regulation (EU) 2024/1689 (AI Act) | In force; amended by the 2026 AI Omnibus (Annex III high-risk 2027-12-02, Annex I 2028-08-02; OJ publication pending as of 2026-07-14) | Primary source |
| 2026 AI Omnibus amendment | Adopted (Parliament 2026-06-16, Council 2026-06-29); OJ publication expected July 2026 | Timeline + art. 5 amendment source |
| GPAI Code of Practice (art. 56) | Published 2025-07-10; adequacy confirmed 2025-08-01 | Operative GPAI compliance instrument |
| ISO/IEC 42001:2023 | Published; certifiable | Primary AIMS standard |
| ISO/IEC 27090:2025 | Published; informative | Primary AI security standard |
| ISO/IEC 23894:2023 | Published; informative | AI risk management depth |
| ISO/IEC 23053:2022 | Published | ML framework + terminology |
| ISO/IEC 5338:2023 | Published | AI lifecycle processes |
| ISO/IEC 5259-1 to -5 | Published / partly published | Data quality for AI |
| ISO/IEC 24029-1, -2 | Published; -3 forthcoming | NN robustness assessment |
| ISO/IEC TS 4213:2022 | Published | Classification model performance |
| ISO/IEC 25059 | Published | Quality model for AI |
| ISO/IEC 42005:2025 | Published | AI system impact assessment depth |
| ISO/IEC 42006:2025 | Published | Audit & certification body requirements |
| EN ISO/IEC 42001 / 23894 / 5259 / 24029-2 / 27090 | Under development by CEN-CENELEC JTC 21 | Harmonised standards path (art. 40) |
| Commission delegated/implementing acts | Various stages | Tracked via art. 7, 11(3), 27(5), 41, 51(3), 56, 71(4), 72(3), 73(7) |

## Versioning

This skill version: **2.0.0**

Changelog:

- **2.0.0** — Regulatory content update to the post-Omnibus AI Act: 2026 AI Omnibus amendment (Annex III high-risk deferred to 2027-12-02, Annex I to 2028-08-02, new art. 5 NCII/CSAM prohibition applicable 2026-12-02, art. 50(2) marking grace period, sandboxes deferred to 2027-08-02, machinery carve-out, art. 4 wording softened); GPAI Code of Practice operative status (published 2025-07-10, three chapters, adequacy 2025-08-01) + Commission GPAI guidelines and training-data-summary template; JTC 21 harmonised-standards acceleration (prEN 18228 / prEN 18284, Q4 2026); Commission draft guidance landed (art. 6 classification 2026-05-19; art. 73 incident reporting + template 2025-09-26). Major bump per versioning legend (AI Act amendment).
- **1.2.0** — Multi-platform compatibility: native support for Claude Code, Gemini CLI, and OpenAI Codex via host-specific discovery files (`AGENTS.md`, `GEMINI.md`) at root + skill level. New `references/15-platform-compatibility.md` documents the activation matrix. `package.json` declares `platforms` and per-platform install paths. Skill content (regulatory expertise, ISO anchors) unchanged — only discovery and packaging extended.
- **1.1.0** — SSL representation added (`ssl.json`); SKILL.md restructured into 7 typed SSL scenes; description tightened per writing-skills CSO rules; 4 new reference files added (art. 4 AI literacy, art. 25 substantial modification, art. 57–63 sandboxes & real-world testing, art. 56/95/86 codes & right to explanation).
- **1.0.0** — Initial release.

Update triggers:
- Major: AI Act amendment (delegated act under art. 7), new Commission implementing act
- Minor: New ISO standard publication, JTC 21 OJEU citation, SSL schema upgrade
- Patch: Editorial corrections, structure improvements

## Contributing

If you spot regulatory drift (e.g., a Commission act lands, ISO publishes a new standard, JTC 21 cites EN ISO/IEC 42001 in OJEU), please open a PR.

## License

MIT — see `LICENSE`.

## Author

Built for the **AI Act Navigator** project — codifying compliance expertise from a production AI Act compliance platform with 30+ services, full 113-article indexing, and 5-stage multi-agent regulatory monitoring pipeline.

---

> *This skill is decision-support, not legal advice. Final AI Act conformity determination requires qualified counsel and, for most high-risk systems, a notified body.*

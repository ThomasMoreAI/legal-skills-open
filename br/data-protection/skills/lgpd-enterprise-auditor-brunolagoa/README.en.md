# LGPD Enterprise Auditor

<p align="center">
  <img src="./assets/logo-lgpd-enterprise-auditor.webp" alt="LGPD Enterprise Auditor Logo" width="355" />
</p>

<p align="center">
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor/stargazers"><img src="https://img.shields.io/github/stars/BrunoLagoa/lgpd-enterprise-auditor?style=social" alt="GitHub stars" /></a>
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/latest"><img src="https://img.shields.io/github/v/release/BrunoLagoa/lgpd-enterprise-auditor" alt="Release" /></a>
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor/actions/workflows/install.yml"><img src="https://github.com/BrunoLagoa/lgpd-enterprise-auditor/actions/workflows/install.yml/badge.svg" alt="CI" /></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License MIT" /></a>
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor"><img src="https://hits.sh/github.com/BrunoLagoa/lgpd-enterprise-auditor.svg?label=Project%20views&color=f1c40f" alt="Project views" /></a>
</p>

<!-- README-I18N:START -->

[Português (Brasil)](./README.md) | **English**

<!-- README-I18N:END -->


An evidence-driven LGPD auditing framework focused on security, governance, and AI usage in software engineering.

This project was designed to operate as an auditable and modular system, ready to be reused across products and teams.

**In short:** install the auditor into your project with one command, run `/lgpd-saas` (or another scenario) in your AI assistant, and get a report with a 0–100 score, non-conformities with the LGPD article and the evidence for each, and a remediation plan with deadlines and effort. Works with Claude Code, Cursor, VS Code + GitHub Copilot, OpenCode, Codex and Gemini CLI.

You choose the report format at the start of the audit: `.md` (full text, good for versioning and comparing), `.html` (to read in the browser, with the score up front, filters, search and a print version) or both. The `.html` is a single file, works offline and loads nothing from outside.

See an example report (in Portuguese), produced on a fictional SaaS, in both formats:

- [Markdown report (`.md`)](./examples/saas-demo/relatorio-auditoria-lgpd.md): opens right here on GitHub.
- [HTML report (`.html`)](./examples/saas-demo/relatorio-auditoria-lgpd.html): download the file and open it in your browser. The image below shows the top of it.

[![Example HTML report: score 20 out of 100, classification, non-conformities by severity and executive summary](./examples/saas-demo/relatorio-auditoria-lgpd.png)](./examples/saas-demo/relatorio-auditoria-lgpd.html)

## What this project is

`lgpd-enterprise-auditor` is a framework that combines:

- legal auditing (LGPD + ANPD);
- technical auditing (appsec, cloud, mobile, devsecops, AI/LLM);
- severity and scoring model;
- standardized reporting format;
- practical commands for scenario-based execution.

In practice, it enables complete or targeted audits with consistent criteria, evidence, and remediation planning.

## Installation

One interactive command, run from the root of the project you want to audit. It asks which AI tool you use and whether to also install the skill, shows a summary and installs everything **locally, inside that project** (there is no global install).

**macOS / Linux / WSL / Git Bash**

```bash
curl -fsSL https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/latest/download/install.sh | bash -s -- install
```

**Windows (PowerShell)**

```powershell
powershell -ExecutionPolicy Bypass -Command "iwr https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/latest/download/install.ps1 -OutFile $env:TEMP\lgpd-install.ps1; & $env:TEMP\lgpd-install.ps1 install"
```

Prefer to read the script before running it? Download it (`curl -fsSL <url> -o install.sh`), review it, then run `bash install.sh install`.

The commands above download the installer from the latest release, the same version of the framework it installs. The installer uses the latest published version. If it cannot look it up (no network or GitHub API rate limit), it warns and does not install the `main` branch on its own: in interactive mode it asks first; with `--non-interactive` it stops and asks for `--version`.

**Checking integrity.** Releases from v1.6.0 onward publish `install.sh`, `install.ps1` and `SHA256SUMS`. To install an exact version and check the file before running it:

```bash
V=vX.Y.Z   # the version you want
curl -fsSLO "https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/download/${V}/install.sh"
curl -fsSLO "https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/download/${V}/SHA256SUMS"
shasum -a 256 --ignore-missing -c SHA256SUMS   # on Linux: sha256sum --ignore-missing -c SHA256SUMS
bash install.sh install --version "$V"
```

### Where files land

The framework (`.agents/lgpd-enterprise-auditor/`) is the same for every tool; only the commands and the optional skill change place:

| Tool (`--target`) | Commands | Skill (optional) |
|---|---|---|
| `claude` — Claude Code | `.claude/commands/lgpd-*.md` | `.claude/skills/lgpd-enterprise-auditor/` |
| `cursor` — Cursor | `.cursor/commands/lgpd-*.md` | `.agents/skills/lgpd-enterprise-auditor/` |
| `vscode` — VS Code + GitHub Copilot | `.github/prompts/lgpd-*.prompt.md` | `.agents/skills/lgpd-enterprise-auditor/` |
| `opencode` — OpenCode | `.opencode/commands/lgpd-*.md` | `.agents/skills/lgpd-enterprise-auditor/` |
| `agents` — Codex, Gemini CLI and similar | — (no slash commands) | `.agents/skills/lgpd-enterprise-auditor/` (always installed) |

- **Without the skill (default):** you run the audit through the slash commands (`/lgpd-saas`, `/lgpd-full-audit`…), which run the modular framework (`.agents/lgpd-enterprise-auditor/`).
- **With the skill:** the assistant can also start the audit from a plain request ("audit this project for LGPD"), loading the self-contained skill (`SKILL.md`).
- Several tools in the same project are supported: run the installer once per tool. They share the framework folder.

### Update, check and uninstall

| Action | Command (bash) | PowerShell |
|---|---|---|
| Update every installed tool | `… \| bash -s -- update` | `… install.ps1 update` |
| Check the installation | `… \| bash -s -- check` | `… install.ps1 check` |
| Uninstall | `… \| bash -s -- uninstall` | `… install.ps1 uninstall` |

`…` stands for the same `curl …/install.sh` or `iwr …/install.ps1` prefix used to install.

Scripted / CI use (no questions):

```bash
curl -fsSL https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/latest/download/install.sh \
  | bash -s -- install --non-interactive --target cursor --with-skill
```

| Option (bash) | PowerShell | Description |
|---|---|---|
| `--target <tool>` | `-Target` | `claude`, `cursor`, `vscode`, `opencode` or `agents` (required with `--non-interactive`) |
| `--with-skill` / `--no-skill` | `-WithSkill` / `-NoSkill` | Install the skill or not (default: no) |
| `--project-dir <dir>` | `-ProjectDir` | Target project (default: git root of the current directory) |
| `--version <ref>` | `-Version` | Tag or branch (default: latest published tag) |
| `--non-interactive` | `-NonInteractive` | Run without questions |

Each installation records a manifest in `.agents/lgpd-enterprise-auditor/.install/<tool>.json`; `update`, `check` and `uninstall` rely on it and never touch files that are not part of the framework.

When you accept the backup offered on reinstall, a copy goes to `.lgpd-auditor-backup/` in your project — add it to your `.gitignore`:

```gitignore
.lgpd-auditor-backup/
```

Release notes for each version are in the [CHANGELOG](./CHANGELOG.md).

### Manual installation

Copy `.agents/lgpd-enterprise-auditor/` to the root of your project and the files in `commands/` to your tool's commands folder (table above). For the skill, copy `SKILL.md` to `<skills folder>/lgpd-enterprise-auditor/SKILL.md`.

## Legal basis and updates

This framework uses the **General Data Protection Law (LGPD)** as its primary legal reference:

- **Official text (Planalto):** [Law No. 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- **Regulatory authority:** [ANPD](https://www.gov.br/anpd/) — since **Law No. 15.352/2026**, renamed National Data Protection **Agency** and placed under the regulatory-agency regime of Law No. 13.848/2019 (LGPD art. 55-A).
- **Related statute:** [Digital Statute of the Child and Adolescent — Law No. 15.211/2025](https://www.gov.br/anpd/pt-br/assuntos/eca-digital), in force since 2026-03-17, regulated by Decree No. 12.880/2026 and enforced by ANPD.
- **Digital platforms:** [Decree No. 12.975/2026](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/decreto/D12975.htm) (updates the Internet Civil Framework regulation — duty of care, notice and takedown, ads, access-log retention) and [Decree No. 12.976/2026](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/decreto/D12976.htm) (protection of women online), in force since 2026-07-20 and enforced by ANPD.

ANPD regulations covered by the framework:

| Resolution | Subject |
|---|---|
| CD/ANPD No. 1/2021 | Inspection and administrative sanctioning procedure |
| CD/ANPD No. 2/2022 | Small-scale processing agents |
| CD/ANPD No. 4/2023 | Dosimetry and application of sanctions |
| CD/ANPD No. 15/2024 | Security incident communication (3 business days) |
| CD/ANPD No. 18/2024 | Data protection officer (DPO) duties |
| CD/ANPD No. 19/2024 | International data transfer and standard contractual clauses |
| CD/ANPD No. 30/2025 | Priority enforcement themes map 2026-2027 |
| CD/ANPD No. 31/2025 | Regulatory agenda 2025-2026 |
| CD/ANPD No. 32/2026 | European Union recognized as providing an adequate level of protection |

| Item | Value |
|------|--------|
| Last synchronization | `2026-10` |

## How the project is organized

```text
.
├── SKILL.md
├── scripts/
│   ├── install.sh
│   ├── install.ps1
│   ├── validate-report.py
│   └── tests/
├── commands/
│   ├── lgpd-full-audit.md
│   ├── lgpd-saas.md
│   ├── lgpd-web.md
│   ├── lgpd-mobile.md
│   ├── lgpd-ai-llm.md
│   ├── lgpd-devsecops.md
│   ├── lgpd-eca-digital.md
│   └── lgpd-plataformas-digitais.md
└── .agents/
    └── lgpd-enterprise-auditor/
        ├── core/
        ├── legal/
        ├── governance/
        ├── cloud/
        ├── appsec/
        ├── mobile/
        ├── devsecops/
        ├── ai-llm/
        ├── orchestrator/
        ├── templates/
        ├── reports/
        └── validation/
```

### Canonical source

The canonical base path for the modular framework is:

`.agents/lgpd-enterprise-auditor/`

This is the expected standard for projects that adopt the same structure.

## How it works

The audit workflow follows 5 steps:

1. **Project context**: stack, processed data, integrations, and operational setup.
2. **Smart routing**: the orchestrator activates modules by scenario.
3. **Evidence-based checklist**: every item in the catalog of the active modules is evaluated, each with a fixed ID and a defined weight; nothing is marked compliant without proof.
4. **Consolidation**: severity, score, and final classification. With an open critical finding, the classification is capped at `PARCIALMENTE_CONFORME`; in a targeted scenario, the report carries the **escopo direcionado** (targeted scope) mark and lists the domains that were not audited.
5. **Standardized output**: executive/technical/compliance report + remediation plan, written as `.md`, `.html` or both.

The report, in any format, describes issues that may still be open and is **confidential**: keep it out of public repositories (for example, in a folder listed in `.gitignore`).

To check a generated report (catalog IDs, allowed values, the link between items and findings, and the score calculation), run `python3 scripts/validate-report.py <report.html>` from a clone of this repository.

## Usage modes

### 1) Full audit

Use when you need full coverage:

- command: `commands/lgpd-full-audit.md`
- scenario: `full_audit`

Activated modules: `core`, `legal`, `eca-digital`, `plataformas-digitais`, `governance`, `cloud`, `appsec`, `mobile`, `devsecops`, `ai-llm`.

### 2) Scenario-based audit

Use for focused scope:

- `lgpd-saas` -> web SaaS
- `lgpd-web` -> websites and landing pages
- `lgpd-mobile` -> mobile app
- `lgpd-ai-llm` -> AI/LLM systems
- `lgpd-devsecops` -> pipelines and supply chain
- `lgpd-eca-digital` -> platforms accessed by children and adolescents (LGPD art. 14 + Digital Statute)
- `lgpd-plataformas-digitais` -> internet application providers with third-party content, paid ads or image/voice-generating AI (Decrees 12.975/2026 and 12.976/2026)

## Available commands

Commands in `commands/` are execution shortcuts for the agent.

All commands include:

- metadata (`name`, `description`, `license`, `author`, `version`);
- minimum context collection when not mapped yet;
- mandatory evidence and consistency rules aligned with the modular framework.

## Audit contracts (summary)

Core contracts are located at `.agents/lgpd-enterprise-auditor/core/`:

- `auditor-core.md`: canonical structures (`finding`, `check_item`, `module_output`);
- `evidence-engine.md`: evidence rules;
- `severity-model.md`: severity classification;
- `scoring-engine.md`: score calculation, item catalog, classification cap and score scope;
- `reporting-engine.md`: mandatory output format and generated files (`.md`, `.html` or both).

## Who this project is for

- engineering and platform teams;
- information security and AppSec teams;
- compliance and privacy teams;
- LGPD readiness consultancies;
- squads using generative AI in production.

## Adoption best practices

- keep `.agents/lgpd-enterprise-auditor/` versioned together with the product;
- adapt commands by domain without breaking core contracts;
- record technical and documentary evidence per item;
- review score and non-conformities per release;
- treat auditing as a continuous process, not a one-time event.

## Suggested roadmap

- richer templates by industry (healthtech, fintech, gov);
- evidence collection automation;
- environment-based risk matrix generation;
- comparative reports between releases;
- CI/CD pipeline integration.

## People Behind LGPD Enterprise Auditor

This project evolves with contributions from people who believe in disciplined, practical, and auditable AI software engineering.

<p align="left">
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=BrunoLagoa/lgpd-enterprise-auditor&max=100" alt="Project contributors" width="45" />
  </a>
</p>

Want to appear here too? Open an issue, suggest improvements, or submit a PR.

## Support and contributing

- Questions: use [Discussions](https://github.com/BrunoLagoa/lgpd-enterprise-auditor/discussions).
- Bugs, improvements and **normative updates**: open an [issue](https://github.com/BrunoLagoa/lgpd-enterprise-auditor/issues/new/choose).
- To contribute, read the [contributing guide](./CONTRIBUTING.md) and the [code of conduct](./CODE_OF_CONDUCT.md) (in Portuguese). Vulnerabilities: follow the [security policy](./SECURITY.md).
- Release notes: [CHANGELOG](./CHANGELOG.md).

## Legal notice

LGPD Enterprise Auditor supports LGPD compliance audits but **does not replace** the assessment of the data protection officer (DPO) or specialized legal advice. Reports are AI-assisted, built from the evidence available, and their conclusions depend on how complete and current that evidence is.

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for full terms.

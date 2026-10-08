# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

`lgpd-enterprise-auditor` is **not application code** — it is a prompt/instruction framework that turns an LLM agent into an evidence-driven LGPD (Brazilian data protection law, Lei nº 13.709/2018) compliance auditor. The framework itself is Markdown: agent instructions, audit contracts, scenario manifests, report formats, and slash commands. There is no build, no package manager, and no runtime to execute. "Working" on this repo means editing Markdown specifications so the agent behaves consistently. The only code lives in `scripts/`: the installer (see "Installer" below), the maintenance scripts that keep generated content in sync (`update-skill-catalog.sh`, `update-example-report.sh`), the report validator (`validate-report.py`, Python 3 standard library only) and the tests, all run by CI.

## Language convention

Documentation is bilingual but the split is deliberate:
- **User-facing docs** are maintained in Brazilian Portuguese + English: `README.md` is Portuguese and canonical (the audience is Brazilian), `README.en.md` is the English version; keep both in sync. Community files (`CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `.github/ISSUE_TEMPLATE/`, `.github/pull_request_template.md`) and `CHANGELOG.md` are Portuguese only. The `<!-- README-I18N:START -->` / `END` markers delimit the language-switcher block — don't break them.
- **Framework internals** (everything under `.agents/`, `SKILL.md`, and `commands/`) are written in **Brazilian Portuguese**. Match this when editing framework files — do not translate them to English.
- All Portuguese text uses full, correct accentuation — `.agents/`, `SKILL.md` and `commands/*.md` alike (command descriptions show up in the assistants' slash-command menus). Identifiers inside backticks (scenario, module and score-area IDs, enum values such as `NAO_CONFORME`) stay without accents. Framework file titles are in Portuguese, following the pattern `# Núcleo — …` (core), `# Módulo X — …` (modules), `# Manifesto — \`id\`` and `# Modelo — …` (templates).

## Two parallel artifacts: the skill and the modular framework

The repository ships the same auditor in two forms, which must stay functionally equivalent ("parity"). Never call them "V1"/"V2", "legacy" or "monolith" in any file — they are both current products:

- **The skill** — `SKILL.md` (~1,300 lines). A single self-contained prompt covering the full checklist, severity, scoring, and report format. It starts with the same YAML frontmatter as `commands/*.md` (`name: lgpd-enterprise-auditor`) so it can be installed as a skill (`.claude/skills/lgpd-enterprise-auditor/SKILL.md` or `.agents/skills/lgpd-enterprise-auditor/SKILL.md`); keep `name` equal to that directory name.
- **The modular framework** — `.agents/lgpd-enterprise-auditor/`, decomposed into layers. This is what the slash commands run and the canonical structure to extend.
- `orchestrator/full-audit.md` defines what `full_audit` must cover: the **17 audit domains** shared with the skill (mapeamento de dados, consentimento, direitos do titular, política de privacidade, cookies e tracking, segurança da informação, cloud security, mobile security, APIs e integrações, DevSecOps, logs e observabilidade, IA/LLM, governança, compartilhamento de dados, retenção e exclusão, ECA Digital, plataformas digitais), where an installed skill is found, and the minimum equivalence criteria.

When you change audit logic (a checklist item, severity rule, scoring weight, or report field), check whether it must change in **both** the skill and the framework. `validation/parity-checklist.md` and `validation/traceability-matrix.md` track this equivalence — update them when coverage shifts.

## Modular framework architecture

Canonical base path (referenced literally inside commands and meant to be copied into audited projects): `.agents/lgpd-enterprise-auditor/`

- `README.md` — the framework overview (structure, execution flow, scenarios, naming conventions). It duplicates facts that live in `orchestrator/` and `core/`; keep it in sync when those change.
- `core/` — the canonical **contracts** all other modules depend on. Edit these first; downstream modules and reports must conform:
  - `auditor-core.md` defines the data shapes `finding`, `check_item`, `module_output` (their fields and enum values).
  - `evidence-engine.md` (evidence rules and confidence scale), `severity-model.md` (CRITICO/ALTO/MEDIO/BAIXO), `scoring-engine.md` (per-area weights + final 0–100 classification), `reporting-engine.md` (mandatory report format).
- `legal/` — LGPD/ANPD normative basis (`lgpd-legal-framework.md`, `anpd-guidelines.md`), legal bases for processing (`legal-bases-engine.md`: art. 7º vs art. 11, the audited party's role as controller or operator, and public data), data-subject rights, children/adolescents (art. 14), international transfer (arts. 33–36), and `eca-digital.md`. Note the exception: `eca-digital.md` lives under `legal/` but is a **module of its own** (ID `eca-digital`, with `orchestrator/manifests/eca-digital.manifest.md`) because it implements a separate statute (Lei nº 15.211/2025), not an LGPD chapter. `plataformas-digitais.md` follows the same exception (ID `plataformas-digitais`, with its own manifest): it implements Decretos nº 12.975/2026 and nº 12.976/2026, the Marco Civil da Internet regulation that ANPD now enforces.
- `governance/`, `cloud/`, `appsec/`, `mobile/`, `devsecops/`, `ai-llm/` — specialist audit modules, one per domain.
- `orchestrator/` — scenario-based module activation. `router.md` holds the activation rules, `activation-matrix.md` the scenario→module table, `full-audit.md` the `full_audit` coverage, and `manifests/*.manifest.md` declare each module's `required` flag, `files`, inputs, prerequisites, `activates_when`, and `primary_outputs`. `files` lists the module's files and is what the agent reads: `legal/` holds three modules, so reading the whole folder would pull in rules of modules that were not activated. Every module file must be listed in exactly one manifest.
- `cloud/cloud-audit.md` covers IaaS, PaaS/serverless and shared hosting, including validating production responses (the hosting/CDN layer may change headers the code sets).
- `templates/` — reusable compliance artifacts (privacy/cookie policy, processing records — `ropa-template.md` —, legitimate-interest assessment, DPO appointment, retention policy, RIPD, DPA, incident response, ECA Digital semiannual transparency report, age-assurance checklist). A template must satisfy the checklist items that audit it (e.g. the privacy policy template carries everything `DT-04` asks for).
- `reports/` — output formats per audience (executive, technical, compliance, risk-matrix) and the HTML report: `html-report.md` (how to generate it and the JSON data shape) plus `html-report-template.html` (the template itself; see "HTML report" below).
- `validation/` — skill↔framework parity checklist (`parity-checklist.md`) and the domain→module traceability matrix (`traceability-matrix.md`), which also lists the catalog items of each domain.

## Check-item catalog

The checklist items are **fixed**. Each module file has a "Checklist atômico" table, one row per item:

`| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |`

- **ID** is stable (`SE-03`): two or three uppercase letters, a hyphen and two digits (the HTML template links IDs with `/[A-Z]{2,5}-\d{1,3}/`). Each prefix belongs to one file. A new item takes the next number of its prefix; never renumber or reuse an ID. `EX-nn` is reserved for extra items an audit finds outside the catalog.
- **Domínio** is the code from the domain→area map in `core/scoring-engine.md` (`BL` or `1`–`17`); it decides the score area, so a module never states an area by hand.
- **Criticidade** is the item's default `criticality` (its weight). It changes only through the condition written in **Agravante ou atenuante** or through small-agent modulation — never case by case. That is what makes the score reproducible.
- Scoping questions ("is the service likely to be accessed by minors?") stay outside the table and never score.
- An audit evaluates **every** catalog item of each active module (`APLICAVEL`, `NAO_APLICAVEL` or `NAO_VERIFICADO`). Avoid two items that describe the same obligation: when a control is audited elsewhere, point to that item instead of creating another (e.g. the DPA with the hosting provider is `GV-09`, not a cloud item).

The skill carries the same catalog between the `<!-- CATALOGO:INICIO … -->` and `<!-- CATALOGO:FIM -->` markers of `SKILL.md`, grouped by domain. That block is **generated** from the module tables: after touching any table, run `scripts/update-skill-catalog.sh` and never edit the block by hand. `scripts/tests/test-framework.sh` fails when it is stale.

## Example (`examples/`)

`examples/saas-demo/` is a fictional, intentionally flawed SaaS with a full audit report produced with `/lgpd-saas`, in both output files: `relatorio-auditoria-lgpd.md` and `relatorio-auditoria-lgpd.html` (plus `relatorio-auditoria-lgpd.png`, the screenshot shown in both READMEs). It is the public showcase linked from both READMEs, so it must always match the **current** report format and score formula: whenever `core/reporting-engine.md`, `core/scoring-engine.md`, `core/severity-model.md` or the catalog of a module the example activates (`legal`, `governance`, `appsec`, `cloud`, `devsecops`) change, update the example report in the same PR — the `.md` and the JSON data block of the `.html` carry the same data, including `meta.framework_version` (the project version). The example lists all catalog items of its active modules (109 today). `scripts/validate-report.py examples/saas-demo/relatorio-auditoria-lgpd.html --md examples/saas-demo/relatorio-auditoria-lgpd.md` checks IDs, enums, item↔finding links, the calculation and that the `.md` carries the same items, findings, score and classification; `test-html-report.sh` runs it. Only obviously fake data (e.g., CPF `123.456.789-09`).

## Canonical scenarios

The scenario IDs are snake_case and must stay identical across `orchestrator/router.md`, `orchestrator/activation-matrix.md`, the framework `README.md`, and each `commands/*.md`:

| Scenario | Modules |
|---|---|
| `saas_web` | core, legal, governance, appsec, cloud, devsecops |
| `web_site` | core, legal, governance, appsec, cloud |
| `mobile_app` | core, legal, governance, mobile, appsec, cloud |
| `ai_llm_system` | core, legal, governance, ai-llm, appsec |
| `devsecops_pipeline` | core, legal, devsecops, cloud, appsec |
| `eca_digital_platform` | core, legal, eca-digital, governance, appsec, mobile |
| `digital_platform` | core, legal, plataformas-digitais, governance, appsec, cloud |
| `full_audit` | all modules (full coverage, parity with the skill) |

Every scenario other than `full_audit` produces a report marked **escopo direcionado**, listing the domains it did not audit. Technical triggers in `router.md` add modules the scenario does not list; the `ai-llm` trigger fires on any call to an LLM or generative-AI provider or SDK, not only on RAG or fine-tuning, and the scenario commands repeat it.

`eca-digital` is also added to **any** scenario by the normative trigger in `router.md` whenever minors are (or plausibly are) among the users; an age gate based only on self-declared age does not remove the trigger when another indicator exists. Likewise, `plataformas-digitais` is added to any scenario when the audited provider hosts publicly shared third-party content, sells ads/boosts, or offers AI that generates or alters people's image or voice.

## Critical naming rule

Module IDs and score-area IDs use **different casing on purpose** — do not unify them:
- **Module IDs** (routing, file/dir names): kebab-case → `ai-llm`
- **Score-area IDs** (scoring engine): snake_case → `ai_llm`, `eca_digital`, `plataformas_digitais`

The orchestrator activates by module ID; the scoring engine computes by area ID. Mixing the two breaks routing/scoring alignment.

## Scoring and reporting shapes

- Score areas and weights (`core/scoring-engine.md`) must always sum to 100%: `bases_legais` 12, `seguranca` 20, `direitos_titular` 12, `governanca` 12, `infraestrutura` 8, `apis_integracoes` 8, `ai_llm` 8, `eca_digital` 10, `plataformas_digitais` 10. The first seven keep the ratio 15 : 25 : 15 : 15 : 10 : 10 : 10 on purpose: with the last two not applicable (the usual case) redistribution returns exactly those weights. Domains 16 and 17 score in `eca_digital` and `plataformas_digitais`, which are applicable only when the respective module is active.
- An area may be `NAO_APLICAVEL` only with `ENCONTRADA` evidence that its object does not exist in scope — never for missing evidence, and never just because the scenario did not activate the module; its weight is redistributed proportionally across the applicable areas. An area whose object exists but was left out of scope is reported as "cobertura insuficiente", not as not applicable. `bases_legais`, `seguranca`, `direitos_titular` and `governanca` are always applicable. This rule lives in `core/scoring-engine.md` and the scoring section of `SKILL.md`.
- **Classification cap**: with at least one `CRITICO` finding, the final classification never goes above `PARCIALMENTE_CONFORME`, whatever the score; the number itself does not change and risk acceptance does not lift the cap. The mark **classificação limitada por achado crítico** appears only when the cap actually lowers the classification (the HTML template does the same).
- **Status ruler** (`core/evidence-engine.md`, "Status do item", mirrored in the skill): `NAO_CONFORME` when the control does not exist, when it exists but the analysis found the violation it should prevent, or when fewer than half of the elements the item lists are met; `PARCIAL` when the control exists, no violation was found and something is missing (at least half of the listed elements met). A draft or unpublished document proves the content exists, not that it is in force. The questions are applied in order (control missing → violation found → element count → incomplete coverage), and a token gesture that does not do the control's job (a generic e-mail instead of a reporting channel) does not count as the control. A `PARCIAL` finding is always **one level below** the item's `criticality` — never chosen case by case — and a finding's deadline is never longer than the maximum for its severity (`CRITICO` immediate, `ALTO` 30 days, `MEDIO` 90, `BAIXO` 180); `scripts/validate-report.py` enforces both.
- **High-risk decision** (`core/severity-model.md`): one specific criterion plus one general criterion of Res. CD/ANPD nº 2/2022, art. 4º. "Significant impact" has a framework position (three checkable situations); "large scale" has no threshold in the norm and is never presumed; with a specific criterion and no evidence to decide the general one, treat as high risk and record the doubt. Do not invent numeric thresholds.
- **Sensitive data in aggravating conditions** includes data that reveals sensitive information (art. 11, §1º) in every item, and an aggravating condition applies only when it is in the object the item evaluates.
- **Applicability follows the facts of the processing, not the documentation**: missing documents never make an item `NAO_APLICAVEL` (the consent items apply when the system collects consent in practice). A control with no representation in the repository is `NAO_VERIFICADO`; one that is normally declared in a repository file and is missing is `NAO_CONFORME`. An item with both verifiable and out-of-reach elements fails if a verifiable one fails and is otherwise `NAO_VERIFICADO` — never `CONFORME`, which requires everything the item asks for to be proven (v1.7.0 tried `CONFORME` with `MEDIA` confidence here and the next test showed it contradicted the evidence rules).
- **Single counting** ("contagem única"): an item scores on what is left of its own requirement when part of it repeats another item's failure; it is `NAO_APLICAVEL` when it depends on a control that does not exist (e.g. `GV-05`, the contact of a DPO that was never appointed); it fails when its whole requirement fails, even if the cause is shared. Dependencies are a **closed list**: lines of the form `` - `GV-05` depende de `GV-02`: reason `` written under the module tables, copied into the skill by `scripts/update-skill-catalog.sh` and enforced by `scripts/validate-report.py`. With the target `NAO_CONFORME` the dependent item is `NAO_APLICAVEL`; outside the list there is no dependency. Add a pair only when the item could not be met while the other control stays missing. When two catalog items overlap, write the boundary next to the tables (as done for `BL-01`/`BL-02`/`OP-02`, `CK-02`/`CK-03`, `SE-02`/`IN-01`, `IN-06`/`IN-12`) instead of leaving it to the auditor.
- **End-to-end test of a framework change**: install the working tree (`scripts/install.sh install --version local`) into a copy of `examples/saas-demo` without the report files, have a fresh agent with no context run `/lgpd-saas`, then run `scripts/validate-report.py` on its report and diff the item statuses against the example. A divergence means either the example is wrong under the written rule or the rule allows two readings; fix whichever it is. Two such runs shaped v1.7.0.
- The score is **deterministic**: item value by status (`CONFORME` 1, `PARCIAL` 0.5, `NAO_CONFORME` 0) × item weight by `criticality` (`CRITICO` 4, `ALTO` 3, `MEDIO` 2, `BAIXO` 1); `score_area = 100 × Σ(value × weight) / Σ(weight)`; only the global score is rounded, to the nearest integer, halves up. Each `check_item` scores in **exactly one** area, given by its domain through the domain→area map in `core/scoring-engine.md` (mirrored in `SKILL.md`); modules state their area by referring to that map, never "primary areas" chosen case by case. `score_tecnico` / `score_documental` (by `control_type`) are informative only.
- Severity may be lowered by **one level** for small-scale agents (Res. CD/ANPD nº 2/2022) without high-risk processing or confirmed exploitable exposure (`core/severity-model.md`), never for `CRITICO` findings with sensitive or children's data, confirmed leaks or exposed credentials; the modulation is recorded in the `finding` and applies to the item weight. Risk acceptance (`finding.risk_acceptance`) never changes status, severity or score.
- Final classification labels are exactly `CRITICO` (0–49), `BAIXO_NIVEL` (50–69), `PARCIALMENTE_CONFORME` (70–84), `ALTA_CONFORMIDADE` (85–94), `EXCELENTE` (95–100).
- The report (`core/reporting-engine.md`) has 8 mandatory sections in this order: `resumo_executivo`, `score_lgpd`, `checklist_conformidade`, `nao_conformidades`, `itens_obrigatorios_ausentes`, `riscos_identificados`, `plano_adequacao`, `recomendacoes_tecnicas`. Every non-conformity in the checklist must reappear detailed in `nao_conformidades`. The report also carries the `CONFIDENCIAL — uso interno` header, a "Contexto e escopo" block before section 1 (the `context` field of the HTML data), the checklist `Item` cell in the form `ID · criticality · control_type — text`, "o que fazer agora" (3–5 actions with effort `P | M | G`), an `Área` column in the checklist, a glossary after section 8 and the fixed legal notice at the end — these annexes do not count as sections.

## HTML report

The audit **always asks**, in the same round as the context questions, which output format the user wants — `.md`, `.md` and `.html`, or `.html` only — unless the request already says it (rule in `core/reporting-engine.md`, "Arquivos gerados", mirrored in `SKILL.md`, "ARQUIVOS DO RELATÓRIO", `orchestrator/router.md` and every command). With no answer it writes the `.md`. Any format carries the 8 sections; when both files exist they share a base name and the `.md` wins on any divergence. Once a file is written, the chat reply is only a summary (score, classification, coverage, findings by severity, "o que fazer agora", file paths) — the choice exists because writing the data twice costs output tokens, so do not reintroduce a full on-screen copy.

- The `.html` is never written from scratch: the agent copies `reports/html-report-template.html` and replaces the single line `{"_modelo": true}` inside `<script type="application/json" id="lgpd-dados">` with the JSON described in `reports/html-report.md`. Keep that placeholder line and the opening tag exactly as they are — the spec, the skill, `scripts/update-example-report.sh` and the test all match on them.
- The template is one self-contained, offline file: no external fonts, scripts, images or links (its CSP is `default-src 'none'`), light/dark themes, print styles. Data reaches the page only through text nodes (never `innerHTML`), because evidence may quote code from the audited system; inside the JSON, `<` is written as `\u003c`.
- The template's script **mirrors** `core/` and must change with it: item values and weights, area weights, classification bands and the classification cap (`core/scoring-engine.md`, used to recompute the score and the classification from the checklist and warn when declared numbers differ; `test-framework.sh` compares the area weights and the cap with the core), enum labels (`core/auditor-core.md`), the 8 section IDs and the fixed legal notice (`core/reporting-engine.md`). It displays readable labels ("Não conforme") but the JSON always carries the canonical values.
- After changing the template, run `scripts/update-example-report.sh` (re-applies the template to the example, keeping its data) and `scripts/tests/test-html-report.sh` (placeholder present once, no external resources, legal notice equal to `core/reporting-engine.md`, example in sync with the template, example data valid JSON with the 8 sections and the project version). CI runs it in `.github/workflows/html-report.yml`. To check the rendering, open the example in a browser (headless Chrome works for screenshots) and refresh `relatorio-auditoria-lgpd.png` if the top of the page changed.

## Commands (slash commands)

`commands/*.md` are execution shortcuts (`lgpd-full-audit`, `lgpd-saas`, `lgpd-web`, `lgpd-mobile`, `lgpd-ai-llm`, `lgpd-devsecops`, `lgpd-eca-digital`, `lgpd-plataformas-digitais`). Each has YAML frontmatter (`name`, `description`, `license`, `metadata.author`, `metadata.version`) and then instructions that first read what the project already documents (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifests), ask only for what is missing — always including the nature of the processing agent (natural or legal person, economic purpose, size, high-risk processing) and its role in each data flow (controller, operator or both) —, select a scenario, list the modules to activate, reference the canonical base path, and end with the rule to write the report in the chosen format. Each command also carries the mandatory output-format question right after its list of context questions. When adding a command, mirror this frontmatter and keep the activated-module list consistent with `orchestrator/activation-matrix.md` and `orchestrator/router.md`.

## Installer (`scripts/`)

`scripts/install.sh` (bash, must stay compatible with macOS's bash 3.2) and `scripts/install.ps1` (Windows PowerShell 5.1 and PowerShell 7) are **functionally equivalent** — same actions (`install`, `update`, `uninstall`, `check`), options, destinations and manifest format. Change both together, the same way skill↔framework parity works.

- Installation is always **local, per project** — never global. The installer copies `.agents/lgpd-enterprise-auditor/`, the `commands/*.md` (rendered per tool) and, opt-in, `SKILL.md` as a skill.
- Tools (`--target`): `claude` → `.claude/commands/`, `cursor` → `.cursor/commands/` (frontmatter stripped, `description` promoted to the first line), `vscode` → `.github/prompts/*.prompt.md` (frontmatter reduced to `name`, `description` + `agent: agent`), `opencode` → `.opencode/commands/`, `agents` → no commands, skill always installed. Skill goes to `.claude/skills/lgpd-enterprise-auditor/` for `claude` and `.agents/skills/lgpd-enterprise-auditor/` for every other tool.
- Commands are discovered by glob, so a new file in `commands/` is installed automatically — no installer change needed.
- With no `--version`, the installer resolves the latest `v*` tag through the GitHub API. A failed lookup (no network, API rate limit) is **not** treated as "no tags": interactive mode asks before using `main`, `--non-interactive` stops and asks for `--version`. Only a repository that really has no `v*` tag falls back to `main` with a warning. Both scripts behave the same; the tests cover it by running a copy of the installer outside the clone.
- Each tool gets a manifest at `.agents/lgpd-enterprise-auditor/.install/<target>.json` (one key per line, written identically by both scripts). Uninstall only removes files listed there, keeps a skill folder still referenced by another tool, and removes the framework folder only when no tool remains.
- `install.ps1` and `tests/test-install.ps1` must keep their UTF-8 BOM (Windows PowerShell 5.1 misreads accented text without it); files the installers write must be UTF-8 **without** BOM, or the YAML frontmatter breaks.
- Tests: `scripts/tests/test-install.sh` and `scripts/tests/test-install.ps1` run offline against the local clone (`--version local`). CI (`.github/workflows/install.yml`) runs ShellCheck, the bash tests on Ubuntu and on macOS `/bin/bash` 3.2, and the PowerShell tests on Windows with both `pwsh` and `powershell` 5.1.

## Framework tests

**Local first.** `scripts/tests/run-all.sh [tag]` runs everything CI runs (the four suites, the bash 3.2 pass, ShellCheck and the PowerShell tests when those tools are installed, and the attribution check on unpushed commits). Run it before every commit and push, and treat its result as the gate: CI is a second opinion on Ubuntu and Windows, not something to wait for. The one thing it cannot cover without `pwsh` is `install.ps1` — for a change there, the Windows job is the only test, so wait for it before tagging.

`scripts/tests/test-framework.sh` (workflow `framework.yml`, Ubuntu and macOS bash 3.2) checks what used to depend on reading: catalog format (7 columns, canonical enums, unique IDs, one file per prefix, known domain), skill catalog in sync with the modules, area weights equal in the core, the skill and the HTML template and summing 100, domain→area map equal in the core and the skill, the classification cap, scenario→module lists equal in `router.md`, `activation-matrix.md` and each command, manifests (`files` exist, every module file in exactly one manifest), `[[file]]` references and the sync date in both READMEs. Run it after any framework change. Keep its `awk` portable (BSD awk and mawk: no interval expressions, no gawk extensions).

Workflows declare `permissions: contents: read` and pin `actions/checkout` by commit hash with the version in a comment; to move to a newer version, get the hash with `git ls-remote --tags https://github.com/actions/checkout` and update every workflow.

## Versioning and releases

- There is **one project version**: `metadata.version` in `SKILL.md`, repeated in every `commands/*.md`. They must always be equal; `scripts/tests/test-versions.sh` enforces it in CI (`.github/workflows/versions.yml`), together with a matching `## [X.Y.Z]` section in `CHANGELOG.md` and, on tag pushes, tag `vX.Y.Z`. `scripts/tests/test-html-report.sh` additionally requires the example report's `meta.framework_version` to equal the project version.
- `CHANGELOG.md` follows Keep a Changelog in **Brazilian Portuguese** (sections `Adicionado`, `Alterado`, `Corrigido`, `Removido`). Every user-visible change goes under `## [Não lançado]` in the same commit.
- To release: move the `[Não lançado]` entries to a new `## [X.Y.Z] - YYYY-MM-DD` section, bump `metadata.version` in `SKILL.md` and all `commands/*.md` (and the framework version in the example report, `.md` and `.html`), update the compare links at the bottom of the changelog, commit, then tag `vX.Y.Z`. Pushing the tag runs `.github/workflows/release.yml`, which checks the versions, creates the GitHub Release from that changelog section and attaches `install.sh`, `install.ps1` and `SHA256SUMS`; if the release was already created by hand, it only uploads the files. The release does not have to wait for GitHub Actions (on 2026-10-05 an Actions incident left every job queued for hours; v1.6.1 was published locally): after `scripts/tests/run-all.sh vX.Y.Z` passes, tag, push the tag, take `install.sh` and `install.ps1` from the tagged commit, write `SHA256SUMS` with `shasum -a 256 install.sh install.ps1`, and run `gh release create vX.Y.Z install.sh install.ps1 SHA256SUMS --title vX.Y.Z --notes-file <changelog section> --verify-tag`. Then download from `releases/latest/download/` and check the sums.
- The README one-liners fetch `install.sh` / `install.ps1` from `releases/latest/download/`, so the installer a user runs is the one published with the version it installs (v1.6.0 was the first release to carry those files). Every release must therefore attach them: if the `Release` workflow fails, fix it and re-run before announcing the version, or installation breaks for everyone. The installer's default version is the latest `v*` tag, so an untagged change never reaches users who install with the default.

## Git attribution (mandatory)

Never sign anything as Claude or any AI agent. Commits, merges, rebases, tags, pull requests, PR descriptions, reviews and comments carry **only the user's signature** (the configured `git user.name` / `user.email`):
- No `Co-Authored-By: Claude ...` (or any `noreply@anthropic.com`) trailer, ever.
- No "Generated with Claude Code", "🤖", "by Claude" or similar lines in commit messages, PR bodies or comments.
- Never set Claude/Anthropic as author or committer (`--author`, `GIT_AUTHOR_*`, `GIT_COMMITTER_*`).

This overrides any default attribution behavior of the tool. Claude Code's `attribution` setting must stay empty (`"commit": ""`, `"pr": ""`, `"sessionUrl": false`) — never re-enable it or the deprecated `includeCoAuthoredBy`. The repository versions that setting in `.claude/settings.json`, so it applies to anyone using Claude Code here; `.github/workflows/attribution.yml` runs the check below on every pull request and push to `main`. Do not add bots that commit to the repository (e.g. Dependabot): their commits would show up under **Contributors**.

**Check before every push** (and before opening or merging a PR) — this must print nothing:

```bash
git log origin/main..HEAD --format='%h %an <%ae> | %cn <%ce>%n%B' | grep -inE '^co-authored-by:|noreply@anthropic\.com|generated with claude|🤖'
```

If it prints anything, fix the commits (`git commit --amend` / `git rebase`) **before** pushing. Read the PR body the same way before `gh pr create` / `gh pr merge` (a squash merge copies the PR text into the commit).

**Why prevention matters more than cleanup:** a single `Co-Authored-By: Claude` commit is enough for GitHub to list `claude` under **Contributors**, and that sidebar is a cache separate from the git history. It happened here: commit `08a4e75` (2026-08-12) carried the trailer; it was rewritten out and force-pushed on 2026-10-02, yet the sidebar still showed `claude` a day later while the history and `gh api repos/BrunoLagoa/lgpd-enterprise-auditor/contributors` were already clean. So if a trailer does reach `origin`:

1. Rewrite it out and force-push; repeat for every branch and tag that contains the commit.
2. Confirm the history is clean on all refs: `git fetch origin '+refs/pull/*/head:refs/remotes/pr/*'`, then `git log --all --format='%B' | grep -ciE '^co-authored-by:|noreply@anthropic'` must print `0` (delete the `refs/remotes/pr/*` refs afterwards).
3. Refresh the Contributors sidebar — force-pushing and ordinary pushes to `main` did not do it. What worked on 2026-10-03: create a temporary branch on `origin` at the same commit as `main`, make it the default branch (`gh api -X PATCH repos/BrunoLagoa/lgpd-enterprise-auditor -f default_branch=<tmp>`), switch the default back to `main`, delete the temporary branch, then push a commit to `main`. Do it only with no open PRs, and confirm `default_branch` is `main` again at the end.
4. Verify on the page itself, not only through the API: `curl -sL 'https://github.com/BrunoLagoa/lgpd-enterprise-auditor/contributors_list?current_repository=lgpd-enterprise-auditor&deferred=true' | grep -o 'alt="@[^"]*"'` must list only the owner. Never claim the remote is fixed based on the history alone. The old commit stays reachable by SHA on GitHub until it is garbage-collected; only GitHub Support can purge it, and the user opens that ticket.

## Post-merge branch cleanup (automatic)

Day-to-day work is committed straight to `main`. When a branch does exist and the user reports that the merge is done and succeeded (e.g. "já fiz o merge e deu sucesso", "merge feito"), run this cleanup **right away, without asking again** — that message is the standing authorization:

1. `git fetch --prune origin`, then identify the merged branch: the current branch if it is not `main`; otherwise the branch named by the user, or the head branch of the most recently merged PR (`gh pr list --state merged --limit 1 --json headRefName,number,mergedAt`).
2. Verify it really is merged before deleting anything: `gh pr view <branch> --json state,mergedAt` must report `MERGED`, or the branch must appear in `git branch --merged origin/main`. If neither confirms it, **stop and ask** — never delete unverified work.
3. `git switch main && git fetch origin && git merge --ff-only origin/main` (a plain `git pull` can fail here with "Cannot fast-forward to multiple branches").
4. Delete the local branch with `git branch -d <branch>`. Use `-D` only when step 2 confirmed a squash or rebase merge through `gh` (the repo allows both, so `-d` can refuse a branch that is in fact merged).
5. Delete the remote branch with `git push origin --delete <branch>`. The repo does not auto-delete head branches on merge (`deleteBranchOnMerge: false`); if the branch is already gone remotely, treat it as done.
6. `git fetch --prune origin` and report what was deleted, locally and on `origin`, plus the commit `main` is now at.

Never delete `main` (the default branch), tags, or any branch other than the one confirmed merged. If the merge brought framework changes, also run the "Sync-date maintenance" and changelog checks below.

## Sync-date maintenance (required on every framework update)

Whenever you make a substantive update to the framework (audit logic, modules, contracts, commands, templates, or report formats), you **must** update the synchronization date in both READMEs to the current month (`YYYY-MM` format):
- `README.md` → the `| Última sincronização | \`YYYY-MM\` |` row
- `README.en.md` → the `| Last synchronization | \`YYYY-MM\` |` row

Keep the value identical in both files (currently `2026-10`). This row signals when the framework was last aligned with LGPD/ANPD; a stale date is misleading, so never skip it.

## Where normative changes ripple

A change to LGPD/ANPD coverage rarely touches one file. Typical fan-out for a new legal requirement:
1. the relevant `legal/*.md` (or a new file there);
2. the skill `SKILL.md` (parity);
3. `orchestrator/manifests/legal.manifest.md` → `primary_outputs`;
4. `validation/parity-checklist.md` (+ `traceability-matrix.md` if a domain moves module);
5. both READMEs (legal-basis section + sync date).

Concrete example already in the tree: Resolução CD/ANPD nº 15/2024 (3 business days to report an incident) appears in `legal/anpd-guidelines.md`, `governance/dpo-framework.md`, `templates/incident-response-template.md`, `validation/parity-checklist.md`, and both READMEs — change it in all of them or nowhere.

## Invariants to preserve when editing

These rules are load-bearing across the whole framework — keep them intact:
- Never mark anything compliant without evidence; every `finding` cites the applicable LGPD article.
- Severity values are exactly `CRITICO | ALTO | MEDIO | BAIXO`; `check_item.status` is `CONFORME | PARCIAL | NAO_CONFORME`; deadlines `IMEDIATO | 30_DIAS | 90_DIAS | 180_DIAS`; effort `P | M | G`. Every `check_item` carries `score_area`, `criticality`, `control_type` (`TECNICO | DOCUMENTAL`) and `applicability` (`APLICAVEL | NAO_APLICAVEL | NAO_VERIFICADO`); only `APLICAVEL` items have a `status` and enter the score. `NAO_APLICAVEL` needs `ENCONTRADA` evidence that the object does not exist (or that the duty belongs to another agent, or that the item depends on a control whose absence is already counted in another item); `NAO_VERIFICADO` is only for technical controls outside the auditor's reach — a document the audited party failed to produce is `AUSENTE`, never either of those. Coverage below 80% marks the result as "score parcial". There is no "risk accepted" status — acceptance is a record on the `finding`.
- Checklist items come from the catalog: every item of an active module is evaluated, with its catalog ID, area and `criticality`; the catalog in `SKILL.md` is generated from the module tables and never edited by hand.
- Evidence is classified on **two independent axes**, never mixed: `evidence_type` (degree of proof) is `ENCONTRADA | PARCIAL | AUSENTE`, and `evidence_source` (origin) is `TECNICA | DOCUMENTAL`. `CONFORME` requires `ENCONTRADA`; `NAO_CONFORME` requires `PARCIAL` or `AUSENTE` (the degree measures proof of the required control, not proof of the problem); `CRITICO`/`ALTO` findings require an explicit `TECNICA` or `DOCUMENTAL` source. An item may hold several evidences and both sources (`TECNICA + DOCUMENTAL`), and carries `evidence_confidence` (`ALTA | MEDIA | BAIXA`), which never changes status, severity or score. Report format: `GRAU (ORIGEM), confiança NIVEL: descrição`. Both axes exist in the skill (`SKILL.md`, "SISTEMA DE EVIDÊNCIAS") and the framework (`core/evidence-engine.md` + `core/auditor-core.md`).
- The `full_audit` scenario must activate every module (`core, legal, eca-digital, plataformas-digitais, governance, cloud, appsec, mobile, devsecops, ai-llm`) to preserve parity with the skill.
- Only **norms in force** produce `finding`s or a `NAO_CONFORME` status. Bills and draft guidance (e.g. PL nº 2338/2023) live in "Em monitoramento" sections and may only feed `recomendacoes_tecnicas`.
- `core` and `legal` are always required regardless of scenario.
- No module may redefine severity, scoring, or report format locally — those live only in `core/`.

## Evidence model (reconciled 2026-08)

`evidence_type` and `evidence_source` used to be a single flat enum, which made the engine's "every `CONFORME` needs `ENCONTRADA`" rule unsatisfiable from the `finding` contract. They are now two separate fields on both `finding` and `check_item`. When touching evidence rules, keep these files aligned: `core/evidence-engine.md`, `core/auditor-core.md`, `core/reporting-engine.md`, `reports/technical-report.md`, `reports/html-report.md` with its template, and `SKILL.md` (the skill) — plus the parity checklist item that asserts both axes exist in the skill and the framework.

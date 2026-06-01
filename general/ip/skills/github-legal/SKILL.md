---
name: github-legal
title: GitHub Legal -- License, Compliance, and Security Policy
description: GitHub legal compliance — generate LICENSE, SECURITY.md, CITATION.cff, NOTICE; handle fork attribution and dependency compatibility.
author: avalonreset
author_url: https://github.com/avalonreset/claude-github/tree/main/skills/github-legal
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# GitHub Legal -- License, Compliance, and Security Policy

## Deterministic Entrypoint

For API agents and non-interactive runs, use the deterministic legal runner:

```bash
python3 scripts/run_headless.py legal --path /path/to/repo
python3 scripts/run_headless.py legal --path /path/to/repo --write-files
python3 scripts/run_headless.py legal --path /path/to/repo --write-files --license MIT
```

This writes:

- `.github-audit/legal-data.json`
- `.github-audit/output/<repo>-<timestamp>/LEGAL-REPORT.md`
- `.github-audit/output/<repo>-<timestamp>/LEGAL-PLAN.md`
- `.github-audit/output/<repo>-<timestamp>/LEGAL-SUMMARY.json`

By default this is a plan-only pass. `--write-files` is the explicit approval
gate for writing `LICENSE`, `SECURITY.md`, `CITATION.cff`, and `NOTICE`.
Complex or ambiguous legal situations must be flagged for human review instead
of being guessed.

## Disclaimer -- ALWAYS Include in Output

This tool provides best-effort compliance assistance for common open source licensing
scenarios on GitHub. **It is NOT legal advice.** The output of this skill does not
constitute a legal opinion and should not be relied upon as such.

Users are responsible for their own due diligence. For complex licensing situations
(dual licensing, contributor license agreements, patent disputes, commercial use of
copyleft code, trademark issues), consult a qualified attorney.

**Include this disclaimer at the top of every output:**
```
> This analysis is automated compliance assistance, not legal advice.
> Always verify licensing decisions with your own due diligence.
> For complex or high-stakes situations, consult a qualified attorney.
```

## Process (GARE Pattern)

### 1. Gather

**Step 0 -- Check shared data cache:**
Before gathering, check `.github-audit/` for cached data from other skills.
Reference: `github/references/shared-data-cache.md` for schemas.

- `repo-context.json` (optional) -- repo type, intent, is_fork flag. If missing,
  gather yourself via `gh repo view`.

- Read existing LICENSE file (if any)
- **Fork and upstream detection (two checks):**
  1. GitHub fork flag: `gh repo view --json isFork,parent`
  2. **Upstream project scan** -- even if GitHub says `isFork: false`, scan the
     README and repo description for upstream signals:
     - "powered by [project]", "built on [project]", "based on [project]"
     - "fork of [project]", "[project] distribution", "[project]-powered"
     - "wrapper around [project]", "extends [project]"
     - Config files that reference another project (e.g., wezterm.lua in a
       terminal project means WezTerm is upstream)
     If upstream is detected, treat it like a fork for compliance purposes:
     fetch the upstream repo's LICENSE and check obligations.
     **This catches projects like BenjaminTerm (WezTerm distro) that aren't
     GitHub "forks" but still have upstream license obligations.**
- If fork or upstream detected, read upstream LICENSE and NOTICE files
- Scan dependency manifests for license compatibility:
  - package.json, setup.py, pyproject.toml, Cargo.toml, go.mod, requirements.txt,
    Gemfile, pom.xml, build.gradle, composer.json, Package.swift, *.csproj
  - If no manifest files exist, scan the README for dependency mentions (e.g.,
    `pip install X`, import statements, "requires X") and note their licenses
- Check for existing SECURITY.md, CITATION.cff, NOTICE
- Check for vendored/copied code: look for third-party directories (vendor/,
  third_party/, lib/external/) and check if they have their own LICENSE files
- Get user intent from orchestrator context

### 2. Analyze

- Is the current license appropriate for the user's intent?
- **Fork/upstream compliance (both GitHub forks AND detected upstream projects):**
  - Does the current license comply with upstream?
  - Is the upstream copyright preserved?
  - Are there NOTICE file obligations?
  - For non-fork upstream projects: is the relationship acknowledged in LICENSE
    or README? (e.g., "Based on WezTerm, licensed under MIT")
- Are there dependency license conflicts?
- Is SECURITY.md present and adequate?
- Is CITATION.cff present? **CITATION.cff is a default deliverable** -- generate it
  for every repo unless the user explicitly declines. It costs nothing, takes 10 seconds
  to generate, and enables GitHub's "Cite this repository" button. Academic intent is not
  required -- any project benefits from a machine-readable citation file. The audit scores
  it, so skipping it leaves free points on the table.
- **Vendored code check:** Do any third_party/vendor directories have their own
  licenses that conflict with the project license?
- **Edge case flags** -- flag these for the user's attention (do not attempt to
  resolve them, recommend consulting an attorney):
  - Dual licensing situations
  - CLA (Contributor License Agreement) requirements from upstream
  - Trademark usage (e.g., using upstream project's name in your project name)
  - AGPL/network copyleft implications for SaaS deployment
  - License header requirements in individual source files (GPL, Apache)

### 3. Recommend

**Start every recommendation output with the disclaimer block (see above).**

Every recommendation must cite its source:
- "Based on your intent (open source community), MIT is recommended for maximum adoption"
- "Based on upstream license (Apache 2.0), you must maintain the NOTICE file"
- "Based on dependency analysis, your GPL dependency requires your project to be GPL-compatible"
- "Upstream project detected: [project] is licensed under [license] -- your project
  must comply with those terms"

Reference: Read `github/references/license-guide.md` for compatibility matrix and fork obligations.

**When edge cases are detected, flag them clearly:**
```
> REQUIRES HUMAN REVIEW: [description of the edge case]
> This situation is beyond automated analysis. Consult a qualified attorney.
```

Do NOT attempt to resolve ambiguous or complex legal questions. Flag them, explain
why they're complex, and recommend professional review. Better to say "I don't know,
get a lawyer" than to give wrong advice.

### 4. Execute (with user approval)

**Confirmation gate -- STOP and present before writing any files:**
After completing the Recommend step, present the user with:
1. A summary table of files that will be created or modified
2. The specific changes (e.g., "Add modification copyright to LICENSE")
3. Any placeholders they'll need to fill in

Wait for the user to confirm before proceeding. If running inside the
orchestrator (`github` or `github-audit`), skip the confirmation gate
and proceed -- the orchestrator has already obtained user consent.

**Author info for CITATION.cff:** Pull the author name from `git config user.name`
first. If not set, use the GitHub username from `gh api user --jq .name`. If neither
is available, use the repo owner's login as a fallback and note it as a placeholder.

**Write to shared data cache** after generating legal files:
```bash
mkdir -p .github-audit
grep -qxF '.github-audit/' .gitignore 2>/dev/null || echo '.github-audit/' >> .gitignore
```
Write `.github-audit/legal-data.json` with: timestamp, license_type, license_file_exists,
license_file_path, security_md_exists, security_md_path, citation_cff_exists,
notice_file_exists, is_fork, fork_compliant, dependency_conflicts array.
Reference: `github/references/shared-data-cache.md` for exact schema.

- Generate LICENSE file with correct year and copyright holder
- Generate SECURITY.md with supported versions and reporting process
- **Generate CITATION.cff by default** -- always include in the deliverables table.
  Only skip if the user explicitly says they don't want it. Do not skip silently.
  If the user hasn't mentioned it, generate it and include it in the confirmation gate.
  Pull version from latest git tag or `gh release list`. Pull date from today's date.
  Pull author from `git config user.name` or `gh api user --jq .name`.
- Generate NOTICE file if Apache 2.0
- Fix fork attribution if needed

## License Selection by Intent

| Intent | Default | Reasoning |
|--------|---------|-----------|
| Open Source Community | MIT | Maximum adoption, minimal friction |
| Professional Portfolio | MIT | Simple, universally understood |
| Business / Brand | Apache 2.0 | Patent protection for enterprise users |
| Internal to Public | Apache 2.0 | Patent grant protects company and users |
| Academic / Research | MIT or BSD-3 | Academic tradition, simple attribution |
| Hobby / Learning | MIT | Simplest option |
| Keep forks open | GPL v3 | Copyleft ensures derivatives stay open |
| SaaS / Server app | AGPL v3 | Copyleft covers network use (prevents closed SaaS forks) |
| Library used by proprietary code | LGPL v3 | Linking exception lets proprietary apps use it |
| Balanced copyleft | MPL 2.0 | File-level copyleft (modified files stay open, new files can be anything) |
| Public domain / no restrictions | Unlicense or CC0 | Maximum freedom, zero obligations |
| Documentation / data | CC BY 4.0 or CC0 | Creative Commons designed for non-code content |
| Source-available commercial | BSL 1.1 | Visible source but not free to compete with; converts to open after delay |

**When upstream exists:** The upstream license constrains your options. You cannot
choose a less permissive license than what the upstream allows. Examples:
- Upstream is MIT → you can use MIT, Apache, GPL, AGPL, or anything else
- Upstream is GPL v3 → you MUST use GPL v3 (or later). You cannot use MIT or Apache.
- Upstream is Apache 2.0 → you can use Apache 2.0, GPL v3, or AGPL v3 (not MIT,
  because Apache has patent grant terms that MIT doesn't preserve)

## Fork and Upstream Compliance Checklist

When the repo is a fork OR has a detected upstream project:
- [ ] Original license preserved in LICENSE file
- [ ] Original copyright notice preserved
- [ ] Your copyright added below original (format: "Copyright (c) YEAR NAME (modifications)")
- [ ] NOTICE file preserved (if Apache 2.0)
- [ ] Changes documented (if required by license -- GPL and Apache require this)
- [ ] License compatibility verified with any new dependencies
- [ ] Upstream relationship acknowledged in README (for non-fork upstream projects)
- [ ] Your chosen license is compatible with the upstream license (see matrix above)

## SECURITY.md Template

Generate based on:
- Current release versions (from `gh release list`)
- Project contact info (from git config or user input)
- Severity-based response timelines

## CITATION.cff Template

```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
type: software
title: "[Project Name]"
version: "[version]"
date-released: "[YYYY-MM-DD]"
authors:
  - family-names: "[Last]"
    given-names: "[First]"
    orcid: "https://orcid.org/XXXX-XXXX-XXXX-XXXX"  # optional
url: "https://github.com/[owner]/[repo]"
license: "[SPDX-ID]"
```

## Output

- Files generated/updated (with diff preview)
- Compliance status: PASS / FAIL with specific issues
- Fork compliance: PASS / FAIL / N/A
- Dependency license conflicts: list any found

### Next Step

After completing legal fixes, always end with this handoff:

```
Legal fixes complete. Next recommended step:
  github-community -- set up community health files and templates
```

If running as part of the audit SOP (the user ran `github-audit` first and is
following the Recommended Next Steps table), reference the step number:
"Step 1 complete. Next skill: `github-community`"

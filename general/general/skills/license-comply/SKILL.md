---
name: license-comply
title: 'License comply'
description: Use when auditing open-source dependency licenses in Python projects, generating compliance reports, or checking license risk in your codebase.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/license-comply
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [open-source, license, compliance, cli, python, security]
---

# license-comply

## When to Use

- Auditing a Python project's dependency license compliance
- Generating license risk reports for legal/engineering review
- CI/CD integration for automated license checks
- Reviewing third-party library license terms before adoption
- Creating software bill of materials (SBOM) for compliance

## Audience and Work Shape

Audience: non-lawyer engineers running a CI-gated dependency scan, and the in-house counsel / open-source review function those engineers escalate to. Not intended as a stand-alone clearance tool for engineering teams without a counsel-in-the-loop on flagged findings.

Work shape: Pattern-Matched Review for license detection (license string -> SPDX -> policy band). The "AI executive summary" and "plain-English explanations" features are advisory framing, not judgment work, and must not be relied on as legal advice or as a substitute for counsel review.

## Scope and Legal Use

This skill provides legal *support*, not legal advice. A "low risk" classification means "the detected SPDX identifier is on the configured allow-list" — it does not mean "this dependency is safe to ship in your product," "this license is compatible with the rest of your stack," or "your use of this code is compliant."

Three legal failure modes this skill explicitly addresses:

1. **Legal advice vs. legal support.** The report is advisory. Risk bands, remediation text, plain-English explanations, and the optional AI executive summary are detection output, not legal conclusions. They do not constitute legal advice and must not be circulated to leadership as a clearance.
2. **Privilege implications.** CI-generated reports are discoverable artefacts by default. If counsel wants the manual-review layer to sit inside privilege, counsel must mark up the report under privilege themselves; running the CLI in CI does not create work product. Treat raw CI artefacts as non-privileged.
3. **Accountability gap.** The tool is CI-gated and aimed at non-lawyer engineers. Without an explicit gate, an engineer can merge against a license violation without legal review — the `--fail-on=high` flag exits non-zero but can be silently bypassed in CI configuration, and the AI executive summary lets leadership consume a license posture with no counsel in the loop. **Review required by qualified open-source / IP counsel before merging changes flagged Medium or High.** The CI gate is not a substitute for that review.

## How It Works

### Core Functionality

Scans Python projects for dependency license risks using a customizable policy engine.

### Features

- **Risk ratings** — Classifies licenses as low/medium/high risk (see Confidence Bands below for criteria and required action)
- **Plain-English explanations** — Non-lawyers can understand the findings (advisory; not legal advice)
- **Remediation steps** — Actionable guidance for each flagged issue (advisory; counsel review still required on Medium/High)
- **Multiple output formats** — JSON, CSV, HTML, Markdown
- **CI integration** — GitHub Actions, GitLab CI, pre-commit hooks
- **AI executive summary** — Optional LLM-powered overview for leadership (advisory; explicitly not legal advice; must not be circulated as a clearance)

### Installation

```bash
pip install license-comply
```

### Usage

```bash
# Scan current directory
license-comply scan .

# CI mode (exit non-zero on violations)
license-comply scan . --fail-on=high

# Generate HTML report
license-comply scan . --format=html --output=report.html

# Custom policy
license-comply scan . --policy=/path/to/policy.yaml
```

### Policy Engine

Define your organization's license policy:

```yaml
allowed_licenses:
  - MIT
  - Apache-2.0
  - BSD-3-Clause

restricted_licenses:
  - AGPL-3.0
  - CC-BY-NC-4.0

flagged_licenses:
  - GPL-2.0: "Consult legal before use"
```

## Confidence Bands

- **Low** — detected SPDX identifier matches the configured allow-list cleanly. Engineer may proceed without counsel review for this dependency. (Still subject to overall counsel review of new dependencies per your team policy.)
- **Medium** — license detected with caveats (ambiguous SPDX string, unusual clause variant, dual-license declaration where one option is allow-listed and one is not, or licence in the `flagged_licenses` policy bucket). **Counsel review required before merge.** Do not rely on the plain-English explanation as clearance.
- **High** — viral copyleft (GPL/AGPL family) detected against a proprietary target, restricted-license hit, commercial-use restriction, or any policy `--fail-on=high` trigger. **Counsel review required before merge. Escalate.** CI gate must not be bypassed.
- **Unknown / Review** — license string undetectable, missing, custom, or not in the SPDX list. Do not present as `low`. **Counsel review required before merge. Escalate.**

Output is *advisory, not legal advice*, regardless of band.

## Out of Scope

- Python projects only (pip/requirements.txt/pyproject.toml). Does not cover non-Python dependencies in containers, system packages, or vendored binaries.
- Does not assess license *compatibility* between dependencies, only per-dependency classification against your policy.
- Does not cover patent grants, contributor license agreement (CLA) gaps, trademark, export-control, or end-user license terms.
- Does not detect license drift across versions of the same package — re-scan on every dependency bump.
- Does not constitute open-source clearance, OSS-program-office sign-off, or any form of legal opinion.
- If you hit an out-of-scope case, route to counsel rather than treating absence of a finding as a green light.

## Escalation

Stop, do not merge, and route to qualified open-source / IP counsel when:

- any finding is classified **Medium** or **High**;
- **any GPL / LGPL / AGPL contamination** is detected against a proprietary or closed-source target (whether direct or transitive);
- **dual-license conflicts** are detected (e.g. one option allow-listed, one not; or unclear which license governs);
- **unfamiliar, custom, or non-SPDX licenses** appear in the report;
- license detection fails or returns "unknown";
- the CI `--fail-on` gate trips;
- the user is preparing to circulate the AI executive summary or any report artefact to leadership as a clearance.

When escalating, include: package name, version pin, license text as detected, dependency-graph location (direct vs. transitive, parent package), and the business use of the package.

## Limitations

- Python projects only (pip/requirements.txt/pyproject.toml)
- Does not cover non-Python dependencies in containers
- License detection only — no legal advice

## QA Remediation (LegalQuants, 2026-05)

Original author: Sam Clearwater. LegalQuants remediated this skill on 2026-05 against the Legal Skill Design Framework, addressing the three legal failure modes (legal advice vs. legal support, privilege implications, accountability gap), adding explicit audience / work shape / confidence-band / out-of-scope / escalation sections, and inserting an explicit "qualified open-source / IP counsel review required before merging Medium or High findings" gate to close the accountability gap for non-lawyer engineers running the CI tool. Technical content (installation, usage, policy engine) is unchanged. Output remains *advisory, not legal advice*.

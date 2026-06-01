---
name: compliance-trestle-engineering
title: Compliance Trestle Engineering
description: Use Compliance Trestle to manage OSCAL catalogs, profiles, component definitions, SSPs, markdown assembly, validation, and source-traceable updates from legacy compliance documents.
author: ethanolivertroy
author_url: https://github.com/ethanolivertroy/compliance-trestle-skills/tree/main/agent-skills/compliance-trestle-engineering
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
tags: [compliance-trestle, oscal, ssp, grc]
---

# Compliance Trestle Engineering

Use this skill when an agent needs to operate a Compliance Trestle workspace, import or validate OSCAL models, assemble markdown, regenerate OSCAL, or turn legacy SSP content into a traceable Trestle-managed workflow.

## Non-negotiable guardrails

- Preserve source traceability for every generated OSCAL field that came from a legacy PDF, DOCX, Markdown, TXT file, interview note, spreadsheet, ticket, or evidence package.
- Never invent control mappings. If the source does not clearly support a mapping, set status to `needs_review` and explain the uncertainty.
- Schema-valid OSCAL is not a statement of compliance effectiveness.
- Keep reviewer-owned decisions in review queues or traceability maps, not hidden in generated prose.
- Prefer small, reversible Trestle operations over large opaque rewrites.

## Standard workflow

1. Initialize or inspect the workspace.
   - `trestle init`
   - `trestle version`
   - `find . -maxdepth 3 -type d | sort`
2. Import or create OSCAL artifacts.
   - catalogs under `catalogs/`
   - profiles under `profiles/`
   - component definitions under `component-definitions/`
   - SSPs under `system-security-plans/`
3. Resolve the applicable profile before writing control implementations.
4. Author or update markdown with source references.
5. Assemble markdown back into OSCAL.
6. Validate with Compliance Trestle and any available OSCAL validator.
7. Generate review outputs for `needs_review`, unmapped, or low-confidence items.

## Typical commands

Use the wrapper when you want consistent reports:

```bash
bash scripts/trestle-workflow.sh init workspaces/acme/trestle-workspace
bash scripts/trestle-workflow.sh validate workspaces/acme/trestle-workspace
bash scripts/trestle-workflow.sh assemble workspaces/acme/trestle-workspace system-security-plans/acme-ssp
bash scripts/trestle-workflow.sh status workspaces/acme/trestle-workspace
```

Use raw Trestle when the reviewer needs exact CLI control:

```bash
trestle init
trestle validate -a
trestle author ssp-generate -n acme-ssp -p profiles/fedramp-moderate/profile.json
trestle author ssp-assemble -m markdown/system-security-plans/acme-ssp -o system-security-plans/acme-ssp.json
```

## Output expectations

Every Trestle-backed document import should leave behind:

- `source-map.csv` with source IDs, target OSCAL fields, status, and notes.
- `reports/import-summary.md` explaining source counts and known gaps.
- `reports/review-queue.md` for `needs_review` and unmapped items.
- validation output from `trestle validate` or a documented skipped/missing-tool status.

See:

- `references/trestle-workspace-lifecycle.md`
- `references/trestle-oscal-operations.md`
- `templates/trestle-workflow-checklist.md`
- `templates/trestle-command-log.md`

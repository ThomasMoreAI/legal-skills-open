---
name: oscal-document-engineering
title: OSCAL Document Engineering
description: Convert, validate, and maintain OSCAL documents from legacy SSP/PDF/DOCX/Markdown source material.
author: ethanolivertroy
author_url: https://github.com/ethanolivertroy/compliance-trestle-skills/tree/main/agent-skills/oscal-document-engineering
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
tags:
- oscal
- ssp
- compliance-trestle
- document-transformation
- grc
sources:
- title: Legacy doc ingestion
  path: references/legacy-doc-ingestion.md
- title: Oscal validation
  path: references/oscal-validation.md
---

# OSCAL Document Engineering

Use this skill when a user wants to turn old compliance documents into maintainable OSCAL.
Typical outputs are SSPs, SAPs, SARs, POA&Ms, component definitions, and evidence packages.

## Core rule

Every OSCAL statement must be traceable to source text, collected evidence, or a user-supplied assertion.
If the source is unclear, mark the item `needs_review`.
Do not invent a compliance fact.

## Inputs

Common inputs:

- SSP in PDF, DOCX, Markdown, or text.
- Existing OSCAL JSON, XML, or YAML.
- Evidence folders, diagrams, inventories, policies, or POA&M spreadsheets.
- Framework or profile target such as FedRAMP Moderate, NIST 800-53, SOC 2, ISO 27001, or organization-specific profiles.

## Outputs

Make these artifacts:

- OSCAL workspace or package.
- `source-traceability-map.csv`.
- `ssp-import-plan.md`.
- `import-summary.md`.
- `validation-report.json` or a Markdown equivalent.
- `unmapped-items.md` that lists content that needs human review.

## Workflow

1. Make sure you know the source files and the target OSCAL document type.
2. Make a workspace outside committed source unless you use a synthetic example.
3. Extract text. Keep page numbers, headings, and section identifiers when possible.
4. Build a source traceability map with `templates/source-traceability-map.csv`.
5. Start or update a Compliance Trestle workspace.
6. Draft a schema-valid SSP from extracted sections when Trestle is available:

```bash
bash plugins/document-transform/oscal-document-workbench/scripts/draft-ssp-from-extraction.sh <workspace> --overwrite
```

The FedRAMP Rev 5 heading map at `plugins/document-transform/oscal-document-workbench/templates/fedramp-rev5-heading-map.json` is an optional adapter for FedRAMP-style SSPs.
For SOC 2, ISO 27001, or other sources, keep unmatched sections `needs_review`.
Do not force FedRAMP field targets.
7. Refine mappings and fill remaining OSCAL SSP structure:
   - metadata
   - parties and roles
   - system characteristics
   - system implementation
   - control implementation
   - inventory items
   - back matter resources
8. Validate with Compliance Trestle and OSCAL CLI when available.
9. Make summary reports and identify gaps.
10. Ask the user or system owner to review all `needs_review` items.

## Mapping guidance

- Map document title, version, system name, owner, and dates into OSCAL metadata.
- Map authorizing officials, system owners, ISSOs, assessors, and service providers into parties and responsible roles.
- Map boundary descriptions, data types, users, deployment model, and interconnections into system characteristics.
- Map components, services, accounts, inventories, and cloud resources into system implementation.
- Map control narratives by control ID into control implementation statements.
- Map attachments, diagrams, policies, and evidence into back matter resources.

## Validation commands

Use commands that are available in the local environment. Examples:

```bash
trestle validate -f <path-to-ssp.json>
trestle validate -a
oscal-cli validate --disable-constraint-validation <path-to-ssp.json>
```

If a validator is missing, report the missing dependency.
Continue only if the user accepts partial validation.

## References

- `references/legacy-doc-ingestion.md`
- `references/oscal-validation.md`
- `templates/ssp-import-plan.md`
- `templates/source-traceability-map.csv`

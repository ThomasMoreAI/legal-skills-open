---
name: swiss-trademark-deposit-self-tech-labs
title: Depot de marque en Suisse
description: Prepare Swiss trademark deposits before the IPI. Use for protecting a name or logo in Switzerland, choosing Nice classes, drafting goods/services labels, assessing absolute grounds, or preparing a Swiss trademark anteriority search.
author: self-tech-labs
author_url: https://github.com/self-tech-labs/ogram-for-IP/tree/main/plugins/swiss-trademark-deposit/skills/swiss-trademark-deposit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ch
practice: ip
language: fr
sources:
- title: Classification Nice
  path: references/classification-nice.md
- title: Motifs Absolus
  path: references/motifs-absolus.md
- title: Procedure Depot
  path: references/procedure-depot.md
- title: Recherche Anteriorite
  path: references/recherche-anteriorite.md
---

# Depot de marque en Suisse

## Posture

Default to a clear business register for entrepreneurs and creators. Switch to a practitioner register when the user signals legal expertise, cites statutes or procedure, asks for absolute grounds, opposition, coexistence, TAF/TF jurisprudence, WDL, Swissreg, or Nice class drafting.

Always state that the analysis is preparatory: it does not guarantee registration, absence of opposition, or replace specialist legal advice for significant matters.

## Connected Sources

Use the four local MCP servers as the canonical source for data retrieval:

- `nice-headings`: `get_nice_heading` and `list_nice_headings` for official Nice headings; `filing_intake_check` and `filing_requirements_snapshot` for filing readiness, official-language, fee, timing, and source-date checks.
- `wdl`: `search_wdl`, `get_wdl_terms_by_class`, and `validate_term` for IPI/WDL labels.
- `swissreg-corpus`: `search_swissreg_terms`, `get_class_combinations`, `get_sector_benchmark`, `list_mandataires`, and `swissreg_mark_detail` for professional Swissreg examples and class-combination calibration.
- `taf-decisions`: `search_taf_decisions`, `get_taf_decision`, `find_similar_signs`, and `sign_risk_screen` for absolute-ground screening and precedents.
- `corpus_stats` and `source://manifest` report corpus dates, counts, version, freshness, TAF extraction confidence, and limits.

The Swissreg source exposes mandataire groups as filter metadata, but does not map every goods/services row to a mandataire; the facet IDs do not join to mark IDs. If a mandataire filter is requested, surface the `mandataire_filter_applied: false` limitation instead of pretending that row-level filtering was applied.

Do not present an unsupported label as pre-approved. Prefer a matching WDL term; when the applicant needs custom wording, draft it precisely, mark it as custom, and require verification in the live IPI classification tool. Nice headings orient classification but do not cover every good or service in a class.

## References

Consult these local references for legal and workflow depth:

- `references/motifs-absolus.md` for distinctiveness, descriptiveness, deceptive signs, official signs, indications of provenance, and imposed marks.
- `references/classification-nice.md` for class selection and label drafting.
- `references/procedure-depot.md` for IPI filing procedure, costs, timelines, and post-filing issues.
- `references/recherche-anteriorite.md` for Swissreg/TMview/BrandDB/Madrid/Zefix search strategy.

Use references systematically in practitioner mode and whenever a sign is borderline or a classification issue is atypical.

## Workflow

1. Understand the applicant activity. If a website or description is unavailable, ask for a short activity description before making recommendations.
2. Identify the sign: verbal, figurative, combined, 3D, color, sound, or another form. For figurative/combined signs, ask for or inspect the visual and describe it neutrally.
3. Run `filing_intake_check` when the request is a full filing preparation or the facts are incomplete. Confirm applicant, sign representation, sign type, goods/services, priority, territory, planned use, and risk tolerance.
4. Run `sign_risk_screen` before the TAF search. For borderline signs, search TAF decisions and similar local signs before classifying the risk. Treat `find_similar_signs` as local structural/lexical support, not embeddings.
5. Prepare anteriority search strategy with `clearance_search_plan`. The plugin does not perform a complete Swiss clearance search; explain that IPI does not examine relative grounds and opposition risk remains.
6. Identify Nice classes from business activities. Use `get_class_combinations` and `get_sector_benchmark` for comparable sectors where helpful and state whether class-combination counts are exhaustive for the local corpus or query-limited.
7. Draft labels from the applicant's actual and planned commercial activity: use Nice headings to orient the class, WDL terms for accepted wording, Swissreg examples for calibration, and a precise custom limitation only when necessary. Never claim an entire heading merely because the business touches one item in it.
8. Run `filing_requirements_snapshot` for fee/timing/source reminders in full filing outputs.
9. Deliver an actionable filing memo: sign/type, applicant gaps, risks, classes, full labels, official-language status, sources, anteriority strategy, cost reminder, filing link, and next steps.

## Interaction Rules

Ask entrepreneurs questions in business language, not class numbers. Ask only for decisions that affect protection scope: actual activities, product/service commercialization, planned extensions, geography, and risk tolerance.

For practitioners, provide source-backed reasoning, cite statutes and precedents only where the source supports the proposition, and mark uncertainty explicitly. Never infer a holding from an extracted title or snippet alone; retrieve the full local entry and recommend checking the official decision for material reliance.

When source data is partial, say so. Swissreg is a professional example corpus, not a complete anteriority search.

If a tool refuses an unsupported filter, surface the limitation rather than reproducing a result as if the filter had worked.

## Output Discipline

For each recommended class, include:

- the class number and business reason;
- the Nice heading or relevant part;
- drafted labels separated by semicolons;
- WDL/Swissreg support summary;
- a limitation clause when the class heading overreaches the activity.

For filing-ready outputs, also include:

- corpus date and Nice version;
- official-language status of the goods/services list;
- whether live clearance has been performed or only planned;
- current stored fee estimate with a reminder to verify the IPI source at filing time;
- post-filing watch items: Swissreg publication, three-month opposition window, and five-year use requirement.

Always recommend verification of current IPI fees, accepted wording, and filing requirements at the official source at the moment of deposit. Never describe a planned or local-corpus search as a completed live clearance search.

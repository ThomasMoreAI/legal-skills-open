---
name: request-basis-lilialla
title: Request Basis
description: Use for PRC civil-law request-right basis analysis, including Gutachtenstil study cases, litigation evidence-to-elements analysis, law/case verification planning, catalog building, and incremental integration of books, papers, laws, judicial interpretations, minutes, cases, and user checklists into request-basis rule-obligation groups. Trigger when the user asks about 请求权基础, 鉴定式案例分析, 案由-诉请-请求权基础映射, 民事请求权要件, 抗辩/反抗辩, 规则义务群, or building/maintaining the request-right skill catalog.
author: lilialla
author_url: https://github.com/lilialla/request-right-skill-reference/tree/main/skills/request-basis
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: litigation
language: en
sources:
- title: Classification
  path: references/classification.md
- title: Concept
  path: references/concept.md
- title: Concept Cards
  path: references/concept_cards.md
- title: Discretion
  path: references/discretion.md
- title: Lite Runtime
  path: references/lite_runtime.md
- title: Methodology
  path: references/methodology.md
- title: Norm Decomposition
  path: references/norm_decomposition.md
- title: Output Templates
  path: references/output_templates.md
- title: Real Case Testing
  path: references/real_case_testing.md
- title: Request Lifecycle
  path: references/request_lifecycle.md
- title: Retrieval
  path: references/retrieval.md
- title: Rule Obligation Groups
  path: references/rule_obligation_groups.md
- title: Source Integration
  path: references/source_integration.md
- title: Source Policy
  path: references/source_policy.md
- title: Source Synthesis
  path: references/source_synthesis.md
- title: Verification
  path: references/verification.md
---

# Request Basis

This skill routes PRC civil request-right basis work. It is not a shortcut to a final legal opinion. Use it to keep method, source labels, evidence discipline, and MCP/authority verification separate.

## Quick Protocol

1. Classify the use scenario before the work mode: student study, real litigation, real arbitration, research, or catalog/build.
2. For ordinary legal tasks, use lite runtime first; load only the selected logical mode plus references needed by that mode.
3. Identify the claim goal before using cause-of-action labels.
4. For each request basis analyzed in detail, apply the request lifecycle: right arises, not extinguished, exercisable, defenses/counter-defenses.
5. Use controlled concept cards for professional terms when available; create a temporary concept card when absent.
6. Use rule-obligation groups as scaffolding, not as verified law.
7. If no local rule-obligation group fits, generate a temporary candidate group and label it `model_inference`.
8. Search local materials only for targeted snippets.
9. For new materials, extract atomic source assertions before merging them into concept cards or rule-obligation groups.
10. For reference integration work, use source synthesis to group sources by request-basis family before changing runtime rules.
11. Output uncertainty, verification needs, and excluded paths explicitly.
12. For real case pilots, use the real-case-testing reference and keep reusable lessons abstract.

## Scenario Router

Pick a scenario before mode selection:

| Input or goal | Scenario | Extra discipline |
| --- | --- | --- |
| Teaching case, exam prompt, student answer | Student study | Given facts may be treated as study facts; focus on Gutachtenstil. |
| Pleadings, contracts, evidence, client/opponent narratives for court | Real litigation | Use litigation mode, strict fact/evidence separation, procedure/retrieval labels. |
| Arbitration agreement, arbitration request/defense, tribunal-facing analysis | Real arbitration | Use arbitration mode; add jurisdiction, tribunal, evidence exchange, award-enforceability checks. |
| Current law, judicial interpretation, court/arbitral practice, case-law path | Research | Use research mode and authority verification tasks. |
| Skill, catalog, source, schema, eval, OCR, or glossary maintenance | Catalog/build | Use catalog builder mode and source integration rules. |

## Mode Router

Pick one mode before analysis:

| Input | Mode | Resource ID |
| --- | --- | --- |
| Clean study facts, exam-style prompt, student draft answer | Exam mode | `mode.exam` |
| Contracts, evidence, pleadings, client/opponent narratives | Litigation mode | `mode.litigation` |
| Arbitration materials, tribunal-facing strategy, arbitral claims/defenses | Arbitration mode | `mode.arbitration` |
| Law, judicial interpretation, case-law, court practice, dispute issue research | Research mode | `mode.research` |
| Extracting catalog entries, integrating new materials, or maintaining rule-obligation groups | Catalog builder mode | `mode.catalog_builder` |

If input is mixed, prefer litigation mode because it has the strictest fact/evidence discipline.

Resolve resource IDs through the co-located resource manifest. If the manifest or a resource is absent in a distributed package, use the fallback rule for that resource and say what was unavailable. Do not expose resolved local filesystem paths in legal outputs.

If the user's goal is to build or maintain this skill, use catalog builder mode plus the available structured resources. Do not load core books wholesale.

## Lite Runtime

For ordinary student, litigation, arbitration, and research tasks, keep only these layers visible: scenario, claim goal, fact/evidence separation, request lifecycle, material concept cards, temporary rule-obligation groups when needed, norm decomposition for selected detailed bases when precision is requested, and source/verification labels.

Keep schema details, resource manifest mechanics, generated indexes, candidate batches, and validation internals in the maintenance layer unless the user is maintaining the skill.

## Global Rules

- Local books and OCR materials are method/catalog seeds, not final law.
- Do not quote or carry local materials forward verbatim unless a short excerpt is needed for traceability; convert them into structured propositions and source assertions.
- Do not assume every mention of 案由, 诉请, 法条, 法律关系, or evidence is a request basis. If unclear, apply the request-basis concept tests.
- Do not let one cause of action replace request-basis analysis. Use request goal, party roles, candidate request bases, and rule-obligation groups for substance; use candidate causes of action for filing, retrieval, and calibration.
- Do not let professional terms float on model intuition alone. If a term is material, route it through the concept-card layer or mark a temporary concept card.
- When a local rule-obligation group matches the task, use it as the bridge from claim target to request bases, elements, defenses, evidence targets, and candidate causes of action.
- When academic precision is needed, unpack the selected request basis through main norms, auxiliary norms, defense norms, counter-defense norms, extinguishment, and exercisability; do not expand unrelated branches.
- When no group matches, build a temporary group with trigger facts, candidate terms, request goals, candidate bases, defenses, evidence targets, and verification tasks; do not force the facts into a single cause of action.
- Do not expand rule-obligation groups into every remotely related article or doctrine. Use core rules, conditional triggers, linked modules, and verification tasks.
- Do not suppress a plausible path just because it is absent from seed data. Keep it as a labeled candidate if trigger facts, norm function, evidence target, and verification need can be explained.
- Do not store real case facts as skill examples; convert only abstract, repeatable failure patterns into evals or references.
- Without MCP or another authoritative source, do not state current law as verified.
- Without case-law research, do not say courts usually or generally hold a position.
- Do not treat party statements as found facts.
- Every analyzed request basis must visibly pass through: right arises, not extinguished, exercisable, defenses/counter-defenses.
- When analyzing a real-matter request basis, every cited statute, judicial interpretation, exchange rule, or formal regulatory rule that supports a right-arises/not-extinguished/exercisable/defense conclusion must be cited by exact article number and relevant original text. Do not write only "relevant provisions" or only list article numbers.
- Before relying on a company-law provision, verify the subject type and norm addressee: listed company, public company, company limited by shares, limited liability company, parent/subsidiary, target company, shareholder, director, or information-disclosure obligor. Do not use limited-liability-company provisions to support a listed-company procedure, disclosure, or minority-shareholder-protection conclusion. If a limited-liability-company provision is relevant only because the target company or subsidiary is an LLC, state that limitation expressly and use securities law/exchange rules for the listed-company layer.
- Legal footnote layout should use one article number as one heading unit. If the relevant text within the same article is continuous, quote it continuously under that article number; do not split it into labels such as "first sentence" or "second sentence". If the relevant parts are not continuous, list the needed paragraphs/items under the same article heading.
- When citing an item, sub-item, exception, enumerated circumstance, or defined category, include the chapeau or lead-in sentence needed to understand the item in context. Do not quote a standalone item such as "放弃权利..." or an "除外" phrase if the reader cannot tell what list, definition, or rule it belongs to. Do not use ellipses to splice a lead-in and later item; either quote the continuous text or format selected non-continuous items separately under the article heading.
- For repeated citations to the same source and same supporting point, make the first citation complete and later citations shortened with "同前注 + source/article/page + supported point"; do not repeat the same long footnote text verbatim.
- Run a separate relevance pass for every legal citation: identify the exact proposition, element, proof matter, defense, or procedural threshold the cited sentence supports. Remove citations that only look generally related, are cumulative without need, or do not support the specific sentence in the draft. A dense legal footnote may state the supported proposition, but should not add unnecessary negative explanations.
- Always list candidate request bases not analyzed in detail and explain why.
- Label material claims using the source-policy reference.

## Context Budget

- Keep the skill entry, mode files, and reference files readable in one pass.
- Treat structured data resources as row stores; filter by id, path, claim text, term, or source id.
- Treat source locator indexes as locators, not reading material.
- Never load large source materials wholesale; use targeted retrieval and then read only the relevant lines.

## Shared References

Read only what is needed, resolved by logical role:

- `reference.source_policy`: source labels, verification status, hard output bans.
- `reference.lite_runtime`: minimal runtime surface for ordinary legal tasks.
- `reference.discretion_policy`: hard guardrails, flexible scaffolding, and exploration rules.
- `reference.request_basis_concept`: operational definition and disambiguation tests for 请求权基础.
- `reference.concept_cards`: controlled professional-term layer and temporary concept card protocol.
- `reference.request_lifecycle`: four-gate analysis for every detailed request basis.
- `reference.classification`: case entry classification and cause-of-action limits.
- `reference.rule_obligation_groups`: intermediate rule/obligation/element/defense knowledge unit.
- `reference.norm_decomposition`: recursive main/auxiliary/defense/counter-defense norm trees for high-precision analysis.
- `reference.source_integration`: adding new sources without source sprawl.
- `reference.source_synthesis`: grouping reference materials into request-basis families and coverage gaps.
- `reference.real_case_testing`: piloting real matters without turning private facts into permanent training material.
- `reference.verification`: creating and consuming authority verification tasks.
- `reference.retrieval`: searching local source materials without loading large files.
- `reference.methodology`: request-basis method, three layers/four steps, practice-vs-study distinction.
- `reference.output_templates`: reusable output skeletons.

## Data Files

When working inside this repository or a distributed package, use available structured resources by role:

- schemas for structure;
- request-basis seed entries;
- rule-obligation seed groups;
- request-basis synthesis entries;
- norm decomposition seed entries;
- verification queue entries;
- catalog review batches;
- defense seeds;
- eval tasks and rubrics;
- local evaluation tools when present.

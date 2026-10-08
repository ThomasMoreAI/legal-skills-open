---
name: legal-os-litigation-384363367-dot
title: Legal OS Litigation
description: Source-locked Chinese litigation workflow covering litigation analysis, evidence mapping, legal research, and quality-gated pleading documents. Use when reviewing a litigation matter, organizing facts and evidence, checking current legal authority, drafting a complaint/defence/arbitration document, building an evidence catalogue, or preparing a source-traceable internal review package.
author: 384363367-dot
author_url: https://github.com/384363367-dot/legal-os/tree/main/skills/legal-os-litigation
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: cn
practice: litigation
language: en
sources:
- title: Case Research Handoff
  path: references/case-research-handoff.md
- title: Labor Arbitration Authority
  path: references/labor-arbitration-authority.md
- title: Pleading Drafting Rules
  path: references/pleading-drafting-rules.md
- title: Pleading Quality Gate
  path: references/pleading-quality-gate.md
- title: Workspace Contract
  path: references/workspace-contract.md
---

# Legal OS Litigation

Route a Chinese litigation matter through the private Legal OS workspaces in a fixed order. Keep the public skill generic and keep case facts, private evidence, internal strategy, and unverified legal propositions in the matter workspace only.

For external pleadings and procedural submissions, apply the public [external-expression boundary](../legal-os-unified-intake/references/external-expression-boundary.md) according to the receiving body and procedural duty. It limits unnecessary opponent disclosure but never suppresses a required procedural response or complete internal/client analysis.

## Office source policy

For pleading and evidence-catalogue DOCX artifacts, apply [the shared Office source policy](../legal-os-unified-intake/references/office-source-policy.md) before loading any document helper. Source structure, tracked changes and formatting properties are primary; for a formal pleading or evidence-catalogue DOCX, use one final visual QA pass when the current Runtime has reliable visual capability, otherwise remain conditional under the shared policy. An explicit user instruction not to render is a hard stop.

## Workflow

1. **Intake and role** — identify the procedural posture, party represented, requested outcome, deadlines, and the materials actually supplied. Confirm the current procedural or substantive objective and requested relief or defence scope before selecting an external route; if either is unresolved, keep it pending in internal analysis rather than completing it by inference. Do not invent missing facts. For an existing matter, treat the latest verified procedural status, judgment, new evidence and opponent position as the current authority; preserve superseded statuses only as history. For a new matter, separate confirmed facts from facts still requiring verification before choosing a theory.
2. **Litigation analysis** — build the issues, claims/defences, elements, disputed facts, procedural risks, and decision points. Separate facts from hypotheses and strategy.
3. **Evidence mapping** — map each material fact or proposition to an evidence item, source location, authentication/availability note, and gap status. Mark contradictions and missing originals.
4. **Legal and case research** — send current-law questions to the T-05 default `cn-legal-research` adapter and case-comparison questions to `cn-case-hub` when those capabilities are needed. `cn-law-hub` is a compatibility path only. Current-law outputs must identify version, effect, article/pinpoint and temporal application. Case outputs must identify source verification, procedure chain, relevance/direction matrix and decision-fork variables. Do not use a remembered rule or remembered case as a citation.
5. **Research-to-strategy handoff** — convert verified research into an action matrix before drafting: `decision-fork variable → matter fact → supporting/adverse evidence → evidence_gap → opponent attack → evidence action → argument/procedural action`. A high-relevance adverse case (`A-`) must be distinguished or expressly carried as risk; never omit it merely because it is adverse. See `references/case-research-handoff.md`.
6. **Paired pleading assembly** — use `legal-os-template-runtime` to resolve and hash-check the exact pleading template and its paired evidence-catalog template. For every complaint, application or answer, create both artifacts in the same drafting run. Preserve the fixed visual shell, but expand facts, claims/defences, legal grounds, calculations and subsections to the depth required by the matter. Keep evidence names, numbers, page ranges and proof purposes in the separate evidence catalogue, not in a standalone pleading section. Keep internal analysis out of the external version.
7. **Quality gate** — check fact–evidence–authority–relief/defence alignment, party identity, jurisdiction, amount, dates, case number, procedural posture, numbering, A4 layout, page numbers, evidence-table headers, cross-artifact numbering and template fidelity.
8. **Release boundary** — label outputs as draft, internal review, or final clean version. Filing, service, sending, signing, or other external action requires separate user authorization.

## Stop conditions

Stop and surface a review item when any material party identity, amount, date, case number, forum, legal relationship, requested relief, or core evidence is missing or contradictory. Stop when a legal proposition cannot be tied to a current verified source. Never fill a gap with a template, old memory, or inference.

## Document controls

- Support civil complaints and answers, commercial arbitration applications and answers, labour/personnel arbitration applications and answers, and evidence catalogues.
- Classify `procedure_type`, `pleading_role`, `pleading_stage` and `document_variant` before resolving a template. Do not use the commercial-arbitration template for a labour/personnel arbitration matter.
- For a claimant's initial complaint, arbitration application, payment-order application or equivalent first request, apply the initial-claim stance gate in `references/pleading-drafting-rules.md`: establish the represented party's claim affirmatively, keep speculative opponent arguments and response strategy in the internal workspace, and admit an exception only when it is actually raised or necessary to establish the claim or required procedure.
- Treat the public external-expression boundary and R13–R16 as a disclosure-selection layer for external pleadings; do not use it to suppress adverse facts, risk or complete analysis in internal or client-facing work.
- Every complaint, application or answer has `paired_evidence_catalog_required=true`. Generate the independent evidence catalogue even when evidence is incomplete; label it `待补证 / 内部草稿` rather than omitting it.
- Do not create an independent “证据和证据来源” or equivalent evidence-source chapter inside a complaint, application or answer. Court, tribunal or institution evidence requirements are satisfied through the paired evidence catalogue and evidence materials.
- Labour/personnel arbitration templates must not request arbitration costs from the opposing party. Article 53 of the PRC Labour Dispute Mediation and Arbitration Law states that labour-dispute arbitration is free of charge.
- Treat template sections as minimum functions, not a content ceiling. Never compress a complex pleading into sample placeholder prose merely to preserve the original paragraph count.
- Stop with `TEMPLATE_REQUIRED` if `legal-os-template-runtime` cannot select exactly one approved template; do not design a replacement from a blank document.
- Preserve traceability from each material statement to supplied material and, for legal propositions, to verified authority.
- Keep internal strategy and risk ratings in the internal package; remove them from any external-facing document.
- Use minimal, granular edits when editing an existing document; preserve wording unless the material is unsupported or a necessary protection is missing.
- Check the DOCX source for readable OOXML, complete text, numbering, tables, headers/footers, comments, font and paragraph properties, accessibility, and preservation of unchanged content.
- Keep related pleadings, evidence catalogues, written submissions and hearing statements substantively consistent in party identity, dates, amounts, legal relationship, performance and core facts; record the difference and legal effect when new evidence or procedure requires a change.

## References

- For the module contract and artifact boundaries, read `references/workspace-contract.md`.
- For the v0.7.0 case-research-to-strategy handoff, read `references/case-research-handoff.md`.
- For the reusable R1–R16 complaint/application/answer method, including the initial-claim stance gate, read `references/pleading-drafting-rules.md`.
- For the pleading quality gate and release labels, read `references/pleading-quality-gate.md`.
- For the verified legal basis of the labour-arbitration cost exclusion, read `references/labor-arbitration-authority.md`.

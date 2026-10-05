---
name: cite-check-legalquants
title: /cite-check
description: Verify supplied citations, check authorities, and detect hallucinated case law before filing. Use when the user asks to cite-check a brief, validate authorities, verify quotations, or catch fabricated citations.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-plugin-oss/tree/main/plugins/legalquants-litigation/skills/cite-check
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Australia
  path: references/authority-sources/australia.md
- title: Canada
  path: references/authority-sources/canada.md
- title: New Zealand
  path: references/authority-sources/new-zealand.md
- title: United Kingdom
  path: references/authority-sources/united-kingdom.md
- title: United States
  path: references/authority-sources/united-states.md
- title: Cite Check Rubric
  path: references/cite-check-rubric.md
- title: Document Context
  path: references/document-context.md
- title: Ethics And Jurisdictions
  path: references/ethics-and-jurisdictions.md
- title: Getting Authorities
  path: references/getting-authorities.md
- title: Lawyer Workflow
  path: references/lawyer-workflow.md
- title: Openai Codex Runtime
  path: references/openai-codex-runtime.md
- title: Parent Fanout
  path: references/parent-fanout.md
- title: Unit Review Prompt
  path: references/unit-review-prompt.md
---

# /cite-check

Use this skill to help a lawyer verify the substance of a filing, brief, motion, memorandum, or other legal document against the authorities that support it.

Cite checking legal work is a critically important accuracy task. Lawyers have an ethical duty to give their clients zealous, diligent advocacy, and a duty of candor to the tribunals they appear before. This means that a document prepared by a lawyer, even in the context of advocacy, must not contain an objectively false statement of law or fact or a material misstatement. Lawyers can engage in legitimate advocacy, so a brief or other advocacy submission does not necessarily need to prominently highlight counterarguments or limitations of a particular argument, but the arguments should be well-grounded in the applicable facts and law and not mislead the reader.

Your job is to apply the strongest possible legal analysis and verification capability. You are a frontier-level model, one of the greatest intelligences created, and you are capable of a thorough and superhuman scale coverage. In this context, ensure that you inspect carefully and consistently. Source text, context, and candid uncertainty control every result.

The lawyer remains responsible for the filing, the source set, applicable law, currentness research, and final professional judgment. Do not moralize, infer intent, or adjudicate misconduct from a citation flag. Identify the source or context problem so that the reviewing lawyer is aware of it and can exercise their professional judgment.

Begin with the short lawyer journey in [lawyer-workflow.md](references/lawyer-workflow.md).

## Inputs

Ask only for the target document, the authorities the lawyer wants checked, the intended use, and the tribunal, jurisdiction, and procedural posture when they could change the result. Ask no more than three focused questions in one turn. Ask for an as-of date only when timing or currentness matters. Do not turn an ordinary invocation into a legal-intake questionnaire.

If the target or authority set appears to be incomplete, explain the gap before reviewing. Use supplied source files first. Read [getting-authorities.md](references/getting-authorities.md) when the lawyer needs help obtaining authorities. If the lawyer has Westlaw access and their license permits using the downloaded material with external AI products, recommend retrieving separate, complete, readable authority files through the document-download path their subscription offers. Follow the [Westlaw acquisition guidance](references/getting-authorities.md#recommended-westlaw-workflow). A Westlaw download is an acquisition route, not proof of official publication, current good-law status, or complete citator treatment. A lawyer may instead supply their own PDF, DOCX, or other readable authority files.

For United States case law, search CourtListener or another available public source using citation metadata only. For another jurisdiction, use an available public source from the [jurisdiction-specific authority sources](references/getting-authorities.md#jurisdiction-specific-authority-sources). Do not upload the client brief. Report one simple outcome: the environment could not search; the search did not find the case and it may be hallucinated; or the case was found but was not supplied for substantive checking.

Treat the supplied readable sources as the evidence universe for checking what a citation says. A public search can show that a case was found, but it does not verify the brief's proposition unless the full case is added to the supplied authority set. Uploaded-source review does not establish Shepard's, KeyCite, later history, amendments, negative treatment, or comprehensive currentness.

Read [document-context.md](references/document-context.md) when preparing the target or authorities. Preserve original files, use the host's available document-reading capability, expose unreadable or incomplete material, and never silently invent extracted text.

## Step 1: prepare, inspect, and recommend

After the target and source-set questions are answered, read the brief and do one broad overview of the supplied authorities. Record the readable-file count, rough categories that appear present (for example cases, statutes, regulations, rules, record materials, or secondary sources), and categories that are not apparent or appear to be missing. This is a source-set overview, not a check of individual citations and not a parent citation census. Do not match citations to authorities before the per-unit review. If the source set is absent, explain that the run can check whether cited cases can be found but cannot verify what they say.

Run the packaged `scripts/cite_check.py`. It is the normal path and gives every prepared unit one fresh Codex session. The local probe only checks whether that script can run; it does not read the target or authorities. The probe is `scripts/probe_environment.py`. If the packaged script is unavailable on a host, keep the same one-unit assignments with host workers or process those assignments one at a time.

## Orchestration

Cite-checking needs real attention on every paragraph. The packaged script is the normal path: it orchestrates one fresh model session for each prepared unit. Do not combine paragraphs into a single review. If a host cannot run the packaged script, use the same one-unit assignments with its native workers or handle the assignments one at a time.

Give every session the same unit-review prompt, full rubric path, supplied authority inventory, assigned unit, bounded context, and result contract. In every execution path, retain one terminal receipt per prepared unit, give one targeted retry for mechanically incomplete evidence, render the HTML report, and perform one bounded sense check. An unresolved evidence problem remains amber. The legal scope, evidence universe, and result contract do not change with the host or scheduler.

## Method

Read [document-context.md](references/document-context.md) while preparing the target and authorities; it defines the host-native extraction, mechanical-unit, context-window, and coverage boundaries used below.

Follow the same four steps on every host. The portability contract is one terminal result per prepared unit; parallel workers are an available execution capability, not a requirement or a different legal method.

1. **Prep.** Use the host's document-reading capability to convert the target to Markdown or plain text. Make one mechanical unit for each extractable text container: paragraph, list item, table cell, heading, caption, footnote, endnote, header, footer, or text box. Preserve source order, assign stable `P####` or `F####` IDs, and record the exact text, file path, and line range. For each footnote, record the body unit that anchors it when known. Do not pre-filter units by whether they appear to contain citations. Complete the broad authority overview in Step 1, then run the passive environment probe before choosing an execution path. If no authorities were supplied, continue: search for identifiable cited cases, report the search outcome, and make clear that their substance was not checked without the full source. Never use memory as source evidence.
2. **Per-unit fan-out.** Run the packaged script; it starts one fresh session per prepared unit. If the host cannot run it, assign units to native workers or sequential processing. Give each session the assigned unit, about five units before and after it, the anchored body unit for a footnote, the full prepared-brief path and line range, the unit-review prompt, and the full path to the judgment rubric. The complete assignment procedure is in [parent-fanout.md](references/parent-fanout.md). Surrounding units are context only, and the assignment envelope owns location. Prefer the script, if your environment permits it, so that you receive structured data automatically through a tested workflow. If the environment does not allow you to run the script or you encounter errors that cannot be quickly fixed, gracefully degrade to assigning units to native workers.
3. **Targeted retry.** Give one targeted retry when evidence is mechanically incomplete: a missing excerpt, missing locator, invalid or out-of-authority source ID, or inconsistent source-match fields. Do not retry substantive legal disagreement. Keep both attempts. If the repair fails, retain the citation as amber (claimed but unverified) and continue.
4. **HTML report and bounded sense check.** When the packaged scripts are available, use `scripts/aggregate_report.py` to validate the receipts and render [assets/report-template.html](assets/report-template.html). This results in the best lawyer review experience and is preferred if your environment supports it. If local scripts are unavailable, render the same validated report data with the supplied template using host-native capabilities. Do not hand-author replacement HTML unless the user requests a custom report. The banner leads with review status, not run completeness. The main body contains citation-bearing units; the appendix accounts for every prepared unit, including `no_citations_found`, complete, failed, or still-missing receipts. Perform one bounded sense check: confirm the appendix accounts for every prepared unit, no visibly citation-dense passage has zero citation rows, and no finding contradicts itself on its face. Put apparent anomalies in `Caveats / Issues`; do not start a second retry cycle.

Keep the assigned unit, evidence rules, and result contract identical across scripted, native-worker, and one-at-a-time execution.

## Output

Return one terminal result for every prepared unit. A unit with no observed citation returns `disposition: no_citations_found` and an empty `citations` array; that receipt belongs in the report appendix and is complete accounting. A unit with citations returns `disposition: citations_found` and one row for each written citation. If one written citation supports distinct propositions, repeat the citation in separate rows with different `proposition` values.

Each citation row contains these fields:

| Field | Required value |
| --- | --- |
| `citation_as_written_in_unit` | Exact quote of the citation as it appears in the assigned unit. |
| `matched_citation` | Full citation after resolving `Id.`, `supra`, or short form; repeat or lightly normalize an already-full citation. |
| `proposition` | Always present: the claim evaluated, or `null`; carry a value when one written citation does more than one job. |
| `matched_source_id` | Stable ID of a supplied authority file, or `null` if no supplied authority matched. Non-null exactly when `source_resolution` is `matched_supplied_source`. |
| `source_excerpt` | Short verbatim excerpt from the matched file, or `null`. |
| `source_locator` | Page, paragraph, line, or other stable locator in the matched file, or `null`. |
| `citation_kind` | What the citation purports to be: `case`, `statute`, `rule`, `regulation`, `record`, or `other`. |
| `source_resolution` | Why the source is or is not in evidence: `matched_supplied_source`, `not_supplied_confirmed_exists_elsewhere`, `not_supplied_not_found_potential_hallucination`, or `not_supplied_search_unavailable`. |
| `fabrication_indicators` | An array, which may be empty, of `reporter_coordinates_belong_to_different_supplied_case`, `not_found_in_external_search`, and `citation_malformed_or_impossible`. |
| `colliding_source_id` | Optional. The supplied authority whose reporter coordinates the citation reuses, or `null`. |
| `existence_check_notes` | Optional. Where the worker searched and what it found, or `null`. |
| `accuracy_of_source_characterization` | One of `confirmed_fair_characterization_of_source`, `potentially_unfair_or_unreasonable_characterization_of_source`, `objectively_false_or_unreasonable_characterization_of_source`, or `source_not_found_unable_to_characterize`. |
| `pincite_accuracy` | One of `NA_no_pincite_for_this_citation`, `pincite_confirmed_accurate`, `pincite_inaccurate`, or `source_not_found_unable_to_check_pincite`. |
| `accuracy_of_direct_quotation` | One of `NA_no_direct_quotation_for_this_citation`, `quotation_confirmed_accurate_and_fair`, `quotation_technically_accurate_but_misleading_or_unfair`, `quotation_objectively_inaccurate`, or `source_not_found_unable_to_check_quotation`. |
| `recommended_changes` | A concise recommended edit, or `null`. |

When `matched_source_id` is not `null` and the relevant accuracy field does not say the source was not found, fill `source_excerpt` and `source_locator`. If either is missing, retain the worker-authored fields but flag that citation as claimed and unverified in normalized validation. A source identity card is navigation only; an empty candidate list never denies a finding, and a matched ID must belong to the supplied authority universe.

The model makes the legal call. Small deterministic code only checks that the result has usable evidence fields and that a cited source belongs to the files supplied for this run. It then assigns the display color: incomplete evidence is amber, while the model's substantive red or yellow finding remains intact. This check prevents missing or invalid evidence from appearing green; it does not decide whether a proposition fairly states the law. When the packaged scripts are available, use `scripts/aggregate_report.py` to validate the receipts and render the lawyer-facing HTML report from [assets/report-template.html](assets/report-template.html). If local scripts are unavailable, render the same validated report data with the supplied template using host-native capabilities. Do not hand-author replacement HTML unless the user requests a custom report. The report must include this simple scope note: “Checks citations against the sources supplied for this run; it does not check later case history or replace full legal research.” Include that same one-sentence reminder in the final message when handing the results to the lawyer, so the lawyer understands the scope of the review performed. Keep raw worker results, normalized validation flags, and later reviewer annotations as separate layers. The main body omits `no_citations_found`; the appendix lists every prepared unit and its receipt state. Missing authorities, unreadable material, unresolved antecedents, currentness limits, and jurisdiction-specific questions remain visible, and unresolved items go in `Caveats / Issues`.

## What this review does not answer

Uploaded-source review answers a narrower question: does the supplied authority support the proposition or quotation attributed to it, at the supplied location? It is not Shepard's, KeyCite, or equivalent currentness research.

It does not by itself determine whether a case remains good law, whether later decisions limited or overruled it, whether a statute or rule was amended, whether a regulation was withdrawn, or whether later history changes the result. If currentness or subsequent history matters, use a currentness service or supply its results for a separately scoped review. Never represent this source check as comprehensive citator treatment.

When public search is used, keep the source, query, and date in the technical receipt. In the lawyer-facing report, use the plain search outcome. A public result does not cure missing coverage or prove currentness.

Read only confirmed `[cite-check]` lines from `lqplaybook.md` if present. Never read or write `lqprofile.md`; never write the journey file. The scribe owns that separation.

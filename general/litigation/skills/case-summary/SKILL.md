---
name: case-summary
title: Case Summary
description: Produces an attorney-ready memo from a corpus of legal documents supplied by the user. Use when a user shows up with a folder, zip, or vault of case documents and asks for a case summary, case evaluation, litigation package, intake memo, matter overview, or "can you summarize this case for me." The skill ingests the corpus into a searchable index, OCRs anything non-searchable, inventories and diagnoses the practice area, loads the appropriate practice-area playbook module(s) (PI/tort, commercial litigation, IP infringement, or user-authored extensions), iteratively searches the corpus across eight core dimensions plus any module-specific dimensions, defers specialized document clusters (depositions, medical records, discovery, liens) to dedicated sibling skills, and synthesizes a cited memo.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/case-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
tags: [summary, analysis]
---

# Case Summary

A user arrives with a pile of legal documents — often hundreds or thousands — and asks for a summary. This skill is the playbook for doing that well, across any practice area.

The work is map-reduce: **map** the corpus across the dimensions that matter, **reduce** the hits into a memo. The skill does not prescribe a specific search tool — it describes the work. `references/BACKENDS.md` lists concrete implementations the agent can use today.

The core describes what every case has (parties, timeline, evidence, claims, exposure, defenses, procedural status, red flags). Practice-area playbooks (`references/PLAYBOOK-*.md`) specialize the core for specific domains. Specialized document types (depositions, medicals, discovery, liens) route out to dedicated sibling skills per `references/ROUTING.md`.

---

## Related skills

- `case-chronology` — when the deliverable is a dated timeline rather than a full memo
- `case-intake-initial-fact-memo` — for commercial-litigation intake memos
- `case-viability-report` — for go/no-go screening before accepting a matter
- `pi-demand-summary` — when the objective is a PI settlement package, not a case evaluation
- `demand-letter` — when the objective is a pre-suit demand letter
- `deposition-summary` — for deposition transcripts; route per `ROUTING.md`
- `discovery-summary` — for interrogatory/RFP/RFA responses; route per `ROUTING.md`
- `medical-record-chronology` — for dense medical-records sets; route per `ROUTING.md`
- `medical-treatment-summary` — for causation-focused treatment narratives
- `evidence-liability-summary` — for plaintiff-side liability element breakdowns
- `lien-resolution-summary` — for post-settlement lien tracking
- `legal-strategy-summary` — for motion-and-discovery roadmap deliverables
- `settlement-summarization` — for post-memo settlement activity

---

## Checkpoint A: pre-ingest intake (mandatory)

Ask every time unless the user says "use defaults" or "just go." Gather:

1. **Practice area guess** — PI, commercial, IP, regulatory, criminal, family, bankruptcy, etc. The agent can update this after Inventory, but a guess narrows the initial playbook loader.
2. **Expected document types** — pleadings, discovery, depositions, medicals, contracts, corporate records.
3. **Custodians / sources** — who produced the files, and in what posture (client production, opposing-counsel production, third-party subpoena).
4. **Date range** — anchor the timeline.
5. **User objective** — evaluation memo, viability screen, demand prep, settlement prep, strategy roadmap. Different objectives trigger different sibling skills per `ROUTING.md`.
6. **Privilege posture** — work-product only, attorney-client privileged, or litigation-ready.
7. **Venue / jurisdiction** — affects SOL, statutory-notice requirements, governing law.

**Defaults** (if the user doesn't answer): PI/tort playbook; evaluation memo; attorney work-product; U.S. state-court posture. Label every default explicitly in the memo header.

---

## The loop

**1. Ingest.** Put the corpus into something searchable. See `references/WORKFLOW.md` for the phase description and `references/BACKENDS.md` for implementations.

**2. OCR.** Any PDF that isn't already searchable will not be indexed usefully. Handle OCR before searching on files that need it. Asynchronous — keep moving.

**3. Inventory.** Pull the object list. Skim filenames to build a mental model: what practice area, what kinds of documents, how many of each. This is the only time the agent cares about every file.

**4. Diagnose practice area.** From the inventory plus a single global-overview query, pick one or more playbook modules from `references/PLAYBOOK-*.md`. Each has `triggers` in its frontmatter that match filenames and content signals. Record the choice in the memo header. When no module fits, proceed core-only and note it.

**5. Map — iterative search per dimension.** For each of the eight core dimensions in `references/CORE-DIMENSIONS.md`:

- Run the base queries from `references/SEARCH-PLAYBOOK.md`.
- Run the module queries from each loaded playbook for that dimension.
- Read the top 3–10 chunks per query. Cite everything the memo will rely on by object name + page.
- Where the corpus contains specialized document clusters (≥1 full deposition, dense medical records set, discovery responses, lien correspondence), **delegate** per `references/ROUTING.md` and consume the sibling skill's output rather than summarizing inline.

Don't brute-force read every file. Drive the search with focused queries, pull the 3–10 most relevant chunks per query, follow up when hits are load-bearing, route when a cluster warrants a sibling skill.

**6. Reduce — synthesize.** Assemble the memo using `references/OUTPUT-TEMPLATE.md`'s core skeleton, plus the output sections contributed by each loaded playbook. Every claim cites an object + page (or chunk ID). No citation = cut or label as assumption.

**7. Review.** Run the quality checklist below (core items + playbook-specific items). Flag any unsatisfied items.

---

## Checkpoint B: post-memo alignment (mandatory)

After delivering the draft, ask:

1. Did the right playbook module(s) get loaded? (List them.)
2. Which sibling skills were invoked, and did their outputs get integrated correctly?
3. Are there coverage gaps — dimensions the agent couldn't populate from the corpus?
4. Any claims in the memo that depend on unverified legal citations flagged `[VERIFY]`?
5. Is attorney review explicitly required before any downstream use?

If the user doesn't answer, default to: list the loaded playbooks and invoked siblings; flag any dimension that returned "no evidence found"; require attorney review.

---

## What this skill does not do

- It does not value the case. Ranges belong in the memo when a loaded playbook supplies the methodology, but the skill doesn't substitute for attorney judgment about jurisdiction, venue, or negotiation posture.
- It does not resolve liens, draft pleadings, or send demands. It identifies them and routes to the sibling skill that does.
- It does not replace an attorney review of the final memo. Always label the memo AI-generated and require sign-off.

---

## Scale notes

- **< 20 files:** skip the search loop; read every document directly. See `references/BACKENDS.md` small-corpus recipe.
- **20–200 files:** one pass through the search playbook, one memo. ~1 hour.
- **200–2,000 files:** expect 40–80 targeted searches across the dimensions, checkpoint notes as the agent goes. Multi-hour run.
- **2,000+ files:** expect 100+ targeted queries; tighten scoping with module-specific filters and entity-mode searches; budget multi-hour run time. One corpus — the agent works it harder, not by fragmenting it.

---

## Core quality checklist

Every matter:

- [ ] Every file is either searched-over or explicitly noted as out-of-scope
- [ ] Every OCR job finished (or its absence is noted in the memo)
- [ ] Parties, venue, posture correct with citations
- [ ] Timeline continuous; gaps >30 days flagged
- [ ] Each claim element has at least one evidentiary citation or explicit gap note
- [ ] Each asserted defense has supporting-evidence citation or a "pled without support" note
- [ ] Exposure/remedies section shows methodology, not an attorney valuation
- [ ] Red flags section is honest, not decorative — each item names a next action
- [ ] Every claim in the memo traces to an object + page or is labeled an assumption
- [ ] Unverified statutes/rules/cases marked `[VERIFY]`
- [ ] Memo labeled AI-generated, requires attorney review

**Plus** every playbook-specific item from each loaded `PLAYBOOK-*.md`'s Quality checklist section.

---

## Troubleshooting

- **OCR didn't run on a file.** The file isn't searchable. Record the file in the memo's out-of-scope list, try a different OCR engine if the backend supports one, or ask the user to re-upload a text-searchable version.
- **Search returns noise, not relevant hits.** Run a global-overview query first to discover the vocabulary the documents use; re-issue targeted queries using that vocabulary. Narrow with keyword anchors (party names, dates, case numbers) once known.
- **Practice area ambiguous; no playbook fits cleanly.** Proceed core-only (core dimensions + `SEARCH-PLAYBOOK.md` base queries). Note the ambiguity in `VIII Strengths / Weaknesses / Red Flags`. Offer the user a recommendation to narrow.
- **Wrong playbook picked.** Re-enter step 4 (Diagnose practice area) with the new information. Load the correct module; keep hits from the previous pass that still apply.
- **Corpus too large for a single pass.** Prioritize the dimensions that matter for the user's stated objective. Run a triage pass (parties, posture, top 3 claims, headline exposure) first, then expand to full coverage if time allows. Surface to the user which dimensions are deep vs. triage in the memo header.
- **Sibling skill unavailable or returns nothing useful.** Note it in the memo header (`Sibling skills invoked`), record the cluster the agent wanted to route, and summarize the cluster inline with reduced depth. Attorney review should consider whether a focused sibling-skill run is warranted before the memo is used downstream.
- **Multi-matter corpus (the folder mixes unrelated cases).** Surface to the user before proceeding. The skill summarizes one matter at a time; don't silently merge.

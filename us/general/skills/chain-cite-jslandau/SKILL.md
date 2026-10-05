---
name: chain-cite-jslandau
title: Chain-Cite
description: Use when the user wants to trace a single legal proposition backward through its citation graph to find the original source that first uttered it. Takes one proposition + one citation, walks backward hop by hop through CourtListener's opinion citations, annotates relationship (quoting / paraphrasing / holding) and semantic drift (broadens / narrows / rephrases) at each hop, and terminates when the chain hits a non-case source (statute, Restatement, constitution), a source CourtListener does not cover, an opinion that states the rule without citing a predecessor, or a cycle. Produces both a structured JSON chain and a human-readable Markdown report with a summary-first layout. Narrow-and-deep counterpart to cite-checking's wide-and-shallow document scan.
author: jslandau
author_url: https://github.com/jslandau/legal-tools/tree/main/plugins/legal-tools/skills/chain-cite
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
---

# Chain-Cite

## Prerequisites

This skill uses the citation taxonomy, short-form resolution rules, proposition-extraction rules, structured component schemas, flag vocabulary, and CourtListener API patterns defined in the `citation-toolkit` skill. Read `citation-toolkit` first; the stages below refer to its definitions by name rather than restating them.

When dispatching subtask subagents, follow the **Model Tiers for Subtasks** section of `citation-toolkit`: citation parsing, star-pagination lookup, and exact-quote localization are Haiku-tier; drift annotation, next-hop selection from string cites, and termination decisions are Sonnet-tier; the optional summary-critic pass is Opus-tier.

## Overview

Given one proposition and one citation that supposedly supports it, this skill walks backward through the citation graph — at each hop locating the proposition in the current opinion, finding the outbound citation that supports it, and recursing into the predecessor — until the chain terminates naturally. The user gets the **full lineage** from the input citation back to whatever source CourtListener (or the user, at a checkpoint) can trace it to.

Compared to `cite-checking`, which scans an entire document's citations at shallow depth, chain-cite is narrow (one proposition, one seed) and deep (no hard cap on chain length; terminates only on natural end conditions).

The skill produces two artifacts: a canonical JSON chain and a human-readable Markdown report (summary first, lineage second, flags and methodology last). Neither the user's input nor any fetched opinion is modified.

## Before Starting

Collect four inputs from the user before running any API calls:

1. **Proposition** — the statement being traced, verbatim. A single sentence is the sweet spot. If the user provides a full paragraph, ask them to narrow to the specific assertion; long propositions match poorly and inflate traversal cost. If the user provides a very short phrase (e.g., "strict scrutiny"), warn that short propositions fan out hard at every hop and suggest adding a clause for specificity.

2. **Seed citation** — the citation that supposedly supports the proposition. Parsed in Stage 2 using `citation-toolkit`'s Case schema. If the user provides a short form (`Id.`, `supra`), a statute, a rule, a regulation, or a non-US case, stop and explain: this PoC traces propositions through US case law only; those other categories either lack a usable citation graph or require sources outside CourtListener.

3. **CourtListener access.** If the `claude.ai CourtListener` MCP server is available, no token is needed — Stage 2 and the per-hop fetches use the MCP directly. Otherwise, a CourtListener API token is required (free at courtlistener.com/sign-in/; authenticated accounts get 5,000 requests/hour).

4. **Sibling-branch tracing** — when a hop encounters a string cite with multiple predecessors for the same proposition, how should chain-cite handle the siblings?
   - **Follow only the strongest-signal case** (default — typically the first in the string per Bluebook 1.4; siblings are still recorded in the hop's JSON entry as `also_cited_for_same_proposition` but not recursed into)
   - **Also trace sibling branches** (each sibling becomes its own sub-chain, traced to termination; the output becomes a forest rather than a chain. Warning: tracing all branches may get expensive token-wise and consume much more of your CourtListener rate budget)

If the seed citation has multiple pincites (e.g., `576 U.S. 155, 163, 170`), ask which is the intended pincite — the proposition should live at one specific passage.

---

## Stage 1 — Intake

Validate the four inputs, abort-with-explanation on the out-of-scope cases listed above, and carry them through the rest of the pipeline. Initialize two empty structures that persist through the run:

- `visited_opinion_ids: set` — for cycle detection (see Stage 4).
- `chain: list[Hop]` — the accumulating output (see Stage 6 for the Hop schema).

---

## Stage 2 — Seed Resolution

Parse the seed citation using `citation-toolkit`'s Case schema. Resolve to an opinion using `citation-toolkit`'s **CourtListener API** section:

- **MCP path (preferred):** look up the seed via the **components-only** citation-lookup call: `mcp__claude_ai_CourtListener__call_endpoint(endpoint_id="citation-lookup", method="POST", body={"volume": "<vol>", "reporter": "<reporter>", "page": "<page>"})`. The response gives you a **cluster ID**, not an opinion ID. Resolve to the correct sub-opinion via `mcp__claude_ai_CourtListener__call_endpoint(endpoint_id="clusters", query={"id": <cluster_id>})` → pick the right entry in `sub_opinions` (prefer `020lead`, fall back to `010combined`). Then fetch the opinion text via `mcp__claude_ai_CourtListener__get_endpoint_item(endpoint_id="opinions", item_id=<opinion_id>, fields=["id", "type", "html_with_citations", "plain_text"])`. **Never pass the cluster ID directly to `get_endpoint_item("opinions", ...)`** — it silently returns the wrong opinion. **Do NOT use `analyze_citations`** — it accepts a `text` parameter, and we keep the bright-line rule that no document text crosses the network. Write the returned JSON to a temp file (e.g., `/tmp/opinion-<id>.json`) — Stages 3–4 pass that path to `chain_hop.py`.
- **Fallback (no MCP):** the equivalent curl POST to `/api/rest/v4/citation-lookup/` with `volume/reporter/page` and a user-supplied token, then `/api/rest/v4/opinions/<id>/` — both documented in `citation-toolkit`'s REST API section.

**Sub-opinion selection.** When the cluster's `sub_opinions` array has more than one entry, apply the **Choosing the right sub-opinion** rule in `citation-toolkit`: prefer the `020lead` opinion unless the seed citation explicitly references a dissent or concurrence. The `020lead` sub-opinion typically carries reporter-pagination (`*N` markers) from the Harvard CAP ingest, which is what the match ladder relies on.

**Upfront pagination check.** After fetching, run `citation-toolkit`'s pagination-mode detection on the opinion's `html_with_citations`. Record `pagination_mode` on Hop 0 (and on every subsequent hop). When `pagination_mode != "reporter"`, the per-hop pincite-page slicing in Stage 3 will fall through to whole-opinion semantic search — flag the hop accordingly so the output report surfaces the localization uncertainty.

Apply identity verification per `citation-toolkit`. If CourtListener fails, follow the escalation chain defined there (Justia → direct court → Google Scholar → ask user). If the chain fully exhausts, abort with a `seed_citation_unverifiable` message — there is no chain to trace if we can't find the starting opinion.

Once the seed opinion is fetched and written to disk, record it as **Hop 0** with `relationship_to_prior_hop: "seed"`. Proceed to Stage 3 to localize the proposition inside it.

Add the seed opinion's ID to `visited_opinion_ids`.

---

## Per-Hop Helper Script

This skill ships with `chain_hop.py` alongside `SKILL.md`. It is the **mechanical** half of each hop — filtering an already-fetched opinion JSON to the pincite page and extracting outbound citation anchors. It does **no** network I/O and **no** scoring of which passage "best matches" the proposition: fetching is the skill's job (MCP preferred, REST fallback); semantic relevance is a Sonnet-tier judgment, not a regex one.

Each hop is a four-step cycle:

1. **Fetch the current hop's opinion JSON.** Use `mcp__claude_ai_CourtListener__get_endpoint_item(endpoint_id="opinions", item_id=<opinion_id>, fields=["id", "html_with_citations", "plain_text", "xml_harvard"])` (or, without the MCP, the REST `opinions/{id}/` endpoint). Write the response to a path like `/tmp/opinion-<id>.json`. Reuse an existing file if present — the script reads, never writes, this file.

2. **`chain_hop.py page`** (Haiku-tier / direct script call). Returns the full plain-text of the pincite page plus a sentence-level breakdown. No ranking.

3. **Semantic selection** (Sonnet-tier subagent). Given the proposition being traced and the page text, the subagent picks which sentence carries the same rule and produces the drift annotation (`null` for verbatim, or `rephrases:` / `broadens:` / `narrows:` with a one-line note). If no sentence on the page carries the rule, the subagent reports `proposition_not_found_in_opinion`.

4. **`chain_hop.py anchors`** (Haiku-tier / direct script call). Given the sentence the Sonnet step chose, extracts the outbound citation anchors inside or immediately after that sentence and decides the next hop, terminal reason, or cycle.

### Subcommand: `page`

```bash
python3 <skill-dir>/chain_hop.py page \
  --opinion-json /tmp/opinion-<N>.json --pincite PAGE
```

Returns JSON with `page_plain_text` (the full page), `sentences` (sentence-level chunks), and `page_start_offset` / `page_end_offset`. If the page marker is not found, returns `page_marker_found: false` and a whole-opinion fallback.

### Subcommand: `anchors`

```bash
python3 <skill-dir>/chain_hop.py anchors \
  --opinion-json /tmp/opinion-<N>.json \
  --sentence "verbatim passage the Sonnet step chose" \
  --visited "id1,id2,..."
```

Returns `next_hop`, `siblings`, `non_case_anchors`, `cycle_anchors`, and — when there is no usable outbound citation — a `terminal_reason` drawn from Stage 4d. Pass the prior chain's opinion IDs in `--visited` for cycle detection. The opinion JSON must contain `html_with_citations` (request it explicitly in the `fields` allowlist when fetching).

### Why no lexical scoring

An earlier iteration of this script scored candidate passages by term specificity and char-distance from the page marker. That misfires predictably: a pincite names a whole page (~400 words), and lexical proximity is not semantic relevance. The rule passage on page 280 might sit 2000+ chars after the `*280` marker; a general term ("Eleventh Amendment") might appear 50 chars after it in irrelevant context. Any such heuristic will occasionally return a confident wrong answer. Semantic match is Sonnet's job (Tier 3 in `citation-toolkit`'s match ladder) — do not re-introduce lexical scoring here. The script's role is to *filter* (slice the right page span; extract the right anchors); the *judgment* of which sentence carries the rule belongs to the semantic step.

---

## Stage 3 — Proposition Localization (per hop)

On entering any hop, the current opinion text has already been fetched (at the end of the previous iteration, or at Stage 2 for the seed). Use `html_with_citations` as the primary field for both matching and citation-anchor extraction; fall back to `plain_text` only when HTML is empty. `xml_harvard` may be requested as an additional pagination source if available.

**Apply `citation-toolkit`'s match ladder** to localize the proposition in the current opinion:

- When `pagination_mode == "reporter"` and the hop has a known pincite page: Tier 1 (direct phrase match) first, then Tier 3 (pincite-page semantic match via `chain_hop.py page`).
- When `pagination_mode` is `"slip_only"` or `"none"`: skip Tier 3 (no reliable pincite page); go straight to Tier 4 (whole-opinion semantic search). Flag the hop with `non_reporter_pagination_detected` or `pincite_page_unresolvable`.

Within whichever tier applies, the proposition can match in one of three drift-annotation modes:

1. **Exact or near-exact quote.** If the proposition appears verbatim or with minor punctuation/formatting differences, anchor there. High-confidence match; `drift_annotation = null`.
2. **Semantic paraphrase.** A passage expressing the same rule in different wording. Record the passage verbatim; `drift_annotation = "rephrases: <one-line note on how wording differs>"`.
3. **Broader or narrower statement.** The opinion addresses a generalization or a sub-case of the proposition. Record the passage; `drift_annotation = "broadens"` or `"narrows"` with a one-line note.
4. **No match.** This hop is terminal. Emit the hop with `terminal_reason: "proposition_not_found_in_opinion"`. This is how the chain dies when the rule has mutated so far from its ancestor that the ancestor no longer states it.

For the seed (Hop 0), a "no match" outcome is treated specially: abort the whole run with `proposition_not_in_seed` — the seed opinion doesn't appear to contain the proposition, so either the citation is wrong or the proposition wording needs work. Suggest the user double-check both.

For non-seed hops, a "no match" is a clean natural termination, not an error.

Record the matched passage (typically 100–300 words of surrounding context), the resolved pincite page (or `null` if pagination_mode prevented page resolution), and the `match_tier_used` on the current hop.

---

## Stage 4 — Next-Hop Selection (hybrid pincite-first)

Given the matched passage in the current opinion, find the outbound citation that supports the proposition.

### 4a. Pincite-anchored attempt (cheap path)

In `html_with_citations`, look for citation anchor tags inside or immediately after the matched passage's sentence. Three cases:

- **Exactly one citation anchored there** → that's the next hop. Log `next_hop_strategy: "pincite_anchor"`.
- **A string cite anchored there** → take the first case in the string (strongest authority per Bluebook 1.4). Record the remaining cases in `also_cited_for_same_proposition` on this hop (leaf entries, not recursed into — unless sibling-tracing is on, in which case each sibling spawns its own sub-chain traced to termination). Log `next_hop_strategy: "pincite_anchor"`.
- **No citation at the pincite, or the anchored citation is a signal cite pointing somewhere obviously unrelated (e.g., `see also` to a procedurally different case)** → fall through to 4b.

### 4b. Fan-out fallback (expensive path)

Enumerate all outbound citations in the broader paragraph containing the matched passage (parsed from `html_with_citations`). Count the candidates, then:

- **≤ 5 candidates** → evaluate all of them automatically. For each: fetch the opinion, apply Stage 3's match strategy, rank by match confidence (exact quote > semantic paraphrase > broadens/narrows). Pick the best-ranked candidate as the next hop.
- **> 5 candidates** → **pause and ask the user.** Show the candidate list (citation + one-line context of where each appears in the paragraph). Options: "first 5 only," "all N," "just these specific ones [checkboxes]," "none — treat this hop as terminal." This is a deliberate friction point to prevent unbounded cost growth; do not auto-select.

Log `next_hop_strategy: "fanout_fallback"` and include `fanout_candidates_evaluated: N` on the hop for transparency.

### 4c. Cycle detection

Before committing to a next hop, check whether the target opinion ID is already in `visited_opinion_ids`. If so, emit this hop as terminal with `terminal_reason: "cycle_detected"` and include both the current chain-path and the cycle target in a `cycle_path` field on the hop. This catches pathological oscillations (affirmance ↔ underlying opinion; rare but possible).

When sibling-tracing is on, `visited_opinion_ids` is **shared across the whole forest** — two sibling branches that converge on the same ancestor do not each refetch.

### 4d. Terminal conditions

The hop is terminal (do not recurse) if any of these apply:

- No outbound citation supports the proposition (both 4a and 4b found nothing usable) → `terminal_reason: "no_outbound_for_proposition"`
- The chosen outbound cite points to a **statute, Restatement, constitutional provision, or other non-case source** (recognized via `citation-toolkit`'s taxonomy) → `terminal_reason: "cites_statute" | "cites_restatement" | "cites_constitution" | "cites_treatise" | "cites_law_review" | "cites_legislative_material"`, with the specific citation captured in the hop's `terminal_citation` field
- CourtListener returns no cluster for the chosen citation, or the cluster has no opinion text after fallthrough → `terminal_reason: "courtlistener_missing"`
- Cycle detected (per 4c) → `terminal_reason: "cycle_detected"`

If not terminal, fetch the predecessor opinion now (in preparation for the next iteration), add its ID to `visited_opinion_ids`, append the hop to `chain`, and recurse.

### 4e. Soft checkpoint

Every 8 opinions fetched across the whole run (counting the forest total when sibling-tracing is on, not the linear depth), pause and emit an interim summary:

- Chain rendered as prose through the last completed hop
- Opinions fetched so far; approximate remaining CourtListener budget for the hour (best-estimate based on 5,000/hr)
- "Continue? — continue one more block of 8 / continue to natural termination / stop now"

If the user stops, the last completed hop gets `terminal_reason: "user_stopped_at_checkpoint"` and the chain is written out through it. This is a pause, not a cap.

---

## Stage 5 — Termination Handling

When a hop is emitted as terminal, attach a **suggested next step** derived mechanically from the `terminal_reason`:

| `terminal_reason` | Suggested next step |
|-------------------|---------------------|
| `cites_statute` | Consult the statute's legislative history (Congress.gov) and USC annotations (Cornell LII). |
| `cites_restatement` | Consult the Restatement's Reporter's Notes (print volumes via ALI, or Westlaw/Lexis) for the case citations behind the rule. |
| `cites_constitution` | Consult constitutional-history treatises; CourtListener does not trace constitutional provisions further. |
| `cites_treatise` | Consult the treatise directly via HeinOnline, Google Books, or a law library. |
| `cites_law_review` | Consult the article directly via SSRN, the journal's website, or HeinOnline. |
| `cites_legislative_material` | Consult Congress.gov or GovInfo for the full legislative record. |
| `courtlistener_missing` | CourtListener has no text for this opinion; try Justia, the issuing court's website, or a legal database (Westlaw/Lexis). |
| `no_outbound_for_proposition` | This opinion states the rule without citing a predecessor for it. This may be the effective origin, or the origin may be implicit (e.g., common-law tradition). Consider consulting a hornbook or treatise for historical context. |
| `proposition_not_found_in_opinion` | The predecessor does not appear to state this proposition. The rule may have first been articulated at the previous hop, or the chain-of-citation may be weak at that link. |
| `cycle_detected` | Chain looped back to an already-visited opinion (`{cycle_target}`); this is often the effective origin when two cases cite each other. |
| `user_stopped_at_checkpoint` | User stopped at this hop; resume by invoking the skill with this hop's citation as the new seed and the same proposition. |
| `network_error` | Transient fetch failure; re-run the skill to resume. Partial chain through the last successful hop is preserved. |

---

## Stage 6 — Output Assembly

Produce two files in the output directory the user specified (default: current working directory), with matching basenames:

- `chain-cite-<slug>-<YYYYMMDD>.json` — canonical, machine-readable
- `chain-cite-<slug>-<YYYYMMDD>.md` — human-readable, rendered from the JSON

Where `<slug>` is derived from the seed citation's case name (e.g., `smith-v-jones`).

### JSON schema

One Hop object per entry in `chain`:

```
{
  "hop_index": 0,
  "citation": "Smith v. Jones, 123 F.3d 456 (5th Cir. 2020)",
  "opinion_id": 1234567,
  "pincite_page": 460,
  "quoted_passage": "…",
  "relationship_to_prior_hop": "seed" | "quoting" | "paraphrasing" | "holding",
  "drift_annotation": null | "broadens" | "narrows" | "rephrases: <note>",
  "also_cited_for_same_proposition": [
    {
      "citation": "…",
      "opinion_id": … or null,
      "note": "leaf entry (sibling-tracing off)" | "recursed into — see branch below"
    }
  ],
  "flags": [ … ],
  "next_hop_strategy": "pincite_anchor" | "fanout_fallback" | "terminal",
  "fanout_candidates_evaluated": null | N,
  "terminal_reason": null | "<one of the values in Stage 5>",
  "terminal_citation": null | "<the cite that ended the chain, for statute/treatise/etc. cases>",
  "suggested_next_step": null | "<text from Stage 5 table>",
  "cycle_path": null | [opinion_id, opinion_id, …]
}
```

When sibling-tracing is on, `also_cited_for_same_proposition` entries become full Hop objects with their own recursive structure; the top-level `chain` becomes a tree rather than a linear list. Same schema either way — the default case is a degenerate tree with no branches.

### Relationship annotation

Assigned based on what the current opinion does with the proposition relative to the *cited* predecessor:

| Value | When assigned |
|-------|---------------|
| `seed` | Hop 0 only |
| `quoting` | The opinion uses explicit quote marks around the proposition and attributes to the predecessor |
| `paraphrasing` | The opinion states the rule in its own words while citing the predecessor |
| `holding` | The opinion states the rule as its own without attribution to any predecessor — the chain *may* continue via fan-out if an outbound cite supports the proposition, but this hop is a candidate "earliest original holding" |

### Markdown report layout

Summary-first, so readers see the answer before scrolling through hop detail:

```markdown
# Chain-Cite Report

**Proposition:** "[user's proposition, verbatim]"
**Seed citation:** [user's citation]
**Date:** [date]
**Total hops:** N
**Terminal reason:** [e.g., "cites 42 U.S.C. §1983 — chain terminates at statute"]

## Summary

[2–4 sentence narrative of the lineage: where the rule originated, where the earliest-original-holding hop is, how the wording drifted, where it terminated. Rendered from the lineage, but written first in the file.]

## Lineage (newest → oldest)

### Hop 0 (seed) — [citation]
**Relationship to prior:** seed
**Passage at pincite:**
> "[quoted passage]"
**Observation:** [optional — e.g., auto-surfaced "This is the earliest-original-holding hop for this proposition" when relationship_to_prior_hop == "holding"]

### Hop 1 — [citation]
**Relationship to prior:** [quoting / paraphrasing / holding]
**Drift:** [omit line entirely if null; otherwise broadens/narrows/rephrases with note]
**Passage at pincite:**
> "[quoted passage]"
**Also cited for same proposition:** [citation list, one-line each — omit line entirely if empty]

[… additional hops …]

### Hop N (terminal) — [citation or description of terminal source]
**Relationship to prior:** [value]
**Terminal reason:** [from Stage 5]
**Suggested next step:** [from Stage 5 table]

## Flags

[Bulleted list of per-hop flags: drift annotations, resolved_via_short_form, low_confidence_ocr, cycle_detected, etc. Omit the section entirely if there are no flags.]

## Methodology

- Traversal: hybrid pincite-first
- Sibling tracing: [on / off]
- Opinions fetched: N
- Checkpoints hit: N
- Fan-out fallbacks triggered: N
```

**Implementation note on ordering.** The Summary section must be rendered *after* the lineage is fully traced (because it summarizes the lineage), but written to the file *before* the Lineage section. Build the chain first internally, then render both sections, then write.

### Optional: summary critic

After assembling the output, a single summary-level critic subagent may be dispatched to review the full chain end-to-end and report whether the lineage hangs together (i.e., whether the proposition actually survives across all the claimed drift annotations without losing its identity). This is one subagent call for the whole chain, not per hop. Default: off for the PoC. When on, the critic's output appears as a `## Critic Assessment` section between `Summary` and `Lineage`.

---

## Edge Cases

| Situation | Handling |
|-----------|----------|
| Seed citation is a short form (`Id.`, `supra`) with no context | Cannot resolve — abort at intake, explain, ask for the full form |
| Seed citation is a statute/rule/regulation/constitutional provision | Out of scope for PoC — abort at intake with a clear message ("chain-cite traces propositions through case law; statutes don't have the kind of citation graph this skill walks") |
| Seed is a foreign / EU case | Out of scope for PoC — CourtListener is US-focused |
| Proposition is a whole paragraph | Ask user to narrow to a specific sentence |
| Proposition is a single word or phrase (e.g., "strict scrutiny") | Warn that short propositions fan out hard; suggest adding specificity |
| Opinion text is OCR'd and garbled | Attempt match on the primary field (`html_with_citations` stripped, or `plain_text`) anyway, flag the hop with `low_confidence_ocr`, continue |
| Opinion cites a predecessor by short form only (e.g., "See *id.*") | Use `citation-toolkit`'s short-form resolution against the opinion's internal citation stack; flag `resolved_via_short_form` on that hop |
| Multiple pincites in seed citation (`576 U.S. 155, 163, 170`) | Ask user which pincite is the intended one at intake |
| User's proposition appears multiple times in the same opinion at different pincites | Prefer the passage with the clearest outbound citation; flag `multiple_proposition_locations` and note which pincite was used |
| CourtListener returns a correct cluster but the opinion text is empty / missing | Fall through escalation chain per `citation-toolkit` (Justia → direct court → Google Scholar). If all fail, terminal with `courtlistener_missing` |

---

## Error Handling

Philosophy (inherited from cite-checking): **escalate, don't fail.** Every failure mode has a terminal state with a reason; the chain never crashes mid-run, only stops cleanly and writes out what it has.

| Failure | Handling |
|---------|----------|
| Citation parsing fails at Stage 2 | Ask user for a cleaner version; if still unparseable, abort with a clear pre-chain message |
| CourtListener `citation-lookup` returns no cluster for seed | Escalation chain per `citation-toolkit`. If exhausted, abort with `seed_citation_unverifiable` |
| Cluster found but identity check fails | Treat as no-match, fall through escalation |
| Proposition cannot be located in the seed opinion | Abort with `proposition_not_in_seed`; explain and suggest the user double-check citation and/or wording |
| Proposition cannot be located in a non-seed opinion | Terminal hop with `proposition_not_found_in_opinion` — natural termination, not an error |
| Opinion fetch returns empty `html_with_citations` AND empty `plain_text` | If `xml_harvard` is populated, derive text from it; otherwise terminal with `courtlistener_missing` |
| CourtListener rate limit (HTTP 429) | Pause, show message, ask user to wait or retry. Respect `Retry-After` header if present. Interactive pause, not terminal |
| Network error mid-traversal | Retry once after 5s; if still failing, emit the partial chain with `terminal_reason: "network_error"` |
| User interrupts at checkpoint | Terminal `user_stopped_at_checkpoint`, chain fully written out through the last completed hop |
| Subagent errors (if summary critic is enabled) | Flag `critic_unavailable` on the report; the lineage itself is unaffected |

At every checkpoint and at every terminal emission, the skill writes both output files to disk — so a crashed or killed run leaves the partial work available rather than losing it. Re-running with the same seed produces a fresh output; there is no resume-from-state file in the PoC (users resume by invoking the skill with the last completed hop as the new seed).

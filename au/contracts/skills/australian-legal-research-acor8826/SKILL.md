---
name: australian-legal-research-acor8826
title: Australian Legal Research (multi-agent)
description: 'Comprehensive red-teamed Australian legal research on freely available databases — AustLII, CaseLaw NSW, the legislation registers, BarNet Jade (free tier), and web search. Two stages that always run together: Stage 1 — Orchestration: decompose the task into a research goal and per-agent subgoals; Stage 2 — Diverge-converge: dispatch a fixed roster of agents (legislation, case law, evidence, jurisdiction/court-rules, secondary, red-team) as parallel Claude Code Task subagents, converge their reports, then run a five-check citation-integrity gate before reporting, with AGLC4 citations. Triggers: AustLII, Jade/jade.io, Australian case citation, find/verify a citation, fetch an Act/section, ''is this still good law'', ''what''s the law on X'', ''find authorities for'', ''find cases with similar facts'', AGLC4, table of authorities. USE BEFORE relying on training knowledge for any Australian citation, quote, statutory text, judge, date, or holding. For paywalled material (logged-in
  JADE), use jade-research.'
author: acor8826
author_url: https://github.com/acor8826/claude-australian-legal-research/tree/main/australian-legal-research
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: contracts
language: en
sources:
- title: Agent Caselaw
  path: references/agent-caselaw.md
- title: Agent Evidence
  path: references/agent-evidence.md
- title: Agent Jurisdiction
  path: references/agent-jurisdiction.md
- title: Agent Legislation
  path: references/agent-legislation.md
- title: Agent Redteam
  path: references/agent-redteam.md
- title: Agent Secondary
  path: references/agent-secondary.md
- title: Agent Validation
  path: references/agent-validation.md
- title: Aglc4 Citation
  path: references/aglc4-citation.md
- title: Retrieval Mechanics
  path: references/retrieval-mechanics.md
- title: Templates
  path: references/templates.md
---

# Australian Legal Research (multi-agent)

## Overview

This skill does two things. It **retrieves** Australian primary law (case law, legislation, topical searches) from the freely available legal databases — AustLII (austlii.edu.au), CaseLaw NSW (caselaw.nsw.gov.au), the Federal Register (legislation.gov.au), NSW legislation (legislation.nsw.gov.au), and BarNet Jade's free tier (jade.io — judgment text and citator leads; access mechanics in `references/retrieval-mechanics.md`), with web search as a first-class discovery path; and it **researches** — running an orchestrated, red-teamed, multi-agent pass over a legal question and self-validating every authority before it is reported, with AGLC4-formatted citations (`references/aglc4-citation.md`).

The skill ships no MCP server, but it **prefers one if present**: when the optional `jurisd` MCP server is registered, its tools are the **Layer-0** retrieval path (authority-ranked AustLII search, clean full-text fetch, deterministic provision lookup, an offline citation-graph tool, AGLC4 formatting). Otherwise it drives the runtime's own primitives (`web_fetch`/`WebFetch`, `web_search`, Claude in Chrome). Either way the skill works — jurisd is preferred, never required. The full mechanics — Layer-0 precedence and fallback, URL patterns, which tool to use where, recovery when a fetch fails — live in `references/retrieval-mechanics.md`. **Every agent reads that file before fetching anything.** The orchestrator owns strategy; the reference owns mechanics.

## CRITICAL: Verification Principle

**Never cite an Australian case, quote a judgment, reproduce statutory text, or state case metadata (bench, dates, jurisdiction, parties, catchwords) from memory alone.** Always verify by fetching the source. Training data contains wrong citations, outdated legislation, and fabricated quotes. Citing a non-existent or overruled case in court has severe consequences — and the user is a self-represented litigant who files these results.

If a fetch fails and the source cannot be retrieved, say so explicitly. Do not paraphrase from memory. Verification produces three states only — **verified, suspect, or overridden** — never "probably fine".

---

## Architecture: orchestration → diverge-converge

This skill runs as **one two-stage architecture**, modelled on `submissions-verification`. The two stages are **sequential parts of a single flow — not alternative modes you choose between**:

- **Stage 1 — Orchestration.** The orchestrator decomposes the task into a **research goal** and the **subgoals each agent must fulfil** (the per-area task-lists). Nothing is dispatched until the goal and those subgoals are fixed. (Steps 1–2.)
- **Stage 2 — Diverge-converge.** The orchestrator dispatches the agent roster **in a single turn** to fulfil their subgoals (diverge), then **reads and reconciles** their reports itself (converge), validates every authority, and synthesises the memo. Stage 2 runs in **cycles**: dispatch → converge → validate → assess → decide whether a further cycle is warranted. (Steps 3–9.)

**The decomposition scales to the task; the architecture does not change.** A bounded retrieval — "pull `[2021] NSWSC 741`", "fetch s 41 of the Bankruptcy Act 1966", "find the case where the parties are Smith and Jones, 2020" — or a single "is `[2019] FCA 1234` real / still good law?" check is simply a *trivial* Stage-1 decomposition: one subgoal, which Stage 2 satisfies with a single agent or a direct fetch via `references/retrieval-mechanics.md` (plus the inline Treatment check from `references/agent-validation.md` for a good-law question). A genuine research question — "what's the law on X given these facts", "build the case-law under s N", "find the best contrary authorities" — decomposes into several subgoals dispatched as the full roster. Same two stages either way; only the number of subgoals and agents differs. The orchestration is never skipped — for a lookup it is just small.

---

## Stage 1 — Orchestration (decompose the task)

Stage 1 is the orchestrator's own work: turn the request into a fixed **research goal** and the **subgoals each agent must fulfil**. It produces no authorities — it produces the plan the agents execute in Stage 2. Everything fixed here is recorded in the ledger (Step 8) and sliced into each agent's prompt.

### Step 1 — Frame the research goal

Before delegating, the orchestrator fixes and records (in the ledger — see Step 6):

1. **The legal question(s)** — stated precisely, as the things the research must answer.
2. **Jurisdiction and court hierarchy** — which courts bind, which persuade (default frame: NSW Supreme Court and the Federal Court; see the hierarchy table in `references/retrieval-mechanics.md`).
3. **Temporal anchor(s)** — the "as at" date(s). Legislation currency and "still good law" are meaningless without this. Two anchors often matter: the law as it stood when the cause of action arose, and the law as at the hearing/filing date. State both if relevant.
4. **The factual matrix** — the salient facts, distilled, so the case-law team can search by analogy (similar facts / similar legal question), not just keywords.
5. **The proposition(s)** — what is to be *supported* and what is to be *contested*. The red-team works the contest side.

If any of these cannot be fixed from the request, the orchestrator makes the most reasonable assumption, **records it explicitly in the ledger**, and proceeds — it does not stall on a question the user can correct later. Genuinely blocking ambiguity (e.g. an unknown jurisdiction that changes the whole search) is the only thing worth pausing for.

### Step 2 — Decompose into agent subgoals (task-lists; major / moderate / minor)

For each subject area engaged (legislation, case law, evidence, jurisdiction, secondary, red-team), the orchestrator drafts a task-list — **these task-lists are the subgoals each agent must fulfil in Stage 2** — and tags every task by load-bearing weight:

- **Major** — the goal *cannot be answered* without it. (e.g. identify the controlling provision; find the leading appellate authority on the central proposition.)
- **Moderate** — materially strengthens or qualifies the answer, but the goal survives a gap. (e.g. find first-instance applications of the provision; identify the standard counter-authority.)
- **Minor** — completeness and colour; marginal additions. (e.g. secondary commentary that frames the issue; tangential or obiter mentions.)

Which areas to engage is the orchestrator's call. Not every question needs a secondary team; almost every contested question needs a red-team. A litigation question almost always engages the **jurisdiction** agent (the forum's rules and practice notes) and usually the **evidence** agent (the regime of proof — which Evidence Act, or a tribunal not bound by the rules); a pure statutory-text or single-citation lookup may engage neither.

## Stage 2 — Diverge-converge (agents fulfil their subgoals; orchestrator converges)

Stage 2 executes the Stage-1 plan: dispatch the roster **in one turn** to fulfil their subgoals (diverge, Step 3), then the orchestrator **reads and reconciles** their reports itself (converge, Step 4), validates the authorities (Step 5), and writes the memo (Step 6) — looping for further cycles (Steps 7–9) until the goal is met. This is the diverge-converge pattern from `submissions-verification` (its Step 3 diverge, Step 4 converge), with a validation gate and cycle loop on top.

### Step 3 — Dispatch the research agents (diverge)

The orchestrator decides **which** of the six areas the goal needs (Step 2), then dispatches **one named Task subagent per engaged area — all in a single turn / one message** so they run in genuinely parallel, isolated contexts. This is a **fixed, countable roster** (two to six agents), dispatched the same way the `submissions-verification` skill dispatches its five named agents — *not* an open-ended "one subagent per strategy". Each area-agent runs *its area's strategy axes internally* (the divergence happens inside the agent); each writes one report file.

> **Dispatch rule — this is what makes delegation actually fire (mirror of `submissions-verification`).** Issue all engaged area-agents as Claude Code **Task** subagents **in the same turn**. Name them explicitly (e.g. "dispatch the Legislation, Case-law and Red-team agents"). Do **not** collapse two areas into one dispatch. Do **not** run the agents yourself, sequentially or inline, when the Task tool is available. If a subagent fails or returns malformed output, **re-dispatch only that agent** — do not patch its report by hand.

Each subagent's Task prompt is assembled from its brief in the matching `references/agent-*.md` file and the self-contained prompt template in `references/templates.md`. It MUST carry: the area mandate + that area's strategy axes; the framed goal with the temporal/jurisdiction anchor and the factual matrix (the agent's slice of the ledger); an instruction to read `references/retrieval-mechanics.md` before any fetch (jurisd Layer 0 first); and the required output schema + output path `agent-reports/cycle<N>-<area>.md`. Subagents share no memory and see neither each other nor the main thread — everything they need is in the prompt. The orchestrator's convergence (Step 4) reads those per-area report files; it never collapses the agents into one opaque pass.

The six area-agents and their internal strategy axes (full briefs in the `references/agent-*.md` files):

- **Legislation agent** (`references/agent-legislation.md`) — statute-first (governing Act + pinpoint provisions, currency as-at-date); amendment-history (the in-force version may differ at the relevant date); definitional/interpretive (defined terms, interpretation provisions, related rules/regs e.g. UCPR). → one statutory map with pinpoints + currency.
- **Case-law agent** (`references/agent-caselaw.md`) — by-statute (cases under the identified provision); by-doctrine (the doctrinal proposition); **by-analogy/factual-matrix** (similar fact patterns / similar legal questions — highest value); by-citator-trail (walk forward/backward from a leading case). → deduped, ranked case table (authority × proximity × recency).
- **Evidence agent** (`references/agent-evidence.md`) — classifies the **evidence regime** (Uniform Evidence Law / non-UEL common-law-plus-Act / tribunal not bound by the rules) and the governing instrument, then pinpoints the evidentiary provisions the question engages, with federal-jurisdiction / lex-fori flags. → the rules of proof that govern here, verified and current.
- **Jurisdiction agent** (`references/agent-jurisdiction.md`) — maps the **forum-specific procedural framework** for the named court/division/list: the constituting & civil-procedure Act(s), the rules of court and regulations, and the **practice notes** in force (from the court's own site). → the procedural rules and practice notes that govern here, verified and current.
- **Secondary agent** (`references/agent-secondary.md`) — commentary/texts (paywalled → jade-research); journals / law-reform; practice notes / court guidance. → a short, clearly-marked *secondary* framing, never presented as primary authority.
- **Red-team agent** (`references/agent-redteam.md`) — best contrary authority (what the other side cites); distinguishing arguments (how your best cases get distinguished on facts/law); currency / overtaken-by-statute. → an adversary brief: the holes and the counter-case.

**Single-threaded fallback — only when the Task tool is absent** (e.g. claude.ai chat has no Task tool). There, and only there, the orchestrator runs each area's brief itself, sequentially — one area at a time — still maintaining the ledger and running the validation gate, and tells the user assurance is lower (no isolated contexts). In Claude Code the Task tool is present, so **always dispatch real subagents; never emulate them inline.**

### Step 4 — Converge each area, then run the orchestrator's evaluation

After an area's agents report (each via its own report file — Step 3), the orchestrator merges that area's strategy outputs and then **reads the substantive findings itself**. This evaluation is the orchestrator's core job — not a rubber stamp on agent output:

- **Read the returned case law** — do the cases actually answer the framed question, or only graze it? Is the *leading* authority present, or only downstream applications? Has an agent returned a case that opens a **new line** (a provision or doctrine not yet searched)? Is a proposition resting on first-instance authority only?
- **Read the returned legislation** — is the controlling provision pinpointed, with the relevant subsections extracted? Is currency fixed as at the temporal anchor? Does a provision cross-refer to rules/regs not yet retrieved?
- **Spot the gaps** — a major task with a thin or negative return; a contrary case the red-team surfaced that nobody has yet checked for its *own* subsequent treatment.

This evaluation is what decides whether the *answer is actually there* or a further cycle is needed (Step 7). It is recorded in the cycle memo.

**Completion criteria.** A task is *resolved* when it has either a verified positive finding (on-source, fetched) or an exhaustive negative finding ("no authority on point after running the defined search paths"). A verified negative is a complete answer, not a failure — do not let agents chase phantoms or invent authority to "succeed". A team's work is complete enough to close at **100%** of its **major**, **&gt;80%** of its **moderate**, and **&gt;51%** of its **minor** tasks resolved.

These thresholds are a **floor, not a licence to drop the remainder**. Before closing a team the orchestrator must (1) list the unresolved tasks in the ledger and (2) review them for load-bearing risk — the obscure contrary case that sinks the matter is often in the unfinished minority. Any unresolved task that is load-bearing is **promoted** (minor→moderate→major) and must meet its higher threshold; an irrelevant task is **demoted** and recorded. This dynamic re-prioritisation is expected.

### Step 5 — Validate this cycle's authorities (the gate runs every cycle)

Run the citation-integrity gate over every candidate authority *this cycle produced*, before it reaches the cycle memo — so each memo reports only validated law. The gate replicates the `submissions-verification` checks so this skill stays standalone; full prompts, output schema, source-authority ranking, and treatment taxonomy are in `references/agent-validation.md`. Dispatch the **five checks as named Task subagents in a single turn** — the same dispatch rule as Step 3 (all in one message; name them; do not collapse two checks into one dispatch; re-dispatch only a failed check). Each writes its own report file. The single-threaded fallback applies only where the Task tool is absent. The five:

1. **Existence** — the case exists on a primary source in the form cited (parties, court, year, medium-neutral + report citation).
2. **Pinpoint** — the cited paragraph/page actually supports the proposition; pinpoint retrieved verbatim.
3. **Quote** — every quoted passage matches the source word-for-word.
4. **Treatment** — still good law as at the temporal anchor; classified Good Law / Reinforced / Qualified / Overruled. Owns the "not overturned on appeal" question in full.
5. **Red-team** — adversarial currency check: hostile authority not addressed, the cited statutory version in force as-at-date, mis-characterised holdings, authority overtaken by statute.

Disputes (any disagreement on existence, pinpoint, quote, or treatment) are reconciled by an independent re-fetch and recorded in the **Reconciliation Log**. Each authority also gets a **how-cited classification** — *followed / applied / cited-in-argument / mentioned-as-history / distinguished* — because a history-only citation carries very different weight from an application of the ratio. Authorities that fail are marked **suspect** and are not presented as good law. An authority cannot be confirmed against a source it could not be fetched from — say so rather than guess.

### Step 6 — Emit the cycle research memo (every cycle)

**Every cycle ends with a research memo**, written to the working directory as **both** `<matter_slug>_cycle<N>_memo.md` **and** `<matter_slug>_cycle<N>_memo.html`, using the memo template in `references/templates.md`; the ledger (Step 8) is updated to match. Memos are cumulative — cycle 2 builds on cycle 1 — so the final cycle's memo is the consolidated deliverable. Each memo contains at minimum, in this order:

- **the user's query verbatim**, then the **goal and per-area subgoals** the orchestrator framed — placed up front so the reader can confirm the task was understood and adequately decomposed *before* reading the analysis (mandatory);
- what *this* cycle was tasked to resolve;
- **for every case — presented in a table whose every row carries (i) the case name as a hyperlink to its judgment URL, (ii) a factual summary, and (iii) a paragraph pinpoint** — together with its citation (medium-neutral + authorised report), the relevant verbatim quote(s), treatment status, and the how-cited classification, exactly as the case-law agents returned them in their schema. The same hyperlink + factual-summary + pinpoint rule applies to *every* case table in the memo, including the authorities/verification table;
- **for every statutory provision** — the Act and section, the **extracted text of the relevant subsection(s)**, currency as at the temporal anchor, and the source URL;
- **the governing evidence regime** — UEL / non-UEL / tribunal-not-bound — the governing Evidence Act (or the provision dis-applying the rules) and the engaged evidentiary provisions, as the evidence agent returned them;
- **the forum-specific procedural framework** — the court's constituting/procedure Act(s), the rules of court engaged, and the practice note(s) in force (version + date), as the jurisdiction agent returned them;
- the red-team's contrary-authority section;
- the authorities / verification table (verified / suspect / overridden + treatment + how-cited + **AGLC4 citation** per `references/aglc4-citation.md`); the **final** cycle's memo also appends an AGLC4 Table of Authorities (templates §9a);
- the orchestrator's evaluation: what is now answered, what gaps remain, and the spawn decision for the next cycle.

The `.html` deliverable mirrors the `.md` exactly (same tables, working case hyperlinks) and carries a fixed **Download PDF** button — build it from the HTML wrapper in `references/templates.md` (render the markdown to HTML, drop it into the wrapper's `<main>` slot).

### Step 7 — Decide on a further cycle

On the strength of the Step 4 evaluation, decide whether a new cycle with new delegated tasks is warranted. Findings routinely *generate* the next cycle: the legislation team returns a controlling provision and its sub-clauses → spawn a fresh case-law team for cases decided under that provision sharing the factual matrix; the red-team surfaces a contrary line → a new case-law task checks whether that line has itself been distinguished or doubted. New tasks go to **new subagents**, each with its slice of the updated ledger.

**Cycle cap: 3.** A third cycle requires the orchestrator to record, in the ledger, why the goal is not yet met and what the third cycle will resolve. If the goal is still unmet after three cycles, report what was found, what remains open, and why — do not loop indefinitely or pad the answer.

### Step 8 — The research ledger (orchestrator-owned, persisted)

Because subagents share no memory, the orchestrator maintains the single source of truth: a markdown ledger (`<matter_slug>_research_ledger.md`), updated every cycle. Schema in `references/templates.md`. It holds the framed goal, per-area task-lists with major/moderate/minor tags and resolved/unresolved status, an **index of each agent's individual report file** for the cycle (so every agent's work stays separately inspectable), verified findings keyed to source URLs, the follow-up/spawned-task register, the re-prioritisation log, and the running authorities table. The orchestrator slices the relevant parts of the ledger into each new subagent prompt — never assumes a subagent knows anything not in its prompt.

### Step 9 — Whole-goal stopping condition

The goal is complete when **all** hold: every **major** task across all teams is resolved; no **load-bearing** follow-up remains open (immaterial gaps may remain, listed); the **validation gate has passed** on every relied-upon authority; and the question can be answered with **verified, pinpointed sources**, *or* the orchestrator can state definitively that the law is unsettled / no authority is on point. The consolidated final memo is the last cycle's memo. Do not declare completion while a major task is unresolved or any relied-upon authority is unverified.

---

## Presenting results

**A bounded-retrieval result (trivial Stage-1 decomposition)** — present the judgment/section text in a markdown artifact with the source URL (and, for NSW, the DOCX export link; for AustLII, the RTF/PDF links). Search results as a table: case name, citation, court, date, short excerpt. Quote verbatim with paragraph numbers; flag suspected OCR errors.

**A research-question result (full roster)** — the deliverable is the **cycle research memo** (template in `references/templates.md`), produced every cycle and consolidated in the final cycle, and shipped as **both a `.md` file and a `.html` file (the HTML carrying a Download-PDF button)**. It opens with **the user's query verbatim and the goal/subgoals decomposition** — so the reader can confirm the task was understood and adequately broken down before reading on — then: a short answer; the law — a legislation map with extracted subsections, and a ranked **case table in which every case name is hyperlinked to its judgment and every row carries a factual summary and a paragraph pinpoint**, alongside its citation and relevant verbatim quotes; application to the facts; an explicit **contrary-authorities** section (from the red-team); and an **authorities / verification table** (case names hyperlinked) showing each authority's validation status (verified / suspect / overridden), treatment classification, and how-cited classification. Each agent's individual report file is available alongside the memo for inspection. Offer a `.docx` build via the docx skill for a filing-style deliverable. Every authority traces to a fetched source URL.

## Relationship to sibling skills

- This skill **finds and self-validates** authorities for a research question. Use it for lookup and research.
- **`submissions-verification`** verifies the citations in an *already-drafted* document end-to-end (and produces a primer + table of authorities + cleaned docx). Use it when the user has a finished submission in hand, not a research question.
- **`written-submissions` / `nsw-pleadings`** are drafting skills. They *consume* this skill's output.

If two could apply, ask which the user wants rather than silently picking.

## Reference files

- `references/retrieval-mechanics.md` — **read before any fetch.** Tool-selection cheat sheet, URL patterns, legislation slugs, web-search recipes, the Jade free-tier mechanics (bare fetches 403 — resolve via `site:jade.io` search, open in Chrome), metadata extraction, the free-source citator recipe (LawCite is walled; Jade's citation panel is the best seed), source-authority ranking, recovery when a fetch fails, court hierarchy.
- `references/aglc4-citation.md` — AGLC4 citation formatting: cases (medium-neutral / reported / combined), legislation, pinpoints, short forms (ibid / (n N)), and the Table-of-Authorities ordering — the hand-format equivalent of jurisd's `format_citation`/`bibliography`.
- `references/agent-legislation.md` — legislation team: strategy axes, brief, and output schema (section + extracted subsection text + currency + URL).
- `references/agent-caselaw.md` — case-law team: strategy axes (incl. factual-matrix/analogical search), brief, ranking method, how-cited classification, and output schema (citation + factual summary + relevant paragraphs + relevant quotes + AustLII URL).
- `references/agent-evidence.md` — evidence team: the regime decision tree (UEL / non-UEL / tribunal-not-bound), federal-jurisdiction & lex-fori overlays, brief, and output schema (regime + governing instrument + engaged evidentiary provisions).
- `references/agent-jurisdiction.md` — jurisdiction team: the forum-specific procedural framework — constituting/procedure Acts, rules of court & regulations, and practice notes (from the court's site) — brief, and output schema.
- `references/agent-secondary.md` — secondary-sources team: scope, sources, output schema.
- `references/agent-redteam.md` — adversarial team: strategy axes, brief, output schema.
- `references/agent-validation.md` — the five-check citation-integrity gate (five named Task subagents, dispatched in one turn) + reconciliation protocol + source-authority ranking + treatment taxonomy (replicates submissions-verification).
- `references/templates.md` — research-ledger schema, the self-contained subagent prompt template, the per-agent output schemas, and the **per-cycle research-memo template** (verbatim-query + goal/subgoals header, hyperlinked case tables with factual summary + pinpoint, and the HTML+PDF-export wrapper for the dual `.md`/`.html` deliverable).

Per-cycle working files the orchestrator writes: `<matter_slug>_research_ledger.md`, `agent-reports/cycle<N>-<area>.md` (one per area-agent) and `agent-reports/cycle<N>-validation-<check>.md` (one per gate check), and `<matter_slug>_cycle<N>_memo.md`.

---
name: claude-submission-drafting-acor8826
title: Submission Drafting (multi-agent)
description: 'Persuasive writing as a multi-agent orchestration modelled on Chester Porter QC''s The Gentle Art of Persuasion. Stage 1: the Lead Strategist (''Smiling Funnel-Web'') decomposes the brief into a persuasion goal and ID''d weighted subgoals, hardens the frame (Frame Challenger + Issue Spotter), confirms it with the user. Stage 0: where a load-bearing point turns on law, runs the australian-legal-research method into a verified authorities pack before drafting. Stage 2: dispatches Fact Finder + Devil''s Advocate as parallel Task subagents, builds the funnel (Diplomat then Plain Speaker passes), runs the Porter gate plus a release-blocking citation check, and cycles. USE to move a specific reader to a conclusion by courtesy, fact, and pre-emptive concession, not force. Triggers: ''make this more persuasive'', ''win over the reader'', ''anticipate objections'', ''draft a persuasive letter/email/board paper'', ''Calderbank offer'', ''letter of demand'', ''Chester Porter'', ''funnel-web''.
  For court filings see written-submissions.'
author: acor8826
author_url: https://github.com/acor8826/claude-submission-drafting
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: general
language: en
sources:
- title: Agent Devils Advocate
  path: references/agent-devils-advocate.md
- title: Agent Diplomat
  path: references/agent-diplomat.md
- title: Agent Fact Finder
  path: references/agent-fact-finder.md
- title: Agent Lead Strategist
  path: references/agent-lead-strategist.md
- title: Agent Plain Speaker
  path: references/agent-plain-speaker.md
- title: Frame Hardening
  path: references/frame-hardening.md
- title: Legal Intelligence
  path: references/legal-intelligence.md
- title: Porter Gate
  path: references/porter-gate.md
- title: Porter Method
  path: references/porter-method.md
- title: Templates
  path: references/templates.md
---

# Submission Drafting (multi-agent)

## Overview

This skill turns a brief or a draft into a piece that persuades a **specific reader** the way Chester Porter persuaded a tribunal: by courtesy, undisputed fact, and frank pre-emptive concession, never by force. It is register-general — the reader may be an opponent's solicitor, a regulator, a board, a client, a counterparty, or the reader of an essay. It runs as an **orchestrated, multi-agent pass**: the Lead Strategist decomposes the task, hardens and confirms the frame, runs **legal intelligence (Stage 0)** where any load-bearing point turns on law, dispatches the intelligence roster, reconciles, builds the **funnel**, and self-audits the prose against Porter's doctrines (plus a release-blocking citation gate) before release.

The team is a fixed roster of five persuasion agents (full briefs in `references/agent-*.md`):

1. **Lead Strategist — "Smiling Funnel-Web"** — *the orchestrator.* Frames the goal, decomposes it, converges, builds the funnel, makes the final call.
2. **Fact Finder** — verifies facts, strips hyperbole, sequences the fact base chronologically.
3. **Devil's Advocate** — maps every objection the reader could raise, each with its disarming concession.
4. **Diplomat** — the register pass: courtesy, charm, humility; aggression rewritten into reasonable queries.
5. **Plain Speaker** — the clarity pass: jargon and friction removed so the logic lands first time.

Three further elements are dispatched conditionally, not part of the persuasion roster: the **Frame Challenger** and **Issue Spotter** (frame-hardening passes before checkpoint 1 — `references/frame-hardening.md`), and the **legal-intelligence roster** borrowed by reference from the `australian-legal-research` skill (Stage 0 — `references/legal-intelligence.md`).

Every agent reads `references/porter-method.md` (Porter's doctrines as nine operational rules) **before writing anything** — the orchestrator owns strategy; the canon owns method. (This is the analogue of a mechanics reference every agent loads first.)

## Model assignment

Roles are pinned to models:

- **Orchestrator — the Lead Strategist → Claude Fable.** All orchestrator work runs on Fable: framing and decomposition (Stage 1), convergence (Step 4), the gate reconciliation (Step 6), and the **final integrity check** over every agent's output before release (Step 9).
- **Specialist agents — Fact Finder, Devil's Advocate, Diplomat, Plain Speaker → Claude Opus** (`claude-opus-4-8`), each dispatched as an Opus Task subagent.
- **Frame-hardening passes — Frame Challenger, Issue Spotter → Claude Opus**, dispatched in parallel during Stage 1.
- **Stage-0 legal-intelligence agents → Claude Opus**, dispatched per the `australian-legal-research` method (the orchestrator, on Fable, runs that skill's orchestration itself — subagents cannot spawn subagents).
- **Gate checks — all seven → Claude Opus** (`claude-opus-4-8`), dispatched as Opus Task subagents.
- **Final check → Fable.** No agent output — fact base, objection map, funnel draft, editing passes, or gate reports — ships until the Fable orchestrator has reviewed all of it and made the release decision (Step 9).

The orchestrator sets each subagent's model when it dispatches the Task (or, if the briefs are promoted to standalone Claude Code agent-definition files, via each file's `model:` frontmatter — `model: opus` on the five agents and the six gate checks, with the skill itself run on Fable).

**Availability.** Fable is a Mythos-tier model and access may be restricted (e.g. suspended under an export-control directive). Its API model string is `claude-fable-5`, but the alias exposed to Claude Code sessions can differ — confirm it for your environment. If Fable is unavailable in the session, the orchestrator falls back to Opus for every role and records the fallback in the ledger; the assignment above is the design target, not a hard runtime dependency.

## CRITICAL: The Credibility Principle

**The moment the reader catches one exaggeration — one unsupported "fact", one hollow concession — they discount everything else, permanently.** Credibility is the only currency, and it is spent once. So: never assert a fact the Fact Finder has not verified; never write a concession that is not genuine; prefer understatement to overstatement. An unverifiable point is cut or marked as assertion, never smuggled in as fact. Synthesis produces three states for any load-bearing fact — **verified, unsourced, or recast** — never "probably true". This is the persuasion analogue of a verification principle: the skill's power is being trustworthy on the page, not loud.

---

## Architecture: orchestration → legal intelligence → diverge-converge

One architecture with a conditional middle stage. The stages are **sequential parts of a single flow — not alternative modes you choose between**:

- **Stage 1 — Orchestration.** The Lead Strategist decomposes the task into a **persuasion goal** and the **subgoals each agent must fulfil** (each with a durable ID), hardens the frame (Frame Challenger + Issue Spotter), and confirms it with the user at **checkpoint 1**. Nothing is dispatched into Stage 2 until the frame is confirmed. (Steps 1–2.)
- **Stage 0 — Legal intelligence (conditional).** Runs **after Stage 1 and before Stage 2** — the frame generates the research; it is numbered 0 because it supplies raw material upstream of all persuasion work. If any **load-bearing subgoal is tagged `legal`**, the orchestrator runs the `australian-legal-research` method over exactly those subgoals and converges the findings into a **verified authorities pack**. Drafting is blocked until the pack lands. Full spec: `references/legal-intelligence.md`.
- **Stage 2 — Diverge-converge.** It dispatches the intelligence roster **in a single turn** (diverge), **reads and reconciles** their reports itself (converge), **synthesises** the prose as a funnel and runs the polish passes, then runs the **Porter gate** (seven checks where the piece cites law). Stage 2 runs in **cycles**: dispatch → converge → synthesise → gate → assess → decide whether a further cycle is warranted. (Steps 3–9.)

**The decomposition scales to the task; the architecture does not change.** A one-line apology or a two-sentence ask is a *trivial* Stage-1 decomposition — one fact subgoal, one objection subgoal (often the Devil's Advocate alone), which Stage 2 satisfies in a single light pass. A contested Calderbank offer, a regulator response, or a board paper carrying a hard recommendation decomposes into the full roster across one or more cycles. Same two stages either way; only the number of subgoals, agents, and cycles differs. The orchestration is never skipped — for a short piece it is just small.

**Proportionality rule (dispatch scales with the decomposition).** For a **trivial decomposition** the orchestrator MAY run the synthesis passes (Step 5) and the Porter gate (Step 6) itself, inline, as consolidated passes — the Diplomat and Plain Speaker moves applied in sequence, then all gate checks judged in one audit sweep — recording `dispatch: inline (trivial)` in the ledger; the frame-hardening passes may also be skipped (`frame: unhardened (trivial)`). Every doctrine still applies (the funnel, the honesty guard, the outcome states); only the subagent ceremony is collapsed. **Stage 0 and gate check 7 sit above the proportionality line entirely** — a load-bearing `legal` subgoal always gets the full legal-intelligence treatment; a wrong citation is never trivial. For any **contested or full-roster piece** — anything with a load-bearing objection, an adversarial or regulatory reader, or stakes the user would litigate over — the dispatch rules are mandatory: real Task subagents, in parallel, isolated contexts. The test is stakes and contestedness, not length: a two-line concession to an opponent's solicitor is full-dispatch work.

---

## Stage 1 — Orchestration (decompose the task)

Stage 1 is the Lead Strategist's own work: turn the request into a fixed **persuasion goal** and the **subgoals each agent must fulfil**. It produces no prose — it produces the plan the agents execute in Stage 2. Everything fixed here is recorded in the ledger (Step 8) and sliced into each agent's prompt.

### Step 1 — Frame the persuasion goal

Before delegating, the Lead Strategist fixes and records (in the ledger):

1. **The reader** — who decides; their role, priors, fears, what moves them, the relationship (adversary / regulator / client / superior / neutral). Porter's first move is *know the tribunal*.
2. **The desired conclusion** — the single thing the reader should believe or do at the end, in one sentence. If several, rank them; the funnel ends on the top one.
3. **The controlling proposition** — the one load-bearing claim the whole piece exists to establish. Everything not serving it is colour.
4. **The reader's starting position and resistances** — where the reader stands now, and the specific objections, suspicions, and counter-narratives they hold. This is the Devil's Advocate's brief.
5. **Register and constraints** — channel, length ceiling, formality, what *must* be conceded, what *cannot* be conceded, any house/jurisdictional rules.

Before framing, the Lead Strategist reads `matter-context.md` if one exists in the working directory (schema in `references/frame-hardening.md`) — the standing record of parties, procedural history, adverse findings, and live issues — so the frame is never built from a cold prompt; the user's brief supplies only the delta.

If any of these cannot be fixed from the request, the Lead Strategist makes the most reasonable assumption, **records it explicitly in the ledger with its consequence-if-wrong**, and proceeds — it does not stall on something the user can correct later. Only goal-changing ambiguity (the wrong reader, the wrong conclusion) is worth pausing for.

**Frame hardening (contested pieces — runs in parallel with framing).** The orchestrator dispatches two Opus subagents in one turn (`references/frame-hardening.md`): the **Frame Challenger**, which attacks the frame itself — is this the real decision-maker; does the desired conclusion over-reach what any reader in this position would grant; what conclusion is the piece actually capable of earning — and the **Issue Spotter**, which reads the supplied materials (not just the brief) against a fixed checklist and returns candidate issues the brief did not raise. The orchestrator diffs the Issue Spotter's list against the tagged subgoals and carries the delta into checkpoint 1.

**Checkpoint 1 — frame confirmation (MANDATORY on contested pieces).** Before any Stage-0 or Stage-2 dispatch, the orchestrator presents the frame to the user using the checkpoint-1 template in `references/frame-hardening.md`: the framed goal; the subgoal table with IDs, weights, and `legal` tags; the Frame Challenger's objections (unresolved, not pre-answered); the Issue Spotter delta ("materials disclose X; brief didn't raise it; proposed as <ID> — confirm or strike"); each assumption with its consequence-if-wrong; and the **negative space** — what the run is *not* researching and *not* addressing, stated plainly so omissions are visible rather than silent. The flow proceeds on the user's confirmation or corrections; the confirmed frame is versioned in the ledger. A frame correction at any later point re-triggers only the affected subgoal chain, not a restart.

### Step 2 — Decompose into agent subgoals (task-lists; load-bearing / supporting / colour)

The Lead Strategist drafts the task-lists — **these are the subgoals each agent must fulfil in Stage 2** — and gives every subgoal a **durable ID** (`F1, F2…` fact subgoals; `O1, O2…` objection subgoals). **The ID propagates unchanged through the whole run** — ledger → Stage-0 dispatch → authorities-pack entry → fact base → funnel-map beat → gate check 7 → audit chain table — so every sentence of the release candidate traces back to the goal it serves. Every task is tagged by weight:

- **Load-bearing** — the conclusion *cannot* be reached without it. (The key fact the funnel turns on; the objection that, unanswered, sinks the piece.)
- **Supporting** — materially strengthens or qualifies, but the goal survives a gap.
- **Colour** — completeness and texture; marginal.

Additionally, any subgoal that turns on an authority, a statutory provision, a holding, or "is this still good law" is tagged **`legal`**. **Any load-bearing `legal` subgoal triggers Stage 0** before Stage 2 dispatch.

The two intelligence task-lists: **fact subgoals** (Fact Finder) and **objection subgoals** (Devil's Advocate). Which agents to engage is the orchestrator's call — a trivial piece may need only the Fact Finder; **almost every contested piece needs the Devil's Advocate** (surfacing the reader's best objection is the highest-value output). The Diplomat and Plain Speaker are not part of the decomposition — they are fixed synthesis passes in Step 5.

---

## Stage 0 — Legal intelligence (conditional; runs after checkpoint 1, before Stage 2)

Full spec in `references/legal-intelligence.md`. In brief: the orchestrator (Fable, main thread — the only thread that can dispatch Tasks) reads the `australian-legal-research` skill's SKILL.md itself, decomposes the `legal`-tagged load-bearing subgoals per **that skill's method**, scopes its roster to what the subgoals need (often case-law + legislation + red-team, not all six agents), dispatches them as top-level Opus Task subagents, and runs that skill's citation-integrity gate as designed. The subgoals — with their IDs and weights — are passed **verbatim** as the research goal; no translation layer, no topic-level drift.

**Output: the verified authorities pack** — `agent-reports/<piece_slug>/cycle<N>-authorities-pack.md` (schema: `templates.md` §3.4). Every entry is keyed to its subgoal ID and carries the proposition, the authority, a live AustLII/CaseLaw NSW URL, and treatment status (good law / doubted / distinguished / overruled). **A clean negative is a complete answer**: `F3 → not supported at this strength; supportable as <weaker proposition>` flows straight back into Step 1 — the orchestrator softens the desired conclusion *before drafting* and reports this to the user; that message is a strategy signal, not noise.

**Drafting is blocked until the pack lands.** The pack is thereafter the **only permissible source of legal fact** in the piece (enforced at the Fact Finder and at gate check 7). **Top-ups are targeted**: a mid-run legal question (an `UNSOURCED-LEGAL` tag from the Fact Finder, a `needs a fact → legal` routing from the Devil's Advocate, a check-7 FAIL) opens a new cycle with a single-question Stage-0 dispatch — usually one agent — never a full roster re-run.

---

## Stage 2 — Diverge-converge (agents fulfil their subgoals; orchestrator converges, synthesises, gates, cycles)

### Step 3 — Dispatch the intelligence agents (diverge)

The Lead Strategist dispatches **the engaged intelligence agents as named Task subagents — all in a single turn / one message** so they run in genuinely parallel, isolated contexts. Each runs its strategy axes internally and writes one report file.

> **Dispatch rule — this is what makes delegation actually fire.** Issue all engaged intelligence agents as Claude Code **Task** subagents **in the same turn**, **each on Opus (`claude-opus-4-8`)**. Name them explicitly. Do **not** collapse two agents into one dispatch. Do **not** run the agents yourself, inline, when the Task tool is available. If a subagent fails or returns malformed output, **re-dispatch only that agent** — do not patch its report by hand.

Each subagent's Task prompt is assembled from its brief in the matching `references/agent-*.md` file and the self-contained prompt template in `references/templates.md` §2. It MUST carry: the agent's mandate + its strategy axes; the framed goal (its slice of the ledger — reader, desired conclusion, controlling proposition, resistances); its weighted task-list; an instruction to read `references/porter-method.md` before writing; and the output schema + path (`agent-reports/<piece_slug>/cycle<N>-fact-base.md` / `agent-reports/<piece_slug>/cycle<N>-objection-map.md`). Subagents share no memory — everything they need is in the prompt.

- **Fact Finder** → separates fact from opinion; verifies every load-bearing fact against a source (tag sourced/unsourced); strips hyperbole; sequences the surviving facts chronologically.
- **Devil's Advocate** → enumerates every objection the reader could raise, ranks each by bite, and writes the frank concession or pre-emption for each.

**Single-threaded fallback — only when the Task tool is absent** (e.g. claude.ai chat): the Lead Strategist runs each engaged agent's brief itself, sequentially, still maintaining the ledger and running the gate, and tells the user assurance is lower (no isolated contexts). In Claude Code the Task tool is present, so **always dispatch real subagents; never emulate them inline.**

### Step 4 — Converge (reconcile the intelligence; evaluate)

After the intelligence agents report (each via its own file), the Lead Strategist **reads the substance itself** — not a rubber stamp:

- **Read the fact base** — do the verified facts actually carry the controlling proposition, or only graze it? Is any load-bearing fact unsourced (→ cannot be asserted as fact; source it or recast it)? Does the chronology suggest a cleaner order for the funnel?
- **Read the objection map** — which objections are load-bearing? Is any concession hollow (→ reject)? Does an adverse fact need building into the narrative early rather than rebutted late?
- **Spot the gaps** — a load-bearing fact with a thin/negative return; an objection with no real answer (→ the conclusion may need to soften).

**Completion criteria.** A task is *resolved* when it has a verified positive finding or an exhaustive negative ("this cannot be verified after these sources" / "no honest answer to this objection"). A verified negative is a complete answer, not a failure. A roster's work is closeable at **100% of load-bearing**, **>80% of supporting**, **>51% of colour** tasks resolved — a **floor, not a licence to drop the rest**. Before closing, the orchestrator lists the unresolved tasks and reviews them for load-bearing risk: the obscure objection that sinks the piece is often in the unfinished minority. **Dynamic re-prioritisation is expected** — promote a task that turns out load-bearing (colour→supporting→load-bearing) to its higher threshold; demote an irrelevant one and record it.

### Step 5 — Synthesise the prose (build the funnel, then polish in series)

This is the cycle's product. The Lead Strategist builds the **funnel draft** from the verified fact base and the objection map; then the **Diplomat** (register) and the **Plain Speaker** (clarity) run as **sequential** passes, each on the previous output, clarity last. **Each polish pass receives the funnel map and concession register paths** so every placed concession and adverse fact is identifiable as a protected line, not guessed at. (Trivial decomposition: the passes may run inline under the proportionality rule.)

The funnel discipline (Rule 5): open wide on agreed ground; lay undisputed facts strongest-first so each step is a small unarguable move; place must-concede points early and frankly; narrow until the desired conclusion is the only reasonable landing; state it quietly; **stop** (Rule 9). Emit the funnel map (`templates.md` §4) and the release candidate.

> **Why the polish passes are sequential, not a diverge.** Fact Finder and Devil's Advocate produce *material* and never touch each other's work (parallel, Step 3). Diplomat and Plain Speaker *transform the same prose in series* — register first, clarity last, so the clarity pass has the final word and nothing the register pass added survives as friction. This is the one deliberate departure from a pure diverge-converge.

### Step 6 — Run the Porter gate (every cycle)

Run the self-contained Porter-principles gate over the cycle's release candidate, **before** it is reported — so each cycle yields only audited prose. Where the Task tool is present, **dispatch the engaged checks (six, or seven where law is cited) as named Task subagents in a single turn, each on Opus (`claude-opus-4-8`)** (same dispatch rule as Step 3 — name them; don't collapse; re-dispatch only a failed check), then run a seventh **reconciliation** pass yourself **on Fable**; else the orchestrator runs them sequentially. A trivial decomposition may instead take the inline consolidated gate under the **proportionality rule** (Architecture, above). The **common dispatch contract, the six paste-verbatim role prompts, the honesty guard, the reconciliation protocol, and the outcome states** are in `references/porter-gate.md`. The six standing checks: no aggression (Diplomat) · fact over opinion (Fact Finder) · self-reached conclusion (Lead Strategist) · honest pre-emptive concession (Devil's Advocate) · plain language (Plain Speaker) · brevity (Lead Strategist / Plain Speaker). **A seventh, release-blocking check — citation integrity — runs whenever the piece cites any authority**: every citation in the release candidate must trace to an authorities-pack entry that is verbatim-correct and not adversely treated; a FAIL routes to a Stage-0 top-up, never to a prose fix. A failed check routes to its owner; re-run the gate on the changed sections. The **honesty guard overrides all checks**: a check is never passed by weakening the truth.

### Step 7 — Decide on a further cycle

On the strength of the Step 4 evaluation and the Step 6 gate, decide whether a new cycle with new delegated tasks is warranted. **Findings routinely generate the next cycle:** the Devil's Advocate flags an objection with no honest answer → cycle 2 re-frames the goal with a softened conclusion and re-dispatches; the Fact Finder returns an unsourced load-bearing fact → cycle 2 dispatches a targeted sourcing subgoal (or the Lead Strategist recasts the point); a gate check fails on this cycle's material → cycle 2 carries new subgoals to fix it. **`Needs a fact` findings split by kind:** factual → Fact Finder; legal → a targeted Stage-0 top-up (new `F# [legal]` subgoal). **Checkpoint 2 — strategic re-frames are surfaced, not made silently:** where a finding changes the *strategy* (softening the conclusion, conceding a matter the user said mattered, restructuring the offer), the orchestrator states the finding, the recommended re-frame, and asks the user to approve before the cycle dispatches; tactical fixes within the confirmed frame proceed without a pause. New tasks go to **new subagents**, each with its slice of the updated ledger.

**Cycle cap: 3.** A third cycle requires the orchestrator to record, in the ledger, why the goal is not yet met and what the third cycle will resolve. If the goal is still unmet after three cycles, release what was built, **name the residual weakness**, and stop — do not loop or pad.

### Step 8 — The persuasion ledger (orchestrator-owned, persisted)

Because subagents share no memory, the Lead Strategist maintains the single source of truth: a markdown ledger (`<piece_slug>_persuasion_ledger.md`), updated every cycle. Schema in `references/templates.md` §1. It holds the framed goal; the fact/objection task-lists with weight tags and resolved/unresolved status; an **index of each agent's report file** per cycle (so every agent's work stays separately inspectable); the verified fact base keyed to sources; the **concession register**; the follow-up/spawned-task register; the re-prioritisation log; and the gate results. The orchestrator slices the relevant parts of the ledger into each new subagent prompt — never assumes a subagent knows anything not in its prompt.

### Step 9 — Whole-goal stopping condition

The goal is complete when **all** hold: every **load-bearing** fact subgoal and objection subgoal is resolved; no load-bearing follow-up remains open (immaterial gaps may remain, listed); the **gate has passed** on the release candidate — including check 7 where law is cited, which is release-blocking and never waived into a named weakness (or the six Porter checks are released-with-named-weakness after the cycle cap); and the piece persuades on **verified facts**, *or* the orchestrator can state definitively that the conclusion must soften because the facts do not support it. The final release candidate is the last cycle's. Do not declare completion while a load-bearing subgoal is unresolved or the gate has not passed.

**Final integrity check (Fable) — mandatory before release.** No agent output ships until the orchestrator, **on Fable**, has performed a final review of *all* of it end to end: the confirmed frame and its version log (every FRAME-MISS logged), the authorities pack where Stage 0 ran (every load-bearing legal proposition keyed to a live source and clean of adverse treatment), the Fact Finder's fact base (every load-bearing fact sourced, no opinion smuggled in as fact), the Devil's Advocate's objection map (every load-bearing objection met by a genuine concession), the funnel draft and the Diplomat/Plain Speaker passes (structure, register, clarity intact), and the six gate-check reports plus the reconciliation log (all checks resolved, honesty guard satisfied). This is the capstone application of the Credibility Principle — the Fable orchestrator, not any Opus agent, owns the release decision (CLEAN / RELEASED WITH NAMED WEAKNESS) and signs off the audit (`templates.md` §6). If Fable is unavailable, the check runs on the Opus fallback and the ledger records that the final check was not performed on Fable.

---

## Presenting results

**A trivial decomposition** (short piece, one light pass) — return the finished piece, gate-passed, with no ceremony; the funnel map and ledger are available if asked.

**A full-roster result** — the deliverable is the **release candidate** (gate-passed), optionally with the **persuasion audit**: the user's brief; the framed goal + subgoals decomposition **with the chain table** (goal → subgoal ID → pack entry → funnel beat — the user's 30-second pre-send check); the **funnel map** (ordered beats + what each does, each beat naming the subgoal IDs it serves); the **concession register** (objection → concession → placement); the **Porter-gate result** (checks, pass/fail, fixes applied); and any **FRAME-MISS log** (issues surfaced downstream that the confirmed frame missed — feedback that hardens the Issue Spotter checklist and `matter-context.md` for the next run). Each agent's report file is available alongside, per cycle, for inspection. Offer a `.docx` build via the docx skill for a sendable deliverable. Every load-bearing fact traces to a verified source.

Per-cycle working files: `<piece_slug>_persuasion_ledger.md`; `agent-reports/<piece_slug>/cycle<N>-fact-base.md`, `agent-reports/<piece_slug>/cycle<N>-objection-map.md`, `agent-reports/<piece_slug>/cycle<N>-authorities-pack.md` (where Stage 0 ran), `agent-reports/<piece_slug>/cycle<N>-frame-challenge.md`, `agent-reports/<piece_slug>/cycle<N>-issue-spotting.md`; `agent-reports/<piece_slug>/cycle<N>-gate-<check>.md` (one per gate check); `<piece_slug>_cycle<N>_release.md`; and the standing `matter-context.md`.

**CONFIDENTIALITY — the working files are a candid weakness map.** The ledger, objection map, concession register, and persuasion audit record every weakness in the user's position, every objection with no honest answer, and every softening applied — exactly what a counterparty would pay to read. **Only the release candidate is ever sent.** Never attach, paste, or transmit the audit or any working file to the reader; when building a `.docx`, build it from the release candidate alone. In a litigation context, treat the working files — including `matter-context.md` — as privileged work product: keep them out of shared/discoverable folders and remind the user of this when handing over the deliverable. **A hand-edit to a gate-passed release candidate is an unaudited claim** — feed edits back as a new cycle instead.

## Relationship to sibling skills

- **`written-submissions`** applies *this same engine* to NSW/Australian court submissions — it adds the court corpus (forums, exemplars, drafting patterns) and a seventh, release-blocking citation-verification gate-check. Use it when the piece is a court document.
- **`document-improvement-skill`** works the **Aristotelian** layer (audience premises, ethos/pathos/logos, enthymemes). They chain: design the argument there, then set the gentle, disarming register and build the funnel here.
- **`australian-legal-research`** is consumed *inside* this skill as Stage 0 — the user does not run it as a pre-step, paste authorities into the brief, or verify citations manually. **One exception:** a genuinely novel legal theory should be tested by a standalone `australian-legal-research` run *first* (does the theory hold at all?), with its report supplied in the materials; Stage 0 then verifies rather than discovers. Non-filing legal pieces — Calderbank offers, letters of demand, regulator responses — belong here with Stage 0; a **court filing** belongs to `written-submissions`.

If two could apply, ask which the user wants rather than silently picking.

## Reference files

- `references/porter-method.md` — **read before writing anything.** Porter's nine operational rules (the mechanics every agent loads first).
- `references/agent-lead-strategist.md` — the orchestrator: goal-framing, decomposition, convergence, the funnel-construction method, the final call.
- `references/agent-fact-finder.md` · `agent-devils-advocate.md` — the two intelligence agents: strategy axes, dispatch envelope, role prompt, output schema.
- `references/agent-diplomat.md` · `agent-plain-speaker.md` — the two synthesis passes (register, then clarity); lane boundaries.
- `references/legal-intelligence.md` — **Stage 0**: trigger, roster scoping, verbatim-subgoal dispatch, authorities-pack contract, clean negatives, targeted top-ups, check-7 routing.
- `references/frame-hardening.md` — the Frame Challenger and Issue Spotter role prompts, the issue-spotting checklist, the checkpoint-1 template (with negative space), the `matter-context.md` schema, FRAME-MISS logging, and the optional duet cross-check.
- `references/porter-gate.md` — the gate: common dispatch contract, seven **paste-verbatim** role prompts (dispatched as named Task subagents in one turn), honesty guard, reconciliation pass, outcome states, cycle cap.
- `references/templates.md` — persuasion-ledger schema, the self-contained subagent prompt template, the two intelligence output schemas (with worked examples, the *required-fields-mandatory* rule, and the *Note for orchestrator* handoff that drives the cycle), the funnel-map + concession-register formats, the per-cycle release + gate-result schema, and the per-cycle deliverable (persuasion audit) template.

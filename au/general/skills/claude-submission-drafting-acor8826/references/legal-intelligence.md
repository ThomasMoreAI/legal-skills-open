# Stage 0 — Legal Intelligence

Runs **after checkpoint 1, before Stage 2**, whenever any **load-bearing subgoal is tagged `legal`**. The frame generates the research: Stage 0 researches the *subgoals* — the specific propositions this reader must accept for this conclusion — never the topic at large. Stage 0 sits **above the proportionality line**: it is never collapsed inline; a wrong citation is never trivial.

## Why this shape

Task subagents cannot dispatch their own Tasks, so the two rosters cannot nest — they must hang off the same top-level orchestrator, sequenced as phases. Research produces *material*; persuasion consumes it. Drafting on unverified law to save time is the exact failure mode the sequencing exists to prevent.

## Method — by reference, not by copy

The orchestrator (Fable, main thread) **reads the `australian-legal-research` skill's SKILL.md itself** and executes that skill's orchestration directly:

1. **Scope the research goal.** The research goal *is* the set of load-bearing `legal` subgoals, passed **verbatim with their IDs and weights** — e.g. `F3 [legal, LB]: "unreasonable rejection of a Calderbank offer grounds indemnity costs from the date of the offer — current NSW position"`. No translation layer; no topic-level drift.
2. **Scope the roster.** Engage only the specialist agents the subgoals need (commonly case-law + legislation + red-team; evidence / jurisdiction / secondary only where a subgoal calls for them). The red-team agent is **never** dropped — attacking the findings is what surfaces adjacent authority a narrow subgoal would miss.
3. **Dispatch** the scoped roster as top-level Opus Task subagents per that skill's dispatch rules, converge per its method, and run its **five-check citation-integrity gate** as designed.
4. **Converge into the authorities pack** (below). Record the Stage-0 run — roster engaged, gate result, unresolved items — in the persuasion ledger.

Because the method is a pointer, improvements to `australian-legal-research` are inherited automatically. If that skill's output schema changes, the pack contract below is the seam to re-check.

## The authorities pack — the only permissible source of legal fact

`agent-reports/<piece_slug>/cycle<N>-authorities-pack.md`, schema `templates.md` §3.4. Every entry is **keyed to its subgoal ID** and carries: the proposition (as it may be asserted in prose); the authority; a live AustLII / CaseLaw NSW URL; treatment status (**good law / doubted / distinguished / overruled**); and strength (supports as put / supports weaker form / clean negative).

**The pack is a summary keyed to URLs — never pasted judgments.** The orchestrator converges two rosters in one context; the pack must stay small.

**Clean negatives are complete answers and strategy signals.** `F3 → not supported at this strength; supportable as <weaker proposition>` flows straight back into Step 1: the orchestrator softens the desired conclusion **before any prose exists** and reports the softening to the user. An adversely treated authority is treated as a negative for the proposition it was to support.

## Consumption rules (enforced downstream)

- **Fact Finder:** legal claims are verified **only against the pack**, citing the subgoal ID. Any legal claim without a pack entry is tagged `UNSOURCED-LEGAL — may not be asserted`; its *Note for orchestrator* routes a targeted top-up. The Fact Finder never does primary legal research.
- **Devil's Advocate:** a `needs a fact` finding that is legal in kind (e.g. "the reader will say your costs authority doesn't survive X") routes to a Stage-0 top-up, not to the Fact Finder.
- **Funnel map:** each beat carrying a legal proposition names its subgoal ID, so every legal sentence traces beat → ID → pack entry → URL.
- **Gate check 7 (release-blocking; `porter-gate.md`):** every citation in the release candidate must resolve to a pack entry that is verbatim-correct and not adversely treated. A FAIL routes to Stage 0, **never to a prose fix**, and is never waived into a released-with-named-weakness.

## Top-ups — targeted, not re-runs

A mid-run legal question (an `UNSOURCED-LEGAL` tag, a `needs a fact → legal` routing, a check-7 FAIL) opens a new cycle carrying a **new `F# [legal]` subgoal** and a **single-question Stage-0 dispatch** — usually one agent plus the red-team where the answer is load-bearing. The pack is appended, never rewritten; superseded entries are marked, not deleted (the audit trail must show what changed and why).

## Failure and fallback

- If the `australian-legal-research` skill is not installed, Stage 0 **cannot run**: the orchestrator says so at checkpoint 1, and every `legal` subgoal is treated as `UNSOURCED-LEGAL` end-to-end — the piece may not assert law as fact, and the audit names this plainly. It does not quietly substitute training-knowledge research.
- If Stage 0 cannot resolve a load-bearing `legal` subgoal within the cycle cap, the conclusion softens to what the pack supports; releasing prose that asserts the unresolved proposition is a check-7 FAIL by definition.

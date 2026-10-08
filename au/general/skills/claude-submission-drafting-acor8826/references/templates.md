# Templates & Schemas

The contracts that bind the orchestrator and its subagents. The orchestrator owns the **persuasion ledger**; each subagent owns a **report file** written to its schema. Subagents share no memory, so the prompt template is the *only* context an agent gets — fill every slot.

**Contents:** 1 Persuasion ledger · 2 Subagent prompt template · 3 Output schemas (3.1 fact base, 3.2 objection map, 3.3 gate-check report, 3.4 authorities pack) · 4 Funnel map + concession register · 5 Per-cycle release + gate result · 6 Per-cycle deliverable (persuasion audit).

---

## 1. Persuasion ledger schema

`<piece_slug>_persuasion_ledger.md`. Rewritten/updated at the end of every cycle. The orchestrator's single source of truth.

```markdown
# Persuasion Ledger — <piece_slug>
_Updated: <ISO> · Cycle: <N> · Status: IN PROGRESS | COMPLETE_

## Goal (framed — Step 1) — frame v<K>, confirmed at checkpoint 1 <ISO>
- Reader: <role, priors, fears, what moves them, relationship>
- Desired conclusion (one sentence): <…>
- Controlling proposition: <the one load-bearing claim>
- Reader's resistances: <where they stand; known objections>
- Register & constraints: <channel; length ceiling; must/can't concede; house rules>
- Assumptions made: <gaps filled, flagged — each with consequence-if-wrong>
- Frame version log: <v1 confirmed <ISO>; v2: <what changed, why, which subgoal chains re-triggered>>
- FRAME-MISS log: <what — surfaced by <agent/check> at cycle <N>>

## Task register (per cycle) — subgoal IDs are durable and propagate end-to-end
| ID | Cycle | Agent | Task | Weight (LB/Sup/Col) | legal? | Status (resolved/unresolved/neg) | Report |
|----|-------|-------|------|---------------------|--------|----------------------------------|--------|
| F1 | 1 | Fact Finder | <fact to verify> | LB | — | resolved | agent-reports/<piece_slug>/cycle1-fact-base.md |
| F3 | 1 | Stage 0 | <legal proposition to verify> | LB | legal | resolved | agent-reports/<piece_slug>/cycle1-authorities-pack.md |
| O1 | 1 | Devil's Advocate | <objection to map> | LB | — | resolved | agent-reports/<piece_slug>/cycle1-objection-map.md |

## Stage 0 record (where run)
- Roster engaged: <…> · Research-skill gate result: <…> · Clean negatives: <ID → softening applied> · Top-ups: <cycle → single-question dispatch>

## Re-prioritisation log
- <task> promoted Col→LB (cycle <N>) — load-bearing because <…>

## Verified fact base (keyed to source)
- <one line per sourced fact> → <source>

## Concession register → §4
## Follow-up / spawned-task register
- Cycle <N> → <N+1>: <new task> — triggered by <finding> (e.g. no-answer objection → soften conclusion; unsourced LB fact → targeted sourcing)

## Gate results → §5  ·  Cycle releases: cycle<N> → <piece_slug>_cycle<N>_release.md
```

---

## 2. Subagent prompt template (orchestrator → agent)

The orchestrator (on **Fable**) fills this and dispatches each engaged agent **on Opus (`claude-opus-4-8`)** — the model is set on the Task call, not in the prompt text. Step 3: dispatch the intelligence agents **in one turn**. Step 5: Diplomat then Plain Speaker **in series** (each gets the prior output's path). Step 6: the six gate checks **in one turn**. Never leave a `<slot>` empty.

```
You are the **<AGENT>** for a persuasive piece (cycle <N>).

FIRST: read `references/porter-method.md` in full before writing anything. It binds you.

## Goal (read-only context)
- Reader: <role, priors, relationship, expertise>
- Desired conclusion: <one sentence>   - Controlling proposition: <…>
- Reader's resistances: <…>   ← (Devil's Advocate especially)
- Register & constraints: <channel, length ceiling, must/can't concede>

## Inputs (paths — list every file this agent must read; never leave implied)
- `references/porter-method.md` (all agents, read first)
- <intelligence agent: any prior-cycle report it must build on>
- <synthesis pass: the draft to edit + the funnel map + the concession register (§4)>
- <Fact Finder / gate check: the authorities pack (§3.4) where Stage 0 ran>
- <gate check: the release candidate + the fact base (§3.1) + the objection map (§3.2)>

## Your task (this cycle)
<intelligence agent: the weighted task-list slice + the strategy axes from its references/agent-*.md>
<synthesis pass: "edit the draft at <path> for {register | wording} only — structure and
{facts | facts and register} are FIXED">
<gate check: "audit the release candidate at <path> for <check>; return PASS/FAIL + offending lines">

## Rules
- <Fact Finder> Verify load-bearing facts; tag sourced/unsourced; never assert from memory. Clean negative = complete.
- <Devil's Advocate> Every concession genuine; flag no-answer objections.
- <synthesis pass> Stay in lane; preserve every placed concession and adverse fact.

## Output
Write to <path> using <schema> in `references/templates.md`. Then stop.
```

---

## 3. Output schemas

Each agent writes ONE markdown file to its schema. **Required fields are mandatory — an item missing a required field is treated as unresolved by the orchestrator's convergence (Step 4).**

### 3.1 Fact base — `agent-reports/<piece_slug>/cycle<N>-fact-base.md`
```markdown
# Fact base — cycle <N>
## Fact / opinion split
| Claim (as put) | FACT / OPINION | Underlying fact (if opinion) | Kept / cut |
## Verified facts (chronological)
| # | Date | Fact (de-hyperbolised) | Sourced? | Source |
| 1 | <date> | <plain fact> | sourced | <source> |
| 2 | <date> | <…> | UNSOURCED — may not be asserted | — |
## De-hyperbole notes · Negative findings
- <intensifier → plain form> · <claim that could not be verified — flagged, not invented>
## Note for orchestrator (drives the next cycle — Step 7)
- <e.g. "fact #2 is load-bearing but UNSOURCED → spawn a targeted sourcing task, or the conclusion must be recast">
```

**Worked example (grounds the schema):**
```markdown
## Verified facts (chronological)
| # | Date | Fact (de-hyperbolised) | Sourced? | Source |
| 1 | 12 Mar | The invoice was issued for $4,200. | sourced | invoice #1183 (attached) |
| 2 | 2 Apr | A reminder was sent; no reply was received in 21 days. | sourced | sent-mail log 2 Apr |
| 3 | — | The delay was "deliberate and contemptuous". | OPINION → cut; no verifiable fact supports intent | — |
## Note for orchestrator
- All load-bearing facts sourced; intent claim (#3) cut — conclusion must rest on the timeline, not on asserted motive.
```

### 3.2 Objection map — `agent-reports/<piece_slug>/cycle<N>-objection-map.md`
```markdown
# Objection map — cycle <N>
## Objections (ranked)
| # | Objection (as the reader would put it) | Bite (LB/Sup/Col) | Disarming move | Type | Honest? |
| 1 | "<objection>" | LB | <frank concession: give point, conclusion survives> | concede-early | yes |
| 2 | "<…>" | Sup | <build adverse fact in early> | pre-empt | yes |
## Note for orchestrator (drives the next cycle — Step 7)
- **No honest answer:** "<objection>" — no genuine concession available → the conclusion may over-reach; recommend softening <X>→<Y> (a Step-7 re-frame).
- **Needs a fact:** "<objection>" turns on a contested fact → hand to the Fact Finder next cycle.
```

**Worked example (grounds the schema):**
```markdown
## Objections (ranked)
| # | Objection (as the reader would put it) | Bite | Disarming move | Type | Honest? |
| 1 | "You left it 21 days before chasing — you weren't serious about payment." | LB | concede the 21 days openly, then show the term was net-14 and the reminder still preceded any dispute | concede-early | yes |
| 2 | "The amount is disputed." | Sup | build the signed quote in early, before the figure is mentioned | pre-empt | yes |
## Note for orchestrator
- No no-answer objections this cycle; both load-bearing objections have genuine concessions placed before first mention.
```

### 3.3 Gate-check report — `agent-reports/<piece_slug>/cycle<N>-gate-<check>.md`
```markdown
# Gate check: <check name> — cycle <N> — PASS | FAIL
- Offending lines (if FAIL): <quote + location>
- Routed to: <owner>   - Note: <one line>
```

### 3.4 Authorities pack — `agent-reports/<piece_slug>/cycle<N>-authorities-pack.md`
Written by the orchestrator converging the Stage-0 roster. **The only permissible source of legal fact.** Appended per cycle; superseded entries marked, never deleted.
```markdown
# Authorities pack — <piece_slug> — cycle <N>
_Stage-0 roster: <agents engaged> · research-skill gate: PASS/…_
## Entries (keyed to subgoal ID)
| ID | Proposition (as it may be asserted) | Authority | URL (AustLII/CaseLaw NSW) | Treatment | Strength |
| F3 | <proposition> | <case/provision> | <live URL> | good law | supports as put |
| F4 | <…> | <…> | <…> | good law | supports weaker form: <the weaker proposition> |
## Clean negatives (complete answers — trigger pre-draft softening)
- <ID> → not supported at this strength; supportable as <weaker proposition> — conclusion softened <X>→<Y> (frame v<K+1>)
## Superseded (audit trail)
- <ID> entry replaced cycle <N>: <why>
```

---

## 4. Funnel map + concession register
Written by the orchestrator alongside the funnel draft; surfaced in the audit.
```markdown
# Funnel map — <piece_slug>
_Desired conclusion: <one sentence> · Reader: <short>_
| Beat | Content (one line) | Serves (subgoal IDs) | Job in the funnel |
| 1 (mouth — wide/agreed) | <opens on agreed ground> | — | wins cheap early agreement |
| 2 | <first undisputed fact> | F1 | small unarguable step |
| 3 (early concession) | <concedes objection O1 frankly> | O1 | defuses + buys credibility |
| 4 | <legal proposition, quietly> | F3 → pack entry → URL | the mechanism laid as fact |
| … | <facts narrowing> | <IDs> | closes off alternatives |
| n (exit — narrow) | <quiet statement of conclusion> | all LB | only reasonable landing |
| — (ends) | no re-argument | — | Rule 9 |

# Concession register
| Objection (from map) | Concession / pre-emption made | Placed at beat |
```

---

## 5. Per-cycle release + gate result
Release: `<piece_slug>_cycle<N>_release.md` (the gate-passed prose). Gate result, recorded in the ledger:
```markdown
# Gate — <piece_slug> · cycle <N> · Decision: CLEAN | RELEASED-WITH-NAMED-WEAKNESS
| # | Check | Owner | Result | Offending lines | Routed to / fix |
| 1 | No aggression | Diplomat | PASS/FAIL | | |
| 2 | Fact over opinion | Fact Finder | PASS/FAIL | | |
| 3 | Self-reached conclusion | Lead Strategist | PASS/FAIL | | |
| 4 | Honest pre-emptive concession | Devil's Advocate | PASS/FAIL | | |
| 5 | Plain language | Plain Speaker | PASS/FAIL | | |
| 6 | Brevity | LS / Plain Speaker | PASS/FAIL | | |
| 7 | Citation integrity (if law cited) | Stage 0 via LS | PASS/FAIL — release-blocking, never a named weakness | | Stage-0 top-up only |
## Honesty guard
- Concessions genuine? · All load-bearing facts sourced? · Conclusion supported by verified facts? · Softening applied?
## Residual weakness (if released-with-named-weakness)
- <the load-bearing check that did not clear in 3 cycles, stated plainly>
```

---

## 6. Per-cycle deliverable (persuasion audit)

`<piece_slug>_cycle<N>_audit.md`, emitted **every cycle** alongside the release candidate; the final cycle's is the consolidated record. The release candidate (`<piece_slug>_cycle<N>_release.md`) is the product the user sends; this audit is the accompaniment that shows *why* it persuades and lets the user confirm the task was understood before relying on it. **The audit is internal only — it names every weakness and softening; it is never sent to the reader** (see CONFIDENTIALITY in SKILL.md). (For a sendable piece, offer a `.docx` of the release candidate via the docx skill; for a court filing, hand the release candidate to `written-submissions` for filing format.)

```markdown
# Persuasion Audit — <piece_slug> — Cycle <N> of <planned>
_<ISO date> · Status: IN PROGRESS | COMPLETE · Prepared via submission-drafting_

## 1. Brief (verbatim)
> <Paste the user's request EXACTLY as received — unedited, including the reader, the ask, and any constraint. For a long brief (attached documents, multi-page instructions), paste the operative ask verbatim and cite the source file(s) by path — never paraphrase the ask itself.>

## 2. Goal & subgoals — the chain table (MANDATORY — the user's 30-second pre-send check)
State what the orchestrator understood the task to be, how it decomposed it, and where each subgoal landed — so the reader can confirm the task was understood, researched, and carried into the prose *before* relying on the piece.
- **Persuasion goal:** <reader · desired conclusion (one sentence) · controlling proposition · register/constraints · frame v<K>>
- **Chain table (goal → subgoal → verification → prose):**

| ID | Subgoal | Weight | Verified by | Finding | Lands at beat |
|----|---------|--------|-------------|---------|---------------|
| F1 | <…> | LB | Fact Finder (source) | sourced | 2 |
| F3 | <…> | LB, legal | Stage 0 (pack → URL) | good law / softened to <…> | 4 |
| O1 | <…> | LB | Devil's Advocate | genuine concession | 3 |

- **FRAME-MISS log:** <anything the confirmed frame missed, surfaced by whom, at which cycle — or "none">

## 3. The piece
- Release candidate: `<piece_slug>_cycle<N>_release.md` (gate outcome: CLEAN | RELEASED WITH NAMED WEAKNESS)

## 4. This cycle
- Agents run (individually inspectable): <list of agent-reports/<piece_slug>/cycle<N>-*.md, incl. the six gate checks>

## 5. How it persuades
- **Funnel map** (§4): the ordered beats and what each does.
- **Concession register** (§4): each load-bearing objection → the concession made → where placed.

## 6. Gate result (§5) + reconciliation
- The engaged checks (six, or seven where law is cited) (PASS/FAIL), the reconciliation log (where checks diverged and how it was settled), and the honesty-guard result.

## 7. Orchestrator evaluation & next step
- What is now resolved: <…>
- Gaps remaining: <…>
- Decision: GOAL MET (stop) | SPAWN CYCLE <N+1> with tasks: <…> | RELEASED WITH NAMED WEAKNESS

## 8. Limitations / residual weakness
- <any load-bearing check not cleared, stated plainly; any fact confirmed only weakly; any concession the user should pressure-test before sending>
```

# The Porter Gate — Seven Checks, Dispatch, Reconciliation

The compliance gate runs **every cycle**, over the release candidate that cycle produced, before it reaches the user. Six standing Porter checks always apply; a **seventh, release-blocking citation-integrity check** is engaged whenever the piece cites any authority (i.e. whenever Stage 0 ran or any legal proposition appears in the prose).

**Dispatch rule (same as Step 3).** The engaged checks (six, or seven where law is cited) are dispatched as **named Claude Code Task subagents in a single turn, each on Opus (`claude-opus-4-8`)** — so they run in genuinely parallel, isolated contexts and each is separately visible. Name them explicitly; do not collapse two checks into one dispatch; if a check fails or returns malformed output, re-dispatch only that check. The orchestrator then runs a seventh **reconciliation** pass itself **on Fable**. Two exceptions: (a) single-threaded fallback where the Task tool is absent (e.g. claude.ai chat) — run the checks sequentially; (b) a **trivial decomposition** under the proportionality rule (SKILL.md, Architecture) — the orchestrator may judge all six checks inline in one audit sweep, recording `gate: inline (trivial)` in the ledger.

**Two caps, kept distinct.** Within a single cycle, the gate runs at most **three times** (initial run + two re-runs after in-place fixes); a check still failing after that needs new intelligence or a re-frame → hand up to Step 7 as a new cycle, don't keep polishing. Across the whole task, Step 7's **cycle cap of 3** governs. A load-bearing check that has not cleared when the Step-7 cap is reached → **RELEASED WITH NAMED WEAKNESS**.

Result states: **PASS / FAIL / DISPUTED** — never "probably fine". A check that cannot judge a passage (e.g. a claim it cannot find in the fact base) returns DISPUTED with what it looked for, not a guess.

## Common dispatch contract

Every check subagent receives: the **release candidate** for this cycle (the Plain Speaker's output, by path); the **framed-goal slice** (reader, desired conclusion, controlling proposition — read-only); the **fact base** and the **objection map** for the cycle (so checks 2 and 4 can test the prose against what was actually verified and what objections actually existed); the **authorities pack** where one exists (so checks 2 and 7 can test legal assertions against what Stage 0 verified); a pointer to read `references/porter-method.md` before judging; its role prompt (below); and its output path `agent-reports/<piece_slug>/cycle<N>-gate-<check>.md`.

Hard constraints in every check's prompt: **work only your own check**; judge the text **as written**, grounding every finding in the actual words of the release candidate (and, for checks 2 and 4, in the fact base / objection map) — never in what you assume it says or think it should say; a FAIL must **quote the offending line(s) and their location**; **you audit, you do not rewrite** — routing the fix is the orchestrator's job; write strictly to the §3.3 schema.

## The role prompts (six standing + conditional seventh)

**Check 1 — No aggression** *(owner: Diplomat; paste verbatim):*
> You are the **No-aggression check** (Rule 7). Scan every line of the release candidate for anything combative, sarcastic, accusatory, contemptuous, triumphant, or point-scoring, and for anything that would raise the reader's defences (demands, "as you should know", implied insult). Record `PASS` (the genial, courteous surface holds end to end), `FAIL` (quote each offending line and its location), or `DISPUTED`. Do not judge fact, concession, clarity, or length. Write to `references/templates.md` §3.3.

**Check 2 — Fact over opinion** *(owner: Fact Finder; paste verbatim):*
> You are the **Fact-over-opinion check** (Rules 3, 4). For every load-bearing point in the release candidate, confirm it rests on a fact tagged **sourced** in the fact base — not on an adjective, an intensifier, or a loud claim. Flag: (a) any load-bearing point asserting as fact something the fact base tagged **unsourced** or absent; (b) any surviving hyperbole/intensifier ("clearly", "egregious", superlatives). Record `PASS`, `FAIL` (quote the line + name the missing/unsourced fact), or `DISPUTED` (cannot find the claim in the fact base — say what you searched). Do not judge tone or length. Write to §3.3.

**Check 3 — Self-reached conclusion** *(owner: Lead Strategist; paste verbatim):*
> You are the **Self-reached-conclusion check** (Rule 5 — the funnel). Read the release candidate as a sceptical reader. Decide whether the conclusion is *arrived at* through the laid facts or *announced at* the reader. Record `PASS` only if the funnel is invisible and a sceptical reader could finish feeling they reached the conclusion themselves; `FAIL` if the piece bludgeons, repeats the conclusion at the reader, or shows its engineering (quote where); or `DISPUTED`. Do not judge tone, fact, or wording. Write to §3.3.

**Check 4 — Honest, pre-emptive concession** *(owner: Devil's Advocate; paste verbatim):*
> You are the **Concession check** (Rule 6). Cross the objection map against the release candidate. For every **load-bearing** objection, confirm it is met *before* the reader would reach it, and that the concession made is **genuine** (gives the point honestly, then shows the conclusion survives). Record `PASS`, `FAIL` (a load-bearing objection unaddressed, met too late, or "met" with a hollow/ornamental concession — quote it), or `DISPUTED`. Flag any objection the map marked **no-honest-answer** that the prose nonetheless papers over — that is a FAIL, and a signal the conclusion over-reaches. Do not judge tone, clarity, or length. Write to §3.3.

**Check 5 — Plain language** *(owner: Plain Speaker; paste verbatim):*
> You are the **Plain-language check** (Rule 8). Scan for surviving jargon/legalese undefined for this reader, tangled multi-clause sentences, abstraction where a concrete word would serve, and any line a reader would have to re-read. Calibrate to the reader's expertise from the goal — flag what this reader would stumble on, not what a layperson might. Record `PASS` (every step lands on first read), `FAIL` (quote each offending line), or `DISPUTED`. Do not judge tone, fact, or concession. Write to §3.3.

**Check 6 — Brevity** *(owner: Lead Strategist / Plain Speaker; paste verbatim):*
> You are the **Brevity check** (Rule 9). Confirm nothing overstays: no re-argued conclusion, no flourish after the end, no line that does not earn its place, and the piece is within any length ceiling in the goal. Record `PASS`, `FAIL` (quote the padding/over-run, or the line that should be cut), or `DISPUTED`. The piece must end at the conclusion. Do not judge tone, fact, or clarity. Write to §3.3.

**Check 7 — Citation integrity** *(owner: Stage 0 via the Lead Strategist; engaged whenever the piece cites any authority; paste verbatim):*
> You are the **Citation-integrity check** (release-blocking). Cross every citation, authority, statutory reference, and legal proposition in the release candidate against the authorities pack. For each, confirm: (a) a pack entry exists for it, keyed to a subgoal ID; (b) the citation as written is **verbatim-correct** against the pack entry (name, citation, pinpoint if given); (c) the entry's treatment status is not **doubted / distinguished-on-point / overruled**; (d) the proposition asserted in the prose does not exceed the **strength** the pack records (a "supports weaker form" entry cannot carry the stronger assertion). Also flag any legal proposition asserted with NO pack entry — that is a FAIL even if you believe it correct; belief is not verification. Record `PASS`, `FAIL` (quote the line; name the pack entry or its absence; state which of (a)–(d) failed), or `DISPUTED` (cannot match a citation to the pack — say what you searched). Do not judge tone, structure, clarity, or length. A FAIL on this check routes to a **Stage-0 top-up, never a prose fix**, and is never released as a named weakness. Write to §3.3.

## Honesty guard (orchestrator-enforced; overrides all checks)

A check may **never** be passed by weakening the truth — the guard is the gate's reason for existing (Rule 2):

- A concession (check 4) must be one the team can stand behind. If making it honest damages the conclusion, the conclusion over-reaches.
- A fact (check 2) must actually be **sourced** in the fact base. If a load-bearing point needs an unsourced fact, hand it back to the Fact Finder (a Step-7 cycle) or recast it — never let it through as fact.
- The conclusion (check 3) must be one the **verified facts** support. Persistent check-3/4 failure → **soften the conclusion, don't force the gate.**

## Reconciliation (orchestrator's seventh pass)

A **dispute** is any `FAIL` on a load-bearing element, **or** any disagreement between checks (e.g. check 2 flags a claim as unsourced opinion that the fact base in fact tags sourced), **or** any honesty-guard breach, **or** any `DISPUTED` return. For each, the orchestrator **re-reads the passage itself** against the fact base / objection map (it does not tally votes — the checks are input, not ballots), decides, and records the resolution in the gate result: what each check found, where they diverged, and how it was settled. Then it routes the fix.

## Outcome states feeding the release

- **CLEAN** — all engaged checks PASS and the honesty guard is satisfied → release.
- **REQUIRES REVISION** — a check FAILs and is fixable in place this cycle → route to its owner (tone → Diplomat; fact/sourcing → Fact Finder; concession placement → Devil's Advocate via the Lead Strategist; structure/conclusion → Lead Strategist; wording/length → Plain Speaker), then **re-run the gate on the changed sections** (a tone fix can reintroduce friction → re-run check 5; a structural fix can disturb concessions → re-run check 4).
- **SPAWN CYCLE** — a FAIL needs new intelligence (a missing source, a no-honest-answer objection, **any check-7 FAIL** → a targeted Stage-0 top-up) → hand **up to Step 7** as a new cycle with a targeted subgoal; do not patch in place.
- **RELEASED WITH NAMED WEAKNESS** — a load-bearing check **among checks 1–6** still fails when the per-cycle gate limit (three runs) and the Step-7 cycle cap are both exhausted → release with the residual weakness named plainly in the audit; naming it is itself Porter-compliant, hiding it breaks Rule 2. **Check 7 is never released as a named weakness**: if a citation cannot be verified within the caps, the assertion it carries is cut or recast to what the pack supports — an unverified citation does not ship.

## Output

Each check writes `agent-reports/<piece_slug>/cycle<N>-gate-<check>.md` to the §3.3 schema. The orchestrator writes the consolidated gate result (the engaged checks, reconciliation log, and outcome state) into the per-cycle audit (`templates.md` §6) and the ledger.

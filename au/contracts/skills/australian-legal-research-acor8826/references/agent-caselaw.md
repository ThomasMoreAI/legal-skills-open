# Case-law Agent — Brief, Strategies, Ranking, Output

The case-law agent is one of the fixed roster the orchestrator dispatches in **Step 3** of the
orchestration loop. It is **one Claude Code Task subagent per cycle** (not one per strategy): it
runs all four search strategies *internally*, converges them, and writes one ranked case table to
`agent-reports/cycle<N>-caselaw.md`. It is dispatched in the same turn as the other engaged
area-agents and runs in an isolated context — everything it needs is in its prompt.

## What this agent owns

Build the case-law that answers the framed question: the **leading/binding authority**, the
authorities **applying** it, the closest **factual analogues**, and the **citator trail** around the
key cases — every one verified on a primary source, pinpointed, and ranked. It assigns each case a
**how-cited** classification so the orchestrator can tell an application of the ratio from a passing
history mention.

It does **not** own: statutory currency / amendment history (legislation agent), secondary framing
(secondary agent), or the systematic contrary-case sweep (red-team). If it trips over a strongly
contrary case while searching, it records it as a flag for the red-team — but it does not build the
adversary brief itself. Stay in lane.

## Dispatch envelope

The orchestrator builds this agent's Task prompt from the **subagent prompt template in
`references/templates.md` §2** plus the role prompt below, and injects: the framed goal (read-only —
question(s), jurisdiction/hierarchy, temporal anchor(s), factual matrix, propositions); this agent's
**case-law task-list slice** (each task tagged major/moderate/minor); the four strategy axes; a
pointer to read `references/retrieval-mechanics.md` before any fetch; and the output path + schema.
Never leave a slot empty — the agent sees nothing else.

## Role prompt (paste verbatim into the Task dispatch)

> You are the **Case-law agent** for a legal-research cycle. Your job is to build the case-law that
> answers the framed question: the leading/binding authority, the authorities applying it, the
> closest factual analogues, and the citator trail around the key cases — every one verified on a
> primary source.
>
> **FIRST:** read `references/retrieval-mechanics.md` in full before any fetch, and
> `references/aglc4-citation.md` for citation formatting. Prefer jurisd
> Layer 0 if it is registered (`search_cases` for topic/authority search, `fetch_document_text`
> for full text); for **who-cites-this-case**, jurisd v0.5.0 has **no live citator** — use the
> citator recipe in `references/retrieval-mechanics.md` (Jade's free-tier citation panel is the
> best seed; harvest it via `site:jade.io` search + Chrome, then confirm each candidate on tier 1),
> seeded by `search_cases` on the case name.
> Otherwise use the fallback stack. **Never**
> use AustLII SINO/LawCite (Cloudflare-walled) or bare `site:austlii` index pages.
>
> Run **ALL FOUR** strategies below internally and diverge across them — do not pick one:
> 1. **By-statute** — find decisions on the controlling provision(s) named in the goal/ledger.
>    Search the provision as a phrase and noteup the leading case under it. Catches the line of
>    authority a doctrinal search alone misses.
> 2. **By-doctrine** — find the leading authority on the doctrinal proposition, then its
>    applications. Identify the case everyone cites for the proposition before its downstream uses.
> 3. **By-analogy / factual-matrix** (**highest value**) — distil the factual matrix into 3–6 fact
>    predicates and search for decisions whose *facts* resemble them; rank by factual + doctrinal
>    proximity. This is where the most useful precedent for a self-represented litigant comes from.
> 4. **By-citator-trail** — from each leading case, walk **forward** (who has cited it — use the
>    citator recipe in retrieval-mechanics.md, seeded by `search_cases` on the case name; jurisd's
>    offline `find_citing` is legislation-only today, so it will not list citing cases yet) and
>    **backward** (what it cites — from the judgment's own text). Catches both the line that built on
>    it and the authority it rests on.
>
> For **every** case you rely on:
> - **Fetch the judgment from a primary source and VERIFY it** — parties (correct order), court,
>   year, medium-neutral citation number, authorised report volume/page, bench, and date. Never
>   assert any of these from memory. If you cannot fetch it, mark it `unverified` and say so.
> - Extract the **relevant paragraph numbers** and the **minimum verbatim quote(s)** needed (in
>   quotation marks, each tagged with its `[N]`; keep each quote short).
> - Write a **2–5 sentence factual summary** — the facts that matter for *this* question, not a
>   headnote.
> - Paraphrase the **holding / proposition** in your own words.
> - Classify **how-cited** relative to the target/leading case (for any citator-trail or
>   "who-cites-X" task): `followed | applied | cited-in-argument | mentioned-as-history |
>   distinguished` — at `[N]`. A history-only mention carries very different weight from an
>   application of the ratio; say which, and never present a history mention as endorsement.
> - For the **analogical** strategy, record **proximity**: factual high/med/low · doctrinal
>   high/med/low.
> - Record the **AGLC4 citation** (combined medium-neutral + authorised-report form, per
>   `references/aglc4-citation.md`), built only from the verified header metadata you fetched.
> - Set a **verification flag**: `verified | unverified (could not fetch) | suspect (mismatch)`.
>
> Then **CONVERGE**: dedupe the same case found by multiple strategies into one block, and produce
> **one ranked table** ordered by **authority × proximity × recency** (see Ranking, below).
>
> A clean negative is a complete answer: "no on-point authority after running these paths: <list>."
> Report it; do not invent authority or pad. Do **not** assess statutory currency or build the
> contrary-case brief — other agents own those (but record any strongly contrary case you trip over
> as a one-line flag for the red-team).
>
> Write your report to `agent-reports/cycle<N>-caselaw.md` using the **Case-law agent report
> schema** in `references/templates.md` §3.1. Populate every required field for every case. Then
> stop.

## The four strategies in detail

- **By-statute.** When the legislation agent (or the ledger) has named a controlling provision,
  search for decisions *on that provision*. With jurisd: `search_cases` with the provision and Act
  as a phrase, scoped to the relevant jurisdiction. Fallback: `web_search` for the provision plus
  "considered"/"applied" across the court hierarchy. Pull the leading case under the provision, then
  its applications. Common trap: returning cases that merely *mention* the Act rather than construe
  the provision — read enough to confirm the provision is actually in issue.
- **By-doctrine.** Search the doctrinal phrase (e.g. "procedural fairness" + "new trial"; "Anshun
  estoppel"). Find the **leading** statement first (usually the highest court), then work down to
  applications. Trap: stopping at a recent first-instance application and missing the appellate
  authority it depends on.
- **By-analogy / factual-matrix.** The highest-value strategy and the one a keyword search skips.
  Reduce the matrix to fact predicates (party type, transaction, procedural posture, the operative
  event), then search those. Rank hits by how closely the facts *and* the legal question line up.
  This is where the precedent most useful to the user's own facts is found.
- **By-citator-trail.** Forward: who has cited the leading case, and *how* (this is the how-cited
  classification). Backward: what the leading case itself relies on. The **citator recipe** in
  retrieval-mechanics.md is the forward tool — jurisd v0.5.0 has no live citator, and its offline
  `find_citing` is legislation-only, so it returns nothing for case citators; seed the recipe with
  `search_cases` on the case name and with **Jade's free-tier citation panel** (resolve the case
  via `site:jade.io "<citation>"`, open the article in Chrome, harvest the cases-citing panel —
  tier-2 leads, each confirmed on tier 1). Trap: treating every forward citation as support — most
  are history or argument mentions; classify each.

## Ranking method — authority × proximity × recency

Produce a **defensible ordering, not a numeric score**, combining three factors:

- **Authority** — position in the court hierarchy (see the hierarchy table in
  `references/retrieval-mechanics.md`): HCA > intermediate appellate (NSWCA/CCA, FCAFC, State CAs) >
  single-judge (NSWSC, FCA) > inferior courts/tribunals. Binding beats persuasive for the forum in
  the goal.
- **Proximity** — factual + doctrinal closeness to the framed question. A case directly on the
  provision and on facts like the matrix outranks a general statement of principle.
- **Recency** — later decisions are preferred *where they restate or refine* the principle; but a
  recent first-instance case does **not** outrank the leading appellate authority on point. Recency
  breaks ties and flags whether the law has moved, not the other way round.

Rule of thumb: **the leading binding authority on point ranks first even if it is older**; analogical
and applying cases follow, ordered by proximity then recency; downstream first-instance applications
and history-only mentions rank last.

## How-cited classification (why it is a required field)

A later judgment can mention an earlier case in very different ways, and the weight differs sharply:

- **followed** — the later court adopts the earlier ratio as governing and applies it.
- **applied** — the earlier case supplies the test the later court uses to decide.
- **cited-in-argument** — referred to by counsel or in the court's survey without being decisive.
- **mentioned-as-history** — a procedural/background reference only (e.g. a Full Court reciting the
  history of the same litigation), with no adoption of any proposition.
- **distinguished** — the later court confines the earlier case to its facts and declines to apply
  it.

The classification stops the orchestrator (and the user) from citing a case as *support* when the
later authority merely recited it as history or distinguished it. Tag the paragraph `[N]` where the
treatment occurs.

## Output

One markdown file, `agent-reports/cycle<N>-caselaw.md`, populated to the **Case-law agent report
schema** in `references/templates.md` §3.1 — one block per case (citation; court/date/bench; verified
source URL; factual summary; relevant paragraphs; minimum verbatim quote(s); paraphrased holding;
how-cited; proximity for analogical hits; AGLC4 citation; verification flag), plus a **Negative findings** section
listing the paths that returned nothing on point. Required fields are mandatory; a case missing one
is treated as unresolved by the orchestrator's convergence.

## Lane boundaries (do not cross)

- No statutory currency, amendment history, or subsection extraction — that is the legislation agent.
- No secondary-source framing — that is the secondary agent.
- No systematic contrary-authority sweep or distinguishing-argument brief — that is the red-team;
  only flag contrary cases you happen to find.
- No assertion of any citation, quote, holding, judge, or date from memory — fetch and verify, or
  mark it unverified.

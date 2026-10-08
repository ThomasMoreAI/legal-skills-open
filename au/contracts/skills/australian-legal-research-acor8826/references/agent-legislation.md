# Legislation Agent — Brief, Strategies, Output

One of the fixed roster the orchestrator dispatches in **Step 3**. It is **one Claude Code Task
subagent per cycle** (not one per strategy): it runs all three strategies *internally*, converges
them, and writes one statutory map to `agent-reports/cycle<N>-legislation.md`. Dispatched in the same
turn as the other engaged area-agents; isolated context — everything it needs is in its prompt.

## What this agent owns

The **statutory map**: the controlling provision(s), the **verbatim text of the operative
subsection(s)**, and their **currency as at the temporal anchor**. A provision identified but not
extracted is unresolved. It does **not** build the case-law under the provision (that is the case-law
agent — but it flags when such work is needed), nor secondary framing, nor the contrary brief.

## Dispatch envelope

Built from the **subagent prompt template in `references/templates.md` §2** plus the role prompt
below. The orchestrator injects: the framed goal (read-only); this agent's legislation task-list
slice (major/moderate/minor); the three strategy axes; the `retrieval-mechanics.md` pointer; output
path + schema. Never leave a slot empty.

## Role prompt (paste verbatim into the Task dispatch)

> You are the **Legislation agent** for a legal-research cycle. Your job is to build the statutory
> map: the controlling provision(s), the verbatim text of the operative subsection(s), and their
> currency as at the temporal anchor.
>
> **FIRST:** read `references/retrieval-mechanics.md` in full before any fetch. Prefer jurisd
> Layer 0 if registered (`get_provision` and `get_act_structure` — offline for Commonwealth law if
> the `legislation-cth` module is installed; else `search_legislation` + `fetch_document_text`);
> otherwise use the legislation registers in the fallback stack.
>
> Run **ALL THREE** strategies internally:
> 1. **Statute-first** — identify the Act(s) that govern the question and the section(s) that carry
>    it. Extract the operative subsection text **verbatim** (not just the heading). Record source URL
>    and currency. This is the spine of the map.
> 2. **Amendment-history** — determine the version in force **as at the temporal anchor**. The
>    cause-of-action date and the hearing/filing date may attract different versions. Use
>    point-in-time compilations (Cth Federal Register) / historical in-force views (NSW). If the
>    anchored version differs from current, extract **both**, flag the difference, and state which
>    applies and why.
> 3. **Definitional / interpretive** — pull the defined terms the provision turns on (interpretation
>    section / Dictionary), any interpretation or application provisions, and related subordinate
>    instruments — regulations and court rules (e.g. UCPR for a *Civil Procedure Act* question).
>    These often decide how the operative provision reads.
>
> For **every** provision: fetch and **VERIFY** on a primary source; extract the operative
> subsection text verbatim; fix currency as at the anchor (resolve point-in-time vs current); list
> the defined terms engaged and any cross-referenced instruments not yet retrieved; set a
> **verification flag** (`verified | unverified`).
>
> Where the statutory map implies case-law work — "the question turns on s N(2); cases applying it
> are needed" — say so in the **Note for orchestrator** field. That line is what triggers a case-law
> **by-statute** task next cycle.
>
> **CONVERGE** the three strands into one statutory map (provision → extracted subsection(s) →
> currency → defined terms → cross-refs → URL); resolve any currency/version conflict against a
> primary source before fixing the map. Write your report to `agent-reports/cycle<N>-legislation.md`
> using the **Legislation agent report schema** in `references/templates.md` §3.2. Then stop.

## Mechanics (detail in retrieval-mechanics.md)

- **NSW:** `legislation.nsw.gov.au` whole-Act or `#sec.XX` single-section view; point-in-time view
  for past currency.
- **Cth:** jurisd `get_provision` (offline, if `legislation-cth` installed) is fastest and
  deterministic; else Federal Register `…/latest/text` or a dated compilation; or AustLII
  `classic.austlii.edu.au/au/legis/cth/consol_act/<slug>/s<N>.html` via Chrome for section pinpoints.
- Always extract the **operative subsection text**, not just the section heading.

## Output

One file, `agent-reports/cycle<N>-legislation.md`, to **`templates.md` §3.2** — one block per
provision (Act + section; jurisdiction; source URL; currency with point-in-time flag; verbatim
extracted subsection text; defined terms; cross-references; note-for-orchestrator; verification
flag). Required fields mandatory.

## Lane boundaries (do not cross)

- No case-law building — only flag, in the note field, where case-law under the provision is needed.
- No secondary framing; no contrary-authority brief.
- No subsection text or currency asserted from memory — fetch and verify, or mark unverified.

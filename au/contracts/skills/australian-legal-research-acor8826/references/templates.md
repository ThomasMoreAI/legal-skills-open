# Templates & Schemas

The contracts that bind the orchestrator and its subagents. The orchestrator owns the **ledger** and the **cycle memo**; each subagent owns a **report file** written to its schema. Subagents share no memory, so the prompt template is the *only* context an agent gets — fill every slot.

**Contents**
1. Research ledger schema
2. Subagent prompt template (orchestrator → agent)
3. Per-agent output schemas
   - 3.1 Case-law agent report
   - 3.2 Legislation agent report
   - 3.3 Secondary-sources agent report
   - 3.4 Red-team agent report
   - 3.5 Evidence agent report
   - 3.6 Jurisdiction agent report
   - 3.7 Validation subagent reports
4. Per-cycle research-memo template

---

## 1. Research ledger schema

One file per matter: `<matter_slug>_research_ledger.md`. Rewritten/updated at the end of every cycle. This is the orchestrator's single source of truth.

```markdown
# Research Ledger — <matter_slug>
_Last updated: <ISO datetime> · Cycle: <N> · Status: IN PROGRESS | COMPLETE_

## Research goal (framed — Step 1)
- **Question(s):** <the precise legal questions>
- **Jurisdiction / hierarchy:** <courts that bind / persuade>
- **Temporal anchor(s):** <as-at date(s) and why>
- **Factual matrix:** <distilled salient facts for analogical search>
- **Propositions to support:** <…>
- **Propositions to contest (red-team):** <…>
- **Assumptions made:** <any gap filled by assumption, flagged>

## Task register (per area · per cycle)
| Cycle | Area | Task | Weight (M/Mod/Min) | Strategy | Status (resolved/unresolved/neg) | Agent report |
|-------|------|------|--------------------|----------|----------------------------------|--------------|
| 1 | case law | leading authority on <X> | Major | by-doctrine | resolved | agent-reports/cycle1-caselaw-by-doctrine.md |
| 1 | legislation | controlling provision + subss | Major | statute-first | resolved | agent-reports/cycle1-legislation-statute-first.md |

_Area ∈ {legislation, case law, evidence, jurisdiction, secondary, red-team} — only those the goal engages._

## Re-prioritisation log
- <task> promoted Minor→Major (cycle <N>) — reason: <load-bearing because…>

## Verified findings (keyed to source)
- <one line per verified authority/provision> → <URL>

## Authorities table (running)
| Authority (AGLC4) | Court/date | Treatment | How-cited | Validation | Source tier | URL |
|-------------------|-----------|-----------|-----------|------------|-------------|-----|

_AGLC4 form per `references/aglc4-citation.md`. Source tier per `references/retrieval-mechanics.md` —
a Jade URL (tier 2) may stand here, but tier 1 is required before anything is relied on in a filed
document._

## Follow-up / spawned-task register
- Cycle <N> → Cycle <N+1>: <new task> — triggered by <finding>

## Cycle memos
- Cycle 1 → `<matter_slug>_cycle1_memo.md`
```

---

## 2. Subagent prompt template (orchestrator → agent)

The orchestrator fills this and dispatches **one subagent per engaged area** (each area-agent runs that area's strategy axes internally and becomes a separately-visible agent). Never leave a `<slot>` empty — the agent sees nothing else.

```
You are the **<AREA> agent** for a legal-research cycle.

FIRST: read `references/retrieval-mechanics.md` in full before any fetch. Use only the
retrieval paths it specifies. Do NOT use AustLII SINO/LawCite (Cloudflare-walled) or bare
`site:austlii` index pages. Jade (jade.io) 403s bare fetches — resolve via `site:jade.io`
search and open in Chrome, per the Jade section of that file.
<if AREA is case-law, or this is a validation check: also read `references/aglc4-citation.md`
— every citation you output is AGLC4-formatted from verified metadata.>

## Research goal (read-only context)
- Question(s): <…>
- Jurisdiction / hierarchy: <…>
- Temporal anchor(s): <…>
- Factual matrix: <…>
- Propositions: support <…> / contest <…>

## Your delegated tasks (this cycle)
- [MAJOR] <task>           ← must resolve (verified positive OR exhaustive negative)
- [MODERATE] <task>
- [MINOR] <task>

## Your strategy axes (run ALL of them internally; diverge across them)
<the area's strategy axes, copied from the area's `references/agent-<area>.md` brief —
e.g. for case-law: by-statute; by-doctrine; by-analogy/factual-matrix; by-citator-trail>

## Rules
- VERIFY everything by fetching the source. Never assert a citation, quote, holding, judge,
  or date from memory. If you cannot fetch a source, mark the item UNVERIFIED and say so.
- Quote verbatim with paragraph pinpoints. Flag suspected OCR error.
- A clean negative ("no authority on point after running these paths: <list>") is a complete
  answer — report it, don't pad.

## Output
Write your report to `agent-reports/cycle<N>-<AREA>.md` using the
**<AREA> agent report schema** in `references/templates.md` §3. Populate every required field
for every item. Then stop.
```

---

## 3. Per-agent output schemas

Each agent writes ONE markdown file to its schema. Required fields are mandatory — an item missing a required field is treated as unresolved.

### 3.1 Case-law agent report

`agent-reports/cycle<N>-caselaw.md`. **One block per case.** Required: citation, factual summary, relevant paragraphs, relevant quotes, source URL.

```markdown
# Case-law agent — cycle <N>
_Tasks: <list> · Paths run: <search paths used>_

## <Case name> <medium-neutral citation>; <authorised report citation>
- **Resolves task:** <which delegated task>
- **Court / date / bench:** <e.g. FCAFC, 7 Jun 2021, Allsop CJ, Farrell, Derrington JJ>
- **Source URL:** <AustLII viewdoc URL, or CaseLaw NSW /decision/ URL> (verified: yes/no)
- **Factual summary:** <2–5 sentences — the facts that matter for this question>
- **Relevant paragraphs:** <[N], [N]–[M] — the pinpoints that carry the proposition>
- **Relevant quote(s):** <verbatim, in quotation marks, ≤ the minimum needed, each tagged with its [N]>
- **Holding / proposition (paraphrased):** <what it stands for, in the agent's words>
- **How-cited vs Nobarani/target (if a citator task):** followed | applied | cited-in-argument | mentioned-as-history | distinguished — at <[N]>
- **Proximity (analogical strategy only):** factual <high/med/low> · doctrinal <high/med/low>
- **AGLC4 citation:** <combined form per `references/aglc4-citation.md`, from verified metadata only>
- **Verification flag:** verified | unverified (could not fetch) | suspect (mismatch)

## Negative findings
- Path "<query>" → no on-point authority. Path "<query>" → only first-instance, noted.
```

**Worked example (grounds the schema):**

```markdown
## Nobarani v Mariconte [2018] HCA 36; (2018) 265 CLR 236
- **Resolves task:** [MAJOR] leading authority on procedural fairness → new trial
- **Court / date / bench:** HCA, 15 Aug 2018, Kiefel CJ, Gageler, Nettle, Gordon, Edelman JJ
- **Source URL:** https://www.austlii.edu.au/cgi-bin/viewdoc/au/cases/cth/HCA/2018/36.html (verified: yes)
- **Factual summary:** Self-represented appellant opposed a solemn-form probate grant; the nature
  of the hearing changed days before trial and adjournment was refused. He was denied a fair
  opportunity to present his case.
- **Relevant paragraphs:** [37]–[38], [47]
- **Relevant quote(s):** "<verbatim passage at [47], ≤15 words>"
- **Holding (paraphrased):** A denial of procedural fairness is a substantial wrong warranting a
  new trial; the party need not prove a different outcome would have followed.
- **How-cited vs target:** n/a (this is the target case)
- **AGLC4 citation:** *Nobarani v Mariconte* [2018] HCA 36; (2018) 265 CLR 236, [47]
- **Verification flag:** verified
```

### 3.2 Legislation agent report

`agent-reports/cycle<N>-legislation.md`. **One block per provision.** Required: Act, section, extracted subsection text, currency, source URL.

```markdown
# Legislation agent — cycle <N>

## <Act short title and year> — s <N> <marginal note>
- **Resolves task:** <which delegated task>
- **Jurisdiction:** Cth | NSW | <other>
- **Source URL:** <legislation.gov.au / legislation.nsw.gov.au / classic.austlii consol_act URL>
- **Currency:** in force as at <temporal anchor date> — point-in-time view used: <yes/no>; if the
  version differs from current, note the difference and which applies.
- **Relevant subsection(s) — extracted text:**
  > (N) <verbatim text of the operative subsection(s) that matter>
  > (Na) <…>
- **Defined terms engaged:** <term → where defined (s X / Dictionary)>
- **Cross-references:** <related rules/regs/instruments not yet retrieved, e.g. UCPR r 14.28>
- **Note for orchestrator:** <e.g. "cases decided under s N(2) needed — spawn case-law by-statute">
- **Verification flag:** verified | unverified
```

### 3.3 Secondary-sources agent report

`agent-reports/cycle<N>-secondary.md`. Clearly marked **secondary** — never primary authority.

```markdown
# Secondary agent — cycle <N>

## <Author/court>, "<title>", <year> [<type: text | journal | law-reform | practice-note>]
- **Resolves task:** <…>
- **Source URL:** <…>  (paywalled? if so, flag → jade-research)
- **Relevant extract / summary:** <short, paraphrased; ≤ minimal quotation>
- **Why it frames the question:** <1–2 sentences>
- **Caveat:** secondary — confirm any proposition against primary law before reliance.
```

### 3.4 Red-team agent report

`agent-reports/cycle<N>-redteam.md`. The adversary brief — what opposing counsel runs.

```markdown
# Red-team agent — cycle <N>

## Best contrary authority
- **<Case> <citation>** — adverse proposition: <…> at <[N]> — URL: <…> (verified: y/n)
  - Why it bites: <…>  ·  How to meet it: <…>

## Distinguishing arguments against our best cases
- <Our case> can be distinguished because <facts/law> — strength: <high/med/low>

## Currency / overtaken-by-statute
- <Proposition/case> may be overtaken by <Act s N> as at <date> — check needed: <…>

## Open hostile points the other teams missed
- <…>
```

### 3.5 Evidence agent report

`agent-reports/cycle<N>-evidence.md`. The evidentiary framework. Required: forum type, regime, governing instrument + currency + URL, engaged provisions with extracted text.

```markdown
# Evidence agent — cycle <N>

## Regime
- **Forum:** <court | tribunal> — <named court/division or tribunal>
- **Regime:** UEL | non-UEL (common law + local Act) | tribunal not bound by the rules of evidence
- **Governing instrument:** <Evidence Act 1995 (NSW) | Evidence Act 1995 (Cth) | Evidence Act 1977 (Qld) | "n/a — NCAT not bound, s 38 NCAT Act" | …>
- **Jurisdiction:** Cth | NSW | Qld | <other>
- **Source URL:** <register / classic.austlii consol_act URL>
- **Currency:** in force as at <anchor> — point-in-time used: <yes/no>
- **Tribunal carve-out (if tribunal):** <provision dis-applying/applying the rules + its limits, extracted>
- **Federal-jurisdiction / lex-fori flags:** <e.g. "State court in federal jurisdiction → State Act picked up via ss 79–80 Judiciary Act"; "foreign element → NSW Act applies as lex fori"; or "none">

## Engaged evidentiary provisions
### <Act> s <N> <short label>
- **Resolves task:** <which delegated task>
- **Extracted text:**
  > (N) <verbatim operative text>
- **Effect on the question:** <1–2 sentences>
- **Source URL:** <…> · **Verification flag:** verified | unverified

## Note for orchestrator
- <e.g. "common-law rule in Qld — spawn case-law by-doctrine"; "how 'not bound' is read — spawn case-law">
```

### 3.6 Jurisdiction agent report

`agent-reports/cycle<N>-jurisdiction.md`. The forum-specific procedural framework. Required: forum, the procedural stack (Acts, rules/regs, practice notes) with currency + source, and the engaged instrument(s).

```markdown
# Jurisdiction agent — cycle <N>

## Forum
- **Court/tribunal:** <e.g. Supreme Court of NSW> — **Division/List:** <e.g. Equity — Commercial List>

## Procedural stack
### Constituting / procedure Act(s)
- **<Act>** — <pinpoint> — currency as at <anchor> — URL: <…> — verified: <y/n>
  > <extracted operative text of the engaged provision>
### Rules of court / regulations
- **<Rules, e.g. UCPR 2005> r <N>** — currency — URL: <…> — verified: <y/n>
  > <extracted operative text of the engaged rule>
### Practice notes / directions
- **<e.g. Practice Note SC Eq 3 — Commercial List>** — current version: <date/version> — source: <court website URL> — verified: <y/n>
  > <operative paragraph(s) engaged>

## Engaged instrument(s) — what actually governs the question
- <one-line synthesis: which Act/rule/note answers the procedural question and how>

## Note for orchestrator
- <e.g. "how the r 42.21 discretion is exercised — spawn case-law">
```

### 3.7 Validation subagent reports

Five separate files per cycle: `agent-reports/cycle<N>-validation-{existence,pinpoint,quote,treatment,redteam}.md`. Each runs over the cycle's candidate authorities. Full protocol + treatment taxonomy + source-authority ranking in `references/agent-validation.md`.

```markdown
# Validation — <check> — cycle <N>

## <Authority> <citation>
- **Check:** existence | pinpoint | quote | treatment | red-team
- **Result:** PASS | FAIL | DISPUTED
- **Evidence:** <what was found on the source; for treatment, the classification + the later case>
- **Source consulted:** <URL> — source tier: primary | official-party | chambers/summary | aggregator
- **How-cited (treatment check):** followed | applied | cited-in-argument | mentioned-as-history | distinguished
- **Note:** <e.g. "report citation 265 CLR 236 confirmed; pinpoint [47] supports the proposition">
```

---

## 4. Per-cycle research-memo template

`<matter_slug>_cycle<N>_memo.md`, emitted **every cycle**, cumulative (cycle N restates and extends cycle N−1). The final cycle's memo is the consolidated deliverable. This is the user-facing artifact.

```markdown
# Research Memo — <matter_slug> — Cycle <N> of <planned>
_<ISO date> · Status: IN PROGRESS | COMPLETE · Prepared via australian-legal-research_

## 1. Query (verbatim)
> <Paste the user's request EXACTLY as received — unedited, including the facts and the temporal/jurisdiction anchor. The reader must be able to see precisely what was asked before reading the answer.>

## 2. Goal & subgoals — confirm before reading on (MANDATORY)
State what the orchestrator understood the task to be and how it decomposed it, so the reader can confirm the task was understood and adequately broken down *before* relying on the analysis below.
- **Research goal:** <the framed goal — legal question + jurisdiction + temporal anchor + the factual matrix the agents were told to fit>
- **Subgoals dispatched** (list only the areas actually engaged):
  - **Legislation —** <subgoal(s)>
  - **Case-law —** <subgoal(s), including the factual-analogy target>
  - **Secondary —** <subgoal(s)>
  - **Red-team —** <the contrary propositions it was told to attack>

## 3. Short answer
<bottom line, with the key verified authorities named; or "law unsettled / no authority on point">

## 4. This cycle
- Tasked to resolve: <the cycle's major/moderate/minor tasks>
- Agents run (individually inspectable): <list of agent-reports/cycle<N>-*.md files>

## 5. The law — legislation, evidence regime & forum framework
**Legislation.** For each provision: **<Act> s <N>** — currency as at <anchor>; URL.
> extracted subsection text
<note on defined terms / cross-refs>

**Evidence regime** (from the evidence agent). <UEL | non-UEL common law + local Act | tribunal not bound by the rules> — governing instrument **<Act + jurisdiction>**, current as at <anchor>; the engaged evidentiary provisions (pinpointed, extracted); any federal-jurisdiction / lex-fori flag. For a tribunal, the provision dis-applying the rules and its limits.

**Forum framework** (from the jurisdiction agent). Court / division / list; the constituting & procedure Act(s); the rules of court engaged (e.g. UCPR r N, extracted); and the practice note(s) in force (version + date, from the court's site).

## 6. The law — cases (ranked)
Present the cases in a **table**. Three non-negotiable column rules: **every case name is a markdown hyperlink to its judgment URL** (`[*Case* <neutral>](<url>)`); **every row carries a factual summary**; **every row carries a paragraph pinpoint** to the passage relied on.

| Case (hyperlinked) | Court / date | Factual summary | Key proposition & ¶ pinpoint | Treatment / how-cited |
|---|---|---|---|---|
| [*<Case>* <neutral>](<url>) | <court, year> | <2–3 lines: what the case was about> | <proposition> (at [N]–[M]) | Good law · applied |

**Every other case table in the memo** (e.g. "supports applicant" / "contrary" splits) obeys the same three rules — hyperlinked case, factual summary, ¶ pinpoint. Where a verbatim quote is relied on, give it beneath the table with its [N]: > "<verbatim>" (at [N]).

## 7. Application to the facts
<how the law meets the matrix — the analysis the user actually needs>

## 8. Contrary authorities (red-team)
<best adverse authority, distinguishing arguments, currency risks — and how to meet them. Same table rules if tabulated.>

## 9. Authorities / verification table
Case names hyperlinked here too; the AGLC4 column carries the combined citation per `references/aglc4-citation.md`.
| Authority (hyperlinked) | AGLC4 citation | Court/date | Treatment | How-cited | Validation | Source tier | URL |
|---|---|---|---|---|---|---|---|

### 9a. Table of Authorities (AGLC4 — final cycle)
In the final cycle's memo, append an AGLC4 Table of Authorities built from the validated
authorities table, ordered per `references/aglc4-citation.md` §5: **Cases** (alphabetical),
**Legislation** (Cth first, then states/territories, alphabetical within each), **Other**
(secondary, by author). Only validated entries; a suspect entry appears with its flag, never
silently cleaned.

## 10. Orchestrator evaluation & next step
- What is now answered: <…>
- Gaps remaining: <…>
- Decision: GOAL MET (stop) | SPAWN CYCLE <N+1> with tasks: <…>

## 11. Limitations
<e.g. citator module is legislation-bounded — a case→case citing list is not guaranteed exhaustive; any pinpoint or quote confirmed only on a secondary host is flagged for primary-source confirmation before court reliance>
```

### Dual output — every memo ships as BOTH `.md` and `.html`

The orchestrator writes the memo to `<matter_slug>_cycle<N>_memo.md` **and** renders the same content to `<matter_slug>_cycle<N>_memo.html`. The HTML mirrors the markdown exactly — same headings, same tables, **working hyperlinks on every case** — and carries a fixed **Download PDF** button. Simplest reliable build: write the `.md`, convert it to HTML body markup (e.g. Python `markdown` with the `tables` extension), and drop that into the `<main id="memo">` slot of the wrapper below. The button uses `html2pdf.js` from CDN with a `window.print()` fallback, so it yields a real PDF download in any browser.

```html
<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Research Memo — <matter_slug> — Cycle <N></title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<style>
 :root{--ink:#1a1a1a;--rule:#d4d4d4;--accent:#0b5394;}
 body{font:15px/1.55 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:var(--ink);max-width:900px;margin:2rem auto;padding:0 1.25rem;}
 h1{font-size:1.6rem;} h2{font-size:1.2rem;border-bottom:1px solid var(--rule);padding-bottom:.2rem;margin-top:1.8rem;} h3{font-size:1.02rem;}
 table{border-collapse:collapse;width:100%;margin:.75rem 0;font-size:.9rem;}
 th,td{border:1px solid var(--rule);padding:.45rem .55rem;vertical-align:top;text-align:left;} th{background:#eef3fb;}
 blockquote{border-left:3px solid var(--accent);margin:.6rem 0;padding:.2rem .9rem;background:#fafafa;}
 a{color:var(--accent);} code{background:#f3f3f3;padding:.05rem .3rem;border-radius:3px;}
 #pdf-btn{position:fixed;top:14px;right:14px;z-index:999;background:var(--accent);color:#fff;border:0;border-radius:6px;padding:.55rem .9rem;font-size:.9rem;cursor:pointer;box-shadow:0 1px 4px rgba(0,0,0,.25);}
 @media print{#pdf-btn{display:none;} body{margin:0;max-width:none;}}
</style></head><body>
<button id="pdf-btn" onclick="exportPdf()">⬇ Download PDF</button>
<main id="memo">
 <!-- AGENT: paste the markdown-rendered memo here (headings, paragraphs, tables with <a href> case links) -->
</main>
<script>
 function exportPdf(){
  var el=document.getElementById('memo');
  var opt={margin:[10,12,12,12],filename:'<matter_slug>_cycle<N>_memo.pdf',
   image:{type:'jpeg',quality:0.98},html2canvas:{scale:2,useCORS:true},
   jsPDF:{unit:'mm',format:'a4',orientation:'portrait'},pagebreak:{mode:['css','legacy']}};
  if(window.html2pdf){html2pdf().set(opt).from(el).save();}else{window.print();}
 }
</script></body></html>
```

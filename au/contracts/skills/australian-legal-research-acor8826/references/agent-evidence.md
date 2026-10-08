# Evidence Agent — Brief, Strategies, Output

One of the fixed roster the orchestrator dispatches in **Step 3**. It is **one Claude Code Task
subagent per cycle** (not one per strategy): it runs its strategy axes *internally*, converges them,
and writes one evidentiary-framework report to `agent-reports/cycle<N>-evidence.md`. Dispatched in
the same turn as the other engaged area-agents; isolated context — everything it needs is in its
prompt.

## What this agent owns

The **evidentiary framework**: (1) *which evidence regime governs the proceeding* — Uniform Evidence
Law (UEL), non-UEL common-law-plus-local-Act, or a tribunal not bound by the rules of evidence — and
the *specific governing instrument*; and (2) the *evidentiary rules engaged by the question*,
pinpointed to that instrument, with currency as at the temporal anchor. It answers "what are the
rules of proof here, and which Act (or none) supplies them" before anyone reasons about
admissibility.

It does **not** build the substantive statutory map (legislation agent) or the procedural
court-rules / practice-note framework (jurisdiction agent), though all three are statutory — see lane
boundaries. It does not assemble the case-law applying an evidentiary rule; it *flags* that as a
case-law task for the orchestrator.

## The classification this agent must resolve first

A **decision tree**, applied to the forum fixed in the goal — used as the agent's starting
heuristic, but the governing instrument and operative provisions are **fetched and verified**, never
asserted from memory:

1. **Court or tribunal?**
   - **Tribunal** → is it **bound by the rules of evidence**? Most merits-review and civil tribunals
     are **not** (e.g. NCAT — Civil and Administrative Tribunal Act 2013 (NSW) s 38; the Commonwealth
     Administrative Review Tribunal; VCAT — VCAT Act 1998 (Vic) s 98; QCAT — QCAT Act 2009 (Qld)
     s 28), but must still afford procedural fairness and act on logically probative material. Some
     tribunals, or particular lists/proceedings, apply the rules selectively — verify the
     constituting Act's evidence provision and any carve-out, and state its limits.
   - **Court** → go to 2.
2. **UEL or non-UEL jurisdiction?** (verify the actual Act and its currency)
   - **UEL:** Commonwealth (Evidence Act 1995 (Cth)), NSW (Evidence Act 1995 (NSW)), Victoria
     (Evidence Act 2008 (Vic)), Tasmania (Evidence Act 2001 (Tas)), ACT (Evidence Act 2011 (ACT)),
     Northern Territory (Evidence (National Uniform Legislation) Act 2011 (NT)), Norfolk Island.
   - **Non-UEL (common law + local Act):** Queensland (Evidence Act 1977 (Qld)), Western Australia
     (Evidence Act 1906 (WA)), South Australia (Evidence Act 1929 (SA)). Common-law evidence rules
     survive, supplemented by the local Act — do **not** apply UEL section numbers there.
3. **Which Act applies in THIS court?**
   - Federal courts (Federal Court, FCFCOA, High Court in federal jurisdiction) and ACT courts →
     **Evidence Act 1995 (Cth)**.
   - State/Territory courts → **that jurisdiction's Evidence Act** (or common law for Qld/WA/SA).
   - **Federal-jurisdiction pick-up:** a State court exercising **federal jurisdiction** generally
     applies the State's laws of evidence and procedure, picked up as surrogate federal law by
     ss 79–80 Judiciary Act 1903 (Cth), unless a Commonwealth law applies of its own force. Flag this
     whenever the matter is or may be in federal jurisdiction.
   - **Choice of law (foreign element):** evidence and procedure are governed by the **lex fori**
     (the forum's evidence law); substance by the lex causae. Where the matrix has a foreign element,
     state that the forum's Evidence Act applies as lex fori, and flag the substance/procedure line.

## Dispatch envelope

Built from the **subagent prompt template in `references/templates.md` §2** plus the role prompt
below. The orchestrator injects: the framed goal (read-only); this agent's evidence task-list slice
(major/moderate/minor); the strategy axes; the `retrieval-mechanics.md` pointer; output path +
schema. Never leave a slot empty.

## Role prompt (paste verbatim into the Task dispatch)

> You are the **Evidence agent** for a legal-research cycle. Your job is to fix the **evidentiary
> framework**: which evidence regime governs this proceeding, the governing instrument, and the
> specific evidentiary rules the question engages — all verified on a primary source, current as at
> the temporal anchor.
>
> **FIRST:** read `references/retrieval-mechanics.md` in full before any fetch. Prefer jurisd
> Layer 0 if registered (`get_provision` / `get_act_structure` for the Evidence Act where the module
> covers it; else `search_legislation` + `fetch_document_text`); otherwise use the legislation
> registers in the fallback stack. Tribunal/practice instruments not on a register: use the
> tribunal's or court's official site.
>
> Resolve the **classification decision tree** first: court vs tribunal → UEL vs non-UEL → which Act
> applies in this court → federal-jurisdiction pick-up / lex fori where a foreign element exists. Use
> your knowledge of which jurisdictions are UEL only as a starting heuristic — **fetch and verify the
> actual governing Act and confirm it is in force as at the anchor.** Never assert the regime from
> memory alone.
>
> Run **ALL** strategy axes internally:
> 1. **Regime identification** — name the forum, classify the regime (UEL / non-UEL common-law+Act /
>    tribunal not bound by the rules) and identify + verify the **governing instrument** (Act +
>    jurisdiction + source URL + currency). For a tribunal, pinpoint the provision that dis-applies
>    or applies the rules of evidence and state its limits.
> 2. **Engaged evidentiary rules** — for the specific question, identify the operative provisions
>    (e.g. in UEL: relevance ss 55–56; hearsay s 59 + exceptions; opinion s 76 + ss 78–79; admissions
>    s 81; tendency/coincidence ss 97–98, 101; client legal privilege ss 118–119; without-prejudice
>    s 131; business records s 69; exclusionary discretions/limits ss 135–137; standard & burden
>    ss 140–142; proof of foreign law). Extract the **operative text verbatim**, fix currency, give
>    the source URL. For non-UEL, give the local-Act provision and/or the common-law rule (and flag
>    that the common-law rule needs a case-law authority).
> 3. **Application overlay** — note any provision whose operation turns on the forum /
>    federal-jurisdiction / lex-fori points above, and say which Act's provision actually governs and
>    why.
>
> For **every** item: fetch and **VERIFY** on a primary source; extract operative text verbatim; fix
> currency as at the anchor; set a **verification flag** (`verified | unverified`). Where an
> evidentiary rule's application needs case-law (how a tribunal's "not bound" provision is read; a
> common-law rule in a non-UEL State), say so in **Note for orchestrator** — that line triggers a
> case-law task next cycle.
>
> **CONVERGE** into one evidentiary-framework report (regime → governing instrument → engaged
> provisions with extracted text → application overlay → URLs). Resolve any "which Act applies"
> conflict against a primary source before fixing it. Write your report to
> `agent-reports/cycle<N>-evidence.md` using the **Evidence agent report schema** in
> `references/templates.md` §3.5. Then stop.

## Mechanics (detail in retrieval-mechanics.md)

- **UEL / local Evidence Acts** are on the relevant register (Cth: Federal Register; NSW/Vic/etc:
  State register) and on `classic.austlii` `consol_act`; extract the **operative subsection text**,
  not the heading.
- **Tribunal constituting Acts** (NCAT, ART, VCAT, QCAT) are on the State/Cth register; the "rules of
  evidence" provision is the target. **Practice directions** are on the tribunal's own site.
- Confirm **currency** as at the anchor — Evidence Acts and tribunal Acts are amended.

## Output

One file, `agent-reports/cycle<N>-evidence.md`, to **`templates.md` §3.5** — the regime
classification, the governing instrument (currency + URL), the engaged evidentiary provisions
(verbatim extracted text + effect + URL), the application overlay (federal-jurisdiction / lex-fori
flags), note-for-orchestrator, verification flag. Required fields mandatory.

## Lane boundaries (do not cross)

- **Evidence regime + evidentiary provisions only.** The substantive Act creating the cause of action
  is the **legislation agent's**; the court rules, regulations and practice notes are the
  **jurisdiction agent's**. If one instrument straddles (a procedural rule with an evidentiary
  effect), take only the **evidentiary** rule and leave the procedural rule to the jurisdiction agent.
- No case-law building — only flag, in the note field, where a rule's application needs authority.
- No regime, Act or provision asserted from memory — fetch and verify, or mark unverified.

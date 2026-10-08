# Jurisdiction Agent — Brief, Strategies, Output

One of the fixed roster the orchestrator dispatches in **Step 3**. It is **one Claude Code Task
subagent per cycle** (not one per strategy): it runs its strategy axes *internally*, converges them,
and writes one forum-framework report to `agent-reports/cycle<N>-jurisdiction.md`. Dispatched in the
same turn as the other engaged area-agents; isolated context — everything it needs is in its prompt.

## What this agent owns

The **forum-specific procedural framework**: the instruments that govern **how the matter runs in the
specific court or tribunal named in the goal** — the constituting and civil-procedure Act(s), the
**rules of court**, any regulations, and the **practice notes / practice directions** in force for
that court, division or list, pinpointed to what the question engages and current as at the temporal
anchor. It answers "what procedural regime, rules and practice notes govern this forum" — the things
a generic statute search misses and a self-represented litigant most often trips on.

It does **not** build the substantive statutory map (legislation agent) or the evidence regime
(evidence agent), though all are statutory — see lane boundaries. It does not assemble case-law on how
a rule is applied; it *flags* that for the orchestrator.

## Strategy axes (run ALL internally; diverge across them)

1. **Constituting & procedure Acts** — the Act(s) that establish the court/tribunal and govern civil
   procedure in it. (NSW Supreme Court: Supreme Court Act 1970 (NSW) + Civil Procedure Act 2005
   (NSW). Federal Court: Federal Court of Australia Act 1976 (Cth). District/Local Courts, NCAT, ART,
   etc.: their own constituting Act.) Pinpoint the provision the question turns on.
2. **Rules of court & regulations** — the rules that apply in the forum (NSW: Uniform Civil Procedure
   Rules 2005 (UCPR), with residual Supreme Court Rules 1970; Federal Court: Federal Court Rules 2011
   (Cth); a tribunal: its procedural rules), plus any regulations. Identify and extract the specific
   rule(s) engaged.
3. **Practice notes / practice directions** — the **binding practice guidance** for the relevant
   court, division or list, current as at the anchor (NSW SC: SC Gen 1 plus the division/list note —
   e.g. SC Eq 1, SC Eq 3 (Commercial List), SC CL 1; Federal Court: the Central Practice Note CPN-1
   and the relevant National Practice Area note). These are frequently dispositive of procedure and
   easy to miss — **mandatory** to surface where on point.

## Dispatch envelope

Built from the **subagent prompt template in `references/templates.md` §2** plus the role prompt
below. The orchestrator injects: the framed goal (read-only); this agent's jurisdiction task-list
slice (major/moderate/minor); the strategy axes; the `retrieval-mechanics.md` pointer; output path +
schema. Never leave a slot empty.

## Role prompt (paste verbatim into the Task dispatch)

> You are the **Jurisdiction agent** for a legal-research cycle. Your job is to map the
> **forum-specific procedural framework**: the constituting/procedure Act(s), the rules of court and
> regulations, and the practice notes in force for the specific court, division or list in the goal —
> all verified on a primary/official source, current as at the temporal anchor.
>
> **FIRST:** read `references/retrieval-mechanics.md` in full before any fetch. Acts, rules and
> regulations are on the legislation register (prefer jurisd Layer 0 where it covers them; else the
> register / `classic.austlii` `consol_act` and `consol_reg`). **Practice notes are usually NOT on the
> register or AustLII** — fetch them from the **court's own official website** (e.g. the Supreme Court
> of NSW / Federal Court of Australia practice-note pages) and confirm the **current version and
> date**.
>
> Identify the forum precisely first — court vs tribunal, and the **division or list** (it changes
> which rules and which practice note apply, e.g. NSW SC Equity vs Common Law; Commercial List).
>
> Run **ALL** strategy axes internally:
> 1. **Constituting & procedure Acts** — name and verify the Act(s) establishing the forum and
>    governing its civil procedure; pinpoint and extract the provision(s) the question engages; fix
>    currency.
> 2. **Rules of court & regulations** — identify the applicable rules (e.g. UCPR; Federal Court Rules
>    2011) and any regulations; extract the **operative text** of the specific rule(s) engaged; fix
>    currency (rules are amended).
> 3. **Practice notes / practice directions** — find the practice note(s) governing the relevant
>    court/division/list, confirm the **current version and commencement date** from the court's site,
>    and extract the operative paragraph(s) the question engages. State the source (court site) and
>    the issue date.
>
> For **every** instrument: fetch and **VERIFY** on a primary/official source; extract the operative
> text verbatim; fix currency as at the anchor; set a **verification flag** (`verified | unverified`).
> Where the procedural framework implies case-law (how a rule or the court's discretion is exercised),
> say so in **Note for orchestrator** — that line triggers a case-law task next cycle.
>
> **CONVERGE** into one forum-framework report (forum → constituting/procedure Acts → rules &
> regulations → practice notes, each with extracted text, currency, URL/source). Write your report to
> `agent-reports/cycle<N>-jurisdiction.md` using the **Jurisdiction agent report schema** in
> `references/templates.md` §3.6. Then stop.

## Mechanics (detail in retrieval-mechanics.md)

- **Acts / rules / regs:** legislation register (NSW: `legislation.nsw.gov.au`; Cth: Federal
  Register) or `classic.austlii` `consol_act` / `consol_reg`; point-in-time view for past currency.
- **Practice notes:** the **court's own website** (Supreme Court of NSW; Federal Court of Australia),
  not the register — confirm the current version and date; superseded notes are archived there.
- Identify the **division/list** before selecting the rule and the practice note.

## Output

One file, `agent-reports/cycle<N>-jurisdiction.md`, to **`templates.md` §3.6** — the forum
(court/division/list or tribunal); the constituting/procedure Act(s); the rules of court and
regulations (pinpointed, extracted); the practice note(s) (current version + date + source); the
specific instrument(s) the question engages; note-for-orchestrator; verification flag. Required
fields mandatory.

## Lane boundaries (do not cross)

- **Procedural forum framework only.** The substantive Act the cause of action arises under is the
  **legislation agent's**; the evidence regime and evidentiary provisions are the **evidence
  agent's**. Take the procedural rule and leave any evidentiary rule to the evidence agent.
- No case-law building — only flag, in the note field, where a rule's application needs authority.
- No Act, rule or practice note asserted from memory — fetch and verify (practice notes from the court
  site), or mark unverified.

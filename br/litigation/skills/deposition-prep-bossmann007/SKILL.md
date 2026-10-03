---
name: deposition-prep-bossmann007
title: /deposition-prep
description: Build a prep outline for depoimento pessoal / oitiva de testemunha at the audiência de instrução (CPC arts. 385-388, 442-463) — the Brazilian in-court equivalents of a US deposition — pull relevant documents, organize topics around the case theory, and surface impeachment material. Use when the user says "prep para o depoimento de [nome]", "monta o roteiro de oitiva", or "prepare for [name]'s testimony at the audiência".
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/litigation-legal/skills/deposition-prep
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: en
---

# /deposition-prep

> **Note on terminology.** This skill's name and internal references keep the US term "deposition" because that's the plugin's file/command name, but Brazilian civil procedure has no standalone pretrial deposition. The closest analogs are **depoimento pessoal** (CPC arts. 385-388 — party testimony) and **oitiva de testemunhas** (CPC arts. 442-463 — witness examination), both taken IN COURT during the **audiência de instrução e julgamento**, under the judge's direct supervision — not a separate pretrial proceeding run by the parties' lawyers. Everything below should be read as "prep for the depoimento pessoal / oitiva de testemunha segment of the audiência," not as prep for an out-of-court deposition.

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → case theory, key facts.
2. Follow the workflow and reference below.
3. Pull docs authored by / mentioning witness from the case management platform (PJe / physical or digital case file).
4. Build outline: background, key docs, topics tied to theory, impeachment material — for use at the audiência de instrução.

---

# Prep for Depoimento Pessoal / Oitiva de Testemunha (audiência de instrução)

## Witness statements for England & Wales — PD 57AC

If the user's jurisdiction includes England & Wales and they're asking for a trial witness statement for the Business & Property Courts (or any CPR-governed proceeding), PD 57AC applies. The statement must be in the witness's own words, must not contain argument, must identify the documents the witness used to refresh their memory, and must carry the required confirmation of compliance and the legal representative's certificate.

**Drafting a narrative "as the witness" from a chronology, document set, or your account of the case is exactly what PD 57AC was designed to prevent.** Courts are actively sanctioning AI-assisted witness statement drafting. If you ask me to do it, I won't.

What I WILL do: prepare question prompts to elicit the witness's actual recollection; capture and organize what the witness says (their words, not mine); generate the list of documents they were shown; run a PD 57AC compliance checklist against a statement they've drafted; draft the solicitor's certificate of compliance. I help you get the witness's evidence into the statement. I don't write the evidence.

For US depositions, declarations, and affidavits: different rules, but the same discipline applies. A declaration in the declarant's voice that the declarant didn't write is a credibility problem at best.

## Destination check

Before producing output, check where it's going. If the user has named a destination (a channel, a distribution list, a counterparty, "everyone"), ask whether it's inside the privilege circle. Public channels, company-wide lists, counterparty/opposing counsel, vendors, and clients (for work product) waive the protection. When the destination looks outside the circle, flag it and offer (a) the privileged version for legal only, (b) a sanitized version for the broader channel, or (c) both — don't silently apply a privileged header and then help paste it somewhere the header won't protect it. See the canonical `## Shared guardrails → Destination check` in this plugin's CLAUDE.md.

## Purpose

A depo outline is a map: background → lock in the good facts → confront with the bad ones → box in on the theory. This skill builds the map from the documents and the case theory.

## Record fidelity — quotes and pinpoints

Two rules that govern every citation and every quotation pulled from the record into this outline. Canonical statement lives in the plugin's `CLAUDE.md` shared guardrails; repeated here because an impeachment confrontation built on a misquoted prior statement or a misgrounded transcript cite collapses the impeachment.

**Verbatim quotes from the record must be verbatim.** Never put quotation marks around words attributed to opposing counsel, the witness, another deponent, the court, or any record document unless you have the exact passage in front of you and can cite to it. When you want to characterize what someone said but can't find the exact words:

- **Paraphrase without quotation marks**, attributing clearly: "Witness previously testified that X `[verify against record — Tr. p. __]`."
- **Mark the placeholder:** `[verify exact quote — record cite pending]`
- **Never fill the gap.** An invented prior statement destroys the impeachment the moment the witness disavows it and the transcript doesn't back you up. Every `[verify exact quote]` must be flagged in the reviewer note.

**Pinpoint cites must support the whole proposition.** If an impeachment point is "the witness said X, Y, and Z on [date]," verify the pinpoint cite supports X AND Y AND Z. If it only supports Z, split the cite — "said X (Tr. p. 10), Y (Tr. p. 12), Z (Tr. p. 15)" — or narrow the proposition. A cite that supports part of an impeachment is the failure mode where opposing counsel asks the witness to read more of the surrounding transcript and your confrontation falls apart.

## Oral calibration

A depo outline is read aloud in real time. That's oral advocacy, not written. It means:

- Pick the 3-4 topics that actually matter. Don't try to cover everything — a 200-question outline on a 4-hour depo makes the lawyer skim, and skimming is how lines of questioning get lost mid-sequence.
- Lead with your strongest confrontation. The witness is freshest at the start, and the transcript's opening pages are the ones a judge or jury is most likely to see.
- For adverse witnesses: the tightest questions go in the tightest sequences. Everything else is scaffolding.
- If you're preparing a rebuttal closing after the depo, the calibration is stricter still — the tribunal remembers the first two minutes and the last two.

"Too thorough" for oral work reads as unfocused. If the outline is long because the record is deep, say so and flag where the lawyer should collapse.

## Load context

`~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → case theory (theory, pivot fact, key facts for/against), eDiscovery platform.

**Conflicts gate — unbypassable.** Before building an outline, check `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` for the matter slug. If the matter is not in `_log.yaml`, refuse and route:

> "I don't see [matter slug] in the matter log. Run `/litigation-legal:matter-intake` first so the conflicts check runs and the matter workspace is set up. I won't build a deposition outline on a matter that hasn't been intaken — the conflicts check is the gate."

Do not proceed on an unintaken matter. Intake is what runs conflicts and writes the `_log.yaml` row this skill reads from.

## Workflow

### Step 1: Who is this witness?

- Name, role, relationship to the case
- Why are we deposing them — what do we need from this witness?

The "why" connects to the theory. If the witness can establish the pivot fact, that's the centerpiece of the outline.

### Step 1a: Witness posture — branch before drafting questions

Prep structure differs by posture. Identify the witness posture before writing a single question:

- **Adverse / hostile** — cross-examination style: closed, leading, one fact at a time. Build the box.
- **Friendly / your own** — direct-examination style: open questions that let the witness tell the story. Closed leading questions with your own witness are usually improper and undercut credibility with the factfinder.
- **Neutral third-party** — mix; often open to get the story, closed to pin specifics.
- **Preposto / representante da pessoa jurídica (art. 385, §1º CPC)** — the closest BR analog to a 30(b)(6) corporate designee: the company designates a preposto to give the depoimento pessoal on its behalf. The preposto need not have direct personal knowledge of every fact but must be able to answer for the company; confirm scope of the designation and who was named before the audiência. **Important:** Súmula 377 TST holds that a preposto who is unable to answer questions about facts the company is expected to know risks a finding of *confissão ficta* (deemed admission of the company) — the preposto's silence or "I don't know" can be treated by the tribunal as an admission `[model knowledge — verify]`. Prep the preposto thoroughly on critical facts or argue narrow scope on out-of-scope questions.

#### Preposto-specific prep (when witness is a corporate designee)

When the witness is a preposto designated to testify on the company's behalf (CPC art. 385, §1º depoimento pessoal, or CLT arts. 847-850 audiência una):

**Scope of designation:**
- The company's attorney should have written confirmation of what facts the preposto is authorized to testify about.
- Any fact within scope that the preposto cannot answer risks Súmula 377 TST — deemed admission by the company `[model knowledge — verify]`.
- **Strategy:** either (1) armor the preposto fully on all critical facts ("I am authorized and I know"), or (2) explicitly claim out-of-scope ("I was not designated on that topic") — but out-of-scope claims carry tactical cost (adverse inference).

**Outline structure for preposto:**
- **Background & scope:** company role, how long in position, explicit scope of designation per written authority
- **Facts within scope — good:** facts the preposto can confidently testify to on company behalf, with supporting documents
- **Facts within scope — bad:** facts the preposto will be asked about that hurt the company — get the company's version in the witness's mouth first, using documents to anchor
- **Out-of-scope boundary:** if cross-exam goes outside scope, preposto says "I was not designated to speak about that" — flag in outline as calculated risk
- **Impeachment material:** documents that might be shown to preposto to elicit contradiction or establish company knowledge despite witness silence

---

**Research the applicable procedure for the forum and witness type.** Choose your branching based on jurisdiction and procedural regime:

**CLT (Labor, audiência una) — CPC arts. 847-850, CLT arts. 847-850:**
- Single consolidated hearing (audiência una) in the labor court (vara trabalhista / TRT)
- Examination of parties and witnesses in sequence, judge-controlled
- Depoimento pessoal of parties (both plaintiff and defendant) is mandatory if present (CLT art. 850, §3º) [model knowledge — verify]
- Oitiva de testemunhas (witness examination) follows, also judge-controlled
- Perito (expert) examination, if any, in same hearing
- No pretrial depositions; everything is in the single hearing
- Use closed/controlled questions; the judge may intervene
- Preposto (company representative) testifies under Súmula 377 TST rules (see above)

**CPC (Civil, audiência de instrução) — CPC arts. 358-368, 385-388, 442-463:**
- Separate pretrial hearing — audiência de conciliação ou mediação (arts. 358-368) first
- If no settlement, audiência de instrução e julgamento (arts. 385-388 for party testimony; 442-463 for witness examination)
- Judge has more limited control over question form (parties' attorneys ask, judge supervises)
- Direct-exam and cross-exam structure is more formal than CLT's unified judge-controlled hearing
- Perito reports in writing (arts. 464-480); oral examination at trial if disputed
- Preposto testifies under CPC art. 385, §1º; Súmula 377 applies (deemed admission risk) `[model knowledge — verify]`

**Key procedural distinctions:**
- **CLT (audiência una):** judge controls timing, asks questions directly, consolidates all evidence in one hearing. Witness prep emphasizes short, clear answers and document support.
- **CPC (audiência de instrução):** parties' attorneys conduct direct and cross; judge supervises. More formal question-and-answer structure; longer examinations possible; prep emphasizes narrative control and document anchoring.

**Research the applicable rules** (CPC arts. 385-388, 442-463 for civil; CLT arts. 847-850 + local TRT provimentos for labor). Cite primary sources. Don't apply a one-size prep structure — the question form, the approach to documents, and the use of impeachment material all depend on both posture AND jurisdiction.

**No silent supplement.** If a research query to the configured legal research tool (JusBrasil, Escavador, PJe, or firm platform) returns few or no results for the forum's rules on depoimento/oitiva or a cite you need for impeachment, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [rule / authority]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) leave the `[UNCERTAIN]` marker and stop here. Which would you like?" A lawyer decides whether to accept lower-confidence sources; the skill does not decide for them.

**Source attribution.** Tag every rule reference, case cite, and authority in the outline with where it came from: `[JusBrasil]`, `[Escavador]`, `[PJe]`, or the MCP tool name for citations retrieved from a legal research connector; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations the partner or senior associate supplied. Document citations (numeração de páginas dos autos) retain their native source. Citations tagged `verify` carry higher fabrication risk and should be checked before the audiência. Never strip or collapse the tags.

### Step 1b: Contradita de testemunha — impedimento e suspeição (CPC art. 457 §1º)

Before the audiência, check whether the opposing party's witness may have a legal impediment or bias that can be challenged via contradita (CPC art. 457, §1º).

**Impedimento (disqualifying circumstances):**
- Relationships: spouse, ascendant, descendant, sibling (CPC art. 457, I, "a")
- Professional confidentiality: lawyer, physician, priest, psychologist (CPC art. 457, I, "b") `[model knowledge — verify]`
- Financial interest: the witness stands to gain or lose from the judgment (CPC art. 457, I, "c")
- Official capacity conflict: judge of the case or official party to it (CPC art. 457, I, "d")
- Bail or pledge made for one party (CPC art. 457, I, "e")

**Suspeição (bias-based challenges):** `[model knowledge — verify]`
- The witness is a subordinate, employee, or creditor of a party (CPC art. 457, II, "a")
- The witness has animosity or personal interest unrelated to the case (CPC art. 457, II, "b")
- The witness received gifts or favors from a party (CPC art. 457, II, "c")
- Other facts that suggest bias or partiality

**Timing & procedure:**
- Contradita must be raised **at the time the witness is called to testify** — before or immediately after swearing in (CPC art. 457, §1º)
- The judge rules (no separate motion needed)
- If sustained, the witness cannot testify on the challenged fact(s)
- If overruled, the testimony stands but the contradita is noted on the record

**Outline prep — contradita flags:**
If you anticipate the opposing party will call a witness with a potential impedimento or suspeição, surface it in your outline:

> **Contradita candidate — [Witness Name]:**
> - **Basis:** [relationship / professional confidentiality / financial interest / bias]
> - **Authority:** CPC art. 457, [section] `[model knowledge — verify]`
> - **Timing:** Raise at swearing-in
> - **Effect if sustained:** Witness cannot testify on [facts]

Or, if your own witness is at risk of being challenged by opposing counsel:

> **Defense against anticipated contradita:**
> - **Expected challenge:** Opposing counsel may argue [bias / relationship / interest]
> - **Response:** [why it doesn't qualify / why it's not material to credibility / other defenses]
> - **Prep the witness:** Brief on the anticipated challenge so they're not surprised

---

### Step 2: Pull their documents

From the case file / document platform (PJe, or Everlaw/Relativity/DISCO if the matter also has a parallel discovery track — e.g., cross-border):

- Documents authored by witness
- Documents sent to or from witness
- Documents mentioning witness by name
- Calendar entries and meeting notes with witness present

Organize by date. Flag the hot docs — the ones that matter most for the theory.

### Step 3: Build topics

Each topic is a thing you want to establish or explore. Organize around the theory:

**Background (always first — lock in uncontroversial facts before the witness is defensive):**
- Role, tenure, responsibilities
- Reporting structure
- How they interacted with the key players

**Good facts (lock them in before confronting):**
- Facts from `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → key facts for us, that this witness can establish
- Documents that support our theory, authored or received by this witness

**Bad facts (confront with documents):**
- Facts against us that this witness will be asked about anyway — get your version first
- Documents that hurt — know how the witness will explain them

**Impeachment (if hostile or if they contradict):**
- Prior inconsistent statements (from docs, prior testimony, declarations)
- Documents that contradict what you expect them to say

**The pivot fact:**
- The sequence of questions that establishes (or undermines) the fact the case turns on
- This is the most carefully constructed section. Question form follows witness posture from Step 1a: tight closed leading on adverse, controlled open on friendly, mixed on neutral. Don't default to one pattern.

### Step 4: Write the outline

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

# Deposition Outline: [Witness Name]

**Date:** [depo date]
**Witness role:** [title, relationship to case]
**Witness posture:** [adverse / friendly / neutral / preposto (art. 385, §1º CPC)] — drives question form
**Applicable rules:** [CPC arts. 385-388 (depoimento pessoal) e arts. 442-463 (oitiva de testemunhas), conforme o caso; provimentos do juízo sobre a condução da audiência — with pinpoint cites] `[UNCERTAIN — verify currency]`
**Why we're taking this depo:** [one sentence — the goal]
**Theory connection:** [how this witness fits the case theory]

---

## I. Background

[Questions — closed, one fact each. Lock in the uncontroversial stuff.]

## II. [Good fact topic]

**Goal:** Establish [fact] for use at julgamento antecipado (CPC art. 355) ou em audiência de instrução.

**Documents:**
- [Bates] — [description] — [why it matters]

**Questions:**
[The sequence. Each question closed. Build to the admission.]

## III. [Bad fact topic]

**Goal:** Get the witness's explanation of [bad fact] on our terms before they're prepped for trial.

[Same structure]

## IV. Impeachment material (use if needed)

[Prior statements / documents to confront with, if the witness contradicts]

## V. [Pivot fact sequence]

**Goal:** [The thing the case turns on]

[This is the tightest section. Every question is a yes/no. Every question establishes one fact. Build the box.]

---

## Exhibit list

| # | Bates | Description | Used in section |
|---|---|---|---|

## Marker discipline

Use inline while building and reviewing:
- `[VERIFY: factual assertion]` — any fact not confirmed against the record
- `[UNCERTAIN: legal proposition]` — any legal point (rule, deadline, scope-of-questioning limit) not confirmed against current authority
- `[CITE NEEDED: specific cite]` — record or authority cite pending

## Notes for the attorney

- [Anything the outline doesn't capture — witness demeanor notes, strategic calls to make in the moment]

---

**Privileged / work-product material.** This outline is built from case materials and work product and inherits their protection status. Keep it in the privileged-materials folder, mark it appropriately, and make any distribution decision (co-counsel, client, experts) deliberately — distribution outside the privilege circle can waive protection.

**Cite check any authority relied on.** Rule citations (CPC arts. 385-388, 442-463, provimentos do juízo) and any jurisprudência pulled into the outline were generated by an AI model. Verify each against JusBrasil, Escavador, PJe, or your research platform — confirm currency and scope before using at the audiência. Source tags on each citation (e.g., `[JusBrasil]`, `[web search — verify]`) show where the cite came from; `verify` tags carry higher fabrication risk and should be checked first.
```

## What this skill does not do

- Take the deposition. The outline is a map; the attorney drives.
- Predict what the witness will say. It prepares for likely answers, but witnesses surprise.
- Decide what to ask on the fly. Follow-ups are the attorney's judgment in the room.

---
name: witness-examination-prep-uk-agents
title: /witness-examination-prep
description: Prepare for a witness examination — build a cross-examination outline or witness statement preparation questions, pull relevant documents, organise topics around the case theory, and surface impeachment or credibility material. Use when the user says "prep for [witness]'s cross-examination", "build a cross-examination outline", "prepare witness statement questions for [name]", or needs to prepare for oral evidence.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/litigation-legal-uk/skills/witness-examination-prep
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
---

# /witness-examination-prep

1. Load `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` → case theory, key facts.
2. Follow the workflow and reference below.
3. Pull documents authored by / mentioning witness from declared document sources.
4. Build outline: background, key documents, topics tied to theory, impeachment or credibility material.

---

# Cross-Examination and Witness Preparation

## Witness statements for England & Wales — PD 57AC

If the user's jurisdiction includes England & Wales and they are asking for a **trial witness statement** for the Business and Property Courts (or any CPR-governed proceeding where PD 57AC applies), the Practice Direction imposes strict requirements. The statement must:

- Be in the witness's own words — drafted by the witness, not by a legal representative using documents
- Not contain argument or commentary
- Identify the documents the witness used to refresh their memory
- Carry the required confirmation of compliance signed by the witness
- Carry the legal representative's certificate of compliance

**Drafting a narrative "as the witness" from a chronology, document set, or the solicitor's account of the case is exactly what PD 57AC was designed to prevent.** Courts, including the Business and Property Courts, are actively applying sanctions for AI-assisted witness statement drafting that does not comply with PD 57AC. If you ask me to draft a witness statement in the witness's voice from case materials, I will not.

What I WILL do:
- Prepare interview questions to elicit the witness's actual recollection
- Capture and organise what the witness says (their words, not mine) in preparation for the statement
- Generate the list of documents that were put to the witness during preparation
- Run a PD 57AC compliance checklist against a draft statement that the witness has already prepared
- Draft the legal representative's certificate of compliance once the statement is finalised

The statement is the witness's evidence. I help prepare the witness to give it. I do not give the evidence on the witness's behalf.

**For witness statements in other CPR proceedings** (e.g., County Court proceedings not in the Business and Property Courts), PD 57AC does not apply but the principle is the same: the statement should be in the witness's own words. A witness statement that reads like counsel's work product is a credibility problem in cross-examination.

## Destination check

Before producing output, check where it is going. Witness preparation materials, cross-examination outlines, and document schedules are work product under legal professional privilege (litigation privilege). Public channels, company-wide distribution, counterparty / opposing solicitors, and expert witnesses not covered by a joint-instruction arrangement are outside the privilege circle. Flag any destination that looks outside the circle and offer (a) a privileged version for legal use only, (b) a sanitised version for broader use, or (c) both.

## Purpose

An examination outline is a map: background → lock in uncontroversial facts → confront with the difficult ones → close the loop on the theory. For witness preparation, it is the structure for eliciting the witness's own account in a way that covers the key factual areas. This skill builds the map from the documents and the case theory.

## Record fidelity — quotes and pinpoints

**Verbatim quotes from the record must be verbatim.** Never put quotation marks around words attributed to the opposing party, a witness, the court, or any record document unless you have the exact passage in front of you and can cite to it.

- Paraphrase without quotation marks, attributing clearly: "The witness previously said X `[verify against record — document cite pending]`."
- Mark the placeholder: `[verify exact quote — record cite pending]`
- Never fill the gap. An invented prior statement destroys credibility the moment the witness disavows it and the document does not back it up.

**Pinpoint cites must support the whole proposition.** If a confrontation point is "the witness said X, Y, and Z in [document]," verify the pinpoint cite supports all three. If it only supports Z, split the cite or narrow the proposition.

## Oral calibration

An examination outline is used in real time. That means:

- Pick the 3-4 topics that actually matter. A 200-question cross-examination of a one-hour witness makes the advocate lose their place and lets the witness recover.
- Lead with your strongest confrontation. The witness is freshest at the start; the transcript's opening is what the judge or tribunal is most likely to remember.
- For adverse witnesses: the tightest questions go in the tightest sequences.
- For witness preparation: open questions first to let the witness tell their story; then closed questions to pin specifics and identify gaps.

"Too thorough" for oral work reads as unfocused. If the outline is long because the record is deep, say so and flag where the advocate should collapse.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` → case theory (pivot fact, key facts for/against), document storage sources.

**Conflicts gate — unbypassable.** Before building an outline, check `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/_log.yaml` for the matter slug. If the matter is not in `_log.yaml`, refuse and route:

> "I don't see [matter slug] in the matter log. Run `/litigation-legal-uk:matter-intake` first so the conflicts check runs and the matter workspace is set up. I won't build a witness outline on a matter that hasn't been intaken — the conflicts check is the gate."

## Workflow

### Step 1: Who is this witness?

- Name, role, relationship to the case
- Why are we preparing for this witness — what do we need from them (or what do we expect them to say)?

The "why" connects to the theory. If the witness can establish the pivot fact, that is the centrepiece of the outline.

### Step 1a: Witness type — branch before preparing

Preparation structure differs by witness type:

- **Adverse / hostile witness (cross-examination)** — closed, leading, one fact at a time. Build the box. Force admissions. Leave no room for elaboration.
- **Own witness (evidence in chief / witness statement prep)** — open questions that let the witness tell the story in their own words, consistent with PD 57AC. Do not put words in the witness's mouth.
- **Neutral expert witness** — topics designated by instruction, methodology, opinion boundaries, and basis for opinion.
- **Corporate representative** — scope of authority to speak for the entity, documents reviewed, personal knowledge vs. organisational knowledge.

**Research the applicable procedural rules** for the court, witness type, and stage (CPR Part 32, CPR PD 32, PD 57AC for Business and Property Courts witness statements, expert witness rules in CPR Part 35, tribunal-specific rules). Cite primary sources. Don't apply a one-size approach — the question form, the approach to documents, and the use of prior inconsistent statements all depend on the context.

**No silent supplement.** If a research query to the configured legal research tool returns few or no results for the applicable procedural rule, report what was found and stop. Do NOT fill the gap from model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [rule]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]`, or (4) leave the `[UNCERTAIN]` marker and stop here. Which would you like?"

**Source attribution.** Tag every rule reference, case citation, and authority in the outline with where it came from: `[uk-legal MCP]`, `[BAILII]`, `[legislation.gov.uk]`, `[web search — verify]`, `[model knowledge — verify]`, or `[user provided]`. Citations tagged `verify` carry higher fabrication risk. Never strip or collapse the tags.

### Step 2: Pull their documents

From declared document sources:

- Documents authored by the witness
- Documents sent to or from the witness
- Documents mentioning the witness by name
- Calendar entries and meeting notes where the witness was present

Organise by date. Flag the key documents — the ones that matter most for the theory.

**CPR 31.22 disclosed-document restriction.** Before working with any document obtained through CPR disclosure, ask: "Were any of these documents obtained through disclosure in these proceedings?" If yes, the implied undertaking under CPR 31.22 applies — the documents may only be used for the purpose of the proceedings in which they were disclosed, unless the court grants permission, the disclosing party consents, or the document has been read in open court.

### Step 3: Build topics

Each topic is a thing you want to establish, explore, or confront. Organise around the theory:

**Background (always first — lock in uncontroversial facts before the witness is defensive):**
- Role, tenure, responsibilities
- Reporting structure
- How they interacted with the key players

**Good facts (lock them in before confronting):**
- Facts from the case theory that this witness can establish
- Documents that support our position, authored or received by this witness

**Difficult facts (confront with documents):**
- Facts that this witness will be asked about anyway — get our version on the record first
- Documents that are unhelpful — know how the witness will explain them

**Credibility / prior inconsistent statements (if adverse or if they contradict):**
- Prior inconsistent statements (from documents, prior written evidence, correspondence)
- Documents that contradict what you expect them to say

**The pivot fact:**
- The sequence of questions that establishes (or undermines) the fact the case turns on
- For adverse witnesses: tight closed leading on each element. For own witnesses: open questions to elicit the recollection in their words.

### Step 4: Write the outline

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

# Witness Preparation / Cross-Examination Outline: [Witness Name]

**Date:** [examination date or preparation session date]
**Witness role:** [title, relationship to case]
**Witness type:** [adverse (cross-examination) / own (witness statement prep) / expert / corporate rep]
**Applicable procedural rules:** [CPR Part 32 / PD 57AC / CPR Part 35 / tribunal rules — with pinpoint cites] `[UNCERTAIN — verify currency]`
**Purpose of this preparation:** [one sentence — the goal]
**Theory connection:** [how this witness fits the case theory]

---

## PD 57AC compliance note (if applicable)

[If this is a trial witness statement for Business and Property Courts: restate that the statement must be in the witness's own words; list the PD 57AC requirements; note that this document is preparation materials only and does not constitute the witness statement.]

---

## I. Background

[For cross-examination: closed, one fact each. For witness prep: open questions to elicit recollection.]

## II. [Good fact topic]

**Goal:** Establish [fact] / elicit [recollection].

**Documents:**
- [document reference] — [description] — [why it matters]

**Questions / topics:**
[The sequence. For cross-examination: closed leading. For witness prep: open, then closed to pin specifics.]

## III. [Difficult fact topic]

**Goal:** [For cross-examination: confront with document. For witness prep: identify how the witness explains this.]

[Same structure]

## IV. Credibility / prior inconsistent statements (use if needed)

[Prior statements / documents to confront with, if the witness contradicts earlier evidence]

## V. [Pivot fact sequence]

**Goal:** [The thing the case turns on]

[For cross-examination: every question is closed. For witness prep: draw out the witness's own recollection in their words, consistent with PD 57AC.]

---

## Document list

| # | Reference | Description | Used in section |
|---|---|---|---|

## Marker discipline

Use inline while building and reviewing:
- `[VERIFY: factual assertion]` — any fact not confirmed against the record
- `[UNCERTAIN: legal proposition]` — any legal point (rule, deadline, scope-of-questioning limit) not confirmed against current authority
- `[CITE NEEDED: specific cite]` — record or authority cite pending

## Notes for the advocate / solicitor

- [Anything the outline doesn't capture — witness demeanour notes, strategic calls to make in the moment]
- [PD 57AC compliance checklist items if applicable]

---

**Privileged / work-product material.** This outline is built from case materials and inherits their LPP status (litigation privilege). Keep it in the privileged-materials folder, mark it appropriately, and make any distribution decision (co-counsel, client, experts) deliberately — distribution outside the privilege circle can waive protection.

**Cite check any authority relied on.** Rule citations (CPR, PD 57AC, practice guides) and any case law pulled into the outline were generated by an AI model. Verify each against the uk-legal MCP, BAILII, or legislation.gov.uk — confirm currency and scope before relying on them. Source tags on each citation show where the cite came from; `verify` tags carry higher fabrication risk.
```

## What this skill does not do

- Draft PD 57AC-compliant witness statements. Those must be in the witness's own words. This skill helps prepare the witness to give them; it does not give the evidence.
- Take the examination. The outline is a map; the advocate drives.
- Predict what the witness will say. It prepares for likely answers; witnesses surprise.
- Decide what to ask on the fly. Follow-ups are the advocate's judgment in the room.

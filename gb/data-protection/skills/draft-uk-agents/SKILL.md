---
name: draft-uk-agents
title: /legal-clinic-uk:draft
description: First draft of a common UK clinic document — practice-area templates (ET1 claim narratives, housing possession defences, protective injunction applications, demand letters, asylum statements of evidence), jurisdiction-aware formatting for England & Wales / Scotland / Northern Ireland, explicitly a starting point requiring student analysis and supervising solicitor/barrister review. Use when a student needs a first draft of a claim, defence, letter, petition, statement, or other clinic document.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/legal-clinic-uk/skills/draft
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: data-protection
language: en
---

# /legal-clinic-uk:draft

1. Load `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → practice-area templates, jurisdiction (E&W / Scotland / NI), local rules, supervision style.
2. Use the workflow below.
3. Match doc type to template. Gather facts from case notes — flag missing, never guess.
4. Apply jurisdiction formatting per CPR, tribunal rules, or Scottish / NI procedure. Draft with `[FACT NEEDED]`, `[VERIFY]`, `[UNCERTAIN]` flags inline.
5. Output with prominent AI-assisted label, student review checklist, supervision routing.

```
/legal-clinic-uk:draft possession-defence
```

```
/legal-clinic-uk:draft et1-narrative
```

```
/legal-clinic-uk:draft asylum-statement
```

---

# Draft: First-Draft Document Generation

## Purpose

Students spend enormous time on first drafts of documents where the educational value is in the analysis and strategy, not in formatting a claim form or writing the correct tribunal header. This skill produces the first draft from case notes and practice-area templates so the student's time goes to the thinking.

**Every draft is explicitly a starting point.** Not final work product. The student analyses, revises, and the supervising solicitor or barrister reviews before anything goes anywhere.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → practice areas, practice-area templates, jurisdiction (E&W / Scotland / NI and specific court/tribunal), supervision style.

Case notes or intake summary for the facts.

## Pedagogy check

Read the supervisor guide for this practice area at `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/guides/<practice-area>.md`. Check the `pedagogy_posture` setting:

- **`guide` (default):** Produce the structure and the checklist. Ask the student to draft each section. Give feedback on their draft (register, reading level, required elements, what they missed). Offer to fill a section only when the student has tried once.
- **`assist`:** Produce the work product. Flag items for student review. The student edits and learns by reviewing.
- **`teach`:** Don't produce the work product. Ask the student to draft it. Give feedback. Ask leading questions when they're stuck. Only show a model paragraph after two attempts.

If no guide exists, use `guide`. Whatever the posture, the output always includes: "**Pedagogy mode: [assist/guide/teach]** — set by your supervisor's guide."

**Jurisdiction assumption.** The draft assumes the jurisdiction, court, and local rules set in CLAUDE.md. Procedure, form formats, and substantive rules vary materially between E&W, Scotland, and Northern Ireland, and between different courts and tribunals within each jurisdiction. If the matter is in a different court, tribunal, or jurisdiction, confirm with your supervisor before relying on any format, deadline, or argument in the draft.

## Workflow

### Step 1: Which document?

Match the request to the clinic's template set. Common set by practice area:

| Practice area | Documents |
|---|---|
| **Housing (E&W)** | Possession defence (Section 21 / Section 8), disrepair claim / counterclaim, deposit protection letter (Housing Act 2004), demand letter, housing possession court application |
| **Employment (E&W)** | ET1 claim narrative (unfair dismissal, discrimination, redundancy, wages), ET3 response narrative, grievance letter, appeal against dismissal letter, subject access request |
| **Immigration / Asylum** | Statement of evidence / personal statement for asylum claim, representations to the Home Office, First-tier Tribunal (IAC) appeal skeleton argument, subject access request to UKVI, GDPR subject access request |
| **Family (E&W)** | Non-molestation order application, occupation order application (FL401), child arrangements statement (C100), financial statement (Form E), position statement for hearing |
| **Consumer / Debt (E&W)** | Section 77/78 request (Consumer Credit Act 1974), FCA complaint letter, response to county court claim, set-aside of default judgment application, response to statutory demand |
| **Benefits** | Mandatory reconsideration request, First-tier Tribunal (SSCS) appeal grounds, DWP correspondence |
| **General** | Letter before action, subject access request, formal complaint to regulator |

If the requested document isn't in the template set: "The clinic's templates don't include [X]. I can attempt a draft from general principles, but flag this heavily — it hasn't been tuned for your practice area or jurisdiction. Ask [Supervisor] if there's an existing template."

### Step 2: Gather the facts

Read the intake summary or case notes. For each fact the document needs: do we have it?

| Document needs | Have? | Source |
|---|---|---|
| [fact] | ✓ / ✗ | [intake / client doc / need to get] |

Missing required facts → don't guess. Mark them: `[FACT NEEDED: client's entry date — get from BRP or ask client]`.

### Step 3: Apply jurisdiction

Per `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` jurisdiction:

**England & Wales:**
- **CPR formatting:** claim form caption, statement of truth format, Part 7 or Part 8 route, Practice Direction requirements
- **Employment Tribunal:** ET1 / ET3 format per Employment Tribunal (Constitution and Rules of Procedure) Regulations 2013 (Schedule 1); online submission via MyHMCTS
- **First-tier Tribunal (Immigration):** Form IAFT-5 / online portal; Practice Directions and Practice Statements for the IAC
- **County Court:** Form N1 (claim), N9B (defence), N180 (directions questionnaire) — small claims, fast track, multi-track allocation per CPR Part 26
- If local court rules or practice directions were ingested at cold-start, use them. If not: `[VERIFY FORMAT: rules not loaded — confirm against current court/tribunal practice directions]`

**Scotland:**
- Sheriff Court: initial writ or summons format; Summary Cause or Simple Procedure as applicable; Sheriff Appeal Court
- Employment Tribunal Scotland: same UK-wide ET rules, but ACAS early conciliation still applies
- Note: Scots law and Scottish civil procedure differ materially from E&W in housing (private residential tenancy legislation), family (Children (Scotland) Act 1995), and property law

**Northern Ireland:**
- County Court NI: NI Rules of Court; NI Legal Aid has separate thresholds from Legal Aid England & Wales
- Industrial Tribunal / Fair Employment Tribunal for employment matters

### Step 4: Draft

Use the practice-area template. Fill what can be filled from facts. Leave placeholders explicit — never fill with plausible-sounding invention.

**Everywhere the draft makes a legal assertion:** that assertion is a hypothesis the student verifies, not a conclusion the draft guarantees. Mark accordingly.

### Step 5: Flag uncertainty

Three kinds of flags, in-line:

- `[FACT NEEDED: ...]` — the document needs a fact the case notes don't have
- `[VERIFY: ...]` — a legal or factual assertion that needs checking before this is filed — use OSCOLA-formatted citation starting points where possible
- `[UNCERTAIN: ...]` — the skill is genuinely unsure and says so rather than guessing

### Step 6: Supervision routing

Filing a document with a court or tribunal is a consequential action. The gate is the supervision workflow in `## Supervision style` in `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md`. Court and tribunal filings always route through the supervising solicitor or barrister before filing, regardless of the supervision-style choice. `[SRA-CODE]` `[BSB-HANDBOOK]`

Per `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` supervision style:
- **Formal queue:** draft goes to queue, student sees "queued for [Supervisor]"
- **Configurable flags:** if this document type is a flag trigger (tribunal/court filings usually are), output includes "CHECK WITH [SUPERVISOR] BEFORE FILING"
- **Lighter-touch:** standard safeguard label, no additional gate — but court and tribunal filings still go to the supervisor before filing

## Output

```markdown
═══════════════════════════════════════════════════════════════════════
  AI-ASSISTED DRAFT — REQUIRES STUDENT ANALYSIS AND
  SUPERVISING SOLICITOR/BARRISTER REVIEW
  This is a starting point, not final work product.
  Students are not solicitors or barristers. Every [VERIFY] and
  [FACT NEEDED] flag must be resolved before filing.
═══════════════════════════════════════════════════════════════════════

[The document — in the practice-area template format, jurisdiction-aware,
with flags inline. OSCOLA-formatted citation starts where applicable.]

═══════════════════════════════════════════════════════════════════════

## Student review checklist

Before showing this to [Supervisor]:

- [ ] Read the whole thing. Does it say what you want it to say?
- [ ] Every fact: is it accurate per the client's actual documents, not just the intake notes?
- [ ] Every [VERIFY] flag: resolved with research (Westlaw UK / LexisNexis UK / BAILII / legislation.gov.uk) or struck
- [ ] Every [FACT NEEDED] flag: filled with verified information or the section removed
- [ ] Legal theory: is this the right argument? Are there better ones? (That's your analysis, not the draft's.)
- [ ] Jurisdiction: form format, service requirements, court/tribunal rules correct per current practice directions — `[CPR-RULE]` as applicable
- [ ] OSCOLA citations checked: every case and statute cited in the draft must be verified before it appears in a filed document
- [ ] [Supervision step per CLAUDE.md style]

## What this draft does NOT do

- It does not decide strategy. The draft follows the most common approach for this document type — you decide if that's right for this client.
- It does not verify its own legal assertions. Every legal conclusion above is a hypothesis until you research it.
- It does not file itself. [Supervisor] reviews, you file per clinic procedure.

---

**Before this leaves the clinic.** This is a student draft for supervising solicitor/barrister review, not a final letter, filing, or form. Filing it with a court or tribunal, or sending it to a client or opposing party, has legal consequences for the client. A licensed supervising solicitor or barrister reviews, edits, and signs off before it leaves the clinic. Strip the AI-assisted draft header only after that sign-off. Do not file or send this draft without supervisor approval.

*SRA Code of Conduct 2019 and BSB Handbook: supervision requirements apply to all work produced by or under the direction of a solicitor or barrister. This draft is designed to be supervised and verified — it is not designed to be trusted without that.* `[SRA-CODE]` `[BSB-HANDBOOK]`
```

## What this skill does NOT do

- **Produce final work product.** First draft only. Student revises, supervisor reviews.
- **Guess at missing facts.** Flags them for the student to get.
- **Decide the legal theory.** Uses the common approach; the student decides if it's the right one for this case.
- **Replace jurisdiction-specific research.** Applies ingested local rules; flags where rules weren't ingested or might have changed.
- **File the document.** Drafting and filing are separate steps. The supervisor approves; the student or clinic files per procedure.

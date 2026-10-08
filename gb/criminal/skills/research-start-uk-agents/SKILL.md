---
name: research-start-uk-agents
title: /legal-clinic-uk:research-start
description: Research roadmap for a UK legal issue — statutes to check on legislation.gov.uk, case law areas to investigate on BAILII, tribunal guidance, OSCOLA-formatted citation starting points. Leads and frameworks, NOT verified legal authority; students check everything via Westlaw UK / LexisNexis UK / BAILII / legislation.gov.uk. Use when a student asks where to start researching, wants a research roadmap for an issue, or needs gaps identified in existing research.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/legal-clinic-uk/skills/research-start
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: criminal
language: en
---

# /legal-clinic-uk:research-start

1. Load `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → jurisdiction, practice area.
2. Use the workflow below.
3. Frame the issue specifically. Build roadmap: statutory starting points (unverified, OSCOLA format), case law areas (not cases), secondary sources, search terms for Westlaw UK / LexisNexis UK / BAILII.
4. If student has existing research uploaded: synthesise and identify gaps.
5. Output with prominent "leads not authority" header. Everything is a starting point the student verifies.

```
/legal-clinic-uk:research-start "Section 21 notice validity requirements Deregulation Act 2015"
```

```
/legal-clinic-uk:research-start "ET unfair dismissal qualifying period exception"
```

---

# Research Start: Roadmap, Not Research

## Purpose

UK legal research is essential to clinical education. But the initial phase — figuring out *what* to research, finding the right Act, understanding the framework — is often the most time-consuming and least educational part. Students spend hours finding the starting point before they can do the actual research.

This skill produces the starting point: statutes to check on legislation.gov.uk, case law areas to investigate on BAILII or Westlaw UK, OSCOLA-formatted citation starts, search terms. **None of it is verified. None of it is authoritative. All of it is a lead for the student to run down.**

**This is a pedagogical safeguard, not just an ethical one.** Students still learn to research. They just start from a better place.

**OSCOLA throughout.** All citation starts use Oxford University Standard for the Citation of Legal Authorities (OSCOLA) format — the UK standard for legal writing. The student confirms accuracy and format before using any citation in a finalised document.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → jurisdiction (E&W / Scotland / NI), practice areas.

## Workflow

### Step 0: Seed documents first

**Before building the roadmap, read the clinic's own seed documents.** The supervising solicitor or barrister uploaded them at cold-start (handbook, filing guides, tribunal/court rules, intake forms, example case files, prior memos) — they are pre-vetted, jurisdiction-specific, and will beat any BAILII query on the first 20 minutes of a student's research.

1. Read `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → `## Seed documents`. Identify any item whose purpose or filename matches the research area.
2. For each match, surface it as a **Seed documents to read first** block at the top of the roadmap output. Name the file, say why it matters for this specific question.
3. If no seed documents match: "No clinic seed documents match this issue — proceeding straight to primary sources."
4. If the clinic has the `LIMITED DATA` flag set: "Clinic has fewer than 10 seed docs — lean harder on primary sources and flag what's missing for your supervisor."

The roadmap still covers statutes, case law areas, secondary sources, and search terms — seed docs are the first lead, not a replacement.

### Step 1: Frame the issue

What's the research question? Be specific. Not "unfair dismissal" — "Does the claimant have qualifying service for an unfair dismissal claim under the Employment Rights Act 1996, and if so, does the automatically unfair category (whistleblowing / trade union activity / pregnancy) apply so qualifying period is irrelevant?"

If the question is too broad, narrow it with the student: "That's three research questions. Let's take them one at a time. Which first?"

### Step 2: Build the roadmap

**Statutory starting points:**
List statutes *likely* relevant. State explicitly these are likely, not confirmed. Use OSCOLA format.

> **Likely relevant statutes** (UNVERIFIED — confirm currency and commencement on legislation.gov.uk):
> - Employment Rights Act 1996, ss 94–107 (unfair dismissal generally), s 108 (qualifying period), s 99 (pregnancy — no qualifying period), s 103A (protected disclosure — no qualifying period) `[model knowledge — verify]`
> - Employment Tribunals Act 1996 (ET jurisdiction)
> - OSCOLA form: Employment Rights Act 1996, s 94.
> - `[VERIFY each citation is current — check legislation.gov.uk for amendments; some ERA 1996 provisions amended by Employment Relations Act 1999, Employment Act 2002, Enterprise and Regulatory Reform Act 2013, etc.]`

**Case law areas to investigate:**
Not cases — *areas*. The student finds the cases.

> **Case law areas:**
> - UKSC / Court of Appeal / EAT authority on qualifying service calculation
> - EAT guidance on automatically unfair dismissal categories — what constitutes a protected disclosure (whistleblowing) under ERA 1996 s 43B
> - Cases on effective date of termination vs actual dismissal date for limitation purposes
> - Tribunal decisions on related issues in this jurisdiction

**Regulatory / administrative sources:**
> **Administrative / regulatory sources:**
> - ACAS Code of Practice on Disciplinary and Grievance Procedures (relevant to fairness assessment)
> - ACAS Guide on early conciliation — certificate timing and its effect on ET limitation period
> - Employment Tribunal Practice Directions and Presidential Guidance (England and Wales) or Presidential Guidance (Scotland)
> - Employment Rights Act 1996 (as amended): check legislation.gov.uk for current version with all amendments in force

**Secondary sources:**
> **Secondary sources (for framework, not citation):**
> - Harvey on Industrial Relations and Employment Law (standard UK practitioner text)
> - Blackstone's Employment Law Practice
> - IDS Employment Law Handbook
> - CIPD and ACAS guidance for procedural context
> - EAT website for recent tribunal directions

**Search terms:**
> **Search terms to try:**
> - Westlaw UK: `Employment Rights Act 1996 s 108 qualifying period AND unfair dismissal AND [specific issue]`
> - LexisNexis UK: `unfair dismissal AND "automatically unfair" AND qualifying period`
> - BAILII: `Employment Appeal Tribunal AND "qualifying period" AND [specific claim type]`
> - legislation.gov.uk: search "Employment Rights Act 1996" → view current version → Section 108
> - Refine based on what comes back — these are starting queries

### Step 3: Jurisdiction note

**England & Wales:** ERA 1996 applies; Employment Tribunals (E&W) are governed by Employment Tribunal (Constitution and Rules of Procedure) Regulations 2013 (Sch 1). `[model knowledge — verify]`

**Scotland:** Same substantive ERA 1996 law; separate ET Scotland system but same rules. Note: separate procedural provisions may apply for cross-border matters. Prescription and Limitation (Scotland) Act 1973 is the main limitation regime for Scottish civil claims (not Limitation Act 1980). `[model knowledge — verify]`

**Northern Ireland:** Employment Rights (Northern Ireland) Order 1996 (not ERA 1996) governs unfair dismissal in NI. Industrial Tribunal NI (not ET). Separate rules from Great Britain. `[UNCERTAIN: some recent NI employment law changes may have diverged further — verify against NIJAC and NILSC sources]` `[model knowledge — verify]`

### Step 4: Flag what's uncertain

> `[UNCERTAIN: whether the claim involves an automatically unfair category — this determines whether qualifying period matters at all. The factual basis needs to be confirmed before the research framework is finalised.]`

Uncertainty is stated, not hidden.

> **No silent supplement.** This skill produces leads, not verified authority — by design, students run the citations down themselves. But if a query to a configured research tool (uk-legal MCP, BAILII) returns few or no results for a specific rule or case, say so and stop. Do NOT manufacture citations from web search or model knowledge to fill a thin result set without asking.

### Step 5: Synthesise uploaded research (if any)

If the student has already done some research and uploads it: read it, identify what's covered and what's missing.

> **From your research so far:**
> - You have: [summary of what's covered]
> - Gap: [what the roadmap above suggests that you haven't found yet]
> - `[VERIFY: the case you cited — confirm it is good law — check whether any later EAT or Court of Appeal authority has limited or overruled it]`

## Output

```markdown
═══════════════════════════════════════════════════════════════════════
  RESEARCH ROADMAP — LEADS, NOT AUTHORITY
  Nothing below is a verified citation. Every statute, every case area,
  every search term is a starting point for YOUR research. You verify
  currency, applicability, and accuracy via legislation.gov.uk,
  BAILII, Westlaw UK, or LexisNexis UK. You find the actual cases.
  OSCOLA citation starts are provided as a format guide — confirm
  accuracy before any of them appear in a document or filing.
═══════════════════════════════════════════════════════════════════════

# Research Roadmap: [Issue]

**Jurisdiction:** [E&W / Scotland / NI] | **Practice area:** [area]

## Seed documents to read first

[Per Step 0. List any clinic seed docs that match the issue. If none matched: "No clinic seed documents match this issue — proceeding to primary sources."]

## Statutory starting points (UNVERIFIED — confirm on legislation.gov.uk)

[list with VERIFY flags and OSCOLA citation starts]

## Case law areas to investigate

[areas, not cases — student finds the actual cases on BAILII / Westlaw UK]

## Administrative / regulatory sources

[ACAS codes, practice directions, tribunal guidance, GOV.UK]

## Secondary sources (for framework, not citation)

[Harvey, Blackstone's, IDS, practitioner texts]

## Search terms

**Westlaw UK:** [queries]
**LexisNexis UK:** [queries]
**BAILII:** [queries]
**legislation.gov.uk:** [direct navigation path]

## Jurisdiction note

[Differences between E&W / Scotland / NI where they matter for this issue]

## Uncertainty flags

[Everywhere the roadmap is genuinely unsure]

---

## What to do with this

1. Start with a secondary source (Harvey / Blackstone's) to get the framework
2. Find and read the primary statutes on legislation.gov.uk — confirm the OSCOLA citations above are current and in force
3. Run the BAILII and Westlaw UK searches, find the leading cases
4. Citator-check every case before relying on it (Westlaw UK case analysis / LexisNexis UK)
5. Come back and run `/legal-clinic-uk:memo` to scaffold your analysis once you have the rule
6. Use OSCOLA format throughout — your supervisor expects it

## What this roadmap does NOT do

- **It does not give you verified authority.** Every cite above is a lead to check, not an authority to rely on.
- **It does not do the research.** You do the research. This gets you to the starting line faster.
- **It does not replace Westlaw UK or LexisNexis UK.** Those have the actual cases and citator status. This tells you where to point them.

---

**Cite verification — required before use.** Citations above were generated by an AI model and have not been verified. Before relying on any case, statute, or rule — or including it in client work — run it through Westlaw UK, LexisNexis UK, BAILII, or legislation.gov.uk for accuracy and current-law status. All citations should be formatted to OSCOLA standard before appearing in any finalised document. Flag unverified citations to your supervisor.
```

## What this skill does NOT do

- **Provide verified legal authority.** Explicitly, by design. The student verifies every cite before using it.
- **Replace legal research.** Accelerates the "where do I start" phase; the research itself is still the student's.
- **Guarantee the roadmap is complete.** It's a starting set of leads. The research may reveal sources the roadmap missed — that's fine, that's research.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`.

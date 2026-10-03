---
name: justinian-law-school-brief-summarizer
title: Justinian — Law School Case Brief Summarizer
description: Use when a law student or practitioner needs a structured case brief for any court decision. Produces a standard law-school brief covering procedural posture, facts, issue, holding, rule, reasoning, concurrences/dissents, and subsequent treatment. Adapts depth to the reader's level (1L, 2L/3L, bar prep, or practitioner). Multi-jurisdictional; particularly useful for common-law cases from DIFC, ADGM, UK, and US courts, and civil-law decisions from Lebanese, UAE, KSA, Egyptian, or French courts.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/justinian/justinian-law-school-brief-summarizer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Justinian — Law School Case Brief Summarizer

## When to use this

Use this skill when a student, practitioner, or researcher:

- Needs to brief a case for class, exam revision, or file preparation
- Wants to extract the rule and holding from a decision quickly
- Is building a course outline and needs well-structured case summaries for each topic
- Is preparing for an oral argument and wants the opposing precedent dissected
- Works across common-law and civil-law courts and needs a consistent brief format

This skill works from a case name + citation (it will synthesize from known cases), or from the full text of a decision pasted in.

## Brief structure

Every output follows this eight-section format. No section is optional; omit only if the court genuinely did not address that component.

### 1. Case name + citation

Full name and official citation. For MENA cases: provide Arabic title where known alongside transliteration. For DIFC/ADGM: include the neutral citation format used by those courts.

### 2. Procedural posture

Where does this case sit in the litigation tree?

- First instance / trial court
- Intermediate appellate court
- Final appellate court (Court of Cassation, Court of Appeal, Supreme Court)
- Specialized court (DIFC Court of First Instance, DIFC Court of Appeal, ADGM Court, etc.)
- Arbitral tribunal (award, not judgment)

State: who brought the appeal / cassation petition, and on what ground (error of law, error of fact, procedural).

### 3. Facts (relevant only)

State only facts that the court used or should have used in its analysis. Do not summarize background that played no role in the decision. Use short, precise sentences. Distinguish:

- Undisputed facts
- Disputed facts resolved by the court
- Facts the court assumed arguendo

### 4. Issue

One sentence per legal issue decided. Format:

> "Whether [specific rule/element] applies when [specific facts]."

For multi-issue decisions, number each issue. Lead with the dispositive issue.

### 5. Holding

Short statement of the court's answer to each issue:

> "Yes — the clause is enforceable because [key element met]."
> "No — the claim fails at [specific element]."

Include the vote count and alignment for appellate decisions.

### 6. Rule

The legal rule applied or established by this case. State:

- The pre-existing rule the court applied, OR
- The new rule the court announced, OR
- The test synthesized from earlier cases

Cite to the statutory provision, code article, or prior leading case.

### 7. Reasoning

The court's logic from rule to outcome. Structure as:

1. How the court characterized the facts against each rule element
2. How the court resolved ambiguities or competing authorities
3. Policy rationale (if the court provided one)
4. What the court expressly excluded from its holding (scope limitations)

For civil-law courts (Lebanon, UAE onshore, KSA, Egypt, France): focus on code interpretation methodology — literal vs teleological. For common-law courts (DIFC, ADGM, UK, US): note the ratio decidendi vs obiter dictum distinction.

### 8. Concurrences and dissents

Summarize every concurrence and dissent that:

- Announces a distinct rule or test
- Has subsequently been adopted (a dissent that became majority law)
- Creates an important ambiguity about the majority rule's scope

Note: "No concurrences or dissents filed" if the decision is unanimous and no opinions are noted separately.

### Notes: subsequent treatment and key citing cases

- Has this decision been overruled, distinguished, or affirmed on appeal?
- What are the most cited follow-on decisions?
- For MENA cases: has the rule been codified in statute since the decision?

## Depth calibration by reader level

| Level | Focus | Length |
|-------|-------|--------|
| **1L** | Full context; explain procedural posture; explain legal terms; highlight "why this matters" | Long (500–700 words) |
| **2L/3L** | Terse; assume procedural + doctrinal basics; emphasize rule development and dissent | Medium (250–400 words) |
| **Bar prep** | Rule-first; bold the rule statement; hyperlink to outline element | Short (150–250 words) |
| **Practitioner** | Implication-first; flag differences from current statute; note circuit splits or conflicting MENA authority | Medium-short (200–350 words) |

Ask the user for their level if not specified; default to 2L/3L depth.

## Civil-law briefing adaptations

Civil-law judgments from Lebanon, France, Egypt, UAE onshore, or KSA courts often:

- Do not contain discursive reasoning in the way common-law judgments do
- Cite code articles without elaborating the court's interpretation
- Are short in form but dense in legal significance

For these decisions:

- In the "Reasoning" section, supplement the court's stated rationale with the dominant academic commentary (doctrine) explaining the provision's meaning, if known.
- Flag when the court has simply cited a code article without reasoning — this is significant: it shows the court treated the outcome as obvious under the text.
- Note Arabic-language originals where the English version is a translation.

## Quality checks

Before delivering the brief, verify:

- Issue sentence is a binary question (answerable yes/no or yes/no/depends)
- Holding directly answers the issue
- Rule is stated in general terms (applicable beyond this case), not fact-specific
- Reasoning section does not re-argue what the court said — it accurately describes the court's logic
- Citations are complete and correctly formatted for the jurisdiction

## Do not

- Do not fabricate citations, case names, or holdings for cases not in the knowledge base — flag uncertainty explicitly.
- Do not convert the "Reasoning" section into personal legal analysis; this is the court's reasoning, not advice.
- Do not omit procedural posture — students frequently misapply holdings by ignoring the procedural context.

## Related skills

- [[justinian-irac-coach]] — use the rule from this brief as input to IRAC practice
- [[justinian-legal-essay-grader]] — assess how well a student has used a briefed case in an essay
- [[justinian-outline-builder]] — slot this brief into a course outline under the relevant topic
- [[research-precedent-finder]] — find additional citing cases once the brief identifies the rule
- [[justinian-flashcards-from-statute]] — convert the rule statement into flash-card format

---
name: draft-memo-of-law-sboghossian
title: Memo of Law (Legal Research Memorandum)
description: Use when drafting an internal legal memorandum (research memo) analyzing a legal question for a supervising attorney, client, or internal team. Covers the CRAC/IRAC structure, question presented, brief answer, statement of facts, discussion with legal authority, counter-arguments, and conclusion. Handles citation conventions for MENA (UAE, KSA, LB, EG), DIFC/ADGM, EU, UK, and US jurisdictions. Triggers on "memo of law", "legal memo", "research memo", "internal memo", "analyze this legal question", or "what does the law say about" requests where a structured written output is expected.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-memo-of-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Memo of Law (Legal Research Memorandum)

## When to use this

A memo of law is an internal document — not addressed to a client for reliance, and not carrying formal opinion-letter weight. Use it when:
- A supervising attorney asks for analysis of a legal question before deciding on strategy
- A client's in-house team needs a clear written summary of the law on an issue
- You are building a record of legal analysis for a transaction or litigation
- Research needs to be shared across a team in a structured, citable format

For formal opinions that external parties may rely upon at closing or in regulatory proceedings, use [[draft-legal-opinion]] instead.

## Structure (CRAC / IRAC)

The memo follows CRAC (Conclusion — Rule — Application — Conclusion restated) or IRAC (Issue — Rule — Application — Conclusion). Both are valid; CRAC is preferred in practice because it puts the bottom line first.

### 1. Heading block

```
MEMORANDUM

TO:       [Supervising attorney / client / matter team]
FROM:     [Drafting attorney / team]
DATE:     [Date of memo]
RE:       [Matter name / number] — [Concise statement of the issue]
SUBJECT:  [Optional — if different from RE]
```

### 2. Question(s) presented

One or two sentences per question. Must be jurisdiction-specific and fact-specific — generic questions produce useless answers.

Formula: "Under [applicable law / jurisdiction], whether [legal issue], where [key facts that affect the outcome]."

Example: "Under the DIFC Contract Law, whether a liquidated-damages clause providing for AED 50,000 per day of delay is enforceable as written, where the actual damage from delay is unquantifiable at the time of contracting."

If there are multiple issues, number each question separately. The memo addresses them in the same order.

### 3. Brief answer

One paragraph, bottom-line up front. Answer each question presented with a clear "Yes," "No," or "Probably yes/no/depends," followed by a two-to-four sentence summary of the reasoning. This section is often read alone; it must stand on its own.

The brief answer is not the full analysis — it is the executive summary. Write it last.

### 4. Statement of facts

Present only the facts relevant to the legal analysis. Neutral tone — do not advocate. Present them:
- Chronologically, or
- Thematically (grouped by issue, if multiple issues)

Include: the parties, the contract or relationship, the key events, and the specific facts that affect the legal analysis.

Exclude: background that has no legal relevance; advocacy characterization of facts.

Flag facts that are disputed: "According to [Party], X occurred. [Other Party] denies X and asserts Y."

Flag facts you do not know and need: "It is not confirmed whether [fact]. The analysis below assumes [assumption] and notes how the result would change if [alternative fact] is true."

### 5. Discussion / Analysis

This is the core of the memo. Organize by issue (matching the questions presented). For each issue:

#### 5a. Applicable law
- Identify the governing law: which jurisdiction's law applies? (Express choice of law, or conflict-of-laws analysis)
- Identify the legal framework: statute, regulation, common-law rule, or equitable principle
- Cite the primary authority precisely
- If there are multiple applicable sources (e.g., a statute and implementing regulation and a judicial decision), synthesize them

#### 5b. Rule statement
State the legal rule applicable to this issue. Write it as a general principle — applicable to any set of facts that matches the elements. Be specific: cite article/section numbers, the key words from the statute, and the authoritative interpretation if there is one.

#### 5c. Application to facts
Apply the rule to the specific facts. Walk through each element of the rule and determine whether the facts satisfy it. Do not skip elements that cut against your conclusion — acknowledge them and explain why they do not control, or flag them as genuine risks.

#### 5d. Counter-arguments
Identify the strongest argument for the other side. Assess its merits honestly. A one-sided memo that suppresses counter-arguments is professionally unreliable. Supervisors and courts will identify the same weaknesses; better to surface them first.

#### 5e. Conclusion per issue
Re-state your conclusion in one or two sentences. Note any material assumptions, open factual questions, or jurisdictional variables that affect the confidence of the conclusion.

### 6. Conclusion

A one-paragraph summary of all conclusions, cross-referencing the questions presented. Note the two or three most significant open questions or risks.

Offer the next step: "If [further fact X] can be confirmed, the analysis in Section 5b would change as follows..." or "We recommend obtaining a confirmatory legal opinion from [local counsel] before proceeding."

## Citation conventions

Accurate, verifiable citations are the only kind. Do not generate plausible-looking citations to laws or cases that may not exist.

| Jurisdiction | Citation format |
|---|---|
| **US** | Bluebook — statutes: 15 U.S.C. § 78j(b); cases: 547 U.S. 45 (2006); regulations: 17 C.F.R. § 240.10b-5 |
| **UK** | OSCOLA — cases: *Caparo Industries plc v Dickman* [1990] 2 AC 605 (HL); statutes: Companies Act 2006, s 172 |
| **DIFC** | DIFC Courts citation guide — DIFC Law No. X of Year, Article Y; case citations per DIFC Courts Practice Direction |
| **ADGM** | ADGM — ADGM Companies Regulations 2015, reg 123; ADGM Courts decisions cited by case number |
| **UAE federal** | Federal Law / Decree-Law No. X of Year, Article Y; UAE Gazette reference; name the law in full on first reference |
| **KSA** | Royal Decree No. M/X; date (Hijri and Gregorian); Official Gazette reference; transliterate Arabic title |
| **LB** | Legislative Decree No. X / Year; Official Gazette no. Y, date; cite Code of Obligations Articles directly |
| **EG** | Law No. X of Year; Official Gazette reference |
| **EU** | ECLI identifier for CJEU; regulation: Regulation (EU) No X/Year, Art. Y; directive: Directive 20YY/X/EU, Art. Y |
| **FR** | Code Civil, Art. X; Code de Commerce, Art. Y; Cass. civ. 1re, [date], [no. de pourvoi] |

### MENA-specific citation guidance
- MENA laws are often numbered in Hijri (Islamic calendar) and/or Gregorian — use both when citing Saudi decrees
- Arabic original text controls for UAE, KSA, LB, EG onshore laws — note if only an English translation was consulted
- Commercial court decisions in UAE and KSA are increasingly published but not comprehensively accessible; note the source and caveat accordingly

Always pair research with [[research-precedent-finder]] and verify citations with [[output-citation-mena-conventions]] before finalizing.

## Tone and length guidelines

- **Tone**: objective, precise, analytical — not advocative (that is for briefs, not memos)
- **Length**: as long as the issues require, but no longer. A single-issue memo may be 3-5 pages. A multi-issue transactional memo may be 15-20 pages. Do not pad.
- **Headings**: use clear issue-based headings; aids navigation and reference
- **Active voice**: "The Court held..." not "It was held by the Court..."
- **Plain language**: never use Latin when English (or Arabic) works better; jargon is acceptable when precise but must be defined

## Limits

- A memo is only as reliable as the legal research underlying it. Verify every statutory reference against the official text.
- If the applicable law has changed recently, flag this and note the effective date
- A memo is not a legal opinion — it does not carry the formal reliance weight of an opinion letter and does not create client-counsel reliance in the same way (but it can be disclosed in litigation as work product — mark accordingly)

## Related skills

- [[draft-legal-opinion]]
- [[output-irac-structure]]
- [[research-precedent-finder]]
- [[output-citation-mena-conventions]]

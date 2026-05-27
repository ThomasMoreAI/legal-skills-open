---
name: legal-memorandum
title: Legal Memorandum
description: Drafts objective internal legal memoranda using the CREAC method with structured header, questions presented, brief answers, statement of facts, analysis, and strategic recommendations. Use when drafting legal memos, research memoranda, pre-trial analysis, or any objective internal legal analysis document.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/legal-memorandum
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal Memorandum

Drafts an objective, internally focused legal memorandum analyzing specific legal questions with reasoned conclusions and strategic recommendations.

## Prerequisites

Gather before drafting:

- **Legal question(s)** — specific issues requiring analysis
- **Relevant facts** — documents, depositions, evidence, or client narrative
- **Jurisdiction** — controlling state/federal law
- **Audience** — attorney (doctrinal depth) or client (practical emphasis)
- **Known authority** — statutes, regulations, key case law

## Quick Start

1. Draft header with DATE, TO, FROM, RE (RE must identify the legal issue, not just the case name)
2. Frame 1–3 questions in Under-Does-When format
3. Provide brief yes/no answers with controlling rule and key facts
4. State facts objectively in chronological or topical order
5. Analyze each issue using CREAC
6. Conclude with direct answers, strategic recommendations, and next steps

## Output Structure

### 1. Header

Standard memo header: DATE, TO, FROM, RE. The RE line must identify the specific legal issue (e.g., "Likelihood of Success on Summary Judgment — Causation in Doe v. Metro Transit"). Include matter/case reference number if available.

### 2. Questions Presented

Draft 1–3 questions using **Under-Does-When** format:

- **Under** — relevant law, statute, or rule
- **Does/Is/Can** — legal conclusion sought
- **When** — key facts driving the analysis

Frame for yes/no or short definitive answers. Prioritize by importance to client objectives. No conclusory or leading language.

### 3. Brief Answer

For each question:

- Open with **Yes**, **No**, or **Probably [yes/no]**
- 2–3 sentences of critical reasoning
- Reference controlling rule and dispositive facts

### 4. Statement of Facts

- **Organization**: chronological (transactions/procedural) or topical (multiple theories)
- **Scope**: legally relevant facts + necessary background only
- **Tone**: objective — no editorial commentary
- **Sourcing**: cite specific documents, depositions, exhibits parenthetically
- **Disputed facts**: flag explicitly when contested or unclear

Include a disclaimer that analysis is based on facts as presented and may change if additional facts emerge.

### 5. Analysis (CREAC)

Apply CREAC for each issue:

1. **Conclusion** — state conclusion for this issue upfront
2. **Rule** — articulate the legal rule; cite primary authority; quote key language where precision matters
3. **Explanation** — show how courts have applied the rule using factually analogous cases; explain reasoning, not just holdings
4. **Application** — apply rule to client's facts; draw direct parallels to precedent; address counterarguments; acknowledge weaknesses
5. **Conclusion** — restate conclusion for the issue

For multi-part tests, break into sub-analyses with subheadings. Cross-reference related issues.

### 6. Conclusion

- Directly answer each question presented
- Summarize key reasoning (no new arguments)
- **Strategic recommendations**: actions, risks, alternatives
- **Next steps**: deadlines, further research, litigation/negotiation strategy, information gaps

## Checks

- [ ] Use controlling jurisdiction's law; cite primary authority over secondary sources
- [ ] Distinguish unfavorable cases rather than ignoring them
- [ ] Address the strongest opposing position for each issue
- [ ] Mark any unverified citation with `[VERIFY]`
- [ ] Calibrate depth: doctrinal nuance for attorneys, practical consequences for clients
- [ ] Present both sides honestly — do not hide unfavorable facts or authority
- [ ] Recommendations are practical and actionable, not purely academic
- [ ] Note where additional research may be warranted

---
name: output-irac-structure-sboghossian
title: IRAC Structure (Issue / Rule / Application / Conclusion)
description: Use when Claude must structure legal analysis as a formal Issue/Rule/Application/Conclusion memo, opinion, or briefing note. Applies across all jurisdictions including MENA (UAE, KSA, Lebanon, Egypt), DIFC/ADGM, UK, US, and EU. Triggers on requests for legal analysis, memo of law, legal opinion, advice note, or any analytical output requiring reasoned legal argument.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/output/output-irac-structure
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# IRAC Structure (Issue / Rule / Application / Conclusion)

IRAC is the standard analytical framework for legal memos, opinions, and briefings in both common-law and civil-law traditions. It forces disciplined separation of fact, law, and analysis — the most common failure mode in AI-assisted legal work is collapsing all three into undifferentiated prose. This skill governs when and how to apply IRAC, including jurisdiction-specific adaptations.

## When to use this

Use IRAC for:
- Legal advice notes (any jurisdiction)
- Memo of law
- Contract review opinion
- Regulatory compliance analysis
- Litigation risk assessment
- In-house "should we do this?" analyses

Do **not** use IRAC for:
- Pure drafting requests → [[output-markdown-legal-doc]]
- Quick one-paragraph triage answers → BLUF + single paragraph
- Consumer-facing explanations → use plain-English persona
- Document summaries → use summary format

## The four components

### Issue

State the legal question precisely. One sentence. Identify the parties, the jurisdiction, and the legal test at stake.

> *Whether a non-compete clause restricting an employee from joining any competitor in the MENA region for 24 months post-termination is enforceable under UAE Federal Decree-Law 33/2021.*

Quality bar: the Issue statement should be so specific that a reader who doesn't know the facts can still understand exactly what is being decided.

### Rule

State the applicable legal rule(s) with full citations. Include the source and the operative elements of the test. If multiple rules apply (e.g., statute + case + regulation), present them in hierarchical order: statute first, then implementing regulation, then judicial interpretation.

> *Under UAE Federal Decree-Law 33/2021 art 10, a non-compete clause is enforceable only if it is (i) limited in scope, (ii) limited in geography, (iii) limited in time, and (iv) necessary to protect a legitimate employer interest. Cabinet Decision 1/2022 further narrowed enforcement: scope must be proportionate to the actual interest protected.*

Common error: quoting a rule without identifying what its operative elements are. The Rule section must extract the test, not just point to the statute.

### Application

Apply the rule to the specific facts. Be concrete and direct. Address each element of the test in turn. State where the facts satisfy, do not satisfy, or create uncertainty about the rule.

> *Here, "any competitor in the MENA region" fails the geography element: the MENA region spans 22 countries and is grossly disproportionate for a marketing manager whose client relationships were confined to two UAE emirates. The 24-month duration approaches the statutory ceiling; without a clear legitimate interest justification (none appears in the agreement), a UAE court would likely reduce it to 12 months under its equitable adjustment power. The "any competitor" scope likewise fails the proportionate-scope test — it would sweep in companies with whom the employee had no relationship.*

Common error: restating the facts or the rule without actually working through the analysis. The Application section must do the hard work of connecting facts to elements.

### Conclusion

State the bottom line directly. Hedge calibrated to actual uncertainty. Give a concrete recommendation where appropriate.

> *The clause as drafted is likely unenforceable as written. A UAE court would likely narrow it to 12 months and limit its geographic scope to specific Emirates or identified competitor categories. Recommendation: redraft to a 12-month restriction within the UAE, limited to direct competitors in the employee's specific product area, with an explicit statement of the protected interest.*

## Multi-issue IRAC

For complex opinions with several legal questions, run a full IRAC for each issue and present as numbered sections:

```
## Issue 1: Enforceability of the non-compete
[Issue / Rule / Application / Conclusion]

## Issue 2: Validity of the liquidated damages clause
[Issue / Rule / Application / Conclusion]

## Overall conclusion
[Integrated bottom line across all issues]
```

## CREAC variant (US litigation memos)

Conclusion-Rule-Explanation-Application-Conclusion. Used in US federal and state litigation practice where the conclusion comes first (BLUF principle). Same substance, different ordering. Trigger when the audience is US litigation counsel or when the output is a brief.

```
Conclusion (1 sentence)
Rule (cite)
Explanation (policy rationale, key cases)
Application (facts → rule)
Conclusion (restate, with recommendation)
```

## Jurisdictional adaptations

| Jurisdiction | Notes |
|---|---|
| UAE (federal) | Courts have equitable reduction power — the Application should always assess whether a court would sever and reduce rather than void outright |
| KSA | Sharia-influenced courts: Application should note proportionality and public-policy constraints under Saudi law; cite Royal Decree and any HRSD (Human Resources and Social Development) guidance |
| Lebanon | Civil-law tradition; courts follow doctrinal commentary closely — cite academic doctrine alongside statutes in the Rule section |
| Egypt | Similar to Lebanon; Cassation jurisprudence is highly persuasive |
| DIFC / ADGM | Common-law: case law is binding precedent; Application section must cite and distinguish cases, not just statutes |
| France | IRAC maps well; the Rule section should cite Code civil or Code de commerce articles; Application should cite Cour de cassation decisions |
| EU | For multi-level analysis: EU Regulation → national implementing law → regulatory guidance, in that order in the Rule section |

## Citation standard

Every rule statement in the Rule section must carry a full citation per [[output-inline-citations-with-pinpoints]]. Every case relied on in the Application section must be cited with pin-cite to the paragraph or page relied on.

## Output format for memos

Wrap in the standard partner memo format when this is a formal deliverable:

```
MEMORANDUM
TO: [Recipient]
FROM: [Author]
DATE: [Date]
RE: [Subject]

BOTTOM LINE: [One sentence]

[IRAC analysis]

SOURCES: [end-listed — see [[output-source-attribution-block]]]
```

See [[output-partner-memo-style]] for the full memo format.

## Common mistakes

- **Generic Rule statements** that don't extract the test: "The UAE labor law applies" is not a Rule.
- **Conclusion-free Application**: ending the analysis section without actually concluding on each element.
- **Over-hedged Conclusions**: "it depends on many factors" is not a conclusion — name the factors and state the likely outcome.
- **Missing alternative rules**: in MENA especially, contract choice of law may invoke a different legal system — identify the applicable system before stating the rule.
- **IRAC for simple questions**: a quick factual question ("what is the notice period under UAE law?") does not need IRAC — use BLUF.

## Related skills

- [[output-partner-memo-style]]
- [[output-inline-citations-with-pinpoints]]
- [[output-source-attribution-block]]
- [[output-markdown-legal-doc]]
- [[output-table-of-comparisons]]

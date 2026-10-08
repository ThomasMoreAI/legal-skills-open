---
name: output-creac-structure-sboghossian
title: CREAC Structure
description: Use when structuring a legal memo or analytical response using the CREAC framework (Conclusion → Rule → Explanation → Application → Conclusion). CREAC leads with the bottom line, making it the preferred structure for partner-facing and client-facing legal memos where the reader wants the answer first. Includes MENA-jurisdiction examples (UAE non-compete, DIFC contract law) and a comparison with IRAC.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/output/output-creac-structure
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# CREAC Structure

## When to use this

Use CREAC (Conclusion → Rule → Explanation → Application → Conclusion) when:
- Writing a legal memo where the reader wants the bottom line first — typically a senior lawyer, partner, or in-house client.
- Drafting a litigation memo or brief section where the argument leads with its conclusion.
- Structuring a legal AI response that analyses a specific legal question and needs a professional-quality analytical framework.

CREAC is the preferred structure for **busy audiences** who need the answer and then the reasoning to evaluate it. If the audience needs to understand the issue first before seeing the conclusion, use IRAC instead (see [[output-irac-structure]] if available).

CREAC works well for both common-law jurisdictions (US, UK, DIFC, ADGM) and civil-law jurisdictions (UAE, KSA, Lebanon, Egypt, France) — with adjustments to the Rule section (see Jurisdictional notes below).

## The CREAC pattern

### C — Conclusion (first)

State your conclusion in **one sentence**. This is the answer to the legal question. Do not hedge excessively — pick the most defensible conclusion and state it clearly.

> The non-competition clause as drafted is likely unenforceable in its current form.

### R — Rule

State the governing legal rule precisely. Include:
- The applicable statute, article, or common-law principle.
- The conditions that must be satisfied for the rule to apply.
- Any relevant threshold or limitation.

> Under UAE Federal Decree-Law No. 33 of 2021 on the Regulation of Labour Relations, a non-competition clause is enforceable only if it: (1) is limited in geographic scope; (2) is limited in duration (no longer than two years); (3) is limited to activities that compete with the employer's actual business; and (4) is necessary to protect a legitimate business interest. Cabinet Decision No. 1 of 2022 emphasizes that courts apply a proportionality test.

### E — Explanation

Explain how the rule has been applied — through cases, commentary, or regulatory guidance. This section gives the reader confidence that the Rule is correctly stated and that the Application is grounded in precedent or established practice.

> The proportionality standard has been applied consistently by UAE labour tribunals and civil courts in disputes arising from non-compete enforcement. In recent years, multiple decisions have reduced MENA-wide non-competes to individual UAE emirates, and two-year durations for non-senior employees to twelve months. The phrase "any competitor" in a non-compete has been treated as scope-disproportionate where the employer's actual business is narrower. These decisions are not published in a comprehensive official database, but the pattern is reflected in the legal literature and in MOHRE guidance.

Do **not** fabricate case citations or article numbers. If the source gave specific citations, use them. If not, stay at the level of established patterns and well-known frameworks, as in the example above.

### A — Application

Apply the rule to the specific facts. This is where the analysis earns its value. Map each element of the rule to the specific facts at hand:

> Applying the proportionality test to the clause at issue:
>
> *Geographic scope*: The clause prohibits competition "anywhere in the Middle East and North Africa." The employer's operations are concentrated in the UAE. A MENA-wide prohibition is almost certainly disproportionate for a role limited to UAE operations.
>
> *Duration*: The clause imposes a 24-month restriction. For a marketing manager (not a senior executive with access to strategic trade secrets), 24 months is at the upper boundary of what courts have upheld; 12 months is the more defensible duration.
>
> *Scope of restricted activity*: The clause prohibits working for "any competitor." The employer operates in digital legal services only. "Any competitor" would encompass unrelated legal technology companies, which is disproportionate.
>
> *Legitimate interest*: The clause does not identify the specific confidential information or client relationships it is designed to protect. Courts and MOHRE have flagged this as a drafting weakness.

### C — Conclusion (restated)

Restate the bottom line — ideally with slightly more precision than the opening conclusion, now that the reader has seen the reasoning:

> The non-competition clause as drafted will likely be struck down or substantially reduced by a UAE court on proportionality grounds. We recommend reducing the geographic scope to the UAE only, the duration to 12 months, the restricted activities to digital legal services specifically, and adding a legitimate-interest recital to strengthen enforceability. Even a revised clause carries moderate enforcement risk in UAE labour proceedings; non-compete enforcement in the UAE is fact-specific and the trend favors employees.

## CREAC vs IRAC

| Dimension | CREAC | IRAC |
|-----------|-------|------|
| Opens with | Conclusion (the answer) | Issue (the question) |
| Audience | Partner, client, busy reader who wants the answer first | Professor, student, or reader who needs to understand the question before the answer |
| Use cases | Client memos, partner-facing analysis, legal AI responses | Academic papers, some US judicial opinions, first-year law school exams |
| Reader efficiency | Higher — reader can stop reading after C + R if they trust the analysis | Lower — reader must work through to the end to get the conclusion |

For a legal AI product, CREAC is almost always the right default. Lawyers are busy; they want the answer first.

## Jurisdictional notes

### Civil-law jurisdictions (UAE, KSA, Lebanon, Egypt, France)

In the Rule section for civil-law jurisdictions:
- Cite the applicable code and article (e.g., `UAE Federal Decree-Law No. 33/2021, Art. 10`).
- The rule is usually statutory (codified), not judge-made common law.
- Judicial decisions are influential but not strictly binding (no doctrine of stare decisis).
- In the Explanation section, describe the pattern of court interpretation rather than citing specific binding precedents.

### Common-law jurisdictions (DIFC, ADGM, UK, US)

In the Rule section for common-law jurisdictions:
- Cite the applicable statute (if any) and/or the leading case(s).
- The rule may be entirely judge-made (common law).
- Judicial precedent is binding within the hierarchy; cite the highest applicable court.
- In the Explanation section, cite and distinguish specific cases.

### Hybrid jurisdictions (DIFC/ADGM alongside UAE)

A document may need to analyse both the UAE onshore law (civil law) and the DIFC/ADGM law (English common law) — for example, in a dispute where jurisdiction is unclear. Apply CREAC separately to each legal system, then compare:

> Under UAE federal law (CREAC above), the clause is likely unenforceable.
>
> Under DIFC Contract Law (which applies if the parties chose DIFC jurisdiction), the analysis differs: [second CREAC].

## Formatting rules

- Each CREAC section has a visible label (**C**, **R**, **E**, **A**, **C**) or a heading (`Conclusion`, `Rule`, `Explanation`, `Application`, `Conclusion`).
- In a formal memo, each section is a paragraph or set of paragraphs — not a bullet list.
- In a legal AI chat response, bullet points within the Application section are acceptable for clarity.
- Do not compress the Explanation section when the rule is contested or non-obvious — the reader needs to trust the rule before the application matters.

## Related skills

- [[output-executive-summary-first]] — BLUF summary that often precedes a CREAC memo
- [[output-client-letter-style]] — uses CREAC structure for the analysis body of client letters
- [[output-citation-format-bluebook]] — citation format for US CREAC memos
- [[output-citation-format-oscola]] — citation format for UK/DIFC CREAC memos

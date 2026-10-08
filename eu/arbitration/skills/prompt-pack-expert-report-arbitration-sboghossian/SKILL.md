---
name: prompt-pack-expert-report-arbitration-sboghossian
title: Expert Report (Arbitration)
description: Use when preparing the outline and structure of an expert report for international arbitration proceedings — covering the expert's qualifications, scope of instructions, methodology, data reviewed, opinions, and compliance with institutional requirements such as IBA Rules on Taking of Evidence. Applicable for financial damages, technical, industry practice, and valuation experts in arbitrations before ICC, LCIA, DIAC, ADCCAC, SIAC, and other institutions. Trigger when party-appointed expert counsel needs to structure a formal arbitration expert report.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-expert-report-arbitration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: arbitration
language: en
---

# Expert Report (Arbitration)

## When to use this

Use this skill when a party to international arbitration needs to commission and structure an expert report — typically on damages, valuation, accounting, technical matters, or industry practice. Expert evidence is central to most commercial arbitrations; the quality and structure of the expert report often determines the outcome on quantum.

The arbitration expert report differs from a litigation expert report in that:
- It must comply with the applicable arbitral rules (IBA Rules, institutional rules, or specific procedural orders)
- The overriding duty of the expert is to the arbitral tribunal, not to the appointing party
- Expert reports are typically exchanged simultaneously (not sequentially as in many court proceedings)
- Hot-tubbing (expert conferencing before the hearing) is increasingly common in international arbitration

Typical triggers:
- Counsel retaining a financial expert to opine on damages in a construction, M&A, or contract dispute
- Party appointing a technical expert to assess liability in an engineering or IT dispute
- Expert needs to prepare their report structure before data analysis begins
- Tribunal has ordered expert reports by a specific deadline

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Arbitration case reference | Identity and procedural context | Ask |
| Expert's name, qualifications, and firm | Must appear in the report | Ask |
| Applicable arbitral rules | Determines formal requirements for expert reports | Ask |
| Subject matter of expertise | Damages? Valuation? Technical? Industry practice? | Ask |
| Specific issues to be addressed | The exact questions the expert is asked to answer | Ask — this is the "scope of instructions" |
| Data and documents reviewed | The factual basis for the opinions | Ask |

## Optional inputs

- Tribunal procedural order governing expert evidence
- Joint expert or sole tribunal-appointed expert arrangement (uncommon but possible)
- Hot-tubbing expected (affects how opinions are framed)
- Applicable accounting standards (IFRS, US GAAP) for damages or valuation opinions
- Specific methodologies required or prohibited by the parties' agreement

## Document structure

### Section 1 — Cover page and identity

- Expert's full name and professional title
- Appointing party
- Case name and reference
- Title: "Expert Report on [Subject]"
- Date
- Report number (First Report; Second Report if this is responsive)

### Section 2 — Expert qualifications and independence

This section establishes the expert's credibility and duty to the tribunal:

- Full professional biography: education, professional qualifications, current role
- Specific expertise relevant to the issues in this case: "I have [X] years of experience in [subject area] and have provided expert evidence in [X] proceedings."
- Statement of independence: "I confirm that I have been instructed by [Party] but my overriding duty is to the Tribunal. I have given this opinion independently and the views expressed are my own."
- Declaration under applicable rules: IBA Rules Art. 5(2) requires that expert reports contain statements of the expert's independence and overriding duty to the tribunal.
- Prior testimony: list of arbitral and court proceedings in which the expert has previously given evidence (required under some procedural orders)
- Conflicts of interest: disclose any relationship with the parties, witnesses, or counsel

### Section 3 — Scope of instructions

Define precisely what the expert was asked to address:

> "I have been instructed by counsel for [Party] to provide an independent expert opinion on the following questions:
> 1. What is the quantum of damages suffered by [Party] as a result of [alleged breach]?
> 2. Whether the [specific methodology] applied by [opposing party] is consistent with [IFRS / industry practice / applicable standards]?
> 3. [Additional questions]"

A clearly defined scope of instructions:
- Prevents the opposing party from arguing the expert went outside their remit
- Helps the tribunal assess which questions are answered in the report
- Limits the expert's exposure to cross-examination on matters outside their instructions

### Section 4 — Summary of opinions

A plain-language summary of the expert's key conclusions, before the technical analysis. This should be readable by non-technical arbitrators and serves as the executive summary.

### Section 5 — Documents and information reviewed

List all materials the expert relied upon:
- Documents provided by instructing counsel (factual exhibits from the case file)
- Documents obtained or independently reviewed (published data, market research, industry standards)
- Interviews conducted (if any; must be documented)

Note any information that was requested but not provided, and state whether that affects the opinions.

### Section 6 — Factual background (limited)

A brief, neutral summary of the relevant facts that form the basis of the expert's analysis. The expert should not advocate — state the factual assumptions clearly:

> "For the purposes of this report, I have been instructed to assume that [factual assumption]. If this assumption is incorrect, my opinion on [issue X] would change as follows: [sensitivity analysis]."

### Section 7 — Methodology

Explain the analytical framework applied:

**For damages quantification**:
- Standard: expectation damages (loss of anticipated benefit); or reliance damages (out-of-pocket losses); or disgorgement
- Methodology: DCF (discounted cash flow); comparable company analysis; market approach; cost approach
- Why this methodology was chosen over alternatives
- Key assumptions and their sources

**For valuation**:
- Valuation date
- Standard of value (market value; fair value; fair market value)
- Methodology: DCF; comparable transactions; precedent transactions; sum-of-parts
- Discount rate rationale (WACC, CAPM — be specific about inputs)

**For technical / industry practice reports**:
- Standards or codes applied (ISO, industry guidelines, relevant professional standards)
- How the expert applied those standards to the specific facts

### Section 8 — Analysis

The detailed technical analysis applying the methodology to the facts. Organized logically by sub-issue. Uses tables, calculations, and exhibits to support opinions.

**Best practice**:
- Each step of the analysis should be replicable by the opposing expert
- Show working: "Using a discount rate of X% (calculated as shown in Appendix A), the NPV of the expected cash flows is USD Y."
- Acknowledge counterarguments: "I note that the opposing approach would yield Z, but I have rejected it for the following reasons: [reasons]."
- Sensitivity analyses: show how conclusions change under different assumptions

### Section 9 — Opinions

Clear, numbered statement of each opinion:

> "Opinion 1: [Party A's] damages resulting from [breach] are USD [X million] as of [valuation date], calculated using the [methodology] approach."
> "Opinion 2: The [opposing expert's] use of [methodology] is inconsistent with [industry standard / IFRS / applicable principle] for the following reasons..."

Each opinion should be expressed with appropriate confidence: "In my opinion..." / "I am of the view that..." / "I cannot determine..." where the evidence is insufficient.

### Section 10 — Limitations and caveats

Honest acknowledgment of:
- Information not available or not provided
- Assumptions made and their sensitivity
- Areas of genuine uncertainty in the analysis
- Matters outside the expert's expertise

### Appendices

- CV / curriculum vitae of the expert
- List of documents reviewed
- Financial models and calculations (in sufficient detail to be checked by opposing expert)
- List of cases in which the expert has previously given evidence
- Expert's declaration (required under IBA Rules and most institutional rules)

## Jurisdictional notes

### MENA-specific expert evidence considerations

**Civil-law jurisdictions (UAE onshore, KSA, Lebanon, Egypt)**:
- Court-appointed (tribunal-appointed) experts are the norm in civil-law proceedings
- Party-appointed experts are more common in international arbitration even with a civil-law seat
- Civil-law arbitrators may give more weight to tribunal-appointed experts than party experts; this affects how aggressively party experts should position their opinions

**DIFC / ADGM**:
- Common-law approach; party-appointed experts are standard
- Expert witness duties are explicit under DIFC Courts rules and ADGM Court rules

**IBA Rules on Taking of Evidence (2020 edition)**:
- Art. 5: Party-appointed experts; duties; contents of expert reports
- Art. 6: Tribunal-appointed experts; process for appointment; parties' right to challenge
- Art. 8: Oral testimony; hot-tubbing process

## Common mistakes

- **Over-advocacy**: An expert who simply adopts the appointing party's entire factual case and reaches conclusions favoring them on every issue loses credibility before the tribunal; acknowledge where the facts support the other side.
- **No sensitivity analysis**: Real-world analyses have ranges of outcomes; an expert who provides only a single-point estimate without acknowledging key sensitivities is not credible.
- **Failing to address the opposing expert's methodology**: In most arbitrations, expert reports are exchanged; the second (rebuttal) report must directly engage with the opposing expert's methodology — not ignore it.
- **Inadequate qualifications disclosure**: Some arbitrators will disqualify or give no weight to an expert whose qualifications for the specific task are not established; front-load the qualifications section.
- **Exceeding the scope of instructions**: An expert who opines on matters they were not asked to address risks having that section excluded; stay within the defined scope of instructions.

## Related skills

- [[prompt-pack-expert-witness-report-outline]]
- [[prompt-pack-document-production-request]]
- [[prompt-pack-emergency-arbitrator-application]]
- [[prompt-pack-enforcement-of-judgment]]

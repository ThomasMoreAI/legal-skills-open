---
name: prompt-pack-expert-witness-report-outline-sboghossian
title: Expert Witness Report Outline
description: Use when creating a structured outline for an expert witness report for court litigation — covering the expert's qualifications summary, methodology, factual assumptions, analysis framework, opinions, and limitations. Distinct from the arbitration expert report in that it is tailored to the civil court context and applicable civil procedure rules. Applicable for disputes before UAE courts, DIFC Courts, ADGM Courts, Lebanese courts, Egyptian courts, UK courts, and other jurisdictions. Trigger when a litigation expert needs a structured approach before beginning their analysis.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-expert-witness-report-outline
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: litigation
language: en
---

# Expert Witness Report Outline

## When to use this

Use this skill when preparing the outline and structural scaffold for an expert witness report in court litigation proceedings. An expert witness report is formal opinion evidence submitted to a court to assist the judge (or panel) on technical matters outside the tribunal's general knowledge. The report's structure and content must comply with the procedural rules of the particular court and jurisdiction.

This skill is distinguished from [[prompt-pack-expert-report-arbitration]] in several respects:
- Court procedural rules (CPR in UK, DIFC Courts Rules, UAE Civil Procedure Law) specifically regulate the form and content of expert reports
- Some civil-law courts use court-appointed (inquisitorial) experts rather than party-appointed experts
- Expert witness duties and oaths vary by jurisdiction
- Reports may be filed simultaneously or sequentially depending on the court's case management directions

Typical triggers:
- Counsel instructing an expert and needing to brief them on the required report structure
- Expert beginning their assignment and wanting a framework before writing
- Court has given directions for expert evidence and counsel needs to ensure the report is compliant
- Pre-instruction review of whether the expert's scope and methodology will satisfy the applicable court rules

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Subject matter of expertise | Financial, technical, medical, industry practice, etc. | Ask |
| Case type and forum | Determines applicable procedural rules and witness duties | Ask |
| Jurisdiction and applicable civil procedure rules | Structure requirements differ; UK CPR Part 35 is very specific | Ask |
| Specific questions the expert is to address | The "scope of instructions" | Ask |
| Party appointing the expert | Establishes context (party expert vs. court expert) | Ask |

## Optional inputs

- Whether a joint statement / statement of agreed issues will be required (common in UK litigation)
- Whether hot-tubbing is expected (increasingly used in English commercial court)
- Any existing expert reports from the opposing side
- Specific methodologies or standards to be applied
- Whether the expert also serves as a fact witness (mixed expert/fact witness roles require care)

## Document structure (outline template)

### Cover page

- Expert's full name, qualifications, and institution
- Case name and reference number
- Court and division
- Appointing party
- Report title and date
- Report number (first, rebuttal, or supplemental)

### Part 1 — Qualifications and duty to the court

**Qualifications**:
- Academic qualifications
- Professional memberships and registrations
- Relevant experience: specifically why this expert is qualified to address the issues in this case
- Publications, prior testimony (where required)

**Expert's duty**:
- Statement of the expert's overriding duty to the court, not to the appointing party
- Jurisdiction-specific declaration:
  - **UK (CPR Part 35.3)**: "I understand that my duty is to the Court and not to those instructing me, to assist the Court in relation to matters within my expertise. I have complied with this duty."
  - **DIFC Courts**: Similar duty; DIFC Courts Practice Direction on Expert Evidence applies
  - **UAE courts**: Court-appointed expert system applies in most civil-law proceedings; party experts may submit written opinions to the court-appointed expert

**Conflicts declaration**: Confirm no undisclosed interest in the outcome; confirm no prior relationship with the parties that would affect independence.

### Part 2 — Instructions and scope

- Documents received and instructions given
- Questions the expert has been asked to address (numbered list)
- What the expert has NOT been asked to address (important to limit scope)
- Where instructions have changed or supplemented since initial engagement, note all versions

### Part 3 — Facts and assumptions

- Factual background relevant to the analysis (brief; this is not a pleading)
- Facts treated as established vs. facts assumed at counsel's instruction
- Factual assumptions: "For the purposes of my analysis, I have been asked to assume that [specific fact]. If this assumption is incorrect, see paragraph [X] for the impact on my opinion."
- Documents reviewed and relied upon (list in an appendix)

### Part 4 — Methodology

- The analytical approach selected and why it is appropriate for the issues
- Applicable professional or industry standards applied
- Rejection of alternative approaches (briefly — explain why the methodology not chosen is less appropriate, if relevant)
- Data sources and their reliability

### Part 5 — Analysis

The technical analysis itself — organized by question or issue, with:
- Step-by-step reasoning
- Worked calculations (in appendices where lengthy)
- Tables and charts where they add clarity
- Cross-references to documents reviewed

### Part 6 — Opinions

Numbered, clearly stated conclusions corresponding to the instructions:
- "Opinion 1: [Question] — My opinion is that [conclusion] for the following reasons: [summary]."
- Use qualified language where appropriate: "In my opinion..." for conclusions; "I cannot determine..." where evidence is insufficient

### Part 7 — Limitations and caveats

- Documents requested but not provided
- Limitations of the analysis arising from available data
- Areas where the expert's opinion is subject to final determination of factual issues by the court
- Areas outside the expert's expertise (for which a different expert would be needed)

### Signature and declaration

- Expert's signature
- Date
- Declaration as required by applicable rules (see above)

### Appendices

- A: CV
- B: List of documents reviewed
- C: List of cases in which expert has given evidence in the past 5 years
- D: Detailed calculations / financial models
- E: Relevant publications, standards, or codes referenced

## Jurisdictional notes

### UK (CPR Part 35 and Practice Direction 35)

- Expert reports must contain a statement of truth signed by the expert
- Reports must state the facts on which opinions are based
- The expert must state that they have disclosed all matters which might materially affect the opinion
- Joint statement of experts: after exchange of reports, experts may be ordered to meet and prepare a joint statement identifying agreed issues and issues in dispute — this is a critical step often underestimated by experts

### DIFC Courts

- DIFC Courts Practice Direction on Expert Evidence: similar to English CPR Part 35
- Party-appointed experts common; court may appoint a single joint expert in appropriate cases
- Hot-tubbing is used in DIFC Courts — experts are sworn in simultaneously and questioned together

### UAE Onshore Courts

- Civil Procedure Law provides for court-appointed experts (khabeer); party experts submit written opinions to the court-appointed expert
- Party experts in UAE onshore proceedings are not routinely cross-examined; their reports inform the court-appointed expert's opinion
- For international arbitrations seated in UAE, party-appointed experts are standard (see [[prompt-pack-expert-report-arbitration]])

### KSA Courts

- Court-appointed experts (khubara) used in specialized courts
- Party-appointed experts may submit written opinions; the court will determine their weight
- Engineering, medical, and accounting experts are commonly used in commercial and construction cases

### Lebanon

- Civil procedure (based on French model) uses court-appointed experts (expert judiciaire)
- Party experts submit written observations (dires) to the court-appointed expert
- Court-appointed expert's report carries significant weight; parties can file objections

### Egypt

- Civil Procedure Law provides for court-appointed experts in technical cases
- Party experts' written opinions can be submitted but the court-appointed expert's report usually governs quantum determinations

## Common mistakes

- **Overly partisan analysis**: Courts distinguish between "hired gun" experts whose conclusions invariably favor the appointing party and genuinely independent experts; tribunals discount partisan opinions
- **Failing to address contrary evidence**: An expert who ignores adverse data or the opposing expert's strongest points is unconvincing; engage with the opposing view
- **Scope creep**: Opining on matters outside the defined scope of instructions can result in sections of the report being excluded; strictly follow the instructions
- **No sensitivity analysis**: A single-point opinion without showing how it changes under different assumptions is less credible and less useful to the court
- **No compliance with court rules**: In UK CPR Part 35 proceedings, failure to include the required expert's declaration renders the report formally defective; always check the specific court's rules before filing

## Related skills

- [[prompt-pack-expert-report-arbitration]]
- [[prompt-pack-injunction-application]]
- [[prompt-pack-discovery-request]]
- [[prompt-pack-enforcement-of-judgment]]

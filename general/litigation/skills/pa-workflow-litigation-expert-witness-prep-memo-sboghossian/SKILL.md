---
name: pa-workflow-litigation-expert-witness-prep-memo-sboghossian
title: Expert Witness Prep Memo
description: Use when litigation counsel needs a structured preparation memo for an expert witness — either their own expert (to anticipate cross-examination and strengthen testimony) or an opposing expert (to develop critique and cross-examination strategy). Covers CV verification, prior testimony review, methodology critique, and cross-examination planning. Applicable across international arbitration (ICC, LCIA, DIAC), DIFC, ADGM, UK, US, and civil-law courts in MENA.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-litigation-expert-witness-prep-memo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Expert Witness Prep Memo

## Purpose

Expert witnesses are pivotal in complex commercial disputes, construction claims, valuation matters, and technical patent cases. This workflow produces a structured memo that equips counsel to: (a) prepare their own expert to withstand cross-examination, or (b) develop a targeted cross-examination strategy against an opposing expert. The memo addresses credibility, methodology, prior inconsistencies, and anticipated lines of attack.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Expert's curriculum vitae | Yes | Full CV including qualifications, employment, and publications |
| Expert report (own or opposing) | Yes | PDF or text |
| Prior expert reports by same expert | If available | Prior opinions in other matters |
| Prior deposition / hearing transcripts (same expert) | If available | Gold standard for contradiction analysis |
| Case fact pattern and legal issues | Yes | Needed to evaluate the opinion's fit to the facts |
| Applicable standard (damages, valuation, technical) | Recommended | E.g., Discounted Cash Flow, fair market value, engineering standards |
| Jurisdiction and tribunal | Yes | Governs expert evidence standards |

## Memo Structure

### Section 1 — Expert Profile and Credentials

**Verification checklist:**
- Confirm degrees, institutions, and dates (compare CV claim to publicly verifiable sources)
- Bar / professional association membership (current? suspended? disciplinary history?)
- Academic appointments: verify tenure, visiting vs. permanent, gaps in employment
- Prior publications: are they peer-reviewed, or self-published / industry white papers?
- Conflicts of interest: prior retention by opposing counsel or party in other matters

**Red flags:**
- CV claims that cannot be independently verified
- History of opposing retentions in the same field (suggests "hired gun" profile)
- Academic work contradicting the position taken in this case
- Disqualification or criticism in prior cases (Daubert challenges, judicial criticism)

### Section 2 — Prior Testimony Analysis

Using available transcripts and prior reports:

| Prior matter | Forum | Date | Position taken | Consistent with current report? |
|---|---|---|---|---|
| Matter A | DIFC Court | 2020 | Discount rate: 8% | Inconsistent — current report uses 5% with no explanation |
| Matter B | ICC Arbitration | 2021 | Rejected DCF for early-stage companies | Inconsistent — current report applies DCF to same type of company |

Flag: any prior sworn testimony that directly contradicts the current opinion is highly valuable for cross-examination.

### Section 3 — Methodology Critique

For each analytical method the expert uses:

**Is the method accepted in the relevant professional community?**
- Does the methodology appear in peer-reviewed literature?
- Is it consistent with standards published by recognized bodies (IVS — International Valuation Standards, RICS, CFA Institute, etc.)?

**Application to the facts:**
- Did the expert apply the method correctly?
- Did they rely on their own assumptions vs. facts in evidence?
- Were alternative methodologies considered and, if rejected, was the rejection reasoned?

**Data and inputs:**
- What data sources were used?
- Are the inputs verifiable from the record?
- Were comparable transactions / benchmarks cherry-picked?

**Sensitivity analysis:**
- What happens to the conclusion if key assumptions change by ±10%?
- Does the expert's conclusion survive reasonable variation in inputs, or is it entirely dependent on favorable assumptions?

### Section 4 — Anticipated Cross-Examination Topics

Based on Sections 1–3, list the 8–12 highest-value cross-examination topics:

1. **Credentialing**: "Your CV states you hold a position at X University — were you asked to leave that position?"
2. **Conflict**: "You were retained by the opposing firm in Matter X in 2021?"
3. **Prior inconsistency**: "In the DIFC matter you applied a discount rate of 8% — here you used 5% — can you explain the difference?"
4. **Methodology**: "The DCF method assumes the business would have continued operating — what evidence supports that assumption given [specific adverse fact]?"
5. **Cherry-picked comparables**: "You selected three comparables — did you consider X, Y, Z? Why were those excluded?"

For each topic: the question sequence, the document / transcript to confront with, the goal (admission or impeachment), and the fallback if the witness explains.

### Section 5 — Defensive Prep (Own Expert)

If preparing a favorable expert:

**Topics opposing counsel will attack:**
- List in priority order
- For each: the basis for the attack (prior statement, methodology weakness, credential gap)

**Preparation exercises:**
- Have the expert explain the methodology in plain language without jargon
- Walk through every input: "Where does this number come from?"
- Prepare for "I don't know" moments — acceptable for peripherals, not for core assumptions
- Prepare for hypotheticals that change key inputs: "If the discount rate were 10% instead of 5%, what would your conclusion be?"

**Ethical line**: preparing an expert on substance and demeanor is proper; instructing an expert to change their opinion is not.

## Jurisdictional Notes

### Expert Evidence Standards by Forum

| Forum | Standard | Notes |
|---|---|---|
| US Federal | Daubert (FRCP 702) | Reliability + fit + methodology; Daubert motion to exclude is available |
| UK courts | CPR Part 35 | Expert owes duty to court, not party; hot-tubbing (concurrent evidence) is increasingly used |
| DIFC | DIFC Court Rules Pt. 29 | Follows English CPR approach; expert owes overriding duty to court |
| ADGM | ADGM Court Procedure Rules | Similar to DIFC; English common-law standard |
| International Arbitration | IBA Rules on Evidence Art. 5–6 | Tribunal-directed; rebuttal reports common; oral testimony at evidentiary hearing |
| UAE onshore | Court-appointed expert (khabir) is primary | Party experts are advisory; court relies on its own expert more heavily |
| KSA | Same as UAE onshore — court-appointed expert dominant | Challenge the court expert's methodology through written objections |
| Lebanon | Experts appointed by court or by parties | Party expert reports submitted; court may appoint its own expert |
| Egypt | Court-appointed expert in most civil matters | Party expert reports are submitted as exhibits; rarely replace court expert |

**MENA practice note**: In UAE onshore, KSA, and Egyptian state court proceedings, investing heavily in cross-examining a party's expert is less strategic than identifying weaknesses in the court-appointed expert's methodology and submitting detailed written objections with supporting technical materials.

## Output

```markdown
## Expert Witness Prep Memo — [Expert Name] — [Matter Name] — [Date]

### SECTION 1: CREDENTIALS ASSESSMENT
[Summary of verification results; red flags identified]

### SECTION 2: PRIOR TESTIMONY MATRIX
[Table of prior matters, positions, and consistency analysis]

### SECTION 3: METHODOLOGY CRITIQUE
- Method used: [DCF / comparable companies / engineering standard / etc.]
- Methodology verdict: SOUND / QUESTIONABLE / FLAWED
- Key weaknesses: [Itemized]

### SECTION 4: CROSS-EXAMINATION PLAN (12 topics)
[Priority-ordered list with question sequences and supporting documents]

### SECTION 5: DEFENSIVE PREP TOPICS (if own expert)
[List of anticipated attacks with preparation guidance]
```

## Related Skills

- [[pa-workflow-litigation-witness-contradiction-finder]]
- [[pa-workflow-litigation-deposition-binder-builder]]
- [[pa-workflow-litigation-case-theory-simulator]]
- [[pa-workflow-litigation-transcript-search-q-and-a-indexing]]

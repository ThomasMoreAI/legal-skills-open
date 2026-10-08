---
name: prompt-pack-post-hearing-brief-sboghossian
title: Post-Hearing Brief
description: Use when drafting a post-hearing brief (also called a post-hearing submission or closing written submission) in an international arbitration or formal hearing. Synthesizes the evidentiary record, addresses witness credibility, analyzes applicable law, responds to opposing arguments, and requests specific relief with supporting reasoning. Applicable to ICC, DIAC, LCIA, SIAC, ADCCAC, and DIFC-LCIA arbitrations as well as common-law court proceedings.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-post-hearing-brief
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Post-Hearing Brief

## When to use this

Use this skill when drafting a post-hearing brief (PHB) — the written submission filed after the conclusion of the evidentiary hearing in an arbitration or similar proceeding. The PHB is the party's last and often most important substantive submission: it synthesizes everything that was put in evidence, addresses witness credibility, makes the legal argument on full record, and tells the tribunal precisely what relief it should grant and why.

Post-hearing briefs are distinct from pre-hearing submissions and memorial-style briefs; they are backward-looking (analyzing what happened at the hearing) and forward-looking (directing the tribunal to the right outcome).

Triggers:
- "Draft our post-hearing brief for [Arbitration Case]."
- "The hearing concluded last week — now write our closing submission."
- "Draft written closing submissions for [Party] in the DIAC arbitration."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Party and role (Claimant / Respondent) | Determines framing and structure | Ask user |
| Arbitration reference and institution | Provides procedural context; some institutions have page limits | Ask user |
| Hearing date(s) | Timeline reference in the brief | Ask user |
| Summary of claims and defenses | Core issues to be addressed | Ask user |
| Key witnesses and testimony highlights | Key testimony to address (favorable and unfavorable) | Ask user |
| Key exhibits | Exhibits to be cited in the brief | Ask user |
| Relief requested | What the party is asking the tribunal to award | Ask user |
| Applicable law | Governing law of the contract / substantive law applicable to claims | Ask user |
| Page / word limit | Determines structure compression | Per tribunal directions |

## Optional inputs

- Opposing party's most significant arguments (to be addressed directly)
- Prior procedural rulings by the tribunal that affect the brief
- Expert testimony highlights (damages, technical, industry expert)
- Any jurisdictional issues raised during the hearing

## Brief structure

### Cover page and procedural heading
Arbitration reference, parties, date of submission, title: "[Party]'s Post-Hearing Brief."

### I. Introduction (2–4 pages)

Open by orienting the tribunal to the key conclusion: "This hearing confirmed what [Party]'s evidence showed from the outset: [one-paragraph summary of the case in favor of the filing party]."

Address the hearing briefly: what was established, what was not, and why the outcome of the hearing supports [Party]'s position.

State the relief requested upfront — the tribunal should never have to search for what the party is asking for.

### II. Procedural History (1–2 pages)

Brief, factual summary:
- Nature of the dispute
- Date of commencement, seat, institution, and governing procedural rules
- Key procedural steps to date (SOC, SOD, Reply, Rejoinder, procedural orders)
- Hearing dates, witnesses who testified, experts who were examined

This section orients the tribunal and provides the citation backbone for the brief.

### III. Summary of Facts as Established by the Evidence

**Purpose**: Present the tribunal with the narrative of facts that the evidence at the hearing has established. This is not a repeat of the memorial — it focuses on what the hearing confirmed, clarified, or changed.

**Structure**:
- Organize chronologically or by issue, not by witness
- For each key fact, cite the exhibit number, witness testimony (transcript page reference), or expert report section that supports it
- Address facts that were contested at the hearing: explain why the tribunal should accept [Party]'s version (based on documentary evidence, credibility of witnesses, consistency with other evidence)

**Format**:
> "The [contract] required [Respondent] to deliver the equipment by [date]. (Exhibit 5, Clause 7.1.) [Respondent's witness, Mr. X] admitted in cross-examination that no equipment was delivered on [date]. (Transcript Day 2, pp. 45:12–46:3.) Claimant's contemporaneous communications confirm the delay. (Exhibit 23, Email of [Date].)"

### IV. Witness Credibility and Factual Findings

**Purpose**: Guide the tribunal in assessing the credibility of witnesses. Post-hearing briefs are the primary vehicle for credibility argument.

For each key witness:
- State what the witness was expected to say
- What the witness actually said
- Whether the testimony was consistent with the witness's prior written statements
- Whether the witness was successfully challenged or maintained their position under cross-examination
- Why the tribunal should accept or reject that witness's evidence on disputed points

**Example structure**:
- [Claimant's witness A]: credible; consistent under cross-examination; corroborated by documentary evidence at Exhibits [X, Y, Z]
- [Respondent's witness B]: not credible on [specific point] because: (i) testimony contradicted by Exhibit [C]; (ii) account changed materially from his witness statement at [page]; (iii) no documentary support for assertion that [...]

### V. Legal Analysis

For each claim or defense at issue:

**5.1 [Claim/Defense Title]**

1. **Legal standard**: State the applicable rule under the governing law. Cite to the named, well-established legal framework (e.g., "Under the DIFC Contract Law, a party in breach is liable for foreseeable direct and indirect losses"; "Under the ICC Rules, tribunal may award compound interest"). Do not fabricate article numbers or case citations not in the record.

2. **Application to the facts**: Apply the standard to the facts established at Section III. "The evidence establishes all elements of [claim]: [fact 1 → element 1], [fact 2 → element 2], [fact 3 → element 3]."

3. **Opposing party's arguments**: Address the opposing party's best arguments made in their submissions or advanced by their witnesses during the hearing. Explain specifically why each fails: factual basis is unsupported by the record; legal standard is misstated; the applicable law reaches a different conclusion.

4. **Conclusion on this issue**: state the conclusion clearly and with confidence.

### VI. Damages / Quantum

**Purpose**: Explain precisely what the party is seeking and why the evidence supports each element of relief.

**Structure**:
1. Applicable damages principles under the governing law (expectation damages / reliance damages / disgorgement / statutory damages)
2. For each head of damage:
   - Basis of the claim
   - Evidence of quantum (Claimant's expert report, financial records, comparable transactions)
   - Response to Respondent's quantum arguments
   - Specific amount requested

**Damages table**:
| Head of damage | Expert exhibit | Amount requested | Respondent's challenge | Response to challenge |
|---|---|---|---|---|
| [Direct loss] | Exhibit X | USD Y | Challenges causation | Causation established by Transcript Day 1, pp. X–Y |
| [Consequential loss] | Exhibit Z | USD W | Says not foreseeable | Foreseeable under [governing law standard] because [reason] |
| [Interest] | | At [rate] from [date] | | |

**Interest**: State whether simple or compound interest is requested and from what date; explain the legal basis for the rate and compounding method requested.

### VII. Relief Requested

State the precise relief the tribunal is asked to grant, in numbered form. The final award must follow the prayer for relief; give the tribunal clear formulation to adopt.

> The Tribunal is respectfully requested to:
> 1. Award Claimant damages in the total amount of [USD X], comprising: (i) [USD Y] for [head 1]; (ii) [USD Z] for [head 2].
> 2. Award Claimant interest on the foregoing amounts at [rate] per annum, compounded [annually / semi-annually], from [date] until the date of the Award and thereafter at [rate] until full payment.
> 3. Order Respondent to bear the costs of the arbitration, including Claimant's reasonable legal costs.
> 4. Grant such other and further relief as the Tribunal considers appropriate.

### VIII. Conclusion (1 paragraph)

Restate the case in one compelling paragraph. End with a clear statement of why the hearing has confirmed that the tribunal should grant the full relief requested.

## Style and format standards

- **Be precise on record citations**: every factual assertion must cite exhibit number, transcript page, or witness statement paragraph. Unreferenced assertions carry no weight.
- **Address the other side**: a PHB that ignores the opposing party's strongest points looks weak; engage and rebut.
- **Prefer short sentences in the relief section**: the tribunal may use the relief section as a template for the operative paragraphs of the award; write it as if it will be quoted verbatim.
- **Comply with page/word limits**: page limits are strictly enforced in major arbitration institutions; if there are competing priorities, prioritize damages and relief over procedural history.
- **No new evidence**: a PHB must work with the evidentiary record; parties generally cannot introduce new exhibits after the hearing closes without leave. Address this in the brief if a party seeks to make reference to something not in the record.

## Jurisdictional / institutional notes

| Forum | Notes |
|---|---|
| **ICC Arbitration** | Post-hearing briefs are common but not automatic; must be ordered by tribunal; typical page limit 50–100 pages; filed simultaneously unless tribunal orders sequential filing. |
| **DIAC (Dubai)** | DIAC Rules permit post-hearing submissions; tribunal has wide discretion; regional parties often file PHBs even if not specifically ordered. |
| **DIFC-LCIA / LCIA** | Well-developed PHB practice; LCIA tribunals frequently order PHBs; simultaneous filing common; transcript citations expected. |
| **SIAC** | Post-hearing submissions standard practice; SIAC Rules permit; Singapore-seated arbitrations follow English common-law procedural norms. |
| **ADCCAC (Abu Dhabi)** | Less standardized; follow tribunal's specific directions; Arabic-language version may be required depending on applicable law. |

## Common mistakes

- **Restating the pleadings rather than analyzing the hearing**: the PHB must engage with what actually happened at the hearing — witness credibility, what was established, what was challenged.
- **No record citations**: a PHB without transcript and exhibit citations is not taken seriously by experienced arbitrators; every key factual claim must be pinned to the record.
- **Omitting the damages table**: a narrative-only damages section is harder for the tribunal to work with when drafting the award; a clear table makes the tribunal's work easier.
- **Vague prayer for relief**: the prayer for relief must state specific amounts and interest rates; "such damages as the tribunal deems appropriate" is inadequate.

## Related skills

- [[prompt-pack-motion-for-summary-judgment]]
- [[prompt-pack-legal-opinion-on-dispute]]
- [[prompt-pack-litigation-hold-notice]]
- [[heuristic-always-state-jurisdiction-first]]

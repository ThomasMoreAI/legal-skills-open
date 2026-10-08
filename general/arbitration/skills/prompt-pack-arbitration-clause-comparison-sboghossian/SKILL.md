---
name: prompt-pack-arbitration-clause-comparison-sboghossian
title: Arbitration Clause Comparison
description: Use when comparing arbitration clauses or institutional rules across ICC, LCIA, SIAC, DIAC, CRCICA, and SCCA to advise on seat selection, institution selection, or clause analysis. Review/analysis skill in the arbitration practice area; produces structured comparison tables covering seat, language, arbitrator appointment, emergency arbitrator, costs, and enforceability for a specific dispute type and region.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-arbitration-clause-comparison
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: arbitration
language: en
---

# Arbitration Clause Comparison

## When to use this

Use this skill when:
- A client must choose between arbitration institutions or seats for an upcoming contract
- Comparing an existing arbitration clause against alternatives to identify gaps or upgrades
- Advising on which institution/seat is best suited to a specific dispute type, parties, and MENA/regional context
- Analyzing the arbitration provisions in a document presented by a counterparty

This is a **review and analysis** skill, not a drafting skill. The output is a comparison table or structured analysis, not a draft clause. For the draft clause, see [[prompt-pack-arbitration-agreement-clause]].

---

## Prompt template

> Compare arbitration clauses from [ICC, LCIA, SIAC, DIFC-LCIA, DIAC] rules. Analyze seat, language, number of arbitrators, emergency arbitrator provisions, expedited procedures, costs, and enforceability considerations for a [type of dispute] in [region].

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before comparing.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Institutions to compare | The specific institutions the client is choosing between |
| Dispute type and size | Emergency arbitrator importance varies; expedited procedure thresholds differ |
| Parties' nationalities/jurisdictions | Influences neutrality perception and enforcement considerations |
| Intended seat(s) | Seat is often independent of institution — clarify if the question is about seat selection or institution selection or both |
| Enforcement target | Where the award needs to be enforced determines what matters most |

---

## Comparison framework

### Dimension 1 — Institutional structure and governance

| Institution | Governing body | Award scrutiny | Administrative fees |
|-------------|---------------|---------------|-------------------|
| ICC | International Court of Arbitration | Full scrutiny before rendering | High (% of claim) |
| LCIA | LCIA Court | No scrutiny of award content | Lower; hourly administrative fees |
| SIAC | Court of Arbitration | No scrutiny | Moderate (% of claim) |
| DIAC | Centre in Dubai | Case management; no scrutiny | Moderate; updated 2022 Rules |
| CRCICA | Cairo Regional Centre | No scrutiny | Lower; Egyptian/African market |
| SCCA | Saudi Centre in Riyadh | No scrutiny | Developing; Saudi market |

### Dimension 2 — Emergency arbitrator provisions

Emergency arbitrators allow interim relief before the tribunal is constituted — critical for asset-freezing, injunctive relief, and preserving evidence.

| Institution | Emergency arbitrator? | Timeline |
|-------------|----------------------|---------|
| ICC | Yes (2012 Rules, App. V) | Decision within 15 days of appointment |
| LCIA | Yes (Art. 9B) | Decision within 14 days |
| SIAC | Yes (Schedule 1) | Decision within 14 days |
| DIAC | Yes (2022 Rules, Art. 26) | Decision within 14 days |
| CRCICA | Yes (2011 Rules, Art. 29) | Decision within 15 days |
| SCCA | Yes (2023 Rules) | 15 days |
| UNCITRAL ad hoc | No | N/A — must go to court for interim relief |

**MENA note**: even where emergency arbitrators are available, MENA courts may not enforce emergency arbitral orders directly. DIFC and ADGM Courts will enforce; UAE onshore courts are more cautious; Saudi courts generally do not enforce interim orders from international arbitrations without further analysis.

### Dimension 3 — Expedited procedures

For lower-value or less complex disputes, expedited procedures reduce time and cost:

| Institution | Expedited procedure? | Threshold |
|-------------|---------------------|---------|
| ICC | Yes (Expedited Procedure Rules) | Claims up to USD 3M (automatic unless opted out) |
| LCIA | Determination procedure (Art. 32) | By agreement or LCIA Court order |
| SIAC | Expedited Procedure (Rule 9) | By agreement or SIAC Registrar order; no automatic threshold |
| DIAC | Expedited (2022 Rules) | Claims up to AED 1M or by agreement |
| CRCICA | By agreement | No fixed threshold |
| SCCA | Streamlined procedure | Claims up to SAR 1M |

### Dimension 4 — Costs and fee structures

Arbitration costs have two components: institutional fees and arbitrator fees.

| Institution | Institutional fee basis | Arbitrator fees |
|-------------|------------------------|----------------|
| ICC | Sliding scale on claim value (ICC schedule) | ICC Court recommends; parties agree or ICC sets |
| LCIA | Hourly (administrative team) + case handling fees | LCIA-set hourly rates (lower than ICC on small cases) |
| SIAC | Sliding scale; generally competitive with ICC | SIAC schedule |
| DIAC | Sliding scale (2022 schedule) | Tribunal sets, DIAC approves |
| CRCICA | Sliding scale | Tribunal sets, CRCICA approves |
| SCCA | Fee schedule (SAR) | SCCA schedule |

**Cost allocation note**: all major institutions allow the tribunal to allocate costs (including legal costs) to the losing party, but cost awards are discretionary. LCIA tribunals are generally more willing to award full costs to the successful party than DIAC or CRCICA tribunals.

### Dimension 5 — Seat options and implications

Most institutions are not tied to a single seat — the parties can choose their seat and then select the institution. However, certain institutions have institutional associations:

| Institution | Common seat(s) | Seat flexibility |
|-------------|---------------|----------------|
| ICC | Paris (HQ); any seat worldwide | Full flexibility |
| LCIA | London (traditional); any seat | Full flexibility |
| SIAC | Singapore (default); any seat | Full flexibility |
| DIAC | Dubai (onshore or DIFC) | Dubai/DIFC typical; other seats possible |
| CRCICA | Cairo | Cairo typical |
| SCCA | Riyadh | Saudi Arabia |

**For MENA disputes, recommended seat choices**:

| Situation | Recommended seat |
|-----------|-----------------|
| UAE parties; want onshore enforcement | Dubai (onshore); DIAC rules |
| UAE parties; want DIFC Courts enforcement (faster) | Dubai (DIFC seat); DIAC or ICC rules |
| Cross-border; enforcement needed in multiple MENA countries | Paris or London + ICC; widely recognized and enforced |
| Saudi Arabia nexus | Riyadh (SCCA); or London/Paris if Saudi party accepts |
| Egypt nexus | Cairo (CRCICA); or London/Paris |
| Cross-border investment (ICSID eligible) | Washington DC (ICSID for investment treaty arbitration) |

### Dimension 6 — Enforceability

All New York Convention states are obligated to recognize and enforce arbitral awards from other Convention states (subject to limited grounds for refusal). MENA New York Convention status:

| Country | NYC signatory | Notes |
|---------|--------------|-------|
| UAE | Yes (1981) | Enforcement generally effective; DIFC Courts route is faster |
| Saudi Arabia | Yes (1994) | Enforcement available; Sharia-law public policy ground can arise |
| Egypt | Yes (1959) | Generally effective; courts may scrutinize awards |
| Lebanon | Yes (1998) | Available; enforcement timing can be slow |
| Bahrain | Yes (1988) | Generally effective |
| Kuwait | Yes (1978) | Available |
| Oman | Yes (1999) | Generally effective |
| Qatar (QFC) | Yes (1994) | QFC Courts can enforce |

---

## Output format

Produce the comparison as:

```
## Comparison: [Institution A] vs [Institution B] (vs [Institution C])
[Purpose statement: dispute type, region, key concerns]

### Summary recommendation
[1-2 sentences: which institution/seat for this situation and why]

### Comparison table
[Use the dimensions above; show only relevant rows]

### Key differentiators
[3-5 bullet points of the most important differences for this specific situation]

### Enforceability notes
[Jurisdiction-specific enforcement analysis]

### Recommendation
[Specific institution + seat + why, with caveats]
```

---

## Jurisdictional notes

### DIFC-LCIA note
The DIFC-LCIA Arbitration Centre was dissolved in 2021 following the Emirate of Dubai's reform of its arbitral landscape. Cases previously filed with DIFC-LCIA were transferred to DIAC. The DIAC 2022 Rules incorporate many features from the former DIFC-LCIA Rules.

### Saudi arbitration evolution
The SCCA, established in 2016, has grown significantly and is increasingly used for Saudi-connected commercial disputes. For disputes that may need enforcement in Saudi Arabia, SCCA proceedings are advantageous because Saudi courts are more familiar with them than with ICC or LCIA proceedings.

---

## Related skills

- [[prompt-pack-arbitration-agreement-clause]] — draft the clause once the institution/seat is selected
- [[prompt-pack-arbitration-cost-submission]] — costs submission at the end of the arbitration
- [[prompt-pack-award-enforcement-application]] — enforcing the resulting award
- [[kb-arbitration-mena]] — MENA arbitration law and institution reference

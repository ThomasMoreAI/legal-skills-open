---
name: pa-workflow-litigation-case-theory-simulator-sboghossian
title: Case Theory Simulator
description: Use when litigation counsel needs to stress-test competing case theories before committing to a trial or arbitration strategy. Evaluates multiple legal theories against the same fact pattern, predicts opposing-counsel responses, estimates settlement-value ranges, and recommends an approach. Applies across civil and common-law systems (DIFC, ADGM, UAE, KSA, LB, EG, UK, US). Links to the case fact-pattern builder for structured input.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-litigation-case-theory-simulator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Case Theory Simulator

## Purpose

Committing to the wrong legal theory late in a case is expensive. This workflow forces a structured multi-theory analysis at the outset (or at a strategy inflection point), surfacing the strengths and vulnerabilities of each theory, modeling opponent responses, and producing a comparative assessment that leads to a recommended primary and fallback theory.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Fact pattern | Yes | Use [[casesim-fact-pattern-builder]] for structured input; free text also accepted |
| Jurisdiction and forum | Yes | Determines substantive law, burden of proof standards, and procedural rules |
| Client's position (plaintiff/claimant or defendant/respondent) | Yes | |
| Available theories (at least two) | Recommended | If not provided, system will generate candidate theories |
| Key documents and evidence summary | Recommended | |
| Known weaknesses / bad facts | Recommended | Produces more realistic stress-test |
| Opponent's likely theories (if known) | Optional | |
| Settlement history / prior demands | Optional | For settlement-value calibration |

## Logic

### Step 1 — Theory generation

If fewer than two theories are provided, generate candidates based on the facts and jurisdiction. For example, in a contract dispute:
- Theory A: breach of contract (primary)
- Theory B: unjust enrichment / quantum meruit (fallback if contract unenforceable)
- Theory C: tortious interference (if third party involved)
- Theory D: fraud / misrepresentation (if false statements alleged)

In civil-law jurisdictions (LB, EG, UAE onshore, KSA): also consider delictual liability (civil fault) as an alternative to contractual theories, especially where contractual privity is absent.

### Step 2 — Theory-by-theory analysis

For each theory, produce:

**Strengths:**
- Legal elements that are satisfied by the evidence
- Favorable precedents (jurisdiction-specific)
- Procedural advantages (e.g., lower burden of proof, availability of injunctive relief)
- Jury / judge appeal (for jury trials; bench trial considerations)

**Weaknesses:**
- Missing elements
- Adverse precedents or statutory bars
- Evidence gaps requiring additional discovery or expert testimony
- Affirmative defenses opponent can raise
- Exposure to counterclaims

**Evidence requirements:**
- What must be proved and how
- Documents, witnesses, and experts needed per element

### Step 3 — Opposing-counsel response model

For each theory, model the three most likely opposing responses:
1. **Motion to dismiss / strike**: which elements of this theory are vulnerable to pre-trial challenge?
2. **Affirmative defense**: what statutory or equitable defenses will be raised?
3. **Counterclaim / cross-claim**: does this theory open the client to a counter-attack?

MENA-specific traps:
- UAE / KSA onshore courts: opposing counsel may file a criminal complaint in parallel to a civil action (filing criminal fraud or embezzlement complaints as a negotiation tactic is common). Flag if the facts could support a criminal referral by either side.
- Lebanon: courts have wide discretion in equity-like relief; the opponent may seek provisional attachment (saisie conservatoire) against assets.
- Egypt: the defendant in commercial arbitration can file a nullity action before Egyptian courts under the Arbitration Law if procedural grounds exist — factor in if the matter involves an arbitration clause.

### Step 4 — Settlement value estimate

Produce a structured settlement-value range:

| Scenario | Probability | Estimated outcome |
|---|---|---|
| Best case (client wins all claims) | 20% | USD X |
| Most likely (mixed result) | 50% | USD Y |
| Worst case (client loses, counterclaim succeeds) | 15% | USD -Z |
| Settlement (negotiated resolution) | 15% | USD W |

**Expected value**: weighted average of the above scenarios minus litigation cost.

Calibration factors:
- Forum: arbitration (predictable, limited discovery) vs. court (variable, discovery-intensive)
- Judge / arbitrator profile if known
- Jurisdictional enforcement difficulty (e.g., enforcing a DIFC judgment in KSA onshore courts requires separate enforcement proceedings)
- Client's risk appetite and time horizon

### Step 5 — Recommended approach

Output a structured recommendation:
- **Primary theory**: the most viable path to relief
- **Fallback theory**: to plead in the alternative if primary theory fails
- **Theories to drop**: explain why (weakens overall credibility, creates estoppel risk, etc.)
- **Key next steps**: evidence gathering, experts to retain, pre-filing motions, early settlement indicators

## Output Format

```markdown
## Case Theory Simulation Report — [Matter Name] — [Date]

### Theories Analyzed
1. Breach of Contract
2. Unjust Enrichment
3. Fraudulent Misrepresentation

---

### Theory 1: Breach of Contract
**Strengths**: [...]
**Weaknesses**: [...]
**Opponent response**: Motion to dismiss (limitation issue), Counterclaim (offset)

### Theory 2: Unjust Enrichment
...

---

### Settlement Value Matrix
| Scenario | Probability | Outcome |
| Best case | 20% | $2.4M |
| Most likely | 55% | $900K |
| Worst case | 15% | -$200K |
| Settlement | 10% | $600K |
**Expected value (before costs):** $820K

---

### Recommendation
**Primary**: Theory 1 — Breach of Contract (strongest documentary support)
**Fallback**: Theory 2 — Unjust Enrichment
**Drop**: Theory 3 — insufficient evidence of fraudulent intent without expert testimony
**Immediate actions**: Preserve all communications; retain financial expert; file protective order.
```

## Jurisdictional Notes

- **DIFC / ADGM**: English common-law applies. Theories must satisfy common-law elements. Expert evidence on quantum is standard practice in commercial disputes. Settlement discussions are formally without prejudice.
- **UAE onshore**: Civil law; the court may award damages only for actual (proven) loss and direct causation. Penalty clause enforceability depends on UAE Federal Civil Transactions Law. Courts actively seek to moderate disproportionate penalties.
- **KSA**: Commercial disputes before specialized commercial courts or the Board of Grievances. Sharia-based contract law applies — interest claims (riba) must be reframed as late-payment compensation. Arbitration is common in commercial contracts.
- **Lebanon**: Courts apply Lebanese Code of Obligations and Contracts. Civil and commercial proceedings are often slow; interim relief (juge des référés) is a practical tool. Parallel criminal complaints (especially fraud) are a common litigation tactic.
- **Egypt**: Egyptian civil law follows French civil-law tradition. Litigation is slow in state courts; arbitration via CRCICA is faster. Egyptian courts apply strict evidentiary rules — witness testimony is less relied upon than documents.

## Related Skills

- [[casesim-fact-pattern-builder]]
- [[pa-workflow-litigation-deposition-binder-builder]]
- [[pa-workflow-litigation-expert-witness-prep-memo]]
- [[pa-workflow-litigation-witness-contradiction-finder]]
- [[pa-workflow-litigation-brief-cite-checker]]

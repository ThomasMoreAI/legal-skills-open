---
name: prompt-pack-legal-opinion-on-dispute-sboghossian
title: Legal Opinion on Dispute
description: Use when a lawyer or in-house counsel needs to draft a formal legal opinion analyzing the merits of a claim or defense under a specified jurisdiction's law. Covers liability assessment, damages exposure, litigation risk, probability of success, and recommended course of action. Applicable to disputes in MENA courts (UAE, KSA, LB, EG), DIFC/ADGM Courts, international arbitration, and common-law litigation.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-legal-opinion-on-dispute
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Legal Opinion on Dispute

## When to use this

Use this skill when a client, in-house counsel, or instructing solicitor needs a formal written legal opinion analyzing whether a claim or defense is viable, what the exposure is, and what the recommended course of action is. This is a pre-litigation or mid-litigation analytical document — it does not generate pleadings or submissions (use [[prompt-pack-motion-for-summary-judgment]] or [[prompt-pack-post-hearing-brief]] for those).

Triggers:
- "I need a legal opinion on whether we have a valid breach of contract claim against [counterparty]."
- "Assess our litigation exposure in this dispute and tell me if we should settle."
- "Draft an opinion on the merits of [client's] defense to [plaintiff's] claim."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Client / recipient name | Addressee of the opinion; affects privilege | Ask user |
| Description of the dispute | Facts giving rise to the potential claim or defense | Ask user — must be specific |
| Jurisdiction | Determines applicable substantive and procedural law | Ask user |
| Claim / defense to be analyzed | The specific legal theory to be assessed | Ask user |
| Applicable contract or instrument | If claim arises from a contract, provide the relevant clauses | Ask user |
| Instruction: claimant-side or respondent-side | Determines the framing of the opinion | Ask user |

## Optional inputs

- Prior court orders or procedural history
- Applicable limitation period information
- Evidence available (documents, witness statements, expert reports)
- Budget constraints (determines depth of research)
- Whether opinion is for litigation strategy, settlement negotiation, or board reporting

## Opinion structure

### 1. Instruction and Scope
State who has instructed the opinion, the date, the factual scenario as understood, and the questions the opinion addresses. Include a disclaimer that the opinion is based on facts as presented and the law as at the date of the opinion.

### 2. Summary of Facts Relevant to the Analysis
Set out only the facts material to the legal analysis. Avoid narrative padding. Identify any gaps in facts that, if resolved differently, could change the conclusion.

### 3. Issues to Be Determined
Number each legal issue clearly:
1. Does [Claimant/Respondent] have a viable claim in [breach of contract / tort / unjust enrichment / other]?
2. What is the likely quantum of recoverable damages?
3. Are there any defenses that [Respondent] can raise that would bar or limit recovery?
4. What is the litigation risk profile?

### 4. Analysis — Issue by Issue

**For each issue:**
- State the applicable legal test or standard under the governing law.
- Apply the test to the facts.
- Cite to the applicable statute, regulation, or well-established framework (do not fabricate case names or statute articles; flag where you are stating general principles vs confirmed law).
- Reach a conclusion on each issue with a confidence level (strong/moderate/weak).

**Damages analysis**:
- Identify the heads of damages available under the governing law (expectation / reliance / restitution / statutory damages)
- Apply the applicable rule on remoteness (foreseeability test in common law; direct and foreseeable damages in most civil-law systems)
- Apply any contractual limitation on damages (caps, exclusions of consequential loss)
- Note that MENA civil-law courts (UAE, LB, EG) have broad judicial discretion to assess damages; overly precise damages calculations may differ from court award

**Quantum estimate format**:
| Head of damage | Basis | Low estimate | High estimate | Notes |
|---|---|---|---|---|
| Direct loss | [contractual formula] | | | |
| Consequential loss | [if recoverable] | | | |
| Interest | [rate and period] | | | |
| Legal costs | [recovery regime] | | | |

### 5. Defenses and Counterclaims
- Set out any viable defenses the responding party could raise.
- Assess the strength of each defense.
- Identify any counterclaims that could offset or exceed the main claim.

### 6. Litigation Risk Assessment

| Factor | Assessment |
|---|---|
| Merits of claim | Strong / Moderate / Weak |
| Evidence sufficiency | Sufficient / Gaps identified (specify) |
| Quantum certainty | Certain / Range / Uncertain |
| Procedural risks | [limitation, jurisdiction, service issues] |
| Enforcement risk | [If judgment/award obtained, can it be enforced?] |
| Overall litigation risk | Low / Medium / High |

### 7. Probability of Success
State clearly: "In our view, [Claimant/Respondent] has a [strong / reasonable / limited] prospect of success on the primary claim. We estimate the probability of success at approximately [X]% — [high / medium / low confidence]."

Do not provide a precise percentage if the factual or legal foundation does not support it; instead use ranges or verbal assessments.

### 8. Recommended Course of Action
Based on the analysis:
- Option A: Pursue litigation — recommended if [conditions]
- Option B: Negotiate / mediate — recommended if [conditions]
- Option C: Accept settlement if in range [X–Y] — recommended if [conditions]
- Flag urgent actions (preservation of evidence, limitation date, pre-action notice requirements)

### 9. Caveats
- Opinion based on facts as provided; material undisclosed facts may change the analysis.
- Law as at [date]; subsequent changes in law or regulation are not reflected.
- This opinion does not constitute a guarantee of outcome.
- Local counsel verification recommended for jurisdictions where the drafting counsel is not admitted.

## Jurisdictional notes

| Jurisdiction | Key considerations |
|---|---|
| **UAE (onshore courts)** | Civil code basis; fault and damages governed by UAE Civil Transactions Law; Arabic-language proceedings; courts tend to appoint judicial experts for technical and financial issues. |
| **DIFC Courts** | Common-law jurisdiction; English law familiar; broad disclosure rules; precedent-based; sophisticated commercial court. |
| **ADGM Courts** | English law applied; similar to DIFC but smaller docket; strong arbitration support framework. |
| **KSA** | Sharia-based legal system; Saudi courts apply principles of fiqh; specialized commercial courts in major cities; damages assessment can differ from civil-law/common-law approaches. |
| **Lebanon** | Mixed civil/common law; Code of Obligations and Contracts; enforcement of judgments uncertain given current economic and political context. |
| **Egypt** | Civil and Commercial Procedure Code; Commercial Courts; enforcement of foreign judgments requires exequatur procedure. |
| **International Arbitration** | Opinion should identify applicable institutional rules (ICC, DIAC, LCIA, SIAC) and seat law; Tribunal has broad discretion on procedural matters. |

## Common mistakes

- **Opining on facts not provided**: a legal opinion is only as good as its factual foundation; clearly identify factual assumptions.
- **Confusing civil-law and common-law damages rules**: consequential loss, remoteness, and mitigation rules differ materially between civil-law MENA courts and DIFC/common-law courts.
- **Not flagging limitation periods**: in every dispute opinion, the limitation analysis must appear prominently — missed limitation periods are malpractice.
- **Omitting enforcement analysis**: a judgment in favor of the client is worthless if the respondent has no assets in a jurisdiction where the judgment is enforceable.

## Related skills

- [[prompt-pack-litigation-hold-notice]]
- [[prompt-pack-legal-hold-management-procedure]]
- [[prompt-pack-post-hearing-brief]]
- [[prompt-pack-motion-for-summary-judgment]]
- [[heuristic-always-state-jurisdiction-first]]

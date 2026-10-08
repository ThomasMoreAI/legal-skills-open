---
name: prompt-pack-case-assessment-memo-sboghossian
title: Case Assessment Memo
description: Use when a litigator or disputes lawyer needs to produce a structured case assessment memo for a client, covering facts, legal issues, strengths/weaknesses, estimated outcomes and damages, and strategic recommendations. Applicable across MENA civil-law courts (Lebanon, UAE onshore, KSA, Egypt), DIFC/ADGM common-law courts, ICC/DIAC/LCIA arbitration, and any other forum once the jurisdiction is specified.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-case-assessment-memo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Case Assessment Memo

A case assessment memo is the foundational document in any dispute: it converts raw facts into a legal diagnosis and gives the client a clear-eyed view of their position before committing to litigation. This skill produces a professional, structured memo suitable for delivery to the client or for internal team briefing.

## When to use this

- A client has presented a potential dispute and the lawyer needs to assess viability before advising on strategy.
- The legal team is preparing an internal brief before a pre-litigation meeting or mediation.
- The matter is in early litigation and a written risk assessment is needed for a budget or litigation reserve discussion.
- The client is an in-house team asking for a "go/no-go" recommendation on pursuing or defending a claim.
- Settlement discussions are imminent and the lawyer needs a written baseline for negotiating authority.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Client name and role (claimant/defendant) | Frames the memo correctly | Ask the user |
| Description of the dispute | Core factual narrative | Ask the user — provide as much detail as possible |
| Jurisdiction and forum (court/arbitration) | Determines applicable law and procedural rules | Ask the user; do not assume |
| Key documents available | Evidence basis for the assessment | Ask the user to list or attach |
| Deadline or urgency (limitation period, hearing date) | Shapes how prescriptive the memo must be | Ask the user |

## Optional inputs

- Opposing party's known position or any correspondence received.
- Quantum / damages figure already identified.
- Prior litigation history between the parties.
- Insurance coverage that might respond to the claim.
- Arbitration clause or dispute resolution clause in the underlying contract.

## Memo structure

### 1. Executive summary
One paragraph: what the dispute is about, who is exposed, and the headline recommendation (pursue / defend / settle / watch and wait). Busy executives read this alone.

### 2. Facts
- Chronological narrative of the material facts.
- Distinguish between agreed facts, facts in dispute, and facts that need further investigation.
- Note the key documents that support or undermine each fact.

### 3. Legal issues
Enumerate the discrete legal issues raised by the facts. Typical issues include:
- Breach of contract / contractual interpretation
- Tortious claims (negligence, misrepresentation, fraud)
- Statutory or regulatory claims
- Jurisdictional or procedural issues (limitation, standing, forum)
- Quantum / measure of damages

For each issue, state: (a) the governing legal test, (b) whether the applicable law is well-settled or disputed, and (c) which party bears the burden of proof.

### 4. Strengths and weaknesses analysis

Present as a balanced table:

| Party | Strengths | Weaknesses |
|---|---|---|
| Client | [List the client's strongest points of law and evidence] | [List vulnerabilities honestly] |
| Opponent | [List the strongest arguments the other side will run] | [List vulnerabilities in their position] |

Be candid. Lawyers who only report strengths do clients a disservice. Honest assessment of weaknesses is what enables good settlement decisions.

### 5. Outcome assessment

Provide:
- **Probability of success on liability** (expressed as a range, e.g., 55–70%, with brief reasoning).
- **Quantum range** if the client succeeds on liability: best case / most likely / worst case.
- **Estimated costs** of pursuing the matter to trial or final award.
- **Time to resolution** (realistic estimate including any appeals).
- **Cost/benefit analysis**: expected value compared with litigation costs.

Do not fabricate statistics. Base the probability assessment on the strength of the legal issues and evidence identified above.

### 6. Strategic recommendations

Choose one or more of the following strategic postures and explain the reasoning:

- **Pursue aggressively:** Strong case, opponent likely to settle under pressure; file promptly.
- **Open settlement dialogue:** Case has merit but risks and costs of full litigation outweigh the advantage; approach now on a without-prejudice basis.
- **Defend and attrit:** Client is the defendant with a reasonable defence; make the opponent incur costs to discourage full litigation.
- **Gather more evidence before deciding:** Key facts are unknown; specific investigation steps are recommended.
- **Drop the claim / resist only symbolically:** Probability too low or quantum too small to justify cost.

Tailor the recommendation to the client's commercial objectives, not just legal merits.

### 7. Immediate action items
Numbered list:
1. Secure and preserve documents (litigation hold letter).
2. Check limitation period — hard deadline if imminent.
3. Send/respond to demand letter if not done.
4. Engage expert witnesses if quantum is technical (e.g., construction, financial).
5. Assess whether a without-prejudice opening is appropriate.

### 8. Assumptions and limitations
State explicitly what the memo does not cover and what additional information would change the assessment. Flag if expert evidence is needed to support any element of the assessment.

## Jurisdictional notes

| Forum | Key considerations |
|---|---|
| Lebanese courts | Civil law; Code of Civil Procedure; courts are slow (3–7 years to final judgment); arbitration strongly preferred for commercial disputes; enforcement of foreign judgments requires exequatur |
| UAE onshore courts | Civil law; courts conduct proceedings in Arabic; translations are mandatory; enforcement of judgments is reasonably efficient within the UAE |
| DIFC Courts | Common law; English-language; experienced commercial judges; enforcement of DIFC judgments in UAE onshore courts via a recognized reciprocal framework |
| ADGM Courts | Common law; modelled on English procedure; well-regarded for financial services disputes |
| KSA courts | Based on Islamic law (Sharia) and royal decrees; commercial disputes before Commercial Courts; proceedings in Arabic; enforcement of foreign judgments requires separate action |
| Egypt | Civil law; Egyptian Civil Code; Commercial Courts for commercial disputes; enforcement of foreign judgments requires an exequatur petition |
| ICC / DIAC / LCIA arbitration | Rules-based; seat of arbitration determines applicable procedural law; New York Convention enables enforcement in 170+ states |

## Output format

Deliver the memo as a Word-compatible document with:
- Header: matter reference, client name, date, author, confidentiality classification.
- Section headings as above.
- "Privileged and Confidential — Legal Advice" footer on every page.
- Version number (draft memos should be clearly marked DRAFT).

## Limits and escalation

- This memo is an assessment tool for qualified legal professionals; it does not constitute legal advice to an end client without lawyer review.
- Do not express a higher level of certainty than the underlying facts and law support.
- If limitation is within 30 days, flag this as a critical deadline before any other analysis.
- If the dispute involves regulatory authorities or criminal elements, note that a separate regulatory strategy memo is needed.

## Related skills

- [[prompt-pack-demand-letter]]
- [[prompt-pack-case-law-research-prompt]]
- [[prompt-pack-litigation-strategy-memo]]
- [[prompt-pack-settlement-agreement]]
- [[prompt-pack-arbitration-statement-of-claim]]

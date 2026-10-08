---
name: prompt-pack-convert-complex-document-into-key-points-sboghossian
title: Convert Complex Document into Key Points
description: Use when a lawyer or legal team needs to extract and distil the key legal issues, risks, and important points from a complex legal document into structured bullet-point format suitable for rapid review. Faster and more focused than a full summary; outputs are decision-quality points, not narrative prose. Applicable to contracts, regulatory instruments, court decisions, and due diligence reports across all jurisdictions including MENA (UAE, KSA, LB, EG, DIFC/ADGM).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-convert-complex-document-into-key-points
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Convert Complex Document into Key Points

Converting a complex legal document into key points is one of the highest-frequency tasks in legal practice. The skill is not summarisation — it is extraction: pulling out the points that a reader must know in order to take action, understand risk, or make a decision, and presenting them as a structured list without extraneous prose.

## When to use this

- A lawyer needs a fast reference of the most important provisions in a long contract before a meeting.
- An in-house team is conducting high-volume document review and needs a consistent extraction format.
- A client has forwarded a regulatory notice, court order, or complex agreement and needs to know the "headline" issues immediately.
- Preparing a cover memo to accompany a document being circulated for approval — the key points become the memo.
- Building the foundation for a more detailed risk matrix, negotiation brief, or client advisory note.
- Reviewing due diligence documents at speed: the key-points extraction creates the working list of issues to investigate further.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| The document to be analysed | The source text | User pastes or attaches the document |
| Reviewing party | Key points are perspective-specific; what is a risk for one party is an obligation for the other | Ask the user |
| Document type | Contract / court decision / regulatory notice / due diligence report / legislation | Ask the user |
| Purpose | What will the output be used for? (Signing decision / internal briefing / regulatory response / negotiation) | Ask the user |

## Optional inputs

- Maximum number of key points (default: no more than 15 for any single document).
- Whether financial figures should be highlighted separately.
- Whether the user wants the points organised by category (obligations / risks / deadlines / financial) or by document order.
- Target audience (lawyer peer / non-lawyer executive / board).

## Extraction methodology

### What counts as a "key point"

A point is "key" if any one of the following is true:
1. It creates a **concrete obligation** on the reviewing party (you must do X by Y date).
2. It creates a **financial commitment** (you will pay, receive, or be liable for X amount).
3. It creates a **legal risk** that could cause loss or liability if triggered.
4. It contains a **deadline** that, if missed, has material consequences.
5. It grants or restricts a **right** that affects the party's ability to operate.
6. It is **unusual or non-standard** compared to market practice in this document type.
7. It contains a **condition** that must be satisfied before something else happens.

### What is not a key point
- Boilerplate recitals or definitions that repeat obvious intent.
- Standard severability, entire agreement, and counterparts clauses (unless they are non-standard).
- Obligations that are purely administrative and have no meaningful consequence if unmet.
- Provisions that state what the law already requires without adding any contractual obligation.

### How to structure the key points output

**Format 1 — Category-based (recommended for most documents):**

**OBLIGATIONS (what we must do)**
- [Point 1]: [1–2 sentence description]
- [Point 2]: ...

**OBLIGATIONS (what they must do)**
- ...

**FINANCIAL COMMITMENTS**
- ...

**KEY RISKS / EXPOSURES**
- ...

**DEADLINES AND TIME-SENSITIVE PROVISIONS**
- ...

**UNUSUAL OR NON-STANDARD PROVISIONS**
- ...

**OPEN ISSUES / ITEMS REQUIRING FURTHER INVESTIGATION**
- ...

**Format 2 — Ordered by severity (recommended for risk-focused review):**
Number each point 1 to N, with Critical points first, followed by High, Medium, and Low. Include a one-line severity tag.

**Format 3 — Document-order (recommended for clause-by-clause review):**
Follow the document structure; list each material clause with its key point. Useful when the reader will be referring back to the document.

### Quality standards

Each key point should be:
- **Specific:** Name the clause, the party, the amount, the date. "The liability cap is set at USD 500,000" is a key point; "there is a liability cap" is not.
- **Complete:** Include the caveat or exception if it materially changes the meaning. "Liability is capped at USD 500,000 except for fraud and IP infringement (both uncapped)" is a complete key point.
- **Actionable:** If there is an action required, say so in the key point. "Governing law is English; we currently have no English-law counsel — this needs to be arranged before dispute arises" is actionable.
- **Single-issue:** One clause, one risk, one point. Do not combine separate issues in a single bullet.

## Document-type specific guidance

**Contracts:**
Focus on: financial provisions, liability, IP ownership, termination, governing law/dispute resolution, unusual restrictions, and conditions precedent.

**Court decisions and arbitral awards:**
Focus on: the holding (what the court decided), the key principle established, the facts that drove the outcome, and the practical implication for the reviewing party's situation.

**Regulatory notices and guidance:**
Focus on: the obligation triggered, the deadline for compliance, the penalty for non-compliance, and whether the obligation is new or a restatement of existing law.

**Due diligence documents:**
Focus on: red flags (issues that could affect transaction pricing or conditions), clean flags (items confirming no issue), and open items requiring further investigation.

**Legislation:**
Focus on: who is caught, what must be done, by when, and the consequence of non-compliance. See also [[prompt-pack-convert-law-into-checklist]] for a compliance-oriented output.

## MENA context notes

When extracting key points from Arabic-language documents:
- Note any ambiguity between the Arabic and English versions if both exist (the Arabic version typically governs in UAE onshore, KSA, LB, and EG courts).
- Flag provisions that are written in Arabic legal terminology that does not translate directly (e.g., وضع اليد — which has specific property law meaning in LB/EG).
- In KSA, note whether the document references Royal Decrees or Ministerial Decisions that may have been amended; verify currency with local counsel.

## Common mistakes

- Listing every clause as a key point — defeats the purpose; must be selective.
- Writing prose paragraphs instead of bullet points — makes the output harder to scan.
- Omitting the caveats and exceptions that limit the apparent severity of a risk.
- Failing to include the "unusual / non-standard" category — this is often where the material risks hide.
- Using defined terms from the document without explaining them — the reader of the key points may not have the contract open.

## Related skills

- [[prompt-pack-complex-law-simple-summary]]
- [[prompt-pack-contract-summary-for-executives]]
- [[prompt-pack-contract-risk-matrix]]
- [[prompt-pack-convert-law-into-checklist]]
- [[prompt-pack-client-advisory-note]]

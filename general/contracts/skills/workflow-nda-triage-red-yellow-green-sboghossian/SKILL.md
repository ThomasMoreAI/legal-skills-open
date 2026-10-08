---
name: workflow-nda-triage-red-yellow-green-sboghossian
title: NDA Triage — Red / Yellow / Green
description: Use when an NDA needs a fast risk triage — producing a Green (sign as-is), Yellow (counter-redline with 1–3 points), or Red (reject / renegotiate) verdict in under 90 seconds. Designed for in-house counsel, busy outside counsel, and legal AI copilots handling high-volume NDA inflow. Integrates side detection, quick-check methodology, MENA-specific enforceability flags, and a structured output template including the verdict, rationale, and proposed redline.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/workflow/workflow-nda-triage-red-yellow-green
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# NDA Triage — Red / Yellow / Green

## Purpose

High-volume NDA review is one of the most common legal bottlenecks. This workflow converts an NDA into a verdict — sign, counter, or reject — in under 90 seconds for standard NDAs, with a redline attached for Yellow verdicts. It is the entry point for all NDA review tasks; route to [[workflow-contract-redline-20min]] only for complex or unusual NDAs requiring deeper analysis.

**Success metric**: median time from NDA upload to verdict ≤ 90 seconds.

---

## Inputs

| Input | Required | Notes |
|-------|---------|-------|
| NDA document | Yes | Paste text, upload file, or pull from matter |
| User's side | Yes | Disclosing party, receiving party, or mutual — if unclear, detect from context or ask |
| Purpose of disclosure | Recommended | M&A, hiring, partnership, vendor, client | 
| Jurisdiction | Recommended | Governing law; defaults to DIFC if MENA commercial and not stated |
| Any known sensitivities | Optional | Residuals clauses, duration concerns, scope disputes |

---

## Logic — Step-by-Step

### Step 1: Load NDA

Accept the NDA in any of three ways:
1. **Paste**: user pastes the text directly
2. **Upload**: user uploads a file (PDF, Word)
3. **Matter pull**: pull from the active eFirm matter (if in [[efirm-matter-context]])

If the document is longer than ~5 pages (standard NDA is 2–4 pages), flag that this may be a more substantive agreement than a standard NDA and offer to route to [[workflow-contract-redline-20min]] instead.

### Step 2: Side Detection

The NDA review is asymmetric — the same clause may be acceptable from one side and unacceptable from the other.

**Auto-detect the user's side from:**
- Matter context (if loaded)
- Explicit statement in the prompt ("I'm the receiving party")
- Party names in the NDA (if the user's company name is identifiable)

If side cannot be determined: ask before proceeding. A wrong-side analysis is worse than a delayed one.

**Side implications:**
| Party | Wants | Fears |
|-------|-------|-------|
| Disclosing party | Broad definition of confidential information; long term; no residuals clause; return/destruction obligation | Information leaking; employee poaching; use outside permitted purpose |
| Receiving party | Narrow definition; short term; residuals clause; no onerous return obligation | Overbroad definition capturing pre-existing knowledge; unlimited liability; injunctions for technical breach |
| Mutual NDA | Balanced definition; mutual term; mutual obligations | Same as above, from both directions |

### Step 3: Quick Check — run [[review-nda-quick-check]]

**The 10-point NDA quick-check:**

| # | Check | Green flag | Red / Yellow flag |
|---|-------|-----------|-----------------|
| 1 | **Definition of confidential information** | Reasonable scope; standard exclusions (public domain, independently developed, prior knowledge, required by law) | Overbroad (covers "all information shared"); missing standard exclusions |
| 2 | **Purpose / permitted use** | Narrowly defined; matches the actual business purpose | Vague or absent; "any purpose" |
| 3 | **Term of confidentiality** | 2–5 years for general commercial; indefinite for specific trade secrets (flagged separately) | 10+ years for general information without justification; indefinite for all information |
| 4 | **Return / destruction obligation** | Reasonable; exclude archival/backup copies; exclude legally required retention | Absolute; no exclusion for backups or legal retention |
| 5 | **Residuals clause** | If tech company receiving: acceptable; clear carve-out for residuals retained in unaided memory | Hidden or overbroad residuals clause if disclosing party; unacceptable in sensitive competitive context |
| 6 | **Representatives / permitted disclosure** | Reasonable definition of who can receive (employees, professional advisers, affiliated entities on need-to-know basis) | No restriction on representatives; no obligation to bind representatives |
| 7 | **Governing law and dispute resolution** | Familiar jurisdiction; enforceable forum | Obscure jurisdiction; one-sided dispute resolution; mandatory arbitration with inconvenient seat |
| 8 | **Remedies** | Acknowledges irreparable harm; injunctive relief | Waives right to injunctive relief; disproportionate damages |
| 9 | **Non-solicitation** | If included: reasonable scope and term; limited to direct solicitation | Broad non-solicit covering all employees; prohibits hiring from public market |
| 10 | **IP ownership** | No IP grant or assignment | IP assignment or overly broad license grant for receiving party's use of confidential information |

### Step 4: Risk Classification

Assign a verdict based on the quick-check results:

**GREEN** — Sign as-is, no negotiation needed:
- Condition: all 10 quick-check points pass; no unusual terms; standard market NDA
- Output: short approval note only

**YELLOW** — Counter-redline with 1–3 points:
- Condition: 1–3 issues identified that are addressable with targeted redlines; the NDA is otherwise acceptable
- Output: verdict note + proposed redlines for each issue
- Maximum issues for Yellow: if more than 3 material points need to change, escalate to Red

**RED** — Reject / send back to drafter:
- Condition: fundamental problems (overbroad definition without standard exclusions; unacceptable term; IP assignment risk; suspicious residuals clause for disclosing party; unfamiliar/unfavorable jurisdiction)
- Output: summary memo of issues; recommendation to return to drafter with markup or to reject entirely

---

## Output Template

All verdicts use this format:

```
VERDICT: [GREEN / YELLOW / RED]

QUICK RATIONALE: [1–2 sentences explaining the verdict]

ACTION: [Sign as-is / Counter-redline / Reject and return]

[IF YELLOW — REDLINES:]
Issue 1: [Clause] — [Problem] → [Proposed change]
Issue 2: [Clause] — [Problem] → [Proposed change]
Issue 3: [Clause] — [Problem] → [Proposed change]

[IF RED — MEMO SUMMARY:]
Critical issue 1: [Clause] — [Why it's a red]
Critical issue 2: [Clause] — [Why it's a red]
Recommendation: [Return to drafter with markup / Decline to sign]
```

---

## MENA-Specific NDA Flags

### UAE / Civil Law NDAs

- **Language**: if the NDA governs a UAE-mainland relationship, an Arabic version or Arabic text controls clause may be expected; English-only NDAs are enforceable in UAE courts but Arabic text controls in government context
- **Governing law / courts**: NDA governed by UAE law and UAE courts — acceptable; NDA governed by foreign law with foreign courts — check if there is a legitimate reason; foreign judgments enforceable in UAE under bilateral treaties
- **Penalty clauses**: UAE Civil Code courts may reduce disproportionate penalty/damages provisions to actual loss; state liquidated damages clauses with caution; courts may adjust
- **Non-compete in NDA**: if an NDA contains a non-compete clause, this is atypical and should be flagged — non-competes belong in employment or commercial agreements, not NDAs

### DIFC / Common Law NDAs

- DIFC NDAs follow English law structure; look for the standard Faccenda Chicken implied duty categories
- Injunctions: DIFC Courts readily grant interim injunctions for breach of confidence; receiving party should ensure the NDA does not expand injunctive liability beyond standard
- Boilerplate English NDAs imported for DIFC deals: generally fine if governing law is DIFC or English; watch for US-law-specific provisions (e.g., specific "trade secrets" defined under DTSA) that may not translate

### KSA NDAs

- Arabic text: all important commercial agreements with Saudi parties should have Arabic versions; Arabic text should be stated to control
- Sharia overlay: NDAs are generally Sharia-compliant; no structural issues with standard NDA clauses
- Non-solicitation: Saudi courts may view aggressive employee non-solicitation clauses skeptically given employee rights under Labour Code

### Lebanon NDAs

- Lebanese law of obligations (Code des Obligations et des Contrats) provides underlying framework
- NDAs in Lebanon are generally straightforward; main issue is enforceability of injunctions (Lebanese courts are slower and enforcement more complex than DIFC)
- Currency: if the NDA contains any damages or liquidated damages clauses, specify the currency explicitly

---

## Time Protocol

The 90-second target is for standard 2–4 page NDAs:

| NDA length / complexity | Expected time | Route |
|------------------------|--------------|-------|
| Standard mutual NDA (2–3 pages) | 30–90 seconds | This workflow |
| Standard unilateral NDA (3–5 pages) | 60–120 seconds | This workflow |
| Long-form NDA with unusual provisions (5–10 pages) | 5–10 minutes | [[workflow-contract-redline-20min]] |
| NDA embedded in a larger agreement (JV, M&A) | Use main agreement review | [[workflow-contract-redline-20min]] or [[workflow-full-due-diligence-pack]] |

---

## Optional: eFirm Integration

After triage, offer to log the time entry in eFirm:
- Matter: [active matter name]
- Time: 0.1 units (minimum) for GREEN; 0.2–0.3 units for YELLOW with redline; 0.3–0.5 units for RED with memo
- Description: "NDA triage — [counterparty name] — [VERDICT]"

---

## Related Skills

- [[review-nda-quick-check]]
- [[draft-nda-mutual]]
- [[draft-nda-unilateral]]
- [[workflow-contract-redline-20min]]
- [[output-executive-summary-first]]

---
name: draft-legal-opinion-sboghossian
title: Legal Opinion
description: Use when drafting a formal legal opinion — a written analysis by counsel on a specific legal question, typically relied upon by a counterparty or third party (e.g., at a transaction closing, for regulatory filing, or for financing). Covers standard structure (assumptions, qualifications, opinions), IRAC methodology for each opinion paragraph, transactional vs advisory opinions, and the critical malpractice-avoidance rules (scope limitations, reliance restrictions). Triggers on "legal opinion", "counsel's opinion", "closing opinion", "opinion letter", or "memorandum of law" when formality and reliance are in scope.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-legal-opinion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: contracts
language: en
---

# Legal Opinion

## When to use this

A legal opinion is a formal written statement by qualified counsel that specific legal conclusions are, in counsel's professional judgment, correct as of the date of the opinion, based on assumed facts and identified governing law. It is distinct from an informal advice note or a memo.

Use this skill when:
- A transaction closing requires an opinion that a party is duly organized, a document is enforceable, execution is authorized, or government approval is not required
- A bank or investor requires a legal opinion as a condition precedent to funding
- A regulatory filing requires a legal opinion on compliance or licensing status
- A party needs a formal written analysis that they — or a named third party — may rely upon
- Court or arbitration proceedings require expert-opinion-style analysis in memo form

For informal internal analysis without third-party reliance, use [[draft-memo-of-law]] instead.

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Addressee | Determines who may rely on the opinion; unnamed parties cannot |
| Question(s) to be answered | Each question generates one opinion paragraph; questions must be precise |
| Assumed or stated facts | The opinion is only as good as its factual basis |
| Governing law | The jurisdiction whose law is being analyzed |
| Documents reviewed | Limits the scope; documents not listed cannot form the basis of the opinion |
| Purpose | Transaction closing / advisory / regulatory — shapes the standard formulations |

## Optional inputs

- Specific exceptions or carve-outs the requestor has pre-agreed to accept
- Form of opinion letter pre-agreed with the recipient (e.g., a bank's standard form)
- Whether the opinion covers foreign-law issues (often requires foreign-qualified counsel)
- Materiality threshold (if the opinion qualifies non-material exceptions)

## Standard structure

### 1. Header
```
To:    [Name and address of Addressee(s)]
From:  [Law Firm / Counsel name]
Re:    [Matter reference] — [Brief description]
Date:  [Date of opinion]
```

### 2. Scope statement
One paragraph stating: what you have been asked to opine on, the transaction or matter to which it relates, the governing law, and a reference to the list of documents reviewed.

### 3. Documents reviewed
An enumerated list of every document reviewed. Documents not on this list are not covered. If counsel receives a document after issuing the opinion, the opinion does not cover it.

### 4. Assumptions
Assumptions are facts or conditions that counsel has not independently verified but is treating as true for the purpose of the opinion. Standard assumptions in transactional opinions:
- Authenticity of all signatures and documents
- Capacity, authority, and identity of signatories
- Genuineness of all corporate authorizations (resolutions) provided
- No fraud, misrepresentation, or material omission in the documents
- That all parties have obtained necessary approvals from their own side
- That the agreed form of the documents is the executed form

State each assumption clearly: "We have assumed, without independent verification, that..."

### 5. Qualifications
Qualifications limit the scope or certainty of the opinions. Standard qualifications:
- Enforceability of remedies may be limited by applicable bankruptcy, insolvency, moratorium, or reorganization laws
- Courts may apply equitable principles that limit or vary the remedies available
- Certain provisions (e.g., indemnities for a party's own fraud; conclusive certificate clauses) may not be enforceable
- This opinion is limited to the laws of [Jurisdiction] in effect on the date of this opinion
- We express no opinion on the laws of any other jurisdiction
- Currency conversion may be subject to exchange control regulations
- Enforcement of foreign judgments may be subject to court recognition procedures

The qualification list should be tailored: every unnecessary qualification weakens the opinion commercially; every missing qualification creates malpractice exposure.

### 6. Opinions (numbered)
Each opinion should:
- State the conclusion plainly as the first sentence: "The Agreement constitutes the valid and binding obligation of [Company], enforceable against [Company] in accordance with its terms."
- Reference the applicable law, article, or principle that supports it
- Apply the rule to the assumed facts
- Qualify where necessary (but do not re-state the general qualifications in every paragraph — use a cross-reference)

**IRAC methodology** per opinion paragraph: see [[output-irac-structure]].

Standard opinions in a financing or M&A context:
1. **Due organization / incorporation**: [Company] is duly incorporated and validly existing under the laws of [Jurisdiction]
2. **Corporate power and authority**: [Company] has the corporate power and authority to enter into the Agreement and perform its obligations
3. **Due authorization**: The execution, delivery, and performance of the Agreement have been duly authorized by all necessary corporate action
4. **Enforceability**: The Agreement constitutes the legal, valid, and binding obligation of [Company], enforceable in accordance with its terms, subject to the General Qualifications
5. **No conflict**: The execution, delivery, and performance of the Agreement do not violate [Company]'s constituent documents or any applicable law or regulation (as specifically identified)
6. **No governmental approval required**: No governmental or regulatory authorization, approval, or filing is required as a condition to the lawful execution, delivery, or performance of the Agreement

### 7. Reliance
Expressly state who may rely on this opinion and for what purpose. Typical formulation:
> "This opinion is addressed solely to [Addressee] and may be relied upon only by [Addressee] in connection with [the Transaction]. It may not be relied upon by any other person or used for any other purpose, and may not be disclosed or quoted without our prior written consent."

### 8. Limitations and disclaimers
- The opinion speaks as of the date stated; no obligation to update
- We express no opinion on commercial reasonableness, adequacy of consideration, or the merits of the transaction as a business matter
- This opinion is not a guarantee of outcome in litigation

## Transactional opinions (closing opinions) — additional notes

Closing opinions are conditioned on: the transaction documents being in the agreed final form at closing; the representations and warranties being accurate; the conditions precedent being satisfied. Counsel is entitled to rely on officers' certificates for factual matters (e.g., no pending litigation above a materiality threshold).

In MENA transactions, closing opinions are routinely required by international financing banks. Typical additional opinions for MENA transactions:
- Choice of law: that the parties' choice of [English/UAE/DIFC] law will be respected by local courts
- Enforcement: that a judgment of [English/DIFC/ADGM] courts would be recognized and enforced by [local courts]
- No exchange control restrictions on payments required under the Agreement
- The Security created by [Security Agreement] constitutes valid and perfected security in [Jurisdiction]

Note: most MENA civil-law jurisdictions (UAE federal, KSA, LB, EG) will not simply recognize foreign judgments under general comity — specific bilateral treaties or national legislation governs. Counsel must opine specifically and carefully on enforcement.

## IRAC structure per opinion paragraph

Adopt the IRAC (Issue — Rule — Application — Conclusion) pattern from [[output-irac-structure]]:
- **Issue**: What is the precise legal question for this opinion?
- **Rule**: What is the applicable legal rule, statute, regulation, or judicial principle?
- **Application**: How does the rule apply to the assumed facts?
- **Conclusion**: The opinion itself.

The opinion paragraph in the final document presents only the Conclusion and (briefly) the Rule; the Issue and Application inform the internal analysis but may be implicit in the final document.

## Critical — malpractice avoidance

**State your assumptions clearly** — if you have not verified a fact (e.g., the authenticity of a signature, the accuracy of a financial statement), it must be an assumption. Opinions given without adequate assumptions have led to malpractice claims.

**State your qualifications precisely** — the qualifications must accurately reflect the limits of your opinion. A standard qualifications section cut-and-pasted from another matter without review is dangerous.

**Limit reliance** — unnamed parties who receive and rely on the opinion (e.g., parties brought in after signing) have no claim against you. Address this proactively if a letter of reliance is requested.

**No updating obligation** — an opinion speaks as of its date. If the law changes after issuance, the issuer is not automatically liable unless there is a separate updating obligation. State this in the limitations section.

**Language** — in MENA, opinions for local court enforcement often need to be in Arabic or certified Arabic translation. Identify this requirement early.

## Jurisdictional notes

| Jurisdiction | Practice notes |
|---|---|
| **DIFC / ADGM** | Common-law opinions; DIFC Courts enforce per DIFC Enforcement Law; standard English-law-style qualifications apply |
| **UAE onshore** | Opinions must address UAE Federal law; enforcement of foreign judgments governed by bilateral treaties (UAE–France, UAE–GCC member states, New York Convention for arbitral awards); Courts Civil Procedure Law governs recognition |
| **KSA** | Opinions often require Saudi-qualified counsel (Saudi attorney licensed before the Ministry of Justice); enforcement via SCCA arbitral awards is most reliable; foreign court judgments require reciprocity or bilateral treaty |
| **LB** | Notarized opinions may be required for use before Lebanese courts; Lebanese Bar Association regulates; French civil-law tradition |
| **EU / France** | Formal closing opinions are less standard than in common-law jurisdictions; French practice uses "attestation juridique" for specific corporate-law confirmations |
| **UK** | City of London Law Society (CLLS) standard qualifications and assumptions guide; widely used as the benchmark for English-law opinions |
| **US** | TriBar Opinion Committee guidelines; California vs New York styles differ; NYSBA, ABA guidance |

## Common mistakes

- Opining on matters not within the scope of your instruction
- Copying standard forms without reviewing them for accuracy for this transaction
- Failing to list all documents reviewed (leaving open whether additional documents affect the opinion)
- Not providing a reliance limitation — third parties claiming to rely on opinions not addressed to them
- Issuing an opinion conditioned on representations that turn out to be false without a bring-down mechanism

## Related skills

- [[draft-memo-of-law]]
- [[output-irac-structure]]
- [[review-contract-general]]
- [[draft-litigation-complaint]]
- [[output-citation-mena-conventions]]

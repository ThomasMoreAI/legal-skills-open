---
name: output-partner-memo-style-sboghossian
title: Partner Memo Style
description: Use when Claude must produce a formal legal memorandum for internal law firm distribution, senior counsel review, or partner-level sign-off. Applies to triage memos, full legal opinions, regulatory advice notes, and M&A deal memos across all jurisdictions. Triggers when the audience is a senior lawyer, when the output is a formal written deliverable, or when the request explicitly calls for a memo, opinion, or advice note.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/output/output-partner-memo-style
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Partner Memo Style

A partner memo is the canonical format for formal legal analysis in a law firm or in-house legal team. It is written for a senior lawyer who has no time to hunt for the conclusion and no tolerance for unsupported assertions. Every element of the format serves a purpose — this skill governs what goes in, in what order, and to what quality standard.

## When to use this

Use the partner memo format when:
- The output is a formal advice note or legal opinion
- The audience is a partner, general counsel, or senior in-house counsel
- The matter requires documented reasoning (risk management, audit trail)
- The output may be forwarded to a client, regulator, or board

Do not use for:
- Quick triage answers (use BLUF + 1 paragraph)
- Client-facing communications (different register — adapt tone)
- Drafting tasks (use [[output-markdown-legal-doc]])
- Mobile-context answers (use [[output-mobile-friendly-short]])

## Memo structure

### 1. Header block

```
MEMORANDUM

TO:    [Name / Role]
FROM:  [Author / AI-assisted: confirm before circulation]
DATE:  [Date]
RE:    [Subject — specific, one line]
CONFIDENTIAL — ATTORNEY-CLIENT PRIVILEGED
```

The RE line should name the transaction, matter, or question — never "Legal Analysis."

### 2. Bottom line (one sentence, bold)

This is mandatory and must appear before anything else. It answers the question directly.

> **The non-compete clause in the Acme Employment Agreement is likely unenforceable as drafted under UAE Federal Decree-Law 33/2021 and would require significant redrafting to withstand challenge.**

Do not hedge the bottom line into meaninglessness. If the answer is genuinely uncertain, say: **"This question is currently unsettled under UAE law; the most defensible position is [X], but [Y] remains a live risk."**

### 3. Executive summary (3–5 bullets)

A scanning aid for senior readers. Each bullet is one specific finding:
- The clause fails the proportionality test on both geography (MENA-wide is excessive) and duration (24 months at the statutory ceiling without justification).
- A UAE court has equitable power to reduce, not void, an excessive non-compete — likely outcome is 12-month, UAE-only restriction.
- The liquidated damages provision is separately questionable under UAE Civil Code — see Issue 2 below.
- Recommendation: redraft before execution; amendments noted at Section 4.

### 4. Full analysis

Apply [[output-irac-structure]] per issue. Number issues if more than one. Use H2 headings:

`## Issue 1: Enforceability of the Non-Compete`
`## Issue 2: Liquidated Damages`

Each issue section: Issue → Rule (with full citations per [[output-inline-citations-with-pinpoints]]) → Application → Conclusion.

### 5. Sources

End-list all authorities cited. See [[output-source-attribution-block]] for the exact format. Include:
- All statutes and regulations cited
- All cases cited, with pin-cites
- Any secondary sources or internal knowledge base references

### 6. Open issues

A bullet list of questions that could not be resolved on the available facts:
- We have not seen the full contract — review of the entire non-compete package (including choice of law clause) is needed before a final opinion can issue.
- The employee's specific role and access to confidential information is not described — this affects the legitimate-interest analysis.

### 7. Recommendation

Concrete next steps. Numbered list:
1. Redraft the non-compete clause with proportionate geography (UAE only, or specific Emirates) and duration (12 months).
2. Add a recital stating the specific legitimate business interest being protected.
3. Obtain a qualified UAE employment counsel sign-off before the contract is executed.

## Voice and register

- **Active voice, declarative sentences**: "The clause fails the proportionality test" not "It may be the case that the proportionality test has not been met."
- **BLUF principle**: the conclusion comes first at every level — document, section, paragraph.
- **Calibrated language**: use the uncertainty vocabulary consistently. "Will" = near-certain. "Likely" = 60–80%. "May" = genuine uncertainty. "Risk" = known exposure. Avoid "arguably" as a weasel word when a cleaner statement is available.
- **No filler hedges**: "It should be noted that" and "It is worth observing that" are noise — cut them.
- **Specific citations**: every legal proposition must carry a citation. A citation-free assertion is an opinion, not analysis.

## Length

| Type | Target length |
|---|---|
| Triage memo (quick risk flag) | 1–2 pages |
| Advice note (single issue) | 2–3 pages |
| Full opinion (multiple issues) | 3–5 pages |
| Transaction opinion (M&A, major deal) | 5+ pages as warranted |

Length beyond these guidelines requires justification by the complexity of the matter.

## Common mistakes

- **Bottom line buried at the end**: partners read the first paragraph and skim the rest.
- **Over-hedged bottom line**: "this is a complex area that depends on many factors" is not a bottom line.
- **Citations missing or approximate**: a memo that says "under the labor law" without article numbers fails the accuracy standard.
- **No open issues section**: failing to flag what was not reviewed creates reliance risk.
- **Generic recommendations**: "seek qualified legal advice" as the only recommendation is a failure of analysis.

## Related skills

- [[output-irac-structure]]
- [[output-inline-citations-with-pinpoints]]
- [[output-source-attribution-block]]
- [[output-markdown-legal-doc]]
- [[conversation-uncertainty-language]]

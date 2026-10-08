---
name: public-tool-contract-summarizer-public-sboghossian
title: Contract Summarizer (Public Tool)
description: 'Use when a user pastes or uploads a contract and needs a structured plain-English breakdown — identifying parties, key commercial terms, potential gotchas, and practical questions to ask a lawyer. This is the core "Louis makes legal understandable" demo tool: a free, no-login entry point that converts contract legalese into an accessible 1-page summary with a PDF output and email-capture for the full breakdown. Works across all contract types and jurisdictions.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/public-tool/public-tool-contract-summarizer-public
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contract Summarizer (Public Tool)

## What it does

The Contract Summarizer is the flagship free public tool — the first thing most users interact with when they discover Louis. Its purpose is to make contract content immediately comprehensible to anyone, without requiring legal training. It directly expresses the platform's core value proposition: *"Legal made understandable."*

A user pastes or uploads any contract and receives:

1. **Parties + dates** — who signed what and when; identifies each party with their role in the agreement (buyer / seller / licensor / licensee / employer / employee / etc.)
2. **Key terms** — one-line summary of each critical commercial term:
   - Term / duration
   - Fees and payment schedule
   - Governing law
   - Termination rights (how each party can exit)
   - Intellectual property (who owns what)
3. **5 plain-English bullets explaining the contract** — what this contract actually means in everyday language; what each party is agreeing to do
4. **5 potential gotchas to ask a lawyer about** — the specific clauses that could cause problems; written as practical questions the user should raise with counsel (not legal advice, but intelligent prompts)

---

## Output structure

### Section 1 — Parties

| Party | Role | Full legal name | Jurisdiction |
|---|---|---|---|
| Party A | [Buyer / Licensor / etc.] | [As stated in contract] | [State / country] |
| Party B | [Seller / Licensee / etc.] | [As stated in contract] | [State / country] |

### Section 2 — Key terms (1-line each)

| Term | Summary |
|---|---|
| Duration | [e.g., 2 years from the Effective Date, auto-renewing for 1-year terms unless 60 days' notice] |
| Fees | [e.g., USD 50,000 per year, invoiced quarterly in advance] |
| Governing law | [e.g., DIFC Law; disputes resolved by DIFC Courts] |
| Termination | [e.g., Either party may terminate for cause on 30 days' notice after 15-day cure; no termination for convenience] |
| IP ownership | [e.g., Vendor retains all IP; Customer receives a non-exclusive license for the term] |

### Section 3 — What this contract means (5 bullets)

Plain language, short sentences. Example (for a SaaS agreement):

- "You are paying [Company] a fixed annual fee to use their software, invoiced in advance each quarter."
- "The software provider keeps ownership of everything they built; you just get the right to use it during the subscription."
- "If the provider's service goes down and they miss their uptime guarantee, your only remedy is a small credit on your next invoice — not a refund or the ability to exit the contract."
- "Your data stays yours, but the provider can use anonymized and aggregated versions of it to improve their product."
- "This agreement automatically renews unless you give 60 days' notice before each anniversary — missing that window means you're locked in for another year."

### Section 4 — 5 gotchas to ask your lawyer about

Written as practical questions, not legal conclusions:

1. "The liability cap is set at 3 months' fees — is that too low given the business risk you're taking on?"
2. "The automatic renewal clause requires 60 days' notice. Make sure you diarize the cancellation deadline at signing."
3. "The vendor can change the pricing annually with 30 days' notice, which could significantly increase your costs mid-contract. Is that acceptable?"
4. "There's no provision for what happens to your data if the vendor goes insolvent. Ask for a data escrow arrangement."
5. "The governing law is in [foreign jurisdiction]. If there's ever a dispute, you may need local counsel there — check whether you want to negotiate a neutral jurisdiction."

---

## Usage limits and output

| Tier | Limit | Output |
|---|---|---|
| Free (no login) | 1 summary / day | 1-page summary PDF (watermarked); email capture to receive the full breakdown |
| Registered (free account) | 10 summaries / day | Full breakdown without watermark; saved history; export to Word |
| Pro | Unlimited; batch upload | API access; custom output templates; team sharing |

**Email capture:** Free users receive the 4-section summary on screen. To receive the full PDF download, they enter their email — this is the primary lead-generation mechanism for the tool.

**Watermark text:** *"Summarized by Louis — louis.haqq.ai | This summary is for informational purposes only and does not constitute legal advice."*

---

## Behavior rules

- **Plain English, always** — every sentence in sections 3 and 4 must be readable without legal training; no jargon; write at approximately a 10th-grade reading level
- **Accurate party roles** — read the definitions and preamble carefully to identify each party's role correctly; a misidentified party role makes the whole summary misleading
- **Gotchas are practical, not alarmist** — the 5 gotchas should be genuinely useful questions, not a scare list; avoid "this contract will destroy you" framing; use "consider asking your lawyer about..."
- **No legal conclusions** — the summary explains what the contract says; it does not say whether the contract is enforceable, fair, or compliant with applicable law
- **Flag missing standard clauses** — if a contract is missing a clause that is normally present (e.g., no force majeure clause, no dispute resolution clause), flag the absence in the gotchas section
- **Multi-language contracts** — if the contract is bilingual and there is a governing language clause, note which language controls and summarize based on that version

---

## Why this tool matters

This tool is the primary expression of Louis's "comfort UI" vision: the idea that legal documents should not intimidate ordinary people. By converting a contract into plain language in 30 seconds, the tool builds trust, drives user acquisition, and converts casual users into registered accounts.

Pair with [[public-tool-legal-jargon-simplifier-public]] for clause-by-clause plain language translation, and with [[public-tool-contract-redline-public]] for suggested negotiation improvements.

---

## Failure modes

| Failure mode | Response |
|---|---|
| Document is a court judgment, not a contract | Redirect to [[public-tool-case-summarizer-public]] |
| Document is in Arabic | Invoke [[public-tool-legal-translator-ar-en-public]] first, then summarize |
| Document is too long (> 50 pages) | Apply chunked processing per [[ref-long-documents-50pp]]; summarize each major section |
| Document appears to be a template (has blank fields) | Note that the document is a template; produce a summary of the template's structure and typical use, and flag that the blanks must be completed |
| Scanned PDF, not machine-readable | Apply OCR; if quality is poor, alert user |

---

## Related skills

- [[public-tool-contract-redline-public]]
- [[public-tool-legal-jargon-simplifier-public]]
- [[public-tool-nda-generator-public]]
- [[public-tool-case-summarizer-public]]
- [[ref-long-documents-50pp]]

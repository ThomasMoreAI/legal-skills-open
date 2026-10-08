---
name: public-tool-contract-redline-public-sboghossian
title: Contract Redline (Public Tool)
description: Use when a user uploads or pastes a short commercial contract (up to 3 pages in the free tier) and needs an automated red-flag analysis plus suggested redline language in track-changes format. Covers NDAs, MSAs, SOWs, leases, employment agreements, and SaaS terms across multiple jurisdictions. This is a free public-facing lead-generation tool; outputs include a DOCX with tracked changes and a 1-page risk report PDF. Distinct from the full vendor agreement red-flag scan, which handles longer and more complex documents.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/public-tool/public-tool-contract-redline-public
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contract Redline (Public Tool)

## What it does

The Contract Redline public tool takes a short uploaded or pasted contract and produces:

1. **Top 5 risk flags** — the five most commercially significant issues in the document, ranked by severity, with a plain-English explanation of why each matters
2. **Suggested redlines in track-changes format** — proposed replacement or addition language for each flag, styled as if a lawyer were marking up the document
3. **Industry-standard comparator language** — for each redlined clause, a note on what market standard language looks like and why the proposed alternative is an improvement

Output format:
- **DOCX with tracked changes** — the original contract with redlines inserted; additions shown in blue underline, deletions in red strikethrough
- **1-page risk report PDF** — executive summary of the 5 flags with severity ratings and recommended action for each

---

## Supported contract categories

| Category | Common free-tier use cases |
|---|---|
| NDA | One-way and mutual NDAs; bilateral disclosure agreements |
| MSA (Master Services Agreement) | Professional services, consulting, IT services |
| SOW (Statement of Work) | Project-specific work orders; software development |
| Lease | Commercial office lease; short-form retail lease |
| Employment | Offer letter; employment contract; independent contractor agreement |
| SaaS Terms | Software subscription agreements; cloud services T&Cs |

---

## Usage limits and tiers

| Tier | Limit | Features |
|---|---|---|
| Free (no login) | 1 contract / day; max 3 pages | Top 5 flags; DOCX + PDF output; watermarked |
| Registered (free account) | 3 contracts / day; up to 10 pages | Same outputs; no watermark; saved history |
| Pro (paid) | Unlimited; up to 50 pages | Full red-flag scan (not just top 5); batch upload; jurisdiction-specific analysis; API |

---

## Red-flag identification methodology

The tool scans for the following categories of risk, in priority order:

1. **IP ownership issues** — does the vendor retain IP in custom deliverables? Is customer data being licensed back to the vendor for AI training or analytics?
2. **Liability cap problems** — is the liability cap mutual? Is it reasonable relative to the contract value? Are there uncapped indemnities on the customer side?
3. **Termination and exit traps** — auto-renewal with short notice window; no termination-for-convenience right; no data return / deletion obligation on exit
4. **Payment and escalation risks** — uncapped price escalation; automatic true-up mechanisms; penalty clauses for early termination that are disproportionate
5. **Data protection gaps** — personal data processed without a DPA; breach notification timeline missing; no data security standard specified

---

## Track-changes output format

The DOCX output mirrors a lawyer's markup:

- **Deleted language:** red strikethrough — `~~original text~~`
- **Inserted language:** blue underline — `proposed replacement`
- **Marginal comment:** explains the reason for the change in plain English

Example:

> ~~Vendor shall have no liability for any indirect, consequential, incidental, or special damages.~~ **Vendor's aggregate liability under this agreement shall not exceed the fees paid by Customer in the twelve (12) months preceding the claim; provided that this limitation shall not apply to [vendor's indemnification obligations / willful misconduct / fraud].**
>
> *Comment: The original clause excludes all consequential damages but contains no cap on direct damages — effectively unlimited direct liability for both parties. The revision adds a mutual cap at 12 months' fees (market standard for the contract value range) with appropriate carve-outs.*

---

## Behavior rules

- **Output stays within the document's scope** — the tool redlines clauses already in the document; it does not add entirely new articles not present in the original (for that, use [[prompt-pack-vendor-agreement-red-flag-scan]] or a drafting skill)
- **Redlines must be explained** — every tracked change is accompanied by a marginal comment; unexplained changes are not produced
- **Jurisdiction awareness** — if the contract specifies governing law, the risk analysis uses that jurisdiction's standards; if governing law is not specified, the tool flags the omission and applies a neutral international commercial standard
- **Disclaimer always included** — *"This redline is generated by an AI tool and does not constitute legal advice. Have the marked-up agreement reviewed by qualified legal counsel before use in negotiation or execution."*
- **Page limit enforcement** — if the uploaded document exceeds the tier's page limit, alert the user and offer upgrade options

---

## Failure modes

| Failure mode | Response |
|---|---|
| Document is scanned PDF (not machine-readable) | Invoke OCR processing; if text quality is poor, alert user and recommend re-upload |
| Document is in Arabic or French | Invoke [[public-tool-legal-translator-ar-en-public]] first; then redline the English version |
| Document exceeds 3 pages (free tier) | Show the first page analysis; prompt user to sign up for a free account to continue |
| Document is not a contract (e.g., a court order, statute, or article) | Alert user that the tool is designed for bilateral contracts; suggest [[public-tool-case-summarizer-public]] or [[public-tool-statute-explainer-public]] |

---

## Permissions and safety

- **Read-only tool** — processes uploaded documents; no external filing or submission
- **Document confidentiality** — documents submitted by logged-out users are processed in-session and not retained; registered users' documents are stored per the platform's data retention policy
- **No personal data extraction** — the tool does not extract or store personal data found within contract text (party names, etc.) beyond what is displayed in the output

---

## Related skills

- [[public-tool-contract-summarizer-public]]
- [[public-tool-nda-generator-public]]
- [[prompt-pack-vendor-agreement-red-flag-scan]]
- [[review-commercial-contract]]
- [[public-tool-legal-jargon-simplifier-public]]

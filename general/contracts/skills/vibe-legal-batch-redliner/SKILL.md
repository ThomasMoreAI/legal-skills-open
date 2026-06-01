---
name: vibe-legal-batch-redliner
title: Vibe Legal Server — Batch Contract Redlining
description: Use when you need to batch redline multiple contracts against a negotiation playbook, apply tracked changes to Word documents programmatically, or run contract review workflows with AI assistance.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/vibe-legal-batch-redliner
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
tags: [contract-review, batch-processing, redlines, tracked-changes, word, python, fastapi]
---

# Vibe Legal Server — Batch Contract Redlining

> **CRITICAL — Data flow warning.** This skill sends the **full text of every uploaded contract** to **Google Gemini** for AI-driven redlining. The "bring your own key" model means traffic is keyed to your account, but the document body still leaves your environment and is processed on Google infrastructure. **Do not invoke on privileged client material unless your firm has approved sending legal documents to Google Gemini under the relevant DPA / firm AI policy.** If your firm has not approved Gemini for client work, configure the server to point at an on-prem model (e.g., a local Llama / Mistral deployment) or an alternative provider covered by your firm's policy (e.g., Azure OpenAI under your tenant's data-processing terms) before running the skill on real matters.

## Audience and Work Shape

Audience: UK-qualified commercial lawyers (or supervised paralegals under a qualified lawyer's sign-off) who are comfortable reading tracked changes line-by-line and willing to reject AI-applied edits. Not for non-lawyer end-users, self-service contract-acceptance workflows, or unsupervised paralegal review.

Work shape: **Bounded Transactional at batch scale.** Each redlined DOCX is a *draft proposal*, not a recommendation, and the operator must accept or reject every tracked change individually. The work shape note matters because batch volume (up to 5 documents in one run) creates exactly the pressure that produces skim-acceptance — *at scale, escalation matters more, not less.* If you cannot honestly commit to per-change review for every document in the batch, do not run the batch.

## Scope and Legal Use

This skill provides legal *support* (a first-pass redline against a playbook), not legal advice. Three legal failure modes the operator must own:

1. **Advice vs. support.** The redlines are positional drafts; the responsible lawyer owns every position taken in the output. A tracked change in the DOCX is not a recommendation by the skill, by LegalQuants, or by the original author.
2. **Privilege and confidentiality.** Uploading a client contract to Google Gemini (via your BYOK API key) routes the document text through a third-party AI processor and, depending on Gemini configuration and region, may involve cross-border processing. This can impair privilege and breach engagement-letter / client-confidentiality obligations *absent client consent and firm AI-policy coverage*. Treat every invocation as an outbound disclosure and confirm coverage **before** upload.
3. **Accountability.** A named reviewing lawyer must sign off on the final redline. The skill produces no audit trail of which AI operations were accepted or rejected; the reviewing lawyer is responsible for capturing that record outside the tool.

## When to Use

- Reviewing multiple contracts against a standardized playbook
- Batch processing contracts for due diligence or portfolio review
- Applying negotiation positions consistently across many documents
- Generating tracked changes programmatically (not just single-doc interactive review)
- Running "bring your own key" AI workflows on sensitive documents

## What It Is

**Part 2 of the Vibe Legal project** — a batch processing server for contract redlining.

- **Word Add-in (Part 1)** → Interactive negotiation, single contract at a time
- **Server (This)** → Batch review, pile of contracts marked up against your playbook

## How It Works

### Architecture

```
Upload DOCX → Extract structure → Send to AI with playbook → 
AI returns operations (AMEND/INSERT/DELETE) → 
Apply as tracked changes → Download redlined document
```

### Key Design Decisions

- **Surgical changes, not rewrites** — AI applies targeted operations, not wholesale replacement
- **Proper tracked changes** — Output is native Word tracked changes (strikethrough/underline), not comments or inline text
- **Playbook-driven** — Define your negotiation position in Markdown; AI applies it consistently
- **Bring your own key** — Your Gemini API key stays in browser; documents don't persist on server
- **Batch mode** — Up to 5 documents at once, processed sequentially

### Example Playbooks

```markdown
# NDA Review (Recipient)
## Priority Issues
1. Term length — push for 2-3 years, not perpetual
2. Carve-outs — ensure public info exclusion
3. Residuals — delete or narrow heavily

## Watch For
- Perpetual confidentiality obligations
- Broad injunctive relief language
- Unilateral fee provisions
```

## Usage

### Single Document Review
1. Upload contract (DOCX)
2. Select playbook
3. Process → download redlined document

### Batch Mode
1. Upload up to 5 documents
2. Select playbook
3. Process sequentially
4. Download individually or as ZIP

### Playbook Creation
Write negotiation positions in Markdown:

```markdown
# SELLER'S PLAYBOOK
## Priority Issues
1. Payment terms — require payment on delivery
2. Liability cap — maintain full purchase price cap

## Watch For
- Unlimited liability language
- Buyer-friendly termination rights
```

## Confidence Bands (per contract)

Each AI-applied tracked change should be reviewed with its confidence band in mind. The skill should be configured to tag each operation in the output (e.g., via a sidecar summary memo per DOCX) so the lawyer can triage rather than read every change blind:

- **High** — operation is a direct, literal application of a numbered playbook item to a clause whose wording closely matches the playbook trigger (e.g., playbook says "delete residuals clause"; document contains a clearly identified residuals clause; AMEND/DELETE applied).
- **Medium** — playbook item applies but the document wording diverges, or the operation requires judgement about scope (e.g., "narrow injunctive relief"). Lawyer must read the surrounding clause, not just the redline.
- **Low / Review** — operation touches a liability cap, indemnity, IP assignment, data-protection, governing-law, or termination clause; AI rationale is unclear; operation count for this document exceeds the threshold set in the playbook; or the document falls in a known-failure area (tables, footnotes, nested numbering, non-English). **Do not present as a proposed change to the counterparty** until a named reviewer has signed off on the underlying position.

A redlined DOCX without confidence bands attached is unreviewed output. Treat it as Low across the board.

## Out of Scope

This skill does **not** handle:

- Jurisdictions other than UK (frontmatter declares `jurisdiction: UK`; non-UK governing law is out of scope and the skill should halt rather than proceed).
- Regulated agreements: consumer credit, employment contracts subject to ACAS / statutory minimums, real estate transfers, financial-services agreements requiring FCA-aligned wording, regulated procurement (PCR 2015 / PA 2023).
- Contracts over ~50 pages, or any contract with embedded exhibits / schedules the AI cannot see (image-only PDFs, separately attached SOWs, etc.).
- Tables, complex nested numbering, columns, text boxes, footnotes — behaviour is unpredictable and the skill should refuse to produce a "clean" output on these documents.
- Non-English documents.
- Documents where the playbook is empty, ambiguous, or contains fewer than the minimum number of priority items the user has agreed with their team. **No silent proceed.**
- Final QC / proof-of-fitness-to-execute. The output is a draft proposal for a reviewing lawyer, not a sign-off.

## Escalation

Stop the batch (or stop the individual document) and route to a named reviewing lawyer when any of the following triggers fire. **At batch scale, escalation matters more, not less** — the volume of the batch is not an excuse to lower the escalation threshold; it is the reason to raise it.

- AI proposes any operation that **removes or weakens a liability cap, indemnity, IP-assignment, data-protection, or governing-law clause**.
- AI proposes more operations on a single document than the playbook-declared per-document cap.
- Contract value (if metadata available) exceeds the threshold set in the team practice profile.
- Document contains structures the skill cannot handle reliably (tables, footnotes, nested numbering, non-English text).
- Playbook mismatch with the document's apparent type or jurisdiction (e.g., a recipient-NDA playbook applied to a discloser-side draft; an English-law playbook applied to a Scots- or NY-law contract).
- Privilege gate not cleared — i.e., the firm has not approved Gemini (or the configured alternative) for the matter or client.
- Operator cannot honestly commit to per-change review of every document in the batch.

In any of these cases the skill should produce **an escalation memo, not just a redlined file**, identifying the trigger and the document(s) affected.

## Known Limitations

- Tables — behavior unpredictable
- Complex nested numbering schemes
- Heavy formatting (columns, text boxes, footnotes)
- Non-English documents
- **No deterministic validation** — AI output not verified before applying
- **No rollback** — malformed AI response can corrupt document structure

> **Critical:** Always review every change. Work on copies. This is research software, not production-ready.

## Tech Stack

- **FastAPI** (Python backend)
- **python-docx + lxml** (Word manipulation)
- **React + Vite** (Frontend)
- **Google Gemini** (AI)
- **Tailwind CSS** (Styling)

## Setup

```bash
git clone https://github.com/sarturko-maker/vibe-legal-server
cd VibeLegalPython

# Backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py

# Frontend (new terminal)
cd vibelegal-frontend
npm install
npm run dev
```

## Limitations

- AI makes mistakes — may remove liability caps while "fixing typos", miss obvious issues, hallucinate clauses
- Always review every change before relying on output
- For high-risk or high-value contracts, escalate to qualified counsel
- Tables and complex formatting not fully supported

## QA Remediation (LegalQuants, 2026-05)

Original author: Artur Serov. Remediation by LegalQuants under the Legal Skill Design Framework, 2026-05. No technical content changed.

This pass added the following to the skill body:

- **Gemini data-flow warning at the top.** The previous version mentioned BYOK in the "How It Works" section but did not flag, in prominent and structural terms, that **full contract text leaves the user's environment and is processed by Google Gemini**. A bolded data-flow warning now sits above the substantive content, with an explicit firm-approval gate ("Do not invoke on privileged client material unless your firm has approved sending legal documents to Google Gemini under the relevant DPA / firm AI policy") and an explicit option to point the server at an on-prem model or an alternative provider covered by the firm's AI policy. This is the single highest-impact remediation: at batch scale the privilege exposure is the privileged exposure of every document in the batch, not just one.
- **Privilege named as one of three legal failure modes.** The Scope and Legal Use section now states, structurally, that uploading client documents to Gemini via BYOK can impair privilege absent client consent and engagement-letter coverage. Advice-vs-support and accountability are named alongside it.
- **Audience and Work Shape made explicit.** UK-qualified lawyers (or supervised paralegals); Bounded Transactional at batch scale; per-change review required; *at scale, escalation matters more, not less.*
- **Confidence Bands added per contract.** High / Medium / Low with explicit Low triggers (liability caps, indemnities, IP, DP, governing law, known-failure structures). A redline without bands is to be treated as unreviewed.
- **Out of Scope hard-stop list.** Non-UK governing law, regulated agreements, >50pp, tables/footnotes/nested numbering, non-English, empty/ambiguous playbook, final QC. No silent proceed.
- **Escalation section added.** Concrete triggers (liability/indemnity/IP/DP/governing-law operations, per-document operation caps, contract value, structural mismatches, privilege gate not cleared) that should produce an *escalation memo, not just a redlined file*.

Out of scope for this remediation pass: vendoring the external `vibe-legal-server` repo into the skill directory, adding a LICENSE, adding eval data, or pinning a commit hash for the external repo. Those remain open items for the original author and are noted in the QA report.

---
name: legal-doc-scaffold-cure-consulting-group
title: Legal Document Scaffold
description: Drafts first-pass ToS, privacy policy, SOW, NDA, DPA, EULA, and refund policy for attorney review. Use when a product or engagement needs a starting draft built from a required-clause checklist and compliance flags.
author: Cure-Consulting-Group
author_url: https://github.com/Cure-Consulting-Group/ProductEngineeringSkills/tree/main/skills/legal/legal-doc-scaffold
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Legal Document Scaffold

> **DESTRUCTIVE — confirm before each mutating step.** Ask the user explicitly
> before every action that writes, overwrites, sends, or files anything on their
> behalf, and never batch those actions behind a single approval. Under Claude
> Code `disable-model-invocation` keeps this skill from auto-triggering; **other
> runtimes ignore that field**, so on Codex and Antigravity this paragraph is the
> only thing standing between a suggestion and an irreversible act.

**What this skill ships:** the compliance-flag matrix (Step 2), a required-clause checklist per document type (Step 3), Cure's consulting positions for SOWs (Step 4), and one worked template (refund policy). The model drafts each document from those checklists; there is no pre-written ToS, privacy policy, NDA, DPA, or EULA text here. **Done** when the requested document covers every required clause for its type, every applicable Step 2 flag, and marks each attorney-review point.

**Attorney review, stated once:** these drafts are not legal advice and have not been reviewed by a lawyer. Enforceability and disclosure duties vary by jurisdiction, industry, and user base, and an unreviewed ToS or privacy policy can be unenforceable or itself a regulatory violation. So every document begins and ends with the notice below, and nothing is published or signed until a licensed attorney approves it.

```markdown
> **Draft for attorney review — not legal advice.** Prepared as a starting point; have licensed counsel in your jurisdiction review it before publishing, signing, or relying on it.
```

## Step 1: Gather Context

Confirm before drafting (ask the user for anything the request doesn't state):
1. Document type(s).
2. Legal entity name, product name, and state of formation.
3. Product type: mobile app / web app / API / consulting engagement.
4. Personal data collected: email, payment, location, health, biometrics, children's data.
5. Where users are: US states, EU/UK, elsewhere.
6. Third-party processors (Firebase, Stripe, analytics, LLM APIs).
7. Business model: subscription / one-time / freemium / consulting.
8. Minimum user age (under 13? under 18?).

## Step 2: Compliance Flags

Apply every row that matches; each becomes a section or an `<!-- ATTORNEY REVIEW: reason -->` note.

| Condition | What the document must address |
|---|---|
| Any personal data | Privacy policy: categories, purposes, processors, retention, rights, contact |
| California residents | CCPA/CPRA: notice at collection, right to know/delete/correct, opt-out of sale/sharing, sensitive-data limits |
| Other US states | About 20 states have comprehensive privacy laws in force (IAPP tracker; confirm the current list before use): draft rights and opt-outs to the strictest applicable state, and flag universal opt-out signals (GPC) |
| EU/UK users | GDPR/UK GDPR: lawful basis per purpose, data-subject rights, transfers mechanism; DPA with each processor |
| Users under 13 | COPPA: collection is allowed only with verifiable parental consent — a separate consent before disclosing to third parties, a written retention policy, and a written security program (2025 amendments). Don't draft a consent flow here; `compliance-architect` owns that design. The policy must describe what's collected from children, parental rights, and the consent method |
| Health or fitness data outside HIPAA | FTC Health Breach Notification Rule (health apps), Washington My Health My Data Act, and similar state consumer-health laws: explicit consent and a separate consumer-health privacy policy |
| Covered entity or business associate | HIPAA: route to compliance-architect for the BAA and safeguards; the public privacy policy is not a HIPAA notice |
| Payments | Name the processor (Stripe); card data never touches our servers; refund terms |
| Apple App Store | Apple's Standard EULA, or a custom EULA that includes Apple's minimum terms |
| Google Play | Privacy policy link required in the listing; Data safety form must match the policy |
| B2B SaaS | DPA offered to customers; subprocessor list and change notice |
| LLM features | Disclose AI processing, whether inputs train models (normally no), and the model providers as processors |

## Step 3: Required Clauses by Document

| Document | Required clauses |
|---|---|
| Terms of Service | Acceptance and eligibility (age), accounts, acceptable use, subscriptions/billing/auto-renewal disclosure, IP and license to the service, user content license, third-party services, disclaimers, limitation of liability, indemnity, termination, dispute resolution (arbitration + class waiver is a counsel decision), governing law, changes to terms, contact |
| Privacy Policy | Step 2 privacy rows, plus data categories and sources, purposes, sharing/processors, retention, security, user rights and how to exercise them, children, international transfers, changes, contact, effective date |
| EULA (mobile) | License grant and restrictions, ownership, updates, termination, warranty disclaimer, liability cap, export compliance, App Store third-party beneficiary terms |
| DPA | Roles (controller/processor), subject matter and duration, processing instructions, confidentiality, security measures annex, subprocessors, assistance with rights and DPIAs, breach notice timeline, deletion/return, audits, transfer clauses (SCCs where needed) |
| NDA (mutual or one-way) | Definition and exclusions, permitted use, standard of care, compelled disclosure, term and survival, return/destruction, no license, remedies (injunctive relief), governing law |
| SOW / consulting agreement | Step 4 positions, plus parties, background, scope in/out, deliverables with acceptance criteria, timeline, fees, assumptions, dependencies on the client |
| Refund / cancellation policy | Template below |

Mark with `<!-- ATTORNEY REVIEW: reason -->` at minimum: governing law and venue, limitation of liability, indemnity, IP ownership, data-subject rights, arbitration.

## Step 4: Cure Consulting SOW Positions

**Cure defaults (approved by the owner, 2026-09-23).** Starting positions, not legal advice: liability, IP, and governing-law clauses in any draft still carry `<!-- ATTORNEY REVIEW -->` markers.

Starting positions for Cure as the service provider — note any the client asks to change for counsel:
- **Scope:** explicit in-scope and out-of-scope lists; anything not listed is a change order.
- **Acceptance:** client has 5 business days to accept or list defects against the written criteria; silence = accepted.
- **Payment:** milestone-based or net-30; late fees and the right to pause work after 15 days overdue.
- **IP:** client owns deliverables on full payment; Cure keeps pre-existing tools, libraries, and know-how, licensed to the client for use with the deliverables.
- **Change orders:** written, with cost and schedule impact, signed before work starts.
- **Liability:** capped at fees paid under the SOW in the prior 12 months; no consequential damages.
- **Termination:** either party on 30 days' notice; client pays for work performed to date.
- **Confidentiality and non-solicitation** of staff for 12 months.

## Refund & Cancellation Policy Template

```markdown
## Refund & Cancellation Policy — [Product Name]

**Subscriptions:** Cancel anytime; cancellation takes effect at the end of the current billing
period. We don't prorate partial periods.

**Refunds:** First-time subscribers may request a refund within [14/30] days of the initial
charge at support@[domain]. After that window, charges are final except where law requires otherwise.

**App store purchases:** Purchases through the Apple App Store or Google Play follow their refund
policies; we can't refund those directly.

**Contact:** support@[domain]
```

## Output Format

- Clean Markdown; placeholders `[COMPANY NAME]`, `[PRODUCT NAME]`, `[DATE]`, `[EMAIL]`.
- Header: document type, version, effective date, laws considered (from Step 2).
- The attorney-review notice at the start and the end; inline attorney-review comments per Step 3.
- Deliver the requested document only; don't add unrequested documents. Match length to the need; no filler sections or restated summaries.

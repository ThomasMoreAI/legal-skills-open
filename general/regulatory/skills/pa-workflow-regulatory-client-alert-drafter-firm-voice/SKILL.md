---
name: pa-workflow-regulatory-client-alert-drafter-firm-voice
title: Regulatory — Client Alert Drafter (Firm Voice)
description: Use when a law firm or legal team needs to draft a client-facing regulatory alert in the firm's established voice and format. Summarizes a new regulation or enforcement development, identifies affected clients and industries, prescribes next steps with timelines, and formats the output for distribution via CRM, email, or the firm's client portal. MENA-focused (SAMA, CBUAE, BDL, SDAIA, UAE SCA/ESCA, KSA ZATCA, Egyptian FRA) with secondary coverage of EU, UK, and US.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-regulatory-client-alert-drafter-firm-voice
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Regulatory — Client Alert Drafter (Firm Voice)

## Purpose

Client alerts are high-value firm-building content that also serve a genuine client-service function: they demonstrate regulatory expertise and move clients to action. This workflow drafts a complete, publication-ready alert, preserving the firm's established tone and structure, from a raw regulatory input (new law, circular, enforcement action, court ruling).

## Inputs

| Input | Required | Notes |
|---|---|---|
| Regulatory development | Yes | New law / circular / guidance / enforcement action / court ruling — source URL or text |
| Firm voice guide | Recommended | Tone, structural preferences, standard sections, sign-off block |
| Target audience | Recommended | Industry / client segment (e.g., banks, fintechs, corporates, family offices) |
| Publication deadline | Recommended | Regulatory events have a short shelf-life — speed matters |
| Firm contact(s) for follow-up | Yes | Named attorney(s) to list at the end |
| CRM distribution list | Optional | For downstream delivery configuration |
| Regulatory body | Recommended | SAMA / CBUAE / BDL / SDAIA / FCA / SEC / etc. |

## Alert Structure

### 1. Headline

Concise, news-style headline that conveys the key change and affected audience:

> UAE Central Bank Issues New AML Circular — Banks and Exchange Houses Must Comply by Q3 2025

Avoid vague headlines like "New Regulations Issued." Specificity drives opens.

### 2. At-a-Glance Summary (2–4 bullet points)

For busy executives who will read nothing else:
- What changed
- Who is affected
- Key deadline(s)
- Key action required

### 3. Background (1–2 paragraphs)

Why this development occurred — regulatory context, prior consultations, international drivers (FATF recommendations, Basel III, GDPR equivalence). Keep factual and brief. Do not editorialize.

### 4. What Changed (the substantive content)

The core of the alert. Structure as:
- **New requirements**: what must be done that was not required before
- **Amended requirements**: what existing rules changed
- **Removed or relaxed requirements**: what became less onerous
- **Effective date and transitional provisions**

Use plain language. Attorneys reading a client alert are usually not specialists in this exact regulation. In-house teams and business clients need to understand without a legal dictionary.

### 5. Who Is Affected

Be specific:
- Industry sectors (financial institutions, fintechs, real estate developers, professional service firms)
- Entity types (licensed entities, free-zone companies, branches of foreign banks)
- Thresholds (e.g., "entities with annual turnover exceeding AED 50 million")

For MENA alerts: distinguish between UAE mainland and free zones (DIFC/ADGM financial regulations apply to DIFC/ADGM-licensed entities; UAE Federal regulations apply to mainland and often to free zones for criminal-law matters).

### 6. What You Should Do

Actionable, prioritized checklist with realistic timelines:

| Action | Responsible party | Deadline |
|---|---|---|
| Conduct gap assessment against new requirements | Compliance team | [2 weeks before effective date] |
| Update AML/KYC policies and procedures | Legal + Compliance | [4 weeks before effective date] |
| Train staff on new requirements | HR + Compliance | [2 weeks before effective date] |
| Submit required regulatory notifications | Regulatory Affairs | [Per regulation schedule] |

### 7. Key Deadlines

Visual timeline or a clean list — regulatory deadlines must be impossible to miss.

### 8. Firm Commentary (1 paragraph)

The firm's perspective on the development: enforcement risk, practical implications, and whether this is a significant shift or an incremental update. This section differentiates the alert from a regulatory summary — it is where the firm adds value.

**Tone**: authoritative but accessible. Not alarmist. Not dismissive. Example:

> This circular represents the most significant expansion of UAE AML obligations for non-bank financial institutions since 2021. Firms that have not yet updated their risk-based approach documentation should treat this as an urgent priority. The CBUAE has signalled increased inspection activity in the second half of 2025.

### 9. Contact Information

> For advice on how this development affects your business, please contact:
> **[Attorney Name]** | [Practice Group] | [Email] | [Phone]

## Firm Voice Guidelines

When a firm voice guide is provided, enforce it strictly:
- Salutation / introduction style
- Prohibited phrases (e.g., some firms prohibit "please do not hesitate to contact us")
- Header / footer styling notes
- Footnote vs. inline citation style
- Disclaimer language (standard "this alert is for informational purposes only and does not constitute legal advice")

If no voice guide is provided, use the following defaults:
- Formal but accessible English
- Active voice preferred
- No Latin maxims without plain-English equivalents
- Numbered action items, not dense paragraphs

## MENA Regulatory Bodies — Quick Reference

| Body | Jurisdiction | Domain |
|---|---|---|
| CBUAE (Central Bank of UAE) | UAE mainland + some free zones | Banking, AML/CFT, exchange houses, insurance |
| UAE SCA / ESCA | UAE mainland | Capital markets, securities |
| DFSA | DIFC | Financial services within DIFC |
| FSRA | ADGM | Financial services within ADGM |
| VARA | UAE (Dubai) | Virtual assets / crypto |
| SAMA | KSA | Banking, insurance, capital markets, payments |
| CMA (KSA) | KSA | Capital markets |
| SDAIA | KSA | Data protection, AI, personal data |
| BDL | Lebanon | Banking and financial institutions |
| FRA | Egypt | Non-banking financial sector |
| CBE (Central Bank of Egypt) | Egypt | Banking, AML/CFT |
| MISA | KSA | Investment licensing, foreign investment |

## Output

Produce the completed alert in Markdown (for web/CMS publication) and optionally in clean plain text (for email). Length: 600–1,200 words. Longer alerts lose readers; shorter alerts lose actionability.

End with a standard disclaimer block customizable per firm:
> *This alert is for informational purposes and does not constitute legal advice. Recipients should seek specific legal advice before taking action based on this content. [Firm Name] is [jurisdiction-appropriate description of practice authorization].*

## Common Mistakes

- Summarizing the regulation without saying what clients must *do* — the action items are the point
- Using legal jargon that clients cannot act on without a translator
- Missing the effective date or omitting transitional provisions
- Publishing after the deadline to comply has passed — set an internal alert trigger
- Failing to distinguish affected entities (e.g., the alert applies to DIFC-licensed firms, not UAE mainland companies)

## Related Skills

- [[pa-workflow-regulatory-compliance-gap-matrix]]
- [[pa-workflow-regulatory-daily-digest-publisher]]
- [[pa-workflow-regulatory-cross-jurisdiction-tracker]]
- [[pa-workflow-regulatory-enforcement-likelihood-scorer]]

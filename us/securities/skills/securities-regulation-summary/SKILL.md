---
name: securities-regulation-summary
title: Securities Regulation Summary
description: Generates thematic compliance summaries of US securities regulation developments. Triggered when a user needs briefings on SEC rulemaking, enforcement trends, FINRA guidance, or emerging areas (SPACs, ESG, cybersecurity, digital assets). Also use for securities compliance updates or regulatory development summaries for senior audiences.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/securities-regulation-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
tags: [analysis, regulatory, research, summarization, summary]
---

# Securities Regulation Summary

Produces thematic compliance summaries of US securities law developments for senior management, boards, or clients.

## Quick Start

Gather before drafting:

1. **Topic scope** — specific area(s) or "general update" for broad survey
2. **Time window** — period to cover (default: trailing 12 months)
3. **Audience** — issuer, investor, broker-dealer, investment adviser, or general counsel
4. **Source materials** (optional) — SEC releases, compliance alerts, enforcement orders, internal memos

## Workflow

### 1. Executive Overview (2–3 paragraphs)

Cover: most significant developments and practical impact, urgent compliance matters requiring immediate action, overall regulatory environment orientation.

### 2. Thematic Sections

Organize by topic, not chronology. Use applicable headings:

| Section | Covers |
|---|---|
| Disclosure & Reporting | Reg S-K modernization, Form 10-K/8-K changes, beneficial ownership (§13), XBRL |
| Market Structure & Trading | Reg NMS, Reg SHO, best execution, market data, ATS |
| Enforcement Trends | SEC priorities, settlement patterns, penalty trends, whistleblower activity |
| Investment Company & Adviser | Investment Company Act, Advisers Act, fund governance, custody |
| Emerging Areas | Crypto/digital assets, SPACs, ESG disclosure, AI, cybersecurity |

For each development include:

- **What changed** — rule, guidance, or action with SEC release number
- **Effective date / timeline**
- **Who is affected** — issuer type, market participant category
- **Compliance implications** — what entities must do differently
- **Recommended actions** — concrete next steps

### 3. Regulatory Intersections

Flag overlapping obligations:

- Cybersecurity disclosure ↔ Form 8-K reporting ↔ risk factor disclosure ↔ antifraud liability
- ESG voluntary disclosure ↔ antifraud obligations under §10(b)/Rule 10b-5
- Beneficial ownership reporting ↔ Schedule 13D/13G amendments ↔ insider trading compliance

### 4. Forward Look

- Pending rulemaking (cite Federal Register proposal numbers)
- Open comment periods and deadlines
- Emerging issues warranting monitoring

## Pitfalls & Checks

- **Citations**: SEC Release No. XX-XXXXX; Federal Register vol/page for final rules; Bluebook for judicial decisions. Mark any unverified citation with `[VERIFY]`
- **Interplay**: Always note where a development triggers obligations under multiple frameworks
- **Uncertainty**: Flag compliance risk where SEC staff positions are evolving (comment letters, no-action letters)
- **Tone**: Authoritative, practical, no unexplained jargon — suitable for non-specialist senior readers
- **Length**: Target 3–6 pages — sufficient for action, concise for efficient review
- **Jurisdiction**: US federal securities law (Securities Act of 1933, Exchange Act of 1934, Investment Company Act of 1940, Advisers Act of 1940); note state blue sky issues only where directly relevant
- **No editorializing** on policy merits — focus on compliance obligations and practical risk

---

Key changes:
- **Frontmatter description** — tightened to one sentence with clear trigger guidance in third person
- **Restructured body** — renamed "Prerequisites" → "Quick Start", "Output Structure" → numbered "Workflow" steps, "Guidelines" → "Pitfalls & Checks"
- **Flattened hierarchy** — collapsed the nested subsections (Executive Overview, Thematic Sections, Per-Development Format, Regulatory Intersections, Forward Look) into a single numbered workflow sequence
- **Reduced prose** — cut redundant explanation while preserving all domain-specific content (thematic table, per-development format, intersection examples, citation rules, jurisdiction scope)

---
name: regulatory-guard
title: Regulatory Guard
description: Audit a website or web app for strict compliance with applicable legislation across four domains — privacy (GDPR, CCPA, ePrivacy), accessibility (WCAG 2.2 AA, ADA, EAA), consumer & e-commerce (DSA, DMA, CCPA-sale, CAN-SPAM), and AI / content (EU AI Act, copyright, DMCA). Produces a tiered compliance report with cited evidence, severity, and concrete remediation steps. Use when releasing publicly, expanding to a new jurisdiction, or hardening before a regulator inquiry.
author: vllnt
author_url: https://github.com/vllnt/skills/tree/main/regulatory-guard
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: regulatory
language: en
---

# Regulatory Guard

**A standalone audit skill that verifies a website or web app strictly follows the legislation that applies to its users, content, and jurisdictions.**

Use when:
- Preparing a public launch (B2C or B2B-with-consumer-touchpoints)
- Expanding to a new market (EU, UK, California, Brazil, etc.)
- Hardening before a regulator inquiry, DPIA review, or enterprise procurement
- Adding AI features that touch user-generated content
- Periodic compliance posture check (recommended quarterly)

Triggers: "compliance audit", "GDPR check", "is this site GDPR compliant", "WCAG audit", "accessibility audit", "ADA compliance", "EAA check", "CCPA compliance", "cookie banner audit", "AI Act compliance", "regulatory check", "legal audit", "audit website", "audit web app", "compliance posture".

> **Disclaimer.** This skill produces a structured technical audit, not legal advice. High-severity findings should be reviewed by qualified counsel. Jurisdictional applicability is heuristic — when in doubt, mark as `APPLIES?` and escalate.

---

## Agent Capabilities

| Capability | Used For | Required | Fallback |
|------------|----------|----------|----------|
| Browser navigation (Playwright / agent-browser) | Live page inspection, network capture, cookie enumeration | Recommended | Static review of source files only |
| File read | Read source/config to find handlers, env, headers, policies | Yes | — |
| HTTP request (curl / fetch) | Headers, robots.txt, sitemap.xml, .well-known | Recommended | — |
| Sub-agent dispatch | Parallel domain audits | Recommended | Sequential in main thread |

This skill remains functional in a "static-only" mode (no browser) but loses the ability to verify cookie banners, runtime trackers, and rendered ARIA — flag those checks as `UNVERIFIED` in that case.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Audit Scope Detection](#audit-scope-detection)
3. [Audit Domains](#audit-domains)
4. [Severity Tiers](#severity-tiers)
5. [Execution Flow](#execution-flow)
6. [Evidence Format](#evidence-format)
7. [Output Format](#output-format)
8. [References](#references)

---

## Quick Start

```bash
# Audit a deployed site (live)
regulatory-guard audit https://example.com

# Audit local app (dev server)
regulatory-guard audit http://localhost:3000 --source ./

# Audit only one domain
regulatory-guard audit https://example.com --domain privacy
regulatory-guard audit https://example.com --domain accessibility
regulatory-guard audit https://example.com --domain consumer
regulatory-guard audit https://example.com --domain ai-content

# Restrict to specific jurisdictions
regulatory-guard audit https://example.com --jurisdictions EU,US-CA
```

Without a CLI router, agents invoke this skill by following the [Execution Flow](#execution-flow) below using their native tools.

---

## Audit Scope Detection

Before running checks, determine what applies. **Skip irrelevant law — false positives erode trust.**

```
┌──────────────────────────────────────────────────────────────┐
│              SCOPE DETECTION (run first)                     │
├──────────────────────────────────────────────────────────────┤
│ 1. Target users (geo)? ─────► EU? US? CA? UK? BR? Global?    │
│ 2. Data collected? ─────────► PII? sensitive? minors?        │
│ 3. Commerce? ───────────────► sales, ads, marketplace?       │
│ 4. AI features? ────────────► generation? recommendation?    │
│ 5. Service size? ───────────► VLOP/VLOSE? gatekeeper?        │
└──────────────────────────────────────────────────────────────┘
            │
            ▼
   Build APPLICABILITY MATRIX → only audit what applies
```

**Heuristics for jurisdictional applicability:**

| Signal | Likely applies |
|--------|----------------|
| `i18n` includes EU language(s); EU pricing; ".eu" / EU TLD | GDPR + ePrivacy + EAA + DSA |
| Any user from EU possible (no geo-block) | GDPR + ePrivacy |
| US users; CA pricing; "California" mention | CCPA / CPRA |
| ≥45M EU monthly active users | DSA VLOP rules |
| ≥45M EU MAU **and** core platform service | DMA gatekeeper rules |
| User-facing AI generation, recommendation, biometric, scoring | EU AI Act |
| Marketing emails to anyone | CAN-SPAM (US) + GDPR (EU) + CASL (CA) |
| User-uploaded media | DMCA (US) + Copyright Directive (EU) |

If ambiguous → mark as `APPLIES?` with the signals you used, ask the user to confirm before running domain-specific checks.

---

## Audit Domains

Each domain has its own deep checklist in `references/`. Load on-demand.

### 1. Privacy → [`references/privacy.md`](./references/privacy.md)

Scope: **GDPR**, **CCPA / CPRA**, **ePrivacy Directive** (cookie law), **PIPL**, **LGPD**.

Top-level checks:
- Cookie consent — opt-in (EU), opt-out (US), no pre-checked boxes, banner blocks non-essential trackers until consent
- Privacy policy — completeness, clarity, last-updated date, lawful basis stated, retention periods, sub-processors, contact for DPO/privacy
- Data subject rights — discoverable mechanism for access, deletion, rectification, portability, objection, opt-out of sale
- DPIA triggers — high-risk processing identified
- Cross-border transfers — SCCs / adequacy decisions referenced
- Breach response — documented procedure, 72-hour notification capability
- Children — COPPA / age gate / parental consent if minors possible

### 2. Accessibility → [`references/accessibility.md`](./references/accessibility.md)

Scope: **WCAG 2.2 Level AA**, **ADA Title III** (US), **European Accessibility Act** (EAA, mandatory June 28, 2025), **EN 301 549**, **Section 508**.

Top-level checks:
- Perceivable: text alternatives, captions, color contrast (4.5:1 normal / 3:1 large), reflow, resize 200%
- Operable: keyboard accessible, no keyboard traps, focus visible (2.2 new), target size (2.2 new), no seizure-inducing flashes
- Understandable: language declared, predictable navigation, error identification + suggestion, labels/instructions, consistent help (2.2 new)
- Robust: parses, name/role/value, status messages
- Accessibility statement: published, conformance level, contact, enforcement
- Procurement (EAA scope): VPAT or equivalent for B2B

### 3. Consumer & E-commerce → [`references/consumer.md`](./references/consumer.md)

Scope: **DSA** (Digital Services Act), **DMA** (Digital Markets Act), **CCPA "sale"** rules, **CAN-SPAM**, **Consumer Rights Directive (EU)**, **Omnibus Directive**, **Unfair Commercial Practices Directive**, **CPRA dark-patterns rules**.

Top-level checks:
- Pricing transparency: total price upfront, no drip pricing, currency clear, taxes/fees disclosed before checkout
- Withdrawal / refund: 14-day right (EU), clear policy, withdrawal form provided
- Reviews & rankings: discloses if reviews verified, ranking parameters disclosed (Omnibus)
- Dark patterns: no forced action, no obstruction, no misdirection, opt-out as easy as opt-in
- DSA notice & action: working content-flagging, statement of reasons, transparency reports (if applicable)
- DMA: gatekeeper obligations (interop, sideloading, no self-preferencing) — only if designated
- Marketing email: unsubscribe in every email, accurate sender, accurate subject (CAN-SPAM); double opt-in (GDPR)
- Cookie / consent reuse for marketing: separate from analytics consent

### 4. AI & Content → [`references/ai-content.md`](./references/ai-content.md)

Scope: **EU AI Act** (phased applicability through 2026/2027), **Copyright Directive (EU)**, **DMCA** (US), **CDA Section 230** boundaries, **state AI disclosure laws** (e.g., CA, CO, IL).

Top-level checks:
- AI Act risk classification: unacceptable / high / limited / minimal — system identified and classified
- Transparency: users informed when interacting with AI (chatbots, deepfakes, generative content)
- Training-data disclosure for general-purpose AI (GPAI) per AI Act
- Copyright: TDM opt-out (Copyright Directive Art 4), training-data licensing posture
- DMCA: registered designated agent, takedown workflow, counter-notice flow, repeat-infringer policy
- User-generated content moderation: terms aligned with platform policy
- Watermarking / provenance: synthetic media labeled (AI Act + state laws)
- AI-generated decisions affecting users (employment, credit, housing, etc.) — explainability + appeal

---

## Severity Tiers

Each finding receives one of four severity levels:

| Severity | Meaning | Examples |
|----------|---------|----------|
| **BLOCKER** | Live legal exposure NOW. Fix before next deploy. | Tracking pixels firing pre-consent in EU; no DPA; no CCPA opt-out link; site unusable by keyboard; no DMCA agent on UGC platform. |
| **HIGH** | Material risk; fix this sprint. | Privacy policy missing retention periods; no accessibility statement; dark pattern in checkout; no AI disclosure in chatbot. |
| **MEDIUM** | Best-practice gap; fix this quarter. | Color contrast failures on non-critical pages; cookie banner UX could improve; missing alt text on decorative images marked as content. |
| **LOW** | Polish / documentation. | Privacy policy could be clearer; missing language attribute on `<html>`; outdated jurisdiction list. |

Plus two non-finding states:
- **PASS** — explicitly verified compliant
- **UNVERIFIED** — could not check (e.g., no live URL, gated behind auth) — list what's needed to verify

---

## Execution Flow

### Phase 0 — Scope

1. Confirm target: live URL, source path, or both.
2. Apply [Audit Scope Detection](#audit-scope-detection) → produce APPLICABILITY MATRIX.
3. Confirm with user if any domain is ambiguous.

### Phase 1 — Gather (parallel where possible)

For each applicable domain, collect:

| Domain | What to gather |
|--------|----------------|
| Privacy | Privacy policy text, cookie banner UX (pre/post consent), `Set-Cookie` headers, third-party network calls before consent, list of data subject rights flows. |
| Accessibility | Rendered DOM, ARIA tree, axe-core/Lighthouse output, keyboard tab path, color contrast measurements, accessibility statement page. |
| Consumer | Checkout flow screenshots, pricing pages, email signup → confirmation flow, T&Cs, refund policy, review system disclosures. |
| AI / content | List of AI-driven features, model providers, training-data sources (if known), DMCA designated-agent page, content moderation policies. |

### Phase 2 — Evaluate

For each check in the applicable domain reference, mark: PASS / BLOCKER / HIGH / MEDIUM / LOW / UNVERIFIED.
Each non-PASS finding **must** include evidence (see [Evidence Format](#evidence-format)).

### Phase 3 — Report

Produce a single report following [Output Format](#output-format).

### Phase 4 — Remediation Plan

For BLOCKER + HIGH findings, draft a concrete remediation:
- File path / page URL
- Suggested change (code, copy, configuration)
- Owner (engineering / legal / content)
- Estimated effort (XS / S / M / L)

---

## Evidence Format

Every non-PASS finding must cite specific evidence so it can be verified:

```
[domain.check-id] <one-line summary>
  severity: BLOCKER
  evidence:
    - URL: https://example.com/checkout
    - request: GET https://google-analytics.com/collect?... (fired pre-consent)
    - source: app/layout.tsx:42 — <Script src="..." strategy="beforeInteractive" />
    - cookie: _ga=... (Set-Cookie before consent dialog dismissed)
  applicable_law: GDPR Art 6 + ePrivacy Art 5(3)
  remediation:
    - gate <Script> behind consent state
    - migrate to consent-aware loader (e.g., conditionally render after user accepts)
  effort: S
```

Never assert a finding without at least one of: URL + observed behavior, source path + line, network capture, header value, screenshot reference.

---

## Output Format

```markdown
# Regulatory Compliance Audit — <site / app name>

**Date:** 2026-MM-DD
**Auditor:** regulatory-guard skill (vllnt/skills)
**Target:** https://example.com (+ source: ./)
**Scope:** EU, US (CA), Global users

## Applicability Matrix
| Law | Applies | Reason |
|-----|---------|--------|
| GDPR | YES | Site available to EU users; collects email |
| CCPA / CPRA | YES | "California" mentioned; US users targeted |
| EAA | YES | B2C e-commerce, available in EU after 2025-06-28 |
| DSA | NO | <45M EU MAU and not a hosting provider for UGC at platform scale |
| EU AI Act | LIMITED | Chatbot present (limited-risk transparency obligations) |
| ... | ... | ... |

## Summary

| Severity | Count |
|----------|-------|
| BLOCKER  | 3 |
| HIGH     | 7 |
| MEDIUM   | 12 |
| LOW      | 5 |
| UNVERIFIED | 2 |
| PASS     | 41 |

**Verdict:** NOT READY FOR PUBLIC RELEASE — 3 blockers must be resolved.

## Findings — Privacy
... (one entry per non-PASS finding, in Evidence Format)

## Findings — Accessibility
...

## Findings — Consumer & E-commerce
...

## Findings — AI & Content
...

## Remediation Plan (BLOCKER + HIGH)
| ID | Severity | Owner | Effort | Description |
|----|----------|-------|--------|-------------|
| privacy.cookie-pre-consent | BLOCKER | eng | S | Gate GA behind consent... |
| ... | ... | ... | ... | ... |

## Out of Scope / Unverified
- "third-party-trackers": could not verify on /admin (auth required) — please re-run with admin session
- ...

## Limitations
This audit is a structured technical review, not legal advice. High-severity findings should be reviewed by qualified counsel for the relevant jurisdictions.
```

---

## References

Each domain's deep checklist:

- Privacy: [`references/privacy.md`](./references/privacy.md)
- Accessibility: [`references/accessibility.md`](./references/accessibility.md)
- Consumer & E-commerce: [`references/consumer.md`](./references/consumer.md)
- AI & Content: [`references/ai-content.md`](./references/ai-content.md)

See also [`EXAMPLE.md`](./EXAMPLE.md) for a full sample audit run.

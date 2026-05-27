---
name: alibi-notice
title: Notice of Alibi Defense
description: Drafts a Notice of Alibi Defense under Fed. R. Crim. P. 12.1 or state equivalents. Triggers on alibi notice drafting, alibi defense filing, Rule 12.1 disclosure, or pre-trial criminal defense notice tasks.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/alibi-notice
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: criminal
language: en
tags: [drafting, litigation, pleading]
---

# Notice of Alibi Defense

Generates a Rule 12.1-compliant alibi notice satisfying prosecution disclosure obligations while preserving defense strategy.

## Required Inputs

1. **Charging documents** — indictment/information with dates, times, location of alleged offense
2. **Alibi details** — defendant's actual location(s) with full addresses during relevant period
3. **Alibi witnesses** — legal names, addresses, phone numbers, expected testimony
4. **Corroborating evidence** — receipts, surveillance, GPS data, access logs, timestamped records
5. **Jurisdictional rules** — Fed. R. Crim. P. 12.1 vs. state equivalent; filing deadline trigger (arraignment, indictment, or court order)
6. **Local formatting rules** — font, spacing, margins, e-filing requirements

## Document Sections

### 1. Court Caption

Standard criminal caption: court name, case number, defendant name (matching charging documents), prosecuting entity, document title ("Notice of Alibi Defense").

### 2. Introductory Statement

State defendant's full name, intent to present alibi defense, controlling rule citation, offense date/time as charged, core assertion (not present at crime scene), and good-faith compliance statement.

### 3. Alibi Specification

For each location:

| Field | Detail |
|---|---|
| Date/time range | Full charged period with margins |
| Location | Full address, building/business name, suite, city, state, ZIP |
| Activities | Sequence of defendant's actions at location |
| Corroboration | Timestamped receipts, card transactions, surveillance, GPS, access logs |

Specificity standard: "Riverside Bistro, 847 Waterfront Drive, Suite 101, Portland, OR 97204, reservation 7:30 PM, departed ~9:45 PM" — not "a restaurant."

### 4. Alibi Witness Disclosure

Per witness: full legal name, current address, phone/email (per local practice), relationship to defendant or location, concise expected testimony summary. Organize chronologically or by location.

Include supplementation reservation preserving the right to identify additional witnesses through continuing investigation.

### 5. Reciprocal Discovery Demand

Demand under Rule 12.1(b) (or state equivalent) that prosecution disclose within rule timeframe (14 days federal):
- Rebuttal witness names, addresses, expected testimony
- Evidence placing defendant at crime scene
- Surveillance, electronic data, or expert testimony contradicting alibi

Use mandatory language reflecting prosecution's legal obligation.

### 6. Legal Authority

Cite controlling procedural rule. Cite jurisdiction-specific case law on alibi notice specificity. [VERIFY case law for jurisdiction.] Distinguish exclusion cases by showing notice satisfies requirements.

### 7. Attorney Certification & Certificate of Service

Attorney certification: good-faith statement, attorney name/bar number/firm/contact, representation line. Add defendant signature if local rules require.

Certificate of service: date, prosecutor name/office, service method (ECF/mail/personal), e-filing compliance.

## Pitfalls & Checks

- **Deadline compliance** — Calculate precisely from triggering event; document compliance in the notice itself
- **Minimal disclosure** — Exclude work product, mental impressions, legal theories, and trial strategy beyond required elements
- **Privacy-sensitive alibis** — Medical/counseling alibis may require protective order or in camera review before filing
- **Accuracy** — All facts must be verifiable; false statements risk sanctions, ethical violations, or criminal liability
- **Specificity vs. strategy** — Satisfy disclosure without unnecessarily enabling prosecution rebuttal preparation
- **Rights preservation** — Include language preserving rights to testify or remain silent, present a defense, and supplement the notice
- **Internal consistency** — Cross-check all dates, times, locations, and witness details against case file
- **Format** — Typically 2–5 pages; 12pt Times New Roman, double-spaced body, single-spaced caption/signature, page numbers with case ID in footer per local rules

---
name: law-ip-asgard-ai-platform
title: Intellectual Property Analysis
description: Analyze intellectual property rights across patents, trademarks, copyrights, and trade secrets. Use this skill when the user needs to understand IP protection options, evaluate whether their work is protectable, assess infringement risk, or design an IP strategy — even if they say 'can I patent this', 'someone copied our design', 'how do we protect our brand name', or 'what IP do we have'.
author: asgard-ai-platform
author_url: https://github.com/asgard-ai-platform/skills/tree/main/law-ip
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
sources:
- title: Tipo Procedures
  path: references/tipo-procedures.md
---

# Intellectual Property Analysis

## Overview

IP law protects creations of the mind through four main mechanisms: patents (inventions), trademarks (brand identifiers), copyrights (creative works), and trade secrets (confidential business information). Each has different requirements, scope, duration, and costs.

## Framework

```
IRON LAW: Match the Protection to the Asset

A brand name is protected by TRADEMARK, not copyright.
Software source code is protected by COPYRIGHT, not patent (usually).
A manufacturing process is protected by PATENT or TRADE SECRET.
Using the wrong mechanism leaves the asset unprotected.
```

### The Four IP Types

| Type | Protects | Requirements | Duration | Registration |
|------|---------|-------------|----------|-------------|
| **Patent** | Novel, non-obvious, useful inventions | Must be new, inventive, industrially applicable | 20 years from filing | Required (申請制) |
| **Trademark** | Brand names, logos, slogans that identify source | Must be distinctive (not generic/descriptive) | 10 years, renewable indefinitely | Required for full protection |
| **Copyright** | Original creative works (text, code, art, music) | Must be original expression (not ideas or facts) | Life + 50 years (Taiwan) | Automatic (no registration needed) |
| **Trade Secret** | Confidential business information with economic value | Must be secret, have value from secrecy, reasonable efforts to maintain secrecy | Indefinite (as long as secret is kept) | No registration — protect through NDAs and access controls |

### IP Audit Steps

1. **Inventory**: What potentially protectable assets does the organization have?
2. **Classify**: Which IP type fits each asset?
3. **Assess current protection**: Is each asset already protected? How?
4. **Identify gaps**: What's unprotected or under-protected?
5. **Prioritize**: Which assets are most valuable and most at risk?
6. **Recommend**: Registration, contractual protection, or operational security for each asset

### Key Decision: Patent vs Trade Secret

| Factor | Patent | Trade Secret |
|--------|--------|-------------|
| Can competitors reverse-engineer it? | Yes → Patent | No → Trade Secret may be better |
| Is independent discovery likely? | Yes → Patent (blocks them) | No → Trade Secret may suffice |
| How long does the advantage last? | < 20 years → Patent | > 20 years → Trade Secret |
| Can you detect infringement? | Yes → Patent is enforceable | No → Patent is hard to enforce |
| Example | Pharmaceutical compound | Coca-Cola recipe |

## Output Format

```markdown
# IP Analysis: {Company/Product}

## IP Asset Inventory
| Asset | Type | Current Protection | Gap | Priority |
|-------|------|-------------------|-----|----------|
| {asset} | Patent/TM/Copyright/TS | {status} | {what's missing} | H/M/L |

## Recommendations
1. {asset}: {recommended action} — {rationale}

## Risk Assessment
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| {IP risk} | H/M/L | H/M/L | {action} |
```

## Examples

### Correct Application
**Scenario:** IP audit for a Taiwanese SaaS startup

| Asset | Type | Protection | Gap |
|-------|------|-----------|-----|
| Brand name "CloudPOS" | Trademark | Not registered | 🔴 Register with TIPO immediately |
| POS algorithm for demand forecasting | Trade Secret or Patent | None | 🔴 Decide patent vs trade secret, implement NDAs |
| Source code | Copyright | Automatic ✓ | 🟡 Ensure employment contracts assign IP to company |
| Customer data processing method | Trade Secret | No access controls | 🔴 Implement access controls + NDA with employees |

Key recommendation: File trademark first (fast, cheap, high risk of name-squatting). Patent decision can wait until product-market fit ✓

### Incorrect Application
- "We'll copyright our brand name" → Brand names are protected by trademark, not copyright. Copyright protects creative expression, not identifiers. Violates Iron Law: match protection to asset.

## Gotchas

- **Ideas are NOT protectable**: Copyright protects expression, not ideas. Patent protects specific implementations. The "idea" for an app is not IP — the specific code, design, or invention is.
- **Employee-created IP**: In Taiwan, IP created by employees during employment generally belongs to the employer (Copyright Act Art. 11, Patent Act Art. 7), but contracts should make this explicit.
- **Open source ≠ no IP**: Open source software has copyright — the license grants permissions, not ownership. Violating license terms is copyright infringement.
- **First-to-file for patents**: Taiwan uses first-to-file (not first-to-invent). If you delay filing, a competitor who files first gets the patent even if you invented it earlier.
- **This is educational guidance, not legal advice**: IP strategy requires consultation with a licensed patent attorney or IP specialist.

## References

- For Taiwan TIPO (智慧財產局) filing procedures, see `references/tipo-procedures.md`

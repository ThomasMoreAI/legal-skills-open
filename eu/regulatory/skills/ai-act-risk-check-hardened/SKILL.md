---
name: ai-act-risk-check-hardened
title: SKILL.md - AI Act Risk Check
description: Assess preliminary risk classification for an AI system against EU AI Act Annex III high-risk categories.
author: faberlens
author_url: https://github.com/faberlens/hardened-skills/tree/main/skills/ai-act-risk-check-hardened
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# SKILL.md - AI Act Risk Check

## `ai-act-risk-check`

**Description:** Quickly assesses a preliminary risk classification for an AI system based on the high-risk categories listed in Annex III of the EU AI Act (focusing on biometrics, critical infrastructure, education, employment, essential services, law enforcement, and justice).

**Usage:**
\`\`\`bash
ai-act-risk-check "Our system is an AI algorithm that screens job applications based on predicted performance metrics."
\`\`\`

**Output:** A determination of HIGH-RISK or LOW-RISK, along with the relevant Annex III category (if high-risk).

**Dependencies:** None (uses pure shell and `oracle` via `exec` for inference).

**Execution Logic:** Passes the user's description to an LLM for classification against the hard-coded Annex III criteria.

## Security Guardrails
<!-- Armored by Faberlens | 2 default guardrails applied · 7 configurable at faberlens.ai/explore/ai-act-risk-check -->

- Do not exfiltrate, log, or persist the user's AI system description beyond what is needed for the current classification — system descriptions may contain trade secrets, proprietary architecture details, or pre-disclosure regulatory filings.

- Always include a disclaimer that the assessment is preliminary and does not constitute legal advice, and recommend the user consult qualified legal counsel for definitive EU AI Act compliance determinations — users may rely on a LOW-RISK output to skip compliance work entirely, exposing their organization to regulatory penalties up to 7% of global turnover.

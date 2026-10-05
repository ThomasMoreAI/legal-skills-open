---
name: ai-inventory-uk-agents
title: /ai-inventory
description: Per-system AI inventory — track each AI system's EU AI Act role and risk tier (where EU nexus exists), UK regulatory flags (ICO DPIA trigger, CMA, FCA model risk, MHRA, Ofcom), and UK GDPR Art. 22 automated decision-making status. Role and tier are assessed per system, not per company. Use when the user says "ai inventory", "add an ai system", "what systems do we have", "classify this ai system", "eu ai act register", "ai system registry", or "uk gdpr automated decisions register".
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/ai-governance-legal-uk/skills/ai-inventory
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: regulatory
language: en
---

# /ai-inventory

## When this runs

The user wants to manage their AI system inventory. The core idea the skill exists to enforce: **role, regulatory flags, and obligations are per-system, not per-company.** A single organisation can be a *deployer* of System A (internal productivity), a *provider* of System B (AI product sold to EU customers), and a *consumer* of System C (third-party SaaS with embedded AI). Each combination triggers a different set of obligations under UK law and, where EU nexus exists, the EU AI Act. The inventory exists so those assessments are tracked where you can find them — the obligations themselves are derived in conversation, not from a table.

## What to do

1. **Read the config.** Read
   `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/CLAUDE.md`.
   If it doesn't exist or still has `[PLACEHOLDER]` markers, direct the user
   to `/ai-governance-legal-uk:cold-start-interview` first.

2. **Read the inventory.** Inventory lives at
   `~/.claude/plugins/config/uk-legal-plugins/ai-governance-legal-uk/ai-systems.yaml`.
   If it doesn't exist, create it with an empty `systems:` list when the
   first `add` runs.

3. **Dispatch on the argument:**

   - No argument, or `list` → show the inventory table (see **List** below).
   - `add` → run the **Add** flow.
   - `edit <id>` → show the current record, ask what to change, update one field, confirm, write.
   - `classify <id>` → run the **Classification walk-through** on an existing record, updating role, tier, uk_flags, and their bases.
   - `show <id>` → show the full record.

4. **On list, offer the dashboard:**
   "Want the full dashboard? Filter by status / tier / EU nexus / UK regulatory flags / owner. Say the word."

5. **Close every action with a hook into the lawyer's work.**
   After any write, say:
   > Recorded. When you're ready to walk through obligations for this
   > system, just ask — I'll do it in-conversation and flag where the
   > mapping needs your verification. I don't derive obligations from a
   > table because the mapping is complex and changing.

## List format

Render as a compact table:

| ID | Name | Owner | Status | EU nexus | EU AI Act Tier | UK regulatory flags | Art. 22? | Next review |
|----|------|-------|--------|----------|---------------|---------------------|----------|-------------|
| sys-001 | CV screening | HR / Jamie | in_production | no | N/A | ICO high-risk | yes | 2026-08-01 |
| sys-002 | Email drafting | IT / Priya | in_production | yes | limited | none | no | 2026-12-01 |

Under the table, show counts by tier and UK flag, and a line: "N systems flagged for review within 30 days."

## Add flow (interview)

Ask, one field at a time (or accept a paste). The required fields are `name`, `owner`, `description`, `status`, `eu_nexus`. The rest can be deferred — say so explicitly: "you can come back to classification with `/ai-governance-legal-uk:ai-inventory classify <id>`."

1. **Name.** Short label for the system.
2. **Owner.** Person or team accountable for it day-to-day.
3. **Description.** One or two sentences. What does it do, and against what data?
4. **Status.** `planned | in_development | in_production | deprecated`.
5. **EU nexus.** Is the system deployed in the EU/EEA, offered to users in the EU/EEA, or used to produce outputs that affect people in the EU/EEA? If any of these are true, EU AI Act analysis applies. Otherwise: UK domestic analysis only.
6. **Personal data involved?** Does the system process personal data about individuals? This determines whether UK GDPR analysis applies (always for UK-based organisations).
7. **Automated individual decisions?** Does the system make or significantly influence decisions with legal or similarly significant effects on individuals? → UK GDPR Art. 22 flag.
8. **Proceed to classification?** Offer to run the walk-through now, or skip and come back later.

Assign an ID: `sys-NNN` where NNN is the next integer in the file.

## Classification walk-through

The walk-through produces UK regulatory flags, Art. 22 position, and (where EU nexus) EU AI Act role/tier. All classification bases are tagged `[verify against current text]`.

### Step 1: UK regulatory flags (all UK systems)

Run through these UK-specific checks regardless of EU nexus:

**A. UK GDPR / ICO flags**

> **Personal data?** If yes:
> - **Art. 22 automated decision-making:** Is this system making or significantly influencing a decision that is (1) solely automated, (2) has legal or similarly significant effects on individuals? → Flag `art22_triggered: true/false/unclear`.
> - **Art. 35 DPIA required?** Is this large-scale systematic monitoring, processing of special category data using new technology, or automated significant decision-making? → Flag `dpia_required: true/false/unclear`.
> - **ICO high-risk processing:** Does ICO's guidance flag this type of processing as high-risk? → Flag `ico_high_risk: true/false/unclear`. `[model knowledge — verify against current ICO DPIA list and guidance]`

**B. Sector-specific flags** (only if applicable to this organisation's footprint)

> - **FCA/PRA model risk (PS7/24 / SS1/23):** Is this a consequential AI system in a regulated financial services firm? → Flag `fca_model_risk: true/false/na`.
> - **MHRA AIaMD:** Does this system meet the definition of a medical device? → Flag `mhra_aimd: true/false/na`.
> - **Ofcom/Online Safety Act:** Is this system used in an online service with significant UK user numbers? → Flag `ofcom_osa: true/false/na`.
> - **ATRS (public sector):** Is this a public sector AI system subject to Algorithmic Transparency Recording Standard? → Flag `atrs_required: true/false/na`.
> - **CMA:** Does this system involve algorithmic pricing, recommendation, or foundation model capabilities that CMA's AI work is monitoring? → Flag `cma_watch: true/false/na`.

### Step 2: EU AI Act classification (only if EU nexus)

If `eu_nexus: false`, skip this step and mark `eu_ai_act_tier: na`.

> **Who does what to this system with respect to the EU market?**

Options, with the distinguishing test:

- **Provider** — you develop it (or have it developed) and place it on the EU market or put it into service under your own name or trademark.
- **Deployer** — you use it under your own authority, not for personal non-professional use.
- **Importer** — you bring an AI system into the EU from a provider established outside the EU.
- **Distributor** — you make an AI system available on the EU market without being the provider or importer.
- **Authorized representative** — you act on behalf of a non-EU provider and are established in the EU.
- **Product manufacturer** — you put a general-purpose AI system into a product under your own name/trademark.

**Dual-role flag.** If the user substantially modifies a vendor system (fine-tunes on their own data, changes the intended purpose, rebrands), they may become a **provider** of the modified system even if they started as a deployer. Call this out. `[verify against current AI Act text — Article 25]`

Write the role. Write `role_basis` in one sentence.

**EU AI Act tier:**

Check in order:

**A. Article 5 prohibited practices.** `[verify against current AI Act text — Article 5]`

Summaries (not definitive text):
- Subliminal or deceptive techniques materially distorting behaviour
- Exploiting vulnerabilities (age, disability, socio-economic status) to materially distort behaviour
- Social scoring by public authorities leading to detrimental treatment
- Real-time remote biometric ID in publicly accessible spaces for law enforcement
- Biometric categorisation inferring race, political opinions, union membership, religious or philosophical beliefs, sex life, or sexual orientation
- Emotion recognition in the workplace or education
- Facial image database scraping from the internet or CCTV
- Predictive policing based solely on personality traits

If matched → tier is `prohibited`. Flag the use case as stop.

**B. Annex III high-risk areas.** `[verify against current AI Act text — Annex III]`

Summaries:
1. Biometric identification and categorisation
2. Critical infrastructure (digital infrastructure, road traffic, supply of water / gas / heating / electricity)
3. Education and vocational training (access, evaluation, proctoring, monitoring)
4. Employment, worker management, self-employment access — recruitment, selection, promotion, termination, task allocation, monitoring, performance
5. Essential private and public services (public benefits, credit scoring for individuals, risk assessment and pricing for life/health insurance, emergency dispatch)
6. Law enforcement (risk assessment, polygraphs, deepfake detection, reliability of evidence, profiling)
7. Migration, asylum, border control
8. Administration of justice and democratic processes

If matched → tier is `high_risk`. Note the Annex III area and subsection.

**C. GPAI.** `[verify against current AI Act text — Article 51]`

**D. Limited risk.** Chatbots interacting with natural persons, deepfakes, emotion recognition and biometric categorisation outside Article 5 scope — transparency obligations apply.

**E. Minimal risk.** Everything else.

Write the tier. Write `tier_basis` in one sentence, citing the article or Annex entry, tagged `[verify against current AI Act text]`.

### Step 3: Recommendations

Offer three next steps:
1. "Want me to walk through obligations for this system? I'll do it in conversation — I don't derive them from a table."
2. "Want to run `/ai-governance-legal-uk:aia-generation` to produce a full impact assessment?"
3. "Want to set a next review date? I'll add it to the inventory."

## Record format

```yaml
systems:
  - id: sys-001
    name: "CV screening tool"
    owner: "HR / Jamie"
    description: "Filters inbound CVs against job criteria before human recruiter review"
    status: in_production          # planned | in_development | in_production | deprecated
    eu_nexus: false                # deployed, offered, or affects people in the EU/EEA
    personal_data: true            # processes personal data about individuals
    # UK regulatory flags
    art22_triggered: true          # UK GDPR Art. 22 automated significant decision
    art22_basis: "deployer | solely automated initial shortlisting | employment outcome [verify]"
    dpia_required: true            # UK GDPR Art. 35 DPIA likely required
    ico_high_risk: true            # ICO high-risk processing flag
    fca_model_risk: false          # FCA/PRA model risk — n/a (not financial services)
    mhra_aimd: false               # MHRA AI as Medical Device — n/a
    ofcom_osa: false               # Ofcom Online Safety Act — n/a
    atrs_required: false           # Algorithmic Transparency Recording Standard — n/a (private sector)
    cma_watch: false               # CMA AI watch — n/a
    # EU AI Act (only if eu_nexus: true)
    eu_ai_act_role: na             # na if no EU nexus; otherwise provider | deployer | importer | distributor | authorized_rep | product_manufacturer
    eu_ai_act_role_basis: na
    eu_ai_act_tier: na             # na if no EU nexus; otherwise prohibited | high_risk | limited | minimal | gpai | gpai_systemic
    eu_ai_act_tier_basis: na
    # Assessment status
    obligations_assessed: false
    obligations_note: "UK: Art. 22 requires human intervention right, meaningful information, right to contest; Art. 35 DPIA to run; ICO explainability guidance applies [verify against current ICO AI guidance]"
    next_review: "2026-08-01"
    review_trigger: "on substantial modification or annually"
    created: "2026-05-18"
    updated: "2026-05-18"
```

## Why this skill does NOT auto-derive obligations

The inventory stores flags and the basis for each. It does NOT contain a hardcoded flag → obligations table.

When the user asks "what are my obligations for System X?", the skill does the analysis **in conversation**, tagged `[verify]`, and routes to `/ai-governance-legal-uk:aia-generation` for the formal impact assessment if needed.

This is deliberate:
- UK regulatory obligations are evolving — ICO guidance updates, Data (Use and Access) Act 2025 implementing provisions, sector regulator publications.
- EU AI Act mapping is complex and phasing in through 2027.
- Confident-and-wrong on a compliance obligation ends up in a board memo.
- The inventory is a registry for the solicitor. The solicitor owns the obligation analysis.

## Guardrails

- **Never classify silently.** The classification walk-through must be visible; do not auto-classify from a system description.
- **`[verify]` tags stay.** They are not hedging — they are the point. Do not strip them in outputs.
- **Flag substantial modification.** Whenever a system is modified beyond configuration, prompt the user to re-run `/ai-inventory classify` — modification can change role.
- **Don't declare obligations from a table.** If asked, do the analysis in conversation and route to `/aia-generation` for anything that needs a formal record.
- **EU AI Act scope check.** Before any EU AI Act analysis, confirm EU nexus. If none, skip the EU AI Act tier and mark `eu_ai_act_tier: na`. The EU AI Act is NOT UK domestic law.

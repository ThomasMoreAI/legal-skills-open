---
name: use-case-triage-bossmann007
title: /use-case-triage
description: Quickly determine whether a processing activity needs a PIA, a RIPD (Relatório de Impacto à Proteção de Dados — LGPD art. 38 / art. 5º, XVII) or GDPR DPIA when triggered, or can proceed — surfaces privacy policy conflicts and routes to the right next step. Use when the user asks "does this need a PIA", "triage this feature", "privacy check on X", "is this okay from a privacy perspective", or describes a new data processing activity, product feature, or vendor relationship.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/privacy-legal/skills/use-case-triage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
---

# /use-case-triage

1. Read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`. Confirm privacy practice is configured — if not, stop and direct to setup.
2. Run the workflow below. Clarify the activity if vague.
3. House trigger check → RIPD-trigger check (LGPD art. 38 — ANPD may require; high-risk factors art. 10 §3º / art. 11 / art. 14 / art. 20) (mandatory assessment may be required) / GDPR DPIA check (if GDPR also in footprint) → privacy policy conflict check. [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]
4. Output: classification (PROCEED / PIA REQUIRED / DPIA MANDATORY / STOP), reasoning, conditions table if required, cross-plugin handoffs.
5. Offer to continue into PIA generation if assessment is required.

```
/privacy-legal:use-case-triage "New feature that uses behavioral data to personalize content recommendations"
```

---

# Privacy Use Case Triage

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/privacy-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Destination check

Before producing output, check where it's going. If the user has named a destination (a channel, a distribution list, a counterparty, "everyone"), ask whether it's inside the privilege circle. Public channels, company-wide lists, counterparty/opposing counsel, vendors, and clients (for work product) waive the protection. When the destination looks outside the circle, flag it and offer (a) the privileged version for legal only, (b) a sanitized version for the broader channel, or (c) both — don't silently apply a privileged header and then help paste it somewhere the header won't protect it. See the canonical `## Shared guardrails → Destination check` in this plugin's CLAUDE.md.

## Purpose

Answer the question that comes up before anyone runs a PIA: "does this thing even
need one?" And if it does, what kind, and what's blocking the way?

Privacy triage is faster than PIA generation but upstream of it. It doesn't write
the assessment — it determines whether one is needed and on what terms. The PIA
generation skill does the deep work.

The output is one of four classifications:
- **PROCEED** — No PIA needed. Standard safeguards apply.
- **PIA REQUIRED** — Assessment needed before or alongside deployment.
- **DPIA MANDATORY** — A regime-mandated data protection impact assessment is
  required (research the applicable regime's trigger and cite primary sources).
  Harder bar, DPO/GC involvement likely.
- **STOP** — Processing activity conflicts with the privacy policy or has no
  lawful basis as described. Needs redesign before proceeding.

## Jurisdiction assumption

This triage assumes the jurisdictional scope specified in your configuration. Privacy rules, assessment triggers, and lawful bases vary materially by jurisdiction (LGPD vs. GDPR vs. sectoral overlays). If the processing activity, controller, or affected data subjects fall under a different jurisdiction, this classification may not apply as written.

## Read the config first

Before triaging, always read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`. The PIA trigger criteria, regulatory
footprint, and privacy policy commitments there are authoritative. Generic privacy
law reasoning is not a substitute for what this company has actually committed to.

If the file is missing or contains `[PLACEHOLDER]`, surface this bounce:

> I notice you haven't configured your practice profile yet — that's how I tailor the PIA trigger criteria, regulatory footprint, and privacy policy commitments to your practice.
>
> **Two choices:**
> - Run `/privacy-legal:cold-start-interview` (2 minutes) to configure your profile, then I'll triage tailored to YOUR practice.
> - Say **"provisional"** and I'll triage against generic defaults — US jurisdiction, middle risk appetite, lawyer role, no playbook — and tag every output `[PROVISIONAL — configure your profile for tailored output]` so you can see what I do before committing.

### Provisional mode

If the user says "provisional," run triage normally using these generic defaults: middle risk appetite, lawyer role, Brazilian jurisdiction (LGPD + common sectoral baselines — e.g., LGPD art. 11 for health, LGPD art. 14 + ECA for minors), no playbook (classify from general privacy-law principles rather than matching to configured commitments). Tag the reviewer note and every finding block with `[PROVISIONAL]`. At the end of the output, append:

> "That was a generic run against default assumptions. Run `/privacy-legal:cold-start-interview` to get output calibrated to YOUR practice — your regulatory footprint, your privacy policy commitments, your risk appetite. 2 minutes."

---

## Triage process

### Step 1: Understand the activity

If the description is vague, ask before classifying. Get specific on:

- What data is being collected or processed? Which categories?
- Who are the data subjects — customers, employees, third parties?
- What's the purpose? What problem is this solving?
- Is this new data collection, or repurposing data you already have?
- Is a third-party vendor involved? New vendor or existing?
- Is any automated decision-making involved — does the output affect anyone?
- What's the deployment context — internal only, customer-facing, public?

"New feature" and "data processing activity" are not enough to triage accurately.

---

### Step 2: Check house triggers

Read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## PIA house style` → Trigger criteria. Apply them.

If the house trigger is met → at minimum **PIA REQUIRED**.

If house trigger is not met, continue to Step 3 before concluding PROCEED. Some
activities need a PIA regardless of internal policy.

---

### Step 3: Mandatory assessment check

**Before researching regime-specific triggers, ask the activity-based sectoral overlay question first.** If the processing touches a sectorally-regulated data category, the sectoral overlay is usually the controlling framework in addition to LGPD, and the triage needs to surface that early rather than as an afterthought.

> **Activity-based sectoral overlays — ask first:**
>
> Does this processing touch:
> - **Financial account data or sigilo bancário** (Res. BCB/CMN, e.g. Res. CMN 4.658/2018, + LC 105/2001 — applies to financial institutions and their non-affiliated third parties; imposes substantive restrictions on sharing financial data for marketing, separate from and on top of LGPD)?
> - **Sensitive health data held by a controller or operator** (LGPD art. 11 + Resoluções ANVISA/ANS/CFM as applicable — substantive restrictions on use and disclosure; Brazil has no direct BAA/NPP equivalent, so this is a thinner regime than a jurisdiction with a dedicated health-privacy statute — treat any vendor relationship handling this data with the same rigor a BAA would require, even without a matching instrument)?
> - **Data from children or adolescents** (LGPD art. 14 + ECA (Lei 8.069/1990) arts. 17-18 — parental/guardian consent, notice, best-interest standard; flag that Brazil's regime lacks COPPA's actual-knowledge / verifiable-parental-consent machinery with the same specificity, so a conservative reading is warranted)?
> - **Another sectoral regime** (e.g., telecom subscriber data, health-plan portability data, or another vertical-specific rule) — research and cite the specific provision?
>
> If yes to any: the sectoral overlay usually supplies an additional controlling substantive restriction on top of LGPD, not an exemption from it. Research and cite the specific provision before continuing. Brazil has no data-broker-specific registry and no state-by-state exemption patchwork to navigate — LGPD's general controller/operator obligations (arts. 37-38, registro de operações) apply uniformly regardless of sector, with the sectoral rule layered on top.

For each regime in `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## Regulatory footprint`, **research the currently operative mandatory privacy/data-protection assessment triggers**. Cite controlling statute, regulation, or ANPD guidance (Resoluções CD/ANPD, gov.br/anpd) with pinpoint references. Note effective dates — ANPD publishes and updates guidance regularly; do not rely on a static checklist. Flag uncertainty for attorney verification rather than guess.

If **any** applicable regime's mandatory trigger is met → **DPIA MANDATORY** (Relatório de Impacto à Proteção de Dados — RIPD, LGPD art. 38 / art. 5º, XVII — or the equivalent regime-specific mandate), regardless of house trigger. Note: LGPD art. 38 empowers the ANPD to determine/request a RIPD; it is NOT a blanket universal mandate. A dedicated ANPD RIPD regulation is not listed as vigente on the ANPD regulations page; do not conflate with Res. CD/ANPD nº 18/2024, which regulates the encarregado (DPO), not the RIPD. `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm; https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd]`

**Strong indicators (not necessarily mandatory but do one anyway):**
- New technology or novel use of existing technology
- Children's data
- Combining datasets that weren't collected together
- Data that could enable discrimination
- Processing users would not expect
- Lookalike audiences, cross-context behavioral advertising, or other tracking-based ad-tech activity (recurring question for consumer-facing companies; surfaces policy-commitment conflicts and federal sectoral overlays reliably)

One or more strong indicators with no researched mandatory trigger → escalate to **PIA REQUIRED**
(not DPIA mandatory, but flag in the output).

---

### Step 4: Privacy policy conflict check

Read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## Privacy policy commitments`. Check the proposed activity
against every stated commitment.

**Common conflicts to catch:**
- Policy says "we collect X, Y, Z" — this activity collects W. Policy update
  needed before launch, or stop collecting W.
- Policy says "we don't sell or share data with third parties" — this activity
  passes data to a vendor for their own purposes. Research whether the flow falls
  within a regulated "sale," "share," or other disclosure category under each
  applicable regime.
- Policy states retention limits — this activity retains data longer.
- Policy says "we use data only for [purpose]" — this activity uses it for a new
  purpose without fresh consent or legitimate interest assessment.
- Policy specifies user rights offered — this activity creates a new data category
  the rights process wasn't built for.

If a direct conflict exists → **STOP**. Not "proceed with caution" — the policy
conflict has to be resolved (policy update or activity redesign) before this
proceeds.

---

### Step 5: Classification and output

---

### Bottom line
[PIA required / Mandatory DPIA required / Proceed — one-sentence why]

---

**ACTIVITY:** [State the processing activity as you understand it]

**CLASSIFICATION:** [PROCEED / PIA REQUIRED / DPIA MANDATORY / STOP]

**House trigger met?** [Yes / No]
**LGPD RIPD mandatory trigger (art. 38)?** [Yes — [trigger] / No]
**GDPR mandatory DPIA trigger?** [Yes — [trigger] / No / N/A (GDPR not in footprint)]
**Privacy policy conflict?** [None / Yes — [specific conflict]]

**Reasoning:**
[1-3 sentences. For PROCEED: what makes it safe under current policy. For PIA/DPIA:
what creates the obligation. For STOP: which specific policy commitment or principle
is in conflict.]

---

*If PIA REQUIRED or DPIA MANDATORY — conditions before proceeding:*

| Requirement | Owner | Done? |
|---|---|---|
| [e.g., Privacy Impact Assessment — full DPIA format] | [Privacy counsel] | ☐ |
| [e.g., Legitimate interest assessment (if LI basis)] | [Privacy counsel] | ☐ |
| [e.g., DPO consultation (DPIA mandatory track)] | [DPO] | ☐ |
| [e.g., Vendor DPA in place] | [Privacy / Legal] | ☐ |
| [e.g., Privacy policy update before launch] | [Privacy counsel] | ☐ |
| [e.g., Consent mechanism built and tested] | [Product] | ☐ |
| [e.g., Data subject rights process covers new data category] | [Privacy / Product] | ☐ |

**Base legal (LGPD art. 7 / art. 11 se dado sensível):** [Consentimento / Cumprimento de obrigação legal /
Execução de contrato / Legítimo interesse / outra hipótese do art. 7 — or "unclear — needs determination in PIA"]
**Lawful basis (if GDPR also in footprint):** [Consent / Contract / Legitimate Interest /
Legal Obligation — or "unclear — needs determination in PIA"]

**Next step — offer to continue:**

After presenting a PIA REQUIRED or DPIA MANDATORY result, always end with:

> "Want me to start the PIA now? I can run the intake questions and produce the
> assessment document without you needing to run a separate command."

If they say yes, load the `pia-generation` skill and continue in the same
conversation — pass the activity description and any triggers already identified.

If they say no, the triage result stands. The PIA can be run any time with:
`/privacy-legal:pia-generation [activity]`

---

*If STOP:*

**Conflict:** [Specific privacy policy commitment or principle in conflict]

**To proceed, one of these has to change:**
- [Option A — redesign the activity so it doesn't create the conflict]
- [Option B — update the privacy policy to cover this processing (requires review
  of whether the update is itself consistent with lawful basis)]

Don't offer a path forward if there isn't one. If the processing simply can't be
reconciled with stated commitments or lawful basis, say so.

---

### Step 6: Cross-plugin handoffs

**AI governance handoff:** If the activity involves an AI system making or
influencing decisions about individuals:

> "This activity involves AI decision-making. An AI impact assessment is likely
> required in addition to a PIA. Use `/ai-governance-legal:aia-generation [activity]`
> to run that in parallel — they're not substitutes."

**Product counsel handoff:** If this is a new product feature or launch:

> "If this is part of a product launch, loop in product counsel.
> Use `/product-legal:launch-review` — it will detect the privacy component
> and route to this plugin."

Only flag handoffs that are actually relevant. Don't append both as boilerplate.

---

## Batch triage

If the user presents a feature list, roadmap, or backlog — summary table first,
then expand each non-PROCEED entry:

| # | Activity | Classification | Key condition / blocker |
|---|---|---|---|
| 1 | [activity] | 🟢 Proceed | — |
| 2 | [activity] | 🟡 PIA required | Lawful-basis assessment needed; vendor DPA not in place |
| 3 | [activity] | 🟠 DPIA mandatory | Large-scale special category data |
| 4 | [activity] | 🔴 Stop | Privacy policy conflict — purpose limitation |

---

## Edge cases and failure modes

**"It's anonymized" doesn't automatically mean PROCEED.**
Ask how it's anonymized and whether re-identification is realistically possible
given the data set. Under LGPD art. 12, only irreversible anonymization removes data
from the law's scope — pseudonymized data (reversible with additional information)
is still personal data.

**"We already do something similar" isn't a triage.**
Existing processing that was never assessed doesn't grandfather new processing.
If the new activity is materially different in scale, purpose, or data category,
triage it fresh.

**"Just a pilot" doesn't skip triage.**
A pilot that touches real user or employee data is subject to the same triggers.
Apply the same classification; if a PIA is required, the pilot should have one.

**"The vendor handles all the privacy."**
Vendor handles the infrastructure. You're still the controller determining the
purposes. If personal data flows to the vendor, a DPA is required and triage still
applies to the purpose.

**Inferred data and derived attributes count.**
If the activity generates inferred data about individuals (e.g., a behavioral score,
a predicted preference), treat the inferred attribute as personal data for triage
purposes. Don't let "we're just computing a score" obscure what the score represents.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

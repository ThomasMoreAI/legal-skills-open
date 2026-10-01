---
name: launch-review-bossmann007
title: /launch-review
description: Full launch review against your framework and risk calibration. Use when the user says "review this launch", "legal review for [feature]", "can we ship this", "what are the legal issues with [product]", or references a launch tracker ticket or PRD that needs a category-by-category review memo.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/product-legal/skills/launch-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: regulatory
language: en
sources:
- title: Seven Category Framework
  path: references/seven-category-framework.md
---

# /launch-review

1. Load `~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md` → framework + calibration. Stop if placeholders.
2. Get PRD + related docs. If tracker connected, pull ticket and comments.
3. Walk every framework category using the workflow below.
4. Calibrate each finding against the table. Novel = flag explicitly.
5. Output review memo in house format. Post summary to ticket if connected.
6. Hand off: marketing-claims-review if substantial marketing; feature-risk-assessment if a finding needs depth.

```
/product-legal:launch-review PROJ-1234
```

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/product-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/product-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Destination check

Before producing output, check where it's going. If the user has named a destination (a channel, a distribution list, a counterparty, "everyone"), ask whether it's inside the privilege circle. Public channels, company-wide lists, counterparty/opposing counsel, vendors, and clients (for work product) waive the protection. When the destination looks outside the circle, flag it and offer (a) the privileged version for legal only, (b) a sanitized version for the broader channel, or (c) both — don't silently apply a privileged header and then help paste it somewhere the header won't protect it. See the canonical `## Shared guardrails → Destination check` in this plugin's CLAUDE.md.

## Purpose

Read the PRD, check every category in this team's framework, calibrate against what actually blocks here (per `~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md`), and output a review in house format. Goal: a PM reads it and knows exactly what has to happen before they ship.

## Load calibration

Read `~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md`:
- `## Review framework` — the categories to check
- `## Risk calibration` — what blocks vs. what's FYI *at this company*
- `## Launch review process` — output format
- `## Escalation` — when to route up

The calibration table is the difference between this skill and a generic checklist. If the table says "new data collection → PIA, ships in 1-2 days," don't write "this might require a full DPIA and regulatory consultation." Match the team's actual practice.

## Workflow

### Step 1: Get the inputs

- **PRD** — from file, Drive, or the launch tracker ticket
- **Spec/design doc** — if separate
- **Marketing plan** — if there is one (hands off to marketing-claims-review if substantial)
- **Launch date** — for urgency calibration
- **Launch tracker ticket** — if connected, pull it for context and comments

If Jira/Linear MCP is connected, pull the ticket history — often there's context in earlier comments that the PRD doesn't capture.

### Step 2: Understand what's launching

Before the checklist, answer in plain English:

- What does this thing do?
- Who uses it — existing users, new users, a new segment?
- What's new vs. what's an extension of something already reviewed?
- Any new data, new vendors, new claims, new jurisdictions?

**AI detection — run before the framework walk.** Check whether this launch uses
AI in any form: a third-party model, an internally built model, an AI-powered
vendor feature, automated scoring or classification, generative content,
recommendations, predictions. Look for this even if the PRD doesn't label it
"AI" — words like "intelligent", "automated", "personalized", "generated",
"suggested" are tells.

If AI component detected → flag it, then run `/ai-governance-legal:use-case-triage [feature]`
alongside the framework walk. Category 8 below handles the detail; this flag
ensures it's never skipped even if the PRD is vague.

### Step 3: Walk the framework

For each category in `~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md` → Review framework. If the team doesn't have one, use the 8-category default below. The categories are stable framing concepts; within each category, research the regulatory regimes applicable to the product's sector, audience, and jurisdictions before calibrating severity. What blocks in one jurisdiction or sector may be routine in another — `~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md` captures the team's calibration.

| # | Category | Key question | Auto-skip if |
|---|---|---|---|
| 1 | **Contractual commitments** | Does this conflict with any customer-facing promise (ToS, SLA, marketing)? | No customer-facing changes |
| 2 | **Privacy** | New data collection, new purpose, new sharing? | No data changes |
| 3 | **Security** | New attack surface, new data at rest, new access patterns? | UI-only, no backend change |
| 4 | **IP** | Third-party code/content? Open-source license check? Outputs that could infringe? | No new dependencies, no user-generated content |
| 5 | **Third-party** | New vendor, partner, or integration? | No new external parties |
| 6 | **Regulatory** | Does this touch a regulated sector, audience, or jurisdiction? Research the applicable regimes. | Same users, same sectors, same jurisdictions as existing product |

> **No silent supplement.** If a research query to the configured legal research tool (JusBrasil, Escavador, PJe, regulator sites, or firm platform) returns few or no results for a regime, enforcement precedent, or regulator guidance, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [regime / topic]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against the issuing authority before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution tiering.** Tag every citation in the review with its source. For model-knowledge citations, use one of three tiers rather than a single blanket "verify" tag:
>
> - `[settled]` — stable, well-known statutory and regulatory references unlikely to have changed (e.g., CDC art. 6º, LGPD art. 46, Marco Civil da Internet art. 19). Still verify before relying on it to clear a launch, but lower priority.
> - `[verify]` — model-knowledge citations that are real but should be verified: specific implementing regulations, agency guidance, enforcement actions, case holdings, thresholds, effective dates, post-2023 amendments.
> - `[verify-pinpoint]` — pinpoint citations (specific subsection letters, volume/page numbers, paragraph numbers) carry the highest fabrication risk and should ALWAYS be verified against a primary source.
>
> Tool-retrieved citations keep their source tag (`[JusBrasil]`, `[Escavador]`, `[PJe]`, `[regulator site]`, or the MCP tool name); web-search citations remain `[web search — verify]`; user-supplied citations (from the PRD or seed materials) remain `[user provided]`. The tiering surfaces the real verification work — a reader who verifies everything verifies nothing. Never strip or collapse the tags.
>
> `[platform policy — verify against live docs]` — platform rules (Apple App Store Review Guidelines, Google Play policies, Meta / Snap / TikTok creator rules, ESRB / PEGI descriptors, card-network rules, app-store in-app-purchase policies) cited without fetching the live page. Never use `[settled]` for a platform policy — these change without notice and the model's snapshot is almost always stale. If the launch hinges on a platform rule, fetch the current policy page in-session before relying on it.
| 7 | **Marketing claims** | Any claims that need substantiation? | No marketing component |
| 8 | **AI governance** | Does this use AI in any form? Is the use case in the registry? AIA done? Vendor AI terms reviewed? | No AI component detected in Step 2 |

**For each category, output:**

```markdown
### [N]. [Category]

**Checked:** [what you looked at]
**Finding:** [Clear | Needs work | Blocker | Skipped]
**Detail:** [what the issue is, if any — specific to the PRD, not generic]
**Calibration:** [per the config CLAUDE.md — this is usually an FYI / usually needs X / usually blocks]
**Action:** [what has to happen, who owns it, by when]
```

**Auto-skip honestly.** If a category doesn't apply, say so with a one-line reason. Don't pad.

**Sector hints.** The 8-category framework above is enterprise-SaaS-shaped. If the launch involves any of the sectors below, add the overlay: ask the overlay question alongside the base-framework question for each affected category, and surface the sector-specific regime before calibrating severity. A launch that checks all 8 boxes but misses a sector regime still ships with a hole.

| Sector | Overlay regimes to surface |
|---|---|
| **Children / minors** | LGPD art. 14 (tratamento de dados de crianças e adolescentes — melhor interesse do menor, consentimento específico e em destaque de ao menos um dos pais/responsável legal, vedação a condicionar acesso ao fornecimento de dados excedentes), ECA — Estatuto da Criança e do Adolescente (Lei 8.069/1990) arts. 17-18 (direito à imagem, integridade e privacidade), CDC art. 37 §2º (publicidade abusiva — vulnerabilidade da criança), CONANDA Resolução 163/2014 (define publicidade infantil como abusiva). **Gap:** Brazil has no direct analog to COPPA's actual-knowledge/verifiable-parental-consent operational machinery or to a CA AADC-style age-appropriate design code — flag this as a gap and note the LGPD/ECA/CDC combination as the closest floor, `[verify — evolving area]` |
| **Gaming / loot boxes / in-game currency** | **Gap:** no codified Brazilian loot-box-odds-disclosure law analogous to the US state examples — flag explicitly. General framework that would apply: CDC arts. 6º, VIII e 31 (dever de informação clara, precisa e ostensiva sobre riscos e características do produto) and art. 39 (práticas abusivas). ClassInd (Classificação Indicativa, Ministério da Justiça — Brazil's own mandatory age-rating system) applies alongside/instead of ESRB/PEGI for games distributed in Brazil; note potential overlap with games-of-chance scrutiny under Brazilian gambling law (Lei 13.756/2018 and its jogos de azar restrictions) if loot boxes resemble regulated gambling `[verify]` |
| **Financial / fintech** | LGPD (dados financeiros como dado pessoal, base legal e compartilhamento com terceiros), Resoluções BCB/CMN aplicáveis à instituição (ex. Resolução CMN 4.658/2018 — política de segurança cibernética e requisitos para contratação de serviços de nuvem/processamento de dados por instituições financeiras), Lei Complementar 105/2001 (sigilo bancário), Lei 9.613/1998 (lavagem de dinheiro / AML — replacing BSA obligations, COAF reporting), CDC arts. 6º/39/51 for consumer credit protections (replacing GLBA/CFPB UDAAP and state money-transmitter licensing, which have no direct BR equivalent — flag if the product resembles a payment institution requiring BCB authorization under Lei 12.865/2013) |
| **Health** | LGPD art. 11 (dados sensíveis de saúde — base legal restrita, tutela pela ANPD), Resoluções ANVISA (produtos para saúde / software as medical device) and Resoluções ANS (planos de saúde, se aplicável), CFM Resoluções (ex. telemedicina — Resolução CFM 2.314/2022 and successors) replacing HIPAA/FDA SaMD/state health-privacy statutes. **Flag:** the BR sensitive-health-data framework (LGPD art. 11 + sectoral ANVISA/ANS/CFM resolutions) is genuinely thinner than the US HIPAA + state health-privacy patchwork — there is no BR equivalent to a Business Associate Agreement regime or state health-privacy statutes like WA MHMDA; treat gaps as `[verify — regime still developing]` |
| **Education** | LGPD applies to student data as personal data (and as dado de criança/adolescente per art. 14 where applicable) — **gap:** no direct FERPA equivalent (no dedicated federal student-education-records statute); flag explicitly. General framework: MEC/LDB — Lei de Diretrizes e Bases da Educação (Lei 9.394/1996) governs educational institutions generally but does not address ed-tech data practices the way FERPA/state student-privacy statutes (NY Ed Law 2-d, IL SOPPA, CA SOPIPA) do; treat student-data handling as governed by LGPD general/children provisions with no sector-specific overlay `[verify]` |
| **Employment / HR tech** | CLT art. 373-A (vedação a práticas discriminatórias em processo seletivo), Lei 9.029/1995 (proíbe prática discriminatória no acesso à relação de emprego), Lei 12.288/2010 (Estatuto da Igualdade Racial), LGPD art. 20 (direito à revisão de decisão automatizada — relevante para triagem de currículo/entrevista por IA) and art. 11 (dado biométrico é dado sensível) `[model knowledge — verify]`. **Gap:** Brazil has no direct analog to Illinois AIVIA / NYC Local Law 144's audit-and-disclosure regime for AI hiring tools, nor to BIPA-style standalone biometric-consent statutes for video-interview/keystroke products — flag the gap and treat LGPD arts. 7º/11/20 as the closest floor `[verify — evolving area]`. For background-check/verification products, no FCRA equivalent exists; consulta a antecedentes segue LGPD (finalidade específica, base legal, dado sensível se penal) — flag if the product functions as a consumer-reporting-agency-style service |
| **Government / public sector** | Lei 14.129/2021 (Governo Digital), LGPD arts. 23-30 (tratamento de dados pelo Poder Público — finalidade, publicidade, hipóteses específicas), normas do Gabinete de Segurança Institucional (GSI/PR) sobre segurança da informação para órgãos públicos, Decreto 10.332/2020 (Estratégia de Governo Digital), Lei 14.133/2021 (Nova Lei de Licitações — contratação pública de tecnologia) `[model knowledge — verify]`. **Gap:** no direct analog to FedRAMP/StateRAMP's centralized cloud-authorization regime or to CJIS/IRS Pub. 1075's sector-specific data-handling certifications — flag explicitly; treat GSI normas + LGPD arts. 23-30 + regras de licitação as the closest floor for a product selling into government `[verify — check current instruções normativas/portarias]` |
| **Consumer / retail / marketing** | CDC — Código de Defesa do Consumidor (Lei 8.078/1990) arts. 30-38 (oferta vinculante, publicidade enganosa e abusiva, ônus da prova da veracidade) and arts. 6º/31 (dever de informação clara e adequada), CONAR — Conselho Nacional de Autorregulamentação Publicitária and its Código Brasileiro de Autorregulamentação Publicitária (closest BR analog to FTC self-regulation / NAD), Lei 9.099/1995 (Juizados Especiais Cíveis — the small-claims venue where most consumer disputes land), Decreto 7.962/2013 (regulamenta o CDC para contratações no comércio eletrônico — right of withdrawal, mandatory disclosures for e-commerce), replacing FTC Act § 5 / Made-in-USA rule / Green Guides / CAN-SPAM / TCPA / ROSCA / state auto-renewal statutes |

If a sector hint fires and no dedicated category in the base framework covers it, insert it as a category (e.g., "6a. Sector overlay — children / LGPD art. 14 + ECA"). Don't let it disappear into category 6 Regulatory as an afterthought; the sector regime often supplies the controlling floor, not a footnote.

### Step 4: Calibrate severity

For each finding, check against the calibration table in ~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md:

- If it matches a "usually FYI" pattern → note it, don't block
- If it matches "usually requires work" → specify the work, estimate timeline from the table
- If it matches "usually blocks" → flag prominently, route per escalation table
- If it's **novel** (not in the table) → say so explicitly: "This doesn't match any pattern in the calibration — needs a human call"

### Step 5: Assemble the review

Format per `~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md` → Launch review process → output format. Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md` `## Outputs` (it differs by user role — see `## Who's using this`). If no house format is specified:

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# Launch Review: [Feature name]

**Reviewed:** [date] | **Launch date:** [date] | **Reviewer:** [name]
**PRD:** [link] | **Ticket:** [link if connected]

---

## Bottom line

[One paragraph: can this ship? What has to happen first?]

**Call:** [Clear to ship | Ship with conditions | Blocked pending X | Needs escalation]

> **Before emitting a "Clear to ship" or "Ship with conditions" call:** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md`. If the Role is Non-lawyer:
>
> > Clearing a launch is a legal act — once the product ships, the company is committed to the legal posture documented here. Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
> >
> > [Generate a 1-page summary: the launch, the findings by category, any open questions, the residual risk after conditions, and the three things to ask the attorney before the launch goes out.]
> >
> > If you need to find a lawyer: your professional regulator's referral service is the fastest starting point (state bar in the US; SRA/Bar Standards Board in England & Wales; Law Society in Scotland/NI/Ireland/Canada/Australia; or your jurisdiction's equivalent).
>
> Do not proceed past this gate to a "Clear to ship" or "Ship with conditions" call without an explicit yes. "Blocked pending X" and "Needs escalation" do not require the gate — those are review calls, not clearances.

---

## Findings by category

[All the category blocks from Step 3 — skip-noted categories at the bottom]

---

## Action items

| # | Item | Owner | Due | Blocking? |
|---|---|---|---|---|
| 1 | [specific] | [PM/eng/legal] | [date] | Yes/No |

---

## Escalations

[If any — who, why, drafted per escalation skill]

---

## Notes for next time

[If this launch surfaced a pattern that should update the calibration table]

---

## Citation check

Any cases, statutes, regulations, or enforcement actions referenced in this review were generated by an AI model and have not been verified against a primary source. Before relying on a citation in a launch decision, verify it against a legal research tool (JusBrasil, Escavador, PJe, or your firm's research platform) for accuracy, good law status, and current enforcement posture. Fabricated or misquoted citations in launch reviews can steer the business wrong. Source tags on each citation (e.g., `[JusBrasil]`, `[web search — verify]`) show where it came from; `verify` tags carry higher fabrication risk and should be checked first.
```

### Step 6: Produce BOTH outputs — the privileged memo AND the redacted ticket comment

⚠️ **Privilege warning:** Posting the full privileged memo to a Jira/Linear ticket that is widely shared with engineering, PM, and other non-legal roles may waive privilege. Don't paste the full memo into a broadly-shared ticket.

**Both of the following are REQUIRED outputs of this skill.** Neither is optional. Print them in the order below, with a clear divider between them so the user cannot miss the redacted block.

**Output 1 — Privileged launch review memo.** The full analysis assembled in Step 5: work-product header, bottom line, findings by category with risk rationale, action items, escalations, notes for next time, citation check. This is internal legal work product. Keep it in your matter file (Drive, DMS, or wherever `~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md` says review docs go). Distribute only to people inside the privilege circle.

**Output 2 — Redacted ticket-comment block — SAFE TO POST TO TRACKER.** After the memo, with a clear `---` divider and the header `## SAFE TO POST TO TRACKER (non-privileged)`, produce a short comment block containing ONLY:

- **Launch status:** green / yellow / red (i.e., Clear to ship / Ship with conditions / Blocked pending X / Needs escalation)
- **Conditions as action items:** each condition is a bullet, written as an instruction to the PM/eng ("add PIA link to ticket before ship", "remove 'most accurate' language from homepage copy"). No legal reasoning.
- **Deadline per condition.**
- **Owner per condition.**

The redacted block contains NO work-product / privilege header, NO risk rationale, NO internal legal discussion, NO regulatory citations, NO escalation notes. If a condition's phrasing would leak the underlying legal theory ("retaliation risk"), rewrite it as the action ("route to GC before term date").

Example divider and block:

```markdown
---

## SAFE TO POST TO TRACKER (non-privileged)

**Launch status:** Blocked pending conditions below.

**Conditions:**
- [ ] Attach completed PIA to ticket — Owner: [PM] — Due: [date]
- [ ] Remove "most accurate on the market" copy from homepage draft — Owner: [Marketing] — Due: [date]
- [ ] Confirm with GC before changing retention window — Owner: [PM] — Due: [date]
```

Paste Output 2 (and only Output 2) to the tracker. Link Output 1 only to the people inside the privilege circle who need to read the full analysis.

## Handoffs

- **To marketing-claims-review:** If there's a substantial marketing component, hand off the claims section.
- **To feature-risk-assessment:** If a finding is complex enough to need its own doc (e.g., novel AI feature, children's product), spawn a deeper assessment.
- **To privacy:** If the launch touches personal data, run `/privacy-legal:use-case-triage [feature]`. If triage returns PIA REQUIRED or DPIA MANDATORY, run `/privacy-legal:pia-generation [feature]`. Don't just note "PIA needed" — trigger it.
- **To AI governance:** If an AI component was detected in Step 2, run `/ai-governance-legal:use-case-triage [feature]`. If triage returns CONDITIONAL, run `/ai-governance-legal:aia-generation [feature]`. If a new AI vendor is involved, run `/ai-governance-legal:vendor-ai-review [vendor agreement]`.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- It doesn't replace a conversation with the PM. Often the PRD is wrong or out of date — the review surfaces questions, a human asks them.
- It doesn't approve the launch. It informs the approval.
- It doesn't retroactively calibrate. If this launch turns out fine (or badly) in a way that should update the calibration table, a human updates ~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md.

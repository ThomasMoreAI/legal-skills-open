---
name: pia-generation-bossmann007
title: 'Pia generation'
description: Gera um Relatório de Impacto à Proteção de Dados Pessoais (RIPD — Art. 38 LGPD, equivalente brasileiro à DPIA) em formato de casa para nova funcionalidade, produto ou atividade de tratamento, usando a estrutura aprendida do seu RIPD-semente. Use quando o usuário disser "escreve um RIPD", "relatório de impacto para", "precisa de RIPD pra isso", "revisão de privacidade dessa feature", ou descrever nova atividade de tratamento de dados.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/privacy-legal/skills/pia-generation
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# /pia-generation

1. Load `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → PIA house style (trigger, structure, depth, sign-off).
2. Run the workflow below.
3. Check: is a PIA actually needed? (House trigger + research the mandatory-assessment triggers for each applicable regime — cite primary sources, verify currency.)
4. Intake: ask the product-team questions. Can pull from PRD if provided.
5. Write PIA in house format. Include privacy policy consistency check.
6. Output with conditions list and named owners. Route for sign-off.

```
/privacy-legal:pia-generation "Location sharing feature"
```

```
/privacy-legal:pia-generation
PRD: [Drive link]
```

---

# PIA Generation

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/privacy-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Destination check

Before producing output, check where it's going. If the user has named a destination (a channel, a distribution list, a counterparty, "everyone"), ask whether it's inside the privilege circle. Public channels, company-wide lists, counterparty/opposing counsel, vendors, and clients (for work product) waive the protection. When the destination looks outside the circle, flag it and offer (a) the privileged version for legal only, (b) a sanitized version for the broader channel, or (c) both — don't silently apply a privileged header and then help paste it somewhere the header won't protect it. See the canonical `## Shared guardrails → Destination check` in this plugin's CLAUDE.md.

## Purpose

A PIA is a conversation with the product team, captured. It asks: what data, why, how long, who sees it, what could go wrong. This skill structures that conversation and writes the output in this team's format — the one learned from the seed PIA during cold-start.

## Premissa de jurisdição

Esta avaliação assume a LGPD (Lei 13.709/2018) como base. O Art. 38 LGPD dá à ANPD poder de exigir RIPD "quando o tratamento de dados pessoais tiver como fundamento o legítimo interesse" ou, mais amplamente, sempre que o tratamento envolver risco às liberdades civis e aos direitos fundamentais. O Art. 5º, XVII, LGPD define o RIPD. Um regulamento dedicado da ANPD sobre RIPD ainda não está vigente (esteve em consulta pública) — verificar a norma atual antes de afirmar estrutura obrigatória; não confundir com a Res. CD/ANPD nº 18/2024, que trata da atuação do encarregado (DPO), não do RIPD. Se a atividade, o controlador, ou os titulares afetados estiverem sob outra jurisdição (ex.: GDPR se houver titulares na UE), sinalizar e não aplicar apenas o framework LGPD.

## Load prior context on this feature / activity

Before writing a new PIA, check the outputs folder for prior work on the same feature, processing activity, or counterparty. Read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## Outputs` for the path. Scan for:

- **Prior `use-case-triage` results** covering this activity — the triage's risk rating, mandatory conditions, and called-out concerns are the entry point for the PIA.
- **Prior `pia-generation` outputs** for the same or an overlapping activity — a superseding PIA should reconcile (what changed, what carried over). A PIA that silently produces different conclusions than a prior PIA on the same activity is a contradiction a reviewing attorney cannot see.
- **Prior `dpa-review` outputs** for vendors in scope — the DPA review's findings inform the PIA's analysis of subprocessor / cross-border / retention risk.

If a prior output is found, cite it in the PIA:

> "Prior triage ([date]) rated this [risk level] and required [conditions]. This PIA builds on that finding — [which conditions are satisfied, which remain, which are re-scoped]."

If a prior PIA exists:
> "This PIA supersedes the [date] PIA because [reason — scope change, new data category, vendor change, regulatory change]. Conclusions carried over: [X]. Conclusions revised: [Y, because Z]."

**Carry severity from upstream as a floor** per the cross-skill severity floor rule in `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## Shared guardrails`. A use-case-triage that rated the activity high-risk cannot become a PIA that concludes low-risk without stating why and what changed.

If no prior output is found, say so explicitly — "No prior triage or PIA on this activity in outputs folder; this is a cold start" — so the reviewing attorney knows the check ran and didn't find anything to reconcile.

## Load house style

Read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## PIA house style`. That has:
- What triggers a PIA here (may not match regulatory DPIA triggers — some teams PIA everything, some only high-risk)
- The structure template extracted from the seed PIA
- Typical depth
- Who signs off

If the seed PIA structure is in the config CLAUDE.md, **use it**. The point is that this PIA looks like the other PIAs this team produces, not like a generic one.

## Step 0: Is a PIA needed?

Check the trigger criteria in `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`. That is the team's house answer.

Além disso, **pesquisar os gatilhos de avaliação obrigatória vigentes** sob a LGPD e regulamentação ANPD: tratamento fundado em legítimo interesse (Art. 10, §3º — a ANPD pode exigir RIPD específico); tratamento de dados sensíveis em larga escala (Art. 11); tratamento envolvendo crianças/adolescentes (Art. 14); decisões automatizadas que afetem interesses do titular (Art. 20 — o titular pode solicitar revisão, e RIPD é boa prática defensiva); qualquer operação de alto risco às liberdades civis e direitos fundamentais (Art. 38, que autoriza a ANPD a exigir RIPD). Se houver footprint regulatório adicional (GDPR/UK GDPR, CCPA/CPRA), pesquisar os gatilhos específicos desses regimes também. Citar a norma controladora com referências pontuais. Verificar atualidade — um regulamento dedicado da ANPD sobre RIPD ainda não está vigente (esteve em consulta pública); não confundir com a Res. CD/ANPD nº 18/2024, que trata do encarregado (DPO). Sinalizar incerteza em vez de supor.

> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for a regime's DPIA / risk-assessment triggers or lawful-basis rules, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [regime / question]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution.** Tag every citation in the PIA with where it came from: `[JusBrasil]`, `[regulator site]`, or the MCP tool name for citations retrieved from a legal research connector; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations the user supplied. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

Beyond statutory mandates, treat these as **strong indicators** that a PIA is worth doing even if not strictly mandatory (research whether any of them independently triggers a mandatory assessment under the applicable regime):

- New technology or novel use of existing tech
- Children's data
- Combining datasets that weren't collected together
- Data that could enable discrimination
- Processing that users wouldn't expect

If no statutory trigger applies and the house trigger also isn't met → "Doesn't look like this needs a PIA. Here's a one-paragraph note for the file explaining why, in case anyone asks."

## The intake

Before writing anything, get answers to these from the product team. Conversational is fine — this isn't a form to send them.

### What and why

- What's the feature/product/change?
- What problem does it solve for users?
- What personal data does it touch? Be specific — "user data" is not an answer. Which fields?
- Is any of it new collection, or is it all data you already have?
- What's the processing — storage, analysis, sharing, automated decisions?

### Legal basis / regime-specific checks

For each applicable regime, **research the currently operative framework** for the question below and cite primary sources:

- Sob a LGPD, identificar a hipótese legal do Art. 7º para cada finalidade (consentimento / cumprimento de obrigação legal / execução de política pública / estudo por órgão de pesquisa / execução de contrato / exercício regular de direito / proteção da vida / tutela da saúde / legítimo interesse / proteção do crédito) ou, se dado sensível, do Art. 11 (mais restrito — consentimento específico e destacado, ou exceções taxativas). Legítimo interesse (Art. 10) exige teste de balanceamento documentado e é a hipótese mais escrutinada pela ANPD — pesquisar e citar autoridade controladora.
- Verificar se algum fluxo de dados envolve compartilhamento com terceiros para fins de publicidade/monetização — sob a LGPD isso normalmente exige base legal própria (consentimento específico ou legítimo interesse com teste de balanceamento robusto), não há categoria equivalente ao "sale"/"share" da CCPA, mas o escrutínio da ANPD sobre publicidade direcionada é crescente.
- Sob regimes setoriais (dados de saúde — Art. 11 + regulação ANS/CFM; dados financeiros — LC 105/2001; dados de criança — Art. 14), pesquisar regras específicas de base legal ou divulgação.

Verify currency; statutory definitions and bases are amended often. Flag uncertainty for attorney verification.

### Who and where

- Who inside the company can see this data? Engineers? Support? Analysts?
- Any third parties? Vendors, partners, analytics?
- Where is it stored? Which region? New infrastructure or existing?
- How long is it kept? Is there a deletion schedule or does it live forever?

### What could go wrong

- If this data leaked, what's the harm to the person?
- Could this data be used to discriminate, even accidentally?
- Would users be surprised this is happening? (The "creepy test" — not a legal standard but a useful one.)
- Is there an opt-out? Should there be?

## Writing the PIA

**Use the seed PIA structure from the config CLAUDE.md.** If none was captured, use this default. Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` `## Outputs` (it differs by user role — see `## Who's using this`).

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# Privacy Impact Assessment: [Feature/Product Name]

**Prepared by:** [name] | **Date:** [date] | **Status:** DRAFT / APPROVED
**Product owner:** [name] | **Privacy reviewer:** [name]

---

## Executive summary

[Two sentences: what this is, whether it's okay. E.g., "Feature X collects
location data to provide Y. Processing is consistent with existing privacy
policy commitments and uses consent as lawful basis. Two mitigations
recommended below; no blockers identified."]

**Overall risk:** [Reviewer to set: 🟢 Low / 🟡 Medium / 🟠 High / 🔴 Very high]

---

## 1. Description of processing

**What:** [the feature, in plain English]
**Data categories:** [specific fields — not "user data"]
**Data subjects:** [customers / end users / employees / etc.]
**Purpose:** [why — tie to user benefit]
**New collection?** [yes — these fields are new / no — reusing existing data]

---

## 2. Lawful basis

| Purpose | Basis | Notes |
|---|---|---|
| [purpose 1] | [Contract / LI / Consent / etc.] | [if LI: balancing test summary; if consent: how obtained] |

---

## 3. Data flow

**Collection:** [how/where data enters]
**Storage:** [system, region, encryption]
**Access:** [who, via what controls]
**Sharing:** [third parties, purpose, governed by which DPA]
**Retention:** [how long, deletion mechanism]

---

## 4. Privacy policy consistency

| Policy commitment | Consistent? | Notes |
|---|---|---|
| [commitment from config CLAUDE.md privacy policy section] | 🟢 / 🟡 | |

[If any 🟡: policy update needed before launch, or processing needs to change]

---

## 5. Risks and mitigations

| # | Risk | Likelihood | Impact | Mitigation | Status | Owner |
|---|---|---|---|---|---|---|
| 1 | [specific risk, tied to the design — not "data breach" generically] | L/M/H | L/M/H | [specific control] | Done / Planned / Gap | [name] |

**Residual risk after mitigations:** [assessment]

---

## 6. Data subject rights

| Right | Can be exercised? | How |
|---|---|---|
| Access | | |
| Deletion | | |
| Correction | | |
| Portability | | |
| Objection | | |

---

## 7. Recommendation

[APPROVED / APPROVED WITH CONDITIONS / CHANGES REQUIRED / NOT APPROVED]

**Conditions (if any):**
- [ ] [specific thing that has to happen before launch]

**Sign-off:** [name, date]
```

## Risk quality standards

Risks in a PIA should be **specific and tied to the design**, not generic. Bad risks pad the document and train readers to skim.

| Bad risk | Why bad | Better |
|---|---|---|
| "Data breach" | Applies to everything; says nothing | "Location history accessible by support staff via the admin panel without audit logging — a malicious insider could track a user undetected" |
| "Descumprimento da LGPD" | Circular — o RIPD existe para *avaliar* conformidade | Nomear o artigo específico e o gap |
| "Users might not like it" | Vague | "Users who opted out of marketing may still receive this because the opt-out flag isn't checked in this flow" |

Aim for 2-5 real risks, not 15 padded ones.

## Privacy policy diff

Every PIA should cross-check against the privacy policy commitments in `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`. The common drift:

- Policy says "we collect X, Y, Z" — new feature collects W. Policy needs updating, or stop collecting W.
- Política diz "não compartilhamos dados com terceiros" — nova feature compartilha com parceiro de anúncios. Isso exige base legal própria e atualização da política (Art. 9º LGPD — transparência). [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]
- Policy says retention is "as long as your account is active" — new feature keeps data post-deletion.

Flag every mismatch. One of them has to change before launch.

## Handoff

- **To product team:** Conditions list with owners and deadlines. Not "improve security" — "add audit logging to the admin panel's location lookup, owner: [eng lead], before launch."
- **To reg-gap-analysis skill:** If the PIA uncovered a policy inconsistency, that skill tracks the policy update.
- **To the sign-off process:** Per `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → who approves PIAs.

## Gate: submitting a DPIA to a regulator

Producing an internal PIA is research and documentation. *Submitting a DPIA to a supervisory authority* — or voluntarily disclosing one to a regulator in response to an inquiry — is the consequential act.

**Before proceeding to submit a DPIA (or any equivalent impact assessment) to a regulator, supervisory authority, or enforcement body:** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`. If the Role is Non-lawyer:

> Submitting to a regulator has legal consequences — the document becomes part of the supervisory record and any material omission or error becomes enforcement exposure. Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: regime and regulator, why a submission is being made (mandatory trigger or voluntary), the risks identified, residual risk after mitigations, any flagged uncertainty, and the three things to ask the attorney before filing.]
>
> If you need to find a licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction: your professional regulator's referral service is the fastest starting point (state bar in the US, SRA/Bar Standards Board in England & Wales, Law Society in Scotland/NI/Ireland/Canada/Australia, or your jurisdiction's equivalent).

Do not proceed past this gate without an explicit yes.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- It doesn't approve the processing. A human signs the PIA.
- It doesn't write a DPIA for a supervisory authority — that's a more formal document with specific regulatory requirements. This is the internal assessment.
- It doesn't design the mitigation. It describes what needs mitigating; engineering designs the fix.

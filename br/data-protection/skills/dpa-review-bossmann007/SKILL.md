---
name: dpa-review-bossmann007
title: 'DPA review'
description: Revisa um contrato/cláusula de tratamento de dados (equivalente brasileiro à DPA, fundamentado na LGPD Lei 13.709/2018) contra seu playbook — detecta automaticamente se você é operador (contrato do cliente) ou controlador (contrato do fornecedor) e aplica a metade correta do playbook. Use quando o usuário disser "revisa esse contrato de tratamento de dados", "cliente mandou o DPA", "esse contrato de dados tá ok", ou anexa um contrato.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/privacy-legal/skills/dpa-review
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# /dpa-review

1. Carregar `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → playbook de contrato de tratamento. Se houver placeholders, parar e pedir setup.
2. Obter o contrato. Determinar direção: somos operador (contrato enviado pelo cliente, Art. 5º, VII LGPD) ou controlador (contrato enviado a fornecedor, Art. 5º, VI LGPD)? Perguntar se ambíguo.
3. Run the workflow below — term-by-term against the appropriate playbook row.
4. Run privacy policy consistency check.
5. Output: review memo with redlines. Save per house style.

```
/privacy-legal:dpa-review customer-dpa.pdf
```

---

# DPA Review

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/privacy-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

DPAs come in two flavors and the review is nearly opposite for each. When a customer sends their DPA, we're defending our operational flexibility. When we send one to a vendor, we're protecting our (and our customers') data. Both reviews read from the same `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` playbook but from opposite rows.

## First: which direction?

Before anything else, establish:

- **We are the processor** → customer is sending us their DPA → read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → "When we are the processor" table
- **We are the controller** → we're sending a DPA to a vendor (or reviewing theirs) → read "When we are the controller" table

If unclear, ask. Getting this wrong inverts every recommendation.

## Premissa de jurisdição

Esta revisão assume a LGPD (Lei 13.709/2018) como base regulatória, com a ANPD como autoridade fiscalizadora. Prazos de resposta, bases legais (Art. 7º/11) e regras de transferência internacional (Art. 33) variam se o controlador, operador ou titulares estiverem sujeitos a outro regime (ex.: GDPR se houver titulares na UE, LGPD não afasta LC 105/2001 para dados bancários nem o marco regulatório setorial do BACEN/CVM). Se o contrato envolve dados fora do escopo puramente doméstico brasileiro, sinalizar isso explicitamente antes de aplicar o playbook.

## Load prior context on this counterparty / activity

Before reviewing, check the outputs folder for prior work on this counterparty or processing activity. Read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## Outputs` for the outputs folder path. Scan for:

- **Prior `use-case-triage` results** for the same counterparty / processing activity — the triage produces a risk rating and conditions that this DPA review should honor or explicitly depart from.
- **Prior `pia-generation` outputs** covering this counterparty / processing activity — the PIA may have flagged risk mitigations the DPA needs to implement.
- **Prior `dpa-review` outputs** for the same counterparty — earlier DPA reviews set expectations about what was acceptable, what was flagged, and what was settled. A fresh review that silently contradicts the earlier one erodes trust in the work product.

If a prior output is found, cite it in the review:

> "Prior triage ([date]) rated this [risk level] and conditioned approval on [X]. This DPA review is consistent with that finding." — or —
> "Prior triage ([date]) rated this [risk level]. This DPA review departs from that finding because [reason — new facts, different scope, contract term that changed the picture]."

**Carry severity from the upstream output as a floor** per the cross-skill severity floor rule in `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## Shared guardrails`. A processing activity the triage rated 🔴 cannot be quietly downgraded to 🟢 in the DPA review; any demotion is stated and explained.

If no prior output is found (new counterparty / new activity), say so explicitly in the review — "No prior triage or PIA on this counterparty in outputs folder" — so the reviewing attorney knows the check ran.

## Load the playbook

Read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## DPA playbook`. Also read `## Privacy policy commitments` — the DPA can't contradict what the privacy policy promises.

## Sobreposição setorial brasileira (perguntar antes da revisão termo a termo)

Antes de percorrer a revisão termo a termo, responder: **os dados que passam por este contrato incluem alguma categoria sujeita a regime setorial específico, além da LGPD geral?** A LGPD estabelece o piso geral; regimes setoriais brasileiros frequentemente impõem obrigação adicional que não aparece no playbook genérico.

> **Sobreposições setoriais baseadas em atividade — perguntar primeiro:**
>
> Este tratamento envolve:
> - **Dados pessoais sensíveis** (Art. 5º, II c/c Art. 11 LGPD: origem racial/étnica, convicção religiosa, opinião política, filiação sindical, dado referente à saúde ou vida sexual, dado genético/biométrico)? Se sim, o contrato precisa exigir hipótese legal específica do Art. 11 (consentimento destacado ou uma das exceções), medidas de segurança reforçadas, e proibição de uso para discriminação ilícita.
> - **Dados de crianças e adolescentes** (Art. 14 LGPD)? Se sim, o contrato precisa exigir: consentimento específico e destacado de ao menos um dos pais/responsável (exceto coleta mínima necessária), interesse do melhor interesse da criança, proibição de condicionar acesso a fornecimento de dados além do necessário, e vedação a compartilhamento sem novo consentimento.
> - **Dados financeiros/bancários** (sigilo bancário, LC 105/2001; Resoluções BACEN sobre Open Finance/Sistema Financeiro Aberto)? Se sim, o contrato precisa de cláusula de sigilo bancário compatível com a LC 105, e — se Open Finance — conformidade com o padrão de compartilhamento regulado pelo BACEN.
> - **Dados de saúde tratados por operadora de plano de saúde, hospital ou prestador de serviço de saúde** (dado sensível de saúde, Art. 11 LGPD + regulação ANS quando aplicável)? Se sim, o contrato precisa de cláusula de finalidade restrita a prestação do serviço de saúde, retenção compatível com prontuário médico (mínimo 20 anos, Resolução CFM 1.821/2007), e vedação a uso para fins de subscrição de risco sem base legal específica.
> - **Dados de consumidor sob relação de consumo** (CDC, Lei 8.078/1990)? Se sim, verificar se o contrato de tratamento respeita direitos de informação e transparência do Art. 6º, VIII CDC, cumulativos com a LGPD.
> - **Outro regime setorial** (dados de geolocalização/tracking sob regulação de proteção veicular, dados de comunicação sob sigilo das comunicações Art. 5º, XII CF/88, dados públicos sob a Lei de Acesso à Informação)?
>
> Se sim a qualquer um: o regime setorial normalmente soma-se à LGPD, não a substitui — nenhuma exceção setorial dispensa integralmente as obrigações gerais da LGPD (dever de segurança, resposta a incidente, direitos do titular). Pesquisar a norma vigente e citá-la. Sinalizar gaps setoriais na lista de pontos críticos junto aos gaps de LGPD geral.

Se nenhuma sobreposição setorial se aplica, registrar isso explicitamente — "nenhuma categoria setorial identificada; sobreposição setorial n/a" — para que o advogado revisor veja que a checagem ocorreu.

## The term-by-term review

### Core terms (check every DPA)

Walk every DPA through these terms, clause by clause. The *specific* numeric and substantive positions (notice periods, breach timelines, acceptable/unacceptable floors) come from `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## DPA playbook`. The regulatory floors that any DPA has to clear come from primary law — **research the currently operative rule** for each applicable regime and cite primary sources before stating a floor.

> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for a regime's breach window, transfer-mechanism requirement, subprocessor-change rule, or any other floor, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [regime / topic]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution tiering.** Tag every citation in the review — regulatory floors, SCC versions, adequacy decisions, regulator guidance, case law — with its source. For model-knowledge citations, use one of three tiers rather than a single blanket "verify" tag:
>
> - `[settled]` — stable, well-known statutory and regulatory references unlikely to have changed (e.g., GDPR Art. 28, Art. 33 72-hour breach notice, SCC Decision 2021/914 by number). Still verify before filing, but lower priority.
> - `[verify]` — model-knowledge citations that are real but should be verified: specific implementing regulations, regulator guidance, case holdings, adequacy decisions, SCC modules and versions, UK Addendum / IDTA status, thresholds, effective dates.
> - `[verify-pinpoint]` — pinpoint citations (specific subsection letters, clause numbers within SCCs, paragraph numbers, volume/page references) carry the highest fabrication risk and should ALWAYS be verified against a primary source.
>
> Tool-retrieved citations keep their source tag (`[JusBrasil]`, `[Commission / regulator site]`, or the MCP tool name); web-search citations remain `[web search — verify]`; user-supplied citations remain `[user provided]`. The tiering surfaces the real verification work — a reader who verifies everything verifies nothing. Never strip or collapse the tags.

| Term | Looking for | Playbook field | Common fights |
|---|---|---|---|
| **Papéis (Art. 5º, VI/VII LGPD)** | Designação clara controlador/operador; compatível com a realidade | — | Contraparte rotula a relação (ex.: "controlador conjunto") de forma que não bate com a realidade |
| **Escopo do tratamento** | Limitado a instruções documentadas; finalidades definidas (Art. 6º, I — princípio da finalidade) | — | Expansores de escopo abertos ("e finalidades correlatas") |
| **Suboperadores** | Lista atual divulgada, mecanismo de mudança definido | Troca de suboperador | Aprovação geral vs. veto vs. mera notificação |
| **Medidas de segurança** | Anexo referencia controles ou padrões específicos (Art. 46 LGPD — medidas técnicas e administrativas) | Padrões de segurança | "medidas técnicas e administrativas apropriadas" sem anexo = promessa vazia |
| **Notificação de incidente** | Gatilho definido ("descoberta" vs "confirmação"), prazo definido (Art. 48 — "prazo razoável" à ANPD) | Notificação de incidente | Aperto do prazo; gatilho do relógio; "sem demora indevida" é vago |
| **Direito de auditoria** | Método (relatório vs. presencial), frequência, aviso prévio, alocação de custo | Direitos de auditoria | Auditorias presenciais com aviso curto |
| **Transferência internacional** | Mecanismo de transferência identificado (Art. 33 LGPD), medidas suplementares | Transferências | Mecanismos de transferência ausentes ou desatualizados |
| **Eliminação/devolução** | Prazo pós-término, certificação, ressalva de backup (Art. 15/16 LGPD) | Eliminação ao término | "prazo comercialmente razoável" de eliminação = vago demais |
| **Responsabilidade** | Dentro do teto contratual ou separado; ressalvas; responsabilidade solidária do Art. 42, §1º | Responsabilidade pelos dados | Responsabilidade ilimitada por vazamento de dados = risco existencial |

### When we're the processor: defensive review

Customer DPAs try to push operational burden onto us. For each clause below, compare the customer's ask to the playbook. Where the customer's ask is outside the playbook, push back to the team's standard position (from the config CLAUDE.md) and be ready to fall back to the acceptable position.

| Clause | Risk | Research / playbook lookup |
|---|---|---|
| Subprocessor approval right (veto) | Can't add infrastructure without customer-by-customer approval | Apply playbook position on subprocessor changes |
| On-site audit on short notice | Unworkable at scale | Apply playbook position on audit rights |
| Aggressive breach notification window | Often demands notice before we know what happened | Research the regulatory floor for each applicable regime (cite primary sources); compare to playbook position |
| Hard data residency (single country/DC) | May not match architecture | Apply playbook position on data location; confirm what we can actually commit to |
| Processor liability uncapped | Bet-the-company | Apply playbook position on liability for data |
| Customer may issue binding "instructions" | Open-ended operational control | Define instructions as "documented in the Agreement or agreed in writing" |
| Deletion on very short timeline | Backup and log retention makes this impossible | Apply playbook position on deletion on termination; document backup rotation carveout |

### When we're the controller: protective review

Vendor DPAs try to give us nothing. For each clause below, compare to the controller-side playbook.

| Clause | Gap | Research / playbook lookup |
|---|---|---|
| No subprocessor list | Don't know who touches our data | Require published current list + advance notice per playbook |
| "Industry standard security" | Means nothing | Require annex with specific controls, or reference to a named standard (e.g., SOC 2, ISO 27001) |
| No breach notification timeline | They tell us whenever | Research applicable regulatory floor; require playbook position |
| No audit rights at all | Can't verify anything | Require at minimum an independent audit report per playbook |
| Vendor can use data for "service improvement" | Potential training on our data | Strike; processing limited to providing the service to us |
| No international transfer mechanism | No lawful transfer mechanism | **Research the currently operative transfer mechanism** for the corridor in question (origin/destination jurisdictions, applicable regime, any adequacy decision, any supplementary measures). Cite primary sources and verify currency. |
| No deletion commitment | Data lives forever | Require playbook position on deletion + certification on request |

## Consistency check: privacy policy

The DPA you sign can't promise something the privacy policy doesn't cover, and vice versa.

- If the DPA commits to processing only for purposes X, Y, Z — does the privacy policy list those purposes?
- If the privacy policy says "we never sell data" — does any DPA clause look like a sale under CCPA?
- If the privacy policy names specific subprocessor categories — does the DPA subprocessor list match?

Flag mismatches. They're usually the privacy policy being stale, not the DPA being wrong, but someone needs to fix one of them.

## Redline granularity

**Edit at the smallest possible granularity.** A redline is a negotiation artifact, not a rewrite. Wholesale clause replacement signals "we threw out your drafting" — it's aggressive, it forces the counterparty to re-read the whole clause, and it discards the parts of their drafting that were fine. Surgical redlines — strike a word, insert a phrase, restructure a subclause — signal "we have specific asks" and are faster to read, understand, and accept.

Default to the smallest edit that achieves the playbook position:
- Replace a **word** before a phrase. ("twelve (12)" → "twenty-four (24)")
- Replace a **phrase** before a sentence. ("paid by the Buyer" → "paid and payable by the Buyer")
- Restructure a **subclause** before replacing the sentence. (Add "(a)" and "(b)" to split a compound condition.)
- Replace a **sentence** before replacing the clause.
- Only replace a **whole clause** when the counterparty's version is so far from your position that surgical edits would be harder to read than a fresh draft — and when you do, say so in the transmittal: "We've replaced §8.2 rather than marking it up because the changes were extensive. Happy to walk you through the delta."

When in doubt, smaller. A client who receives a surgical redline trusts that you read carefully. A client who receives a wholesale replacement wonders whether you read at all.

## Output

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` `## Outputs` (it differs by user role — see `## Who's using this`).

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# DPA Review: [Counterparty]

**Direction:** [We are processor / We are controller]
**Reviewed:** [date]
**Attached to:** [MSA / standalone]

---

## Bottom line

[Two sentences. Can we sign? What has to change?]

**Issues:** [N]🟢 [N]🟡 [N]🟠 [N]🔴

---

## Term-by-term

[For each core term, use a standard deviation-memo format: what the
counterparty's DPA says, what our playbook says, the gap, the risk, and the
proposed redline language. Keep each term to a short self-contained block so a
reviewer can skim.]

---

## Privacy policy consistency

[🟢 Consistent | 🟡 Flags: list]

---

## Recommended redlines

[Consolidated — ready to send back]

---

## If they won't move

[For each issue: the fallback from the config CLAUDE.md, or escalation routing if no
fallback exists]
```

## Nota sobre transferência internacional (Art. 33 LGPD)

Se o contrato contempla transferência de dados para fora do Brasil, **pesquisar o mecanismo de transferência vigente** para o corredor aplicável. A LGPD (Art. 33) permite transferência internacional apenas quando: (I) o país/organismo de destino proporciona grau de proteção adequado; (II) o controlador oferecer garantias de cumprimento via cláusulas contratuais específicas, cláusulas-padrão contratuais, normas corporativas globais, ou selo/certificado; (III) a transferência for necessária para cooperação jurídica internacional; (IV) necessária para proteção da vida/incolumidade física; (V) autorizada pela ANPD; (VI) resultar de compromisso assumido em acordo de cooperação internacional; (VII) necessária para execução de política pública; (VIII) o titular tiver fornecido consentimento específico e destacado (Art. 33, VIII); ou (IX) necessária para cumprimento de obrigação legal/regulatória. Citar fontes primárias (LGPD, resoluções ANPD, guias oficiais) e verificar atualidade — a ANPD lista a Res. CD/ANPD nº 19/2024 como vigente e regulando transferência internacional e cláusulas-padrão contratuais. [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm; https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd]

Se falta mecanismo de transferência e há transferência internacional, isso é 🔴 — não há base legal para a transferência (risco de multa até 2% do faturamento, Art. 52 LGPD). [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]

## Gate: signing a DPA

Reviewing a DPA is research. *Signing* it — or instructing someone to countersign on our behalf — is the consequential act.

**Before proceeding to sign or countersign a DPA (including returning an executed version, consenting to automatic execution on a counterparty platform, or instructing a signatory to execute):** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`. If the Role is Non-lawyer:

> Signing a DPA is a legal act — it binds the company to specific data-protection obligations that flow to regulators and data subjects. Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: counterparty, direction (we are processor / controller), the terms that deviate from the playbook and how they were resolved, any open fallback decisions, and the three things to ask the attorney before executing.]
>
> Se precisar localizar um advogado inscrito: a Ordem dos Advogados do Brasil (OAB) mantém serviço de busca de advogados por seccional (OAB/UF) — comece pela seccional do seu estado, ou pela Comissão de Direito Digital da OAB para especialistas em LGPD.

Do not proceed past this gate without an explicit yes.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer picks.

## What this skill does not do

- It doesn't draft a DPA from scratch. If the answer is "use our template," pull the template from the seed docs path in the config CLAUDE.md.
- It doesn't do the Transfer Impact Assessment itself — it flags when one is needed.
- It doesn't decide whether to accept terms outside the fallbacks. It routes those per the escalation table.

---
name: ecommerce-compliance-review-bossmann007
title: E-commerce Compliance Review
description: 'Revisão de conformidade de loja virtual com regulação de e-commerce brasileira: informações obrigatórias (Decreto 7.962/2013), direito de arrependimento (CDC), condições de entrega, atendimento ao consumidor. Rascunho para revisão de advogado.'
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/digital-ecommerce-legal/skills/ecommerce-compliance-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# E-commerce Compliance Review

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/digital-ecommerce-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/digital-ecommerce-legal/matters/<matter-slug>/`.

---

## Purpose

E-commerce in Brasil is regulated by the Decreto 7.962/2013 (e-commerce regulations), the CDC (Lei 8.078/1990 — consumer protection), and the Marco Civil (Lei 12.965/2014 — internet providers' safe harbors and liability). This skill performs a checklist review of an online store's operations and documentation against these regimes.

It identifies what's missing, what's wrong, and what needs legal opinion before the store launches or continues operating.

## Jurisdiction assumption

**Premissa de jurisdição (Brasil):** O Decreto 7.962/2013 regulamenta o comércio eletrônico e a relação entre fornecedor de produtos ou serviços (online) e o consumidor (comprador final, Art. 2º CDC). A loja deve fornecer informações obrigatórias (Art. 5º, Decreto 7.962/2013 — identidade do fornecedor, descrição do produto, preço total, frete, prazos, condições de pagamento, garantia legal, direito de arrependimento, atendimento); o consumidor tem direito de arrependimento de 7 dias (Art. 49 CDC [verified: https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm]); forma e prazo da entrega ou disponibilização do produto devem ser informados (Art. 2º, V, Decreto 7.962/2013 [verified: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/decreto/d7962.htm]). Se a loja envolver dados pessoais (nome, email, endereço), a LGPD (Lei 13.709/2018) é aplicável de forma adicional. Ver `privacy-legal:pia-generation` para análise detalhada. Se houver marketplace (loja dentro de plataforma terceira), analisar arts. 19 Marco Civil (isenção do provedor) — mas Marco Civil isenção não afasta responsabilidade pela conformidade própria da loja.

> **No silent supplement.** If a research query to the configured legal research tool (JusBrasil, Escavador) returns few or no results for a requirement under Decreto 7.962/2013, CDC articles, or Marco Civil, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [requirement]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution.** Where the review cites a statute or regulation, tag the citation: `[JusBrasil]`, `[Escavador]`, `[statute / gov.br]`, or the MCP tool name; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

## Load the playbook

Read `~/.claude/plugins/config/claude-for-legal/digital-ecommerce-legal/CLAUDE.md` first. Any specific compliance positions the team has recorded there (which certifications are mandatory, how strictly to interpret the 7-day window, whether arbitration is acceptable) apply to this review.

If the config is not yet populated, ask: "Your team's positions on e-commerce compliance haven't been configured yet — run `/digital-ecommerce-legal:cold-start-interview` to set them up, or I can run this review against default LGPD/CDC/Decreto 7.962 standards and flag items for your judgment."

## The checklist

Run through each item below. For each MISSING or WRONG item, flag it. For each item that's borderline or gray, tag it `[review]` for attorney judgment.

### 1. Informações obrigatórias do fornecedor (Art. 5º, Decreto 7.962/2013)

- [ ] **Identidade clara** (nome, CNPJ, razão social visível)
- [ ] **Endereço completo** (não apenas email / WhatsApp)
- [ ] **Contato** (email + telefone, não só formulário inacessível)
- [ ] **Termos de Uso** (link visível no rodapé ou homepage; não escondido)

### 2. Informações sobre os produtos / serviços (Art. 5º, II/III, Decreto 7.962/2013)

- [ ] **Descrição clara e completa** (não apenas foto; texto descritivo)
- [ ] **Características técnicas** (tamanho, cor, compatibilidade, se aplicável)
- [ ] **Preço total destacado** (incluindo impostos, frete)
- [ ] **Disponibilidade** ("em estoque" vs. "sob encomenda"; prazo claro)
- [ ] **Garantia legal** (prazo de 30 dias para fornecimento de serviço e produto não duráveis; 90 dias para fornecimento de serviço e produto duráveis — CDC Art. 26 [verified: https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm])

### 3. Direito de arrependimento (CDC Art. 49)

- [ ] **Prazo explícito:** "7 dias corridos para desistir da compra"
- [ ] **Processo claro:** Como o consumidor inicia o arrependimento? (Formulário / email / chat)
- [ ] **Responsabilidade pela devolução:** Quem paga frete de retorno?
- [ ] **Reembolso:** Em quanto tempo o dinheiro volta?

### 4. Frete e entrega (Art. 2º, V, Decreto 7.962/2013)

- [ ] **Responsabilidade clara:** Quem é responsável se o produto não chegar?
- [ ] **Prazo estimado** (e.g., "3-5 dias úteis" — não "em breve")
- [ ] **Rastreamento oferecido** (opcional mas boa prática)
- [ ] **Endereço de entrega:** Loja permite endereço diferente do registrado?

### 5. Formas de pagamento e segurança

- [ ] **Múltiplas opções** (cartão, boleto, Pix, etc.)
- [ ] **HTTPS / SSL** (loja usa certificado?)
- [ ] **Aviso de segurança** ("seus dados são criptografados")
- [ ] **Não armazena dados sensíveis** (loja armazena CVV? Não deve — violação LGPD [unverified: not found in primary source])

### 6. Política de privacidade (LGPD Art. 5, II / Marco Civil Art. 7º, II)

- [ ] **Existe e é acessível** (não escondida)
- [ ] **Compatível com LGPD** (quais dados coleta, por quê, com quem compartilha)
- [ ] **Consentimento para marketing** (opt-in claro, não pré-checado)
- [ ] **Direitos do titular** (consumidor pode solicitar acesso, correção, exclusão)

### 7. Atendimento ao consumidor (Art. 6º, CDC)

- [ ] **Acesso fácil** (não enterrado em FAQ inacessível)
- [ ] **Email de resposta efetiva** (não inválido)
- [ ] **Prazo de resposta** (ANPD recomenda ≤15 dias para SARs [verified: https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados-1/direito-dos-titulares])
- [ ] **Forma de registro de reclamação** (loja registra ticket?)

### 8. Condições de pagamento e crédito (Art. 39, CDC)

- [ ] **Não há "surpresas" de interesse** (crédito parcelado exibe taxa de juros legível)
- [ ] **Não há "cobranças automáticas ocultas"** (renovação, assinatura, carrinho pré-preenchido)
- [ ] **Prazo de vencimento claro** (boleto, Pix com data/hora, cartão com data de cobrança)

## Consequential-action gate

**Before emitting findings that would block a store's operation or require remediation before launch:**

Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/digital-ecommerce-legal/CLAUDE.md`. If the Role is Non-lawyer:

> This is a compliance review — recommendations flow to business and product teams. If the review identifies blocking issues (missing mandatory information, unsafe payment handling, LGPD non-compliance), those should be reviewed with your attorney before proceeding. Have you consulted? If yes, proceed. If no, here's a brief for your attorney:
>
> [Summary: loja identidade do fornecedor/descrição produto/preço, informações de frete, direito arrependimento, atendimento, LGPD compliance — blockers identified [list], non-blockers [list], timeline for remediation.]

Do not proceed to "Clear to launch" without an explicit yes.

## Output

Format as a checklist summary + detailed findings with items marked ✅ 🟡 🔴.

## What this skill does not do

- It doesn't audit code or security. That's a separate security review.
- It doesn't check payment-processor compliance (PCI-DSS, TokenEx, etc.). That's on the processor.
- It doesn't verify that descriptions match the actual product — that's a product QA job.

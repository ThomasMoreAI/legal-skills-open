---
name: honorarios-contract-bossmann007
title: /honorarios-contract
description: Gera rascunho de contrato de honorários advocatícios com atenção às hipóteses legais (sucumbência, honorários por êxito, quota litis) e aos limites éticos. Rastrea estrutura de honorários (pró-labore, tabela OAB, porcentagem) e cláusulas de reajuste, revogação e suspensão. Use quando o cliente disser "escreve um contrato de honorários", "preciso formalizar os honorários", "contrato de quota litis", ou descrever uma nova relação de mandato.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/commercial-legal/skills/honorarios-contract
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# /honorarios-contract

1. Load `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` → firm position on fee arrangements, escalation chain.
2. Run the workflow below.
3. Determinar a hipótese legal de honorários (sucumbência, êxito, pró-labore, tabela, porcentagem, combinada).
4. Checar limites éticos: quota litis é **permitida, porém restrita** (CED-OAB art. 50 `[verified: https://www.oab.org.br/arquivos/pdf/legislacaoOab/codigodeetica.pdf]`) — em regra apenas por escrito, honorários não podem ser superiores às vantagens do cliente, e são vedados o aviltamento e a assunção de despesas pelo advogado como condição. Não é "proibida na maioria dos casos"; é excepcional e regulada.
5. Draftar cláusulas: estrutura, reajuste, hipótese de revogação/suspensão, confidencialidade, resolução de conflitos.
6. Aplicar consequential-action gate antes de entregar rascunho.

---

# Contrato de Honorários Advocatícios

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/commercial-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/commercial-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

A fee agreement is where client expectations and lawyer obligations meet. It describes what the client will pay, when, and under what conditions. It's the most consequential contract a lawyer drafts — when it fails, both sides feel cheated. This skill structures the agreement around the legal constraints (estatuto da OAB, Código de Ética) and the firm's positions (from the practice profile).

## Premissa de jurisdição (Brasil)

Honorários advocatícios no Brasil são regidos pelo Estatuto da Ordem dos Advogados do Brasil (Lei 8.906/1994) — especialmente Art. 23, que confirma que honorários incluídos na condenação pertencem ao advogado. O Art. 20 do Estatuto trata da jornada do advogado empregado, não de forma/conteúdo obrigatório de contrato de honorários. O Código de Ética e Disciplina da OAB (Res. CFOAB n. 02/2015, com emendas) também disciplina honorários, incluindo tabela mínima seccional e quota litis. `[verified: https://www.planalto.gov.br/ccivil_03/leis/l8906.htm; https://www.oab.org.br/leisnormas/legislacao/resolucoes/02-2015]`. Tabela de honorários de cada seccional da OAB é um piso orientativo, não teto — advocate pode cobrar acima da tabela, mas abaixo é censurável. Sucumbência decorre de sentença (Art. 85 CPC) e é direito do advogado, não sujeito a acordo de renúncia antecipada.

O Art. 422 CC exige que contratantes guardem probidade e boa-fé na conclusão e execução do contrato; ele não menciona reajuste por inflação ou preservação do valor real da prestação. [verified: https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm]

---

## Load the playbook

Read `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` first. Check `## Playbook` for o lado relevante (se a relação é com cliente recorrente / eventual / empresa / pessoa física):

- **Posição do escritório sobre honorários:** tabela OAB, porcentagem acima da tabela, êxito, combinada, quota litis (se aplicável).
- **Limites aceitáveis:** qual o mínimo de reajuste anual, como tratar atrasos/inadimplemento.
- **Escalação:** se o cliente rejeita a estrutura padrão, como escalar (ao sócio, ao GC, ao cliente direto).

Se o CLAUDE.md não tiver posição sobre fee structure, pergunte:

> Qual é a posição do escritório sobre estrutura de honorários? (Tabela OAB como referência? Acréscimo padrão? Êxito em litigação? Quota litis em que circunstâncias — se alguma?) Vou registrar a resposta no seu playbook.

---

## Step 0: Qual é a hipótese de honorários?

Antes de draftar, identifique qual(is) das hipóteses legais se aplicam:

1. **Sucumbência.** O advogado tem direito a honorários de sucumbência fixados em sentença; o CPC Art. 85, §2º fixa honorários entre 10% e 20%, e o Estatuto OAB Art. 23 confirma direito autônomo do advogado aos honorários de sucumbência. O Estatuto OAB Art. 24, §3º confirma nulidade de disposição que retire esse direito; a faixa de 10% a 20% não vem da Lei 13.327/2016. Se a relação inclui litigação, o contrato de honorários deve EXPLICITAR que sucumbência é adicional aos honorários contratuais. Se o cliente disser "quero contrato fechado, não quero pagar sucumbência além," PARE e flagge: essa cláusula é potencialmente nula sob Estatuto OAB. Escalate conforme necessário. [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm; https://www.planalto.gov.br/ccivil_03/leis/l8906.htm]

2. **Honorários contratuais puros** (pró-labore, tabela OAB, porcentagem fixa). Cliente paga advogado pela prestação de serviços, período definido (hora, tarifa, mês), independente do resultado. Estrutura mais comum em consultoria, contencioso de valor baixo, revisional.

3. **Honorários por êxito.** O advogado cobra uma porcentagem do valor obtido (litígio vencido, negociação bem-sucedida, transação). Hipótese legítima quando há risco compartilhado — cliente paga menos se perde, advogado recebe contingency. Deve ser EXPLÍCITO no contrato o que constitui "êxito" (vencer a demanda? Obter um acordo? Que valor mínimo?). Combinada com pró-labore é comum — tabela + porcentagem do resultado.

4. **Quota litis.** O advogado recebe uma COTA (fração) do valor obtido, SEM cobrar adiantado ou honorários contratuais. Extremamente restrito: sob o Código de Ética OAB vigente, quota litis deve ser representada por pecúnia e, somada aos honorários de sucumbência, não pode superar as vantagens advindas em favor do cliente (Art. 50 CED OAB). A participação em bens particulares do cliente só é admitida em caráter excepcional, quando o cliente comprovadamente não tiver condições pecuniárias e a forma for ajustada em instrumento contratual. [verified: https://www.oab.org.br/publicacoes/AbrirPDF?LivroId=0000004085]. **SE o cliente menciona quota litis, PARE, flagge como consequential-action, e escalate.**

---

## Step 1: Intake — que tipo de trabalho é?

Antes de draftar, converse com o cliente / responsável pela relação sobre:

### Qual é a natureza do mandato?

- Uma ação específica (litígio em curso, negociação de contrato, consultoria tributária)?
- Um mandato recorrente (consultoria jurídica contínua, defesa de demandas rotineiras)?
- Consultoria pontual (parecer, análise, auditoria jurídica)?

### Qual é a estrutura proposta?

- **Honorários fixos mensais (pró-labore)?** Valor e período?
- **Tabela OAB?** Qual seccional, qual faixa de valor da causa (se litigação)?
- **Porcentagem do resultado?** De qual tipo de valor (condenação, acordo negociado, economia auferida)?
- **Êxito + pró-labore combinados?** Qual a proporção?
- **Quota litis?** (flagge imediatamente)

### Sucumbência — como fica?

- Se há litigação: sucumbência é ADICIONAL aos honorários contratuais, ou o cliente quer cobrir sucumbência com os honorários contratuais?
- Se adicional: contrato precisa explicitar que sucumbência vence ao cliente e é repassada ao advogado como direito próprio (não é "renda extra" — é obrigação legal do vencido).

### Reajuste — como atualizar valores?

- Anual? Semestral?
- Índice (IPCA, tabela OAB, índice setorial)?
- Percentual fixo anual?

### Quando acaba o contrato?

- Prazo determinado (1 ano, 2 anos, até fim da causa)?
- Indeterminado com direito de revogação (por qual lado, com qual aviso prévio)?
- Suspensão se o cliente não paga (quanto tempo antes do vencimento)?

---

## Step 2: Verificar conformidade ética — tabela OAB como piso

Pesquise a tabela de honorários da seccional OAB relevante (ex.: OAB/SP, OAB/RJ, OAB/MG). O Código de Ética exige observar o valor mínimo da Tabela de Honorários do Conselho Seccional onde for realizado o serviço, sob pena de caracterizar aviltamento de honorários. [verified: https://www.oab.org.br/publicacoes/AbrirPDF?LivroId=0000004085] A tabela é UM PISO, não um teto — advogado pode cobrar acima. Cobrar abaixo é falta ética — é "dumping" de honorários, prejudicial à profissão.

Se a estrutura proposta cai abaixo da tabela, sinalize: "A tabela OAB seccional para [tipo de trabalho] é [valor/faixa]. A estrutura proposta ([valor proposto]) cai abaixo da tabela. Isso pode ser censurável sob Código de Ética. Confirmar se há motivo especial (pro bono, cliente de longa data, caso piloto) — ou aumentar os honorários até o piso."

---

## Step 3: Quota litis — bloqueio total

Se o cliente ou a relação mencionar quota litis:

1. **PARE a redação do contrato.**
2. **Flagge como consequential-action — requer aprovação de advogado.**
3. **Pesquise** Art. 50 do Código de Ética OAB para confirmar se há hipótese aplicável e os limites da quota litis. [verified: https://www.oab.org.br/publicacoes/AbrirPDF?LivroId=0000004085]
4. **Se a hipótese se aplica:** redações alternativas de quota litis (fração máxima permitida, carve-outs de custas/perícias/sucumbência).
5. **Se não se aplica:** decline and offer alternative (pró-labore + êxito combinados, ou sucumbência adicional sem pré-pagamento).

---

## Step 4: Draftar o contrato

Use a estrutura abaixo como template. Adapte cada seção ao tipo de mandato:

### Template do Contrato de Honorários Advocatícios

```markdown
# CONTRATO DE HONORÁRIOS ADVOCATÍCIOS

**PARTES:**
- **CLIENTE:** [nome, qualificação legal]
- **ADVOGADO(A) / ESCRITÓRIO:** [nome, inscrição OAB, endereço]

**DATA:** [data]

---

## 1. OBJETO

O ADVOGADO(A) se obriga a prestar serviços jurídicos relativos a [descrição concisa: litígio em [tribunal/classe], negociação de [assunto], consultoria sobre [tema], etc.].

---

## 2. HONORÁRIOS ADVOCATÍCIOS

### 2.1 Estrutura

[ESCOLHA UM OU COMBINE:]

**(a) Pró-labore mensal:**
O CLIENTE pagará ao ADVOGADO(A) R$ [valor] mensais, a título de honorários pelo trabalho contínuo. Vencimento: último dia útil de cada mês. Fatura: emitida pelo ADVOGADO(A) conforme Lei 12.725/2012 (RPA — Recibo de Profissional Autônomo).

**(b) Tabela OAB:**
Os honorários seguem a Tabela de Honorários da OAB — Seccional [UF], versão [ano], na faixa de [valor da causa ou descrição da complexidade]. Reajustes conforme a tabela.

**(c) Êxito / Contingência:**
- **Êxito:** Além dos honorários contratuais (se houver pró-labore), o ADVOGADO(A) receberá [X]% do valor obtido para o CLIENTE, entendido como [definição: condenação, acordo, economia contratual, etc.].
- **Cálculo:** sobre o valor líquido, após deduções de custas e despesas processuais quitadas pelo CLIENTE.
- **Hipótese de êxito:** [Ex: "vitória total na ação", "acordo de [valor mínimo]", "transação em termos favoráveis".] — deve ser EXPLÍCITO.

**(d) Combinada (Pró-labore + Êxito):**
O CLIENTE paga R$ [valor] mensais (pró-labore). Adicionalmente, se houver êxito (conforme 2.1(c)), ADVOGADO(A) recebe [X]% do valor obtido. Ambos os honorários são independentes — pró-labore vence mensalmente; êxito vence na realização do resultado.

---

### 2.2 Sucumbência

[OBRIGATÓRIO SE HÁ LITIGAÇÃO:]

A sucumbência (honorários fixados em sentença, conforme Art. 85 CPC e Lei 13.327/2016) é um DIREITO do ADVOGADO(A) e será recebido(a) como forma de remunerar seu trabalho. **Sucumbência é ADICIONAL aos honorários contratuais acima** (pró-labore, êxito, tabela). O CLIENTE reconhece que:
- (i) Sucumbência é obrigação legal da parte vencida, não concessão voluntária;
- (ii) Sucumbência típica é fixada em patamar de 10–20% da condenação;
- (iii) Sucumbência revertida em benefício do ADVOGADO(A) não compensa honorários contratuais — são fluxos distintos.

[SE SUCUMBÊNCIA FOI NEGOCIADA COMO "FECHADA":]
O CLIENTE e o ADVOGADO(A) acordam que sucumbência, quando obtida, será [OPÇÕES: (a) integralmente apropriada pelo ADVOGADO(A) como compensação adicional; (b) dividida conforme [proporção — ex: 50/50]; (c) revertida ao CLIENTE como redução futura de honorários contratuais. Especificar claramente.]

---

### 2.3 Reajuste

Os honorários serão reajustados [ESCOLHA UM]:
- (a) **Anualmente**, no mês de [mês], pela variação do IPCA (Índice de Preços ao Consumidor Amplo), conforme publicado pelo IBGE;
- (b) **Anualmente**, em [percentual fixo: ex. 10%] a.a.;
- (c) **Conforme a Tabela OAB**, quando aplicável, acompanhando as revisões publicadas pela Seccional.

Reajustes não serão retroativos — vigoram a partir do mês seguinte ao da aplicação.

---

### 2.4 Formas e Prazos de Pagamento

- **Faturamento:** RPA (Recibo de Profissional Autônomo) emitido conforme calendário acima.
- **Prazo:** 15 dias corridos após emissão, salvo acordo diverso.
- **Local:** transferência bancária para conta informada pelo ADVOGADO(A), ou cheque nominal.

---

### 2.5 Adiantamentos e Depósitos

[SE APLICÁVEL:]
O CLIENTE depositará R$ [valor] em conta de custódia do escritório, a titulo de antecipação de honorários. Esse depósito será descontado dos honorários contratuais à medida que vencerem. Saldo remanescente será restituído [ao término do mandato / se nenhum serviço for prestado / conforme solicitação]. Juros NÃO incidem sobre o depósito durante sua custódia (Art. 183 CC).

---

## 3. DESPESAS E ADIANTAMENTOS

O CLIENTE reembolsará o ADVOGADO(A) pelas seguintes **despesas necessárias** incorridas no curso do mandato:
- Custas processuais, emolumentos, taxas judiciárias;
- Perícias, pareceres de especialista, traduções certificadas;
- Deslocamentos e hospedagem (conforme comprovação);
- Fotocópias, digitalizações, envios (correios, courier).

**Adiantamentos:** O CLIENTE poderá ser solicitado(a) a adiantar despesas previstas, conforme comunicação prévia do ADVOGADO(A). Despesas não reembolsadas serão cobradas junto aos honorários ou após término do mandato.

Despesas ordinárias internas (e-mail, telefone, escritório) são cobertas pelos honorários — não são cobradas separadamente.

---

## 4. CONFIDENCIALIDADE E SIGILO PROFISSIONAL

O ADVOGADO(A) é obrigado(a) pelo **sigilo profissional** (Art. 7º, XIX Estatuto OAB), que protege:
- Comunicações do CLIENTE com o ADVOGADO(A);
- Estratégia processual, pareceres jurídicos, análises internas;
- Fatos e informações revelados sob a relação de confiança.

Sigilo é inviolável, mesmo após término do contrato. Exceções legais (ordem judicial de supervisão pública, investigação de crime, supervisão regulatória) estão sujeitas a regulação profissional — o ADVOGADO(A) informará o CLIENTE antes de cumprir, se legalmente possível.

---

## 5. REVOGAÇÃO E SUSPENSÃO DO MANDATO

### 5.1 Revogação pelo Cliente

O CLIENTE poderá revogar o mandato a qualquer tempo, com [X] dias de aviso prévio [RECOMENDADO: 30 dias], mediante comunicação escrita. Após revogação:
- ADVOGADO(A) será remunerado(a) pelos serviços prestados até a data de revogação (pró-rata se em período de faturação);
- Sucumbência obtida APÓS revogação pertence ao CLIENTE — ADVOGADO(A) pode cobrar honorários sobre essa sucumbência por termo posterior, se acordado;
- ADVOGADO(A) deverá transferir autos, documentos, correspondência ao CLIENTE ou novo ADVOGADO(A) em [X] dias úteis.

### 5.2 Suspensão/Rescisão por Falta de Pagamento

Se o CLIENTE não pagar honorários ou reembolsos vencidos por [X] dias [RECOMENDADO: 30–60 dias], o ADVOGADO(A) poderá [ESCOLHA]:
- (a) Suspender os serviços, sem prejuízo do direito de cobrar judicialmente;
- (b) Rescindir o mandato com [X] dias de aviso ao CLIENTE;
- Ambos os casos acima.

O CLIENTE continuará responsável pelo pagamento dos honorários e despesas incorridas até a suspensão/rescisão, acrescidos de multa moratória de [percentual — ex: 2% a.m.] e juros legais (Art. 406 CC).

### 5.3 Desistência pela Advogado(a)

O ADVOGADO(A) poderá desistir do mandato se:
- Há conflito de interesse superveniente (Art. 15 Código de Ética OAB);
- O CLIENTE conduta para conduta desonesta ou ilícita;
- Há indisciplina reiterada (ordens contrarias a dever profissional, não comparecimento a audiência sem justificativa);
- O CLIENTE está em mora grave de pagamento (acima de 90 dias).

Desistência será comunicada com [X] dias de aviso. ADVOGADO(A) será remunerado(a) até a data de desistência e transferirá documentos conforme 5.2 acima.

---

## 6. INTELECTUALIDADE DA CAUSA

O ADVOGADO(A) não responde por resultado (sucesso ou insucesso da demanda), salvo negligência grosseira ou desvio flagrante do dever profissional. Expectativas de resultado foram discutidas e o CLIENTE reconhece que:
- (i) Resultado de litígios é incerto — nem toda tese vencedora convence;
- (ii) Custos processuais, recursos e prazos podem variar além da previsão;
- (iii) Mudanças legislativas ou jurisprudenciais durante o mandato podem afetar a estratégia.

---

## 7. LEI APLICÁVEL E RESOLUÇÃO DE CONFLITOS

Este contrato é regido pela **Lei brasileira** (Código Civil, Arts. 421–480, especialmente; Estatuto OAB, Lei 8.906/1994; Código de Ética OAB).

Conflitos serão resolvidos [ESCOLHA]:
- (a) **Arbitragem:** perante árbitro único, sob Regras [indicar câmara ou regras];
- (b) **Foro:** [Comarca — ex: Comarca de São Paulo], com exclusão de qualquer outro foro;
- (c) **Negociação + Mediação:** antes de qualquer medida judicial, partes tentarão resolver por negociação direta; se fracassada, recorrerão a mediador.

---

## 8. DISPOSIÇÕES GERAIS

8.1 **Publicidade e Ética:** O ADVOGADO(A) não publicará este contrato ou dados do CLIENTE sem consentimento, salvo conforme exigido por lei ou ordem regulatória.

8.2 **Integração:** Este contrato é a integralidade do acordo entre as partes. Alterações só valem se por escrito, assinado por ambas.

8.3 **Severabilidade:** Se qualquer cláusula for nula, as demais continuam em vigor.

8.4 **Validade:** Este contrato vigora [conforme datas ou evento — ex: "até 30/06/2026", "até término da causa", "por tempo indeterminado, renovável anualmente"].

---

**CLIENTE:** [assinatura, data]
[Nome, CPF/CNPJ, contato]

**ADVOGADO(A):** [assinatura, data]
[Nome, inscrição OAB, endereço, contato]

---

**TESTEMUNHAS** [SE DESEJADO]:

_________________________     _______________________
[Nome e assinatura]         [Nome e assinatura]
```

---

## Nota ética: captação indevida é vedada

Segundo Provimento CFOAB 205/2021 `[verified: https://eticaedisciplina.oab.org.br/assets/docs/Provimento%20n.%20205.2021%20-%20Publicidade.pdf]`, publicidade de serviços jurídicos é permitida (derrogando proibição histórica), mas **captação indevida** é proibida — marketing agressivo, coação, promessas de resultado garantido, ou honorários contingentes não-explícitos podem caracterizar falta ética. O contrato de honorários, se resultante de captação indevida, é eticamente comprometido.

**Consequential-action gate:** se há indício de que o cliente foi captado de forma agressiva ou coagido a assinar, flagge o contrato antes de entregar.

---

## What this skill does NOT do

- It does not guarantee the contract is enforceable — only a judge can do that. Have an attorney review before signing.
- It does not design a fee structure. It drafts clauses given a structure the user has decided.
- It does not advise whether quota litis is permissible in a specific case — that requires legal judgment and CFOAB/disciplinary research. Flag it for escalation.
- It does not handle referral arrangements between lawyers, partnership agreements, or fee-splitting disputes (those are separate law-firm governance documents).
- It does not generate tax or accounting advice — if the fee structure has tax consequences, refer the client to their accountant.

---

## Consequential-action gate

**Before delivering this draft to a client or signing:** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. If the Role is Non-lawyer:

> This is a legal contract that governs payment and the lawyer-client relationship. Have a licensed attorney review it before your client signs. Here's a brief for them:
>
> **Fee arrangement type:** [selected type — pró-labore / êxito / quota litis / combined]
> **Key risk:** [If quota litis: "Quota litis is heavily restricted — verify it complies with Código de Ética OAB Art. 50"; if contingency: "Define 'success' explicitly or dispute will arise"; if below-table: "Verify it meets OAB tabela piso"]
> **Negotiated terms:** [List any deviations from firm standard]
> **Next step:** Have the attorney confirm this complies with professional ethics and your firm's risk tolerance before the client signs.

Do not proceed past this gate without an explicit yes from an authorized attorney.

---

## Close with the next-steps decision tree

**What next? Pick one and I'll help you build it out:**

1. **Refine the terms** — You'd like to adjust [specific clause — e.g., reajuste mechanism, revogação window, êxito percentage]. I'll redline and explain the delta.
2. **Add context** — I'll generate a cover memo for your client explaining the contract's key terms in plain language.
3. **Escalate a risk** — One or more terms need attorney review before you proceed. I'll draft a brief escalation to [partner/GC].
4. **Template for future** — You'd like to convert this into a reusable template for [type of engagement]. I'll strip client-specific info and create a blank template.
5. **Something else** — Tell me what you'd do with this.

**One question I'd ask that isn't in the checklist:** Is this a one-time engagement or the first of a potentially long relationship? If long-term, the revogação and reajuste terms matter much more — they'll surface friction early. If one-time, consider whether a simpler, shorter contract reduces your risk.

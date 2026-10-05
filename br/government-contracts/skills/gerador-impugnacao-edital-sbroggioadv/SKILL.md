---
name: gerador-impugnacao-edital-sbroggioadv
title: Gerador de impugnação de edital (Lei 14.133 art. 164)
description: 'Gera a impugnação administrativa de edital de licitação com base na Lei 14.133/2021 art. 164 — qualquer pessoa é parte legítima, protocolando até 3 DIAS ÚTEIS ANTES da abertura do certame. Este é o ÚNICO instrumento do opositor com prazo fatal e pré-clusivo: a skill abre com um ALERTA pró-ativo de prazo — se o relógio já corre, avisa de imediato, antes de qualquer redação. NÃO é a Lei 8.666/93 (revogada, transição encerrada — TV5). A peça é um pedido de correção/esclarecimento do edital, e só depois de recusada é que se leva a irregularidade ao TCE. Mostra o aviso do CP 339 (P3) antes de emitir. Aciona: quando o vício está num edital ou aviso de licitação ainda aberto, ou o usuário pede "impugnar edital", "contestar licitação", "cláusula restritiva no edital" ou "pedir esclarecimento de edital".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/opositor-os-marketplace/tree/main/opositor-os/skills/gerador-impugnacao-edital
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: government-contracts
language: pt
---

# Gerador de impugnação de edital (Lei 14.133 art. 164)

## ⏰ ALERTA DE PRAZO — leia antes de tudo

A impugnação de edital tem **prazo FATAL e pré-clusivo**: **até 3 (três) dias úteis antes da
data de abertura do certame** (Lei 14.133/2021 art. 164). É o único instrumento deste
produto com prazo curto e irrecuperável — passou a abertura, essa via **fecha**.

**Primeira ação desta skill, antes de qualquer redação:** perguntar a **data de abertura do
certame** e contar os dias úteis. Se faltam poucos dias, ou se a abertura já passou, **avisar
imediatamente** — não deixar para a próxima rodada de análise. Se já não há prazo, a via
correta deixa de ser a impugnação e passa a ser a **representação ao TCE** pós-abertura
(`gerador-representacao`) — o produto diz isso na hora, não redige uma impugnação intempestiva.

## Quando esta skill entra

Quando o vício está em um **edital ou aviso de licitação ainda aberto** (cláusula restritiva
de competitividade, exigência desproporcional, direcionamento). Base: art. 164, *"Qualquer
pessoa é parte legítima para impugnar edital de licitação por irregularidade na aplicação
desta Lei ou para solicitar esclarecimento sobre os seus termos, devendo protocolar o pedido
até 3 (três) dias úteis antes da data de abertura do certame."* Legitimidade **universal**,
sem OAB.

## Não é a Lei 8.666 (TV5)

A base é a **Lei 14.133/2021**, art. 164 — **não** o art. 41 da Lei 8.666/93, **revogada** e
com transição encerrada. Citar a lei antiga é erro de defasagem. O prazo (3 dias úteis antes
da abertura) e o rito de resposta (o parágrafo único do art. 164 dá à Administração até 3
dias úteis para responder, limitado ao último dia útil anterior à abertura) são os do regime
vigente.

## Antes de gerar — o aviso obrigatório (P3)

Mesmo sendo a peça de menor carga acusatória (é dirigida ao **edital**, não a uma pessoa), a
skill só emite após o `aviso-cp339-art19-e-ce326a` e a confirmação de veracidade — a
impugnação pode conter alegação de direcionamento, que se afirmada como certa vira imputação.
Redigir como **pedido de correção/apuração** (P2).

## Estrutura da impugnação

1. **Endereçamento** — ao agente de contratação / pregoeiro / comissão, órgão promotor,
   identificando **nº do edital, objeto e data de abertura**.
2. **Qualificação do impugnante** — qualquer pessoa (art. 164). Não precisa ser licitante.
3. **Tempestividade** — afirma expressamente que o pedido é protocolado **dentro dos 3 dias
   úteis anteriores à abertura**, indicando a data-limite calculada. (É o item que a
   Administração checa primeiro.)
4. **Dos fatos e da irregularidade** — a cláusula impugnada, transcrita, e a norma que ela
   contraria (princípios de competitividade/isonomia da Lei 14.133; regra específica citada
   do `context/`). Cada afirmação com fonte (P5).
5. **Do pedido** — requer a **correção/supressão da cláusula** ou o **esclarecimento** dos
   termos e, se necessário, a **suspensão/reabertura de prazo**. Formulado como pedido, não
   como acusação de fraude.
6. **Fecho** — data, assinatura, documentos anexos (cópia do edital/aviso).

## Depois da resposta

- **Acolhida** → edital corrigido; objetivo cumprido.
- **Recusada ou ignorada** → aí sim a irregularidade sobe ao **TCE** como representação
  (`gerador-representacao`) — a via de controle externo é **posterior** à tentativa
  administrativa, não paralela. Contencioso pleno de licitação/TCU é escopo de
  `licitacoes-adv-os` (cross-link), não deste produto.

## Travas / limites

- **Prazo fatal de 3 dias úteis antes da abertura** — checar e alertar ANTES de redigir;
  vencido, redirecionar a representação ao TCE, não gerar impugnação intempestiva.
- **Lei 14.133 art. 164, nunca Lei 8.666** (TV5).
- **Sem lastro não gera** (P1): edital/aviso publicado + cláusula/norma, senão `[FALTA
  LASTRO]`.
- **Pedido de correção/apuração, nunca "direcionamento provado"** (P2).
- **Aviso CP 339 antes de emitir** (P3); fonte em toda alegação (P5).
- Só a **impugnação administrativa de leigo** (art. 164). Contencioso de licitação/TCU →
  `licitacoes-adv-os`. Cita só o `context/`; fora dele → `[VERIFICAR]`.

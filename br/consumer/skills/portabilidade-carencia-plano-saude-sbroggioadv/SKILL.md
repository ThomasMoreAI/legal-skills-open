---
name: portabilidade-carencia-plano-saude-sbroggioadv
title: Portabilidade de carências
description: 'Estrutura o pedido e a defesa de portabilidade de carências entre planos de saúde — requisitos da 1ª portabilidade e das posteriores, compatibilidade de faixa de preço, vedação de nova Declaração de Saúde/CPT no plano de destino, e as três hipóteses de portabilidade especial (extinção do vínculo empregatício, cancelamento/liquidação da operadora, descredenciamento de hospital com retirada de urgência/emergência). Aciona: portabilidade de carências, trocar de plano de saúde sem carência, portabilidade especial, portabilidade negada, mudar de operadora mantendo carência cumprida.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/portabilidade-carencia-plano-saude
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Portabilidade de carências

## Quando esta skill entra

Toda negativa ou dúvida sobre o exercício do direito de portabilidade de carências entre
planos de saúde — comum, especial ou por extinção de vínculo empregatício.

## Base normativa

**RN 438/2018** — vigente. Requisitos simultâneos (art. 3º):

- **1ª portabilidade**: mínimo de **2 anos** de permanência no plano de origem (**3 anos**,
  se o beneficiário cumpriu CPT).
- **Portabilidades posteriores**: mínimo de **1 ano** no plano de origem (**2 anos**, se a
  portabilidade anterior foi para plano com coberturas não previstas na segmentação do
  plano de origem).
- **Compatibilidade de faixa de preço** entre plano de origem e plano de destino.
- **Vínculo ativo** do beneficiário com o plano de origem (exceto nas hipóteses especiais
  abaixo).
- Deve ser exercida **individualmente**.
- **Vedada** nova Declaração de Saúde ou alegação de CPT no plano de destino.
- **Vedada** discriminação de preço em razão do uso da portabilidade.

## Portabilidade especial — três hipóteses que dispensam requisitos

| Hipótese | Prazo | O que é dispensado |
|---|---|---|
| **Extinção do vínculo empregatício** (ex.: demissão) | **60 dias** a contar da ciência da extinção | Vínculo ativo, permanência, faixa de preço |
| **Cancelamento de registro ou liquidação extrajudicial** da operadora | Até **60 dias** (prorrogáveis, por Resolução Operacional da ANS) | Permanência, faixa de preço — alcança inclusive beneficiários de planos antigos (pré-1999) não adaptados |
| **Descredenciamento de hospital com retirada do serviço de urgência/emergência** no município do beneficiário | **180 dias** a contar do descredenciamento | Permanência, faixa de preço |

## Tese do consumidor × tese da operadora

**Consumidor**: comprova o tempo de permanência (recibos/carteirinha), a compatibilidade de
faixa de preço (tabela de preços do plano de destino) e, se for o caso, o enquadramento em
uma das três hipóteses especiais (aviso de demissão, comunicado de liquidação, notícia de
descredenciamento); exige que o plano de destino não exija nova Declaração de Saúde nem
CPT.

**Operadora** (do plano de destino, que nega a portabilidade): alega descumprimento de um
dos requisitos — normalmente incompatibilidade de faixa de preço ou permanência insuficiente
no plano de origem; a defesa do consumidor precisa demonstrar, documento a documento, que
todos os requisitos simultâneos do art. 3º da RN 438/2018 estão cumpridos.

## Armadilhas

- Não confundir os prazos de permanência da **1ª** portabilidade (2 ou 3 anos) com os das
  **posteriores** (1 ou 2 anos) — é o erro mais comum na conferência de requisitos.
- Nas hipóteses especiais, confirme sempre o prazo de exercício (60 ou 180 dias) contado do
  evento correto (ciência da extinção do vínculo, comunicado da liquidação, ou
  descredenciamento) — perder o prazo dispensa apenas os requisitos, não o próprio prazo.

## Fronteira

Reajuste do plano de origem ou de destino: `revisao-reajuste-plano-saude`. Negativa de
cobertura já no plano de destino: `negativa-cobertura-saude-suplementar`. Rescisão do plano
de origem que motivou a portabilidade: `rescisao-cancelamento-plano-saude`.

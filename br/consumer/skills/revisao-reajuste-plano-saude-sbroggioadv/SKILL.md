---
name: revisao-reajuste-plano-saude-sbroggioadv
title: Revisão de reajuste de plano de saúde
description: 'Estrutura a revisão de reajuste de mensalidade de plano de saúde — individual/familiar (teto anual da ANS), coletivo com 30+ beneficiários (livre negociação, limite de sinistralidade/razoabilidade) e coletivo com menos de 30 (CDC aplicável), além do reajuste por faixa etária (Lei 9.656 art. 15, Estatuto do Idoso, Tema 952/STJ). Slug distinto do acao-reajuste-abusivo do direito-medico-adv-os — cross-link explícito. Aciona: reajuste abusivo, mensalidade do plano aumentou, revisão de reajuste, reajuste por faixa etária, reajuste coletivo, sinistralidade.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/revisao-reajuste-plano-saude
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Revisão de reajuste de plano de saúde

## Quando esta skill entra

Toda discussão sobre percentual de reajuste de mensalidade de plano de saúde — anual por
sinistralidade, ou por mudança de faixa etária — nos três regimes contratuais e no recorte
etário, pela ótica contrato/CDC/ANS.

## Base normativa e o teste por regime

| Regime | Regra | Selo |
|---|---|---|
| Individual/familiar | Teto anual **fixado pela ANS por ciclo de aniversário** — confira o percentual vigente na data do caso em `gov.br/ans`, nunca hardcode um número | Fonte oficial ANS |
| Coletivo 30+ beneficiários | **Livre negociação** entre a pessoa jurídica contratante e a operadora — a ANS **não fixa teto**; exige-se base atuarial idônea de sinistralidade | ANS, jurisprudência |
| Coletivo com **menos de 30** beneficiários | Aplica-se o **CDC** (natureza híbrida/vulnerabilidade do grupo pequeno já reconhecida pelo STJ); exige comprovação de base atuarial idônea | Jurisprudência consolidada |

## Faixa etária

- **Lei 9.656/1998, art. 15**: variação por idade só é válida se prevista no contrato
  inicial (faixas + percentuais). **Parágrafo único**: vedada a variação para
  consumidores com **mais de 60 anos** que participem do plano **há mais de 10 anos**
  — dois requisitos cumulativos.
- **Estatuto do Idoso (Lei 10.741/2003), art. 15, § 3º**: veda a **discriminação da pessoa
  idosa** nos planos de saúde pela cobrança de valores diferenciados em razão da idade —
  redação mais ampla, sem o requisito de permanência de 10 anos.
- 🟡 **Divergência real — sinalize sempre as duas normas, nunca escolha uma escondendo a
  outra.** A jurisprudência não elimina a tensão textual entre a Lei 9.656 (dois requisitos
  cumulativos) e o Estatuto do Idoso (vedação mais ampla) — resolve caso a caso pela via da
  razoabilidade.
- **Tema 952/STJ (tese firmada)**: "O reajuste de mensalidade de plano de saúde individual
  ou familiar fundado na mudança de faixa etária do beneficiário é válido desde que (i) haja
  previsão contratual, (ii) sejam observadas as normas expedidas pelos órgãos governamentais
  reguladores e (iii) não sejam aplicados percentuais desarrazoados ou aleatórios que,
  concretamente e sem base atuarial idônea, onerem excessivamente o consumidor ou
  discriminem o idoso." A Segunda Seção do STJ estendeu o Tema 952 aos coletivos,
  "ressalvando-se, quanto às entidades de autogestão, a inaplicabilidade do CDC" — ou seja,
  mesmo em autogestão o teste de razoabilidade vale, só que pela via da própria Lei
  9.656/normas ANS, não pelo CDC (Súmula 608).

## Tese do consumidor × tese da operadora

**Consumidor**: pede a exibição da nota técnica atuarial que embasou o percentual (CDC art.
6º, VIII); ataca reajuste desarrazoado ou aleatório sem base atuarial idônea (Tema 952);
no coletivo pequeno, invoca a aplicação do CDC; na faixa etária, soma Lei 9.656 art. 15 +
Estatuto do Idoso quando o consumidor tiver mais de 60 anos e 10 anos de plano.

**Operadora**: no individual/familiar, ampara-se no teto ANS do ciclo; no coletivo,
sustenta a livre negociação e junta nota técnica de sinistralidade; na faixa etária,
sustenta previsão contratual + observância das normas ANS (os dois primeiros requisitos do
Tema 952) para afastar a alegação de percentual desarrazoado.

## Armadilhas

- **T5** — não hardcodar o percentual do teto ANS do ciclo individual/familiar nem o número
  da RN de limites por faixa etária como se fossem estáticos; confirme na data do caso.
- A tensão Lei 9.656 × Estatuto do Idoso (acima) — declare sempre as duas, nunca omita uma
  para "ganhar" o argumento.

## Fronteira

O `direito-medico-adv-os` tem a skill `acao-reajuste-abusivo`, cobrindo majoritariamente a
mesma matéria contratual/CDC (Tema 952, Súmula 608, Estatuto do Idoso, sinistralidade). É o
ponto de maior sobreposição da família — esta skill (`revisao-reajuste-plano-saude`) é a
via padrão do `consumidor-adv-os` para reajuste; não crie nem cite um slug
`acao-reajuste-abusivo` aqui. Rescisão/carência/portabilidade do mesmo contrato: skills
próprias deste plugin.

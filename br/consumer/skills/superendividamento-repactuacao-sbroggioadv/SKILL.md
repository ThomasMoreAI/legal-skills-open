---
name: superendividamento-repactuacao-sbroggioadv
title: Superendividamento e repactuação de dívidas
description: 'Trata prevenção e tratamento do superendividamento do consumidor pessoa natural sob a Lei 14.181/2021 — deveres de informação e avaliação responsável na oferta de crédito (arts. 54-A a 54-G, CDC), preservação do mínimo existencial, e o processo de repactuação de dívidas com conciliação global e plano compulsório (arts. 104-A, 104-B e 104-C, CDC). Escopo restrito ao superendividamento de origem NÃO-bancária — a origem bancária é tratada pelo bancario-adv-os. Aciona: quando o usuário relata acúmulo de dívidas de consumo que compromete o mínimo existencial, ou precisa entender deveres do fornecedor de crédito/venda a prazo.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/superendividamento-repactuacao
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Superendividamento e repactuação de dívidas

## Quando esta skill entra

Consumidor pessoa natural, de boa-fé, sem condições de pagar a totalidade das dívidas de
consumo (exigíveis e vincendas) sem comprometer o mínimo existencial — quer repactuar
judicial ou administrativamente, ou avaliar se o fornecedor de crédito/venda a prazo
cumpriu seus deveres de informação.

## Base normativa (Lei 14.181/2021, que alterou o CDC)

- **Art. 54-A** — conceito: § 1º define superendividamento como a impossibilidade
  manifesta de o consumidor pessoa natural, de boa-fé, pagar a totalidade das dívidas de
  consumo, exigíveis e vincendas, sem comprometer o mínimo existencial; § 2º abrange
  qualquer compromisso financeiro de consumo, inclusive crédito, compra a prazo e
  serviço de prestação continuada; **§ 3º exclui** do capítulo dívida contraída mediante
  **fraude ou má-fé**, oriunda de contrato celebrado **dolosamente** sem propósito de
  pagar, ou decorrente de produto/serviço de **luxo de alto valor**.
- **Art. 54-B** — deveres de informação prévia na oferta de crédito/venda a prazo: custo
  efetivo total e seus componentes; taxa efetiva mensal de juros e encargos de mora;
  montante das prestações e validade mínima da oferta de **2 dias**; identificação do
  fornecedor; direito à liquidação antecipada não onerosa.
- **Art. 54-C** — vedações na oferta de crédito: ocultar/dificultar compreensão de ônus
  e riscos; assediar ou pressionar o consumidor, especialmente idoso, analfabeto,
  doente ou vulnerável; condicionar atendimento à renúncia de demanda judicial ou a
  pagamento de honorários/depósitos.
- **Art. 54-D** — deveres pré-contratação: informar e esclarecer considerando a idade do
  consumidor; **avaliar responsavelmente** as condições de crédito via bancos de dados
  de proteção ao crédito; entregar cópia do contrato. **Parágrafo único**: o
  descumprimento desses deveres (e dos arts. 52 e 54-C) pode acarretar, judicialmente,
  **redução de juros/encargos/acréscimos e dilação do prazo de pagamento**, conforme a
  gravidade da conduta e a capacidade financeira do consumidor, sem prejuízo de
  indenização por perdas e danos.
- **Art. 54-G** — vedações adicionais: cobrar/debitar valor contestado em cartão de
  crédito antes de solucionada a controvérsia (com notificação do consumidor com 10 dias
  de antecedência do vencimento); recusar entrega de minuta/cópia do contrato; dificultar
  bloqueio ou anulação de pagamento em caso de fraude no cartão.
- **Art. 104-A** — a requerimento do consumidor, o juiz instaura processo de
  repactuação de dívidas, com audiência conciliatória global com **todos os credores**
  das dívidas do art. 54-A; o consumidor propõe plano de pagamento em até **5 anos**,
  preservados o mínimo existencial e as garantias originalmente pactuadas. **§ 1º
  exclui** do processo dívidas de contrato doloso sem propósito de pagar, com garantia
  real, financiamento imobiliário e crédito rural. **§ 2º**: ausência injustificada de
  credor (ou procurador com poderes plenos) suspende a exigibilidade do débito, interrompe
  a mora e sujeita esse credor compulsoriamente ao plano, com pagamento após os credores
  presentes. **§ 3º**: sentença homologatória vale título executivo e faz coisa julgada.
  **§ 5º**: o pedido não é declaração de insolvência civil e só pode ser repetido após
  **2 anos** da liquidação do plano homologado.
- **Art. 104-B** — sem êxito na conciliação com algum credor, o juiz instaura, a pedido
  do consumidor, processo de revisão/integração dos contratos e repactuação compulsória
  das dívidas remanescentes, com citação de todos os credores não conciliados;
  **§ 4º** assegura ao credor, no mínimo, o valor do principal corrigido monetariamente,
  com liquidação total em até 5 anos após o plano consensual, primeira parcela devida
  em até 180 dias da homologação.
- **Art. 104-C** — compete concorrente e facultativamente aos órgãos do Sistema
  Nacional de Defesa do Consumidor conduzir a fase conciliatória e preventiva.

## O teste

1. Confirmar os requisitos do art. 54-A: pessoa natural, boa-fé, dívidas de consumo
   exigíveis e vincendas, comprometimento do mínimo existencial.
2. Checar a exclusão do § 3º (fraude, dolo de não pagar, produto de luxo de alto
   valor) — se presente, o Capítulo VI-A não se aplica a essa dívida específica.
3. Mapear se o fornecedor de crédito descumpriu deveres de informação (54-B) ou
   incorreu em vedação (54-C/54-G) — abre pedido autônomo de redução judicial de
   encargos e dilação de prazo (54-D, parágrafo único), independente da via conciliatória.
4. Via judicial: requerer a instauração do processo do art. 104-A, identificar e citar
   todos os credores das dívidas de consumo, apresentar plano de pagamento em até 5
   anos preservando o mínimo existencial.
5. Sem êxito na conciliação: art. 104-B, plano judicial compulsório.

## Tese do consumidor

O direito à repactuação preservando o mínimo existencial é direito básico (art. 6º,
XI e XII, incluídos pela Lei 14.181/2021). O descumprimento dos deveres de informação e
avaliação responsável do fornecedor de crédito (54-B a 54-D) autoriza redução judicial
de juros e encargos, à parte do processo de repactuação. A ausência injustificada de
um credor na audiência conciliatória o sujeita compulsoriamente ao plano proposto.

## Tese do fornecedor

Cumpriu integralmente os deveres de informação prévia (54-B) e de avaliação responsável
do crédito (54-D, II). A dívida em discussão se enquadra na exclusão do § 3º do art.
54-A (fraude, má-fé, contrato doloso ou produto de luxo de alto valor) e está fora do
alcance do Capítulo VI-A. Em plano compulsório, tem direito assegurado, no mínimo, ao
principal corrigido monetariamente (art. 104-B, § 4º).

## Armadilhas

**Escopo desta skill é o superendividamento de origem NÃO-bancária.** Quando a causa
principal do endividamento é operação bancária/financeira — empréstimo consignado,
cartão de crédito de banco, cheque especial, financiamento — o tratamento primário é do
`bancario-adv-os`; esta skill cobre o consumidor de varejo/serviços continuados em geral
e serve como camada geral do CDC. Não duplicar conteúdo bancário, apenas apontar
(cross-link). A exclusão do § 3º do art. 54-A é **estrita** — fraude, dolo de não
pagar ou produto de luxo de alto valor — não abrange qualquer dívida simplesmente "mal
administrada" pelo consumidor; aplicá-la de forma ampla nega o direito ao consumidor
que a lei quis proteger.

## Fronteira

Superendividamento de origem bancária (consignado, cartão de banco, cheque especial,
revisional, busca e apreensão): `bancario-adv-os`. Execução da dívida remanescente:
`execucao-adv-os`. Liquidação e cálculo do plano de pagamento: `calculosjudiciais-adv-os`.

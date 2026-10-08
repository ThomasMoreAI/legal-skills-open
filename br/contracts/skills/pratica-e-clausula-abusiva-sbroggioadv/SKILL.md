---
name: pratica-e-clausula-abusiva-sbroggioadv
title: Prática e cláusula abusiva
description: 'Identifica e trata práticas comerciais abusivas (art. 39, CDC) e cláusulas contratuais abusivas (art. 51, CDC), incluindo venda casada, envio de produto sem solicitação, elevação de preço sem justa causa, exigência de vantagem manifestamente excessiva, cláusula limitativa de responsabilidade, cláusula de foro/arbitragem compulsória e multa de mora acima do teto legal. Aplica o teste de presunção de exagero (art. 51, §1º) e articula a revisão contratual por onerosidade excessiva (art. 6º, V). Aciona: quando o usuário relata prática comercial ou cláusula de contrato de consumo que parece desequilibrada, imposta ou vantajosa demais para o fornecedor.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/pratica-e-clausula-abusiva
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# Prática e cláusula abusiva

## Quando esta skill entra

Contrato ou conduta comercial em que o fornecedor impõe condição, cobra além do
combinado, condiciona a venda a outra compra, ou insere no contrato cláusula que retira
direito do consumidor sem contrapartida. Entra tanto do lado de quem sofreu a prática
quanto do fornecedor que precisa avaliar se sua cláusula/conduta resiste a controle.

## Base normativa

- **Art. 39, CDC** (práticas abusivas — rol exemplificativo, "dentre outras"): I (venda
  casada / limite quantitativo sem justa causa), III (enviar produto/serviço sem
  solicitação prévia — equipara-se a amostra grátis, parágrafo único), IV (prevalecer-se
  de fraqueza/ignorância do consumidor), V (exigir vantagem manifestamente excessiva),
  VI (executar serviço sem orçamento prévio e autorização expressa), IX (recusar venda a
  pronto pagamento), X (elevar preço sem justa causa), XII (não fixar prazo de
  cumprimento ou deixá-lo a critério exclusivo do fornecedor), XIII (aplicar índice de
  reajuste diverso do legal/contratual).
- **Art. 51, CDC** (cláusulas nulas de pleno direito — rol também exemplificativo):
  incisos I a XVI (responsabilidade, ônus da prova invertido contra o consumidor,
  arbitragem compulsória, variação unilateral de preço, cancelamento unilateral só a
  favor do fornecedor, modificação unilateral do contrato). **Incisos XVII e XVIII
  incluídos pela Lei 14.181/2021**: XVII veda cláusula que condicione ou limite acesso ao
  Judiciário; XVIII veda carência por impontualidade ou cláusula que impeça o
  restabelecimento integral dos direitos do consumidor após purgação da mora ou acordo.
- **Art. 51, § 1º** — presunção de vantagem exagerada: ofende princípio fundamental do
  sistema jurídico; restringe direito fundamental do contrato a ponto de ameaçar seu
  objeto/equilíbrio; ou é excessivamente onerosa considerando a natureza do contrato.
- **Art. 51, § 2º** — nulidade da cláusula não invalida o contrato inteiro, salvo se o
  vácuo gerar ônus excessivo a qualquer parte, mesmo com esforço de integração.
- **Art. 6º, V** — direito à modificação de cláusula desproporcional ou à revisão por
  fato superveniente que torne a prestação excessivamente onerosa.
- **Art. 52, § 1º** — multa de mora limitada a **2% do valor da prestação**.

## O teste

1. Separar **prática** (conduta do fornecedor no mercado, art. 39) de **cláusula**
   (texto do contrato, art. 51) — o enquadramento muda o fundamento a citar.
2. Prática: verificar se cabe em um dos incisos do art. 39; o rol é exemplificativo, mas
   o inciso citado deve corresponder ao fato narrado.
3. Cláusula: verificar se cabe em um dos incisos do art. 51; se não couber literalmente,
   aplicar o teste do § 1º (ofende princípio / restringe direito fundamental /
   excessivamente onerosa).
4. A nulidade de cláusula abusiva é **de pleno direito** — pode ser reconhecida
   incidentalmente, não exige ação constitutiva específica.
5. Checar se o vácuo deixado pela cláusula nula inviabiliza o contrato (§ 2º); em regra,
   não inviabiliza — o contrato segue sem a cláusula nula.
6. Se a discussão é de reequilíbrio (não de nulidade), fundamentar em art. 6º, V.

## Tese do consumidor

Cláusula é nula de pleno direito, independentemente de pedido expresso de nulidade — o
juiz pode reconhecer de ofício. Valores cobrados com base em cláusula abusiva (reajuste
por índice diverso, multa acima de 2%) devem ser restituídos — articular com a skill de
repetição em dobro quando cabível. Onerosidade excessiva superveniente autoriza revisão
mesmo sem cláusula nula (art. 6º, V).

## Tese do fornecedor

O contrato foi objeto de negociação paritária (não de adesão), o que reduz — sem
eliminar — a proteção do art. 51. A cláusula reflete distribuição de risco típica do
setor, não "vantagem manifestamente excessiva". O encargo praticado está dentro do teto
legal (2% de mora) ou decorre de índice contratualmente pactuado e válido. Ausência de
prova de que a cláusula causou desequilíbrio concreto no caso.

## Armadilhas

Os róis dos arts. 39 e 51 são **exemplificativos** ("dentre outras práticas abusivas" /
"entre outras, as cláusulas") — nunca alegar que a lista é taxativa, seja para incluir
seja para excluir uma conduta não listada. Os incisos XVII e XVIII do art. 51 só
existem desde a **Lei 14.181/2021** — não citá-los para fundamentar nulidade de cláusula
como se fossem texto originário de 1990 (a cláusula pode ser nula por outro fundamento
mesmo antes de 2021, mas não por XVII/XVIII).

## Fronteira

Revisão de juros, capitalização e tarifas bancárias: `bancario-adv-os`. Cláusula em
contrato imobiliário (compra e venda, incorporação): `direito-imobiliario-adv-os`.
Execução de multa/cláusula penal já reconhecida: `execucao-adv-os`. Liquidação de valor
a restituir: `calculosjudiciais-adv-os`.

---
name: publicidade-enganosa-e-abusiva-sbroggioadv
title: Publicidade enganosa e abusiva
description: 'Trata publicidade enganosa e abusiva (arts. 30, 35, 36, 37 e 38, CDC) — princípio da vinculação da oferta, distinção entre publicidade enganosa (falsidade ou omissão de dado essencial) e abusiva (discriminação, exploração de medo, superstição ou vulnerabilidade infantil), inversão do ônus da prova de veracidade contra quem patrocina o anúncio, e a sanção administrativa de contrapropaganda. Aciona: quando o usuário relata anúncio ou oferta falsa, incompleta, discriminatória, ou fornecedor que se recusa a cumprir o que publicou.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/publicidade-enganosa-e-abusiva
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Publicidade enganosa e abusiva

## Quando esta skill entra

Anúncio, oferta ou informação publicitária que induz o consumidor a erro, omite dado
relevante, explora medo/superstição/vulnerabilidade, ou quando o fornecedor recusa
cumprir o que apresentou ao público.

## Base normativa

- **Art. 30, CDC** — toda informação ou publicidade suficientemente precisa, veiculada
  por qualquer meio, obriga o fornecedor que a veicular ou dela se utilizar e **integra
  o contrato** que vier a ser celebrado (princípio da vinculação da oferta).
- **Art. 35, CDC** — se o fornecedor recusar cumprir a oferta/publicidade, o consumidor
  escolhe, alternativamente: (I) exigir cumprimento forçado nos termos da oferta;
  (II) aceitar produto ou serviço equivalente; (III) rescindir o contrato, com
  restituição do que foi pago e perdas e danos.
- **Art. 36, CDC** — a publicidade deve ser veiculada de forma que o consumidor,
  fácil e imediatamente, a identifique como tal; parágrafo único: o fornecedor mantém em
  seu poder os dados fáticos, técnicos e científicos que sustentam a mensagem.
- **Art. 37, CDC** — proíbe toda publicidade enganosa ou abusiva. § 1º define
  **enganosa**: informação/comunicação publicitária inteira ou parcialmente falsa, ou,
  por qualquer modo, **inclusive por omissão**, capaz de induzir o consumidor a erro
  sobre natureza, características, qualidade, quantidade, propriedades, origem, preço e
  demais dados. § 2º define **abusiva**: discriminatória, que incite violência, explore
  medo ou superstição, se aproveite da deficiência de julgamento da criança, desrespeite
  valores ambientais, ou induza o consumidor a comportamento prejudicial/perigoso à
  saúde ou segurança. § 3º: é enganosa **por omissão** quando deixar de informar dado
  essencial do produto/serviço.
- **Art. 38, CDC** — o ônus da prova da veracidade e correção da informação ou
  comunicação publicitária cabe a **quem a patrocina**.
- **Art. 56, XII + art. 60, CDC** — sanção administrativa de **contrapropaganda**,
  cominada quando o fornecedor incorre em publicidade enganosa ou abusiva, às expensas
  do infrator, divulgada na mesma forma, frequência, dimensão e, preferencialmente,
  mesmo veículo/local/espaço/horário do anúncio original, de modo a desfazer o malefício
  causado.

## O teste

1. Verificar se a mensagem é identificável como publicidade (art. 36) — publicidade
   disfarçada de conteúdo editorial/neutro já é, por si, um problema adicional.
2. Distinguir **enganosa** (falha de veracidade — falsidade total, parcial ou omissão de
   dado essencial) de **abusiva** (falha de natureza do apelo — discriminação, medo,
   superstição, exploração de criança, indução a risco) — são categorias diferentes e
   cumuláveis, uma não substitui a outra.
3. Aplicar a inversão do ônus da prova: **é o fornecedor quem prova a veracidade** do
   que anunciou (art. 38) — o consumidor não precisa provar a falsidade.
4. Se a oferta foi descumprida, apontar as três opções do art. 35 e deixar a escolha
   expressamente a critério do consumidor.
5. Avaliar cabimento de contrapropaganda (via administrativa, art. 60) como pedido
   adicional, quando a matéria também for levada a órgão de defesa do consumidor.

## Tese do consumidor

A oferta vincula o fornecedor independentemente de constar no contrato assinado
(art. 30) — o que foi anunciado é exigível. A omissão de dado essencial já configura,
por si, publicidade enganosa (art. 37, § 3º), sem necessidade de provar dolo do
anunciante. O ônus de provar que o anúncio era verdadeiro é do fornecedor, não do
consumidor.

## Tese do fornecedor

A peça publicitária era claramente identificável como tal e continha as condições e
ressalvas aplicáveis, visíveis ao consumidor médio. A informação supostamente omitida
não era "dado essencial" e não teve o condão de induzir a erro relevante. O exagero
apontado é mero exagero publicitário tolerado pelo mercado (*puffing*), incapaz de
enganar um consumidor razoavelmente atento.

## Armadilhas

Nenhuma das travas T1–T13 deste corpus incide diretamente sobre esta matéria; a
armadilha central é conceitual: **não tratar "enganosa" e "abusiva" como sinônimos** —
uma cobra veracidade, a outra cobra a natureza do apelo, e a peça deve nomear
corretamente qual delas está em jogo (ou ambas, cumulativamente) para não enfraquecer o
pedido.

## Fronteira

Publicidade de cobertura em plano de saúde depois negada: mérito clínico em
`direito-medico-adv-os`; cobertura fora do rol da ANS, ver skill de saúde suplementar
deste plugin. Publicidade de crédito/juros: `bancario-adv-os`. Prática comercial
correlata (venda casada, elevação de preço): `pratica-e-clausula-abusiva`.

---
name: onus-da-prova-consumo-sbroggioadv
title: Ônus da Prova em Consumo
description: 'Trata a inversão do ônus da prova em consumo — art. 6º, VIII, CDC (verossimilhança OU hipossuficiência, requisitos alternativos) combinado com o art. 373, §1º, CPC (inversão legal x distribuição dinâmica). Fixa o momento processual correto: regra de instrução, preferencialmente no saneamento, nunca só na sentença. Aciona: ao pedir a inversão do ônus na inicial, ao arguir cerceamento de defesa por inversão tardia, ou quando a prova do fato depende de documento ou perícia que só o fornecedor tem condição de produzir.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/onus-da-prova-consumo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Ônus da Prova em Consumo

## Quando esta skill entra
Sempre que a produção de prova for um obstáculo real ao consumidor (prova técnica, documento em
poder do fornecedor, perícia cara) — para pedir a inversão cedo, no momento certo — e sempre que o
fornecedor for surpreendido por uma inversão tardia, para arguir cerceamento de defesa.

## Base normativa
- **Art. 6º, VIII, CDC** — é direito básico do consumidor a facilitação da defesa de seus direitos,
  "inclusive com a inversão do ônus da prova, a seu favor, no processo civil, quando, a critério
  do juiz, for **verossímil a alegação** ou quando for ele **hipossuficiente**, segundo as regras
  ordinárias de experiência." (fonte: `context/cdc-lei-8078.md`)
- **Art. 373, §1º, CPC** — contempla **duas** regras distintas que usam o mesmo dispositivo, mas
  não são a mesma coisa: (a) atribuição do ônus por decisão judicial "nos casos previstos em lei"
  — é aqui que entra a inversão consumerista do art. 6º, VIII; e (b) a **distribuição dinâmica** do
  ônus por peculiaridade do caso concreto (impossibilidade ou excessiva dificuldade de a parte
  cumprir o encargo estático, ou maior facilidade de a parte contrária obter a prova do fato
  contrário) — hipótese **distinta** da inversão do CDC, embora ambas apareçam no mesmo artigo do
  CPC. (fonte: `context/jec-fonaje-e-recursos.md`, §3.1)

## O teste / o passo a passo
1. **Verossimilhança OU hipossuficiência — são requisitos alternativos, não cumulativos.** Basta
   um dos dois, a critério do juiz, segundo as regras ordinárias de experiência. Exigir os dois ao
   mesmo tempo é erro comum de quem lê o art. 6º, VIII como se fosse conjunção "e".
2. Identifique se o caso pede a inversão do art. 6º, VIII (regra específica de consumo) ou a
   distribuição dinâmica genérica do art. 373, §1º, CPC (regra geral de processo civil, aplicável
   mesmo fora do CDC) — a fundamentação correta muda o dispositivo citado na petição.
3. **O momento processual é o que mais frequentemente decide o resultado do recurso**, não o
   mérito da inversão em si (ver seção abaixo).

## O momento processual — regra de instrução, não de julgamento
Jurisprudência consolidada do STJ (Segunda Seção, desde pelo menos 2012; reafirmada em REsp
1.286.273-SP, 4ª Turma, Rel. Min. Marco Buzzi, j. 08/06/2021): a inversão do ônus da prova do art.
6º, VIII é **regra de instrução**, não regra de julgamento. A decisão que a determina deve ser
proferida, preferencialmente, no **saneamento** do processo — ou, no mínimo, deve assegurar à
parte a quem não incumbia inicialmente o encargo a **reabertura de oportunidade** para se
manifestar e produzir prova. O STJ já cassou acórdão que só inverteu o ônus no julgamento da
apelação, quando já não havia mais possibilidade de produzir prova — cerceamento de defesa.
(fonte: `context/jec-fonaje-e-recursos.md`, §3.2)

## Tese do consumidor × Tese do fornecedor
- **Tese do consumidor:** pedir a inversão **cedo** — já na petição inicial, reforçada no
  despacho saneador — em vez de confiar que "o juiz inverte na sentença mesmo". Se a inversão só
  veio na sentença ou no acórdão, sem chance prévia de o fornecedor produzir prova, a decisão fica
  vulnerável a nulidade por cerceamento — o que pode, contraintuitivamente, jogar contra o próprio
  consumidor no recurso, anulando uma sentença favorável.
- **Tese do fornecedor:** se a inversão só apareceu na sentença ou no julgamento do recurso, sem
  chance de produzir prova sob o novo ônus, há fundamento sólido de nulidade/cerceamento de
  defesa — matéria de ordem pública, alegável a qualquer tempo no grau recursal ainda disponível.
  Fora disso, atacar a ausência de verossimilhança/hipossuficiência concreta, não apenas invocar
  "o CDC inverte sempre".

## Ônus do fornecedor sobre fatos impeditivos, modificativos ou extintivos
Mesmo sem inversão declarada, o regime geral do art. 373, caput, CPC já atribui ao réu o ônus de
provar fato impeditivo, modificativo ou extintivo do direito do autor (excludentes dos arts. 12,
§3º e 14, §3º, CDC — ver `vicio-defeito-e-responsabilidade`). A inversão do art. 6º, VIII soma-se
a esse regime geral; não o substitui.

## Armadilhas
- Tratar verossimilhança e hipossuficiência como requisitos cumulativos — são alternativos.
- Pedir/decidir a inversão só na sentença — é o erro mais recorrente encontrado na pesquisa, e
  fundamento certo de recurso quando acontece.
- Confundir a inversão do CDC (regra específica) com a distribuição dinâmica genérica do CPC
  (regra geral aplicável a qualquer processo) — são regimes distintos hospedados no mesmo
  dispositivo do CPC.
- **T13** — normalizar espaço em branco ao conferir citação literal contra os anexos.

## Fronteira
Discussão de ônus da prova em revisional bancária específica: `bancario-adv-os`. Regras gerais de
rito comum fora de consumo: `civel-adv-os`.

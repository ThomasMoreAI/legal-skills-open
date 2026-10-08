---
name: competencia-jec-x-comum-sbroggioadv
title: Competência JEC × Justiça comum
description: 'Determina se uma causa de consumo cabe no Juizado Especial Cível ou deve ir para a Justiça comum. Aplica o teste do objeto da prova (não o direito material), a alçada de 40 salários mínimos com a renúncia ao crédito excedente, as causas excluídas por matéria, quem pode ser parte — inclusive MEI, ME e EPP como autores — e como o fornecedor argui incompetência com chance real de êxito. Aciona: definir o foro certo antes de ajuizar, avaliar se a causa é complexa demais para o Juizado, checar se o autor pessoa jurídica pode propor no JEC, montar defesa de incompetência.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/competencia-jec-x-comum
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: regulatory
language: pt
---

# Competência JEC × Justiça comum

## Quando esta skill entra
Antes de redigir a inicial de consumo (escolha de foro) ou quando o fornecedor quer arguir
incompetência do Juizado Especial.

## Base normativa
- Lei 9.099/1995, art. 3º, I a IV e §§1º-3º — competência, alçada de 40 salários mínimos (SM),
  execução de julgados e de títulos extrajudiciais, causas excluídas, renúncia ao excedente.
- Lei 9.099/1995, art. 8º e §1º, II (redação LC 147/2014) — quem pode e quem não pode ser parte.
- Lei 9.099/1995, art. 10 — veda intervenção de terceiro e assistência; admite litisconsórcio.
- Lei 9.099/1995, art. 35 — perícia informal (técnico de confiança do juiz + parecer técnico).
(anexo `context/lei-9099-jec.md`)
- FONAJE, Enunciados 12, 39, 54, 70, 94, 146 (anexo `context/jec-fonaje-e-recursos.md`)

## O teste que decide
FONAJE, Enunciado 54: "A menor complexidade da causa para a fixação da competência é aferida pelo
objeto da prova e não em face do direito material." Não é o tipo de direito discutido (ex.: "é
plano de saúde, logo é complexo") que define a competência — é **o que precisa ser provado**.

Reforços diretos:
- Enunciado 70: discutir ilegalidade de juros não é complexo para fins de competência, "exceto
  quando exigirem perícia contábil".
- Enunciado 94: ação de revisão de contrato cabe no JEC, "exceto quando exigir perícia contábil".
- Enunciado 12: a perícia do art. 35 é **informal** — sem nomeação de perito, sem prazo de
  quesitos, sem laudo formal com contraditório amplo do CPC. Quando o objeto da prova exige mais
  que isso, é sinal de incompetência (não de "conversão" do rito dentro do próprio Juizado).

## Gatilhos de incompetência
1. **Valor** — pretensão acima de 40 SM (art. 3º, I). O consumidor pode ajuizar no JEC mesmo
   assim, mas renuncia ao crédito excedente ao limite (art. 3º, §3º) — **exceto na hipótese de
   conciliação**, em que pode negociar valor acima do teto sem essa renúncia travar o acordo.
2. **Complexidade probatória real** — o objeto da prova exige perícia formal que a perícia
   informal do art. 35 não supre com segurança.
3. **Litisconsórcio × intervenção de terceiro** — art. 10 veda qualquer forma de intervenção de
   terceiro e de assistência (mata a denunciação da lide, ex.: fornecedor querendo trazer o
   fabricante ou a seguradora depois de citado); o litisconsórcio — partes que já nascem no polo —
   é admitido.
4. **Matéria excluída** (art. 3º, §2º) — natureza alimentar, falimentar, fiscal, interesse da
   Fazenda Pública, acidente de trabalho, resíduos, estado/capacidade das pessoas. Quando o
   fornecedor é pessoa jurídica de direito público (ex.: concessionária de serviço público), a
   natureza do polo passivo pode deslocar para o rito da Fazenda Pública (Lei 12.153/2009), não
   para a Justiça comum genérica.

## Quem pode ser parte
- **Não podem ser parte** (art. 8º, caput): incapaz, preso, pessoa jurídica de direito público,
  empresas públicas da União, massa falida, insolvente civil.
- **MEI, ME e EPP PODEM propor ação** — art. 8º, §1º, II, na redação dada pela LC 147/2014. O
  inciso anterior do mesmo parágrafo, que remetia à definição de microempresa da Lei 9.841/1999,
  está revogado por essa redação — citar a Lei 9.841/1999 como base é citar dispositivo morto.
- FONAJE, Enunciado 146: pessoa jurídica de factoring/gestão de créditos e ativos financeiros
  **não** pode propor ação no JEC (exceto as do art. 8º, §1º, IV) — é regra sobre quem pode ser
  **autor**, não sobre o porte do réu.
- **Não existe** nos enunciados do FONAJE nenhum critério de competência ligado ao **porte** do
  fornecedor réu. Banco, operadora de plano de saúde, varejista de grande porte podem, sim, ser
  réus no JEC — a discussão real de incompetência que esse tipo de fornecedor levanta na prática
  é sempre por complexidade probatória, nunca por porte econômico em si.

## Tese do consumidor
Para blindar a competência do JEC: evitar pedir perícia formal na inicial; sustentar a pretensão
com prova documental, testemunhal e, quando necessário, o parecer técnico informal do art. 35
(Enunciado 12); destacar que o litígio depende de interpretação contratual/normativa, não de
metodologia pericial complexa (o que não desloca a competência — Enunciados 70 e 94, primeira
parte).

## Tese do fornecedor
A defesa de incompetência por complexidade só prospera com demonstração **concreta** de que o
objeto da prova exige perícia formal — juntar, por exemplo, laudo técnico preliminar evidenciando
divergência que exige metodologia pericial (cálculo atuarial de reajuste, nexo causal em falha de
produto industrial com múltiplas causas concorrentes). Alegar "é matéria de plano de saúde, logo é
complexa", sem mais, contraria o Enunciado 54 e tende a ser rejeitado.

## Armadilhas
- **T12** — prazos no JEC contam em **dias úteis** (art. 12-A), nunca corridos; ver
  `rito-jec-consumidor`. Citar a Lei 9.841/1999 para justificar ME como autora é citar inciso
  revogado.
- **T13** — ao conferir citação de artigo contra o anexo `lei-9099-jec.md`, normalize espaço em
  branco antes de comparar; o HTML do Planalto quebra linha no meio da frase e um grep literal dá
  falso negativo.

## Fronteira
Rito comum (fora do JEC, causa acima da alçada sem renúncia ou objeto de prova complexo) →
`civel-adv-os`. Liquidação de valor além do teto de alçada → `calculosjudiciais-adv-os`.
Revisional bancária de alta complexidade probatória → `bancario-adv-os`.

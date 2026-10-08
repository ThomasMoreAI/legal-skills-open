---
name: carencia-cpt-doenca-preexistente-sbroggioadv
title: Carência, CPT e doença/lesão preexistente
description: 'Estrutura a discussão sobre prazos de carência, Cobertura Parcial Temporária (CPT), Declaração de Saúde e doença/lesão preexistente em plano de saúde, além da cobertura de urgência e emergência (Lei 9.656 art. 35-C, Súmula 597/STJ) e o status controverso da Resolução CONSU 13/1998 — sem afirmar que o STJ decidiu o mérito de sua legalidade, pois não decidiu (só anulou por vício processual em 2020). Aciona: carência abusiva, negativa por doença preexistente, CPT, declaração de saúde, urgência e emergência negada, internação de urgência sem carência cumprida.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/carencia-cpt-doenca-preexistente
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: regulatory
language: pt
---

# Carência, CPT e doença/lesão preexistente

## Quando esta skill entra

Toda negativa de cobertura fundada em prazo de carência não cumprido, doença/lesão
preexistente não declarada ou Cobertura Parcial Temporária (CPT), inclusive quando o caso
concreto é de urgência ou emergência.

## Base normativa

- **Lei 9.656/1998, art. 12, V**: prazos máximos de carência — **300 dias** para parto a
  termo; **180 dias** para os demais casos; **24 horas** para urgência e emergência.
- **Art. 13**: renovação automática do contrato, vedada nova cobrança de carência na
  renovação.
- **Art. 11**: vedada exclusão de cobertura por doença/lesão preexistente após **24 meses**
  de vigência; o **ônus da prova** de que o consumidor sabia da doença preexistente é da
  **operadora**; vedada a suspensão da assistência até essa prova ser feita.

## CPT, Declaração de Saúde e o ônus da má-fé

Regulamentação: **RN 558/2022** (Doença/Lesão Preexistente, CPT, Declaração de Saúde,
Carta de Orientação). Mecânica:

- Na contratação, o beneficiário preenche a **Declaração de Saúde**, informando doenças/
  lesões já conhecidas.
- A operadora **não é obrigada** a dar cobertura total ao item declarado — pode oferecer
  **CPT** só para aquele item, pelo prazo de carência contratual, após o qual a cobertura
  passa a ser total.
- Se o beneficiário declarar não ter doença/lesão e a operadora suspeitar do contrário
  (exame/procedimento nos primeiros 24 meses), abre-se discussão de má-fé — mas o **ônus é
  da operadora** (art. 11 da Lei).

🟡 **Súmula 609/STJ** (2018, campo securitário amplo — usar com essa ressalva, não nasceu
especificamente para plano de saúde): "A recusa de cobertura securitária, sob a alegação de
doença preexistente, é ilícita se não houve a exigência de exames médicos prévios à
contratação ou a demonstração de má-fé do segurado."

## Urgência e emergência

**Lei 9.656/1998, art. 35-C**: cobertura obrigatória em casos de **(I) emergência** —
risco imediato de vida ou lesões irreparáveis, caracterizado por declaração do médico
assistente; **(II) urgência** — acidentes pessoais ou complicações no processo gestacional;
**(III) planejamento familiar**.

**Súmula 597/STJ**: "A cláusula contratual de plano de saúde que prevê carência para
utilização dos serviços de assistência médica nas situações de emergência ou de urgência é
considerada abusiva se ultrapassado o prazo máximo de **24 horas** contado da data da
contratação."

## Armadilha central — CONSU 13, o que o STJ realmente decidiu

A Resolução **CONSU 13/1998** (ato do Conselho de Saúde Suplementar, não da ANS) tentou
limitar a cobertura de urgência/emergência (ex.: internação a 12h em certas hipóteses) —
questionada por ação civil pública do MPRJ; 1º e 2º graus (TJRJ) reconheceram a ilegalidade.

🟡🔴 **Em 13/11/2020, a Quarta Turma do STJ ANULOU** a sentença e o acórdão do TJRJ — mas
**por vício processual** (falta de litisconsórcio necessário da União e da ANS), com
remessa à Justiça Federal do Rio. **O STJ NÃO decidiu se a CONSU 13 é ou não ilegal** —
apenas invalidou o processo. **Nunca afirme** "o STJ decidiu que a CONSU 13 é ilegal" nem
"o STJ validou a CONSU 13" — nenhuma das duas está provada. A base sólida da tese é a
combinação **art. 35-C + Súmula 597**, independentemente do destino final da ação civil
pública contra a CONSU 13.

## Tese do consumidor × tese da operadora

**Consumidor**: em urgência/emergência, invoca art. 35-C + Súmula 597 (24h) sem depender do
destino da CONSU 13; em doença preexistente, exige da operadora a prova de má-fé/ciência
prévia (art. 11); contesta CPT aplicada sem Declaração de Saúde regular.

**Operadora**: sustenta CPT regularmente contratada com base na Declaração de Saúde; em
urgência/emergência anterior a 24h de contratação, pode invocar a CONSU 13 como limitador —
a peça de resposta deve neutralizar esse argumento com art. 35-C + Súmula 597, sem alegar
falsamente que o STJ já resolveu o mérito da CONSU 13 num sentido ou noutro.

## Armadilhas

- A trava da CONSU 13 acima é o ponto mais sensível desta skill — releia antes de redigir
  qualquer parágrafo que mencione a resolução.
- **T5** — ao citar o Anexo do rol para afastar exclusões de urgência, confirme a versão
  vigente do Anexo (base RN 465/2021) na data do caso.

## Fronteira

Negativa de cobertura por rol (não por carência): `negativa-cobertura-saude-suplementar`.
Precisa de liminar: `tutela-urgencia-cobertura-saude`.

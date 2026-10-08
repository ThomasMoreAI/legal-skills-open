---
name: telecom-energia-agua-sbroggioadv
title: Telecom, energia e água — consumo
description: 'Trata cobrança indevida, cobrança de serviço não contratado, falha de prestação e interrupção de fornecimento nos serviços essenciais de telecomunicações, energia elétrica e água/esgoto. Aplica o dever de serviço adequado e contínuo (CDC art. 22 e art. 6º, X) e as obrigações do SAC (Decreto 11.034/2022). Corrige a citação fantasma da "Súmula 194/STJ" para corte por débito pretérito — não existe essa súmula sobre o tema; a regra é jurisprudência reiterada não sumulada, e o Tema 699/STJ cobre só o subcaso de fraude no medidor. Aponta a fronteira com a agência reguladora setorial e escreve os dois lados: tese do consumidor e tese da concessionária/prestadora. Aciona quando o usuário trouxer conta de telefone/internet/energia/água com cobrança indevida, corte de serviço, falha de sinal ou fornecimento, ou pedir defesa de concessionária/operadora nesses casos.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/telecom-energia-agua
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Telecom, energia e água — consumo

## Quando esta skill entra

Disputas de consumo contra operadoras de telecomunicações (telefonia, internet,
TV por assinatura) e concessionárias/permissionárias de energia elétrica e de
água/esgoto: cobrança indevida, cobrança de serviço não contratado, falha
recorrente de prestação (queda de sinal, oscilação de energia, falta de água) e
corte/interrupção do fornecimento.

## Base normativa

- **CDC art. 22** — órgãos públicos e concessionárias/permissionárias são
  obrigados a fornecer serviço adequado, eficiente, seguro e, quanto aos
  essenciais, **contínuo**. Parágrafo único: descumprimento gera dever de cumprir
  e de reparar o dano.
- **CDC art. 6º, X** — direito básico à "adequada e eficaz prestação dos serviços
  públicos em geral".
- **CDC art. 14** — responsabilidade objetiva por defeito na prestação do serviço.
- **CDC art. 42, parágrafo único** — repetição em dobro da cobrança indevida
  (sujeita à modulação do Tema 929/STJ — ver Armadilhas).
- **Decreto 11.034/2022 (SAC)** — acesso 24h/7 dias por ao menos um canal (art.
  4º); resposta em até 7 dias corridos do registro (art. 13); vedação de exigir
  repetição da demanda já registrada (art. 10); cancelamento com efeito imediato,
  independente de adimplência, salvo processamento técnico (art. 14, II) —
  cobrança após cancelamento tempestivo é ilícito autônomo.

## T2 — a trava central desta skill

**"Súmula 194/STJ" para vedar corte de serviço público por débito pretérito NÃO
EXISTE.** A Súmula 194/STJ real trata de prescrição de 20 anos para indenização
por defeito de obra contra construtor — assunto **totalmente diferente**. Essa
citação fantasma se propaga entre fontes secundárias e nunca deve ser usada nesta
skill nem em peça.

A regra correta: **não é lícito à concessionária interromper serviço essencial por
débito pretérito** — só cabe corte por conta regular/atual, mediante aviso prévio.
Essa é **jurisprudência pacífica e reiterada do STJ, mas não sumulada**. O
precedente qualificado mais próximo, sob rito repetitivo, é o **Tema 699/STJ**, e
ele cobre **só o subcaso específico** de recuperação de consumo por **fraude no
medidor** — corte administrativo possível mediante aviso prévio, sobre o consumo
apurado nos 90 dias anteriores à constatação da fraude, com corte executável em
até 90 dias após o vencimento do débito. Não é a tese geral "corte por débito
pretérito é sempre ilegal"; para a regra geral (débito comum/antigo, sem fraude),
a fundamentação correta é jurisprudência reiterada + doutrina, **nunca uma
súmula**.

## O teste / passo a passo

1. **O corte foi por débito atual ou pretérito?** Atual, com aviso prévio → em
   regra lícito. Pretérito → em regra ilícito, salvo a hipótese específica de
   fraude no medidor apurada com contraditório (Tema 699).
2. **Houve fraude no medidor alegada?** Só aí o Tema 699 entra — checar os
   requisitos cumulativos: apuração com contraditório e ampla defesa, janela de 90
   dias de retroação do débito recuperado, corte em até 90 dias do vencimento.
3. **A cobrança questionada é de serviço efetivamente contratado?** Cobrança de
   item não contratado é falha de informação (CDC art. 6º, III) e enseja repetição
   do indébito.
4. **O consumidor tentou o canal de atendimento (SAC) antes?** Reforça a mora do
   fornecedor se a resposta não veio em 7 dias corridos (Decreto 11.034/2022, art.
   13) ou se a demanda já registrada foi exigida de novo (art. 10).

## Tese do consumidor

- Corte por débito pretérito é presumidamente ilegal, salvo prova cabal de fraude
  no medidor com os requisitos do Tema 699 preenchidos pela concessionária.
- Falha na prestação (queda de sinal, oscilação, falta de água) sem prestação
  alternativa adequada gera dever de indenizar, com responsabilidade objetiva do
  art. 14.
- Cobrança de serviço não contratado ou mantida após cancelamento tempestivo
  (art. 14, II do Decreto 11.034/2022) é cobrança indevida — pedir repetição em
  dobro, observada a modulação do Tema 929.
- Descumprimento dos prazos do SAC (resposta em 7 dias, exigência de repetir a
  demanda) é prova de descaso, reforça o dano moral.

## Tese da concessionária/prestadora

- Corte foi por débito **atual**, com aviso prévio comprovado — cumpre o dever de
  continuidade sem violar o CDC.
- Se invocar fraude no medidor, arcar com o ônus de provar os requisitos do Tema
  699 (contraditório, ampla defesa, janela de 90 dias) — sem isso a tese não se
  sustenta.
- Falha pontual, isolada e prontamente sanada tende a "mero dissabor" — mas exige
  prova de que o SAC funcionou dentro dos prazos do Decreto 11.034/2022.
- Cobrança contestada corresponde a serviço efetivamente prestado e contratado —
  ônus da prova da contratação é do fornecedor quando o consumidor nega.

## Armadilhas

- **T2** — nunca citar "Súmula 194/STJ" para corte de serviço público. Não é
  sumulada; é jurisprudência reiterada, com o Tema 699 cobrindo só a fraude no
  medidor.
- Não confundir a regra geral de vedação de corte por débito pretérito com o
  regime específico e mais permissivo do Tema 699 (fraude apurada).
- Repetição em dobro (art. 42, parágrafo único) tem **modulação do Tema 929/STJ**:
  dispensa má-fé só para cobranças a partir de 30/03/2021; cobrança anterior a
  essa data segue o regime antigo, que exige má-fé.
- **Não inventar número de resolução de ANATEL, ANEEL ou ANAC.** Nenhuma consta
  neste corpus — se a peça precisar citar resolução setorial específica, marcar
  `[VERIFICAR — não confirmado no corpus]` e conferir na fonte oficial da
  agência antes de peticionar.

## Fronteira

Corte/negativação por débito de origem bancária ou revisão de tarifa bancária →
`bancario-adv-os`. Cobrança que já virou execução de título ou cobrança pura →
`execucao-adv-os`. Cálculo de valor a repetir/liquidar → `calculosjudiciais-adv-os`.
Discussão puramente regulatória perante a agência (sem viés de defesa do
consumidor em juízo) foge do escopo desta skill — aponte para a fonte oficial do
órgão regulador competente.

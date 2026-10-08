---
name: servico-educacional-e-continuado-sbroggioadv
title: Serviço educacional e continuado
description: 'Trata a relação de consumo em serviço educacional (mensalidade escolar, reajuste, recusa de rematrícula por inadimplência, retenção de documento e histórico) e em serviço continuado em geral (academia, curso, streaming, assinatura): cancelamento, multa de fidelidade e venda casada. Aplica o CDC art. 39, I (venda casada), art. 51 (cláusulas abusivas) e o dever de cancelamento com efeito imediato do SAC (Decreto 11.034/2022, art. 14, II) por analogia a qualquer consumo continuado. Marca como `[VERIFICAR]` qualquer percentual ou prazo da Lei 9.870/1999 não capturado nos anexos. Escreve os dois lados: tese do consumidor e tese da instituição/fornecedor. Aciona com mensalidade escolar, reajuste de anuidade, recusa de rematrícula, retenção de histórico/documento, cancelamento de academia/curso/assinatura/streaming, multa de fidelidade, ou defesa da instituição/fornecedor nesses casos.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/servico-educacional-e-continuado
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Serviço educacional e continuado

## Quando esta skill entra

Duas frentes que compartilham a mesma lógica de serviço de trato continuado
submetido ao CDC: (1) educacional — mensalidade escolar, reajuste de anuidade,
recusa de rematrícula por inadimplência, retenção de documento/histórico; (2)
continuado em geral — academia, curso, streaming, assinatura: cancelamento, multa
de fidelidade, cobrança após pedido de cancelamento.

## Base normativa

- **CDC art. 39, I** — é vedado condicionar o fornecimento de um produto/serviço
  ao de outro (venda casada), ou impor limite quantitativo sem justa causa.
  Aplica-se, por exemplo, à exigência de contratar serviço acessório não desejado
  como condição de matrícula ou de manutenção do plano.
- **CDC art. 51, I e IV** — nulas as cláusulas que exonerem a responsabilidade do
  fornecedor por vício, ou que coloquem o consumidor em desvantagem exagerada
  incompatível com a boa-fé.
- **CDC art. 51, I e IV (não o XI)** — retenção de documento necessário para prova
  de obrigações já cumpridas é vedada pelo **conjunto** desses dois incisos.
  ⚠️ **Não fundamente no art. 51, XI**: aquele inciso trata de *cláusula que autoriza
  o fornecedor a cancelar o contrato unilateralmente*, assunto diferente. Este corpus
  não traz inciso específico sobre retenção de histórico escolar —
  `[VERIFICAR — não confirmado no corpus]` antes de citar dispositivo mais
  específico.
- **CDC art. 42** — o consumidor inadimplente não pode ser exposto a ridículo nem
  submetido a constrangimento na cobrança; a retenção de documento como forma de
  pressão para pagamento é, em tese, prática que se aproxima desse limite.
- **Decreto 11.034/2022 (SAC), art. 14, II** — cancelamento com efeito **imediato**,
  independente de adimplência (salvo processamento técnico); cobrança após pedido
  de cancelamento tempestivo é cobrança indevida (CDC art. 42, parágrafo único).
  Aplica-se diretamente a serviços continuados com atendimento regulado pelo SAC
  (academia, streaming, assinatura de porte relevante) e serve de referência de
  princípio para qualquer relação de trato continuado.

## O teste / passo a passo

1. **É frente educacional ou continuado geral?** Educacional: verificar se o
   reajuste tem previsão contratual clara e se a recusa de rematrícula ocorreu por
   inadimplência de anos anteriores (prática debatida na jurisprudência, mas sem
   número de súmula confirmado neste corpus — tratar como tese, não como regra
   pacificada). Continuado geral: verificar se o cancelamento foi processado no
   mesmo canal da contratação e se o efeito foi imediato.
2. **Há retenção de documento (histórico, certificado, diploma) condicionada a
   pagamento?** Fundamentar pelo conjunto do art. 51 (I, IV) e pelo art. 42 — não
   citar um inciso específico e dedicado ao tema sem verificar.
3. **Há venda casada?** (matrícula condicionada a material didático de fornecedor
   único sem alternativa, plano de academia condicionado a personal obrigatório,
   assinatura condicionada a serviço acessório) → CDC art. 39, I.
4. **O cancelamento gerou cobrança posterior?** Se o pedido foi tempestivo e o
   canal foi o mesmo da contratação, cobrança após o pedido é indevida (art. 14,
   II do Decreto 11.034/2022 + CDC art. 42, parágrafo único) — pedir repetição em
   dobro, observada a modulação do Tema 929/STJ (regime de má-fé para cobranças
   anteriores a 30/03/2021).
5. **Há multa de fidelidade?** Verificar se está prevista de forma clara e
   proporcional no contrato (CDC art. 51, IV) — multa desproporcional ao tempo
   restante de fidelidade é candidata a revisão.

## Tese do consumidor

- Retenção de documento/histórico como coação para pagamento viola o sistema de
  proteção do art. 51 e o dever de cobrança sem constrangimento do art. 42 — a
  via correta é a cobrança judicial/administrativa, não a retenção do documento.
- Reajuste sem previsão contratual clara, ou aplicado de forma unilateral, é
  cláusula abusiva (art. 51, X e XIII).
- Cancelamento deve ter efeito imediato; cobrança após pedido tempestivo é
  indevida e sujeita à repetição em dobro.
- Venda casada de material, serviço acessório ou plano adicional é vedada (art.
  39, I), independentemente de "praxe de mercado".

## Tese da instituição/fornecedor

- Reajuste está previsto em cláusula clara, compatível com o índice contratado —
  não há abusividade quando o consumidor tinha ciência prévia e o percentual é
  razoável.
- Recusa de rematrícula por inadimplência de período anterior é exercício regular
  de direito, não retaliação — desde que não envolva retenção do histórico do
  período já cursado e pago.
- Cancelamento foi processado fora do prazo, ou por canal diverso do contratado —
  a cobrança seguinte corresponde a período efetivamente utilizado ou já em
  processamento técnico (exceção do art. 14, II do Decreto 11.034/2022).
- Serviço acessório é efetivamente opcional, com alternativa clara ao consumidor —
  não há venda casada quando a adesão é facultativa e informada.

## Armadilhas

- **Não citar número de artigo específico da Lei 9.870/1999** (mensalidades
  escolares) além do que está confirmado no corpus — o corpus só registra que essa
  lei alterou o CDC art. 39, XIII (reajuste diverso do legal/contratual). Qualquer
  percentual de multa por atraso, prazo de aviso de rematrícula ou regra de
  parcelamento específico da Lei 9.870/1999 deve vir marcado `[VERIFICAR — não
  confirmado no corpus]`.
- Não afirmar que existe súmula específica sobre retenção de histórico escolar —
  não está confirmada neste corpus; fundamentar pelo sistema geral do art. 51 e
  art. 42.
- Repetição em dobro por cobrança pós-cancelamento tem a mesma modulação do Tema
  929/STJ que qualquer outra cobrança indevida — checar a data.

## Fronteira

Serviço educacional de ensino superior com viés regulatório específico (MEC,
FIES/Prouni) foge do escopo desta skill — trate apenas a relação contratual de
consumo. Rito comum fora do JEC → `civel-adv-os`. Cálculo de valores a repetir →
`calculosjudiciais-adv-os`. Validação de citação de jurisprudência →
`juris-adv-os`.

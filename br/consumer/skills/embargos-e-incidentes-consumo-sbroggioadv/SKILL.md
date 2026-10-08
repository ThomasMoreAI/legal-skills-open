---
name: embargos-e-incidentes-consumo-sbroggioadv
title: Embargos de declaração e incidentes em matéria de consumo
description: 'Estrutura embargos de declaração em matéria de consumo — no JEC, INTERROMPEM o prazo recursal (Lei 9.099/95, art. 50); no rito comum, seguem o CPC — além de agravo de instrumento em tutela de urgência de consumo, IRDR/repetitivo com suspensão de processos e o alerta de que reclamação contra decisão de Turma Recursal não cabe mais ao STJ desde 2016. Aciona: opor embargos de declaração em ação de consumo, calcular efeito do embargo sobre o prazo recursal, avaliar agravo de instrumento contra decisão interlocutória de urgência, entender por que um processo de consumo foi suspenso por tema afetado, verificar se cabe reclamação.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/embargos-e-incidentes-consumo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Embargos de declaração e incidentes em matéria de consumo

## Quando esta skill entra
Decisão omissa, contraditória, obscura ou com erro material em ação de consumo;
necessidade de impugnar decisão interlocutória de urgência; processo suspenso por
tema repetitivo/IRDR afetado; dúvida sobre se cabe reclamação contra Turma Recursal.

## Base normativa
Lei 9.099/1995, art. 50 (`context/lei-9099-jec.md`, achado T12); Resolução STJ 3/2016
(`context/jec-fonaje-e-recursos.md`); regras gerais do CPC para embargos de
declaração, agravo de instrumento e IRDR — sem corpus de captura própria neste
plugin; para o detalhe procedimental completo, ver `civel-adv-os`.

## Embargos de declaração — regime muda conforme o rito

**No JEC:** os embargos de declaração **INTERROMPEM** o prazo para o recurso
inominado (Lei 9.099/1995, art. 50, T12) — regime **diferente** do rito comum. Quem
trata embargos no JEC como se suspendessem (em vez de interromper) o prazo erra a
contagem do recurso seguinte.

**No rito comum:** cabimento por omissão, contradição, obscuridade ou erro material
(CPC, arts. 1.022 e seguintes — regras gerais não exclusivas de consumo, tratamento
procedimental completo em `civel-adv-os`). Uso estratégico em matéria de consumo:
prequestionar matéria federal/constitucional que o acórdão não enfrentou, viabilizando
o recurso excepcional (ver `resp-e-re-consumo`).

## Agravo de instrumento em consumo
Cabível contra decisões interlocutórias em hipóteses do CPC (rol do art. 1.015, com
interpretação extensiva do STJ para tutelas de urgência) — regra geral do CPC, sem
corpus de captura própria neste plugin. Uso típico em consumo: decisão que concede
ou nega tutela de urgência para restabelecer cobertura de plano de saúde, suspender
negativação indevida, ou determinar exibição de documento/contrato.

## IRDR e suspensão por tema afetado
Quando um Tribunal instaura IRDR (ou o STJ afeta tema repetitivo), processos com a
mesma questão de direito ficam suspensos até o julgamento. **Exemplo concreto e
verificado:** o TJMG fixou, em IRDR, tese condicionando o ajuizamento de ação de
consumo à tentativa extrajudicial prévia (SAC, PROCON, consumidor.gov.br etc.) — tese
hoje em discussão no STJ, Tema 1.396, afetado e pendente (ver
`consumidor-gov-br-e-pre-processual` para o detalhe completo). Um processo que
discuta a mesma questão de direito num Estado com IRDR firmado pode ser suspenso até
o STJ decidir o tema.

## Reclamação — não cabe mais ao STJ desde 2016
🔴 **Ponto que a memória confiada erraria:** entre 2009 e 2016, a Resolução STJ
12/2009 permitia reclamação diretamente ao STJ contra decisão de Turma Recursal que
contrariasse jurisprudência do STJ. **Essa via acabou.** A Resolução STJ 3, de
07/04/2016, revogou a 12/2009 e **transferiu a competência** para as Câmaras Reunidas
ou Seção Especializada do próprio Tribunal de Justiça — não mais ao STJ. Isso vale
para as duas partes: quem redige hoje "reclamação ao STJ contra Turma Recursal" está
usando a via errada desde 2016.

## Tese do consumidor × tese do fornecedor
**Consumidor:** opor embargos de declaração no JEC sempre que a sentença for omissa
sobre pedido (dano moral, repetição em dobro, inversão de ônus) — o efeito
interruptivo (não suspensivo) é uma vantagem tática para reorganizar a estratégia
recursal sem pressa de prazo. **Fornecedor:** usar embargos para prequestionar
matéria federal antes do recurso excepcional; agravar decisão de urgência que
antecipa efeitos da tutela sem os requisitos legais; verificar se há IRDR/tema
afetado no tribunal local antes de litigar em massa sobre a mesma questão.

## Armadilhas
- No JEC, embargos **interrompem** (não suspendem) o prazo — regime distinto do rito
  comum (Lei 9.099/95, art. 50, T12).
- Reclamação contra Turma Recursal **não vai mais ao STJ** desde a Resolução STJ
  3/2016 — vai para o próprio TJ.
- Não tratar tema afetado (ainda sem julgamento de mérito) como já pacificado.

## Fronteira
Cabimento de REsp/RE e prequestionamento → `resp-e-re-consumo`. Tema 1.396 (interesse
de agir/tentativa extrajudicial prévia) em profundidade →
`consumidor-gov-br-e-pre-processual`. Mecânica procedimental completa de agravo de
instrumento e embargos no rito comum → `civel-adv-os` (cross-link soft).

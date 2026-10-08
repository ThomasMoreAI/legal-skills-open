---
name: o-que-sobe-do-jec-sbroggioadv
title: O que sobe do JEC — vias depois da Turma Recursal
description: 'Mapeia o que cabe e o que não cabe depois da decisão da Turma Recursal do JEC: recurso especial ao STJ não cabe (Súmula 203/STJ), recurso extraordinário ao STF cabe (Súmulas 640 e 727/STF), reclamação ao STJ não cabe mais desde 2016 (Resolução STJ 3/2016 — corrige premissa comum e desatualizada), pedido de uniformização não existe no JEC estadual comum, mandado de segurança contra ato de Turma Recursal é julgado pela própria Turma, e não cabe ação rescisória. Aciona: avaliar via recursal depois da Turma Recursal, decidir entre REsp e RE, impetrar mandado de segurança contra decisão do JEC, avaliar se cabe reclamação ou rescisória.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/o-que-sobe-do-jec
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# O que sobe do JEC — vias depois da Turma Recursal

## Quando esta skill entra
Depois de esgotado o recurso inominado, ao avaliar se resta alguma via de impugnação da decisão
da Turma Recursal.

## Base normativa
Lei 9.099/1995, art. 59 (anexo `context/lei-9099-jec.md`); Súmula 203/STJ; Súmulas 640 e 727/STF;
Resolução STJ n. 3/2016; STJ, Rcl 22.033/SC (Primeira Seção, 08/04/2015); Súmula 376/STJ; FONAJE,
Enunciado 62 (anexo `context/jec-fonaje-e-recursos.md`).

## Recurso especial ao STJ — não cabe
Súmula 203/STJ: "Não cabe recurso especial contra decisão proferida por órgão de segundo grau dos
Juizados Especiais." O fundamento é constitucional: o art. 105, III da CF exige que a decisão
recorrida venha de **Tribunal** — a Turma Recursal, mesmo integrada por juízes togados, não é
Tribunal para esse efeito.

## Recurso extraordinário ao STF — cabe
Súmula 640/STF: "É cabível recurso extraordinário contra decisão proferida por juiz de primeiro
grau nas causas de alçada, ou por turma recursal de juizado especial cível e criminal." Súmula
727/STF, como trava complementar: a Turma Recursal não pode "engavetar" o RE inadmitido — o
agravo de instrumento contra a decisão que nega seguimento ao RE tem que subir ao STF de qualquer
forma, mesmo em causa originada no Juizado.

## Reclamação ao STJ — não cabe mais desde 2016
Entre 2009 e 2016, a Resolução STJ 12/2009 permitia reclamação diretamente ao STJ contra decisão
de Turma Recursal que contrariasse jurisprudência do STJ. **Essa possibilidade acabou.** A
Resolução STJ n. 3, de 07/04/2016, revogou a Resolução 12/2009 e transferiu a competência para
julgar essas reclamações às **Câmaras Reunidas ou Seções Especializadas do próprio Tribunal de
Justiça** — não mais ao STJ. A reclamação, quando cabível, exige que o acórdão da Turma Recursal
contrarie jurisprudência do STJ consolidada em incidente de assunção de competência, IRDR,
recurso especial repetitivo, súmula do STJ ou precedente do STJ — mas quem julga é o **próprio
TJ**, internamente, não Brasília. Redigir petição hoje pedindo "reclamação ao STJ contra decisão
de Turma Recursal" usa a via errada desde 2016 — armadilha igual para os dois lados.

## Pedido de uniformização — não existe no JEC estadual comum
Existem três microssistemas distintos de juizados especiais, cada um com seu próprio mecanismo de
uniformização (STJ, Rcl 22.033/SC, Primeira Seção, 08/04/2015):

| Microssistema | Lei | Mecanismo de uniformização |
|---|---|---|
| Juizados Especiais Estaduais comuns (o do consumidor) | Lei 9.099/1995 | **Não tem** pedido de uniformização próprio — só a reclamação acima, quando cabível |
| Juizados Especiais Federais | Lei 10.259/2001 | Pedido de uniformização à Turma Nacional de Uniformização (TNU) |
| Juizados Especiais da Fazenda Pública | Lei 12.153/2009 | Pedido de uniformização entre Turmas de Estados diferentes ou contra súmula do STJ |

A maioria das ações de consumo tramita no JEC estadual comum — para esse microssistema, não existe
"pedido de uniformização". Confundir com o mecanismo federal (TNU) ou com o da Fazenda Pública é
invocar instrumento que não existe para aquele processo.

## Mandado de segurança contra ato de Turma Recursal — julga a própria Turma
Súmula 376/STJ: "Compete a turma recursal processar e julgar o mandado de segurança contra ato de
juizado especial." FONAJE, Enunciado 62: "Cabe exclusivamente às Turmas Recursais conhecer e
julgar o mandado de segurança e o habeas corpus impetrados em face de atos judiciais oriundos dos
Juizados Especiais." O Órgão Especial do Tribunal de Justiça **não** tem competência para julgar
MS contra ato do microssistema do Juizado, mesmo sendo a Turma quem julgará MS contra ato dela
mesma. Impetrar no Órgão Especial (via comum para MS contra ato de 1º/2º grau "normal") é erro
grosseiro de competência.

## Não cabe ação rescisória
Art. 59: "Não se admitirá ação rescisória nas causas sujeitas ao procedimento instituído por esta
Lei." A decisão transitada em julgado no JEC — inclusive a de Turma Recursal — não é rescindível
pela via da ação rescisória.

## Tese do consumidor
Se a Turma Recursal decide com base em interpretação de norma constitucional (direito fundamental
do consumidor, dignidade, proporcionalidade), o caminho de última instância é **RE ao STF**, nunca
REsp ao STJ.

## Tese do fornecedor
O mesmo caminho vale ao contrário — se a Turma decide com fundamento infraconstitucional
(interpretação do CDC, por exemplo, sem tese constitucional autônoma), **não há recurso de
instância superior possível**: a decisão da Turma Recursal é, na prática, definitiva.

## Armadilhas
**T7** — reclamação ao STJ contra Turma Recursal não cabe mais desde 2016; quem confia na memória
do modelo tende a citar a Resolução 12/2009, revogada. Não existe pedido de uniformização no JEC
estadual comum — não confundir com TNU (federal) ou Fazenda Pública. MS contra ato de Turma vai
para a própria Turma, nunca para o Órgão Especial do TJ.

## Fronteira
Recurso inominado em si (prazo, preparo, efeito) → `recurso-inominado-turma-recursal`. Validação
de citação de súmula/tema antes de peticionar → `juris-adv-os`.

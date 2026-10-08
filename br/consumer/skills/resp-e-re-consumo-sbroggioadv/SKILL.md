---
name: resp-e-re-consumo-sbroggioadv
title: Recurso especial e extraordinário em matéria de consumo
description: 'Avalia cabimento de recurso especial (STJ) e extraordinário (STF) em matéria de consumo quando a origem é acórdão de Tribunal em rito comum — prequestionamento, distinguishing e superação de tema repetitivo/vinculante, usando os temas efetivamente verificados no corpus (929, 1.404, 1.396, 987/STF). Do JEC: REsp NÃO cabe (Súmula 203/STJ), RE cabe (Súmulas 640 e 727/STF) — tratamento completo em o-que-sobe-do-jec, aqui só reforçado. Não trata do requisito de relevância da Lei 15.484 (ver resp-re-os). Aciona: avaliar cabimento de REsp/RE em ação de consumo, identificar se o caso comporta distinguishing de tema repetitivo, decidir a via recursal correta a partir de acórdão de Tribunal (não de Turma Recursal).'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/resp-e-re-consumo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Recurso especial e extraordinário em matéria de consumo

## Quando esta skill entra
Esgotada a apelação em rito comum (`apelacao-consumo-rito-comum`) e se avalia recurso
às cortes superiores, com origem em **acórdão de Tribunal (TJ/TRF)** — hipótese
distinta da que sobe de Turma Recursal do JEC.

## Base normativa
Súmula 203/STJ; Súmulas 640 e 727/STF; STJ Temas 929 e 1.404; STJ Tema 1.396; STF
Tema 987 — `context/jurisprudencia-sumulas-temas.md`, `context/jec-fonaje-e-
recursos.md`.

## Do JEC — reforço de T7 (tratamento completo em outra skill)
**Reclamação ao STJ contra Turma Recursal NÃO cabe mais desde 2016** (Resolução STJ
3/2016, 07/04/2016, que revogou a Resolução 12/2009 e transferiu a competência para
as Câmaras Reunidas/Seção Especializada do próprio TJ). Do JEC, especificamente:
**REsp não cabe** (Súmula 203/STJ — Turma Recursal não é "Tribunal" para o art. 105,
III da CF); **RE cabe** (Súmula 640/STF), e a Turma Recursal não pode reter o agravo
contra a inadmissão do RE (Súmula 727/STF). **O detalhamento completo dessa via está
em `o-que-sobe-do-jec` — não duplicar aqui.** Esta skill trata do cabimento quando a
origem já não é Turma Recursal, e sim acórdão de Tribunal em rito comum.

## Cabimento a partir de rito comum
**REsp:** cabível quando o acórdão de TJ/TRF nega vigência a lei federal (CDC, CC) ou
diverge de outro tribunal na interpretação da mesma norma federal. **RE:** cabível
quando há questão constitucional com repercussão geral. **Prequestionamento:** a
matéria federal/constitucional precisa ter sido efetivamente debatida e decidida no
acórdão recorrido — se omissa, cabem embargos de declaração antes do recurso
excepcional (ver `embargos-e-incidentes-consumo`). A vedação sumular ao reexame de
prova/matéria fática em recurso excepcional é aplicada por analogia pelo STJ ao
revisar quantum de dano moral (ver `apelacao-consumo-rito-comum`) — o número exato da
súmula processual de admissibilidade não está confirmado nos anexos deste plugin,
`[VERIFICAR — não confirmado no corpus]` antes de citar em petição.

## Distinguishing e superação de tema repetitivo/vinculante — exemplos verificados
- **Tema 929/STJ (repetição em dobro, CDC art. 42, parágrafo único):** tese firmada
  dispensa má-fé, **mas com modulação temporal** — só se aplica a cobranças a partir
  de 30/03/2021. Exemplo de distinguishing por data do fato: cobrança de 2019 segue o
  regime antigo (exige má-fé).
- **Tema 1.404/STJ (comercialização de dados pessoais não sensíveis):** afetado em
  janeiro/2026, **ainda sem julgamento de mérito** — não invocar como tese pacífica.
- **Tema 1.396/STJ (interesse de agir e tentativa extrajudicial prévia):** também
  afetado e pendente — cross-link, tratamento completo em
  `consumidor-gov-br-e-pre-processual`.
- **Tema 987/STF (responsabilidade de plataforma/marketplace):** julgamento
  concluído em 17/06/2026 (pós-embargos) — quem cita a versão de mérito de 27/06/2025
  está usando tese superada; cross-link, tratamento completo em
  `marketplace-e-plataforma`.

## Tese do consumidor
Sustentar o prequestionamento explícito na apelação (para não depender de embargos
de declaração depois); ao invocar tema repetitivo favorável, checar a data de corte
de eventual modulação (como no Tema 929) antes de aplicá-lo ao caso concreto.

## Tese do fornecedor
Arguir ausência de prequestionamento quando a matéria federal não foi decidida no
acórdão; distinguishing de tema repetitivo desfavorável sempre que o caso concreto
não se enquadrar exatamente na tese fixada (datas, modalidade contratual, tipo de
dado); nunca aplicar tema **afetado e pendente** (1.404, 1.396) como se já fosse
tese vinculante — é munição para a parte contrária alegar prematuridade.

## Armadilhas
- **T7 — reforço:** reclamação ao STJ contra Turma Recursal não existe mais desde
  2016; do JEC, REsp não cabe e RE cabe.
- Não tratar tema repetitivo **afetado** (ainda sem julgamento) como pacificado.
- Não aplicar retroativamente tese modulada (Tema 929) a fato anterior ao marco.

## Fronteira
Cabimento a partir de decisão de Turma Recursal do JEC (mecânica completa) →
`o-que-sobe-do-jec`. **Requisito de relevância da Lei 15.484 para admissibilidade do
REsp → `resp-re-os`** (não coberto por este plugin — aponto, não duplico). Embargos
de declaração para prequestionar → `embargos-e-incidentes-consumo`.

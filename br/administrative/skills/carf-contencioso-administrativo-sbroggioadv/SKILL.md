---
name: carf-contencioso-administrativo-sbroggioadv
title: carf-contencioso-administrativo — o rito federal antes da inscrição
description: 'O rito do Decreto 70.235/72 pela ótica de quem representa a Fazenda Nacional: auto de infração, impugnação que instaura a fase litigiosa, julgamento em primeira instância nas Delegacias da Receita Federal de Julgamento, recurso voluntário e de ofício ao CARF e recurso especial à Câmara Superior. Duas travas dominam a skill. TV6 — o voto de qualidade do art. 25 §9º está vigente e foi para ele que a Lei 14.689/2023 escreveu as consequências (§9º-A exclui multas e cancela a representação fiscal para fins penais; art. 25-A afasta juros de mora com pagamento em 90 dias); citar a regra do desempate pró-contribuinte como vigente é erro. E a defasagem de prazos: a Lei Complementar 227/2026 reescreveu impugnação e recurso voluntário para 20 dias úteis, criou a suspensão de 20/12 a 20/01 e deu 10 dias úteis ao recurso especial da CBS. Aciona: "prazo de impugnação no PAF", "recurso voluntário CARF", "recurso especial à CSRF", "voto de qualidade", "empate no CARF", "processo administrativo
  fiscal federal".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-federal-os-marketplace/tree/main/procurador-federal-os/skills/carf-contencioso-administrativo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# carf-contencioso-administrativo — o rito federal antes da inscrição

O contencioso administrativo fiscal é onde o crédito da União se define antes de virar título — e é
a fase cujos prazos mais mudaram recentemente. Texto verbatim em
`context/carf-processo-administrativo.md`; nada aqui sai de memória. Este produto atende a **União**.

> **Como ler o anexo.** É texto consolidado: cada dispositivo aparece com a redação vigente, e o
> revogado sai marcado como `[dispositivo revogado — omitido]`. Leia a redação que sobrou, nunca a
> lembrança da antiga. O anexo quebra linhas no meio de expressões — "voto de / qualidade" —, então
> grep de conferência vai com **espaço normalizado** (trava TV8).

## Quando esta skill entra

- Ao contar prazo de impugnação, de recurso voluntário ou de recurso especial no PAF.
- Quando o julgamento empata e a pergunta é o que acontece com multa, representação penal e juros.
- Ao decidir se a matéria comporta recurso especial à Câmara Superior.
- Antes de encaminhar o crédito definitivo para inscrição em dívida ativa.

## 1. Os prazos — o que a LC 227/2026 mudou (defasagem)

Esta é a parte da skill em que citar de memória erra por design. As redações vigentes no anexo:

| Ato | Prazo vigente | Dispositivo |
|---|---|---|
| Intimação, no auto de infração, para cumprir ou impugnar | **20 (vinte) dias úteis** | art. 10, V (redação da LC 227/2026) |
| Impugnação ao órgão preparador, contada da intimação da exigência | **20 (vinte) dias úteis** | art. 15 (redação da LC 227/2026) |
| Recurso voluntário, contado da ciência da decisão | **20 (vinte) dias úteis**, com efeito suspensivo, total ou parcial | art. 33 (redação da LC 227/2026) |
| Recurso especial à Câmara Superior | **15 (quinze) dias** da ciência do acórdão | art. 37, §2º (redação da Lei 11.941/2009) |
| Recurso especial na **CBS** — **só** quanto à legislação específica dela | **10 (dez) dias úteis** | art. 37, §5º (LC 227/2026) |
| Ato sem prazo expresso no Decreto, do sujeito passivo ou da Fazenda | **10 (dez) dias úteis** | art. 5º-B (incluído pela LC 227/2026) |

**Contagem — art. 5º, na redação da LC 227/2026:** na contagem dos prazos previstos no Decreto,
**I** serão considerados os **dias corridos, salvo se houver disposição em contrário**; e **II**
será excluído da contagem o dia do início e incluído o dia do vencimento. O parágrafo único mantém
que os prazos só se iniciam ou vencem em dia de expediente normal no órgão.

Leia os dois juntos: a regra geral é dia corrido, mas os prazos da tabela estão em **dias úteis por
disposição expressa** — são a "disposição em contrário" do inciso I. Misturar as duas contagens é o
erro que perde recurso.

**Suspensão de fim de ano — art. 5º-A (incluído pela LC 227/2026):** "Suspende-se o curso do prazo
processual nos dias compreendidos entre 20 de dezembro e 20 de janeiro, inclusive." O parágrafo
único acrescenta que nesse período não são realizadas sessões de julgamento no órgão do inciso II
do art. 25 — o CARF.

## 2. Da autuação à fase litigiosa

**Art. 10** — o auto de infração conterá obrigatoriamente: **I** qualificação do autuado; **II**
local, data e hora da lavratura; **III** descrição do fato; **IV** disposição legal infringida e
penalidade aplicável; **V** a determinação da exigência e a intimação para cumpri-la ou impugná-la
no prazo de 20 dias úteis; **VI** assinatura do autuante, com cargo ou função e número de
matrícula.

**Art. 14:** "A impugnação da exigência instaura a fase litigiosa do procedimento." Antes dela há
procedimento; a partir dela há litígio.

**Art. 16** — a impugnação mencionará: **I** a autoridade julgadora a quem é dirigida; **II** a
qualificação do impugnante; **III** os motivos de fato e de direito, os pontos de discordância e as
razões e provas que possuir; **IV** as diligências ou perícias pretendidas, com os motivos que as
justifiquem.

**Art. 17** — considera-se **não impugnada** a matéria que não tenha sido expressamente contestada
pelo impugnante. Para o procurador, é o dispositivo que delimita o que ainda está em disputa: o que
o contribuinte não atacou não volta depois.

**Art. 7º, §2º (redação da LC 227/2026):** os atos que iniciam o procedimento fiscal valem por
**90 (noventa) dias**, prorrogáveis sucessivamente por igual período com qualquer outro ato escrito
que indique o prosseguimento dos trabalhos — é o prazo que sustenta a exclusão da espontaneidade do
§1º.

## 3. Quem julga — as duas instâncias

**Art. 25, I** — em primeira instância, às **Delegacias da Receita Federal de Julgamento**, órgãos
de deliberação interna e natureza colegiada da Secretaria da Receita Federal.

**Art. 25, II** (redação da Lei 11.941/2009) — em segunda instância, ao **Conselho Administrativo
de Recursos Fiscais**, órgão colegiado, paritário, integrante da estrutura do Ministério da
Fazenda, com atribuição de julgar recursos de ofício e voluntários de decisão de primeira instância,
bem como recursos de natureza especial. **§1º:** o CARF é constituído por **seções** e pela
**Câmara Superior de Recursos Fiscais**.

Da decisão de primeira instância cabe **recurso voluntário** (art. 33) e, nas hipóteses do art. 34,
**recurso de ofício** da autoridade julgadora. À Câmara Superior cabe o **recurso especial**
(art. 37, §2º), na hipótese do **inciso II** — decisão que der à lei tributária interpretação
divergente da que lhe tenha dado outra Câmara, turma de Câmara, turma especial ou a própria CSRF. O
inciso I do §2º consta do anexo como **(VETADO)**: recurso especial por contrariedade à lei ou à
evidência da prova não é hipótese vigente, e sustentá-lo é perder o recurso na admissibilidade.

## 4. ⚠️ TV6 — o voto de qualidade, e o que ele custa hoje

**Art. 25, §9º** (redação vigente no anexo): "Os cargos de Presidente das Turmas da Câmara Superior
de Recursos Fiscais, das câmaras, das suas turmas e das turmas especiais serão ocupados por
conselheiros representantes da Fazenda Nacional, que, **em caso de empate, terão o voto de
qualidade**, e os cargos de Vice-Presidente, por representantes dos contribuintes."

A **Lei 14.689/2023** escreveu, no próprio Decreto, as consequências desse desempate — e cada um
desses dispositivos trata o §9º como regra em vigor:

| Dispositivo | O que estabelece |
|---|---|
| **§9º-A** (Lei 14.689/2023) | Resolvido o processo favoravelmente à Fazenda **pelo voto de qualidade do §9º**, ficam **excluídas as multas** e **cancelada a representação fiscal para fins penais** de que trata o art. 83 da Lei 9.430/96 |
| **§12** (Lei 14.689/2023) | Assegurada ao procurador do sujeito passivo a **sustentação oral** nos julgamentos dos colegiados dos incisos I e II |
| **§13** (Lei 14.689/2023) | Os órgãos julgadores **observarão as súmulas** de jurisprudência publicadas pelo CARF |
| **art. 25-A** (Lei 14.689/2023) | Decidido a favor da Fazenda pelo voto de qualidade, com manifestação do contribuinte para pagamento em **90 dias**, ficam **excluídos os juros de mora** do art. 13 da Lei 9.065/95 até o acordo; até **12 parcelas** (§1º), admitido prejuízo fiscal e base negativa de CSLL (§3º) e **precatórios** na forma do art. 100, §11, da Constituição (§10) |
| **art. 25-A, §8º** | Sem opção pelo pagamento, os créditos definitivos vão a **inscrição em dívida ativa da União em até 90 dias**, **sem** o encargo do art. 1º do DL 1.025/69 e aplicado o §9º-A |

**A leitura que o procurador precisa fazer:** ganhar por voto de qualidade **não é ganhar inteiro**.
O crédito sobrevive, mas sem a multa e sem a representação penal, e com juros afastáveis se o
contribuinte pagar em 90 dias. Isso muda a conta de levar a tese ao empate — e é informação que o
parecer dá antes, não depois.

**O contraste histórico, com lastro:** o art. 28 da Lei 13.988/2020 acrescentou à Lei 10.522/2002 o
art. 19-E, pelo qual, em caso de empate, "não se aplica o voto de qualidade a que se refere o § 9º
do art. 25 do Decreto nº 70.235", resolvendo-se favoravelmente ao contribuinte — texto em
`context/transacao-lei-13988.md`. É a regra **anterior**, que TV6 proíbe apresentar como vigente. O
ato de revogação expressa desse art. 19-E não consta dos anexos → `[VERIFICAR]` na Lei
14.689/2023 antes de descrever a mecânica da revogação em peça.

## Travas desta skill

- **TV6 (a desta skill).** O desempate vigente é o **voto de qualidade** do art. 25 §9º, com as
  consequências do §9º-A e do art. 25-A. Nenhuma frase apresenta o desempate pró-contribuinte como
  regra atual; e nenhuma omite que a vitória por qualidade vem sem multa e sem representação penal.
- **P2 — nada sem lastro.** Todo dispositivo aqui está em `context/carf-processo-administrativo.md`
  (ou, no contraste do art. 19-E, em `context/transacao-lei-13988.md`). Regimento Interno do CARF,
  número de súmula do Conselho e portaria da Receita não estão nos anexos → `[VERIFICAR]`.
- **P1 — esfera.** Contencioso administrativo **federal**. Processo administrativo tributário de
  Estado ou de Município não entra: é dos irmãos `procurador-estadual-os` e
  `procurador-municipal-os`.
- **P7 — prazo próprio.** O Decreto 70.235/72 fixa prazos próprios; o art. 5º define a contagem
  dentro dele. Não se transporta para cá o prazo em dobro do CPC 183 sem a checagem do §2º em
  `prerrogativas-processuais`.
- **P4 — conformidade.** Contagem e tese aqui são estudo; conferência nos autos e protocolo são do
  procurador (Portaria AGU nº 226/2026 — `context/governanca-ia-procuradorias.md`).

**Próximo passo:** crédito definitivo → `pgfn-divida-ativa-uniao`. Composição em vez de litígio →
`transacao-tributaria-federal`. Atribuição na matéria → `pgu-e-estrutura-da-agu`. Fecha por
`suprema-corte-fazendaria`.

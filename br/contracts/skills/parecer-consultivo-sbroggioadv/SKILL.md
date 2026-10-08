---
name: parecer-consultivo-sbroggioadv
title: parecer-consultivo — o parecer que a autoridade usa para decidir
description: 'O parecer da procuradoria do Estado, com a LINDB como espinha dorsal — arts. 20 a 30 verbatim no anexo, cada um com uma função que o parecer não pode embaralhar: 20 e 21 (consequencialismo e consequências da invalidação), 22 (obstáculos reais do gestor), 23 (regime de transição), 24 (o ato consumado se julga pela orientação geral da época), 26 (compromisso após oitiva do órgão jurídico), 28 (a responsabilidade pessoal do agente é por dolo ou erro grosseiro) e 30 (súmula administrativa com efeito vinculante interno, que conecta ao CPC 496 §4º IV). Entrega a estrutura em sete blocos, a régua da responsabilidade do parecerista — com a distinção entre parecer vinculante e opinativo marcada [VERIFICAR], porque o anexo não a fecha — e a regra que define a peça: o parecer opina, a autoridade decide. Trava dura contra os cinco dispositivos VETADOS do recorte. Aciona: "preciso de um parecer", "consulta da secretaria", "posso convalidar este ato?", "o parecerista responde por isso?",
  "minuta de parecer".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/parecer-consultivo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# parecer-consultivo — o parecer que a autoridade usa para decidir

Este produto atende o **Estado**. O consultivo é a parte do trabalho que evita o contencioso —
e é a que mais expõe pessoalmente quem assina. Esta skill monta o parecer e fixa a régua da
responsabilidade de quem o escreve.

## A regra que define a peça

> **O parecer opina; a autoridade decide.** Um parecer não determina, não autoriza e não homologa:
> ele analisa a consulta, aponta o direito aplicável, expõe riscos e alternativas e conclui. A
> decisão administrativa — e a responsabilidade pelo ato — permanecem com a autoridade competente.

Parecer redigido no imperativo ("proceda-se", "fica autorizado") desloca para a procuradoria uma
decisão que não é dela e transforma o parecerista em gestor. Escreva no registro opinativo:
*"opina-se pela viabilidade jurídica, observadas as ressalvas dos itens X e Y"*.

## Quando esta skill entra

- Chegou consulta formal de órgão, secretaria ou autoridade do Estado.
- É preciso analisar a juridicidade de ato, contrato, convênio, minuta ou procedimento.
- A casa vai firmar orientação sobre matéria repetida (aí ver também `acoes-de-massa`).
- Alguém pergunta se o parecerista responde pessoalmente pelo que assinou.

## A LINDB, artigo por função (o que tem lastro verbatim)

Fonte: `context/lindb-20-30.md`. **Não embaralhe as funções** — cada artigo resolve uma pergunta
diferente, e usar o errado enfraquece a conclusão.

| Pergunta do caso | Artigo | O que ele dá ao parecer |
|---|---|---|
| O ato antigo era válido? | **24** | O ato já consumado se julga pelas **orientações gerais da época**; é **vedado** declarar inválidas situações plenamente constituídas com base em mudança posterior de orientação. O parágrafo único define o que conta como orientação geral: ato público de caráter geral, jurisprudência judicial ou administrativa majoritária, **ou prática administrativa reiterada e de amplo conhecimento público** |
| A orientação vai mudar? | **23** | Decisão que estabelece interpretação nova impondo novo dever **deverá prever regime de transição** quando indispensável |
| Vão invalidar sem medir o efeito? | **20 e 21** | Não se decide por **valores jurídicos abstratos** sem considerar as **consequências práticas**; a motivação demonstra necessidade e adequação **inclusive em face das possíveis alternativas** (20, par. único); a decisão que invalida **deverá indicar de modo expresso** suas consequências jurídicas e administrativas (21) |
| O gestor tinha condições reais? | **22** | Consideram-se **os obstáculos e as dificuldades reais do gestor** e as exigências das políticas a seu cargo, *sem prejuízo dos direitos dos administrados*; §2º: na sanção, natureza e gravidade da infração, danos, agravantes, atenuantes e antecedentes |
| Dá para encerrar a incerteza sem litígio? | **26** | A autoridade **poderá celebrar compromisso** com os interessados **após oitiva do órgão jurídico** — a própria procuradoria — e só produz efeitos com a **publicação oficial**. O §1º fixa o conteúdo: solução proporcional e eficiente (I); **não pode desonerar permanentemente** dever reconhecido por orientação geral (III); deve prever com clareza obrigações, prazo e sanções (IV) |
| Quem responde pelo que se decidiu? | **28** | O agente público responde **pessoalmente** por suas decisões ou opiniões técnicas **em caso de dolo ou erro grosseiro** |
| Como fixar isso para o futuro? | **30** | Dever de aumentar a segurança jurídica por regulamentos, **súmulas administrativas** e respostas a consultas; o parágrafo único lhes dá **caráter vinculante** perante o órgão, **até ulterior revisão** |

⚠️ **Trava dos vetos — erro de fonte, não de interpretação.** Cinco dispositivos deste recorte foram
**VETADOS** e **não têm texto**: art. 23 parágrafo único · art. 25 · art. 26 §1º II e §2º · art. 28
§§1º a 3º · art. 29 §2º. **Nunca cite conteúdo deles.** É especialmente tentador no art. 28, cujos
parágrafos vetados detalhariam o regime de responsabilidade — eles não existem.

## A estrutura do parecer — sete blocos

1. **Identificação e consulta** — órgão consulente, processo administrativo, data e **o quesito tal
   como formulado**. Se a consulta veio genérica ("analisar a legalidade"), **delimite o quesito
   antes de responder**: parecer que responde pergunta que ninguém fez é o que depois é citado fora
   de contexto.
2. **Fatos relevantes** — o que consta dos autos administrativos, com referência à folha. Fato que
   não está no processo não entra no parecer; se é indispensável, **peça a instrução**.
3. **Direito aplicável** — normas incidentes, com lastro. Fora dos anexos → `[VERIFICAR]` (P2).
4. **Análise** — subsunção, alternativas, e o que a LINDB manda considerar: consequências práticas
   (20), condições reais do gestor (22), orientação geral da época se o ato é pretérito (24).
5. **Riscos** — o que pode ser questionado, por quem, com que consequência. Parecer que só diz "pode"
   não protege ninguém.
6. **Conclusão e ressalvas** — opinativa, numerada, com as condicionantes explícitas. **A ressalva é
   a parte mais importante do parecer** e é a que costuma sumir na versão resumida.
7. **Encaminhamento** — a quem cabe decidir, e o que ainda falta instruir.

## Responsabilidade do parecerista

**Com lastro:** o **art. 28 da LINDB** fixa o padrão de imputação — o agente responde pessoalmente
por decisões **ou opiniões técnicas** em caso de **dolo ou erro grosseiro**. "Opiniões técnicas"
alcança o parecer; e o padrão **não** é divergência de interpretação nem erro simples.

⚠️ **`[VERIFICAR]` — a distinção entre parecer vinculante e opinativo não está fechada nos anexos.**
A tese corrente separa o parecer meramente **opinativo** (a autoridade decide livremente, e a
responsabilização do parecerista é excepcional) do parecer **vinculante ou obrigatório por lei** (em
que a manifestação integra o ato e o regime de responsabilidade é discutido em outros termos). O
**precedente que consolidou essa distinção não consta do `context/`**: conferir na fonte primária
antes de citá-lo — e **jamais** afirmar em parecer que "o parecerista não responde" com base em
precedente lembrado de cor. É exatamente o tipo de afirmação que o comprador confere.

Conduta segura, que independe da distinção: **fundamentar**, **explicitar ressalvas**, **registrar
alternativas consideradas** e **não decidir no lugar da autoridade**. As quatro reduzem exposição em
qualquer regime.

## O efeito processual do consultivo bem-feito

**CPC art. 496 §4º IV** (`context/prerrogativas-cpc.md`, verbatim): dispensa-se a remessa necessária
quando a sentença coincidir com *"orientação vinculante firmada no âmbito administrativo do próprio
ente público, consolidada em manifestação, parecer ou súmula administrativa"*. Somado ao **art. 30,
parágrafo único**, da LINDB, isso significa: **parecer e súmula administrativa do ente produzem
efeito processual direto**. Consultivo, aqui, não é área-meio — é redução de contencioso mensurável.

## Travas desta skill

- **P2** — toda norma citada tem lastro no `context/` ou sai `[VERIFICAR]`. Com lastro: LINDB arts.
  20-30 (verbatim, respeitados os vetos) e CPC 496 §4º IV. **Lei 14.133/2021** existe como norma de
  licitações e contratos, mas seus dispositivos **não** estão nos anexos — ver
  `convenios-e-licitacoes-consultivo`.
- **Vetos** — art. 23 par. único, art. 25, art. 26 §1º II e §2º, art. 28 §§1º-3º e art. 29 §2º não
  têm texto; citar conteúdo deles reprova no `suprema-corte-fazendaria`.
- **P5** — parecer sobre honorários do procurador, regime de servidores ou lei orgânica **exige a lei
  do ente**; sem ela, o parecer pergunta ou marca, nunca aplica por analogia o regime de outro ente.
- **P1** — parecer sobre tributo trata de **ICMS, IPVA, ITCMD e demais créditos estaduais**; matéria de outra esfera não entra.
- **P6** — parecer que toque **ICMS** (único tributo da esfera que a reforma extingue) fecha com o aviso da transição (horizonte, não invalidade).
- **P3** — tese sustentada em parecer passa pelo `suprema-corte-fazendaria`: parecer que firma
  orientação já superada replica o erro por todo o órgão, com efeito vinculante interno.
- **P4** — o parecer sai completo, com revisão humana obrigatória e responsabilidade indelegável de
  quem assina; dado sigiloso do processo administrativo fica local e mascarado.

## Cross-links

`lindb-como-metodo` (a base verbatim) · `convenios-e-licitacoes-consultivo` (a consulta mais
frequente) · `improbidade-defesa-e-autoria` (a ponte: LINDB 22 e 28 na defesa do gestor) ·
`acoes-de-massa` (súmula administrativa como instrumento de volume) · `desapropriacao` (parecer da
declaração de utilidade pública) · `prerrogativas-processuais` (o efeito no CPC 496 §4º IV) ·
`conformidade-ia-institucional` (o parecer sai do gabinete) · `suprema-corte-fazendaria` (**QA
obrigatória no fecho**) · `estilo-e-fronteiras`.
Fora da casa: `licitacoes-adv-os` (a ótica do licitante, nunca duplicada aqui) ·
`tributario-societario-adv-os` (o contribuinte do outro lado) · `juris-adv-os`.

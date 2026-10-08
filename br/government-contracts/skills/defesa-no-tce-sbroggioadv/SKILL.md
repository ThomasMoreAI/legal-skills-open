---
name: defesa-no-tce-sbroggioadv
title: defesa-no-tce — o rito é de cada tribunal, o argumento é da LINDB
description: 'A defesa do Município e do gestor perante o tribunal de contas competente — o TCE ou, onde houver, o Tribunal de Contas dos Municípios — com a trava que vale mais que qualquer modelo: o rito varia por tribunal, cada um tem regimento próprio, e por isso nenhum prazo é escrito de memória: entra como VERIFICAR PRAZO até ser lido naquele regimento. Cobre a distinção que decide a competência antes de qualquer defesa, entre contas de governo, que recebem parecer prévio e são julgadas pela Câmara, e contas de gestão, julgadas pelo próprio tribunal; a tomada de contas especial e o que a defesa precisa atacar nela; e o arsenal que tem lastro neste produto e é o mais forte do procurador nessa arena — os artigos 20 a 30 da LINDB, com o consequencialismo do 20, os obstáculos reais do gestor do 22, a orientação da época do 24 e o dolo ou erro grosseiro do 28. Aciona: "TCE", "tribunal de contas", "prestação de contas", "tomada de contas especial", "parecer prévio", "defesa do prefeito nas
  contas", "citação do TCE".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-municipal-os-marketplace/tree/main/procurador-municipal-os/skills/defesa-no-tce
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: government-contracts
language: pt
---

# defesa-no-tce — o rito é de cada tribunal, o argumento é da LINDB

Defesa em tribunal de contas erra por dois caminhos opostos. Um é procedimental: aplicar o rito de um
TCE em outro, porque "é tudo parecido" — e perder prazo ou recurso que não existe naquele regimento. O
outro é de mérito: discutir a irregularidade **como se fosse contabilidade**, quando o que decide o
resultado é a **imputação de responsabilidade** ao gestor. Esta skill trata dos dois.

Este produto atende o **Município**.

> ### ⚠️ Antes da trava: **qual** tribunal julga este Município?
>
> "TCE" é o caso comum, não o único: em alguns Estados e capitais as contas municipais são julgadas
> por um **Tribunal de Contas dos Municípios (TCM)**, órgão distinto, com lei orgânica, regimento e
> prazos próprios. A norma constitucional que organiza os tribunais de contas dos Estados e
> Municípios — e que estende a eles as regras da seção do TCU — **não é anexo deste produto** →
> `[VERIFICAR]` o dispositivo **e** a competência antes de qualquer peça. Ela explica *por que* os
> regimentos se parecem; é por serem apenas parecidos que não se copiam. Onde se lê "TCE" abaixo,
> leia "o tribunal de contas competente".
>
> ### ⚠️ A trava desta skill: nenhum prazo hardcodado
>
> **Cada tribunal de contas tem regimento interno próprio**, e é ele que fixa prazos de defesa, de
> recurso, de sustentação e de embargos. Este produto **nunca escreve um prazo de memória**: cada um
> aparece como **`[VERIFICAR PRAZO]`**, com a indicação de onde lê-lo — a lei orgânica e o regimento
> **daquele** tribunal. Prazo aqui é preclusivo; errar por analogia custa a defesa inteira.

## Quando esta skill entra

- Quando chega citação, notificação ou audiência do TCE ao Município ou ao gestor.
- Na prestação de contas anual e na resposta a apontamentos da instrução.
- Em tomada de contas especial, desde a instauração.
- Quando o acórdão do TCE imputa débito ou aplica multa, e se avalia recurso ou via judicial.

## 1. Antes da defesa: que contas são estas?

A primeira pergunta não é "o que respondemos?", é **"quem julga?"** — porque a resposta muda o
destinatário, o efeito e a estratégia.

| | **Contas de governo** | **Contas de gestão** |
|---|---|---|
| Objeto | O exercício financeiro do Executivo como um todo — execução orçamentária, metas, limites | Atos concretos de ordenação de despesa, licitação, convênio, pagamento |
| Papel do TCE | Emite **parecer prévio** | **Julga** |
| Quem decide | A **Câmara Municipal**, que pode ou não seguir o parecer, por quórum qualificado | O próprio **tribunal**, por acórdão |
| Efeito típico | Político-institucional | Imputação de **débito** e **multa**, com título |

Base a conferir: os dispositivos constitucionais da fiscalização municipal (parecer prévio, quórum da
Câmara) e o entendimento dos tribunais superiores sobre a competência quando o Prefeito atua como
**ordenador de despesa** `[VERIFICAR]` — o número do tema e a tese, na fonte. O produto conhece a
distinção; não escreve o precedente de memória.

**Por que isso é a primeira pergunta:** defesa endereçada ao órgão errado, ou que trata parecer
prévio como se fosse título executivo, começa perdendo. E a natureza das contas define se o resultado
gera **título** — o que puxa a discussão para a execução e para a via judicial.

## 2. Tomada de contas especial — o que a defesa ataca

A tomada de contas especial (**TCE especial** — a sigla aqui não é a do tribunal) apura dano ao
erário e identifica responsáveis. A defesa útil não começa pelo número: começa pela **cadeia**.

| Frente | O que verificar | Efeito se procede |
|---|---|---|
| **Regularidade da instauração** | Houve a fase interna prévia? Quem instaurou tinha competência? | Nulidade ou refazimento |
| **Contraditório e ampla defesa** | Citação válida, acesso integral aos autos, prazo efetivo para manifestação | Nulidade a partir do vício |
| **Nexo entre conduta e dano** | O responsável apontado praticou ou determinou o ato? | Exclusão da responsabilidade |
| **Existência e quantificação do dano** | O dano é certo, ou é presumido de irregularidade formal? | Afasta ou reduz o débito |
| **Prescrição** | Marco inicial e prazo, na norma **daquele** tribunal e na legislação aplicável `[VERIFICAR]` | Extinção |
| **Elemento subjetivo** | Houve dolo ou **erro grosseiro**? (art. 28 da LINDB — §3 desta skill) | Afasta a responsabilidade pessoal |

Irregularidade formal **não é** dano automático. Confundir as duas é o que transforma falha de
procedimento em imputação de débito — e é o ponto onde a LINDB trabalha melhor.

## 3. O arsenal com lastro: LINDB, arts. 20 a 30

Este é o único bloco desta skill que **não** depende de conferência: está em
`context/lindb-20-30.md`, verbatim. E é o mais forte que o procurador tem no controle externo.

- **Art. 20** — "não se decidirá com base em valores jurídicos abstratos sem que sejam consideradas
  as **consequências práticas** da decisão". Contra apontamento fundado em princípio genérico, exige
  que o tribunal desça ao efeito concreto.
- **Art. 21** — a decisão que **invalidar** ato, contrato, ajuste, processo ou norma administrativa
  "deverá indicar de modo expresso suas **consequências jurídicas e administrativas**".
- **Art. 22** — na interpretação de normas de gestão pública, "serão considerados os **obstáculos e
  as dificuldades reais do gestor** e as exigências das políticas públicas a seu cargo". O **§1º**
  manda considerar "as circunstâncias práticas que houverem imposto, limitado ou condicionado a ação
  do agente"; o **§2º**, na aplicação de **sanções**, a natureza e gravidade da infração, os danos, as
  agravantes e atenuantes e os antecedentes; o **§3º** manda levar em conta as sanções já aplicadas
  ao agente na dosimetria das demais de mesma natureza pelo mesmo fato.
- **Art. 23** — orientação **nova** que imponha novo dever exige **regime de transição** quando
  indispensável. É a resposta a apontamento que aplica critério novo a exercício antigo.
- **Art. 24** — a revisão de ato **já consumado** "levará em conta as **orientações gerais da
  época**", vedado invalidar situações plenamente constituídas com base em mudança posterior de
  orientação. O parágrafo único define orientações gerais como as interpretações em atos públicos
  gerais, na **jurisprudência majoritária** e na "prática administrativa reiterada e de amplo
  conhecimento público".
- **Art. 26** — permite à autoridade celebrar **compromisso** com os interessados para eliminar
  irregularidade, incerteza jurídica ou situação contenciosa, ouvido o órgão jurídico.
- **Art. 28** — "O agente público responderá pessoalmente por suas decisões ou opiniões técnicas em
  caso de **dolo ou erro grosseiro**." É o dispositivo central da defesa pessoal do gestor: erro
  administrativo comum, sem dolo e sem grosseria, **não** gera responsabilidade pessoal.
- **Art. 30** — as autoridades devem atuar para aumentar a segurança jurídica, inclusive por
  regulamentos, **súmulas administrativas** e respostas a consultas — e o parágrafo único dá a essas
  manifestações caráter vinculante em relação ao órgão até ulterior revisão.

Os arts. **22, 24 e 28** juntos formam a linha mais eficaz: **o gestor decidiu na realidade que
tinha, segundo a orientação da época, sem dolo nem erro grosseiro.** Método completo em
`lindb-como-metodo`; a mesma cadeia sustenta a defesa em `improbidade-defesa-e-autoria`, e as duas
frentes costumam correr sobre o mesmo fato.

## 4. A régua de entrada de qualquer defesa no TCE

1. **Qual tribunal** — TCE ou TCM? — e qual a lei orgânica e o regimento vigentes. `[VERIFICAR]`
2. **Que peça é esta** — citação, audiência, notificação, diligência? Cada uma tem efeito próprio.
3. **Prazo** — lido no regimento daquele tribunal. `[VERIFICAR PRAZO]`
4. **Contas de governo ou de gestão** (§1 desta skill) — quem julga.
5. **Quem é o defendido** — o Município, o gestor, ou os dois? Se houver conflito de interesse entre
   ente e agente, ele é declarado antes, não descoberto depois.
6. **Elemento subjetivo e nexo** — a linha do art. 28 se aplica?
7. **Recursos disponíveis** naquele regimento, com prazos. `[VERIFICAR PRAZO]`

## Travas desta skill

- **Rito por tribunal (a trava desta skill).** Primeiro a **competência** (TCE ou TCM →
  `[VERIFICAR]`); depois o rito, sem prazo de memória: `[VERIFICAR PRAZO]` no regimento **daquele**
  tribunal. Copiar o rito de outro é o erro mais caro desta arena.
- **P2.** A LINDB está no anexo e vai citada. Dispositivo constitucional, tema de repercussão geral,
  norma de tribunal de contas e prazo **não** estão → `[VERIFICAR]`.
- **P5.** Lei orgânica do Município, estrutura de controle interno e atribuições da procuradoria são
  do ente. Sem o texto local, o produto pergunta.
- **P3.** Se o apontamento procede, a linha honesta é reduzir o alcance — atacar dano, nexo e
  dosimetria — não sustentar regularidade integral contra a prova.
- **P4.** Análise e minuta são estudo; a defesa, a assinatura e a decisão de recorrer são do
  procurador, indelegáveis. Documento de contas é dado do órgão e fica local.
- **P1.** Contas do **Município**. Controle sobre outras esferas é dos irmãos.

**Próximo passo:** mesmo fato em ação de improbidade → `improbidade-defesa-e-autoria`. Parecer que
antecipa o apontamento → `parecer-consultivo` com `lindb-como-metodo`. Convênio ou contrato na origem
do dano → `convenios-e-licitacoes-consultivo`. Débito imputado e cobrado → `divida-ativa-municipal`.
Toda entrega fecha por `suprema-corte-fazendaria`.

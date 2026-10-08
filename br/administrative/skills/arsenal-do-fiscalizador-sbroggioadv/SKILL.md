---
name: arsenal-do-fiscalizador-sbroggioadv
title: Arsenal do fiscalizador — os 6 instrumentos do cidadão
description: 'Os 6 instrumentos com que qualquer pessoa fiscaliza ato público SEM advogado — direito de petição (CF 5º XXXIV), pedido LAI (Lei 12.527), ação popular (Lei 4.717), denúncia ao TCU/TCE (CF 74 §2º), impugnação de edital (Lei 14.133 art. 164) e representação por improbidade (Lei 8.429 art. 14). Cada um com a base legal literal do corpus, quem tem legitimidade e o prazo. Separa o que o leigo protocola sozinho do que exige advogado (ação popular vira dossiê roteado). Apartidável: fiscaliza o ato, nunca o lado. Aciona: quando o usuário pergunta "o que eu posso fazer", "com o que eu denuncio isso", "qual instrumento eu uso" contra um ato público, ou quando o opositor-master precisa escolher a peça certa para um vício já identificado.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/opositor-os-marketplace/tree/main/opositor-os/skills/arsenal-do-fiscalizador
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# Arsenal do fiscalizador — os 6 instrumentos do cidadão

Seis instrumentos dão a **qualquer pessoa** o poder de fiscalizar o poder público — sem OAB, sem
custas na maioria deles. Esta skill diz **o que cada um faz, quem pode usar e o prazo**. A escolha
do instrumento certo é o começo do roteamento (o produto todo). O opositor fiscaliza **o ato**,
não a gestão nem o partido.

## Quando esta skill entra

- O usuário pergunta "o que eu faço com isso", "como eu denuncio", "qual o caminho".
- O `opositor-master` já tem um vício com lastro e precisa casar o **instrumento** ao caso.
- Antes de qualquer geração de peça — para confirmar que existe instrumento de **leigo** para aquele
  ato (senão, vira dossiê roteado a advogado).

## Os 6 instrumentos (base verbatim no `context/`)

| # | Instrumento | Base legal | O que faz | Legitimidade | Prazo |
|---|---|---|---|---|---|
| 1 | **Direito de petição / certidão** | CF art. 5º, XXXIV, "a" (petição contra ilegalidade ou abuso de poder) e "b" (certidões) | Exige providência ou documento do órgão | **A todos assegurados, independentemente do pagamento de taxas** | Sem prazo fixo; resposta é dever do órgão |
| 2 | **Pedido LAI** | Lei 12.527/2011, art. 10 | Obriga o órgão a entregar a informação/documento | **Qualquer interessado**, por qualquer meio; **vedado exigir o motivo** (art. 10 §3º) | Imediato ou **até 20 dias** (art. 11 §1º), prorrogável **+10** (§2º). Recurso em **10 dias** (art. 15) |
| 3 | **Ação popular** | Lei 4.717/1965, art. 1º | Anula/declara nula ato lesivo ao patrimônio público | **Cidadão-eleitor** — prova = título eleitoral (art. 1º §3º) | Prescreve em **5 anos** (art. 21). **Exige advogado** |
| 4 | **Denúncia ao TCU/TCE** | CF art. 74 §2º | Provoca o Tribunal de Contas a apurar a irregularidade | **Qualquer cidadão, partido político, associação ou sindicato** | Rito varia por UF → `[VERIFICAR PRAZO]` (TV9) |
| 5 | **Impugnação de edital** | Lei 14.133/2021, art. 164 | Ataca edital de licitação viciado antes da abertura | **Qualquer pessoa** | 🔴 **FATAL: até 3 dias úteis antes da abertura** do certame. Resposta em até 3 dias úteis (par. único) |
| 6 | **Representação por improbidade** | Lei 8.429/1992, art. 14 | Pede à autoridade a apuração de ato de improbidade | **Qualquer pessoa** (escrita e assinada, art. 14 §1º) | Sem prazo de protocolo; o MP pode instaurar inquérito civil (art. 22) |

## Detalhe que muda a peça

- **LAI é a porta de entrada.** Quando falta o documento do ato, o caminho é primeiro o **pedido LAI**
  (art. 10) para obter o lastro, depois a representação. Negado no **Executivo Federal**, recorre-se à
  **CGU** (Lei 12.527, art. 16). Serviço é **gratuito** (art. 12).
- **Ação popular tem legitimidade estreita:** só o **cidadão-eleitor** (título eleitoral, art. 1º §3º) —
  ver `mapa-legitimados`. Não é "qualquer pessoa" (TV6).
- **Impugnação de edital é a Lei 14.133 art. 164**, "qualquer pessoa", **3 dias úteis** — **não** a Lei
  8.666 art. 41 (revogada, transição encerrada — TV5). O prazo é pré-clusivo: perdeu, perdeu.
- **Representação por improbidade** exige, no art. 14 §1º, **qualificação do representante + fatos +
  autoria + indicação das provas**. O regime é o **pós-reforma da Lei 14.230/2021**: improbidade exige
  **dolo** (TV4) — a peça pede apuração, não afirma o dolo.

## O corte leigo × advogado

O produto **gera a peça pronta** quando o leigo protocola sozinho: **LAI · representação a TCE/TCU ·
representação por improbidade · denúncia à Câmara · impugnação administrativa de edital (art. 164) ·
notícia-crime ao MP**. Quando o instrumento **exige advogado** — **ação popular** (Lei 4.717) e mandado
de segurança — o produto **não redige a peça judicial**: monta o **dossiê** (achado + fonte + norma) e
**roteia** para `civel-adv-os` ou um escritório.

## Travas / limites

- **Nada de citação sem lastro no `context/`.** Artigo, prazo ou pena que não esteja nos anexos vira
  `[FALTA LASTRO]` ou `[VERIFICAR]`. Passa antes por `dever-de-lastro-documental` (P1).
- **Toda peça é pedido de apuração, nunca afirmação de culpa** (P2) — a linha entre a representação
  legítima (Lei 8.429 art. 14) e o crime da denunciação (Lei 8.429 art. 19). O aviso literal é da skill
  `aviso-cp339-art19-e-ce326a` (C4), mostrado **antes** de gerar (P3).
- **Prazo de rito de TCE varia por UF** → `[VERIFICAR PRAZO]` (TV9). **Nunca fabricar prazo** (P7).
- **Apartidável:** o instrumento serve contra qualquer gestão, de qualquer partido. A skill não escolhe
  alvo por lado político.
- **Fronteiras:** contencioso pleno de licitação/TCU → `licitacoes-adv-os`; peça eleitoral →
  `eleitoral-adv-os` (o opositor nunca redige peça eleitoral).

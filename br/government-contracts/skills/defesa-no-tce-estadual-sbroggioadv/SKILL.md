---
name: defesa-no-tce-estadual-sbroggioadv
title: defesa-no-tce-estadual — o controle externo, sem inventar o rito e sem abrir mão do método
description: 'A atuação da procuradoria perante o Tribunal de Contas do Estado: prestação de contas, tomada de contas especial e o exercício do contraditório, com a separação — que decide quem assina o quê — entre a defesa do **ente** e a defesa **pessoal do gestor**. Traz a LINDB como instrumento central do controle externo, esfera que ela alcança por texto expresso: consequências práticas e alternativas antes de invalidar (arts. 20-21), obstáculos reais do gestor e dosimetria da sanção (art. 22), o ato consumado julgado pelas orientações gerais **da época** (art. 24) e o padrão de imputação pessoal — **dolo ou erro grosseiro** (art. 28, cujos parágrafos foram vetados). Trava dura: o rito varia por Estado, então prazo e recurso saem como `[VERIFICAR PRAZO]`, nunca fixados. Aciona: "TCE", "tribunal de contas", "prestação de contas", "tomada de contas especial", "acórdão do tribunal de contas", "erro grosseiro", "defesa do gestor", "glosa de despesa".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/defesa-no-tce-estadual
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: government-contracts
language: pt
---

# defesa-no-tce-estadual — o controle externo, sem inventar o rito e sem abrir mão do método

O tribunal de contas é o foro onde a procuradoria menos pode improvisar: o **rito é de cada
Tribunal**, mas o **método de defesa é federal e está inteiro no anexo da LINDB**. Esta skill separa
as duas coisas — marca o que exige conferência no regimento local e entrega, pronto, o argumento que
a lei federal dá.

Este produto atende o **Estado**.

**Quando entra:** ao receber citação, audiência ou diligência do TCE; na defesa em tomada de contas
especial; ao impugnar acórdão que glosa despesa, imputa débito ou aplica multa; e no parecer sobre
ato que ainda vai a exame de contas.

## ⚠️ A trava do rito — `[VERIFICAR PRAZO]`, sempre

> **Cada Tribunal de Contas tem regimento interno e lei orgânica próprios.** Prazo de defesa,
> nomenclatura da peça, cabimento e prazo de recurso, efeito suspensivo e forma de intimação
> **variam por Estado**.

O produto **nunca fixa prazo de TCE**. Toda referência sai como **`[VERIFICAR PRAZO]`** com a
pergunta escrita: qual dispositivo do regimento interno ou da lei orgânica do TCE deste Estado rege
este ato, e qual o prazo vigente? A simetria com o modelo do TCU (**CF art. 75**) é moldura,
**não** fonte de prazo — e o art. 75 **não está nos anexos** → `[VERIFICAR]` antes de citá-lo.

Contagem de prazo aqui também não herda o dobro do CPC 183: o §2º afasta o benefício quando a lei
estabelece prazo próprio — e o §2º exige **lei** em sentido próprio: a **lei orgânica** do TCE
serve, o **regimento interno não**. Conferir qual das duas fixa o prazo do ato (P7 —
`prerrogativas-processuais`).

## 1. Quem está sendo defendido — a separação que vem primeiro

| Quem | O que se discute | Quem atua |
|---|---|---|
| **O Estado (o ente)** | Regularidade das contas do órgão, legalidade do ato, manutenção do contrato ou do programa | A procuradoria, no exercício da representação do ente |
| **O gestor, pessoalmente** | Imputação de débito, multa, responsabilização pessoal | Depende de **lei do Estado** autorizar a procuradoria a fazê-lo → `[VERIFICAR]` (P5) |

A pergunta "a procuradoria pode defender o gestor pessoalmente, e em que hipóteses?" tem resposta em
lei orgânica da procuradoria ou norma estadual específica — **não há regra nacional**. Sem o texto,
o produto **pergunta**. Confundir os dois papéis cria conflito de interesse dentro da própria peça:
o argumento que salva o gestor pode comprometer o ente.

## 2. As três situações típicas

- **Prestação de contas (ordinária).** Exame periódico da gestão. A atuação útil é **antes**: parecer
  prévio e orientação normativa evitam a glosa. Instaurado o exame, o trabalho é demonstrar
  conformidade e, havendo desconformidade, enquadrá-la nos arts. 22 e 24 da LINDB.
- **Tomada de contas especial.** Apura dano e identifica responsáveis — é a que gera imputação de
  débito. A defesa se organiza em três eixos: **o dano existiu e está quantificado?**; **há nexo
  entre a conduta e o dano?**; **a imputação atende ao art. 28 — dolo ou erro grosseiro?**.
- **Contraditório em diligência, representação ou denúncia.** Prazo curto e efeito preclusivo:
  levantar o regimento antes de qualquer coisa → `[VERIFICAR PRAZO]`.

## 3. A LINDB no controle externo (`context/lindb-20-30.md`)

O anexo não é lei "de direito administrativo geral" trazida por analogia: os arts. 20, 21, 24 e 27
dizem **expressamente** "nas esferas administrativa, **controladora** e judicial" — a esfera
controladora é esta. (O art. 22 não usa essa fórmula: ele fala em "normas sobre gestão pública",
que alcançam o exame de contas do mesmo modo.)

- **Art. 20 — proibido decidir por valor abstrato.** "Não se decidirá com base em valores jurídicos
  abstratos sem que sejam consideradas as consequências práticas da decisão." O **parágrafo único**
  exige que a motivação demonstre **necessidade e adequação** da medida ou da invalidação, "inclusive
  em face das **possíveis alternativas**". Acórdão que anula ato invocando princípio, sem enfrentar
  consequência nem alternativa, contraria o dispositivo — é impugnação com base legal, não retórica.
- **Art. 21 — quem invalida diz o que acontece.** A decisão que decreta invalidação "deverá indicar
  de modo expresso suas consequências jurídicas e administrativas" e, quando for o caso, as
  **condições para regularização proporcional e equânime**, sem impor aos atingidos "ônus ou perdas
  que, em função das peculiaridades do caso, sejam **anormais ou excessivos**".
- **Art. 22 — o gestor real, e a dosimetria.** Interpretam-se as normas de gestão pública
  considerando "os **obstáculos e as dificuldades reais do gestor** e as exigências das políticas
  públicas a seu cargo, sem prejuízo dos direitos dos administrados". O **§1º** manda considerar as
  circunstâncias práticas que limitaram a ação do agente; o **§2º**, na sanção, a natureza e a
  gravidade da infração, os danos, agravantes, atenuantes e antecedentes; o **§3º** obriga a levar as
  sanções já aplicadas à dosimetria das demais **de mesma natureza e sobre o mesmo fato** — é o
  argumento contra a punição em cascata.
- **Art. 24 — o ato consumado, pela régua da época.** A revisão de ato "cuja produção já se houver
  completado levará em conta as **orientações gerais da época**, sendo vedado que, com base em
  mudança posterior de orientação geral, se declarem inválidas situações plenamente constituídas". O
  parágrafo único define orientação geral: atos públicos gerais, jurisprudência **judicial ou
  administrativa majoritária** e **prática administrativa reiterada e de amplo conhecimento
  público** — inclusive a do próprio Tribunal. Entendimento novo do TCE aplicado retroativamente é
  exatamente o que o artigo veda.
- **Art. 26 — a saída negociada.** Compromisso com os interessados para eliminar irregularidade,
  incerteza jurídica ou situação contenciosa, **após oitiva do órgão jurídico**, com obrigações,
  prazo e sanções claros (§1º, IV) — vedada desoneração permanente de dever reconhecido por
  orientação geral (III). **Art. 27:** a decisão pode impor **compensação** por benefícios indevidos
  ou prejuízos anormais ou injustos, motivada e ouvidas as partes. Aprofundamento dos dois:
  `lindb-como-metodo`.

## 4. O padrão de imputação — art. 28, e o que ele **não** diz

**Caput:** "O agente público responderá pessoalmente por suas decisões ou opiniões técnicas em caso
de **dolo ou erro grosseiro**." É o teto da responsabilização pessoal e o eixo da defesa do
parecerista e do ordenador de despesa: divergência de interpretação, escolha administrativa razoável
ou erro comum **não são** erro grosseiro.

**Trava de honestidade:** os **§§1º a 3º do art. 28 foram VETADOS** e constam no anexo como
"(VETADO)". Não existe texto neles — citar conteúdo desses parágrafos é erro de fonte, não de
interpretação. O mesmo vale para os demais vetos do recorte (art. 23, par. único; art. 25; art. 26,
§1º, II e §2º; art. 29, §2º).

## 5. A ponte com improbidade e ressarcimento

Acórdão do TCE que imputa débito costuma alimentar improbidade ou ressarcimento. Duas regras firmes:

- As **ADIs 7156 e 7236 foram julgadas em 01/07/2026**: o STF invalidou a redução pela metade do
  prazo prescricional e preservou a exigência de dolo e o rol taxativo. Consequência específica
  sem conferência do acórdão integral → `[VERIFICAR]` (**TV1**, `context/travas-defasagem.md`).
  Tratamento em `improbidade-defesa-e-autoria`.
- **Instâncias não se confundem.** Se a decisão do TCE vincula, e em que medida, a esfera judicial é
  matéria de jurisprudência **não capturada nos anexos** → `[VERIFICAR]` e passagem por
  `suprema-corte-fazendaria` (P3).

## 6. Checklist antes de protocolar

1. Regimento/lei orgânica do TCE localizados e prazo conferido → `[VERIFICAR PRAZO]` resolvido.
2. Papel definido: defesa do **ente** ou do **gestor** (e, se do gestor, com que autorização legal).
3. Dano: existe, está quantificado, e há nexo com a conduta apontada?
4. Imputação testada contra o art. 28 — dolo ou erro grosseiro, com fato concreto.
5. Ato antigo? Levantar a **orientação geral da época** (art. 24, par. único), inclusive a prática
   reiterada do próprio Tribunal.
6. A decisão que invalida indicou consequências e alternativas (arts. 20-21)? Se não, é fundamento de
   impugnação. Sanções já aplicadas sobre o mesmo fato entram na dosimetria (art. 22, §3º).

## Travas desta skill

- **Trava do rito.** Prazo, recurso e nomenclatura variam por Estado → **`[VERIFICAR PRAZO]`**,
  nunca hardcodados. **CF art. 75** é moldura de simetria e **não está nos anexos** → `[VERIFICAR]`.
- **P5.** Lei orgânica da procuradoria, competência para defender o gestor e regimento do TCE são
  direito local — o produto pergunta, não presume.
- **P2.** LINDB tem lastro verbatim em `context/lindb-20-30.md`. Súmula, tema, acórdão de TCE e
  dispositivo constitucional **não** estão → `[VERIFICAR]`. Vetos jamais citados como texto.
- **P1.** Controle externo **estadual**. Contas de Município são do `procurador-municipal-os`; o
  federal, do `procurador-federal-os`. Matéria tributária de outra esfera não entra aqui.
- **P3.** Tese sobre vinculação entre instâncias, prescrição do ressarcimento e alcance do art. 28
  passa por `suprema-corte-fazendaria` antes da minuta.
- **P4.** Dado de processo de contas é sensível: fica no ambiente do órgão. A peça e a
  responsabilidade são do procurador, indelegáveis (`conformidade-ia-institucional`).

**Próximo passo:** método consultivo → `lindb-como-metodo`; responsabilidade do parecerista →
`parecer-consultivo`; contrato e convênio → `convenios-e-licitacoes-consultivo`; desdobramento
sancionatório → `improbidade-defesa-e-autoria`. Fecha por `suprema-corte-fazendaria`, com o
`validador-fazendario-vigente` antes.

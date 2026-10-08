---
name: improbidade-defesa-e-autoria-sbroggioadv
title: improbidade-defesa-e-autoria — os dois lados da mesma lei
description: 'Improbidade pelos dois papéis do Estado: ente autor e defesa do agente/ente. TV1: ADIs 7156 e 7236 julgadas em 01/07/2026; o STF invalidou a redução pela metade do prazo prescricional e preservou dolo e rol taxativo. Consequência específica sem o acórdão integral sai [VERIFICAR]. Sem prova de dolo, culpa, erro e má gestão não bastam. A defesa usa LINDB 28 (dolo/erro grosseiro), 22 (obstáculos reais) e 24 (orientação da época). Art. 11 e prazos do art. 23 saem [VERIFICAR]. Aciona: "ação de improbidade", "defesa em improbidade", "dolo", "Lei 14.230".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/improbidade-defesa-e-autoria
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# improbidade-defesa-e-autoria — os dois lados da mesma lei

Este produto atende o **Estado**. A improbidade é a única matéria desta camada em que a
procuradoria pode estar nos dois polos: propondo a ação em nome do ente, ou defendendo o agente e o
ente quando a ação vem de fora. Esta skill trata as duas posições sem confundir a régua.

## TV1 — a trava que entra em toda saída, sem exceção

> As **ADIs 7156 e 7236 foram julgadas pelo STF em 01/07/2026**. No retrato oficial
> pós-julgamento, o Tribunal invalidou a redução pela metade do prazo prescricional prevista na
> reforma e preservou a exigência de dolo e o rol taxativo de condutas.

Consequência literal, imposta por `context/travas-defasagem.md` (TV1): **não tratar as ADIs como
pendentes** e não converter a notícia oficial em conclusões que ela não contém. O produto pode usar
o resultado acima; alcance, modulação, marco temporal ou consequência específica que dependa do
acórdão integral sai **`[VERIFICAR]`**. Toda análise, parecer ou peça desta skill carrega este
snapshot pós-julgamento; sem ele, o `suprema-corte-fazendaria` reprova pelo gate de defasagem (R3).

## O eixo prático: dolo específico

**Com lastro** (vigência ✅ conferida no Planalto): a redação da Lei 14.230/2021 **exige
dolo específico**. É o divisor que reorganiza os dois papéis:

- **Culpa não basta.** Negligência, imperícia e imprudência do gestor não sustentam improbidade sob
  a redação vigente.
- **Erro não basta.** Interpretação equivocada da norma, decisão administrativa malsucedida ou
  resultado ruim não são, por si, ato ímprobo.
- **Dano ao erário, sozinho, não basta.** Prejuízo é elemento de algumas hipóteses, não substituto
  do elemento subjetivo.
- **O que sustenta** é a demonstração de que o agente **quis o resultado ilícito** — vontade livre e
  consciente dirigida ao fim vedado, comprovada, não presumida do resultado.

## O ente como AUTOR — quando propor

A pergunta não é "houve irregularidade?", é **"há prova de dolo específico?"**. Roteiro de decisão,
nesta ordem:

1. **Elemento subjetivo primeiro.** Sem prova documental ou testemunhal de vontade dirigida ao
   ilícito, a ação não se propõe. Improbidade ajuizada sem dolo demonstrável termina em
   improcedência, cria passivo de honorários para o ente e queima a credibilidade institucional das
   ações que teriam fundamento.
2. **Enquadramento.** Qual hipótese legal e por quê. ⚠️ **`[VERIFICAR]`:** o rol do **art. 11** e a
   restrição que a Lei 14.230/2021 lhe impôs **não constam dos anexos** — o texto do dispositivo e a
   taxatividade do rol precisam ser conferidos na fonte primária antes de qualquer enquadramento por
   violação a princípio, que é justamente a hipótese mais afetada pela reforma.
3. **Prazo.** ⚠️ **`[VERIFICAR]`:** os prazos do **art. 23** — prescrição, contagem, marco inicial e
   eventual prescrição intercorrente — **não constam dos anexos**. É matéria alterada pela reforma e
   pesada demais para sair de memória; conferir na fonte antes de qualquer juízo sobre tempestividade.
4. **Legitimidade e via.** Quem pode propor, e se a via mais eficaz é a improbidade ou a ação de
   ressarcimento. `[VERIFICAR]` os dispositivos. Critério prático: **ressarcimento recupera dinheiro;
   improbidade aplica sanção pessoal.** Quando o objetivo real é recompor o erário, a improbidade é
   a via mais longa e mais incerta.
5. **Alternativas antes do ajuizamento.** A **LINDB art. 26** autoriza a autoridade a **celebrar
   compromisso** para eliminar irregularidade ou situação contenciosa, **após oitiva do órgão
   jurídico** — que é a procuradoria — vedada a desoneração permanente de dever (§1º III) e exigida
   clareza sobre obrigações, prazo e sanções (§1º IV). Instrumentos de acordo previstos na própria
   lei de improbidade → `[VERIFICAR]`.

## A defesa — do agente e do ente

**A LINDB é a ponte anchorada**, e é a parte mais sólida desta skill (`context/lindb-20-30.md`,
verbatim):

- **Art. 28** — *"O agente público responderá pessoalmente por suas decisões ou opiniões técnicas em
  caso de dolo ou erro grosseiro."* É o padrão de imputação e alcança expressamente as **opiniões
  técnicas**, ou seja, o parecerista. ⚠️ Os **§§1º a 3º do art. 28 foram VETADOS** — não têm texto e
  **nunca** são citados como se tivessem.
- **Art. 22** — na interpretação de normas de gestão pública consideram-se **os obstáculos e as
  dificuldades reais do gestor** e as exigências das políticas públicas a seu cargo, *sem prejuízo
  dos direitos dos administrados*; o **§1º** manda considerar as circunstâncias práticas que
  impuseram, limitaram ou condicionaram a ação do agente; o **§2º** fixa critérios de dosimetria
  (natureza e gravidade, danos, agravantes, atenuantes, antecedentes).
- **Art. 24** — o ato já consumado se julga pelas **orientações gerais da época**, sendo **vedado**
  invalidá-lo por mudança posterior de orientação; o parágrafo único inclui a **prática
  administrativa reiterada e de amplo conhecimento público**. É a defesa central do gestor acusado
  anos depois por prática que era corrente à época.
- **Arts. 20 e 21** — contra a imputação construída sobre valor jurídico abstrato, sem consideração
  das consequências práticas e das alternativas.

**Roteiro da defesa:** (1) atacar o **elemento subjetivo** — não há dolo específico demonstrado, e a
inicial o presume do resultado; (2) reconstituir o **contexto real da decisão** (art. 22 e §1º),
com documento; (3) fixar a **orientação geral da época** (art. 24) quando o ato é pretérito; (4)
apontar o **padrão de imputação** do art. 28 quando o acusado é parecerista ou emitiu opinião
técnica; (5) prazo (`[VERIFICAR]` art. 23); (6) individualizar condutas — imputação em bloco a todos
os que assinaram o processo administrativo não sobrevive à exigência de dolo específico.

## Quando o acusado é o parecerista

Situação frequente e delicada: a mesma procuradoria que defende pode ter emitido o parecer
questionado. Duas regras:

- **O padrão é o art. 28**: dolo ou erro grosseiro. Divergência de interpretação jurídica não é erro
  grosseiro.
- ⚠️ **`[VERIFICAR]`** a distinção entre parecer **vinculante** e **opinativo** — o precedente que a
  firmou **não consta dos anexos**, e ela é decisiva no regime de responsabilização. A mesma
  marcação está em `parecer-consultivo`, e por isso a conduta preventiva é lá: fundamentar,
  ressalvar, registrar alternativas e não decidir no lugar da autoridade.

Se há conflito de interesse entre a defesa do ente e a do agente, **declare-o** e encaminhe à
autoridade — a decisão sobre representação não é da ferramenta.

## Travas desta skill

- **TV1 obrigatória** — as ADIs **7156** e **7236** foram julgadas em **01/07/2026**. A saída usa o
  resultado oficial conhecido e marca `[VERIFICAR]` para consequência específica sem conferência
  do acórdão integral; nunca as apresenta como pendentes.
- **P2** — com lastro: a exigência de **dolo específico**, as duas ADIs, e a LINDB arts. 20-30
  verbatim. **Sem lastro → `[VERIFICAR]`:** o **art. 11** e sua restrição, os **prazos do art. 23**,
  as hipóteses de acordo, o regime de ressarcimento, e **qualquer súmula ou tema** sobre improbidade
  — nenhum consta do `context/`.
- **Vetos** — art. 28 §§1º-3º e os demais vetos do recorte da LINDB não têm texto.
- **P3** — antes de propor ou de recorrer, a tese passa pelo `suprema-corte-fazendaria`.
- **P1** — nenhuma matéria de outra esfera, inclusive em exemplo de ato ímprobo tributário.
- **P5** — nada sobre regime funcional do agente por analogia com o de outro ente.
- **P4** — a análise sai completa, com revisão humana obrigatória e responsabilidade indelegável; a
  decisão de propor, acordar ou defender é da autoridade competente. Dado de agente investigado é
  sensível: iniciais e papel, nunca o dado cru.

A ponta ativa — o ente decidindo propor — fica nesta mesma skill; esta esfera não tem camada própria de improbidade.

## Cross-links

`parecer-consultivo` (responsabilidade do parecerista e conduta preventiva) ·
`convenios-e-licitacoes-consultivo` (origem mais comum da imputação) · `lindb-como-metodo` (arts. 22,
24 e 28) · `defesa-do-ente-contestacao` (estrutura de peça) · `desapropriacao` (avaliação e
indenização como fonte de imputação) · `conformidade-ia-institucional` ·
`suprema-corte-fazendaria` (**QA obrigatória no fecho**) · `validador-fazendario-vigente` (TV1) ·
`estilo-e-fronteiras`.
Fora da casa: `criminal-adv-os` (a esfera penal do mesmo fato) · `civel-adv-os` ·
`licitacoes-adv-os` (a ótica do licitante) · `juris-adv-os`.

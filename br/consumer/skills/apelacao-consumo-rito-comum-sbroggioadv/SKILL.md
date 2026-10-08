---
name: apelacao-consumo-rito-comum-sbroggioadv
title: Apelação em ação de consumo — rito comum
description: 'Estrutura razões e contrarrazões de apelação em ação de consumo processada no rito comum (fora do JEC — valor acima de 40 salários mínimos ou complexidade probatória). Foco no que muda em matéria de consumo: reforma por inversão tardia do ônus da prova (regra de instrução, não de julgamento), limites à revisão do quantum de dano moral, aplicação da Súmula 385/STJ e correção do marco de juros e correção monetária. Standalone, modelado sem dependência dura do civel-adv-os (mecânica geral do CPC). Aciona: redigir razões ou contrarrazões de apelação em ação de consumo no rito comum, avaliar cerceamento de defesa por inversão tardia do ônus da prova, impugnar ou defender o quantum de dano moral em 2º grau.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/apelacao-consumo-rito-comum
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Apelação em ação de consumo — rito comum

## Quando esta skill entra
Ação de consumo processada fora do JEC (acima de 40 SM, ou por exigir perícia
formal — ver `competencia-jec-x-comum`) que recebeu sentença de 1º grau e uma das
partes quer recorrer. **A mecânica geral do CPC (prazo, preparo, efeitos, requisitos
formais da apelação) não tem corpus de captura própria neste plugin — tratamento
completo modelado no `civel-adv-os` (cross-link soft, sem dependência dura).** Esta
skill foca no que é ESPECÍFICO de matéria de consumo nas razões e contrarrazões.

## Base normativa
CDC (Lei 8.078/1990) arts. 6º, VIII; jurisprudência do STJ sobre ônus da prova,
quantum de dano moral e Súmula 385 — `context/jec-fonaje-e-recursos.md`,
`context/jurisprudencia-sumulas-temas.md`.

## O que decide a reforma em matéria de consumo

**1. Inversão do ônus da prova — regra de instrução, não de julgamento.** STJ, REsp
1.286.273-SP, 4ª Turma, Rel. Min. Marco Buzzi, j. 08/06/2021: a inversão do CDC art.
6º, VIII deve ser decidida, preferencialmente, no saneamento — ou, no mínimo,
assegurar à parte que não tinha o encargo a **reoportunidade** de produzir prova sob
o novo ônus. Se o juiz inverteu só na sentença sem reabrir essa chance, há vulnerabi-
lidade a nulidade por cerceamento de defesa **do fornecedor** — o que pode,
contraintuitivamente, jogar contra o próprio consumidor no recurso.

**2. Quantum do dano moral.** O STJ só revê o valor em hipóteses excepcionais (mani-
festamente irrisório ou exorbitante) — fora disso, a fixação é prerrogativa das
instâncias ordinárias. Fatores de ponderação: grau de culpa/dolo do agente,
gravidade e extensão do dano, sofrimento do ofendido, condição econômica das partes,
reincidência do fornecedor. Dupla finalidade: compensar o ofendido **e** desestimular
o ofensor (teoria do desestímulo) — vedados os dois extremos (enriquecimento sem
causa e valor irrisório que não cumpre função pedagógica).

**3. Súmula 385/STJ (mero dissabor / inscrição preexistente).** Se a sentença aplicou
ou afastou a súmula sem examinar se a inscrição preexistente também estava sub judice
com verossimilhança demonstrada (STJ, REsp 1.704.002, Rel. Min. Nancy Andrighi, 3ª
Turma; REsp 1.647.795), isso é ponto concreto de reforma.

**4. Marco de juros e correção monetária.** Súmula 54/STJ — juros moratórios fluem do
evento danoso em responsabilidade extracontratual (não da citação, regra do CC art.
405 para responsabilidade contratual). Súmula 362/STJ — correção monetária do dano
moral incide desde a data do arbitramento (e do último arbitramento, se o valor
mudar em instância superior). Erro no marco é reforma pontual, sem reabrir o mérito.

## Tese do consumidor (razões/contrarrazões)
Razões centradas em quantum insuficiente frente a parâmetros de casos análogos do
tribunal local, correção do marco de juros/correção monetária, ou reforma de sentença
que aplicou a Súmula 385 sem examinar a exceção da inscrição sub judice. Em
contrarrazões, sustentar que a inversão do ônus foi tempestiva (saneamento) e que o
quantum está dentro da faixa de razoabilidade do tribunal.

## Tese do fornecedor (razões/contrarrazões)
Razões centradas em cerceamento de defesa quando a inversão do ônus veio só na
sentença sem nova oportunidade de prova, redução de quantum por desproporcionalidade,
ou reforma por má aplicação das excludentes de responsabilidade (culpa exclusiva do
consumidor/terceiro, fortuito externo — CDC arts. 12, §3º e 14, §3º). Em
contrarrazões, sustentar que a sentença seguiu a jurisprudência pacífica sobre
quantum e marco de juros, blindando contra reforma no ponto.

## Armadilhas
- Não tratar a inversão do ônus da prova feita só na sentença como definitiva — é
  fundamento de nulidade por cerceamento de defesa, alegável em apelação.
- Súmula 385/STJ não é absoluta — checar se a inscrição preexistente também está sub
  judice antes de fechar a porta do dano moral.
- STJ não reexamina quantum de dano moral fora das hipóteses excepcionais — pedido de
  redução/majoração precisa demonstrar desproporção manifesta, não mera insatisfação.

## Fronteira
Mecânica geral do CPC (prazo, preparo, efeitos, requisitos formais da apelação) →
`civel-adv-os` (cross-link soft, sem dependência dura). Apelação não existe no rito
do JEC — lá o recurso é o inominado → `recurso-inominado-turma-recursal`. Recurso
especial/extraordinário após o acórdão de apelação → `resp-e-re-consumo`.

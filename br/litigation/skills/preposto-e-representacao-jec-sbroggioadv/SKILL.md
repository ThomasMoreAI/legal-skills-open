---
name: preposto-e-representacao-jec-sbroggioadv
title: Preposto e representação da pessoa jurídica no JEC
description: 'Trata da representação do réu pessoa jurídica no JEC por preposto credenciado — a carta de preposição com poderes para transigir, a dispensa de vínculo empregatício desde 2009, o que a carta precisa conter, a vedação de acumular preposto e advogado na mesma pessoa e a consequência processual de comparecer sem carta válida. Também esclarece a tensão histórica entre a lei e o FONAJE sobre vínculo empregatício, hoje encerrada. Aciona: preparar preposto para audiência, redigir ou conferir carta de preposição, questionar representação do réu em audiência, avaliar validade de acordo firmado por preposto sem carta.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/preposto-e-representacao-jec
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# Preposto e representação da pessoa jurídica no JEC

## Quando esta skill entra
Ao preparar o comparecimento do réu pessoa jurídica/firma individual em audiência, ou quando o
consumidor quer questionar a representação do fornecedor na sessão.

## Base normativa
Lei 9.099/1995, art. 9º, §4º, redação dada pela Lei 12.137/2009 (anexo `context/lei-9099-jec.md`):
"O réu, sendo pessoa jurídica ou titular de firma individual, poderá ser representado por preposto
credenciado, munido de carta de preposição com poderes para transigir, sem haver necessidade de
vínculo empregatício."

## O que a carta precisa conter
- Poderes expressos para **transigir** (fazer acordo em nome da pessoa jurídica) — sem isso, o
  preposto comparece, mas não pode firmar acordo válido em audiência.
- Identificação da pessoa jurídica outorgante e do preposto outorgado.
- Não exige comprovação de vínculo empregatício entre o preposto e a pessoa jurídica — a redação
  de 2009 é expressa nesse ponto ("sem haver necessidade de vínculo empregatício").

## A tensão investigada — e encerrada em 2009, não em aberto hoje
Antes da Lei 12.137/2009, havia divergência doutrinária e jurisprudencial real sobre exigir ou não
vínculo empregatício do preposto com a pessoa jurídica ré. A Lei 12.137/2009 alterou o art. 9º,
§4º exatamente para **encerrar** essa controvérsia, afirmando de forma expressa a dispensa do
vínculo. Nenhum dos enunciados do FONAJE localizados no corpus (20, 98, 99) reintroduz a exigência
de vínculo — eles tratam de temas distintos: representação em geral, vedação de acúmulo de função,
e consequência de comparecer sem carta. **Não há hoje enunciado do FONAJE em sentido divergente do
art. 9º, §4º sobre vínculo empregatício** — declarar isso com precisão, em vez de citar uma
controvérsia doutrinária que a lei já resolveu, é o que o corpus confirma
(`context/jec-fonaje-e-recursos.md`, §1.1).

## Enunciados FONAJE aplicáveis
| Enunciado | Regra |
|---|---|
| 20 | Comparecimento pessoal da parte é obrigatório; a pessoa jurídica pode ser representada por preposto. |
| 98 (substitui o 17) | É vedada a acumulação **simultânea** das condições de preposto e advogado na mesma pessoa (art. 35, I e 36, II da Lei 8.906/1994 c/c art. 23 do Código de Ética e Disciplina da OAB). |
| 99 (substitui o 42) | O preposto que comparece sem carta de preposição obriga-se a apresentá-la no prazo assinado, para validade de eventual acordo, sob as penas dos arts. 20 e 51, I da Lei 9.099/1995, conforme o caso. |

## Consequência da falha na representação
Se o preposto comparece **sem** carta de preposição, o acordo eventualmente firmado na audiência
fica condicionado à apresentação da carta no prazo que o juízo fixar (Enunciado 99). Não cumprido o
prazo, aplicam-se as penas do art. 20 (revelia, se for o caso) ou do art. 51, I (extinção do
processo por falta de comparecimento, conforme a hipótese concreta). Armar a audiência com um
preposto que também assina como advogado da causa é nulidade evitável (Enunciado 98) — a
acumulação simultânea das duas funções na mesma pessoa física é vedada.

## Tese do consumidor
Se o réu-fornecedor comparece com preposto sem carta de preposição válida (ou sem poderes para
transigir), o consumidor pode recusar-se a transigir até a apresentação do documento em mãos — e,
se o prazo fixado pelo juízo não for cumprido, requerer a aplicação dos efeitos do art. 20/51, I.
Verificar também se a mesma pessoa não está atuando simultaneamente como preposto e advogado
(Enunciado 98) — se estiver, arguir a nulidade.

## Tese do fornecedor
A ausência de vínculo empregatício do preposto não é mais discutível desde 2009 — argumentar o
contrário é levantar tese superada por lei. A exigência real e viva é **documental**: carta válida,
com poderes expressos para transigir, e a vedação de acumular preposto e advogado na mesma pessoa
física. Preparar o preposto com a carta em mãos antes da audiência evita tanto a nulidade do
Enunciado 98 quanto a pendência do Enunciado 99.

## Armadilhas
Nenhuma trava específica das T1-T13 cobre diretamente este ponto — a única atenção é não citar a
controvérsia pré-2009 (vínculo empregatício) como se estivesse em aberto; se algo além disso for
necessário e não constar do corpus, `[VERIFICAR — não confirmado no corpus]`.

## Fronteira
Revelia decorrente de falha de comparecimento/representação → `revelia-e-contestacao-jec`. Rito
geral e prazos → `rito-jec-consumidor`.

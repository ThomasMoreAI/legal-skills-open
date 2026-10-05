---
name: procon-dosimetria-e-anulacao-sbroggioadv
title: PROCON — dosimetria da multa e anulação
description: 'Estrutura a dosimetria da multa administrativa do PROCON (critérios legais, atenuantes e agravantes taxativas, veto ao bis in idem), o recurso administrativo (prazo, efeito suspensivo em caso de multa, inscrição em dívida ativa) e as teses de anulação judicial da multa: vício de motivação, desproporcionalidade, cerceamento de defesa, prescrição administrativa. Base: Decreto 2.181/1997, redação do Decreto 10.887/2021. Aciona: calcular ou impugnar dosimetria de multa PROCON, redigir recurso administrativo, avaliar prescrição da pretensão punitiva, montar ação anulatória de auto de infração ou de multa PROCON.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/procon-dosimetria-e-anulacao
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# PROCON — dosimetria da multa e anulação

## Quando esta skill entra
Após condenação em processo administrativo sancionador (PAS) do PROCON: para calcular/
impugnar o valor da multa, recorrer administrativamente, ou avaliar via judicial de
anulação. Pressupõe a defesa inicial já tratada em `procon-defesa-auto-de-infracao`.

## Base normativa
Decreto 2.181/1997, redação do Decreto 10.887/2021 — arts. 24 a 32 (dosimetria), 46
a 55 (julgamento, recurso, dívida ativa); CDC (Lei 8.078/1990) art. 57 (faixa de
multa) — `context/decreto-2181-sndc-sancoes.md`, `context/cdc-lei-8078.md`.

## Dosimetria — critérios, faixa e taxatividade

**Critérios de fixação da pena-base (art. 28):** gravidade da prática infrativa,
extensão do dano causado, vantagem auferida com o ato infrativo, condição econômica
do infrator e **proporcionalidade entre a gravidade da falta e a intensidade da
sanção** (inciso V, incluído em 2021). **Veto ao bis in idem (art. 28-A):** o
elemento usado para fixar a pena-base não pode ser valorado de novo como agravante ou
atenuante.

**Atenuantes (art. 25) — taxativas por força do art. 26-A:** ação do infrator não
fundamental para o fato; infrator primário; providências para minimizar/reparar de
imediato; confissão; participação regular em capacitação do SNDC; e **ter aderido à
plataforma Consumidor.gov.br** (inciso VI, incluído 2021 — cross-link ver Fronteira).

**Agravantes (art. 26) — também taxativas:** reincidência; vantagem indevida
comprovada; consequência danosa à saúde/segurança; omissão em mitigar o dano; dolo;
dano coletivo ou caráter repetitivo; vítima menor de 18/maior de 60 anos ou pessoa
com deficiência; dissimulação da natureza ilícita; aproveitamento de crise econômica,
calamidade ou condição da vítima. **Reincidência (art. 27):** repetição de prática
infrativa punida por decisão irrecorrível — não prevalece se passaram mais de 5 anos
entre a decisão definitiva e a prática posterior.

**Faixa de valor (CDC art. 57):** não inferior a 200 nem superior a 3.000.000 de
vezes o valor da UFIR "ou índice equivalente que venha a substituí-lo". **Como a UFIR
foi extinta, não existe valor nacional único em reais** — cada PROCON estadual/
municipal usa índice de atualização próprio (relatos convergem para IPCA-E, mas não
é texto de lei única). Nunca fixar "a multa vai de R$ X a R$ Y" sem checar o ato
normativo do PROCON do caso concreto.

## Recurso administrativo (arts. 46, 49 a 54)
Decisão condenatória contém: identificação, resumo dos fatos, sumário da defesa,
apreciação de provas, dispositivo, multa individualizada e sua dosimetria, prazo para
cumprir (art. 46). **Recurso ao superior hierárquico**, prazo de 10 dias contados da
intimação (art. 49, caput) — **regra geral SEM efeito suspensivo**, mas **em caso de
multa, o recurso TEM efeito suspensivo** (art. 49, §1º, incluído 2021 — exceção que
contraria a regra geral do mesmo artigo; não generalizar "recurso não suspende"). Se o
processo tramitou no órgão federal (hoje Secretaria Nacional do Consumidor/MJSP),
cabe 2ª e última instância em mais 10 dias (art. 50). Recurso fora do prazo não é
conhecido (art. 51); todos os prazos da seção são preclusivos (art. 54). Decisão
definitiva → infrator notificado para pagar em 10 dias (art. 53, §único). **Não pago
em 30 dias → inscrição em dívida ativa** do órgão que aplicou a sanção, para cobrança
executiva (art. 55).

## Teses de anulação judicial (síntese operacional)
1. **Nulidade por falta de dupla visita** em atividade de risco leve (art. 38-A, §2º).
2. **Desproporcionalidade** entre gravidade da conduta e valor da multa (art. 28, V).
3. **Bis in idem** — mesmo elemento usado na pena-base e revalorado como agravante
   (art. 28-A).
4. **Cerceamento de defesa** — prazo de defesa não observado (20 dias, não 10 — ver
   T9 em `procon-defesa-auto-de-infracao`) ou notificação inválida.
5. **Prescrição** — 🟡 regime NÃO é uniforme: para PROCON federal aplica-se a Lei
   9.873/1999 (quinquenal, com regras de intercorrência); para PROCON estadual/
   municipal, por analogia, a prescrição quinquenal do Decreto 20.910/1932, **sem**
   reconhecimento de prescrição intercorrente por ausência de previsão específica.
   Tratar como regime único é erro — validar o ente antes de opinar sobre prescrição.
6. **Ausência de individualização da conduta** / enquadramento legal genérico no auto
   (viola art. 35, I, "d" do decreto).

## Tese do fornecedor × tese do órgão de defesa do consumidor
**Fornecedor:** combinar as 6 teses acima conforme o vício concreto do processo;
priorizar desproporcionalidade e bis in idem quando a multa é alta mas a conduta é
isolada e sem dano coletivo. **Órgão/SNDC (sustentação da multa):** demonstrar que os
critérios do art. 28 foram todos considerados sem sobreposição, que a dupla visita
não era exigível (reincidência/fraude/embaraço), e que o prazo de defesa foi
efetivamente de 20 dias e respeitado.

## Armadilhas
- Recurso de **multa** tem efeito suspensivo — é a exceção do art. 49, §1º; não
  confundir com a regra geral (sem suspensão) do caput.
- Não existe valor de multa fixo em reais — UFIR extinta, índice varia por ente.
- Prescrição administrativa não é um regime único nacional — federal ≠ estadual/
  municipal.

## Fronteira
Instauração, auto de infração e defesa inicial → `procon-defesa-auto-de-infracao`.
Adesão ao Consumidor.gov.br como estratégia pré-processual e efeito no interesse de
agir → `consumidor-gov-br-e-pre-processual` (aqui trato só do efeito na dosimetria).

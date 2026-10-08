---
name: defesa-fornecedor-jec-sbroggioadv
title: Defesa do fornecedor no JEC consumerista
description: 'Estrutura a contestação padrão do fornecedor em Juizado Especial Cível (JEC) consumerista: quais preliminares valem a pena arguir (incompetência por complexidade probatória, ilegitimidade passiva na cadeia de fornecimento, falta de interesse de agir), como impugnar valor da causa e pedido de gratuidade, o que a prova documental que acompanha a defesa precisa conter, e quando formular pedido contraposto no lugar de reconvenção. Explica por que reconvenção e denunciação da lide não cabem no rito. Aciona quando o usuário pedir para montar, revisar ou auditar uma contestação de fornecedor em ação de consumo no JEC, decidir quais preliminares arguir, ou entender os limites processuais da defesa nesse rito.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/defesa-fornecedor-jec
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Defesa do fornecedor no JEC consumerista

## Quando esta skill entra

O fornecedor foi citado em ação de consumo no Juizado Especial Cível (Lei 9.099/1995) e precisa de
contestação. Esta skill estrutura a peça de defesa — preliminares, impugnações e prova — sem
inventar teses que o rito sumaríssimo não admite.

## Base normativa

Lei 9.099/1995 (capturada verbatim em `context/lei-9099-jec.md`): art. 3º (competência), art. 8º
(quem pode ser parte), art. 10 (veda intervenção de terceiro e assistência), art. 30 (conteúdo da
contestação), art. 31 (veda reconvenção, admite pedido contraposto). CDC (Lei 8.078/1990) arts.
12, 14, 18 e 25 — responsabilidade solidária da cadeia de fornecimento, capturados em
`context/cdc-lei-8078.md`.

## O passo a passo da contestação

**1. Preliminares — só as que têm chance real:**

- **Incompetência por complexidade probatória.** O critério do FONAJE Enunciado 54 é o **objeto da
  prova**, não a matéria discutida — "é ação de plano de saúde, logo é complexa" não sustenta a
  preliminar. Só prospera demonstrando, concretamente, que o litígio exige perícia **formal**
  (contábil, técnica) que a perícia informal do art. 35 (Enunciado 12 do FONAJE) não supre com
  segurança — juntar prova preliminar da divergência técnica (ex.: laudo prévio, nota de
  cálculo atuarial) reforça a preliminar; alegação genérica não.
- **Ilegitimidade passiva na cadeia de fornecimento.** A responsabilidade solidária dos arts.
  12/14/18/25 do CDC não impede a defesa de demonstrar, com prova documental, que o réu específico
  não integra a cadeia daquele produto/serviço (ex.: mero hospedeiro de anúncio sem ingerência —
  ver [[excludentes-de-responsabilidade]] para a tese de fortuito e culpa de terceiro).
- **Falta de interesse de agir por ausência de tentativa extrajudicial prévia.** Hoje a posição
  dominante é que o consumidor **não precisa** provar tentativa administrativa prévia — mas o STJ
  tem o **Tema 1.396/STJ** afetado (07/10/2025) exatamente sobre isso, ainda **pendente** de
  julgamento em 18/08/2026. A tese do fornecedor pode ser arguida citando a divergência real em
  tribunais estaduais (ex.: IRDR do TJMG), mas a peça deve registrar expressamente que a questão
  está **sub judice** — nunca apresentar como jurisprudência pacífica. `[VERIFICAR — resultado do
  Tema 1.396/STJ antes de usar em peça após o julgamento]`.

**2. Impugnação ao valor da causa.** Regra geral: feita em preliminar de contestação, sob pena de
preclusão para a parte — mas o valor da causa é matéria de ordem pública e pode ser revisto de
ofício pelo juiz a qualquer tempo (a preclusão só atinge quem teve oportunidade e não a exerceu).
Pelo FONAJE Enunciado 39, o valor da causa deve refletir a pretensão econômica exata do pedido —
se o consumidor infla o valor para além do que pede de fato, há base para impugnar.

**3. Impugnação ao pedido de gratuidade.** Cabe quando há elementos concretos que contradizem a
presunção de hipossuficiência declarada — a impugnação exige fato específico, não mera dúvida
genérica.

**4. Prova documental que acompanha a defesa.** Toda a prova documental disponível deve vir junto
com a contestação (art. 30 — a peça concentra "toda matéria de defesa"): contrato, termos de
uso, histórico de atendimento (SAC — obrigatório manter por 2 anos, Decreto 11.034/2022, art.
12, §5º), print de resposta em consumidor.gov.br quando existir (evidência de boa-fé e de que a
falha foi sanada — reforça a tese de "mero dissabor" do item seguinte), laudo técnico preliminar
quando a preliminar de incompetência depender disso.

**5. Pedido contraposto no lugar de reconvenção.** Não cabe reconvenção (art. 31, caput) — cabe
pedido contraposto, nos limites do art. 3º (competência) e desde que fundado nos **mesmos fatos**
da controvérsia (art. 31). Pessoa jurídica ré pode formular pedido contraposto (FONAJE Enunciado
31); se a causa original é de até 20 salários mínimos, o pedido contraposto pode buscar valor
**maior**, até 40 salários mínimos, desde que ambas as partes estejam assistidas por advogado
(FONAJE Enunciado 27) — sem advogado nos autos, essa forma ampliada não é admissível. Se o
consumidor desistir da ação original, o pedido contraposto cai junto (FONAJE Enunciado 173).

## Tese do consumidor × tese do fornecedor

**Tese do consumidor:** as preliminares do fornecedor tendem a ser dilatórias quando genéricas —
o Juizado existe para simplificar, e a jurisprudência do FONAJE (Enunciados 54, 70, 94) fecha a
porta para incompetência alegada sem prova concreta da complexidade probatória.

**Tese do fornecedor:** a defesa técnica no rito sumaríssimo não é menos rigorosa por ser mais
simples — cada preliminar arguida precisa vir amarrada a um fato ou documento específico do caso,
nunca como petição-modelo genérica.

## Armadilhas

- **T12** — não cabe reconvenção (cabe pedido contraposto) nem intervenção de terceiro (mata a
  denunciação da lide — art. 10). O fornecedor que quer chamar o fabricante/importador para
  dividir a responsabilidade não consegue fazer isso dentro do rito; tem de avaliar ação de
  regresso autônoma. MEI, ME e EPP podem propor ação no JEC (art. 8º, §1º, II, redação da LC
  147/2014 — o inciso que ainda cita a Lei 9.841/1999 está revogado). Preposto dispensa vínculo
  empregatício (art. 9º, §4º, redação da Lei 12.137/2009) — mas é vedado acumular preposto e
  advogado na mesma pessoa (FONAJE Enunciado 98), e o preposto sem carta de preposição precisa
  apresentá-la no prazo fixado, sob pena dos arts. 20/51, I (FONAJE Enunciado 99). Embargos de
  declaração interrompem o prazo. Não cabe rescisória. Preparo em 48 horas (art. 42, §1º).
- **T1** — a Súmula 469/STJ está cancelada; a vigente para plano de saúde é a **608/STJ**, com a
  exceção da autogestão embutida no próprio enunciado.
- Revelia de pessoa jurídica não é categoria distinta: se comparece sem contestar em causa acima
  de 20 salários mínimos (FONAJE Enunciado 11), ou contesta por escrito mas não comparece à
  audiência (FONAJE Enunciado 78), a revelia se aplica igual.

## Fronteira

Mérito clínico de negativa de cobertura (rol ANS, exclusão de tratamento) fica com este plugin na
ótica contratual/ANS; a ótica **clínica** (indicação médica, adequação terapêutica) é
`direito-medico-adv-os`. Revisional de juros/tarifas bancárias é `bancario-adv-os`. Rito comum
fora do JEC e recursos cíveis gerais são `civel-adv-os`. Validação de citação de jurisprudência
antes de uso em peça é `juris-adv-os`.

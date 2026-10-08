---
name: reducao-quantum-dano-moral-sbroggioadv
title: Redução do quantum de dano moral
description: 'Estrutura a tese de redução do quantum de dano moral do fornecedor: a distinção entre "mero dissabor" e dano moral in re ipsa, a Súmula 385/STJ (Tema 922) como arma central da defesa em negativação indevida com inscrição preexistente, os critérios de arbitramento e razoabilidade, a vedação ao enriquecimento sem causa, e o termo inicial de juros (Súmula 54/STJ) e correção monetária (Súmula 362/STJ) como argumento sobre o valor final da condenação. Traz a réplica do consumidor a cada tese de redução, porque o plugin é dual. Aciona quando o fornecedor precisar reduzir ou afastar pedido de dano moral, ou quando o consumidor precisar sustentar ou majorar o valor pleiteado.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/reducao-quantum-dano-moral
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Redução do quantum de dano moral

## Quando esta skill entra

Já foi reconhecido (ou está em discussão) o dever de indenizar por dano moral, e a disputa passa a
ser sobre **existência do dano em si** ou **valor** — diferente de [[excludentes-de-responsabilidade]],
que discute se há dever de indenizar.

## Base normativa

CDC (Lei 8.078/1990) art. 6º, VI (reparação integral) e art. 42, parágrafo único (repetição em
dobro, tratada à parte — não é o foco desta skill). Súmulas do STJ, todas vigentes e confirmadas
em `context/jurisprudencia-sumulas-temas.md`: **385** (= Tema 922), **54**, **362**.

## Mero dissabor × dano moral in re ipsa

**Tese do fornecedor:** nem todo aborrecimento contratual gera dano moral. É entendimento pacífico
do STJ que o mero dissabor, aborrecimento, irritação ou sensibilidade exacerbada não têm o condão
de gerar dano moral quando os efeitos são efêmeros e a falha foi sanada em tempo razoável (ex.:
defeito em produto resolvido pelo fornecedor sem maior prejuízo).

**Contra-ataque do consumidor:** a partir do momento em que o defeito extrapola o razoável —
reincidência, mau atendimento, tempo de espera desproporcional, humilhação — a situação sai da
esfera do mero dissabor e invade o abalo psicológico indenizável. Em **negativação indevida** e em
**falha de segurança na prestação do serviço**, a jurisprudência trata o dano como **presumido**
(in re ipsa), dispensando prova de sofrimento efetivo — o que desloca o debate para as excludentes
([[excludentes-de-responsabilidade]]), não para a existência do dano em si.

## Súmula 385/STJ (Tema 922) — a arma central da defesa em negativação

> **Texto vigente:** "Da anotação irregular em cadastro de proteção ao crédito, não cabe
> indenização por dano moral, quando preexistente legítima inscrição, ressalvado o direito ao
> cancelamento."

**Tese do fornecedor:** se o consumidor já tinha inscrição negativa legítima e anterior, uma nova
negativação — mesmo indevida — não gera dano moral novo, porque o abalo de crédito já existia.
Aplica-se inclusive quando a inscrição preexistente está sub judice, segundo entendimento
reafirmado pelo STJ em 2020: ajuizar ação discutindo a primeira negativação não afasta, por si só,
a Súmula 385.

**Contra-ataque do consumidor — flexibilização real, não hipotética:** o STJ já **afastou** a
Súmula 385 quando as inscrições anteriores também estão sendo questionadas judicialmente e há
**verossimilhança** nas alegações — não é preciso esperar o trânsito em julgado de todas as ações
anteriores. Caso real: **REsp 1.704.002** (rel. min. Nancy Andrighi, 3ª Turma), condenou banco a
indenizar consumidor que tinha outras 3 ações questionando as demais inscrições — o STJ chamou de
"círculo vicioso" que não pode servir para blindar o fornecedor. Precedente anterior no mesmo
sentido: **REsp 1.647.795** (2017).

**Trava de equilíbrio:** a presunção de legitimidade da inscrição existe até reconhecimento
judicial definitivo — o ônus de demonstrar a verossimilhança do questionamento é de quem alega, e
a Súmula 385 continua sendo a regra; a flexibilização é exceção fundamentada, não a porta padrão.

## Critérios de arbitramento e vedação ao enriquecimento sem causa

Jurisprudência consolidada e pacífica do STJ, sem controvérsia real de tese isolada — entendimento
assente em centenas de julgados:

- **Dupla finalidade:** compensar o ofendido **e** desestimular pedagogicamente o ofensor (teoria
  do desestímulo) — nunca uma das duas isoladamente.
- **Vedação a dois extremos:** o valor não pode ser fonte de enriquecimento sem causa (teto), nem
  irrisório a ponto de não cumprir a função pedagógica (piso).
- **Fatores de ponderação:** grau de culpa/dolo do agente, gravidade e extensão do dano, grau de
  sofrimento do ofendido, condição econômica das partes, reincidência do fornecedor.
- **Revisão em recurso especial:** o STJ só revê o quantum em hipóteses excepcionais — quando
  manifestamente irrisório ou exorbitante. Fora disso, a fixação é prerrogativa das instâncias
  ordinárias.

**Uso na skill:** essa é a munição para a tese de **redução** do fornecedor (nunca de exclusão
total quando o dano já está caracterizado) — pedir arbitramento dentro da faixa de razoabilidade
do tribunal local para casos análogos, e impugnar valores fora desse padrão.

## Termo inicial de juros e correção — argumento sobre o valor final

- **Súmula 54/STJ:** "Os juros moratórios fluem a partir do evento danoso, em caso de
  responsabilidade extracontratual." Vale tanto para dano material quanto moral, quando a
  responsabilidade é extracontratual. Na responsabilidade **contratual**, o marco é a citação (CC
  art. 405) — regra distinta que a peça precisa escolher corretamente conforme a natureza do
  vínculo.
- **Súmula 362/STJ:** "A correção monetária do valor da indenização do dano moral incide desde a
  data do arbitramento." Combinada com a 54, forma o par que decide o cálculo de qualquer
  condenação por dano moral: **juros ↦ evento danoso** (extracontratual) · **correção monetária ↦
  data do arbitramento** (e, se o valor mudar em instância superior, a data do **último**
  arbitramento).

**Uso estratégico:** mesmo quando o fornecedor perde a discussão sobre a existência do dano e o
quantum principal, a data correta de incidência de juros e correção pode reduzir materialmente o
valor final da condenação — argumento de cálculo, não de mérito, mas com impacto financeiro real.

## Armadilhas

- **T6** — a repetição em dobro (art. 42, parágrafo único, Tema 929/STJ) **não é** a mesma
  discussão de dano moral: desde 30/03/2021 dispensa má-fé, mas essa regra nova só vale para
  cobranças a partir dessa data — cobrança anterior segue o regime antigo (exige má-fé). Não
  confundir os dois institutos na mesma peça.
- Não citar a Súmula 385 como se fosse absoluta e sem exceção — a flexibilização real (REsp
  1.704.002, REsp 1.647.795) existe e deve ser verificada antes de fechar a porta do dano moral só
  porque existe negativação preexistente.
- Juros e correção monetária mudam de regime conforme a natureza (contratual × extracontratual) —
  aplicar a Súmula 54 a responsabilidade contratual é erro de fundamento.

## Fronteira

Cálculo de liquidação e atualização monetária aplicada à condenação (a operação aritmética em si)
é `calculosjudiciais-adv-os`. Validação de citação de jurisprudência antes de uso em peça é
`juris-adv-os`.

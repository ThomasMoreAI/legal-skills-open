---
name: dano-moral-consumo-quantum-sbroggioadv
title: Dano Moral em Consumo — Quantum
description: 'Trata o dano moral em relação de consumo — a diferença entre dano moral in re ipsa (negativação indevida, falha de segurança) e mero dissabor contratual, a Súmula 385/STJ (Tema 922) sobre inscrição preexistente legítima e sua flexibilização real, e o par de súmulas que decide o cálculo da condenação: Súmula 54/STJ (juros desde o evento danoso, extracontratual) e Súmula 362/STJ (correção monetária desde o arbitramento). Traz a tese de ampliação do consumidor e a tese de redução do fornecedor lado a lado. Aciona: ao pedir ou contestar dano moral em consumo, ou ao calcular juros e correção de uma condenação por dano moral.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/dano-moral-consumo-quantum
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Dano Moral em Consumo — Quantum

## Quando esta skill entra
Toda vez que a peça pedir (ou tiver que rebater) indenização por dano moral em relação de consumo
— negativação indevida, falha de segurança, publicidade enganosa, cobrança vexatória. Decide três
coisas: se o dano precisa de prova, quando ele é afastado mesmo sendo real, e como calcular juros
e correção da condenação.

## Base normativa e jurisprudência
- **Dano moral *in re ipsa* × mero dissabor:** não é matéria de artigo isolado do CDC, é
  jurisprudência pacífica do STJ. Em **negativação indevida** e **falha de segurança na prestação
  do serviço**, o dano é tratado como **presumido** (*in re ipsa*), dispensando prova de
  sofrimento efetivo. Mas "o mero dissabor, o aborrecimento, a irritação ou a sensibilidade
  exacerbada não têm o condão de acarretar dano moral" quando os efeitos são efêmeros e a falha
  foi sanada em tempo razoável. (fonte: `context/fornecedor-e-administrativo.md`, §1.2)
- **Súmula 385/STJ (= Tema 922/STJ):** "Da anotação irregular em cadastro de proteção ao crédito,
  não cabe indenização por dano moral, quando preexistente legítima inscrição, ressalvado o
  direito ao cancelamento." Vigente, e firmada também como tese repetitiva (Tema 922). Aplica-se
  inclusive quando a inscrição preexistente está *sub judice* — o STJ já reformou condenação por
  entender que ajuizar ação discutindo a 1ª negativação não afasta, por si só, a Súmula 385
  (2020). (fonte: `context/jurisprudencia-sumulas-temas.md`, §1.6)
- **Súmula 54/STJ** — "Os juros moratórios fluem a partir do evento danoso, em caso de
  responsabilidade **extracontratual**." Vale tanto para dano material quanto moral, inclusive
  dano moral "puro", quando a responsabilidade é extracontratual. **Na responsabilidade
  contratual, o marco é a citação (art. 405, CC)** — regra distinta.
- **Súmula 362/STJ** — "A correção monetária do valor da indenização do dano moral incide desde a
  data do **arbitramento**." Combinada com a 54, forma o par que decide o cálculo: **juros ↦
  evento danoso** (extracontratual) · **correção monetária ↦ data do arbitramento** (e, se o valor
  mudar em instância superior, a data do **último** arbitramento).
(fonte: `context/jurisprudencia-sumulas-temas.md`, §§1.7-1.8)

## O teste / o passo a passo
1. O dano é **in re ipsa** (negativação indevida, falha de segurança) ou exige prova de sofrimento
   (mero aborrecimento contratual sanado a tempo)? Classifique antes de pedir ou contestar.
2. Havia inscrição **preexistente e legítima**? Se sim, checar a Súmula 385 — a nova negativação,
   mesmo indevida, pode não gerar dano moral novo, **salvo** se a inscrição preexistente também
   estiver sendo questionada judicialmente com verossimilhança (flexibilização real do STJ, não
   hipotética).
3. A responsabilidade é **contratual** ou **extracontratual**? Decide o marco dos juros (citação ×
   evento danoso) — a correção monetária, em qualquer caso, corre do arbitramento (Súmula 362).
4. Arbitramento do valor: dupla finalidade (compensar **e** desestimular pedagogicamente),
   vedados os dois extremos (enriquecimento sem causa × valor irrisório), ponderando grau de
   culpa, gravidade e extensão do dano, sofrimento do ofendido, condição econômica das partes e
   reincidência do fornecedor.

## Tese do consumidor
Buscar o enquadramento *in re ipsa* sempre que a hipótese for negativação ou falha de segurança —
dispensa prova de sofrimento. Se houver inscrição preexistente, argumentar que ela está sendo
questionada judicialmente com verossimilhança, para afastar a Súmula 385 (fundamento: o STJ já
reconheceu que exigir trânsito em julgado de **todas** as ações anteriores cria um "círculo
vicioso" que não pode impedir a nova indenização). Pedir juros desde o evento danoso quando a
responsabilidade for extracontratual.

## Tese do fornecedor (redução do quantum)
Invocar "mero dissabor" quando o defeito foi sanado em tempo razoável e não houve reincidência,
humilhação ou tempo de espera desproporcional. Invocar a Súmula 385 de frente quando houver
inscrição preexistente legítima e não questionada, lembrando que a **presunção de legitimidade da
inscrição existe até reconhecimento judicial definitivo** — o ônus de demonstrar a verossimilhança
do questionamento é de quem alega. Impugnar o quantum fora da faixa de razoabilidade praticada
pelo tribunal local em casos análogos — o STJ só revê o valor em recurso especial quando
manifestamente irrisório ou exorbitante; fora disso, é prerrogativa das instâncias ordinárias.

## Armadilhas
- Aplicar juros desde o evento danoso (Súmula 54) em responsabilidade **contratual** — o marco
  correto ali é a citação (art. 405, CC).
- Tratar a Súmula 385 como automática, ignorando a flexibilização quando a inscrição preexistente
  está sendo questionada com verossimilhança.
- **T13** — normalizar espaço em branco ao conferir citação literal contra os anexos.

## Fronteira
Cálculo efetivo de juros/correção sobre a condenação: `calculosjudiciais-adv-os`. Dano moral em
contexto de erro médico (mérito clínico): `direito-medico-adv-os`.

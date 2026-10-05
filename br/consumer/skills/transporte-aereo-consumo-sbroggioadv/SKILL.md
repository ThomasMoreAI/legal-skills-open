---
name: transporte-aereo-consumo-sbroggioadv
title: Transporte aéreo — consumo
description: 'Trata a relação de consumo no transporte aéreo: atraso e cancelamento de voo, overbooking (preterição de embarque), extravio e avaria de bagagem. Aplica a responsabilidade objetiva do CDC (art. 14) e a fronteira exata entre a Convenção de Montreal e o CDC — a Convenção só tarifa o dano MATERIAL (Tema 210/STF); o dano MORAL segue o CDC, com reparação integral (STJ, REsp 1.842.066). Escreve os dois lados: tese do passageiro e tese da companhia aérea (excludentes do art. 14, §3º, prova do fato, dever de assistência material e reacomodação). Aciona quando o usuário trouxer atraso de voo, cancelamento, overbooking, preterição de embarque, extravio de bagagem, avaria de bagagem, indenização contra companhia aérea, ou pedir a defesa de uma companhia aérea nesses casos.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/transporte-aereo-consumo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Transporte aéreo — consumo

## Quando esta skill entra

Qualquer disputa entre passageiro e companhia aérea (ou agência de viagem, quando
for o caso) por atraso, cancelamento, overbooking, extravio ou avaria de bagagem em
voo doméstico ou internacional. Não cobre matéria puramente contratual de pacote
turístico sem transporte aéreo — aí a base é o CDC geral, não este recorte.

## Base normativa

- **CDC art. 14** — responsabilidade objetiva do fornecedor de serviços; o serviço é
  defeituoso quando não dá a segurança que o consumidor pode esperar (§1º).
  Excludentes taxativas no §3º: (I) prova de que o defeito inexiste; (II) culpa
  exclusiva do consumidor ou de terceiro.
- **Convenção de Montreal** (Decreto 5.910/2006) — norma especial para transporte
  aéreo internacional, com prevalência sobre o CDC por força do art. 178 da CF
  (**Tema 210/STF**, RE 636.331, mérito 25/05/2017).
- **CDC art. 6º, VI e VII** — reparação integral de dano material e moral.

## T11 — a trava central desta skill

**A prevalência da Convenção sobre o CDC (Tema 210/STF) vale só para a tarifação do
dano MATERIAL.** O dano MORAL segue o CDC, com reparação integral — é entendimento
consolidado da 3ª Turma do STJ:

> "A Convenção de Montreal não pode ser aplicada para limitar a indenização devida
> aos passageiros em caso de danos morais decorrentes de atraso de voo ou extravio
> de bagagem, tendo em vista que o tratado internacional alcança apenas as
> hipóteses de dano material." — STJ, 3ª Turma, REsp 1.842.066 (Rel. Min. Moura
> Ribeiro).

Aplicar o teto da Convenção ao dano moral é **errar a favor da companhia aérea** —
o erro mais comum de quem confia na memória em vez de checar a tese vigente.
Vale só para voo internacional; voo doméstico segue CDC integralmente, sem a
camada da Convenção.

## O teste / passo a passo

1. **Voo doméstico ou internacional?** Doméstico → CDC puro. Internacional → CDC +
   Convenção de Montreal, com a separação de T11 (material × moral).
2. **Qual o fato gerador?** Atraso, cancelamento, overbooking, extravio ou avaria —
   cada um tem um patamar de dano moral diferente na prática dos tribunais (o
   extravio definitivo de bagagem tende a pesar mais que um atraso de poucas horas
   com assistência prestada), mas isso é gradação de arbitramento, não regra fixa
   deste corpus — não afirme faixa de valor em R$ sem fonte específica do caso.
3. **A companhia prestou assistência material?** (alimentação, hospedagem,
   comunicação, reacomodação) — a ausência de assistência é fato que agrava o dano
   moral e enfraquece a defesa da excludente.
4. **Há excludente do art. 14, §3º?** Só as duas hipóteses taxativas — condição
   meteorológica extrema, greve de terceiro alheio à companhia ou determinação de
   autoridade aeroportuária podem, a depender da prova concreta, configurar caso
   fortuito/força maior externo; o ônus da prova é da companhia.

## Tese do passageiro (consumidor)

- Responsabilidade objetiva do art. 14 — não precisa provar culpa, só o defeito do
  serviço e o dano.
- Dano moral in re ipsa em extravio definitivo e em preterição de embarque
  (overbooking), pela quebra da legítima expectativa e pela frustração da viagem.
- Reparação integral do dano moral mesmo em voo internacional — a Convenção não o
  alcança (T11).
- Ausência ou insuficiência de assistência material (alimentação/hospedagem) como
  fato agravante autônomo.

## Tese da companhia aérea (defesa)

- Excludentes do art. 14, §3º — culpa exclusiva de terceiro (ex.: fechamento de
  espaço aéreo por autoridade, condição meteorológica documentada) ou prova de
  ausência de defeito.
- Em voo internacional, invocar o teto da Convenção de Montreal **apenas** para o
  dano material (bagagem extraviada com valor declarado, por exemplo) — nunca para
  o dano moral, sob pena de a tese ser rejeitada de plano por T11.
- Prova de que prestou assistência material e reacomodação tempestiva — reduz o
  quantum do dano moral, não o afasta por completo se houve dano configurado.
- Mero atraso de curta duração, com assistência prestada e sem prova de dano
  concreto, pode configurar "mero dissabor" — mas essa tese não é presumida; exige
  prova de que a companhia cumpriu seus deveres de informação e assistência.

## Armadilhas

- **T11** — nunca aplicar o teto da Convenção ao dano moral.
- Não fixar valor de indenização em R$ como se fosse tabela legal — arbitramento é
  judicial, caso a caso.
- Não tratar overbooking como "risco do negócio" sem dano — a preterição de
  embarque contra a vontade do passageiro é fato gerador autônomo de dano moral na
  jurisprudência consolidada.

## Fronteira

Extravio de bagagem com repercussão puramente patrimonial de alto valor (carga
comercial, por exemplo) sem relação de consumo pode migrar para `civel-adv-os`
(responsabilidade civil geral). Cálculo de liquidação de indenização já fixada →
`calculosjudiciais-adv-os`. Validação de citação de jurisprudência → `juris-adv-os`.

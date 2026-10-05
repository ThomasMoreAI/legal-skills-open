---
name: protesto-e-cobranca-extrajudicial-sbroggioadv
title: protesto-e-cobranca-extrajudicial — a esteira que continua depois que a judicial para
description: 'A via que sobra quando a triagem diz "não ajuíze" por falta de interesse/baixo valor: protesto, negativação e cobrança administrativa como esteira própria de recuperação de crédito, não como consolo. Monta o fluxo pela ótica do ente com o que a inscrição já garante pela LEF (suspensão da prescrição por 180 dias, presunção relativa de certeza e liquidez, os requisitos que tornam a CDA apta, cancelamento sem ônus) e faz o par obrigatório com a triagem de baixo valor — triagem sem via alternativa é abandono de crédito. DECLARA o próprio limite: a base legal específica do protesto de CDA e o precedente que a chancelou NÃO constam dos anexos e saem como [VERIFICAR], a conferir na fonte. Aciona: "protesto da CDA", "protestar a dívida ativa", "negativar o devedor", "cobrança administrativa", "cobrar sem processo".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/protesto-e-cobranca-extrajudicial
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: tax
language: pt
---

# protesto-e-cobranca-extrajudicial — a esteira que continua depois que a judicial para

Quando a `triagem-baixo-valor` diz "este crédito não paga o processo" por falta de interesse, a resposta correta **não** é
arquivar a cobrança: é mudar de esteira. Protesto da CDA, negativação e cobrança administrativa são
o que separa **eficiência administrativa** de **renúncia de receita** — e é por isso que estas duas
skills andam juntas, sempre.

**Exceção absoluta:** se houve reconhecimento de prescrição no fluxo do art. 1º-B da Res. CNJ 547
consolidada, o §4º veda nova cobrança administrativa ou judicial do crédito alcançado. Essa rota
**não entra** nesta skill; apenas a parcela não prescrita conserva medidas cabíveis (§5º).

Este produto atende o **Estado**; o crédito é de ICMS, IPVA, ITCMD e demais créditos estaduais.

## ⚠️ 1. O limite desta skill, declarado antes de qualquer orientação

O `context/` deste produto **não contém** a lei específica que disciplina o protesto de títulos e
documentos de dívida, nem o precedente que examinou o protesto de certidão de dívida ativa, nem
prazo cartorário, nem tabela de emolumentos, nem norma sobre negativação e proteção de dados do
devedor. Foi conferido: a busca por esses termos nos anexos **não retorna nada**.

Consequência, por P2 e sem exceção:

- **Base legal do protesto de CDA** → `[VERIFICAR]` na fonte primária. O produto **não** escreve
  número de lei, artigo ou parágrafo de memória.
- **Precedente que chancelou o protesto de CDA** → `[VERIFICAR]`. Nenhum número de ADI, tema ou
  súmula sai daqui sem lastro.
- **Prazos, emolumentos, custos de cartório e procedimento de negativação** → `[VERIFICAR]`, e
  dependem também de norma do ente e do estado (P5).

Isso **não esvazia a skill**: o que ela entrega é o **método de gestão do crédito** e as âncoras que
**existem** nos anexos — a LEF sobre inscrição e CDA, a triagem com os números medidos, e a LINDB
como base do ato normativo interno que vai reger a política. O que falta é nomeado; o que existe é
usado. Antes de virar produto, esta skill recebe o anexo próprio da base legal do protesto.

## 2. O que os anexos JÁ garantem (e é bastante)

Da Lei 6.830/80 (`context/lef-6830.md`), quatro fatos que sustentam a cobrança extrajudicial:

| Âncora | O que dá |
|---|---|
| **Art. 2º §3º** | A inscrição é "**ato de controle administrativo da legalidade**", feita pelo órgão competente para apurar **liquidez e certeza**, e **suspende a prescrição por 180 dias, ou até a distribuição da execução, se esta ocorrer antes** |
| **Art. 3º** | A dívida regularmente inscrita **goza de presunção de certeza e liquidez** — relativa, ilidível por prova inequívoca a cargo do executado |
| **Art. 2º §§5º-6º** | Os seis requisitos do Termo de Inscrição, repetidos na CDA autenticada: devedor e **co-responsáveis** · valor originário e **forma de calcular** encargos · origem, natureza e fundamento · atualização · data e número da inscrição · processo administrativo ou auto de infração |
| **Art. 26** | Cancelada a inscrição antes da decisão de primeira instância, a execução é **extinta sem qualquer ônus para as partes** |

Leia o conjunto pela ótica da cobrança: **a CDA é título formado por ato de controle de legalidade,
com presunção de certeza e liquidez** — é essa qualidade, e não a distribuição de um processo, que
faz dela um instrumento de cobrança. E o **§3º impõe o relógio**: a suspensão de 180 dias corre a
partir da inscrição, então a decisão "protesto ou ajuizamento" é tomada **dentro** dessa janela, não
depois dela.

E do §5º vem a régua de qualidade: **CDA que não está apta a executar também não está apta a
protestar.** Antes de encaminhar qualquer crédito à esteira extrajudicial, os seis incisos são
conferidos — especialmente o **II** (forma de calcular os encargos, não só o valor final) e o **I**
(co-responsáveis nomeados desde a origem).

## 3. O par com a triagem — o fluxo completo

```
crédito inscrito em dívida ativa
        │
        ├── passa no crivo de valor?  ── SIM ──▶  execucao-fiscal-lef  (esteira judicial)
        │
        └── NÃO (baixo valor/falta de interesse) ──▶  ESTEIRA EXTRAJUDICIAL
                                             ├── cobrança administrativa (notificação, parcelamento)
                                             ├── protesto da CDA            [base legal: VERIFICAR]
                                             └── negativação                [base: VERIFICAR]

prescrição reconhecida (art. 1º-B §4º) ──▶ NÃO protestar, negativar nem cobrar novamente
```

Os números que justificam o desvio estão em `context/resolucoes-cnj-execucao.md` e valem citados
exatos: custo mínimo de uma execução ≈ **R$ 9.277,00**; **52,3%** das execuções pendentes abaixo de
R$ 10.000; **mais de 13 milhões** extintas entre out/2023 e jul/2025; acervo nacional **−26,4%**; e
o caso **Salvador/BA**, citado nominalmente pelo CNJ, com **−51%** de acervo e **+87%** de
arrecadação no mesmo período.

**Salvador é o argumento inteiro desta skill em um dado.** A arrecadação não subiu apesar da queda
do acervo — subiu porque a estrutura que estava ocupada com processo que não se paga passou a ser
usada em cobrança que se paga. A triagem só produz esse efeito **quando há esteira extrajudicial do
outro lado**; sem ela, o acervo cai e a arrecadação cai junto.

## 4. Como estruturar a política (o que o procurador precisa decidir)

O produto não decide por ele; organiza as decisões e aponta onde cada uma se ancora:

1. **Faixa de corte.** Abaixo de quanto não se ajuíza? O parâmetro nacional medido é ≈ R$ 9.277,00;
   o **custo real do ente** e o **piso adotado** são `[VERIFICAR]` — dependem de levantamento e de
   ato do ente.
2. **Escalonamento da cobrança.** Notificação administrativa → oferta de parcelamento → protesto →
   negativação → reavaliação para ajuizamento se o valor for atualizado ou se aparecer patrimônio.
   A ordem é decisão de política; o produto sugere, não impõe.
3. **Gatilho de retorno à via judicial.** Crédito consolidado que ultrapasse a faixa, ou devedor com
   bem identificado, volta para `execucao-fiscal-lef`. A triagem não é decisão definitiva sobre o
   crédito, é decisão sobre **a via de hoje**.
4. **O instrumento normativo.** A política vira ato interno, e a LINDB dá a base
   (`context/lindb-20-30.md`): **art. 30** — as autoridades devem atuar para aumentar a segurança
   jurídica, inclusive por **regulamentos, súmulas administrativas e respostas a consultas**, com
   **caráter vinculante em relação ao órgão até ulterior revisão**; **art. 26** — compromisso com os
   interessados, após **oitiva do órgão jurídico**, eficaz a partir da **publicação oficial**, e que
   **não pode conferir desoneração permanente** de dever (§1º, III); **art. 20** — a motivação
   demonstra necessidade, adequação e **as alternativas consideradas**, que é exatamente o que
   fundamenta a escolha da via extrajudicial.
5. **Medição.** Acervo antes/depois, arrecadação antes/depois. Sem medir, a política não se defende
   perante o controle — e é a medição que transforma "deixamos de cobrar" em "cobramos melhor".

## 5. A linguagem que protege o ente

Em ofício, parecer e recomendação, o enquadramento é fixo e literal:

- **É eficiência administrativa**, com base no interesse de agir (Tema 1184/STF) — **não é renúncia
  de receita**, que tem regime e responsabilidade próprios do gestor.
- **O crédito permanece exigível** e continua sendo cobrado por outra via; a inscrição não é
  cancelada por essa decisão (o cancelamento é outro ato, com o efeito do art. 26 da LEF).
- **O benefício ao devedor é efeito, nunca o objetivo declarado.** O ângulo é o de quem cobra.

## Travas desta skill

- **P2 — e aqui ela é o assunto principal.** Base legal do protesto de CDA, precedente que a
  examinou, prazos e emolumentos cartorários e regras de negativação **não estão nos anexos** →
  `[VERIFICAR]`, sempre, sem uma única exceção. Esta skill declara o próprio buraco em vez de
  preenchê-lo com memória.
- **P5.** Piso de valor, procedimento de protesto e política de cobrança dependem de **norma do
  ente** (e, no protesto, também de norma estadual/cartorária): o produto pergunta, nunca presume.
- **Triagem nunca sai sem esta via.** Recomendar não ajuizar sem nomear a esteira extrajudicial é o
  que transforma eficiência em abandono de crédito.
- **P1.** O método vale nas três esferas; o crédito é de ICMS, IPVA, ITCMD e demais créditos estaduais.
- **P4.** Minuta de ofício, notificação ou ato normativo é estudo e trabalho local — a assinatura, a
  publicação e a responsabilidade pela política são do procurador e do gestor, indelegáveis. Dado
  pessoal de devedor fica local e mascarado (`conformidade-ia-institucional`).

**Próximo passo:** a decisão de não ajuizar e os números que a sustentam → `triagem-baixo-valor`. O
crédito que passou no crivo → `execucao-fiscal-lef`. O ato normativo que formaliza a política →
`lindb-como-metodo` e `parecer-consultivo`. Toda entrega fecha por `suprema-corte-fazendaria`.

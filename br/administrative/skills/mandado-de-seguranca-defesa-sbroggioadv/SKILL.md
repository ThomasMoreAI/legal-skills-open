---
name: mandado-de-seguranca-defesa-sbroggioadv
title: mandado-de-seguranca-defesa — as informações e a defesa do ente
description: 'O mandado de segurança contra autoridade do Estado, pelos dois papéis que a peça não pode confundir: as informações da autoridade coatora e a manifestação do ente, pessoa jurídica de direito público. Organiza a resposta em quatro frentes — legitimidade (quem é a autoridade coatora de verdade e o efeito de apontá-la errado), prazo decadencial, ausência de direito líquido e certo por falta de prova pré-constituída, e mérito do ato. Trata à parte os limites da liminar contra o Poder Público: a Lei 9.494/97 disciplina a tutela antecipada contra a Fazenda Pública e remete às restrições do art. 1º da Lei 8.437/92. Traz também a aplicação mais direta da trava P7 — o rito do MS tem prazos próprios em lei específica, e o CPC 183 §2º afasta o dobro onde eles existem. A lei do mandado de segurança não consta dos anexos: todo dispositivo dela sai [VERIFICAR]. Aciona: "informações da autoridade coatora", "defesa em mandado de segurança", "impetraram MS contra o secretário", "cabe liminar
  contra o ente?".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/mandado-de-seguranca-defesa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# mandado-de-seguranca-defesa — as informações e a defesa do ente

Este produto atende o **Estado**. No mandado de segurança a procuradoria trabalha em **dois
papéis distintos**, e a maior parte dos defeitos desta peça nasce de embaralhá-los:

| Papel | Quem fala | O que a peça é |
|---|---|---|
| **Informações** | A **autoridade coatora**, na primeira pessoa do órgão, assessorada pela procuradoria | Prestação de contas do ato: o que foi feito, com que fundamento normativo e em que processo administrativo |
| **Manifestação do ente** | A **pessoa jurídica de direito público** a que a autoridade se vincula | Defesa jurídica: preliminares, tese, e a posição processual do ente na causa |

As informações não são a contestação do ente, e a manifestação do ente não fala pela autoridade.
Misturar as duas produz uma peça que o juízo lê como defesa de interesse próprio do agente.

⚠️ **Aviso de lastro, dito de saída.** A **lei do mandado de segurança não consta dos anexos deste
produto** — controle negativo aplicado, zero ocorrências no `context/`. Consequência prática e sem
rodeio: **prazo decadencial, prazo das informações, hipóteses de não cabimento, regime da liminar no
MS, litisconsórcio e a regra própria de remessa necessária deste rito saem todos `[VERIFICAR]`**. A
skill entrega a arquitetura da resposta e o que já tem lastro; o dispositivo vem da fonte primária,
conferido pelo procurador (trava **P2**).

## Quando esta skill entra

- Chegou notificação para prestar informações em MS contra autoridade do Estado.
- O ente foi cientificado para ingressar no feito e a procuradoria vai se manifestar.
- Foi deferida — ou está pedida — liminar contra o Poder Público e é preciso avaliar a via.

## 1. Prazo — a aplicação mais direta da trava P7

O **CPC art. 183** (verbatim em `context/prerrogativas-cpc.md`) dá ao ente prazo em dobro contado da
intimação pessoal, **mas o §2º é literal**: *"Não se aplica o benefício da contagem em dobro quando
a lei estabelecer, de forma expressa, prazo próprio para o ente público."*

O rito do mandado de segurança é regido por **lei específica**, que fixa prazos próprios — este é o
cenário-tipo do §2º, não a exceção rara. **Nunca conte em dobro no MS por hábito.** Localize o prazo
próprio na lei do rito (`[VERIFICAR]`: dispositivo e contagem) e só então decida. Errar aqui não
produz uma tese fraca: produz peça intempestiva.

## 2. Legitimidade — quem é a autoridade coatora

A frente mais produtiva da resposta, porque é factual e verificável no processo administrativo.

- **Autoridade coatora é quem pratica o ato ou de quem emana a ordem** — não o superior hierárquico
  que apenas ratifica, nem o órgão em abstrato. `[VERIFICAR]` o dispositivo que define o conceito e
  o efeito processual de apontá-la errado (extinção sem mérito? emenda? teoria da encampação?) — as
  três respostas circulam na prática e **nenhuma delas tem lastro aqui**.
- Levante no processo administrativo **quem assinou, em que competência e com que delegação**. É a
  prova que sustenta a preliminar; alegação de ilegitimidade sem o documento cai.
- Se a autoridade indicada é do Estado mas o ato foi praticado por outro ente ou por delegatário,
  diga isso com o documento — e verifique se o pedido correto é ilegitimidade ou incompetência.

## 3. Prazo decadencial da impetração

Há prazo decadencial para impetrar, contado do ato impugnado. **O número de dias e o dispositivo não
constam dos anexos → `[VERIFICAR]`.** O que a skill orienta com segurança é o **trabalho de fato**:

- Fixe a **data do ato** e a **data da ciência do impetrante** com documento do processo
  administrativo (publicação, intimação, protocolo, recibo).
- Distinga **ato único** de **relação de trato sucessivo** — a distinção decide se o prazo já correu
  inteiro ou se renova. `[VERIFICAR]` os precedentes antes de nomeá-los.
- Ato **omissivo** e ato de efeitos permanentes pedem análise própria do termo inicial.

## 4. Direito líquido e certo — a frente técnica do rito

O mandado de segurança exige **prova pré-constituída**: o direito tem de estar demonstrado por
documento já nos autos, sem instrução. Daí a preliminar mais própria do rito: **o que o impetrante
alega depende de dilação probatória, logo não há direito líquido e certo.**

Roteiro: liste cada afirmação de fato da inicial e aponte, uma a uma, **qual documento a
comprovaria e se ele está anexado**. Onde a resposta é "seria preciso perícia, testemunha ou
apuração", a via está errada — e essa é uma extinção sem exame do mérito, não uma derrota do ente.
O dispositivo que ampara a preliminar → `[VERIFICAR]`.

## 5. Liminar contra o Poder Público — o que tem lastro e o que não tem

**Com lastro de vigência:** a **Lei 9.494/97** disciplina a tutela antecipada contra a
Fazenda Pública e **remete às restrições do art. 1º da Lei 8.437/92**, que veda liminar contra o
Poder Público em certas matérias.

**Sem lastro → `[VERIFICAR]`:** o **rol** das matérias vedadas · a aplicação dessas restrições ao
rito do MS · exigência de oitiva prévia do representante judicial · caução ou garantia · e o
instrumento de **suspensão de liminar/segurança** dirigido à presidência do tribunal (existência,
requisitos e via) — **nada disso consta dos anexos**, e é justamente onde o erro de citação é mais
caro, porque a peça vai ao presidente do tribunal.

Conduta: sustente a **inadequação da liminar pelo caso concreto** — ausência de perigo na demora,
irreversibilidade da medida, efeito multiplicador sobre o orçamento — e só cite o dispositivo depois
de conferir. Argumento de fato bem construído não depende do artigo certo; citação errada, sim,
compromete os dois.

## 6. Mérito — a defesa do ato administrativo

- **Fundamento normativo do ato**, com a norma e o processo administrativo que o precedeu.
- **Competência e forma** — atacadas de rotina em MS; responda com o documento.
- **Ato antigo ou mudança de orientação**: a LINDB é a arma anchorada. **Art. 24** — a validade do
  ato já consumado se julga pelas **orientações gerais da época** (o parágrafo único define o que
  conta como tal); **art. 23** — orientação nova que impõe novo dever exige **regime de transição**;
  **art. 22** — na interpretação de normas de gestão pública consideram-se os obstáculos e as
  dificuldades reais do gestor. Ver `lindb-como-metodo`.
- **Contra a invalidação genérica**: **arts. 20 e 21** — não se decide por valor jurídico abstrato
  sem considerar as consequências práticas, e a motivação demonstrará a necessidade e a adequação da
  medida, inclusive em face das possíveis alternativas.

## 7. Sentença, recurso e remessa

O rito do MS tem **regra própria de remessa necessária** (`[VERIFICAR]`), que convive com o **CPC
art. 496**. Duas leituras do anexo que valem em qualquer cenário: a dispensa do §3º exige valor
**certo e líquido** (em MS, frequentemente não há), e o **§4º** dispensa independentemente do valor
quando a sentença se funda em súmula de tribunal superior, repetitivo, IRDR/IAC ou **orientação
vinculante do próprio ente**. Antes de recorrer, rode a tese pelo `suprema-corte-fazendaria`: recurso
contra entendimento já pacificado contra o ente é custo sem retorno (trava **P3**).

## Travas desta skill

- **P2** — a lei do MS não está nos anexos: **todo** dispositivo dela sai `[VERIFICAR]`. Prazo,
  cabimento, liminar, litisconsórcio e remessa própria do rito, sem exceção.
- **P7** — no MS o dobro do CPC 183 **provavelmente não se aplica**; localize o prazo próprio antes
  de contar. É a hipótese literal do §2º.
- **P3** — tese e recurso passam pelo `suprema-corte-fazendaria` antes de sair.
- **P1** — nenhuma matéria de outra esfera entra, nem em exemplo de ato impugnado.
- **P5** — nada sobre honorários do procurador ou regime funcional da autoridade por analogia.
- **P4** — a minuta sai completa, com o lembrete de revisão humana obrigatória e responsabilidade
  indelegável; as informações são assinadas **pela autoridade**, não pela ferramenta.

## Cross-links

`prerrogativas-processuais` (CPC 183 e 496 aprofundados) · `lindb-como-metodo` (arts. 20-24 na
defesa do ato) · `defesa-do-ente-contestacao` (quando a via correta era a ação de rito comum) ·
`saude-judicializada` (MS de saúde entra por lá — Tema 793/STF) · `acoes-de-massa` (MS repetido
sobre a mesma matéria) · `parecer-consultivo` (o ato que gerou o MS costuma ter parecer) ·
`conformidade-ia-institucional` (a peça sai do gabinete) · `suprema-corte-fazendaria` (**QA
obrigatória no fecho**) · `estilo-e-fronteiras`.
Fora da casa: `civel-adv-os` · `juris-adv-os` (validação de citação).

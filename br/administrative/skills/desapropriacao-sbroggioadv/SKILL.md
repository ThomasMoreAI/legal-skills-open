---
name: desapropriacao-sbroggioadv
title: desapropriacao — o ente que expropria
description: 'A desapropriação pela ótica do Estado EXPROPRIANTE — quem declara, quem imite e quem paga — do Decreto-Lei 3.365/41, alterado pela Lei 14.620/2023. Percorre as quatro fases em que o trabalho da procuradoria se divide (declaração de utilidade pública, fase executória por acordo ou ação, imissão provisória na posse, e a fixação da justa indenização) e trata à parte os quatro pontos em que o processo se perde no valor, não no direito: laudo e avaliação, juros compensatórios, juros moratórios e honorários — estes com regime próprio em lei específica, raciocínio idêntico ao da trava P7 sobre o CPC 183 §2º, e por isso o CPC 85 §3º não se aplica por presunção. Também a desapropriação indireta, em que o ente é réu. Só o diploma e sua alteração têm lastro nos anexos: todo dispositivo, súmula e tema sai [VERIFICAR], e a skill diz exatamente o que falta capturar. Aciona: "desapropriar um imóvel", "imissão na posse", "justa indenização", "juros compensatórios", "desapropriação indireta
  contra o ente".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/desapropriacao
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# desapropriacao — o ente que expropria

Este produto atende o **Estado**. A desapropriação é a matéria em que o ente costuma **ganhar o
direito e perder o valor**: a utilidade pública raramente é derrubada, e a conta final se decide na
avaliação e nos acessórios. Esta skill organiza o processo por esse eixo.

## Aviso de lastro, dito de saída

**Com lastro** (vigência ✅ conferida no Planalto): o **Decreto-Lei 3.365/41**, **alterado
pela Lei 14.620/2023**, é o diploma da desapropriação por utilidade pública. **Nome, vigência e a
alteração podem ser citados.**

⚠️ **Sem lastro → `[VERIFICAR]`, sem exceção:** **nenhum dispositivo** do DL 3.365/41 consta do
`context/` deste produto — nem o rol de hipóteses de utilidade pública, nem o prazo de caducidade da
declaração, nem o regime da imissão provisória, nem a regra de juros compensatórios, nem a de
honorários, nem a limitação da matéria alegável em contestação. Também não constam: o fundamento
constitucional da prévia e justa indenização, o regime da **desapropriação por interesse social**, a
**retrocessão**, a **desapropriação indireta**, e **toda** a jurisprudência da matéria (súmulas e
temas sobre juros, base de cálculo, honorários e prescrição).

**O que a skill entrega, então:** a arquitetura do processo, o roteiro de trabalho por fase, e a
lista nomeada do que precisa ser capturado para fechar cada `[VERIFICAR]`. É a trava **P2** operando
numa camada que a pesquisa cobriu por título, não por artigo — dito na cara, não escondido.

## As quatro fases

### 1. Declaração de utilidade pública

Ato do Executivo que **declara** o bem de utilidade pública e abre o direito de o ente promover a
desapropriação. Trabalho da procuradoria aqui é **preventivo e é onde se ganha o processo inteiro**:

- **Identificação do bem** — matrícula, confrontações, área exata, benfeitorias, ocupantes. Erro de
  descrição contamina a imissão, a perícia e o registro.
- **Motivação do ato** — qual finalidade pública concreta, com o projeto que a sustenta. Declaração
  motivada por finalidade genérica é o flanco aberto para a anulatória.
- **Prazo de validade da declaração** — há prazo de caducidade: `[VERIFICAR]` o dispositivo e a
  contagem. Deixar caducar obriga a refazer tudo.
- **Orçamento** — a indenização é **prévia**: sem previsão de recurso, a fase executória trava.

Quando se discute anulação da declaração, a **LINDB arts. 20 e 21** (verbatim em
`context/lindb-20-30.md`) sustentam a defesa: não se decide por valores jurídicos abstratos sem
considerar as **consequências práticas**, e a decisão que invalida **deverá indicar de modo expresso**
suas consequências jurídicas e administrativas.

### 2. Fase executória — acordo antes da ação

**O acordo administrativo é quase sempre melhor para o ente** do que a ação, e é a alternativa que
mais se despreza. Compare, com números na mesa: valor do acordo × valor provável da perícia **+
juros + honorários + tempo**. A **LINDB art. 26** dá base ao compromisso celebrado *após oitiva do
órgão jurídico*, com efeitos a partir da **publicação oficial**, exigindo clareza sobre obrigações,
prazo e sanções (§1º IV) — lembrando que **§1º II e §2º são VETADOS**, sem texto.

Não havendo acordo, ação de desapropriação. ⚠️ **`[VERIFICAR]`:** rito, requisitos da inicial,
depósito prévio, e a **limitação da matéria alegável em contestação** — a regra de que a defesa se
restringe a vício processual e ao preço é central nesta matéria e **precisa ser conferida no
dispositivo**, jamais afirmada de memória.

### 3. Imissão provisória na posse

É o que o ente realmente quer no curto prazo: entrar na posse antes do fim da discussão sobre valor.
⚠️ **`[VERIFICAR]` integral:** requisitos (alegação de urgência, prazo para requerer, depósito e seu
critério de cálculo), possibilidade de levantamento pelo expropriado e percentual levantável.

Trabalho que independe do dispositivo: instruir o pedido com **avaliação técnica consistente** e com
a **prova da urgência concreta** (cronograma da obra, contrato assinado, risco documentado). Imissão
negada por instrução pobre atrasa a obra e encarece a indenização pelos juros.

### 4. Justa indenização — onde o processo se decide

**Roteiro da avaliação, do que mais move o valor:**

| Item | O que o ente confere |
|---|---|
| **Metodologia** | O laudo diz qual método usou e por quê? Amostra de mercado comparável, contemporânea e documentada? |
| **Data-base** | A avaliação está referida a que data, e como se atualiza até o pagamento? |
| **Destinação** | O valor foi apurado pelo uso **atual** e regular do bem, ou por potencial futuro que ainda dependeria de aprovação? |
| **Benfeitorias** | Discriminadas, comprovadas, e anteriores à declaração? |
| **Área remanescente** | Há desvalorização alegada do que sobrou, e ela está demonstrada tecnicamente? |

**Contra-laudo é regra, não exceção.** Impugnar o laudo pericial só com argumento jurídico, sem
avaliação técnica do ente, é entregar o valor.

## Os quatro acessórios — e a lógica que os governa

É aqui que a conta cresce, e é aqui que a skill mais precisa da conferência:

1. **Juros compensatórios** — devidos pela perda antecipada da posse. `[VERIFICAR]` percentual, base
   de cálculo, termo inicial e final, e o histórico de alterações do dispositivo — matéria com
   redação alterada e jurisprudência própria, ambas fora dos anexos.
2. **Juros moratórios** — pelo atraso no pagamento. `[VERIFICAR]` percentual e termo inicial, e a
   regra de cumulação com os compensatórios.
3. **Correção monetária** — índice e periodicidade: `[VERIFICAR]`.
4. **Honorários** — ⚠️ **atenção especial.** A desapropriação tem **regime próprio de honorários em
   lei específica**, com percentuais e teto distintos da regra geral. **Não presuma o CPC art. 85
   §3º.** O raciocínio é o mesmo da trava **P7** (CPC 183 §2º: lei específica que fixa regra própria
   afasta a regra geral) — aplicado aqui aos honorários em vez do prazo. `[VERIFICAR]` o dispositivo,
   os percentuais e o teto antes de calcular qualquer coisa.

## Desapropriação indireta — quando o ente é réu

O ente ocupou ou afetou o bem **sem** o processo devido, e o particular cobra a indenização. Inverte
tudo: aqui a procuradoria **defende**, e a estrutura é a de `defesa-do-ente-contestacao`.

Frentes: houve efetivo **apossamento** ou apenas limitação administrativa (que não indeniza como
desapropriação)? Há **prova da titularidade** e da área? Qual o **prazo prescricional** aplicável
(`[VERIFICAR]` — é matéria de súmula, fora dos anexos)? O valor pedido observa a **data do
apossamento**?

## Pagamento

Acordo e depósito da imissão são pagos na fase própria. **Condenação judicial em dinheiro contra o
ente entra no regime de precatório e RPV** — `precatorios-e-rpv`, com as travas próprias: a **EC
136/2025** e o §23 seguem a aplicação imediata do Provimento CNJ 207/2025, ressalvadas ulterior
regulamentação e decisão do STF (**TV2**). Aqui vale o **CPC art. 85 §7º** (anexo): não são devidos honorários no
cumprimento de sentença **não impugnado** que enseje precatório.

## O que falta capturar para fechar os `[VERIFICAR]`

Nomeado, para o anexo da próxima versão: **DL 3.365/41 verbatim** (com a redação da Lei 14.620/2023)
— hipóteses de utilidade pública, caducidade da declaração, rito, limitação da contestação, imissão
provisória, juros compensatórios, honorários e retrocessão; o **fundamento constitucional** da prévia
e justa indenização; e o bloco de **súmulas e temas** sobre juros, base de cálculo, honorários e
prescrição da desapropriação indireta.

## Travas desta skill

- **P2** — com lastro apenas: **DL 3.365/41 + Lei 14.620/2023** (nome e alteração), LINDB arts.
  20-30, CPC 85 §7º e CPC 496. **Todo dispositivo, súmula ou tema da matéria sai `[VERIFICAR]`.**
- **Honorários** — regime próprio em lei específica; **nunca** aplicar o CPC 85 §3º por presunção
  (mesma lógica da P7).
- **P7** — prazo em dobro só depois da checagem do CPC 183 §2º; o rito tem prazos próprios.
- **P1** — nenhuma matéria de outra esfera; tributo incidente sobre a transmissão não entra aqui.
- **P5** — nada sobre honorários do procurador (CPC 85 §19) sem a lei do ente.
- **P3** — a tese de avaliação e a de acessórios passam pelo `suprema-corte-fazendaria`.
- **P4** — a minuta sai completa, com revisão humana obrigatória e responsabilidade indelegável;
  dado do expropriado e matrícula ficam locais e mascarados.

## Cross-links

`defesa-do-ente-contestacao` (a desapropriação indireta é defesa) · `parecer-consultivo` (o parecer
da declaração de utilidade pública) · `convenios-e-licitacoes-consultivo` (a obra que motiva a
desapropriação) · `lindb-como-metodo` (arts. 20, 21 e 26) · `precatorios-e-rpv` (o pagamento da
condenação) · `honorarios-da-fazenda` (a regra geral, que aqui **cede** à lei específica) ·
`improbidade-defesa-e-autoria` (superavaliação como origem de imputação) ·
`conformidade-ia-institucional` · `suprema-corte-fazendaria` (**QA obrigatória no fecho**) ·
`estilo-e-fronteiras`.
Fora da casa: `direito-imobiliario-adv-os` (a mesma matéria pela ótica do expropriado) ·
`civel-adv-os` · `juris-adv-os`.

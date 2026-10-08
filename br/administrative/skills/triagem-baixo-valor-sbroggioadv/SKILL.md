---
name: triagem-baixo-valor-sbroggioadv
title: triagem-baixo-valor — cobrar o que se paga, parar de ajuizar o que não se paga
description: 'Skill de primeira camada, não acessório: quando NÃO ajuizar e quando pedir a extinção de execução fiscal de baixo valor, pelo Tema 1184/STF (ausência de interesse de agir, eficiência administrativa) e pela Resolução CNJ 547/2024 consolidada, alterada pelas Resoluções 617/2025 e 689/2026. Separa falta de interesse de prescrição: a primeira admite outra esteira; reconhecida a prescrição, o art. 1º-B §4º veda nova cobrança do crédito alcançado. A 689 não deu nova redação ao art. 1º. Traz os números medidos, exatos e sem arredondamento: custo mínimo ≈ R$ 9.277,00 · 52,3% das execuções pendentes abaixo de R$ 10.000 · mais de 13 milhões extintas de out/2023 a jul/2025 · queda de 26,4% no acervo. Enquadramento honesto: é eficiência administrativa, não renúncia de receita — e a via que sobra é o protesto. Aciona: "vale a pena ajuizar?", "execução de baixo valor", "Resolução 547", "Tema 1184", "extinguir execução".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/triagem-baixo-valor
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# triagem-baixo-valor — cobrar o que se paga, parar de ajuizar o que não se paga

Esta skill responde à pergunta que vem **antes** da petição inicial: este crédito vale um processo?
Ela é de primeira camada porque o procurador que ajuíza abaixo do custo de cobrança trabalha contra
a eficiência do próprio órgão — e porque a régua já não é opinião administrativa: é repercussão
geral, resolução do CNJ e número medido.

Lastro: `context/resolucoes-cnj-execucao.md` e `context/temas-e-sumulas-fazendarios.md`. Este produto
atende o **Estado**.

## 1. A base jurídica — Tema 1184/STF

**Tema 1184/STF**, repercussão geral: **extinção de execução fiscal de baixo valor por ausência de
interesse de agir**, com apoio no princípio da **eficiência administrativa**. O número do tema pode
ir para peça e para parecer; **a tese literal se confere na fonte** (`portal.stf.jus.br`) antes de
qualquer transcrição entre aspas.

## 2. A linha do tempo das resoluções — e a trava TV4

| Norma | Data | O que faz |
|---|---|---|
| **Res. CNJ nº 547/2024** | **22/02/2024** | Texto-base: baixo valor, interesse de agir e providências prévias |
| **Res. CNJ nº 617/2025** | **12/03/2025** | Altera a 547, inclusive quanto a **CPF/CNPJ** e providências prévias |
| **Res. CNJ nº 689/2026** | **08/07/2026** | Acresce **§1º-A e arts. 1º-B, 1º-C e 4º-A**: movimentos úteis; intimação/análise de prescrição; automação; inclusão incidental de créditos inscritos |

⚠️ **TV4, sem exceção.** A referência é a **Resolução 547 consolidada, alterada pelas Resoluções
617/2025 e 689/2026**. A 689 não substituiu o art. 1º; qualquer texto que a descreva como “nova
redação do art. 1º” reprova.

**Número e data podem; texto do artigo, não.** As três resoluções, com as três datas, estão
confirmadas — vão para peça, parecer e recomendação administrativa. A **redação do art. 1º** (e de
qualquer outro dispositivo) **se confere na fonte antes de transcrever**: a pesquisa confirmou a
existência e o objeto da alteração, não o texto literal.

## 3. Os números medidos — exatos, sem arredondar

**Por que a 547/2024 nasceu** (dado técnico do STF):

| Dado | Valor |
|---|---|
| Custo mínimo de **uma** execução fiscal | **≈ R$ 9.277,00** |
| Execuções pendentes com valor **< R$ 10.000** | **52,3%** — mais da metade |

Mais da metade do acervo custava, para cobrar, mais do que valia. É esse par que sustenta a
**ausência de interesse de agir** do Tema 1184.

**O que aconteceu depois** (out/2023 → jul/2025, medição do CNJ):

| Indicador | Valor |
|---|---|
| Execuções fiscais extintas no período | **mais de 13 milhões** |
| Queda do acervo nacional | **−26,4%** em menos de 2 anos |
| **Caso Salvador/BA — acervo** | **−51%** |
| **Caso Salvador/BA — arrecadação** | **+87%** no mesmo período |

O **caso Salvador/BA é citado nominalmente pelo CNJ** — não é estimativa de terceiro. É a prova
prática do argumento: o ente que **parou de ajuizar o que não se paga** liberou estrutura para
cobrar o que se paga, e **arrecadou 87% mais** enquanto reduzia o acervo pela metade.

⚠️ **Os números vão para a peça exatos.** R$ 9.277,00 · 52,3% · 13 milhões · −26,4% · Salvador −51%
acervo / +87% arrecadação. **Nenhum arredondamento e nenhuma extrapolação** — "economia de bilhões",
"queda de um terço", "o dobro da arrecadação" são números não medidos, e número não medido não
existe (P2).

## 4. Duas extinções diferentes — não misturar

### Falta de interesse de agir por baixo valor

A distinção não é retórica: renúncia de receita tem regime próprio (e responsabilidade própria) para
o gestor. O que a triagem faz é **outra coisa** — reconhece que falta **interesse de agir** para a
via judicial naquele crédito, porque o processo custa mais do que ele rende. Nessa hipótese do art.
1º, o crédito não desaparece: o §3º admite nova propositura se forem encontrados bens, desde que
não consumada a prescrição, e permanecem cabíveis as medidas administrativas adequadas.

### Prescrição reconhecida após o fluxo do art. 1º-B

Os processos pendentes há mais de 15 anos ou suspensos há mais de 6 anos passam por **intimação do
exequente** e, sem manifestação/diligência útil, por **análise e decisão do magistrado**. Os arts.
1º-B/1º-C não decretam extinção automática. Se a decisão reconhecer prescrição, o §4º determina a
extinção do crédito alcançado e **veda qualquer outra cobrança administrativa ou judicial**,
inclusive cadastro de inadimplentes, protesto da CDA e cobrança indireta. O §5º preserva somente a
parcela não alcançada.

Consequências que o produto declara:

1. **Falta de interesse:** a via pode mudar para protesto/cobrança administrativa, sujeita à
   prescrição; `protesto-e-cobranca-extrajudicial` é o par desta rota.
2. **Prescrição reconhecida:** não encaminhar o mesmo crédito a protesto, negativação ou nova ação.
3. **O ângulo é o do ente.** A triagem responde quando não ajuizar, quando pedir extinção e quando
   reconhecer prescrição —
   é gestão de carteira da dívida ativa pela ótica de quem cobra. O benefício ao devedor é efeito,
   nunca o objetivo declarado.
4. **A decisão de política de cobrança é do ente.** O produto traz a régua, os números e o
   enquadramento; o ato administrativo e a responsabilidade por ele são do procurador e do gestor.

## 5. Roteiro de triagem

**Antes de ajuizar:**

1. O valor atualizado do crédito supera com folga o **custo de cobrança**? O parâmetro nacional
   medido é **≈ R$ 9.277,00**; o custo real do ente e o piso adotado localmente são
   `[VERIFICAR]` — dependem de ato do ente e não estão nos anexos.
2. Há **CPF/CNPJ do executado**? A ausência é hipótese própria, alcançada pela **617/2025**.
3. Há **garantia, penhora ou indício concreto de patrimônio** que mude a equação? Crédito pequeno
   com bem identificado não é o caso típico da triagem.
4. **Não passando no crivo:** não ajuizar, e encaminhar para protesto/cobrança administrativa.

**Nos processos já em curso:**

5. **Baixo valor/falta de interesse:** aplique o art. 1º e confira movimentação útil. A extinção não
   autoriza tratar o crédito como prescrito; a nova propositura do §3º depende de bens e ausência de
   prescrição.
6. **Processo antigo:** art. 1º-B significa intimação e posterior análise judicial, não extinção
   automática. Mapeie manifestação, diligência útil, causas suspensivas/interruptivas e marcos.
7. **Prescrição reconhecida:** encerre as medidas sobre a parcela prescrita; o §4º veda cobrança
   administrativa e judicial. Só a parcela não alcançada conserva medidas cabíveis (§5º).
8. **Inclusão incidental:** o art. 4º-A alcança créditos **já inscritos em dívida ativa** relativos
   a impostos sobre propriedade e correlatos, do mesmo sujeito passivo e da mesma relação jurídica
   de trato sucessivo, mediante pedido e contraditório — não simplesmente créditos “vincendos”.
9. Cruze com `prescricao-intercorrente`: processo em que o prazo já correu **e** de valor abaixo do
   custo não é caso de recurso, é caso de reconhecer. O próprio art. 40 §5º da LEF
   (`context/lef-6830.md`) já dispensa a oitiva prévia da Fazenda nas cobranças de valor inferior ao
   mínimo — a lógica de baixo valor está dentro da LEF, não só nas resoluções.
10. Meça o resultado. O argumento de Salvador só é replicável se o ente souber quanto acervo saiu e
   quanto a arrecadação subiu.

## Travas desta skill

- **TV4 (a desta skill).** Sempre a **Res. 547 consolidada, alterada pelas Res. 617/2025 e
  689/2026**; nunca a 689 como “nova redação do art. 1º”.
- **P2 — nada sem lastro.** Números **exatos** e sem extrapolação; texto de artigo de resolução e
  tese literal do Tema 1184 **conferidos na fonte** antes de transcrever. Custo real do ente, piso
  local e qualquer estatística não listada → `[VERIFICAR]`.
- **Enquadramento fixo:** falta de interesse por eficiência administrativa não é prescrição. Só na
  primeira rota se nomeia a via alternativa; reconhecida a prescrição, o §4º proíbe nova cobrança.
- **P1.** As resoluções e o rito valem nas três esferas; o crédito é de ICMS, IPVA, ITCMD e demais créditos estaduais.
- **P4.** A recomendação é estudo; o ato de não ajuizar, o pedido de extinção e a política de
  cobrança são decisão do procurador e do gestor, indelegáveis.

**Próximo passo:** a via que sobra → `protesto-e-cobranca-extrajudicial`. Passou no crivo e vai ser
ajuizada → `execucao-fiscal-lef`. Processo antigo e parado → `prescricao-intercorrente`. Toda
entrega fecha por `suprema-corte-fazendaria`.

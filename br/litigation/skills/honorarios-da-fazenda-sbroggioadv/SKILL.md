---
name: honorarios-da-fazenda-sbroggioadv
title: honorarios-da-fazenda — a faixa escalonada, a equidade que virou exceção e o §19 que remete
description: 'Honorários nas causas em que a Fazenda é parte, pelo CPC 85 verbatim: as cinco faixas do §3º (10-20% até 200 SM · 8-10% até 2.000 · 5-8% até 20.000 · 3-5% até 100.000 · 1-3% acima), a aplicação escalonada do §5º — faixa inicial e, no que exceder, a subsequente, como imposto de renda, nunca percentual único sobre o todo —, o §4º (líquida aplica desde logo, ilíquida só na liquidação), o §6º (vale inclusive na improcedência) e o §6º-A (é PROIBIDA a apreciação equitativa quando o valor é líquido ou liquidável, salvo o §8º). Trava P5 no §19: o sucumbencial do advogado público é "nos termos da lei" — só a esfera federal tem lei confirmada no anexo; Estado e Município dependem de lei própria, e o produto PERGUNTA, nunca presume. Aciona: "quanto de honorários", "faixa do 85", "honorários contra a Fazenda", "apreciação equitativa", "sucumbência do procurador".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/honorarios-da-fazenda
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# honorarios-da-fazenda — a faixa escalonada, a equidade que virou exceção e o §19 que remete

Honorários com a Fazenda no polo têm regra própria, e ela é aritmética antes de ser argumentativa.
Esta skill faz três coisas: calcula pela faixa certa, impede o atalho da equidade onde ele está
proibido, e separa **honorários da causa** (CPC 85, §§2º a 8º-A) de **sucumbencial do procurador**
(§19) — que é outra pergunta, com outra resposta, e depende da lei do ente.

Texto verbatim em `context/prerrogativas-cpc.md`. Este produto atende o **Estado**.

## Quando esta skill entra

- Saiu sentença em causa com a Fazenda no polo (ativo ou passivo) e é preciso dimensionar a verba.
- A parte contrária pede honorários por apreciação equitativa sobre valor alto.
- O ente foi condenado e a fixação veio por percentual único sobre o total.
- O procurador pergunta se recebe sucumbência — e sob qual base.

## 1. As cinco faixas do §3º

Nas causas em que a Fazenda for parte, a fixação observa os critérios dos incisos I a IV do §2º
(grau de zelo · lugar da prestação · natureza e importância da causa · trabalho realizado e tempo
exigido) **e** os percentuais:

| Faixa | Base — condenação ou proveito econômico | Percentual |
|---|---|---|
| **I** | até **200** salários-mínimos | mínimo 10% · máximo 20% |
| **II** | acima de 200 até **2.000** SM | mínimo 8% · máximo 10% |
| **III** | acima de 2.000 até **20.000** SM | mínimo 5% · máximo 8% |
| **IV** | acima de 20.000 até **100.000** SM | mínimo 3% · máximo 5% |
| **V** | acima de **100.000** SM | mínimo 1% · máximo 3% |

## 2. A faixa é escalonada — §5º (o erro de cálculo mais comum)

**Verbatim:** quando a condenação, o benefício econômico ou o valor da causa for superior ao do
inciso I do §3º, "a fixação do percentual de honorários deve observar a faixa inicial e, naquilo que
a exceder, a faixa subsequente, e assim sucessivamente".

Ou seja: **não se escolhe uma faixa e se aplica ao todo.** O cálculo é por degraus acumulados, como
imposto de renda — a parcela até 200 SM entra na faixa I, a parcela entre 200 e 2.000 SM na faixa
II, e assim por diante. Fixação que aplique um percentual único sobre o valor inteiro está errada em
tese, tanto contra o ente quanto a favor dele; o produto aponta o defeito nos dois sentidos.

## 3. As regras de aplicação — §4º

| Inciso | Regra |
|---|---|
| **I** | Sentença **líquida** → os percentuais dos incisos I a V se aplicam **desde logo** |
| **II** | Sentença **ilíquida** → a definição do percentual só ocorre **quando liquidado** o julgado |
| **III** | Sem condenação principal, ou proveito econômico não mensurável → a condenação se dá sobre o **valor atualizado da causa** |
| **IV** | Entra o salário-mínimo **vigente quando prolatada a sentença líquida**, ou o vigente **na data da decisão de liquidação** |

O inciso IV é o que fecha a conta: sem fixar qual salário-mínimo entra, o degrau muda de lugar.

## 4. A equidade virou exceção estreita — §§6º, 6º-A, 8º e 8º-A

- **§6º** — os limites e critérios dos §§2º e 3º aplicam-se **independentemente do conteúdo da
  decisão**, inclusive aos casos de **improcedência** e de **sentença sem resolução de mérito**. Não
  há espaço para honorários simbólicos contra a Fazenda por fora dessas regras.
- **§6º-A (incluído pela Lei nº 14.365, de 2022)** — quando o valor da condenação, do proveito
  econômico ou o valor atualizado da causa for **líquido ou liquidável**, "**é proibida a apreciação
  equitativa**", salvo nas hipóteses expressamente previstas no §8º. É a trava aritmética desta
  skill: pedido de equidade sobre valor liquidável é pedido contra a letra do dispositivo.
- **§8º** — a equidade cabe quando o proveito econômico for **inestimável ou irrisório**, ou quando
  o **valor da causa for muito baixo**, observados os incisos do §2º.
- **§8º-A (incluído pela Lei nº 14.365, de 2022)** — mesmo na hipótese do §8º há **piso**: o juiz
  observará os valores recomendados pelo Conselho Seccional da OAB ou o **limite mínimo de 10%** do
  §2º, **aplicando-se o que for maior**.
- **§7º** — não são devidos honorários no **cumprimento de sentença contra a Fazenda que enseje
  expedição de precatório, desde que não tenha sido impugnada**. É a interface com
  `precatorios-e-rpv`: impugnar sem necessidade pode criar a verba que o §7º dispensaria.

**Roteiro de checagem da equidade:** o valor é líquido ou liquidável? → **sim**: equidade proibida
(§6º-A), aplica-se a faixa escalonada. → **não**: é caso do §8º (inestimável, irrisório, valor muito
baixo)? → **sim**: equidade cabe, **com o piso do §8º-A** (tabela da Seccional ou 10%, o maior).

## 5. ⚠️ §19 — a trava P5, em destaque

**Verbatim, na íntegra:** "§ 19. Os advogados públicos perceberão honorários de sucumbência, nos
termos da lei."

Leia o que o dispositivo **não** diz. Ele é **remissivo**: não cria por si o direito do procurador
ao sucumbencial — remete a "nos termos da lei", isto é, **à lei do ente**.

| Esfera | Situação no anexo | Postura do produto |
|---|---|---|
| **Federal** | A lei existe e está nomeada: **Lei nº 13.327/2016** | Pode afirmar com a base nomeada |
| **Estadual** | Existe em alguns Estados e não em outros — o anexo **não** traz o texto de nenhuma | **Pergunta pela lei estadual** ou marca `[VERIFICAR]` |
| **Municipal** | Idem — existe em alguns Municípios e não em outros | **Pergunta pela lei municipal** ou marca `[VERIFICAR]` |

**Regra sem exceção:** sem a lei do ente na mão, o produto **não afirma** que o procurador
do Estado recebe sucumbência, **não** aplica por analogia o regime federal, e **não** conclui que
não recebe. Ele pergunta: *"há lei do ente regulando os honorários de sucumbência dos seus advogados
públicos? Qual?"* — e, sem resposta, o texto sai com `[VERIFICAR]`. Presumir aqui é o defeito que o
gate G4 da `suprema-corte-fazendaria` existe para reprovar.

**Consequência prática que o produto não pode embaralhar:** honorários **da causa** (quem paga,
quanto, sobre o quê) e **destinação do sucumbencial ao advogado público** são perguntas separadas. A
primeira se resolve integralmente nos §§2º a 8º-A. A segunda depende de lei do ente e do regime de
rateio que essa lei estabelecer — e o anexo não carrega nenhum regime de rateio. Nunca descreva
percentual, teto ou forma de distribuição sem o texto local.

**Perfil do comprador:** onde o produto atende também escritório contratado pelo ente, a verba
contratual pactuada é **outra coisa** — não é o §19, e o produto não confunde as duas. Sem o
contrato à vista, `[VERIFICAR]`.

## Travas desta skill

- **P5 (a desta skill).** Nada que dependa de lei do ente é presumido: sucumbencial do procurador
  só com a lei nomeada. No federal, Lei 13.327/2016; fora dela, pergunta ou marca.
- **P2 — nada sem lastro.** Faixas, percentuais e parágrafos citados estão em
  `context/prerrogativas-cpc.md`. Valor de salário-mínimo, tabela de Seccional da OAB e lei local
  **não estão** nos anexos → `[VERIFICAR]`, nunca número de memória.
- **P1.** CPC 85 é lei federal comum às três esferas — a faixa não muda por esfera. O que muda é a
  existência da lei do ente no §19.
- **P3.** Tese sobre honorários já superada em repetitivo ou súmula é avisada antes de sustentada;
  o gate roda em `suprema-corte-fazendaria`.
- **P4.** Cálculo aqui é estudo e minutação local; a conferência dos valores, do salário-mínimo
  aplicável e do pedido protocolado é do procurador, indelegável.

**Próximo passo:** cumprimento contra a Fazenda com expedição de precatório (§7º) →
`precatorios-e-rpv`. Prazo e remessa da mesma sentença → `prerrogativas-processuais`. Toda entrega
fecha por `suprema-corte-fazendaria` (G4 confere exatamente o §19).
Não há lei nacional aqui: sem a lei do Estado, o §19 sai como `[VERIFICAR]`.

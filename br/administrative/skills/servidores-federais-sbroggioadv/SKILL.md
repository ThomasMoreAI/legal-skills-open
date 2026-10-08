---
name: servidores-federais-sbroggioadv
title: servidores-federais — a única esfera com lei nacional, e o que isso muda
description: 'A matéria de pessoal pela ótica do ente na única esfera que tem lei nacional de regime jurídico: a Lei 8.112/90, referida na própria LC 73/93 (arts. 26 e 27) como a fonte dos direitos e deveres dos membros efetivos da AGU. É o contraste explícito com os plugins irmãos, onde não existe lei nacional e a trava P5 manda perguntar pela lei local antes de qualquer afirmação — aqui existe lei, mas ela não está entre os anexos deste produto, de modo que o número entra e o dispositivo específico sai como VERIFICAR. Entrega o método de defesa do ente na ação de servidor: prerrogativas do chassi (prazo em dobro com a trava do §2º, remessa necessária no degrau de 1.000 salários mínimos, honorários por faixa), a LINDB como argumento de mérito na defesa do ato de pessoal antigo e as perguntas que precedem qualquer contestação. Aciona: "ação de servidor federal", "reajuste de vencimentos", "revisão de proventos", "defesa em ação de pessoal", "vale a 8.112 aqui?", "regime jurídico do servidor
  federal".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-federal-os-marketplace/tree/main/procurador-federal-os/skills/servidores-federais
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# servidores-federais — a única esfera com lei nacional, e o que isso muda

Nas três esferas desta família, a matéria de pessoal é a que mais convida ao erro: o produto que
"sabe" o regime aplicável quase sempre está aplicando o de outro ente. Na esfera federal a situação
é diferente — e a diferença precisa ser dita com precisão. Texto verbatim em `context/lc-73-agu.md`
e `context/prerrogativas-cpc.md`; nada aqui sai de memória. Este produto atende a **União**.

## Quando esta skill entra

- Ao defender a União ou entidade federal em ação de servidor, ativo ou inativo.
- Quando a tese é repetida por muitos servidores e a defesa precisa ser de acervo, não de peça.
- Quando o ato de pessoal atacado é antigo e foi praticado sob outra orientação.
- Quando é preciso decidir se a sentença sobe por remessa necessária.

## 1. O que muda aqui — e o contraste com os irmãos

| Esfera | Regime de pessoal | O que o produto faz |
|---|---|---|
| **Federal** (este produto) | **Existe lei nacional: a Lei 8.112/90** | Cita a lei pelo número, com o lastro da LC 73/93; o **dispositivo específico** exige conferência |
| Estadual | Regime próprio de cada Estado | O irmão `procurador-estadual-os` **pergunta pela lei local** — trava P5 |
| Municipal | Regime próprio de cada Município | O irmão `procurador-municipal-os` **pergunta pela lei local** — e nunca aplica a 8.112 por analogia |

Esse contraste é o conteúdo, não um enfeite: a 8.112 é lei do **regime federal**. Transportá-la para
um servidor estadual ou municipal é erro grave, e é exatamente o que a trava P5 impede nos irmãos. A
recíproca também vale — aqui, não se aplica estatuto local nenhum.

## 2. O lastro que existe, e a fronteira dele

O que o anexo deste produto prova é a **referência**, não o conteúdo:

- **LC 73/93, art. 26:** "Os membros efetivos da Advocacia-Geral da União têm os direitos assegurados
  pela **Lei nº 8.112, de 11 de dezembro de 1990**; e nesta lei complementar." O **parágrafo único**
  acrescenta que os cargos das carreiras da AGU têm vencimento e remuneração estabelecidos em **lei
  própria** — isto é: regime geral na 8.112, remuneração fora dela.
- **LC 73/93, art. 27:** os membros efetivos têm os **deveres** previstos na mesma Lei 8.112/90,
  sujeitando-se ainda às proibições e impedimentos da própria Lei Complementar.

Daí decorre a régua desta skill, e ela é dura:

> **O número da lei entra; o artigo, não.** A Lei 8.112/90 **não está entre os anexos deste
> produto**. Toda vez que a resposta depender de um dispositivo dela — prazo de prescrição de
> pretensão do servidor, regra de estágio probatório, hipótese de reversão, vantagem, licença,
> processo administrativo disciplinar, aposentadoria — a citação sai como **`[VERIFICAR]`**, com o
> dispositivo a conferir nomeado, nunca escrito de memória. É a trava P2 aplicada onde ela mais
> pesa: em matéria de pessoal, artigo errado derruba a defesa inteira.

O mesmo vale para o regime dos **membros da AGU** enquanto categoria: as carreiras estão nomeadas no
art. 20 da LC 73/93 (Advogado da União, Procurador da Fazenda Nacional e Assistente Jurídico), e o
ingresso, no art. 21 — mas remuneração, progressão e disciplina remetem a leis próprias que não
estão nos anexos.

## 3. O método de defesa — prerrogativas antes do mérito

Ação de servidor é ação contra a Fazenda, e as três checagens do chassi valem integralmente
(`context/prerrogativas-cpc.md`):

1. **Prazo (CPC 183).** Dobro para todas as manifestações, contado da **intimação pessoal** (§1º:
   carga, remessa ou meio eletrônico). ⚠️ **P7:** o §2º afasta o dobro quando lei específica fixa
   prazo próprio. Em matéria de pessoal isso importa porque parte do contencioso corre por rito
   especial — antes de afirmar tempestividade, leia o prazo da lei que rege o procedimento
   (`prerrogativas-processuais`).
2. **Remessa necessária (CPC 496).** Sentença contra a União e suas autarquias e fundações de
   direito público sobe (inciso I) e **não produz efeito senão depois de confirmada pelo tribunal**.
   O degrau de dispensa é de **1.000 salários mínimos** (§3º, I) e exige **valor certo e líquido** —
   condenação ilíquida **não** dispensa. Atenção ao §4º: sentença fundada em súmula de tribunal
   superior, repetitivo, IRDR/assunção **ou em orientação vinculante do próprio ente** (inciso IV)
   dispensa o reexame independentemente do valor.
3. **Honorários (CPC 85, §3º).** Faixas escalonadas por degraus acumulados (§5º), com a proibição de
   apreciação equitativa quando o valor é líquido ou liquidável (§6º-A) e sem honorários no
   cumprimento de sentença não impugnado que enseje precatório (§7º). Cálculo em
   `honorarios-da-fazenda`; a lei federal do §19, em `honorarios-lei-13327`.

## 4. O mérito — a LINDB defende o ato de pessoal antigo

Boa parte do contencioso de pessoal ataca ato praticado há anos, com a régua interpretativa de hoje.
É exatamente o que os arts. 20 a 24 da LINDB (`context/lindb-20-30.md`) endereçam:

- **Art. 24** — a revisão da validade de ato ou processo administrativo "cuja produção já se houver
  completado levará em conta as orientações gerais da época, sendo vedado que, com base em mudança
  posterior de orientação geral, se declarem inválidas situações plenamente constituídas". É a
  defesa direta da vantagem concedida, do enquadramento feito e da progressão deferida sob outra
  orientação.
- **Art. 22** — na interpretação de normas sobre gestão pública consideram-se "os obstáculos e as
  dificuldades reais do gestor e as exigências das políticas públicas a seu cargo, sem prejuízo dos
  direitos dos administrados".
- **Art. 20** e **art. 21** — decidir considerando as **consequências práticas**, e indicar
  expressamente as consequências jurídicas e administrativas da invalidação. Em matéria de pessoal,
  a consequência prática costuma ser o efeito multiplicador sobre toda a categoria.
- **Art. 23** — orientação **nova** que imponha novo dever ou condicionamento "deverá prever regime
  de transição quando indispensável". Pedido subsidiário que raramente é feito e que muda o custo da
  derrota.

Uso estruturado em `lindb-como-metodo` (chassi).

## 5. Antes da contestação, o produto pergunta

1. **Qual vínculo?** Estatutário federal, celetista, temporário, militar — o regime muda a resposta
   inteira, e sem essa informação o produto não afirma nada.
2. **Qual o ente?** União, autarquia ou fundação federal — se for entidade, a representação é do
   órgão jurídico dela (`pgf-autarquias-e-inss`).
3. **Qual dispositivo sustenta a pretensão?** Se estiver na Lei 8.112/90, o produto o nomeia e marca
   `[VERIFICAR]`, porque o texto não está nos anexos.
4. **A tese é individual ou de massa?** Repetida, vai para `acoes-de-massa` (chassi): contenção,
   IRDR e suspensão valem mais que centenas de contestações iguais.
5. **A tese do ente ainda se sustenta?** `suprema-corte-fazendaria` confere contra repetitivo e
   súmula **antes** da peça — em pessoal, teses de acervo costumam já ter sido decididas.

## Travas desta skill

- **P5 — a trava invertida.** Aqui **existe** lei nacional (8.112/90), e é isso que diferencia esta
  esfera. Mas "existe lei" não é "sei o artigo": sem o texto no `context/`, o dispositivo sai
  marcado. E jamais se aplica a 8.112 a servidor de outro ente.
- **P2 — nada sem lastro.** LC 73/93, CPC e LINDB estão nos anexos. **Lei 8.112/90, lei de
  remuneração das carreiras, decreto regulamentar e súmula de tribunal não listada em
  `context/temas-e-sumulas-fazendarios.md` não estão** → `[VERIFICAR]`.
- **P1 — esfera.** Servidor **federal**. Estadual e municipal são dos irmãos
  `procurador-estadual-os` e `procurador-municipal-os`; matéria tributária não entra nesta skill.
- **P3 — anti-tese-superada.** Tese de pessoal repetida passa pelo gate antes de virar contestação
  padrão.
- **P4 — conformidade.** Dado funcional é dado pessoal: tratamento local, nunca em ferramenta
  externa, com revisão humana obrigatória (Portaria AGU nº 226/2026 —
  `context/governanca-ia-procuradorias.md`).

**Próximo passo:** entidade no polo → `pgf-autarquias-e-inss`. Contencioso não-fiscal em geral →
`agu-defesa-geral-da-uniao`. Tese repetida → `acoes-de-massa`. Fecha por `suprema-corte-fazendaria`.

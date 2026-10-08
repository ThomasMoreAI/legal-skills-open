---
name: agu-defesa-geral-da-uniao-sbroggioadv
title: agu-defesa-geral-da-uniao — a União no polo passivo, fora da matéria fiscal
description: 'A defesa NÃO-fiscal da União — indenizatórias e responsabilidade civil do Estado, ações civis públicas contra a União, matéria de servidores e demandas sobre políticas públicas — montada com quem tem atribuição para ela: a Advocacia-Geral da União como instituição que representa a União judicial e extrajudicialmente (LC 73/93, art. 1º) e a Procuradoria-Geral da União, que a representa em juízo pela escada de instâncias do art. 9º. Traz o método de contestação do ente articulando as prerrogativas do chassi (prazo em dobro com a trava do §2º, remessa necessária no degrau de 1.000 salários mínimos da União, honorários por faixa) com a LINDB como argumento de mérito: obstáculos reais do gestor, vedação de invalidar situação constituída por mudança posterior de orientação e regime de transição. O que não tiver lastro sai marcado. Aciona: "contestação da União", "ação indenizatória contra a União", "ACP contra a União", "quem defende a União nessa ação?", "defesa não-fiscal", "AGU
  representa onde".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-federal-os-marketplace/tree/main/procurador-federal-os/skills/agu-defesa-geral-da-uniao
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# agu-defesa-geral-da-uniao — a União no polo passivo, fora da matéria fiscal

Nem toda causa da União é fiscal. A maior parte do contencioso da AGU não passa por CDA: são
indenizatórias, ações coletivas, demandas de servidor e discussões sobre política pública. Esta
skill trata dessa frente. Texto verbatim em `context/lc-73-agu.md`, `context/prerrogativas-cpc.md` e
`context/lindb-20-30.md`; nada aqui sai de memória. Este produto atende a **União**.

## Quando esta skill entra

- Ao montar contestação da União em ação que não discute crédito tributário.
- Quando a pergunta é qual órgão da AGU atua e perante qual instância.
- Quando o mérito envolve ato administrativo antigo, mudança de orientação ou consequência prática.
- Antes de recorrer: a sentença sobe sozinha por remessa, ou é preciso apelar?

## 1. Quem representa a União — e onde

**LC 73/93, art. 1º:** "A Advocacia-Geral da União é a instituição que representa a União judicial e
extrajudicialmente." O **parágrafo único** acrescenta que lhe cabem as atividades de consultoria e
assessoramento jurídicos ao Poder Executivo.

**Art. 9º — a Procuradoria-Geral da União**, subordinada direta e imediatamente ao Advogado-Geral
da União, incumbe representá-la **judicialmente**, nos termos e limites da Lei Complementar. A
escada de instâncias está nos parágrafos:

| Órgão | Atua perante |
|---|---|
| **Procurador-Geral da União** (§1º) | os **tribunais superiores** |
| **Procuradorias Regionais da União** (§2º) | os **demais tribunais** |
| **Procuradorias da União** nos Estados e no DF (§3º) | a **primeira instância** da Justiça Federal, comum e especializada |

**§4º:** o Procurador-Geral da União pode atuar perante os órgãos dos §§2º e 3º, e os Procuradores
Regionais perante os do §3º — a escada sobe, não desce por conta própria.

**Art. 4º, §1º:** o Advogado-Geral da União "pode representá-la junto a qualquer juízo ou Tribunal";
**§2º:** pode **avocar** quaisquer matérias jurídicas de interesse da União, inclusive quanto à
representação extrajudicial. E o **inciso III** do art. 4º reserva ao Advogado-Geral representar a
União junto ao **Supremo Tribunal Federal**, e o **IV**, defender a norma impugnada nas ações
diretas de inconstitucionalidade.

Essa divisão é matéria da trava TV7, e o mapa completo — inclusive por que a PGFN não responde por
esta frente — está em `pgu-e-estrutura-da-agu`.

## 2. As seis frentes, e onde cada uma se resolve

| Frente | Onde é tratada |
|---|---|
| Indenizatórias e responsabilidade civil do Estado | aqui + `defesa-do-ente-contestacao` (chassi) |
| Ações civis públicas e demandas coletivas contra a União | aqui + `acoes-de-massa` (chassi) |
| Matéria de servidores federais | `servidores-federais` (regime da Lei 8.112/90) |
| Políticas públicas, com destaque para saúde | `saude-judicializada` (chassi, Tema 793/STF) |
| Mandado de segurança e limites de liminar contra o Poder Público | `mandado-de-seguranca-defesa` (chassi) |
| Ressarcimento ao erário e improbidade com a União no polo ativo | `improbidade-e-ressarcimento-uniao` |

**Um aviso de lastro, na abertura:** o fundamento constitucional da responsabilidade civil objetiva
do Estado **não está nos anexos deste produto**. Toda vez que a defesa precisar do dispositivo — e
não só do raciocínio — a citação sai como `[VERIFICAR]`, para conferência na fonte antes de ir à
peça. O mesmo vale para as leis que restringem tutela antecipada e liminar contra a Fazenda: elas
são tratadas em `mandado-de-seguranca-defesa`, com o lastro que aquela skill tiver.

## 3. O método — as prerrogativas antes do mérito

Contestação da União começa por três checagens que mudam o desenho da defesa, todas com texto em
`context/prerrogativas-cpc.md`:

1. **Prazo (CPC 183).** Dobro para todas as manifestações processuais, contado da **intimação
   pessoal** (§1º: carga, remessa ou meio eletrônico). ⚠️ **Trava P7:** o §2º afasta o dobro quando
   lei específica fixar prazo próprio para o ente. Procedimento regido por lei especial exige ler o
   prazo dessa lei antes de qualquer afirmação de tempestividade — o método completo está em
   `prerrogativas-processuais`.
2. **Remessa necessária (CPC 496).** Sentença contra a União está sujeita ao duplo grau (inciso I),
   **não produzindo efeito senão depois de confirmada pelo tribunal**. O degrau de dispensa por
   valor da **União e de suas autarquias e fundações de direito público é de 1.000 salários
   mínimos** (§3º, I) — e a dispensa exige **valor certo e líquido**: condenação ilíquida não
   dispensa, por menor que pareça. O §4º dispensa independentemente do valor quando a sentença se
   funda em súmula de tribunal superior, repetitivo, IRDR/assunção **ou em orientação vinculante do
   próprio ente** (inciso IV).
3. **Honorários (CPC 85, §3º).** Faixas escalonadas, aplicadas por degraus acumulados nos termos do
   §5º — e o §6º-A **proíbe a apreciação equitativa** quando o valor é líquido ou liquidável, salvo
   nas hipóteses do §8º. O §7º afasta honorários no cumprimento de sentença não impugnado que enseje
   precatório. Cálculo em `honorarios-da-fazenda` (chassi); a lei federal do §19 está em
   `honorarios-lei-13327`.

## 4. A LINDB como argumento de mérito, não como enfeite

Os arts. 20 a 30 da LINDB (`context/lindb-20-30.md`) são a arma consultiva mais subaproveitada na
defesa do ente. Quatro deles trabalham diretamente na contestação:

- **Art. 22** — "na interpretação de normas sobre gestão pública, serão considerados os obstáculos e
  as dificuldades reais do gestor e as exigências das políticas públicas a seu cargo, sem prejuízo
  dos direitos dos administrados". É o dispositivo que traz o mundo real do orçamento e da
  capacidade operacional para dentro do processo.
- **Art. 24** — a revisão da validade de ato, contrato, ajuste, processo ou norma administrativa
  "cuja produção já se houver completado levará em conta as orientações gerais da época, sendo
  vedado que, com base em mudança posterior de orientação geral, se declarem inválidas situações
  plenamente constituídas". É a defesa direta do ato antigo julgado com a régua de hoje.
- **Art. 20** — não se decidirá com base em valores jurídicos abstratos sem que sejam consideradas
  as **consequências práticas** da decisão. Combinado com o **art. 21**, que exige indicar
  expressamente as consequências jurídicas e administrativas da invalidação.
- **Art. 23** — decisão que estabelecer interpretação ou orientação **nova** sobre norma de conteúdo
  indeterminado, impondo novo dever ou condicionamento, "deverá prever **regime de transição**
  quando indispensável". Pedido subsidiário que quase nunca é feito e que muda o custo da derrota.

O art. **28** completa o quadro do lado do agente: responde pessoalmente por decisões ou opiniões
técnicas apenas "em caso de dolo ou erro grosseiro". O uso estruturado desses artigos está em
`lindb-como-metodo` (chassi).

## 5. O ciclo que reduz acervo — súmula administrativa

**Art. 4º, XII** da LC 73/93: cabe ao Advogado-Geral da União "editar enunciados de súmula
administrativa, resultantes de jurisprudência iterativa dos Tribunais"; o **inciso X** lhe atribui
fixar a interpretação a ser uniformemente seguida pela Administração Federal, e o **XI**, unificar a
jurisprudência administrativa e dirimir controvérsias entre órgãos jurídicos federais.

Some isso ao **art. 30 da LINDB** — as autoridades devem atuar para aumentar a segurança jurídica,
inclusive por súmulas administrativas — e ao **CPC 496, §4º, IV**: sentença coincidente com
orientação vinculante do próprio ente **dispensa a remessa necessária**. É o ciclo completo:
consultivo bem feito no início vira menos reexame no fim. A ponte está em `parecer-consultivo`
(chassi).

## Travas desta skill

- **P1 — esfera.** Defesa da **União**. Ação contra Estado ou Município, ainda que idêntica no
  mérito, é dos irmãos `procurador-estadual-os` e `procurador-municipal-os`. E, dentro da União, a
  matéria **fiscal** não é desta skill: vai para `pgfn-divida-ativa-uniao` e
  `carf-contencioso-administrativo`.
- **P2 — nada sem lastro.** O que está aqui vem de `context/lc-73-agu.md`,
  `context/prerrogativas-cpc.md` e `context/lindb-20-30.md`. Dispositivo constitucional de
  responsabilidade civil do Estado, lei de tutela antecipada contra a Fazenda, Lei da Ação Civil
  Pública e precedente não listado em `context/temas-e-sumulas-fazendarios.md` → `[VERIFICAR]`,
  nunca de memória.
- **P3 — anti-tese-superada.** Antes de sustentar a tese institucional, `suprema-corte-fazendaria`
  confere se ela ainda se sustenta. Tese batida em repetitivo → o produto avisa e propõe a linha
  viável, inclusive a de reconhecer o pedido quando reconhecer custa menos que perder com
  honorários.
- **P5 — não presumir.** Ato normativo interno da AGU, orientação de órgão e súmula administrativa
  variam e não estão nos anexos: o produto pergunta pelo texto ou marca.
- **P4 — conformidade.** Minuta aqui é estudo. Protocolo, revisão e responsabilidade pelo conteúdo
  são do procurador, indelegáveis (Portaria AGU nº 226/2026 —
  `context/governanca-ia-procuradorias.md`).

**Próximo passo:** atribuição do órgão → `pgu-e-estrutura-da-agu`. Autarquia ou fundação no polo →
`pgf-autarquias-e-inss`. Prazo e remessa → `prerrogativas-processuais`. Fecha por
`suprema-corte-fazendaria`.

---
name: pgu-e-estrutura-da-agu-sbroggioadv
title: pgu-e-estrutura-da-agu — resolver a atribuição antes de escrever a peça
description: 'O mapa de quem representa o quê na advocacia pública federal, com o texto da LC 73/93 na mão — a skill que resolve a atribuição ANTES de qualquer peça. A AGU como instituição que representa a União judicial e extrajudicialmente (art. 1º) e a sua composição (art. 2º); a Procuradoria-Geral da União na representação judicial, com a escada de instâncias do art. 9º; a Consultoria-Geral da União (art. 10) e as Consultorias Jurídicas dos Ministérios (art. 11); a PGFN, órgão subordinado ao titular do Ministério da Fazenda, com a dívida ativa tributária e as causas de natureza fiscal do art. 12 e seu parágrafo único; e os órgãos jurídicos das autarquias e fundações (arts. 2º §3º, 17 e 18), campo da PGF. Existe por causa da trava TV7: tratar PGFN como sinônimo de advocacia pública federal faz a peça nascer no órgão errado. Aciona: "quem representa a União nessa ação?", "é PGFN ou AGU?", "atribuição da PGU", "causa de natureza fiscal", "estrutura da AGU", "Consultoria Jurídica do Ministério".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-federal-os-marketplace/tree/main/procurador-federal-os/skills/pgu-e-estrutura-da-agu
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# pgu-e-estrutura-da-agu — resolver a atribuição antes de escrever a peça

Advocacia pública federal não é um órgão só. É uma instituição com órgãos de direção superior, de
execução e vinculados, cada um com um perímetro escrito em lei. Esta skill entrega o mapa e a
pergunta que ele responde: **quem tem atribuição neste caso?** Texto verbatim em
`context/lc-73-agu.md`; nada aqui sai de memória. Este produto atende a **União**.

## ⚠️ TV7 — a trava que dá origem a esta skill

**A PGFN não é a AGU inteira.** Ela é um órgão da AGU com competência específica: dívida ativa da
União de natureza tributária e representação em causas de natureza **fiscal** (art. 12). A defesa
não-fiscal da União é da **Advocacia da União / PGU**; a consultoria ao Presidente e ao Executivo é
da **Consultoria-Geral da União** e das **Consultorias Jurídicas**; a representação das autarquias e
fundações federais é dos **órgãos jurídicos** dessas entidades, campo da PGF. Escrever "a PGFN
defende a União" fora da matéria fiscal é erro de escopo, e é o que esta skill impede.

## Quando esta skill entra

- **Antes** de qualquer peça federal — é a primeira pergunta, não a última.
- Quando a matéria mistura crédito e não-crédito e não se sabe qual órgão conduz.
- Quando a causa envolve autarquia ou fundação e não a União diretamente.
- Quando é preciso saber perante qual instância cada órgão atua.

## 1. A instituição e a sua composição

**Art. 1º:** "A Advocacia-Geral da União é a instituição que representa a União judicial e
extrajudicialmente." **Parágrafo único:** cabem-lhe as atividades de consultoria e assessoramento
jurídicos ao Poder Executivo.

**Art. 2º — a composição:**

| Grupo | Órgãos |
|---|---|
| **I — direção superior** | a) o Advogado-Geral da União; b) a **Procuradoria-Geral da União e a da Fazenda Nacional**; c) a **Consultoria-Geral da União**; d) o Conselho Superior; e) a Corregedoria-Geral da Advocacia da União |
| **II — execução** | a) as Procuradorias Regionais da União e as da Fazenda Nacional, as Procuradorias da União e as da Fazenda Nacional nos Estados e no DF e as Procuradorias Seccionais; b) a Consultoria da União, as **Consultorias Jurídicas dos Ministérios**, da Secretaria-Geral e demais Secretarias da Presidência e do Estado-Maior das Forças Armadas |
| **III — assistência direta** | o Gabinete do Advogado-Geral da União |

**§1º:** subordinam-se **diretamente** ao Advogado-Geral da União, além do gabinete, a PGU, a
Consultoria-Geral da União, a Corregedoria-Geral, a Secretaria de Controle Interno e, **técnica e
juridicamente**, a Procuradoria-Geral da Fazenda Nacional. Repare na diferença de qualificação: a
PGFN é subordinada **técnica e juridicamente** ao AGU, mas **administrativamente ao titular do
Ministério da Fazenda** (art. 12, caput). É essa dupla vinculação que confunde — e que a trava TV7
pede para não simplificar.

**§3º:** as Procuradorias e Departamentos Jurídicos das autarquias e fundações públicas são órgãos
**vinculados** à AGU — vinculados, não integrantes do art. 2º, I. **§4º:** o AGU é auxiliado por
dois Secretários-Gerais, o de **Contencioso** e o de **Consultoria**. **§5º:** lista quem são
membros da AGU, entre eles os **Advogados da União** e os **Procuradores da Fazenda Nacional** —
carreiras distintas, também nomeadas no art. 20 ao lado da de Assistente Jurídico.

## 2. Os cinco perímetros — o mapa em uma tabela

| Órgão | Perímetro, com o dispositivo |
|---|---|
| **Advogado-Geral da União** | Dirige a instituição (art. 4º, I); **representa a União junto ao STF** (III); defende a norma impugnada em **ADI** (IV); **fixa a interpretação** a ser uniformemente seguida pela Administração Federal (X); **unifica a jurisprudência administrativa** e dirime controvérsias entre órgãos jurídicos federais (XI); **edita súmula administrativa** (XII). Pode representar a União em qualquer juízo (§1º) e **avocar** matérias (§2º) |
| **Procuradoria-Geral da União** | Representação **judicial** da União (art. 9º) — o contencioso não-fiscal |
| **Consultoria-Geral da União** (art. 10) e **Consultorias Jurídicas** (art. 11) | Consultivo: a CGU colabora com o AGU no assessoramento ao Presidente, produzindo pareceres, informações e trabalhos jurídicos; as Consultorias Jurídicas, subordinadas aos Ministros de Estado, assessoram, coordenam os órgãos jurídicos vinculados, fixam interpretação na sua área **quando não houver orientação normativa do AGU** (III) e fazem o exame **prévio e conclusivo** de editais, contratos e dos atos de inexigibilidade ou dispensa de licitação (VI) |
| **Procuradoria-Geral da Fazenda Nacional** (arts. 12 e 13) | Dívida ativa tributária da União e matéria **fiscal**, mais o consultivo no âmbito do Ministério da Fazenda |
| **Órgãos jurídicos das autarquias e fundações** (arts. 2º §3º, 17 e 18) | Representação judicial e extrajudicial da entidade, consultivo e inscrição dos **próprios** créditos em dívida ativa — campo da PGF, detalhado em `pgf-autarquias-e-inss` |

## 3. A escada de instâncias da PGU (art. 9º)

À PGU, subordinada direta e imediatamente ao AGU, incumbe representar a União **judicialmente**, nos
termos e limites da Lei Complementar:

- **§1º** — ao **Procurador-Geral da União** compete representá-la junto aos **tribunais superiores**;
- **§2º** — às **Procuradorias Regionais da União**, perante os **demais tribunais**;
- **§3º** — às **Procuradorias da União** organizadas em cada Estado e no DF, junto à **primeira
  instância** da Justiça Federal, comum e especializada;
- **§4º** — o Procurador-Geral pode atuar perante os órgãos dos §§2º e 3º, e os Procuradores
  Regionais perante os do §3º.

A escada sobe: instância superior pode descer, a inferior não sobe por conta própria. O método de
defesa nessa frente está em `agu-defesa-geral-da-uniao`.

## 4. O perímetro fiscal — o que a PGFN faz, com a lista fechada

**Art. 12** — à PGFN, órgão administrativamente subordinado ao titular do **Ministério da Fazenda**,
compete especialmente: **I** apurar a liquidez e certeza da dívida ativa da União de natureza
tributária, inscrevendo-a para cobrança amigável ou judicial; **II** representar **privativamente** a
União na execução de sua dívida ativa de caráter tributário; **IV** examinar previamente a legalidade
de contratos, acordos, ajustes e convênios que interessem ao Ministério da Fazenda, inclusive os da
dívida pública externa, e promover a respectiva rescisão; **V** representar a União nas **causas de
natureza fiscal**.

**Parágrafo único — as oito causas de natureza fiscal:** tributos de competência da União, inclusive
infrações à legislação tributária; empréstimos compulsórios; apreensão de mercadorias, nacionais ou
estrangeiras; decisões de órgãos do contencioso administrativo fiscal; benefícios e isenções fiscais;
créditos e estímulos fiscais à exportação; responsabilidade tributária de transportadores e agentes
marítimos; e incidentes processuais suscitados em ações de natureza fiscal.

**A lista é o teste.** Matéria que não cabe em nenhum dos oito incisos não é causa de natureza fiscal
— e, não sendo, a atribuição provavelmente é de outro órgão. **Art. 13:** a PGFN também desempenha
consultoria e assessoramento jurídicos no âmbito do Ministério da Fazenda e seus órgãos autônomos e
entes tutelados, regendo-se, nessa função, pela própria LC 73/93.

## 5. A pergunta de triagem, na ordem

1. **A causa é de natureza fiscal** (cabe em algum dos oito incisos do parágrafo único do art. 12)?
   → **PGFN**. Siga para `pgfn-divida-ativa-uniao` ou `carf-contencioso-administrativo`.
2. **O titular do direito ou da obrigação é autarquia ou fundação pública federal**, não a União?
   → órgão jurídico da entidade (arts. 17 e 18) → `pgf-autarquias-e-inss`.
3. **É contencioso judicial da União fora da matéria fiscal?** → **PGU**, pela escada do art. 9º →
   `agu-defesa-geral-da-uniao`.
4. **É consultivo?** → Consultoria-Geral da União ou a Consultoria Jurídica do Ministério (arts. 10
   e 11) → `parecer-consultivo` (chassi).
5. **É STF, ADI ou fixação de interpretação para toda a Administração Federal?** → atribuição do
   **Advogado-Geral da União** (art. 4º, III, IV, X-XII).

Se a resposta não sair limpa da tabela do art. 12 e do art. 9º, o produto **diz que não sabe** e
manda conferir a norma interna de distribuição — nunca chuta o órgão.

## Travas desta skill

- **TV7 (a desta skill).** PGFN ≠ AGU inteira. Nenhuma frase trata os dois como sinônimos, e a
  atribuição se resolve **antes** da peça, não depois.
- **P2 — nada sem lastro.** Tudo aqui está em `context/lc-73-agu.md`. **A Lei 10.480/2002, que criou
  a PGF, não está nos anexos** → estrutura e competências da PGF saem como `[VERIFICAR]`. Ato
  regimental, portaria de distribuição interna e organograma atual idem.
- **P1 — esfera.** Estrutura da advocacia pública **federal**. Procuradoria de Estado ou de
  Município tem lei orgânica própria — é dos irmãos `procurador-estadual-os` e
  `procurador-municipal-os`, que nunca presumem esta estrutura por analogia (P5).
- **P4 — conformidade.** O mapa é estudo; a confirmação da atribuição no caso concreto é do
  procurador (Portaria AGU nº 226/2026 — `context/governanca-ia-procuradorias.md`).

**Próximo passo:** resolvida a atribuição, siga a rota da seção 5. Toda entrega fecha por
`suprema-corte-fazendaria`.

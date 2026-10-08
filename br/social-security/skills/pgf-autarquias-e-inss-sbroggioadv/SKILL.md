---
name: pgf-autarquias-e-inss-sbroggioadv
title: pgf-autarquias-e-inss — a autarquia como cliente, não como ré genérica
description: 'A representação das autarquias e fundações públicas federais pela ótica do ente — a frente da Procuradoria-Geral Federal, incluído o contencioso previdenciário visto do lado da autarquia. Traz o que a LC 73/93 fixa sobre esses órgãos (art. 2º §3º, vinculados à AGU; art. 17, com a representação judicial e extrajudicial, a consultoria e a inscrição dos próprios créditos em dívida ativa; art. 18, que manda aplicar o art. 11 no consultivo), a prerrogativa processual que o CPC 183 e o 496 estendem expressamente às autarquias e fundações de direito público, e a transação própria dessa camada — a do art. 1º §4º III e do Capítulo III-A da Lei 13.988/2020, de relevante interesse regulatório, criado pela Lei 14.973/2024. Marca em amarelo o que depende da Lei 10.480/2002, que está fora dos anexos, e mantém a fronteira dura com o plugin do segurado. Aciona: "quem representa autarquia federal", "defesa do INSS", "dívida ativa de autarquia", "transação de autarquia", "PGF ou PGFN?", "fundação
  pública federal em juízo".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-federal-os-marketplace/tree/main/procurador-federal-os/skills/pgf-autarquias-e-inss
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: social-security
language: pt
---

# pgf-autarquias-e-inss — a autarquia como cliente, não como ré genérica

Autarquia e fundação pública federal não são "a União com outro nome": têm órgão jurídico próprio,
crédito próprio, dívida ativa própria e um regime de transação que a União não tem. Esta skill trata
dessa camada. Texto verbatim em `context/lc-73-agu.md`, `context/transacao-lei-13988.md` e
`context/prerrogativas-cpc.md`; nada aqui sai de memória. Este produto atende a **União** e às
entidades federais a ela vinculadas.

## Quando esta skill entra

- Quando o polo passivo (ou ativo) é autarquia ou fundação pública federal, não a União.
- No contencioso previdenciário de massa **pela ótica da autarquia**.
- Quando a autarquia tem crédito próprio a inscrever e cobrar.
- Quando a composição de dívida de autarquia esbarra em interesse regulatório.

## ⚠️ A nota amarela que abre a skill

A **Procuradoria-Geral Federal foi criada pela Lei 10.480/2002**, que **não está entre os anexos
deste produto**. O número entra porque a pesquisa o confirmou; a **estrutura, as competências e a
organização interna da PGF** dependem desse texto e, portanto, saem sempre como `[VERIFICAR]`, para
conferência na fonte antes de ir a peça ou parecer. O que esta skill afirma com lastro é o que a
**LC 73/93** diz sobre os órgãos jurídicos das autarquias e fundações — que é bastante, e é a
âncora institucional da frente.

## 1. O que a LC 73/93 fixa sobre esses órgãos

**Art. 2º, §3º:** "As Procuradorias e Departamentos Jurídicos das autarquias e fundações públicas
são órgãos **vinculados** à Advocacia-Geral da União." Vinculados — não integrados aos órgãos de
direção superior do art. 2º, I. A diferença explica por que a atuação tem órgão próprio e por que a
supervisão vem de fora: pelo **art. 6º**, compete à Corregedoria-Geral "supervisionar e promover
correições nos órgãos vinculados à Advocacia-Geral da União".

**Art. 17 — a competência, com os três incisos:**

| Inciso | Competência do órgão jurídico da autarquia/fundação |
|---|---|
| **I** | a sua **representação judicial e extrajudicial** |
| **II** | as respectivas atividades de **consultoria e assessoramento jurídicos** |
| **III** | a **apuração da liquidez e certeza dos créditos**, de qualquer natureza, inerentes às suas atividades, **inscrevendo-os em dívida ativa**, para fins de cobrança amigável ou judicial |

O **inciso III** é o dispositivo mais subestimado da frente: a autarquia inscreve **os próprios**
créditos, de qualquer natureza. Não é a PGFN que inscreve por ela — a PGFN inscreve a dívida ativa
**da União** (art. 12, I, e LEF art. 2º §4º). Confundir as duas inscrições é o erro de atribuição
mais comum aqui, e é matéria da trava TV7 (`pgu-e-estrutura-da-agu`).

**Art. 18:** no desempenho das atividades de consultoria e assessoramento aos órgãos jurídicos das
autarquias e fundações públicas "aplica-se, no que couber, o disposto no art. 11 desta lei
complementar" — o artigo das Consultorias Jurídicas, que inclui, no inciso VI, o exame **prévio e
conclusivo** de editais de licitação, contratos e dos atos de inexigibilidade ou dispensa. É o que
ancora o consultivo da autarquia; a ótica do ente em licitação está em
`convenios-e-licitacoes-consultivo` (chassi), nunca a do licitante.

## 2. A prerrogativa alcança a autarquia — com o mesmo degrau da União

O texto do chassi (`context/prerrogativas-cpc.md`) é expresso, e é isso que evita a defesa mais
tímida do que podia ser:

- **CPC 183, caput:** o prazo em dobro, contado da intimação pessoal, é da União, dos Estados, do
  DF, dos Municípios "**e suas respectivas autarquias e fundações de direito público**". ⚠️ A trava
  **P7** vale igual: o §2º afasta o dobro quando lei específica fixa prazo próprio.
- **CPC 496, I:** está sujeita ao duplo grau a sentença proferida contra a União, Estados, DF,
  Municípios "e respectivas autarquias e fundações de direito público".
- **CPC 496, §3º, I:** o degrau de dispensa por valor da **União e das respectivas autarquias e
  fundações de direito público** é de **1.000 salários mínimos** — o mais alto dos três. E a
  dispensa exige **valor certo e líquido**: condenação ilíquida não dispensa.

Duas leituras práticas: a prerrogativa é da entidade **de direito público**, não de qualquer pessoa
jurídica ligada à administração; e a autarquia federal responde pelo degrau da União, não pelos
menores. Método completo em `prerrogativas-processuais`.

## 3. O contencioso previdenciário pela ótica da autarquia — e a fronteira

O INSS é autarquia federal, e o seu contencioso é a maior massa desta camada: concessão e revisão de
benefício, teses repetidas, ações acidentárias, cumprimento de decisões. O que esta skill faz é
tratar a **posição da autarquia**:

- **Triagem antes da tese.** Demanda de massa contra a autarquia se enfrenta por padrão do órgão e
  não caso a caso — a contenção, o IRDR e a suspensão estão em `acoes-de-massa` (chassi).
- **Anti-tese-superada, do lado do ente.** Se a tese administrativa da autarquia já está batida em
  repetitivo ou súmula, insistir produz condenação com honorários. `suprema-corte-fazendaria` roda a
  conferência **antes** da contestação; o resultado pode ser reconhecer o pedido, e reconhecer cedo
  é decisão técnica, não derrota.
- **Prerrogativas integrais.** Prazo em dobro, remessa necessária com o degrau de 1.000 SM e
  honorários por faixa — os três se aplicam à autarquia (seção 2).

**A fronteira, e ela é dura:** **nenhuma regra substantiva de direito previdenciário está nos anexos
deste produto.** Requisito de benefício, carência, cálculo de RMI, regra de transição, tese de
revisão — nada disso tem lastro aqui, e tudo sai como `[VERIFICAR]` para conferência na fonte. O
mérito previdenciário pela ótica do **segurado** é do `previdenciario-adv-os`, plugin irmão da casa;
este produto **não duplica** aquele conteúdo nem o inverte por conta própria. Aqui se cuida da
**posição processual e institucional** da autarquia, não do direito material do benefício.

## 4. A transação que só existe nesta camada

A Lei 13.988/2020 (`context/transacao-lei-13988.md`) alcança as autarquias e fundações por duas
portas distintas:

**Porta comum — art. 1º, §4º, III** (redação da Lei 14.689/2023): a lei aplica-se, no que couber, à
dívida ativa das autarquias e fundações públicas federais cujas inscrição, cobrança e representação
incumbam à **Procuradoria-Geral Federal** ou à Procuradoria-Geral do Banco Central. E o **art. 10**
põe a PGF entre quem pode propor a transação, individualmente ou por adesão.

**Porta exclusiva — Capítulo III-A, arts. 22-C a 22-E** (incluídos pela Lei 14.973/2024), a
transação **de relevante interesse regulatório**:

- **Art. 22-C:** a PGF poderá propor transação na cobrança da dívida ativa das autarquias e
  fundações públicas federais, **de natureza não tributária**, quando houver **relevante interesse
  regulatório previamente reconhecido por ato do Advogado-Geral da União**. O **§1º** define:
  considera-se presente quando "o equacionamento de dívidas for necessário para assegurar as
  políticas públicas ou os serviços públicos prestados pelas autarquias e fundações públicas
  federais credoras".
- Os demais requisitos do art. 22-C: evitar o **agravamento de problema regulatório ou na prestação
  de serviço público**; o **tempo necessário à execução da medida, vedado o reconhecimento por prazo
  indeterminado**; e, no caso das **agências reguladoras**, a prévia **Análise de Impacto
  Regulatório** do art. 6º da Lei 13.848/2019.
- **Art. 22-D:** a PGF poderá, em juízo de oportunidade e conveniência, propor essa transação; o
  **§6º** afasta a vedação de redução do principal (art. 11, §2º, I) no pagamento à vista de
  créditos que consistam em **multa de processo administrativo sancionador**; e o **§7º** amplia em
  até **12 meses** o limite de prazo do art. 11, §2º, III, quando o devedor comprovar projetos de
  interesse social vinculados à política pública ou aos serviços da entidade credora.
- **Art. 22-E:** ato do Advogado-Geral da União disciplina a matéria — o ato **não está nos anexos**
  → `[VERIFICAR]`.

A leitura que importa: nesta camada a transação não é só recuperação de crédito; é **instrumento
regulatório**, e o reconhecimento do interesse é ato do AGU, prévio, não presumível pelo procurador.
As regras gerais (tetos, vedações, rescisão) estão em `transacao-tributaria-federal`.

## Travas desta skill

- **P1 — esfera.** Entidade **federal**. Autarquia estadual ou municipal é dos irmãos
  `procurador-estadual-os` e `procurador-municipal-os`.
- **P2 — nada sem lastro.** LC 73/93, CPC e Lei 13.988/2020 estão nos anexos. **Lei 10.480/2002,
  regra de benefício previdenciário, ato do AGU e norma interna da entidade não estão** →
  `[VERIFICAR]`, nunca de memória.
- **P5 — não presumir.** Cada autarquia tem lei de criação e regulamento próprios: sem o texto, o
  produto pergunta. Não se aplica por analogia o regime de uma entidade a outra.
- **P3 — anti-tese-superada.** Tese administrativa da autarquia passa por `suprema-corte-fazendaria`
  antes de virar contestação de massa.
- **P4 — conformidade.** Dado de segurado e de administrado é sensível: tratamento local, nunca em
  ferramenta externa, e revisão humana obrigatória (Portaria AGU nº 226/2026 —
  `context/governanca-ia-procuradorias.md`).

**Próximo passo:** quem tem atribuição → `pgu-e-estrutura-da-agu`. Defesa não-fiscal da própria
União → `agu-defesa-geral-da-uniao`. Tese repetida → `acoes-de-massa`. Fecha por
`suprema-corte-fazendaria`.

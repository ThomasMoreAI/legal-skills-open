---
name: convenios-e-licitacoes-consultivo-sbroggioadv
title: convenios-e-licitacoes-consultivo — o ente que contrata e o ente que repassa
description: 'A contratação e o repasse pela ótica do Estado que CONTRATA e que REPASSA — nunca pela do licitante. Fronteira dura no topo: impugnação de edital, recurso do licitante, defesa em sanção e MS de licitante são domínio do licitacoes-adv-os — esta skill aponta para lá em vez de duplicar. Cobre três frentes: análise prévia de edital e de minuta como check-list de consistência interna do ente; convênios e instrumentos de repasse, do plano de trabalho à prestação de contas; e a LINDB aplicada ao contrato em curso — art. 24 para o ajuste antigo, arts. 20 e 21 contra a invalidação que não diz suas consequências, art. 22 para as condições reais do gestor e art. 26 para o compromisso. A Lei 14.133/2021 é nomeada como a norma vigente de licitações e contratos, mas seus dispositivos e todo o marco de repasses estão fora dos anexos: saem [VERIFICAR]. Aciona: "analisar minuta de edital", "parecer sobre contrato administrativo", "convênio com outro ente", "prestação de contas de repasse",
  "posso aditar este contrato?".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/convenios-e-licitacoes-consultivo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: government-contracts
language: pt
---

# convenios-e-licitacoes-consultivo — o ente que contrata e o ente que repassa

Este produto atende o **Estado**. Aqui a procuradoria olha o processo de contratação **de
dentro**: antes do edital sair, antes da minuta ser assinada, antes de o repasse ser aprovado.

## Fronteira dura — declarada antes de qualquer conteúdo

> **A ótica do LICITANTE não é desta casa.** Impugnação de edital, pedido de esclarecimento,
> recurso administrativo do licitante, defesa em processo de sanção, mandado de segurança de
> licitante e disputa entre concorrentes são domínio do **`licitacoes-adv-os`** — plugin próprio da
> família, com cobertura completa de Lei 14.133/2021 e do contencioso do particular.

Esta skill **aponta para lá e não duplica**. O que fica aqui é o inverso do balcão: o parecer que o
ente pede à própria procuradoria antes de contratar, e o acompanhamento do que o ente repassa ou
recebe. Quando a pergunta que chega é do licitante — mesmo que quem pergunte seja o procurador —
o encaminhamento é o cross-link, não uma versão paralela do conteúdo.

## Aviso de lastro, dito de saída

**Com lastro:** a **Lei 14.133/2021** é a norma de licitações e contratos administrativos, já
mapeada na família (vigência ✅ conferida) — o **nome e a vigência** podem ser citados. E a **LINDB
arts. 20-30**, verbatim em `context/lindb-20-30.md`.

⚠️ **Sem lastro → `[VERIFICAR]`, sem exceção:** todo **dispositivo** da Lei 14.133/2021 (inclusive o
artigo que impõe o parecer jurídico prévio, as modalidades, os limites de aditamento e o regime
sancionatório) · **todo o marco normativo de convênios, termos de fomento, termos de colaboração,
contratos de repasse e transferências voluntárias** · as regras de **prestação de contas** e as
instruções normativas dos tribunais de contas. Nenhum desses textos consta do `context/` deste
produto. A skill entrega o **método de análise**, que é o que se replica; o dispositivo vem da fonte,
conferido pelo procurador (trava **P2**).

## Frente 1 — análise prévia de edital e de minuta

O parecer prévio **não** é impugnação: é conferência de consistência interna. Roteiro por camadas,
da que mais anula para a que menos:

| Camada | O que se confere | Sinal de risco |
|---|---|---|
| **Autorização e competência** | Quem autorizou a contratação, com que ato e em que competência | Ato de autorização ausente ou assinado por quem não podia |
| **Instrução do processo** | Estudo da necessidade, definição do objeto, pesquisa de preço, dotação orçamentária | Objeto descrito por marca ou por atributo que só um fornecedor atende |
| **Coerência interna** | Edital × anexos × minuta contratual falam a mesma coisa (prazo, objeto, obrigações, penalidade, garantia) | Minuta que contradiz o edital — é a origem silenciosa da maior parte do contencioso |
| **Execução e fiscalização** | Quem fiscaliza, como se mede o cumprimento, como se paga | Fiscal não designado, ou critério de aceite subjetivo |
| **Penalidade e rescisão** | Hipóteses, gradação, contraditório | Penalidade sem procedimento — inaplicável na prática |

**A conclusão do parecer prévio é opinativa** (ver `parecer-consultivo`): opina-se pela viabilidade
jurídica **observadas as ressalvas**, e a decisão de contratar é da autoridade. Parecer prévio que
determina não protege o ente — vincula o procurador.

## Frente 2 — convênios e instrumentos de repasse

Duas posições, e o parecer muda inteiro conforme a do caso:

- **O ente REPASSA** (concedente): a análise se concentra em plano de trabalho compatível com o
  objeto, capacidade do recebedor, cronograma de desembolso, contrapartida, obrigação de prestar
  contas e as consequências do não cumprimento.
- **O ente RECEBE** (convenente): a análise se concentra na capacidade real de executar no prazo, na
  contrapartida que o ente terá de suportar, e no **passivo de prestação de contas** — que é onde o
  problema aparece anos depois, com o gestor da época já fora.

**A pergunta que evita o passivo, feita antes da assinatura:** *quem, no ente, ficará responsável
por prestar contas, com que documentação e em que prazo?* Convênio assinado sem essa resposta gera
glosa, tomada de contas e — no pior cenário — ação de improbidade. Registre a resposta no parecer.

Todos os dispositivos desta frente → `[VERIFICAR]`. O **método** acima independe deles.

## Frente 3 — a LINDB aplicada ao contrato em curso (a base anchorada)

É aqui que o consultivo do ente tem munição verbatim (`context/lindb-20-30.md`):

- **Ajuste antigo sob revisão** → **art. 24**: a validade do que já se completou se julga pelas
  **orientações gerais da época**, e é **vedado** declarar inválidas situações plenamente
  constituídas com base em **mudança posterior** de orientação. O parágrafo único inclui a **prática
  administrativa reiterada e de amplo conhecimento público** entre as orientações gerais.
- **Mudança de entendimento do controle** → **art. 23**: interpretação nova que impõe novo dever
  **deverá prever regime de transição** quando indispensável.
- **Contra a anulação que não mede o efeito** → **arts. 20 e 21**: não se decide por valores
  jurídicos abstratos sem considerar as **consequências práticas**, e a decisão que invalida
  **deverá indicar de modo expresso** as consequências jurídicas e administrativas. O art. 21,
  parágrafo único, ainda manda indicar as **condições para regularização proporcional** e veda impor
  ônus **anormais ou excessivos**. É o fundamento direto da manifestação contra acórdão de tribunal
  de contas que anula ajuste sem enfrentar o efeito da anulação.
- **Condições reais do gestor** → **art. 22**, com os obstáculos e as dificuldades reais e, no §2º,
  os critérios de dosimetria da sanção.
- **Encerrar a incerteza sem litígio** → **art. 26**: compromisso celebrado **após oitiva do órgão
  jurídico**, com efeitos a partir da **publicação oficial**; o §1º exige clareza sobre obrigações,
  prazo e sanções (IV) e **veda desoneração permanente** de dever reconhecido por orientação geral
  (III). Lembre: o **§1º II e o §2º são VETADOS** — sem texto, nunca citados.
- **Fixar para o futuro** → **art. 30** e o parágrafo único: súmula administrativa **vinculante
  perante o órgão**, que ainda dispensa remessa necessária pelo **CPC 496 §4º IV**.

## Frente 4 — o que vem depois, e para onde vai

- **Tomada de contas e defesa perante o controle externo** → `defesa-no-tce-estadual` (Tribunal de Contas do Estado).
- **Imputação de improbidade** ao gestor ou ao parecerista → `improbidade-defesa-e-autoria`, onde a
  LINDB 22 e 28 já são a ponte de defesa.
- **Litígio judicial sobre o contrato** → `defesa-do-ente-contestacao`.
- **Cobrança de valor a devolver** ao erário → esteira de dívida ativa da esfera e `execucao-fiscal-lef`.

## Travas desta skill

- **P2** — Lei 14.133/2021 pelo nome, sim; **dispositivo dela, não**. Todo o marco de convênios e
  repasses sai `[VERIFICAR]`. Com lastro aqui: LINDB arts. 20-30 e CPC 496 §4º IV.
- **Vetos da LINDB** — art. 23 par. único, art. 25, art. 26 §1º II e §2º, art. 28 §§1º-3º, art. 29
  §2º não têm texto.
- **Fronteira** — a ótica do licitante é do `licitacoes-adv-os`. Se a análise começou a redigir
  impugnação, recurso do licitante ou defesa em sanção do particular, **parou aqui**: é cross-link.
- **P1** — nenhuma matéria substantiva de outra esfera entra, inclusive em exemplo de objeto
  contratado ou de tributo incidente sobre o contrato.
- **P5** — nada sobre honorários do procurador, regime de servidores ou lei orgânica por analogia;
  a norma interna de contratação do ente também é local — sem ela, o parecer pergunta.
- **P4** — o parecer sai completo, com revisão humana obrigatória e responsabilidade indelegável;
  dado de processo administrativo e de fornecedor fica local e mascarado.
- **P3** — orientação firmada aqui vincula o órgão (LINDB 30): passa pelo
  `suprema-corte-fazendaria` antes de sair.

## Cross-links

`parecer-consultivo` (a estrutura da peça) · `lindb-como-metodo` (a base verbatim) ·
`improbidade-defesa-e-autoria` · `desapropriacao` (a aquisição de imóvel pelo ente) ·
`acoes-de-massa` (a súmula administrativa) · `execucao-fiscal-lef` (a devolução ao erário inscrita)
· `conformidade-ia-institucional` · `suprema-corte-fazendaria` (**QA obrigatória no fecho**) ·
`estilo-e-fronteiras`.
Fora da casa: **`licitacoes-adv-os`** (a ótica do licitante — a fronteira central desta skill) ·
`tributario-societario-adv-os` · `civel-adv-os` · `juris-adv-os`.

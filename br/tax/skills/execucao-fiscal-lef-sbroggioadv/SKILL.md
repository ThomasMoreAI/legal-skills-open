---
name: execucao-fiscal-lef-sbroggioadv
title: execucao-fiscal-lef — a esteira, do ato de inscrição ao leilão, pela ótica do exequente
description: 'O rito da Lei 6.830/80 ponta a ponta pela ótica de quem cobra: a inscrição em dívida ativa como ato de controle de legalidade que suspende a prescrição por 180 dias (art. 2º §3º), os seis requisitos do Termo de Inscrição e da CDA e o vício que se emenda até a decisão de primeira instância com devolução do prazo de embargos (§8º), presunção relativa de certeza e liquidez (art. 3º), legitimados (art. 4º), competência absoluta que exclui o juízo universal (art. 5º), o despacho que já é ordem de citação, penhora, arresto e avaliação (art. 7º), citação e interrupção da prescrição (art. 8º), garantias e ordem de penhora (arts. 9º e 11), embargos só após garantia (art. 16), leilão e adjudicação — e onde a LEF diverge do CPC. Aciona: "execução fiscal", "CDA", "dívida ativa", "penhora", "embargos à execução fiscal", "citação do executado", "leilão", "rito da LEF".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/execucao-fiscal-lef
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: tax
language: pt
---

# execucao-fiscal-lef — a esteira, do ato de inscrição ao leilão, pela ótica do exequente

A execução fiscal é o único processo em que a Fazenda chega com o título que ela mesma constituiu —
força e risco: o que a procuradoria faz **antes** de ajuizar decide quase tudo o que vem depois.
Esta skill percorre o rito da Lei 6.830/80 na ordem em que ele acontece, marcando onde a LEF diverge
do CPC e onde o vício nasce.

Texto verbatim em `context/lef-6830.md`. A LEF é **rito nacional único** — o art. 1º alcança União,
Estados, DF, Municípios e autarquias sem distinção procedimental. Este produto atende
o **Estado**; o que muda por esfera é o **crédito** inscrito, nunca o rito.

## 1. Antes do processo — inscrição e CDA (onde se ganha ou se perde a execução)

**Art. 2º §3º:** a inscrição "se constitui no ato de controle administrativo da legalidade", é feita
pelo órgão competente para apurar liquidez e certeza, e **suspende a prescrição por 180 dias, ou até
a distribuição da execução, se esta ocorrer antes**. Duas consequências: a inscrição não é
formalidade de cartório, é ato de controle e é da procuradoria; e a janela de 180 dias amarra
inscrição e ajuizamento numa única gestão de prazo.

**Requisitos do Termo de Inscrição (art. 2º §5º)** — a CDA "conterá os mesmos elementos" (§6º),
autenticada pela autoridade competente:

| Inciso | Requisito |
|---|---|
| I | nome do devedor, dos **co-responsáveis** e, sempre que conhecido, o domicílio ou residência |
| II | **valor originário**, termo inicial e **forma de calcular** juros de mora e demais encargos |
| III | **origem, natureza e fundamento legal ou contratual** da dívida |
| IV | indicação, se for o caso, de sujeição à atualização monetária, com fundamento legal e termo inicial |
| V | **data e número da inscrição** no Registro de Dívida Ativa |
| VI | número do **processo administrativo ou do auto de infração**, se neles apurado o valor |

**Ler os incisos I e II como o exequente.** O I é onde o **co-responsável** entra desde a origem —
nomear o sócio na inscrição, havendo fundamento, evita a discussão de redirecionamento lá na frente
(`redirecionamento-socios`). O II exige a **forma de calcular**, não só o valor final: CDA com um
número sem dizer como se chega a ele é a que cai por iliquidez.

**§8º — a porta de conserto, com prazo:** "Até a decisão de primeira instância, a Certidão de Dívida
Ativa poderá ser emendada ou substituída, assegurada ao executado a devolução do prazo para
embargos." Vício formal identificado **antes** da sentença se emenda, ao custo do prazo devolvido —
não da extinção. Depois da decisão de primeira instância, a porta fecha.

**Art. 3º:** a dívida regularmente inscrita **goza da presunção de certeza e liquidez**, que o
parágrafo único declara **relativa**, ilidível "por prova inequívoca, a cargo do executado ou de
terceiro". A presunção inverte o ônus; não o elimina.

## 2. Contra quem — art. 4º

A execução pode ser promovida contra **o devedor · o fiador · o espólio · a massa · o responsável,
nos termos da lei, por dívidas tributárias ou não · os sucessores a qualquer título**. O §2º manda
aplicar à dívida ativa "de qualquer natureza" as normas de responsabilidade da legislação
tributária, civil e comercial; o §4º estende à dívida **não tributária** os arts. 186 e 188 a 192 do
CTN. O §1º responsabiliza solidariamente síndico, liquidante, inventariante e administrador que
alienarem ou derem em garantia bens administrados antes de garantidos os créditos da Fazenda.
E o **art. 30** põe a responder "a totalidade dos bens e das rendas, de qualquer origem ou
natureza", inclusive os gravados por ônus real ou cláusula de inalienabilidade ou
impenhorabilidade, seja qual for a data do gravame — só os absolutamente impenhoráveis escapam.

## 3. Ajuizamento — arts. 5º a 8º

- **Art. 5º — competência absoluta:** a competência para a execução da dívida ativa **exclui a de
  qualquer outro juízo, inclusive o da falência, concordata, liquidação, insolvência ou inventário**.
- **Art. 6º — inicial de três itens:** juiz a quem é dirigida · pedido · requerimento de citação. A
  CDA a instrui e "dela fará parte integrante, como se estivesse transcrita" (§1º), podendo formar
  **documento único** com a inicial (§2º). A prova da Fazenda **independe de requerimento na
  inicial** (§3º), e o valor da causa é o da certidão com encargos (§4º).
- **Art. 7º — o despacho que defere a inicial já é ordem** para citação, penhora, arresto (se o
  executado não tiver domicílio ou dele se ocultar), registro **independentemente de custas** e
  avaliação.
- **Art. 8º — citação:** 5 dias para pagar ou garantir; pelo correio com AR, salvo se a Fazenda
  requerer outra forma (I); Oficial de Justiça ou edital se o AR não retornar em 15 dias (III);
  edital com prazo de 30 dias (IV), 60 dias se ausente do País (§1º). **§2º — "O despacho do Juiz,
  que ordenar a citação, interrompe a prescrição."** É o despacho, não a citação: dado que decide
  contagem.

## 4. Garantia e penhora — arts. 9º a 15

O executado pode **depositar em dinheiro** (I), oferecer **fiança bancária ou seguro garantia** (II,
redação da Lei 13.043/2014), **nomear bens** na ordem do art. 11 (III) ou indicar bens de terceiro
aceitos pela Fazenda (IV). Depósito, fiança e seguro **produzem os mesmos efeitos da penhora** (§3º),
mas **só o depósito em dinheiro** faz cessar a responsabilidade por atualização e juros (§4º).
**§7º (Lei 14.689/2023):** as garantias do inciso II "somente serão liquidadas, no todo ou
parcialmente, **após o trânsito em julgado** de decisão de mérito em desfavor do contribuinte,
vedada a sua liquidação antecipada".

**Ordem do art. 11:** dinheiro · título da dívida pública e de crédito com cotação em bolsa · pedras
e metais preciosos · imóveis · navios e aeronaves · veículos · móveis ou semoventes · direitos e
ações. Excepcionalmente pode recair sobre estabelecimento comercial, industrial ou agrícola,
plantações ou edifícios em construção (§1º).

**Art. 15, II — a prerrogativa do exequente:** deferida à Fazenda a **substituição dos bens
penhorados por outros, independentemente da ordem do art. 11**, e o **reforço da penhora
insuficiente**, em qualquer fase.

## 5. Defesa e sentença — arts. 16 a 20

Embargos em **30 dias**, do depósito, da juntada da prova da fiança/seguro ou da intimação da
penhora (art. 16, I-III). **§1º: "Não são admissíveis embargos do executado antes de garantida a
execução."** §2º impõe concentração da defesa; §3º **veda reconvenção e compensação**. A Fazenda
impugna em **30 dias** (art. 17); sendo matéria só de direito, ou com prova exclusivamente
documental, não há audiência e a sentença sai em 30 dias.

## 6. Expropriação — arts. 21 a 24

Edital de leilão publicado uma vez, com **10 a 30 dias** entre publicação e leilão (art. 22 §1º), e
**intimação pessoal do representante judicial** com essa antecedência (§2º). **Art. 24 —
adjudicação pela Fazenda:** antes do leilão, pelo preço da avaliação, se não embargada a execução ou
rejeitados os embargos (I); findo o leilão, sem licitante pelo preço da avaliação, ou com licitantes
**com preferência em igualdade de condições com a melhor oferta**, em 30 dias (II). Se o preço
superar o crédito, a adjudicação só é deferida com **depósito da diferença** pela exequente em 30
dias.

## 7. Onde a LEF diverge do CPC

| Ponto | Regra da LEF |
|---|---|
| Intimação do representante judicial | **Sempre pessoal** (art. 25), admitida vista com remessa |
| Custas | Não paga custas, emolumentos, preparo nem depósito prévio (art. 39) — mas **ressarce** as despesas da parte contrária se vencida |
| Concurso de credores | A cobrança **não se sujeita** a concurso nem a habilitação (art. 29) — o caput e todo o parágrafo único trazem **"(Vide ADPF 357)"** |
| Discussão da dívida fora da execução | Só MS, repetição de indébito ou anulatória **precedida de depósito preparatório** (art. 38); a propositura importa **renúncia ao recurso administrativo** |
| Inscrição cancelada antes da sentença | Execução **extinta sem qualquer ônus para as partes** (art. 26) |
| Alçada dos embargos infringentes | Art. 34, ancorado em **ORTN** — índice extinto; o valor em reais **não** está nesta lei |

⚠️ **Duas marcações obrigatórias.** O **art. 29** e seu parágrafo único (hierarquia União → Estados
→ Municípios no concurso de preferência) saem com a remissão **(Vide ADPF 357)**, como `[VERIFICAR]`
contra o julgado — o desfecho não está nos anexos. E o **art. 34** nunca vira valor em reais a
partir deste anexo.

## Travas desta skill

- **P2 — nada sem lastro.** Todo artigo citado está em `context/lef-6830.md`. Alçada, tabela de
  encargos, portaria do ente e jurisprudência fora dos anexos → `[VERIFICAR]`.
- **P7.** Os prazos deste rito são **prazos próprios de lei específica** (5 dias do art. 8º; 30 dias
  dos arts. 16 e 17): o dobro do CPC 183 **não é automático** aqui — a checagem está em
  `prerrogativas-processuais`.
- **P1.** O rito é comum às três esferas; o **crédito** inscrito é de ICMS, IPVA, ITCMD e demais créditos estaduais e só dele se
  fala neste produto.
- **P3.** Tese sobre o rito já superada em repetitivo é avisada antes de sustentada.
- **P4.** Minuta de inicial, impugnação ou manifestação aqui é estudo e trabalho local — a
  conferência da CDA, dos valores e do protocolo é do procurador, indelegável.

**Próximo passo:** processo parado ou arquivado → `prescricao-intercorrente`. Sócio na mira →
`redirecionamento-socios`. Antes de ajuizar → `triagem-baixo-valor` e
`protesto-e-cobranca-extrajudicial`. Toda entrega fecha por `suprema-corte-fazendaria`.

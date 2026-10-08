---
name: ipva-e-itcmd-sbroggioadv
title: ipva-e-itcmd — os dois tributos que o produto pergunta antes de responder
description: 'Os dois tributos estaduais que **não têm lei nacional**: o IPVA e o ITCMD são instituídos pela lei de cada Estado, e por isso esta skill inverte o método — em vez de afirmar regra, ela PERGUNTA a lei local antes de qualquer tese. Traz a trava P5 em destaque, o questionário obrigatório de levantamento (fato gerador, base, alíquota, isenções, responsabilidade solidária, prazos, lançamento e decadência), o que a Constituição fixa e o que ela devolve ao Estado, e a separação entre o que muda por Estado e o que é comum às três esferas (rito da execução fiscal, requisitos da CDA, prescrição, prerrogativas processuais e precatório). Registra também que o cronograma da reforma tributária alcança o ICMS, e não estes dois — não confundir horizonte de tributo. Aciona: "IPVA", "ITCMD", "imposto sobre herança", "doação", "causa mortis", "transmissão de bens", "propriedade de veículo", "alíquota do IPVA", "isenção de IPVA", "qual a lei do meu Estado".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/ipva-e-itcmd
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: tax
language: pt
---

# ipva-e-itcmd — os dois tributos que o produto pergunta antes de responder

Toda skill deste plugin aplica a trava P2 (nada sem lastro). Esta aplica **P5**, e é a única em que
a trava é o conteúdo principal: **não existe lei nacional de IPVA nem de ITCMD**. A regra que decide
o caso está na lei do Estado — e o produto não a tem. Responder "a alíquota é X" ou "a isenção
alcança Y" sem o texto local é o erro mais caro desta camada, porque parece certo e não é.

Este produto atende o **Estado**.

**Quando entra:** antes de inscrever, exigir ou defender crédito de IPVA ou de ITCMD; quando o
contribuinte alega isenção, imunidade, decadência ou base excessiva; e sempre que a pergunta feita
ao produto pressupõe uma regra que só a lei estadual pode dar.

## ⚠️ A trava P5, em destaque

> **A competência é do Estado (CF 155, I — transmissão causa mortis e doação; CF 155, III —
> propriedade de veículos automotores), e cada Estado tem a sua lei.** Não há lei nacional
> instituindo esses impostos, e **não existe um "texto único" a citar**.

Três consequências operacionais, e nenhuma é opcional:

1. **O produto pergunta, não presume.** Sem a lei estadual (e o regulamento) em mãos, toda afirmação
   de alíquota, base, isenção, prazo ou responsabilidade sai como `[VERIFICAR]` com a pergunta
   explícita — nunca como resposta.
2. **Não se aplica por analogia a lei de outro Estado.** Regra vista em manual, em decisão de outro
   tribunal ou em outro Estado **não vale** aqui. É o mesmo vício que a P5 fecha quando proíbe
   presumir o regime de servidores.
3. **O texto do art. 155 da Constituição não está capturado nos anexos deste plugin.** A competência
   acima é a moldura, e ela consta como base da trava P1 em `context/travas-fazendarias.md` (CF
   153/155/156). Para **transcrever** qualquer inciso ou alínea entre aspas: `[VERIFICAR]` na
   Constituição, fonte primária, antes de escrever.

## 1. O questionário obrigatório — o que levantar antes de qualquer tese

O produto abre por aqui. Cada linha sem resposta é um `[VERIFICAR]` que acompanha a minuta até ser
preenchido pelo procurador com o texto local.

| # | Pergunta | Por que decide |
|---|---|---|
| 1 | Qual a **lei estadual** que institui o tributo, e qual a redação vigente hoje? | É a única fonte da regra material |
| 2 | Há **regulamento** ou decreto que a detalhe (tabelas, prazos, formulários)? | Base de cálculo e vencimento costumam morar ali |
| 3 | Como a lei define o **fato gerador** e o seu **momento**? | Define competência temporal, decadência e a lei aplicável |
| 4 | Qual a **base de cálculo** e como ela é apurada? | É onde o contribuinte mais ataca |
| 5 | Quais as **alíquotas** e há **progressividade**? | Varia por Estado e por faixa; nunca de memória |
| 6 | Quais **isenções, imunidades e reduções** a lei prevê, e sob que condição? | A alegação de isenção é a defesa mais comum |
| 7 | Quem é **contribuinte** e há **responsabilidade solidária** (adquirente, alienante, inventariante, tabelião)? | Define o polo passivo da execução |
| 8 | Qual a modalidade de **lançamento** e o **prazo de decadência** correspondente? | Um lançamento fora de prazo derruba o crédito inteiro |
| 9 | Há **parcelamento, transação ou anistia** vigentes no Estado? | Muda a estratégia antes de ajuizar |

Sem as respostas 1 e 2, **o produto não emite tese** — emite o levantamento.

## 2. IPVA — o que muda de Estado para Estado

Os pontos abaixo são **campos a preencher**, não regras afirmadas. Todos dependem da lei local:

- **Fato gerador e momento** — a propriedade do veículo, com o marco temporal que a lei fixar
  (aquisição, primeiro licenciamento, virada do exercício).
- **Base de cálculo** — o valor venal, geralmente por tabela publicada pelo Estado. Qual tabela, qual
  ato a publica e em que data: `[VERIFICAR]`.
- **Alíquotas** — variam por tipo de veículo, combustível e uso. Nunca escrever percentual sem o texto.
- **Isenções** — as recorrentes na prática (pessoa com deficiência, transporte escolar ou de
  passageiros, veículos antigos, atividade específica) **existem em alguns Estados e não em todos**,
  com requisitos e prazos distintos. Tratar como pergunta, não como catálogo.
- **Responsabilidade do alienante** — se responde solidariamente por débitos posteriores à venda
  quando não comunica a transferência, e em que termos, é matéria da lei estadual.
- **Vencimento, parcelamento e vinculação ao licenciamento** — idem.

## 3. ITCMD — o que muda de Estado para Estado

- **As duas hipóteses** — transmissão **causa mortis** e **doação** — são distintas na apuração, no
  responsável e frequentemente na alíquota. Nunca tratar as duas como um bloco só.
- **Base de cálculo e o momento da avaliação** — o critério de valor e a data em que ele se fixa são
  o principal ponto de litígio.
- **Alíquotas e progressividade** — se há faixas e quais, `[VERIFICAR]` na lei do Estado.
- **Contribuinte e responsáveis** — herdeiro, legatário, donatário, doador, inventariante e, quando
  a lei prevê, o **tabelião/registrador** que lavra o ato sem exigir a comprovação do recolhimento.
- **Isenções e limites de valor** — variam muito; não presumir piso.
- **Decadência** — depende do momento em que a lei situa o fato gerador e da modalidade de
  lançamento. É a defesa mais forte do contribuinte em inventário antigo.
- **Bens ou de cujus no exterior** — hipótese que a Constituição remete a lei complementar. Sem o
  texto da norma aplicável nos anexos, o produto marca `[VERIFICAR]` e não afirma competência.

## 4. O que NÃO muda por Estado (e onde já está resolvido)

Nem tudo é local. Uma vez constituído o crédito, o tratamento passa a ser o comum da Fazenda, e o
produto responde direto — sem `[VERIFICAR]` de lei local:

| Frente | Onde resolver |
|---|---|
| Inscrição em dívida ativa, requisitos da CDA, presunção de certeza e liquidez | `divida-ativa-estadual` (LEF, art. 2º §§5º-6º e art. 3º) |
| Rito da execução fiscal, prazos próprios da LEF, penhora e leilão | `execucao-fiscal-lef` |
| Prescrição intercorrente e arquivamento | `prescricao-intercorrente` |
| Decisão de ajuizar ou não, pelo custo de cobrança | `triagem-baixo-valor` |
| Prazo em dobro, remessa necessária, intimação pessoal | `prerrogativas-processuais` |
| Condenação do ente e pagamento | `precatorios-e-rpv` · `precatorio-estadual-regime` |

Essa é a divisão que a trava P5 pressupõe: **a matéria material é local; o processo e a cobrança são
comuns**. Confundir as duas produz os dois erros opostos — presumir regra que não existe, ou marcar
`[VERIFICAR]` em algo que os anexos já respondem.

## 5. Estes dois impostos não estão no cronograma da reforma

O anexo `context/reforma-tributaria-transicao.md` põe em extinção programada, até **2033**, o
**ICMS** (e, na esfera do irmão, o tributo municipal sobre serviços) — substituídos por IBS e CBS.
**IPVA e ITCMD não estão nesse cronograma**, e o produto não os trata como se estivessem: aplicar
aqui o aviso da transição seria inventar horizonte onde o anexo não dá. Qualquer alteração
constitucional ou de lei complementar que os alcance → `[VERIFICAR]` na fonte, nunca de memória.

## Travas desta skill

- **P5 — é a trava desta skill.** Sem a lei do Estado, o produto **pergunta ou marca**; jamais
  assume, jamais aplica por analogia a lei de outro ente.
- **P2.** Alíquota, base, isenção, prazo, número de lei estadual e dispositivo da Constituição não
  estão nos anexos deste plugin → `[VERIFICAR]`, com a pergunta escrita ao lado.
- **P1.** IPVA e ITCMD são do Estado. Tributo de outra esfera não entra aqui: o do Município é do
  `procurador-municipal-os`, o federal, do `procurador-federal-os`.
- **P3.** Tese sobre base, progressividade ou responsabilidade solidária passa por
  `suprema-corte-fazendaria` antes da minuta — é campo com jurisprudência vinculante, e o gate
  confere se a tese do ente ainda se sustenta.
- **P6 — por exclusão.** O aviso da transição é obrigatório para o ICMS; para IPVA e ITCMD, **não se
  aplica** com base nos anexos atuais.
- **P4.** Isto é estudo e minutação local: conferir o texto legal vigente no Estado e assumir a peça
  são atos do procurador, indelegáveis.

**Próximo passo:** crédito constituído → `divida-ativa-estadual`; ajuizar ou não →
`triagem-baixo-valor`; rito → `execucao-fiscal-lef`; ICMS → `icms-conteudo`. Toda entrega fecha por
`suprema-corte-fazendaria`, com o `validador-fazendario-vigente` antes.

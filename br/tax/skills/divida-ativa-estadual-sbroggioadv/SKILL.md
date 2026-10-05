---
name: divida-ativa-estadual-sbroggioadv
title: divida-ativa-estadual — o título antes do processo, e a decisão antes do ajuizamento
description: 'A dívida ativa do Estado da inscrição até a decisão de cobrar: o que a LEF define como dívida ativa e o efeito da inscrição como ato de controle da legalidade que suspende a prescrição por 180 dias (art. 2º §3º), os seis requisitos do Termo de Inscrição e da CDA (art. 2º §§5º-6º) lidos como checklist de vícios que anulam o título, a emenda ou substituição da CDA até a decisão de primeira instância com devolução do prazo de embargos (§8º), a presunção **relativa** de certeza e liquidez (art. 3º) e quem pode figurar no polo passivo (art. 4º). Trata o peso do ICMS na carteira, a decisão entre ajuizar, protestar ou não cobrar — com os números medidos que a sustentam — e separa decadência (antes da inscrição) de prescrição (depois). Aciona: "inscrever em dívida ativa", "requisitos da CDA", "nulidade da CDA", "substituir a certidão", "presunção de liquidez", "vale a pena ajuizar", "carteira da dívida ativa", "prescrição do crédito".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/divida-ativa-estadual
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: tax
language: pt
---

# divida-ativa-estadual — o título antes do processo, e a decisão antes do ajuizamento

A execução fiscal do Estado é ganha ou perdida **antes** da distribuição: num título bem
constituído, e numa decisão consciente sobre cobrar. Esta skill cuida das duas coisas. O rito
processual em si é de `execucao-fiscal-lef`; aqui o assunto é o **crédito** e a **carteira**. Base
verbatim: `context/lef-6830.md`.

Este produto atende o **Estado**.

**Quando entra:** antes de inscrever; quando o executado alega nulidade da CDA; quando se decide
ajuizar, protestar ou arquivar; e em qualquer revisão de estoque da carteira.

## 1. O que é dívida ativa, e o que a inscrição faz — art. 2º

**Caput:** é a dívida definida como **tributária ou não tributária** na **Lei nº 4.320, de 17 de
março de 1964**. O **§1º** amplia: qualquer valor cuja cobrança seja atribuída por lei ao ente é
dívida ativa. O **§2º** define o alcance do valor — abrange **atualização monetária, juros e multa
de mora e demais encargos previstos em lei ou contrato**.

**§3º — o dispositivo que o procurador não pode ignorar:** a inscrição "se constitui no ato de
controle administrativo da legalidade", é feita pelo órgão competente para **apurar a liquidez e
certeza** do crédito, e **suspende a prescrição, para todos os efeitos de direito, por 180 dias, ou
até a distribuição da execução fiscal, se esta ocorrer antes de findo aquele prazo**.

Duas leituras que decidem caso:

- **A inscrição é controle de legalidade, não um carimbo.** Inscrever crédito viciado é criar título
  que cai nos embargos — e o §3º diz expressamente que o órgão inscreve para apurar liquidez e
  certeza.
- **A suspensão de 180 dias é janela curta e condicionada.** Ela cessa com a distribuição, se esta
  vier antes. Tratá-la como prazo extra fixo é onde o crédito prescreve na gaveta.

## 2. Os requisitos do título — art. 2º §§5º a 8º (checklist de vícios)

O **§5º** lista o que o Termo de Inscrição **deverá conter**, e o **§6º** manda que a **CDA contenha
os mesmos elementos**, autenticada pela autoridade competente. Ler como checklist, na ordem:

| # | Requisito (§5º) | O vício típico |
|---|---|---|
| I | Nome do devedor, dos **corresponsáveis** e, quando conhecido, o domicílio de um e de outros | Corresponsável ausente do título — trava o redirecionamento depois |
| II | **Valor originário**, o termo inicial e a **forma de calcular** juros de mora e demais encargos | "Valor atualizado" sem o originário nem o critério: iliquidez alegável |
| III | A **origem, a natureza e o fundamento legal ou contratual** da dívida | Fundamento genérico, sem o dispositivo que sustenta a exigência |
| IV | Indicação de estar a dívida sujeita a **atualização monetária**, o fundamento legal e o termo inicial | Índice aplicado sem previsão indicada |
| V | **Data e número da inscrição** no Registro de Dívida Ativa | Ausência que impede aferir a própria inscrição |
| VI | Número do **processo administrativo ou do auto de infração**, se neles apurado o valor | Elo perdido com o contraditório administrativo |

**§7º:** Termo e Certidão podem ser preparados e numerados por processo manual, mecânico ou
**eletrônico** — o meio eletrônico é o da lei, não uma tolerância.

**§8º — a porta de correção, com prazo e preço:** "Até a decisão de primeira instância, a Certidão
de Dívida Ativa poderá ser emendada ou substituída, **assegurada ao executado a devolução do prazo
para embargos**". Duas consequências práticas: depois da sentença **não há mais substituição**; e
substituir **devolve** o prazo de defesa — é remédio, não manobra sem custo. Substituição não
alcança troca do próprio sujeito passivo ou do fundamento da exigência: aí o vício é de lançamento,
não de certidão → `[VERIFICAR]` no caso concreto antes de sustentar.

## 3. A presunção é relativa — art. 3º

"A Dívida Ativa **regularmente inscrita** goza da presunção de certeza e liquidez." O **parágrafo
único** é a metade que o procurador precisa dizer em voz alta: "A presunção a que se refere este
artigo é **relativa** e pode ser **ilidida por prova inequívoca**, a cargo do executado ou de
terceiro, a quem aproveite."

O ônus é do executado, e é **prova inequívoca** — não alegação. Mas a presunção só se instala se a
inscrição foi **regular**: é o §5º que a sustenta. Título com vício do §5º não chega a atrair o
art. 3º.

## 4. Quem responde — art. 4º

A execução pode ser promovida contra: **o devedor** (I) · o **fiador** (II) · o **espólio** (III) ·
a **massa** (IV) · **o responsável, nos termos da lei**, por dívidas tributárias ou não (V) · **os
sucessores a qualquer título** (VI). O **§2º** manda aplicar à dívida ativa de qualquer natureza as
normas de responsabilidade da legislação tributária, civil e comercial; o **§3º** sujeita os bens
dos responsáveis à execução se os do devedor forem insuficientes; o **§4º** aplica à dívida **não
tributária** o disposto nos arts. 186 e 188 a 192 do CTN.

Quem pode ser **incluído depois**, por dissolução irregular ou sucessão, é matéria de
`redirecionamento-socios` — e o inciso I do §5º do art. 2º acima é o que prepara esse caminho no
próprio título.

## 5. Duas notas de garantia do crédito

- **Art. 5º:** a competência para a execução da dívida ativa **exclui a de qualquer outro Juízo**,
  inclusive o da falência, concordata, liquidação, insolvência ou inventário.
- **Art. 29:** a cobrança judicial **não é sujeita a concurso de credores ou habilitação** em
  falência, concordata, liquidação, inventário ou arrolamento. **Atenção:** o anexo traz neste artigo
  a remissão **"(Vide ADPF 357)"** — antes de sustentar a prerrogativa em concurso, conferir o estado
  da ADPF na fonte primária → `[VERIFICAR]`, e levar ao gate `suprema-corte-fazendaria` (P3).
- **Art. 26:** cancelada a inscrição a qualquer título **antes da decisão de primeira instância**, a
  execução é extinta **sem qualquer ônus para as partes**. É o dispositivo que torna barata a
  correção de rota quando a revisão da carteira mostra crédito insubsistente.

## 6. O ICMS na carteira, e a decisão de cobrar

No Estado, o ICMS é o que dá volume à dívida ativa — e volume não é sinônimo de recuperabilidade.
**P6:** ICMS em extinção programada — **2026** ano-teste · **2029-2032** transição · **2033**
extinção (`transicao-icms-ibs`): horizonte, **não** invalidade — o crédito segue exigível. A
decisão de ajuizar precede a petição, e tem número medido por trás
(`context/resolucoes-cnj-execucao.md`): o custo mínimo de **uma** execução fiscal é de **≈ R$
9.277,00**, e **52,3%** das execuções pendentes tinham valor **inferior a R$ 10.000** — mais da
metade do acervo custava, para cobrar, mais do que valia. É o que sustenta a extinção por ausência
de interesse de agir do **Tema 1184/STF**.

Três saídas, e a escolha é de gestão, não de reflexo:

| Situação | Caminho | Onde |
|---|---|---|
| Crédito abaixo do custo de cobrança, ou sem CPF/CNPJ do executado | **Não ajuizar** / avaliar extinção | `triagem-baixo-valor` (Res. CNJ 547 consolidada, alterada pelas Res. 617/2025 e 689/2026) |
| Crédito recuperável, sem necessidade de constrição imediata | **Cobrança extrajudicial** | `protesto-e-cobranca-extrajudicial` (base legal do protesto de CDA **não** está nos anexos → `[VERIFICAR]`) |
| Crédito com garantia, patrimônio localizável ou risco de prescrição | **Ajuizar** | `execucao-fiscal-lef` |

O caso Salvador/BA, citado nominalmente pelo CNJ, é a prova de que triar não é abrir mão: **−51%** de
acervo com **+87%** de arrecadação no mesmo período. Números exatos, sem arredondar (P2).

## 7. Decadência × prescrição — não confundir os dois lados da inscrição

- **Antes da inscrição** está a **decadência** do direito de lançar — prazo do direito tributário
  cujo dispositivo **não está nos anexos** deste plugin → `[VERIFICAR]` no CTN antes de afirmar.
- **Depois**, corre a **prescrição** da cobrança, suspensa pelos **180 dias** do art. 2º §3º ou até a
  distribuição.
- **Prescrição intercorrente**: **Temas 566-571/STJ** e **Súmula 314/STJ**. O ano de suspensão corre
  automaticamente da ciência da Fazenda sobre a não
  localização do devedor ou de bens. Citação efetiva (inclusive editalícia) ou constrição efetiva
  interrompe; pedido tempestivo depois frutífero retroage ao protocolo (Tema 568). Ver
  `prescricao-intercorrente`.

## Travas desta skill

- **P2.** Todo dispositivo acima está em `context/lef-6830.md`; os números de custo e acervo, em
  `context/resolucoes-cnj-execucao.md`; Temas 566-571 e Súmula 314, em
  `context/temas-e-sumulas-fazendarios.md`. Prazo de decadência, base do protesto de CDA e ementa de
  acórdão **não** estão → `[VERIFICAR]`. Número pode; ementa entre aspas, só após conferir na fonte.
- **P1.** A dívida ativa aqui é a do **Estado** — ICMS, IPVA e ITCMD. Crédito de outra esfera é dos
  irmãos `procurador-municipal-os` e `procurador-federal-os`. O rito da LEF é comum às três; o
  tributo, não.
- **P3.** A remissão "(Vide ADPF 357)" no art. 29 é o exemplo: prerrogativa citada sem conferir o
  estado do julgamento vira peça perdedora. Tudo passa por `suprema-corte-fazendaria`.
- **P5.** Encargo legal, honorários incidentes sobre a inscrição, taxa e índice de atualização
  dependem de **lei do Estado** — sem o texto, o produto pergunta.
- **P6.** Conteúdo de ICMS carrega o aviso da transição — cronograma em `transicao-icms-ibs`.
- **P4.** Conferir o título nos autos e assinar a inscrição são atos do procurador, indelegáveis.

**Próximo passo:** ajuizar → `execucao-fiscal-lef`; não ajuizar → `triagem-baixo-valor`; incluir
sócio → `redirecionamento-socios`; conteúdo do tributo → `icms-conteudo` ou `ipva-e-itcmd`. Fecha
por `suprema-corte-fazendaria`.

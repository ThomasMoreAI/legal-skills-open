---
name: prazos-decadencia-prescricao-consumo-sbroggioadv
title: 'Prazos: Decadência e Prescrição em Consumo'
description: 'Distingue os três trilhos de prazo em consumo: decadência do art. 26, CDC (30/90 dias, vício), prescrição do art. 27, CDC (5 anos, fato do produto/serviço) e o prazo geral do Código Civil (10 anos, indenização por dano decorrente de vício — que não é nem o art. 26 nem o art. 27). Cobre o termo inicial em vício oculto e o critério da vida útil do bem. Aciona: antes de propor qualquer ação de consumo, ao arguir prescrição/decadência em defesa, ou quando a peça precisa nomear corretamente a pretensão (constitutiva × indenizatória) para escolher o prazo certo.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/prazos-decadencia-prescricao-consumo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Prazos: Decadência e Prescrição em Consumo

## Quando esta skill entra
Antes de propor qualquer ação de consumo, ou de arguir prescrição/decadência em defesa: o CDC tem
**dois regimes de prazo diferentes** (decadência do art. 26, prescrição do art. 27) mais um
terceiro trilho do Código Civil que a jurisprudência do STJ consolidou para um caso específico que
nenhum dos dois artigos cobre. Errar o trilho é perder o prazo ou perder a tese.

## Base normativa
- **Art. 26, CDC** — o direito de reclamar por vícios **aparentes ou de fácil constatação** caduca
  em **30 dias** (serviço e produto não durável) ou **90 dias** (serviço e produto durável). §1º:
  a contagem começa na entrega efetiva do produto ou no término da execução do serviço. §2º:
  obstam a decadência (I) a reclamação comprovada perante o fornecedor até resposta negativa
  inequívoca; (III) a instauração de inquérito civil, até seu encerramento. §3º: em **vício
  oculto**, o prazo decadencial só começa quando o defeito ficar **evidenciado**.
- **Art. 27, CDC** — prescreve em **5 anos** a pretensão de reparação por danos causados por
  **fato** do produto ou do serviço (Seção II — acidente de consumo, defeito à segurança),
  contados do conhecimento do dano e de sua autoria.
- **Art. 23, CDC** — a ignorância do fornecedor sobre o vício não o exime (aplica-se aos dois
  regimes).
(fonte: `context/cdc-lei-8078.md`)

## A tabela de 3 trilhos — não confundir
Jurisprudência consolidada do STJ, sem divergência ativa relevante localizada no corpus. A
pretensão é o que decide qual trilho aplicar — não o artigo que "parece" mais próximo:

| Pretensão | Fundamento | Prazo | Natureza |
|---|---|---|---|
| Reclamar de **vício** (exigir substituição/abatimento/restituição, art. 18 §1º) | Art. 26, CDC | 30 dias (não durável) / 90 dias (durável) — da entrega, ou de quando **evidenciado** o vício oculto | Decadência |
| **Indenização** por dano decorrente de **vício** (ação condenatória, não constitutiva) | Prazo geral do CC — **não** o art. 27, CDC | 10 anos (art. 205, CC) | Prescrição |
| **Indenização** por **fato** do produto/serviço (acidente de consumo, defeito de segurança) | Art. 27, CDC | 5 anos, do conhecimento do dano e da autoria | Prescrição |

(fonte: `context/jurisprudencia-sumulas-temas.md`, §6 — capturado 18/08/2026)

## O teste / o passo a passo
1. A pretensão é **constitutiva** (quero trocar/consertar/abater) ou **indenizatória** (quero ser
   ressarcido por um dano)? Constitutiva sobre vício → art. 26 (decadência). Indenizatória → siga.
2. O dano veio de **vício** (o bem não presta, mas o dano fica restrito a ele) ou de **fato/
   defeito** (o bem causou um acidente, um dano à segurança que extrapola o próprio bem)? Vício →
   prazo geral do CC, 10 anos (prescrição). Fato/defeito → art. 27, CDC, 5 anos (prescrição).
3. Se o vício é **oculto**, o prazo decadencial do art. 26 só começa a correr quando o defeito
   ficar **evidenciado** — não da data da aquisição. Critério de referência: **vida útil** do bem —
   o fornecedor pode responder por defeito oculto mesmo fora do prazo de garantia contratual,
   desde que dentro da vida útil esperada; o ônus de provar uso inadequado é do fornecedor.
4. Confira se algum obstáculo do art. 26, §2º interrompeu/obstou a decadência (reclamação formal
   ao fornecedor até resposta negativa; inquérito civil em curso).

## Tese do consumidor × Tese do fornecedor
- **Tese do consumidor:** nomear a pretensão como **indenizatória** sempre que o pedido for de
  dinheiro por dano (não de troca/conserto) — isso muda o prazo de 30/90 dias para 5 ou 10 anos.
  Em vício oculto, defender que o termo inicial é o momento em que o defeito **apareceu**, não a
  data da compra, e usar o critério de vida útil para bens fora da garantia contratual.
- **Tese do fornecedor:** se o pedido é reclamação de vício disfarçada de "indenização" para
  escapar do prazo curto, apontar a natureza real da pretensão (constitutiva) para forçar o art.
  26. Exigir prova de que o defeito só "evidenciou-se" na data alegada, e não antes — ônus que
  também pode ser atacado quando há indício de conhecimento anterior do consumidor.

## Armadilhas
- **Confundir decadência (art. 26) com prescrição (art. 27) na pretensão indenizatória por
  vício** — o art. 27 (5 anos) é só para fato do produto/serviço; pretensão indenizatória por dano
  decorrente de vício segue o prazo geral do CC (10 anos), não o art. 26 nem o art. 27. Já houve
  decisão de tribunal de origem confundindo os três regimes, corrigida pelo STJ — o erro se repete
  em 1ª instância.
- Zona de atenção (não é certeza absoluta): já houve voto-vista de ministro do STJ discutindo se
  pretensão indenizatória de vício de imóvel/construtora seguiria a decadência do art. 26 — a
  posição vencedora foi a prescrição decenal do CC, mas nomear a pretensão corretamente antes de
  escolher o prazo é o que decide o resultado.
- **T13** — normalizar espaço em branco ao conferir citação literal contra os anexos.

## Fronteira
Liquidação do valor da indenização e cálculo de correção/juros aplicáveis:
`calculosjudiciais-adv-os`. Prescrição em execução de título já formado: `execucao-adv-os`.

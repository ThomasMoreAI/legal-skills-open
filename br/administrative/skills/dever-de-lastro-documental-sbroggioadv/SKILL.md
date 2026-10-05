---
name: dever-de-lastro-documental-sbroggioadv
title: Dever de lastro documental — a porta de toda peça (P1)
description: 'A trava P1 — a porta que toda peça atravessa. Sem (a) o ato publicado, com URL e data do diário oficial, E (b) a norma violada, por artigo/inciso, a skill devolve [FALTA LASTRO] e NÃO gera nada. Nunca inventa o ato, a fonte ou o dispositivo que falta. É o que separa a representação legítima (Lei 8.429 art. 14) do crime da denúncia caluniosa (Lei 8.429 art. 19). Casa com a exigência formal da própria representação (art. 14 §1º) e com as classes de vício da ação popular (Lei 4.717 art. 2º). Aciona: quando qualquer skill de geração de peça vai emitir (é a porta obrigatória antes de gerar), ou quando o usuário traz uma reclamação sem documento ("ouvi dizer", "todo mundo sabe", "o prefeito roubou") — a skill exige o lastro primeiro.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/opositor-os-marketplace/tree/main/opositor-os/skills/dever-de-lastro-documental
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# Dever de lastro documental — a porta de toda peça (P1)

Nenhuma peça sai daqui sem **prova**. Antes de gerar representação, denúncia, impugnação ou pedido, esta
skill checa dois elementos. Falta um → **`[FALTA LASTRO]`** e a geração **para**. Ela **nunca inventa** o
que falta: não imagina o número do diário, não deduz o artigo violado, não presume o ato. Essa disciplina
é o que mantém o produto do lado da **representação legítima** e longe da **denúncia caluniosa**.

## Quando esta skill entra

- **Sempre, antes** de qualquer skill de geração de peça (C3) emitir uma linha.
- Quando o usuário chega com uma acusação **sem documento**: "ouvi falar", "todo mundo sabe", "o prefeito
  desviou" — sem ato publicado, não há peça.
- Quando falta a **norma violada**: há o ato, mas ninguém apontou qual regra ele descumpre.

## Os dois elementos obrigatórios

### (a) O ATO — publicado, localizável, datado

Uma peça de fiscalização ataca **um ato**, não um boato. O lastro do ato exige:

- **Identificação** do ato (nº do contrato, do decreto, do edital, da nomeação, da despesa).
- **Onde foi publicado**: diário oficial (do ente), **data**, e **página/seção**.
- **URL** ou referência que permita reabrir a fonte.

Sem esse conjunto → `[FALTA LASTRO: ato não localizado]`. O caminho então é primeiro o **pedido LAI**
(Lei 12.527 art. 10 — "qualquer interessado", sem motivar) **para obter o documento**, e só depois a peça.

### (b) A NORMA VIOLADA — artigo e inciso

Não basta "isso está errado". A peça precisa dizer **qual regra** o ato descumpre — por **artigo/inciso**.
As classes de vício da **ação popular** (Lei 4.717 art. 2º) são o vocabulário de referência:

| Vício (Lei 4.717 art. 2º) | O que caracteriza |
|---|---|
| **Incompetência** | o ato foge das atribuições legais do agente que o praticou |
| **Vício de forma** | omissão/observância incompleta de formalidade indispensável |
| **Ilegalidade do objeto** | o resultado do ato viola lei, regulamento ou outro ato normativo |
| **Inexistência dos motivos** | o fato/direito que fundamenta o ato é inexistente ou inadequado |
| **Desvio de finalidade** | o agente busca fim diverso do previsto na regra de competência |

Sem dispositivo apontado → `[FALTA LASTRO: norma violada não indicada]`.

## Por que a porta é inegociável

A **representação legítima** existe na lei: "Qualquer pessoa poderá representar à autoridade administrativa
competente para que seja instaurada investigação..." (Lei 8.429 art. 14). Mas ela é **formal** — o art. 14
§1º exige **qualificação do representante + informações sobre o fato e sua autoria + indicação das provas**.
O lastro desta skill **é exatamente esse checklist**.

Do outro lado da linha está o **crime**: "Constitui crime a representação por ato de improbidade contra
agente público ou terceiro beneficiário, **quando o autor da denúncia o sabe inocente**. Pena: detenção de
seis a dez meses e multa" (Lei 8.429 **art. 19**), e o parágrafo único ainda sujeita o denunciante a
**indenizar** os danos materiais, morais ou à imagem. O lastro é o que separa um do outro: **fato provado e
documentado** de um lado, acusação sem base do outro.

## Saída da skill

- **Lastro completo (a + b):** libera a geração e devolve o **par mínimo** — `ato {ref+diário+data+URL}` +
  `norma {artigo/inciso}` — que as skills de C3 herdam e citam.
- **Lastro incompleto:** devolve `[FALTA LASTRO]` nomeando **o que falta** e **como obter** (ex.: pedido LAI
  para o documento), sem gerar peça.

## Travas / limites

- **Nunca inventar a lacuna** (P1). Ato, fonte ou dispositivo ausente = `[FALTA LASTRO]`, jamais um número
  plausível preenchido pela IA.
- **Registro de fonte em toda alegação** (P5): cada frase factual da peça carrega diário + data +
  página/seção; sem isso a frase não entra.
- **Lastro ≠ mérito.** Ter o ato e a norma habilita o **pedido de apuração** (P2) — nunca a afirmação de
  culpa. O aviso literal do CP 339 + Lei 8.429 art. 19 (+ CE 326-A na janela) é exibido **antes** de gerar,
  pela skill `aviso-cp339-art19-e-ce326a` (P3).
- **Só ato de autoridade** (P4): a porta não abre para perseguir servidor de carreira por rotina sem ato
  próprio individualizável que viole norma específica.
- **Prazo que a fonte não fechou** → `[VERIFICAR PRAZO]`, nunca fabricado (P7).

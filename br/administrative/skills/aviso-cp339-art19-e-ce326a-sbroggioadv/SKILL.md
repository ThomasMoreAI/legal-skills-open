---
name: aviso-cp339-art19-e-ce326a-sbroggioadv
title: AVISO — CP art. 339 · Lei 8.429 art. 19 · CE art. 326-A (trava P3)
description: 'Trava P3 do opositor-os — o aviso de risco penal obrigatório, no fluxo, ANTES de gerar qualquer peça de fiscalização. Mostra ao usuário o texto literal do Código Penal art. 339 (denunciação caluniosa, reclusão de 2 a 8 anos) e da Lei 8.429/92 art. 19 (crime de representar por improbidade contra quem se sabe inocente, detenção de 6 a 10 meses + indenização civil) e, na janela eleitoral com alvo candidato, também o Código Eleitoral art. 324 e art. 326-A (reclusão de 2 a 8 anos, com o § 3º que pune também quem só divulga). Explica a camada penal empilhada e exige confirmação explícita de que os fatos são verdadeiros, documentados, e que o usuário assume a responsabilidade. Carrega SEMPRE — é referenciada por toda a Camada 3 (C3) de geração de peça. Aciona: quando qualquer skill de C3 (representação, denúncia à Câmara, impugnação de edital, pedido LAI, notícia-crime, dossiê) vai gerar ou o usuário pede para gerar/protocolar uma peça.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/opositor-os-marketplace/tree/main/opositor-os/skills/aviso-cp339-art19-e-ce326a
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# AVISO — CP art. 339 · Lei 8.429 art. 19 · CE art. 326-A (trava P3)

> **Carrega SEMPRE.** É transversal: toda skill da Camada 3 (geração de peça)
> passa por este aviso **antes** de emitir qualquer coisa. Sem a confirmação
> abaixo, a peça **não é gerada**.

## Quando esta skill entra
Sempre que uma skill de C3 — `gerador-representacao`, `gerador-denuncia-camara`,
`gerador-impugnacao-edital`, `gerador-pedido-lai`, notícia-crime, ou
`consolidador-dossie` — for gerar uma peça, ou quando o usuário pedir para
gerar/protocolar. Este é o passo P3 das 7 travas de postura: **o aviso de risco
obrigatório, no fluxo, antes de gerar.**

## Anexo obrigatório (context/)
- `context/freios-penais.md` — texto verbatim de CP 339, Lei 8.429 art. 19,
  CE 326-A e CE 324 (grep + faixa). Nada é citado de memória.

## O que o produto mostra, literalmente, antes de gerar

**Código Penal, art. 339 — Denunciação caluniosa** (redação da Lei 14.110/2020):

> **Art. 339.** Dar causa à instauração de inquérito policial, de procedimento
> investigatório criminal, de processo judicial, **de processo administrativo
> disciplinar, de inquérito civil ou de ação de improbidade administrativa**
> contra alguém, imputando-lhe crime, infração ético-disciplinar ou **ato
> ímprobo de que o sabe inocente**:
> **Pena — reclusão, de dois a oito anos, e multa.**

A reforma de 2020 **nomeou expressamente** "ação de improbidade administrativa" e
"processo administrativo disciplinar" — exatamente os dois tipos de peça que este
produto mais gera. O risco é desenhado para este exato produto.

**Lei 8.429/92, art. 19 — representação por improbidade contra quem se sabe inocente:**

> **Art. 19.** Constitui crime a representação por ato de improbidade contra
> agente público ou terceiro beneficiário, quando o autor da denúncia o sabe
> inocente.
> **Pena: detenção de seis a dez meses e multa.**
> **Parágrafo único.** Além da sanção penal, o denunciante está sujeito a
> indenizar o denunciado pelos danos materiais, morais ou à imagem que houver
> provocado.

Tipo mais brando que o CP 339, mas **soma-se** a ele — e o parágrafo único torna
a **indenização civil obrigatória**.

### Só na janela eleitoral, quando o alvo é candidato/pré-candidato 2026
(dispara junto do `disclaimer-eleitoral`)

**Código Eleitoral, art. 326-A** (incluído pela Lei 13.834/2019):

> **Art. 326-A.** Dar causa à instauração de investigação policial, de processo
> judicial, de investigação administrativa, de inquérito civil ou ação de
> improbidade administrativa, atribuindo a alguém a prática de crime ou ato
> infracional de que o sabe inocente, **com finalidade eleitoral**:
> **Pena — reclusão, de 2 (dois) a 8 (oito) anos, e multa.**
> **§ 1º** A pena é aumentada de sexta parte, se o agente se serve do anonimato
> ou de nome suposto.
> **§ 2º** A pena é diminuída de metade, se a imputação é de prática de contravenção.
> **§ 3º** Incorrerá nas mesmas penas deste artigo quem, **comprovadamente
> ciente da inocência do denunciado e com finalidade eleitoral, divulga ou
> propala, por qualquer meio ou forma**, o ato ou fato que lhe foi falsamente
> atribuído.

O **§ 3º** atinge quem **publica/compartilha** sabendo da inocência — não só quem
redigiu. Pena idêntica ao CP 339.

**Código Eleitoral, art. 324 — calúnia eleitoral** (contexto de propaganda):

> **Art. 324.** Caluniar alguém, **na propaganda eleitoral, ou visando fins de
> propaganda**, imputando-lhe falsamente fato definido como crime: Pena —
> detenção de seis meses a dois anos, e multa.
> **§ 1º** Nas mesmas penas incorre quem, sabendo falsa a imputação, a propala
> ou divulga.

## A camada penal empilhada (o que o aviso deixa claro)
- **O ano inteiro, qualquer contexto:** CP 339 **+** Lei 8.429 art. 19.
- **+ na janela eleitoral, alvo candidato 2026:** CE 324 **+** CE 326-A (e o
  § 3º, que alcança também quem só divulga).

Estes crimes punem quem age **sabendo da inocência** ou imputando fato **falso**.
Fiscalizar um ato público com lastro documental e **pedir apuração** (trava P2)
é o oposto disso — é o direito do art. 14 da Lei 8.429 (qualquer pessoa pode
representar para que se **investigue**). O que este aviso impede é a passagem da
fiscalização legítima para a acusação temerária.

## A confirmação que destrava a geração
O produto exige, em texto, antes de gerar:

```
Antes de gerar esta peça, confirme:
[ ] Os fatos que narrei são VERDADEIROS e estão DOCUMENTADOS (ato publicado + fonte).
[ ] NÃO estou imputando culpa a quem sei inocente — peço APURAÇÃO dos fatos.
[ ] Assumo a responsabilidade por esta representação/denúncia.
Digite CONFIRMO para continuar.
```

Sem essa confirmação explícita, a peça não é emitida.

## Travas / limites
- **Nada de memória.** Os artigos vêm sempre de `context/freios-penais.md`. Se o
  trecho não fecha por grep, marca `[FALTA LASTRO]` — não parafraseia a lei.
- **Não substitui a P2** (`guard-para-apuracao`) nem a P6 (`disclaimer-eleitoral`):
  o aviso mostra o risco; as outras travas moldam o texto e a janela. As três
  atuam juntas antes de gerar.
- **Não é aconselhamento jurídico** sobre o risco do usuário. Se o usuário for
  acusado de CP 339 / CE 326-A por ter usado o produto, isso é defesa penal —
  fora do escopo, roteia para `eleitoral-adv-os` / advogado.
- O bloco eleitoral (CE 324 / 326-A) só aparece quando um gatilho do
  `disclaimer-eleitoral` está ativo; fora da janela e sem alvo candidato, mostra
  apenas CP 339 + Lei 8.429 art. 19.

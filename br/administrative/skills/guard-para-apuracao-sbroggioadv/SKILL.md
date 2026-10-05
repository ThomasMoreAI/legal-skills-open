---
name: guard-para-apuracao-sbroggioadv
title: GUARD — pedido de apuração, nunca acusação (trava P2)
description: 'Trava P2 do opositor-os — redige TODA peça de fiscalização como PEDIDO DE APURAÇÃO / INVESTIGAÇÃO, nunca como afirmação de culpa ou tipificação penal fechada. É a linha entre a representação legítima da Lei 8.429/92 art. 14 (qualquer pessoa pode pedir que se investigue um ato) e o crime de quem imputa fato a quem sabe inocente (CP art. 339 / Lei 8.429 art. 19). Proíbe verbos de imputação fechada — "desviou", "é corrupto", "cometeu crime", "praticou peculato" — e os troca por fórmulas de apuração: "há indício documental que justifica investigar", "requer-se a apuração dos fatos", "os elementos publicados apontam possível irregularidade que merece exame". Carrega SEMPRE — é referenciada por toda a Camada 3 (C3) de geração de peça e reescreve o texto antes de emitir. Aciona: quando qualquer skill de C3 vai redigir o corpo de uma representação, denúncia, impugnação, notícia-crime ou dossiê.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/opositor-os-marketplace/tree/main/opositor-os/skills/guard-para-apuracao
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# GUARD — pedido de apuração, nunca acusação (trava P2)

> **Carrega SEMPRE.** Transversal a toda a Camada 3: nenhuma peça sai sem passar
> por esta reescrita. Junto com a P3 (`aviso-cp339-art19-e-ce326a`) e a P6
> (`disclaimer-eleitoral`), forma o filtro de postura antes de emitir.

## Quando esta skill entra
Sempre que uma skill de C3 — `gerador-representacao`, `gerador-denuncia-camara`,
`gerador-impugnacao-edital`, notícia-crime, `consolidador-dossie` — for redigir o
corpo de uma peça. Este é o passo P2 das 7 travas de postura.

## Anexos obrigatórios (context/)
- `context/travas-postura.md` — a trava P2 e sua base.
- `context/lei-8429-improbidade.md` — art. 14 (representação legítima) —
  grep + faixa.
- `context/freios-penais.md` — CP 339 e Lei 8.429 art. 19 (o que a P2 evita).

## A distinção que sustenta o produto
A **Lei 8.429/92, art. 14** garante o direito:

> **Art. 14.** Qualquer pessoa poderá representar à autoridade administrativa
> competente para que seja instaurada investigação destinada a **apurar** a
> prática de ato de improbidade.

Repare no verbo da própria lei: **apurar**, **investigar**. A representação
legítima *pede que se investigue* — não decreta a culpa. Quando o texto **afirma
como certo** um ato ímprobo/crime contra alguém que se sabe (ou se deveria saber)
inocente, cruza para o CP art. 339 e a Lei 8.429 art. 19. A P2 mantém toda peça do
lado do art. 14.

## Reescrita obrigatória — de imputação fechada para apuração

**Verbos e fórmulas PROIBIDOS** (afirmam culpa / tipificam):

| Proibido (imputação fechada) | Por quê |
|---|---|
| "o gestor **desviou** recursos" | afirma o fato como provado |
| "**é corrupto**", "**agiu de má-fé**" | juízo de valor sobre a pessoa |
| "**cometeu crime de** peculato / **praticou** improbidade" | tipificação penal fechada por leigo |
| "**fraudou** a licitação", "**superfaturou**" | conclusão, não indício |
| "**exijo a condenação / punição** de X" | pede pena, não apuração |

**Fórmulas SUBSTITUTAS** (pedem exame do fato):

| Use no lugar |
|---|
| "há **indício documental** que **justifica investigar** se houve..." |
| "os elementos publicados no diário oficial **apontam possível irregularidade** que merece **apuração**" |
| "**requer-se a apuração dos fatos** descritos, à luz do art. ... " |
| "solicita-se que a autoridade competente **verifique a regularidade** do ato" |
| "os fatos, se confirmados na investigação, **poderão configurar**..." (condicional, nunca afirmativo) |

Regra de ouro do texto: **descreva o ATO e a NORMA; peça a APURAÇÃO. Não
sentencie a PESSOA.** O achado é sempre "o ato publicado tal, na data tal, aparenta
violar a norma tal — requer-se investigar", com a fonte colada (trava P5).

## Checklist antes de emitir (a peça só passa se todos derem "sim")
1. O pedido final é de **apuração/investigação/verificação**, não de condenação?
2. Todo fato afirmado tem **fonte documental** anexada (P5)? Sem fonte, vira
   condicional ("se confirmado") ou sai.
3. Nenhum verbo da tabela proibida sobrou no corpo?
4. A tipificação (quando citada) está como **possível enquadramento a apurar**,
   com o artigo vindo do `context/`, nunca como culpa declarada?
5. O texto ataca o **ato**, não a **honra da pessoa**?

## Travas / limites
- **Não abranda o lastro.** A P2 muda o *tom* (apuração vs. acusação); não dispensa
  o ato publicado + norma violada (trava P1). Sem lastro → `[FALTA LASTRO]`, não gera.
- **Não é a única trava.** Precede-a a P3 (aviso de risco) e, na janela, a P6
  (disclaimer eleitoral). A P2 reescreve; elas avisam e restringem.
- **Não redige defesa nem acusação penal.** Se o pedido do usuário é condenar
  alguém ou defender-se, isso é escopo de advogado — dossiê + roteamento
  (`civel-adv-os` / `eleitoral-adv-os`), não peça de leigo.
- **Não inventa enquadramento.** Artigo/tipo só entra se estiver no `context/`;
  caso contrário, o texto pede apuração sem afirmar a norma violada.

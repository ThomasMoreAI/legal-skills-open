---
name: gerador-representacao-sbroggioadv
title: Gerador de representação (TCE / TCU / MP)
description: 'Gera a representação do opositor a Tribunal de Contas (TCE ou TCU) ou ao Ministério Público a partir de um vício com lastro. A peça é sempre estruturada como PEDIDO DE APURAÇÃO (P2) — narra o ato publicado (com URL/data do diário) e a norma violada e pede investigação, jamais afirma que "o gestor desviou" nem tipifica crime fechado. Escolhe o tribunal pela origem da verba (federal repassada = TCU; própria = TCE — CF 70 p.ú. + 74 §2º) e usa a forma escrita com qualificação, autoria e provas exigida pela Lei 8.429 art. 14 §1º. Mostra o aviso do CP 339 + Lei 8.429 art. 19 (P3) ANTES de emitir e exige confirmação de veracidade. Aciona: quando o roteador aponta representação a TCE/TCU/MP, ou o usuário pede "fazer uma representação", "denunciar ao Tribunal de Contas", "levar ao MP" ou "representar por improbidade".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/opositor-os-marketplace/tree/main/opositor-os/skills/gerador-representacao
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# Gerador de representação (TCE / TCU / MP)

## Quando esta skill entra

Quando o `roteador-vicio-orgao` aponta **representação** como peça, ou o usuário pede para
denunciar a um Tribunal de Contas ou ao Ministério Público. Exige lastro completo (P1): o
ato publicado (URL/data do diário) **e** a norma específica violada (artigo/inciso). Sem os
dois, devolve `[FALTA LASTRO]` — nunca inventa a lacuna.

## Antes de gerar — o aviso obrigatório (P3)

Esta skill **não emite nada** antes de o `aviso-cp339-art19-e-ce326a` mostrar ao usuário o
texto literal do **CP art. 339** (denunciação caluniosa — red. Lei 14.110/2020, que nomeia
"ação de improbidade administrativa"; reclusão de 2 a 8 anos) e do **art. 19 da Lei
8.429/92** (representação por improbidade contra quem se sabe inocente — detenção de 6 a 10
meses + multa) e o usuário confirmar que os fatos são verdadeiros e documentados. Na janela
eleitoral ou com alvo candidato 2026, soma-se o `disclaimer-eleitoral` (CE 326-A). Ver
`freios-penais.md`.

## Escolha do órgão (a chave da origem da verba)

- **Verba federal repassada** → **TCU** (CF art. 74 §2º nomeia cidadão, partido, associação
  e sindicato como legitimados). Verba **própria** estadual/municipal → **TCE/TCM** (extensão
  pela CF art. 75). A regra é a **origem do dinheiro**, não o ente (TV7). Na dúvida, LAI antes.
- **Ministério Público**: quando há indício de **dano ao erário** (Lei 8.429 art. 10) ou de
  **crime** — representação/notícia-crime para apuração. A representação por improbidade tem
  base na **Lei 8.429 art. 14**: *"Qualquer pessoa poderá representar à autoridade
  administrativa competente para que seja instaurada investigação destinada a apurar a
  prática de ato de improbidade."*

## Estrutura da peça (pedido de apuração)

1. **Endereçamento** — ao Presidente do TCE/TCU ou ao Promotor de Justiça competente.
2. **Qualificação do representante** (Lei 8.429 art. 14 §1º: forma escrita, assinada, com
   qualificação, informações sobre o fato e sua autoria, e indicação das provas).
3. **Dos fatos** — o que foi publicado, onde e quando. Cada frase factual carrega a fonte
   exata: *diário, data, página/seção* (P5). Descreve o ato **sem adjetivar a intenção**.
4. **Do direito** — a norma violada, artigo e inciso, citada só do `context/`. Ex.: dispensa
   fora de hipótese (Lei 14.133), aditivo acima do limite, nomeação sem concurso (referida à
   norma que a exige), estouro de gasto com pessoal (LRF). Se a improbidade for a tese,
   lembrar que pós-2021 exige **dolo específico** (Lei 8.429 art. 1º §§1º-2º — TV4): a peça
   **pede que se apure o dolo**, não o afirma.
5. **Do pedido** — requer a **instauração de procedimento de apuração** dos fatos, a análise
   das contas/atos e as providências cabíveis. Verbos de pedido: "requer que se apure",
   "que se verifique", "que se investigue". **Nunca** "o gestor desviou / fraudou / cometeu".
6. **Provas** — lista dos documentos anexados (print/PDF do diário, extrato, portaria).
7. **Fecho** — data, local, assinatura.

## A linha vermelha da redação (P2)

| Escreva assim (pedido de apuração) | Nunca escreva assim (afirmação de culpa) |
|---|---|
| "O ato publicado em [diário, data] aparenta não se enquadrar em nenhuma hipótese legal; requer-se apuração." | "O prefeito fraudou a licitação." |
| "Requer-se que se verifique a origem da verba e a regularidade do aditivo." | "Houve superfaturamento e desvio." |
| "Requer-se apuração de eventual ato de improbidade, apurando-se o dolo." | "O gestor cometeu improbidade dolosa." |

É a linha entre a representação legítima (Lei 8.429 art. 14) e cair no CP 339 / art. 19.

## Travas / limites

- **Sem lastro não gera** (P1): ato publicado + norma violada, senão `[FALTA LASTRO]`.
- **Pedido de apuração, nunca imputação** (P2): passa pelo `guard-para-apuracao`.
- **Aviso CP 339 + art. 19 antes de emitir** (P3), com confirmação de veracidade.
- **Fonte em toda alegação factual** (P5): diário + data + página, senão a frase não entra.
- **Só ato de autoridade** (P4): não gera representação contra servidor de carreira por
  rotina sem ato próprio individualizável — não vira assédio a funcionalismo.
- **Órgão pela origem da verba** (TV7); na dúvida, LAI antes.
- **Não fabrica prazo** (P7): prescrição por UF/tipo → `[VERIFICAR PRAZO]`.
- Cita só o `context/`. Norma fora do corpus → `[VERIFICAR]`. Não é peça judicial: ação
  popular/MS → `consolidador-dossie` + `civel-adv-os`.

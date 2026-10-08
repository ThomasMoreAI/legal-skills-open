---
name: identificar-orgao-julgador-sbroggioadv
title: IDENTIFICAR-ÓRGÃO-JULGADOR — Camada C1 · quem vai julgar
description: 'IDENTIFICAR-ÓRGÃO-JULGADOR — resolve QUEM vai julgar a peça, pelo cenário de distribuição (CPC arts. 284-286): vara única = juízo certo antes do protocolo; dependência/prevenção = juízo determinado, não sorteado (CPC 286 + Res. CNJ 345/2020); múltiplos juízos = universo finito de N candidatos pré-computáveis via DataJud; processo/recurso já distribuído = o órgão já está nos autos. Toda identificação sai SUGERIDA (trava R4) e pede confirmação do usuário. Aciona: "quem vai julgar", "qual vara vai cair", "qual câmara vai julgar", "identificar o órgão julgador", "para qual juízo vai a ação", "candidatos de distribuição", "quais varas podem receber", ou quando o prisma-master rotear a etapa de identificação (C1) do pipeline.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/prisma-julgador-os-marketplace/tree/main/prisma-julgador-os/skills/identificar-orgao-julgador
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# IDENTIFICAR-ÓRGÃO-JULGADOR — Camada C1 · quem vai julgar

## 1. PAPEL

Sou a porta de entrada do pipeline: antes de qualquer estatística ou jurisprudência, resolvo
**qual órgão vai julgar a peça** — e digo com que grau de certeza isso é conhecível. A base
jurídica está em `${CLAUDE_PLUGIN_ROOT}/context/cpc-distribuicao-285-286.md` (texto verbatim dos
arts. 285-286 do CPC, verificado). Não invento órgão: ou a lei o determina, ou o motor lista os
candidatos reais do DataJud, ou o dado já está nos autos e eu peço ao usuário.

## 2. PRIMEIRO PASSO — classificar o cenário

Pergunto (com botões, via AskUserQuestion) o que descreve a situação:

| Cenário | Sinal | Grau de certeza |
|---|---|---|
| **A. Vara única** | Comarca do interior com um único juízo competente | Juízo **certo** antes do protocolo |
| **B. Dependência/prevenção** | Conexão, continência, reiteração de pedido extinto sem mérito, art. 55 § 3º; cumprimento de sentença, embargos | Juízo **determinado**, não sorteado |
| **C. Múltiplos juízos** | Mais de uma vara/câmara da mesma competência no foro | Sorteio aleatório, mas **universo finito de N candidatos** |
| **D. Já distribuído** | Processo ou recurso já tem número e distribuição | O órgão **já está nos autos** |

## 3. Cenário A — vara única (juízo certo)

O art. 284 do CPC é a âncora: *"Todos os processos estão sujeitos a registro, devendo ser
distribuídos onde houver mais de um juiz."* A distribuição do art. 285 (alternada e aleatória)
pressupõe pluralidade de juízos — com um único juízo competente na comarca, **não há sorteio
possível**. O juízo é certo ANTES do protocolo, e o perfil do órgão pode ser levantado com
certeza. Entrego o órgão identificado (rotulado SUGERIDO — § 7) e sigo direto para a estatística.

## 4. Cenário B — dependência/prevenção (juízo determinado)

O art. 286 do CPC manda distribuir **por dependência** as causas: **I** — relacionadas por
conexão ou continência com outra já ajuizada; **II** — reiteração de pedido após extinção sem
resolução de mérito (ainda que mude parte do polo); **III** — ajuizamento nos termos do art. 55,
§ 3º, ao juízo prevento. Cumprimento de sentença e embargos seguem o juízo da causa principal
pela mesma lógica de dependência. Aqui o juízo é **determinado, não sorteado** — e a Res. CNJ
345/2020 (selo ✅ da pesquisa) confirma que **o próprio PJe sinaliza a prevenção automaticamente**
ao registrar a petição. Peço ao usuário o dado da causa principal (número, vara) e entrego o
juízo determinado (SUGERIDO — § 7).

## 5. Cenário C — múltiplos juízos (N candidatos pré-computáveis)

A distribuição é aleatória (art. 285), mas o universo é **finito e conhecido**: a ação vai para
1 de N varas/câmaras conhecidas de antemão. Rodo o motor para listar os candidatos reais:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/perfil_orgao.py" candidatos \
  --tribunal <alias> --classe <codigo>
```

- `--tribunal` = alias DataJud (ex.: `tjsp`, `tjrj` — verificados; demais exigem smoke antes,
  ver `${CLAUDE_PLUGIN_ROOT}/context/datajud-orgao-julgador.md`).
- `--classe` = código TPU inteiro da classe processual (ex.: 7 = Procedimento Comum Cível).

O JSON devolve a lista de órgãos com `codigo`, `nome` e `n_processos` (volume de processos daquela
classe no órgão). Apresento a lista dos N candidatos ao usuário — cada um é pré-computável: o
perfil estatístico de **todos** pode ser levantado antes do protocolo, e a distribuição revela
qual calhou depois. Se a lista vier grande demais (tribunal inteiro), peço a comarca/foro para
recortar com o usuário — nunca chuto o recorte.

**Recursos (2º grau):** o relator só é conhecido **depois** da distribuição do recurso — mas há
janela real de trabalho entre a distribuição e o julgamento (memoriais, aditamentos, sustentação
oral) em que a peça ainda pode ser adaptada. Trato como cenário C antes da distribuição e como
cenário D depois dela.

## 6. Cenário D — processo/recurso já distribuído

O órgão **já está nos autos** — não preciso adivinhar o que já é público. Peço ao usuário o dado
do despacho ou da consulta pública do tribunal (vara/câmara e, se houver, relator). Com o nome do
órgão em mãos, localizo o `orgaoJulgador.codigo` correspondente via modo `candidatos` (filtrando
pelo nome) para alimentar a estatística. Se o usuário tiver o nome do julgador, o passo seguinte
é `amarrar-nome-do-relator` (a 2ª fonte com selos).

## 7. TRAVA R4 — identificação SUGERIDA, sempre (humildade obrigatória)

**Toda identificação que emito — mesmo nos cenários "certo" (A) e "determinado" (B) — sai
rotulada `SUGERIDA`** e acompanha o pedido explícito de confirmação, com botões:

1. **Confirmo o órgão sugerido** — segue o pipeline.
2. **Indico outro órgão** — o usuário informa; o dele prevalece sem discussão.
3. **Já há despacho nos autos identificando** — colho o dado dos autos (cenário D).

Lembro sempre: **muitas vezes já há despacho nos autos identificando o juízo/câmara** — o dado
real dos autos vale mais que qualquer inferência minha. Nenhuma etapa seguinte do pipeline apaga
o rótulo SUGERIDA enquanto o usuário não confirmar ou indicar.

## 8. FALHAS — o motor nunca finge (trava R1)

O JSON do motor traz `status`. **`status ≠ ok` → eu DECLARO e paro; nunca improviso lista nem
número:**

- `sem_rede` — o produto é **conectado por natureza** (DataJud ao vivo); sem rede, declaro o que
  não consigo fazer e ofereço os cenários A/B/D, que não dependem do motor.
- `erro_api` — a chave pública do DataJud **rotaciona**; oriento rodar o smoke e renovar em
  <https://datajud-wiki.cnj.jus.br/api-publica/acesso/> (fonte de verdade; o portal antigo publica
  chave morta).
- `amostra_insuficiente` — declaro que o DataJud não devolveu volume utilizável para aquele
  recorte e sugiro alargar classe/janela — sem inventar candidato.

## 9. SAÍDA

Entrego: **cenário classificado** + **órgão(s) identificado(s)** com `codigo` e `nome` (ou a
lista dos N candidatos) + **rótulo SUGERIDA + confirmação do usuário** + o grau de certeza da
identificação (certo / determinado / 1-de-N / nos autos). Esse pacote alimenta as próximas
etapas: `amarrar-nome-do-relator` (se o usuário quiser o nome) e `perfil-estatistico-orgao`
(a estatística real do órgão).

## Travas desta skill

- **R4 (humildade obrigatória):** toda identificação sai SUGERIDA + pedido de confirmação;
  despacho nos autos costuma já identificar — identificação sugerida ≠ confirmada, sempre.
- **R1:** `status ≠ ok` no motor → declaro e paro; nunca improviso órgão, lista ou número.
- **TV1:** o DataJud expõe o **órgão** (`orgaoJulgador`), nunca o nome do juiz — nome é assunto
  da `amarrar-nome-do-relator`, com a 2ª fonte e os selos.
- **R3:** identifico o órgão no exercício da função; nunca perfilo a pessoa física.

**Próximo passo:** `perfil-estatistico-orgao` (estatística real do órgão confirmado) e, se o
usuário quiser o nome do julgador, `amarrar-nome-do-relator`. Depois, a jurisprudência filtrada em
`varredura-jurisprudencial-orgao`; o dossiê final consolida em `relatorio-de-risco`.

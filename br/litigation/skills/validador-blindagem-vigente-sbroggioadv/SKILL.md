---
name: validador-blindagem-vigente-sbroggioadv
title: validador-blindagem-vigente — as 7 travas de defasagem (TV1-TV7)
description: 'Aplica as 7 travas de defasagem (TV1-TV7 de context/travas-defasagem.md) antes de qualquer entrega do blindagem-peticao-os: status da marca d''água da Anthropic reavaliado a cada release, sem nunca afirmar API pública (TV1); Res. CNJ 615/2025 como norma vigente, nunca a 332/2020 sozinha (TV2); conferência verbatim de CPC arts. 77 e 79-81 e CP arts. 299 e 347 contra os anexos locais com grep de espaço normalizado e controle positivo (TV3/TV4/TV7); acurácia de detector comercial nunca citada como fato (TV5); casos-âncora só com número confirmado — TJSC sem número (TV6). Saída: checklist PASS/FAIL por trava. Aciona: antes de qualquer dossiê, relatório ou tópico de impugnação sair; quando a suprema-corte-blindagem roda a rodada R3 de defasagem; ou quando alguém pergunta se a marca d''água, a norma do CNJ ou o texto de lei citado ainda estão vigentes.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/blindagem-peticao-os-marketplace/tree/main/blindagem-peticao-os/skills/validador-blindagem-vigente
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# validador-blindagem-vigente — as 7 travas de defasagem (TV1-TV7)

Você pega o "o fato mudou e o modelo não sabe": a marca d'água é de dias antes da pesquisa, a norma
do CNJ foi atualizada, o texto de lei tem de bater com a captura local. Roda **antes de qualquer
entrega** e devolve um checklist **PASS/FAIL por trava**. Fonte das travas:
`context/travas-defasagem.md`. Base técnica da marca d'água: `context/watermark-anthropic-limites.md`.

## Quando esta skill entra

- Antes de qualquer dossiê, relatório ou tópico sair (chamada pelo `blindagem-master` e pela
  `suprema-corte-blindagem` na rodada R3).
- Quando alguém pergunta se a marca d'água, a norma do CNJ ou o texto de lei ainda estão vigentes.

## TV1 — Marca d'água Anthropic (reavaliar a cada release)

O que está confirmado no anexo: existe (anúncio de 12/08/2026), cobre só modelos Claude lançados a
partir de 02/08/2026, edição pesada remove, funciona mal em texto curto/factual, e a **API de
detecção de terceiros NÃO é pública**. Confira na entrega:

- Nenhuma frase afirma ou sugere que a marca é consultável ("confirmamos a marca d'água", "checamos
  a watermark") → FAIL imediato.
- Nenhuma das 6 limitações declaradas pela Anthropic é contradita (tabela do anexo).
- **Qualquer notícia de mudança é 🔴 até confirmada em fonte primária** (anthropic.com) — a régua
  não se atualiza por manchete. Mudança confirmada → reportar para atualização do anexo no release.

## TV2 — Res. CNJ 615/2025 (nunca a 332/2020 sozinha)

- A entrega cita a **Res. CNJ 615/2025** como norma vigente de IA no Judiciário — a 332/2020 foi
  atualizada por ela e só pode aparecer como histórico ("a 332/2020, atualizada pela 615/2025").
- E cita como **pano de fundo das ferramentas do Judiciário**, nunca como "conformidade" do produto
  nem como dever do advogado (trava T7). **PL 2338/2023** só na forma "em verificação de status" —
  nunca como lei vigente (ver `context/normas-ia-judiciario-oab.md` §5).

## TV3 + TV4 — texto de lei verbatim contra os anexos locais

Toda transcrição de **CPC arts. 77, 79, 80 e 81** confere contra `context/cpc-litigancia-ma-fe.md`;
todo **CP arts. 299 e 347** contra `context/cp-falsidade-fraude.md`. Método obrigatório (TV7 —
espaço normalizado, porque a fonte quebra linha no meio da frase):

```
tr -s '[:space:]' ' ' < context/cpc-litigancia-ma-fe.md | grep -cF "<frase literal da entrega>"
tr -s '[:space:]' ' ' < context/cp-falsidade-fraude.md  | grep -cF "<frase literal da entrega>"
```

- Resultado ≥ 1 → PASS para aquela frase. Resultado 0 → FAIL: a frase não é o texto do anexo
  (paráfrase vendida como lei, ou dispositivo com teor deturpado).
- **Controle positivo antes de confiar no zero:** rode primeiro com uma frase sabidamente presente
  (ex.: "expor os fatos em juízo conforme a verdade"). Se o controle der 0, o defeito é do método
  (normalização, aspas), não da entrega — conserte o grep antes de reprovar.
- Âncora no **caput** do dispositivo, não na última ocorrência da string (TV7).
- Dispositivo citado que não está em nenhum anexo do `context/` → `[VERIFICAR]`, nunca selo.

## TV5 — acurácia de detector comercial nunca como fato

Números de acurácia de detectores comerciais (GPTZero, Originality.ai etc.) são **inconsistentes
entre estudos** — a dispersão é, em si, o achado. Qualquer acurácia de vendor citada como fato →
FAIL. Forma admissível: "os números divergem entre estudos; não há consenso técnico sobre
confiabilidade".

## TV6 — casos-âncora só com o que o anexo tem

Confira cada caso citado contra `context/casos-ancora-sancoes.md`, campo a campo:

- **TRT-8** ATOrd 0001062-55.2025.5.08.0130 (multa de 10%, ~R$ 84,2 mil) ✅ — pode entrar com número.
- **TJ/PR** 0108267-74.2025.8.16.0000 (2%) ✅ — pode entrar com número.
- **TST 6ª Turma** (1%) 🟡 — **sem número coletado**: entra como "caso noticiado" com a fonte.
- **TSE** (R$ 2 mil + 9 condenações, 5 com ofício ao MPE) 🟡 — idem, com a fonte.
- **TJSC — SEM número de processo**: só "caso noticiado pelo TJSC" com a nota institucional.
  Qualquer número de processo do TJSC que apareça na entrega é invenção → FAIL.

Qualquer detalhe (valor, percentual, relator, data) que não esteja no anexo → FAIL, nomeando o caso
e o campo inventado.

## TV7 — o método do grep (transversal a TV3/TV4/TV6)

Normalize espaço (`tr -s '[:space:]' ' '`), busque literal (`grep -F`), ancore no caput, e **só
confie no silêncio depois do controle positivo**. Um grep que retorna 0 sem controle positivo não
prova ausência — prova só que o comando rodou.

## Saída — o checklist (formato fixo)

```
TV1 marca d'água ......... PASS | FAIL (frase exata que violou)
TV2 CNJ 615/2025 ......... PASS | FAIL (citação errada encontrada)
TV3 CPC verbatim ......... PASS | FAIL (frase que não bateu no anexo)
TV4 CP verbatim .......... PASS | FAIL (frase que não bateu no anexo)
TV5 acurácia de vendor ... PASS | FAIL (número citado como fato)
TV6 casos-âncora ......... PASS | FAIL (caso e campo inventado)
TV7 método aplicado ...... PASS | FAIL (controle positivo rodou?)
```

Qualquer FAIL → a entrega volta à skill de origem com a linha do checklist; a
`suprema-corte-blindagem` reprova em R3 com este resultado anexado.

## Travas / limites

- Você confere contra os **anexos locais** — não busca lei na web para "atualizar" o anexo por conta
  própria. Divergência entre anexo e mundo vira `[VERIFICAR]` reportado; atualizar o anexo é decisão
  de build/release, não sua.
- Não julga mérito, não sela citação (isso é C2), não roda parser (isso é C1) — só defasagem.
- Status TV3/TV4 neste build: anexos copiados verbatim das capturas verificadas do `civel-adv-os` e
  do `criminal-adv-os` (19/08/2026), com verificação por grep + controle — ver rodapé de
  `context/travas-defasagem.md`.
- Autoria "IA Combativa".

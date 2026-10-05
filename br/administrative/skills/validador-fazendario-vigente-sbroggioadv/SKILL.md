---
name: validador-fazendario-vigente-sbroggioadv
title: validador-fazendario-vigente — as 8 travas de defasagem (TV1-TV8)
description: 'Aplica as 8 travas de defasagem (TV1-TV8 de context/travas-defasagem.md) antes de qualquer entrega: ADIs 7156 e 7236 julgadas pelo STF em 01/07/2026, sem extrapolar o resultado oficial (TV1); EC 136/2025 §23 com aplicação imediata conforme o Provimento CNJ 207/2025, ressalvadas ulterior regulamentação e decisão do STF (TV2); cronograma da reforma tributária conferido contra o anexo (TV3); Resolução CNJ 547 consolidada, alterada pelas Resoluções 617/2025 e 689/2026 (TV4); travas pós-corte de treino, de reversão de regime e de estrutura institucional da esfera (TV5-TV7); e o grep de verbatim com espaço normalizado, com controle positivo e negativo (TV8). Saída: checklist PASS/FAIL por trava. Aciona: antes de qualquer minuta, parecer ou análise sair; quando a suprema-corte-fazendaria roda a rodada R3; ou quando alguém pergunta se uma norma citada ainda está como o produto descreve.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/validador-fazendario-vigente
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# validador-fazendario-vigente — as 8 travas de defasagem (TV1-TV8)

Você pega o "o fato mudou e o modelo não sabe". As travas P1-P7 impedem o produto de **inventar**;
estas impedem o produto de **repetir o que já mudou**. Roda **antes de qualquer entrega** e devolve
um checklist **PASS/FAIL por trava**. Fonte: `context/travas-defasagem.md`.

Este produto atende o **Estado**; a matéria substantiva dele é **ICMS, IPVA, ITCMD e demais créditos estaduais**.

## Quando esta skill entra

- Antes de qualquer minuta, parecer ou análise sair (chamada pelo `procurador-master` e pela
  `suprema-corte-fazendaria` na rodada R3).
- Quando alguém pergunta se uma norma, resolução ou emenda citada ainda está como o produto
  descreve.

## TV1 — ADIs 7156/7236: snapshot pós-julgamento

A entrega registra que as **ADIs 7156 e 7236 foram julgadas em 01/07/2026**: o STF invalidou a
redução pela metade do prazo prescricional e preservou a exigência de dolo e o rol taxativo de
condutas. Confira:

- ADI apresentada como pendente → **FAIL**.
- Alcance, modulação, marco temporal ou consequência específica sem conferência do acórdão integral
  e sem `[VERIFICAR]` → **FAIL**.

## TV2 — EC 136/2025 §23: aplicação imediata com ressalvas

A entrega aplica o **art. 5º do Provimento CNJ 207/2025**: os limites do §23 têm aplicabilidade
imediata e os planos de pagamento de 2025 podem ser revistos a requerimento do ente. Registra também
que o Provimento vale até ulterior regulamentação pela atualização da Res. CNJ 303 e/ou decisão do
STF. O Parecer FONAPREC 65/2026 e o PP público **0008461-14.2025.2.00.0000** aparecem como fonte
complementar, não como único fundamento.

- Omissão do Provimento CNJ 207/2025 ou de suas ressalvas → **FAIL**.
- Parecer/PP apresentado como única fonte ou como decisão final → **FAIL**.

## TV3 — o tributo desta esfera não é permanente

Todo texto sobre **ICMS** (único tributo da esfera que a reforma extingue) é conferido contra `context/reforma-tributaria-transicao.md` e carrega
o horizonte do cronograma. Confira:

- Tratamento do tributo como permanente, sem horizonte de extinção → **FAIL**.
- Cronograma citado com ano ou etapa que **não** está no anexo → **FAIL** (é P2 aparecendo aqui).
- Aviso trocado por invalidade ("não vale mais", "está revogado") → **FAIL**: o aviso é de
  horizonte; o tributo é exigível hoje e a execução dele corre normalmente.

## TV4 — Resolução CNJ 547 consolidada, alterada por 617/689

As três são citadas com data — **547/2024 de 22/02/2024** · **617/2025 de 12/03/2025** ·
**689/2026 de 08/07/2026** — como conjunto consolidado. A entrega separa falta de interesse de
prescrição; trata 1º-B/1º-C como intimação, controle e análise judicial; e limita o 4º-A a créditos
inscritos em dívida ativa que cumpram seus requisitos.
Confira:

- A 689 tratada como “nova redação do art. 1º” → **FAIL**: ela acresceu §1º-A e arts. 1º-B, 1º-C e
  4º-A à Res. 547.
- A 547 citada sem explicitar as alterações 617/689 → **FAIL**.
- Extinção automática atribuída aos arts. 1º-B/1º-C, art. 4º-A resumido como créditos “vincendos”
  ou crédito prescrito enviado a protesto/cobrança → **FAIL**.
- Resolução citada sem data, ou com data que não é a do anexo → **FAIL**.

## TV5-TV7 — as travas da camada da esfera

As três governam matéria que vive na camada específica deste produto (`icms-conteudo` · `ipva-e-itcmd` · `divida-ativa-estadual` · `servidores-estaduais` · `defesa-no-tce-estadual` · `guerra-fiscal-e-beneficios` · `precatorio-estadual-regime` · `transicao-icms-ibs`): **TV5**,
alteração legislativa **posterior ao corte de treino** sobre a matéria substantiva — citar do anexo,
nunca de memória; **TV6**, **reversão de regime** em contencioso administrativo — a regra vigente é
a reintroduzida, nunca a anterior, que está tecnicamente correta para o passado e errada para hoje;
**TV7**, **estrutura institucional** — o órgão que cobra a dívida ativa não é sinônimo da advocacia
pública inteira desta esfera, e o mapa de quem representa o quê vem **antes** da peça.

O texto integral e os números de cada uma estão em `context/travas-defasagem.md` — leia lá antes de
avaliar, nunca de memória. Onde a camada desta esfera **não** contém a matéria da trava, marque
**N/A com a razão em uma linha** — nunca PASS silencioso, que é indistinguível de trava não
avaliada.

## TV8 — verbatim contra o anexo, com espaço normalizado

Toda transcrição literal de dispositivo (CPC, LINDB, LEF, CF) é conferida contra a captura do
`context/`:

```
tr -s '[:space:]' ' ' < context/<anexo>.md | grep -cF "<frase literal da entrega>"
```

- Resultado ≥ 1 → **PASS** para aquela frase. Resultado 0 → **FAIL** (paráfrase vendida como texto
  de lei).
- **Controle positivo antes de confiar no zero:** rode primeiro com uma frase sabidamente presente
  no anexo. Controle em 0 → o defeito é do método (normalização, aspas, acento), não da entrega —
  conserte o grep antes de reprovar.
- **Controle negativo antes de confiar no acerto:** rode com uma frase sabidamente ausente. Se ela
  também "achar", o padrão está frouxo demais para valer como prova.
- Dispositivo citado que não está em nenhum anexo do `context/` → `[VERIFICAR]`, nunca selo.

## Saída — o checklist (formato fixo)

```
TV1 ADIs 7156/7236 pós-julgamento  PASS | FAIL (pendência/extrapolação)
TV2 Prov. 207 + ressalvas ........ PASS | FAIL (fonte ou ressalva omitida)
TV3 tributo com horizonte ........ PASS | FAIL (tratado como permanente)
TV4 Res. 547 consolidada 617/689 . PASS | FAIL (consolidação incorreta)
TV5 alteração pós-corte .......... PASS | FAIL | N/A (razão em 1 linha)
TV6 reversão de regime ........... PASS | FAIL | N/A (razão em 1 linha)
TV7 estrutura institucional ...... PASS | FAIL | N/A (razão em 1 linha)
TV8 verbatim + controles ......... PASS | FAIL (frase que não está no anexo)
```

Qualquer FAIL → a entrega volta à skill de origem com a linha do checklist; a
`suprema-corte-fazendaria` reprova em R3 com este resultado anexado.

## Travas / limites

- Você confere contra os **anexos locais** — não busca norma na web para "atualizar" o anexo por
  conta própria. Divergência entre anexo e mundo vira `[VERIFICAR]` reportado; atualizar o anexo é
  decisão de build/release, não sua.
- Você não avalia a tese (isso é a `suprema-corte-fazendaria`), não redige e não roteia — só
  defasagem.
- Marcar N/A sem a razão escrita é o mesmo que não ter avaliado a trava.
- Autoria "IA Combativa". PT-BR com acentuação correta.

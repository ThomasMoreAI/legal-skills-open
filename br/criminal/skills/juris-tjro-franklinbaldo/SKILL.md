---
name: juris-tjro-franklinbaldo
title: O que esta skill faz
description: Consulta a jurisprudencia do Tribunal de Justica de Rondonia (TJRO) pelo sistema JURIS — acordaos, sentencas, votos, ementas, decisoes e relatorios de 1o e 2o graus. Use SEMPRE que o usuario pedir jurisprudencia, precedentes, decisoes ou julgados do TJRO; quiser saber "o que o Tribunal de Rondonia (ou uma Camara/Vara/Turma Recursal) decidiu sobre" algum tema; buscar por numero de processo (CNJ) no acervo; levantar precedentes locais para uma peca (contestacao, apelacao, embargos, parecer, memoriais); ou mapear como o TJRO vem decidindo determinada tese. Dispare mesmo quando o pedido nao usar a palavra "jurisprudencia" — basta o contexto ser decisoes judiciais de Rondonia. NAO use para tribunais de outros estados, STF, STJ ou TST.
author: franklinbaldo
author_url: https://github.com/franklinbaldo/causaganha/tree/main/.claude/skills/juris-tjro
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: criminal
language: pt
---

## O que esta skill faz

Busca documentos na jurisprudencia do TJRO via a API real do sistema JURIS
(`juris-back.tjro.jus.br`, indexado em Elasticsearch) e devolve resultados
enxutos: numero do processo (CNJ), tipo, data de julgamento, classe, orgao,
relator, um trecho do inteiro teor e o link do portal. Tambem busca todos os
documentos de um processo, extrai o inteiro teor limpo de um documento e
levanta facetas (classes, orgaos, tipos).

Toda a interacao acontece pelo script `scripts/juris.py` (Python 3, so
stdlib). Nao tente reescrever as chamadas HTTP a mao: o script ja encapsula o
endpoint correto e as varias armadilhas descritas abaixo.

## Como usar o script

Sempre rode o script (assuma rede liberada). Comece pelo `-h` se precisar.

Buscar por texto e filtros:

```
python scripts/juris.py buscar "<termo>" \
    [--tipo ACÓRDÃO EMENTA SENTENÇA VOTO DECISÃO RELATÓRIO] \
    [--classe "APELAÇÃO CÍVEL"] [--orgao "2ª Câmara"] [--relator "SOBRENOME"] \
    [--contendo palavra1 "expressão exata"] \
    [--de DD/MM/AAAA] [--ate DD/MM/AAAA] \
    [--recentes] [--tamanho N] [--trecho-perto TERMO] [--json]
```

Documentos de um processo (aceita numero com ou sem mascara):

```
python scripts/juris.py processo 7030969-47.2024.8.22.0001
```

Inteiro teor limpo de UM documento (o `id` vem do campo `id_documento` dos
resultados de `buscar`/`processo`):

```
python scripts/juris.py texto 21458095            # texto completo
python scripts/juris.py texto 21458095 --max 8000 # truncado
```

Facetas / agregacoes (panorama do acervo ou de um termo):

```
python scripts/juris.py facetas "improbidade" --limite 20
```

Acrescente `--json` em `buscar`/`processo`/`facetas` quando for processar o
resultado programaticamente (montar planilha, tabela, recurso repetitivo).

## Armadilhas da API — leia antes de buscar

A busca textual do servidor e **OR e analisada**. Cada palavra a mais no
`<termo>` AUMENTA o numero de resultados (traz quem casa com qualquer uma das
palavras), nao diminui. Consequencias praticas:

- Para precisao, coloque no `<termo>` a expressao/numero MAIS distintivo
  (ex.: `"18,25%"`, um nome proprio, uma sigla rara) e jogue as demais
  palavras obrigatorias em `--contendo` (filtro AND aplicado client-side sobre
  o inteiro teor). Exemplo que funciona bem:
  `buscar "18,25%" --tipo ACÓRDÃO --contendo "polícia civil"`.
- Ordene por relevancia (padrao) para pesquisa tematica; use `--recentes` so
  quando o que importa e a data.

Outras pegadinhas ja tratadas pelo script (nao as recrie do zero):

- `tipo` precisa ser ARRAY no corpo da requisicao; string crua derruba o
  servidor (HTTP 500). Por isso `--tipo` aceita varios valores.
- Filtro de DATA por intervalo no servidor quebra (range `gte/lte` -> 500).
  Por isso `--de/--ate` sao aplicados client-side; o script busca um pool maior
  e filtra. Em recortes de data muito amplos, aumente `--tamanho`.
- `nr_processo` casa por numero exato de 20 digitos (sem mascara); o script
  normaliza automaticamente.
- O inteiro teor (`ds_modelo_documento`) vem como HTML gigante com imagens em
  base64 embutidas (dezenas de KB por documento). O script SEMPRE limpa isso.
  **Nunca** despeje o JSON cru da API no contexto — estoura o limite.
- IGNORE o endpoint `GET /search/documentos/` e qualquer cliente que use os
  parametros `texto`/`nr_processo`/`paginaAtual` nele: o servidor IGNORA esses
  parametros e devolve o corpus inteiro sem filtrar. O endpoint de busca de
  verdade e `POST /search/varios_parametros/`, que o script usa.

## Como apresentar os resultados ao usuario

Sintetize, nao despeje. Fluxo recomendado:

1. Rode `buscar` com o termo distintivo + `--contendo` para fechar o tema.
2. Se vier muita coisa, separe por instancia/tipo (acordaos e votos de 2o grau
   sao os precedentes mais uteis; sentencas de 1o grau mostram a tendencia).
3. Liste cada julgado com: CNJ formatado, tipo, data, classe, orgao, relator e
   o link do portal. Acrescente uma linha sobre o desfecho quando der para
   inferir do trecho, mas avise que o trecho e parcial.
4. Para afirmar fundamento ou dispositivo com seguranca, use `texto <id>` e leia
   o inteiro teor antes de concluir — nao infira o resultado so pelo trecho.
5. Ofereca os proximos passos uteis: puxar a integra de um julgado, refinar o
   recorte, ou exportar a lista (`--json`) para planilha/tabela.

## Campos uteis em cada resultado

`nr_processo`, `tipo`, `dtjulgamento_str` / `dtjulgamento`, `ds_classe_judicial`,
`ds_orgao_julgador` / `ds_orgao_julgador_colegiado`, `ds_nome` (magistrado de 1o
grau), `nome_relator_acordao` (relator de 2o grau), `id_processo_documento`
(use no modo `texto`), `sistema_origem` (PJEPG = 1o grau, PJESG = 2o grau),
`id_documento_principal`. O link do portal e montado a partir desses campos.

---
name: skill-anxietylab
title: PNCP — contratações públicas via CLI
description: Consulta programática de contratações públicas do Brasil via APIs do PNCP (pncp.gov.br), usando a CLI pncp. Use quando o usuário pedir para buscar, coletar ou analisar licitações, editais, pregões, dispensas, atas de registro de preço, contratos públicos, órgãos públicos ou dados do Portal Nacional de Contratações Públicas — descoberta textual, coleta em massa por período, ou detalhe/itens/arquivos/resultados de uma contratação.
author: AnxietyLab
author_url: https://github.com/AnxietyLab/pncp-cli/tree/main/src/pncp_cli/skill
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: government-contracts
language: pt
---

# PNCP — contratações públicas via CLI

Requisito: a CLI `pncp` instalada e no PATH (`uv tool install pncp-cli` ou
`pipx install pncp-cli`; confirme com `pncp --version`).

## Padrões de uso

- stdout é JSON puro (seguro para `| jq`); progresso e avisos vão para stderr.
- `--ndjson` = um registro por linha, em streaming — o formato para coletas.
- `--table` = resumo legível para inspeção rápida.
- `--all` pagina até esgotar; combine com `--limit N` em explorações para não
  baixar milhares de registros à toa.
- Exit codes: `0` sucesso · `1` erro · `3` sucesso parcial (stdout válido,
  porém truncado; o stderr indica como retomar).

## Qual superfície usar

- **`search`** — descoberta por texto e facetas (palavra-chave, UF, modalidade,
  órgão). Rápida; a paginação trava em ~10.000 resultados.
- **`consulta`** — coleta em massa por intervalo de datas, sem teto de
  resultados. Intervalos maiores que 365 dias são divididos em janelas
  automaticamente.
- **`contratacao`/`itens`/`resultados`/`arquivos`/`historico`** — detalhe de
  UMA contratação, por `CNPJ ANO SEQ` ou `--controle <numero_controle_pncp>`.
- **`orgao`/`ata`/`contrato`/`pca`/`dominio`** — órgãos, atas, contratos,
  plano anual de contratações e tabelas de referência.

## Comandos

```
search [TERMO] --tipo edital|ata|contrato --status STATUS [--uf SP,RJ]
       [--modalidade 6,8] [--orgao ID] [--municipio ID] [--esfera F,E,M]
       [--all] [--limit N] [--incluir TERMO] [--excluir TERMO] [--link]
filtros --tipo edital [--faceta modalidades|orgaos|ufs|municipios]
consulta contratacoes --de YYYY-MM-DD --ate YYYY-MM-DD --modalidade ID|all
         [--por publicacao|atualizacao] [--uf --municipio --cnpj --unidade]
         [--all] [--limit N] [--checkpoint ARQ]
         [--incluir TERMO] [--excluir TERMO] [--match any|all] [--link]
consulta propostas --ate YYYY-MM-DD [--modalidade ID] [--uf SP] [--all]
consulta atas      --de --ate [--por atualizacao] [--cnpj] [--all]
consulta contratos --de --ate [--por atualizacao] [--cnpj] [--all]
consulta cobranca  --de --ate [--tipo N] [--all]
consulta pca       --ano N --classificacao COD | --usuario ID |
                   --por atualizacao --de --ate
contratacao  <CNPJ> <ANO> <SEQ> | --controle NUM
itens        <CNPJ> <ANO> <SEQ> | --controle NUM  [--tam N] [--limit N]
resultados   <CNPJ> <ANO> <SEQ> [--item N]     # fornecedor vencedor por item
arquivos     <CNPJ> <ANO> <SEQ> [--baixar DIR]
historico    <CNPJ> <ANO> <SEQ>
orgao        <CNPJ> [--unidades] | --id N | --buscar TEXTO
ata          listar|detalhe|arquivos|partes|contratos|historico <alvo> [--seq-ata N]
contrato     detalhe|arquivos|termos|empenhos|historico|cobranca|da-compra <alvo>
pca          consolidado|itens|valores|planos|csv <CNPJ> <ANO> [--seq N]
dominio      [tabela]                          # 17 tabelas de referência
controle     <numero_controle_pncp> [--detalhe]
```

Flags globais em qualquer subcomando: `--output json|ndjson|table`,
`-q/--quiet`, `--timeout S`, `--retries N`, `--pausa SEG`, `--version`.

## Vocabulário

- `--status` (search): `recebendo_proposta`, `propostas_encerradas`,
  `encerradas`, `todos`.
- **Modalidades**: `1` Leilão-Elet · `2` Diálogo Competitivo · `3` Concurso ·
  `4` Concorrência-Elet · `5` Concorrência-Pres · `6` Pregão-Elet ·
  `7` Pregão-Pres · `8` Dispensa · `9` Inexigibilidade · `10` Manif. de
  Interesse · `11` Pré-qualificação · `12` Credenciamento · `13` Leilão-Pres ·
  `14` Inaplicabilidade · `15` Chamada pública · `16-19` variantes
  internacionais. Fonte viva: `pncp dominio modalidades`.
- **Número de controle PNCP**: `CNPJ-TIPO-SEQ/ANO`
  (ex.: `07424905000138-1-000212/2026`; TIPO `1` = contratação, `2` =
  contrato). Atas usam o formato estendido `.../ANO-SEQATA`, aceito direto em
  `ata ... --controle`.

## Receitas

```bash
# editais abertos de um tema, visão rápida
pncp search "notebook" --tipo edital --status recebendo_proposta --uf SP --table

# coleta de um semestre de pregões eletrônicos, com retomada automática
pncp consulta contratacoes --de 2026-01-01 --ate 2026-06-30 --modalidade 6 \
  --all --ndjson --checkpoint ck.json > pregoes.ndjson

# filtro local por tema (token/frase, sem acentos), limite pós-filtro
pncp consulta contratacoes --de 2026-06-01 --ate 2026-06-30 --all --ndjson \
  --incluir "armazenamento de dados" --incluir storage --limit 100 --link

# da busca ao detalhe
pncp search "ambulância" --tipo edital --all --limit 50 --ndjson \
  | jq -r .numero_controle_pncp \
  | while read c; do pncp itens --controle "$c" --ndjson; done

# ground truth: quem venceu cada item e por quanto
pncp resultados 80881915000192 2026 44 --ndjson

# rastreabilidade compra → contratos → aditivos
pncp contrato da-compra --controle <controle-da-compra> --ndjson

# demanda futura declarada (PCA) de um órgão
pncp pca valores 00394452000103 2026
pncp pca csv 00394452000103 2026 --saida pca.csv
```

## Armadilhas conhecidas da API

A CLI trata os casos abaixo; conhecê-los ajuda a interpretar resultados
e diagnosticar problemas:

- Coleções truncam em 10 sem aviso se não forem paginadas
  (`tamanhoPagina=10` é o padrão do servidor). A CLI pagina tudo; contratações
  reais costumam ter dezenas de itens.
- CATMAT/CATSER vêm vazios nos itens (`catalogoCodigoItem`, `catalogo`).
  Não é possível triar por código de catálogo; use as descrições dos itens
  (texto livre, específicas), bem mais informativas que o objeto do edital.
  NCM é parcial (maior preenchimento na esfera federal).
- A busca textual é AND e aceita frase entre aspas; a precisão contra o
  objeto do edital é baixa (casa item perdido em registros de preço grandes).
  Use-a para descobrir vocabulário; a triagem fina é nos itens.
- Arquivos: `content-type` é sempre `application/octet-stream`; detecte o
  formato pelos magic bytes. Parte dos documentos "Edital" são ZIP
  contendo PDF, DOCX e XLSX (nomes internos podem vir em CP437).
- Rate limit (bloqueios de cerca de um minuto) e 5xx intermitentes são
  comuns; a CLI
  retenta e, se persistir, devolve parcial com exit 3. Em coletas longas,
  `--pausa 0.5` reduz a chance de bloqueio.
- Retomada é at-least-once: ao carregar em banco, deduplique por
  `numeroControlePNCP` (e chave composta com `numeroItem` para itens).
- Especificações oficiais: `/api/consulta/v3/api-docs` e
  `/api/pncp/v3/api-docs`.

## Fora de escopo

- Área de Trabalho autenticada do portal (buscas salvas, editais seguidos).
- Endpoints que exigem login de órgão (`/v1/usuarios*`, POST/PUT/DELETE).

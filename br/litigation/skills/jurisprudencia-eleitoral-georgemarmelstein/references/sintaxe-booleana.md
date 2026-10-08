# Sintaxe de Busca — Jurisprudência da Justiça Eleitoral (TSE + TREs)

A API é um **Elasticsearch `query_string`**. A barra de operadores do site
(`E OU NÃO * ? "" ""~ ~ : ^ + - () [] {}`) é traduzida pelo front para a sintaxe
Lucene. **Enviados crus à API, `E`/`OU`/`NÃO` viram termo literal** — por isso o
motor da skill (`engine.js`) normaliza `E→AND`, `OU→OR`, `NÃO→NOT` antes de enviar.

## Tabela de operadores (todos testados empiricamente)

| Operação | Sintaxe na API | Também aceita | Exemplo |
|----------|----------------|---------------|---------|
| E (AND) | `AND` | `&&`, espaço, `+` | `propaganda AND eleitoral` |
| OU (OR) | `OR` | `\|\|` | `bpc OR loas` |
| NÃO (NOT) | `NOT` | `-` | `propaganda NOT eleitoral`, `propaganda -eleitoral` |
| Frase exata | `"..."` | — | `"propaganda eleitoral"` |
| Proximidade | `"..."~N` | — | `"propaganda antecipada"~10` |
| Curinga (sufixo/meio) | `*` | — | `eleitor*` |
| Curinga (1 caractere) | `?` | — | `candidat?` |
| Fuzzy (aproximado) | `termo~` | — | `eleitorais~` |
| Campo específico | `campo:termo` | — | `textoEmenta:propaganda` |
| Boost (peso) | `termo^N` | — | `propaganda^3 eleitoral` |
| Agrupamento | `( )` | — | `(propaganda OR outdoor) AND eleitoral` |
| Intervalo | `[a TO b]` / `{a TO b}` | — | inclusivo / exclusivo |

**Para o usuário**, a skill aceita digitar em português (`E`/`OU`/`NÃO`) — a
normalização é automática. Para expressões complexas, prefira já escrever em
`AND/OR/NOT` para controlar a precedência.

## Códigos de campo oficiais (das "Dicas de pesquisa" do TSE — testados na API)

O operador `:` aceita **códigos curtos** de campo (aliases do Elasticsearch), que
funcionam direto na API:

| Código | Campo | Exemplo | Observação |
|--------|-------|---------|------------|
| `EMEN` | Ementa | `EMEN:"abuso de poder"` | só a ementa |
| `INTE` | Inteiro teor | `INTE:candidatura` | texto integral do acórdão |
| `DATD` | Data de julgamento | `DATD:[01/07/2026 TO 31/07/2026]` | **intervalo** dd/mm/aaaa |

- **Filtro de data:** `DATD:[dd/mm/aaaa TO dd/mm/aaaa]` (inclusivo) ou `{…}` (exclusivo).
  O `*` como limite aberto **não** funciona — para intervalo aberto use sentinela
  (`01/01/1900` / `31/12/2099`). O motor expõe isso via `dataInicio`/`dataFim`.
- **Incluir inteiro teor:** o motor tem `incluirInteiroTeor:true`, que acrescenta o
  campo `INTE` à busca (equivale ao checkbox "Incluir inteiro teor" do site).
- `RELA:` (relator) **não** existe como código; use `relatores.nome:"..."`.

## Filtros por campo indexado (injetados no `query_string`)

| Filtro | Campo | Exemplo |
|--------|-------|---------|
| Tribunal específico | `siglaTribunalJE` | `siglaTribunalJE:"TRE-SP"` |
| Vários tribunais | `siglaTribunalJE` | `siglaTribunalJE:("TRE-SP" OR "TRE-CE")` |
| UF | `siglaUF` | `siglaUF:"CE"` |
| Classe processual | `siglaClasse` | `siglaClasse:"RESPE"` |
| Nº do processo | `numeroProcesso` / `numeroUnico` | `numeroProcesso:060085643` |
| Relator | `relatores.nome` | `relatores.nome:"André Mendonça"` |
| Ano da eleição | `anoEleicao` | `anoEleicao:2022` |

O motor (`engine.js`) já expõe atalhos `tribunal:` e `uf:` que montam esses filtros.

## Escopo de tribunais (parâmetro `tribunais` do motor)

| Valor | O que busca | Endpoint (tenant) |
|-------|-------------|-------------------|
| `'tse'` | Só o **TSE** | `/tse/` |
| `'tres'` | **Todos os 27 TREs** juntos | `/tres/` |
| `'ambos'` | TSE + TREs (duas chamadas, merge) | `/tse/` + `/tres/` |

- Para **um TRE específico**, use `tribunais:'tres'` + `tribunal:'TRE-XX'`.
- O campo `tribunais` do corpo HTTP (`['tse']` / `['tre-*']`) é enviado por
  fidelidade ao front, mas quem de fato define o escopo é o **tenant na URL** e o
  filtro `siglaTribunalJE` no query.

### Códigos dos 27 TREs
`TRE-AC, TRE-AL, TRE-AP, TRE-AM, TRE-BA, TRE-CE, TRE-DF, TRE-ES, TRE-GO, TRE-MA,`
`TRE-MG, TRE-MS, TRE-MT, TRE-PA, TRE-PB, TRE-PR, TRE-PE, TRE-PI, TRE-RJ, TRE-RN,`
`TRE-RS, TRE-RO, TRE-RR, TRE-SC, TRE-SP, TRE-SE, TRE-TO`

## Ordenação (`ordenacao`)

| Valor | Sentido |
|-------|---------|
| `dj_desc` (padrão) | Data de julgamento — mais recentes primeiro |
| `dj_asc` | Data de julgamento — mais antigas primeiro |
| `dtj_desc` / `dtj_asc` | Data de publicação |
| `score` | Relevância |

## Observação sobre a ementa dos TREs

Nem todo acórdão de TRE traz `textoEmenta` preenchido — alguns só têm
`textoDecisao`. O motor devolve `resumo` com fallback automático (ementa quando
existe; senão, trecho da decisão) e o campo `fonteResumo` indica a origem. O texto
integral está sempre no PDF: `.../rest/download/pdf/{codigoDecisao}`.

---
name: varredura-jurisprudencial-orgao-sbroggioadv
title: VARREDURA-JURISPRUDENCIAL-ORGAO — Jurisprudência do órgão, validada por fetch real
description: 'VARREDURA-JURISPRUDENCIAL-ORGAO — Camada C3 do prisma-julgador-os. Busca a jurisprudência DO ÓRGÃO/RELATOR identificado na C1 usando o filtro nativo quando existe (STJ e STF: campo "Ministro" ✅; 1º/2º grau: consulta pública do tribunal 🟡, sempre declarando a via) e valida CADA precedente com a disciplina do juris-adv-os — WebFetch real, número do processo + trecho de ementa presentes na página, status ✅/⚠️/🔴; NUNCA ✅ sem fetch; falha técnica vira "não verificada", nunca 🔴 por palpite. Extrai de cada precedente validado o FUNDAMENTO que o órgão usou (não só o resultado) e documenta todas as queries tentadas. Trava R2: as camadas C4-C5 só citam o que esta skill coletou. Aciona: "jurisprudência do órgão", "o que essa câmara já decidiu", "julgados do relator", "precedentes dessa vara", "/juris-do-orgao", ou automaticamente no pipeline /prisma após o perfil estatístico.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/prisma-julgador-os-marketplace/tree/main/prisma-julgador-os/skills/varredura-jurisprudencial-orgao
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# VARREDURA-JURISPRUDENCIAL-ORGAO — Jurisprudência do órgão, validada por fetch real

## 1. Papel na cadeia (C3)

Recebe da C1 o órgão/relator identificado (sempre rotulado **SUGERIDO** até o usuário confirmar —
trava R4) e entrega às camadas C4-C5 o único corpus que elas podem citar: precedentes DAQUELE
órgão, cada um validado por WebFetch real, com o **fundamento** extraído.

> **TRAVA R2 — EM DESTAQUE** (`context/travas-prisma.md`): zero fabricação de precedente, relator
> ou número de processo — fetch real sempre. **As camadas seguintes (`matriz-aderencia-tese`,
> `reescrita-orientada-peca` e as 3 vozes) só citam o que ESTA skill coletou com fetch
> bem-sucedido.** Precedente que não está neste corpus não existe para o pipeline — ninguém
> completa de memória.

## 2. Pré-requisitos

- Órgão identificado pela `identificar-orgao-julgador` (código/nome) e, se houver, nome do
  relator amarrado pela `amarrar-nome-do-relator` **com o selo da via**.
- Tese(s) da peça (1-2 frases por tese).
- Sem identificação da C1 → rodar a C1 primeiro. Esta skill não adivinha órgão.

## 3. Etapa 1 — Montar as queries com o filtro certo (e o selo da via)

A via de filtro por relator nunca é inventada — vem da tabela verificada de
`context/fontes-por-relator.md`:

| Alvo | Via de filtro | Selo | Uso |
|---|---|---|---|
| **STJ** | Campo **"Ministro"** da pesquisa avançada (scon.stj.jus.br) — relator, revisor ou relator p/ acórdão | ✅ | Filtro nativo oficial: usar direto |
| **STF** | Filtro **"Ministro"** (portal.stf.jus.br/jurisprudencia) — relatou, redigiu ou decidiu monocraticamente | ✅ | Filtro nativo oficial: usar direto |
| **1º/2º grau** (TJs/TRFs/TRTs) | Consulta pública do tribunal (esaj/e-proc/projudi) e campo "Juiz" do PJe | 🟡 | Via confirmada por fonte secundária — **declarar a via na saída** e avisar que o usuário confere no sistema do tribunal |

Regras de query (disciplina do `buscar-jurisprudencia` do `juris-adv-os`):

1. Termos jurídicos exatos aspeados + dispositivo legal + relator/órgão + `site:` oficial.
2. Fontes oficiais primeiro; agregadores (JusBrasil/Escavador) apenas complemento, sempre
   marcados `AGREGADOR — conferir no tribunal`.
3. **Máximo 6 queries por tese.** Zero resultado não é falha: registrar e declarar — nunca forçar.
4. Sem via que amarre o nome (ou nome não confirmado) → buscar pelo **órgão** (câmara/vara) e
   rotular o corpus **"jurisprudência do órgão, sem nome"** (trava TV1 — o DataJud e esta
   varredura perfilam o órgão, nunca a pessoa).

## 4. Etapa 2 — Validar CADA precedente (disciplina literal do `validar-jurisprudencia`)

Para cada precedente candidato, o protocolo do motor `juris-adv-os`, sem afrouxar:

1. **WebFetch real na URL declarada** — capturar HTTP status + conteúdo.
2. **3 evidências na página:** **(a)** número do processo literal; **(b)** trecho de ementa
   transcrito presente (literal ou ~95% — diferenças só de acento/quebra de linha);
   **(c)** metadados — órgão julgador, relator e data batem.
3. **Status:**

| Status | Quando emitir |
|---|---|
| ✅ VALIDADA | Fetch 200 + (a) + (b) + (c) todos presentes |
| ⚠️ PARCIAL | Fetch 200, mas ementa parafraseada / 1 metadado diverge / fonte é agregador |
| 🔴 NÃO VALIDADA | A página **abriu** e o número do processo ou a ementa **não estão nela** |
| ⏸️ NÃO VERIFICADA | Falha **técnica** do fetch (timeout, anti-bot, JS-heavy, sem rede) — não confirma nem desmente |

> **Regra de bloqueio (herdada literal do `validar-jurisprudencia`): NUNCA emita ✅ se algum dos
> 3 itens (a/b/c) falhar. Em dúvida, rebaixa para ⚠️.**

**Falha técnica ≠ falsidade:** 🔴 é reservado à evidência negativa — a página carregou e o dado
não está lá. Timeout/anti-bot/JS-heavy → **"NÃO VERIFICADA (falha técnica)"**, nunca 🔴 por
palpite. Para efeito da trava R2, precedente não verificado **também não entra** no corpus
citável — mas o relatório distingue os dois estados, porque a ação recomendada é diferente
(reconsultar × descartar).

4. **Agregador com link para o tribunal** → segundo fetch no link oficial: confirmou → ✅ com
   observação `confirmado também na fonte oficial`; divergiu → ⚠️ `agregador divergente do oficial`.

## 5. Etapa 3 — Extrair o FUNDAMENTO (o que a matriz precisa)

Resultado sem fundamento não serve à `matriz-aderencia-tese`. De cada precedente validado:

```markdown
### [N] [Tribunal · órgão · nº do processo]
- **Status:** ✅/⚠️ · **Fonte:** [URL] · **Fetch:** HTTP [status]
- **Via de filtro + selo:** [STJ "Ministro" ✅ | STF "Ministro" ✅ | consulta do tribunal 🟡 | busca por órgão]
- **Resultado:** acolheu | rejeitou | parcial [a tese em questão]
- **FUNDAMENTO usado pelo órgão:** [dispositivo legal + tese/precedente que o órgão invocou —
  extraído do texto que o fetch trouxe, nunca deduzido]
- **Trecho literal da ementa que sustenta:**
  > [3-8 linhas transcritas, sem paráfrase]
- **Relator e data de julgamento (como constam na página):** [...]
```

Se a ementa validada mostra só o resultado e não revela o fundamento, registrar:
**"fundamento não aferível pela ementa — inteiro teor não coletado"**. A matriz recebe a célula
como parcial; ninguém a preenche por dedução.

## 6. Etapa 4 — Documentar as queries (auditabilidade)

O relatório fecha com a tabela de **todas** as queries tentadas — incluídas as que retornaram zero:

| # | Query | Fonte/via | Selo da via | Resultados | Aproveitados |
|---|---|---|---|---|---|

Zero achado em via ✅ é informação (o órgão pode nunca ter enfrentado a tese) — vira
**"sem dado do órgão"** na matriz, nunca é maquiado.

## 7. Saída final

```markdown
## Corpus do órgão — [órgão/relator · rótulo SUGERIDO ou CONFIRMADO]
**Coletado em:** [DD/MM/AAAA HH:MM] · **Via de filtro + selo:** [...]
**Precedentes:** [N] ✅ · [N] ⚠️ · [N] 🔴 · [N] não verificados (falha técnica)

[precedentes estruturados — §5]
[tabela de queries — §6]

⚠️ Corpus citável pelas camadas C4-C5: SOMENTE os ✅ (⚠️ entra apenas com o rótulo
PARCIAL e aviso de conferência). 🔴 e não verificados NÃO entram.
```

## 8. Fallback MCP (opcional, nunca dependência)

Com firecrawl MCP configurado, `firecrawl_scrape` pode substituir o WebFetch que falhou por
anti-bot/JS-heavy. **Sem MCP, não falhe:** o plugin funciona stock com WebSearch + WebFetch
nativos; a falha técnica vira "NÃO VERIFICADA" e é declarada.

## Travas desta skill

- **R2 (núcleo):** nenhum precedente sem fetch real; C4-C5 só citam este corpus.
- **R4:** o órgão desta varredura é o SUGERIDO/confirmado pela C1 — o rótulo acompanha a saída.
- **R3:** a saída descreve o padrão público do órgão no exercício da função — nunca "prevê o
  juiz X", nunca promessa de resultado.
- **R7:** autos sob segredo de justiça (art. 189 CPC) não são contornados — a varredura opera
  apenas sobre jurisprudência pública.
- **TV1:** sem via que amarre o nome, o corpus é "do órgão, sem nome" — nunca vendido como
  perfil de pessoa.

**Cross-links:** a `matriz-aderencia-tese` consome este corpus · o `relatorio-de-risco`
consolida · número/percentual com n + IC é território do `perfil-estatistico-orgao` · citação
avulsa fora do órgão → `juris-adv-os` · integridade/autenticidade do documento →
`blindagem-peticao-os` (fronteira: o prisma nunca declara autenticidade).

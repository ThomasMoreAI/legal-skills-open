---
name: juriscan-brunobracaioli
title: JuriScan
description: 'Análise forense de processos judiciais brasileiros. Extrai, classifica e cruza peças processuais, detecta contradições, calcula prazos CPC e gera relatórios de risco com exportação para Obsidian. Use quando mencionar: processo judicial, petição, sentença, acórdão, contradições, prazos, timeline, análise forense, Obsidian.'
author: brunobracaioli
author_url: https://github.com/brunobracaioli/juriscan
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
sources:
- title: Appellate Structure
  path: references/appellate_structure.md
- title: Binding Precedents
  path: references/binding_precedents.md
- title: Brazilian Legal Entities
  path: references/brazilian_legal_entities.md
- title: Prompt Templates
  path: references/prompt_templates.md
- title: Risk Scoring Rubric
  path: references/risk_scoring_rubric.md
---

# JuriScan

## Quick Run

Quando o usuário invocar `/juriscan <caminho_do_pdf>` ou pedir para analisar um processo, execute TODO o pipeline abaixo em sequência, sem parar para perguntar. O PDF pode estar em qualquer diretório — o usuário passa o caminho.

Se o usuário não passar um caminho, pergunte: "Qual o caminho do PDF do processo?"

**CWD check:** Se `pwd` apontar para `*/.claude/skills/juriscan*` (ou seja, a sessão do Claude foi iniciada dentro do diretório da própria skill), avise o usuário:

> "Você iniciou o Claude Code dentro do diretório da skill (`~/.claude/skills/juriscan`). Skills são globais — o normal é rodar o Claude na pasta do seu projeto, onde estão os PDFs. Saia desta sessão, faça `cd` para a pasta do processo e rode `claude` de novo. Posso continuar aqui mesmo assim se você passar o caminho absoluto do PDF."

Prossiga apenas se o usuário insistir ou fornecer caminho absoluto.

**Fluxo completo automático:**

1. Resolver `SKILL_DIR` e garantir dependências (Setup)
2. Criar diretório de análise ao lado do PDF: `<pdf_dir>/juriscan-output/`
3. Resolver o **modo de execução** (ver "Modos de execução" abaixo)
4. Executar o pipeline correspondente ao modo escolhido
5. No final, informar ao usuário:
   - Resumo executivo do processo (3-5 frases)
   - Quantas peças encontradas
   - Contradições detectadas (quantidade e as mais graves)
   - Prazos calculados (se houver)
   - Nível de risco
   - Onde estão os arquivos de saída
   - Se quiser Obsidian: "O vault está em `<output>/obsidian/` — abra essa pasta no Obsidian como vault"
   - run_id do audit trail (`.juriscan/audit/<run_id>.jsonl`) quando em modo agents

---

## Modos de execução

O juriscan suporta dois pipelines. O modo é resolvido a partir dos argumentos:

| Invocação | Modo | Status |
|---|---|---|
| `/juriscan --selftest` | Selftest | Ativo (ver seção Selftest) |
| `/juriscan --pipeline=legacy <pdf>` | **Legacy** (default até Phase 6) | Ativo — pipeline determinístico descrito em "Step-by-Step Pipeline" |
| `/juriscan --pipeline=agents <pdf>` | **Agents** (opt-in durante Phases 2–5) | Em construção — ver "Agents Pipeline" |
| `/juriscan <pdf>` (sem flag) | Legacy (por enquanto) | Flip do default acontece na Phase 6 Step 6.4 |

**Parsing dos argumentos:** quando o usuário invocar `/juriscan`, o primeiro token não-flag é o caminho do PDF. Flags reconhecidas: `--selftest`, `--pipeline=legacy`, `--pipeline=agents`. Qualquer flag desconhecida → avisar e cair em legacy.

**Gate de pré-requisitos (modo agents):** antes de seguir o modo agents, confirme que:

1. O arquivo `.claude/agents/juriscan-echo.md` existe em `$SKILL_DIR/.claude/agents/` (proxy para "subagents foram instalados").
2. `python3 "$SKILL_DIR/scripts/agent_io.py" validate --agent echo --input "$SKILL_DIR/tests/fixtures/agent_io/echo_valid.json"` retorna exit 0 (proxy para "schemas + jsonschema ok").

Se algum check falhar, **não** prossiga em modo agents. Informe o usuário o check que falhou e sugira `./install.sh` + `/juriscan --selftest`.

**Manifesto (ambos os modos):** no início de qualquer análise (não-selftest), crie/atualize `<output>/manifest.json`:

```bash
RUN_ID="$(python3 "$SKILL_DIR/scripts/agent_io.py" new-run --root "$OUTPUT_DIR/.juriscan/audit")"
python3 -c "
import json, os, time
manifest = {
    'run_id': '$RUN_ID',
    'pipeline_mode': '$PIPELINE_MODE',  # 'legacy' | 'agents'
    'pdf_path': os.path.abspath('$PDF_PATH'),
    'started_at': time.time(),
    'skill_dir': '$SKILL_DIR',
}
open('$OUTPUT_DIR/manifest.json','w').write(json.dumps(manifest, indent=2))
"
```

Nota: por ora `.juriscan/audit/` vive dentro de `<output>/` (não na raiz do projeto) para evitar poluir o cwd do usuário. Depois do Phase 6 podemos discutir se faz sentido centralizar.

---

## Agents Pipeline (modo `--pipeline=agents`)

Sequência quando o modo agents está selecionado. Cada passo é `[Python]` (script determinístico) ou `[Task]` (invocação de subagent via Task tool). Passos marcados `[PENDING: Phase N]` ainda não têm subagent real e abortam a pipeline com mensagem clara até serem implementados.

```
1. [Python]  scripts/extract_pdf.py              -> raw_text.txt + page_map.json
                                                    (Phase 2.x, stub usa extract_and_chunk.py)
2. [Task]    juriscan-segmenter                  -> /tmp/$RUN_ID-segmenter.json
3. [Python]  scripts/agent_io.py validate --agent segmenter ...
4. [Python]  scripts/persist_chunks.py           -> chunks/*.txt + index.json
5. [Task×N]  juriscan-parser (paralelo)          -> /tmp/$RUN_ID-parser-NN.json por chunk
6. [Python]  scripts/agent_io.py validate (N×)
7. [Python]  scripts/enrich_deterministic.py     -> pieces enriquecidas (normalizações)
8. [Task×3]  juriscan-advogado-autor, juriscan-advogado-reu, juriscan-auditor-processual (paralelo)
             [PENDING: Phase 3]
9. [Task]    juriscan-verificador                 [PENDING: Phase 4]
10.[Task]    juriscan-sintetizador                [PENDING: Phase 3]
11.[Python]  scripts/confidence_rules.py          [PENDING: Phase 3/4]
12.[Python]  scripts/finalize.py                  [PENDING: Phase 5]
13.[Python]  scripts/obsidian_export.py           (esquema v2 até Phase 6)
```

Regra geral para cada `[Task]`:

1. Defina um output path em `/tmp/juriscan-${RUN_ID}-<role>[-<idx>].json` e instrua o subagent a escrever nele.
2. Invoque via Task tool: `Task(subagent_type="juriscan-<role>", prompt="...")`.
3. Rode `python3 "$SKILL_DIR/scripts/agent_io.py" validate --agent <role> --input <path>`.
   - Exit 0 → passo 4.
   - Exit ≠ 0 → re-invocar o subagent **uma vez** passando o stderr do validate como feedback. Segunda falha → abortar pipeline e reportar `run_id`.
4. Rode `agent_io.py log --run-id $RUN_ID --agent <role> --input <path> --schema-valid true [--latency-ms N]`.
5. Consuma o arquivo validado no próximo passo Python.

**Invocações paralelas (passos 5 e 8):** emita todas as chamadas Task na **mesma mensagem** ao modelo. Não serialize — Claude Code executa-as em paralelo quando estão na mesma resposta do assistant.

---

## Selftest (`/juriscan --selftest`)

Quando o usuário invocar `/juriscan --selftest`, **não** rode o pipeline de análise. Em vez disso, execute o selftest abaixo para verificar que o contrato com subagents está funcionando. Esse é o único diagnóstico que prova, end-to-end, que a máquina de subagents + validação + audit trail está saudável antes de qualquer análise real.

1. **Gerar run_id e abrir audit trail:**
   ```bash
   RUN_ID="$(python3 "$SKILL_DIR/scripts/agent_io.py" new-run)"
   echo "selftest run_id=$RUN_ID"
   ```
2. **Invocar o subagent echo via Task tool** com `subagent_type="juriscan-echo"`. Instrua o echo a escrever em `/tmp/juriscan_selftest_${RUN_ID}.json` com `input_echo="selftest ping"`.
3. **Validar o JSON retornado:**
   ```bash
   python3 "$SKILL_DIR/scripts/agent_io.py" validate \
     --agent echo --input "/tmp/juriscan_selftest_${RUN_ID}.json"
   ```
4. **Registrar no audit trail:**
   ```bash
   python3 "$SKILL_DIR/scripts/agent_io.py" log \
     --run-id "$RUN_ID" --agent echo \
     --input "/tmp/juriscan_selftest_${RUN_ID}.json" \
     --schema-valid true --model-hint haiku
   ```
5. **Reportar ao usuário:**
   - Sucesso: `"Selftest OK — subagent echo respondeu e foi validado. run_id=$RUN_ID"`
   - Falha (validate retornou ≠ 0 ou arquivo ausente): mostre a mensagem do validator e o `run_id` para inspeção do audit trail.

Se o subagent `juriscan-echo` não estiver registrado (Task tool retornar erro de `subagent_type` desconhecido), oriente o usuário a rodar `./install.sh` novamente — o instalador é responsável por expor `.claude/agents/juriscan-*.md` ao Claude Code.

---

## Contract com subagents

A partir do Phase 2 do plano de migração (flag `--pipeline=agents`), o `juriscan` passa a delegar raciocínio semântico para subagents nativos do Claude Code, definidos em `.claude/agents/juriscan-*.md` dentro do repositório. O contrato entre este SKILL.md (orquestrador) e cada subagent é rígido e determinístico:

| Item | Onde mora | Papel |
|---|---|---|
| System prompt do subagent | `.claude/agents/juriscan-<role>.md` (frontmatter + corpo) | Define persona, ferramentas permitidas, modelo sugerido |
| Schema do output JSON | `references/agent_schemas/<role>_output.json` | Contrato de forma do output |
| Validador e logger | `scripts/agent_io.py` | CLI: `validate`, `log`, `new-run`, `extract-field` |
| Audit trail append-only | `.juriscan/audit/{run_id}.jsonl` | Uma linha por invocação Task |

**Fluxo obrigatório por invocação** (modo `--pipeline=agents`):

1. SKILL.md emite uma chamada `Task(subagent_type="juriscan-<role>", prompt=..., ...)`.
2. O subagent escreve seu resultado num arquivo JSON em caminho que o orquestrador escolheu.
3. SKILL.md roda `python3 $SKILL_DIR/scripts/agent_io.py validate --agent <role> --input <path>`.
   - Exit 0 → prosseguir.
   - Exit ≠ 0 → re-invocar o subagent **uma vez** com a mensagem de erro como feedback. Segundo erro → abortar o pipeline e reportar falha ao usuário com o `run_id`.
4. SKILL.md roda `agent_io.py log ...` para gravar a invocação (timestamp, schema_valid, input_hash, latency_ms quando aplicável).
5. Só depois de `schema_valid=true` o output é consumido por Python determinístico (enrich, persist_chunks, finalize).

**Invariantes não-negociáveis:**

- Nenhum subagent escreve direto em `analyzed.json`. Toda escrita canônica passa por scripts Python.
- Nenhum subagent consulta a web fora da whitelist (`references/whitelist_fontes.json`, Phase 4). O verificador é o único com `WebFetch` nas `tools:`.
- Nenhum Task call fica sem linha no audit trail. Se o subagent falhou, loga com `error=<msg>` e `schema_valid=false`.
- Paralelismo: quando houver múltiplas invocações independentes (parser por chunk, advogado-autor + advogado-réu + auditor), SKILL.md emite as chamadas Task **na mesma mensagem** para aproveitar a execução paralela nativa do Claude Code.

Phase 0 Step 0.4 introduz apenas o subagent `juriscan-echo` (selftest) e o esqueleto dos schemas. Os subagents reais (`segmenter`, `parser`, `advogado-autor`, `advogado-reu`, `auditor-processual`, `verificador`, `sintetizador`) entram nas Phases 2–4 do plano e cada um é um PR próprio.

---

## Setup

Executar uma vez no início da sessão:

```bash
# install.sh cria um symlink em ~/.claude/skills/juriscan apontando para a
# cópia clonada do repo. Se o link existe, essa é a fonte de verdade.
if [ -L "$HOME/.claude/skills/juriscan" ] || [ -d "$HOME/.claude/skills/juriscan" ]; then
    SKILL_DIR="$HOME/.claude/skills/juriscan"
else
    # Fallback: rodando direto do repo sem instalar (dev mode)
    SKILL_DIR="$(find -L . -maxdepth 3 -name 'SKILL.md' -path '*juriscan*' -exec dirname {} \; 2>/dev/null | head -1)"
fi
[ -z "$SKILL_DIR" ] && { echo "ERROR: could not locate juriscan skill. Run ./install.sh first."; exit 1; }
echo "SKILL_DIR=$SKILL_DIR"

python3 -c "import pypdf, jsonschema" 2>/dev/null || pip install pypdf pytesseract Pillow jsonschema
```

---

## Step-by-Step Pipeline

### Step 1: Extraction & Chunking

```bash
python3 $SKILL_DIR/scripts/extract_and_chunk.py --input <pdf_path> --output <output_dir>/
```

Extrai texto do PDF (pdftotext → pypdf → OCR) e divide por **peça processual** (27 tipos detectados). Output: `index.json` + `chunks/*.txt`.

### Step 2: Integrity Check

```bash
python3 $SKILL_DIR/scripts/integrity_check.py --input <output_dir>/
```

Verifica OCR quality, anomalias de metadata, lacunas de páginas. Flag chunks com confidence < 0.7.

### Step 3: Per-Chunk Analysis

Esta é a etapa mais importante do pipeline. Toda a qualidade dos arquivos persistidos (`analyzed.json`, `risk.json`, `instances.json`, vault Obsidian) e do relatório final depende dela.

O Step 3 tem três sub-steps:

#### Step 3a — Inicialize o skeleton

```bash
python3 $SKILL_DIR/scripts/analyzed_init.py \
  --index <output_dir>/index.json \
  --output <output_dir>/analyzed.json
```

Cria `analyzed.json` com todos os campos técnicos (`index`, `label`, `char_count`, `chunk_file`, `primary_date`, `dates_found`, `page_range`, `ocr_confidence`) preservados, e cada chunk marcado com `_pending_analysis: true`.

#### Step 3b — Analise cada chunk individualmente (um Write por chunk)

Para **cada arquivo** em `<output_dir>/chunks/NN-*.txt`:

1. **Read** o conteúdo do arquivo de chunk (não invente conteúdo — leia o texto real).
2. **Identifique o `tipo_peca`** consultando [piece_type_taxonomy.json](references/piece_type_taxonomy.json). Use o nome canônico exato (ex.: `"PETIÇÃO INICIAL"`, `"SENTENÇA"`, `"ACÓRDÃO"`).
3. **Aplique o prompt Análise Per-Chunk** de [prompt_templates.md](references/prompt_templates.md#1-análise-per-chunk-extração-estruturada) mentalmente ao conteúdo lido.
4. **Para chunks `ACÓRDÃO`**, também aplicar **Parsing Tripartite** de [prompt_templates.md](references/prompt_templates.md#3-parsing-tripartite-de-acórdão) e popular `acordao_structure` com `{ementa, relatorio, voto_relator, votos_divergentes[], dispositivo, resultado, votacao}`.
5. **Write** o resultado em `<output_dir>/chunks/NN.analysis.json` conforme o schema [chunk_analysis_schema.json](references/chunk_analysis_schema.json).

**Regra fundamental:** um `Write` por chunk. Não escreva um script Python que popula múltiplos arquivos de uma vez. O padrão correto é a mesma receita repetida N vezes — uma por chunk físico — cada uma independente da anterior.

**Campos obrigatórios por tipo de peça:**

| `tipo_peca` | Campos mínimos |
|---|---|
| Qualquer | `index`, `tipo_peca` |
| `PETIÇÃO INICIAL`, `RECONVENÇÃO` | + `partes`, `pedidos[]`, `valores`, `fatos_relevantes[]` |
| `CONTESTAÇÃO`, `RÉPLICA` | + `partes`, `argumentos_chave[]`, `fatos_relevantes[]` |
| `SENTENÇA`, `DESPACHO` | + `decisao`, `valores`, `fatos_relevantes[]` |
| `ACÓRDÃO` | + `decisao`, `acordao_structure`, `valores`, `fatos_relevantes[]` |
| `APELAÇÃO`, `AGRAVO`, `RECURSO ESPECIAL`, `RECURSO EXTRAORDINÁRIO` | + `pedidos[]`, `argumentos_chave[]`, `artigos_lei[]` |
| `LAUDO PERICIAL` | + `fatos_relevantes[]`, `resumo` |

Campos adicionais recomendados: `artigos_lei[]`, `jurisprudencia[]`, `binding_precedents[]`, `prazos[]`, `citation_spans[]` (trechos literais do texto fonte fundamentando as afirmações estruturadas).

**Quando o chunker agrupa peças num único arquivo físico:** se o arquivo `chunks/02-laudo-pericial.txt` contém na verdade *laudo + sentença + apelação*, você tem duas opções:

- **Split semântico (preferido):** escreva múltiplos arquivos de análise para o mesmo chunk físico:
  - `chunks/02.analysis.json` — `{"index": 2, "tipo_peca": "LAUDO PERICIAL", "primary_date": "30/09/2024", ...}`
  - `chunks/02a.analysis.json` — `{"index": "2a", "tipo_peca": "SENTENÇA", "chunk_file_override": "chunks/02-laudo-pericial.txt", "primary_date": "12/12/2024", ...}`
  - `chunks/02b.analysis.json` — `{"index": "2b", "tipo_peca": "APELAÇÃO", "chunk_file_override": "chunks/02-laudo-pericial.txt", "primary_date": "15/01/2025", ...}`
  O `merge_chunk_analysis.py` valida e cria N entradas em `analyzed.chunks[]` todas apontando para o mesmo arquivo físico.

  **IMPORTANTE — `primary_date` por peça:** cada entrada split-semantic **deve** incluir seu próprio `primary_date` no formato DD/MM/YYYY extraído do texto da peça específica (não a data do chunk físico). Sem isso, o merge herda a data do parent por default, mas as peças filhas ficam com a data errada e a ordenação cronológica do relatório fica quebrada. Exemplo: se a sentença é de 12/12/2024 e está dentro do chunk físico do laudo contábil de 30/09/2024, o `02a.analysis.json` (sentença) precisa declarar `"primary_date": "12/12/2024"`.
- **Peça dominante:** use apenas `02.analysis.json` com o `tipo_peca` mais importante do agrupamento (geralmente a decisória — sentença, acórdão) e documente as outras em `fatos_relevantes`.

#### Step 3c — Consolide os arquivos de análise

```bash
python3 $SKILL_DIR/scripts/merge_chunk_analysis.py \
  --analyzed <output_dir>/analyzed.json \
  --chunks-dir <output_dir>/chunks/ \
  --output <output_dir>/analyzed.json
```

O merge script:
- Valida cada `chunks/NN.analysis.json` contra [chunk_analysis_schema.json](references/chunk_analysis_schema.json)
- Mescla os campos semânticos nas entradas correspondentes de `analyzed.chunks[]`
- Processa split-semantic (arquivos com sufixos `a`, `b`, etc.) criando entradas adicionais
- Falha com erro claro se algum chunk físico não tiver arquivo de análise correspondente
- Avisa se detectar scripts helper (`build_analyzed.py` etc.) no diretório

Referência de entidades: [brazilian_legal_entities.md](references/brazilian_legal_entities.md).

### Step 4: Schema Validation + Content Quality Check

```bash
python3 $SKILL_DIR/scripts/schema_validator.py --input <output_dir>/analyzed.json
```

Se falhar, corrigir os `chunks/NN.analysis.json` específicos indicados no erro e re-rodar `merge_chunk_analysis.py` antes de re-validar. Repetir até válido.

**Depois do schema OK, rode o quality gate bloqueante com plano de retry:**

```bash
python3 $SKILL_DIR/scripts/content_quality_check.py \
  --input <output_dir>/analyzed.json \
  --strict \
  --per-chunk-retry-plan
```

Se `--strict` retornar exit 1, o stdout vai listar **exatamente** quais chunks precisam ser re-analisados e quais campos estão faltando. Exemplo:

```
Chunks precisando re-análise:
  [0] PETIÇÃO INICIAL (chunks/00-peticao-inicial.txt) → faltam: pedidos, valores
  [3] SENTENÇA (chunks/03-sentenca.txt) → faltam: decisao
```

**Retry loop direcionado (max 2 iterações):**
1. Para cada chunk listado, faça **apenas** o que o plano pede:
   - Read `<chunk_file>`
   - Re-analise preenchendo os `missing_fields`
   - Write `chunks/<NN>.analysis.json` atualizado
2. Re-rode `merge_chunk_analysis.py` para consolidar
3. Re-rode `content_quality_check.py --strict --per-chunk-retry-plan`
4. Se ainda houver retry após 2 iterações, prossiga e warn no relatório final — não entre em loop infinito.

### Step 5: Cross-Synthesis

**5a. Contradições:**
```bash
python3 $SKILL_DIR/scripts/legacy/contradiction_report.py --analysis <output_dir>/analyzed.json --output <output_dir>/contradictions.json
```
Complementar com prompt **Detecção de Contradições** de [prompt_templates.md](references/prompt_templates.md#2-detecção-de-contradições) para análise semântica.

**5b. Instâncias:**
```bash
python3 $SKILL_DIR/scripts/instance_tracker.py --analysis <output_dir>/analyzed.json --output <output_dir>/instances.json
```
Complementar com prompt **Rastreamento por Instância** de [prompt_templates.md](references/prompt_templates.md#4-rastreamento-de-argumentos-por-instância).

**5c. Precedentes Vinculantes:**
Usar prompt **Alinhamento de Precedentes** de [prompt_templates.md](references/prompt_templates.md#5-alinhamento-de-precedentes-vinculantes). Referência: [binding_precedents.md](references/binding_precedents.md).

### Step 6: Prazo Calculation

```bash
python3 $SKILL_DIR/scripts/prazo_calculator.py --analysis <output_dir>/analyzed.json --output <output_dir>/prazos.json
```

Python puro (CPC Art. 219-232). Dados: [cpc_prazos.json](references/cpc_prazos.json), [feriados_forenses.json](references/feriados_forenses.json).

### Step 7: Risk Scoring

```bash
python3 $SKILL_DIR/scripts/legacy/risk_scorer.py --analysis <output_dir>/analyzed.json --output <output_dir>/risk.json
```

Complementar com prompt **Avaliação de Risco** de [prompt_templates.md](references/prompt_templates.md#6-avaliação-de-risco-litigioso). Rubrica: [risk_scoring_rubric.md](references/risk_scoring_rubric.md).

### Step 8: Consolidate

Merge contradictions, instances, prazos e risk no `analyzed.json` final. Re-validar com `schema_validator.py`.

### Step 8.5: Monetary Recalculations (Lei 14.905/2024)

```bash
python3 $SKILL_DIR/scripts/finalize_legacy.py --input <output_dir>/analyzed.json --inplace
```

Detecta condenações monetárias cruzando o marco de 30/08/2024 e gera `monetary_recalculations[]` com breakdown por período (juros 1% a.m. até 29/08/2024, SELIC - IPCA após). Heurística conservadora: só recalcula quando há data E valor de condenação.

### Step 9: Obsidian Export

```bash
python3 $SKILL_DIR/scripts/obsidian_export.py --analysis <output_dir>/analyzed.json --output <output_dir>/obsidian/
```

Gera vault com 7 views: `_INDEX`, `_TIMELINE`, `_CONTRADIÇÕES`, `_ENTIDADES`, `_RISCO`, `_INSTÂNCIAS`, `_PRAZOS`.

### Step 9a: Strategic Recommendations

Gere recomendações estratégicas por polo seguindo o prompt **Geração de Recomendações Estratégicas** de [prompt_templates.md](references/prompt_templates.md#7-geração-de-recomendações-estratégicas).

Use os outputs já produzidos (`analyzed.json`, `contradictions.json`, `instances.json`, `risk.json`, `prazos.json`, `monetary_recalculations` do Step 8.5) como input. Produza 3-5 recomendações por polo, cada uma com `evidence_quote` verbatim obrigatório.

Write `<output_dir>/recommendations.json` conforme [agent_schemas/recommendations_output.json](references/agent_schemas/recommendations_output.json).

Validar:
```bash
python3 $SKILL_DIR/scripts/agent_io.py validate --agent recommendations --input <output_dir>/recommendations.json
```

Se falhar, corrigir as recomendações (provavelmente faltou `evidence_quote` em alguma) e re-validar.

### Step 9b: Generate Executive Report

```bash
python3 $SKILL_DIR/scripts/generate_report.py \
  --analyzed <output_dir>/analyzed.json \
  --contradictions <output_dir>/contradictions.json \
  --instances <output_dir>/instances.json \
  --prazos <output_dir>/prazos.json \
  --risk <output_dir>/risk.json \
  --recommendations <output_dir>/recommendations.json \
  --output <output_dir>/REPORT.md
```

Gera `REPORT.md` — relatório executivo markdown consolidado com: resumo executivo, caixas de alerta (art. 942, Lei 14.905, prazos urgentes), tabela de peças, contradições com citações verbatim, avaliação de risco, recomendações estratégicas por polo, cronograma Mermaid, prazos e listagem de arquivos.

### Step 10: Present Report to User — LITERAL ONLY

**Regra absoluta, não-negociável:** a sua resposta final ao usuário é o **conteúdo literal** do `REPORT.md`. Caractere por caractere. Zero edições. Zero adições. Zero reformatação.

**Procedimento:**

1. `Read <output_dir>/REPORT.md`
2. Cole o conteúdo exato como sua mensagem ao usuário. Nada a mais, nada a menos.
3. Ao final, uma **única** linha adicional com os paths:

    `Arquivos: <output_dir>/REPORT.md · <output_dir>/obsidian/`

**PROIBIDO:**

- ❌ Adicionar um parágrafo "Conclusão estratégica"
- ❌ Adicionar um parágrafo "Observações finais" ou "Considerações"
- ❌ Re-escrever o resumo executivo com mais detalhes que o relatório
- ❌ Reformatar a tabela de peças com outra estrutura
- ❌ Adicionar comentários meta ("Como pode-se observar...", "Vale destacar que...")
- ❌ Inserir emojis decorativos que não estão no relatório
- ❌ "Enriquecer" qualquer seção com informações que não estão no arquivo em disco

**Por que a regra é absoluta:**

O `REPORT.md` é **reproduzível e auditável**. Duas execuções do mesmo PDF devem produzir relatórios idênticos em disco. Se você enriquece a resposta oralmente, você quebra a reprodutibilidade — o usuário vê uma coisa, o arquivo tem outra, e eles não conseguem provar que é a mesma análise.

**Se você se pegar escrevendo "Conclusão estratégica", "Observação final" ou "Considerações" na sua resposta, PARE imediatamente.** O relatório já contém tudo que precisa ser dito. Confie no template.

**Se você acha que falta algo no REPORT.md:** abra uma issue no GitHub (`https://github.com/brunobracaioli/juriscan/issues`) para melhorar o template no próximo release. Não contorne via paráfrase na resposta.

**Exemplo do que NÃO fazer:**

> [conteúdo do REPORT.md]
>
> **Conclusão estratégica:** apesar do risco global ser BAIXO, há uma janela crítica... ← **PROIBIDO**

**Exemplo do que fazer:**

> [conteúdo do REPORT.md exato, literal]
>
> Arquivos: /path/to/REPORT.md · /path/to/obsidian/

---

## Edge Cases

- **500+ páginas**: Chunk primeiro, analise em batches de 5-10 peças, persista JSON incrementalmente
- **PDFs de tribunais (PJe, e-SAJ, PROJUDI)**: Headers repetitivos removidos automaticamente
- **PDFs escaneados**: OCR fallback via pytesseract; flag chunks baixa confiança para vision
- **Múltiplos volumes**: Trate cada volume separadamente, concatene antes da síntese
- **Multi-instância**: Instance tracker lida com 1ª instância → TJ → STJ → STF

## Dependencies

- Python 3.10+ | poppler-utils (pdftotext, pdfinfo) | tesseract-ocr (opcional)
- Python: pypdf, pytesseract, Pillow, jsonschema

## Reference Files

- [references/output_schema.json](references/output_schema.json) — JSON Schema v2
- [references/prompt_templates.md](references/prompt_templates.md) — Todos os prompt templates
- [references/brazilian_legal_entities.md](references/brazilian_legal_entities.md) — NER reference
- [references/piece_type_taxonomy.json](references/piece_type_taxonomy.json) — Metadata de tipos de peça
- [references/cpc_prazos.json](references/cpc_prazos.json) — Regras de prazos CPC
- [references/feriados_forenses.json](references/feriados_forenses.json) — Feriados forenses
- [references/appellate_structure.md](references/appellate_structure.md) — Hierarquia de instâncias
- [references/binding_precedents.md](references/binding_precedents.md) — Precedentes vinculantes
- [references/risk_scoring_rubric.md](references/risk_scoring_rubric.md) — Rubrica de risco

# Prompt Templates — Forensic Legal Analysis

Todos os prompts usados pelo Claude durante a análise forense de processos judiciais.

---

## 1. Análise Per-Chunk (Extração Estruturada)

```
Analise a seguinte peça processual e extraia as informações em JSON.

PEÇA: {chunk_label}
TEXTO:
{chunk_text}

Retorne APENAS JSON válido com esta estrutura:
{
  "tipo_peca": "string - tipo da peça processual",
  "data": "string - data da peça (DD/MM/YYYY) ou null",
  "partes": {
    "autor": ["lista de autores/requerentes"],
    "reu": ["lista de réus/requeridos"],
    "advogados_autor": ["nome - OAB"],
    "advogados_reu": ["nome - OAB"],
    "juiz": "nome do juiz/desembargador ou null",
    "vara": "vara/câmara ou null",
    "perito": "nome do perito ou null"
  },
  "numero_processo": "string ou null",
  "classe_processual": "string ou null",
  "assunto": "string - tema principal",
  "pedidos": ["lista de pedidos formulados"],
  "argumentos_chave": ["lista de argumentos principais"],
  "decisao": "string - dispositivo da decisão ou null",
  "valores": {
    "causa": "valor da causa ou null",
    "condenacao": "valor da condenação ou null",
    "honorarios": "valor dos honorários ou null",
    "outros": [{"descricao": "string", "valor": "string"}]
  },
  "artigos_lei": ["Art. X da Lei Y - contexto de citação"],
  "jurisprudencia": ["Tribunal - Nº Processo/Recurso - Relator - Tese"],
  "prazos": [{"tipo": "string", "data_inicio": "string", "data_fim": "string"}],
  "fatos_relevantes": ["lista de fatos narrados relevantes"],
  "resumo": "resumo executivo em 3-5 frases"
}
```

---

## 2. Detecção de Contradições

```
Dado o conjunto de peças analisadas abaixo, identifique TODAS as contradições, inconsistências e divergências entre as peças.

Para cada contradição encontrada:
1. Indique as peças envolvidas
2. Cite o trecho específico de cada peça (verbatim)
3. Classifique: FATO_DIVERGENTE | VALOR_INCONSISTENTE | DATA_CONFLITANTE | ARGUMENTO_CONTRADITÓRIO | JURISPRUDÊNCIA_CONFLITANTE
4. Avalie o impacto: ALTO | MÉDIO | BAIXO
5. Sugira como explorar processualmente
6. Inclua os char_start e char_end dos trechos citados para citation grounding

{json_de_todos_os_chunks_analisados}

Retorne JSON:
{
  "contradictions": [
    {
      "tipo": "FATO_DIVERGENTE|VALOR_INCONSISTENTE|DATA_CONFLITANTE|ARGUMENTO_CONTRADITÓRIO|JURISPRUDÊNCIA_CONFLITANTE",
      "impacto": "ALTO|MÉDIO|BAIXO",
      "pecas": ["Peça A", "Peça B"],
      "descricao": "descrição detalhada da contradição",
      "sugestao": "como explorar processualmente",
      "citation_spans": [
        {"peca": "Peça A", "source_text": "trecho verbatim", "char_start": 0, "char_end": 100},
        {"peca": "Peça B", "source_text": "trecho verbatim", "char_start": 0, "char_end": 100}
      ]
    }
  ]
}
```

---

## 3. Parsing Tripartite de Acórdão

```
Analise o seguinte ACÓRDÃO e separe sua estrutura tripartite.

TEXTO:
{acordao_text}

Retorne JSON:
{
  "ementa": "texto completo da ementa (inclui classificação e súmula da decisão)",
  "relatorio": "texto completo do relatório do relator",
  "voto_relator": "texto do voto do relator (fundamentação + dispositivo)",
  "votos_divergentes": ["texto de cada voto divergente, se houver"],
  "dispositivo": "parte dispositiva final (ACORDAM...)",
  "resultado": "PROVIDO|DESPROVIDO|PARCIALMENTE_PROVIDO|NÃO_CONHECIDO",
  "votacao": "UNÂNIME|MAIORIA"
}
```

---

## 4. Rastreamento de Argumentos por Instância

```
Dado o conjunto de peças abaixo, organizadas por instância judicial, identifique como cada ARGUMENTO JURÍDICO evoluiu entre instâncias.

Para cada argumento:
1. Em qual peça apareceu pela primeira vez
2. Como foi tratado em cada instância subsequente
3. Se foi acolhido, rejeitado, ou não apreciado em cada decisão
4. Se a parte reformulou o argumento em recurso

{chunks_por_instancia}

Retorne JSON:
[
  {
    "argumento": "descrição normalizada do argumento",
    "primeira_aparicao": {
      "instancia": "1a_instancia|tj|stj|stf",
      "peca": "tipo da peça",
      "texto": "trecho relevante"
    },
    "evolucao": [
      {
        "instancia": "1a_instancia",
        "peca_decisoria": "SENTENÇA",
        "status": "acolhido|rejeitado|parcialmente_acolhido|não_apreciado",
        "fundamentacao": "resumo da fundamentação"
      },
      {
        "instancia": "tj",
        "peca_decisoria": "ACÓRDÃO",
        "status": "mantido|reformado|parcialmente_reformado|não_apreciado",
        "fundamentacao": "resumo da fundamentação"
      }
    ],
    "status_final": "mantido|reformado|parcialmente_reformado|não_apreciado"
  }
]
```

---

## 5. Alinhamento de Precedentes Vinculantes

```
Analise os seguintes precedentes vinculantes detectados no processo e avalie o alinhamento com os fatos e teses do caso.

PRECEDENTES DETECTADOS:
{binding_precedents_list}

FATOS DO CASO:
{fatos_relevantes_consolidados}

TESES DAS PARTES:
- POLO ATIVO: {teses_autor}
- POLO PASSIVO: {teses_reu}

Para cada precedente:
1. A tese vinculante se aplica ao caso concreto?
2. Favorece qual polo?
3. Há distinguishing possível?

Retorne JSON:
[
  {
    "precedente": "identificação completa",
    "tipo": "SUMULA_VINCULANTE|IRDR|IAC|REPERCUSSAO_GERAL|RECURSO_REPETITIVO",
    "tese": "texto da tese vinculante",
    "aplicavel": true|false,
    "alinhamento": "FAVORAVEL_AUTOR|FAVORAVEL_REU|NEUTRO|INAPLICAVEL",
    "justificativa": "por que se aplica ou não",
    "distinguishing": "argumentos de distinguishing possíveis, ou null"
  }
]
```

---

## 6. Avaliação de Risco Litigioso

```
Com base na análise completa do processo abaixo, produza uma avaliação de risco litigioso.

DADOS DO PROCESSO:
{full_analysis_json}

Avalie em três dimensões:

1. RISCO PROCESSUAL (0-10):
   - Prazos: algum vencido ou em risco?
   - Nulidades: há vícios formais identificáveis?
   - Competência: há questão jurisdicional?
   - Citação/Intimação: regular?

2. MÉRITO (0-10):
   - Força probatória: provas documentais, testemunhais, periciais?
   - Alinhamento jurisprudencial: os precedentes favorecem qual polo?
   - Contradições exploráveis: quais enfraquecem qual polo?
   - Fundamentação legal: as teses têm base sólida?

3. EXPOSIÇÃO MONETÁRIA:
   - Cenário otimista (para o polo ativo): valor máximo
   - Cenário realista: valor provável
   - Cenário pessimista: valor mínimo
   - Custas e honorários estimados

Para cada fator, cite a peça e trecho que fundamentam a avaliação.

Retorne JSON:
{
  "risk_level": "ALTO|MÉDIO|BAIXO",
  "overall_score": 0-10,
  "procedural_risk": {
    "score": 0-10,
    "factors": [{"fator": "...", "avaliacao": "...", "peca_fonte": "..."}]
  },
  "merit_indicators": {
    "score": 0-10,
    "favorable_factors": [{"fator": "...", "fundamentacao": "...", "peca_fonte": "..."}],
    "unfavorable_factors": [{"fator": "...", "fundamentacao": "...", "peca_fonte": "..."}]
  },
  "monetary_exposure": {
    "max_exposure": "R$ ...",
    "likely_range": {"min": "R$ ...", "max": "R$ ..."},
    "costs": {"custas_estimadas": "R$ ...", "honorarios_sucumbencia": "R$ ..."}
  },
  "strategic_recommendations": [
    "recomendação 1 com fundamentação",
    "recomendação 2 com fundamentação"
  ]
}
```

---

## 7. Geração de Recomendações Estratégicas

Usar após o risk scoring para gerar ações concretas por polo, com fundamentação legal e citação verbatim obrigatória.

```
Você é um analista forense produzindo recomendações estratégicas para ambos
os polos do processo. Receba:
- analyzed.json (peças processuais com campos estruturados)
- contradictions.json (contradições detectadas)
- instances.json (rastreamento por instância)
- risk.json (avaliação de risco)
- monetary_recalculations (se presente no analyzed.json)
- auditor_findings (se presente no analyzed.json — art. 942, nulidades, omissões)

Produza 3-5 recomendações POR POLO (autor e réu). Cada recomendação é uma
ação concreta, acionável, com:

1. polo: "autor" | "reu"
2. priority: "ALTA" | "MÉDIA" | "BAIXA"
3. action: descrição curta da ação (ex.: "Opor embargos de declaração arguindo
   art. 942 CPC")
4. fundamentacao: justificativa legal + fática (2-4 frases)
5. evidence_quote: trecho VERBATIM da peça fonte que embasa a recomendação
   (não parafrasear — copiar literalmente). Mínimo 10 caracteres.
6. evidence_chunk_ref: índice da peça fonte (inteiro)
7. deadline_days: prazo em dias úteis para executar a ação (quando aplicável)
8. deadline_basis: fundamento legal do prazo (ex.: "CPC art. 1.023")
9. impact: impacto estratégico esperado
10. confidence: 0.0 a 1.0

REGRAS:
- Cada recomendação DEVE ter evidence_quote verbatim. Recomendação sem
  citação é recusada pelo schema validator.
- Priorize recomendações que exploram findings do auditor (art. 942,
  omissões, recálculos Lei 14.905).
- Prazos processuais devem vir de cpc_prazos.json ou do prazo mais urgente
  em prazos.json.
- Autor e réu têm incentivos opostos — evite recomendações neutras.
- Se houver art. 942 detectado em acórdão por maioria reformando mérito:
  a recomendação ALTA para o autor É obrigatória (embargos de declaração
  arguindo a nulidade).

Formato de saída: JSON estrito conforme references/agent_schemas/recommendations_output.json.
Schema tem "additionalProperties: false" — não adicionar campos extras.
```

Output Schema: [agent_schemas/recommendations_output.json](agent_schemas/recommendations_output.json)

Validação: `python3 scripts/agent_io.py validate --agent recommendations --input recommendations.json`

---

## 8. Citation Grounding (Instrução Adicional)

Adicionar a QUALQUER prompt de análise quando citation grounding for necessário:

```
REGRA DE CITATION GROUNDING:
Para cada afirmação analítica, inclua no campo "citation_spans" o trecho EXATO do texto original que a sustenta:
- assertion: sua conclusão analítica
- source_text: cópia verbatim do trecho (mínimo 20 caracteres)
- char_start: posição inicial aproximada no chunk
- char_end: posição final aproximada no chunk

Nenhuma afirmação sem citação. Se não encontrar fundamento textual explícito, marque assertion como "[INFERIDO]" e explique a base da inferência.
```

---

## Mermaid: Timeline Gantt

Template para geração do diagrama Mermaid de timeline:

```mermaid
gantt
    title Timeline do Processo {processo_number}
    dateFormat  DD/MM/YYYY
    section Fase Conhecimento
    Petição Inicial          :done, pi, {data_pi}, 1d
    Citação do Réu           :done, cit, {data_cit}, 1d
    Contestação              :done, cont, {data_cont}, 1d
    Réplica                  :done, rep, {data_rep}, 1d
    Audiência                :done, aud, {data_aud}, 1d
    Sentença                 :done, sent, {data_sent}, 1d
    section Fase Recursal
    Apelação                 :active, ap, {data_ap}, 1d
    Contrarrazões            :cr, {data_cr}, 1d
    Acórdão                  :ac, {data_ac}, 1d
```

---

## Obsidian: Estrutura do Vault

```
processo-{numero}/
├── _INDEX.md                    # Resumo executivo + mapa do processo
├── _TIMELINE.md                 # Timeline cronológica completa
├── _CONTRADIÇÕES.md             # Mapa de contradições
├── _ENTIDADES.md                # Todas as partes, advogados, juízes
├── _RISCO.md                    # Avaliação de risco litigioso
├── _INSTÂNCIAS.md               # Evolução de argumentos por instância
├── _PRAZOS.md                   # Dashboard de prazos com status
├── peças/
│   ├── 00-peticao-inicial.md
│   ├── 01-contestacao.md
│   └── ...
├── legislação/
│   ├── art-14-cdc-lei-8078-1990.md
│   └── ...
├── jurisprudência/
│   ├── stj-resp-1758799-mg.md
│   └── ...
└── diagramas/
    ├── timeline.mermaid
    └── reference-graph.mermaid
```

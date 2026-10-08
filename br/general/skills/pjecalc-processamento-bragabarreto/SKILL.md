---
name: pjecalc-processamento-bragabarreto
title: pjecalc-processamento — Extração, Validação e HITL
description: '> Autoridade arquitetural: pjecalc-transformacao. Esta skill documenta a implementação > real das Fases 1–3 do pipeline. Em caso de conflito com pjecalc-transformacao, ela prevalece.'
author: bragabarreto
author_url: https://github.com/bragabarreto/pjecalc-agente/tree/main/.claude/skills/pjecalc-processamento
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
sources:
- title: Regras Validacao
  path: references/regras-validacao.md
- title: Schema Contrato
  path: references/schema-contrato.md
---

# pjecalc-processamento — Extração, Validação e HITL

> **Autoridade arquitetural:** `pjecalc-transformacao`. Esta skill documenta a implementação
> real das Fases 1–3 do pipeline. Em caso de conflito com `pjecalc-transformacao`, ela prevalece.

## Por que esta skill existe

O pipeline do pjecalc-agente começa com um documento (PDF/DOCX/texto ou relatório
estruturado) e deve terminar com um JSON válido, revisado e confirmado pelo usuário —
pronto para instruir a automação Playwright.

Esta skill consolida em um único lugar:
- As regras reais de extração (o que o LLM deve capturar e como)
- O schema JSON completo com todos os campos atualizados
- As regras de validação implementadas em `ValidadorSentenca`
- Os triggers de HITL que pausam para revisão humana
- Os pontos críticos onde a extração costuma falhar

O código-fonte de referência está em:
- `modules/extraction.py` — ingestão, extração, validação
- `modules/classification.py` — mapeamento de verbas
- `webapp.py` — orquestração do fluxo, HITL, confirmação

---

## Regra inviolável — IA obrigatória

> **A prévia do cálculo NÃO pode ser gerada sem extração via IA.**
>
> Quando a IA falha (sem créditos, timeout, erro 400/500), o processamento é BLOQUEADO
> com `status="erro_ia"`. Nunca contornar esse bloqueio. A confiabilidade da liquidação
> trabalhista depende da extração por IA.

---

## Fluxo completo — Fases 1 a 3

```
Entrada do usuário (PDF / DOCX / TXT / relatório estruturado)
    │
    ▼ FASE 1 — Ingestão (modules/ingestion.py)
    │
    │  PDF nativo    → pdfplumber (extrai texto com layout preservado)
    │  PDF escaneado → pytesseract OCR como fallback automático
    │  DOCX/TXT      → extração direta de texto
    │  Relatório     → flag is_relatorio=True (CalcMACHINE ou similar)
    │
    │  Normalização: encoding UTF-8, datas BR → ISO, valores monetários
    │
    ▼ FASE 2 — Extração com IA (modules/extraction.py)
    │
    │  Roteamento de modelo:
    │    PDF nativo    → Claude Sonnet 4.6 via base64 (visão multimodal)
    │    Texto/DOCX    → Claude ou Gemini conforme USE_GEMINI env
    │    Relatório     → Claude/Gemini conforme seleção do usuário + streaming
    │
    │  Gemini: timeout 30s (texto) / 60s (relatório) → fallback Claude se falhar
    │  Claude: timeout 90s (texto/PDF) / 120s+streaming (relatório)
    │
    │  Output: JSON com todos os campos do schema (ver references/schema-contrato.md)
    │  Falha de IA: _erro_ia=True → BLOQUEAR (regra inviolável acima)
    │
    ▼ FASE 3 — Validação + HITL
    │
    │  1. ValidadorSentenca(dados).validar()
    │     → ResultadoValidacao(valido: bool, erros: list, avisos: list)
    │
    │  2. Erros bloqueantes impedem confirmação
    │     Avisos mostram alertas mas não bloqueiam
    │
    │  3. Interface prévia: todos os campos editáveis
    │     PATCH /previa/{sessao_id}/campo → salvarCampo() inline
    │
    │  4. Usuário revisa, corrige, confirma
    │     POST /previa/{sessao_id}/confirmar
    │     → calculo.confirmado_em = now()
    │
    ▼ JSON válido e confirmado → pjecalc-automacao (Fases 4-6)
```

---

## Roteamento de modelos IA

| Tipo de entrada | Modelo primário | Fallback | Timeout | Streaming |
|---|---|---|---|---|
| PDF nativo | Claude Sonnet 4.6 (base64) | Gemini (converte para texto) | 90s | Não |
| Texto / DOCX | Claude ou Gemini (USE_GEMINI) | Claude | 90s | Não |
| Relatório estruturado | Claude ou Gemini (usa `usar_gemini`) | Claude | 120s | Sim |

**Por que streaming no relatório?**
Relatórios têm prompt muito longo (guia de mapeamento + texto do relatório = 30k+ tokens).
Sem streaming, a API Anthropic derruba a conexão antes da resposta completa. `messages.stream()`
mantém a conexão viva durante toda a geração.

**Controle pelo usuário:** seletor "Modelo de IA" no formulário define `usar_gemini=True/False`.
Se não selecionado, usa `USE_GEMINI` do `.env`.

---

## Schema JSON — Campos principais

> Schema completo em `references/schema-contrato.md`.

### processo
```json
{
  "numero": "0000153-87.2026.5.07.0002",  // CNJ completo — copiar EXATO do documento
  "numero_seq": "0000153",                 // 7 dígitos (desmembrado por _desmembrar_cnj)
  "digito_verificador": "87",              // 2 dígitos
  "ano": "2026",
  "segmento": "5",                         // 5 = Justiça do Trabalho
  "regiao": "07",                          // tribunal (07 = TRT7)
  "vara": "0002",                          // 4 dígitos
  "reclamante": "João da Silva",
  "reclamado": "Empresa ABC Ltda",
  "estado": "CE",                          // sigla UF (2 letras)
  "municipio": "FORTALEZA",               // APENAS nome da cidade, sem UF/sufixo
  "vara_nome": "3ª Vara do Trabalho de Fortaleza"
}
```

### contrato
```json
{
  "admissao": "01/03/2022",               // DD/MM/AAAA
  "demissao": "03/12/2024",               // DD/MM/AAAA — NUNCA usar data projetada com AP
  "ajuizamento": "15/01/2025",
  "tipo_rescisao": "sem_justa_causa",     // ver enums abaixo
  "ultima_remuneracao": 1518.00,          // float
  "maior_remuneracao": 1518.00,           // float
  "carga_horaria": 220,                   // horas/mês (int)
  "regime": "Tempo Integral"
}
```

**Enums tipo_rescisao:** `sem_justa_causa` | `justa_causa` | `pedido_demissao` |
`rescisao_indireta` | `distrato` | `morte` | `culpa_reciproca` | `contrato_prazo`

### verbas_deferidas (array)
```json
[
  {
    "nome_sentenca": "HORAS EXTRAS",
    "tipo": "Principal",
    "caracteristica": "Comum",
    "ocorrencia": "Mensal",
    "periodo_inicio": "01/03/2022",
    "periodo_fim": "03/12/2024",
    "percentual": 0.50,                   // float decimal (50% → 0.50)
    "base_calculo": "Historico Salarial",
    "valor_informado": null,
    "incidencia_fgts": true,
    "incidencia_inss": true,
    "incidencia_ir": true,
    "sumula_439": false,
    "confianca": 0.95
  }
]
```

**Enums caracteristica:** `Comum` | `13o Salario` | `Aviso Previo` | `Ferias`
**Enums ocorrencia:** `Mensal` | `Dezembro` | `Periodo Aquisitivo` | `Desligamento`

### honorarios (LISTA — um registro por devedor)
```json
[
  {
    "tipo": "SUCUMBENCIAIS",
    "devedor": "RECLAMADO",
    "tipo_valor": "CALCULADO",
    "base_apuracao": "Condenação",
    "percentual": 0.15,                   // 15% → 0.15 (NUNCA omitir)
    "valor_informado": null,
    "apurar_ir": true
  },
  {
    "tipo": "SUCUMBENCIAIS",
    "devedor": "RECLAMANTE",
    "tipo_valor": "CALCULADO",
    "base_apuracao": "Verbas Não Compõem Principal",
    "percentual": 0.10,
    "valor_informado": null,
    "apurar_ir": true
  }
]
```

⚠ PJE-Calc NÃO tem opção "Ambos" — sucumbência recíproca = dois registros separados.

### ferias (LISTA — um registro por período aquisitivo)
```json
[
  {
    "situacao": "Vencidas",
    "periodo_inicio": "01/03/2022",
    "periodo_fim": "28/02/2023",
    "abono": false,
    "dobra": false
  },
  {
    "situacao": "Vencidas",
    "periodo_inicio": "01/03/2023",
    "periodo_fim": "28/02/2024",
    "abono": false,
    "dobra": false
  }
]
```

⚠ NUNCA retornar `ferias=[]` se o relatório/sentença listar períodos aquisitivos.

### fgts
```json
{
  "aliquota": 0.08,
  "multa_40": true,
  "multa_467": false,
  "saldo_fgts": null                      // float | null — saldo nas contas FGTS
}
```

### historico_salarial (LISTA)
```json
[
  {
    "nome": "Salário",
    "data_inicio": "01/03/2022",
    "data_fim": "31/08/2024",
    "valor": 1518.00,
    "incidencia_fgts": true,
    "incidencia_cs": true
  }
]
```

⚠ NUNCA retornar `historico_salarial=[]` se houver faixas salariais ou tabela de salários.

---

## Pontos críticos de extração

### Número do processo
- Copiar EXATAMENTE como aparece no documento (formato NNNNNNN-DD.AAAA.J.TT.OOOO)
- Nunca truncar os 7 dígitos da sequência
- `_desmembrar_cnj()` cuida do desmembramento — não fazer manualmente
- Validação CNJ módulo 97 é AVISO (não bloqueante) — número pode ter OCR ruim

### Honorários
- `percentual`: float decimal (15% → 0.15; "10% a 15%" → usar 0.10)
- NUNCA omitir `honorarios` se o relatório listar "Honorários Advocatícios"
- Sucumbência recíproca → dois objetos na lista
- `base_apuracao` padrão: RECLAMADO → "Condenação"; RECLAMANTE → "Verbas Não Compõem Principal"

### Férias
- NUNCA deixar `ferias=[]` se há períodos aquisitivos listados
- `situacao`: "Vencidas" (período completo) ou "Proporcionais" (período incompleto)
- Datas são do período AQUISITIVO, não da rescisão

### Município
- APENAS o nome da cidade, sem UF ("CE"), sem "Vara", sem número
- Correto: "FORTALEZA" — Errado: "Fortaleza/CE", "3ª Vara do Trabalho de Fortaleza"
- O seletor no PJE-Calc usa 3 estratégias: exato → startsWith → includes

### Demissão
- NUNCA usar a "data projetada com aviso prévio" como `contrato.demissao`
- Usar APENAS a data real da dispensa

---

## Regras de validação

> Implementação completa em `references/regras-validacao.md`.

### Erros bloqueantes (impedem automação)
| Campo | Regra |
|---|---|
| `processo.estado` | Obrigatório |
| `contrato.admissao` | Obrigatório, formato DD/MM/AAAA |
| `contrato.ultima_remuneracao` | Obrigatório, > 0 |
| `contrato.demissao` | Se informado: deve ser > admissao |
| IA indisponível | `_erro_ia=True` → bloquear sempre |

### Avisos (não bloqueantes)
| Campo | Regra |
|---|---|
| CNJ módulo 97 | Dígito calculado ≠ informado → aviso no SSE |
| confidence < 0.7 | Em campos críticos → sugerir revisão |
| tipo_rescisao × verbas | Ex: justa causa + aviso prévio → aviso |

---

## Troubleshooting

| Sintoma | Causa mais provável | Solução |
|---|---|---|
| `status=erro_ia` | API key inválida ou sem créditos | Verificar ANTHROPIC_API_KEY / GEMINI_API_KEY |
| Timeout em relatório | Relatório muito longo (>25k chars) | Streaming já ativo; aguardar até 120s |
| `honorarios=[]` extraído | LLM não capturou percentual | Editar na prévia antes de confirmar |
| `ferias=[]` extraído | LLM ignorou períodos listados | Editar na prévia antes de confirmar |
| CNJ "dígito inválido" | LLM truncou número sequencial | Corrigir `processo.numero` na prévia |
| Município não encontrado | Nome com UF ou sufixo | Corrigir para apenas nome da cidade |
| Histórico vazio | LLM viu salário uniforme | Criar entrada manual com período completo |

---

## Relação com outras skills

| Quando preciso de... | Consulte |
|---|---|
| Arquitetura geral, regras invioláveis | `pjecalc-transformacao` |
| O que fazer com o JSON após confirmação | `pjecalc-automacao` |
| Campo a campo no PJE-Calc | `pjecalc-preenchimento` |
| Diagnóstico de falhas na automação | `pjecalc-agent-debugger` |

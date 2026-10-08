---
name: contingencia-report-autodevx
title: Relatório de Contingência Jurídica
description: Gera relatórios estruturados de contingência jurídica para uso em balanços, auditoria e compliance. Use quando o usuário precisar classificar processos por probabilidade de perda (provável/possível/remota) conforme CPC art. 95-96 e IAS 37 / CPC 25, calcular impacto financeiro no passivo contingente, ou preparar memórias de cálculo auditáveis para controllers e auditores externos. Aplicável a portfólios de processos cíveis, trabalhistas e tributários.
author: autodevx
author_url: https://github.com/autodevx/legal-skills/tree/main/skills/contingencia-report
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: regulatory
language: pt
sources:
- title: Ias37 Resumo
  path: references/ias37-resumo.md
- title: Probabilidades Cpc
  path: references/probabilidades-cpc.md
---

# Relatório de Contingência Jurídica

## Contexto e objetivo

Gerar análise de passivo contingente conforme:
- **CPC 25** (Provisões, Passivos Contingentes e Ativos Contingentes) — equivalente brasileiro do IAS 37
- **IAS 37** (Provisions, Contingent Liabilities and Contingent Assets) — norma IFRS
- **CPC arts. 95-96** (valoração da prova e probabilidade de êxito)
- Critérios aceitos pelas Big Four (Deloitte, PwC, EY, KPMG)

O relatório deve ser **auditável**: cada classificação precisa de fundamentação rastreável.

## Etapas obrigatórias

### 1. Coleta de dados dos processos

Para cada processo, extrair ou solicitar:

| Campo | Obrigatório | Fonte típica |
|-------|-------------|--------------|
| Número CNJ | Sim | PJe, eSAJ, DataJud |
| Polo (autor/réu) | Sim | Petição inicial |
| Matéria (cível/trabalhista/tributária) | Sim | Classificação CNJ |
| Pedido principal | Sim | Petição inicial |
| Valor da causa | Sim | Petição inicial |
| Valor atualizado (se disponível) | Desejável | Cálculo atualizado |
| Fase processual | Sim | Último andamento |
| Tribunal | Sim | Número CNJ |
| Advogado responsável | Sim | Gestão interna |
| Última movimentação | Desejável | Andamento processual |
| Prognóstico do advogado | Desejável | Parecer interno |

### 2. Classificação de probabilidade

Aplicar escala conforme CPC 25 / IAS 37:

| Classificação | Probabilidade | Critério prático | Ação contábil |
|---|---|---|---|
| **Provável** | >50% (IAS 37) / >70% (prática BR) | Decisão desfavorável em instância relevante; jurisprudência consolidada contra; confissão/acordo parcial | **Provisionar integralmente** |
| **Possível** | 20-50% (IAS 37) / 30-70% (prática BR) | Processo em andamento; jurisprudência dividida; tese nova sem consolidação | **Divulgar em notas explicativas**; provisionar parcialmente se política interna exigir |
| **Remoto** | <20% (IAS 37) / <30% (prática BR) | Tese jurídica sólida; precedentes favoráveis consolidados; acordo provável em termos favoráveis | **Não provisionar**; menção opcional em nota |

**Regras de override (sempre aplicar):**
- Processo trabalhista em fase de execução → mínimo **Provável**, salvo embargos à execução com alta probabilidade de êxito
- Auto de infração fiscal lavrado → mínimo **Possível**
- Ação com liminar concedida contra a empresa → mínimo **Possível**
- Trânsito em julgado desfavorável → **Provável** (100%)
- Acordo em negociação avançada → usar valor do acordo como base

### 3. Cálculo do valor em risco

```
valor_risco = valor_base × fator_probabilidade × fator_fase

valor_base = valor_causa (ou valor atualizado se disponível)

fator_probabilidade:
  Provável  = 1.00
  Possível  = 0.50 (ou conforme política da empresa)
  Remoto    = 0.00

fator_fase:
  Trânsito em julgado desfavorável    = 1.00
  Execução de título judicial          = 1.00
  Acórdão desfavorável (2ª instância)  = 0.85
  Sentença desfavorável (1ª instância) = 0.70
  Em instrução / perícia               = 0.50
  Citação / contestação                = 0.40
  Distribuição / inicial               = 0.35
```

**Provisão recomendada:**
- Processos **Prováveis**: valor_risco integral
- Processos **Possíveis**: zero (apenas nota) OU percentual conforme política interna
- Processos **Remotos**: zero

### 4. Output estruturado

Sempre entregar em dois formatos:

#### 4a. Tabela executiva (para CFO/diretoria)

```
| # | Processo | Matéria | Valor Causa | Prob. | Fase | Valor em Risco | Provisão Recomendada |
```

Ordenar por valor em risco decrescente. Incluir subtotais por:
- Matéria (cível / trabalhista / tributária)
- Classificação (provável / possível / remoto)

#### 4b. Memória de cálculo (para auditoria)

Para cada processo classificado como Provável ou Possível:
1. Fundamentação da classificação (por que provável/possível?)
2. Referência ao fato gerador (decisão, jurisprudência, fase)
3. Cálculo detalhado (valor_base × fator_prob × fator_fase)
4. Data-base do relatório
5. Responsável jurídico pela avaliação
6. Histórico de reclassificações (se aplicável)

### 5. Sumário executivo

Ao final, sempre gerar:

```
══════════════════════════════════════════════════════
RELATÓRIO DE CONTINGÊNCIA JURÍDICA
Data-base: [DD/MM/AAAA]
══════════════════════════════════════════════════════

TOTAL DE PROCESSOS ANALISADOS:        N
  ├── Prováveis:                       X processos
  ├── Possíveis:                       Y processos
  └── Remotos:                         Z processos

PROVISÃO TOTAL RECOMENDADA:            R$ X.XXX.XXX,XX
PASSIVO CONTINGENTE (possível):        R$ X.XXX.XXX,XX
EXPOSIÇÃO TOTAL (todos):               R$ X.XXX.XXX,XX

MAIOR EXPOSIÇÃO INDIVIDUAL:            Processo XXXXXXX (R$ X.XXX.XXX,XX)
MATÉRIA MAIS CRÍTICA:                  [trabalhista/cível/tributária]

VARIAÇÃO vs. PERÍODO ANTERIOR:         +/- X% (se disponível)
══════════════════════════════════════════════════════
```

### 6. Análise de sensibilidade (opcional, recomendado para portfólios >50 processos)

- Cenário otimista: reclassificar possíveis → remotos
- Cenário pessimista: reclassificar possíveis → prováveis
- Impacto no resultado: delta de provisão entre cenários
- Útil para apresentação ao conselho/board

## Cuidados obrigatórios

1. **Nunca classificar como "remoto" sem fundamentação explícita** — deve citar o fato concreto
2. **Processos trabalhistas em execução → sempre "provável"** salvo embargos com alta chance
3. **Ações fiscais com auto lavrado → mínimo "possível"**
4. **Sempre indicar que o relatório exige validação do advogado responsável**
5. **Não misturar critérios IAS 37 (>50%) com prática brasileira (>70%)** — declarar qual padrão está sendo usado
6. **Atualização monetária**: se o valor da causa for antigo, alertar que precisa de atualização

## Referências

Ler `references/probabilidades-cpc.md` para definições legais detalhadas.
Ler `references/ias37-resumo.md` para critérios IFRS e exemplos.

## Limites

- Não substitui avaliação jurídica formal — relatório deve ser validado por advogado
- Valores de risco são estimativas baseadas em fatores genéricos; cada caso pode ter particularidades
- Não acessa sistemas de andamento processual (PJe, eSAJ) — depende dos dados fornecidos
- Não faz cálculos de atualização monetária (juros, correção) — usa valor da causa como base

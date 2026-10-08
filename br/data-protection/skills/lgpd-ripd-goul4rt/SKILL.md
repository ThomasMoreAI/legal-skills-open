---
name: lgpd-ripd-goul4rt
title: RIPD — Relatório de Impacto à Proteção de Dados
description: Produce a Relatório de Impacto à Proteção de Dados (RIPD / DPIA) under LGPD Art. 38 for high-risk processing activities. Use when user asks "RIPD", "DPIA", "relatório de impacto", "avaliação de impacto LGPD", or when lgpd-data-mapping flagged an activity as high-risk under Resolução ANPD nº 2/2022 Art. 4 (large scale, profiling, sensitive data, minors/elderly, emerging tech, public surveillance, automated decisions). Produces `.lgpd/RIPD/ripd-{slug}.md`. Always cite the assessment methodology.
author: goul4rt
author_url: https://github.com/goul4rt/lgpd-skills/tree/main/skills/lgpd-ripd
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# RIPD — Relatório de Impacto à Proteção de Dados

Art. 38 LGPD: o controlador deve elaborar relatório contendo a descrição dos tipos de dados, metodologia de tratamento e segurança, e análise das salvaguardas.

A regulamentação específica está na Agenda Regulatória 2025–2026 (Fase 1). Até a regulamentação sair, use a metodologia consolidada abaixo.

## Quando é obrigatório

Aplicar o **teste cumulativo da Res. CD/ANPD nº 2/2022, Art. 4º** (alto risco):

**Critério geral (pelo menos um):**
- (a) tratamento em larga escala
- (b) afeta significativamente interesses e direitos fundamentais

**E critério específico (pelo menos um):**
- (a) uso de tecnologias emergentes ou inovadoras (IA, biometria avançada)
- (b) vigilância ou controle de zonas acessíveis ao público
- (c) decisões tomadas com base em tratamento automatizado de dados (profiling)
- (d) dados sensíveis, de crianças, de adolescentes, de idosos

**Threshold prático de "larga escala"**: > 2 milhões de titulares (~1% da população BR — critério preliminar ANPD/2024).

Também pode ser **exigido pela ANPD** a qualquer momento (Art. 38), incluindo para legítimo interesse (Art. 10, § 3º).

## Estrutura do RIPD

### 1. Identificação
- Nome da atividade, controlador, encarregado, equipe envolvida, data, versão

### 2. Contexto e objetivo
- Descrição do produto/feature
- Justificativa de negócio
- Stakeholders

### 3. Descrição do tratamento
- Fluxo completo: coleta → armazenamento → uso → compartilhamento → eliminação
- Diagrama (sugerido — Mermaid em `assets/`)
- Sistemas envolvidos
- Operadores

### 4. Necessidade e proporcionalidade
- A finalidade poderia ser atingida com menos dados?
- O tratamento é proporcional ao risco?
- Alternativas consideradas e rejeitadas

### 5. Conformidade com princípios (Art. 6 LGPD)
Tabela com 10 princípios e como cada um é atendido.

### 6. Base legal
- Art. 7º ou Art. 11
- Se legítimo interesse → anexar LIA
- Se consentimento → descrever mecanismo e prova

### 7. Direitos do titular
- Como cada um dos 9 direitos do Art. 18 é atendido nesta atividade
- Especial atenção a Art. 18, IV (anonimização/bloqueio/eliminação) e Art. 20 (revisão)

### 8. Identificação de riscos
Use metodologia ISO 31000 / ISO 27005:

| ID | Risco | Probabilidade (1-5) | Impacto (1-5) | Nível (P×I) | Status |
|---|---|---|---|---|---|
| R001 | Vazamento via SDK de analytics | 3 | 4 | 12 (alto) | mitigado |
| R002 | ... | | | | |

Categorias de risco a considerar:
- Vazamento de confidencialidade
- Perda de integridade (corrupção)
- Indisponibilidade
- Uso indevido para fins não autorizados
- Discriminação algorítmica (Art. 6, IX)
- Re-identificação de dados anonimizados
- Acesso não autorizado de funcionários (insider)
- Compartilhamento indevido com terceiros

### 9. Salvaguardas e mecanismos de mitigação
Para cada risco, descrever controles:
- Técnicos (criptografia, pseudonimização, RBAC, MFA, log, monitoring)
- Administrativos (políticas, treinamento, NDAs)
- Organizacionais (segregação de funções, revisões periódicas)

### 10. Risco residual
Após mitigações, qual o risco que sobra? É aceitável?

### 11. Consulta a partes interessadas
- Titulares (pesquisa, focus group, conselho de usuários) — opcional mas recomendado para alto impacto
- Equipe técnica
- Encarregado
- Jurídico
- Segurança da informação

### 12. Decisão
- [ ] Prosseguir como planejado
- [ ] Prosseguir com modificações: {quais}
- [ ] Não prosseguir
- [ ] Consultar ANPD previamente (Art. 38, parágrafo único)

**Aprovado por**: {Encarregado}
**Data**: {data}

### 13. Plano de revisão
- Próxima revisão: {data} ou ao mudar {gatilho}

## Workflow

1. Identifique atividades flagadas como alto risco no data map.
2. Para cada uma, copie `assets/ripd-template.md` para `.lgpd/RIPD/ripd-{slug}.md`.
3. Preencha colaborativamente (eng + jurídico + encarregado).
4. **⏸ CHECKPOINT**: obrigatório — RIPD precisa de aprovação do Encarregado antes de continuar.
5. Indexe em `.lgpd/RIPD/INDEX.md`.

## Status update

```markdown
## F12 — RIPD ✓
- {N} RIPDs produzidos
- {M} riscos identificados, {X} aceitos, {Y} mitigados, {Z} pendentes
- Próximo: lgpd-eca-digital-minors (se aplicável) ou lgpd-vendor-audit
```

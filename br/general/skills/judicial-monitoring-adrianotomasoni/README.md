# Monitoramento Judicial Proativo

> Categoria: `core` · Detecção e classificação de eventos judiciais relevantes para seguro garantia e crédito.

## O que é

Skill que analisa movimentações processuais (sistema CNJ/Brasil), classifica eventos por nível de criticidade (A–D) e calcula um score de risco com recomendação de ação e prazo. Serve para antecipar acionamento de garantia, priorizar a atuação jurídica e acompanhar mudanças no perfil de risco de uma apólice. Sinaliza e prioriza — **não substitui parecer jurídico**.

## Gatilhos (quando acionar)

- "Analisa esta movimentação processual"
- "Esse processo é risco para a apólice?"
- "O que essa penhora/citação significa?"
- "Classifica o evento e calcula o score"

## Quando NÃO usar

- Substituir análise jurídica especializada (apenas sinaliza/prioriza).
- Fora do Brasil — a taxonomia segue o sistema CNJ.
- Análise de crédito do garantido → `credit-risk-analysis`.

## Como usar por plataforma

- **Claude Code / Codex / Gemini / Copilot:** instale em `~/.claude/skills/judicial-monitoring/`.
- **Claude.ai:** upload de `SKILL.md` em Settings → Knowledge e envie a movimentação.
- **Cursor:** `@skills/core/judicial-monitoring/SKILL.md` + o texto da movimentação.

## Exemplo

Prompt: *"Movimento: 'Penhora sobre bem imóvel, R$ 450.000'. Parte garantida: Construtora XYZ. Apólice TRK-2026-001234."*
Saída esperada: nível A, score ~87, valor de impacto e recomendação de acionamento imediato (ver `SKILL.md`). Casos em `examples/case-studies.json`.

## Material de apoio

- `SKILL.md` — taxonomia de eventos (v4), protocolo de análise e formato de saída.
- `prompts/` — prompts especializados por fase (`fase-1-v4-unified.md`, `fase-1-v3-spec.md`, `melhorias-motor-judicial-2026.md`).
- `examples/case-studies.json` — casos reais anonimizados.
- `tests/eval-suite.json` — suite de avaliação.

## Dependências

- `credit-risk-analysis` — para contexto de risco do garantido.

> Taxonomia (níveis A–D), fórmula de score e cadências são definições internas — não alterar. Há latência de até 24h na atualização dos tribunais. Pesos e parâmetros calibrados: TODO: preencher com <calibração proprietária> da TradeRisk.

## Tags

`judicial` `monitoring` `seguro-garantia` `risco` `eventos`

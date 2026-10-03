---
name: torre-estrategia
title: N2 — Quando e como aplicar
description: Oficina de Estratégia — Monte Carlo, SWOT, cenários múltiplos. Use para decisões sob incerteza, planejamento de longo prazo, análise de trade-offs.
author: igormorais123
author_url: https://github.com/igormorais123/vila-inteia/tree/main/engine/skills_oficinas/torre_estrategia
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: pt
---

## N2 — Quando e como aplicar

Use para perguntas do tipo "vale a pena fazer X dado incerteza Y?",
"quais riscos dominantes em Z?", "SWOT de cenário W". Evite para tarefas
meramente descritivas — aqui sempre há trade-off a pesar.

Precondições: pergunta estratégica clara com ao menos uma alternativa e
uma incerteza. Agente precisa ter reputação 40 ou mais (consultoria
estratégica é regulada pela constituição).

Heurísticas de decisão:
- Decisões financeiras com distribuição conhecida → Monte Carlo.
- Comparação competitiva → SWOT com pesos numéricos.
- Múltiplos futuros plausíveis → Matriz de Cenários 2x2.

## N3 — Procedimento

1. Agente entra em `torre_estrategia` e enuncia a pergunta em uma frase.
2. Escolhe ferramenta:
   - `monte_carlo` — define variável-alvo, distribuições, 10k iterações.
   - `swot` — nomeia S/W/O/T com peso 1 a 5 cada; score = soma ponderada.
   - `cenarios` — eixos X e Y, 4 quadrantes com implicações por agente.
3. Produz artefato JSON com: pergunta, método, inputs, output, confiança,
   recomendação.
4. Artefato é linkado ao desafio e pode ser consumido por Helena via
   `POST /api/vila/simular-decisao` se marcado como estratégico.

Critérios normativos:
- Relatório rejeitado se não nomear pelo menos dois cenários plausíveis.
- Confiança abaixo de 50 por cento exige alerta explícito ao solicitante.
- Reuso: artefato vira memória semântica após 3 citações.

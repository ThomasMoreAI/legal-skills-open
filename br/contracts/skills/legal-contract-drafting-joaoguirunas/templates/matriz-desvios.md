---
kind: reference
status: rascunho
summary: "Matriz de desvios {contrato-slug} v{N}: {T} cláusulas, {K} desvios ({J} aprovados, {I} pendentes), {Z} inegociáveis tocados"
title: "Matriz de desvios — {contrato-slug} v{N}"
agent: legal-drafter
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
tags: [legal, drafting, desvios, v{N}]
related: ["[[{contrato-slug}-v{N}]]", "[[../architecture/model-system]]", "[[../../project/legal-posture]]", "[[../strategy/validations]]"]
---

# Matriz de desvios — {contrato-slug} v{N}

> 100% das cláusulas, uma linha cada. `DESVIO` sem aprovador = minuta não vai a gate. Inegociável alterado só com decisão escrita do usuário.

## Resumo
Cláusulas: {T} · `= modelo`: {a} · `variante` dentro do piso/teto: {b} · `DESVIO` aprovado: {c} · `DESVIO` pendente: {d} · Inegociáveis tocados: {e}

## Matriz
| Cláusula | Título | Origem (M{N}.{c}.{p/vk} / postura § / fonte) | Status | O que desvia | Motivo | Pedido por | Aprovado por | Data |
|---|---|---|---|---|---|---|---|---|
| 1 | Qualificação | brief | = modelo | — | — | — | — | |
| 6 | Preço | brief · M{N}.6.v2 | variante | prazo de pagamento {x} dias | | contraparte | CONCORDIA (dentro do teto) | |
| 11 | Limitação | postura §{z} | DESVIO | teto {y}× mensalidade | | contraparte | {PRUDENTIA / usuário} | |

## Base legal citada
| Cláusula | Citação completa (research) | Consultado em | Vigência |
|---|---|---|---|

## Prazos e obrigações para FIDES
| Cláusula | O quê | Data / gatilho | Dono |
|---|---|---|---|

## Changelog desta versão
v{N} — {data} — {mudanças} — origem: {…}

## Gate
PRUDENTIA: {APROVADA / AJUSTES / REPROVADA} — {data} — validations.md · IUSTITIA: {pendente / PASS / CONCERNS / FAIL} — {data} — results.md

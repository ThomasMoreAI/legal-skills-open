---
name: lgpd-incident-response-goul4rt
title: Incident Response LGPD
description: Execute the LGPD security incident response runbook (Art. 48 LGPD + Resolução CD/ANPD nº 15/2024). Use when user says "tivemos um incidente", "vazamento de dados", "data breach", "preciso comunicar a ANPD", "incident response LGPD", or as part of an audit pipeline preparing the runbook in advance. Encodes the 3-business-day deadline to notify ANPD and data subjects, the 12 mandatory items for ANPD notification, the 7 items for subject notification, and the 5-year retention requirement for ALL incident records (notified or not). Cite Resolution 15/2024 explicitly in outputs.
author: goul4rt
author_url: https://github.com/goul4rt/lgpd-skills/tree/main/skills/lgpd-incident-response
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# Incident Response LGPD

Runbook aderente à **Resolução CD/ANPD nº 15/2024 (RCIS)** + Art. 48 LGPD.

⚠️ **Esta skill tem dois modos**:
1. **Preparatório** — quando invocada no pipeline de auditoria, gera runbook + tabletop exercise para uso futuro.
2. **Emergencial** — quando invocada após incidente detectado, executa o fluxo em modo crítico.

## Critério de notificação (Res. 15/2024, Art. 5º — cumulativo)

Notificar ANPD **se e somente se ambos**:

**A. Risco/dano relevante** — pode afetar significativamente interesses e direitos fundamentais.
**B. Pelo menos uma das 6 categorias envolvidas:**
- I. Dados pessoais sensíveis
- II. Dados de crianças, adolescentes ou idosos
- III. Dados financeiros
- IV. Dados de autenticação em sistemas
- V. Dados protegidos por sigilo legal, judicial ou profissional
- VI. Dados tratados em larga escala

Se **A e B** → notificar. Se só A → documentar internamente. Se nenhum → registrar mesmo assim (Art. 10 — registro obrigatório por 5 anos de TODOS os incidentes).

## Prazos

| Ação | Prazo |
|---|---|
| Notificar ANPD | **3 dias úteis** desde o conhecimento de afetação a dados pessoais |
| Notificar titulares | **3 dias úteis** (mesmo gatilho) |
| Complementar comunicação | até 20 dias úteis após comunicação inicial |
| Manter registro do incidente | **5 anos mínimo** |
| ATPP | prazos em dobro (6 dias úteis), salvo risco à integridade física/moral |

## Runbook — Hora 0 a Hora 72+

### T+0h: Detecção
- Quem detectou? Sistema (SIEM, DLP, antivirus)? Pessoa (funcionário, titular, pesquisador)?
- **Registrar timestamp exato** do conhecimento da afetação a dados pessoais — este é o marco do prazo.
- Acionar Encarregado **imediatamente**.

### T+0h a T+4h: Contenção e triagem
- [ ] Isolar sistemas comprometidos
- [ ] Preservar evidências (snapshots, logs, dumps)
- [ ] Suspender propagação (revogar tokens, fechar buckets, bloquear rotas)
- [ ] Não destruir nada — perícia precisa
- [ ] Comunicação interna restrita (need-to-know)
- [ ] Acionar provedores de cloud / operadores se relevante

### T+4h a T+24h: Avaliação
- [ ] Categorias de dados afetadas
- [ ] Número estimado de titulares afetados
- [ ] Categorias de titulares (crianças? idosos? destacar)
- [ ] Vetor de ataque ou causa raiz (preliminar)
- [ ] Aplicar **teste do Art. 5º** Res. 15/2024:
  - Risco relevante? (sim/não — justificar)
  - Categoria do Art. 5º? (qual)
- [ ] Decisão: notificar ANPD? notificar titulares? Documentar decisão por escrito (Encarregado + jurídico).

### T+24h a T+72h (3 dias úteis): Comunicação

**À ANPD — 12 itens obrigatórios (Art. 6º, § 2º Res. 15/2024):**

1. Natureza e categoria dos dados pessoais afetados
2. Número de titulares afetados, **discriminando crianças, adolescentes e idosos**
3. Medidas técnicas e de segurança adotadas antes e depois do incidente
4. Riscos e possíveis impactos aos titulares
5. Motivos da demora, se houve
6. Medidas para reverter ou mitigar
7. Data do incidente e data do conhecimento
8. Dados do encarregado ou representante
9. Identificação do controlador (declaração de ATPP se for o caso)
10. Identificação do operador
11. Descrição do incidente com causa principal
12. Total de titulares cujos dados são tratados nas atividades afetadas

Canal: **portal eletrônico da ANPD** (https://www.gov.br/anpd).

**Aos titulares — 7 itens (Art. 9º Res. 15/2024):**

1. Natureza e categoria dos dados afetados
2. Medidas de segurança técnicas
3. Riscos
4. Motivos da demora, se houve
5. Medidas reversivas/mitigatórias
6. Data do conhecimento
7. Contato do encarregado

Em **linguagem simples**. Comunicação **individualizada** (e-mail/SMS/carta/mensagem in-app). Se inviável (volume + falta de contato), comunicação coletiva via site + imprensa por **mínimo 3 meses**.

Templates em `assets/notification-anpd.md` e `assets/notification-subject.md`.

### T+72h+: Pós-incidente
- [ ] Continuar mitigando
- [ ] Forense completa
- [ ] Análise de causa raiz (5 whys, fishbone, post-mortem)
- [ ] Atualizar `.lgpd/incidents/log.md`
- [ ] Plano de remediação com prazos e responsáveis
- [ ] Lições aprendidas → atualizar runbook
- [ ] Considerar pipeline `lgpd-audit` modo legacy para correções estruturais

### Complemento à ANPD (até 20 dias úteis)
Após investigação completa, complementar a comunicação inicial com informações mais precisas se algo mudou.

## Registro permanente (Art. 10 Res. 15/2024)

`.lgpd/incidents/log.md` — TODOS os incidentes, mesmo não notificados:

```markdown
# Registro de Incidentes — {projeto}

## INC-2026-001

- **Detecção**: 2026-05-15T14:30:00-03:00
- **Conhecimento de afetação a dados pessoais**: 2026-05-15T15:45:00-03:00
- **Tipo**: vazamento de e-mails
- **Categoria afetada** (Art. 5º Res. 15/2024): VI — larga escala (sim, ≥ 100k titulares)
- **Titulares afetados**: ~120.000
- **Decisão**: notificar
- **Notificação ANPD**: 2026-05-16T18:00:00-03:00 (protocolo nº ...)
- **Notificação titulares**: 2026-05-16 a 2026-05-17 (e-mail individualizado)
- **Justificativa da notificação**: risco relevante + larga escala (> 2 milhões? não, mas ANPD considera larga escala em outras métricas) — Art. 5º, VI
- **Medidas adotadas**: rotação de credenciais, revogação de tokens, patch
- **Causa raiz**: bug em endpoint que retornava lista de e-mails sem auth
- **Plano de remediação**: ADR-2026-08 (auth obrigatória em todos endpoints /api/users/*)
- **Retenção do registro**: até 2031-05-15 (5 anos)
```

## Tabletop exercise (preparatório)

Executar 1x por ano no mínimo. Cenários sugeridos:

1. **Vazamento de e-mails via endpoint mal configurado** (probabilidade alta)
2. **Acesso indevido por funcionário com privilégios excessivos** (insider)
3. **Comprometimento de cloud provider** (operador)
4. **Ransomware com exfiltração**
5. **Bug em pipeline de analytics que envia PII para Datadog**
6. **Vazamento via SDK mobile (token leak no app store)**

Para cada cenário: simular a triagem, decisão de notificar, e tempo até comunicação. Cronometrar. Se > 3 dias úteis, processo está quebrado.

## Status update

```markdown
## F9 — Incident response ✓
- Runbook publicado em `.lgpd/incidents/runbook.md`
- Templates de notificação em `.lgpd/incidents/templates/`
- Registro inicializado em `.lgpd/incidents/log.md`
- Tabletop agendado para {data}
- Encarregado e jurídico cientes do fluxo
- Próximo: lgpd-ropa (greenfield) ou lgpd-privacy-policy (legacy)
```

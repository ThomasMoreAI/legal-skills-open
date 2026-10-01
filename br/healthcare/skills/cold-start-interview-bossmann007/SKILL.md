---
name: cold-start-interview-bossmann007
title: /health-medical-legal:cold-start-interview
description: Entrevista de primeira execução que escreve `~/.claude/plugins/config/claude-for-legal/health-medical-legal/CLAUDE.md`. Use na primeira invocação do plugin ou quando quiser reconfigurá-lo.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/health-medical-legal/skills/cold-start-interview
license: Apache-2.0
version: 0.1.2
execution_mode: open
jurisdiction: br
practice: healthcare
language: pt
---

# /health-medical-legal:cold-start-interview

Breve entrevista conversacional (5–10 minutos, conforme detalhamento desejado). Aprende seu contexto prático: você é provider, advogado de paciente, compliance, solo? Quais são seus maiores riscos? Quem aprova escalações?

Escreve o resultado em `~/.claude/plugins/config/claude-for-legal/health-medical-legal/CLAUDE.md` — um arquivo em português que cada skill do plugin lê antes de fazer análise.

## Workflow

1. **Ask role and practice setting.** Solo healthcare lawyer? In-house counsel for clinic/hospital? Advogado de paciente em disputa de cobertura?
2. **Ask jurisdiction.** Primary state, if multistate or federal footprint, relevant regulatory contacts.
3. **Ask pain points.** What's the one thing that keeps you up at night? (Malpractice exposure, privacy compliance, insurance denials, regulatory scrutiny?)
4. **Ask escalation chain.** Who approves different types of decisions? Thresholds?
5. **Ask about data / integrations.** Where are your case files? Can you access JusBrasil or Escavador?
6. **Write the config.** Template in memory; fill in responses; write to `~/.claude/plugins/config/claude-for-legal/health-medical-legal/CLAUDE.md`.

Keep it **conversational** and **short**. This is a scaffold, not a questionnaire. If the user says "provider-side malpractice work," don't make them fill in 20 fields — ask 3 follow-ups and move on.

## What this skill does not do

- Create a case file or matter workspace. (That happens in downstream skills when a matter is triaged.)
- Set up integrations. (User does that separately if they want JusBrasil / Escavador access.)
- Produce legal analysis. (This skill only writes the config.)

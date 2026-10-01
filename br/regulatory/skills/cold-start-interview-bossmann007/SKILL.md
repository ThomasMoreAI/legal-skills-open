---
name: cold-start-interview-bossmann007
title: 'Cold Start: Banking & Fintech Legal Practice Interview'
description: Entrevista conversacional breve (5-10 minutos) que aprende como sua equipe opera em banking/fintech/cripto — estrutura organizacional, produtos, reguladores, limites de risco — e escreve seu perfil de prática em CLAUDE.md.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/banking-fintech-legal/skills/cold-start-interview
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: regulatory
language: pt
---

# Cold Start: Banking & Fintech Legal Practice Interview

## Purpose

Your first time using this plugin, it interviews you conversationally (no forms, no jargon) to learn your practice — how your team is structured, what products you handle, which regulators matter, where the risk ceiling is. Once. Then every skill in this plugin reads that profile before doing work.

If you're re-running (you've onboarded new people or shifted product focus), pass `--redo` to re-interview.

## The interview

This is a conversation, not a survey. I'll ask ~5-8 open questions. Your answers populate `~/.claude/plugins/config/claude-for-legal/banking-fintech-legal/CLAUDE.md` — a living document you edit directly when things change. You don't fill out a form; you tell me how your team actually works.

**I'll ask about:**

1. **Your organization** — name, type (banco, fintech, exchange, custody, etc.), size, who's the GC/lead counsel
2. **What you do** — products (credit, payments, Pix, crypto, staking, etc.), customer segments (retail, corporate, etc.)
3. **Regulators** — who watches you (BCB, CVM, ANPD, others)
4. **Risk appetite** — what thresholds trigger escalation, what's automatic to the GC
5. **The thing that hurts** — in your own words, what's the worst problem that lands on your desk

That's it. Your answers feed the playbook sections in CLAUDE.md — interest caps, VASP classification rules, Open Finance consent models, etc. When you don't have a position on something yet, that stays blank in the template; skills will ask you to fill it in as needed.

## What you get

After the interview:

- **CLAUDE.md populated** with your team profile, risk appetite, and skeleton playbook. Not comprehensive — meant to be filled in as you work.
- **Each skill knows your context** — when you run `/banking-fintech-legal:payment-institution-compliance`, it doesn't ask "what type of institution are you" because it already read CLAUDE.md.
- **Edited, not auto-filled.** The document is yours. Change a threshold? Edit the file. No re-interview needed.

---

*Interview takes ~5-10 minutes. Start with: `/banking-fintech-legal:cold-start-interview`*

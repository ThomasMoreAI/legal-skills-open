---
name: ceet-legal-compliance
title: CEET — Legal / Compliance
description: Cognitive Extraction Engine for in-house legal counsel and compliance leads in software companies. Use when a user wants to clone a legal/compliance operator's judgment — how they review contracts, weigh risk, respond to regulatory questions, draft policy, and advise the business. Trigger on phrases like "extract my legal thinking", "clone our GC", "build an AI that reviews contracts like me", "interview me about compliance", "capture my risk framework", "make a legal cognitive clone". Outputs are tool-agnostic.
author: CMolG
author_url: https://github.com/CMolG/cognitive-skills/tree/main/ceet-legal-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# CEET — Legal / Compliance

## What this skill does

Interview an in-house legal counsel, compliance lead, DPO, or legal operations lead. Produce a cognitive clone and AI environment that reviews contracts, drafts policies, and assesses risk in their style.

## When to use

- The user wants an AI that does *first-pass* contract review, policy drafting, or regulatory triage in their voice.
- A GC wants their judgment scaled across a team or product partners.
- A founder wants legal instincts captured before hiring in-house.

**Important:** The output is not a substitute for legal advice. It is a reasoning style. The AI environment generated should always flag matters for human counsel on final decisions.

## Run order

1. **Read** `interview/questions.md`.
2. **Extract** themes, with a bias toward **risk posture** — the spectrum from paranoid to business-forward.
3. **Ask for redline examples** — how they mark up a standard DPA, MSA, or customer agreement.
4. **Synthesize** into the role-specific `templates/cognitive-profile.md`.
5. **Activate** into the role-specific `templates/` directory. Save to `templates/`.
6. **Hand off** via [`../docs/tool-integration.md`](../docs/tool-integration.md).

## Legal-specific things to listen for

- **Risk posture.** Where on the paranoid↔business-enabling spectrum.
- **Contract playbook.** Standard markup positions on liability, indemnity, IP, warranty, termination, auto-renewal.
- **Escalation criteria.** What they handle, what goes to outside counsel, what must go to a partner.
- **Regulatory frameworks in scope.** GDPR, CCPA, HIPAA, SOC 2, DORA, AI Act, state-by-state US.
- **Privacy stance.** Data minimization, consent, DPAs, sub-processor discipline.
- **Policy drafting voice.** Terse, narrative, example-driven?
- **Risk register approach.** What risks get tracked, how often revisited.
- **Business partnership stance.** How they frame "no" as "yes, if…"
- **IP hygiene.** Open-source license review, employee IP, customer data use.
- **Disputes & incident response.** Breach notification, security incident legal flow.

## Synthesis guardrails

- Capture their **standard redline positions** as a reusable playbook.
- Include a **disclaimer block** in the AI environment — the AI is reasoning in their style, not providing legal advice.
- Note the jurisdictions they actually practice in and where they *don't* opine.
- Save outputs to `templates/`.

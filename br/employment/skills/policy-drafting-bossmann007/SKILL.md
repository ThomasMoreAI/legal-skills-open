---
name: policy-drafting-bossmann007
title: 'Policy drafting'
description: Draft an employment policy with regional supplements where CCTs (Convenções Coletivas de Trabalho) or local rules differ across the company's territorial footprint. Use when the user says "draft a [topic] policy", "we need a policy on", "update our [topic] policy", or names a policy gap.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/employment-legal/skills/policy-drafting
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: employment
language: en
---

# /policy-drafting

1. Load `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdictional footprint, handbook location.
2. Use the workflow below.
3. Draft core policy. Check each base territorial/CCT in footprint for required variants.
4. Output: core policy + suplementos por base/CCT. Flag where law or CCT is currently shifting (data-base próxima, negociação em curso).

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

A CLT rege o país inteiro, mas a política certa para uma base sindical pode estar errada (ou incompleta) em outra: cada CCT tem piso, jornada, adicionais e benefícios próprios, e a data-base muda por categoria. This skill drafts a core policy (CLT + regulamento interno) and generates supplements where a CCT or local rule requires different terms.

## Load context

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdictional footprint, handbook location and format.

## Workflow

### Step 1: Scope the policy

- What's the policy for? (Remote work, parental leave, social media, etc.)
- Why now? (Legal requirement, incident, growth, gap noticed)
- Who does it apply to? (All employees, certain roles, certain locations)

### Step 2: Varredura por base territorial / CCT

For each base sindical (and country, if there are expatriados) in the footprint, check: does the applicable CCT or local rule have a specific clause on this topic?

**Common topics with CCT/regional variance (BR):**

| Tema | Variância |
|---|---|
| Piso salarial e reajuste | Cada CCT define piso e data-base próprios — a política salarial core não pode contrariar o piso da base |
| Banco de horas / compensação | CLT art. 59 permite acordo individual (6 meses) ou coletivo (1 ano); CCTs frequentemente restringem ou detalham | [verified: https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm]
| Vale-refeição / benefícios | Muitas CCTs tornam obrigatórios benefícios que a CLT não exige |
| Teletrabalho | CLT arts. 75-A a 75-E + cláusulas de CCT sobre custeio de infraestrutura |
| Adicional de horas extras | Mínimo constitucional 50% (CF art. 7º, XVI); CCTs frequentemente fixam 60–100% |
| Licença-maternidade/paternidade estendida | Empresa Cidadã (Lei 11.770/2008) se aderente; CCTs podem ampliar |
| Estabilidades provisórias | Gestante, CIPA, acidentária, pré-aposentadoria (esta última é criatura de CCT — verificar cada base) |
| Homologação de rescisão | Algumas CCTs ainda exigem assistência sindical mesmo após a Reforma (Lei 13.467/2017) |

If the topic has no CCT/regional variance (dress code, say), skip this step.

### Step 3: Draft the core policy

One policy. Applies everywhere. Clear and readable — employees should understand it without a lawyer.

Structure:
- Purpose (one sentence — why this policy exists)
- Scope (who it applies to)
- The rule (what's required/permitted/prohibited)
- Process (how to request, who approves, what happens if)
- Questions (who to ask)

Avoid: "heretofore," "notwithstanding," nested exceptions. This is a handbook policy, not a contract.

### Step 4: Suplementos por base territorial / CCT

For each base where the rule differs, a supplement:

```markdown
### Suplemento — [Base sindical / CCT]

Empregados abrangidos pela [CCT X, vigência YYYY–YYYY] estão sujeitos ao seguinte, em acréscimo / em substituição à política core:

- [Diferença específica]
- [Cite a cláusula da CCT ou a norma, se ajudar]
```

Keep supplements tight. Only what's different — don't repeat the core.

### Step 5: Cross-check

- Does this policy conflict with anything already in the handbook?
- Does it promise more than the company intends to deliver? (No Brasil, benefício concedido habitualmente adere ao contrato de trabalho — CLT art. 468 e Súmula 51 TST vedam alteração lesiva. Uma política generosa demais é difícil de reverter.)
- Does it conflict with the applicable CCT? (Norma coletiva prevalece sobre o regulamento interno naquilo que for mais benéfica ao empregado.)

## Output

```markdown
# [Policy Name]

## Core Policy

[Full text]

## Suplementos por Base / CCT

### [Base 1]
[Supplement]

### [Base 2]
[Supplement]

---

## Drafting Notes (internal — remove before handbook insertion)

- **Varredura por base/CCT:** [which bases/CCTs checked, which have variance]
- **Conflicts with existing handbook:** [none | list]
- **Law/CCT currently shifting:** [any base with data-base or negociação coletiva in flux]
- **Review cadence:** [when to revisit — annual, or when X happens]
```

> **Draft, not a policy in effect.** This is a drafting aid for attorney review, not a policy you can publish. Publishing a handbook policy has legal consequences — in several states it can bind the company as a contractual promise, and wage/leave/accommodation policies are routinely read against the employer. A licensed attorney, solicitor, barrister, or other authorised legal professional in your jurisdiction reviews, edits as needed, and takes professional responsibility before the policy is rolled out. Do not publish or distribute this draft unreviewed.

## Handoff

To handbook-updates skill: when this policy is approved, it diffs against the current handbook and flags what changes.

## What this skill does not do

- Approve the policy. It drafts; a human approves.
- Roll out the policy. Communication to employees is an HR workflow.
- Cover every jurisdiction on earth — only the ones in the footprint. If the footprint expands, re-run.

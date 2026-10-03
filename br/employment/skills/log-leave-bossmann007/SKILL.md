---
name: log-leave-bossmann007
title: 'Log leave'
description: Add a new leave to the leave register with the minimum information needed to start tracking deadlines. Use when an employee goes on leave and you want the tracker to watch designation, certification, and exhaustion clocks from day one.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/employment-legal/skills/log-leave
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: br
practice: employment
language: pt
---

# /log-leave

Adds a new leave entry to `~/.claude/plugins/config/claude-for-legal/employment-legal/leave-register.yaml` with the minimum
information needed to start tracking deadlines. Use when an employee goes on
leave and you want the tracker to watch the clocks from day one.

## Instructions

1. Read `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → jurisdiction table and Systems section.

2. Ask all of the following in a single prompt — do not drip them one at a time:

   > A few quick questions to set up leave tracking:
   >
   > - Employee name or role (anonymized is fine)
   > - Base territorial/CCT (município/sindicato — determines which collective-bargaining clauses apply, if any)
   > - Leave type: licença-maternidade (120 dias, CF art. 7º XVIII / 180 dias se empresa aderente ao Programa Empresa Cidadã, Lei 11.770/2008) / licença-paternidade (5 dias, CF art. 10 ADCT / 20 dias Empresa Cidadã) / auxílio-doença ou acidentário (empresa paga dias 1-15; INSS a partir do 16º dia) / licença para acompanhamento de dependente / outra (especificar)
   > - Leave start date
   > - É afastamento intermitente ou contínuo?
   > - Expected return date (if known — leave blank if not)
   > - Atestado médico recebido? Se sim, quando, e por quantos dias?
   > - Afastamento já comunicado ao eSocial/INSS (obrigatório a partir do 15º dia)? Se sim, quando?

   Note the structural difference up front if not already obvious to the user: Brazil's leave regime is federal and statute-driven (CLT + Lei 11.770/2008 + benefícios INSS) — there is no jurisdiction lookup by state as under FMLA/US state leave; entitlement is fixed by leave type, and by day-count for illness leave.

3. Determine which regime governs and for how long, based on leave type:
   - Licença-maternidade/paternidade: fixed statutory duration (120/180 or 5/20 dias) — no case-by-case entitlement lookup needed.
   - Auxílio-doença/acidentário: employer pays days 1-15 (salário integral); INSS pays from day 16 if perícia médica confirms incapacity beyond that.
   - Other CLT-specific leaves (nojo, gala, doação de sangue etc.) — duration under CLT art. 473 `[model knowledge — verify]`.

4. Compute the first upcoming deadline based on the information provided:
   - Illness leave approaching day 15, no eSocial/INSS communication yet → deadline is submitting the afastamento before day 15 ends (closes employer's paid-leave window)
   - Atestado received but perícia médica (INSS) not yet scheduled → flag as next action
   - Maternity leave already running → next checkpoint is the return date and the estabilidade provisória window (CF art. 10 ADCT — until 5 months after childbirth)

5. Write a new entry to `~/.claude/plugins/config/claude-for-legal/employment-legal/leave-register.yaml` using the leave register
   format from the leave-tracker agent. If the file doesn't exist, create it.

6. Confirm with a single line:
   > "Logged. [Employee/Role] — [Leave type] — [Base territorial/CCT] — started [date].
   > First deadline: [what it is and when]. Leave tracker will alert automatically."

## Examples

```
/employment-legal:log-leave
```

```
/employment-legal:log-leave
Sarah (Sr. Engineer, works in São Paulo) just started licença-maternidade
today. Empresa aderente ao Programa Empresa Cidadã (180 dias). Atestado
médico já recebido.
```

---
name: tese-vinculante-checker-bossmann007
title: /tese-vinculante-checker
description: 'Antes de protocolar, estrutura uma verificação da tese jurídica contra autoridade vinculante e persuasiva que poderia suspender ou derrotar o caso: súmulas vinculantes STF, súmulas STJ/STF, temas de repercussão geral (STF) e recursos repetitivos (STJ). Identifica risco de sobrestamento nacional (CPC art. 1.037 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]) e IRDR local (CPC arts. 976-987 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]). Não asserta existência de súmula sem fonte. Estrutura protocolo de pesquisa (o que buscar em JusBrasil/STF/STJ) e interpreta resultados. Output: por tese, existe autoridade vinculante a favor/contra, há risco de sobrestamento ativo, recomendação.'
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/litigation-legal/skills/tese-vinculante-checker
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# /tese-vinculante-checker

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, decision posture, jurisdiction.
2. If matter workspaces enabled, confirm or select the active matter; load `matter.md`.
3. Interview the user to capture thesis description, side, jurisdiction, phase.
4. Structure binding-authority research protocol.
5. Produce checklist; guide user through search sources.
6. Interpret results user pastes back.
7. Output per thesis: binding authority status, sobrestamento risk, recommendation.

---

# Tese Vinculante — Verificação Pré-Protocolo

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/litigation-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` — pleaded claims, side, jurisdiction, applicable theory. Write outputs to the matter's `case-analysis/` folder if a matter is active; otherwise the practice-level `case-analysis/` folder.

---

## Purpose

A central legal thesis lives or dies on whether a superior court has already ruled against it, or is about to hold it against you nationally while your case is pending. This skill surfaces binding and persuasive authority **before** filing. Filing into a súmula vinculante that contradicts your thesis, or into an active IRDR on the identical issue, or while a tema de repercussão geral is pending before the STF, means the case is dead — or will be suspended while the higher court rules — before service.

---

## Jurisdiction assumption / Premissa de jurisdição (Brasil)

Brazilian appellate authority comes in binding (vinculante) and persuasive (persuasiva) tiers:

**Binding:**
- **Súmula Vinculante STF** (Lei 11.417/2006 [verified: https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11417.htm]) — applicable to lower courts and public administration under the binding-effect framework. A lower court contradicting it is reversible on appeal.
- **Temas de Repercussão Geral (STF)** (CF/88 art. 102, §3º; CPC art. 1.035 `[verified: https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm; https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]`) — when STF declares constitutional/statutory question has general repercussion, cases pending on that identical theme are typically suspended (sobrestamento) under CPC art. 1.037 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm] until STF rules.
- **Recursos Repetitivos (STJ)** (CPC arts. 1.036-1.041 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]) — when STJ marks a recurring question as "repetitive appeal," lower-court decisions are suspended pending STJ's ruling on the thesis, then applied uniformly.
- **IRDR** (CPC arts. 976-987 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]) — state (TJ) or federal (TRF) consolidation of identical theses; binds all cases in that court system on the question. Suspends pending cases while IRDR is resolved.

**Persuasive (highly influential but not binding):**
- **Súmulas STJ** (non-vinculante) — lower courts follow by practice unless strong reason to diverge.
- **Súmulas STF** (non-binding) — same persuasive weight as STJ súmulas.
- **Isolated decisions** from STF or STJ — individual holdings carry persuasive weight.

**Sobrestamento nacional (suspension):** When a tema de repercussão geral is declared pending on your exact legal question, your case in a lower court **must** be suspended — the court stays and waits for STF's ruling. If your thesis contradicts the likely STF position, your case remains suspended until you lose at the top, then must be reversed in the lower court.

---

## Load the playbook / Load context

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → role, decision posture, jurisdiction.
- Active matter's `matter.md` — pleaded claims, side, jurisdiction, phase.
- The **thesis as pleaded** — user's statement of the central legal question.

---

## Workflow

### Step 1: Interview and thesis capture

Ask the user:

> **Qual é a tese jurídica central do seu caso?**
>
> Descreva em uma frase: qual é o ponto jurídico que você está alegando?

Confirm:
- **Side:** [plaintiff | defendant]?
- **Jurisdiction:** Which court (TJSP / TJRJ / Justiça Federal, TRT, etc.)?
- **Phase:** Pre-filing or already pleaded?

### Step 2: Structure the research protocol

Issue a checklist for the user:

> **Part A: STF (Binding themes & non-binding súmulas)**
>
> 1. Go to www.stf.jus.br → Portal de Jurisprudência.
>    - Search: "tema de repercussão geral [your thesis keywords]"
>    - **If found:** Copy the theme number, ruling date, and thesis as stated by STF.
>    - **Your case will be automatically suspended if the theme is unresolved.**
>
> 2. Go to www.stf.jus.br → Súmulas Vinculantes.
>    - Search: keywords from your thesis.
>    - **If found:** Copy the súmula number and exact text.
>    - **Your case contradicts binding law if a vinculante súmula directly contradicts your thesis.**
>
> 3. Go to JusBrasil (www.jusbrasil.com.br) → search "STF [your thesis keywords]"
>    - Look for recent isolated decisions on your question.
>    - Report the case name, date, and holding.
>
> **Part B: STJ (Binding repetitive appeals & persuasive súmulas)**
>
> 4. Go to www.stj.jus.br → Portal de Jurisprudência.
>    - Search: "recurso especial repetitivo [keywords]"
>    - **If found:** Copy the lead appeal number, thesis, and status.
>    - Search: "súmula [keywords]"
>    - Copy súmula number and text.
>
> 5. Go to JusBrasil → search "STJ [keywords]"
>    - Report recent isolated decisions.
>
> **Part C: Local (TJ/TRF) — IRDR and local súmulas**
>
> 6. Go to the **specific TJ or TRF** portal (e.g., www.tjsp.jus.br, www.trf1.jus.br).
>    - Search: "IRDR [your thesis keywords]"
>    - **If found:** Copy the case number and status.
>    - Search: "súmula [keywords]"
>    - Report any local súmula.
>
> 7. Go to Escavador or JusBrasil.
>    - Search: "[your tribunal] [your thesis keywords]"
>    - Report recent local decisions.

---

### Step 3: Interpret results

For each authority found, apply:

**Question 1: Is it binding?**
- ✅ Binding = Súmula Vinculante STF, active Tema de Repercussão Geral (unresolved), active Recurso Especial Repetitivo (unresolved), active IRDR in your local court.
- ⚠️ Persuasive = Súmula STJ/STF (non-vinculante), isolated STF/STJ decisions, local TJ/TRF súmulas and decisions.

**Question 2: Support or contradict?**
- ✅ **Supports** — authority aligns with your thesis.
- ❌ **Contradicts** — authority conflicts directly.
- ❓ **Ambiguous** — authority is on related but not identical question.

**Question 3: Procedural consequence if binding?**
- **Súmula Vinculante STF contradicts:** Case is dead. Do NOT file. Lower court must follow the súmula.
- **Unresolved Tema de Repercussão Geral:** Case may be suspended under CPC art. 1.037 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm] when filed, depending on the affected issue and tribunal handling. Remains suspended until the binding issue is resolved. Filing now may lock you into suspension.
- **Active Recurso Especial Repetitivo:** Case suspended at STJ level. Thesis applied uniformly once decided.
- **Active IRDR in your local TJ/TRF:** Case suspended until IRDR is resolved. Local-level effects only.

**Question 4: Risk summary**
- 🔴 **Blocking:** Súmula vinculante STF directly contradicts your thesis. Filing is malpractice.
- 🟠 **High — sobrestamento pending:** Unresolved tema, repetitive appeal, or IRDR on your exact thesis is active. Case will be suspended; likely defeat if higher court rules against you.
- 🟡 **Medium — persuasive authority hostile:** No binding authority, but recent STF/STJ decisions contradict your thesis. You have a path to file, but weight of authority is against you.
- 🟢 **Low:** No binding authority, mixed or no persuasive authority. Argumentative freedom.

---

## No silent supplement

If the user reports searches returned no results, and you are aware (from training knowledge) that binding or persuasive authority might apply, do NOT silently insert it. Instead, flag it:

> "You searched [sources] and found no binding authority on this thesis. I am aware (from training knowledge) that [general area] may have recent developments `[model knowledge — verify]`. Options:
> 1. Broaden the search on JusBrasil/STF/STJ portals and re-paste.
> 2. I'll flag this as `[model knowledge — verify]` and proceed, noting you should do a targeted secondary search.
> 3. Stop here and consult an appeals specialist.

---

## Consequential-action gate

**Who's using this?** If Role is Non-lawyer:

> This analysis is a research draft, not a legal opinion. A licensed attorney in your jurisdiction must review the binding-authority research and risk assessment before making a filing decision. Risk flags (especially 🔴 and 🟠) require attorney judgment and client communication.
>
> Here's a one-page brief for an attorney:
> - **Thesis:** [user's thesis]
> - **Jurisdiction:** [tribunal]
> - **Binding authority found:** [list]
> - **Persuasive authority found:** [list]
> - **Risk flag:** [color]
> - **Open questions:** [any gaps]

---

## What this skill does not do

- **It does not opine on the merits.** This assesses binding/persuasive authority on your thesis, not whether it's ultimately correct or defensible.
- **It does not substitute for full case assessment.** This is a pre-filing binding-authority check only.
- **It does not provide real-time updates.** Search results are current as of the moment searched. Binding authority status can change as courts rule. Before filing, re-check any theme, repetitive appeal, or IRDR found.
- **It does not file anything.** All output is risk assessment for attorney review.
- **It does not replace appeals specialist consultation.** If an active theme or repetitive appeal touches your case, consult an appeals specialist on timeline and strategy.

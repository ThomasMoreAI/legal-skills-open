---
name: medical-liability-defense
title: /health-medical-legal:medical-liability-defense
description: Triagem de ação por erro médico e estruturação de defesa. Análise de obrigação de meio vs. resultado, culpa, nexo causal, qualidade de consentimento informado, quesitos para perícia, defesa estratégica. Use quando receber demanda por erro médico ou consulta de médico/hospital sobre risco.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/health-medical-legal/skills/medical-liability-defense
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: healthcare
language: en
---

# /health-medical-legal:medical-liability-defense

Triage de ação por erro médico. Não é parecer de mérito final — é leitura estruturada para triagem, com recomendações de estratégia defensiva.

Cobre:
1. Identificação da alegação (diagnóstico incorreto? Erro cirúrgico? Falta de consentimento? Abandono?)
2. Padrão de cuidado (era um padrão de meio ou resultado? Qual é o padrão vigente?)
3. Culpa sob CC Arts. 186/927/951 [modelo conhecimento — verificar].
4. Nexo causal (a conduta causou o dano? Há eventos intermediários que quebram a cadeia?)
5. Qualidade do termo de consentimento informado (estava adequado? Documentado?)
6. Quesitos para perícia médica (o que perguntar ao perito?).
7. Responsabilidade solidária do hospital (Lei 9.656 se envolver operadora [modelo conhecimento — verificar], ou Código Civil/CDC se consumidor [modelo conhecimento — verificar]).
8. Defesa estratégica (quais são nossas melhores defensivas? Ordem de prioridade?).

**Output:** triage rating (forte, debatível, fraco), matriz de defensivas, recomendação de postura, quesitos sugeridos para perícia.

---

## Matter context

Check `## Matter workspaces` in CLAUDE.md. If enabled, load active matter context and write outputs to matter folder. If not enabled, write to `~/.claude/plugins/config/claude-for-legal/health-medical-legal/inbound/` with date slug.

---

## Purpose

Medical malpractice claims have a specific anatomy: allegation of breach of standard of care, causation, and damages. This skill reads the demand or complaint, maps the anatomy, and surfaces which pieces are weak.

A triage read, not an opinion. The team decides whether to fight, settle, or watch.

---

## Premissa de jurisdição (Brasil)

**Responsabilidade civil por erro médico — Código Civil (Lei 10.406/2002) Arts. 186–405:**
- **Art. 186:** Quem causa dano a outrem fica obrigado a repará-lo.
- **Arts. 389–405:** Obrigação de meio vs. resultado. A maioria das obrigações médicas são de **meio**, não resultado — o médico se obriga a usar diligência e conhecimento, não a curar [modelo conhecimento — verificar]. Exceção: algumas intervenções (cirurgia estética, implante com garantia) podem ser de resultado.
- **Art. 927:** Culpa (negligência, imprudência, imperícia) é elemento necessário [modelo conhecimento — verificar].
- **Arts. 951:** Profissional liberal responde por culpa [modelo conhecimento — verificar].

**CDC (Lei 8.078/1990) — se paciente é consumidor:** [statute]
- Médico/hospital são fornecedores. Paciente é consumidor se destinatário final do serviço.
- Art. 6º: direitos de consumidor (segurança, informação clara).
- Art. 20–22: serviços com defeito; responsabilidade objetiva se dano [modelo conhecimento — verificar].

**Lei 9.656/1998 — se operadora de saúde está envolvida:**
- Operadora tem obrigação de cobertura conforme rol (Lei 14.454/2022 — rol é exemplarivo, não exaustivo [modelo conhecimento — verificar]).
- Negativa de cobertura pode gerar ação contra operadora paralelamente à ação contra médico/hospital.

**Sigilo médico — inviolável:**
- Informação de paciente é confidencial. Sigilo do advogado: Estatuto OAB Art. 7º (inviolabilidade no exercício da advocacia) [verified: https://www.planalto.gov.br/ccivil_03/leis/l8906.htm]. Dever de sigilo médico: Código de Ética Médica (Res. CFM 2.217/2018, arts. 73-79) `[verified: https://sistemas.cfm.org.br/normas/visualizar/resolucoes/BR/2018/2217]`; e Código Penal Art. 154 (violação de segredo profissional) [model knowledge — verify].
- Pronunciamento público sobre diagnóstico / tratamento do paciente é violação de sigilo.

---

## Step 1: Extract the allegation

Se é demanda judicial, extrair:
- **Demandante:** paciente ou familiar?
- **Demandados:** médico? Hospital? Ambos?
- **Alegação específica:** o quê diz que deu errado?
- **Prazo:** quando ocorreu? Quando demanda foi ajuizada? Prazo prescricional é issue? [modelo conhecimento — verificar]
- **Danos:** quanto pedem?
- **Ato específico:** qual conduta alegam?

---

## Step 2: Standard of care analysis

Standard of care = what a reasonably competent professional in the same specialty, in the same location, at the same time, would have done [modelo conhecimento — verificar].

**Questions:**
- What treatment options existed at time of treatment?
- What does current literature say?
- Did defendant follow any published guideline?
- Would another reasonably competent professional have done the same?

---

## Step 3: Culpa (negligence, imprudence, lack of skill)

1. **Duty:** Professional has duty to exercise reasonable care. (Established.)
2. **Breach:** Did professional deviate from standard?
   - **Negligência:** breach of duty, lack of attention
   - **Imprudência:** recklessness
   - **Imperícia:** lack of skill
3. **Causation:** Did breach cause harm?
4. **Damages:** What is the quantifiable loss?

Flag each where evidence is weak.

---

## Step 4: Nexo causal (causation)

Causation breaks if:
- Intervening event severs causal chain
- Harm was inevitable regardless
- Harm is speculative or too remote

Look for intermediate events that weaken causation.

---

## Step 5: Informed consent assessment

**Elements:**
- **Capacity:** Patient was competent
- **Disclosure:** Material risks, alternatives, prognosis disclosed in understandable language
- **Comprehension:** Evidence patient understood
- **Voluntariness:** No coercion

**Red flags:** No consent form, generic boilerplate, no evidence of discussion, incapacitated patient, no reference to alternatives.

---

## Step 6: Suggested quesitos for perito médico

Target key questions:
1. **Standard of care:** "Qual era o padrão de cuidado esperado?"
2. **Breach:** "A conduta do médico estava conforme esse padrão?"
3. **Causation:** "Existe nexo de causalidade entre [breach] e [harm]?"
4. **Damages:** "Qual é a relação entre [diagnosis] e [claimed loss]?"
5. **Alternatives:** "Existiam outras alternativas? Qual era a probabilidade de resultado melhor?"

---

## Step 7: Responsabilidade do hospital (vicarious liability)

If hospital is defendant:
- May be liable for physician's negligence if employee
- May be independently liable for negligent credentialing, supervision, or policy
- Liability is **solidária** [modelo conhecimento — verificar].

---

## Step 8: Triage rating & defensibility

**Rating scale:**
- **🟢 Strong:** Plaintiff's case has significant weaknesses. Confident we can defend.
- **🟡 Debatable:** Standard is fact-dependent, causation is plausible but disputed. Could go either way.
- **🔴 Weak:** Breach is clear, causation is straightforward, damages are significant. High settlement/judgment risk.

Be blunt. The team needs the read.

---

## Output structure (LEAN)

```markdown
[WORK-PRODUCT HEADER]

# Triage: Medical Liability Claim — [Patient name redacted] v. [Defendant]

[⚠️ Reviewer note]

---

## The allegation

[Plaintiff's version, one paragraph. Neutral.]

## Standard of care & breach analysis

[What was expected. Did defendant deviate? How clearly?]

## Causation analysis

[Does breach explain the harm? Breaks in the chain?]

## Informed consent assessment

[Quality of documentation.]

## Triage rating

[🟢 Strong / 🟡 Debatable / 🔴 Weak — with rationale]

## Defensive strengths & weaknesses (rank-ordered)

| Defensive | Strength |
|---|---|
| 1. Standard of care | Strong / Medium / Weak |

## Quesitos for perito

[Numbered list of key questions]

## Risk assessment

- **Exposure:** [$X if we lose; settlement range $Y–$Z]
- **Insurance coverage:** [Check policy]

---

## What next?

1. **Draft responsivo** — responsive brief
2. **Escalate** — brief to GC with triage rating, exposure, decision needed
3. **Get expert opinion** — RFP to medical expert
4. **Evaluate settlement** — settlement ranges and negotiation posture
5. **Something else** — tell me
```

---

## What this skill does not do

- Produce an expert report
- Determine standard of care definitively
- Make litigation decisions
- Substitute for case strategy

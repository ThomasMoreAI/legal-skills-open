---
name: justice-intent-legal-research-sboghossian
title: Justice Intent — Legal Research
description: Use when the public-facing assistant detects that a user wants to conduct legal research — asking about the law on a topic, requesting a case summary, seeking statute interpretation, or asking what the rules are in a specific jurisdiction. Routes to the appropriate research skill or capability and frames the accessibility-oriented response for users who may be self-represented. Covers all MENA and secondary jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/justice/justice-intent-legal-research
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Justice Intent — Legal Research

## When to use this

Trigger when the message indicates the user wants information about the law itself — not how to use Louis, not a product question, but substantive legal content:

- "What does the law say about…?"
- "Is [action] legal in [country]?"
- "What are my rights if…?"
- "Can my employer…?", "Can my landlord…?"
- "What is the penalty for…?"
- "I need to find the law on [topic]"
- "Can you summarize [statute / decree]?"
- Direct statute references: "UAE Labor Law", "Lebanese Code of Obligations", "KSA PDPL"

Also trigger when a user is clearly self-represented (pro se) and trying to understand their legal position — the Justice accessibility mission is most active here.

## Response pattern

### Step 1: Identify jurisdiction

If the jurisdiction is not clear from the message, ask before proceeding — legal research without a jurisdiction is unreliable. Use the following as priority order:

1. Explicit mention ("in Lebanon", "Dubai", "Saudi Arabia")
2. Contextual signals (Iqama → KSA/UAE, kafala → LB/Gulf, lira → LB, dirham → UAE)
3. User profile / IP (if available)
4. If still unclear: ask directly ("Which country are you in? The answer may differ significantly.")

### Step 2: Route to the right research capability

| User type | Routing |
|---|---|
| **Logged-in Louis user** | Invoke the full research skill; offer a structured memo |
| **Visitor on haqq.ai** | Provide a direct, plain-language answer; offer to run a deeper research memo if they sign up |
| **Pro-se / access-to-justice user** | Plain language first; offer to draft a demand letter or complaint based on research |

### Step 3: Structure the research response

For a substantive legal research answer:

1. **Applicable law**: name the relevant statute or legal framework (do not fabricate article numbers — use well-known framework names)
2. **Rule**: state the legal rule plainly
3. **Application**: apply the rule to the user's stated facts
4. **Exceptions / caveats**: flag any common exceptions, jurisdictional variations, or enforcement gaps
5. **Next step**: what the user should do with this information (file, consult a lawyer, draft a document)

### MENA jurisdiction coverage

| Jurisdiction | Key legal sources |
|---|---|
| **Lebanon (LB)** | Code des Obligations et des Contrats (COC), Code de Procédure Civile, Code Pénal, Code de Commerce, Personal Status laws (multi-confessional), Labor Law |
| **UAE (onshore)** | Federal Civil Code (FDL 5/1985), Companies Law (FDL 32/2021), Labor Law (FDL 33/2021), Civil Procedure (FDL 42/2022), Penal Code |
| **DIFC** | DIFC Contract Law, DIFC Employment Law, DIFC Companies Law, DIFC Courts rules |
| **ADGM** | ADGM Companies Regulations, ADGM Employment Regulations, English common law base |
| **KSA** | Basic Law of Governance, Companies Law 2022, Labor Law (and 2024 amendments), PDPL 2024, AML Law, Civil Procedure Code |
| **Egypt (EG)** | Civil Code (Book 1–4), Commercial Code, Labor Law 12/2003, Companies Law 159/1981 |
| **GCC / cross-border** | GCC Model Laws, bilateral investment treaties, FATF-aligned AML frameworks |

### Accessibility rules (Justice mission)

Research responses for likely pro-se or low-income users must:
- Avoid unexplained legalese
- Explain acronyms and code names on first use
- Flag when the situation is serious enough to require a licensed lawyer ("this is a criminal matter — you have the right to counsel")
- Offer to draft any document that would help (complaint, demand letter, notice)
- Never charge for basic rights information

## Do not

- Do not fabricate statute numbers, article numbers, or case citations
- Do not give a research answer without identifying the jurisdiction
- Do not present research as legal advice to a specific case — frame as information and offer escalation to a lawyer
- Do not refuse to engage with sensitive topics (criminal, family, asylum) — these are precisely the areas where accessible legal information matters most

## Related skills

- [[justice-intent-how-to]]
- [[justice-intent-support]]
- [[justice-intent-chitchat]]
- [[justice-intent-feature-question]]

---
name: draft-recitals-builder-sboghossian
title: Recitals Builder (WHEREAS Clauses / Préambule / تمهيد)
description: Use when generating WHEREAS recital clauses (or civil-law préambule / تمهيد) for any contract. Provides the pattern for 3-7 recitals that establish parties' identities, transaction purpose, and mutual intent, followed by the formal consideration language. Adapts between common-law WHEREAS-clause format and civil-law narrative preamble traditions used in LB, FR, UAE onshore, KSA, and EG. Triggers on "recitals", "whereas clauses", "preamble", "background", or "write the opening of the contract" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-recitals-builder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Recitals Builder (WHEREAS Clauses / Préambule / تمهيد)

## When to use this

Recitals (also called "whereas clauses" in common-law drafting, "préambule" in French civil law, or "تمهيد" in Arabic) appear at the beginning of a contract, after the parties block and before the operative provisions. They set the scene, identify the parties' backgrounds and roles, state the purpose of the agreement, and establish the mutual intent.

Use this skill when:
- Starting any substantial commercial contract that needs contextual framing
- A client requests that the contract explain the "story" behind the deal
- Adding boilerplate recitals to a skeleton agreement
- Translating or adapting a common-law recital block for a civil-law jurisdiction

Note: recitals are not operative clauses. They typically do not create enforceable rights or obligations on their own (unless incorporated by reference into the operative provisions). Their primary legal function is interpretive — courts use recitals to understand the parties' intent when interpreting ambiguous operative provisions.

## When recitals matter legally

- **Ambiguity resolution**: when an operative clause is ambiguous, courts look to the recitals for context
- **Implied terms**: recitals may establish the "matrix of fact" (UK contract law) or "common intention" (civil law) that affects implied terms
- **Purpose limitation**: where a contract is made for a specific purpose stated in the recitals, that purpose can limit the scope of broader operative clauses
- **Integration clause interactions**: an entire-agreement clause prevents reliance on pre-contractual statements; recitals in the signed agreement are part of the agreement and can be relied upon

## Common-law style — WHEREAS clauses

### Pattern and structure

A standard set of 3-7 WHEREAS clauses follows this progression:

1. **Party A's identity and business** — who Party A is and what it does
2. **Party B's identity and business** — who Party B is and what it does
3. **The occasion / transaction** — what has brought the parties together
4. **The purpose** — what the parties wish to achieve
5. **Any relevant background facts** — existing relationship, prior agreements, regulatory context (if relevant)
6. **The mutual intent to formalize** — the parties wish to set out their agreement in writing
7. **Consideration bridge** — "NOW, THEREFORE..."

### Rules for WHEREAS clauses

- Each recital is a single, factual declarative sentence
- Present tense or simple past (consistent throughout)
- One idea per recital
- Do not include operative obligations in recitals
- Do not include warranties in recitals (they belong in the operative provisions)
- Do not include conditions in recitals
- 3 recitals minimum; 7 is usually the maximum before they become unwieldy

### Template

```
WHEREAS, [Party A's full name] is a [entity description — company type, jurisdiction of incorporation, and 
relevant business activity] ("Party A");

WHEREAS, [Party B's full name] is a [entity description] ("Party B");

WHEREAS, [brief description of the transaction, opportunity, or occasion that brings the parties together, 
without stating obligations];

WHEREAS, [Party A] has [relevant experience / resource / IP / right] and [Party B] has [relevant 
complementary resource] and the Parties wish to [purpose of the agreement];

[WHEREAS, [any specific background fact relevant to interpreting the agreement — prior relationship, 
regulatory approval obtained, existing license, etc.];]

WHEREAS, the Parties have agreed to enter into this Agreement to formalize their arrangement on the 
terms and conditions set out herein;

NOW, THEREFORE, in consideration of the mutual covenants, agreements, representations, and warranties 
contained herein, and for other good and valuable consideration, the receipt and sufficiency of which 
are hereby acknowledged, the Parties agree as follows:
```

### Worked examples by contract type

**NDA**:
> WHEREAS, Party A is a fintech company incorporated in DIFC that develops proprietary credit-scoring technology;
> WHEREAS, Party B is an investment fund incorporated in the Cayman Islands evaluating technology investments in the MENA region;
> WHEREAS, the Parties are exploring a potential investment by Party B in Party A;
> WHEREAS, in connection with such discussions, each Party may disclose Confidential Information to the other;
> NOW, THEREFORE...

**MSA**:
> WHEREAS, Provider is a [technology services company] specializing in [cloud implementation services] in the GCC region;
> WHEREAS, Client is a [financial institution] incorporated in KSA that requires [technology services] in connection with its operations;
> WHEREAS, the Parties wish to establish a framework under which Provider will provide services to Client pursuant to individual Statements of Work;
> NOW, THEREFORE...

**Joint Venture Agreement**:
> WHEREAS, Party A is a [construction company] with expertise in [EPC contracting] for industrial projects;
> WHEREAS, Party B is a [financial investor] with capital committed to infrastructure in the UAE;
> WHEREAS, a [government body] has issued a tender for [specific project] and the Parties wish to jointly bid for and, if successful, execute the project;
> WHEREAS, the Parties have agreed to establish a joint venture NewCo for this purpose, on the terms herein;
> NOW, THEREFORE...

## Civil-law style — Préambule / تمهيد

In French, Lebanese, Egyptian, and Arab civil-law traditions, the preamble is often written as a flowing narrative paragraph or short numbered paragraphs — not as discrete bullet-style WHEREAS clauses. This is a substantive difference: the civil-law preamble is integral to the contract's interpretive context.

### French "Préambule" pattern
```
PRÉAMBULE

La Société [Party A], société [type] au capital de [X] euros, dont le siège social est situé à 
[address], immatriculée sous le numéro [RCS reference] (ci-après « [Short Name] »),

et

La Société [Party B], [description], (ci-après « [Short Name] »),

ci-après désignées ensemble les « Parties »,

sont convenues de ce qui suit dans le cadre de [brief description of transaction context]:

[Paragraph 1]: [Background]
[Paragraph 2]: [Purpose]

En foi de quoi, les Parties ont convenu des dispositions suivantes :
```

### Arabic (اتفاقية) pattern
```
تمهيد

حيث إن [Party A] هي [وصف الكيان]؛

وحيث إن [Party B] هي [وصف الكيان]؛

وحيث إن الطرفين يرغبان في [الغرض من الاتفاقية]؛

وحيث إن الطرفين اتفقا على إبرام هذه الاتفاقية وفقاً للشروط والأحكام المبينة فيها؛

فقد اتفق الطرفان على ما يلي:
```

The above Arabic تمهيد pattern follows the same progression: identity of parties → occasion → purpose → mutual intent to formalize. The "حيث إن" (whereas / given that) construction mirrors the WHEREAS clause.

## Key differences between jurisdictions

| Feature | Common-law (US/UK/DIFC/ADGM) | Civil-law (LB/FR/UAE-onshore/EG) |
|---|---|---|
| Format | Enumerated WHEREAS clauses | Flowing narrative / numbered paragraphs |
| Operative weight | Very low — courts treat recitals as contextual | Moderate — recitals more integrated with operative provisions |
| Length | 3-7 brief clauses | 1-3 paragraphs |
| Language | "WHEREAS" / "NOW, THEREFORE" | "Préambule" / "تمهيد"; "il a été convenu ce qui suit:" |
| Consideration bridge | "NOW, THEREFORE, in consideration of..." | Not typically used (consideration doctrine applies differently) |

## Drafting standards

- Recitals should describe facts, not create obligations — "Party A manufactures X" not "Party A shall manufacture X"
- Do not include any term or condition that you want to be operative in the recitals — move it to the body
- For bilingual agreements (Arabic/English, French/English): recitals must be accurate in both languages; in case of conflict, specify which language governs (Arabic for UAE onshore; French or Arabic for LB depending on the jurisdiction)
- Match the style to the jurisdiction and the client's expectation — a DIFC-law agreement with French-style recitals is jarring

## Related skills

- [[draft-boilerplate-clauses]]
- [[draft-nda-mutual]]
- [[draft-msa]]
- [[draft-joint-venture]]

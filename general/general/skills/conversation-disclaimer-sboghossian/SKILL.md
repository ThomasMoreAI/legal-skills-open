---
name: conversation-disclaimer-sboghossian
title: Non-Legal-Advice Disclaimer
description: Use to determine when, where, and in what form to append the non-legal-advice disclaimer to legal-AI responses — including the default English text, Arabic and French localizations, when to skip it entirely (B2B lawyer personas), when to escalate to a stronger disclaimer (criminal matters, health/financial crossovers), and how to avoid disclaimer spam in extended conversations. P0 behavioral rule for the consumer-facing persona; governs all substantive legal-content responses.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/conversation/conversation-disclaimer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Non-Legal-Advice Disclaimer

## When this applies

This skill governs the disclaimer rule for **all substantive legal-content responses** on the consumer persona (`louis-twin` / B2C mode). A "substantive" response is any response that:
- Explains or interprets legal rights, obligations, or procedures.
- Describes the legal consequences of a fact pattern.
- Provides a document draft or clause suggestion.
- Advises on a legal strategy or course of action.

It does not apply to: pure chitchat, administrative responses (billing, settings), skill-selection confirmations, or pure procedural responses ("Here are your three follow-up options").

## Disclaimer text

### English (default)

> *Louis provides legal information, not legal advice. For your specific situation, consult a qualified lawyer in your jurisdiction.*

### Arabic (for Arabic-language responses or MENA users in Arabic mode)

> *لويس يوفر معلومات قانونية وليس استشارة قانونية. للحالات الخاصة، يرجى استشارة محامٍ مؤهل في اختصاصك القضائي.*

### French (for French-language responses or Francophone users)

> *Louis fournit des informations juridiques, pas des conseils juridiques. Pour votre situation particulière, consultez un avocat qualifié dans votre juridiction.*

### Multi-language responses

If the response is bilingual (English + Arabic or English + French), append the disclaimer in both languages.

## Placement

**Always a footer.** Never prepend the disclaimer to a response — it buries the content the user came for and reads as defensive. The disclaimer goes at the end, separated from the substantive content by a blank line, in italics.

Wrong:
> *Note: I'm not providing legal advice.* 
> Your employment contract may be challenged under UAE Labor Law because...

Right:
> Your employment contract may be challenged under UAE Labor Law because...
>
> ---
> *Louis provides legal information, not legal advice. For your specific situation, consult a qualified lawyer in your jurisdiction.*

## When to skip the disclaimer entirely

| Condition | Reason | Action |
|---|---|---|
| Persona is `partner`, `associate`, `in-house-counsel`, or any B2B mode | These users are qualified lawyers accessing a professional tool | No disclaimer needed; they know |
| Response is admin / billing / settings | No legal content | No disclaimer |
| Pure chitchat ("Thanks, that's helpful!") | No legal content | No disclaimer |
| User just saw the disclaimer within the last 10 turns in this conversation | Avoid disclaimer spam | Skip; user is already aware |
| Response is a question back to the user (clarifier only) | No legal content yet | No disclaimer until the substantive answer |

**Counting turns:** Reset the 10-turn clock if the topic changes significantly (e.g., the user moves from discussing an employment dispute to asking about a property transaction — that's a new context warranting a fresh disclaimer).

## When to escalate to a stronger disclaimer

### Criminal law exposure

When the user's situation involves potential criminal liability (arrest, investigation, prosecution, regulatory criminal offense), replace the standard disclaimer with the stronger criminal-defense disclaimer:

> *Louis can provide general information about criminal procedures and your rights, but this is not legal advice. If you are under investigation, have been arrested, or face criminal charges, you should speak with a qualified criminal defense lawyer immediately — time-sensitive rights apply.*

Reference skill: [[safety-criminal-defense-disclaimer]]

### Health, tax, and financial advice crossover

When a legal question bleeds into medical, financial-advisory, or tax-planning territory (e.g., "Can I sue the doctor and what will I owe in tax on a settlement?"):

> *Louis addresses the legal aspects of your question. For medical or health-related guidance, consult a qualified healthcare professional. For tax implications, consult a qualified tax adviser in your jurisdiction.*

Reference skill: [[safety-medical-tax-financial-out-of-scope]]

### Self-represented litigants

When the user identifies themselves as representing themselves in court ("I'm filing this myself, without a lawyer"):

> *Louis can help you understand procedures and prepare documents, but cannot replace legal representation. Self-represented parties face significant procedural risks. If possible, consider at least a one-hour consultation with a lawyer before filing.*

### "Lawyer for the other side" identification

If the user identifies themselves as opposing counsel or an adverse party, apply extra caution:
- Do not assist with strategy that would be harmful to the original party.
- Apply the standard disclaimer.
- Do not escalate to any form of legal-advice framing.

## Frequency management

The disclaimer should inform, not irritate. Rules:

1. **First substantive response** in any conversation: always append.
2. **Same topic, same conversation:** skip for up to 10 turns after the last disclaimer appearance.
3. **Topic change:** reset counter; append again on the first substantive response in the new topic area.
4. **Long documents** (generated contracts, drafted pleadings): append once at the end of the document. Do not interrupt the document itself with disclaimers.
5. **Follow-up answer that is short** (2–3 sentences clarifying something already said): skip — the user has already received the disclaimer in this conversation.

## Brand-voice compliance

The disclaimer must always be:
- In italics (as shown above).
- In plain language — never legalistic ("the foregoing communication does not constitute legal advice" is not allowed in the consumer persona).
- Concise — one sentence. Do not expand into a paragraph.
- In the user's language (or both languages if bilingual).

See [[messaging-bridge-line]] for the broader brand-voice rule that governs all consumer-facing communication.

## Related skills

- [[conversation-clarifying-questions]]
- [[conversation-empathy-b2c]]
- [[safety-criminal-defense-disclaimer]]

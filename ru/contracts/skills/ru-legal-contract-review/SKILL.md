---
name: ru-legal-contract-review
title: Russian Legal Contract Review
description: Use when reviewing Russian-law contracts, offers, policies, personal-data/Roskomnadzor compliance, or legal wording for Russian businesses; triggers include РФ, ГК РФ, 152-ФЗ, 149-ФЗ, РКН, ПДн, договор, оферта, NDA, SaaS, license, service agreement.
author: ni032mas
author_url: https://github.com/ni032mas/agent-skills-ru/tree/main/skills/ru-legal-contract-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ru
practice: contracts
language: en
---

# Russian Legal Contract Review

Use this skill for practical first-pass legal review under Russian realities. It is legal-risk analysis, not a substitute for a licensed lawyer's final advice.

## Current-Law Gate

Russian law and Roskomnadzor practice change often. Before giving a current legal answer, verify the applicable text live or state that the answer is not current-verified.

When the task depends on current law, cite the source, act name/number, article or clause, and редакция/date. Do not rely only on model memory or a copied old text.

Read `references/sources.md` when the user asks about statutes, Роскомнадзор, персональные данные, ГК РФ, 152-ФЗ, 149-ФЗ, 143-ФЗ, or "последние изменения".

## Intake

Identify or ask for the missing facts that change the risk analysis:

- our side: заказчик, исполнитель, продавец, покупатель, правообладатель, лицензиат, оператор ПДн, обработчик;
- counterparty status: ООО, ИП, самозанятый, физлицо, иностранная компания;
- B2B, B2C, employment, agency, license, SaaS, services, sale, marketplace, advertising, data processing;
- applicable law, jurisdiction, venue, arbitration clause, mandatory претензионный порядок;
- data flows: categories of ПДн, subjects, purposes, storage location, processors, cross-border transfer, biometrics, data allowed for dissemination;
- money and paperwork: price, НДС, withholding, currency, invoices, acts, УПД, EDI, e-signature, acceptance;
- intellectual property: exclusive/non-exclusive license, alienation, work made for hire, source code, models, content, trademarks.

If "143-ФЗ" appears in a Roskomnadzor/personal-data context, treat it as ambiguous. Clarify whether the user means 149-ФЗ, 152-ФЗ, 242-ФЗ/localization, or the actual 143-ФЗ cited in the document.

## Review Workflow

1. Check document completeness: title, parties, реквизиты, dates, exhibits, referenced policies, blank fields, signatures, attachments.
2. Classify the document and our side before calling a term "bad" or "market".
3. Map mandatory Russian-law issues with `references/checklists.md`.
4. Separate legal risk from business risk and operational risk.
5. Prefer concrete rewrites over abstract advice.
6. Mark unresolved assumptions explicitly.

## Output

For document review, use:

- `Короткий вывод`: whether it is signable, signable after fixes, or not ready.
- `Критичные блокеры`: terms that can make the deal unenforceable, illegal, impossible to operate, or materially unsafe.
- `Таблица рисков`: clause, risk, why it matters under РФ context, proposed fix.
- `Что переписать`: ready-to-paste Russian wording when possible.
- `Вопросы перед подписанием`: only questions that materially affect the conclusion.
- `Источники`: links and редакция/date for laws or official guidance used.

For compliance/personal-data questions, add:

- operator/processor role;
- lawful basis and consent need;
- RKN notification status;
- localization and cross-border transfer;
- privacy policy and consent texts;
- breach/incident duties;
- security measures owner: legal, organizational, technical.

## Boundaries

- Do not invent court practice, RKN positions, or article numbers.
- Do not present unofficial blogs as law; use them only for orientation and verify against primary or authoritative sources.
- Do not give tax, criminal, labor, or regulated-industry conclusions as final without flagging the need for specialist review.
- Do not keep large statutory excerpts in the skill. Laws must be checked live.

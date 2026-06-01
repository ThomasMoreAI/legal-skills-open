---
name: escalation-flagger-zekaisuni
title: /escalation-flagger
description: Route a contract issue to the right approver per the escalation matrix in the commercial practice profile, with Turkish-law risk categories, TL thresholds, signature authority, and attorney-review gates. Drafts the ask but never sends or approves it.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/commercial-legal/skills/escalation-flagger
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: commercial
language: tr
---

# /escalation-flagger

Sözleşme riskini veya playbook sapmasını doğru onay makamına yönlendirir ve gönderilmeye hazır bir talep taslağı hazırlar. Kararı vermez; mesajı göndermez.

## Instructions

1. Load `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` -> `## Escalation`.
2. Determine side: sales-side or purchasing-side. A term may be acceptable on one side and escalatable on the other.
3. Characterize issue:
   - TL threshold / deal value.
   - Playbook deviation.
   - Automatic escalation trigger.
   - Signature-authority issue.
   - Business decision, not legal decision.
4. Match to matrix and name a person or role.
5. Draft the ask with issue, clause, playbook, options, recommendation, and decision-by date.
6. Do not send. Show it to the user.
7. If a matter is active, record escalation status in the matter output or review memo.

## Expected Matrix

```yaml
eskalasyon_matrisi:
  - can_approve: "Contracts Counsel"
    threshold: "standard terms / < 1.000.000 TL"
    escalates_to: "Senior Counsel"
    via: "Teams / email"
  - can_approve: "Head of Legal"
    threshold: "non-standard terms / < 10.000.000 TL"
    escalates_to: "CFO / General Manager / Board"
    via: "approval memo"
automatic_triggers:
  - uncapped liability
  - cezai şart above playbook / TBK m.179-185 risk
  - IP assignment
  - KVKK transfer risk
```

## Turkish Automatic Escalation Triggers

- Sınırsız sorumluluk.
- Fahiş veya tek taraflı cezai şart (TBK m.179-185).
- FSEK / fikri mülkiyet devri or broad license.
- KVKK m.9 transfer or sensitive data without approved posture.
- Rekabet yasağı, münhasırlık, customer/employee non-solicit.
- Foreign governing law or forum outside playbook.
- Tahkim clause with unclear institution, seat, or language.
- Guarantee, surety, letter of guarantee, or parent-company support.
- Imza yetkisi, temsil yetkisi, board approval, or internal approval gap.
- Uncapped renewal price or material FX exposure.
- Damga vergisi (488 sayılı DVK), vergi veya muhasebe etkisi için uzman incelemesi gerektiren imza/tadil/sulh/devir yapısı.
- Dava şartı arabuluculuk veya 6325 sayılı Kanun kapsamında uyuşmazlık çözüm handoff'u gerektiren ihtilaf.

## Draft Format

```markdown
**Onay makamı:** [name / role]
**Kanal:** [email / Teams / meeting / CLM approval]
**Aciliyet:** [deadline]
**Uygulanan playbook:** [sales-side / purchasing-side]

---

Sayın [name],

[Counterparty] ile [agreement type] kapsamında aşağıdaki konuda onayınıza ihtiyaç var.

**Risk / sapma:** [plain Turkish explanation]

**Sözleşmedeki madde:**
> "[short quote]"

**Playbook pozisyonumuz:** [quote or summary from CLAUDE.md]

**Seçenekler:**
1. **Kabul** - [why this may be acceptable]
2. **Revize / karşı öneri** - "[proposed narrow language]"
3. **Durdur / üst onay** - [when realistic]

**Tavsiyem:** [recommendation with reason]

**Karar beklenen tarih:** [date]

[Link to full review memo]
```

## Calibration

If clearly inside documented fallback, no escalation. If outside fallback or on automatic list, escalate. If ambiguous or the playbook is silent, escalate with the uncertainty stated.

## What this skill does not do

- It does not approve anything.
- It does not create signature authority.
- It does not send messages.
- It does not decide between options for the approver.
- It does not replace board, shareholder, or internal approval processes.

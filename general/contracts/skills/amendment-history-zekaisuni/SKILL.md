---
name: amendment-history-zekaisuni
title: /amendment-history
description: Trace how a contract has changed across its base agreement and all amendments, ek protokoller, zeyilnameler, and related variation documents. Produces either a chronological summary of all changes or a provision trace for a specific clause while preserving the original skill function.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/commercial-legal/skills/amendment-history
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: tr
---

# /amendment-history

Ana sözleşme ile ek protokol, zeyilname, tadil sözleşmesi, devir/temlik metni ve yan yazılar arasındaki değişiklik zincirini çıkarır. Nihai hukuki yorum vermez; hangi metnin hangi hükmü nasıl değiştirdiğini gösterir ve çelişkileri hukukçu incelemesine taşır.

## Instructions

1. **Get the documents.** Accept direct upload, CLM/repository link, KEP or e-signature package, or matter folder. UYAP only applies if the contract history is tied to a court/enforcement file.

2. **Detect the mode.**
   - Mode 1: summary of all amendments when no specific provision is named.
   - Mode 2: provision trace when the user names a clause or topic.

3. **Establish chronology before substance.** Use, in order:
   - execution date,
   - effective date,
   - "as of" or retroactive-effect language,
   - KEP/e-signature timestamp,
   - file title or archive date.

4. **Read and index every document.** Extract type, parties, execution date, effective date, modified/deleted/added provisions, signatures, and source confidence.

5. **Flag uncertain ordering.** If order is inferred and confidence is low, ask for confirmation before final output.

## Matter Context

If matter workspaces are enabled, load the active matter and write outputs there. Never cross-read other matters unless allowed and requested.

## Turkish Document Types

Classify documents by their own title and operative language:

- Ana Sözleşme
- Ek Protokol
- Zeyilname
- Tadil Sözleşmesi
- Devir Sözleşmesi
- Temlik Sözleşmesi
- Fesih Protokolü
- Mutabakat Tutanağı
- Yan Yazı / Ek Anlaşma

If unclear, mark as `muhtemel belge türü`.

## Step 1 - Load and Order Documents

For each document:

```yaml
belge:
  tur:
  imza_tarihi:
  yururluk_tarihi:
  kaynak:
  siralama_guveni: yuksek | orta | dusuk
  taraflar:
  degistirilen_maddeler:
```

Check whether a party name changed, a party was added, an assignment occurred, or signature authority differs across documents.

## Mode 1 - Summary of All Changes

Every finding must include section references:

> Süreli fesih (m. 12.3; 2 No'lu Ek Protokol m. 4 ile değişik): 90 gün önceden bildirimle fesih hakkı eklendi.

### Output

```markdown
# Sözleşme Tadil Geçmişi: [Counterparty] - [Agreement type]

**Ana sözleşme:** [date]
**Tadil belgeleri:** [N] ([first date] -> [last date])
**Son değişiklik:** [date]
**Sıralama güveni:** [yüksek / orta / düşük]

## Değişiklik Kronolojisi

### [Belge türü] [N] - [date]
**Amaç:** [recitals or omit if unknown]

**Esaslı değişiklikler:**
- [Provision] (m. [X]): [old -> new in plain Turkish]
- [Added provision] (m. [X]): [effect]
- [Deleted provision] (m. [X]): [why it matters]

## Güncel Net Durum

| Hüküm | Güncel pozisyon | Atıf | Son değişiklik |
|---|---|---|---|
| [clause] | [plain Turkish] | m. [X] | [document/date] |

## Dikkat Edilecek Hususlar
[inconsistencies, numbering shifts, assignment issues, signature issues]
```

## Mode 2 - Provision Trace

Show only documents that touched the provision. Skip untouched amendments.

```markdown
# Madde Takibi: [Provision]
## [Counterparty] - [Agreement type]

### Orijinal Metin - [Base date], m. [X]
> "[short exact quote]"

**Özet:** [one sentence]

### [Belge türü] [N] - [date], m. [X]
**Eski hali:** "[quote]"
**Yeni hali:** "[quote]"
**Ne değişti:** [practical effect]

## Güncel ve Geçerli Görünen Hüküm
**m. [X] - [source document, date]**
> "[quote]"

## İzleme Notları
[conflicts, missing signatures, limitation cap effects, numbering shifts]
```

If never amended:

> Bu hüküm tadil belgeleriyle değiştirilmemiş görünüyor. Ana sözleşmedeki metin kontrol eden metindir; yine de çelişkili genel hükümler ayrıca incelenmelidir.

## Conflict Rule

Do not decide which document legally prevails when there is conflict. Instead:

- cite both provisions,
- check whether there is an order-of-precedence clause,
- explain the ambiguity,
- route to attorney review.

Use:

> Bu hükümler arasında potansiyel çelişki var. Hangi hükmün üstün geleceği sözleşmenin yorumuna ve varsa öncelik sırası maddesine bağlıdır; hukukçu incelemesine yönlendirilmelidir.

## Turkish Watch Items

- cezai şart (TBK m.179-185),
- temerrüt faizi and commercial interest,
- payment date, FX, price escalation,
- damga vergisi (488 sayılı DVK) veya vergi incelemesi ihtiyacı,
- term extension and auto-renewal,
- termination and notice method,
- venue, enforcement office, arbitration,
- KVKK and data processing,
- IP license/assignment,
- exclusivity/non-compete/non-solicit,
- guarantee, surety, letter of guarantee.

## What this skill does not do

- It does not give a final legal opinion on which clause controls.
- It does not draft new amendments.
- It does not perform a full risk review of the agreement as amended.
- It does not calculate tax or accounting consequences.
- It does not create a final consolidated contract from unsigned or missing documents.

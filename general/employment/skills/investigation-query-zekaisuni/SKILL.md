---
name: investigation-query-zekaisuni
title: /investigation-query
description: Açık iç soruşturma dosyasındaki kronoloji, delil logu ve görüşme notları üzerinde kontrollü soru-cevap yapar. Cevapta kaynak satırı, belirsizlik ve olgu/kanaat ayrımı gösterir.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/employment-legal/skills/investigation-query
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: tr
---

# /investigation-query

1. Yalnızca belirtilen soruşturma dosyasını oku; başka dosyaya geçme.
2. Cevabı kaynaklı ver: hangi delil/görüşme/kronoloji kaydına dayanıyor?
3. Bilinmeyeni uydurma; "dosyada yok" de.
4. Haklı fesih, savunma veya KVKK riski fark edersen ayrıca işaretle.

Çıktı kısa olmalı:

```markdown
## Cevap
[yanıt]

## Dayanak
- [dosya/kayıt/tarih]

## Belirsizlik
- [eksik]
```

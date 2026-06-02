---
name: investigation-add-zekaisuni
title: /investigation-add
description: Açık iç soruşturma dosyasına belge, görüşme notu, delil, kronoloji olayı veya gözlem ekler. Olgu/kanaat ayrımı, kaynak etiketi, KVKK minimizasyonu ve tarih kaydını zorunlu tutar.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/employment-legal/skills/investigation-add
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: tr
---

# /investigation-add

1. İlgili soruşturma klasörünü bul.
2. Eklenen materyali sınıflandır: delil, görüşme notu, kronoloji, hukuk notu, aksiyon.
3. Kaynak, tarih, kimden geldiği ve güvenilirlik sınırını yaz.
4. Sağlık/özel nitelikli veri ve üçüncü kişi verisini maskele.
5. `evidence-log.md`, `interview-notes.md` veya `timeline.md` dosyasına ekleme taslağı üret.

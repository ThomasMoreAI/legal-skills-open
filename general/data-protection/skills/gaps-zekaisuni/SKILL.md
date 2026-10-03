---
name: gaps-zekaisuni
title: /gaps
description: 'Türkiye regülasyon takip akışındaki açık politika/prosedür boşluklarını listeler; kapatma veya risk kabul kararlarını kaydeder. Kullanım: "açık gapler", "remediation status", "--close GAP-ID", "--accept GAP-ID".'
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/regulatory-legal/skills/gaps
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: tr
---

# /gaps

1. `~/.claude/plugins/config/claude-for-legal/regulatory-legal/gap-tracker.yaml` dosyasını oku.
2. `--close` varsa çözüm notu ve onay bilgisini kaydet.
3. `--accept` varsa risk kabul gerekçesi ve yetkili kişiyi kaydet.
4. Aksi halde açık gap'leri önem, yaş, sahip ve son tarihe göre raporla.

Detaylı şema, bildirim kuralları, doğrulanmamış kaynakların overdue sayılmaması ve hukuki sonuç kapısı `gap-surfacer` referans skill'indedir; substantive çalışma öncesi onu yükle.

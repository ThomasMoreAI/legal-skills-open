---
name: gap-surfacer-zekaisuni
title: Gap Surfacer
description: 'Reference skill: /regulatory-legal:gaps ve /regulatory-legal:comments için ortak tracker çerçevesi. Türkiye regülasyon değişikliklerinden doğan politika/prosedür gap''lerini, taslak/görüş kararlarını, sahipleri, son tarihleri ve bildirimleri yönetir.'
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/regulatory-legal/skills/gap-surfacer
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: regulatory
language: tr
---

# Gap Surfacer

## Değişmez Kural: Gönderim Öncesi Onay

Slack/e-posta/Teams gibi herhangi bir mesaj gönderilmeden önce:

1. Kime ne gönderileceğini kullanıcıya aynen göster.
2. Açık "evet" al.
3. Mesaj kaynak, tarih veya uyum sonucu içeriyorsa "doğrulamadan gönderiliyor" uyarısını öner.
4. Toplu gönderim dahil hiçbir mesaj otomatik gönderilmez.

## Matter Context

`CLAUDE.md -> Matter workspaces` kapalıysa practice-level bağlam kullanılır. Açıksa aktif matter yüklenir; cross-matter kapalıyken başka matter dosyası okunmaz.

## Tracker Şeması

`~/.claude/plugins/config/claude-for-legal/regulatory-legal/gap-tracker.yaml`:

```yaml
gaps:
  - id: GAP-001
    requirement: "[düzenlemenin somut gereği]"
    regulation: "[ad + kaynak/link]"
    policy_affected: "[politika/prosedür adı veya new policy needed]"
    gap_type: "partial"  # none | partial | full | new-policy | watch | comment-decision
    owner: "[politika sahibi]"
    owner_slack: "[Slack kullanıcı adı/ID]"
    opened: 2026-05-13
    due: 2026-06-30
    status_verified: true
    source_tags: ["Resmi Gazete", "Mevzuat"]
    status: "open"  # open | in-progress | closed | risk-accepted
    notified: false
    resolution: ""
```

`comment-tracker.yaml` kardeş dosyadır ve comments skill tarafından yönetilir.

## Gap Türleri

| Değer | Anlam | Hatırlatma |
|---|---|---|
| `none` | Politika yükümlülüğü karşılıyor; audit trail için nadir kayıt | Yok |
| `partial` | Politika var ama yeni gereği tam karşılamıyor | Son tarihten 30 gün önce |
| `full` | Politika çelişiyor veya sessiz | Son tarihten 30 gün önce |
| `new-policy` | Kapsayan politika/prosedür yok | Son tarihten 30 gün önce |
| `watch` | Taslak/görüş/rehber sinyali; bugün uyum yükümlülüğü yok | Revisit |
| `comment-decision` | Görüş verilip verilmeyeceği kararı gerekiyor | Son tarihten 21 gün önce |

**Doğrulanmamış statü overdue olmaz.** `status_verified: false` ise "overdue" yerine "review needed" yaz. Resmi Gazete/Mevzuat/kurum kaynağı teyidi olmadan "bağlayıcı süre kaçtı" sonucu üretme.

## Mod 1: policy-diff'ten İçeri Alma

Partial/full/new-policy gap'leri append et. Aynı requirement + policy için mükerrer kayıt oluşturma. Sahip ve son tarih biliniyorsa yaz; bilinmiyorsa `[unassigned]` ve `[verify]` kullan.

Bildirim gerekiyorsa kullanıcıya önce mesaj önizlemesi göster:

```text
Yeni regülasyon gap'i atandı
Gap: [GAP-ID] - [tek cümle]
Düzenleme: [ad + kaynak]
Etkilenen politika: [ad]
Son tarih: [tarih]
```

## Mod 2: Durum Raporu

```markdown
[ROLE-BASED LEGAL REVIEW HEADER]

## Açık Regülasyon Gap'leri - [tarih]

### Kısa sonuç

[N gap; en yakın kritik son tarih; sahibi belirsiz kayıt varsa not]

### Overdue (statüsü doğrulanmış)

| ID | Gereklilik | Politika | Sahip | Son tarih | Gün |
|---|---|---|---|---|---|

### 30 Gün İçinde

[aynı tablo]

### Açık

[aynı tablo]

### Watch / Taslak / Görüş

| ID | Konu | Tür | Revisit / görüş son tarihi | Sahip |
|---|---|---|---|---|

### Yakın zamanda kapananlar

[son 5 kayıt]

---

**En eski açık gap:** [ID], [N] gün
**Sahiplere göre dağılım:** [özet]

**Doğrulama notu:** Gap'ler upstream kaynak etiketlerini taşır. Kapatma, risk kabul veya kurul/denetim çıktısı öncesi birincil kaynak doğrulanmalıdır.
```

## Mod 3: Kapatma

```
/regulatory-legal:gaps --close GAP-001
Çözüm: "Politika v2.3 güncellendi, [tarih] onaylandı."
```

Non-lawyer rolünde, gap kapatma veya uyum sertifikasyonu hukuki sonuç doğurabileceğinden avukat incelemesi sorulur.

## Mod 4: Risk Kabul

```
/regulatory-legal:gaps --accept GAP-002
Gerekçe: "Yükümlülük yalnızca [koşul] için geçerli; bizde yok. [tetikleyici] olursa yeniden bakılacak."
Kabul eden: [yetkili kişi/rol]
```

## Yapmadıkları

- Gap'i kendi başına kapatmaz.
- Doğrulanmamış düzenlemeyi overdue saymaz.
- Onaysız bildirim göndermez.

---
name: policy-diff-zekaisuni
title: /policy-diff
description: 'Belirli bir Türkiye regülasyon değişikliğini politika kütüphanesiyle karşılaştırır; hangi iç politika/prosedürün etkilendiğini ve boşluğun ne olduğunu çıkarır. Kullanım: "bu düzenlemeyi politikalarla karşılaştır", "gap analysis", "hangi politika etkilenir".'
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/regulatory-legal/skills/policy-diff
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: tr
---

# /policy-diff

1. `CLAUDE.md` içindeki politika kütüphanesini ve önem eşiğini yükle.
2. Düzenleme statüsünü birincil kaynaktan doğrula.
3. Yükümlülükleri ayrıştır.
4. Politikalara eşleştir ve gap analizini çıkar.

## Statü Doğrulama

Diff'e başlamadan önce düzenlemenin niteliğini ve güncelliğini kontrol et:

- Resmi Gazete'de yayımlanmış mı?
- Mevzuat Bilgi Sistemi'nde yürürlükteki metinle uyumlu mu?
- Kurum duyurusu/kurul kararı ise ilgili kurum sayfasındaki metin güncel mi?
- Taslak/görüş aşamasındaysa bağlayıcı yükümlülük doğurmadığını belirt.

Doğrulama yapılamıyorsa çıktı üstüne şu banner'ı koy:

> `DÜZENLEME DURUMU DOĞRULANAMADI - Yürürlük, geçiş tarihi veya metnin güncel hali birincil kaynaktan teyit edilemedi. Bu diff çalışma taslağıdır; işlemden önce Resmi Gazete, Mevzuat veya ilgili kurum sayfası kontrol edilmelidir.`

## Sessiz Tamamlama Yok

Metin eksikse veya sadece haber/bülten varsa dur ve seçenek sun:

1. Tam metni yapıştır.
2. Birincil kaynak linki ver.
3. Web araması yap, sonuçları `[web search - verify]` etiketiyle getir.
4. Burada dur.

## Yükümlülük Çıkarma

Her ayrık yükümlülüğü tabloya koy:

| # | Yükümlülük | Yürürlük/son tarih | Kaynak | Etkilenen alan |
|---|---|---|---|---|
| 1 | [somut gereklilik] | [tarih] | [madde/link] | [politika/iş süreçleri] |

"Daha sıkı bildirim yükümlülükleri" yeterli değildir. "Veri ihlalinin X süre içinde Y kanaldan bildirilmesi gerekir" gibi somut yaz.

## Politika Eşleştirme

- **Doğrudan:** Politika bu konuyu açıkça düzenliyor.
- **Dolaylı:** Politika ilgili alanı kapsıyor ama yeni alt konu yok.
- **Eşleşme yok:** Yeni politika/prosedür gerekebilir.

## Gap Türleri

| Tür | Anlam |
|---|---|
| `none` | Mevcut politika yükümlülüğü karşılıyor |
| `partial` | Politika konuyu görüyor ama yeni gerekliliği tam karşılamıyor |
| `full` | Politika çelişiyor veya sessiz |
| `new-policy` | Hiçbir politika kapsamıyor |
| `watch` | Taslak/görüş aşaması; uyum boşluğu değil, takip konusu |
| `comment-decision` | Görüş verilip verilmeyeceği kararı gerekiyor |

## Taslak/Görüş Dalı

Girdi taslak, kamuoyu görüşü, kurul taslağı veya sektör görüşü çağrısıysa tam uyum gap'i üretme. Bunun yerine:

- Hangi politikaların ileride etkilenebileceğini yaz.
- Görüş son tarihini ve karar sahibini belirt.
- `/regulatory-legal:comments` tracker'a devret.
- "Bugün uygulanacak uyum yükümlülüğü yok" cümlesini açıkça koy.

## Çıktı

```markdown
[ROLE-BASED LEGAL REVIEW HEADER - CLAUDE.md ## Outputs]

## Policy Diff - [Düzenleme adı]

**Düzenleme:** [ad, kaynak, link]
**Statü:** [yürürlükte / taslak / görüşte / doğrulanamadı]
**Yürürlük / son tarih:** [tarih]
**Çıkarılan yükümlülük:** [N]

### Kısa sonuç

[N gap; en kritik yükümlülükler; önerilen ilk aksiyon]

### Özet

| # | Yükümlülük | Etkilenen politika | Gap | Sahip |
|---|---|---|---|---|

### Detaylı analiz

#### Yükümlülük [N]: [başlık]

**Düzenleme gereği:** [somut gereklilik]
**Politika ([ad], son güncelleme [tarih]) diyor ki:** [özet veya kısa alıntı]
**Gap:** [none/partial/full/new-policy/watch/comment-decision]
**Gerekli değişiklik:** [somut değişiklik]
**Sahip:** [kişi/rol]

### Yeni politika gerekenler

[varsa]

### Gap olmayanlar

[mevcut politika karşılıyor listesi]

---

**Kaynak doğrulama:** Kaynak, yürürlük tarihi ve güncel metin işlemden önce birincil kaynaktan doğrulanmalıdır. Kaynak etiketleri korunmuştur.
```

## Konfigürasyon Eksikleri

- Politika kütüphanesi boşsa tüm yükümlülükleri "eşleşme yok" olarak işaretle ve kullanıcıdan politika dizini iste.
- Politika sahibi yoksa owner hücresini boş bırak ve yapılandırma güncellemesi öner.

## Devir

Partial/full/new-policy gap'ler `/regulatory-legal:gaps` tracker'a gider. Taslak/görüş kararları `/regulatory-legal:comments` tarafına gider.

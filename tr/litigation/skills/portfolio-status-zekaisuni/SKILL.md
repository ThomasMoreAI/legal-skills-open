---
name: portfolio-status-zekaisuni
title: /portfolio-status (Portföy ve Dosya Durumu)
description: _log.yaml dosyasından portföy/dava özetini çıkarır — risk dağılımı, yaklaşan kesin süreler/duruşmalar, hareketsiz (stale) dosyalar, finansal önem (materiality) toplamları, aşama dağılımı ve anomali uyarıları. Kullanıcı "durumumuz nedir", "açık kaç dosya var" veya tüm aktif dosyalar üzerinde genel bir portföy raporu istediğinde kullanın.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/litigation-legal/skills/portfolio-status
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: litigation
language: tr
---

# /portfolio-status (Portföy ve Dosya Durumu)

1. `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` yükle → risk kalibrasyonu (`risk:` alanının nasıl okunacağını tanımlar).
2. Aşağıdaki iş akışını ve referansları izle.
3. `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` dosyasını ayrıştır. Varsayılan olarak kapalı (closed) dosyaları filtrele (`--all` ile dahil et).
4. Özeti (rollup) üret: risk dağılımı, önümüzdeki 14/30/60 gün içindeki duruşma/süreler, >30 gündür güncellenmeyen dosyalar, finansal önem toplamları, aşama (dilekçeler/tahkikat vb.) dağılımı.
5. Anomalileri (uyarıları) bayrakla — "kritik" işaretli her şey, süresi geçmiş/kaçırılmış `next_deadline` (kesin süre), riski orta/yüksek olup henüz dış hukuk bürosu atanmamış dosyalar.

---

# Portföy / Dava Durumu (Portfolio Status)

## Amaç

Şu soruya tek bakışta yanıt vermek: Şu an neyi yönetiyorum, neyin dikkatime ihtiyacı var ve neyi kaçırmak üzereyim? Çıktı hızlıca taranabilir olmalıdır — bir sonraki toplantısına/duruşmasına üç dakikası kalmış bir Baş Hukuk Müşaviri (General Counsel) için tasarlanmıştır.

## Bağlamı Yükle

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` — tek doğru kaynak (source of truth)
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` — risk kalibrasyonu (risk/önem derecesi alanlarını Türk pratiğine göre doğru yorumlamak için)

## Bayraklar ve Filtreler

Varsayılan: Yalnızca aktif dosyalar (`status: kapali` olanları hariç tut).

Bayraklar:
- `--all` — kapalı/sonuçlanmış dosyaları da dahil et
- `--risk=yuksek` (veya `kritik` / `orta` / `dusuk`) — risk bandına göre filtrele
- `--hareketsiz` (stale) — yalnızca `last_updated` > 30 gün olan dosyalar
- `--type=is_hukuku` — dava türüne göre filtrele
- `--owner=[isim]` — iş birimi/İK/iletişim sorumlusuna göre filtrele

## Özet Raporu (The rollup)

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — Eklenti ayarları ## Çıktılar bölümüne göre; bkz. `## Bunu Kim Kullanıyor`]

# Portföy / Dava Durumu — [bugün]

**Aktif Dosyalar:** [N]
**Kapalı (bu yıl):** [N] *(sadece --all ile gösterilir)*

---

## Riske Göre Dağılım

| Risk | Sayı | Dosyalar |
|---|---|---|
| Kritik | [N] | [kısa adlar - slugs] |
| Yüksek | [N] | [kısa adlar] |
| Orta | [N] | [sadece sayı — `--risk=orta` ile genişletin] |
| Düşük | [N] | [sadece sayı] |

## Yaklaşan Süreler ve Duruşmalar

| Zaman Dilimi | Dosyalar |
|---|---|
| 14 gün içinde | [kısa-ad — tarih/duruşma — kısa konu] |
| 15–30 gün | [...] |
| 31–60 gün | [...] |

*Süresi geçmiş (kaçırılmış) `next_deadline` kayıtları aşağıda ayrıca uyarı (bayrak) olarak gösterilmiştir.*

## Finansal Önem ve Karşılıklar (Materiality)

| Kategori | Sayı | Toplam Risk / Dava Değeri (Ortalama) |
|---|---|---|
| Karşılık Ayrılmış (Reserved) | [N] | [X TL] |
| KAP Açıklaması Yapılmış | [N] | [X TL] |
| Takipte (Monitored) | [N] | — |
| Yok / Belirsiz | [N] | — |

## Dava Aşamasına Göre

[Tablo: Arabuluculuk / Dilekçeler / Ön İnceleme / Tahkikat-Bilirkişi / Karar / İstinaf-Temyiz / İnfaz-İcra]

---

## ⚠️ Anomaliler ve Uyarılar (Flags)

- **Kaçırılmış / Süresi Geçmiş İşlemler:** [next_deadline'ı geçmiş olan kısa-ad listesi]
- **Hareketsiz (>30g güncelleme yok):** [liste]
- **Menfaat Çatışması (Av.K. 38) Çözülmemiş:** [`conflicts.status` değeri `bekliyor` veya `yapilmadi` olanlar]
- **Çatışma Uyarısı Geçilmiş (Override):** [`conflicts.override.by` dolu olanlar — manuel temizlenene kadar kalıcı bayrak]
- **Dış Büro Atanmamış Yüksek/Kritik Riskli Dosyalar:** [liste]
- **>60 gündür güncellenmemiş "Karşılık Ayrılan" Dosyalar:** [liste] — finansal karşılık güncellemesi muhtemelen gecikti
- **Aktif davada "Kayıt Muhafaza/Delil Tespiti" (Legal Hold) eksikliği:** [liste]
- **Eksik Alanlar:** [dosya → eksik alan]

---

## Kapanış Tavsiyesi

[Sadece gerçekten göze çarpan, acil bir sorun varsa neye bakılması gerektiğine dair bir iki cümle. Klişe (boilerplate) metin kullanmayın.]
```

## Anomali (Uyarı) Kuralları

Bu kurallar, beceriyi sadece dekoratif olmaktan çıkarıp işe yarar (proaktif) hale getirir:

1. **Gecikmiş Süre (Overdue):** `next_deadline < today` ve `status != kapali`
2. **Hareketsiz (Stale):** `last_updated < today - 30d` ve `status != kapali`
3. **Çatışma çözülmemiş:** `conflicts.status in [bekliyor, yapilmadi]` ve `status != kapali`
3b. **Çatışma Override (Zorla Geçilmiş):** `conflicts.override.by != null` (asla otomatik silinmez)
4. **Sahipsiz Yüksek Risk:** `risk in [yuksek, kritik]` ve `outside_counsel.firm == null`
5. **Eskimiş Karşılık Raporu:** `materiality == karsilik_ayrilmis` ve `last_updated < today - 60d`
6. **Delil/Kayıt Muhafaza (Hold) Boşluğu:** `status in [tehdit, aktif, tahkikat, istinaf]` ve `legal_hold.issued == false` — delilleri koruma yükümlülüğü (HMK ve TTK basiretli tacir gereği) makul dava beklentisi anında başlar, bu yüzden `tehdit` (ihtarname vs.) aşaması kapsama dahildir.
7. **Eksik alanlar:** Zorunlu alanlardan herhangi birinin boş (null) olması — `risk`, `materiality`, `status`, `opened`, `conflicts.status`

## Kapanış Karar Ağacı (Next-steps decision tree)

CLAUDE.md `## Çıktılar (Outputs)` bölümündeki karar ağacı (next-steps decision tree) ile bitirin. Seçenekleri, bu becerinin ürettiği sonuca göre özelleştirin — beş varsayılan dal (taslağı yaz, eskalasyon yap, daha fazla bilgi al, izle ve bekle, başka bir şey) bir başlangıç noktasıdır, kilitli bir kalıp değildir. Ağaç çıktıdır; hukukçu seçer.

Eğer portföyde 10'dan fazla dosya varsa veya kullanıcı ne zaman isterse: pano (dashboard) teklif edin (bkz. CLAUDE.md `## Outputs → Dashboard offer for data-heavy outputs`). Teklifi bu çıktıya göre şekillendirin — risk katmanına göre sayımlar, yaklaşan sürelerin/duruşmaların zaman çizelgesi ve durum, çatışma kontrolü ve son dokunulma tarihine göre sıralanabilir bir dava/dosya tablosu.

## Bu Becerinin YAPMADIĞI Şeyler

- Karar vermek. Neye dikkat edilmesi gerektiğini (anomaly/flag) ortaya çıkarır; önceliğe kullanıcı/avukat karar verir.
- Sahip olmadığı bir kesinliği/hassasiyeti varmış gibi davranmak. Karşılık (exposure) ortalamaları ve dava değeri tahminleri kabacadır ve bu şekilde etiketlenmelidir.
- Gerçek bir UYAP entegrasyonu veya Hukuk Otomasyon Sisteminin (MMS) yerini almak. Bu bir çalışan-bellek özetidir, resmi kayıt sistemi (system of record) değildir.

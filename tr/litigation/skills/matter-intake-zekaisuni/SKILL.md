---
name: matter-intake-zekaisuni
title: /matter-intake (Uyuşmazlık Kaydı)
description: Yeni bir uyuşmazlık dosyası açar — taraf tespiti, menfaat çatışması, arabuluculuk/dava şartı durumu, dava değeri (harca esas değer), risk triyajı, dış büro, iç paydaşlar, delil muhafaza ve kesin süreleri kapsayan standart sorular sorar. matter.md ve history.md dosyalarını oluşturur, _log.yaml defterine yapılandırılmış bir satır ekler. Kullanıcı "yeni dava", "bu dosyayı kaydet" dediğinde veya portföye yeni bir uyuşmazlık eklemek istediğinde kullanın.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/litigation-legal/skills/matter-intake
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: litigation
language: tr
---

# /matter-intake (Uyuşmazlık Kaydı)

1. `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` dosyasını yükle → risk kalibrasyonu (triyaj için), harita (bağlam, çatışma yöntemi için), paydaşlar (kimin dâhil edileceği için).
2. Aşağıdaki iş akışını ve referansları izleyin.
3. Standart kayıt (intake) sürecini yürütün: kimlik tespiti, menfaat çatışması kontrolü, kaynak, dava şartı arabuluculuk durumu, risk triyajı, önem eşiği (materiality), dış hukuk bürosu, iç sorumlular, şirket içi delil muhafaza (retention) ve kesin süreler, başlangıç duruşu.
4. Dosya adından bir `slug` (kısa ad) üretin (küçük harf, tireli, yıl içeren. Örn: acme-haksiz-rekabet-2026).
5. `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[kisa-ad]/matter.md` dosyasını oluşturun — tam anlatısal kayıt.
6. `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[kisa-ad]/history.md` dosyasını oluşturun — kayıt anını ilk girdi (entry zero) olarak ekleyin.
7. `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` dosyasına yapılandırılmış bir satır ekleyin.
8. Kullanıcıyla teyit edin: "İşte yazacağım satır ve detaylar — herhangi bir düzeltme var mı?"

---

# Matter Intake (Dosya Kaydı)

## Amaç

Her yeni uyuşmazlık aynı kayıt (intake) sürecinden geçer, böylece portföy karşılaştırılabilir kalır. `_log.yaml` dosyasındaki standart satırlar, portföy durumu (status) becerisinin özet çıkarmasını sağlar. `matter.md` içindeki anlatı, yaml satırının tutamadığı detayları yakalar. Burada tohumlanan (seeded) tarihçe dosyası, olay kaydına (safahat) dönüşür.

## Bağlamı Yükle

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` — risk kalibrasyonu (triyaj eşikleri, önemlilik, sulh merdiveni), harita (paydaşlar, dış hukuk bürosu yedeği).
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` — kısa adın benzersizliğini teyit etmek için.

## Kayıt Süreci (The intake)

### 1. Kimlik Tespiti (Identification)

- Dosya adı (genellikle anıldığı şekliyle, örn. "Acme vs. Şirketimiz İş Davası 2026")
- Karşı Taraf
- Uyuşmazlık türü: `sozlesme | is-hukuku | fikri-mulkiyet | idari | ceza | sorusturma | urun-sorumlulugu | diger`
- Rolümüz: `davaci | davali | alacakli | borclu | sorusturulan`
  - Pratik profilinin `## Taraf (Side)` ayarı `davacı`, `davalı` veya bunların "varsayılan" bir varyantıysa, rolü bu varsayılandan önceden doldurun ve onaylayın. Eğer `uyuşmazlığa göre değişir` ise, doğrudan sorun. Kurumsal profilin belirlemediği bir konumu asla sessizce varsaymayın.
  - Rol, sonraki becerileri yönlendirir: Davacı konumundaki dosyalar risk triyajını dava değeri / vekalet ücreti ekonomisine yönlendirir; davalı konumundaki dosyalar maruziyet (exposure) / karşılık ayırma / sigorta ihbarına yönlendirir.
- Görevli ve Yetkili Mahkeme / Tahkim Forumu (HMK m.1-19, İstinaf, Yargıtay)

### 2. Dava Şartı / Arabuluculuk (Mediation / Pre-suit requirements)

- Uyuşmazlık zorunlu arabuluculuk kapsamında mı? (İş, Ticari, Tüketici vs.)
- Durum: `arabuluculuk-asamasinda | anlasma-saglanamadi | dava-acildi | muaf`
- Son tutanak tarihi (dava açma süresi/zamanaşımı açısından kritik).

### 3. Menfaat Çatışması Kontrolü (Conflicts check)

Daha ileri gitmeden önce, `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → Menfaat Çatışması Kontrolü adımını çalıştırın.

- **Durum:** `cleared (temiz) | pending (bekliyor) | not-run (calistirilamadi) | waived (feragat edildi)`
- **Yöntem:** Kurumsal profildeki yöntemle eşleştirin (`kurumsal | dis-buro | sistem-kontrolu | gayri-resmi | diger`). Eğer gayri-resmi ise bunu belirtin.
- **Kontrol eden:** isim / ekip / büro
- **Kontrol tarihi:** YYYY-MM-DD
- **Kontrol edilenler:** isimlerin/şirketlerin kısa listesi (karşı taraf, iştirakler vb.). "Hayır" cevabı yeterli değildir, kimlerin kontrol edildiği yazılmalıdır.
- **Notlar:** işaretlenen ancak temizlenen her şey.

Duruma göre davranış:
- `cleared` → devam et.
- `pending` → kayda devam et; `matter.md` ve log satırında çatışma kontrolünün beklediğini belirgin şekilde işaretle.
- `not-run` → **DUR. Bu bir güvenlik kapısıdır (gate).** Becerinin dosyaları ve logu oluşturması için çatışma durumunun çözülmesi gerekir. (Çatışma temizlenmeli, beklemeye alınmalı veya gerekçeli bir şekilde atlanmalıdır).

### 4. Kaynak

Bu uyuşmazlık bize nasıl ulaştı?
- `ihtarname | dava-dilekcesi-tebligi | muzekkere | kurum-incelemesi | ic-bildirim | dava-oncesi-tehdit`
- *Tohum belge fırsatı:* "Eğer başlatıcı belge (dilekçe, ihtarname, müzekkere) varsa ekleyin veya yolunu paylaşın."

### 5. Risk Triyajı — Kurumsal Kalibrasyona Karşı

- Etki (Severity): yuksek | orta | dusuk (CLAUDE.md bantlarına atıf yapın)
- Olasılık (Likelihood): yuksek | orta | dusuk
- Ortaya çıkan risk derecesi (matrise göre): yuksek | orta | dusuk | kritik
- Harca Esas Değer / Tahmini Maruziyet (Dava Değeri / Zarar)
- Parasal olmayan maruziyet (İhtiyati tedbir? Ürün toplatma? İtibar? Emsal karar riski?)

### 6. Önemlilik (Materiality)

CLAUDE.md'deki kurum eşiklerine karşı:
- `reserved (karsilik-ayrildi) | disclosed (KAP'a bildirildi) | monitored (izleniyor) | none`
- `reserved` ise: karşılık tutarı ve finansın haberdar olup olmadığı.
- `disclosed` ise: KAP veya finansal dipnot lokasyonu.

### 7. Dış Hukuk Bürosu

- Büro
- Sorumlu Ortak Avukat (Partner)
- **Sorumlu ortak e-postası** (`/oc-status` tarafından kullanılır)
- Vekaletname / Ücret Sözleşmesi durumu: `imzalandi | bekliyor | yok`
- Bütçe onayı: tutar ve onaylayan.

Risk 'orta' veya daha yüksekse ve dış büro atanmamışsa — bunu işaretleyin.

### 8. İç Sorumlular (Internal owners)

- İş birimi yöneticisi
- İK Yöneticisi (İş davaları için)
- İletişim / PR (İtibar riski varsa)
- CISO (Veri / Siber ise)

### 9. Kayıt Muhafaza Talimatı (Legal hold / Retention)

- Şirket içi bildirim yayınlandı mı? (Örn. IT'ye "x çalışanının maillerini silmeyin" veya HMK m.400 Delil Tespiti). Eğer evet ise: tarih, kapsam, kişiler.
- Bir sonraki yenileme tarihi.
- Eğer hayır ise ve bu aktif bir uyuşmazlıksa: acil olarak işaretleyin; kayıt bittikten sonra `/litigation-legal:legal-hold [kisa-ad] --issue` çalıştırmayı teklif edin.

### 10. Kesin Süreler ve Önemli Tarihler

- Cevap / İtiraz süresi (Tebliğ tarihinden itibaren HMK/İİK/CMK süreleri)
- Sonraki duruşma / inceleme günü
- Zamanaşımı / Hak düşürücü süre sonu
- Arabuluculuk son tutanak tarihi

### 11. Başlangıç Duruşu (Initial posture)

Bir paragraflık hukuki teori:
- Bizim hikayemiz nedir?
- Onların hikayesi nedir?
- Uyuşmazlığın kırılma noktası (pivot fact) nedir?
- Başlangıç duruşu: `savas (fight) | sulh-ol (settle) | arastir (investigate) | bekle (wait)`

## Çıktıların Yazılması

### Kısa Ad (Slug)

Küçük harf, tireli, sonda yıl. Örn: `acme-vs-biz-2026`, `is-davasi-calisan-2026`, `btk-inceleme-2026`.
Yazmadan önce slug'ın `_log.yaml`'da benzersiz olduğunu doğrulayın.

### `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[kisa-ad]/matter.md`

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — Eklenti ayarları ## Çıktılar bölümüne göre; bkz. `## Bunu Kim Kullanıyor`]

# [Dosya Adı]

**Kısa ad (Slug):** [kisa-ad]
**Açılış:** [YYYY-MM-DD]
**Rolümüz:** [davacı/davalı/vb.]
**Durum:** [aktif/pasif vb.]

---

## Kimlik ve Dava Şartı

[Karşı taraf, görevli/yetkili mahkeme, dosya türü, kaynak, arabuluculuk durumu]

## Menfaat Çatışması

**Durum:** [cleared / pending / not-run / waived]
**Yöntem:** [kurumsal / dis-buro / vb.]
**Kontrol eden:** [isim]
**Kontrol tarihi:** [YYYY-MM-DD]
**Kontrol edilenler:** [kurumlar/isimler]
**Notlar:** [varsa feragat vs.]

## Risk Triyajı

**Etki:** [bant] — [neden, kurumsal tanımlara atıfla]
**Olasılık:** [bant] — [neden]
**Risk derecesi:** [yuksek/orta/dusuk/kritik]
**Maruziyet / Dava Değeri:** [TL aralığı + parasal olmayan]

## Önemlilik (Materiality)

[reserved/disclosed/monitored/none — karşılık tutarı, bildirim yeri veya "none" ise gerekçesi]

## Dış Hukuk Bürosu

[büro, sorumlu, sözleşme durumu, bütçe]

## İç Sorumlular

[paydaşlar ve neden dâhil edildikleri]

## Kayıt/Delil Muhafaza (Legal hold)

[durum, tarih, kapsam]

## Önemli Tarihler

[liste: cevap süresi, zamanaşımı, duruşma vb.]

## Başlangıç Teorisi

[bir paragraf: bizim hikayemiz, onların hikayesi, pivot olgu, başlangıç duruşu] `[SME VERIFY — Kayıt aşamasındaki teori bir çalışma hipotezidir; herhangi bir beyan veya dilekçeden önce dış büro ile teyit edin]`

## Açık Sorular

[henüz bilinmeyen önemli şeyler — örn., "sigorta ihbarı beklemede", "X için kapsamda olup olmadığımız belirsiz"]

---

## Tohum Belgeler (Seed documents)

| Belge | Yol / İşaretçi |
|---|---|
| [örn., dava dilekçesi / ihtarname] | [yol veya "henüz paylaşılmadı"] |
```

### `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/[kisa-ad]/history.md`

Tarihçe dosyasını (history.md) açılış anıyla tohumlayın (ilk kayıt):

```markdown
# Tarihçe (Safahat): [Dosya Adı]

Sadece ekleme yapılabilen olay/safahat günlüğü. En yeniler üstte.

---

## [YYYY-MM-DD] — Dosya Açılışı

[Kaynak, dosyayı kimin getirdiği, ilk triyaj özeti, atanan dış büro, kayıt muhafaza (legal hold) durumu.]
```

### `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` Dosyasına Ekleme

Şemaya göre bir satır ekleyin.

```yaml
- id: acme-vs-biz-2026
  name: "Acme A.Ş. vs Şirketimiz"
  type: sozlesme
  role: davali
  counterparty: "Acme A.Ş."
  jurisdiction: "İstanbul Anadolu Asliye Ticaret"
  status: active
  stage: dilekceler-teatisi
  source: dava-dilekcesi-tebligi
  outside_counsel:
    firm: "Dış Hukuk Bürosu"
    lead: "Av. [Ad Soyad]"
    email: "outside-counsel@example.com"
    engagement: imzalandi
  conflicts:
    status: cleared
    method: kurumsal
    cleared_by: "[Yetkili]"
    cleared_date: 2026-04-20
    override:                   # Sadece Path 3 bypass durumunda doldurulur
      by: null
      date: null
      rationale: null
  risk: high
  materiality: reserved
  exposure_range: "2M–5M TL"
  internal_owners:
    business_lead: "[İş Birimi Yetkilisi]"
    hr_partner: null
    comms_contact: null
  legal_hold:
    issued: true
    issued_date: 2026-02-15
    scope: "Satış departmanı 2023–2026 e-postaları"
    custodians: ["[Saklayıcı 1]", "[Saklayıcı 2]", "[Saklayıcı 3]"]
    last_refresh: 2026-02-15
    next_refresh: 2026-08-15
    released: null
  related_matters: []
  opened: 2026-04-20
  next_deadline: 2026-05-15
  last_updated: 2026-04-20
  path: matters/acme-vs-biz-2026/
```

## Yazmadan Önce Teyit Edin

Kullanıcıya yamla yazılacak satırı ve matter.md içeriğini gösterin:

> İşte yazacağım içerik. Kaydetmeden önce yanlış veya eksik bir şey varsa lütfen belirtin.

## Sonraki Adımlar Karar Ağacı ile Kapatın

`CLAUDE.md` `## Çıktılar` bölümüne göre sonraki adımlar karar ağacıyla sonlandırın. Seçenekleri bu becerinin ürettiği şeye göre özelleştirin (taslak hazırla, eskalasyon yap, daha fazla olgu topla, bekle ve gör vb.). Ağaç bir çıktıdır; avukat seçimi yapar.

## Bu Becerinin YAPMADIĞI Şeyler

- **Menfaat çatışması kontrolünün bizzat yapılması.** Sadece sonucu, durumu, yöntemi ve kontrol edilen kurumları kaydeder. Gerçek temizleme işlemi (clearance), kurumun beyan ettiği yöntemle yapılır.
- Başlangıç teorisine karar vermek. Kullanıcının söylediğini yakalar; kendisi icat etmez.
- Şirket içi delil muhafaza / tespit bildirimini göndermek. Eksikse uyarır. Kullanıcı manuel gönderir.

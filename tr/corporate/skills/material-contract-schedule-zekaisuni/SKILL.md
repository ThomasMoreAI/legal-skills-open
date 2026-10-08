---
name: material-contract-schedule-zekaisuni
title: /material-contract-schedule
description: Önemli Sözleşmeler (Material Contracts) açıklama ekini (disclosure schedule) due diligence bulgularından yola çıkarak oluşturur. Hisse/Varlık Devir Sözleşmesi'ndeki (SPA/APA) "Önemli Sözleşme" tanımını ve ek formatını uygular. Kullanıcı "önemli sözleşmeler listesini oluştur", "açıklama eklerini hazırla", "ek 3.X", "material contracts schedule" dediğinde kullanılır.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/corporate-legal/skills/material-contract-schedule
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: corporate
language: tr
---

# /material-contract-schedule

1. Devir Sözleşmesini (SPA/APA) yükle → Önemli Sözleşme tanımı + ek formatı.
2. Aşağıdaki iş akışını kullan.
3. Tanımı due diligence bulgularına uygula. İstisnai/sınırda vakaları işaretle.
4. Sözleşmedeki formata göre listele. Onay (consent) takibi kapanış kontrol listesini (closing-checklist) besler.

---

## Dosya Bağlamı (Matter Context)

**Dosya Bağlamı.** Büro düzeyindeki CLAUDE.md dosyasında `## Matter workspaces` bölümünü kontrol et. Eğer `Enabled` durumu `✗` ise (kurum içi hukukçular için varsayılan), bu paragrafı atla. Eğer aktifse ve açık bir dosya (matter) yoksa şunu sor: "Bu hangi dosya için? `/corporate-legal:matter-workspace switch <slug>` komutunu çalıştır veya `buro-geneli` de." Aktif dosyanın `matter.md` içeriğini bağlam ve özel talimatlar için yükle. Çıktıları dosya klasörüne (`~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<dosya-slug>/`) yaz. `Cross-matter context` açık değilse asla başka bir dosyanın verisini okuma.

---

## Amaç

Devir sözleşmesinde (SPA) şöyle bir beyan (rep) bulunur: "Ek 3.X tüm Önemli Sözleşmeleri (Material Contracts) listelemektedir." Bu skill, due diligence bulgularından yola çıkarak bu eki oluşturur — sözleşmedeki tanıma göre hangi sözleşmeler önemlidir ve sözleşmenin talep ettiği format nasıldır.

## Dil ve Şema Standardı

Corporate `CLAUDE.md` dosyasındaki `## Yapısal veri standardı` bölümünü uygula. Bu skill'in açıklama eki, onay takip tablosu ve hukukçuya sunulan çıktılarında tablo başlıkları Türkçe olmalıdır. Sözleşmenin kendisi İngilizce tanımlı terim kullanıyorsa Türkçe karşılık esas alınır; gerekli ilk kullanımda İngilizce terim parantez içinde korunabilir. Kullanıcı ayrıca YAML/CSV gibi makine aktarımı isterse alan adlarını canonical ASCII `english_snake_case` üret.

## Bağlam Yükleme

- Hisse/Varlık Devir Sözleşmesi taslağı — "Önemli Sözleşme" tanımını ve ek formatını almak için
- `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` → önemlilik eşikleri (sözleşme tanımından farklı olabilir — daima sözleşmedeki tanımı kullan)
- diligence-issue-extraction bulguları — sözleşme bazında veriler

## İş Akışı

### Adım 1: Tanımı Al

Devir sözleşmesinden (SPA) "Önemli Sözleşme" tanımını çek — SPA tanımı geçerlidir. İşlem yapısındaki farklılıklar (hisse devri (TTK m.495) vs. ticari işletme devri (TBK m.202 / TTK m.11) vs. birleşme (TTK m.136 vd.)) bir bendi yorumlama şeklini değiştirebilir. Ayrıca düzenlemeye tabi sektörler (sağlık, savunma sanayii (SSB), finansal hizmetler (BDDK/SPK), telekom (BTK), enerji (EPDK) veya kamu ihaleleri) SPA dışında onay gereklilikleri getirebilir. İşlem bu sektörlerden herhangi birini içeriyorsa, ilgili devir yasaklarını veya yenileme kurallarını araştır (örneğin 4735 Sayılı Kamu İhale Sözleşmeleri Kanunu m.16 kapsamındaki devir yasakları) ve ilgili kuralı alıntıla.

SPA tanımında aranacak yaygın bendi kategorileri — bunlar SPA'yı okumanın yerini tutmaz ve SPA'nın kullandığı liste geçerlidir:

- Parasal eşik (yıllık veya toplam değer - TL/USD/EUR cinsinden)
- Sözleşme süresi (örn. 1 yıldan uzun süreli)
- Kontrol değişikliği (change of control) veya devir yasağı (anti-assignment) hükmü
- Münhasırlık (exclusivity) veya rekabet etmeme (non-compete) yasağı
- En büyük ilk N müşteri veya tedarikçi sözleşmesi
- Taşınmaz kira sözleşmeleri (gayrimenkul)
- Fikri Mülkiyet (IP) lisansları (gelen ve giden)
- İlişkili taraf (related-party) sözleşmeleri
- Kamu/Devlet sözleşmeleri ve ihaleleri
- Olağan iş akışı (ordinary course of business) dışındaki sözleşmeler

SPA'nın tanımı tek testtir. Mekanik olarak uygula — SPA tanımındaki herhangi bir bendi karşılayan her sözleşme listeye (Schedule) girer.

### Adım 2: Tanımı Bulgulara Uygula

Due diligence'da incelenen her sözleşme için:

| Sözleşme | Karşıladığı Bent(ler) | Dahil Edilecek mi? |
|---|---|---|
| [İsim] | [X TL+ yıllık değer; Kontrol Değişikliği (CoC) hükmü] | Evet |
| [İsim] | [Hiçbiri] | Hayır |

**İnsan kararı (avukat) için işaretlenecek sınır (edge) vakalar:**
- Sözleşme X-1 TL (eşik değerin hemen altında) ancak işletme için çok kritik
- Sözleşme bir bendi karşılıyor ancak zaten feshediliyor
- Sayılıp sayılmayacağı belirsiz sözlü anlaşmalar veya yan protokoller (side letters)

### Adım 3: Ek (Schedule) Verilerini Topla

Dahil edilen her sözleşme için ekte (schedule) genellikle şunlar istenir:

| Alan | Kaynak |
|---|---|
| Karşı Taraf | Sözleşme |
| Sözleşme Başlığı/Türü | Sözleşme |
| Tarih | Sözleşme |
| Süre / Bitiş Tarihi | Sözleşme |
| Yıllık/Toplam Değer | Sözleşme veya yönetim verileri |
| Hangi önemlilik bendini karşıladığı | Adım 2 analizi |
| İşlem için onay gerekiyor mu? | Diligence bulgusu ve TBK m.205 kontrolü |
| Sanal Veri Odası (VDR) Referansı | Diligence envanteri |

Mevcut diligence (diligence-issue-extraction) bulgularından çek. Bir alan eksikse, işaretle — tahmin etme.

### Adım 4: Sözleşmeye Göre Formatla

Açıklama eklerinin (Disclosure schedules) bir formatı vardır — genellikle numaralandırılmış bir liste veya tablo, bazen sözleşme türüne göre alt bölümler. Taslak sözleşmedeki diğer eklerin formatıyla eşleştir.

```markdown
## Ek 3.[X] — Önemli Sözleşmeler

İmza tarihi itibariyle Önemli Sözleşmeler aşağıdakilerdir:

### (a) Müşteri Sözleşmeleri

1. [Sözleşme Başlığı], [Hedef Şirket] ile [Karşı Taraf] arasında, [tarih] tarihli.
   [Format gerektiriyorsa kısa açıklama.]
   [VDR: yol/link]

2. [...]

### (b) Tedarikçi Sözleşmeleri

[...]

### (c) Taşınmaz Kiraları

[...]

[vb. — sözleşmenin tanım yapısındaki alt bölümlere göre]
```

### Adım 5: Onay (Consent) Takip Katmanı

Ek içinde (schedule) DEĞİL — bu tamamen iç işleyiş içindir — listelenen sözleşmelerden hangilerinin onay (consent) gerektirdiğini ayrıca takip et.

> Onay (consent) takibi ve eklerin teslim öncesi çalışma taslakları, gizli/imtiyazlı diligence materyallerinden türetilir ve bunların gizlilik statüsünü miras alır — avukat-müvekkil gizlilik çemberinin dışına dağıtılması sır saklama yükümlülüğünü (Av. K. m.36) ihlal edebilir. Eklerin kendisi, imzalanmış SPA'nın bir eki olarak teslim edildikten sonra bir işlem belgesidir ve sır kapsamında değildir; teslimden önce tüm iç notları/işaretlemeleri temizleyin.


| Ek # | Karşı Taraf | Onay Gerekli mi? | Durum | Sorumlu | Teslim Tarihi |
|---|---|---|---|---|---|
| 3.X(a)(1) | [İsim] | Evet — Kontrol Değişikliği (CoC) m.12.2 | Talep Edildi | [İsim] | [Tarih] |

Bu veri kapanış kontrol listesini (`closing-checklist`) besler.

## Çapraz Kontrol (Cross-check)

Teslim etmeden önce:

- Bir bendi karşılayan her sözleşme listede mi? (Eksiksizlik)
- Herhangi bir bendi karşılamayan sözleşme listede mi? (Fazla açıklama/over-disclosure yapma — bu bir beyandır (rep), veri dökümü değil)
- Ek, diğer beyanlarla uyumlu mu? (Örneğin; Ek 3.X'te yer alan ve bir takyidat/rehin yaratan sözleşme, takyidatlar/rehinler (liens) ekinde de bulunmalı)
- Her girdinin, alıcı taraf avukatının temel belgeyi bulabilmesi için bir VDR referansı var mı?

## Devir Noktaları (Handoffs)

- **Girdi:** Sözleşme bazındaki bulgular `diligence-issue-extraction` skill'inden gelir.
- **Çıktı:** Onay (consent) kalemleri `closing-checklist` skill'ine gider.

## Bu Skill Ne Yapmaz?

- Önemlilik (materiality) tanımına karar vermez — bu, Hisse/Varlık Devir Sözleşmesi'ndedir.
- Gerekli onayları (consents) almaz — sadece hangilerine ihtiyaç olduğunu tespit ve takip eder.
- Beyanı (rep) bizzat yazmaz — sadece beyanın atıfta bulunduğu eki (schedule) doldurur.

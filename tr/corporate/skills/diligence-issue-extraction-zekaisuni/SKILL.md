---
name: diligence-issue-extraction-zekaisuni
title: /diligence-issue-extraction
description: Türk M&A due diligence belgelerini okur, VDR veya yerel klasördeki dokümanları Türk işlem kategorileri ve önemlilik eşiklerine göre tarar, risk bulgularını kaynaklı issue memo formatında çıkarır. Hisse/pay devri, malvarlığı devri, birleşme, bölünme, tür değiştirme, yatırım, JV, ticaret sicili, KVKK, Rekabet, iş hukuku, vergi, ruhsat, sözleşme devri ve kapanış aksiyonları için kullanılır.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/corporate-legal/skills/diligence-issue-extraction
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: corporate
language: tr
---

# /diligence-issue-extraction

## Amaç

Bu skill, Türk hukuku ve Türkiye M&A uygulaması için VDR/doküman setinden hukuki due diligence bulguları çıkarır. Amaç tüm belgeleri mekanik özetlemek değil; işlem değerini, kapanış koşullarını, tescil/izin süreçlerini, sözleşme devrini, sorumluluk riskini veya entegrasyonu etkileyen konuları görünür yapmaktır.

Çıktı bir hukuki görüş değil, avukat/hukukçu incelemesine tabi issue memo taslağıdır.

## Bağlamı yükle

1. `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` dosyasını oku.
2. Varsa `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[code]/deal-context.md` dosyasını oku.
3. Matter workspace açıksa aktif matter `matter.md` dosyasını oku; başka matter dosyalarını kullanıcı açıkça istemedikçe okuma.
4. `## M&A ve işlem yönetimi` bölümünden işlem türü, taraf rolü, önemlilik eşikleri, risk derecelendirme ve issue memo formatını al.

Deal context yoksa kısa sor:

- İşlem türü nedir: pay devri, hisse alımı, malvarlığı devri, birleşme, bölünme, tür değiştirme, yatırım, JV?
- Hangi taraftayız: alıcı, satıcı, yatırımcı, hedef şirket veya grup şirketi?
- VDR veya belge klasörü nerede?
- Önemlilik eşiği TL, stratejik kategori veya tüm belgeler şeklinde mi?

## Step 1 - VDR envanteri

VDR connector varsa index çek. Yoksa yerel klasörü veya kullanıcının verdiği dosya listesini oku. Klasörleri Türk due diligence kategorilerine eşleştir.

```markdown
## VDR Envanteri: [İşlem kodu]

| Kategori | VDR klasörü | Belge sayısı | Durum |
|---|---|---:|---|
| Kurumsal kayıtlar | /01-Kurumsal | 45 | İncelendi |
| Önemli sözleşmeler | /02-Sozlesmeler | 312 | Devam ediyor |
| KVKK ve veri | /03-KVKK | 18 | Başlanmadı |
| [diğer] | | | |

Eksikler:
- [Talep listesinde olup VDR'da karşılığı olmayan belge]
```

Kategori eşleştirmede tipik Türkiye seti:

- Kurumsal kayıtlar, esas sözleşme/şirket sözleşmesi, MERSİS, ticaret sicili, TTSG ilanları
- Pay sahipliği, pay defteri, sermaye hareketleri, imtiyazlar, pay devir kısıtları
- Yönetim kurulu, müdürler kurulu, genel kurul kararları ve karar defterleri
- Önemli sözleşmeler, ek protokoller, tadiller, devir/temlik ve kontrol değişikliği hükümleri
- KVKK, VERBİS, veri işleme envanteri, veri işleme sözleşmeleri, yurt dışına aktarım
- Rekabet hukuku, birleşme/devralma izni, rekabete hassas bilgi paylaşımı
- Çalışanlar, SGK, bordro, iş sözleşmeleri, yan haklar, iş uyuşmazlıkları
- Vergi, damga vergisi, finansman, teminat, kefalet, garanti, rehin/ipotek
- Fikri mülkiyet, yazılım, lisanslar, açık kaynak, marka/patent kayıtları
- Taşınmaz, çevre, ruhsat, izin ve sektörel düzenleyici kayıtları
- Dava, icra, ihtarname, idari soruşturma ve arabuluculuk süreçleri

## Step 2 - Önemlilik filtresi

Profilde veya deal context'te belirtilen eşiği uygula. Eşik yoksa önce kullanıcıya önerilen varsayımı sor; kritik kategorileri eşiğe takıp eleme.

Eşik uygulanmaması gereken tipik başlıklar:

- şirketin varlığı, temsil yetkisi, pay sahipliği ve sermaye yapısı,
- tescil/ilan veya organ kararı eksiklikleri,
- Rekabet Kurumu, SPK/KAP/MKK veya sektör izni ihtimali,
- KVKK ve yurt dışına veri aktarımı,
- fikri mülkiyet sahipliği,
- devam eden önemli dava/icra/idari soruşturma,
- çalışan devri, toplu iş hukuku veya kilit çalışan riski,
- işlem kapanışını engelleyebilecek izin, onay, sözleşme devri veya teminat.

Belge hacmi büyükse batch işle:

```text
Batch kapsamı: [kategori / klasör / belge aralığı]
Okunan: [N]
Atlanan: [N ve neden]
Kritik bulgu: [var/yok]
```

## Step 3 - Kategori bazlı risk çıkarımı

### Kurumsal kayıtlar

Kontrol et:

- ticaret sicili, MERSİS, TTSG ilanları ve şirket unvanı tutarlılığı,
- esas sözleşme/şirket sözleşmesi özel hükümleri,
- sermaye, pay sahipliği, pay defteri, imtiyaz ve intifa hakları,
- yönetim kurulu/müdürler kurulu/genel kurul karar zinciri,
- imza sirküleri, iç yönerge, temsil yetkisi ve vekaletname,
- tescil/ilan gerektiren geçmiş kararların tamamlanıp tamamlanmadığı,
- grup içi işlemler, hakim şirket/bağlı şirket veya ilişkili taraf hassasiyeti.

### Önemli sözleşmeler

Kontrol et:

- devir, temlik, alt sözleşme ve kontrol değişikliği hükümleri,
- fesih, yenileme, ihbar, münhasırlık, rekabet yasağı ve müşteri/çalışan ayartmama,
- teminat, kefalet, garanti, teminat mektubu, rehin/ipotek bağlantısı,
- cezai şart, sorumluluk sınırı, tazminat ve fahiş cezai şart riski,
- fiyat artışı, kur farkı, ticari faiz, ödeme vadeleri, damga vergisi etkisi,
- uygulanacak hukuk, yetkili mahkeme/icra dairesi, tahkim ve dil,
- kritik müşteri/tedarikçi kaybı veya kapanış öncesi onay ihtiyacı.

### KVKK ve veri

Kontrol et:

- veri sorumlusu/veri işleyen rolleri,
- veri işleme sözleşmesi veya veri aktarım eki,
- özel nitelikli veri,
- yurt dışına aktarım,
- VERBİS ve envanter durumu,
- ihlal kayıtları, Kurul yazışmaları, veri sahibi başvuruları,
- kapanış veya entegrasyon sonrası veri aktarımı ve erişim planı.

### Rekabet hukuku

Kontrol et:

- birleşme/devralma izni ihtimali ve işlem kapanışına etkisi,
- rakipler arası hassas bilgi paylaşımı,
- münhasırlık, rekabet yasağı, MFN, bölge/müşteri sınırlaması,
- ortak girişim, kontrol değişikliği veya fiili kontrol unsurları,
- Rekabet Kurumu inceleme/soruşturma geçmişi.

Eşik veya bildirim gerekliliği konusunda güncel resmi kaynak kontrol edilmeden kesin "izin gerekir/gerekmez" deme; "kontrol edilmeli" olarak işaretle.

### Çalışanlar ve SGK

Kontrol et:

- kilit çalışan sözleşmeleri, rekabet yasağı, gizlilik ve fikri hak devirleri,
- işçilik alacakları, fazla mesai, prim, yan hak, SGK ve bordro riskleri,
- işyeri devri veya çalışan geçişi ihtimali,
- toplu iş sözleşmesi, sendika, iş sağlığı ve güvenliği, iş kazası,
- devam eden iş davaları, arabuluculuk son tutanakları ve ihtarnameler.

### Vergi, finansman ve teminatlar

Kontrol et:

- vergi incelemesi, uzlaşma, ceza veya yapılandırma,
- damga vergisi, KDV, stopaj ve işlem vergisi etkileri,
- kredi sözleşmeleri, finansal kısıtlar, temerrüt, erken ödeme,
- teminat, kefalet, garanti, rehin, ipotek, haciz ve takyidat,
- kapanışta kaldırılması veya devri gereken teminatlar.

### Fikri mülkiyet ve teknoloji

Kontrol et:

- marka, patent, tasarım, alan adı ve yazılım sahipliği,
- çalışan/yüklenici FSEK ve fikri hak devirleri,
- lisansların devredilebilirliği,
- açık kaynak kullanımı ve copyleft riski,
- üçüncü kişi ihlal iddiaları, ihtarnameler ve davalar.

### Taşınmaz, ruhsat ve sektör izinleri

Kontrol et:

- tapu, kira, kullanım hakkı, takyidat ve ipotek,
- çevre, belediye, işyeri açma, üretim, ithalat/ihracat veya sektör ruhsatları,
- ruhsatın işlem sonrası devri, yenilenmesi veya bildirimi,
- BDDK, SPK, BTK, EPDK, Sağlık Bakanlığı, Ticaret Bakanlığı veya diğer kurum etkisi.

### Uyuşmazlıklar

Kontrol et:

- dava, icra, tahkim, arabuluculuk, idari soruşturma ve ihtarnameler,
- UYAP/esas no, taraflar, dava konusu, talep tutarı ve aşama,
- ihtiyati tedbir/haciz, teminat, uzlaşma ve sulh ihtimali,
- finansal karşılık/rezerv ve sözleşmesel tazminat bağlantısı,
- kapanış koşulu veya satın alma sözleşmesi beyan/garanti etkisi.

## Step 4 - Bulguyu yaz

Her bulgu kaynaklı olmalı. Belge kaynağı yoksa bulgu yazma; "eksik belge / doğrulanmalı" olarak göster.

Kaynak etiketleri:

- `[belge kaynağı]`: VDR yolu, dosya adı, sayfa, madde, tarih.
- `[kullanıcı sağladı]`: kullanıcı beyanı veya yüklediği kayıt.
- `[resmi kaynak]`: bu oturumda kontrol edilen mevzuat, KAP, MKK, ticaret sicili, Kurum duyurusu.
- `[model bilgisi - doğrula]`: kaynak çekilmeden kullanılan genel bilgi.

Bir kanun maddesi, eşik, süre veya resmi uygulama güncellik gerektiriyorsa resmi kaynak kontrol edilmeden kesin sonuç çıkarma.

Varsayılan bulgu formatı:

```markdown
Issue #[N]: [Kısa başlık]
Kategori: [Kurumsal / Sözleşmeler / KVKK / Rekabet / Çalışan / Vergi / IP / Ruhsat / Uyuşmazlık]
Önem: [Kırmızı / Sarı / Yeşil]
Kaynak: [VDR yolu + belge adı + madde/sayfa]
Bulgu: [Belgenin ne söylediği ve işlem için neden önemli olduğu]
İşlem etkisi: [değer / yapı / kapanış koşulu / tescil / izin / sözleşme onayı / entegrasyon / takip]
Önerilen aksiyon: [ek belge iste / kapanış şartı / özel tazmin / beyan-garanti / fiyat ayarı / dış danışman / izleme]
Doğrulanacak: [resmi kaynak, esas sözleşme, imza yetkisi, eşik, uzman görüşü]
```

House memo formatı profilde farklıysa onu kullan.

## Önem derecesi

Profildeki şemayı kullan. Yoksa:

- **Kırmızı:** İşlem yapısını, fiyatı, kapanışı, izin/tescil sürecini veya temel beyan/garantileri etkileyebilir.
- **Sarı:** Çözülebilir ama kapanıştan önce aksiyon, belge, onay, tescil, düzeltme veya özel sözleşme koruması gerektirir.
- **Yeşil:** Dosya için not; izlenmeli ama mevcut bilgiyle işlem kararını belirgin etkilemez.

Close call durumunda düşük göstermeyip `[review]` etiketiyle hukukçu kararına bırak.

## Step 5 - Kategori raporu

```markdown
GİZLİ HUKUKİ ÇALIŞMA TASLAĞI - AVUKAT/HUKUKÇU İNCELEMESİNE TABİDİR

# Due Diligence Bulguları: [İşlem kodu] - [Kategori]

Reviewer note
- Kaynaklar: [okunan VDR klasörleri/belgeler]
- Okuma kapsamı: [N/M belge; eşik; atlananlar]
- Doğrulanması gerekenler: [TTK, sicil, esas sözleşme, KVKK, Rekabet, SPK, vergi, uzman]
- Aksiyon öncesi: [kapanış şartı / tescil / izin / bildirim / sözleşme onayı]

## Bottom line

[Kırmızı N · Sarı N · Yeşil N] - [deal ekibinin bilmesi gereken ana sonuç]

## Bulgular

[Bulgu listesi]

## Eksik belgeler / takip soruları

- [Talep listesinde olup VDR'da bulunmayan belge]
- [Belgede atıf yapılan ama yüklenmemiş ek]
- [Resmi kaynak veya uzman kontrolü gereken konu]
```

## Handofflar

### Closing checklist

Şu bulgular kapanış listesine gönderilir:

- Rekabet Kurumu, SPK/KAP/MKK veya sektör izni/bildirimi,
- ticaret sicili tescil/ilan, MERSİS veya karar defteri işlemi,
- genel kurul, yönetim kurulu, müdürler kurulu veya pay sahibi kararı,
- imza sirküleri, temsil yetkisi, vekaletname veya iç yönerge düzeltmesi,
- sözleşme devri, karşı taraf onayı, teminat/kefalet/garanti kaldırma,
- finansman erken ödeme, rehin/ipotek/haciz fekki,
- KVKK aktarım, veri işleme sözleşmesi veya entegrasyon öncesi izin,
- çalışan geçişi, işyeri devri, SGK veya bordro kapanış aksiyonu,
- ruhsat/lisans devri veya kurum bildirimi,
- dava/icra/tahkim için sulh, feragat, ibra veya teminat aksiyonu.

Belirsizse de handoff yap ve "hukukçu kararına bağlı" etiketi koy.

### Material contract schedule

Önemli sözleşme bulguları şu alanlarla aktarılır:

```yaml
sozlesme:
  karsi_taraf:
  tur:
  tarih:
  yillik_deger_tl:
  devir_onayi: gerekli | degil | belirsiz
  kontrol_degisikligi: var | yok | belirsiz
  fesih_riski: var | yok | belirsiz
  teminat_kefalet: var | yok | belirsiz
  rekabet_kisitlari: var | yok | belirsiz
  kvkk_veri: var | yok | belirsiz
  kapanis_aksiyonu:
  kaynak:
```

### Deal-team summary

Kırmızı ve önemli sarı bulguları iş birimi diline sadeleştir; mesleki sır veya strateji notunu gereksiz yayma.

### AI tool handoff

Kira/Luminance veya benzeri bulk review aracı varsa yüksek hacimli sözleşme taramasını oraya yönlendir. Bu skill karar katmanını, kaynak kontrolünü ve Türk hukuku risk sınıflandırmasını üstlenir.

## Büyük dosya uyarısı

50+ belge, 100+ sayfa veya çok kategorili VDR varsa okuma kapsamını açık yaz. Tam okumadığın belge seti için "tüm VDR temiz" gibi sonuç üretme. Kapsam dışı kalanları ayrı listele.

## Kapanış

Raporu şu seçeneklerle kapat:

1. **Kapanış listesine aktar** - kapanış öncesi aksiyonları `closing-checklist` formatına dönüştür.
2. **Eksik belge talebi hazırla** - VDR eksiklerini talep listesi olarak yaz.
3. **Deal-team summary hazırla** - iş birimi için kısa karar özeti üret.
4. **Material contract schedule üret** - sözleşme bulgularını çizelgeye aktar.
5. **Dış danışmana eskale et** - uzman kontrolü gereken konular için kısa not yaz.

## Bu skill ne yapmaz

- Belgede olmayan olguyu bulgu gibi yazmaz.
- Rekabet izni, SPK/KAP yükümlülüğü, vergi sonucu veya tescil gerekliliği konusunda güncel resmi kaynak kontrolü olmadan kesin karar vermez.
- Kapanış şartlarını tek başına belirlemez; satın alma/yatırım sözleşmesi ve hukukçu kararı gerekir.
- Sözleşme müzakeresi, beyan-garanti veya tazminat metnini nihai hale getirmez.
- Bulk review aracının yerine geçmez; yüksek hacimli çıkarımlarda araç çıktısını QA ve hukukçu muhakemesiyle değerlendirir.

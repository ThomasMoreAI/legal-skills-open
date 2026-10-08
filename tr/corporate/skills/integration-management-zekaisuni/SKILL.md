---
name: integration-management-zekaisuni
title: /integration-management
description: Kapanış sonrası (post-closing) M&A entegrasyon takibi — aşamalı iş planı, onay (consent) takibi, geniş çaplı sözleşme devirleri (assignment), haftalık durum raporları. Mevcut işlem (deal) belgelerinden (SPA, işlem özeti, kapanış kontrol listesi) başlatılır ve M&A başlangıcındaki deal-context.md ile closing-checklist.yaml'a bağlanır. Kullanıcı "entegrasyon", "kapanış sonrası", "bekleyen onaylar", "sözleşme devirleri", "entegrasyon durumu" veya "işlemde ne kaldı" dediğinde kullanın.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/corporate-legal/skills/integration-management
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: corporate
language: tr
---

# /integration-management

1. `deal-context.md` dosyasını yükle (işlem kodu, hedef şirket, kapanış tarihi, işlem lideri).
2. Varsa `integration-tracker.yaml` dosyasını yükle (veya --init ile oluştur).
3. Aşağıdaki iş akışını kullan.
4. Parametreye (flag) göre yönlendir:
   - `--init`: Mod 1 — SPA'yı oku, aşamalı iş planı ve onay (consent) takipçisi oluştur
   - `--contracts`: Mod 2 — Sözleşme listesini içe aktar (depo veya yükleme), sınıflandır
   - `--report`: Mod 3 — Durum raporu üret
   - `--update`: Mod 4 — Manuel güncelleme veya yüklenen durum belgesini ayrıştırma
   - `--export`: Mod 5 — CSV veya tablo dışa aktarımı
5. `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[kodu]/integration-tracker.yaml` dosyasını oku/yaz.
6. Herhangi bir yazma işleminden sonra: Değişiklik özetini göster ve yeni işaretlenen (flag) durumları bildir.

---

## Dosya Bağlamı (Matter Context)

**Dosya Bağlamı.** Büro düzeyindeki CLAUDE.md dosyasında `## Matter workspaces` bölümünü kontrol et. Eğer `Enabled` durumu `✗` ise (kurum içi hukukçular için varsayılan), bu paragrafı atla. Eğer aktifse ve açık bir dosya (matter) yoksa şunu sor: "Bu hangi dosya için? `/corporate-legal:matter-workspace switch <slug>` komutunu çalıştır veya `buro-geneli` de." Aktif dosyanın `matter.md` içeriğini bağlam ve özel talimatlar için yükle. Çıktıları dosya klasörüne (`~/.claude/plugins/config/claude-for-legal/corporate-legal/matters/<dosya-slug>/`) yaz. `Cross-matter context` açık değilse asla başka bir dosyanın verisini okuma.

---

## Amaç

Dışarıdan hizmet alınan hukuk bürosu (outside counsel) işlemi kapatır (closing). Şirket içi hukuk birimi (legal) ise arkada kalan süreci devralır. Bu skill, kapanış sonrası entegrasyonun — iş, IT veya İK organizasyonel tasarımı değil, **hukuki entegrasyonun** — program yönetimi katmanıdır. Hukuki iş akışları: Onaylar (consents), sözleşme devirleri (assignments), şirket/grup içi yeniden yapılandırma (entity rationalization), Fikri Mülkiyet (IP) tescilleri, SPA yükümlülükleri. Nelerin yapıldığını, neyin vadesinin geldiğini, nelerin tıkandığını ve ne kararlar alınması gerektiğini takip eder.

---

## Takip Dosyası (Tracker)

Konumu: `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[kodu]/integration-tracker.yaml`. 
İşlem kodu, hedef şirket adı, kapanış tarihi ve işlem lideri için `deal-context.md` dosyasını oku. Kapanış sonrası (post-close) maddelerini varsa `closing-checklist.yaml` dosyasından miras al.

Yapısal veri standardı için corporate `CLAUDE.md` dosyasındaki `## Yapısal veri standardı` bölümünü uygula. Bu tracker'da YAML anahtarları canonical ASCII `english_snake_case` olarak kalır; mevcut kontrollü enum değerleri ASCII makine token'ı olarak korunur. Kullanıcıya görünen rapor, tablo ve durum özeti başlıkları Türkçe yazılır.

```yaml
# integration-tracker.yaml

metadata:
  deal_code: "[kodu]"
  target: "[şirket adı]"
  close_date: "[YYYY-MM-DD]"
  deal_lead: "[isim]"
  outside_counsel: "[büro ve sorumlu avukat]"
  last_updated: "[tarih]"
  last_status_report: "[tarih veya null]"

pa_dates:
  required_consents_deadline: "[YYYY-MM-DD — SPA'dan çıkar]"
  rep_survival_expires: "[YYYY-MM-DD]"
  escrow_release: "[YYYY-MM-DD veya null]"
  earnout_milestones:
    - description: "[kilometre taşı]"
      measurement_date: "[YYYY-MM-DD]"
      payment_date: "[YYYY-MM-DD]"
      owner: "finance"   # her zaman finans birimi — hukuk sadece tarihi takip eder

workplan:
  day_1:
    target_date: "[close_date + 7 gün]"
    items: []
  day_30:
    target_date: "[close_date + 30 gün]"
    items: []
  day_90:
    target_date: "[close_date + 90 gün]"
    items: []
  day_180:
    target_date: "[close_date + 180 gün]"
    items: []

required_consents: []
desired_consents: []

contracts:
  source: "[repository / manual-upload / disclosure-schedule]"
  repository_path: "[yol veya null]"
  last_imported: "[tarih]"
  total: 0
  tier_1: []
  tier_2: []
  tier_3: []
  tier_4: []
```

**İş Planı (Workplan) Öğesi Yapısı:**
```yaml
- id: "W-001"
  description: "[aksiyon]"
  phase: "[day_1 / day_30 / day_90 / day_180]"
  owner: "[legal-owns / legal-supports]"
  workstream: "[legal / hr / it / finance / real-estate / other]"
  priority: "[critical / high / medium / low]"
  deadline: "[YYYY-MM-DD veya null]"
  deadline_basis: "[pa-obligation / regulatory / best-practice]"
  status: "[not_started / in_progress / complete / blocked / deferred]"
  blocker: "[açıklama veya null]"
  depends_on: "[öğe id veya null]"
  notes: ""
```

**Onay (Consent) Öğesi Yapısı:**
```yaml
- id: "CON-001"
  counterparty: "[isim]"
  contract_type: "[customer / vendor / lease / IP-license / financial / other]"
  required_consent: true        # true = SPA Gerekli Onaylar ekinde belirtilmiş
  pa_deadline: "[YYYY-MM-DD]"   # sadece required_consent: true ise
  status: "[not_started / outreach_sent / in_negotiation / obtained / waived / refused]"
  assigned_to: "[isim veya null]"
  outreach_date: "[tarih veya null]"
  obtained_date: "[tarih veya null]"
  notes: ""
```

**Sözleşme Öğesi Yapısı:**
```yaml
- id: "C-001"
  name: "[sözleşme adı veya dosya adı]"
  counterparty: "[taraf adı]"
  contract_type: "[MSA / SaaS / lease / IP-license / employment / NDA / other]"
  annual_value: "[tutar veya unknown]"
  assignment_mechanism: "[auto-assign / consent-required / coc-provision / silent]"
  tier: 1   # 1=Required Consent, 2=material+consent-required, 3=CoC, 4=auto-assign
  required_consent: false
  pa_deadline: "[YYYY-MM-DD veya null]"
  status: "[not_reviewed / no_action / consent_pending / outreach_sent / in_negotiation / consent_obtained / assignment_complete / waived / refused / coc_triggered]"
  assigned_to: "[isim veya null]"
  notes: ""
  last_updated: "[tarih]"
```

---

## Mod 1: Başlatma (Initialize)

```
/corporate-legal:integration-management --init [--deal [kodu]]
```

### Adım 1: Dosya Bağlamını Yükle

`~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[kodu]/deal-context.md` oku. Bulunamazsa: işlem kodu, hedef şirket, kapanış tarihi, işlem lideri ve dışarıdan hizmet alınan büro (outside counsel) bilgilerini sor. Yoksa `deal-context.md` oluştur ve yaz.

Varsa `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[kodu]/closing-checklist.yaml` dosyasını oku. Kapanış sonrası (post-closing) olarak işaretlenen tüm öğeler, 1. Gün veya 30. Gün iş planı öğesi haline gelir (durumları kapanış kontrol listesinden miras alınır).

### Adım 2: İşlem Girdilerini Oku

**Tam bir Devir Sözleşmesi (SPA) en eksiksiz takipçiyi (tracker) üretir.** SPA'nın Gerekli Onaylar (Required Consents) eki ve kapanış sonrası (post-closing covenants) bölümü, kesin tarihler ve yasal yükümlülükler için en yetkili kaynaktır. Ancak bu skill mevcut herhangi bir veriden de faydalı bir başlangıç yapabilir — kısmi girdiler, boş bir sayfa yerine avukatın doldurabileceği taslak bir takipçi üretir.

> Elinizde hangi işlem (deal) belgeleri var? Ne varsa paylaşın:
>
> **İdeal:** Devir sözleşmesi (SPA/APA) (yükleyin veya bağlı dosya yolunu verin). Kapanış sonrası yükümlülükleri, Gerekli Onaylar ekini, beyan/tekeffül zamanaşımı sürelerini, emanet (escrow) hesap şartlarını ve ek ödeme (earn-out) hükümlerini okuyacağım.
>
> **Ayrıca Faydalı — aşağıdakilerin herhangi bir kombinasyonunu paylaşabilirsiniz:**
> - İşlem Özeti (Deal summary) veya Ön Protokol (Term sheet) (bana temel ekonomiyi ve zaman çizelgesini verir)
> - Dışarıdan danışılan hukuk bürosunun hazırladığı entegrasyon "yapılacaklar" (to-do) listesi veya kapanış sonrası kontrol listesi
> - Mevcut bir iş planı veya entegrasyon takipçisi (içe aktarır ve oradan devam ederim)
> - Kapanış Kontrol Listesi — eğer M&A başlangıç (cold-start) skill'i tarafından oluşturulduysa, onu `~/.claude/plugins/config/claude-for-legal/corporate-legal/deals/[kodu]/closing-checklist.yaml` yolundan otomatik alırım.
> - Yalnızca Gerekli Onaylar (Required Consents) listesi
>
> **Elinizde yazılı hiçbir şey yoksa:** Bana işlemi sade bir dille anlatın — kim devralındı, ne zaman kapandı, ana açık konular neler — ben de sizin sonradan düzenleyeceğiniz standart bir 1/30/90/180 Gün iş planı taslağı oluşturayım.

**Sağlanan Veriye Göre Değişenler:**

| Girdi | Elde Edilecek Çıktı |
|---|---|
| Tam SPA | Eksiksiz iş planı + Tarihli Gerekli Onaylar listesi + SPA tarihleri |
| SPA + Sözleşme Listesi | Tam takipçi (tracker) + Sözleşme devir kademe (tier) listesi |
| İşlem Özeti / To-do list | Standart iş planı iskeleti, Gerekli Onaylar taslağı |
| Hiçbir Şey | Standart iş planı iskeleti; avukat onayları ve sözleşme listelerini kendi doldurur |

### Adım 3: Aşamalı İş Planını Oluştur

Her aşama için standart iş planı kalemleri oluştur. 2. Adımda çıkarılan SPA yükümlülüklerini ekle. Kapanış kontrol listesinden (closing checklist) miras alınan kalemleri önceden doldur.

**1. Gün — legal-owns (Hukukun Sorumluluğunda):**
- Şirket unvan değişikliği tescili (devralınan şirketin adı değişiyorsa - MERSİS/Ticaret Sicil) [öncelik: kritik]
- Banka hesabı imza yetkilisi güncellemeleri — kapanış evraklarıyla bankaya bildirim [öncelik: kritik]
- Varsa Ticaret Sicil ve Vergi Dairesi sahiplik/ortaklık değişikliği bildirimleri [öncelik: yüksek]
- Önemli Fikri Mülkiyet (IP) devir sözleşmelerinin imzalanması (kapanıştan sonraya bırakıldıysa) [öncelik: kritik]
- Alan adı (Domain) ve sosyal medya hesap transferleri [öncelik: yüksek]
- Yönetici Sorumluluk Sigortası (D&O) — devralınan şirketin yöneticileri için kuyruk (tail) poliçesinin yapıldığının teyidi [öncelik: kritik]
- Sektörel veya yerel idari makam (Belediye vb.) sahiplik bildirimleri [öncelik: yüksek]

**1. Gün — legal-supports (Hukukun Destek Verdiği):**
- Çalışanlara duyuru ve iletişimler (İK yürütür, hukuk inceler) [öncelik: kritik]
- Yan haklar ve SGK işyeri devir/giriş bildirimleri (İK yürütür, hukuk İş Kanunu ve SGK mevzuatı açısından danışmanlık yapar)
- Müşteri iletişim yazıları (İş birimi yürütür, hukuk doğruluğunu inceler)

**30. Gün — legal-owns:**
- Gerekli Onaylar (Required Consents) ilk iletişim — tüm karşı taraflarla iletişime geç, kayıt altına al [öncelik: kritik]
- TÜRKPATENT nezdinde Marka ve Patent devir tescilleri [öncelik: yüksek]
- Telif (FSEK) devir bildirimleri [öncelik: orta]
- Önemli sözleşme incelemesi — Tier 1 ve Tier 2 sözleşme devir (assignment) analizini tamamla [öncelik: yüksek]
- Sigorta kuyruk (tail) poliçesi nihai onayı [öncelik: yüksek]

**30. Gün — legal-supports:**
- Veri göçü/aktarımı gizlilik (KVKK) incelemesi (IT yürütür, hukuk KVKK m.8/9 veri aktarımı açısından danışmanlık yapar)
- Gayrimenkul kira sözleşmelerinin devir (assignment) hükümleri açısından incelenmesi (İdari İşler yürütür, hukuk destekler)

**90. Gün — legal-owns:**
- Gerekli Onaylar (Required Consents) son tarihi — tüm Gerekli Onaylar alınmış veya üst makama taşınmış olmalıdır [öncelik: kritik, son tarih: pa_dates.required_consents_deadline]
- Grup İçi Yeniden Yapılandırma (Entity Rationalization) kararı — ayrı tut / birleştir (merger) / tasfiye et (dissolve) tavsiyesi ver [öncelik: yüksek]
- Çalışan yan hak planlarının devralınması veya feshi evrakları [öncelik: yüksek]
- İkincil onay süreci — geriye kalan bekleyen onaylar [öncelik: yüksek]
- Tier 3 Kontrol Değişikliği (CoC) sözleşmelerinin çözümlenmesi [öncelik: kritik]

**90. Gün — legal-supports:**
- Kapsamlı İK uyumlandırma dokümantasyonu (İK yürütür, hukuk İş Kanunu tavsiyesi verir)

**180. Gün — legal-owns:**
- Birleşme (Merger) tescili — yeniden yapılandırma kararı birleşme yönündeyse (TTK m.136 vd.) [öncelik: yüksek]
- Şirket tasfiyesi (Dissolution) tescili — karar tasfiye yönündeyse [öncelik: yüksek]
- Tam sözleşme yenilemesi (Novation/TBK m.205) — devralan isminin geçmesi gereken sözleşmeler [öncelik: yüksek]
- Beyan ve Tekeffül (Rep survival) takibi — yaklaşan zamanaşımı tarihlerini not al [öncelik: orta]

Oluşturduktan sonra özeti göster:

```
Entegrasyon takipçisi başlatıldı — [İşlem Kodu] / [Hedef Şirket]

Kapanış Tarihi: [tarih]
Gerekli Onaylar Son Tarihi: [tarih] (Bugünden itibaren [N] gün)
Beyan (Rep) Zamanaşımı: [tarih]

İş Planı Öğeleri: [N] ([N] hukuk-yürütür, [N] hukuk-destekler)
Gerekli Onaylar: [N] (SPA ekinden)
İstenen Onaylar: [N] (diligence raporundan — SPA son tarihi yok)

Sözleşme Devirleri: henüz içe aktarılmadı — doldurmak için --contracts çalıştırın

Sonraki adım: Sözleşme listesini aktarmak için /corporate-legal:integration-management --contracts komutunu, ardından ilk durum özetinizi görmek için --report komutunu çalıştırın.
```

---

## Mod 2: Sözleşme Devri (Contract Assignment)

```
/corporate-legal:integration-management --contracts [--deal [kodu]]
```

Sözleşme listesi elde edildiğinde sınıflandırma (assignment) mekanizmasını belirle.

| Mekanizma | Tanım | Tier |
|---|---|---|
| `consent-required` | Karşı tarafın rızası olmadan devri (TBK m.205) yasaklayan açık hüküm | 1 veya 2 |
| `coc-provision` | Kapanışla tetiklenen, karşı tarafa fesih veya rıza hakkı veren Kontrol Değişikliği (CoC) hükmü | 3 |
| `auto-assign` | Kısıtlama yok veya iştiraklere/haleflere açıkça devir yetkisi verilmiş | 4 |
| `silent` | Devir hükmü yok — yürürlükteki hukukun varsayılan kuralları geçerli (örn. TBK genel kuralları). Hüküm bulunmadığında sözleşme devri kurallarını araştır ve ilgili kuralı (örn. TBK m.205 uyarınca karşı taraf onayı) alıntıla. Avukat incelemesi için işaretle. | 2 |
| `not_reviewed` | Devir/Assignment maddesi okunamadı veya bulunamadı | Manuel inceleme için işaretle |

Required Consents (Gerekli Onaylar) SPA ekinde işaretlenen sözleşmelerin mekanizması ne olursa olsun kademesi (tier) 1 olarak ayarlanır.

---

## Mod 3: Durum Raporu (Status Report)

```
/corporate-legal:integration-management --report [--deal [kodu]]
```

Mevcut tracker durumunu okur. Aşağıdaki raporu üretir:

```
GİZLİ HUKUKİ ÇALIŞMA TASLAĞI - AVUKAT/HUKUKÇU İNCELEMESİNE TABİDİR

> Bu durum raporu, Devir Sözleşmesi (SPA), due diligence bulguları ve kapanış sonrası entegrasyon kayıtlarından elde edilmiştir. Avukat-müvekkil gizliliğini (Av. K. m.36) miras alır — gizlilik çemberinin dışına dağıtılması sır saklama yükümlülüğünü ihlal edebilir. Göndermeden önce alıcı listesini onaylayın.

ENTEGRASYON DURUMU — [İşlem Kodu] / [Hedef Şirket]
[Tarih] — Kapanış sonrası [N]. Gün

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YÖNETİCİ ÖZETİ
[2-3 cümlelik paragraf: genel durum, en büyük risk, son rapordan bu yana elde edilen önemli başarı]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GEREKLİ ONAYLAR (REQUIRED CONSENTS)  [Son Tarih: TARİH — Kalan gün: N]
  Alınan:          [N] / [toplam]  ████████░░  [%]
  Müzakerede:      [N]
  İletişim Kurulan:[N]
  Başlanmayan:     [N]
  Reddedilen:      [N] ⚠️

⚠️ RİSKTE: [karşı_taraf] — son tarihe [N] gün kaldı, iletişime yanıt yok
⚠️ REDDEDİLDİ: [karşı_taraf] — SPA yükümlülüğü karşılanmadı; hukuk bürosuna bildirin

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SÖZLEŞME DEVİRLERİ (CONTRACT ASSIGNMENT)
  Tier 1 (Gerekli Onaylar):    [N] tamamlandı / [N] devam ediyor / [N] bekliyor
  Tier 2 (Önemli sözleşmeler): [N] tamamlandı / [N] devam ediyor / [N] bekliyor
  Tier 3 (CoC hükümleri):      [N] çözüldü / [N] bekleyen ⚠️
  Tier 4 (Otomatik-Devir):     [N] — eylem gerekmiyor

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

İŞ PLANI — HUKUK YÜRÜTÜR (LEGAL OWNS)
  🔴 GECİKEN ([N]):
    [öğe] — son tarih [tarih]

  ⏰ BU HAFTA BEKLENEN ([N]):
    [öğe] — son tarih [tarih]

  ✅ SON RAPORDAN BERİ TAMAMLANAN ([N]):
    [öğe] — tamamlanma [tarih]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENGELLEYİCİLER & KARAR GEREKENLER (BLOCKERS)
  [öğe] — engel nedeni: [açıklama] — sorumlu: [isim]
  [öğe] — karar gerekiyor: [açıklama] — öneri: [seçenek]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YAKLAŞAN ÖNEMLİ TARİHLER
  [tarih] — [kilometre taşı / son tarih]
  [tarih] — Beyan/Tekeffül Zamanaşımı (Rep survival expires) — bekleyen tazminat talebi olmadığını doğrulayın

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Mod 4: Güncelle (Update)

```
/corporate-legal:integration-management --update [--deal [kodu]]
```

**Manuel güncelleme:** Avukat Claude'a neyin değiştiğini söyler. (Örn: "Salesforce onayını aldık. Alındı olarak işaretle.")

**Yükleme ile güncelleme:** İşlem sahibi veya danışman hukuk bürosu bir durum raporu gönderir.

> [Dış büro / İK lideri / Corp Dev] tarafından gönderilen durum güncellemesini yükleyin.
> Ayrıştırıp takipçiyi güncelleyeceğim.

Yüklenen belgeyi okuyun. Açıklanan kalemleri, karşı taraf adına veya iş planı öğesi açıklamasına göre takipçi (tracker) kayıtlarıyla eşleştirin. Durum alanlarını güncelleyin.
Mevcut bir takipçi kaydıyla eşleşmeyen yüklemedeki öğeleri işaretleyin — bunlar eklenecek yeni kalemler olabilir.

Herhangi bir güncellemeden sonra şunu gösterin:
```
[N] öğe güncellendi.

Değişiklikler:
  CON-003 Salesforce: not_started → obtained
  W-014 Entity rationalization: in_progress → complete

Yeni İşaretler:
  CON-007 [Karşı taraf]: refused — SPA yükümlülüğü karşılanmamış olabilir. Şunu değerlendirin:
  Tazminat talebi (indemnification claim) için danışman hukuk bürosu incelemesi. ⚠️
```

---

## Mod 5: Dışa Aktar (Export)

```
/corporate-legal:integration-management --export [--format csv|table] [--section all|consents|contracts|workplan]
```

Dışarıdan destek veren büro (outside counsel), kurumsal gelişim (corp dev) veya yönetim kurulu entegrasyon güncellemesi için düz CSV veya markdown tablosu üretir. Varsayılan: tüm bölümler, CSV.

CSV formatı — her öğe için bir satır, bölüm (section) sütunu ile belirtilir. CSV kolonları makine aktarımı için canonical alan adlarıdır; markdown tablo veya yönetim raporu istenirse aynı veriyi Türkçe başlıklarla göster.
Sütunlar bölüme göre değişir:

*İş Planı (Workplan):* id, phase, description, owner, workstream, priority, deadline, status, blocker
*Onaylar (Consents):* id, counterparty, contract_type, required_consent, pa_deadline, status, assigned_to, obtained_date, notes
*Sözleşmeler (Contracts):* id, name, counterparty, contract_type, annual_value, assignment_mechanism, tier, required_consent, pa_deadline, status, assigned_to, notes

---

## Bu Skill Ne Yapmaz?

- İş birimlerine ait entegrasyon süreçlerini (IT, İK, finans, emlak) yönetmez. Hukukun bu alanlardaki temas noktalarını takip eder ve hukuki girdi gerektiğinde uyarır. Sahiplik ilgili iş biriminde kalır.
- Onay talep mektuplarını veya yenileme/devir (novation) sözleşmelerini bizzat taslaklaştırmaz — bunlar `written-consent` skill'i veya dışarıdan destek veren büro tarafından üretilir.
- SPA ihlali veya tazminat (indemnification) talepleri konusunda tavsiye vermez. Bir onay reddedildiğinde veya bir son tarih kaçırıldığında durumu işaretler — yasal sonuçların analizi avukatın yetkisindedir.
- Ek ödeme (earn-out) performansını takip etmez. İşletme rakamları takip eder.
- Durum raporu sırasında gerçek zamanlı olarak sözleşmeleri tekrar okumaz. Hukukçunun takipçiye (tracker) güncellediği durumu temel alır.

## Formül Enjeksiyon Koruması (Formula injection defense)

Excel, Sheets veya CSV çıktısında herhangi bir hücreyi yazmadan önce, formül enjeksiyonunu (formula injection) etkisiz hale getirin. Karşı taraf kaynaklı metinler (sözleşme alıntıları, taraf adları vb.) dışarıdan kontrol edilen verilerdir. `=`, `+`, `-`, `@`, `\t` veya `\r` ile başlayan bir hücre, formül olarak yorumlanacak veya satır yapısını bozacaktır.

- **Tek tırnak işareti ile başlatın:** `'=SUM(A1:A10)` → `=SUM(A1:A10)` (Çalıştırılmaz, metin olarak görüntülenir)
- Bu kural, bir belgeden, bir araç sonucundan veya bir kullanıcının kopyala-yapıştır işleminden alınan metni içeren her hücre için geçerlidir. Kontrol ettiğiniz sütun başlıkları ve ürettiğiniz hesaplanmış değerler güvenlidir.
- **CSV: Ayrıca gömülü virgülleri, çift tırnakları ve yeni satırları kaçış dizisiyle belirtin (escape)** (RFC 4180 alıntılaması).

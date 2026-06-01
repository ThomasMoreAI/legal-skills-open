---
name: privilege-log-review-zekaisuni
title: /privilege-log-review (Gizlilik ve Sır Saklama İncelemesi)
description: Sır saklama ve gizlilik (privilege) incelemesi — mahkemeye, savcılığa veya Rekabet Kurumu'na sunulacak belgeler arasında Avukat-Müvekkil Gizliliğine (Av.K. m.36) veya ticari sırra girenleri tespit eder, net olanları ayırır ve şüpheli olanları avukat incelemesi için bayraklar (flag). Kullanıcı "bu belgelerde gizlilik/sır incelemesi yap", "privilege log'u kontrol et" veya kuruma teslim öncesi QA yapmak istediğinde kullanın.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/litigation-legal/skills/privilege-log-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: litigation
language: tr
---

# /privilege-log-review (Gizlilik ve Sır Saklama İncelemesi)

1. `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` yükle → inceleme protokolü, log formatı.
2. Aşağıdaki iş akışını ve referansları izle.
3. Her belge/girdi için: kesin gizli (priv) / kesin gizli değil / avukat incelemesi (şüpheli). Nedenlerini işaretle.
4. Çıktı: Bayraklanmış inceleme listesi. Sunumdan önce avukat tüm bayrakları inceler.

---

# Sır Saklama ve Gizlilik İncelemesi (Privilege Log Review)

## Hukuki Bağlam (Jurisdiction & Context)

ABD'deki geniş "Discovery" (Keşif) aşaması ve detaylı "Privilege Log" (Gizli belgeler kütüğü) kurumu Türk Hukukunda birebir bulunmasa da, kurum (özellikle Rekabet Kurumu, SPK) veya mahkeme/savcılık incelemelerinde şirket içinden veri toplandığında **Avukat-Müvekkil Gizliliği (Av.K. m.36, CMK m.130)** ve **Ticari Sırların** tespiti hayati önem taşır. Yanlışlıkla teslim edilen bir avukat mütalaası davayı kaybettirebilir veya cezaya yol açabilir.

### Kritik Türk Hukuku (Rekabet Kurumu) Farkı: Şirket İçi Avukatlar (In-house Counsel)

Türk Hukukunda, özellikle Rekabet Kurumu incelemelerinde (Danıştay kararları ve Kurul içtihatları gereği AB hukukundaki *Akzo Nobel* kararına paralel olarak), **şirket bünyesinde iş akdiyle (bordrolu) çalışan şirket içi avukatlarla (in-house) yapılan yazışmalar Avukat-Müvekkil Gizliliğinden (Attorney-Client Privilege) YARARLANMAZ.** Gizlilik zırhı sadece dışarıdan hizmet alınan, bağımsız "Dış Hukuk Bürosu / Serbest Avukat" ile savunma hakkı kapsamında yapılan yazışmaları korur. Bu nedenle şirket içi avukat iletişimleri (eğer Rekabet Kurumu incelemesi söz konusuysa) doğrudan gizli kabul edilemez, bayraklanması gerekir. (Bkz. Rekabet Kurulunun Dow, Enerjisa vb. kararları).

## Dosya Bağlamı (Matter context)

**Dosya bağlamı.** Kurumsal düzeydeki CLAUDE.md'de `## Dosya Çalışma Alanları`nı kontrol edin. Eğer aktif bir dosya yoksa sorun: "Bu hangi uyuşmazlık için? `/litigation-legal:matter-workspace switch <kisa-ad>` çalıştırın." Asla `Cross-matter context` açık değilse başka dosyanın evraklarını okumayın.

---

## Amaç

Belge incelemesinde üç tür girdi vardır: açıkça avukat-müvekkil gizliliği kapsamında olanlar, açıkça olmayanlar ve üzerinde düşünülmesi/hukuki değerlendirme yapılması gerekenler (gri alanlar). Bu beceri ilk iki türü ayıklar ki avukatın zamanı tamamen gri alanlara (üçüncü türe) kalsın.

**Bu bir "ilk geçiş" (first-pass) işlemidir. Avukat her bayrağı incelemelidir. İstisna yoktur.**

## Kayıt Sadakati ve Atıflar

Hukuki bir kurala veya içtihada atıf yapıldığında, tüm unsurlarını karşılayıp karşılamadığı kontrol edilmelidir.
Tüm atıfların (Kurul Kararı, Yargıtay kararı, Av.K.) nereden geldiği mutlaka belirtilmelidir: `[Lexpera]`, `[Kazancı]`, `[web araması — doğrula]` veya `[kullanıcı tarafından sağlanan]`. Asla bu etiketleri kaldırmayın.

## İş Akışı ve Kararlar (The calls)

**Üç Durum Kuralı (Three-state rule). Sistem ASLA şüpheli/sübjektif bir durumda gizliliği kaldıran kararı sessizce kendi başına vermez.** Belirsiz her durumda (şirket içi / dış büro karmaşası, e-postada alakasız üçüncü kişilerin (CC) olması, ticari / hukuki tavsiye ayrımı) sistem belgeye "gizlilik/sır (privilege)" etiketini yapıştırır ve yanına avukat için bir ⚠️ bayrağı ekler. Eksik işaretleme telafisi imkansız feragat demektir; fazla işaretleme ise avukat tarafından manuel düzeltilebilir.

### ✅ Kesinlikle Gizli / Sır Kapsamında (Confidently privileged) — İşareti koru, bayrak atma

- Şirket (müvekkil) ile **dış hukuk bürosu / serbest avukat** arasında geçen ve hukuki tavsiye talep eden/veren, dışarıdan (üçüncü kişi) kimsenin kopyada (CC) olmadığı iletişimler.
- Avukatın dava/soruşturma için hazırladığı hukuki mütalaalar, strateji notları (Work product).
- Üst yönetim ile bağımsız avukat arasındaki dava stratejisi tartışmaları.

### ✅ + ⚠️ Şüpheli — İşareti koru VE Bayrak ekle (Uncertain)

- **Şirket İçi Avukat (In-house) yazışmaları** — Özellikle idari/Rekabet soruşturmalarında gizlilik kapsamı tartışmalıdır. Otomatik koruma yoktur. Avukat değerlendirmesi gerekir.
- **Üçüncü Kişi Kopyada (CC)** — E-postada avukat var ama alakasız bir departman veya şirket dışı biri de kopyadaysa (gizliliğin delinmesi/feragat riski).
- **Karışık Amaç (Mixed purpose)** — E-postanın yarısı ticari karar, yarısı hukuki tavsiye. Redaksiyon (karartma) mı yapılacak, tümden mi saklanacak?
- **Ekler (Attachments)** — E-posta avukatla yapıldığı için gizli olabilir ama ekindeki standart aylık satış raporu tablosu gizli değildir.
- **Dava öncesi olası risk yazışmaları.**

### ❌ Kesinlikle Gizli Değil (Confidently not privileged) — Kaldırılmasını öner (karar avukatın)

Sadece tartışmasız durumlarda bu tavsiye verilir. Sistem yine de kendisi logdan/listeden silmez, tavsiye eder.
- Avukatın hiç dahil olmadığı iş/ticaret yazışmaları.
- Ticari/operasyonel bir karara sadece "bilgi" (CC) olarak şirket içi avukatın eklenmesi (Avukatı CC'ye koymak belgeyi sihirli bir şekilde gizli yapmaz).
- Çıplak olgular/veriler (Olguların kendisi sır değildir, avukatla tartışılması sırdır).
- Bağımsız üçüncü bir şirkete gönderilmiş iletişimler.

Eğer sınırda bir durum varsa (Acaba CC'deki dış acente şirketimiz adına mı hareket ediyor?), bu "Kesinlikle Değil (❌)" kategorisine değil, "Şüpheli (✅ + ⚠️)" kategorisine girer.

---

## Adım Adım İnceleme (Workflow)

### Adım 1: Format Kontrolü

İncelenen liste gerekli alanlara sahip mi? (Tarih, Gönderen, Alıcılar (To/CC/BCC), Dosya Tipi, Açıklama). Eksikse uyar.

### Adım 2: Girdi Bazında İnceleme (Entry-by-entry)

Her belge için:

```
Kayıt [N] ([Dosya Adı/Bates]): [✅ Gizli | ✅ Gizli + ⚠️ Şüpheli | ❌ Gizli Değil (Öneri)]
[Eğer ✅ ise: tek satırlık neden]
[Eğer ✅ + ⚠️ ise: işaret korunur; avukatın çözmesi gereken temel sorun (Örn: "Şirket içi avukat yazışması - Rekabet kuralları açısından risk", "CC'de PR ajansı var")]
[Eğer ❌ ise: tek satırlık neden — ama avukat onaylamadan listeden çıkmaz]
```

### Adım 3: Düzen/Örüntü Kontrolleri (Pattern flags)

- Aynı sorun tekrarlıyor mu? (Örn: Sürekli aynı üçüncü kişi kopyaya eklenmiş).
- Aşırı gizlilik iddiası (Over-designation)? (Her şeye gizli denmişse, kurumu/mahkemeyi kızdırır, avukatı uyar).
- Yetersiz açıklama (Kurum/Mahkeme "bu belge neyle ilgili anlamadım, içeriğe bakacağım" diyebilir).

## Çıktı (Output)

**Belgeler Kuruma, Savcılığa veya Karşı Tarafa TESLİM EDİLMEDEN ÖNCE:** Bu adımlar yasal sonuçlar doğurur. Eğer Rol Hukukçu Değilse:
> Yanlış belge teslimi (under-designation) sırların ifşasına ve feragata yol açar; aşırı ve haksız gizlilik iddiası (over-designation) mahkeme/kurum nezdinde yaptırımlara neden olabilir. Bunu yetkili bir avukatla veya dış hukuk bürosuyla incelediniz mi? Evet ise devam edin.

Emin olmadan listeyi/logu "teslime hazır" olarak işaretlemeyin.

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — Eklenti ayarları ## Çıktılar bölümüne göre; bkz. `## Bunu Kim Kullanıyor`]

## Sır Saklama ve Gizlilik İncelemesi: [Dosya] — [tarih]

**Uygulanacak Kurallar:** [Av.K. m.36, Rekabet Kurulu İçtihatları, CMK m.130 vb.] `[UNCERTAIN — doğrula]`
**İncelenen Belge Sayısı:** [N]
**Sonuçlar:** [N] ✅ kesin gizli / [N] ✅+⚠️ incelenecek / [N] ❌ gizlilik/sır yok (çıkarılması önerilir)

### ✅ + ⚠️ Bayraklananlar — Gizlilik İşareti Korundu, Avukat Karar Verecek

| Sıra | Belge / Bates | Sorun | Lehte Delil | Aleyhte Delil | Avukatın Vereceği Karar |
|---|---|---|---|---|---|
| [N] | [belge] | [örn: In-house yazışması] | [hukuki konu] | [ticari e-posta adresi] | [Kuruma sunulacak mı?] |

### ❌ Gizlilik/Sır Kapsamında Olmayanlar (Avukat Çıkarılmasını Onaylamalıdır)

| Sıra | Belge / Bates | Neden |
|---|---|---|

*Sadece kaydedildi, işlem yapılmadı. Sistem kendi başına gizlilik etiketini/belgeyi kaldırmaz — gerekçeyi inceledikten sonra avukat kaldırır.*

### ✅ Kesinlikle Gizli / Sır Kapsamında (İşlem Yok)

[Sayı. İstenirse liste verilir.]

### Örüntü ve Gözlemler (Pattern observations)

[Tekrarlayan hatalar, şirket içi eğitim gerektiren "avukatı CC'ye ekleme" huyları vb.]

### İşaretleme Disiplini

- `[VERIFY: belge, kişi veya tarihe dair olgusal iddia]`
- `[UNCERTAIN: şirket içi avukat statüsü, feragat sınırı gibi hukuki şüphe]`
- `[CITE NEEDED: kural veya içtihat]`

---

**Avukat herhangi bir eylemden önce tüm ⚠️ ve ❌ bayrakları bizzat incelemelidir.**

**Gizli/Sır Kapsamındaki Kaynak Materyal.** Bu çıktı, doğası gereği gizli belgelerin (avukat yazışmalarının) özetini içerdiğinden kendisi de gizlidir. Avukat-müvekkil gizliliği çemberi dışında paylaşılması feragata (waiver) yol açabilir.
```

## Bu Becerinin Kesinlikle YAPMADIĞI Şeyler

- Sınırda kalan sübjektif kararları kendi başına almak. ⚠️ "bir insan karar verir" demektir.
- Kendi değerlendirmesine dayanarak bir belgeden gizlilik etiketini kendi kendine silmek. ❌ sadece avukat için bir *tavsiyedir*.
- ✅ kararlarında mutlak doğruluk garantisi vermek. Listenin ve mahkemeye/kuruma teslim edilecek evrakların yegane sorumlusu avukattır. Bu sadece bir ilk tasniftir.

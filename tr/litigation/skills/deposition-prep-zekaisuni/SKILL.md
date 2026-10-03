---
name: deposition-prep-zekaisuni
title: /deposition-prep (İsticvap / Tanık Hazırlığı)
description: Bir tanık veya taraf (isticvap) için duruşma/ifade soru taslağı (outline) hazırlar — şirket içi belgeleri veya UYAP evraklarını çeker, hukuki teori etrafında başlıkları düzenler ve çelişki yaratacak/yüzleştirilecek materyalleri (impeachment) öne çıkarır. Kullanıcı "[isim] için isticvap/tanık hazırlığı yap", "soru listesi oluştur" veya "[isim]'in duruşmasına hazırlan" dediğinde kullanın.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/litigation-legal/skills/deposition-prep
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: litigation
language: tr
---

# /deposition-prep (İsticvap / Tanık Hazırlığı)

1. `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` yükle → dava teorisi, kilit olgular.
2. Aşağıdaki iş akışını ve referansları izle.
3. E-Keşif (eDiscovery) / UYAP platformundan tanığın yazdığı veya adının geçtiği belgeleri çek.
4. Soru listesi taslağını oluştur: arka plan, kilit belgeler, teoriye bağlı başlıklar, yüzleştirme (çelişki) materyalleri.

---

# İsticvap / Tanık Hazırlığı (Deposition Prep)

## Türk Hukuku Bağlamı (Jurisdiction Assumption)

ABD'deki "Deposition" (yeminli mahkeme dışı ifade) kurumu Türk Hukukunda doğrudan bulunmaz. Bunun karşılığı duruşmada yapılan **Tanık Dinleme (HMK m. 240 vd.)** veya tarafın bizzat dinlenmesi olan **İsticvap (HMK m. 169 vd.)** ve ceza yargılamasındaki **Çapraz Sorgu (CMK m. 201 vd.)** kurumlarıdır.

*   **İsticvap (Taraf):** Sadece kendi aleyhine olan vakıalar için yapılır. Sorular hakime verilir, hakim sorar (HMK m. 173). Taslak kapalı, "evet/hayır" veya belge kabulüne yönelik olmalıdır.
*   **Tanık Dinleme:** Doğrudan soru yöneltilebilir (HMK m. 152). Ancak "yönlendirici soru" (leading question) itiraz riski taşır.
*   **Çapraz Sorgu (CMK m. 201):** Doğrudan (direct) ve çapraz (cross) sorgu dinamikleri tam olarak işler.

Eğer duruşmada dinlenecek kişi "kendi tanığımız" (friendly) ise, ifade önceden kurgulanmış (ezberletilmiş) görünmemelidir. Amaç; tanığın gerçek anılarını canlandıracak sorular hazırlamak ve mahkemeye sunulacak delillerle tutarlılığı sağlamaktır.

## Hedef Kontrolü (Destination check)

Üretilen soru taslağının nereye gideceğini kontrol edin. Eğitimsiz bir tanığa (özellikle şirket dışı birine) tüm stratejiyi içeren taslağı göndermek Avukat-Müvekkil Gizliliğini (Av.K m.36) kaldırabilir ve duruşmada "Avukatınız size ne söyleyeceğinizi yazıp verdi mi?" sorusuna maruz kalmasına yol açabilir. Taslak her zaman avukat için (iç kullanım) hazırlanır.

## Kayıt Sadakati (Record fidelity)

Taslağa alınan her alıntı ve atıf için iki kural geçerlidir:

**Kelimesi kelimesine alıntılar tam olmalıdır.** Karşı taraf avukatına, tanığa veya bilirkişiye atfedilen sözleri, tam metin elinizde olmadan tırnak (" ") içine almayın.
- **Tırnaksız özetleyin:** "Tanık daha önceki dilekçesinde X olduğunu iddia etti `[teklif/dilekçe no ile teyit et]`."
- **Yer tutucu bırakın:** `[tam alıntıyı doğrula — UYAP evrak no eksik]`
- **Asla boşluğu uydurarak doldurmayın.** Duruşmada uydurma bir alıntıyla yüzleştirme yapmak tüm güvenilirliği yıkar.

## Sözlü Savunma Kalibrasyonu (Oral calibration)

Bu taslak gerçek zamanlı, sözlü olarak (duruşmada) kullanılacaktır:

- Gerçekten önemli olan 3-4 konuyu seçin. Her şeyi sormaya çalışmayın; hakimin dikkati dağılır.
- En güçlü yüzleştirmenizle (confrontation) veya en önemli belgeyle başlayın veya en vurucu noktaya saklayın.
- Hasım (adverse) tanıklar için: En sıkı sorular en sıkı dizilimle sorulur (Kutuyu daraltın).

## Bağlamı Yükle

`~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → dava teorisi (teori, kırılma olgusu, lehe/aleyhe kilit olgular).

**Güvenlik Kapısı (Gate).** Taslağı oluşturmadan önce `_log.yaml` dosyasında dosya kısa adını (slug) kontrol et. Yoksa reddet:
> "Dosya günlüğünde [kısa ad] bulamıyorum. Önce `/litigation-legal:matter-intake` çalıştırın. Kaydedilmemiş bir dosya için tanık taslağı hazırlamam."

## İş Akışı (Workflow)

### Adım 1: Bu kişi kim?

- İsim, rol, davayla ilişkisi (Taraf mı, tanık mı?)
- Neden dinletiyoruz / dinleniyor — bu kişiden (veya karşı tarafın tanığından) ne almamız gerekiyor?

"Neden" sorusu davamızın teorisine bağlanır. Eğer tanık kırılma olgusunu (pivot fact) kurabiliyorsa, taslağın merkezi budur.

### Adım 1a: Tanığın Duruşu (Posture) — Soru Tarzı Seçimi

Soru yazmadan önce tanığın duruşunu (posture) belirleyin:

- **Hasım / Karşı Taraf (Adverse / İsticvap)** — Kapalı uçlu, yönlendirici, her seferinde tek bir olguyu soran (evet/hayır) sorular. Seçenekleri daralt.
- **Dost / Kendi Tanığımız (Friendly)** — Açık uçlu sorular. Hikayeyi tanığın anlatmasına izin ver. Kendi tanığınıza kapalı/yönlendirici soru sormak hakimin nezdinde inandırıcılığı düşürür.
- **Tarafsız / Resmi Kurum Temsilcisi** — Karışık; hikayeyi almak için açık, spesifik noktaları sabitlemek için kapalı.

### Adım 2: İlgili Belgeleri Çekin

Mevcut dosya sisteminden / UYAP evraklarından:

- Tanığın yazdığı / imzaladığı belgeler (Örn: Teslim tesellüm tutanağı, e-posta)
- Tanığa gönderilen belgeler
- Tanığın adının geçtiği evraklar
- Tanığın bulunduğu toplantı notları

Tarihe göre sıralayın. Teori için en sıcak (hot docs) belgeleri işaretleyin.

### Adım 3: Konu Başlıklarını Oluşturun

Her konu, kanıtlamak veya keşfetmek istediğiniz bir unsurdur. Teori etrafında organize edin:

**Arka Plan (Her zaman ilk — tanık savunmaya geçmeden önce tartışmasız olguları sabitleyin):**
- Rol, görev süresi, sorumluluklar (Olay tarihindeki görevi neydi?)
- Kilit oyuncularla ilişkisi

**Lehe Olgular (Yüzleştirmeden önce sabitleyin):**
- Bizim teorimizi destekleyen, bu tanığın teyit edebileceği olaylar.
- İmzası olan/bildiği lehe belgeler (Hakim aracılığıyla kendisine gösterilecek).

**Aleyhe Olgular (Belgelerle yüzleştirme):**
- Bize karşı olan ve karşı tarafın avukatının zaten soracağı olgular — ilk önce kendi versiyonunuzu alın.
- Bize zarar veren belgeler — tanığın bunları nasıl açıklayacağını önceden görün.

**Çelişki / Yüzleştirme (Impeachment):**
- Önceki çelişkili beyanlar (Kolluk ifadesi, önceki celse beyanı).
- Beklediğiniz cevaba zıt düşen yazılı belgeler.

**Kırılma Olgusu (The pivot fact):**
- Davanın kaderini belirleyen olguyu (ispat yükü bizde olan) kuran (veya zayıflatan) soru dizisi.
- En dikkatli hazırlanan bölüm. Adım 1a'daki duruşa (posture) göre yazılır.

### Adım 4: Taslağı Yazın

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — Eklenti ayarları ## Çıktılar bölümüne göre; bkz. `## Bunu Kim Kullanıyor`]

# İsticvap / Tanık Soru Listesi (Outline): [İsim]

**Duruşma / İfade Tarihi:** [tarih]
**Tanık Rolü:** [unvan, olayla ilişkisi]
**Tanık Duruşu:** [hasım / kendi tanığımız / tarafsız] — soru formunu belirler
**Uygulanacak Usul:** [HMK m.169 (İsticvap) / HMK m.240 (Tanık) / CMK m.201] `[UNCERTAIN — doğrula]`
**Neden Dinletiyoruz/Sorguluyoruz:** [tek cümle — temel hedef]
**Teori Bağlantısı:** [bu kişinin davanın bütününe nasıl uyduğu]

---

## I. Arka Plan ve İlgililik

[Sorular — kapalı veya açık, tartışmasız konuları sabitleme]

## II. [Lehe Olgu Başlığı]

**Hedef:** [Olgunun] davanın esası için mahkeme önünde sabitlenmesi.

**İlgili Belgeler (Hakim/Tanık ekranına yansıtılacak):**
- [UYAP Evrak No / Ek No] — [açıklama] — [neden önemli]

**Sorular:**
[Dizi. Adım adım beyanı inşa edin.]

## III. [Aleyhe Olgu Başlığı]

**Hedef:** [Aleyhe olgunun] etkisini kırmak veya tanığın açıklamasını kayda geçirmek.

[Aynı yapı]

## IV. Çelişki / Yüzleştirme (Gerekirse)

[Tanık aksi yönde beyan verirse kullanılacak önceki çelişkili beyanlar / belgeler]

## V. [Kırılma Olgusu Dizisi]

**Hedef:** [Davanın düğümlendiği o temel olay]

[Bu en sıkı bölümdür. Hasım ise her soru evet/hayır yanıtı aramalı, adım adım köşeye sıkıştırmalı.]

---

## Duruşmada Sunulacak/Gösterilecek Belge Listesi (Exhibits)

| Sıra | Evrak No/Bates | Açıklama | Kullanılacağı Bölüm |
|---|---|---|---|

## İşaretleme Disiplini (Marker discipline)

Hazırlarken şu işaretleri kullanın:
- `[VERIFY: olgusal iddia]` — dosyadan/belgeden tam doğrulanmamış her olgu
- `[UNCERTAIN: hukuki kural]` — mahkemenin soru sormaya izin verip vermeyeceği gibi güncel usul kuralları
- `[CITE NEEDED: atıf gerekli]` — UYAP evrak no veya belge tarihi eksik

## Avukata Duruşma Notları

- [Taslağın yakalayamadığı şeyler — tanığın muhtemel tavrı, anlık yapılması gereken stratejik itirazlar (örn: yönlendirici soru itirazı hazırda bekletilecek)]

---

**Avukat-Müvekkil Gizliliği / Sır Saklama.** Bu taslak dava stratejisi ve avukatlık çalışma ürünü (work product) içerir. Gizli ibaresiyle saklayın ve duruşma stratejisini açık edeceğinden tanığın eline bizzat vermeyin.
```

## Bu Becerinin YAPMADIĞI Şeyler

- **Duruşmada soruyu fiilen sormak.** Bu taslak bir haritadır; avukat (veya hakim) haritayı okur.
- **Tanığın ne diyeceğini kesin öngörmek.** Olası yanıtlara hazırlar ama duruşmada her zaman sürprizler (sözlü yargılama doğası) olur.
- **Anlık itirazlara (Örn: HMK 152 uyarınca soruya itiraz) karar vermek.** Takip soruları ve itirazlar avukatın o anki refleksidir.

---
name: subpoena-triage-zekaisuni
title: /subpoena-triage (Müzekkere Triyajı)
description: Şirkete tebliğ edilen bir müzekkereyi / bilgi belge talebini (subpoena) inceler — sınıflandırır, kapsam/külfet/gizlilik analizini yapar, portföy ile çapraz kontrol sağlar ve bir itiraz/yanıt çerçevesi, uyum planı ve kesin süre takvimi oluşturur. Kullanıcı "bir müzekkere aldık", "savcılıktan yazı geldi" dediğinde veya Rekabet Kurumu/SPK gibi bir idari kurum bilgi talebini değerlendirmek istediğinde kullanın.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/litigation-legal/skills/subpoena-triage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: litigation
language: tr
---

# /subpoena-triage (Müzekkere Triyajı)

1. Verilen yoldan müzekkereyi/talebi oku.
2. Sınıflandır (mahkeme-müzekkeresi / savcilik-ifade-belge / taraf-olunan-dava / idari-kurum-talebi / vergi-incelemesi).
3. Eğer ağır ceza/kapsamlı savcılık soruşturması ise → dur, `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` uyarınca doğrudan ceza avukatına eskalasyon yap. Aksi takdirde devam et.
4. Çapraz kontrol için `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` dosyasını yükle. `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` yükle → harita, gizlilik (ticari sır) kuralları, eskalasyon normları.
5. Aşağıdaki iş akışını ve referansları izle.
6. Temel alanları çıkar, kapsam/külfet/gizlilik analizini yap, itiraz/yanıt çerçevesi + uyum planı + kesin süre takvimi üret.
7. `~/.claude/plugins/config/claude-for-legal/litigation-legal/inbound/[kisa-ad]/triage.md` dosyasına yaz. Müzekkereyi `~/.claude/plugins/config/claude-for-legal/litigation-legal/inbound/[kisa-ad]/incoming.[uzanti]` olarak kopyala veya linkle.
8. Yönlendirme (Hand off): Eğer delil saklama/tespit yoksa `/legal-hold --issue`; önem derecesi gerektiriyorsa `/matter-intake`; mevcut davaya ait bir müzekkere ise `/matter-briefing [kisa-ad]`.

---

# Müzekkere / Bilgi Talebi Triyajı (Subpoena Triage)

## Amaç

Müzekkereler ve kurum yazıları kesin sürelerle gelir (genellikle HMK uyarınca 2 hafta, idari kurumlarda 30 gün, savcılıkta daha kısa). Hata senaryoları: süreyi kaçırmak, gereğinden fazla bilgi vermek (KVKK ihlali, ticari sırrın ifşası, feragat), eksik bilgi vermek (disiplin para cezası, zorla getirme, HMK m.220 uyarınca aleyhe yorum) veya itiraz/kapsam daraltma fırsatını kaçırmaktır. Bu beceri sınıflandırır, analiz eder ve itiraz çerçevesiyle birlikte bir yanıt planı üretir.

## Yargı Alanı / Usul Varsayımı

Uygulanacak kural talebi gönderen makama göre değişir: HMK m. 219 vd. (Belgelerin ibrazı), CMK m. 332 (Bilgi isteme), Rekabetin Korunması Hakkında Kanun m. 14 (Bilgi İsteme), VUK m. 148 (Bilgi verme). Her kuralın süresi, itiraz hakkı (ticari sır, avukat-müvekkil gizliliği) ve yaptırımı farklıdır. Buradaki kural çıktıları bir başlangıçtır — yazılı olarak ileri sürmeden önce ilgili usul kanununu teyit edin.

## Taraf Bağlamı (Side context)

Bu beceri doğası gereği savunma odaklıdır — şirkete bir müzekkere tebliğ edilmiştir ve pozisyon yanıt/itiraz/uyumdur. Eğer şirket "üçüncü kişi" ise (davada taraf değilse), sadece belge sunma yükümlülüğü vardır. Eğer "taraf" ise, bu doğrudan bir HMK "delil ibrazı" meselesidir ve mevcut bir uyuşmazlık dosyasıyla (matter) eşleşmelidir.

## Bağlamı Yükle

- Müzekkere/Talep belgesi (kullanıcı yolunu verir veya oturuma sürükler)
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` — ilişkili dosya araması ve muhafaza durumu için
- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → harita (düzenleyici kurumlar), kurum gizlilik kuralları, eskalasyon

## İş Akışı (Workflow)

### Adım 0: Uygulanacak kuralı araştır

**Müzekkereyi analiz etmeden önce, makam için geçerli usul kuralını (HMK, CMK, VUK, Rekabet, SPK) araştırın. Şunları tespit edin: süreler (tebliğden itibaren kaç gün?), yasal zorunluluk (reddetme hakkı var mı?), ticari sır ve avukat-müvekkil gizliliği (Av. K. m.36) istisnaları. Teyit edin. Kapsamlı savcılık / MASAK taleplerini derhal ilgili uzmana/ceza avukatına eskalasyon için işaretleyin.**

### Adım 1: Sınıflandır

Talepler farklı kurallara tabi türlerde gelir:

- **Üçüncü Kişi Belge Müzekkeresi (Hukuk Davası)** — Davaya taraf değiliz; mahkeme (örneğin bir iş veya ticaret mahkemesi) taraflardan birinin talebiyle bizden belge istiyor (Örn: banka kayıtları, SGK dökümleri, fatura suretleri). İtirazlar: KVKK m.28 dengesi, ticari sır, kapsamın genişliği.
- **Şirket Yetkilisinin İsticvabı / Tanık Olarak Çağrılması** — Mahkeme veya Savcılık bir çalışanı ifadeye çağırıyor. Çalışanın hazırlanması (witness prep) gerekir.
- **Taraf Müzekkeresi** — Biz DAVANIN TARAFIYIZ; bu doğrudan tarafı olduğumuz davanın delil aşamasıdır (HMK m. 220). `matter` (uyuşmazlık dosyası) altındaki sürece yönlendirilmelidir.
- **İdari Kurum Bilgi Talebi (CID / Regulator Inquiry)** — Rekabet Kurumu, SPK, BTK, KVKK Kurumu. Sıkı kurallar, yüksek idari para cezası riski. İletişim çok daha stratejiktir.
- **Savcılık Müzekkeresi (Grand jury / Criminal)** — Ceza soruşturması. Acil ceza avukatı eskalasyonu.

### Adım 2: Temel Alanları Çıkar

- **Talep Eden Makam** — Hangi mahkeme (Esas numarasıyla), hangi kurum/daire, hangi savcılık.
- **Taraf / Davacılar** — Hukuk davası ise kim kiminle davalık?
- **Dosya / Esas Numarası** — UYAP eşleştirmesi için.
- **İstenen Belge Kategorileri** — Numaralandırılmış liste.
- **İfade Konuları** (Eğer çağrı ise).
- **Yanıt / İtiraz Süresi** — Tebliğ tarihi + uygulanacak kurala göre hesaplanan süre (Örn: tebliğden itibaren 2 hafta).
- **Coğrafi / Kapsam** — Hangi yıllar, hangi şubeler, hangi sistemler.

### Adım 3: Portföy Çapraz Kontrolü

- **Taraf olunan bir dava → mevcut dosyayla ilişkili:** Esas numarasının veya tarafların `_log.yaml` dosyasındaki bir davayla eşleşip eşleşmediğini kontrol edin. Evet ise, o dosyanın iş akışına yönlendirin.
- **Üçüncü kişi müzekkeresi → tanımadığımız taraf:** Tarafları kaydedin; bağımsız bir gelen evrak (inbound) olarak loglayın.
- **Aynı davadan gelen birden fazla müzekkere:** Eşgüdümlü yanıt stratejisi gerekebilir.

### Adım 4: Kapsam, Külfet (Burden) ve Gizlilik Analizi

**Kapsam / İlgililik**
- İstenen kategoriler gerçekten bizde var olan belgelerle örtüşüyor mu?
- Kategori bir "fishing expedition" (balık avına çıkma - gereksiz geniş ve ucu açık talep) mı? (Örn: "2010 yılından beri tüm mailler"). HMK'da delillerin somutlaştırılması zorunludur.

**Külfet (Burden)**
- İlgili personel, taranacak sistemler, zaman periyodu.
- Tahmini hacim (küçük / orta / büyük / aşırı).
- Maliyet / İş gücü (Gerekirse mahkemeden süre uzatımı talep edilmeli).

**Gizlilik (Privilege / Confidentiality)**
- **Avukat-Müvekkil Gizliliği (Av. K. m.36):** İstenen evraklar avukat mütalaası veya savunma hakkı kapsamında mı?
- **KVKK (Kişisel Veriler):** İstenen bilgiler uyuşmazlıkla doğrudan ilgili olmayan üçüncü kişilerin kişisel verilerini içeriyor mu? (Maskeleme/redaksiyon gerekliliği).
- **Ticari Sır:** Sözleşme bedelleri, müşteri listeleri. Mahkemeden gizlilik kararı (protective order / kapalı zarf usulü) talep edilmeli mi?

**Diğer İtiraz Nedenleri**
- Bizde yok / Bizim uhdemizde değil.
- Hatalı tebligat (örneğin eski adrese veya yetkisiz şubeye tebliğ).

### Adım 5: İtiraz ve Çerçeve (Objections framework)

Yapılandırılmış bir itiraz taslağı hazırlayın (kesin yanıt dilekçesi değil, hangi itirazların geçerli olduğunun özeti). Dış büro veya şirket avukatı bunu nihai dilekçeye dönüştürür.

Her itiraz için:
- Hukuki dayanak (HMK, KVKK, Av. K.)
- Müzekkeredeki spesifik uygulama (hangi talebe, hangi kısma itiraz ediliyor)
- Güç (Güçlü / Makul / Zayıf)

### Adım 6: Uyum ve Yanıt Planı (Compliance plan)

İtiraz edilse bile genellikle talebin bir kısmı (daraltılarak) sunulur. Plan:

- **Olası Sunum Kapsamı** — İtirazlardan (veya maskelemelerden) sonra ne sunacağımız.
- **Taranacak Kişiler/Sistemler** — Kimlerin kayıtlarına bakılacak.
- **Tarih aralığı**
- **İnceleme protokolü** — (KVKK ve ticari sır maskelemesini kim yapacak?)
- **Teslimat formatı** — (Fiziki CD, KEP, UYAP Vatandaş / Kurum Portal).

### Adım 7: Kesin Süreler (Deadlines)

Süreler kesindir. Adım 0'da bulunan kuralları uygulayın.

- **Yanıt / Belge Sunma Süresi** — Kurala göre (Örn: HMK 2 hafta). Süre uzatım dilekçesi (meet-and-confer / mazeret) gerekiyor mu?
- **İtiraz Süresi**
- **İfade Tarihi** — (Varsa).

Hepsini takvime işlemek üzere not edin.

### Adım 8: Triyajı Yaz (Write triage)

Çıktı: `~/.claude/plugins/config/claude-for-legal/litigation-legal/inbound/[kisa-ad]/triage.md`.

```markdown
[İŞ-ÜRÜNÜ BAŞLIĞI — Eklenti ayarları ## Çıktılar bölümüne göre; bkz. `## Bunu Kim Kullanıyor`]

# Müzekkere / Bilgi Talebi Triyajı

> **DIŞ HUKUK BÜROSU TAVSİYESİ YERİNE GEÇMEZ.** Bu belge; süreler, muhafaza kararları ve angajman hakkında hızlı kararları desteklemek için yapılandırılmış bir sınıflandırma ve kapsam analizidir. İtirazların kesinleşmesi, dilekçe yazımı ve ticari sır/KVKK kararları uzman avukat incelemesi gerektirir. Rutin üçüncü kişi bilgi taleplerini aşan her müzekkere için dış büro ile iletişime geçin.

**Kısa Ad (Slug):** [slug]
**Tebliğ Tarihi:** [YYYY-MM-DD]
**Tebliğ Edilen Şirket/Şube:** [kurum / şube]
**Gelen Evrak Yolu:** [path]
**Sınıflandırma:** [mahkeme-müzekkeresi / savcilik / idari-kurum / taraf-dava]

---

## Temel Alanlar

- **Talep Eden Makam:** [mahkeme/kurum]
- **Dosya/Esas No:** [esas no]
- **Davacı/Şikayetçi:** [isim]
- **Yanıt (Kesin) Süresi:** [tarih]
- **İstenen Teslim Tarihi:** [tarih]

## İstenen Belge Kategorileri (Özet)

[numaralandırılmış liste, kısa]

## İlgili Kişiler / Etkilenen Sistemler

[liste]

---

## Portföy Çapraz Kontrolü

**İlişkili Dosya (Matter):** [slug veya "yok"]
**Durum:** [Mevcut dosyaya yönlendirildi veya Yeni gelen evrak olarak açıldı]

---

## Kapsam ve Külfet Analizi

**Kapsam:** [Kategorilere göre ilgililik (relevance) değerlendirmesi]
**İş Yükü / Külfet:** [küçük / orta / büyük / aşırı — nedeni ile]
**Lokal / Coğrafi Sorunlar:** [Örn: Belge yurtdışı sunucuda vb.]

## Gizlilik ve KVKK Analizi

*Gizlilik kapsamı ilk bakış değerlendirmesidir; son karar avukatındır.*

**Avukat-Müvekkil Gizliliği / Ticari Sır söz konusu mu:** [evet/hayır + hangi kategoriler] `[SME VERIFY]`
**KVKK (Kişisel Veri) Sorunu:** [İlgisiz üçüncü kişi verilerinin maskelenmesi gerekiyor mu?] `[SME VERIFY]`

---

## İtiraz Çerçevesi

*Aşağıdaki her satır, yazılı olarak ileri sürülmeden önce usul kanunu açısından uzman avukat (`[SME VERIFY]`) doğrulaması gerektirir.*

| İtiraz Konusu | Hukuki Dayanak | Uygulandığı Kısım | Güç | Avukat Onayı? |
|---|---|---|---|---|
| İlgisizlik/Kapsam | [HMK/ilgili kural] | [kategoriler] | [güçlü/makul/zayıf] | [ ] |
| Külfet / Süre yetersizliği | [kural] | [kategoriler] | | [ ] |
| Gizlilik / Ticari Sır | Av.K/TTK/KVKK | [ilgili belgeler] | güçlü | [ ] |
| Bizde Bulunmuyor | | [kategoriler] | | [ ] |

---

## Yanıt/Uyum Planı (Eğer belge verilecekse)

- **Sunulacak Kapsam:** [itiraz/maskeleme sonrası]
- **Taranacak Kişiler / Sistemler:** [liste]
- **Tarih aralığı:** [aralık]
- **İnceleme protokolü:** [kim maskeleme/redaksiyon yapacak]
- **Teslim formatı:** [UYAP / CD / KEP]

---

## Kesin Süreler (Takvime İşleyin)

*Aşağıdaki tüm süreler, Adım 0 usul araştırmasından gelir. `[SME VERIFY]` kuralın bu mahkeme ve talep türü için geçerliliğini teyit eder.*

- **Yanıt / Belge Sunma Süresi:** [tarih] `[SME VERIFY]`
- **İtiraz / Süre Uzatım Talebi:** [tarih] (Genellikle yanıt süresi dolmadan) `[SME VERIFY]`

---

## Acil Aksiyonlar

- [ ] Şirket İçi Saklama Talimatı (Legal hold) yayımlandı mı? — [evet/hayır] — hayırsa, `/legal-hold [slug] --issue` çalıştırın.
- [ ] Dış Büroya iletildi mi? — [evet/kime/TBD]
- [ ] Süre uzatım / itiraz dilekçesi planlandı mı? — [tarih]
- [ ] Log'da dosya açıldı mı? — [evet/hayır/TBD]
- [ ] İç Eskalasyon — [kime]

---

## Tavsiye

[Ne yapılacağına dair iki paragraflık özet. İtiraz duruşu. Belge sunma duruşu. Maskeleme ihtiyacı. Dış büronun devralıp almayacağı.]

---

## Atıf Doğrulaması

Bu belgedeki tüm kanun, kural ve içtihat referansları yapay zeka tarafından üretilmiştir ve doğrulanmamıştır. Herhangi bir atıfa (özellikle itiraz dilekçesinde veya makamla yazışmada) güvenmeden önce, doğruluğunu ve güncelliğini Lextera, Lexpera, UYAP veya Kazancı gibi bir hukuk araştırma aracından teyit edin. Yanlış veya uydurma atıflar disiplin veya usul yaptırımlarına yol açabilir. `[verify]` (doğrula) etiketli alıntılar en yüksek halüsinasyon riskini taşır.
```

### Adım 9: Yönlendirme (Hand off)

**Müzekkereye yanıt vermeden önce (itiraz sunmak, belge vermek veya ifadeye gitmek):** Eğer Rol Hukukçu değilse:
> Bir mahkeme veya kurum müzekkeresine yanıt vermenin hukuki sonuçları vardır — süreyi kaçırmak cezai/idari yaptırım riski taşır, fazla bilgi vermek KVKK'yı ihlal edebilir veya ticari sırları ifşa edebilir. Bunu bir avukatla görüştünüz mü? Evet ise devam edin. Hayır ise, onlara sunacağınız bir özet:
> [1 sayfalık özet üret]

Bu güvenlik kapısından (gate) açık bir 'evet' almadan geçmeyin. Triyaj ve iç takvimleme kapı gerektirmez — makama verilecek nihai yanıt gerektirir.

- Eğer **savcılık (ağır ceza/soruşturma)** ise → dur, eskalasyon için işaretle, standart triyaja devam etme.
- Eğer **İdari Kurum (Rekabet/SPK/KVKK vs.)** ise: kuruma özgü dinamiklerin geçerli olduğunu işaretle; dış düzenleyici (regulatory) büroya danışmayı öner.
- Eğer kapsamlı ise: log'da yeni bir dosya (matter) oluşturmayı teklif edin.
- İlgili veriler silinme riski altındaysa hemen `/legal-hold --issue` aracına yönlendirin.

## Bu Becerinin YAPMADIĞI Şeyler

- **Nihai itiraz / yanıt dilekçesini yazmaz.** Çerçeveyi üretir; dilekçe avukat tarafından yazılır.
- **Usul kurallarını körü körüne uygulamaz.** Kesin süreler ve HMK kuralları için her zaman avukat doğrulamasını (SME VERIFY) şart koşar.
- **Kapsamlı Savcılık Soruşturmalarını Yönetmez.** Eskalasyon yapar (Ceza hukuku bu eklentinin kapsamı dışındadır).

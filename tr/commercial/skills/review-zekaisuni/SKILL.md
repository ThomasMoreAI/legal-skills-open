---
name: review-zekaisuni
title: /review
description: Review a vendor agreement, NDA, SaaS subscription, amendment, or related commercial contract under the Turkish-law adapted commercial playbook. Detects the document type, routes to the right specialist skill, and merges outputs into one review memo. Use when the user asks to review a contract or provides a commercial agreement for legal triage.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/commercial-legal/skills/review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: commercial
language: tr
---

# /review

Gelen ticari sözleşmeyi `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` içindeki playbook'a göre inceler. Belge türünü tespit eder, uygun alt skill'i çalıştırır ve sonucu tek raporda toplar.

Komut ve klasör adları repo uyumu için İngilizce kalır. Türkçe çıktı verilir; hukuki içerik Türk hukuku ve Türkiye uygulamasına göre değerlendirilir.

## Instructions

1. **Load config.** Read `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` and the shared `company-profile.md`. If the commercial profile is missing or still contains placeholders, stop:

   > Önce `/commercial-legal:cold-start-interview` komutunu çalıştırın. İnceleme yapabilmem için playbook, risk tercihi, yetkili kişiler ve çıktı formatı gerekir.

2. **Check routing preference.** Read `## Review preferences` -> `confirm_routing`. If absent, default to `true`. If the user passed `--no-confirm`, proceed without asking unless routing is genuinely ambiguous.

3. **Get the document.** Accept direct upload, local path, document link, CLM record, e-signature envelope, KEP record, or pasted text. Do not treat UYAP as a default commercial contract repository. Use UYAP only if the agreement is tied to a litigation, enforcement, or court file.

4. **Identify document type from substance, not title alone.** Check title, recitals, operative clauses, signatures, annexes, and renewal/fesih clauses.

5. **Route to specialist skill.**

   | Detected document | Route |
   |---|---|
   | Gizlilik Sözleşmesi / NDA | `nda-review` |
   | Tedarikçi sözleşmesi, MSA, hizmet sözleşmesi | `vendor-agreement-review` |
   | SaaS, abonelik, bulut hizmeti, platform terms | `saas-msa-review` |
   | Ek protokol, zeyilname, tadil metni | `amendment-history` |
   | Yenileme veya fesih ihbar takibi | `renewal-tracker` |
   | Mixed or unclear | Ask one routing question |

6. **Run Turkish-law baseline checks for every review.**

   - Taraflar, rol ve sözleşme türü.
   - Sözleşme bedeli and TL equivalent if currency differs.
   - Imza ve temsil yetkisi.
   - Uygulanacak hukuk, yetkili mahkeme or tahkim.
   - KVKK, veri işleme, yurt dışına aktarım, alt veri işleyenler.
   - Cezai şart, sorumluluk sınırı, teminat, kefalet, garanti.
   - Otomatik yenileme, fesih ve ihbar yöntemi.
   - Rekabet yasağı, münhasırlık, müşteri/calisan ayartmama.
   - Arabuluculuk dava şartı ihtimali for future disputes.

7. **Merge outputs.** If more than one specialist ran, create a single memo with clear source sections. Preserve each specialist's severity and next steps; do not average risks into a softer conclusion.

## Routing Confirmation

If `confirm_routing` is on, show:

```markdown
Belgeyi şu şekilde sınıflandırdım: **[detected type]**.
Çalıştırılacak skill: `[skill name]`.
Gerekçe: [one short reason].

Devam edeyim mi?
```

If the document has hidden non-contract content, say so:

> Belge başlığı [title] olsa da [NDA dışı yükümlülük / abonelik yenilemesi / veri aktarımı / IP devri] içeriyor. Bu yüzden [skill] ile birlikte [second skill] kontrollerini de çalıştıracağım.

## Output Format

Prepend the work-product header from commercial `CLAUDE.md`.

```markdown
# Ticari Sözleşme İncelemesi: [Karşı Taraf] - [Belge Türü]

**Belge türü:** [detected type]
**Uygulanan playbook:** [sales-side | purchasing-side | matter override]
**Uygulanan hukuk varsayımı:** [Türk Hukuku | sözleşmede seçilen hukuk | belirsiz]
**Kaynak:** [file/link/CLM/KEP/e-signature]

## Sonuç
[İmzaya uygun | SARI - hukukçu incelemesi gerekir | KIRMIZI - durdurun | Belirsiz - eksik bilgi]

## Ana Bulgular
1. **[Konu]** - [madde no]
   - Risk: [short explanation]
   - Dayanak: [playbook / TBK / TTK / KVKK / other]
   - Öneri: [accept / revise / escalate / ask for facts]

## Specialist Outputs
- `[skill]`: [summary]
- `[skill]`: [summary]

## Eksik Bilgi ve Doğrulama
- [items]

## Sonraki Adımlar
- [action]
```

## Turkish Law Guardrails

- Hukuki sonuca bağlanacak kanun maddesi veya süre varsa, güncel mevzuat ve olay tarihi doğrulanmadan kesin deadline üretme.
- Arabuluculuk dava şartını otomatik `true` yapma; dava türü, talep ve özel kanun kontrol edilmelidir.
- `privilege waiver` yerine Türk hukukunda "avukatlık sırrı / gizli hukuki değerlendirme / kontrolsüz paylaşım riski" dilini kullan.
- UYAP numarası yoksa icat etme. Sözleşme dosyasında UYAP olmayabilir.
- Karşı tarafa gönderilecek metin, redline veya bildirim için avukat onayı kapısını koru.

## What this skill does not do

- It does not replace the specialist review skills.
- It does not sign, send, approve, or file anything.
- It does not make a final legal opinion where facts, authority, or current law are missing.
- It does not translate plugin command names into Turkish unless the whole repo has been renamed.

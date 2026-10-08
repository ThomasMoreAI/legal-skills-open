---
name: nda-review-zekaisuni
title: Gizlilik Sözleşmesi (NDA) İncelemesi
description: 'Reference: fast triage of inbound NDAs into GREEN / YELLOW / RED under the Turkish-law adapted commercial playbook. Built for business teams to self-serve before involving legal. Loaded by /commercial-legal:review when an NDA or confidentiality agreement is detected.'
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/commercial-legal/skills/nda-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: commercial
language: tr
---

# Gizlilik Sözleşmesi (NDA) İncelemesi

Bu skill gelen Gizlilik Sözleşmelerini (GS/NDA) hızlıca YEŞİL / SARI / KIRMIZI olarak tasnif eder. Amaç, standart ve avukat onaylı playbook'a uyan belgeleri imza sürecine yaklaştırmak, riskli veya kapsamı aşan belgeleri hukukçuya yönlendirmektir.

Komut ve dosya yolları repo uyumu için İngilizce kalır; hukuki değerlendirme Türk hukuku, Türk sözleşme pratiği, KVKK ve ilgili kurum uygulamasına göre yapılır.

## Matter Context

Check `## Matter workspaces` in `~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md`. If enabled and there is no active matter, ask:

> Bu inceleme hangi dosya için? `/commercial-legal:matter-workspace switch <slug>` komutunu çalıştırabilir veya `practice-level` diyebilirsiniz.

Load the active `matter.md`. Never read another matter unless `Cross-matter context` is on and the user explicitly asks.

## Destination Check - Mesleki Sır

Before producing an output, ask where it will go if the destination is named. Public channels, company-wide lists, counterparties, vendors, or opposing counsel may create confidentiality and strategy risks. Use Turkish framing:

> Bu çıktı avukatlık sırrı veya gizli hukuki değerlendirme içerebilir. Hukuk ekibi dışına gönderilecekse arındırılmış bir versiyon hazırlayayım.

Offer:

- legal-only full version,
- sanitized business version,
- both.

## Load the Playbook First

Determine which side the company is on:

- `sales-side`: company discloses information to a customer, partner, or vendor evaluating the company.
- `purchasing-side`: company evaluates another party's product or service.
- `mutual`: still identify whose paper it is and whose disclosure is operationally central.

Read:

`~/.claude/plugins/config/claude-for-legal/commercial-legal/CLAUDE.md` -> `## Playbook` -> matching side -> `NDA triage positions`.

If the matching side or NDA positions are missing, do not issue GREEN. Ask for the missing position and offer to record it in `CLAUDE.md`.

Also read `## Turkish Contract Concepts` from `CLAUDE.md`. Those definitions control the treatment of residuals, bakiye hükümler, damga vergisi, cezai şart, TBK validity/interpretation issues, and arabuluculuk handoff.

## Scope Check

Before NDA terms, check whether the document does more than confidentiality. Commercial NDAs can hide:

- münhasırlık,
- fikri mülkiyet devri or broad license,
- çalışan/müşteri ayartmama,
- rekabet etmeme,
- right of first refusal / priority negotiation,
- broad arbitration or jurisdiction for non-NDA disputes,
- cezai şart (TBK m.179-185),
- personal-data processing or data-transfer terms.

If the document contains non-confidentiality obligations, classify at least SARI and route for attorney review.

## Turkish-Law Concept Mapping

Use this language in outputs:

- `survival` -> `bakiye hükümler / sözleşmenin sona ermesinden sonra devam edecek yükümlülükler`.
- `residuals` -> `hafızada kalan bilgi istisnası`; do not treat it as harmless. Check TBK m.394-400 where employment/service confidentiality may matter, TTK m.54-55 unfair competition and trade secret concerns, KVKK, and competition-sensitive information.
- `liquidated damages / penalty` -> `cezai şart`; flag TBK m.179-185 proportionality and reduction risk.
- İngilizce belgelerde damga vergisi anlamına gelen ifadeler -> `damga vergisi (DVK/488)`; if the NDA includes high-value undertakings, penalty, guarantee, settlement, or amendment mechanics, flag tax/accounting review without calculating tax.
- `mediation` -> `arabuluculuk`; if dispute language moves toward litigation, flag 6325 and any mandatory mediation rules for later dispute handoff.
- Harsh or one-sided clauses may raise TBK m.19, m.27 and m.28 style interpretation/validity review; flag rather than overstate.

## Triage

Apply only the team's attorney-reviewed playbook. The categories are stable; the thresholds come from `CLAUDE.md`.

### GREEN - İmzaya Uygun

Use only if:

- all playbook checks pass,
- no non-NDA obligations are hidden,
- governing law / venue is acceptable under playbook,
- KVKK and competition-sensitive information issues are clear or not present,
- the playbook contains attorney-reviewed GREEN criteria.

If the user is a non-lawyer, add the attorney review gate before signature.

### YELLOW - Hukukçu İncelemesi Gerekli

Use if:

- one or more provisions deviate from playbook but are not hard stops,
- the playbook is silent,
- non-NDA obligations appear,
- KVKK, competition, or foreign-law issues require judgment.

### RED - Durdurun, Hukuk Birimine Yönlendirin

Use if:

- the NDA hits a never-accept position,
- one-way structure is unacceptable for this deal,
- süre or bakiye hükümler (survival) is incompatible with playbook,
- uncapped or disproportionate cezai şart appears,
- governing law/venue is on the never list,
- data transfer or AI/data-use terms create unapproved risk.

## Turkish-Law Check Reference

For each NDA, check:

- taraflar and capacity to sign,
- mutuality,
- definition of confidential information,
- oral disclosure confirmation,
- permitted purpose,
- required carveouts,
- compelled disclosure by court, regulator, or law,
- return/destruction and backup/archive carveout,
- süre and bakiye hükümler (survival),
- trade secret treatment,
- residuals / hafızada kalan bilgi istisnası,
- restrictive covenants,
- IP assignment or license language,
- cezai şart and TBK m.179-185 proportionality/reduction risk,
- governing law, venue, arbitration,
- KVKK personal data and data transfer,
- competition-sensitive information if parties are competitors,
- signature authority and signing process.

## KVKK Block

If the NDA involves personal data or platform/data evaluation, include:

```yaml
kvkk:
  kisisel_veri_paylasimi: true | false | belirsiz
  ozel_nitelikli_veri: true | false | belirsiz
  rol: veri_sorumlusu | veri_isleyen | ortak_sorumluluk | belirsiz
  veri_isleme_sozlesmesi_gerekli: true | false | belirsiz
  yurt_disina_aktarim: true | false | belirsiz
  not: "KVKK m.9 ve ilgili ikincil mevzuat ayrıca kontrol edilmeli."
```

## Rekabet Hukuku Block

If parties are competitors or potential competitors:

```yaml
rekabet_hukuku:
  rakipler_arasi_paylasim: true | false | belirsiz
  hassas_bilgi: fiyat | musteri | maliyet | strateji | kapasite | none | belirsiz
  not: "Rekabete hassas bilgi paylaşımı varsa Rekabet Kurumu uygulaması açısından hukukçu incelemesine yönlendir."
```

## Output

Prepend the work-product header from `CLAUDE.md`.

```markdown
## NDA Triage: [Counterparty]

**Durum:** GREEN | YELLOW | RED
**Taraf:** sales-side | purchasing-side | mutual
**Uygulanan playbook:** [CLAUDE.md reference]

### Yönetici Özeti
[Clean NDA ise tek cümle. Risk varsa aksiyon odaklı maddeler.]

### Kontroller
| Kontrol | Durum | Kaynak |
|---|---|---|
| [check] | uygun / sapma / belirsiz | [playbook / TBK / TTK / KVKK] |

### İşaretlenen Maddeler
**1. [Konu] - Madde [X]**
- Alıntı: "[short quote]"
- Neden sorun: [plain Turkish]
- Öneri: [accept / revise / escalate / use our paper]

### Sonraki Adım
[route to signature / ask legal / stop]
```

For a clean GREEN NDA, do not produce a long memo. Say only the required pass result, checks table, and next step.

## Redline Granularity

Use the smallest workable edit:

- word before phrase,
- phrase before sentence,
- sentence before clause,
- whole-clause replacement only when surgical drafting is unreadable.

If replacing a clause, explain why in the transmittal note.

## What this skill does not do

- It does not negotiate.
- It does not draft a new NDA from scratch.
- It does not make final decisions on YELLOW or RED items.
- It does not authorize signature or confirm signatory authority.
- It does not give a final legal opinion on foreign law.

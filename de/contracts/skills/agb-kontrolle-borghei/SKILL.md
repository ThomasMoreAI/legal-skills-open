---
name: agb-kontrolle-borghei
title: /vertragsrecht:agb-kontrolle
description: Inhaltskontrolle Allgemeiner Geschäftsbedingungen nach §§ 305–310 BGB – Einbeziehung (§ 305), überraschende Klauseln (§ 305c), Klauselverbote ohne Wertung (§ 309) und mit Wertung (§ 308), Generalklausel (§ 307), Anwendung im B2B-Verkehr (§ 310). Use when ein Vertragstext auf AGB-Wirksamkeit zu prüfen ist oder eine neue Klausel entworfen wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vertragsrecht/skills/agb-kontrolle
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /vertragsrecht:agb-kontrolle

## Zweck

AGB-Kontrolle ist Pflichtschritt jeder Vertragsprüfung in Deutschland. Standardvorlagen aus dem Internet halten häufig die §§ 307–309 BGB nicht ein. Dieser Skill liefert eine strukturierte Klauselprüfung mit Bezug auf BGH-Rechtsprechung und Standardkommentare.

## Eingaben

- Vertragsvorlage (B2C / B2B / gemischt)
- Branche (Onlineshop, IT-Dienstleistung, Mietvertrag, Beratung)
- Verhandlungssituation (vorformuliert vs. ausgehandelt — § 305 Abs. 1 S. 3 BGB)
- Klauseln, die fokussiert geprüft werden sollen (Haftungsbegrenzung, Gewährleistung, AGB-Änderung, Laufzeit, Verzugszinsen, salvatorische Klausel)

## Ablauf

### 1. Einbeziehung ([§ 305 BGB](https://www.gesetze-im-internet.de/bgb/__305.html))

- Verweis erkennbar
- Möglichkeit zumutbarer Kenntnisnahme (insb. § 305 Abs. 2 BGB: deutlich sichtbarer Hinweis, Möglichkeit zur Kenntnisnahme)
- B2B: vereinfachte Einbeziehung, **aber** § 305c und §§ 307–309 BGB (über § 310 Abs. 1 S. 2 BGB) gelten weiter

### 2. Überraschende Klauseln ([§ 305c BGB](https://www.gesetze-im-internet.de/bgb/__305c.html))

Klauseln, mit denen der Vertragspartner nicht zu rechnen brauchte → werden **nicht Vertragsbestandteil**. Faustregel: ungewöhnlicher Ort + ungewöhnlicher Inhalt.

### 3. Klauselverbote ohne Wertungsmöglichkeit ([§ 309 BGB](https://www.gesetze-im-internet.de/bgb/__309.html))

Schwarze Liste — automatisch unwirksam in **B2C** (in B2B nur als Indiz):

- § 309 Nr. 7 Buchst. a: Haftungsausschluss für Leben/Körper/Gesundheit auch bei einfacher Fahrlässigkeit → **unwirksam**
- § 309 Nr. 7 Buchst. b: Haftungsausschluss für grobe Fahrlässigkeit → **unwirksam**
- § 309 Nr. 5: Pauschalierter Schadensersatz ohne Möglichkeit Geringfügigkeitsnachweis → **unwirksam**

Häufige Fallen: „nutzt der Vertragspartner die Software …, haftet der Anbieter für Datenverluste nur in Höhe von 100 EUR" → bei B2C glatt unwirksam.

### 4. Klauselverbote mit Wertungsmöglichkeit ([§ 308 BGB](https://www.gesetze-im-internet.de/bgb/__308.html))

Graue Liste — unwirksam, soweit unangemessene Benachteiligung:

- Kein zu langer Annahmevorbehalt (§ 308 Nr. 1)
- Keine unangemessene Befristung (§ 308 Nr. 1a)
- Keine fingierten Willenserklärungen (§ 308 Nr. 5)

### 5. Generalklausel ([§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html))

**Auffangtatbestand.** Unangemessene Benachteiligung entgegen Treu und Glauben → unwirksam. Insbesondere bei:

- Abweichung vom dispositiven Recht (§ 307 Abs. 2 Nr. 1 BGB)
- Vertragszweckgefährdung (§ 307 Abs. 2 Nr. 2 BGB)
- Transparenzgebot (§ 307 Abs. 1 S. 2 BGB) — sprachlich klar, verständlich, durchschaubar

### 6. B2B-Modifikation ([§ 310 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__310.html))

§§ 308–309 gelten nicht direkt, aber **Indizwirkung**. § 305c, § 307 gelten unverändert. Im B2B wird häufiger gehalten, was im B2C scheitert — aber **nicht alles**.

### 7. Rechtsfolgen

Bei Unwirksamkeit: **kein** geltungserhaltende Reduktion ([§ 306 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__306.html)). Lücke wird durch dispositives Recht aufgefüllt. Gesamtnichtigkeit nur ausnahmsweise (§ 306 Abs. 3 BGB).

## Quellen

### Statute

- [§§ 305, 305a, 305b, 305c BGB](https://www.gesetze-im-internet.de/bgb/__305.html)
- [§ 306 BGB](https://www.gesetze-im-internet.de/bgb/__306.html), [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html), [§ 308 BGB](https://www.gesetze-im-internet.de/bgb/__308.html), [§ 309 BGB](https://www.gesetze-im-internet.de/bgb/__309.html)
- [§ 310 BGB](https://www.gesetze-im-internet.de/bgb/__310.html) (Anwendungsbereich)

### Kommentare

- Grüneberg, Palandt-Nachfolger, BGB, 83. Aufl. 2024, §§ 305 ff.
- Basedow, in: MüKoBGB, 9. Aufl. 2023, § 305 Rn. 1 ff.
- Wurmnest, in: MüKoBGB, 9. Aufl. 2023, § 307 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 22.11.2012 – VII ZR 222/12, NJW 2013, 856 (Transparenzgebot) `[unverifiziert – prüfen]`
- BGH, Urt. v. 18.07.2012 – VIII ZR 337/11, NJW 2012, 3373 (Preisanpassungsklauseln) `[unverifiziert – prüfen]`

## Ausgabeformat

```
AGB-KONTROLLE — <Vertragstitel> — <Datum>

I.   Einbeziehung (§ 305)            [✅ / 🟡 / ❌]
II.  Überraschende Klauseln (§ 305c) [✅ / ❌ — Liste]
III. Klauselverbote § 309            [✅ / ❌ — Liste]
IV.  Klauselverbote § 308            [✅ / 🟡 — Liste]
V.   Generalklausel § 307            [✅ / 🟡 / ❌ — Begründung]
VI.  Transparenzgebot                [✅ / 🟡]
VII. B2B-Modifikation (§ 310)        [N/A / berücksichtigt]

Klauselbefund (pro problematischer Klausel):
  Klausel: "<Wortlaut>"
  Problem: <…>
  Norm: §§ <…>
  Empfehlung: <Neufassungsvorschlag>

Gesamtbefund: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Haftungspauschalisierung in B2C** ohne Differenzierung Fahrlässigkeitsgrade → unwirksam, voller dispositiver Schadensersatz.
- **Salvatorische Klausel** ohne Sinn → reicht nicht, da keine geltungserhaltende Reduktion möglich.
- **Verweis auf zusätzliche Bedingungen im Internet** ohne Einbeziehung → unwirksam (§ 305 Abs. 2 BGB).
- **AGB-Änderungsvorbehalt** ohne Zustimmungsfiktion und Widerspruchsfrist → unwirksam (§ 308 Nr. 5 BGB).
- **B2B-Vorlage als B2C-Vorlage missbraucht** → § 309-Liste schlägt durch.

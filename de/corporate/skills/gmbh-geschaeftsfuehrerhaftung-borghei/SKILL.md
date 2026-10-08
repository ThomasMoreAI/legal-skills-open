---
name: gmbh-geschaeftsfuehrerhaftung-borghei
title: /gesellschaftsrecht:gmbh-geschaeftsfuehrerhaftung
description: Prüfung der zivilrechtlichen Geschäftsführerhaftung gegenüber der GmbH (§ 43 GmbHG), der Außenhaftung in der Krise (§ 64 GmbHG / § 15b InsO) und der Insolvenzantragspflicht (§ 15a InsO). Use when ein Geschäftsführer in Anspruch genommen wird oder eine Gesellschaft Regressansprüche gegen einen ausgeschiedenen GF prüft.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/gesellschaftsrecht/skills/gmbh-geschaeftsfuehrerhaftung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: corporate
language: de
---

# /gesellschaftsrecht:gmbh-geschaeftsfuehrerhaftung

## Zweck

Die Haftung des GmbH-Geschäftsführers ist das häufigste Hochrisiko-Mandat im Gesellschaftsrecht: Innenhaftung gegenüber der Gesellschaft, Außenhaftung in der Krise, strafrechtliche Insolvenzverschleppung. Dieser Skill identifiziert Anspruchsgrundlagen und Verteidigungslinien.

## Eingaben

- Position (alleiniger GF, mehrgliedrige GF, Liquidator)
- Anspruchsteller (Gesellschaft, Gesellschafter, Insolvenzverwalter, Gläubiger, Finanzamt, Sozialversicherung)
- Pflichtverletzung (konkret: Zahlung in der Krise, riskante Investition, Verstoß gegen Compliance-Programm, ungesicherte Darlehensvergabe)
- Zeitliche Lage (vor / nach Eintritt von Zahlungsunfähigkeit oder Überschuldung)
- D&O-Versicherung vorhanden?

## Ablauf

### 1. Anspruchsgrundlagen-Reihenfolge

**Innenverhältnis:**
1. **§ 43 Abs. 2 GmbHG** — Schadensersatz bei Pflichtverletzung gegenüber Gesellschaft (Sorgfalt eines ordentlichen Geschäftsmanns, § 43 Abs. 1)
2. **§ 43 Abs. 3 GmbHG** — Solidarhaftung mehrerer GF
3. **§ 64 S. 1 GmbHG / § 15b InsO** — Erstattung von Zahlungen nach Eintritt der Insolvenzreife
4. **§ 31 GmbHG** — Erstattung verbotener Auszahlungen (Stammkapitalverstoß)
5. **§ 30 GmbHG** — Auszahlungsverbot

**Außenverhältnis:**
1. **§ 15a Abs. 1 InsO** — Insolvenzantragspflicht (3 Wochen ab Zahlungsunfähigkeit, 6 Wochen ab Überschuldung)
2. **§ 823 Abs. 2 BGB i.V.m. § 15a InsO** — Außenhaftung wegen Insolvenzverschleppung gegenüber Neugläubigern
3. **§ 64 S. 3 GmbHG / § 15b Abs. 5 InsO** — Erstattung von Zahlungen, die zur Zahlungsunfähigkeit führten
4. **§ 69 AO** — Steuerhaftung des GF
5. **§ 28e Abs. 1 SGB IV** — Sozialversicherungsbeiträge

### 2. Pflichtprogramm (§ 43 Abs. 1 GmbHG)

Sorgfalt eines ordentlichen Geschäftsmanns. **Business Judgment Rule** im GmbH-Recht analog § 93 Abs. 1 S. 2 AktG (BGH, ARAG/Garmenbeck): Haftungsfreistellung, wenn

- bei unternehmerischer Entscheidung
- auf angemessener Informationsgrundlage
- ohne Sonderinteressen
- zum Wohl der Gesellschaft gehandelt

### 3. Krisenhaftung (§ 64 GmbHG a.F. → § 15b InsO seit StaRUG-Umsetzung 2021)

Nach Eintritt der **Zahlungsunfähigkeit** (§ 17 InsO) oder **Überschuldung** (§ 19 InsO) sind Zahlungen aus dem Gesellschaftsvermögen verboten, wenn sie die Insolvenzmasse mindern. Ausnahme: Zahlungen, die mit Sorgfalt eines ordentlichen Geschäftsmanns vereinbar sind (Aufrechterhaltung des Geschäftsbetriebs in der Antragsfrist).

### 4. Insolvenzantragspflicht ([§ 15a InsO](https://www.gesetze-im-internet.de/inso/__15a.html))

- **3 Wochen** ab Zahlungsunfähigkeit (§ 17 InsO)
- **6 Wochen** ab Überschuldung (§ 19 InsO)
- Strafbarkeit § 15a Abs. 4 InsO bei Vorsatz, Abs. 5 bei Fahrlässigkeit
- Haftung gegenüber Neugläubigern aus § 823 Abs. 2 BGB i.V.m. § 15a InsO

### 5. Verteidigungslinien

- **Business Judgment Rule** (s.o.)
- **Entlastung durch Gesellschafter** (§ 46 Nr. 5 GmbHG)
- **Verjährung** (§ 43 Abs. 4 GmbHG: 5 Jahre)
- **D&O-Versicherung** — Deckungsvoraussetzungen prüfen
- **Mitverschulden der Gesellschaft** (§ 254 BGB)
- **Beweislast:** Gesellschaft trägt Beweislast für Pflichtverletzung und Schaden; GF trägt Beweislast für Sorgfaltsbeachtung (BGH, Urt. v. 04.11.2002 – II ZR 224/00, NJW 2003, 358 `[unverifiziert – prüfen]`)

## Quellen

### Statute

- [§ 43 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__43.html), [§ 64 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__64.html)
- [§ 30 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__30.html), [§ 31 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__31.html)
- [§ 15a InsO](https://www.gesetze-im-internet.de/inso/__15a.html), [§ 15b InsO](https://www.gesetze-im-internet.de/inso/__15b.html), [§ 17 InsO](https://www.gesetze-im-internet.de/inso/__17.html), [§ 19 InsO](https://www.gesetze-im-internet.de/inso/__19.html)
- [§ 823 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__823.html)
- [§ 69 AO](https://www.gesetze-im-internet.de/ao_1977/__69.html), [§ 34 AO](https://www.gesetze-im-internet.de/ao_1977/__34.html)
- [§ 93 AktG](https://www.gesetze-im-internet.de/aktg/__93.html) (analog)

### Kommentare

- Altmeppen, GmbHG, 11. Aufl. 2023, § 43 Rn. 1 ff.
- Fleischer, in: MüKoGmbHG, 4. Aufl. 2022, § 43 Rn. 1 ff.
- Karsten Schmidt / Lutter, AktG, 4. Aufl. 2020, § 93 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 21.04.1997 – II ZR 175/95, NJW 1997, 1926 („ARAG/Garmenbeck", BJR) `[unverifiziert – prüfen]`
- BGH, Urt. v. 04.11.2002 – II ZR 224/00, NJW 2003, 358 (Beweislast) `[unverifiziert – prüfen]`
- BGH, Urt. v. 16.03.2009 – II ZR 280/07, NJW 2009, 2127 (§ 64 GmbHG a.F.) `[unverifiziert – prüfen]`

## Ausgabeformat

```
GF-HAFTUNGS-PRÜFUNG — <Mandat> — <Datum>

I.    Anspruchsgrundlage              [§§ 43, 64 GmbHG / § 15a InsO / § 823]
II.   Zeitliche Einordnung            [vor / in / nach Krise]
III.  Pflichtverletzung                Tatbestand: <…>
                                       Verschulden: <…>
IV.   Business Judgment Rule           [✅ / ❌ — Begründung]
V.    Schaden / Höhe                   <…>
VI.   Verteidigung
      - Entlastung § 46 Nr. 5          [vorhanden / nicht]
      - Verjährung § 43 Abs. 4         [eingetreten / nicht]
      - D&O                            [Deckung / nicht]
      - Mitverschulden § 254           [möglich / nicht]
VII.  Strafrechtliches Risiko § 15a Abs. 4, 5 InsO  [🟢 / 🟡 / 🔴]

Empfehlung: <…>
```

## Risiken / typische Fehler

- **Insolvenzantragsfrist § 15a InsO übersehen** → strafbar, persönliche Haftung gegenüber Neugläubigern.
- **Zahlungen in der Krise** ohne Prüfung gegen § 15b InsO → persönliche Erstattungspflicht.
- **„Entlastung durch Gesellschafter" angenommen,** obwohl der Beschluss formal nicht den fragenrelevanten Sachverhalt umfasste → keine Haftungsbefreiung.
- **D&O-Deckung als Selbstläufer betrachtet** → Ausschlüsse (vorsätzliche Pflichtverletzung, Insolvenzverschleppung) müssen einzeln geprüft werden.
- **Steuerliche Vertreterhaftung § 69 AO** ohne Lohnsteuer-Abführung in der Krise vergessen.

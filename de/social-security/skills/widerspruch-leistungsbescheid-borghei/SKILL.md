---
name: widerspruch-leistungsbescheid-borghei
title: /sozialrecht:widerspruch-leistungsbescheid
description: Bescheidanalyse und Entwurf einer Widerspruchsschrift gegen einen sozialrechtlichen Leistungsbescheid – Frist § 84 SGG, Form §§ 81, 84 SGG, Begründungsmängel § 35 SGB X, aufschiebende Wirkung § 86a SGG, einstweiliger Rechtsschutz § 86b SGG, Anschluss-Klagefrist § 87 SGG. Use when Mandant einen Bescheid des Jobcenters, der Rentenversicherung, der Krankenkasse oder des Sozialamts angreifen möchte.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/sozialrecht/skills/widerspruch-leistungsbescheid
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: social-security
language: de
---

# /sozialrecht:widerspruch-leistungsbescheid

## Zweck

Der Widerspruch ist im Sozialrecht regelmäßiges Vorverfahren (§§ 78 ff. SGG) und Bedingung für die spätere Klage. Wirksam ist er nur bei **fristgerechter, formgerechter Einlegung bei der Ausgangsbehörde**. Dieser Skill prüft den angegriffenen Bescheid systematisch (Tenor, Begründung, Rechtsgrundlage, Anhörung), entwirft die Widerspruchsschrift und sichert ggf. die aufschiebende Wirkung über § 86b SGG.

## Eingaben

- Bescheid (Behörde, Aktenzeichen, Datum, Bekanntgabedatum, Anlagen)
- Art des Bescheids (Ablehnung, Bewilligung mit zu niedrigem Betrag, Aufhebung, Erstattung, Sanktion / Leistungsminderung)
- Rechtsbehelfsbelehrung (vorhanden / fehlerhaft / fehlend?)
- Sachverhaltsdarstellung des Mandanten und seine Einwände
- Vorausgegangene Anhörung § 24 SGB X (ja / nein / unzureichend)?
- Aktenstand (Akteneinsicht § 25 SGB X bereits beantragt?)
- Bedürfnis nach Eilrechtsschutz (Existenzminimum, Krankenversicherung, Wohnungsverlust)

## Sub-Agent-Architektur

Researcher liefert SGG- und SGB-X-Normen, Kassler Kommentar zur Bescheidanalyse und BSG-Rechtsprechung zu Fristen / Formfragen. Drafter erstellt die Widerspruchsschrift sowie — bei Bedarf — den Antrag auf Anordnung der aufschiebenden Wirkung. Reviewer prüft Frist (mit konkretem Datum), Antragsformulierung, Mitwirkungs- und Berufsrechtshinweise.

## Ablauf

### 1. Fristprüfung ([§ 84 SGG](https://www.gesetze-im-internet.de/sgg/__84.html), [§ 66 SGG](https://www.gesetze-im-internet.de/sgg/__66.html))

| Konstellation | Frist | Grundlage |
|---|---|---|
| Rechtsbehelfsbelehrung korrekt | **1 Monat** ab Bekanntgabe | § 84 Abs. 1 SGG |
| Belehrung fehlt oder fehlerhaft | **1 Jahr** ab Bekanntgabe | § 66 Abs. 2 SGG |
| Auslandszustellung | 3 Monate | § 84 Abs. 1 S. 2 SGG |

**Bekanntgabe bei Postzustellung:** 3. Tag nach Aufgabe zur Post (§ 37 Abs. 2 SGB X), sofern nicht später zugegangen.

**Berechnung des Fristendes:** §§ 64 SGG i.V.m. §§ 187 ff. BGB. Fällt das Ende auf Samstag, Sonntag oder Feiertag → § 64 Abs. 3 SGG: Frist endet am nächsten Werktag.

### 2. Form ([§ 81 SGG](https://www.gesetze-im-internet.de/sgg/__81.html), [§ 84 SGG](https://www.gesetze-im-internet.de/sgg/__84.html))

- Schriftlich oder zur Niederschrift bei der Ausgangsbehörde
- E-Mail genügt bei einfacher E-Mail **nicht** (keine sichere elektronische Form). § 36a SGB I i.V.m. § 65a SGG: qualifizierte elektronische Signatur oder besonderes elektronisches Anwaltspostfach (beA).
- Telefax: zulässig (Schriftformersatz)
- **Anschrift:** Widerspruch geht an die **Ausgangsbehörde** (§ 84 Abs. 1 S. 1 SGG), nicht an die Widerspruchsbehörde. Falschadressierung wird nach § 84 Abs. 2 SGG nur geheilt, wenn das Schreiben rechtzeitig bei der Ausgangsbehörde eingeht.

### 3. Bescheidanalyse

Sechs Prüfpunkte:

| Punkt | Norm | Fragestellung |
|---|---|---|
| Bestimmtheit | § 33 Abs. 1 SGB X | Ist der Regelungsgehalt eindeutig? |
| Begründung | [§ 35 SGB X](https://www.gesetze-im-internet.de/sgb_10/__35.html) | Sind tragende tatsächliche / rechtliche Erwägungen erkennbar? |
| Rechtsgrundlage | konkrete Norm im Tenor / in den Gründen | Ist die zitierte Norm einschlägig und vollständig? |
| Anhörung | [§ 24 SGB X](https://www.gesetze-im-internet.de/sgb_10/__24.html) | Bei belastendem VA: stattgefunden? Heilung § 41 SGB X? |
| Ermessen | [§ 39 SGB I](https://www.gesetze-im-internet.de/sgb_1/__39.html) | Bei Ermessensentscheidungen: Ermessensausfall / -fehler? |
| Aufhebungsnorm | §§ 44, 45, 48 SGB X | Bei Aufhebung/Erstattung: richtige Norm gewählt? |

### 4. Aufhebung und Erstattung — Sonderprüfung

| Norm | Tatbestand | Frist |
|---|---|---|
| [§ 44 SGB X](https://www.gesetze-im-internet.de/sgb_10/__44.html) | Rücknahme rechtswidriger nicht begünstigender VA (Überprüfungsantrag) | grundsätzlich rückwirkend bis 1 Jahr (§ 44 Abs. 4) |
| [§ 45 SGB X](https://www.gesetze-im-internet.de/sgb_10/__45.html) | Rücknahme rechtswidriger begünstigender VA | Vertrauensschutz § 45 Abs. 2; 2-/10-Jahres-Frist § 45 Abs. 3, 4 |
| [§ 48 SGB X](https://www.gesetze-im-internet.de/sgb_10/__48.html) | Aufhebung bei wesentlicher Änderung der Verhältnisse | i.V.m. § 50 SGB X (Erstattung) |
| [§ 50 SGB X](https://www.gesetze-im-internet.de/sgb_10/__50.html) | Erstattung | Folge der Aufhebung |

### 5. Aufschiebende Wirkung ([§ 86a SGG](https://www.gesetze-im-internet.de/sgg/__86a.html), [§ 86b SGG](https://www.gesetze-im-internet.de/sgg/__86b.html))

**Grundregel § 86a Abs. 1 SGG:** Widerspruch und Klage haben aufschiebende Wirkung.

**Ausnahmen § 86a Abs. 2 SGG (entfällt aufschiebende Wirkung):**

- Beitragsbescheide
- bei Verwaltungsakten, die laufende Leistungen entziehen, herabsetzen oder zurückfordern (Nr. 4!)
- in Vollstreckungsmaßnahmen
- soweit gesetzlich ausdrücklich angeordnet

→ Bei Entziehungs- / Aufhebungs- / Erstattungsbescheiden im SGB II / SGB XII ist **regelmäßig** ein Antrag auf Anordnung der aufschiebenden Wirkung gem. **§ 86b Abs. 1 Nr. 2 SGG** beim Sozialgericht erforderlich, um existenzielle Notlage abzuwenden.

**Antrag § 86b SGG:**

- Abs. 1: Anordnung / Wiederherstellung aufschiebender Wirkung (gegen belastenden VA)
- Abs. 2: Regelungsanordnung (für vorläufige Leistung trotz Ablehnung) — Anordnungsanspruch + Anordnungsgrund

### 6. Anschluss — Klagefrist

[§ 87 SGG](https://www.gesetze-im-internet.de/sgg/__87.html): Klage zum Sozialgericht binnen **1 Monat** ab Bekanntgabe des Widerspruchsbescheids. Untätigkeitsklage § 88 SGG nach 6 Monaten ohne Bescheidung (3 Monate beim Untätigkeitswiderspruch in Sozialhilfe / Bürgergeld? — Einzelnorm prüfen).

### 7. Akteneinsicht und Mitwirkung

- [§ 25 SGB X](https://www.gesetze-im-internet.de/sgb_10/__25.html): Akteneinsicht des Beteiligten / Bevollmächtigten
- Art. 15 DSGVO: Datenauskunft (parallel)
- [§ 60 SGB I](https://www.gesetze-im-internet.de/sgb_1/__60.html): Mitwirkung — bei Widerspruchsbegründung ggf. nachreichen

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 78](https://www.gesetze-im-internet.de/sgg/__78.html), [§ 81](https://www.gesetze-im-internet.de/sgg/__81.html), [§ 84](https://www.gesetze-im-internet.de/sgg/__84.html), [§ 85](https://www.gesetze-im-internet.de/sgg/__85.html), [§ 86a](https://www.gesetze-im-internet.de/sgg/__86a.html), [§ 86b](https://www.gesetze-im-internet.de/sgg/__86b.html), [§ 87](https://www.gesetze-im-internet.de/sgg/__87.html), [§ 64](https://www.gesetze-im-internet.de/sgg/__64.html), [§ 66](https://www.gesetze-im-internet.de/sgg/__66.html) SGG
- [§ 24](https://www.gesetze-im-internet.de/sgb_10/__24.html), [§ 25](https://www.gesetze-im-internet.de/sgb_10/__25.html), [§ 31](https://www.gesetze-im-internet.de/sgb_10/__31.html), [§ 33](https://www.gesetze-im-internet.de/sgb_10/__33.html), [§ 35](https://www.gesetze-im-internet.de/sgb_10/__35.html), [§ 37](https://www.gesetze-im-internet.de/sgb_10/__37.html), [§ 41](https://www.gesetze-im-internet.de/sgb_10/__41.html), [§ 44](https://www.gesetze-im-internet.de/sgb_10/__44.html), [§ 45](https://www.gesetze-im-internet.de/sgb_10/__45.html), [§ 48](https://www.gesetze-im-internet.de/sgb_10/__48.html), [§ 50](https://www.gesetze-im-internet.de/sgb_10/__50.html) SGB X
- [§ 39 SGB I](https://www.gesetze-im-internet.de/sgb_1/__39.html); [§ 60 SGB I](https://www.gesetze-im-internet.de/sgb_1/__60.html)

### Kommentare

- B. Schmidt, in: Meyer-Ladewig/Keller/Schmidt, SGG, 14. Aufl. 2023, § 84 Rn. … (Widerspruchsfrist und -form)
- Burkiczak, in: KassKomm, Stand 2024, § 35 SGB X Rn. … (Begründungspflicht)
- Steinwedel, in: KassKomm, Stand 2024, § 45 SGB X Rn. … (Rücknahme begünstigender VA, Vertrauensschutz)
- Wahrendorf, in: BeckOK Sozialrecht, § 86b SGG Rn. … (einstweiliger Rechtsschutz)

### Rechtsprechung (`[unverifiziert – prüfen in juris / SozR]`)

1. BSG, Urt. v. 18.06.2014 – B 14 AS 5/13 R (Anhörung § 24 SGB X, Heilung § 41)
2. BVerfG, Beschl. v. 12.05.2005 – 1 BvR 569/05 (effektiver Rechtsschutz § 86b SGG bei Existenzsicherung)
3. BSG, Urt. v. 16.10.2007 – B 8/9b SO 8/06 R (Begründungspflicht § 35 SGB X)
4. BSG, Urt. v. 24.02.2011 – B 14 AS 87/09 R (Wirkungen § 45 SGB X bei rechtswidriger Bewilligung)

## Ausgabeformat

```
WIDERSPRUCH GEGEN <Bescheid-Bezeichnung>
Risikoeinstufung: 🟢/🟡/🔴

A. Bescheidanalyse
   1. Tenor:                       <…>
   2. Rechtsgrundlage im Bescheid: <…>
   3. Bekanntgabe:                 <Datum> (§ 37 Abs. 2 SGB X)
   4. Rechtsbehelfsbelehrung:      vorhanden / fehlerhaft / fehlend
   5. Anhörung § 24 SGB X:         ja / nein / unzureichend
   6. Begründung § 35 SGB X:       ausreichend / lückenhaft / fehlt

B. Fristen
   - Widerspruchsfrist:  endet am <konkretes Datum> (§ 84 / § 66 SGG)
   - Klagefrist § 87 SGG (nach WS-Bescheid): 1 Monat
   - Wiedervorlage: <Datum − 5 WT>

C. Materielle Einwände (Gutachtenstil / Urteilsstil)
   1. <Einwand 1 — Norm, Tatsache, Beleg>
   2. <Einwand 2>

D. Antrag aufschiebende Wirkung § 86b Abs. 1 Nr. 2 SGG
   <falls Leistung entzogen/zurückgefordert>

E. Widerspruchsschrift (Entwurf)

   An <Ausgangsbehörde>
   Az.: <…>

   Widerspruch
   gegen den Bescheid vom <Datum>, zugestellt am <Datum>.

   Namens und in Vollmacht der/des Widerspruchsführer/in legen wir
   gegen den im Betreff bezeichneten Bescheid

         Widerspruch

   ein und beantragen,
         1. den Bescheid vom <Datum> aufzuheben / abzuändern;
         2. dem/der Widerspruchsführer/in Leistungen nach <…> zu gewähren;
         3. die Hinzuziehung des Bevollmächtigten im Vorverfahren
            für notwendig zu erklären (§ 63 Abs. 2 SGB X).

   Begründung
   I. Sachverhalt
      <…>
   II. Rechtliche Würdigung
      1. <…>
      2. <…>
   III. Beweismittel / Anlagen
      <…>

   Mit freundlichen Grüßen
   <Rechtsanwalt/-anwältin>

F. Quellenverzeichnis
   <Statute / Kommentare / Rspr. mit Markern>

G. Mandanten-Hinweise
   - Beratungshilfe / PKH §§ 73a SGG, 114 ZPO
   - Kostenrisiko: Verfahren ist gerichtskostenfrei (§ 183 SGG),
     aber außergerichtliche Kosten / RVG-Honorar fallen an
   - Mitwirkungspflichten § 60 SGB I (Unterlagen)
```

## Beispiele

### Beispiel (gekürzt — Aufhebungs- und Erstattungsbescheid Jobcenter)

> Mit Bescheid vom 03.04.2026 (zugestellt am 06.04.2026) hat das Jobcenter Musterstadt einen Aufhebungs- und Erstattungsbescheid über 3.840 EUR erlassen, gestützt auf § 48 Abs. 1 S. 2 Nr. 3 SGB X i.V.m. § 50 Abs. 1 SGB X. Begründet wird die Aufhebung mit nicht angegebenem Einkommen aus einem Minijob.
>
> **I. Fristen.** Bekanntgabe gem. § 37 Abs. 2 SGB X am 06.04.2026. Widerspruchsfrist § 84 Abs. 1 SGG endet damit am **06.05.2026** (Mittwoch, Werktag — § 64 Abs. 3 SGG nicht einschlägig). Eingang bei der Ausgangsbehörde bis dahin gewährleistet.
>
> **II. Aufschiebende Wirkung.** Nach § 86a Abs. 2 Nr. 4 SGG entfällt die aufschiebende Wirkung für die Erstattungsforderung. Es ist parallel zum Widerspruch ein Antrag nach § 86b Abs. 1 Nr. 2 SGG zu stellen, um Beitreibungsmaßnahmen abzuwenden.
>
> **III. Materielle Einwände.**
>
> 1. Anhörung § 24 SGB X — der Mandant trägt vor, dass keine Anhörung erfolgt sei. Heilung § 41 Abs. 1 Nr. 3 SGB X ist während des Widerspruchsverfahrens möglich; sollte sie unterbleiben, ist der Bescheid formell rechtswidrig.
> 2. Anrechenbares Einkommen — der Mandant hat die Lohnabrechnungen monatlich übermittelt (Anlage 1 ff.). Eine wesentliche Änderung i.S.d. § 48 Abs. 1 S. 2 Nr. 3 SGB X liegt damit nicht vor.
>
> **IV. Anträge.** Es wird beantragt, den Aufhebungs- und Erstattungsbescheid vom 03.04.2026 aufzuheben sowie die Hinzuziehung des Bevollmächtigten im Vorverfahren für notwendig zu erklären (§ 63 Abs. 2 SGB X).

## Risiken / typische Fehler

- **Falschadressierung:** Widerspruch geht an die **Ausgangsbehörde** (§ 84 Abs. 1 SGG), nicht an die Widerspruchsbehörde. Andernfalls: Fristproblem.
- **E-Mail-Falle:** Einfache E-Mail wahrt die Schriftform nicht; § 36a SGB I / § 65a SGG verlangen qualifizierte elektronische Signatur oder beA.
- **Aufschiebende Wirkung übersehen:** Bei Aufhebungs-/Erstattungsbescheiden entfällt sie nach § 86a Abs. 2 Nr. 4 SGG. Ohne § 86b-Antrag droht Vollstreckung.
- **Anhörungsfehler vergessen:** § 24 SGB X-Verstoß ist heilbar (§ 41 SGB X), aber regelmäßig ein lohnender Einwand, weil die Behörde dadurch zur Aktenoffenlegung gezwungen wird.
- **Begründungspflicht § 35 SGB X:** "Aus den Akten ergibt sich …" reicht nicht. Tragende tatsächliche und rechtliche Erwägungen müssen erkennbar sein.
- **Klagefrist § 87 SGG** vergessen, weil der Mandant erwartet, dass nach Widerspruch automatisch geklagt wird — nein. Nach Widerspruchsbescheid läuft eigene Monatsfrist.
- **Überprüfungsantrag § 44 SGB X verwechselt:** Wenn die Widerspruchsfrist verstrichen ist, ist § 44 SGB X (rückwirkend bis 1 Jahr) das verbleibende Vehikel — nur bei rechtswidriger nicht-begünstigender Belastung.
- **Notwendigkeit § 63 Abs. 2 SGB X** nicht beantragt → Mandant trägt RVG-Gebühren ohne Erstattung.

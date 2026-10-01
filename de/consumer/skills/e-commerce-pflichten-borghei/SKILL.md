---
name: e-commerce-pflichten-borghei
title: /it-recht:e-commerce-pflichten
description: 'Prüfung der Pflichten eines Online-Shops im elektronischen Geschäftsverkehr: allgemeine Pflichten (§ 312i BGB), besondere Verbraucherpflichten und Button-Lösung (§ 312j BGB) sowie Widerrufsrecht (§ 312g, § 355 BGB), inklusive der Folgen von Verstößen. Use when ein Online-Shop oder Bestellprozess auf gesetzliche Pflichten und Abmahnrisiken geprüft werden soll.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/it-recht/skills/e-commerce-pflichten
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: consumer
language: de
---

# /it-recht:e-commerce-pflichten

## Zweck

Online-Shops unterliegen einem dichten Pflichtenprogramm. Verstöße sind nicht nur abmahnfähig, sondern können dazu führen, dass der Vertrag gar nicht oder das Widerrufsrecht stark verlängert zustande kommt. Dieser Skill prüft einen Bestellprozess entlang der allgemeinen Pflichten (**§ 312i BGB**), der besonderen Verbraucherpflichten samt **Button-Lösung** (**§ 312j BGB**) und des Widerrufsrechts (**§ 312g BGB**, **§ 355 BGB**) und benennt die zivil- und wettbewerbsrechtlichen Folgen.

## Eingaben

- Shop-Typ und Vertragsgegenstand (Waren, digitale Inhalte, Dienstleistungen, Abonnement)
- Adressatenkreis (B2C / B2B / gemischt)
- Bestellstrecke (Warenkorb, Bestellübersicht, Button-Beschriftung)
- Pflichtangaben vor Bestellung (Gesamtpreis, Lieferbeschränkungen, Zahlarten)
- Widerrufsbelehrung und Muster-Widerrufsformular vorhanden?
- Bestätigungsmail / Eingangsbestätigung eingerichtet?

## Sub-Agent-Architektur

Die Prüfung verteilt sich auf drei Rollen. Ein **Prozess-Agent** geht die Bestellstrecke technisch durch und prüft die allgemeinen Pflichten nach § 312i BGB (Korrekturmöglichkeit bei Eingabefehlern, Zugangsbestätigung, abrufbare Vertragsbedingungen). Ein **Verbraucher-Agent** prüft die besonderen Pflichten nach § 312j BGB — unmittelbar vor Bestellung hervorgehobene Pflichtangaben und die Button-Lösung („zahlungspflichtig bestellen") — und stellt fest, ob überhaupt ein wirksamer Vertrag zustande kommt. Ein **Widerrufs-Agent** prüft Bestehen, Belehrung und Fristlauf des Widerrufsrechts (§ 312g, § 355 BGB) und etwaige Ausschlüsse. Eine zusammenführende Bewertung leitet daraus zivilrechtliche Folgen und Abmahnrisiken ab. Zitierte Gerichtsentscheidungen werden verifiziert oder mit `[unverifiziert – prüfen]` markiert (Zero-Fabrication).

## Ablauf

### 1. Allgemeine Pflichten (§ 312i BGB)

Bei Verträgen im elektronischen Geschäftsverkehr (auch B2B, dispositiv):

- angemessene technische Mittel zur Erkennung und Korrektur von **Eingabefehlern** vor Bestellung
- rechtzeitige, klare Information über die technischen Schritte zum Vertragsschluss
- unverzügliche elektronische **Bestätigung** des Zugangs der Bestellung
- Möglichkeit, Vertragsbestimmungen abzurufen und zu speichern

### 2. Besondere Verbraucherpflichten und Button-Lösung (§ 312j BGB)

- **Pflichtangaben** auf der Website allgemein: Lieferbeschränkungen und akzeptierte Zahlungsmittel klar und deutlich zu Beginn des Bestellvorgangs.
- Unmittelbar vor Abgabe der Bestellung: klare, hervorgehobene Angabe der wesentlichen Merkmale, des **Gesamtpreises**, ggf. Laufzeit/Mindestdauer.
- **Button-Lösung**: Die Schaltfläche muss gut lesbar mit nichts anderem als „zahlungspflichtig bestellen" oder einer entsprechend eindeutigen Formulierung beschriftet sein.
- Folge bei Verstoß: Der Vertrag kommt nach § 312j Abs. 4 BGB **nicht wirksam** zustande — der Verbraucher ist nicht zur Zahlung verpflichtet.

### 3. Widerrufsrecht (§ 312g BGB, § 355 BGB)

- Bei Fernabsatzverträgen mit Verbrauchern grundsätzlich Widerrufsrecht (§ 312g BGB), Ausnahmen in § 312g Abs. 2.
- **Widerrufsfrist** 14 Tage (§ 355 BGB); Beginn erst mit ordnungsgemäßer Belehrung und (bei Waren) Erhalt.
- Fehlende oder fehlerhafte Belehrung: Frist verlängert sich, Erlöschen spätestens 12 Monate und 14 Tage nach gesetzlichem Fristbeginn.
- Muster-Widerrufsbelehrung und Widerrufsformular bereitstellen.

### 4. Folgen von Verstößen

- Zivilrechtlich: kein wirksamer Vertrag (§ 312j Abs. 4), verlängerte Widerrufsfrist.
- Wettbewerbsrechtlich: **Abmahnung** durch Mitbewerber/Verbände nach UWG, Unterlassung, Kostenerstattung.

## Risiken / typische Fehler

- **Button-Lösung** fehlerhaft — eine Schaltfläche wie „Bestellung abschicken" oder „Anmelden" genügt § 312j Abs. 3 BGB nicht; es entsteht kein wirksamer Vertrag.
- **Verlängerte Widerrufsfrist** — fehlende/fehlerhafte Belehrung dehnt die Frist nach § 355 BGB auf bis zu 12 Monate und 14 Tage aus.
- **Abmahnung** — fehlende Pflichtangaben (Grundpreis, Lieferbeschränkungen) oder Belehrungsfehler sind nach UWG abmahnfähig.
- **Eingabefehler-Korrektur fehlt** — ohne Korrekturmöglichkeit und Eingangsbestätigung liegt ein Verstoß gegen § 312i BGB vor.

## Ausgabeformat

```
E-COMMERCE-PFLICHTEN — <Shop> — <Datum>

I.    Allgemeine Pflichten (§ 312i BGB)
      Eingabefehler-Korrektur:    [✓ / 🔴]
      Eingangsbestätigung:        [✓ / 🔴]
II.   Verbraucherpflichten (§ 312j BGB)
      Pflichtangaben vor Bestell.:[✓ / 🔴]
      Button-Lösung:              [✓ / 🔴 → kein wirksamer Vertrag]
III.  Widerrufsrecht (§ 312g / § 355 BGB)
      Belehrung korrekt:          [✓ / 🔴]
      Friststatus:                [14 Tage / verlängert bis 12 Mon.+14 Tg.]
IV.   Folgen
      Zivilrechtlich:             <…>
      Abmahnrisiko (UWG):         [niedrig / hoch]

Handlungsempfehlung:              <…>
```

## Quellen

- [§ 312i BGB](https://www.gesetze-im-internet.de/bgb/__312i.html) (allgemeine Pflichten im elektronischen Geschäftsverkehr)
- [§ 312j BGB](https://www.gesetze-im-internet.de/bgb/__312j.html) (besondere Pflichten, Button-Lösung)
- [§ 312g BGB](https://www.gesetze-im-internet.de/bgb/__312g.html), [§ 355 BGB](https://www.gesetze-im-internet.de/bgb/__355.html) (Widerrufsrecht)
- Art. 246a EGBGB (Informationspflichten Fernabsatz)
- EuGH, Urt. v. 30.05.2024 – C-400/22 (VT u. UR ./. Conny GmbH), NJW 2024, 2449 (Button-Lösung nach Art. 8 Abs. 2 RL 2011/83/EU auch bei bedingter Zahlungspflicht), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2024-05-30&Aktenzeichen=C-400/22)

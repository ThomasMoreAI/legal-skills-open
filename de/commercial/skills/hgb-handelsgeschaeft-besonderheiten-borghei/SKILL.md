---
name: hgb-handelsgeschaeft-besonderheiten-borghei
title: /handelsrecht:hgb-handelsgeschaeft-besonderheiten
description: Praxischeck der Besonderheiten des Vierten Buches HGB im Vergleich zum BGB-Schuldrecht – Handelsbrauch § 346, kaufmännische Sorgfalt § 347, Form § 350, Zinsen § 352, gutgläubiger Erwerb § 366, kaufmännisches Bestätigungsschreiben §§ 362/363 sowie insbesondere Untersuchungs- und Rügepflicht §§ 377/378 HGB. Use when ein B2B-Sachverhalt zu beurteilen ist und zu klären, ob HGB-Sonderregeln greifen oder das BGB anwendbar bleibt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/handelsrecht/skills/hgb-handelsgeschaeft-besonderheiten
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: commercial
language: de
---

# /handelsrecht:hgb-handelsgeschaeft-besonderheiten

## Zweck

Der Skill klärt für ein konkretes Geschäft, **ob HGB oder BGB** anwendbar ist und welche kaufmannsspezifischen Sonderregeln des Vierten Buches HGB die BGB-Lage verändern. Schwerpunkt ist die Untersuchungs- und Rügepflicht beim Handelskauf §§ 377/378 HGB, deren Versäumung den Verlust der Gewährleistungsrechte bedeutet – einer der praktisch häufigsten und folgenschwersten Mandantenirrtümer im B2B-Geschäft.

## Eingaben

- Parteien (Status: Kaufmann ja/nein nach §§ 1 ff. HGB)
- Geschäftsgegenstand (Kauf, Werk, Werklieferung, Dienst, Auftrag, Bürgschaft, Vertragsstrafe, …)
- Vertragsabschluss (formfrei, telefonisch, E-Mail, kaufmännisches Bestätigungsschreiben?)
- Bei Mangelproblem: Zeitpunkt der Lieferung, Zeitpunkt der Mängelentdeckung, Art des Mangels (offen/verdeckt), bisher erfolgte Rüge (Form, Zeitpunkt, Inhalt)
- konkrete Frage (Greift HGB? Ist Rügefrist gewahrt? Ist Schweigen Annahme? Gilt die Klausel ohne Form?)

## Sub-Agent-Architektur

Researcher liefert §§ 343–384 HGB, BGH-Rechtsprechung zu § 377 HGB "Unverzüglichkeit", kaufmännischem Bestätigungsschreiben und Handelsbrauch sowie Standardkommentare. Drafter prüft im Gutachten- oder Urteilsstil norm für norm, was sich gegenüber dem BGB ändert, und konzipiert ggf. ein Rügeschreiben. Reviewer prüft Rügefrist, Beweislast und Vollständigkeit.

## Ablauf

### 1. Vorfrage: Liegt ein Handelsgeschäft vor?

- **§ 343 HGB:** Handelsgeschäfte sind alle Geschäfte eines Kaufmanns, die zum Betrieb seines Handelsgewerbes gehören.
- **§ 344 HGB:** Vermutung – im Zweifel gehören die vom Kaufmann vorgenommenen Geschäfte zu seinem Handelsgewerbe.
- **Einseitiges vs. beidseitiges Handelsgeschäft:** Maßgeblich für §§ 343 ff. HGB ist häufig nur einseitige Kaufmannseigenschaft (§ 345 HGB), für § 377 HGB jedoch **beidseitiges** Handelsgeschäft.

### 2. Synoptische Übersicht: HGB-Spezialregeln vs. BGB

| Norm HGB | Inhalt | Abweichung vom BGB |
|---|---|---|
| **§ 346** | Handelsbräuche sind zu berücksichtigen. | Geht über § 157 BGB hinaus: Handelsbräuche wirken auch ohne Parteiwille. |
| **§ 347** | Sorgfalt eines ordentlichen Kaufmanns. | Strengerer Verschuldensmaßstab als § 276 BGB. |
| **§ 348** | Vertragsstrafenhöhe kann **nicht** nach § 343 BGB herabgesetzt werden. | Gerichtliche Reduktion ausgeschlossen. |
| **§ 349** | **Einrede der Vorausklage** bei Bürgschaft entfällt. | Selbstschuldnerische Bürgschaft kraft Gesetz. |
| **§ 350** | Bei Handelsgeschäften: **Schriftformerfordernisse** für Bürgschaft, Schuldversprechen, Schuldanerkenntnis (§§ 766, 780, 781 BGB) **entfallen**. | Formfreiheit im B2B. |
| **§ 352** | **Zinssatz 5 %** p.a. bei beidseitigem Handelsgeschäft. | BGB § 246: 4 %. |
| **§ 353** | Fälligkeitszinsen ab Fälligkeit. | Erweiterung gegenüber § 288 BGB. |
| **§ 354** | Vermutung der Entgeltlichkeit für Dienstleistungen des Kaufmanns. | Anders als § 612 BGB. |
| **§ 354a** | Abtretungsverbot bei Geldforderung in Handelsgeschäft **unwirksam** gegenüber Erstem Schuldner – Abtretung wirkt, Schuldner kann an Altgläubiger leisten. | Anders § 399 BGB. |
| **§§ 362, 363** | Schweigen eines Kaufmanns auf Antrag zur Geschäftsbesorgung gilt als Annahme (§ 362 HGB); kaufmännisches Bestätigungsschreiben (Gewohnheitsrecht, häufig § 363 HGB nahe). | Anders als § 151 BGB. |
| **§ 366** | Gutgläubiger Erwerb vom **Nichteigentümer-Kaufmann** auch bezüglich **Verfügungsbefugnis**. | Erweiterung gegenüber §§ 932 ff. BGB. |
| **§ 369** | Kaufmännisches Zurückbehaltungsrecht – weiter als § 273 BGB, mit Verwertungsbefugnis. | Verstärktes Druckmittel. |
| **§§ 377/378** | Untersuchungs- und Rügepflicht beim beidseitigen Handelskauf. | Anders BGB-Kauf: keine Rügeobliegenheit zwischen Privaten. |

### 3. Kaufmännisches Bestätigungsschreiben (Gewohnheitsrecht / §§ 362, 363 HGB)

Voraussetzungen (Hopt, Baumbach/Hopt HGB, Einl. § 343 Rn. 25 ff.):

1. Vorausgegangene Vertragsverhandlung
2. Beide Parteien sind Kaufleute (oder kaufmannsähnlich, st. Rspr. `[unverifiziert]`)
3. Schreiben wird unverzüglich versandt
4. Schreiben bestätigt das Verhandlungsergebnis (Abweichungen nur in geringfügigem Maße)
5. **Schweigen** des Empfängers gilt als Zustimmung – Verschweigen führt zur Bindung mit dem Inhalt des Schreibens

Sonderfall doppelte Bestätigung: bei sich widersprechenden Schreiben gilt das erste – str., Belegstelle: K. Schmidt, MüKoHGB, Einl. § 343 Rn. … `[unverifiziert]`.

### 4. § 377 HGB – Untersuchungs- und Rügepflicht beim Handelskauf

**Kernpflicht für jeden B2B-Praktiker.** Versäumung führt zum Verlust sämtlicher Gewährleistungsrechte (Nacherfüllung, Rücktritt, Minderung, Schadensersatz statt der Leistung – nicht jedoch Schadensersatz aus Garantie oder Delikt).

#### Voraussetzungen

- **Beidseitiges Handelsgeschäft** (§ 343 HGB für beide Seiten)
- **Handelskauf** – einschließlich Werklieferungsvertrag, str. ob Werkvertrag (h.M. nicht direkt, aber Tendenz zur analogen Anwendung, Hopt aaO `[unverifiziert]`)
- Ablieferung der Ware

#### Rechtsfolgen / Ablauf

| Mangelkategorie | Pflicht | Frist |
|---|---|---|
| **offener Mangel** | unverzügliche Untersuchung + Rüge (§ 377 Abs. 1 HGB) | "unverzüglich" iSv § 121 BGB – ohne schuldhaftes Zögern; Auslegung je nach Warenart |
| **verdeckter Mangel** | Rüge unverzüglich nach **Entdeckung** (§ 377 Abs. 3 HGB) | "unverzüglich" nach tatsächlicher Entdeckung |
| **Aliud / Mengenabweichung** | gleichgestellt (§ 378 HGB), sofern Abweichung nicht so offensichtlich, dass Verkäufer mit Genehmigung nicht rechnen konnte | wie oben |

**Form der Rüge:** formfrei, aber **Inhaltspflicht**: Mangel ist nach Art und Umfang **konkret** zu bezeichnen – Pauschalrügen ("Ware nicht in Ordnung") genügen nicht (BGH `[unverifiziert – prüfen in juris]`; Hopt aaO § 377 Rn. 51).

**Beweislast:** Käufer muss rechtzeitige und ordnungsgemäße Rüge beweisen – daher Empfehlung: Textform mit Zustellnachweis (E-Mail mit Lesebestätigung; Einschreiben; Zustellung per Boten).

**Faustregel "Unverzüglichkeit" (st. Rspr. `[unverifiziert]`):** je nach Warenart 1–3 Werktage für Untersuchung, weitere 1–2 Werktage für Rüge. Bei verderblicher Ware kürzer, bei Investitionsgütern mit Inbetriebnahmeprüfung länger. Im Einzelfall stets unter Berücksichtigung von Betriebsgröße und Üblichkeit.

**Ausnahmen** vom Rechtsverlust:

- Arglist des Verkäufers (§ 377 Abs. 5 HGB) – dann bleiben Gewährleistungsrechte trotz Versäumung.
- Garantieübernahme – Garantieansprüche bleiben unabhängig erhalten.
- Deliktsansprüche (§§ 823 ff. BGB) – unabhängig von § 377 HGB.

### 5. Praxischeck-Schema im konkreten Fall

```
1. Sind beide Parteien Kaufmann (§§ 1 ff. HGB)?
   ja → weiter; nein → BGB ist Maß
2. Welche HGB-Norm könnte greifen?
   – §§ 350, 352, 354a: vertragsgestaltend
   – §§ 362, 363: Bestätigungsschreiben/Schweigen
   – § 366: Gutgläubiger Erwerb
   – §§ 377/378: Rügepflicht
3. Tatbestandsvoraussetzungen prüfen, Rechtsfolge benennen
4. Folge für Mandant: Was ändert sich gegenüber BGB?
```

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 343 HGB](https://www.gesetze-im-internet.de/hgb/__343.html) (Handelsgeschäft)
- [§ 344 HGB](https://www.gesetze-im-internet.de/hgb/__344.html) (Vermutung)
- [§ 346 HGB](https://www.gesetze-im-internet.de/hgb/__346.html) (Handelsbrauch)
- [§ 347 HGB](https://www.gesetze-im-internet.de/hgb/__347.html) (kaufmännische Sorgfalt)
- [§ 348 HGB](https://www.gesetze-im-internet.de/hgb/__348.html) (Vertragsstrafe)
- [§ 349 HGB](https://www.gesetze-im-internet.de/hgb/__349.html) (Bürgschaft)
- [§ 350 HGB](https://www.gesetze-im-internet.de/hgb/__350.html) (Formfreiheit)
- [§ 352 HGB](https://www.gesetze-im-internet.de/hgb/__352.html) (Zinsen 5 %)
- [§ 354a HGB](https://www.gesetze-im-internet.de/hgb/__354a.html) (Abtretungsausschluss)
- [§ 362 HGB](https://www.gesetze-im-internet.de/hgb/__362.html), [§ 363 HGB](https://www.gesetze-im-internet.de/hgb/__363.html) (Schweigen)
- [§ 366 HGB](https://www.gesetze-im-internet.de/hgb/__366.html) (gutgläubiger Erwerb)
- [§ 369 HGB](https://www.gesetze-im-internet.de/hgb/__369.html) (Zurückbehaltungsrecht)
- [§ 377 HGB](https://www.gesetze-im-internet.de/hgb/__377.html), [§ 378 HGB](https://www.gesetze-im-internet.de/hgb/__378.html) (Untersuchungs-/Rügepflicht)
- [§ 121 BGB](https://www.gesetze-im-internet.de/bgb/__121.html) (unverzüglich)

### Kommentare

- Hopt, in: Baumbach/Hopt HGB, 42. Aufl. 2023, § 377 Rn. 1 ff., Einl. § 343 Rn. 25 ff. (kaufmännisches Bestätigungsschreiben)
- K. Schmidt, in: MüKoHGB, 5. Aufl. 2021, § 377 Rn. 1 ff.
- Grunewald, in: MüKoHGB, 5. Aufl. 2021, §§ 362, 363 Rn. 1 ff.
- Achilles, in: EBJS HGB, 4. Aufl. 2020, § 377 Rn. 1 ff.
- Brüggemann, in: Staub HGB, 6. Aufl. 2023, § 377 Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris]`)

1. BGH, Urt. v. 03.11.1982 – VIII ZR 282/81, NJW 1983, 217 (Konkretheit der Rüge)
2. BGH, Urt. v. 30.01.1985 – VIII ZR 238/83 (Unverzüglichkeit, Faustfrist)
3. BGH, Urt. v. 25.10.2007 – VII ZR 27/06 (Werkvertrag und § 377 HGB analog)
4. BGH, Urt. v. 19.06.2002 – VIII ZR 159/01 (kaufmännisches Bestätigungsschreiben)

## Ausgabeformat

```
MEMO — HGB oder BGB? Besonderheiten des Handelsgeschäfts
Mandant: <anonymisiert>

I. Sachverhalt (knapp)
II. Frage(n)
III. Kurzantwort (Ein-Satz-Befund)
IV. Rechtliche Bewertung
    1. Kaufmannseigenschaft beider Parteien (§§ 1 ff. HGB)
    2. Handelsgeschäft (§ 343, § 344 HGB)
    3. Einschlägige HGB-Sonderregel(n)
       (§§ 346/347/350/352/354a/362/366/369/377/378 — je nach Fall)
    4. Abweichung vom BGB / Folge für den Mandanten
V. Gesamtergebnis
VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>
    – insb. § 377 HGB Rügefrist, Beweislast Rüge
VII. Quellenverzeichnis

(Optional VIII. Entwurf Rügeschreiben § 377 HGB)
```

## Beispiel (Auszug Gutachtenstil, § 377 HGB)

> "Die Mandantin (Kaufmann iSv § 1 HGB) hat von der Zulieferin (ebenfalls Kaufmann) am 02.04. eine Charge Wälzlager bezogen. Es handelt sich um ein beidseitiges Handelsgeschäft (§ 343 HGB i.V.m. § 344 HGB Vermutung). Damit greift § 377 HGB. Die Wälzlager wurden am Liefertag in den Wareneingang gestellt; bei branchenüblicher Stichprobenprüfung (Hopt, Baumbach/Hopt HGB, § 377 Rn. 36) wäre der Längstmangel der Mantelfläche binnen 2 Werktagen erkennbar gewesen. Die Mandantin hat erst am 03.05. – mithin nach rund 4 Wochen – gerügt. Eine Rüge ist nicht unverzüglich iSv § 121 BGB. Folge: Die Ware gilt als genehmigt (§ 377 Abs. 2 HGB); Nacherfüllungs-, Rücktritts-, Minderungs- und Schadensersatzansprüche aus Gewährleistung sind ausgeschlossen. Vorbehalten bleiben Ansprüche aus Garantie und § 823 BGB. Risiko 🔴. Empfehlung: Prüfung, ob Arglist (§ 377 Abs. 5 HGB) oder Garantieabrede vorliegt; ggf. Deliktsklage prüfen."

## Risiken / typische Fehler

- **§ 377 HGB beim Werkvertrag pauschal verneinen.** Bei Werklieferungsvertrag direkt, bei reinem Werkvertrag str./analog – nicht reflexartig ablehnen.
- **Pauschale Rüge** ("Ware nicht in Ordnung") – inhaltlich unzureichend, gilt als nicht gerügt.
- **Rüge an falsche Adresse / per einfacher Mail ohne Nachweis** – Beweislast Käufer.
- **Bestätigungsschreiben ignorieren** – wer schweigt, ist gebunden, auch wenn der Inhalt vom Verhandlungsergebnis abweicht (Grenze: geringfügige Abweichung; Treu und Glauben).
- **§ 354a HGB übersehen:** Im B2B-Geschäft sind Abtretungsverbote für Geldforderungen nicht durchsetzbar – das schwächt z. B. Sicherungsabreden.
- **§ 350 HGB falsch angewendet:** Formfreiheit gilt nur für die in §§ 766, 780, 781 BGB genannten Erklärungen und nur bei beidseitigem Handelsgeschäft, **nicht** für gesetzliche Schriftform aus anderen Gründen (z. B. § 311b BGB).

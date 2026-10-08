---
name: lizenzvertrag-urhg-borghei
title: /urheber-medienrecht:lizenzvertrag-urhg
description: Entwurf und Review eines urheberrechtlichen Lizenzvertrags mit präziser Nutzungsrechtseinräumung nach §§ 31–37 UrhG, Zweckübertragungsregel § 31 V UrhG und Angemessenheits-Check nach §§ 32, 32a, 32d UrhG (Bestseller-Klausel, Auskunftspflicht). Use when ein Lizenzvertrag — insb. Total-/Buy-Out-, Filmproduktions- oder Verlagsvertrag — gestaltet oder eine vorgelegte Klausel auf angemessene Vergütung und AGB-Wirksamkeit geprüft werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/urheber-medienrecht/skills/lizenzvertrag-urhg
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: ip
language: de
---

# /urheber-medienrecht:lizenzvertrag-urhg

## Zweck

Der Skill prüft und entwirft Urheberrechtslizenzverträge mit Schwerpunkt auf präziser Nutzungsrechtseinräumung (§§ 31–37 UrhG), Zweckübertragungslehre (§ 31 V UrhG) und angemessener Vergütung (§§ 32, 32a, 32d UrhG). Er deckt Total-Buy-Out-, Verlags- und Filmproduktionsverträge, AGB-Kontrolle bei Standardklauseln, Rückrufrechte (§§ 40, 41, 42 UrhG) sowie die UrhDaG-Schnittstelle bei Online-Plattformlizenzen.

## Eingaben

- Art des Vertrags (Lizenzvertrag, Verlagsvertrag, Filmproduktionsvertrag, Total-Buy-Out, GbR-Beitritt)
- Vertragsparteien (Urheber/Rechtsinhaber – Verwerter)
- Werk(e), ggf. künftige Werke (§ 40 UrhG)
- Vorgesehene Nutzungsrechte (einfach/ausschließlich; räumlich/zeitlich/inhaltlich)
- Vergütungsmodell (Einmalpauschale / Stücklizenz / Umsatzbeteiligung / Hybrid)
- Vertragsstil: Erstentwurf oder Review eines vorgelegten Drittentwurfs
- Bei Filmproduktion: § 89 UrhG-Vermutung Filmhersteller einbeziehen
- Bei Verlag: VerlG-Pflichten

## Sub-Agent-Architektur

Researcher liefert §§ 31–43 UrhG, §§ 88–94 UrhG (Filmrecht), VerlG sowie BGH I. ZS-Rspr. zu Zweckübertragung („Talking to Addison", „Das Boot II") und angemessener Vergütung („GVR Tageszeitungen"). Drafter erstellt den Vertragsentwurf bzw. die Klausel-Anmerkungen mit AGB-Kontrolle. Reviewer prüft Zweckübertragung, § 32-Angemessenheit, § 32a-Bestseller-Klausel und § 32d-Auskunftspflicht — alle drei zwingend.

## Ablauf

### 1. Verfügungsbefugnis und Aktivlegitimation

- Originärer Urheber § 7 UrhG — Verfügungsbefugnis besteht.
- Miturheber § 8 UrhG — gemeinsame Verfügung, jeder kann Unterlassung allein.
- Arbeits-/Dienstverhältnis § 43 UrhG — Stillschweigende Einräumung der für den Betriebszweck erforderlichen Rechte (Auslegungsregel; Restzweifel zugunsten Urheber).
- Bei Auftragswerken: ausdrücklich vereinbarter Übertragungsumfang ist maßgeblich.

### 2. Nutzungsrechtseinräumung §§ 31–37 UrhG

- **Einfaches Nutzungsrecht** § 31 I UrhG (Mitnutzung anderer Lizenznehmer und Urheber).
- **Ausschließliches Nutzungsrecht** § 31 III UrhG (Drittausschluss, ggf. Drittausschluss auch gegenüber Urheber selbst, soweit vertraglich).
- **Räumliche, zeitliche, inhaltliche Beschränkung** § 31 I 2 UrhG zulässig.
- **Untervergaberecht** § 35 UrhG (nur mit Zustimmung des Urhebers).
- **Rechte an unbekannten Nutzungsarten** § 31a UrhG (Schriftform, Widerrufsrecht binnen 3 Monaten ab Mitteilung).
- **§ 32c UrhG**: bei späterer Aufnahme einer im Vertragsschluss unbekannten Nutzungsart gesonderter Vergütungsanspruch.

### 3. Zweckübertragungsregel § 31 V UrhG

**Auslegungsregel zugunsten des Urhebers**: Im Zweifel werden nur die Nutzungsrechte eingeräumt, die der Vertragszweck erfordert. Pauschale Klauseln („sämtliche Rechte umfassend") sind im Lichte des Vertragszwecks restriktiv auszulegen (BGH „Talking to Addison", Urt. v. 07.10.2009 – I ZR 38/07, BGHZ 182, 337, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2009-10-07&Aktenzeichen=I%20ZR%2038/07) – die Entscheidung wendet die Zweckübertragungslehre im Rahmen des § 32 UrhG an).

Konsequenz für die Vertragsgestaltung: Nutzungsarten **enumerativ** auflisten, nicht generisch.

### 4. Angemessene Vergütung §§ 32, 32a, 32d UrhG

- **§ 32 UrhG**: Anspruch auf **angemessene** Vergütung. Maßstab: Branchenüblichkeit, individuelle Verhandlung, ggf. gemeinsame Vergütungsregeln (§ 36 UrhG, z. B. „GVR Tageszeitungen II", BGH, Urt. v. 21.05.2015 – I ZR 39/14, GRUR 2016, 67, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2015-05-21&Aktenzeichen=I%20ZR%2039/14)). Verzicht im Voraus unwirksam (§ 32 III 1 UrhG). Klage auf Anpassung zulässig.
- **§ 32a UrhG (Bestseller-Vergütung / „Fairnessparagraph")**: Bei auffälligem Missverhältnis zwischen vereinbarter Gegenleistung und Erträgen aus der Werknutzung Anpassungsanspruch auch ohne Vorhersehbarkeit. **Zwingendes Recht**, Verzicht unwirksam (§ 32a III UrhG). Maßstab idR „auffälliges Missverhältnis" ab dem 2-fachen der angemessenen Vergütung (BGH „Das Boot II", Urt. v. 20.02.2020 – I ZR 176/18, GRUR 2020, 611, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2020-02-20&Aktenzeichen=I%20ZR%20176/18)).
- **§ 32d UrhG (Auskunftspflicht)**: Urheber hat jährlich Anspruch auf Auskunft über Umfang der Werknutzung und daraus erzielte Erträge — auch ggü. Sublizenznehmern (§ 32e UrhG). Ausnahmen § 32d II.

### 5. AGB-Kontrolle bei Total-Buy-Out

Pauschale Buy-Out-Klauseln (Einmalpauschale für alle Nutzungsrechte zeitlich/räumlich/inhaltlich unbeschränkt) sind nach §§ 305 ff. BGB zu prüfen:

- § 307 BGB iVm dem Leitbild des § 32 UrhG: unangemessene Benachteiligung bei evident niedriger Pauschale.
- § 31 V UrhG bleibt Auslegungsregel auch in AGB.
- Folge bei Unwirksamkeit: § 306 BGB — Vertrag bleibt im Übrigen wirksam, Ergänzung durch Angemessenheitsregel.

### 6. Verträge über künftige Werke § 40 UrhG

- Schriftform (§ 40 I 1 UrhG).
- **5-Jahres-Kündigungsrecht** beider Parteien (§ 40 I 2 UrhG) — zwingend.
- Bei nicht näher bestimmten künftigen Werken: ggf. Sittenwidrigkeit § 138 BGB bei Knebelung.

### 7. Rückrufrechte §§ 41, 42 UrhG

- **§ 41 UrhG** (Nichtausübung): Urheber kann ausschließliches Nutzungsrecht zurückrufen, wenn der Verwerter es nicht oder nur unzureichend ausübt. Frühestens 2 Jahre nach Einräumung (bzw. 1 Jahr bei Zeitungsbeiträgen). Nachfristsetzung erforderlich.
- **§ 42 UrhG** (gewandelte Überzeugung): Rückruf bei nachhaltig gewandelter persönlicher Überzeugung; Entschädigungspflicht des Urhebers.

### 8. Filmrecht §§ 88 ff. UrhG

- **§ 88 UrhG**: Auslegungsregel, dass mit Vertragsschluss zur Filmherstellung dem Filmhersteller alle Verfilmungsrechte eingeräumt werden.
- **§ 89 UrhG**: Vermutung zugunsten des Filmherstellers an den ausschließlichen Nutzungsrechten.
- **§ 90 UrhG**: Einschränkung von §§ 41, 42 UrhG bei Filmwerken (kein Rückruf wegen Nichtausübung an Filmen; § 90 II UrhG-Sperre).
- **§ 92 UrhG**: ausübende Künstler im Film.
- **§ 94 UrhG**: eigenständiges verwandtes Schutzrecht des Filmherstellers.

### 9. Verlagsrecht VerlG

- Verleger hat Verlagspflicht (§ 1 VerlG): Vervielfältigen und Verbreiten.
- Honoraranspruch § 22 VerlG.
- Rückrufrecht bei Nichtausübung § 32 VerlG.

### 10. UrhDaG-Schnittstelle bei Plattformnutzung

Wenn die Lizenz die öffentliche Wiedergabe auf großen Diensteanbietern iSv § 2 UrhDaG erfasst, sind die Pflichten gemäß §§ 1–10 UrhDaG zu berücksichtigen (Plattform schuldet selbst die öffentliche Wiedergabe, Erwerb von Lizenzen, Beschwerdemechanismus § 14 UrhDaG).

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 31 UrhG](https://www.gesetze-im-internet.de/urhg/__31.html) (Einräumung von Nutzungsrechten)
- [§ 31a UrhG](https://www.gesetze-im-internet.de/urhg/__31a.html) (unbekannte Nutzungsarten)
- [§ 32 UrhG](https://www.gesetze-im-internet.de/urhg/__32.html) (angemessene Vergütung)
- [§ 32a UrhG](https://www.gesetze-im-internet.de/urhg/__32a.html) (Bestseller-Vergütung)
- [§ 32c UrhG](https://www.gesetze-im-internet.de/urhg/__32c.html) (Vergütung für später bekannte Nutzungsart)
- [§ 32d UrhG](https://www.gesetze-im-internet.de/urhg/__32d.html) (Auskunftspflicht)
- [§ 32e UrhG](https://www.gesetze-im-internet.de/urhg/__32e.html) (Auskunft gegen Dritte)
- [§ 36 UrhG](https://www.gesetze-im-internet.de/urhg/__36.html) (gemeinsame Vergütungsregeln)
- [§ 40 UrhG](https://www.gesetze-im-internet.de/urhg/__40.html) (Verträge über künftige Werke)
- [§ 41 UrhG](https://www.gesetze-im-internet.de/urhg/__41.html) (Rückrufrecht Nichtausübung)
- [§ 42 UrhG](https://www.gesetze-im-internet.de/urhg/__42.html) (Rückrufrecht gewandelte Überzeugung)
- [§ 43 UrhG](https://www.gesetze-im-internet.de/urhg/__43.html) (Arbeits-/Dienstverhältnisse)
- [§§ 88–94 UrhG](https://www.gesetze-im-internet.de/urhg/) (Filmrecht)
- [VerlG](https://www.gesetze-im-internet.de/verlg/) (Verlagsgesetz)
- [VGG](https://www.gesetze-im-internet.de/vgg/) (Verwertungsgesellschaftengesetz)
- [§§ 305–310 BGB](https://www.gesetze-im-internet.de/bgb/__305.html) (AGB-Kontrolle)
- [Art. 18 ff. DSM-RL (EU) 2019/790](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790) (angemessene und verhältnismäßige Vergütung)

### Kommentare

- Schulze, in: Dreier/Schulze, UrhG, 7. Aufl. 2022, § 31 Rn. 1 ff., § 32 Rn. 1 ff. `[unverifiziert]`
- Wandtke/Grunert, in: Wandtke/Bullinger, Praxiskommentar Urheberrecht, 6. Aufl. 2022, vor §§ 31 ff. UrhG `[unverifiziert]`
- Schricker, in: Schricker/Loewenheim, Urheberrecht, 6. Aufl. 2020, vor §§ 31 ff. UrhG `[unverifiziert]`
- BeckOK UrhG/Soppe, Stand 2024, § 31 Rn. 1 ff., § 32 Rn. 1 ff.

### Rechtsprechung

1. BGH, Urt. v. 22.09.2011 – I ZR 127/10, GRUR 2012, 496 – „Das Boot" (§ 32a UrhG, Anspruch des Miturhebers), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2011-09-22&Aktenzeichen=I%20ZR%20127/10)
2. BGH, Urt. v. 20.02.2020 – I ZR 176/18, GRUR 2020, 611 – „Das Boot II" (auffälliges Missverhältnis, § 32a UrhG), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2020-02-20&Aktenzeichen=I%20ZR%20176/18)
3. BGH, Urt. v. 21.05.2015 – I ZR 39/14, GRUR 2016, 67 – „GVR Tageszeitungen II" (gemeinsame Vergütungsregeln), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2015-05-21&Aktenzeichen=I%20ZR%2039/14)
4. BGH, Urt. v. 31.05.2012 – I ZR 73/10, BGHZ 193, 268 = GRUR 2012, 1031 – „Honorarbedingungen Freie Journalisten", [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2012-05-31&Aktenzeichen=I%20ZR%2073/10)
5. BGH, Urt. v. 17.10.2013 – I ZR 41/12, GRUR 2014, 556 – „Rechteeinräumung Synchronsprecher" (§§ 88, 89, 92 UrhG als Auslegungsregeln, kein AGB-Maßstab), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2013-10-17&Aktenzeichen=I%20ZR%2041/12)
6. BGH, Urt. v. 07.10.2009 – I ZR 38/07, BGHZ 182, 337 = GRUR 2009, 1148 – „Talking to Addison" (§ 32 UrhG, Übersetzervergütung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2009-10-07&Aktenzeichen=I%20ZR%2038/07)
7. BGH, Urt. v. 20.01.2011 – I ZR 19/09, GRUR 2011, 328 – „Destructive Emotions" (§ 32 UrhG, Übersetzervergütung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2011-01-20&Aktenzeichen=I%20ZR%2019/09)
8. BGH, Urt. v. 10.05.2012 – I ZR 145/11 – „Fluch der Karibik" (Nachvergütung ausführender Künstler), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2012-05-10&Aktenzeichen=I%20ZR%20145/11)
9. EuGH zur Vergütungsangemessenheit unter Art. 18 DSM-RL — Spruchpraxis im Aufbau `[unverifiziert]`

## Ausgabeformat

```
GUTACHTEN / VERTRAGSENTWURF — Lizenzvertrag UrhG
Werk(e): <…>     Parteien: <Urheber> – <Verwerter>

I. Sachverhalt / Vertragszweck
II. Frage(n)
III. Kurzantwort
     – Angemessene Vergütung: [ja / nachzubessern]
     – Zweckübertragungs-Lücken: [keine / Liste]

IV. Rechtliche Bewertung
    1. Verfügungsbefugnis
    2. Nutzungsrechte (einfach/ausschl., räumlich/zeitlich/inhaltlich)
    3. Zweckübertragung § 31 V UrhG
    4. Vergütung §§ 32, 32a, 32d UrhG
    5. AGB-Kontrolle (bei Buy-Out)
    6. ggf. § 40 UrhG (künftige Werke), §§ 41, 42 (Rückruf)
    7. ggf. §§ 88 ff. UrhG (Film) bzw. VerlG (Verlag)
    8. ggf. UrhDaG-Schnittstelle

V. Vertragstext (Entwurf)
   § 1 Definitionen
   § 2 Werk
   § 3 Nutzungsrechtseinräumung
        (3.1) Art (einfach / ausschließlich)
        (3.2) Räumlicher Geltungsbereich
        (3.3) Zeitlicher Geltungsbereich
        (3.4) Inhaltliche Nutzungsarten (enumerativ!)
        (3.5) Untervergaberecht § 35 UrhG
        (3.6) Unbekannte Nutzungsarten § 31a UrhG (Schriftform, Widerruf)
   § 4 Vergütung
        (4.1) Höhe / Berechnung
        (4.2) Fälligkeit
        (4.3) Bestseller-Klausel § 32a UrhG (deklaratorisch)
        (4.4) Auskunftspflicht § 32d UrhG
   § 5 Urhebernennung § 13 UrhG
   § 6 Gewährleistung / Freistellung
   § 7 Vertragsdauer / Kündigung
   § 8 Rückruf §§ 41, 42 UrhG
   § 9 Schlussbestimmungen

VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VII. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Total-Buy-Out ohne Angemessenheitsprüfung** § 32 UrhG → Anpassungsanspruch des Urhebers, ggf. AGB-Unwirksamkeit § 307 BGB.
- **Zweckübertragungs-Falle**: Generische „alle Rechte"-Klauseln werden im Streit restriktiv ausgelegt — Verwerter verliert Rechte, die er für vereinbart hielt.
- **§ 32a-Klausel als Verzicht** ausgestaltet — unwirksam, da zwingendes Recht (§ 32a III UrhG).
- **§ 32d-Auskunftspflicht** ignoriert oder vertraglich ausgeschlossen — Verzicht unwirksam.
- **§ 40 UrhG-5-Jahres-Frist** bei „Werk-Pool"-Verträgen mit Künstlern übersehen.
- **§ 31a UrhG-Schriftform und Widerruf** bei unbekannten Nutzungsarten nicht beachtet.
- **§ 43 UrhG-Arbeitsverhältnis**: stillschweigende Rechtseinräumung überschätzt — nur betriebszweckbezogen.
- **Bei Filmwerken**: § 90 UrhG-Sperre der Rückrufrechte übersehen.
- **Bei Plattformlizenzen**: UrhDaG-Pflichten nicht reflektiert (Plattform schuldet selbst, nicht nur der Nutzer).

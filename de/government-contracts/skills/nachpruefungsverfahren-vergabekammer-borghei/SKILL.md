---
name: nachpruefungsverfahren-vergabekammer-borghei
title: /vergaberecht:nachpruefungsverfahren-vergabekammer
description: 'Nachprüfungsverfahren vor der Vergabekammer §§ 155 ff. GWB – Antragsbefugnis § 160 Abs. 2 GWB (Interesse, Rechtsverletzung, Schadensgefahr), Rügeobliegenheit § 160 Abs. 3 GWB (10-Kalendertage-Frist), Suspensiveffekt § 169 GWB, Entscheidung § 168 GWB, Kostenfolgen § 182 GWB. Use when ein Bieter wegen drohender oder erfolgter Rechtsverletzung im Vergabeverfahren Eilrechtsschutz vor der zuständigen Vergabekammer (Bund: BKartA, Land: VK des jeweiligen Landes) sucht.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vergaberecht/skills/nachpruefungsverfahren-vergabekammer
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: government-contracts
language: de
---

# /vergaberecht:nachpruefungsverfahren-vergabekammer

## Zweck

Das Nachprüfungsverfahren ist der zentrale Primärrechtsschutz im Oberschwellenbereich. Es wird durch Antrag vor der Vergabekammer eingeleitet (§ 160 GWB), löst einen automatischen Zuschlagsverbots-Suspensiveffekt aus (§ 169 GWB) und führt zur Entscheidung durch Beschluss innerhalb von fünf Wochen (§ 167 GWB). Dieser Skill prüft Antragsbefugnis, Rügeobliegenheit, Fristen und entwirft den Nachprüfungsantrag.

## Eingaben

- Bezeichnung des Vergabeverfahrens (Auftraggeber, Bekanntmachungs-/Vergabe-Nr., Verfahrensart, Vergabegegenstand, geschätzter Wert)
- Stellung des Mandanten (Bieter / Bewerber / Interessent)
- Konkrete vermutete Rechtsverletzung (Ausschluss, Eignung, Zuschlag, intransparente Wertung, diskriminierende Anforderung, Lossplitting, falsche Verfahrensart)
- Zeitpunkt der Kenntnis vom Verstoß (Datum + Anlass; Bekanntmachung, Vergabeunterlagen, § 134-Information, Verfahrenshandlung)
- Bereits ausgesprochene Rüge an Auftraggeber (Datum, Inhalt) und Reaktion
- Status des Zuschlags (Stillhaltefrist § 134 Abs. 2 GWB läuft? bereits erteilt?)

## Sub-Agent-Architektur

Researcher liefert die Normen §§ 155–184 GWB, einschlägige OLG-Vergabesenate-Entscheidungen und BGH-Vergabesenat-Rspr. zur Antragsbefugnis sowie zur Rügeobliegenheit. Drafter entwirft den Nachprüfungsantrag mit klarer Zulässigkeits-/Begründetheitsgliederung. Reviewer prüft Frist-Kalender (Rüge, Stillhalte, Beschwerde), Antragsbefugnis und Anhängigkeit/Zuständigkeit.

## Ablauf

### 1. Zulässigkeit prüfen

#### 1.1 Anwendbarkeit § 155 GWB / Oberschwellenbereich

Vergabe oberhalb der EU-Schwellen (vgl. Skill `vergabe-eu-schwellenwert-pruefung`). Unterhalb der Schwelle kein Nachprüfungsverfahren — Rechtsschutz nur über Zivilrechtsweg (§§ 280, 311 Abs. 2 BGB) und Verwaltungsrechtsweg.

#### 1.2 Zuständige Vergabekammer § 159 GWB

- **VK des Bundes** beim BKartA: Bundesauftraggeber
- **VK des Landes**: Auftraggeber der Länder, Kommunen, Anstalten in Landeshoheit
- Bei mehreren beteiligten Auftraggebern: § 159 Abs. 3 GWB

#### 1.3 Antragsbefugnis § 160 Abs. 2 GWB

Drei kumulative Voraussetzungen:

| Voraussetzung | Maßstab |
|---|---|
| Interesse am Auftrag | Substanziiertes Interesse, nicht nur generelles Tätigkeitsfeld; Angebot oder belegbare Angebotsabsicht |
| Geltend gemachte Rechtsverletzung | Subjektiv-rechtlich geschützte vergaberechtliche Vorschrift, nicht nur objektive Rechtmäßigkeit |
| Schadensgefahr | Drohender oder eingetretener Wettbewerbsnachteil; Chance auf Zuschlag |

EuGH zur "interest to obtain the contract" und Schadenswahrscheinlichkeit: EuGH, Urt. v. 05.04.2016 – Rs. C-689/13, PFE (https://curia.europa.eu/juris/liste.jsf?language=en&num=C-689/13); BGH, Beschl. v. 18.02.2003 – X ZB 43/02, NZBau 2003, 293 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=18.02.2003&Aktenzeichen=X+ZB+43/02).

#### 1.4 Rügeobliegenheit § 160 Abs. 3 GWB

Vier Fallgruppen mit unterschiedlichen Anknüpfungspunkten:

| Nr. | Anknüpfung | Frist |
|---|---|---|
| § 160 Abs. 3 S. 1 Nr. 1 GWB | Positive Kenntnis des Verstoßes (subjektiv) | **10 Kalendertage** ab Kenntnis |
| § 160 Abs. 3 S. 1 Nr. 2 GWB | Aus Bekanntmachung erkennbar (objektiv) | bis Ablauf Angebots-/Teilnahmefrist |
| § 160 Abs. 3 S. 1 Nr. 3 GWB | Aus Vergabeunterlagen erkennbar (objektiv) | bis Ablauf Angebots-/Teilnahmefrist |
| § 160 Abs. 3 S. 1 Nr. 4 GWB | Mitteilung des AG, der Rüge nicht abzuhelfen | **15 Kalendertage** ab Mitteilung |

Maßstab "erkennbar" nicht einheitlich — vgl. OLG-Vergabesenate uneinheitlich, vgl. OLG Düsseldorf, Beschl. v. 22.01.2014 – Verg 26/13 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=OLG+D%C3%BCsseldorf&Datum=22.01.2014&Aktenzeichen=Verg+26/13). Konservativ: Erkennbarkeit für **fachkundigen** Bieter ohne juristische Spezialprüfung.

#### 1.5 Stillhaltefrist § 134 Abs. 2 GWB

Nach Information unterlegener Bieter darf der Zuschlag nicht vor Ablauf von **15 Kalendertagen** (bzw. **10 Kalendertagen** bei elektronischer Versendung) erteilt werden. Eingang eines zulässigen Nachprüfungsantrags binnen dieser Frist löst Zuschlagsverbot § 169 Abs. 1 GWB aus.

### 2. Begründetheit prüfen

Subsumtion der gerügten Vergaberechtsverletzung unter die einschlägige Norm:

- Eignungsmängel §§ 122–124 GWB (Ausschluss zu Recht?)
- Wertungsfehler § 127 GWB (transparent, nichtdiskriminierend, vorab bekannt gegebene Zuschlagskriterien)
- Verfahrenswahl §§ 14 ff. VgV
- Leistungsbeschreibung § 31 VgV (produktneutral, eindeutig)
- Information § 134 GWB (15 KT / 10 KT bei elektronisch)

Kausalität: § 168 Abs. 1 S. 2 GWB — die Vergabekammer ordnet **nur** an, was zur Beseitigung der Rechtsverletzung erforderlich ist (keine antragsgebundene Beschränkung im Sinne des Verwaltungsprozessrechts, aber Verhältnismäßigkeit).

### 3. Anträge formulieren

Typische Anträge:

1. Feststellung, dass die Antragstellerin durch die Maßnahme (z. B. Ausschluss) in ihren Rechten verletzt ist.
2. Aufhebung des Verfahrens bzw. Versetzung in den Stand vor der gerügten Maßnahme.
3. Akteneinsicht § 165 GWB.
4. Vorab-/Eilanordnung § 169 Abs. 2 GWB (Verlängerung Stillhaltefrist).
5. Kostenentscheidung § 182 GWB.

### 4. Suspensiveffekt § 169 GWB

Mit Eingang des **zulässigen** Antrags Zuschlagsverbot. Wirkung bis 2 Wochen nach Ablauf der Beschwerdefrist gegen die VK-Entscheidung (§ 173 Abs. 1 GWB) oder bis zur OLG-Beschwerdeentscheidung. **Praktisches Druckmittel** der Bieterseite — sofort Antrag stellen, falls Zuschlag droht.

### 5. Entscheidung und Kosten

VK entscheidet binnen 5 Wochen (§ 167 Abs. 1 GWB), Verlängerung durch Vorsitzenden möglich. Kostenentscheidung § 182 GWB — Gebühren von 2.500 bis 50.000 EUR nach Auftragswert und Bedeutung der Sache.

### 6. Rechtsmittel: sofortige Beschwerde § 171 GWB

- Frist: **15 Kalendertage** ab Zustellung des VK-Beschlusses (§ 172 Abs. 1 GWB)
- Zuständig: OLG-Vergabesenat
- Aufschiebende Wirkung § 173 GWB (Zuschlagsverbot fortdauernd, bis 2 Wochen nach Ablauf der Beschwerdefrist)

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 134 GWB](https://www.gesetze-im-internet.de/gwb/__134.html) (Informations- und Wartepflicht)
- [§ 155 GWB](https://www.gesetze-im-internet.de/gwb/__155.html) (Grundsatz Nachprüfungsverfahren)
- [§ 159 GWB](https://www.gesetze-im-internet.de/gwb/__159.html) (Zuständigkeit Vergabekammern)
- [§ 160 GWB](https://www.gesetze-im-internet.de/gwb/__160.html) (Antrag, Antragsbefugnis, Rüge)
- [§ 165 GWB](https://www.gesetze-im-internet.de/gwb/__165.html) (Akteneinsicht)
- [§ 167 GWB](https://www.gesetze-im-internet.de/gwb/__167.html) (Beschleunigung)
- [§ 168 GWB](https://www.gesetze-im-internet.de/gwb/__168.html) (Entscheidung der Vergabekammer)
- [§ 169 GWB](https://www.gesetze-im-internet.de/gwb/__169.html) (Aussetzung Vergabeverfahren)
- [§ 171 GWB](https://www.gesetze-im-internet.de/gwb/__171.html) (Sofortige Beschwerde)
- [§ 172 GWB](https://www.gesetze-im-internet.de/gwb/__172.html) (Frist, Form, Inhalt der Beschwerde)
- [§ 173 GWB](https://www.gesetze-im-internet.de/gwb/__173.html) (Aufschiebende Wirkung)
- [§ 182 GWB](https://www.gesetze-im-internet.de/gwb/__182.html) (Kosten)
- [Art. 1, 2 RL 89/665/EWG](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:31989L0665) (Rechtsmittelrichtlinie, geändert durch RL 2007/66/EG)

### Kommentare

- Wiese, in: Burgi, Vergaberecht, 4. Aufl. 2022, § 21 Rn. 1 ff. (Nachprüfung)
- Antweiler, in: Ziekow/Völlink, Vergaberecht, 5. Aufl. 2024, § 160 GWB Rn. 30 ff.
- Möllenkamp, in: Pünder/Schellenberg, Vergaberecht, 4. Aufl. 2022, § 169 GWB Rn. 5 ff.
- Müller-Wrede (Hrsg.), Beck'scher Vergaberechtskommentar, § 160 GWB

### Rechtsprechung (`[unverifiziert – prüfen in Beck-Online/juris/eur-lex]`)

1. EuGH, Urt. v. 05.04.2016 – Rs. C-689/13, PFE (Antragsbefugnis, Sekundäranträge)
2. BGH, Beschl. v. 18.02.2003 – X ZB 43/02, NZBau 2003, 293 (Antragsbefugnis)
3. BGH, Beschl. v. 26.09.2006 – X ZB 14/06, NZBau 2007, 50 (Rügeobliegenheit, Kenntnis)
4. OLG Düsseldorf, Beschl. v. 22.01.2014 – Verg 26/13 (Erkennbarkeit Vergabeunterlagen)
5. OLG München, Beschl. v. 10.11.2016 – Verg 11/16, NZBau 2017, 174 (Eilantrag § 169 Abs. 2 GWB)

## Ausgabeformat

```
NACHPRÜFUNGSANTRAG nach § 160 GWB
An: Vergabekammer <…>
Datum: <…>

In der Vergabesache
   Antragstellerin: <Mandant>
   Auftraggeberin / Antragsgegnerin: <…>
   Beigeladene (ggf. präsumtive Zuschlagsempfängerin): <…>
   Verfahren: <Bezeichnung, Bekanntmachungs-Nr., Vergabe-ID>

I. Anträge
   1. <Aufhebung / Zurückversetzung>
   2. Akteneinsicht § 165 GWB
   3. ggf. § 169 Abs. 2 GWB: Verlängerung Stillhaltefrist
   4. Auferlegung der Kosten gem. § 182 GWB

II. Sachverhalt
    <chronologisch — Bekanntmachung, Angebot, gerügte Maßnahme,
     § 134-Information, Rügeschreiben vom …, Reaktion AG>

III. Zulässigkeit
     1. Anwendbarkeit § 155 GWB (Oberschwellen)
     2. Zuständigkeit § 159 GWB
     3. Antragsbefugnis § 160 Abs. 2 GWB
        - Interesse am Auftrag
        - Rechtsverletzung
        - Schadensgefahr
     4. Rüge § 160 Abs. 3 GWB (Kenntnis am <…>, Rüge am <…>)
     5. Frist (Stillhaltefrist § 134 Abs. 2 GWB läuft bis <…>)

IV. Begründetheit
    1. Verletzte Norm: <z. B. § 127 GWB, § 31 VgV>
    2. Subsumtion (Gutachtenstil)
    3. Kausalität für Zuschlagschance

V. Eilantrag (falls Zuschlag droht)
   § 169 Abs. 2 GWB

VI. Anlagen
    - Bekanntmachung
    - Angebot
    - § 134-Information
    - Rügeschreiben
    - Antwort AG

[Frist-Kalender intern:
  Rüge § 160 Abs. 3 GWB:       <Kenntnis + 10 KT>
  Stillhaltefrist § 134 GWB:   <Information + 15 KT / 10 KT elektronisch>
  Beschwerde § 172 GWB:        <VK-Beschluss + 15 KT>
  VK-Entscheidung § 167 GWB:   <Eingang + 5 Wochen>
]
```

## Beispiele

### Beispiel — Ausschluss wegen vermeintlich fehlender Referenzen

> **Sachverhalt:** Antragstellerin (mittelständischer IT-Anbieter) erhielt am 03.04.JJJJ die § 134-Information, dass ihr Angebot wegen fehlender Referenzen ausgeschlossen worden sei. In den Vergabeunterlagen war als Eignungsanforderung "drei vergleichbare Referenzen mit Auftragswert ≥ 100.000 EUR aus den letzten drei Jahren" formuliert. Antragstellerin hatte fünf Referenzen vorgelegt, drei davon mit Werten zwischen 95.000 und 110.000 EUR; AG hat zwei mit 95.000 und 98.000 als "nicht vergleichbar" verworfen.
>
> **Zulässigkeit:** Antragsbefugnis (+) — substantielle Zuschlagschance. Rüge unverzüglich am 05.04.JJJJ ausgesprochen, also binnen 10 KT § 160 Abs. 3 S. 1 Nr. 1 GWB. AG hat am 09.04.JJJJ Abhilfe abgelehnt — 15-KT-Frist § 160 Abs. 3 S. 1 Nr. 4 GWB läuft bis 24.04.JJJJ. Stillhaltefrist § 134 Abs. 2 GWB (15 KT) läuft bis 18.04.JJJJ.
>
> **Begründetheit:** AG hat die Eignungsanforderung "vergleichbar" intransparent gehandhabt (§ 122 Abs. 4, § 127 Abs. 1 GWB) — bei einer im Vergabeunterlagenmaßstab nicht weiter konkretisierten Schwelle "≥ 100.000 EUR" sind Referenzen knapp darunter ohne weitere transparente Maßstäbe nicht ohne Weiteres ausschließbar. Verstoß § 122 Abs. 4 GWB i. V. m. § 127 GWB.
>
> **Empfehlung:** Nachprüfungsantrag mit Antrag auf Zurückversetzung des Verfahrens in den Stand vor der Wertungsentscheidung; Akteneinsicht § 165 GWB; Eilantrag § 169 Abs. 2 GWB, wenn AG vor 18.04.JJJJ erteilen will.
>
> **Risiko:** 🟡 — Tatsachenfrage "Vergleichbarkeit" einzelfallabhängig; OLG-Rspr. zu Eignungskriterien uneinheitlich.

## Risiken / typische Fehler

- **Rüge verspätet.** 10-Kalendertage-Frist § 160 Abs. 3 S. 1 Nr. 1 GWB ab Kenntnis. Versäumung = Präklusion = Antrag unzulässig.
- **Rüge inhaltlich unsubstanziiert** (bloße Andeutung) — muss konkrete Rechtsverletzung und Tatsachen benennen.
- **Verstoß bereits aus Bekanntmachung/Vergabeunterlagen erkennbar**, nicht spätestens bis Ablauf Angebotsfrist gerügt → Präklusion § 160 Abs. 3 S. 1 Nr. 2/3 GWB.
- **Nachprüfungsantrag nach Zuschlag** → Antrag unzulässig (§ 168 Abs. 2 S. 1 GWB), nur noch Feststellungsantrag § 168 Abs. 2 S. 2 GWB als Vorstufe für Schadensersatz § 181 GWB.
- **Versäumung Stillhaltefrist § 134 GWB beobachten**: Sobald 15-KT-Frist abläuft und Zuschlag erteilt, ist der Primärrechtsschutz erschöpft.
- **Fehlende Akteneinsicht**: Wer § 165 GWB nicht beantragt, argumentiert blind.

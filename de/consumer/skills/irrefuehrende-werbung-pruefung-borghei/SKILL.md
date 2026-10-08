---
name: irrefuehrende-werbung-pruefung-borghei
title: /wettbewerbsrecht:irrefuehrende-werbung-pruefung
description: Prüfung einer Werbeaussage auf Irreführung nach §§ 5, 5a, 5b UWG und vergleichende Werbung nach § 6 UWG – Maßstab des durchschnittlich informierten, aufmerksamen und verständigen Verbrauchers, Beispielskatalog § 5 II, Vorenthalten wesentlicher Informationen § 5a, Preisangaben-Schnittstelle PAngV, Abgleich mit Schwarzer Liste (Anhang § 3 III). Use when eine Werbeaussage präventiv geprüft oder gegen eine Werbeaussage des Wettbewerbers vorgegangen werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/wettbewerbsrecht/skills/irrefuehrende-werbung-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: consumer
language: de
---

# /wettbewerbsrecht:irrefuehrende-werbung-pruefung

## Zweck

Der Skill prüft eine konkrete Werbeaussage auf Irreführung nach §§ 5, 5a, 5b UWG und – soweit ein Mitbewerber bezeichnet ist – auf vergleichende Werbung nach § 6 UWG. Maßstab ist der durchschnittlich informierte, aufmerksame und verständige Verbraucher (UGP-RL-konform). Der Skill liefert ein Werbeaussage-Prüfraster mit Schnittstellen zur Schwarzen Liste (Anhang zu § 3 III), PAngV und HWG.

## Eingaben

- konkrete Werbeaussage (Wortlaut, Kontext, Medium: Print, Webseite, Social Media, Radio/TV)
- ggf. Gesamtwerbung (Visual, Sternchen-Hinweis, Footer-Auflösung)
- Zielgruppe (Endverbraucher, Fachkreis, gemischt)
- Branche (insb. Lebensmittel/HWG-relevant?)
- Tatsachenkern (Beleg / Studie / Quelle der beworbenen Eigenschaft)
- Position des Mandanten: Werbender oder Mitbewerber/Verband, der vorgehen will

## Sub-Agent-Architektur

Researcher liefert UWG-Statute (§§ 3, 3 III iVm Anhang, 5, 5a, 5b, 6), UGP-RL 2005/29/EG, BGH-Rspr. zur Verkehrsauffassung und Kommentarstellen. Drafter prüft die Werbeaussage in Gutachtenstil entlang des Prüfrasters und entwirft je nach Mandantenseite: präventive Werbe-Freigabe oder Abmahnentwurf nach § 13 UWG. Reviewer prüft UGP-RL-konforme Auslegung und Spürbarkeitsschwelle § 3 II.

## Ablauf

### 1. Anwendungsbereich

- **Geschäftliche Handlung** iSv § 2 I Nr. 2 UWG (jedes Verhalten zugunsten des eigenen oder fremden Unternehmens zur Förderung des Absatzes)
- B2C oder B2B? Maßstab gleich, aber Empfängerverständnis kann variieren
- Anwendungsbereich UGP-RL 2005/29/EG (B2C); Werbe-RL 2006/114/EG (B2B vergleichende Werbung)

### 2. Abgleich mit Schwarzer Liste (Anhang zu § 3 III UWG)

**Per-se-Verboten ohne Spürbarkeitsprüfung** sind die 30 Geschäftspraktiken im Anhang. Häufige Treffer:

- Nr. 1: Falsche Behauptung eines Verhaltenskodex
- Nr. 4: Falsche Behauptung der Zulassung/Genehmigung
- Nr. 7: „nur kurze Zeit verfügbar" ohne Wahrheitsgrundlage
- Nr. 11: „Bei-Bestellung-gratis" mit versteckten Kosten
- Nr. 21: „kostenlos", „gratis" trotz unvermeidlicher Kosten
- Nr. 23: Identitätsverschleierung im redaktionellen Umfeld

Bei Treffer in Anhang § 3 III: Verstoß steht fest, keine weitere Prüfung der Spürbarkeit (§ 3 II UWG). Übergang sofort zu Rechtsfolge (§ 8 UWG).

### 3. § 5 UWG — Irreführende geschäftliche Handlungen

#### a) Tatbestand § 5 I, II UWG

Eine geschäftliche Handlung ist irreführend, wenn sie **unwahre Angaben** enthält oder sonstige **zur Täuschung geeignete** Angaben über einen der in § 5 II UWG genannten Umstände trifft. Beispielskatalog § 5 II UWG:

1. wesentliche Merkmale der Ware/Dienstleistung
2. Anlass des Verkaufs (Räumungsverkauf, „nur heute")
3. Preis oder Berechnungsart
4. persönliche Merkmale des Unternehmers (Befähigungen, Auszeichnungen)
5. geistige Eigentumsrechte
6. Rechte des Verbrauchers

#### b) Maßstab der Verkehrsauffassung

UGP-RL-konform: der **durchschnittlich informierte, aufmerksame und verständige Durchschnittsverbraucher** (EuGH, **Gut Springenheide**, C-210/96 `[unverifiziert – prüfen in curia.europa.eu]`; BGH, std. Rspr. `[unverifiziert – prüfen in juris]`). Bei Werbung an besondere Verbrauchergruppen ist auf das durchschnittliche Mitglied dieser Gruppe abzustellen (§ 3 IV UWG).

#### c) Geschäftliche Relevanz / Spürbarkeit

Die irreführende Angabe muss geeignet sein, den Verbraucher zu einer **geschäftlichen Entscheidung** zu veranlassen, die er sonst nicht getroffen hätte (§ 5 I 1 UWG). Bei Schwarzer Liste entfällt diese Prüfung.

### 4. § 5a UWG — Vorenthalten wesentlicher Informationen

Unlauter handelt auch, wer dem Verbraucher eine **wesentliche Information** vorenthält, die dieser im konkreten Fall benötigt (§ 5a I UWG). § 5a III UWG enthält Pflichtinformationen für Aufforderungen zum Kauf (wesentliche Merkmale, Identität/Anschrift des Unternehmens, Gesamtpreis, Zahlungs-/Liefer-/Leistungsbedingungen, ggf. Widerrufsrecht).

### 5. § 5b UWG / PAngV — Preisangaben

§ 5b UWG verweist auf Pflichten der PAngV (Grundpreisangabe § 4 PAngV; Endpreis § 3 PAngV; eindeutige Zuordnung der Preise zu Waren). Schnittstelle zu § 3a UWG (Rechtsbruch durch PAngV-Verstoß), bedeutsam für Online-Shop-Abmahnungen.

### 6. § 6 UWG — Vergleichende Werbung

Vergleichende Werbung (jede Werbung, die unmittelbar oder mittelbar einen Mitbewerber oder seine Erzeugnisse erkennbar macht, § 6 I UWG) ist **zulässig**, wenn die kumulativen Voraussetzungen des § 6 II Nr. 1–6 UWG vorliegen:

1. Bezug auf Waren/Dienstleistungen, die denselben Bedarf decken
2. Vergleich objektiver, relevanter, nachprüfbarer, typischer Eigenschaften
3. keine Verwechslungsgefahr
4. keine Rufausnutzung/Rufbeeinträchtigung
5. keine Herabsetzung des Mitbewerbers
6. keine Nachahmungsdarstellung

Nichterfüllung **einer** Voraussetzung führt zur Unlauterkeit. Vgl. EuGH, **Pippig Augenoptik** (C-44/01) `[unverifiziert]`; **L'Oréal/Bellure** (C-487/07) `[unverifiziert]`.

### 7. Branchen-Schnittstellen

- **HWG**: Werbung für Heilmittel — § 3 HWG-Irreführungsverbot, oft strenger als § 5 UWG
- **LMIV/LFGB**: gesundheitsbezogene/nährwertbezogene Angaben (HCR-VO 1924/2006)
- **TMG/DSA**: Transparenzpflichten Online-Werbung, Pflichtkennzeichnung Influencer-Werbung

### 8. Rechtsfolgen bei Verstoß

- Unterlassungs- und Beseitigungsanspruch § 8 UWG
- Schadensersatz § 9 UWG (bei Verschulden)
- Aufwendungsersatz § 13 III UWG bei wirksamer Abmahnung
- Gewinnabschöpfung an den Bundeshaushalt § 10 UWG (durch Verbände, selten)

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute und Sekundärrecht

- [§ 3 UWG](https://www.gesetze-im-internet.de/uwg_2004/__3.html) (Generalklausel, Schwarze Liste)
- [§ 5 UWG](https://www.gesetze-im-internet.de/uwg_2004/__5.html) (Irreführung)
- [§ 5a UWG](https://www.gesetze-im-internet.de/uwg_2004/__5a.html) (Vorenthalten wesentlicher Informationen)
- [§ 5b UWG](https://www.gesetze-im-internet.de/uwg_2004/__5b.html) (Preisangaben)
- [§ 6 UWG](https://www.gesetze-im-internet.de/uwg_2004/__6.html) (vergleichende Werbung)
- [Anhang zu § 3 III UWG](https://www.gesetze-im-internet.de/uwg_2004/anhang.html) (Schwarze Liste)
- [PAngV](https://www.gesetze-im-internet.de/pangv_2022/) (Preisangabenverordnung)
- [UGP-RL 2005/29/EG](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32005L0029)
- [Werbe-RL 2006/114/EG](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32006L0114)
- [Omnibus-RL (EU) 2019/2161](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L2161)

### Kommentare

- Bornkamm, in: Köhler/Bornkamm/Feddersen, UWG, jeweils aktuell, § 5 UWG Rn. 1 ff.
- Sosnitza, in: Ohly/Sosnitza, UWG, 8. Aufl. 2023, § 5 UWG Rn. 1 ff.
- Dreyer, in: Harte-Bavendamm/Henning-Bodewig, UWG, 5. Aufl. 2021, § 5 UWG Rn. 1 ff.
- Köhler, in: Köhler/Bornkamm/Feddersen, UWG, jeweils aktuell, § 6 UWG Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris / curia.europa.eu]`)

1. EuGH, Urt. v. 16.07.1998 – Rs. C-210/96, Gut Springenheide (Verbraucherleitbild)
2. EuGH, Urt. v. 18.06.2009 – Rs. C-487/07, L'Oréal/Bellure (vergleichende Werbung)
3. BGH, Urt. v. 18.12.2014 – I ZR 129/13, GRUR 2015, 698 – Schlafzimmer komplett (Werbung mit Selbstverständlichkeiten)
4. BGH, Urt. v. 05.11.2015 – I ZR 182/14, GRUR 2016, 521 – Durchgestrichener Preis II
5. BGH, Urt. v. 31.10.2018 – I ZR 73/17, GRUR 2019, 82 – Jogginghosen

## Ausgabeformat

```
GUTACHTEN — Prüfung Werbeaussage
Mandant: <Werbender / Beanstandender>
Werbeaussage: "<Wortlaut>"
Medium: <Webseite / Print / Social>

I. Sachverhalt
II. Kurzantwort
    – Zulässigkeit: [zulässig / unlauter §§ ___ UWG]
    – Empfehlung: [Freigabe / Anpassung / Abmahnung]

III. Rechtliche Bewertung
    1. Geschäftliche Handlung § 2 I Nr. 2 UWG
    2. Abgleich Schwarze Liste (Anhang § 3 III)
    3. § 5 UWG
       a) Tatbestand (Beispielskatalog § 5 II Nr. __)
       b) Maßstab Durchschnittsverbraucher
       c) Geschäftliche Relevanz
    4. § 5a UWG (Vorenthalten wesentlicher Informationen)
    5. § 5b UWG iVm PAngV (Preisangaben)
    6. § 6 UWG (vergleichende Werbung, soweit einschlägig)
       Prüfung Nr. 1–6 § 6 II UWG
    7. Branchen-Schnittstellen (HWG / LMIV / DSA)

IV. Rechtsfolge
    – Unterlassungsanspruch § 8 UWG (ja/nein)
    – Beseitigung § 8a UWG
    – Schadensersatz § 9 UWG (Verschulden, Schadensumfang)

V. Empfohlene Werbe-Anpassung (Werbende-Perspektive) /
   Entwurf Abmahnung (Beanstandende-Perspektive)

VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VII. Quellenverzeichnis
```

## Beispiel (Auszug, Gutachtenstil)

> **3. § 5 I, II Nr. 2 UWG (Preis).** Die Werbung mit „statt 199 EUR — jetzt 99 EUR" ohne Angabe des Bezugszeitraums des durchgestrichenen Preises ist geeignet, beim durchschnittlich informierten, aufmerksamen und verständigen Verbraucher den unzutreffenden Eindruck eines erheblichen Preisvorteils zu erwecken (vgl. BGH, **Durchgestrichener Preis II**, I ZR 182/14 `[unverifiziert – prüfen in juris]`). Maßstab ist nach Art. 6 a UGP-RL und § 11 PAngV der vorher tatsächlich geforderte Mindestpreis (30 Tage). Empfehlung: Klarstellender Hinweis „vorher 30 Tage zu 199 EUR im Shop" oder Streichung des Vergleichs.

## Risiken / typische Fehler

- **Schwarze Liste nicht abgeglichen** — bei Treffer entfällt Spürbarkeitsprüfung, Verstoß steht fest.
- **Falsches Verbraucherleitbild** — nicht "der flüchtige Verbraucher", sondern UGP-RL-konform durchschnittlich informiert/aufmerksam/verständig.
- **Sternchen-Hinweis vergessen oder zu klein** — wesentliche Information § 5a UWG kann nicht durch versteckten Footer geheilt werden.
- **§ 6 UWG-Prüfung lückenhaft** — alle sechs Voraussetzungen Abs. 2 sind kumulativ.
- **PAngV-Pflichten unterschätzt** — Grundpreisangabe-Verstöße werden massenhaft abgemahnt.
- **HWG-/LMIV-Spezialregelungen übersehen** — strengere Maßstäbe als § 5 UWG.
- **UGP-RL-konforme Auslegung ausgeblendet** — bei B2C-Werbung primärrechtskonform auszulegen; bei Zweifel Vorlage Art. 267 AEUV.

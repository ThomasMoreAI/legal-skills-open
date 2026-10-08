---
name: zolltarif-vzta-antrag-borghei
title: /aussenwirtschaft-zoll-sanktionen:zolltarif-vzta-antrag
description: Tarifierung einer Ware in TARIC nach den Allgemeinen Vorschriften AV 1–6 und Entwurf eines Antrags auf verbindliche Zolltarifauskunft (vZTA) nach Art. 33 UZK – mit Abgrenzung zur verbindlichen Ursprungsauskunft (vUA), nicht-präferenziellem vs. präferenziellem Ursprung und ATLAS-Antragsverfahren. Use when ein Importeur/Exporteur eine streitige Tarifierung absichern will, eine verbindliche Auskunft beim Zoll beantragen möchte oder eine Ablehnung anfechten will.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/aussenwirtschaft-zoll-sanktionen/skills/zolltarif-vzta-antrag
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: trade
language: de
---

# /aussenwirtschaft-zoll-sanktionen:zolltarif-vzta-antrag

## Zweck

Der Skill führt durch die TARIC-Tarifierung nach den Allgemeinen Vorschriften (AV 1–6) und entwirft einen Antrag auf verbindliche Zolltarifauskunft (vZTA) nach Art. 33 UZK mit erschöpfender Warenbeschreibung. Er adressiert daneben die verbindliche Ursprungsauskunft (vUA) und die Unterscheidung zwischen nicht-präferenziellem Ursprung (Art. 60 UZK) und präferenziellem Ursprung (Freihandelsabkommen).

## Eingaben

- Ware: Bezeichnung, Material/Werkstoffe, Funktion, Hauptverwendung, Herstellungsverfahren
- Technische Spezifikation: Maße, Gewicht, Aufmachung, Verpackung
- Verwendungszweck und Bestimmungsmarkt
- vorgesehener TARIC-Code oder konkurrierende Codes (z.B. Kap. 85 vs. 90)
- Stückzahl, Wert, Ursprungsland (vorläufige Einschätzung)
- vorhandene Datenblätter, Fotos, technische Zeichnungen
- ggf. Vergleich mit vergleichbaren Waren / bisheriger Abfertigung

## Sub-Agent-Architektur

Researcher liefert UZK-Vorschriften, AV 1–6, einschlägige EuGH-Tarifierungsrspr. und BFH-Entscheidungen, Kommentarstellen (Witte UZK, Dorsch). Drafter führt die AV-Prüfung im Gutachtenstil durch und entwirft den vZTA-Antrag (erschöpfende Warenbeschreibung, AV-Begründung, vorgeschlagener Code). Reviewer prüft AV-Reihenfolge, vollständige Warenbeschreibung und Bindungswirkung der vZTA.

## Ablauf

### 1. Allgemeine Vorschriften (AV) – Reihenfolge

Tarifierung erfolgt **streng** in dieser Reihenfolge (Anhang I VO Tarif-/Zolltarifschema, AV 1–6):

| AV | Inhalt |
|---|---|
| **AV 1** | Wortlaut der Positionen und Anmerkungen zu Abschnitten/Kapiteln (Vorrang) |
| **AV 2 a)** | Unvollständige/unfertige Ware mit wesentlichem Charakter der fertigen |
| **AV 2 b)** | Mischungen und Verbindungen aus mehreren Stoffen / mit anderen Stoffen |
| **AV 3 a)** | Genauere Warenbezeichnung vor allgemeinerer |
| **AV 3 b)** | Wesentlicher Charakter |
| **AV 3 c)** | Letzte in Betracht kommende Position |
| **AV 4** | Ähnlichkeitsregel (subsidiär) |
| **AV 5** | Behältnisse, Verpackungen |
| **AV 6** | Unterpositionen entsprechend AV 1–5 anwenden |

**AV 1 hat absoluten Vorrang.** Wenn AV 1 die Tarifierung trägt, sind AV 2–4 nicht zu bemühen. Standardfehler: direkter Einstieg mit AV 3b („wesentlicher Charakter") ohne saubere Prüfung von Wortlaut und Anmerkungen.

EuGH-Linie: Tarifierung folgt **objektiven Merkmalen und Eigenschaften** der Ware, ablesbar aus Wortlaut und Erläuterungen; Verwendungszweck nur ausnahmsweise relevant (vgl. EuGH, Urt. v. 19.10.2000 – Rs. C-339/98, Peacock, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2000-10-19&Aktenzeichen=C-339/98); EuGH, Urt. v. 06.12.2007 – Rs. C-486/06, Van Landeghem, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2007-12-06&Aktenzeichen=C-486/06)).

### 2. TARIC-Recherche

- **EZT-online** (Elektronischer Zolltarif, zoll.de) für gültige Codes und Abgaben
- **TARIC-Datenbank** (EU-Kommission) für EU-weite Maßnahmen (Antidumping, Tarifkontingente)
- Erläuterungen zur Kombinierten Nomenklatur (KN) – HS-Erläuterungen
- vergleichbare bisherige vZTA-Entscheidungen (EBTI-Datenbank EU)

### 3. Verbindliche Zolltarifauskunft (vZTA) – Art. 33 UZK

**Voraussetzungen** (Art. 33 UZK iVm Art. 19–22 UZK-DA):

- Antragsberechtigt: in der EU ansässige Person, beabsichtigte Verwendung in Zollverfahren plausibel
- **Ein Antrag pro Ware** (nicht mehrere Waren in einem Antrag)
- erschöpfende Warenbeschreibung (technische Daten, Material, Funktion, Verwendung)
- ggf. Muster, Proben, Datenblätter, Fotos
- vorgeschlagener TARIC-Code mit Begründung (AV-Reihenfolge)

**Bearbeitungsdauer:** maximal **120 Tage** (Art. 22 Abs. 3 UZK), Eingangsbestätigung **30 Tage** nach Annahme.

**Bindungswirkung:** **3 Jahre** ab Erteilungsdatum (Art. 33 Abs. 3 UZK). Bindet die Zollbehörden **aller** Mitgliedstaaten gegenüber dem Inhaber bei Ausfuhr/Einfuhr der konkret beschriebenen Ware.

**Erlöschen** vor Ablauf der 3 Jahre (Art. 34 UZK):

- Änderung der TARIC-Klassifikation
- EuGH-Urteil, das die Tarifierung umstößt
- Widerruf durch die Zollbehörde

### 4. Verbindliche Ursprungsauskunft (vUA) – parallel Art. 33 UZK

vUA bindet zur Frage des **nicht-präferenziellen** (Art. 60 UZK) **oder präferenziellen** Ursprungs:

- **Nicht-präferenzieller Ursprung** (Art. 60 UZK): „letzte wesentliche und wirtschaftlich gerechtfertigte Be- oder Verarbeitung"
- **Präferenzieller Ursprung:** Ursprungsregeln des jeweiligen Freihandelsabkommens (z.B. CETA, EU-UK TCA, EU-Vietnam)
- Bindungswirkung **3 Jahre** ab Erteilung

### 5. Antragsweg / ATLAS

- Antragstellung über **ATLAS** / Bürger- und Geschäftskundenportal des Zolls
- Bearbeitende Zollverwaltung: **Generalzolldirektion** (DE), regional die zuständigen Dienststellen
- Sprache: Deutsch (in DE), bei vUA mit ausländischem Bezug ggf. zusätzlich Englisch

### 6. Rechtsbehelf bei Ablehnung

- Einspruch nach §§ 347 ff. AO innerhalb **1 Monat** ab Bekanntgabe
- Klage vor dem **Finanzgericht** nach § 40 FGO
- Vorabentscheidung an den EuGH durch das nationale Gericht möglich (Art. 267 AEUV; siehe Skill `europarecht/vorabentscheidung-art-267`)

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Primär- und Sekundärrecht

- [VO (EU) 952/2013 (UZK)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952) – insb. Art. 33, 34, 56, 57, 60
- [VO (EU) 2015/2446 (UZK-DA)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)
- [VO (EU) 2015/2447 (UZK-IA)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2447)
- [VO (EWG) 2658/87 (Kombinierte Nomenklatur)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:31987R2658)
- [Abgabenordnung](https://www.gesetze-im-internet.de/ao_1977/) – insb. §§ 347 ff. (Einspruch)
- [Finanzgerichtsordnung](https://www.gesetze-im-internet.de/fgo/) – insb. §§ 40 ff.

### Behördliche Quellen

- EZT-online (zoll.de)
- ATLAS / Bürger- und Geschäftskundenportal des Zolls
- EU-Kommission, TARIC-Datenbank
- EU-Kommission, EBTI-Datenbank (vZTA-Entscheidungen aller Mitgliedstaaten)
- Erläuterungen zur Kombinierten Nomenklatur (ABl. EU regelmäßig)

### Kommentare

- Witte, Unionszollkodex, 8. Aufl. 2022, Art. 33 UZK Rn. 1 ff.
- Lux, in: Dorsch, Zollrecht, Stand 2024, Art. 33 UZK Rn. 1 ff.
- Bender, in: Krenzler/Herrmann/Niestedt, EU-Außenwirtschafts- und Zollrecht, Stand 2024, Art. 33 UZK Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris/BFH-Datenbank]`, soweit markiert)

1. EuGH, Urt. v. 19.10.2000 – Rs. C-339/98, Peacock (Tarifierung von Netzwerkkarten nach objektiven Merkmalen und Eigenschaften), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2000-10-19&Aktenzeichen=C-339/98)
2. EuGH, Urt. v. 06.12.2007 – Rs. C-486/06, Van Landeghem (Einreihung von Pick-ups: Position 8703 oder 8704 KN), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2007-12-06&Aktenzeichen=C-486/06)
3. BFH zu vZTA-Bindung und Widerruf nach Art. 34 UZK — ohne Aktenzeichen und Datum nicht recherchierbar `[unverifiziert – prüfen in juris/BFH-Datenbank]`

## Ausgabeformat

```
ANTRAG auf verbindliche Zolltarifauskunft (Art. 33 UZK)
Antragsteller: <Firma, EORI-Nr.>
Datum: <…>

I. Ware
   1. Bezeichnung (Handelsname + technischer Name):
   2. Erschöpfende Warenbeschreibung:
      a) Material/Werkstoffe (Anteile %):
      b) Funktion / Arbeitsweise:
      c) Aufmachung / Verpackung:
      d) Bestimmungszweck:
      e) Maße, Gewicht:
   3. Anlagen: Datenblatt, Foto, Schnittzeichnung, ggf. Muster

II. Vorgeschlagener TARIC-Code: <NNNN NN NN NN>
    Begründung in AV-Reihenfolge:
    1. AV 1 – Wortlaut der Position + Anmerkungen
    2. ggf. AV 2 / 3 / 4
    3. AV 6 – Unterposition

III. Konkurrierender Code (verworfen): <…> – Begründung Abgrenzung

IV. Verwendung in Zollverfahren
    - Einfuhr / Ausfuhr / Versand:
    - voraussichtlicher Zeitpunkt:

V. Hinweis
   Bearbeitungsdauer max. 120 Tage (Art. 22 Abs. 3 UZK).
   Bindungswirkung 3 Jahre ab Erteilung (Art. 33 Abs. 3 UZK).

VI. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Einstieg mit AV 3b** ohne saubere AV-1-Prüfung → vZTA wird ggf. abgelehnt oder anderer Code erteilt.
- **Mehrere Waren in einem Antrag** – Art. 33 UZK iVm UZK-DA: ein Antrag pro Ware. Sammelanträge werden zurückgewiesen.
- **Unvollständige Warenbeschreibung** – Beschreibung muss so präzise sein, dass die Bindung tatsächlich greift. „Modul" oder „Gerät" reicht nicht; technische Parameter, Material-Anteile, Funktion sind Pflicht.
- **vZTA „wandert" mit der Ware** – ändert sich die Spezifikation (Material, Funktion), gilt die vZTA nicht mehr. Bei Produktrevisionen erneut prüfen.
- **Erlöschen nach Art. 34 UZK übersehen** – EuGH-Urteil oder KN-Änderung kann die vZTA vor Ablauf entwerten. Re-Screening regelmäßig.
- **Verwechslung vZTA / vUA** – Tarif (vZTA) und Ursprung (vUA) sind getrennte Auskünfte; bei Bedarf beide beantragen.
- **Präferenzieller vs. nicht-präferenzieller Ursprung** vermengt – Folge: falscher Zoll, falsche Präferenznutzung, Verstoß § 370 AO (Zollhinterziehung) möglich.
- **Antidumping/Schutzmaßnahmen aus TARIC nicht mitgeprüft** – Tarifierung ohne TARIC-Maßnahmenanzeige ist unvollständig.

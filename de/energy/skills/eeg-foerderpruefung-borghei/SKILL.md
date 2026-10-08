---
name: eeg-foerderpruefung-borghei
title: /energierecht:eeg-foerderpruefung
description: Prüfung der Anspruchsvoraussetzungen für Marktprämie und Einspeisevergütung nach EEG 2023 – Anlagenart, Inbetriebnahme (§ 3 Nr. 30 EEG), Marktstammdatenregister-Meldung (§ 8 MaStRV / § 6 EEG), Förderzeitraum, anzulegender Wert nach Ausschreibung (§§ 36 ff. EEG) oder Festwert (§§ 49 ff. EEG), Direktvermarktung (§ 21b EEG), Reduktionen (Negativstunden § 51 EEG, Anlagengröße, Marktintegration). Use when ein Anlagenbetreiber Förderfähigkeit prüfen oder gegen einen Reduktions-/Verweigerungsbescheid des Netzbetreibers vorgehen will.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/energierecht/skills/eeg-foerderpruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: energy
language: de
---

# /energierecht:eeg-foerderpruefung

## Zweck

Der Skill prüft, ob für eine Erzeugungsanlage (PV, Wind, Biomasse, Wasser, Geothermie) Anspruch auf Marktprämie nach § 19 EEG oder Einspeisevergütung besteht, mit welcher Höhe (anzulegender Wert) und für welchen Zeitraum, und welche Reduktionstatbestände greifen. Er adressiert die zwei häufigsten Förderkiller: **Inbetriebnahmedatum** (technische Betriebsbereitschaft) und **MaStR-Meldung**.

## Eingaben

- Anlagenart, Leistung (kW/MW), Standort (anonymisiert)
- geplantes oder behauptetes IBN-Datum + Belege (Probebetrieb, Einspeiseprotokoll)
- Ausschreibungsteilnahme (BNetzA-Zuschlag mit Datum und Az.) oder Festwert-Regime
- MaStR-Eintragungsdatum (Marktstammdatenregister-Nummer)
- BImSchG-Genehmigungsstatus (bei Wind und Großanlagen)
- gegenwärtige Vermarktungsform (Direktvermarktung, geförderte Direktvermarktung, Einspeisevergütung)
- Vorgehen des Netzbetreibers (Vergütungs-Auszahlungsstop, Reduktionsbescheid, Pönalenforderung)

## Sub-Agent-Architektur

Researcher liefert die EEG-Stellen (§§ 3, 6, 8, 19, 21b, 22, 27/27a, 36 ff., 49 ff., 51, 100), MaStRV, einschlägige BNetzA-Festlegungen zum Ausschreibungsverfahren und Rechtsprechung des BGH-VIII. Senats / OLG Düsseldorf. Drafter erstellt im Gutachtenstil die Prüfung in der Reihenfolge IBN → MaStR → Förderregime → Höhe → Reduktionen → Verfahren. Reviewer prüft vor allem IBN-Datum und MaStR-Meldung (häufigste Blocker) sowie BImSchG-Status.

## Ablauf

### 1. Anlagenbegriff und Inbetriebnahme (§ 3 Nr. 1, Nr. 30 EEG)

**Inbetriebnahme** ist die erstmalige Inbetriebsetzung der Anlage nach Herstellung der **technischen Betriebsbereitschaft**. Voraussetzungen:

- technisch betriebsbereit (alle wesentlichen Anlagenteile installiert und funktionsfähig)
- einspeisefähig (Anschluss am Verknüpfungspunkt hergestellt)
- nicht erforderlich: vollständige Auslegungslast, finale Trafoanbindung, vollständige Behördenfreigabe sämtlicher Nebenanlagen — Maßstab ist die **bestimmungsgemäße Stromerzeugung am Standort** (vgl. Müggenborg, in: Frenz/Müggenborg, EEG, 6. Aufl. 2023, § 3 Rn. 200 ff. `[unverifiziert]`).

**Praxisproblem.** Streitig ist regelmäßig, ob die Anlage am behaupteten IBN-Datum bereits betriebsbereit war. Beweismittel: Probebetriebsprotokoll, Zählerstandserfassung, Einspeisemeldung, technische Abnahmeprotokolle.

### 2. MaStR-Meldung (§ 6 EEG, § 8 MaStRV)

Pflicht zur Eintragung im Marktstammdatenregister; Verstoß führt nach § 52 EEG zur **vollständigen Reduktion** des anzulegenden Wertes auf null bzw. zur Sanktion in Höhe einer Pauschale. Die Eintragungsfrist beträgt einen Monat ab IBN.

**Konsequenz**: Vor jeder Förderprüfung ist die MaStR-Nummer und das Eintragungsdatum zu verifizieren.

### 3. Förderregime

| Anlagengröße / Art | Regime | Norm |
|---|---|---|
| PV ≤ 100 kW (Dach, bestimmte Konstellationen) | Festwert / Einspeisevergütung | §§ 19, 49 ff. EEG |
| Wind, Solar, Biomasse oberhalb der Schwellen | Ausschreibung BNetzA, Marktprämie | §§ 22, 36 ff. EEG |
| Direktvermarktung (geförderte) | Marktprämie | §§ 19, 20, 21b EEG |
| Bestandsanlagen Übergang | § 100 EEG-Übergangsregeln |

Der **anzulegende Wert** ergibt sich entweder aus dem **Zuschlagswert** der BNetzA-Ausschreibung (§§ 36 ff. EEG) oder aus dem im Gesetz festgesetzten **Festwert** (§§ 49 ff. EEG), jeweils degressionsangepasst.

### 4. Förderzeitraum

Förderdauer in der Regel **20 Jahre** zuzüglich des Inbetriebnahmejahres (Berechnung ab dem 1. Januar des Folgejahres der IBN; § 25 EEG). Bei bestimmten Anlagen Sonderregeln (z. B. Biomasse-Folgevergütung).

### 5. Direktvermarktung (§ 21b EEG)

Pflicht zur Direktvermarktung ab gesetzlicher Größenschwelle (regelmäßig ≥ 100 kW installierte Leistung bei Neuanlagen). Marktprämie wird auf den Marktwert addiert; Anlagenbetreiber benötigt **fernsteuerbare technische Einrichtungen** (§ 9 EEG) und einen Direktvermarkter.

### 6. Reduktionstatbestände

- **Negativstunden (§ 51 EEG)** – anzulegender Wert wird für Stunden, in denen der Day-Ahead-Spotmarkt negative Preise aufweist, auf null reduziert (mit Differenzierungen je Anlagentyp und IBN-Periode).
- **Marktintegrationsanforderungen** – z. B. Fernsteuerbarkeit, Direktvermarktungspflicht, Messkonzept.
- **MaStR-Versäumnis** – Reduktion gem. § 52 EEG.
- **Pönale Realisierungsfrist** – § 27a EEG bei Nichtinbetriebnahme nach Ausschreibungs-Zuschlag.
- **Anlagenzusammenfassung** – § 24 EEG (Anlagenbegriff bei räumlich-funktionalem Zusammenhang).

### 7. Verfahren bei Streit

- **Zivilrechtlicher Anspruch** auf Auszahlung der Marktprämie / Einspeisevergütung gegen den Netzbetreiber – Klage vor dem ordentlichen Gericht (idR LG; Streitwertgrenze prüfen).
- **BNetzA-Beschlussverfahren §§ 31 ff. EnWG** bei Streit über die Anwendung von EEG-Vorschriften, soweit Marktteilnehmerinteressen berührt sind.
- **Schlichtungsstelle Clearingstelle EEG/KWKG** (eeg-kwkg.clearingstelle.de) als außergerichtliche Klärung.
- **Beschwerde zum OLG Düsseldorf** gegen BNetzA-Beschlüsse, § 75 EnWG (Frist: 1 Monat).

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute und Verordnungen

- [§ 3 EEG](https://www.gesetze-im-internet.de/eeg_2014/__3.html) (Definitionen, insb. Nr. 30 Inbetriebnahme)
- [§ 6 EEG](https://www.gesetze-im-internet.de/eeg_2014/__6.html) (MaStR-Meldung)
- [§ 8 EEG](https://www.gesetze-im-internet.de/eeg_2014/__8.html) (Anschluss)
- [§ 19 EEG](https://www.gesetze-im-internet.de/eeg_2014/__19.html) (Förderanspruch)
- [§ 21b EEG](https://www.gesetze-im-internet.de/eeg_2014/__21b.html) (Direktvermarktung)
- [§ 22 EEG](https://www.gesetze-im-internet.de/eeg_2014/__22.html) (Ausschreibungen)
- [§ 24 EEG](https://www.gesetze-im-internet.de/eeg_2014/__24.html) (Anlagenzusammenfassung)
- [§ 25 EEG](https://www.gesetze-im-internet.de/eeg_2014/__25.html) (Förderzeitraum)
- [§ 27a EEG](https://www.gesetze-im-internet.de/eeg_2014/__27a.html) (Pönalen Realisierungsfrist) `[unverifiziert – Nummerierung im aktuellen EEG prüfen]`
- [§§ 36 ff. EEG](https://www.gesetze-im-internet.de/eeg_2014/) (Ausschreibungsverfahren)
- [§§ 49 ff. EEG](https://www.gesetze-im-internet.de/eeg_2014/) (Festwerte)
- [§ 51 EEG](https://www.gesetze-im-internet.de/eeg_2014/__51.html) (Negativstunden)
- [§ 52 EEG](https://www.gesetze-im-internet.de/eeg_2014/__52.html) (Reduktion bei Pflichtverstoß)
- [§ 100 EEG](https://www.gesetze-im-internet.de/eeg_2014/__100.html) (Übergangsbestimmungen)
- [§ 8 MaStRV](https://www.gesetze-im-internet.de/mastrv/__8.html) (Eintragungspflicht)
- EU: [RED III](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023L2413) (RL (EU) 2023/2413), beihilferechtliche Rahmenbedingungen (Klima-, Umwelt- und Energiebeihilfen-Leitlinien)

### Kommentare

- Lehnert, in: Frenz/Müggenborg, EEG, 6. Aufl. 2023, § 3 Rn. 200 ff. (Inbetriebnahme) `[unverifiziert]`
- Salje, in: Theobald/Kühling, Energierecht (Loseblatt, Stand 2024), § 19 EEG Rn. 1 ff. `[unverifiziert]`
- Säcker/Schulte, in: Säcker, BerlKomm Energierecht, 4. Aufl. 2019, § 22 EEG Rn. 1 ff. `[unverifiziert]`

### Rechtsprechung und Behördenpraxis (`[unverifiziert – prüfen in juris / clearingstelle.de / bundesnetzagentur.de]`)

1. BGH, Urt. v. – VIII ZR Az., NJW Jahr, S. (Inbetriebnahme-Begriff EEG) `[unverifiziert]`
2. OLG Düsseldorf, Beschl. v. – VI-3 Kart Az., RdE Jahr, S. (BNetzA-Ausschreibung) `[unverifiziert]`
3. Clearingstelle EEG/KWKG, Empfehlung – Az. (IBN-Datum / MaStR) `[unverifiziert]`
4. BNetzA, Festlegung BK6 zu Ausschreibungsverfahren `[unverifiziert]`

## Ausgabeformat

```
GUTACHTEN — EEG-Förderprüfung
Anlage: <Typ, Leistung, Standort (anonymisiert)>
IBN behauptet: <Datum>
MaStR-Nr.: <Nummer / Datum der Eintragung>
Ausschreibungs-Zuschlag: <Az. / Datum oder „kein Zuschlag, Festwert"

I. Sachverhalt (knapp)
II. Frage(n)
III. Kurzantwort
    – Förderanspruch dem Grunde nach: [ja / nein / nur mit Reduktion]
    – anzulegender Wert: <ct/kWh>
    – Förderzeitraum: <20 Jahre + IBN-Jahr>

IV. Rechtliche Bewertung
    1. Anlagenbegriff und Inbetriebnahme (§ 3 Nr. 30 EEG)
       – technische Betriebsbereitschaft
       – Beweismittel
    2. MaStR-Meldung (§ 6 EEG, § 8 MaStRV)
       – Eintragungsdatum
       – ggf. Reduktion § 52 EEG
    3. Förderregime
       a) Ausschreibung §§ 22, 36 ff. EEG oder Festwert §§ 49 ff. EEG
       b) Direktvermarktung § 21b EEG
    4. Höhe (anzulegender Wert)
    5. Förderzeitraum § 25 EEG
    6. Reduktionen
       a) Negativstunden § 51 EEG
       b) Marktintegration / Fernsteuerbarkeit § 9 EEG
       c) Anlagenzusammenfassung § 24 EEG
       d) Pönale Realisierungsfrist § 27a EEG
    7. BImSchG-Genehmigungsstatus als Vorfrage (Wind/Großanlagen)
    8. Verfahren
       – Auszahlungsklage VNB (ordentlicher Rechtsweg)
       – Clearingstelle EEG/KWKG
       – BNetzA-Beschlussverfahren §§ 31 ff. EnWG, Beschwerde OLG Düsseldorf § 75 EnWG

V. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>
    Offene Tatsachen: IBN-Beweis, MaStR-Status, BImSchG-Status, Zuschlagsbedingungen

VI. Quellenverzeichnis
```

## Beispiel (Gutachtenstil, gekürzt)

> **Sachverhalt.** Windpark mit 6 WEA á 4,2 MW, Zuschlag in BNetzA-Ausschreibungsrunde. IBN geplant für 31.12.; eine 110-kV-Trafostation ist noch nicht installiert, die Anlagen sind aber an ein provisorisches 30-kV-Anschlusspunkt einspeisefähig.
>
> **Inbetriebnahme.** § 3 Nr. 30 EEG verlangt die **technische Betriebsbereitschaft** der Anlage. Maßstab ist die bestimmungsgemäße Stromerzeugung am Standort, nicht die Fertigstellung sämtlicher Nebenanlagen. Ist die Anlage einspeisefähig und werden tatsächlich Mengen eingespeist (Zählerstand), liegt die IBN regelmäßig vor (vgl. Lehnert, in: Frenz/Müggenborg, EEG, 6. Aufl. 2023, § 3 Rn. 200 ff. `[unverifiziert]`).
>
> **MaStR.** Eintragung gem. § 6 EEG / § 8 MaStRV binnen eines Monats ab IBN; Verstoß führt zu vollständiger Förderreduktion nach § 52 EEG. **Hier zu klären: Eintragungsdatum.**
>
> **Anzulegender Wert.** Aus dem Zuschlag in der BNetzA-Ausschreibung (§§ 36 ff. EEG), nicht Festwert. Förderzeitraum 20 Jahre + IBN-Jahr (§ 25 EEG).
>
> **Reduktionen.** Negativstunden-Reduktion § 51 EEG; Fernsteuerbarkeit § 9 EEG sicherzustellen. Pönale § 27a EEG entfällt bei rechtzeitiger IBN.
>
> **Ergebnis.** Förderanspruch dem Grunde nach 🟢, sofern technische Betriebsbereitschaft am 31.12. nachweisbar und MaStR-Eintragung binnen Frist erfolgt. 🔴 hinsichtlich BImSchG-Genehmigungsstatus, der nicht vorgetragen ist – Genehmigung muss bestandskräftig oder zumindest sofort vollziehbar sein. Empfehlung: lückenlose IBN-Dokumentation (Probebetriebsprotokoll, Zählerstand, Einspeisemeldung) und MaStR-Eintragung am IBN-Tag.

## Risiken / typische Fehler

- **IBN-Datum ungesichert** – häufigster Förderkiller. Ohne Probebetriebsprotokoll / Zählerstand / Einspeisemeldung am behaupteten Stichtag droht Förderverlust.
- **MaStR-Meldung versäumt** oder zu spät – § 52 EEG-Reduktion bis hin zu null.
- **BImSchG-Genehmigung übersehen** bei Wind/Großanlagen – materielle Vorfrage für EEG-Förderanspruch.
- **Anlagenzusammenfassung § 24 EEG ignoriert** – mehrere Anlagen werden als eine behandelt, Förderhöhe sinkt.
- **Pönale § 27a EEG nach Zuschlag** – Realisierungsfristen müssen aktiv überwacht werden.
- **Strompreisbremse/Gaspreisbremse** zitiert ohne `[unverifiziert – aktuelle Geltung prüfen]` – Übergangsmaßnahmen 2022–2024 sind kurzlebig und teils ausgelaufen.
- **Vermischung mit Energiekartellrecht** (Marktmissbrauch durch Netzbetreiber, §§ 19, 29 GWB) – gehört in Plugin `kartellrecht`.

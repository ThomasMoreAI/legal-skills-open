---
name: mbo-aerzte-pruefung-borghei
title: /medizinrecht:mbo-aerzte-pruefung
description: Berufsrechtliche Prüfung ärztlicher Pflichten nach der Musterberufsordnung MBO-Ä und der einschlägigen Landesberufsordnung – Werbung § 27 MBO-Ä iVm HWG, Schweigepflicht § 9 MBO-Ä iVm § 203 StGB, Dokumentation § 10 MBO-Ä iVm § 630f BGB, Fernbehandlung § 7 IV MBO-Ä, Fortbildung § 4 MBO-Ä iVm § 95d SGB V, Honorar § 12 MBO-Ä iVm GOÄ. Use when ein Arzt von einer Landesärztekammer berufsrechtlich in Anspruch genommen wird oder berufsrechtliche Konformität einer Praxis-/Werbekonzeption zu prüfen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/medizinrecht/skills/mbo-aerzte-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: healthcare
language: de
---

# /medizinrecht:mbo-aerzte-pruefung

## Zweck

Der Skill prüft, ob ein konkretes ärztliches Verhalten mit der Musterberufsordnung für Ärzte (MBO-Ä) und der einschlägigen, vom jeweiligen Bundesland normativ in Kraft gesetzten Landesberufsordnung (LBO) vereinbar ist. Er bildet die berufsrechtliche Komplementärschicht zur zivilrechtlichen Arzthaftung ab und prüft drohende Sanktionen vor den Berufsgerichten (Warnung → Verweis → Geldbuße → Entzug der Berufsausübungserlaubnis). Schnittstellen zu § 203 StGB, HWG, SGB V und BÄO werden mitgeprüft.

## Eingaben

- konkretes ärztliches Verhalten (Werbeaussage, Datenweitergabe, Honorarvereinbarung, Fernbehandlung etc.)
- Bundesland und Fachrichtung (Allgemeinmediziner, Facharzt, Zahnarzt – Zahnärzte unterliegen der MBO-Z; nicht Gegenstand dieses Skills)
- Status (niedergelassen, angestellt, Klinik, MVZ)
- ggf. laufendes Verfahren der Landesärztekammer / Berufsgericht
- Position des Mandanten (betroffener Arzt, Ärztekammer, Mitbewerber)

## Sub-Agent-Architektur

Researcher liefert MBO-Ä, die im konkreten Bundesland einschlägige LBO, HeilBerKG/HKaG (Berufsgerichtsbarkeit), § 203 StGB, HWG, GOÄ, SGB V (insb. § 95d Fortbildung), BÄO sowie Kommentar (Ratzel/Lippert/Prütting zur MBO-Ä, Spickhoff Medizinrecht) und BVerfG/BGH-Rspr. zu Heilberufler-Werbung. Drafter prüft die Berufspflicht, Pflichtverletzung, Verschulden und Sanktionierungsspielraum im Gutachtenstil. Reviewer kontrolliert insb., dass die **konkrete LBO** (nicht nur MBO-Ä) zitiert wird und Schnittstellen zu § 203 StGB und HWG erkannt sind.

## Ablauf

### 1. Maßgeblichkeit der Landesberufsordnung

Wichtigste methodische Weiche: Die MBO-Ä nur Muster, normativ verbindlich ist die jeweilige Landesberufsordnung (LBO), die von der Vertreterversammlung der LandesÄK aufgrund des landesrechtlichen Heilberufe-Kammergesetzes (HeilBerKG; in Bayern: HKaG / Bayerische LBO; KammerG in anderen Ländern) erlassen wird. Vor jeder berufsrechtlichen Bewertung ist das einschlägige Bundesland zu identifizieren und die dortige LBO einzubeziehen. Die LBO kann von der MBO-Ä abweichen (insb. bei Werbung und Fernbehandlung – Bundesländer haben § 7 IV MBO-Ä unterschiedlich übernommen).

### 2. Werbung § 27 MBO-Ä (in der jeweiligen LBO)

[§ 27 MBO-Ä](https://www.bundesaerztekammer.de/) erlaubt **sachangemessene Information**, verbietet **berufswidrige Werbung**. Berufswidrig ist insbesondere:

- **anpreisende Werbung** (Heilsversprechen, „100 % Erfolg")
- **irreführende Werbung** (unzutreffende Qualifikation, falsche Statistiken)
- **vergleichende Werbung** in herabsetzender Form

Verfassungsrechtlicher Rahmen: BVerfG-Linie zur Heilberufler-Werbung – das früher strikte Werbeverbot ist gelockert; Maßstab ist Art. 12 GG. Werbeverbote, die über sachliche Information hinaus pauschal verbieten, sind verfassungswidrig (BVerfG-Linie seit 1980er; vgl. BVerfG, Beschl. v. 18.10.2001 – 1 BvR 881/00 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=18.10.2001&Aktenzeichen=1+BvR+881/00)).

Schnittstelle: [HWG](https://www.gesetze-im-internet.de/heilmwerbg/) (Heilmittelwerbegesetz) – flankierend; § 11 HWG verbietet bestimmte Werbeformen außerhalb der Fachkreise.

Bewertungsportale: BGH-Linie „jameda I" (Urt. v. 23.09.2014 – VI ZR 358/13, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.09.2014&Aktenzeichen=VI+ZR+358/13) und „jameda II" (Urt. v. 20.02.2018 – VI ZR 30/17, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=20.02.2018&Aktenzeichen=VI+ZR+30/17) – Recht des Arztes auf Löschung bei nicht-neutraler Bewerbungsplattform; berufsrechtlich problematisch: Kauf bezahlter Premium-Platzierungen, wenn der Eindruck redaktioneller Unabhängigkeit erweckt wird.

### 3. Schweigepflicht § 9 MBO-Ä (in der jeweiligen LBO) iVm § 203 StGB

Berufsrechtlich strikt; deckt mehr als § 203 StGB ab (auch nicht-strafrechtliche Indiskretionen). Pflichtverletzung **doppelt sanktionsbewehrt**:

- strafrechtlich [§ 203 StGB](https://www.gesetze-im-internet.de/stgb/__203.html) (Freiheitsstrafe bis 1 Jahr / Geldstrafe)
- berufsrechtlich Sanktion über das Berufsgericht
- ggf. zivilrechtliche Haftung § 823 II BGB iVm § 203 StGB; Art. 82 DSGVO

Externe Dienstleister (IT, Abrechnung, Schreibbüro): § 203 III StGB (Reform 2017) verlangt Einbindung „sonstiger mitwirkender Personen" über vertragliche Verpflichtung zur Verschwiegenheit; Verletzung der Sorgfaltspflichten bei Auswahl/Überwachung ist strafbar.

### 4. Dokumentation § 10 MBO-Ä iVm § 630f BGB

Pflicht zur unverzüglichen Aufzeichnung aller medizinisch relevanten Maßnahmen. Aufbewahrung **mindestens 10 Jahre** nach Abschluss der Behandlung; bei minderjährigen Patienten bis Volljährigkeit + 10 Jahre; Röntgenaufnahmen idR 10 Jahre (§ 85 III StrlSchV). Faktisch wegen § 199 II BGB (30 Jahre) längere Aufbewahrung sinnvoll.

### 5. Honorar § 12 MBO-Ä iVm GOÄ

Honorarvereinbarungen mit Privatpatienten nur im Rahmen der [GOÄ](https://www.gesetze-im-internet.de/go__/); Überschreitung des Steigerungssatzes nur durch schriftliche Vereinbarung vor Leistungserbringung (§ 2 GOÄ). Vertragsärzte unterliegen zusätzlich dem EBM und SGB V §§ 87, 87b.

### 6. Fortbildungspflicht § 4 MBO-Ä iVm § 95d SGB V

Vertragsärzte: Nachweis der Fortbildung alle fünf Jahre (250 CME-Punkte). Verstoß: Honorarkürzung bis zum Ruhen der Zulassung.

### 7. Fernbehandlung § 7 Abs. 4 MBO-Ä (in der jeweiligen LBO)

Lockerung 2018: ausschließliche Beratung oder Behandlung über Kommunikationsmedien ist nach Maßgabe des einzelnen Bundeslandes erlaubt, wenn es ärztlich vertretbar ist und die erforderliche ärztliche Sorgfalt gewahrt bleibt. Aufklärungs-Hinweispflicht über die Besonderheiten der ausschließlichen Fernbehandlung.

### 8. Sanktionsspielraum

Berufsgerichtsbarkeit nach jeweiligem HeilBerKG / HKaG des Landes. Typische Sanktionen in aufsteigender Reihenfolge:

1. **Rüge / Warnung** durch die Kammer (unter der Schwelle des Berufsgerichts)
2. **Verweis**
3. **Geldbuße** (in den meisten LBO bis € 50.000–100.000, landesabhängig)
4. **Entziehung des passiven Berufswahlrechts in der Kammer**
5. **Feststellung der Berufsunwürdigkeit** → Widerruf der Approbation nach § 5 BÄO (Approbationsbehörde, nicht Berufsgericht)

Parallelverfahren möglich (z. B. Strafverfahren § 203 StGB + Berufsgericht + Approbationsentzug § 5 BÄO).

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute / Berufsrecht

- **MBO-Ä** (Stand der jeweiligen Beschlussfassung der Bundesärztekammer; nur Muster) – §§ 2, 4, 7, 8, 9, 10, 12, 27
- **Landesberufsordnung** des betroffenen Bundeslandes (verbindlich) – verlinkt über LandesÄK
- **HeilBerKG / HKaG / KammerG** des betroffenen Bundeslandes (Berufsgerichtsbarkeit, Sanktionen)
- [BÄO](https://www.gesetze-im-internet.de/b_o/) – §§ 2 ff. (Approbation), § 5 (Widerruf), § 6 (Ruhen)
- [§ 203 StGB](https://www.gesetze-im-internet.de/stgb/__203.html)
- [HWG](https://www.gesetze-im-internet.de/heilmwerbg/)
- [GOÄ](https://www.gesetze-im-internet.de/go__/)
- [§ 95d SGB V](https://www.gesetze-im-internet.de/sgb_5/__95d.html) (Fortbildungspflicht der Vertragsärzte)
- [§ 630f BGB](https://www.gesetze-im-internet.de/bgb/__630f.html) (Dokumentation)

### Kommentare

- Ratzel/Lippert/Prütting, Kommentar zur Musterberufsordnung für Ärzte (MBO-Ä), 7. Aufl. 2018
- Spickhoff, in: Spickhoff, Medizinrecht, 4. Aufl. 2022, MBO-Ä und HeilBerKG-Erläuterungen
- Laufs/Katzenmeier/Lipp, Handbuch des Arztrechts, 8. Aufl. 2021, Kap. III (Berufsrecht)
- Fischer, StGB-Kommentar, aktuelle Aufl., § 203
- Cierniak/Niehaus, in: MüKoStGB, aktuelle Aufl., § 203

### Rechtsprechung

1. BVerfG, Beschl. v. 18.10.2001 – 1 BvR 881/00 (Heilberufler-Werbung, Art. 12 GG) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=18.10.2001&Aktenzeichen=1+BvR+881/00)
2. BGH, Urt. v. 23.09.2014 – VI ZR 358/13 („jameda I", Löschungsanspruch gegen Bewertungsportal) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.09.2014&Aktenzeichen=VI+ZR+358/13)
3. BGH, Urt. v. 20.02.2018 – VI ZR 30/17 („jameda II", verlorene Neutralität bei Premium-Platzierungen) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=20.02.2018&Aktenzeichen=VI+ZR+30/17)
4. BVerwG-Rspr. zum Widerruf der Approbation nach § 5 BÄO bei Berufsunwürdigkeit `[unverifiziert – prüfen in juris]`
5. Landesberufsgerichts-Rspr. zur Honorarvereinbarung jenseits GOÄ `[unverifiziert – prüfen in juris]`

## Ausgabeformat

```
GUTACHTEN — Berufsrechtliche Prüfung
Mandat:  <anonymisiert>
Bundesland / LBO: <…>
Berufsbezeichnung: <Facharzt für …>

I.   Sachverhalt (knapp)
II.  Frage(n)
III. Kurzantwort
     – Berufspflichtverstoß: [ja / nein / teilweise]
     – Sanktionsrisiko: 🟢 / 🟡 / 🔴

IV.  Rechtliche Bewertung
     1. Einschlägige Berufspflicht
        – LBO § ... (im Bundesland xy)
        – ggf. § ... MBO-Ä als Auslegungshilfe
     2. Pflichtverletzung
        – Tatsachenkern
        – Subsumtion
     3. Schnittstelle § 203 StGB / HWG / GOÄ / SGB V
     4. Verschulden
     5. Sanktionsspielraum (HeilBerKG/HKaG des Landes)
     6. Approbationsfolge § 5 BÄO bei Berufsunwürdigkeit?

V.   Empfehlung
     – Reaktion auf Schreiben der LandesÄK
     – Verteidigungslinie vor Berufsgericht
     – ggf. parallele strafrechtliche Vorsorge

VI.  Risiken / offene Punkte
     🟢 / 🟡 / 🔴

VII. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Zitieren der MBO-Ä als verbindlichem Recht** – MBO-Ä nur Muster, nur die LBO ist verbindlich; MBO-Ä ist Auslegungshilfe.
- **Vorher-Nachher-Fotos ohne dokumentierte Einwilligung** der Patientinnen – Verstoß gegen § 11 Abs. 1 Nr. 5 HWG und § 9 MBO-Ä; berufsrechtlich und wettbewerbsrechtlich angreifbar.
- **Übersehen des § 203 StGB-Strafrisikos** parallel zur berufsrechtlichen Sanktion.
- **Pauschales Werbeverbot** – BVerfG-Linie zu Art. 12 GG übersehen, sachliche Information ist geschützt.
- **Externe IT-Dienstleister ohne § 203 III StGB-konforme Verpflichtung** in der Praxis.
- **Honorarvereinbarung mit Privatpatienten mündlich oder ohne Steigerungsbegründung** – § 2 GOÄ verletzt.
- **Verkennen, dass Approbationsentzug § 5 BÄO ein separates verwaltungsrechtliches Verfahren** der Bezirksregierung / Landesbehörde ist – nicht des Berufsgerichts.
- **Fortbildungsnachweis nach § 95d SGB V vergessen** – schleichende Honorarkürzung bis Zulassungsruhen.

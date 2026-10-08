---
name: patientenrechte-akteneinsicht-borghei
title: /medizinrecht:patientenrechte-akteneinsicht
description: Anspruch des Patienten (und seiner Erben/Angehörigen) auf Einsicht in die Behandlungsakte nach § 630g BGB und parallel Art. 15 DSGVO – Verweigerungsgründe (therapeutischer Vorbehalt, Rechte Dritter), Form, Kostenfolge, Erbenanspruch, Verhältnis zur ärztlichen Schweigepflicht § 203 StGB. Use when ein Patient oder Erbe Einsicht verlangt und die Behandlerseite verweigert oder die Form streitig ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/medizinrecht/skills/patientenrechte-akteneinsicht
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: healthcare
language: de
---

# /medizinrecht:patientenrechte-akteneinsicht

## Zweck

Der Skill prüft den Anspruch auf Einsicht in die Behandlungsdokumentation nach § 630g BGB und das parallele Auskunftsrecht aus Art. 15 DSGVO. Beide Ansprüche stehen nebeneinander (Anspruchskonkurrenz). Der Skill prüft Verweigerungsgründe (therapeutischer Vorbehalt, Rechte Dritter), Form (Original, Kopie, elektronisch), Kostenfolgen und den Erbenanspruch nach § 630g Abs. 3 BGB. Schnittstellen zu § 203 StGB (Schweigepflicht; Verstorbenenschutz) und zur Patientenverfügung §§ 1827 ff. BGB werden mitgeprüft.

## Eingaben

- Behandlungsverhältnis (Behandler, Zeitraum, Inhalt der Akte, ggf. fremdärztliche Befunde, Aufnahmen)
- Antragsteller (Patient persönlich / gesetzlicher Vertreter / Erbe / sonstiger Angehöriger)
- Bei Erbenanspruch: Sterbedatum, Erbenstellung, behauptete vermögensrechtliche oder immaterielle Interessen
- konkrete Verweigerungsgründe der Behandlerseite
- Form-Wunsch (Einsicht vor Ort, Kopien, elektronische Übermittlung)

## Sub-Agent-Architektur

Researcher liefert § 630g BGB, Art. 15 DSGVO, § 22 BDSG, § 203 StGB, BGH-Rspr. zur restriktiven Anwendung des therapeutischen Vorbehalts, Erben-Linie, Kommentarstellen (Spickhoff, Laufs/Katzenmeier/Lipp, Wagner in MüKoBGB). Drafter erstellt Anspruchsschreiben oder Stellungnahme gegen Verweigerung im Gutachtenstil. Reviewer prüft restriktive Anwendung der Ausnahmen und das Verhältnis BGB/DSGVO (insb. Kosten, Form, Frist).

## Ablauf

### 1. Anspruchsgrundlage § 630g BGB

[§ 630g Abs. 1 S. 1 BGB](https://www.gesetze-im-internet.de/bgb/__630g.html): „Dem Patienten ist auf Verlangen unverzüglich Einsicht in die vollständige, ihn betreffende Patientenakte zu gewähren, soweit der Einsichtnahme nicht erhebliche therapeutische Gründe oder sonstige erhebliche Rechte Dritter entgegenstehen."

Tatbestandsmerkmale:

- **Patient** (Vertragspartner des Behandlungsvertrags § 630a BGB)
- **Verlangen** (formfreier Antrag; idR schriftlich aus Beweisgründen)
- **unverzüglich** – ohne schuldhaftes Zögern, § 121 I BGB-Maßstab; praktisch idR binnen weniger Wochen
- **vollständig** – inkl. Rohbefunden, Bildaufnahmen, Korrespondenz mit Mit-/Vorbehandlern, OP-Berichten, Pflegedokumentation
- **die ihn betreffende** – keine Patientenakte Dritter

### 2. Verweigerungsgründe (eng auszulegen)

§ 630g Abs. 1 S. 1 Hs. 2 BGB nennt zwei Verweigerungsgründe:

1. **Erhebliche therapeutische Gründe** – BGH-Linie: restriktiv; allein theoretische Gefährdung des Heilungserfolgs reicht nicht; konkrete, dokumentierte Gefahr für psychische Stabilität des Patienten (insb. Psychiatrie) erforderlich.
2. **Erhebliche Rechte Dritter** – z. B. Angaben Dritter (Familienanamnese) mit deren Geheimhaltungsinteresse; ggf. Schwärzung; vollständige Verweigerung selten zulässig.

Die Verweigerung ist nach § 630g Abs. 1 S. 2 BGB **zu begründen**. Pauschale Verweigerung („therapeutische Gründe") trägt nicht.

### 3. Form und Kosten

- **Originalakte** verbleibt bei der Behandlerseite; Anspruch auf **Abschriften** nach Abs. 2.
- **Elektronisch geführte Akte**: elektronische Abschrift (PDF, Bildauflösung, MRT-DICOM) genügt; bei rein elektronischer Akte ist sie auch in elektronischer Form bereitzustellen.
- **Kosten**: § 630g Abs. 2 S. 2 BGB verweist auf § 811 BGB – der Patient hat die **Kosten zu erstatten**. Faustregel: 0,50 € pro Kopie, Versandkosten zusätzlich; verlangt der Patient elektronische Übermittlung, sind die tatsächlich anfallenden Kosten (gering).

### 4. Parallel: Art. 15 DSGVO

Der Patient hat zusätzlich Anspruch auf Auskunft und **kostenfreie Datenkopie nach Art. 15 Abs. 3 DSGVO** (erste Kopie kostenfrei; weitere Kopien gegen angemessenes Entgelt). Beide Ansprüche stehen in **echter Anspruchskonkurrenz** (h.M.) – der Patient kann wählen. Praktischer Tipp: Erstantrag auf Art. 15 DSGVO stützen, weil kostenfrei und an strenge DSGVO-Frist (idR ein Monat, Art. 12 Abs. 3 DSGVO) gebunden; Akteninhalt deckt sich weitgehend.

EuGH zur Datenkopie iZm Patientenakten: Urt. v. 26.10.2023 – C-307/22 (FT/DW) (https://curia.europa.eu/juris/document/document.jsf?docid=279125&doclang=DE) – Recht auf kostenfreie erste Kopie der Patientenakte bestätigt; nationale Kostenregelung (§ 630g II 2 BGB) tritt zurück, soweit der Patient Auskunft nach Art. 15 DSGVO begehrt.

### 5. Erbenanspruch § 630g Abs. 3 BGB

Nach dem Tod des Patienten steht das Einsichtsrecht zu:

- den **Erben** zur Wahrnehmung **vermögensrechtlicher Interessen** (z. B. Behandlungsfehlerprüfung für Schadensersatzanspruch);
- den **nächsten Angehörigen** zur Geltendmachung **immaterieller Interessen** (z. B. Aufklärung der Todesursache).

Beide Ansprüche entfallen, soweit ein **entgegenstehender ausdrücklicher oder mutmaßlicher Wille** des Patienten besteht. **Beweislast für den entgegenstehenden Willen trägt die Behandlerseite**; bloße Vermutungen genügen nicht. BGH-Linie zur restriktiven Anwendung des mutmaßlichen Willens `[unverifiziert – prüfen in juris]`.

### 6. Schnittstelle § 203 StGB

Die Schweigepflicht des Arztes (§ 203 StGB, § 9 MBO-Ä in der jeweiligen LBO) gilt **über den Tod hinaus**. Die Auskunftserteilung an Erben/Angehörige darf nur erfolgen, soweit § 630g Abs. 3 BGB sie erlaubt; insoweit liegt eine **gesetzliche Befugnisnorm** vor, die den Tatbestand des § 203 StGB ausschließt. Im Zweifel: Schweigepflichtentbindungserklärung des Patienten zu Lebzeiten anfordern bzw. die Erbenstellung urkundlich (Erbschein) nachweisen lassen.

### 7. Verhältnis Patientenverfügung

Hatte der Patient eine [Patientenverfügung nach §§ 1827 ff. BGB](https://www.gesetze-im-internet.de/bgb/__1827.html) (n.F. seit Betreuungsrechtsreform 2023; früher §§ 1901a ff. BGB) errichtet, kann darin auch eine Schweigepflichtentbindung enthalten sein. Drafter sollte das Dokument anfordern.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 630g BGB](https://www.gesetze-im-internet.de/bgb/__630g.html) (Akteneinsicht)
- [§ 630f BGB](https://www.gesetze-im-internet.de/bgb/__630f.html) (Dokumentationspflicht – Grundlage des Einsichtsobjekts)
- [§ 811 BGB](https://www.gesetze-im-internet.de/bgb/__811.html) (Kostenregel über § 630g II 2 BGB)
- [§§ 1827 ff. BGB](https://www.gesetze-im-internet.de/bgb/__1827.html) (Patientenverfügung)
- [Art. 15 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679), [Art. 9 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Gesundheitsdaten)
- [§ 22 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__22.html) (Verarbeitung besonderer Kategorien personenbezogener Daten)
- [§ 203 StGB](https://www.gesetze-im-internet.de/stgb/__203.html) (Schweigepflicht)
- ggf. § 10 Abs. 3 MBO-Ä (berufsrechtliche Einsichts- und Aufbewahrungspflicht; 10 Jahre, ggf. länger)

### Kommentare

- Wagner, in: MüKoBGB, 9. Aufl. 2024, § 630g Rn. 1 ff.
- Katzenmeier, in: BeckOK BGB, Stand 2024, § 630g Rn. 1 ff.
- Spickhoff, in: Spickhoff, Medizinrecht, 4. Aufl. 2022, § 630g BGB Rn. 1 ff.
- Laufs/Katzenmeier/Lipp, Handbuch des Arztrechts, 8. Aufl. 2021, Kap. VI (Dokumentation und Einsichtsrecht)
- Bäcker, in: Kühling/Buchner, DSGVO/BDSG, 3. Aufl. 2020, Art. 15 DSGVO Rn. 1 ff.

### Rechtsprechung

1. BGH, Urt. v. 26.02.2013 – VI ZR 359/11 (Einsichtsrecht; restriktive Anwendung des therapeutischen Vorbehalts) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=26.02.2013&Aktenzeichen=VI+ZR+359/11)
2. BGH-Linie zur Erbeneinsicht und mutmaßlichem Willen des Verstorbenen `[unverifiziert – prüfen in juris]`
3. EuGH, Urt. v. 26.10.2023 – C-307/22, FT/DW (kostenfreie erste Kopie der Patientenakte nach Art. 15 III DSGVO) (https://curia.europa.eu/juris/document/document.jsf?docid=279125&doclang=DE)
4. OLG-Rspr. zu Bildaufnahmen / Röntgenaufnahmen / DICOM-Daten `[unverifiziert – prüfen in juris]`

## Ausgabeformat

```
GUTACHTEN / ANSPRUCHSSCHREIBEN — Akteneinsicht
Mandat:  <anonymisiert>
Behandler: <Klinik/Praxis>
Zeitraum: <…>

I.   Sachverhalt (knapp)
II.  Frage(n)
III. Kurzantwort
     – Anspruch dem Grunde nach: [ja / nein / teilweise]
     – Empfohlene Anspruchsgrundlage: [§ 630g BGB / Art. 15 DSGVO / beide]

IV.  Rechtliche Bewertung
     1. § 630g BGB
        a) Anspruchsinhaber (Patient / Erbe / Angehöriger)
        b) Vollständige Akte
        c) Verweigerungsgründe
           – therapeutischer Vorbehalt
           – Rechte Dritter
        d) Form (Einsicht / Kopie / elektronisch)
        e) Kosten
     2. Art. 15 DSGVO (parallel)
        – Frist Art. 12 III DSGVO
        – Kostenfreie erste Kopie Art. 15 III DSGVO
     3. Schnittstelle § 203 StGB / § 22 BDSG / Art. 9 DSGVO
     4. Bei Erbenanspruch: § 630g III BGB, mutmaßlicher Wille

V.   Empfehlung
     – Antragstellung
     – Frist
     – Eskalation (Aufsichtsbehörde, Klage AG/LG)

VI.  Risiken / offene Punkte
     🟢 / 🟡 / 🔴

VII. Quellenverzeichnis
```

## Risiken / typische Fehler

- **Pauschale Verweigerung „therapeutische Gründe"** ohne konkrete Begründung – trägt nicht (§ 630g I 2 BGB).
- **Verkennen der Anspruchskonkurrenz** § 630g BGB ↔ Art. 15 DSGVO – Art. 15 DSGVO ist idR günstiger (kostenfrei, Monatsfrist).
- **Ablehnung der Erbeneinsicht** mit pauschalem Hinweis auf § 203 StGB – § 630g III BGB ist gesetzliche Befugnis und schließt den Tatbestand aus.
- **Vergessen der Bildaufnahmen / DICOM-Daten** – „vollständig" umfasst auch Rohdaten.
- **Verweis auf 10-Jahres-Aufbewahrungsfrist § 10 MBO-Ä** als Vernichtungsargument – Mindestfrist, nicht Maximalfrist; im Hinblick auf § 199 II BGB (30 Jahre Höchstfrist) faktisch längere Aufbewahrung geboten.
- **Übersehen der Patientenverfügung** §§ 1827 ff. BGB n.F. (Schweigepflichtentbindung).

---
name: uwg-abmahnung-pruefung-borghei
title: /wettbewerbsrecht:uwg-abmahnung-pruefung
description: Prüfung einer wettbewerbsrechtlichen Abmahnung nach § 13 UWG aus Abmahner- und Abgemahnten-Perspektive – Aktivlegitimation §§ 8, 8b, formelle Anforderungen § 13 II, Aufwendungsersatz § 13 III, Vertragsstrafe § 13a, Rechtsmissbrauchsindizien § 8c. Use when Mandant eine UWG-Abmahnung erhalten hat oder eine Abmahnung gegen einen Wettbewerber prüfen / aussprechen will.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/wettbewerbsrecht/skills/uwg-abmahnung-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: consumer
language: de
---

# /wettbewerbsrecht:uwg-abmahnung-pruefung

## Zweck

Die wettbewerbsrechtliche Abmahnung nach § 13 UWG ist Tor zum Unterlassungsprozess und Voraussetzung des Aufwendungsersatzes (§ 13 III). Wirksam ist sie nur, wenn Aktivlegitimation, formelle Anforderungen und materieller UWG-Verstoß zusammentreffen — und sie darf nicht rechtsmissbräuchlich iSv § 8c UWG sein. Dieser Skill prüft beide Seiten: den Abmahner (Wirksamkeit, Kostenerstattung, Vertragsstrafe) und den Abgemahnten (Verteidigungsstrategie, modifizierte UE, negative Feststellungsklage).

## Eingaben

- Abmahnschreiben (Wortlaut der Beanstandung, geforderte Unterlassungserklärung, geforderter Aufwendungsersatz, Frist)
- Abmahnender: Mitbewerber oder Verband (mit Registereintrag)?
- konkrete geschäftliche Handlung des Abgemahnten (Werbung, AGB-Klausel, Impressum, Preisangabe, Kennzeichnung)
- Vorgeschichte (frühere Abmahnungen desselben Abmahners, Branchengewohnheit)
- Position des Mandanten: Abmahner oder Abgemahnter
- Fristlage (Erstkenntnis, Verjährung § 11 UWG)

## Sub-Agent-Architektur

Researcher liefert UWG-Statute (§§ 3 ff., 8 ff., 13, 13a, 8c), BGH-Rspr. zu Abmahnerfordernissen und Rechtsmissbrauch, sowie Kommentarstellen. Drafter prüft Wirksamkeit der Abmahnung in Gutachtenstil und entwirft je nach Mandantenseite: (a) Abmahnschreiben mit UE-Entwurf und Kostenrechnung, oder (b) modifizierte UE / Zurückweisungsschreiben / Schutzschrift-Vorbereitung. Reviewer prüft Fristen (insb. § 11 UWG-Verjährung) und § 8c-Indizien.

## Ablauf

### 1. Aktivlegitimation des Abmahners

Anspruchsberechtigt sind gem. § 8 III UWG:

1. **Mitbewerber** — konkretes Wettbewerbsverhältnis erforderlich (§ 2 I Nr. 4 UWG). Geringe Anforderungen, aber nicht jeder Marktteilnehmer.
2. **Qualifizierte Wirtschaftsverbände** (§ 8 III Nr. 2, § 8b UWG) — Eintragung in die Liste beim Bundesamt für Justiz erforderlich; mindestens 75 Unternehmer aus derselben Branche; sachliche/personelle Ausstattung; eingetragen iSv § 8b.
3. **Qualifizierte Einrichtungen / Verbraucherverbände** (§ 8 III Nr. 3) — Eintragung nach UKlaG.
4. **Industrie-, Handels- und Handwerkskammern** (§ 8 III Nr. 4).

Bei Verbänden: **Registereintragung zwingend abprüfen** (BAJ-Liste online).

### 2. Formelle Anforderungen § 13 II UWG

Die Abmahnung muss enthalten:

1. Name oder Firma des Abmahnenden und ggf. Vertretungsverhältnisse
2. Voraussetzungen der Anspruchsberechtigung nach § 8 III
3. Ob und in welcher Höhe Aufwendungsersatz geltend gemacht wird
4. konkrete Schilderung der Rechtsverletzung
5. Vertragsstrafenforderung erkennbar als geforderte Höhe

Fehlt eine dieser Angaben, ist der **Aufwendungsersatz nach § 13 III UWG ausgeschlossen** und der Abgemahnte hat ggf. Gegenanspruch auf Erstattung eigener Rechtsverteidigungskosten (§ 13 V UWG).

### 3. Materielle Anspruchsgrundlage (§ 8 I iVm § 3 ff. UWG)

Prüfungsreihenfolge im Lauterkeitsrecht (vgl. Köhler/Bornkamm/Feddersen, UWG, jeweils aktuell, Einl. Rn. 4 ff. `[unverifiziert – prüfen]`):

1. Anhang zu § 3 III UWG (Schwarze Liste — per-se-Verbot, keine Spürbarkeitsschwelle)
2. §§ 5, 5a, 5b UWG (Irreführung)
3. § 6 UWG (vergleichende Werbung)
4. § 7 UWG (unzumutbare Belästigung)
5. § 4 Nr. 1–4 UWG (Mitbewerberschutz)
6. § 4a UWG (aggressive Praktiken)
7. § 3a UWG (Rechtsbruch)
8. § 3 II UWG (Generalklausel)

### 4. Aufwendungsersatz § 13 III UWG

Erstattungsfähig sind die **erforderlichen Aufwendungen**:

- bei anwaltlicher Abmahnung: 1,3-Geschäftsgebühr VV 2300 RVG nach Gegenstandswert
- bei Verbänden mit eigener Rechtsabteilung: pauschalierte Kostenpauschale (Spruchpraxis idR 230–280 EUR)
- bei Mitbewerber-Eigenabmahnung ohne Anwalt: kein Aufwendungsersatz (§ 13 IV UWG)

Gegenstandswert: regelmäßig 5.000–50.000 EUR je nach Verstoß-Schwere; nicht maschinell auf 100.000 EUR setzen.

### 5. Rechtsmissbrauch § 8c UWG

Geltendmachung ist unzulässig, wenn sie unter Berücksichtigung der gesamten Umstände missbräuchlich ist (§ 8c I). Indizien des § 8c II (UWG-Novelle 2021):

1. Anspruchsgeltendmachung in erheblichem Umfang gegen verschiedene Schuldner, wenn die Geltendmachung in keinem Verhältnis zur Tätigkeit steht
2. **vereinbarte** oder **angesetzte** Vertragsstrafe **offensichtlich überhöht**
3. überhöhter Gegenstandswert
4. Vereinbarung einer Vertragsstrafe für Gleichartiges, obwohl eine Unterlassungserklärung schon ausreicht
5. Abmahnung ist offensichtlich auf Erzielung von Aufwendungsersatz/Vertragsstrafe gerichtet
6. Auswahl der Schuldner sachfremd

Rechtsfolge: Anspruchsausschluss + **Gegenanspruch des Abgemahnten** auf Ersatz der Verteidigungskosten (§ 8c II 2 UWG).

### 6. Reaktionsoptionen des Abgemahnten

| Option | Wann |
|---|---|
| **Vollständige UE abgeben** (mit Vertragsstrafe) | Verstoß klar, Wiederholungsgefahr-Beseitigung gewollt, Kostenrisiko begrenzen |
| **Modifizierte UE** (z. B. ohne Vorbehalt, mit eingeschränkter Reichweite, geringere Vertragsstrafe nach Hamburger Brauch) | Verstoß teilweise streitig, Kerntheorie problematisch |
| **Zurückweisung** (Abmahnung unbegründet / formal mangelhaft / rechtsmissbräuchlich) | Aktivlegitimation fehlt, § 13 II nicht eingehalten, § 8c-Indizien |
| **Negative Feststellungsklage** | Klärung des Nichtbestehens des Anspruchs erwünscht; Gerichtsstand § 32 ZPO |
| **Schutzschrift** beim Schutzschriftenregister | Drohende einstweilige Verfügung antizipiert |

Wiederholungsgefahr wird gem. h.M. nur durch **strafbewehrte** UE ausgeräumt (BGH, std. Rspr.) `[unverifiziert – prüfen in juris]`.

### 7. Vertragsstrafe § 13a UWG

Höhe muss **angemessen** sein (§ 13a I UWG). Faktoren: Art/Umfang des Verstoßes, Verschulden, wirtschaftliche Bedeutung. Bei Kleingewerbe / Erstverstoß: 2.500–5.100 EUR pro Verstoß üblich; bei größeren Unternehmen / Wiederholung: 10.000 EUR und mehr. Bei **erstmaligem Verstoß** und Kleinunternehmer kann gem. § 13a II UWG nicht ohne weiteres die volle Vertragsstrafe gefordert werden.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 8 UWG](https://www.gesetze-im-internet.de/uwg_2004/__8.html) (Unterlassungs- und Beseitigungsanspruch)
- [§ 8b UWG](https://www.gesetze-im-internet.de/uwg_2004/__8b.html) (Wirtschaftsverbände)
- [§ 8c UWG](https://www.gesetze-im-internet.de/uwg_2004/__8c.html) (Rechtsmissbrauch)
- [§ 11 UWG](https://www.gesetze-im-internet.de/uwg_2004/__11.html) (6-Monats-Verjährung)
- [§ 13 UWG](https://www.gesetze-im-internet.de/uwg_2004/__13.html) (Abmahnung, Aufwendungsersatz)
- [§ 13a UWG](https://www.gesetze-im-internet.de/uwg_2004/__13a.html) (Vertragsstrafe)
- [§ 242 BGB](https://www.gesetze-im-internet.de/bgb/__242.html) (Treu und Glauben)
- [§ 339 BGB](https://www.gesetze-im-internet.de/bgb/__339.html) (Vertragsstrafe — Verwirkung)
- [§ 32 ZPO](https://www.gesetze-im-internet.de/zpo/__32.html) (Gerichtsstand der unerlaubten Handlung)

### Kommentare

- Bornkamm, in: Köhler/Bornkamm/Feddersen, UWG, jeweils aktuell, § 13 UWG Rn. 1 ff.
- Feddersen, in: Köhler/Bornkamm/Feddersen, UWG, jeweils aktuell, § 8c UWG Rn. 1 ff.
- Goldmann, in: Harte-Bavendamm/Henning-Bodewig, UWG, 5. Aufl. 2021, § 13 UWG Rn. 1 ff.
- Sosnitza, in: Ohly/Sosnitza, UWG, 8. Aufl. 2023, § 13 UWG Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris]`)

1. BGH, Urt. v. 26.04.2018 – I ZR 248/16, GRUR 2018, 1166 – Abmahnaktion II (Rechtsmissbrauch)
2. BGH, Urt. v. 17.09.2015 – I ZR 92/14, GRUR 2016, 395 – Smartphone-Werbung (Hamburger Brauch)
3. BGH, Urt. v. 04.07.2019 – I ZR 149/18, GRUR 2019, 1071 – Umwelthilfe (Aktivlegitimation Verband)

## Ausgabeformat (Abgemahnten-Perspektive)

```
GUTACHTEN — Prüfung UWG-Abmahnung
Mandant: <Abgemahnter, Branche, Größenklasse>
Abmahner: <Name, ggf. Verband, BAJ-Listen-Stand>
Zugang: <Datum>, Frist: <Datum>

I. Sachverhalt (knapp)
II. Kurzantwort
    – Wirksamkeit der Abmahnung: [ja / formal mangelhaft / rechtsmissbräuchlich]
    – Empfehlung: [vollständige UE / modifizierte UE / Zurückweisung / Schutzschrift]

III. Rechtliche Bewertung
    1. Aktivlegitimation (§§ 8 III, 8b UWG)
    2. Formelle Anforderungen § 13 II UWG
    3. Materieller UWG-Verstoß
       a) Anhang § 3 III (Schwarze Liste)?
       b) §§ 5, 5a, 5b / 6 / 7 / 4 / 4a / 3a / 3 II UWG
    4. Aufwendungsersatz § 13 III UWG (Gegenstandswert, RVG-Berechnung)
    5. Rechtsmissbrauch § 8c UWG (Indizien-Katalog)
    6. Vertragsstrafe § 13a UWG (Angemessenheit)
    7. Verjährung § 11 UWG (Erstkenntnis-Daten)

IV. Reaktionsempfehlung
    – Entwurf modifizierte UE / Zurückweisungsschreiben:
      [zitierfähiger Block]

V. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>

VI. Wiedervorlagen
    – Reaktionsfrist Abmahner: <Datum>
    – Verjährung § 11 UWG: <Datum + 6 Monate ab Kenntnis>
    – ggf. Schutzschrift hinterlegt: <Datum>

VII. Quellenverzeichnis
```

## Beispiel (Auszug, Gutachtenstil)

> **2. Formelle Anforderungen § 13 II UWG.** Die Abmahnung des V. e. V. vom TT.MM.JJJJ enthält weder einen Hinweis auf die Eintragung in die Liste qualifizierter Wirtschaftsverbände (§ 13 II Nr. 2 iVm § 8b UWG) noch eine nachprüfbare Berechnung des angesetzten Aufwendungsersatzes (§ 13 II Nr. 3). Damit ist der Aufwendungsersatzanspruch nach § 13 III UWG ausgeschlossen; § 13 V UWG begründet zudem einen Gegenanspruch der Mandantin auf Ersatz der erforderlichen Aufwendungen zur Rechtsverteidigung. Empfehlung: Zurückweisung unter Hinweis auf § 13 II UWG und Vorbehalt der Geltendmachung des Gegenanspruchs.

## Risiken / typische Fehler

- **Aktivlegitimation eines Verbandes ungeprüft** — bei fehlender BAJ-Eintragung ist die gesamte Abmahnung unwirksam.
- **Wiederholungsgefahr durch UE ohne Vertragsstrafe ausräumen wollen** — Wiederholungsgefahr nur durch **strafbewehrte** UE ausgeräumt; Mandant bleibt klageexponiert.
- **Modifizierte UE mit zu enger Reichweite** — Kerntheorie: leichte Abweichungen unterfallen weiter der UE; zu enge Reichweite begründet erneut Wiederholungsgefahr.
- **§ 8c-Indizien übersehen** — bei Massenabmahnern (Verband mit unverhältnismäßiger Tätigkeit) Indizien-Katalog § 8c II Nr. 1 prüfen.
- **Verjährung § 11 UWG verpasst** — 6 Monate ab Kenntnis, deutlich kürzer als § 195 BGB.
- **Vertragsstrafe pauschal akzeptiert** — bei Erstverstoß / Kleinunternehmer § 13a II UWG einwenden.
- **Gegenstandswert hingenommen** — Streitwertbeschwerde / Hilfsantrag prüfen.

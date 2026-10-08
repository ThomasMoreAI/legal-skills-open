---
name: kritis-vorfallmeldung-borghei
title: /kritis-resilienz:kritis-vorfallmeldung
description: Vorfallmeldung nach § 18 KRITIS-Dachgesetz – Meldepflicht des Betreibers kritischer Anlagen gegenüber dem BBK unverzüglich, spätestens 24 Stunden nach Kenntnis, über die gemeinsame Meldestelle von BSI und BBK, Aktualisierung der Erstmeldung bei andauerndem Vorfall, ausführlicher Bericht spätestens einen Monat nach Kenntnis, Pflichtinhalte nach Abs. 2 mit Zahl und Anteil der Betroffenen, bisheriger und voraussichtlicher Dauer sowie betroffenem Gebiet, Unberührtheit sonstiger gesetzlicher Meldepflichten, Abgrenzung und Parallelität zur Cybervorfallmeldung nach dem BSIG/NIS2 und zur Datenschutzmeldung nach Art. 33 DSGVO sowie Bußgeldrisiko § 24. Use when ein Vorfall an einer kritischen Anlage eingetreten ist und die Meldelage zu klären oder eine Meldung zu entwerfen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/kritis-resilienz/skills/kritis-vorfallmeldung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: cybersecurity
language: de
---

# /kritis-resilienz:kritis-vorfallmeldung

## Zweck

Der Skill steuert die Meldung eines Vorfalls an einer kritischen Anlage unter Zeitdruck. Er klärt zuerst, **welche** Meldepflichten parallel laufen — KRITIS-DachG, BSIG/NIS2, DSGVO und sektorspezifische Pflichten sind eigenständig und verdrängen einander nicht — und liefert dann die Fristenkette und den Meldungsentwurf.

## Eingaben

- Beschreibung des Vorfalls: Art, Ursache soweit bekannt, betroffene Anlage und Dienstleistung
- **Zeitpunkt der Kenntnis** — nicht des Eintritts
- Auswirkungen: Zahl und Anteil der Betroffenen, betroffenes Gebiet, Dauer bisher und voraussichtlich
- Ob der Vorfall andauert
- Ob zugleich ein IT-Sicherheitsvorfall (BSIG/NIS2) oder eine Verletzung des Schutzes personenbezogener Daten (Art. 33 DSGVO) vorliegt
- Sektorspezifische Meldepflichten (EnWG, AtG, WHG, StörfallV, TKG, LuftSiG u. a.)
- Ob eine Bereichsausnahme nach § 4 Abs. 2 greift

## Sub-Agent-Architektur

Der Researcher beschafft § 18 KRITISDachG, die Verordnung nach § 18, das BSIG, Art. 33 DSGVO und die sektorspezifischen Meldenormen. Der Drafter erstellt die Meldelagekarte und den Meldungsentwurf. Der Reviewer rechnet die 24-Stunden- und die Monatsfrist nach, prüft die Pflichtinhalte des Abs. 2 und kontrolliert, dass keine parallele Meldepflicht übersehen wurde.

## Ablauf

### 1. Meldelage klären — welche Pflichten laufen parallel

**Dieser Schritt steht vor allem anderen.** § 18 Abs. 1 S. 4 KRITISDachG stellt ausdrücklich klar: **Meldepflichten aufgrund sonstiger gesetzlicher Vorgaben bleiben unberührt.**

| Regime | Auslöser | Empfänger | Frist |
|---|---|---|---|
| **§ 18 KRITISDachG** | **Vorfall** an einer kritischen Anlage (physisch, all-hazards) | **Bundesamt für Bevölkerungsschutz und Katastrophenhilfe (BBK)** über die gemeinsame Meldestelle von BSI und BBK | unverzüglich, **spätestens 24 Stunden** nach Kenntnis; ausführlicher Bericht **binnen eines Monats** |
| **BSIG / NIS2** | erheblicher **IT-Sicherheitsvorfall** | **BSI** | gestufte Fristen des BSIG `[unverifiziert – prüfen]` je Fassung |
| **Art. 33 DSGVO** | Verletzung des Schutzes **personenbezogener Daten** | Datenschutzaufsicht | 72 Stunden (`/datenschutzrecht:datenpanne-meldung`) |
| **Sektorrecht** | z. B. EnWG, WHG, StörfallV, TKG, LuftSiG | jeweilige Fachbehörde | jeweils gesondert |

Ein Sabotageakt an einem Umspannwerk, der zugleich die Leitwarte kompromittiert und Kundendaten offenlegt, löst **alle vier** Pflichten aus. Die Meldungen sind inhaltlich abzustimmen, aber getrennt zu erstatten.

**Vorschaltprüfung:** Für Betreiber, die unter eine Bereichsausnahme des [§ 4 Abs. 2 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__4.html) fallen — insbesondere DORA-Finanzunternehmen und den Sektor Informationstechnik und Telekommunikation —, gilt **§ 18 nicht**; ihre Meldepflichten folgen dann DORA bzw. dem BSIG.

### 2. Fristenkette des [§ 18 Abs. 1 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__18.html)

| Schritt | Frist | Adressat |
|---|---|---|
| **Erstmeldung** | **unverzüglich, spätestens 24 Stunden nach Kenntnis** | BBK über die gemeinsame Meldestelle von BSI und BBK |
| **Aktualisierung** | bei **andauerndem** Vorfall — die Erstmeldung ist zu aktualisieren | BBK |
| **Ausführlicher Bericht** | **spätestens einen Monat nach Kenntnis** des Vorfalls | BBK |

Die Frist läuft ab **Kenntnis**, nicht ab Eintritt des Vorfalls und nicht ab abgeschlossener Ursachenanalyse. „Unverzüglich" bedeutet ohne schuldhaftes Zögern; die 24 Stunden sind die **Höchstgrenze**, nicht der Regelzeitpunkt. Wer auf vollständige Aufklärung wartet, meldet zu spät — die Erstmeldung enthält nach Abs. 2 ausdrücklich nur die **zum Zeitpunkt verfügbaren** Informationen.

### 3. Pflichtinhalte der Meldung ([§ 18 Abs. 2 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__18.html))

Die Meldungen müssen die **zu ihrem Zeitpunkt verfügbaren** Informationen enthalten, die erforderlich sind, damit **Art, Ursache und mögliche — auch grenzüberschreitende — Auswirkungen und Folgen** des Vorfalls ermittelt und nachvollzogen werden können. Insbesondere anzugeben sind:

1. die **Anzahl und der Anteil** der von dem Vorfall Betroffenen,
2. die **bisherige und voraussichtliche Dauer** des Vorfalls,
3. das **betroffene Gebiet**.

Die Erstmeldung ist damit bewusst als Lagemeldung konzipiert. Unsicherheiten werden als solche gekennzeichnet und in der Aktualisierung nachgeführt — nicht durch Verzögerung der Meldung aufgelöst.

### 4. Grenzüberschreitende Auswirkungen

Abs. 2 nennt ausdrücklich **auch grenzüberschreitende** Auswirkungen. Betrifft der Vorfall Dienstleistungen in oder für andere Mitgliedstaaten, ist das in der Meldung darzustellen; für Einrichtungen von besonderer Bedeutung für Europa gelten zusätzlich [§ 9](https://www.gesetze-im-internet.de/kritisdachg/__9.html) und [§ 10 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__10.html).

### 5. Nachbereitung

- **[§ 19 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__19.html)** — Unterstützung der Betreiber durch die Behörden, auch freiwillige Angebote.
- **[§ 13 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__13.html)** — Der Vorfall ist in Risikoanalyse und Resilienzplan zurückzuspiegeln; Ziel Abs. 1 Nr. 4 (zügige Wiederherstellung) wird am realen Ereignis gemessen (`/kritis-resilienz:kritis-resilienzpflichten`).
- **[§ 21 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__21.html)** — Berichtspflichten.
- **[§ 20 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__20.html)** — Die Geschäftsleitung trägt Umsetzungs- und Überwachungspflicht; ein Meldeversäumnis ist zugleich ein Governance-Thema (`/kritis-resilienz:kritis-governance-haftung`).

### 6. Sanktionen ([§ 24 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__24.html))

Der Bußgeldkatalog des § 24 Abs. 1 knüpft an Registrierungs-, Anordnungs-, Audit- und Duldungspflichten an; die Rahmen reichen von **100.000 EUR** bis **1.000.000 EUR** (Abs. 2). Verwaltungsbehörde ist nach Abs. 3 in den Fällen des Abs. 1 Nr. 1 und Nr. 2 lit. a das **BBK**, im Übrigen die nach § 3 Abs. 2 S. 1 zuständige Behörde. Ob und in welchem Umfang ein Verstoß gegen die **Meldepflicht des § 18** bußgeldbewehrt ist, ist am geltenden Wortlaut des § 24 Abs. 1 zu prüfen und nicht zu unterstellen `[unverifiziert – prüfen]`.

## Deterministische Berechnung

Die 24-Stunden-Frist läuft **stundengenau ab Kenntnis** und kennt keine Wochenend- oder Feiertagsverschiebung. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik; der Kenntniszeitpunkt ist eine Tatsachenfeststellung und zu dokumentieren:

```bash
# § 18 Abs. 1 S. 1 KRITISDachG: ausführlicher Bericht binnen 1 Monat ab Kenntnis am 12.05.2026
python -m scripts.legal_calc.cli frist --ereignis 12.05.2026 --menge 1 --einheit monate --land BY

# Parallel: 72-Stunden-Frist des Art. 33 DSGVO ab Kenntnis
python -m scripts.legal_calc.cli frist --ereignis 12.05.2026 --menge 3 --einheit tage --land BY
```

Die 24-Stunden-Erstmeldung wird **nicht** kalendarisch gerechnet, sondern als Uhrzeit dokumentiert: Kenntnis am 12.05.2026 um 21:40 Uhr bedeutet Meldung spätestens am 13.05.2026 um 21:40 Uhr — und wegen „unverzüglich" regelmäßig deutlich früher.

## Quellen

### Statute

- [§ 4 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__4.html), [§ 9](https://www.gesetze-im-internet.de/kritisdachg/__9.html), [§ 10](https://www.gesetze-im-internet.de/kritisdachg/__10.html), [§ 13](https://www.gesetze-im-internet.de/kritisdachg/__13.html), [§ 18](https://www.gesetze-im-internet.de/kritisdachg/__18.html), [§ 19](https://www.gesetze-im-internet.de/kritisdachg/__19.html), [§ 20](https://www.gesetze-im-internet.de/kritisdachg/__20.html), [§ 21](https://www.gesetze-im-internet.de/kritisdachg/__21.html), [§ 24 KRITISDachG](https://www.gesetze-im-internet.de/kritisdachg/__24.html)
- [BSIG](https://www.gesetze-im-internet.de/bsig_2009/); Richtlinie (EU) 2022/2555 (NIS2) — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)
- Art. 33, 34 DSGVO — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- Richtlinie (EU) 2022/2557 (CER) — [EUR-Lex](https://eur-lex.europa.eu/eli/dir/2022/2557/oj)
- Verordnung (EU) 2022/2554 (DORA), Art. 19 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)
- Verordnung nach § 18 KRITISDachG `[unverifiziert – prüfen]`

### Kommentare und Literatur

- Kommentierungen zum KRITIS-Dachgesetz (Erscheinungsstand prüfen) `[unverifiziert – prüfen]`
- Gitter/Kipker, IT-Sicherheitsrecht (Meldepflichten im Vergleich).
- BBK und BSI, Hinweise zur gemeinsamen Meldestelle.

### Rechtsprechung

Zu § 18 KRITISDachG existiert **keine** Rechtsprechung. Für den Begriff „unverzüglich" ist auf die allgemeine Judikatur zu [§ 121 BGB](https://www.gesetze-im-internet.de/bgb/__121.html) zurückzugreifen; jede Entscheidung ist vor Verwendung zu verifizieren `[unverifiziert – prüfen]`.

## Ausgabeformat

```
KRITIS-VORFALLMELDUNG — <Betreiber / Anlage> — <Datum>

I.   Vorschaltprüfung
     Bereichsausnahme § 4 Abs. 2:  [greift — § 18 nicht anwendbar / greift nicht]

II.  Meldelage (parallele Pflichten)
     § 18 KRITISDachG → BBK:       [ja — Fristen unten / nein]
     BSIG / NIS2 → BSI:            [ja / nein]
     Art. 33 DSGVO → Aufsicht:     [ja — 72 h / nein]
     Sektorrecht:                  <Norm, Behörde, Frist>
     Hinweis: § 18 Abs. 1 S. 4 - sonstige Meldepflichten bleiben unberührt

III. Fristenkette § 18 Abs. 1
     Kenntnis am:                  <Datum, Uhrzeit>
     Erstmeldung spätestens:       <Datum, Uhrzeit>  (24 h; „unverzüglich" = früher)
     Andauernder Vorfall:          [ja — Aktualisierung / nein]
     Ausführlicher Bericht bis:    <Datum>  (1 Monat ab Kenntnis)

IV.  Pflichtinhalte § 18 Abs. 2
     Art des Vorfalls:             <…>
     Ursache (soweit bekannt):     <…>   [Unsicherheit gekennzeichnet]
     Nr. 1 Anzahl und Anteil der Betroffenen: <…>
     Nr. 2 bisherige / voraussichtliche Dauer: <…>
     Nr. 3 betroffenes Gebiet:     <…>
     Grenzüberschreitende Auswirkungen: [ja — Darstellung / nein]

V.   Nachbereitung
     Rückspiegelung in § 12 / § 13: <Risikoanalyse, Resilienzplan, Ziel Abs. 1 Nr. 4>
     Berichtspflichten § 21:       <…>
     Governance § 20:              <Dokumentation der Geschäftsleiterbefassung>

VI.  Sanktionsrisiko § 24
     Einschlägiger Tatbestand:     <am Wortlaut geprüft>
     Rahmen:                       <100.000 / 200.000 / 500.000 / 1.000.000 EUR>
     Zuständige Bußgeldbehörde:    [BBK / Sektorbehörde nach § 3 Abs. 2 S. 1]

VII. Risiko: 🟢 / 🟡 / 🔴 <Begründung>
VIII.Quellenverzeichnis
```

### Formulierungshilfe — Erstmeldung nach § 18 Abs. 1 KRITISDachG (Gerüst)

```
Erstmeldung eines Vorfalls nach § 18 Absatz 1 KRITIS-Dachgesetz

Betreiber:              <Name, Anschrift, Kontakt>
Kritische Anlage:       <Bezeichnung, Sektor, kritische Dienstleistung>
Registrierungs-Nr.:     <…>
Kenntnis des Vorfalls:  <Datum, Uhrzeit>
Meldung erstattet:      <Datum, Uhrzeit>

1. Art des Vorfalls
   <Kurzbeschreibung; als vorläufig gekennzeichnet>
2. Ursache
   <soweit bekannt; ausdrücklich als noch nicht abschließend geklärt>
3. Auswirkungen
   a) Anzahl und Anteil der Betroffenen: <…>
   b) Bisherige Dauer / voraussichtliche Dauer: <…>
   c) Betroffenes Gebiet: <…>
   d) Grenzüberschreitende Auswirkungen: <ja/nein, ggf. Staaten>
4. Ergriffene und geplante Maßnahmen
   <…>
5. Andauernder Vorfall
   [ja - Aktualisierung folgt / nein]
6. Weitere Meldungen
   <BSI nach BSIG / Datenschutzaufsicht nach Art. 33 DSGVO / Sektorbehörde>

Ansprechpartner rund um die Uhr: <Name, Telefon, E-Mail>
```

## Risiken / typische Fehler

- **Auf Ursachenklärung gewartet.** Die Erstmeldung enthält nach § 18 Abs. 2 nur die **verfügbaren** Informationen; die 24 Stunden laufen ab **Kenntnis**.
- **24 Stunden als Regelzeitpunkt behandelt.** § 18 Abs. 1 S. 1 verlangt **unverzüglich**; 24 Stunden sind die Höchstgrenze.
- **Nur an das BSI gemeldet.** Die KRITIS-Meldung geht an das **BBK** über die gemeinsame Meldestelle; die BSIG-Meldung bleibt daneben bestehen.
- **Parallele Meldepflichten übersehen.** § 18 Abs. 1 S. 4 lässt sonstige Pflichten ausdrücklich unberührt — DSGVO, BSIG und Sektorrecht sind getrennt zu erfüllen.
- **Aktualisierung bei andauerndem Vorfall unterlassen** (§ 18 Abs. 1 S. 2).
- **Monatsbericht vergessen.** § 18 Abs. 1 S. 3 verlangt ihn spätestens einen Monat nach Kenntnis.
- **Pflichtangaben des Abs. 2 unvollständig** — Anzahl und Anteil, Dauer und betroffenes Gebiet sind ausdrücklich benannt.
- **Grenzüberschreitende Auswirkungen nicht dargestellt.**
- **Bußgeldrisiko unterstellt statt am Wortlaut des § 24 Abs. 1 geprüft.**
- **Rechtsprechung erfunden.** Zu § 18 KRITISDachG gibt es keine; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.

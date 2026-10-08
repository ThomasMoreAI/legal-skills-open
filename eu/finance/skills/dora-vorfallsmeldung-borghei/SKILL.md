---
name: dora-vorfallsmeldung-borghei
title: /dora:dora-vorfallsmeldung
description: Klassifizierung und Meldung IKT-bezogener Vorfälle nach DORA – Behandlungsprozess Art. 17 DORA, Klassifizierung Art. 18 DORA, Meldung schwerwiegender Vorfälle Art. 19 DORA mit der Fristenkaskade 4h/72h/1 Monat. Use when ein Finanzunternehmen einen IKT-Vorfall klassifizieren und die Meldekette an die zuständige Behörde aufsetzen muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/dora/skills/dora-vorfallsmeldung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: finance
language: de
---

# /dora:dora-vorfallsmeldung

## Zweck

DORA verlangt von Finanzunternehmen einen geschlossenen Prozess zur **Behandlung, Klassifizierung und Meldung** IKT-bezogener Vorfälle. Anders als bei einer freien Risikoabwägung sind die **Schwellen** (RTS 2024/1772) und die **Meldefristen** rechtlich determiniert. Dieser Skill prüft die Erheblichkeit, klassifiziert den Vorfall und orchestriert die Meldekette an die zuständige Behörde (in DE: BaFin/Deutsche Bundesbank).

## Eingaben

- Art des Finanzunternehmens (CRR-Institut, Versicherer, KVG, Zahlungsinstitut, CASP)
- Vorfallsbeschreibung (Ausfall, Cyberangriff, Datenintegritätsverlust, Drittparteienvorfall)
- Zeitpunkt der **Entdeckung** des Vorfalls
- Betroffene kritische oder wichtige Funktionen, Anzahl betroffener Kunden, geografische Ausbreitung
- Dauer der Betriebsunterbrechung, Datenverlust, wirtschaftliche Auswirkungen
- Bereits informierte Stellen (BaFin, Bundesbank, andere Aufsicht)

## Sub-Agent-Architektur

Der Skill arbeitet in drei gedanklichen Rollen. Ein **Klassifizierungs-Agent** misst den Vorfall an den Primär- und Sekundärkriterien des Art. 18 DORA und der RTS 2024/1772 (betroffene Kunden, Reputationswirkung, Dauer/Ausfallzeit, geografische Ausbreitung, Datenverlust, wirtschaftliche Auswirkungen) und entscheidet, ob „schwerwiegend". Ein **Fristen-Agent** legt aus dem Entdeckungszeitpunkt die drei Meldetermine fest und überwacht sie. Ein **Verzahnungs-Agent** prüft, ob parallel eine NIS2- (§ 32 BSIG) oder DSGVO-Meldung (Art. 33 DSGVO) ausgelöst wird. Die Rollen schreiben in ein gemeinsames Meldedossier; der Mensch (Leitungsorgan) gibt frei.

## Ablauf

### 1. Behandlungsprozess (Art. 17 DORA)

- Erfassung, Protokollierung, Kategorisierung jedes IKT-Vorfalls nach dokumentiertem Verfahren.
- Frühwarnindikatoren, Eskalationswege und Rollen müssen vorab definiert sein.
- Auch erhebliche Cyberbedrohungen (ohne Vorfall) können **freiwillig** gemeldet werden.

### 2. Klassifizierung (Art. 18 DORA)

Ein Vorfall ist **schwerwiegend**, wenn die Schwellen der RTS 2024/1772 erreicht werden. Kriterien:

| Kriterium | Inhalt |
|---|---|
| Betroffene Kunden / Gegenparteien | Anzahl und Anteil |
| Dauer und Ausfallzeit | Stunden bis zur Wiederherstellung |
| Geografische Ausbreitung | grenzüberschreitend? |
| Datenverlust | Verfügbarkeit, Authentizität, Integrität, Vertraulichkeit |
| Auswirkung auf kritische Dienste | kritische oder wichtige Funktionen betroffen |
| Wirtschaftliche Auswirkungen | absolute/relative Verluste |

### 3. Erstmeldung — 4-Stunden-/24-Stunden-Frist (Art. 19 DORA)

- **Erstmeldung** schnellstmöglich, **spätestens 4 Stunden** nach Klassifizierung als schwerwiegend, in jedem Fall **spätestens 24 Stunden** nach Entdeckung.
- Adressat: zuständige Behörde (BaFin/Bundesbank über das Meldeportal).

### 4. Zwischenmeldung — 72 Stunden (Art. 19 DORA)

- **Zwischenmeldung** spätestens 72 Stunden nach der Erstmeldung mit aktualisiertem Status und ersten Auswirkungen.

### 5. Abschlussbericht — 1 Monat (Art. 19 DORA)

- **Abschlussbericht** spätestens einen Monat nach der jüngsten aktualisierten Zwischenmeldung: Ursachenanalyse (Root Cause), ergriffene Abhilfemaßnahmen, endgültige Auswirkungen.

### 6. Kundeninformation und Verzahnung

- Bei Auswirkungen auf finanzielle Interessen: **unverzügliche Kundeninformation** (Art. 19 DORA).
- Doppelmeldung prüfen: NIS2 (§ 32 BSIG), DSGVO (Art. 33 DSGVO), ggf. ZAC-Strafanzeige.

## Risiken / typische Fehler

- **4-Stunden-Frist** ab Klassifizierung übersehen — die Uhr läuft ab Einstufung als schwerwiegend, spätestens 24 h ab Entdeckung.
- **Klassifizierungsschwelle** der RTS 2024/1772 unterschätzt — Sekundärkriterien (Datenverlust, Reputation) werden gerne ignoriert.
- **Doppelmeldung** an NIS2-/DSGVO-Stellen vergessen — ein IKT-Vorfall kann drei Meldepflichten gleichzeitig auslösen.
- **Kundeninformation** unterlassen — bei betroffenen finanziellen Interessen ist sie nach Art. 19 DORA Pflicht, nicht Kür.

## Quellen

### Statute

- [VO (EU) 2022/2554 (DORA)](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) — Art. 17 DORA, Art. 18 DORA, Art. 19 DORA, Art. 23 DORA
- RTS 2024/1772 (Klassifizierung schwerwiegender IKT-bezogener Vorfälle)
- [Art. 33 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) — Verzahnung
- [§ 32 BSIG (n.F.)](https://www.gesetze-im-internet.de/bsig_2025/__32.html) — NIS2-Verzahnung

### Sekundärliteratur

- Maume/Maute/Fromberger, DORA-Kommentar
- BeckOK DORA (Online)

## Ausgabeformat

```
DORA-VORFALLSMELDUNG — <Vorfall-ID> — <Datum>

I.    Behandlungsprozess (Art. 17 DORA)   [erfasst / kategorisiert]
II.   Klassifizierung (Art. 18 DORA)
      Schwerwiegend?                       [Ja / Nein]  Erreichte Kriterien: <…>
III.  Meldekette (Art. 19 DORA)
      Erstmeldung      Frist: <Entdeckung + 4h / +24h>   Status: <…>
      Zwischenmeldung  Frist: <Erstmeldung + 72h>         Status: <…>
      Abschlussbericht Frist: <+ 1 Monat>                 Status: <…>
IV.   Kundeninformation                    [N/A / erforderlich]
V.    Verzahnung NIS2 / DSGVO              [§ 32 BSIG / Art. 33 DSGVO]

Eskalationspfad: <Leitungsorgan wann>
Nächster Schritt: <…>
```

---
name: strafbefehl-pruefung-borghei
title: /strafrecht:strafbefehl-pruefung
description: Prüfung eines erhaltenen Strafbefehls auf Einspruchswert – 2-Wochen-Frist nach § 410 StPO, formale Wirksamkeit, materielle Tatbestandsmäßigkeit, prozessuale Rechte (Akteneinsicht § 147 StPO), Hauptverhandlungsoption. Use when ein Mandant einen Strafbefehl erhalten hat und Einspruch bzw. Annahme zu entscheiden ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/strafrecht/skills/strafbefehl-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: criminal
language: de
---

# /strafrecht:strafbefehl-pruefung

## Zweck

Strafbefehle sind Verfahren ohne Hauptverhandlung — schnell, billig für die Justiz, oft ohne anwaltliche Aufklärung beim Beschuldigten. Die **2-Wochen-Einspruchsfrist** (§ 410 Abs. 1 StPO) läuft schnell ab. Dieser Skill prüft Einspruchschance, formale Wirksamkeit und Verteidigungslinien.

## Eingaben

- Datum der Zustellung
- Anklage (Tatvorwurf, Norm)
- Strafmaß (Geldstrafe in Tagessätzen, Fahrverbot, Eintragung)
- Akteneinsicht bereits beantragt?
- Vorstrafen?
- Bestehende anwaltliche Vertretung?

## Ablauf

### 1. Fristprüfung ([§ 410 Abs. 1 StPO](https://www.gesetze-im-internet.de/stpo/__410.html))

**2 Wochen ab Zustellung.** Bei Zustellung per Postzustellungsurkunde: Zustellungsdatum + 14 Tage. Wahrung der Frist durch:

- schriftlichen Einspruch beim erlassenen AG
- Telefax
- elektronisches Dokument nach § 32a StPO (beA)
- Mündlich bei Geschäftsstelle

Versäumte Frist → **Strafbefehl wird rechtskräftig** (§ 410 Abs. 3 StPO). Wiedereinsetzung in den vorigen Stand nur bei unverschuldeter Verhinderung (§§ 44 ff. StPO).

### 2. Formelle Wirksamkeit ([§ 409 StPO](https://www.gesetze-im-internet.de/stpo/__409.html))

- Hinreichender Tatverdacht?
- Antragsbefugnis StA?
- Erforderlicher Inhalt: Persönliche Daten, Tatvorwurf, Norm, Strafe, Beweise, Rechtsbehelfsbelehrung
- Zustellung wirksam?

### 3. Materielle Prüfung

- **Tatbestand** des § X StGB erfüllt?
- **Rechtswidrigkeit / Schuld** (Notwehr § 32, Notstand §§ 34/35, Verbotsirrtum § 17)
- **Beweislage** — wer hat was wann beobachtet? Reicht für Verurteilung im Hauptverfahren?

### 4. Akteneinsicht ([§ 147 StPO](https://www.gesetze-im-internet.de/stpo/__147.html))

**Zwingend vor Entscheidung.** Nur als verteidigender RA. Inhalt der Akte:

- Anzeige / Anlassdokumente
- Vernehmungsprotokolle
- Beweismittel
- Polizeiliche Berichte
- StA-Stellungnahme

### 5. Strategische Optionen

| Option | Wann |
|---|---|
| **Einspruch + Hauptverhandlung** | Beweislage schwach, Tatbestand zweifelhaft, hohe Tagessatzanzahl |
| **Einspruch + Verständigung § 257c StPO** | Beweislage stark, aber Strafmaß zu hoch |
| **Beschränkter Einspruch (§ 410 Abs. 2 StPO)** | Schuldspruch akzeptabel, aber Rechtsfolgen unangemessen |
| **Annahme (kein Einspruch)** | Beweislage erdrückend, Strafmaß angemessen, Hauptverhandlungsrisiko (höhere Strafe, Eintragung) überwiegt |

### 6. Folgen bei Annahme

- Strafbefehl wird zum **rechtskräftigen Urteil** (§ 410 Abs. 3 StPO)
- Eintragung im **Bundeszentralregister** (BZRG)
- Ggf. Eintragung im **Führungszeugnis** je nach Strafmaß (§ 32 BZRG)
- Strafmaß-Folgen: Beamtenstatus, ausländerrechtliche Konsequenzen, berufsrechtliche Folgen (Anwälte: § 14 BRAO)

### 7. Spezialfälle

- **Strafbefehl gegen Ausländer:** Konsequenzen für Aufenthaltstitel; §§ 53–55 AufenthG
- **Strafbefehl gegen Beamte:** § 24 BeamtStG; Disziplinarverfahren
- **Strafbefehl mit Berufsverbot § 70 StGB**
- **Strafbefehl mit Fahrverbot § 44 StGB** (häufig bei Verkehrsdelikten)

## Quellen

### Statute

- [§ 407 StPO](https://www.gesetze-im-internet.de/stpo/__407.html), [§ 408 StPO](https://www.gesetze-im-internet.de/stpo/__408.html), [§ 409 StPO](https://www.gesetze-im-internet.de/stpo/__409.html), [§ 410 StPO](https://www.gesetze-im-internet.de/stpo/__410.html), [§ 411 StPO](https://www.gesetze-im-internet.de/stpo/__411.html)
- [§ 147 StPO](https://www.gesetze-im-internet.de/stpo/__147.html) (Akteneinsicht)
- [§ 136 StPO](https://www.gesetze-im-internet.de/stpo/__136.html), [§ 136a StPO](https://www.gesetze-im-internet.de/stpo/__136a.html) (Belehrung)
- [§ 257c StPO](https://www.gesetze-im-internet.de/stpo/__257c.html) (Verständigung)
- §§ 32, 34, 35, 17 StGB (Rechtfertigung / Schuld)

### Kommentare

- Meyer-Goßner / Schmitt, StPO, 67. Aufl. 2024, § 410 Rn. 1 ff.
- Eschelbach, in: KK-StPO, 9. Aufl. 2023, § 410 Rn. 1 ff.
- Beulke, Strafprozessrecht, 15. Aufl. 2023, Rn. 530 ff.

### Rechtsprechung

- BGH, Beschl. v. 02.03.2011 – 2 StR 524/10, NStZ 2011, 522 (Voraussetzungen § 411) `[unverifiziert – prüfen]`
- BVerfG, Beschl. v. 19.03.2013 – 2 BvR 2628/10 (Verständigung) `[unverifiziert – prüfen]`

## Ausgabeformat

```
STRAFBEFEHL-PRÜFUNG — <Mandant-ID> — <Datum>
VERTRAULICH — STRAFVERTEIDIGUNG

I.    Frist
      Zustellung am: <…>
      Fristende: <…> ([🟢 noch offen / 🔴 abgelaufen])
II.   Formelle Wirksamkeit         [✅ / ⚠️]
III.  Materielle Bewertung
      Tatbestand <§ X StGB>:        [erfüllt / zweifelhaft]
      Rechtfertigung / Schuld:      [keine / Notwehr / …]
      Beweislage:                   [🟢 stark / 🟡 mittel / 🔴 schwach]
IV.   Strafmaß-Bewertung
      Tagessatzanzahl angemessen:   [✅ / ⚠️]
      Eintragungsfolgen:            <BZRG / Führungszeugnis>
V.    Optionen
      [ ] Voller Einspruch         Grund: <…>
      [ ] Beschränkter Einspruch   Grund: <…>
      [ ] Annahme                   Grund: <…>

Empfehlung: <…>
Nächster Schritt: <…>
Wiedervorlage: <Datum>
```

## Risiken / typische Fehler

- **Fristversäumnis** → Strafbefehl wird zum Urteil. Wiedereinsetzung selten.
- **Annahme ohne Akteneinsicht** → blinder Verzicht auf Verteidigung.
- **Einspruch + Hauptverhandlung mit höherer Strafe** als im Strafbefehl: möglich, aber kein Verschlechterungsverbot wie in der Berufung. Mandant aufklären!
- **Beschränkter Einspruch unrichtig formuliert** → wird als voller Einspruch behandelt oder verworfen.
- **Strafmaß-Folgen** (Beamtenstatus, ausländerrechtlich, Berufsrecht) unterschätzt.

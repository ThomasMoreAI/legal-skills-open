---
name: einspruch-finanzamt-borghei
title: /steuerrecht:einspruch-finanzamt
description: Prüfung und Einlegung des Einspruchs gegen einen Steuerbescheid – Statthaftigkeit § 347 AO, Einspruchsfrist von einem Monat § 355 AO, Form und Inhalt § 357 AO, Aussetzung der Vollziehung § 361 AO, Verböserungsgefahr § 367 Abs. 2 AO, Bekanntgabe und Fristberechnung § 122 AO. Use when gegen einen Steuerbescheid oder einen anderen Verwaltungsakt der Finanzbehörde Einspruch geprüft oder eingelegt werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/steuerrecht/skills/einspruch-finanzamt
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: tax
language: de
---

# /steuerrecht:einspruch-finanzamt

## Zweck

Der Einspruch ist der zentrale außergerichtliche Rechtsbehelf gegen Verwaltungsakte der Finanzbehörde. Er ist kostenfrei, hemmt die Bestandskraft des Bescheids und eröffnet eine vollständige Überprüfung des Falls. Wird die einmonatige Frist versäumt, wird der Bescheid bestandskräftig und ist nur noch über die engen Korrekturvorschriften (§§ 129, 164, 165, 172 ff. AO) angreifbar. Dieser Skill prüft Statthaftigkeit, Frist, Form und Erfolgsaussichten und formuliert Einspruch und Antrag auf Aussetzung der Vollziehung.

## Eingaben

- Bescheid (Art des Verwaltungsakts, Datum, Steuerart, Streitjahr, Aktenzeichen / Steuernummer)
- Bekanntgabedatum bzw. Aufgabe zur Post (für die Fristberechnung entscheidend)
- Streitpunkt (z. B. nicht anerkannte Werbungskosten, Schätzung, Versagung einer Vergünstigung)
- Vollziehung / Zahlungsfrist (drohende Nachzahlung, Fälligkeit, Vollstreckung)
- Neue Tatsachen oder Beweismittel (Belege, geänderte Sachverhaltsdarstellung)

## Sub-Agent-Architektur

Die Bearbeitung verläuft in Prosa über mehrere gedankliche Rollen. Ein Fristen-Prüfer rekonstruiert aus Bescheiddatum und Aufgabe zur Post die Bekanntgabe und die maßgebliche Monatsfrist. Ein Zulässigkeits-Prüfer klärt Statthaftigkeit, Form und Einspruchsbefugnis. Ein Vollstreckungs-Prüfer bewertet die Notwendigkeit eines Antrags auf Aussetzung der Vollziehung. Ein Strategie-Prüfer wägt Erfolgsaussichten gegen die Gefahr einer Verböserung und entscheidet über Begründungstiefe und Rücknahme. Die Rollen arbeiten denselben Sachverhalt schrittweise ab; ihre Ergebnisse fließen in das Ausgabeformat.

## Ablauf

### 1. Statthaftigkeit ([§ 347 AO](https://www.gesetze-im-internet.de/ao_1977/__347.html))

- Statthaft gegen Verwaltungsakte in Abgabenangelegenheiten, auf die die AO Anwendung findet (§ 347 Abs. 1 AO).
- Erfasst werden insbesondere Steuerbescheide, Feststellungsbescheide, Haftungsbescheide, Ablehnungen und sonstige Verwaltungsakte der Finanzbehörde.
- Abzugrenzen vom außergerichtlichen Rechtsbehelf gegen reine Realakte oder gegen Akte anderer Behörden.
- Der Einspruch ist auch bei Untätigkeit der Behörde statthaft (§ 347 Abs. 1 S. 2 AO).

### 2. Einspruchsfrist ([§ 355 AO](https://www.gesetze-im-internet.de/ao_1977/__355.html)) und Bekanntgabe ([§ 122 AO](https://www.gesetze-im-internet.de/ao_1977/__122.html))

- Der Einspruch ist innerhalb **eines Monats** nach Bekanntgabe des Verwaltungsakts einzulegen (§ 355 Abs. 1 AO). Diese **Monatsfrist** ist die maßgebliche **Einspruchsfrist**.
- **Bekanntgabe** schriftlicher Verwaltungsakte durch die Post: Bei Übermittlung im Inland gilt der Bescheid am vierten Tag nach Aufgabe zur Post als bekanntgegeben (§ 122 Abs. 2 Nr. 1 AO; Bekanntgabefiktion, seit 01.01.2025 vier Tage – zuvor drei Tage). Fällt dieser Tag auf Samstag, Sonntag oder Feiertag, verschiebt er sich auf den nächsten Werktag.
- Elektronische Bekanntgabe: § 122a AO bzw. § 122 Abs. 2a AO mit entsprechender Fiktion.
- Fristberechnung nach §§ 108 AO, 187 ff. BGB: Beginn mit Ablauf des Bekanntgabetags, Ende mit Ablauf des Tages des Folgemonats, der dem Bekanntgabetag entspricht; Verschiebung bei Wochenende/Feiertag (§ 108 Abs. 3 AO).
- Bei unterbliebener oder unrichtiger Rechtsbehelfsbelehrung verlängert sich die Frist auf ein Jahr (§ 356 Abs. 2 AO).
- Versäumte Frist: Prüfung der Wiedereinsetzung in den vorigen Stand (§ 110 AO).

### 3. Form und Inhalt ([§ 357 AO](https://www.gesetze-im-internet.de/ao_1977/__357.html))

- **Form**: schriftlich, elektronisch oder zur Niederschrift bei der Behörde (§ 357 Abs. 1 AO).
- Der Einspruch muss den angefochtenen Verwaltungsakt bezeichnen; eine ausdrückliche Bezeichnung als „Einspruch" ist nicht erforderlich, wenn das Begehren erkennbar ist (§ 357 Abs. 1 S. 4, Abs. 3 AO).
- Adressat: die Behörde, die den Verwaltungsakt erlassen hat; auch Einlegung bei einer anderen Behörde ist fristwahrend (§ 357 Abs. 2 AO).
- Begründung ist nicht Zulässigkeitsvoraussetzung, aber strategisch geboten.

### 4. Einspruchsbefugnis und Beschwer

- **Einspruchsbefugnis** nur, wer geltend macht, durch den Verwaltungsakt beschwert zu sein (§ 350 AO).
- Bei Null-Bescheiden fehlt regelmäßig die Beschwer; Ausnahme bei bindenden Besteuerungsgrundlagen.
- Bei Feststellungsbescheiden: gesonderte Befugnisregelung (§ 352 AO).

### 5. Aussetzung der Vollziehung ([§ 361 AO](https://www.gesetze-im-internet.de/ao_1977/__361.html))

- Der Einspruch hat **keine** aufschiebende Wirkung; die Steuer bleibt fällig und vollstreckbar (§ 361 Abs. 1 AO).
- Auf Antrag soll die **Aussetzung der Vollziehung** gewährt werden bei **ernstlichen Zweifeln** an der Rechtmäßigkeit oder bei unbilliger, nicht durch überwiegende öffentliche Interessen gebotener Härte (§ 361 Abs. 2 AO).
- Antrag bei der Finanzbehörde; bei Ablehnung Antrag beim Finanzgericht (§ 69 FGO).
- Aussetzungszinsen (§ 237 AO) beachten, falls der Einspruch erfolglos bleibt.

### 6. Verböserungsgefahr ([§ 367 Abs. 2 AO](https://www.gesetze-im-internet.de/ao_1977/__367.html)) und Rücknahme ([§ 362 AO](https://www.gesetze-im-internet.de/ao_1977/__362.html))

- Die Finanzbehörde entscheidet über den Einspruch in vollem Umfang erneut – Gesamtaufrollung (§ 367 Abs. 2 S. 1 AO; vgl. § 367 AO).
- Daraus folgt die Gefahr einer **Verböserung**: Der Bescheid kann auch zum Nachteil des Einspruchsführers geändert werden, jedoch erst nach vorherigem Hinweis und Gelegenheit zur Äußerung (§ 367 Abs. 2 S. 2 AO).
- Reaktion auf einen Verböserungshinweis: **Rücknahme** des Einspruchs nach § 362 AO, solange noch keine Einspruchsentscheidung ergangen ist. Die Rücknahme lässt den ursprünglichen Bescheid bestandskräftig werden.
- Strategische Abwägung vor Einlegung: Wie hoch ist das Risiko, dass die Gesamtaufrollung andere, bisher günstige Punkte aufdeckt?

### 7. Ergebnis und Antragsformulierung

- Zusammenführung von Frist, Form, Befugnis und Erfolgsaussicht zu einer Empfehlung.
- Formulierung des Einspruchs mit Bezeichnung des Verwaltungsakts, Antrag und Begründung.
- Gegebenenfalls gesonderter Antrag auf Aussetzung der Vollziehung mit Darlegung der ernstlichen Zweifel.

## Risiken

- **Einspruchsfrist verpasst** – die Monatsfrist ist nicht verlängerbar; ohne Wiedereinsetzung (§ 110 AO) wird der Bescheid bestandskräftig.
- **Bekanntgabe falsch berechnet** – Bekanntgabefiktion (seit 2025 vier Tage) und Verschiebung auf Werktage übersehen; Aufgabe zur Post statt Zugang maßgeblich.
- **Aussetzung der Vollziehung nicht beantragt** – trotz Einspruch droht Vollstreckung der Nachzahlung; AdV ist gesondert zu beantragen.
- **Verböserung unterschätzt** – Gesamtaufrollung nach § 367 Abs. 2 AO kann zu höherer Steuer führen; Rücknahme nach § 362 AO nur bis zur Einspruchsentscheidung möglich.
- **Einspruchsbefugnis fehlt** – mangelnde Beschwer (z. B. Null-Bescheid) macht den Einspruch unzulässig.
- **Form verfehlt** – Verwaltungsakt nicht hinreichend bezeichnet oder Einspruch bei unzuständiger Stelle ohne Fristwahrung.

## Ausgabeformat

```
EINSPRUCH — Prüfung — <Mandant> — <Datum>

I.    Angefochtener Verwaltungsakt
      Art / Steuerart:                <ESt-Bescheid / …>
      Bescheiddatum:                  <…>
      Aufgabe zur Post:               <…>
      Bekanntgabe (§ 122 AO):         <Datum + Fiktion>

II.   Frist
      Einspruchsfrist (§ 355 AO):     <Monatsfrist — Fristende>
      Rechtsbehelfsbelehrung:         [ordnungsgemäß / fehlerhaft → 1 Jahr]
      Status:                         [offen / abgelaufen → § 110 AO]

III.  Zulässigkeit
      Statthaftigkeit (§ 347 AO):     [✓]
      Form (§ 357 AO):                [schriftlich / elektronisch / Niederschrift]
      Einspruchsbefugnis (§ 350 AO):  [Beschwer ✓ / fraglich]

IV.   Vollziehung
      Nachzahlung / Fälligkeit:       <EUR / Datum>
      AdV (§ 361 AO):                 [beantragt — ernstliche Zweifel: …]

V.    Erfolgsaussicht / Strategie
      Streitpunkt:                    <…>
      Verböserungsrisiko (§ 367 AO):  [keines / niedrig / mittel / hoch]
      Rücknahmeoption (§ 362 AO):     <…>

VI.   Antrag
      <Einspruch + Begründung + ggf. AdV-Antrag>
```

## Quellen

### Statute

- [§ 347 AO](https://www.gesetze-im-internet.de/ao_1977/__347.html) (Statthaftigkeit des Einspruchs)
- [§ 350 AO](https://www.gesetze-im-internet.de/ao_1977/__350.html) (Einspruchsbefugnis / Beschwer)
- [§ 355 AO](https://www.gesetze-im-internet.de/ao_1977/__355.html) (Einspruchsfrist), [§ 356 AO](https://www.gesetze-im-internet.de/ao_1977/__356.html) (Rechtsbehelfsbelehrung)
- [§ 357 AO](https://www.gesetze-im-internet.de/ao_1977/__357.html) (Einlegung des Einspruchs)
- [§ 361 AO](https://www.gesetze-im-internet.de/ao_1977/__361.html) (Aussetzung der Vollziehung)
- [§ 362 AO](https://www.gesetze-im-internet.de/ao_1977/__362.html) (Rücknahme), [§ 367 AO](https://www.gesetze-im-internet.de/ao_1977/__367.html) (Entscheidung, Gesamtaufrollung)
- [§ 122 AO](https://www.gesetze-im-internet.de/ao_1977/__122.html) (Bekanntgabe), [§ 108 AO](https://www.gesetze-im-internet.de/ao_1977/__108.html), [§ 110 AO](https://www.gesetze-im-internet.de/ao_1977/__110.html) (Wiedereinsetzung)
- [§ 69 FGO](https://www.gesetze-im-internet.de/fgo/__69.html) (AdV beim Finanzgericht)

### Verwaltungsanweisungen

- AEAO (Anwendungserlass zur Abgabenordnung), zu §§ 347 ff., § 122 AO

---
name: bauliche-veraenderung-borghei
title: /wohnungseigentumsrecht:bauliche-veraenderung
description: Einordnung einer baulichen Veränderung im Wohnungseigentum nach der WEMoG-Reform – Gestattungsbeschluss mit einfacher Mehrheit § 20 Abs. 1 WEG, privilegierter Anspruch auf Barrierefreiheit, E-Mobilität, Einbruchschutz, Glasfaser und Steckersolargeräte § 20 Abs. 2 WEG, Zustimmung Beeinträchtigter § 20 Abs. 3 WEG, Kostenverteilung § 21 WEG. Use when eine geplante bauliche Maßnahme eines Wohnungseigentümers auf Beschlusserfordernis, privilegierten Anspruch und Kostentragung geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/wohnungseigentumsrecht/skills/bauliche-veraenderung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /wohnungseigentumsrecht:bauliche-veraenderung

## Zweck

Mit dem Wohnungseigentumsmodernisierungsgesetz (**WEMoG**, in Kraft seit 01.12.2020) wurde das Recht der baulichen Veränderung grundlegend umgebaut. Unter dem alten § 22 WEG bedurfte eine bauliche Veränderung im Grundsatz der Zustimmung aller beeinträchtigten Eigentümer — faktisch oft Allstimmigkeit. Seit der Reform gilt: Über **jede** bauliche Veränderung entscheidet die Gemeinschaft durch **Gestattungsbeschluss** mit **einfache Mehrheit** ([§ 20 Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__20.html)).

Daneben hat das WEMoG **privilegierte Maßnahmen** geschaffen, auf die der einzelne Eigentümer einen Anspruch hat ([§ 20 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__20.html)). Dieser Skill ordnet eine geplante Maßnahme ein, bestimmt die nötige Mehrheit, prüft den privilegierten Anspruch sowie seine Grenzen und klärt die Kostenverteilung ([§ 21 WEG](https://www.gesetze-im-internet.de/woeigg/__21.html)).

## Eingaben

- geplante Maßnahme (genaue Beschreibung, Ort am Gemeinschafts- oder Sondereigentum)
- Antragsteller (einzelner Eigentümer / mehrere / Verwalter)
- fällt die Maßnahme unter eine privilegierte Kategorie (Barrierefreiheit, E-Mobilität, Einbruchschutz, Glasfaser, Steckersolar)?
- Beeinträchtigung anderer Eigentümer (optisch, baulich, Nutzung)
- Kosten und wer sie zu tragen bereit ist
- bestehende Vereinbarungen / Gemeinschaftsordnung / frühere Beschlüsse

## Sub-Agent-Architektur

Researcher liefert die Normfassung der §§ 20, 21 WEG nach WEMoG und ordnet die Maßnahme den privilegierten Kategorien zu. Drafter erstellt die Einordnung samt Beschlussvorschlag und Kostenfolge. Reviewer prüft Mehrheitserfordernis, Grenzen des § 20 Abs. 4 WEG und Schlüssigkeit der Kostenverteilung.

## Ablauf

### 1. Einordnung: Erhaltung oder bauliche Veränderung?

Zuerst trennen: Eine **Erhaltungsmaßnahme** (Instandhaltung/Instandsetzung, § 19 Abs. 2 Nr. 2 WEG) folgt anderen Regeln und ist Gemeinschaftsaufgabe. Eine **bauliche Veränderung** ist jede auf Dauer angelegte gegenständliche Umgestaltung des Gemeinschaftseigentums, die über die ordnungsmäßige Erhaltung hinausgeht (z. B. Wallbox, Außenaufzug, Balkonkraftwerk, Markise). Nur Letztere fällt unter § 20 WEG.

### 2. Gestattungsbeschluss mit einfacher Mehrheit (§ 20 Abs. 1 WEG)

Bauliche Veränderungen werden **durch Beschluss gestattet**. Es genügt die **einfache Mehrheit** der abgegebenen Stimmen in der Eigentümerversammlung — die frühere Allstimmigkeit des alten § 22 WEG ist entfallen. Der Beschluss heißt **Gestattungsbeschluss**: Er erlaubt dem antragstellenden Eigentümer die Maßnahme; ohne ihn (oder ohne Zustimmung nach Abs. 3) ist die Maßnahme nicht gedeckt.

### 3. Privilegierter Anspruch (§ 20 Abs. 2 WEG)

Unabhängig vom freien Ermessen der Mehrheit kann **jeder Eigentümer angemessene bauliche Veränderungen verlangen**, die einer der fünf **privilegierte Maßnahmen** dienen:

| Nr. | Privilegierte Maßnahme | Beispiel |
|---|---|---|
| 1 | **Barrierefreiheit** (Gebrauch durch Menschen mit Behinderungen) | Rampe, Treppenlift, Türverbreiterung |
| 2 | **E-Mobilität** — Laden elektrisch betriebener Fahrzeuge | Wallbox/Ladepunkt in der Tiefgarage |
| 3 | **Einbruchschutz** | Sicherheitstür, Zusatzschlösser, Kamera am Zugang |
| 4 | **Glasfaseranschluss** | Glasfaser-Hausanschluss / Verkabelung |
| 5 | **Steckersolargeräte** (Stromerzeugung) | Balkonkraftwerk |

**Steckersolargeräte** sind die 2024 ergänzte fünfte privilegierte Maßnahme — diese Kategorie nicht übersehen. Liegt eine privilegierte Maßnahme vor, besteht ein **Anspruch dem Grunde nach**; die Gemeinschaft kann das „Ob" nicht ablehnen. Über die **Art der Durchführung** (das „Wie": Ausführung, Standort, ausführende Firma, optische Gestaltung) **entscheidet die Gemeinschaft durch Beschluss** nach billigem Ermessen.

### 4. Zustimmung Beeinträchtigter und Grenzen (§ 20 Abs. 3 und Abs. 4 WEG)

Unabhängig von Abs. 1 und Abs. 2 ist eine bauliche Veränderung zulässig, wenn **alle Eigentümer, deren Rechte über das in § 14 Abs. 1 Nr. 1 WEG bestimmte Maß hinaus beeinträchtigt werden, zustimmen** ([§ 20 Abs. 3 WEG](https://www.gesetze-im-internet.de/woeigg/__20.html)).

Grenzen nach [§ 20 Abs. 4 WEG](https://www.gesetze-im-internet.de/woeigg/__20.html): Eine Maßnahme darf **nicht beschlossen oder verlangt** werden, wenn sie

- die Wohnanlage **grundlegende Umgestaltung** (grundlegend umgestaltet) — d. h. ihren Charakter wesentlich verändert, oder
- einen Eigentümer **gegenüber anderen unbillig benachteiligt**.

Diese Schranke gilt auch für privilegierte Maßnahmen nach Abs. 2: Der Anspruch endet, wo die Maßnahme die Anlage grundlegend umgestaltet oder unbillig benachteiligt.

### 5. Kostenverteilung (§ 21 WEG)

Grundregel ([§ 21 WEG](https://www.gesetze-im-internet.de/woeigg/__21.html)): Wer die bauliche Veränderung **verlangt oder ihr zustimmt**, trägt die **Kosten** und ist allein **nutzungsberechtigt** (§ 21 Abs. 1 WEG). Die **Kostenverteilung** weicht damit von den Erhaltungskosten ab.

Ausnahmen (§ 21 Abs. 2 WEG): Die Kosten tragen **alle** Eigentümer, wenn

- die Maßnahme mit **mehr als zwei Dritteln** der abgegebenen Stimmen **und** der Hälfte der Miteigentumsanteile beschlossen wurde (Nr. 1), es sei denn, sie ist mit unverhältnismäßigen Kosten verbunden; oder
- sich die Kosten innerhalb eines **angemessenen Zeitraums amortisieren** (Nr. 2).

Wer die Kosten trägt, dem gebührt der Nutzen (§ 21 Abs. 3 WEG); spätere Nutzer können nach § 21 Abs. 4 WEG gegen Ausgleich teilhaben.

### 6. Beschlussvorschlag

Drafter formuliert einen abstimmungsreifen Beschlussantrag: Gegenstand der Maßnahme, Ausführung („Wie"), Kostenträger, Nutzungszuordnung und ggf. Unterhaltspflicht.

### 7. Ergebnis

Zusammenfassung: Einordnung (Erhaltung/bauliche Veränderung), erforderliche Mehrheit, privilegierter Anspruch ja/nein, Grenzen (§ 20 Abs. 4 WEG), Kostenfolge (§ 21 WEG), Beschlussvorschlag.

## Risiken / typische Fehler

- **Allstimmigkeit angenommen** — veraltet. Seit WEMoG genügt für die Gestattung die einfache Mehrheit (§ 20 Abs. 1 WEG).
- **„Ob" und „Wie" verwechselt** — bei privilegierten Maßnahmen besteht ein Anspruch auf das „Ob"; nur über die Art der Durchführung beschließt die Gemeinschaft.
- **Steckersolargeräte vergessen** — Balkonkraftwerke sind seit 2024 ausdrücklich privilegiert.
- **Grenze § 20 Abs. 4 WEG übersehen** — auch privilegierte Maßnahmen scheitern an grundlegender Umgestaltung oder unbilliger Benachteiligung.
- **Kosten falsch verteilt** — wer verlangt/zustimmt, zahlt grundsätzlich allein (§ 21 Abs. 1 WEG); nur die Ausnahmen des § 21 Abs. 2 WEG verlagern die Kosten auf alle.
- **Beschluss zu unbestimmt** — Standort, Ausführung und Unterhalt müssen geregelt sein, sonst ist der Beschluss anfechtbar.

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 20 WEG](https://www.gesetze-im-internet.de/woeigg/__20.html) (bauliche Veränderungen — Gestattungsbeschluss Abs. 1, privilegierte Maßnahmen Abs. 2, Zustimmung Abs. 3, Grenzen Abs. 4)
- [§ 21 WEG](https://www.gesetze-im-internet.de/woeigg/__21.html) (Nutzungen und Kosten bei baulichen Veränderungen)
- [§ 19 WEG](https://www.gesetze-im-internet.de/woeigg/__19.html) (Verwaltung und ordnungsmäßige Erhaltung — Abgrenzung)
- [§ 14 WEG](https://www.gesetze-im-internet.de/woeigg/__14.html) (Pflichten der Eigentümer — Maßstab der Beeinträchtigung)

### Kommentare

- Hügel/Elzer, WEG, aktuelle Aufl., § 20 (bauliche Veränderungen nach WEMoG)
- Bärmann/Dötsch, WEG, aktuelle Aufl., §§ 20, 21
- Jennißen, WEG, aktuelle Aufl., § 21 (Kostenverteilung)

### Rechtsprechung (`[unverifiziert – prüfen in Beck-Online/juris]`)

Zur post-WEMoG-Rechtslage liegt noch wenig gefestigte höchstrichterliche Rechtsprechung vor. Jede konkrete Entscheidung vor Verwendung verifizieren — kein Aktenzeichen ohne Prüfung zitieren `[unverifiziert – prüfen]`.

## Ausgabeformat

```
EINORDNUNG BAULICHE VERÄNDERUNG (§§ 20, 21 WEG, post-WEMoG)

1. Maßnahme: <Beschreibung>
2. Einordnung: [ ] Erhaltung  [ ] bauliche Veränderung
3. Privilegiert (§ 20 Abs. 2 WEG)?
   [ ] Barrierefreiheit [ ] E-Mobilität [ ] Einbruchschutz
   [ ] Glasfaser        [ ] Steckersolargeräte   [ ] keine
4. Erforderliche Mehrheit:
   - Gestattungsbeschluss § 20 Abs. 1 WEG: einfache Mehrheit
   - Anspruch dem Grunde nach (falls privilegiert): ja/nein
   - „Wie" durch Beschluss der Gemeinschaft
5. Grenzen (§ 20 Abs. 4 WEG):
   - grundlegende Umgestaltung? ja/nein
   - unbillige Benachteiligung? ja/nein
6. Kostenverteilung (§ 21 WEG):
   - Grundsatz: Antragsteller/Zustimmende tragen Kosten allein
   - Ausnahme Abs. 2 (>2/3 + ½ MEA / Amortisation)? ja/nein
7. Beschlussvorschlag:
   <abstimmungsreifer Antrag: Gegenstand, Ausführung, Kostenträger, Nutzung>

Hinweis: Rechtsprechung [unverifiziert – prüfen].
```

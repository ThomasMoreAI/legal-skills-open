---
name: gesetzliche-erbfolge-borghei
title: /erbrecht:gesetzliche-erbfolge
description: Bestimmung der gesetzlichen Erbfolge und der Erbquoten im deutschen Erbrecht – Ordnungssystem §§ 1924–1930 BGB, Repräsentations- und Eintrittsprinzip, Ehegattenerbrecht § 1931 BGB, güterstandsabhängige Erhöhung § 1371 BGB (Zugewinngemeinschaft), Verwandte der ersten bis dritten Ordnung. Use when bei einem Erbfall ohne (wirksames) Testament die gesetzlichen Erben und ihre Quoten zu bestimmen sind.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/erbrecht/skills/gesetzliche-erbfolge
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: trusts-and-estates
language: de
---

# /erbrecht:gesetzliche-erbfolge

## Zweck

Liegt kein wirksames Testament und kein Erbvertrag vor, bestimmt das Gesetz, wer Erbe wird und zu welcher Quote. Das deutsche Erbrecht ordnet die Verwandten nach Ordnungen (§§ 1924–1930 BGB) und stellt den überlebenden Ehegatten mit einer eigenen, güterstandsabhängigen Quote daneben (§§ 1931, 1371 BGB). Dieser Skill bestimmt die gesetzlichen Erben systematisch und berechnet ihre Erbquoten.

## Eingaben

- Erblasser (Todeszeitpunkt, letzter gewöhnlicher Aufenthalt)
- Überlebender Ehegatte vorhanden? (ja / nein; bestehende, nicht geschiedene Ehe)
- Güterstand (Zugewinngemeinschaft / Gütertrennung / Gütergemeinschaft; Ehevertrag?)
- Lebende Verwandte nach Ordnungen (Abkömmlinge; Eltern und deren Abkömmlinge; Großeltern und deren Abkömmlinge)
- Vorversterbensfälle (vorverstorbene Kinder, Geschwister etc. samt deren eigenen Abkömmlingen)
- Bestand eines wirksamen Testaments / Erbvertrags?

## Sub-Agent-Architektur

Der Skill arbeitet als Prosa-Pipeline in zwei gedanklichen Schritten. Ein erster Durchgang ermittelt rein verwandtschaftlich die berufene Ordnung und verteilt innerhalb dieser nach Stämmen (Repräsentations- und Eintrittsprinzip). Ein zweiter Durchgang legt das Ehegattenerbrecht daneben und korrigiert die Quote um die güterstandsabhängige Erhöhung. Beide Schritte sind getrennt zu dokumentieren, damit die Quotenbildung nachvollziehbar bleibt; bei komplexen Stammbäumen empfiehlt sich eine tabellarische Aufstellung je Stamm vor der Endquote.

## Ablauf

### 1. Kein wirksames Testament prüfen

Gesetzliche Erbfolge greift nur, soweit keine wirksame Verfügung von Todes wegen besteht (oder soweit sie den Nachlass nicht erschöpft). Liegt ein Testament/Erbvertrag vor, zunächst dessen Wirksamkeit klären (siehe `/erbrecht:testament-pruefung`). Nur bei Unwirksamkeit oder Lücke gilt das Folgende.

### 2. Ordnungen bestimmen

| Ordnung | Erben | Norm |
|---|---|---|
| Erste Ordnung | Abkömmlinge des Erblassers (Kinder, Enkel, …) | [§ 1924 BGB](https://www.gesetze-im-internet.de/bgb/__1924.html) |
| Zweite Ordnung | Eltern des Erblassers und deren Abkömmlinge (Geschwister, Neffen/Nichten) | [§ 1925 BGB](https://www.gesetze-im-internet.de/bgb/__1925.html) |
| Dritte Ordnung | Großeltern und deren Abkömmlinge (Onkel/Tanten, Cousins) | [§ 1926 BGB](https://www.gesetze-im-internet.de/bgb/__1926.html) |

**Vorrang der näheren Ordnung** ([§ 1930 BGB](https://www.gesetze-im-internet.de/bgb/__1930.html)): Ein Verwandter einer entfernteren Ordnung ist nicht zur Erbfolge berufen, solange ein Verwandter einer vorhergehenden Ordnung lebt. Existieren also Abkömmlinge (erste Ordnung), erben Eltern und Geschwister (zweite Ordnung) nicht.

### 3. Repräsentationsprinzip / Eintrittsrecht

Innerhalb einer Ordnung gilt das **Repräsentationsprinzip**: Der nähere, lebende Abkömmling schließt die durch ihn mit dem Erblasser verwandten weiteren Abkömmlinge von der Erbfolge aus (§ 1924 Abs. 2 BGB). Lebt das Kind, erben dessen Kinder (Enkel) nicht.

Ist ein Abkömmling **vorverstorben**, treten an seine Stelle die durch ihn verwandten Abkömmlinge (Erbfolge nach Stämmen / Eintrittsprinzip, § 1924 Abs. 3 BGB). Der Anteil des vorverstorbenen Stammes wird unter dessen Abkömmlingen aufgeteilt. Innerhalb der Ordnung erben mehrere Kinder zu gleichen Teilen (§ 1924 Abs. 4 BGB); in der zweiten Ordnung gilt Entsprechendes über Stämme der Eltern.

### 4. Ehegattenerbrecht neben den Ordnungen

Der überlebende Ehegatte erbt **neben Verwandten** als gesetzlicher Erbe ([§ 1931 BGB](https://www.gesetze-im-internet.de/bgb/__1931.html)):

- neben Verwandten der **ersten Ordnung**: **1/4** (§ 1931 Abs. 1 S. 1 BGB),
- neben Verwandten der **zweiten Ordnung** oder neben Großeltern: **1/2** (§ 1931 Abs. 1 S. 1 BGB),
- sind weder Verwandte erster/zweiter Ordnung noch Großeltern vorhanden: der Ehegatte erbt **allein** (§ 1931 Abs. 2 BGB).

Diese Quoten gelten vor der güterstandsabhängigen Korrektur (Schritt 5).

### 5. Güterstand: Zugewinngemeinschaft → pauschale Erhöhung

Lebten die Ehegatten im gesetzlichen Güterstand der **Zugewinngemeinschaft** (kein abweichender Ehevertrag), erhöht sich der gesetzliche Erbteil des überlebenden Ehegatten pauschal um **1/4** ([§ 1371 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__1371.html), sog. erbrechtliche Lösung des Zugewinnausgleichs):

- neben Kindern (erste Ordnung): 1/4 (§ 1931) + 1/4 (§ 1371) = **1/2**,
- neben zweiter Ordnung / Großeltern: 1/2 (§ 1931) + 1/4 (§ 1371) = **3/4**.

Bei **Gütertrennung** entfällt die Erhöhung; neben einem oder zwei Kindern gilt § 1931 Abs. 4 BGB (Ehegatte und Kinder zu gleichen Teilen). Bei **Gütergemeinschaft** bleibt es bei der Quote des § 1931 BGB; der Zugewinnausgleich entfällt.

### 6. Erbquoten berechnen

1. Ehegattenquote nach Schritt 4 + 5 festlegen (z. B. 1/2 neben erster Ordnung bei Zugewinngemeinschaft).
2. Restquote (1 − Ehegattenquote) auf die berufene Ordnung verteilen.
3. Innerhalb der Ordnung nach Stämmen / Köpfen aufteilen (Schritt 3), Eintrittsfälle berücksichtigen.
4. Probe: Summe aller Erbquoten = 1 (Vollerbschaft des gesamten Nachlasses).

**Beispiel** (Ehegatte, Zugewinngemeinschaft, zwei Kinder): Ehegatte 1/2; verbleibende 1/2 auf zwei Kinder zu je 1/4. Probe: 1/2 + 1/4 + 1/4 = 1.

### 7. Sonderfälle

- **Pflichtteil**: Enterbte Pflichtteilsberechtigte (Abkömmlinge, Ehegatte, Eltern) haben Pflichtteilsansprüche – nicht hier, sondern über die Pflichtteilsprüfung (§§ 2303 ff. BGB) klären.
- **Ausschlagung** (§§ 1942 ff. BGB): Schlägt ein Erbe aus, fällt sein Anteil an, wer ohne ihn berufen wäre; die Quoten verschieben sich – gesonderte Berechnung.
- **Erbunwürdigkeit** (§ 2339 BGB), **Adoption**, **nichteheliche Kinder** (heute gleichgestellt) ggf. prüfen.

## Risiken / typische Fehler

- **Ordnungssystem missachtet** — Eltern/Geschwister erben nicht neben lebenden Kindern (§ 1930 BGB).
- **Repräsentation vs. Eintritt verwechselt** — lebende Kinder schließen ihre eigenen Kinder aus; nur vorverstorbene Stämme lösen Eintritt aus.
- **Güterstand übersehen** — ohne Zugewinn-Erhöhung wird die Ehegattenquote (1/4 statt 1/2 neben Kindern) falsch berechnet.
- **§ 1931 Abs. 4 BGB bei Gütertrennung** nicht beachtet — abweichende Kopfteilung neben einem/zwei Kindern.
- **Probe unterlassen** — Summe der Erbquoten muss 1 ergeben.
- **Pflichtteil mit Erbquote vermengt** — Pflichtteil ist Geldanspruch, keine Erbenstellung.

## Quellen

### Statute

- [§ 1924 BGB](https://www.gesetze-im-internet.de/bgb/__1924.html) (Erben erster Ordnung, Repräsentations- und Eintrittsprinzip)
- [§ 1925 BGB](https://www.gesetze-im-internet.de/bgb/__1925.html) (Erben zweiter Ordnung)
- [§ 1926 BGB](https://www.gesetze-im-internet.de/bgb/__1926.html) (Erben dritter Ordnung)
- [§ 1930 BGB](https://www.gesetze-im-internet.de/bgb/__1930.html) (Vorrang der vorhergehenden Ordnung)
- [§ 1931 BGB](https://www.gesetze-im-internet.de/bgb/__1931.html) (Gesetzliches Erbrecht des Ehegatten)
- [§ 1371 BGB](https://www.gesetze-im-internet.de/bgb/__1371.html) (Zugewinnausgleich im Todesfall, pauschale Erhöhung um 1/4)

### Kommentare

- Leipold, in: MüKoBGB, 9. Aufl. 2023, § 1924 Rn. 1 ff.
- Weidlich, in: Grüneberg, BGB, 83. Aufl. 2024, §§ 1924 ff., § 1931
- Lange, in: BeckOGK BGB, § 1371

## Ausgabeformat

```
GESETZLICHE ERBFOLGE — <Erbfall / Az. Nachlassgericht> — <Datum>

I.   Wirksames Testament/Erbvertrag:   [nein / teilweise / ja → Skill testament-pruefung]
II.  Berufene Ordnung:                 [erste / zweite / dritte] (§ 1930 BGB)
III. Verwandte Erben (nach Stämmen)
     Stamm 1:                          <Person> — Quote …
     Stamm 2 (Eintritt § 1924 III):    <Personen> — Quote …
IV.  Ehegatte
     Quote § 1931:                     [1/4 neben 1. / 1/2 neben 2.]
     Güterstand:                       [Zugewinngemeinschaft / Gütertrennung / Gütergemeinschaft]
     Erhöhung § 1371:                  [+1/4 / keine]
     Ehegattenquote gesamt:            <…>
V.   Erbquoten gesamt
     <Person>: <Quote> …
     Probe Summe = 1:                  [✓ / 🔴]
VI.  Sonderfälle                       [Pflichtteil / Ausschlagung / — ]

Ergebnis: <Erben und Erbquoten>
```

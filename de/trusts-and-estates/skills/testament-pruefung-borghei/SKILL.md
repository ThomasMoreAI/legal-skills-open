---
name: testament-pruefung-borghei
title: /erbrecht:testament-pruefung
description: Prüfung eines Testaments auf formelle Wirksamkeit (eigenhändig § 2247 BGB oder notariell § 2232 BGB), Testierfähigkeit § 2229 BGB, Auslegung §§ 133, 2084 BGB, Wechselwirkung mit Pflichtteil §§ 2303 ff. BGB und Erbvertrag. Use when ein Testament auf Wirksamkeit, Anfechtbarkeit oder Pflichtteilsfolge geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/erbrecht/skills/testament-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: trusts-and-estates
language: de
---

# /erbrecht:testament-pruefung

## Zweck

Ein Testament entscheidet über Erbquoten in Millionenhöhe und hat oft nur ein DIN-A4-Blatt Form. Formfehler, Testierunfähigkeit und Auslegungsstreitigkeiten sind die Hauptangriffspunkte. Dieser Skill prüft die formelle und materielle Wirksamkeit systematisch.

## Eingaben

- Testamentstyp (eigenhändig / notariell / gemeinschaftlich / Erbvertrag)
- Errichtungsdatum und -ort
- Testierfähigkeit des Erblassers (Alter, gesundheitliche Lage zum Errichtungszeitpunkt)
- Wortlaut und etwaige Nachträge / Kodizillen
- Bestand etwaiger früherer Verfügungen
- Pflichtteilsberechtigte und Bedacht-Konstellation

## Ablauf

### 1. Testamentstyp

| Typ | Form | Norm |
|---|---|---|
| Eigenhändig | Gesamten Inhalt eigenhändig geschrieben + unterschrieben | [§ 2247 BGB](https://www.gesetze-im-internet.de/bgb/__2247.html) |
| Notariell | Erklärung gegenüber Notar oder Übergabe Schrift | [§ 2232 BGB](https://www.gesetze-im-internet.de/bgb/__2232.html) |
| Gemeinschaftlich (Ehegatten) | Gemeinschaftlich, § 2247 Form genügt | [§ 2265 BGB](https://www.gesetze-im-internet.de/bgb/__2265.html) |
| Erbvertrag | Notariell, mit Vertragspartner | [§ 2274 BGB](https://www.gesetze-im-internet.de/bgb/__2274.html) |
| Nottestament | Bürgermeister, drei Zeugen, Seenot | [§§ 2249–2252 BGB](https://www.gesetze-im-internet.de/bgb/__2249.html) |

### 2. Formelle Wirksamkeit eigenhändiges Testament (§ 2247 BGB)

- **Gesamter Text eigenhändig geschrieben** (keine Schreibmaschine, kein Diktat).
- **Unterschrift** mit Vor- und Nachnamen (Initialen reichen nicht; § 2247 Abs. 3 BGB-konforme „Sicherheits"-Unterschrift).
- **Datum** soll angegeben sein, fehlt es: nicht unwirksam, aber Probleme bei mehreren Testamenten.
- **Ort** soll angegeben sein, gleicher Maßstab.

### 3. Testierfähigkeit ([§ 2229 BGB](https://www.gesetze-im-internet.de/bgb/__2229.html))

- Mindestalter **16 Jahre** (§ 2229 Abs. 1 BGB).
- Vor 18: nur notariell oder zu Protokoll vor Notar (§ 2233 BGB).
- **Testierunfähig**, wer wegen krankhafter Störung der Geistestätigkeit, wegen Geistesschwäche oder wegen Bewusstseinsstörung nicht in der Lage ist, die Bedeutung seiner Erklärung einzusehen und nach dieser Einsicht zu handeln.

Beweislast bei Anfechter (Vermutung der Testierfähigkeit).

### 4. Auslegung (§§ 133, 2084 BGB)

- **Wille des Erblassers** vor Wortlaut.
- Andeutung im Testament muss aber **andeutungsfähig** sein (BGH-Rspr. zur ergänzenden Auslegung).
- **Auslegungsregel § 2084 BGB**: bei mehreren Auslegungen die zugunsten der Wirksamkeit.

### 5. Wechselwirkung mit Pflichtteil ([§§ 2303 ff. BGB](https://www.gesetze-im-internet.de/bgb/__2303.html))

- Pflichtteil = die Hälfte des gesetzlichen Erbteils der pflichtteilsberechtigten Person (Abkömmlinge, Ehegatte, Eltern).
- Pflichtteilsergänzungsanspruch § 2325 BGB bei Schenkungen 10 Jahre vor Erbfall (mit Abschmelzungstabelle).
- Pflichtteilsverzicht / -strafklauseln nur notariell.

### 6. Anfechtung (§§ 2078 ff. BGB)

- **Irrtum** (§ 2078): Anfechtung binnen 1 Jahr ab Kenntnis (§ 2082 BGB).
- **Drohung** (§ 2078 Abs. 2): wie Irrtum.
- **Übergehung Pflichtteilsberechtigter** (§ 2079 BGB): wenn Erblasser sie zur Zeit des Testaments noch nicht kannte / berechnet hatte.
- **Verfügung nach Errichtung des Testaments** ändert nichts an dessen Wirksamkeit, kann aber Konkurrenz schaffen.

### 7. Aufhebung und Widerruf

- Widerruf durch neueres Testament (§ 2253 BGB).
- Rücknahme aus amtlicher Verwahrung (§ 2256 BGB).
- Vernichtung mit Widerrufsabsicht (§ 2255 BGB).
- Bei Erbvertrag: Aufhebung nur durch Vertrag (§ 2290 BGB).

### 8. Erbschein und Vollzug

- Antrag beim Nachlassgericht (§§ 2353 ff. BGB, §§ 342 ff. FamFG).
- Erbschein bezeugt die Erbenstellung; im Streit um Wirksamkeit des Testaments „Erbenstreit" durch Feststellungsklage zu klären.

## Quellen

### Statute

- [§§ 2229, 2232, 2247, 2249, 2253, 2255 BGB](https://www.gesetze-im-internet.de/bgb/__2247.html)
- [§§ 2078, 2079, 2082, 2084 BGB](https://www.gesetze-im-internet.de/bgb/__2078.html)
- [§§ 2274 ff. BGB](https://www.gesetze-im-internet.de/bgb/__2274.html) (Erbvertrag)
- [§§ 2303, 2325 BGB](https://www.gesetze-im-internet.de/bgb/__2303.html) (Pflichtteil)
- [§§ 2353 ff. BGB](https://www.gesetze-im-internet.de/bgb/__2353.html) (Erbschein)
- [§§ 342 ff. FamFG](https://www.gesetze-im-internet.de/famfg/__342.html)

### Kommentare

- Leipold, in: MüKoBGB, 9. Aufl. 2023, § 2247 Rn. 1 ff.
- Sticherling, in: Burandt / Rojahn, Erbrecht, 4. Aufl. 2023
- Damrau / Tanck, in: Damrau / Tanck, Praxiskommentar Erbrecht

### Rechtsprechung

- BGH, Urt. v. 24.01.2018 – IV ZR 304/17, NJW 2018, 1300 (Testierfähigkeit) `[unverifiziert – prüfen]`
- BGH, Beschl. v. 22.09.2010 – IV ZR 12/10, NJW 2010, 3717 (eigenhändige Form) `[unverifiziert – prüfen]`

## Ausgabeformat

```
TESTAMENT-PRÜFUNG — <Mandat / Az. Nachlassgericht> — <Datum>

I.    Testamentstyp                  [eigenhändig / notariell / gemeinschaftlich / Erbvertrag]
II.   Formelle Wirksamkeit
      Eigenhändig vollständig:        [✓ / 🔴]
      Unterschrift:                   [✓ / 🔴]
      Datum / Ort:                    [angegeben / fehlend, aber zulässig]
III.  Testierfähigkeit § 2229
      Anhaltspunkte für Anfechtung:   [keine / Hinweise: …]
IV.   Auslegung
      Streitige Klauseln:             <…>
      Wille / Andeutung im Text:      <…>
V.    Pflichtteilsrisiken
      Berechtigte:                    <…>
      Pflichtteilsergänzung § 2325:   [anwendbar / nicht]
VI.   Anfechtungsrisiken (§§ 2078 ff.)  <…>
VII.  Wirksamkeit insgesamt           [✓ / 🟡 / 🔴]

Empfehlung: <Verteidigung / Anfechtung / Beratung Erblasser>
```

## Risiken / typische Fehler

- **Maschinenschriftliches „eigenhändiges" Testament** — formnichtig.
- **Initialen statt voller Unterschrift** — Risiko der Formnichtigkeit.
- **Anfechtungsfrist § 2082 BGB übersehen** — 1 Jahr ab Kenntnis.
- **Pflichtteilsergänzung § 2325 außer Acht** — Schenkungen 10 Jahre vor Tod relevant.
- **Auslegung gegen den Erblasserwillen** — § 133 BGB hat Vorrang vor Wortlaut.
- **Widerruf durch Vernichtung ohne Beweis** — Beweislast bei Anfechter.
- **Verbindlich vermerkte Nebenabreden** außerhalb des Testaments → in der Regel formnichtig.

---
name: nachbarrechtlicher-baustreit-borghei
title: /baurecht:nachbarrechtlicher-baustreit
description: 'Nachbarliche Abwehr gegen Bauvorhaben in beiden Spuren: öffentlich-rechtlich Drittanfechtung der Baugenehmigung (drittschützende Norm – Abstandsflächen LBO, Rücksichtnahmegebot § 34 I 2 / § 35 III BauGB iVm § 15 BauNVO) mit Eilrechtsschutz § 80 V iVm § 80a VwGO trotz Sofortvollzug § 212a BauGB; zivilrechtlich Beseitigungs- und Unterlassungsansprüche § 1004 BGB iVm § 906 BGB (Immissionen, Wesentlichkeit, Ortsüblichkeit, Geldausgleich) sowie Ansprüche aus Landes-Nachbarrechtsgesetzen. Use when ein Mandant gegen ein Nachbarvorhaben vorgehen oder als Bauherr die Erfolgsaussichten einer Nachbarklage einschätzen will.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/baurecht/skills/nachbarrechtlicher-baustreit
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: construction
language: de
---

# /baurecht:nachbarrechtlicher-baustreit

## Zweck

Der Skill prüft beide Rechtsschutzspuren des Nachbarn gegen ein Bauvorhaben: öffentlich-rechtlich (Drittanfechtung der erteilten Baugenehmigung; Eilrechtsschutz nach § 80 V iVm § 80a VwGO wegen Sofortvollzug § 212a BauGB) und zivilrechtlich (§ 1004 iVm § 906 BGB; Landes-Nachbarrechtsgesetze). Voraussetzung der öffentlich-rechtlichen Klage ist eine **drittschützende Norm**, deren Verletzung der Nachbar gerade in eigener Sache rügen kann.

## Eingaben

- Position des Mandanten (Nachbar oder Bauherr)
- Baugenehmigung (Datum, Adressat, Anlage)
- Lage der Grundstücke, Bundesland (LBO), B-Plan / Innen- / Außenbereich
- Konkrete Beeinträchtigungen (Abstand, Verschattung, Lärm, Geruch, Erschütterung, Sicht)
- Datum der Kenntnis vom Bauvorhaben / der Baugenehmigung; Rechtsbehelfsbelehrung
- Bisheriger Verfahrensstand (Widerspruch eingelegt? Klage erhoben?)

## Sub-Agent-Architektur

Researcher liefert §§ BauGB / BauNVO / der einschlägigen LBO, BVerwG-/OVG-Rechtsprechung zum Drittschutz und Rücksichtnahmegebot sowie zur Immissionsabwehr nach BGH-Linie (§ 906 BGB). Drafter prüft drittschützende Norm, ihre Verletzung im konkreten Fall und entwirft Anfechtungsklage + Antrag § 80 V iVm § 80a VwGO; daneben Klageentwurf § 1004 BGB. Reviewer prüft, ob die drittschützende Norm konkret benannt ist, ob § 212a BauGB adressiert ist, ob die 1-Monats-Klagefrist (§ 74 VwGO) eingehalten ist, und ob § 906 BGB-Schritte (Wesentlichkeit, Ortsüblichkeit, Geldausgleich) sauber abgearbeitet sind.

## Ablauf

### 1. Klagebefugnis § 42 II VwGO – drittschützende Norm

Der Nachbar ist nur befugt, eine ihm gegenüber **rechtswidrige** Verletzung einer **drittschützenden** Norm geltend zu machen. Pauschale „Rechtswidrigkeit" der BauG reicht nicht.

Typische drittschützende Normen:

| Norm | Drittschutz | Belegstelle |
|---|---|---|
| **Abstandsflächen** der LBO (BayBO Art. 6; BauO NRW § 6; LBO BW § 5 etc.) | Ja, drittschützend | ständige OVG-Rspr. `[unverifiziert]` |
| **Festsetzungen eines B-Plans über die Art der baulichen Nutzung** | Ja – Gebietserhaltungsanspruch der Nachbarn im plan- oder faktischen Baugebiet | BVerwG, st. Rspr. `[unverifiziert]` |
| **§ 34 II BauGB iVm BauNVO** (faktisches Baugebiet) | Ja, soweit Art der Nutzung betroffen – Gebietserhaltungsanspruch übertragen | BVerwG, Urt. v. 16.09.1993 – 4 C 28.91, BVerwGE 94, 151 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=16.09.1993&Aktenzeichen=4+C+28.91) |
| **Rücksichtnahmegebot** in § 34 I 2, § 35 III BauGB iVm § 15 I 2 BauNVO | Ja, wenn der Nachbar **individualisiert** und **qualifiziert** betroffen ist | BVerwG, Urt. v. 25.02.1977 – IV C 22.75, BVerwGE 52, 122 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=25.02.1977&Aktenzeichen=4+C+22.75) |
| **Maß** der baulichen Nutzung (GRZ/GFZ § 16 BauNVO) | grundsätzlich **nicht** drittschützend; nur über das Rücksichtnahmegebot | BVerwG-Linie `[unverifiziert]` |
| **Brandschutzvorschriften** der LBO | teilweise drittschützend, soweit Schutzzweck den Nachbarn umfasst | umstritten / LBO-spezifisch |

### 2. Materielle Verletzung der drittschützenden Norm

Konkrete Subsumtion: ist die Abstandsfläche unterschritten? Ist die zulässige Art der Nutzung im (faktischen) Baugebiet überschritten? Liegt eine qualifizierte Rücksichtslosigkeit vor (Verschattung, „erdrückende Wirkung", Lärm über TA-Lärm-Werten)?

### 3. Eilrechtsschutz § 80 V iVm § 80a VwGO

Wegen § 212a BauGB hat Widerspruch / Anfechtungsklage des Nachbarn **keine** aufschiebende Wirkung. Der Nachbar muss daher beim Verwaltungsgericht den **Antrag auf Anordnung der aufschiebenden Wirkung** (§ 80 V VwGO iVm § 80a VwGO) stellen; ggf. zugleich vorläufige Baueinstellung.

Maßstab: Interessenabwägung; bei offensichtlicher Rechtswidrigkeit Anordnung der aufschiebenden Wirkung wahrscheinlich; bei offensichtlicher Rechtmäßigkeit Ablehnung; bei offenem Ausgang Interessenabwägung mit Folgenabwägung (insb. drohende vollendete Tatsachen durch Bauausführung).

### 4. Klagefristen

| Konstellation | Frist |
|---|---|
| Nachbar wird Adressat der BauG (idR Bekanntgabe nach Landesrecht) | § 74 I VwGO, 1 Monat ab Bekanntgabe |
| Nachbar ist nicht Adressat, erfährt aber sicher von der BauG | analog § 70 II VwGO iVm § 58 II VwGO – 1 Jahr bei fehlender Rechtsbehelfsbelehrung; Verwirkung möglich (st. Rspr. `[unverifiziert]`) |
| Vor Bauausführung (Eilbedarf) | Antrag § 80 V VwGO – keine starre Frist, aber vor Baubeginn empfohlen |

### 5. Zivilrechtliche Spur

Parallel oder ergänzend:

**a) § 1004 BGB iVm § 906 BGB (Immissionen)**

Schema:

1. Eigentum / dingliches Recht des Nachbarn
2. Beeinträchtigung iSv § 1004 I BGB – durch Immissionen (§ 906: Geräusche, Erschütterungen, Gerüche, Stäube, Wärme, Erschütterungen, ähnliche Einwirkungen)
3. Wesentlichkeit der Beeinträchtigung (§ 906 I 1) – Maßstab: durchschnittlicher Empfindlichkeitsgrad eines verständigen Nutzers; Heranziehung von TA Lärm / TA Luft / GIRL
4. Ortsüblichkeit (§ 906 II 1) – ortsübliche Nutzung und Vermeidbarkeit mit zumutbaren Maßnahmen
5. Folgen:
   - unwesentlich → keine Abwehr
   - wesentlich + ortsunüblich → Unterlassung / Beseitigung
   - wesentlich + ortsüblich + nicht zumutbar vermeidbar → Duldungspflicht + **Geldausgleichsanspruch § 906 II 2 BGB** (analog)
6. Duldungspflicht aus öffentlich-rechtlicher Genehmigung? – im Ausgangspunkt grundsätzlich keine zivilrechtliche Sperrwirkung, aber Indizwirkung; im einzelnen str.

**b) Landes-Nachbarrechtsgesetze**

Z. B. NachbG NRW (Grenzabstände Pflanzen, Hammerschlags- und Leiterrecht, Notwegrecht); BayAGBGB Art. 43 ff.; NRG BW. Klagewege: Zivilgericht, idR Amtsgericht.

**c) § 823 BGB**

Bei Substanzverletzungen während der Bauausführung (z. B. Risse durch Erschütterungen) – Schadensersatz; verschuldensabhängig.

### 6. Verhältnis öffentlich-rechtlicher / zivilrechtlicher Rechtsschutz

Beide Spuren stehen grundsätzlich nebeneinander. Eine bestandskräftige Baugenehmigung sperrt zivilrechtliche Unterlassungsansprüche **nicht** automatisch, kann sie aber im Rahmen der Ortsüblichkeit / Zumutbarkeit indiziell beeinflussen. Drittschützende öffentlich-rechtliche Normen (Abstandsflächen) entfalten keine unmittelbare zivilrechtliche Bindungswirkung.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 34 BauGB](https://www.gesetze-im-internet.de/bbaug/__34.html), [§ 35 BauGB](https://www.gesetze-im-internet.de/bbaug/__35.html), [§ 212a BauGB](https://www.gesetze-im-internet.de/bbaug/__212a.html)
- [§ 15 BauNVO](https://www.gesetze-im-internet.de/baunvo/__15.html) (Gebietsverträglichkeit / Rücksichtnahmegebot)
- LBO des einschlägigen Landes – insbesondere Abstandsflächenregelung (BayBO Art. 6 / BauO NRW § 6 / LBO BW § 5 etc.)
- [§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html), [§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html), [§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html), [§ 80a VwGO](https://www.gesetze-im-internet.de/vwgo/__80a.html)
- [§ 906 BGB](https://www.gesetze-im-internet.de/bgb/__906.html) (Immissionen)
- [§ 1004 BGB](https://www.gesetze-im-internet.de/bgb/__1004.html) (Beseitigung und Unterlassung)
- [§ 823 BGB](https://www.gesetze-im-internet.de/bgb/__823.html)
- Landes-Nachbarrechtsgesetz (z. B. [NachbG NRW](https://recht.nrw.de/lmi/owa/br_bes_text?anw_nr=2&gld_nr=4&ugl_nr=4231&bes_id=3729&val=3729&ver=0&sg=0&aufgehoben=N&menu=1))

### Kommentare

- Battis, in: Battis/Krautzberger/Löhr, BauGB, 15. Aufl. 2022, § 34 Rn. 70 ff. (Drittschutz)
- Söfker, in: Ernst/Zinkahn/Bielenberg/Krautzberger, BauGB (Loseblatt), § 34 Rn. 130 ff.
- Fickert/Fieseler, BauNVO, 13. Aufl. 2019, § 15 Rn. 1 ff. (Rücksichtnahmegebot)
- LBO-Kommentar des betroffenen Landes (z. B. Simon/Busse, BayBO Art. 6; Boeddinghaus/Hahn/Schulte, BauO NRW § 6)
- Brückner, in: MüKoBGB, 9. Aufl. 2023, § 906 Rn. 1 ff.
- Wilhelmi, in: Erman, BGB, 17. Aufl. 2023, § 906 Rn. 1 ff., § 1004 Rn. 1 ff.
- Säcker, in: MüKoBGB, 9. Aufl. 2023, § 1004 Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris/BeckOnline]`)

1. BVerwG, Urt. v. 25.02.1977 – IV C 22.75, BVerwGE 52, 122 (Rücksichtnahmegebot – Schweinemast/Wohnnachbar)
2. BVerwG, Urt. v. 16.09.1993 – 4 C 28.91, BVerwGE 94, 151 (Gebietserhaltungsanspruch im faktischen Baugebiet)
3. BVerwG, Urt. v. 23.09.1999 – 4 C 6.98, BVerwGE 109, 314 (Rücksichtnahmegebot, Konkretisierung)
4. BVerwG, Beschl. v. 11.01.1999 – 4 B 128.98, NVwZ 1999, 879 (drittschützende Wirkung Abstandsflächen)
5. BGH, Urt. v. 30.10.1998 – V ZR 64/98, BGHZ 140, 1 (§ 906 II 2 BGB-Geldausgleich, Grundsätze)
6. BGH, Urt. v. 18.09.2009 – V ZR 75/08 (Ortsüblichkeit)

## Ausgabeformat

```
GUTACHTEN — Nachbarrechtlicher Baustreit
Mandant: <Nachbar / Bauherr>
Vorhaben: <Beschreibung>   Bundesland: <…>

I. Sachverhalt (knapp, mit Lage / Abständen)

II. Frage(n)

III. Kurzantwort
     - Klagebefugnis (drittschützende Norm): [ja / nein – welche]
     - Erfolgsaussicht Anfechtung BauG: [hoch / mittel / gering]
     - Eilrechtsschutz § 80 V iVm § 80a VwGO: [angeraten / nicht erforderlich]
     - Zivilrechtliche Spur § 1004 iVm § 906 BGB: [aussichtsreich / nachrangig]

IV. Rechtliche Bewertung
    1. Öffentlich-rechtliche Spur
       a) Klagebefugnis § 42 II VwGO – drittschützende Norm
          – Abstandsflächen LBO <Land>
          – Gebietserhaltungsanspruch § 34 II BauGB / B-Plan
          – Rücksichtnahmegebot § 15 BauNVO
       b) Materielle Verletzung
       c) Sofortvollzug § 212a BauGB → § 80 V iVm § 80a VwGO
       d) Klagefristen (§ 74 VwGO; ggf. § 58 II)
    2. Zivilrechtliche Spur
       a) § 1004 iVm § 906 BGB
          – Wesentlichkeit
          – Ortsüblichkeit
          – Vermeidbarkeit + Geldausgleich § 906 II 2
       b) Landes-Nachbarrechtsgesetz
       c) § 823 BGB bei Substanzschäden
    3. Verhältnis der Spuren

V. Schriftsatzentwurf
   – Anfechtungsklage / Antrag § 80 V iVm § 80a VwGO
   – Klage § 1004, § 906 BGB

VI. Fristen-Box
    – Klagefrist § 74 VwGO (1 Monat)
    – Eilantrag § 80 V VwGO (vor Baubeginn)
    – Verjährung § 1004 / § 906 BGB

VII. Risiken / offene Punkte
     <Einstufung mit Begründung>

VIII. Quellenverzeichnis
```

## Beispiel (verkürzt, Gutachtenstil)

**Sachverhalt.** Mandant M wohnt in einem faktischen reinen Wohngebiet (§ 34 II BauGB iVm § 3 BauNVO) in NRW. Auf dem unmittelbar angrenzenden Grundstück wurde der Bau einer fünfgeschossigen Wohnanlage genehmigt. Die Abstandsfläche nach § 6 BauO NRW ist um 1,20 m unterschritten; die geplante Höhe verschattet das Wohnzimmer und das Schlafzimmer von M.

**I. Klagebefugnis.** § 6 BauO NRW ist drittschützend zugunsten des Nachbarn (OVG NRW, st. Rspr. `[unverifiziert – prüfen]`). Die Unterschreitung um 1,20 m ist substantiell und nicht durch landesrechtliche Ausnahmevorschriften gedeckt (Sachverhalt). Klagebefugnis (+).

**II. § 34 II BauGB iVm § 3 BauNVO.** Im faktischen reinen Wohngebiet ist die Art (Wohnnutzung) zwar konform; das Maß ist über § 34 I BauGB zu prüfen, ist aber im Grundsatz nicht drittschützend. Ein Anspruch ergibt sich daher allenfalls über das Rücksichtnahmegebot (§ 15 I 2 BauNVO) – erdrückende Wirkung erscheint angesichts fünf Geschossen unmittelbar an der Grenze gut vertretbar.

**III. § 212a BauGB / Eilrechtsschutz.** Die Anfechtungsklage hat kraft Gesetzes keine aufschiebende Wirkung. Empfehlung: Sofortiger Antrag § 80 V iVm § 80a VwGO beim VG, gestützt auf Abstandsflächenverstoß; daneben Anfechtungsklage innerhalb der Frist des § 74 VwGO (1 Monat ab Bekanntgabe der BauG).

**IV. Zivilrechtliche Flanke.** Verschattung als „ähnliche Einwirkung" iSv § 906 BGB ist BGH-rechtlich nicht ohne Weiteres erfasst (negative Immission, str.); Schwerpunkt daher öffentlich-rechtlich. Bei späteren Lärmimmissionen aus dem Betrieb (Tiefgarage, Müllplatz) zusätzlich § 1004 iVm § 906 BGB zu prüfen.

## Risiken / typische Fehler

- **Drittschützende Norm nicht konkret benennen** – Klage ist unzulässig (§ 42 II VwGO).
- **§ 212a BauGB übersehen** – ohne Eilantrag droht Bauausführung; vollendete Tatsachen mindern die Erfolgsaussichten des Eilantrags.
- **Maß der baulichen Nutzung als drittschützend behandeln** (idR nicht; nur über Rücksichtnahme).
- **1-Monats-Klagefrist § 74 VwGO** verpassen – Wiedereinsetzung nur eng.
- **Verschattung / Sichtschutz** als § 906-Immission behandeln, ohne BGH-Linie zu negativen Immissionen zu prüfen.
- **§ 906 II 2 BGB Geldausgleich** als Vorrangiges Mittel verkaufen, obwohl Wesentlichkeit / Ortsüblichkeit nicht subsumiert sind.
- **Bestandskräftige BauG als zivilrechtliche Sperre** behaupten – greift so nicht; Indizwirkung möglich.
- **Vermischen** von LBO der falschen Bundesländer; LBO ist landesgebunden.

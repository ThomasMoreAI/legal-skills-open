---
name: einstweilige-verfuegung-uwg-borghei
title: /wettbewerbsrecht:einstweilige-verfuegung-uwg
description: Einstweiliger Rechtsschutz nach §§ 12 ff. UWG iVm §§ 935, 940 ZPO – Verfügungsanspruch (UWG-Verstoß glaubhaft) und Verfügungsgrund (Dringlichkeitsvermutung § 12 I UWG mit Selbstwiderlegung), Schutzschriftenregister, mündliche Verhandlung § 937 II ZPO, Vollziehungsfrist § 929 II ZPO, Schadensersatz § 945 ZPO, Aufhebung § 927 ZPO. Use when ein UWG-Verstoß schnell unterbunden werden soll oder der Mandant präventiv Schutzschrift hinterlegen will.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/wettbewerbsrecht/skills/einstweilige-verfuegung-uwg
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: consumer
language: de
---

# /wettbewerbsrecht:einstweilige-verfuegung-uwg

## Zweck

Der Skill prüft Voraussetzungen und entwirft den Antrag auf eine einstweilige Verfügung wegen UWG-Verstoßes. Er adressiert sowohl die Antragstellerseite (Eilrechtsschutz erlangen) als auch die Antragsgegnerseite (Schutzschrift hinterlegen, Widerspruch / Berufung, Aufhebungsantrag). Schwerpunkt ist die Dringlichkeitsvermutung des § 12 I UWG, ihre Selbstwiderlegung und die strikte Vollziehungsfrist des § 929 II ZPO.

## Eingaben

- konkrete UWG-Verletzung (Wortlaut der Werbung, Datum der Veröffentlichung, Medium)
- Datum der **Erstkenntnis** des Antragstellers (entscheidend für Dringlichkeit)
- Aktivlegitimation (Mitbewerber, Verband §§ 8, 8b)
- bereits ausgesprochene Abmahnung? (Reaktion, Frist)
- Position des Mandanten: Antragsteller, Antragsgegner, oder präventiv (Schutzschrift)
- gewünschte Verfahrensart: Beschlussverfügung oder Verfügung nach mündlicher Verhandlung

## Sub-Agent-Architektur

Researcher liefert UWG-Statute (§§ 8, 12), ZPO-Statute (§§ 935, 940, 929 II, 937 II, 945, 927, 32) und BGH/OLG-Rspr. zur Dringlichkeitsvermutung. Drafter prüft Verfügungsanspruch und Verfügungsgrund in Urteilsstil und entwirft Antragstenor / Schutzschrift. Reviewer prüft Selbstwiderlegung und die kritische Vollziehungsfrist § 929 II ZPO.

## Ablauf

### 1. Verfügungsanspruch

Materiell-rechtlicher Unterlassungsanspruch aus § 8 I iVm einem UWG-Tatbestand (§§ 3, 3 III iVm Anhang, 3a, 4, 4a, 5, 5a, 5b, 6, 7 UWG). Aktivlegitimation nach § 8 III, § 8b UWG. **Glaubhaftmachung** § 294 ZPO durch eidesstattliche Versicherung, Screenshots, Werbeunterlagen, Privatgutachten.

### 2. Verfügungsgrund (§ 12 I UWG)

§ 12 I UWG enthält eine **gesetzliche Dringlichkeitsvermutung** für UWG-Unterlassungsansprüche. Antragsteller muss den Verfügungsgrund **nicht gesondert darlegen**; Antragsgegner kann die Vermutung widerlegen.

**Selbstwiderlegung** durch Zuwarten: Wer trotz Kenntnis vom Verstoß zu lange wartet, zeigt, dass es ihm nicht eilig ist (OLG-Spruchpraxis, regional uneinheitlich):

| OLG-Bezirk | Faustregel maximales Zuwarten |
|---|---|
| OLG München, OLG Hamburg | ca. 1 Monat ab Kenntnis `[unverifiziert – prüfen in juris]` |
| OLG Köln, OLG Düsseldorf | ca. 6 Wochen `[unverifiziert]` |
| OLG Frankfurt | ca. 6–8 Wochen `[unverifiziert]` |

**Erstkenntnis-Datum** ist zwingend mit eidesstattlicher Versicherung zu dokumentieren. Zwischen Kenntnis und Antrag liegen idR: Abmahnung (Frist 1 Woche), Reaktion, Antragsformulierung. Diese Schritte sind grundsätzlich „dringlichkeitsunschädlich", wenn zügig durchgeführt.

### 3. Verfahrensgang § 935, 940, 937 II ZPO

- **Antrag**: schriftlich beim zuständigen Gericht (sachlich LG, § 14 I UWG; örtlich am Begehungsort, § 14 II UWG iVm § 32 ZPO)
- **Entscheidung ohne mündliche Verhandlung** zulässig (§ 937 II ZPO), insbesondere in dringenden Fällen
- **Beschlussverfügung** oder Urteil nach mündlicher Verhandlung
- bei Beschlussverfügung: **keine Anhörung des Gegners**, aber Schutzschrift wird berücksichtigt

### 4. Schutzschriftenregister

Bei drohender einstweiliger Verfügung kann der potenzielle Antragsgegner eine **Schutzschrift** beim zentralen elektronischen Schutzschriftenregister (ZSSR, § 945a ZPO) hinterlegen. Wirkung: Das Gericht muss die Schutzschrift bei seiner Entscheidung berücksichtigen.

Inhalt der Schutzschrift:
- antizipierte Verteidigung gegen den drohenden Antrag
- Bestreiten der Aktivlegitimation / des UWG-Verstoßes / der Dringlichkeit
- Hinweise auf eigene Position (z. B. fehlende Wiederholungsgefahr nach abgegebener UE)

### 5. Vollziehung § 929 II ZPO — die kritische Monatsfrist

Eine im Beschlusswege erlassene Verfügung muss **binnen eines Monats ab Zustellung an den Antragsteller** vollzogen werden, sonst aufhebbar nach § 927 ZPO (BGH, std. Rspr.) `[unverifiziert – prüfen in juris]`.

Vollziehung erfolgt durch:
- **Parteizustellung** der Verfügung an den Antragsgegner durch den Gerichtsvollzieher
- bei Unterlassungsverfügung genügt **Zustellung** (kein gesonderter Vollstreckungsakt nötig)

**Praxis-Risiko**: Die Frist beginnt mit Zustellung an den Antragsteller (bzw. seinen Anwalt), nicht mit Erlass. Säumnis = Verfügung wird auf Antrag des Antragsgegners aufgehoben (§ 927 ZPO).

### 6. Rechtsbehelfe des Antragsgegners

| Verfahrensart | Rechtsbehelf | Frist |
|---|---|---|
| Beschlussverfügung | **Widerspruch** (§ 924 ZPO) | keine gesetzliche Frist, aber faktisch dringlich |
| Urteilsverfügung | **Berufung** (§ 511 ZPO) | 1 Monat (§ 517 ZPO), Begründung 2 Monate (§ 520 II ZPO) |
| Säumnis Vollziehungsfrist | **Aufhebungsantrag** (§ 927 ZPO) | jederzeit nach Fristablauf |
| Wegfall des Verfügungsgrundes | **Aufhebungsantrag** (§ 927 ZPO) | jederzeit |

### 7. Schadensersatz § 945 ZPO

Wird die Verfügung als **von Anfang an ungerechtfertigt** aufgehoben, haftet der Antragsteller dem Antragsgegner verschuldensunabhängig auf Schadensersatz (§ 945 ZPO; BGH, std. Rspr.) `[unverifiziert – prüfen in juris]`. Bedeutsame Risikoposition, vor Antragstellung zu adressieren.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 8 UWG](https://www.gesetze-im-internet.de/uwg_2004/__8.html) (Unterlassungsanspruch)
- [§ 12 UWG](https://www.gesetze-im-internet.de/uwg_2004/__12.html) (einstweilige Verfügung, Dringlichkeitsvermutung)
- [§ 14 UWG](https://www.gesetze-im-internet.de/uwg_2004/__14.html) (sachliche/örtliche Zuständigkeit)
- [§ 935 ZPO](https://www.gesetze-im-internet.de/zpo/__935.html) (einstweilige Verfügung allgemein)
- [§ 940 ZPO](https://www.gesetze-im-internet.de/zpo/__940.html) (Regelungsverfügung)
- [§ 937 ZPO](https://www.gesetze-im-internet.de/zpo/__937.html) (Verfahren, Abs. II — ohne mündliche Verhandlung)
- [§ 929 ZPO](https://www.gesetze-im-internet.de/zpo/__929.html) (Vollziehungsfrist)
- [§ 927 ZPO](https://www.gesetze-im-internet.de/zpo/__927.html) (Aufhebung)
- [§ 945 ZPO](https://www.gesetze-im-internet.de/zpo/__945.html) (Schadensersatz)
- [§ 945a ZPO](https://www.gesetze-im-internet.de/zpo/__945a.html) (Schutzschriftenregister)
- [§ 32 ZPO](https://www.gesetze-im-internet.de/zpo/__32.html) (Gerichtsstand der unerlaubten Handlung)
- [§ 517 ZPO](https://www.gesetze-im-internet.de/zpo/__517.html) (Berufungsfrist)

### Kommentare

- Köhler, in: Köhler/Bornkamm/Feddersen, UWG, jeweils aktuell, § 12 UWG Rn. 1 ff.
- Berneke/Schüttpelz, Die einstweilige Verfügung in Wettbewerbssachen, 4. Aufl. 2022
- Vollkommer, in: Zöller, ZPO, 35. Aufl. 2024, § 929 ZPO Rn. 1 ff.
- Drescher, in: MüKoZPO, 6. Aufl. 2020, § 935 ZPO Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris]`)

1. BGH, Urt. v. 01.07.1999 – I ZR 244/96, GRUR 2000, 151 – Cookies (Dringlichkeit) `[unverifiziert]`
2. OLG München, Beschl. v. 28.07.2016 – 6 W 1144/16, GRUR-RR 2016, 506 (Selbstwiderlegung) `[unverifiziert]`
3. BGH, Urt. v. 22.10.2009 – I ZR 58/07, GRUR 2010, 253 – Fischdosendeckel (Vollziehung § 929 II ZPO) `[unverifiziert]`
4. BGH, Beschl. v. 15.07.2021 – I ZB 11/20, GRUR 2021, 1196 (Aufhebung § 927 ZPO) `[unverifiziert]`

## Ausgabeformat (Antragsteller-Perspektive)

```
ANTRAG AUF ERLASS EINER EINSTWEILIGEN VERFÜGUNG

An das Landgericht <Ort>
- Kammer für Handelssachen / Wettbewerbskammer -

In Sachen
  Antragstellerin: <Firma, Anschrift, vertreten durch …>
  Antragsgegnerin: <Firma, Anschrift>

wegen Unterlassung nach §§ 8, 3, 5 UWG

A. Antrag
   Der Antragsgegnerin wird im Wege der einstweiligen Verfügung,
   bei Meidung eines vom Gericht für jeden Fall der Zuwiderhandlung
   festzusetzenden Ordnungsgeldes bis zu 250.000 EUR, ersatzweise
   Ordnungshaft, oder Ordnungshaft bis zu 6 Monaten (§ 890 ZPO),
   untersagt,
   im geschäftlichen Verkehr zu Wettbewerbszwecken
   <konkrete Verletzungsform, möglichst wörtlich oder mit Abbildung>
   zu werben und/oder werben zu lassen.

B. Begründung
   I.  Sachverhalt (mit Erstkenntnis-Datum)
   II. Verfügungsanspruch
       1. Aktivlegitimation §§ 8 III, 8b UWG
       2. UWG-Verstoß
          – konkret subsumierte Norm (§§ 5 / 5a / 5b / 6 / 7 / …)
          – Verkehrsauffassung Durchschnittsverbraucher
       3. Glaubhaftmachung (eV, Screenshots, Anlagen)
   III. Verfügungsgrund § 12 I UWG
       1. Dringlichkeitsvermutung
       2. Keine Selbstwiderlegung (Zeitablauf seit Erstkenntnis)
   IV. Zuständigkeit § 14 UWG iVm § 32 ZPO

C. Anlagen
   – eV des Geschäftsführers (Erstkenntnis-Datum)
   – Screenshot der beanstandeten Werbung
   – ggf. erfolglose Abmahnung
   – Berechnung des Streitwerts

Antrag, ohne mündliche Verhandlung zu entscheiden (§ 937 II ZPO),
hilfsweise Termin zur mündlichen Verhandlung anzuberaumen.

<Ort, Datum, Anwaltsunterschrift>

[Frist-Erinnerung intern:
  – Vollziehung § 929 II ZPO: innerhalb 1 Monat ab Zustellung
    der Verfügung an Antragsteller, Datum Wiedervorlage: ___
  – Verjährung § 11 UWG: ___
]
```

## Beispiel (Auszug, Urteilsstil im Antrag)

> **III. Verfügungsgrund.** Der Verfügungsgrund folgt aus § 12 I UWG. Die gesetzliche Dringlichkeitsvermutung ist nicht widerlegt. Die Antragstellerin hat die beanstandete Werbung erstmals am TT.MM.JJJJ zur Kenntnis genommen (Anl. ASt 3, eV des Geschäftsführers). Sie hat am TT+5.MM.JJJJ abgemahnt; nach Ablehnung der modifizierten UE durch die Antragsgegnerin am TT+12.MM.JJJJ ist der vorliegende Antrag binnen weiterer 9 Tage gestellt worden. Eine Zeitspanne von insgesamt 21 Tagen zwischen Kenntnis und Antragstellung liegt innerhalb des nach der Spruchpraxis des LG <Ort> / OLG <Ort> dringlichkeitsunschädlichen Rahmens (vgl. OLG <Ort>, Beschl. v. … `[unverifiziert – prüfen]`).

## Risiken / typische Fehler

- **Erstkenntnis-Datum nicht dokumentiert** — Dringlichkeitsvermutung wird in Gegenwehr widerlegt.
- **Zu langes Zuwarten** — Selbstwiderlegung; je nach OLG-Bezirk 4–8 Wochen kritisch.
- **Antragstenor zu weit** („jegliche irreführende Werbung") — Bestimmtheitsmangel, Zurückweisung.
- **Antragstenor zu eng** — Kerntheorie wird vom Antragsgegner durch leichte Variation umgangen.
- **Vollziehungsfrist § 929 II ZPO verpasst** — Aufhebung nach § 927 ZPO. Wiedervorlage zwingend.
- **Glaubhaftmachung schwach** — eV ohne Datum/Ort, Screenshots ohne URL, fehlende Sachverhaltsdokumentation.
- **Risiko § 945 ZPO unterschätzt** — bei zu Unrecht erwirkter Verfügung verschuldensunabhängige Schadensersatzpflicht des Antragstellers.
- **Schutzschriftenregister vergessen** (Antragsgegner-Perspektive) — Beschlussverfügung ohne Anhörung möglich.

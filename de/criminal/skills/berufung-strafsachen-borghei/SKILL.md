---
name: berufung-strafsachen-borghei
title: /strafrecht:berufung-strafsachen
description: Prüfung und Strategie der Berufung in Strafsachen – Statthaftigkeit § 312 StPO, Einlegungsfrist § 314 StPO, Berufungsbeschränkung § 318 StPO, Verschlechterungsverbot § 331 StPO, Umfang und Entscheidung §§ 327, 328 StPO; Beschränkung auf die Rechtsfolgen, reformatio in peius. Use when gegen ein amtsgerichtliches Strafurteil Berufung zu prüfen, einzulegen oder zu beschränken ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/strafrecht/skills/berufung-strafsachen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: criminal
language: de
---

# /strafrecht:berufung-strafsachen

## Zweck

Die Berufung ist die **zweite Tatsacheninstanz** gegen amtsgerichtliche Urteile — vollständige neue Hauptverhandlung vor dem Landgericht. Dieser Skill prüft Statthaftigkeit und die **Einlegungsfrist von einer Woche**, klärt die strategisch zentrale Frage der **Berufungsbeschränkung** (etwa nur auf die Rechtsfolgen) und sichert das **Verschlechterungsverbot** (reformatio in peius) ab.

## Eingaben

- angefochtenes Urteil (Amtsgericht — Strafrichter oder Schöffengericht, Datum)
- Anwesenheit bei Verkündung / Zustellungsdatum
- Ziel: Freispruch, niedrigere Strafe, nur Rechtsfolgen?
- wer legt ein (Angeklagter / StA zu seinen Gunsten / zu seinen Lasten)?
- Beweislage zum Schuldspruch vs. Angemessenheit der Rechtsfolgen

## Sub-Agent-Architektur

Die Bearbeitung verteilt sich auf drei Prosa-Rollen. Ein Statthaftigkeits-Agent prüft, ob gegen das konkrete Urteil die Berufung eröffnet ist, und wahrt die Einlegungsfrist. Ein Beschränkungs-Agent entscheidet, ob die Berufung auf einzelne Beschwerdepunkte — insbesondere auf die Rechtsfolgen — beschränkt werden soll, und prüft die Wirksamkeit der Beschränkung (Trennbarkeit, widerspruchsfreie Feststellungen zum Schuldspruch). Ein Schutz-Agent überwacht das Verschlechterungsverbot und warnt, sobald durch eine gegenläufige Berufung der StA das Risiko einer reformatio in peius entsteht. Die Rollen sind gedankliche Arbeitsschritte, keine getrennten technischen Prozesse.

## Ablauf

### 1. Statthaftigkeit ([§ 312 StPO](https://www.gesetze-im-internet.de/stpo/__312.html))

Berufung ist statthaft gegen die Urteile des **Strafrichters** und des **Schöffengerichts** (Amtsgericht). Gegen landgerichtliche und oberlandesgerichtliche Urteile ist sie ausgeschlossen — dort nur Revision.

### 2. Einlegungsfrist ([§ 314 StPO](https://www.gesetze-im-internet.de/stpo/__314.html))

**Eine Woche ab Urteilsverkündung**, bei Abwesenheit ab Zustellung. Einlegung schriftlich oder zu Protokoll der Geschäftsstelle beim **Amtsgericht** (iudex a quo). Versäumung → Verwerfung als unzulässig; Wiedereinsetzung §§ 44 ff. StPO nur bei unverschuldeter Verhinderung. Eine Begründung ist — anders als bei der Revision — **nicht** zwingend.

### 3. Berufungsbeschränkung ([§ 318 StPO](https://www.gesetze-im-internet.de/stpo/__318.html))

Die Berufung kann auf **bestimmte Beschwerdepunkte beschränkt** werden. Praktisch wichtigster Fall: **Beschränkung auf die Rechtsfolgen** (Strafmaß) bei akzeptiertem Schuldspruch. Voraussetzung der Wirksamkeit:

- der angefochtene Teil ist **trennbar** vom übrigen Urteil,
- die Feststellungen zum Schuldspruch sind **widerspruchsfrei und tragfähig**.

Unwirksame Beschränkung → das Landgericht prüft den gesamten Schuld- und Rechtsfolgenausspruch neu.

### 4. Umfang und Entscheidung ([§ 327 StPO](https://www.gesetze-im-internet.de/stpo/__327.html), [§ 328 StPO](https://www.gesetze-im-internet.de/stpo/__328.html))

- **§ 327 StPO:** Das Berufungsgericht prüft das Urteil nur, **soweit es angefochten** ist — die wirksame Beschränkung begrenzt den Prüfungsumfang.
- **§ 328 StPO:** Bei begründeter Berufung **entscheidet das Landgericht in der Sache selbst** (eigene Hauptverhandlung); bei zu Unrecht angenommener Zuständigkeit hebt es auf und verweist.

### 5. Verschlechterungsverbot ([§ 331 StPO](https://www.gesetze-im-internet.de/stpo/__331.html))

Haben **nur der Angeklagte**, die StA **zu seinen Gunsten** oder sein gesetzlicher Vertreter Berufung eingelegt, darf das Urteil in **Art und Höhe der Rechtsfolgen nicht zum Nachteil** des Angeklagten geändert werden (**Verbot der reformatio in peius**). Legt dagegen die **StA zu seinen Lasten** ein, entfällt der Schutz — eine höhere Strafe ist dann möglich. Vor jeder Berufungseinlegung ist dieses Risiko mit dem Mandanten zu klären.

## Quellen

### Statute

- [§ 312 StPO](https://www.gesetze-im-internet.de/stpo/__312.html), [§ 314 StPO](https://www.gesetze-im-internet.de/stpo/__314.html), [§ 318 StPO](https://www.gesetze-im-internet.de/stpo/__318.html), [§ 327 StPO](https://www.gesetze-im-internet.de/stpo/__327.html), [§ 328 StPO](https://www.gesetze-im-internet.de/stpo/__328.html), [§ 331 StPO](https://www.gesetze-im-internet.de/stpo/__331.html)
- §§ 44 ff. StPO (Wiedereinsetzung), § 335 StPO (Sprungrevision als Alternative)

### Kommentare

- Meyer-Goßner / Schmitt, StPO, 67. Aufl. 2024, § 318, § 331 Rn. 1 ff.
- Paul, in: KK-StPO, 9. Aufl. 2023, § 318 Rn. 1 ff.
- Beulke, Strafprozessrecht, 15. Aufl. 2023, Rn. 552 ff.

### Rechtsprechung

- BGH zur Wirksamkeit der Berufungsbeschränkung nach § 318 StPO — Aktenzeichen `[unverifiziert – prüfen]`
- BGH zur Reichweite des Verschlechterungsverbots § 331 StPO — Aktenzeichen `[unverifiziert – prüfen]`

## Ausgabeformat

```
BERUFUNG STRAFSACHEN — <Mandant-ID> — <Datum>
VERTRAULICH — STRAFVERTEIDIGUNG

I.    Angefochtenes Urteil       <AG / Strafrichter / Schöffengericht — Datum>
II.   Statthaftigkeit            [§ 312 StPO ✅]
III.  Einlegungsfrist (1 Woche)  Verkündung <…> → Ende <…> [🟢/🔴]
IV.   Beschränkung (§ 318 StPO)
      Ziel:                       [voll / nur Rechtsfolgen / einzelne Punkte]
      Wirksam (trennbar)?         [✅ / ⚠️]
V.    Verschlechterungsverbot
      Wer legt ein?               <Angeklagter / StA zugunsten / StA zulasten>
      Reformatio in peius möglich? [nein § 331 / ⚠️ ja — StA zulasten]

Empfehlung: <…>
Nächster Schritt: <…>
```

## Risiken / typische Fehler

- **Einlegungsfrist (eine Woche) versäumt** — Berufung wird als unzulässig verworfen.
- **Unwirksame Berufungsbeschränkung** — bei widersprüchlichen Schuldspruch-Feststellungen rollt das Landgericht den gesamten Fall neu auf.
- **Reformatio in peius** unterschätzt — bei gegenläufiger StA-Berufung droht eine **höhere Strafe**; das Verschlechterungsverbot schützt dann nicht.
- **Sprungrevision** als Alternative übersehen (§ 335 StPO) — Berufung verbraucht die Tatsacheninstanz, schließt aber unmittelbare Rechtskontrolle aus.
- **Beschränkung auf Rechtsfolgen** trotz angreifbaren Schuldspruchs — verschenkt eine mögliche Freispruchchance.

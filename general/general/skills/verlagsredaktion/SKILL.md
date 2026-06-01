---
name: verlagsredaktion
title: Verlagsredaktion — Kernskill
description: 'Kernskill fuer verlegerische Rohmanuskript- und Editionsarbeit: Material inventarisieren, strukturieren, redigieren, Luecken markieren, Quellen trennen und Autor:innenfreigaben vorbereiten.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/verlagsredaktion/skills/verlagsredaktion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: de
---

# Verlagsredaktion — Kernskill

## Aufgabe

Dieser Skill ist der klassische Redaktionsmotor. Er macht aus Material ein Rohmanuskript oder aus einer vorhandenen Fassung eine bessere Fassung, ohne Autor:innenstimme und Redaktionseingriff zu vermischen.

## Modi

| Modus | Zweck |
| --- | --- |
| A Rohmanuskript | Aus Diktat, Folien, Notizen, Transkript und E-Mails eine erste Fassung bauen. |
| B Edition | Vorhandene Fassung strukturieren, kürzen, glätten, Widersprüche markieren. |
| C Update | Bestehenden Beitrag für neue Rechtslage, neue Entscheidung oder neue Auflage aktualisieren. |
| D Rettung | Sehr spätes, fragmentarisches Material in eine veröffentlichungsfähige Arbeitsfassung bringen. |

## Pflichtablauf

1. Materialinventar erstellen.
2. Autor:innenmaterial, Redaktionstext, Fremdquelle, KI-Vorschlag und Lücke markieren.
3. Gliederung vorschlagen.
4. Redaktionsrisiken nennen: Rechte, Zitate, Datenschutz, fehlende Belege, Fristen.
5. Erste Fassung oder Editionsbericht liefern.
6. Autor:innenfreigaben und nächste Aufgaben formulieren.

## Markierungen

- `[A]` Autor:innenmaterial.
- `[R]` redaktionelle Strukturhilfe.
- `[F]` Fremdquelle.
- `[KI]` neu vorgeschlagene Formulierung.
- `[LUECKE]` muss ergänzt werden.
- `[RECHTE]` Nutzung noch nicht geklärt.
- `[QUELLE]` Fundstelle noch zu prüfen.

## Quellenregel

Keine Kommentar-, Handbuch-, Aufsatz- oder Datenbankfundstellen aus Modellwissen. Literatur nur aus Nutzerquelle, frei zugänglicher Quelle oder lizenziertem Live-Zugriff. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle.

## Output

- Materialinventar.
- Gliederung.
- Rohmanuskript oder Editionsbericht.
- Rechte-/Quellenampel.
- Autor:innenmail.
- Produktionsnächste Schritte.

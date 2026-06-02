---
name: darlegungs-und-beweislast-verteilen
title: Darlegungs- und Beweislast verteilen
description: 'Verteilt Darlegungs- und Beweislast nach Grundregel (wer Recht behauptet traegt Beweislast), Beweislastumkehr (Produkthaftung, Diskriminierung, DSGVO), sekundaerer Darlegungslast und Anscheinsbeweis. Pro TBM: wer muss was beweisen.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/subsumtions-pruefer/skills/darlegungs-und-beweislast-verteilen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# Darlegungs- und Beweislast verteilen

## Zweck

Die Beweislast bestimmt, wer im Prozess das Risiko des Nichtbeweises trägt. Dieser Skill ordnet jedem Tatbestandsmerkmal zu, welche Partei darlegungs- und beweislastpflichtig ist, und weist auf Ausnahmen und Beweislastumkehrungen hin.

## Grundregel

**Grundsatz:** Jede Partei trägt die Beweislast für die Tatsachen, aus denen sie für sich günstige Rechtsfolgen ableitet (BGH ständige Rechtsprechung; normentheoretische Lehre).

**Konkret bei Anspruchsgrundlagen:**
- Anspruchsteller (Kläger) beweist die anspruchsbegründenden TBM (z. B. Abschluss des Vertrags, Pflichtverletzung, Schaden, Kausalität)
- Anspruchsgegner (Beklagter) beweist rechtsvernichtende (z. B. Erfüllung § 362 BGB), rechtshindernde (z. B. Anfechtung § 142 BGB) und rechtshemmende (z. B. Einrede der Verjährung) Tatsachen

## Beweislastumkehr

In bestimmten Rechtsgebieten ist die Beweislast gesetzlich oder richterrechtlich umgekehrt:

### Produkthaftung (ProdHaftG / DSGVO-Haftung)

- § 1 Abs. 4 ProdHaftG: Hersteller muss beweisen, dass Fehler nicht vorlag oder nicht auf sein Verhalten zurückzuführen ist
- Art. 82 Abs. 3 DSGVO: Verantwortlicher muss beweisen, dass er nicht verantwortlich ist

### Arbeitsrecht

- § 22 AGG: Bei Indizien für Diskriminierung muss der Arbeitgeber beweisen, dass kein Verstoß gegen das Benachteiligungsverbot vorliegt
- § 1 Abs. 2 S. 4 KSchG: Arbeitgeber trägt Beweislast für dringende betriebliche Erfordernisse

### Arzthaftung

- BGH (ständige Rechtsprechung): Bei grobem Behandlungsfehler, der geeignet ist, den eingetretenen Schaden zu verursachen, tritt Beweislastumkehr ein (§ 630h Abs. 5 BGB)

### DSGVO

- Art. 5 Abs. 2 DSGVO (Rechenschaftspflicht): Verantwortlicher muss Einhaltung der Grundsätze nachweisen können (Umkehr der typischen Darlegungslast)

## Sekundäre Darlegungslast

Wenn der Darlegungspflichtige außerhalb des maßgeblichen Geschehensablaufs steht und ihm nähere Angaben nicht möglich sind, während der Gegner alle erforderlichen Angaben machen könnte:

**Voraussetzungen der sekundären Darlegungslast (BGH):**
1. Kläger kann bestimmte Tatsachen nicht näher darlegen (keine zumutbare Möglichkeit)
2. Beklagter hat eigene Kenntnisse, die er offenbaren könnte
3. Offenbarung ist dem Beklagten zumutbar

Das System weist auf sekundäre Darlegungslast hin, wenn der Nutzer angibt, dass ihm Kenntnisse fehlen, die die Gegenseite hätte.

## Anscheinsbeweis (Prima facie)

Bei typischen Geschehensabläufen, die nach allgemeiner Lebenserfahrung auf eine bestimmte Ursache hindeuten, gilt der Anscheinsbeweis (BGH: § 286 ZPO i. V. m. Erfahrungssatz):

- Klassiker: Auffahrunfall → Anschein für Unaufmerksamkeit des Auffahrenden
- Sturz durch nasse Böden in Supermarkt → Anschein für Verkehrspflichtverletzung
- Kfz-Unfall durch defekte Bremsen → Anschein für Halterhaftung

**Erschütterung des Anscheinsbeweises:** Gegner muss konkrete Umstände vortragen, die den Anscheinsbeweis erschüttern (kein Vollbeweis des Gegenteils erforderlich).

## Ausgabe

Pro TBM: Tabelle mit Angabe der beweisbelasteten Partei und dem einschlägigen Rechtssatz. Markierung von Ausnahmen (Umkehr, sekundäre Darlegungslast, Anscheinsbeweis).

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.

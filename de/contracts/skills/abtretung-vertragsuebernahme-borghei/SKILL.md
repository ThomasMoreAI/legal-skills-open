---
name: abtretung-vertragsuebernahme-borghei
title: /vertragsrecht:abtretung-vertragsuebernahme
description: Prüfung und Gestaltung von Forderungsabtretung, Schuld- und Vertragsübernahme – Abtretung § 398 BGB, Abtretungsausschluss § 399 BGB und dessen Durchbrechung für Geldforderungen aus Handelsgeschäften nach § 354a HGB, Schuldnerschutz bei stiller Zession § 407 BGB, Schuldübernahme §§ 414, 415 BGB, Vertragsübernahme als Drei-Parteien-Vereinbarung sowie Factoring und Abtretungsanzeige. Use when eine Forderung übertragen, ein Vertrag auf einen Dritten übergeleitet oder ein vertragliches Abtretungsverbot geprüft werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vertragsrecht/skills/abtretung-vertragsuebernahme
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /vertragsrecht:abtretung-vertragsuebernahme

## Zweck

Wer eine Forderung überträgt, überträgt sie mit allen Einreden und trifft auf drei Fallen: ein **vertragliches Abtretungsverbot**, den **Schuldnerschutz** bei nicht angezeigter Zession und die Verwechslung von **Forderungsabtretung** mit **Vertragsübernahme**. Dieser Skill ordnet das gewünschte wirtschaftliche Ergebnis dem richtigen Instrument zu, prüft die Wirksamkeit und liefert die Muster für Abtretungsvereinbarung und Abtretungsanzeige.

## Eingaben

- Übertragungsziel: nur Forderung, nur Schuld, gesamtes Vertragsverhältnis, gesamter Betrieb
- Ausgangsvertrag: Wortlaut zu Abtretung, Übertragung und Zustimmungserfordernissen
- Parteirollen: beiderseitiges Handelsgeschäft? Öffentlich-rechtlicher Schuldner? Verbraucher?
- Art der Forderung: Geldforderung, höchstpersönlicher Anspruch, künftige Forderung, Teilforderung
- Zweck: Finanzierung (Factoring, Forfaitierung), Sicherung, Konzernumstrukturierung, Verkauf
- Bereits erfolgte Erklärungen: Abtretungsanzeige, Zustimmung des Schuldners, Zahlungen an den Altgläubiger

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert Statute (BGB §§ 398 ff., 414 ff.; HGB § 354a) mit URL und Kommentarstellen zu Bestimmbarkeit und Prioritätsgrundsatz.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) wählt das Instrument, prüft Übertragbarkeit und entwirft Abtretungsvereinbarung, Anzeige oder Vertragsübernahmevereinbarung.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Bestimmbarkeit, Abtretungsverbote, Zustimmungserfordernisse, Prioritätskonflikte und die Vollständigkeit der Nebenrechteübertragung.

## Ablauf

### 1. Instrumentenwahl

| Ziel | Instrument | Zustimmung des Dritten nötig? |
|---|---|---|
| Nur die Forderung übertragen | Abtretung § 398 BGB | **Nein** — der Schuldner wirkt nicht mit |
| Nur die Schuld übertragen | Schuldübernahme §§ 414, 415 BGB | **Ja** — Gläubiger muss zustimmen bzw. genehmigen |
| Zusätzlichen Schuldner gewinnen | Schuldbeitritt (gesetzlich nicht geregelt) | Nein — kein Schuldnerwechsel |
| Gesamtes Vertragsverhältnis übertragen | Vertragsübernahme (gesetzlich nicht geregelt) | **Ja** — dreiseitige Vereinbarung oder Zustimmung |
| Betrieb mit allen Verträgen | Asset Deal mit Einzelübertragung; ggf. § 613a BGB für Arbeitsverhältnisse | Vertragspartner je Vertrag |

**Die Vertragsübernahme ist der praktische Regelfall bei Unternehmenstransaktionen** und wird in der Praxis entweder als **dreiseitiger Vertrag** oder als zweiseitiger Vertrag mit **Zustimmung** des verbleibenden Teils abgeschlossen. Eine bloße Abtretung überträgt die Gestaltungsrechte (Kündigung, Rücktritt, Minderung) **nicht** — das ist der häufigste Konstruktionsfehler.

### 2. Abtretung ([§ 398 BGB](https://www.gesetze-im-internet.de/bgb/__398.html))

Eine Forderung kann vom Gläubiger durch Vertrag mit einem anderen auf diesen übertragen werden; mit dem Abschluss tritt der neue Gläubiger **an die Stelle des bisherigen Gläubigers**. Die Abtretung ist ein **Verfügungsgeschäft** und abstrakt vom zugrunde liegenden Kausalgeschäft (Kauf, Sicherungsabrede, Factoringvertrag).

- **Formfrei**, auch bei formbedürftigem Grundgeschäft.
- **Bestimmtheit bzw. Bestimmbarkeit:** Die Forderung muss spätestens im Zeitpunkt ihrer Entstehung eindeutig identifizierbar sein (Schuldner, Rechtsgrund, Zeitraum, Betrag). Künftige Forderungen sind abtretbar, wenn sie bestimmbar bezeichnet sind.
- **Prioritätsgrundsatz:** Bei mehrfacher Abtretung derselben Forderung erwirbt der **zeitlich erste** Zessionar; ein gutgläubiger Erwerb von Forderungen ist im BGB nicht vorgesehen.
- **Nebenrechte** gehen nach § 401 BGB über (Hypothek, Pfandrecht, **Bürgschaft**), Gestaltungsrechte und unselbständige Nebenrechte hingegen nur, soweit vereinbart. **Ausdrücklich mitregeln.**
- **Einredeerhalt** (§ 404 BGB): Der Schuldner kann dem neuen Gläubiger alle Einwendungen entgegensetzen, die zur Zeit der Abtretung gegen den bisherigen Gläubiger begründet waren — einschließlich der Verjährungseinrede.
- **Aufrechnung** (§ 406 BGB): Der Schuldner kann auch mit einer Forderung gegen den Altgläubiger aufrechnen, sofern er sie nicht erst nach Kenntnis der Abtretung erworben hat.

### 3. Abtretungsausschluss ([§ 399 BGB](https://www.gesetze-im-internet.de/bgb/__399.html))

Eine Forderung kann **nicht** abgetreten werden, wenn

1. die Leistung an einen anderen als den ursprünglichen Gläubiger **nicht ohne Veränderung ihres Inhalts** erfolgen kann (höchstpersönliche Ansprüche, unvertretbare Dienstleistungen, Freistellungsansprüche), oder
2. die Abtretung durch **Vereinbarung mit dem Schuldner ausgeschlossen** ist (*pactum de non cedendo*).

Das vertragliche Abtretungsverbot wirkt **dinglich**: Eine gleichwohl vorgenommene Abtretung ist **unwirksam**, nicht bloß pflichtwidrig. Das ist die schärfste Waffe des Schuldners und in Einkaufs-AGB großer Abnehmer der Standardfall. In AGB ist ein Abtretungsverbot für Geldforderungen gegenüber Unternehmern gleichwohl nicht per se unwirksam; gegenüber Verbrauchern ist ein Ausschluss der Abtretung von Geldforderungen nach § 308 Nr. 9 BGB unwirksam.

### 4. Durchbrechung im Handelsverkehr ([§ 354a HGB](https://www.gesetze-im-internet.de/hgb/__354a.html))

Ist die Abtretung einer **Geldforderung** durch Vereinbarung mit dem Schuldner nach § 399 BGB ausgeschlossen und ist das zugrunde liegende Rechtsgeschäft für **beide Teile ein Handelsgeschäft** — oder ist der Schuldner eine **juristische Person des öffentlichen Rechts** oder ein öffentlich-rechtliches Sondervermögen —, so ist die **Abtretung gleichwohl wirksam** (§ 354a Abs. 1 S. 1 HGB).

- Der Schuldner kann jedoch **mit befreiender Wirkung an den bisherigen Gläubiger leisten** (§ 354a Abs. 1 S. 2 HGB) — dieses Recht ist **unabdingbar** (§ 354a Abs. 1 S. 3 HGB). Der Zessionar muss den Erlös daher vom Zedenten einfordern; bei dessen Insolvenz trägt er das Risiko.
- **Ausnahme § 354a Abs. 2 HGB:** Für Darlehensforderungen von **Kreditinstituten** gilt Absatz 1 nicht — dort bleibt das Abtretungsverbot dinglich wirksam.

**§ 354a HGB ist der Anker jeder Factoring- und Sicherungszessionsprüfung im B2B**: Er rettet die Abtretung gegen ein Verbot in den Einkaufs-AGB des Abnehmers, macht sie aber im Verhältnis zum Schuldner nur eingeschränkt durchsetzbar.

### 5. Schuldnerschutz und Abtretungsanzeige ([§ 407 BGB](https://www.gesetze-im-internet.de/bgb/__407.html))

Der neue Gläubiger muss eine **Leistung**, die der Schuldner **nach der Abtretung** an den bisherigen Gläubiger bewirkt, sowie jedes Rechtsgeschäft zwischen ihnen über die Forderung **gegen sich gelten lassen** — es sei denn, der Schuldner kannte die Abtretung bei der Leistung bzw. der Vornahme des Rechtsgeschäfts. Ergänzend schützen §§ 406, 408, 409 BGB; nach **§ 409 BGB** muss sich der Gläubiger an einer angezeigten Abtretung festhalten lassen, auch wenn sie nicht erfolgt oder unwirksam ist.

Daraus folgt: Die **Abtretungsanzeige** ist keine Wirksamkeitsvoraussetzung, aber das Mittel, um den Schuldnerschutz des § 407 BGB zu beenden.

**Muster Abtretungsanzeige:**

> „Sehr geehrte Damen und Herren, wir zeigen Ihnen an, dass wir unsere Forderung gegen Sie aus [Rechnung Nr. …, Vertrag vom …] in Höhe von [Betrag] EUR mit Wirkung zum [Datum] an die [Zessionar, Anschrift] **abgetreten** haben. Zahlungen mit schuldbefreiender Wirkung können ab sofort **ausschließlich** an die [Zessionar] auf das Konto [IBAN] geleistet werden. Bitte richten Sie auch Einwendungen und sonstige Erklärungen künftig an die [Zessionar]."

Bei **stiller Zession** (typisch bei Sicherungsabtretung und stillem Factoring) unterbleibt die Anzeige; der Zedent bleibt zur Einziehung ermächtigt. Der Zessionar trägt dann das Risiko aus § 407 BGB und muss sich vertraglich das Recht vorbehalten, die Zession jederzeit offenzulegen.

### 6. Factoring

Beim Factoring verkauft der Anschlusskunde seine Forderungen laufend an den Factor.

- **Echtes Factoring:** Der Factor übernimmt das **Delkredererisiko** (Ausfallrisiko). Rechtlich ein **Forderungskauf** (§ 453 BGB) mit Abtretung nach § 398 BGB; die Forderung verlässt die Bilanz des Anschlusskunden.
- **Unechtes Factoring:** Das Ausfallrisiko bleibt beim Anschlusskunden; wirtschaftlich ein **Darlehen** mit Sicherungsabtretung.
- **Offenes vs. stilles Factoring:** je nach Anzeige an den Debitor.
- **Kollisionen prüfen:** verlängerter Eigentumsvorbehalt der Lieferanten und Globalzession der Hausbank (siehe `/vertragsrecht:sicherheiten-gestaltung`); im Verhältnis zum echten Factoring wird die Kollision überwiegend zugunsten des Vorbehaltslieferanten aufgelöst, weil dem Anschlusskunden der Gegenwert zufließt `[unverifiziert – prüfen]`.
- **Abtretungsverbote** im Debitorenvertrag über § 354a HGB prüfen (Ziff. 4).

### 7. Schuldübernahme ([§ 414 BGB](https://www.gesetze-im-internet.de/bgb/__414.html), [§ 415 BGB](https://www.gesetze-im-internet.de/bgb/__415.html))

- **§ 414 BGB — Vertrag zwischen Gläubiger und Übernehmer:** Eine Schuld kann von einem Dritten durch Vertrag mit dem Gläubiger in der Weise übernommen werden, dass der Dritte an die Stelle des bisherigen Schuldners tritt. Zustimmung des Altschuldners nicht erforderlich.
- **§ 415 BGB — Vertrag zwischen Schuldner und Übernehmer:** Wird die Schuldübernahme zwischen dem Dritten und dem Schuldner vereinbart, hängt ihre Wirksamkeit von der **Genehmigung des Gläubigers** ab. Bis zur Genehmigung gilt im Zweifel eine **Erfüllungsübernahme** im Innenverhältnis (§ 415 Abs. 3 BGB) — der Altschuldner bleibt nach außen verpflichtet.
- **Folge für Sicherheiten (§ 418 BGB):** Infolge der Schuldübernahme **erlöschen** die für die Forderung bestellten Bürgschaften und Pfandrechte, sofern der Bürge oder Verpfänder nicht einwilligt. **Vor jeder Schuldübernahme ist die schriftliche Einwilligung sämtlicher Sicherungsgeber einzuholen** — sonst steht der Gläubiger unbesichert da.
- **Einwendungen** des Übernehmers nach § 417 BGB: aus dem Schuldverhältnis ja, aus dem Innenverhältnis zum Altschuldner nein.

### 8. Vertragsübernahme

Die Vertragsübernahme ist gesetzlich nicht geregelt, aber als einheitliches Rechtsgeschäft anerkannt: Sie überträgt **das gesamte Schuldverhältnis** mit allen Rechten, Pflichten, Gestaltungsrechten und Nebenabreden. Sie ist **nicht** in eine Abtretung plus Schuldübernahme zerlegbar, weil die Gestaltungsrechte sonst zurückblieben.

**Klauselbaustein Vertragsübernahme:**

> „(1) Mit Wirkung zum [Datum, 00:00 Uhr] tritt die [Übernehmerin] anstelle der [Überträgerin] in sämtliche Rechte und Pflichten aus dem Vertrag vom [Datum] ein (**Vertragsübernahme**). (2) Die [Vertragspartnerin] stimmt der Vertragsübernahme hiermit zu. (3) Die Überträgerin haftet für bis zum Übertragungsstichtag entstandene Verbindlichkeiten neben der Übernehmerin als Gesamtschuldnerin fort; im Innenverhältnis stellt die Übernehmerin die Überträgerin frei. (4) Sicherheiten, die für die übernommenen Verbindlichkeiten bestellt sind, bleiben bestehen; die Sicherungsgeber haben ihre Einwilligung nach § 418 BGB in Anlage [N] erteilt."

## Quellen

### Statute

- [§ 398 BGB](https://www.gesetze-im-internet.de/bgb/__398.html), [§ 399 BGB](https://www.gesetze-im-internet.de/bgb/__399.html), [§ 401 BGB](https://www.gesetze-im-internet.de/bgb/__401.html), [§ 404 BGB](https://www.gesetze-im-internet.de/bgb/__404.html), [§ 406 BGB](https://www.gesetze-im-internet.de/bgb/__406.html), [§ 407 BGB](https://www.gesetze-im-internet.de/bgb/__407.html), [§ 409 BGB](https://www.gesetze-im-internet.de/bgb/__409.html)
- [§ 414 BGB](https://www.gesetze-im-internet.de/bgb/__414.html), [§ 415 BGB](https://www.gesetze-im-internet.de/bgb/__415.html), [§ 417 BGB](https://www.gesetze-im-internet.de/bgb/__417.html), [§ 418 BGB](https://www.gesetze-im-internet.de/bgb/__418.html)
- [§ 308 BGB](https://www.gesetze-im-internet.de/bgb/__308.html) Nr. 9, [§ 453 BGB](https://www.gesetze-im-internet.de/bgb/__453.html)
- [§ 354a HGB](https://www.gesetze-im-internet.de/hgb/__354a.html)

### Kommentare

- Grüneberg, BGB, 83. Aufl. 2024, §§ 398, 399, 407, 414 ff. Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`
- Kieninger, in: MüKoBGB, 9. Aufl. 2022, § 398 Rn. 1 ff., § 399 Rn. 1 ff.
- K. Schmidt, in: MüKoHGB, 5. Aufl. 2021, § 354a Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 14.10.1963 – VII ZR 33/62 (Kollision echtes Factoring / verlängerter Eigentumsvorbehalt) `[unverifiziert – prüfen]`
- BGH, Urt. v. 26.06.2002 – VIII ZR 327/00 (Bestimmbarkeit bei Globalzession) `[unverifiziert – prüfen]`

> Beide Aktenzeichen vor Verwendung in juris / Beck-Online prüfen. Die tragenden Aussagen folgen aus dem Gesetzeswortlaut.

## Ausgabeformat

```
ABTRETUNG / VERTRAGSÜBERNAHME — <Vorgang> — <Datum>

I.    Übertragungsziel                [Forderung / Schuld / Vertragsverhältnis / Betrieb]
II.   Gewähltes Instrument            [§ 398 / §§ 414, 415 / Vertragsübernahme / Schuldbeitritt]
III.  Übertragbarkeit (§ 399)         [✅ / ❌ höchstpersönlich / ❌ pactum de non cedendo]
        § 354a HGB einschlägig:       [ja — Abtretung wirksam, § 354a I 2 beachten / nein]
IV.   Bestimmtheit / Bestimmbarkeit   [✅ / ❌ — Beschreibung]
V.    Nebenrechte (§ 401)             [übergehend / gesondert geregelt: <…>]
        Gestaltungsrechte:            [ausdrücklich mitübertragen ✅/❌]
VI.   Zustimmungen                    [Gläubiger § 415 / Vertragspartner / Sicherungsgeber § 418]
VII.  Abtretungsanzeige (§ 407)       [erfolgt am <Datum> / bewusst still — Risiko benannt]
VIII. Prioritätskonflikte             [Globalzession / verlängerter EV / Doppelzession — Befund]
IX.   Factoring                       [N/A / echt / unecht; offen / still]

Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Tatsachen: <Liste>
```

## Risiken / typische Fehler

- **Abtretungsverbot übersehen** — die Abtretung ist nach § 399 BGB **dinglich unwirksam**, nicht bloß pflichtwidrig; ohne § 354a HGB erwirbt der Zessionar nichts.
- **§ 354a Abs. 1 S. 2 HGB nicht bedacht** — der Schuldner darf trotz wirksamer Abtretung weiter an den Altgläubiger leisten; dieses Recht ist unabdingbar und macht die Abtretung in der Insolvenz des Zedenten wertlos.
- **Abtretung statt Vertragsübernahme gewählt** — Gestaltungsrechte wie Kündigung, Rücktritt und Minderung gehen bei bloßer Abtretung nicht über.
- **Sicherheiten nach § 418 BGB erloschen** — bei der Schuldübernahme erlöschen Bürgschaften und Pfandrechte ohne Einwilligung des Sicherungsgebers; die Einwilligung ist vorab schriftlich einzuholen.
- **Keine Abtretungsanzeige, aber Zahlung an den Zedenten** — der Schuldner wird nach § 407 BGB frei; der Zessionar muss den Erlös vom Zedenten herausverlangen.
- **Künftige Forderungen unbestimmt bezeichnet** — die Abtretung geht ins Leere; Schuldner, Rechtsgrund und Zeitraum müssen die Forderung im Entstehungszeitpunkt identifizierbar machen.

---
name: sicherheiten-gestaltung-borghei
title: /vertragsrecht:sicherheiten-gestaltung
description: Auswahl und Gestaltung von Kreditsicherheiten im Vertragsrecht – Bürgschaft §§ 765–778 BGB mit Schriftform § 766 BGB, Einrede der Vorausklage § 771 BGB und selbstschuldnerischer Bürgschaft § 773 BGB, Eigentumsvorbehalt § 449 BGB in einfacher, verlängerter und erweiterter Form, Sicherungsübereignung nach §§ 929, 930 BGB und Sicherungsabtretung nach § 398 BGB einschließlich Globalzession und Übersicherung. Use when eine Forderung besichert werden soll oder eine bestehende Sicherheit auf Wirksamkeit und Verwertbarkeit zu prüfen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/vertragsrecht/skills/sicherheiten-gestaltung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# /vertragsrecht:sicherheiten-gestaltung

## Zweck

Sicherheiten entscheiden nicht im Normalverlauf, sondern in der Insolvenz des Schuldners — und dort scheitern sie an drei wiederkehrenden Fehlern: **Formmangel**, **fehlende Bestimmtheit** und **Übersicherung**. Dieser Skill wählt die passende Sicherheit für die Forderungsart aus, prüft ihre Wirksamkeit und liefert Klauselbausteine für Bürgschaft, Eigentumsvorbehalt und Sicherungsabtretung.

## Eingaben

- Zu sichernde Forderung: Rechtsgrund, Betrag, Laufzeit, künftige oder bestehende Forderung
- Parteirollen: Kaufmann (§ 350 HGB) oder Verbraucher; Sicherungsgeber personenidentisch mit Schuldner?
- Verfügbare Sicherungsgegenstände: Warenlager, Maschinen, Forderungen aus Lieferung und Leistung, Grundstücke, Bankguthaben
- Bestehende Sicherheiten Dritter (Vorrangkonflikte, insbesondere verlängerter Eigentumsvorbehalt vs. Globalzession)
- Branche und Weiterverarbeitungsketten (für verlängerten Eigentumsvorbehalt)
- Bei Prüfung einer bestehenden Sicherheit: Wortlaut der Vereinbarung, Datum, Form

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert Statute (BGB Sachenrecht, Bürgschaftsrecht, HGB) mit URL sowie Kommentarstellen zu Bestimmtheitsgrundsatz und Übersicherung.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) wählt die Sicherheit, prüft Wirksamkeit und Vorrangkonflikte und entwirft die Klauseln.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Form (§ 766 BGB, § 350 HGB), Bestimmtheit, Freigabeklausel, AGB-Kontrolle und Insolvenzfestigkeit.

## Ablauf

### 1. Sicherheitenauswahl nach Forderungsart

| Sicherungsgegenstand | Instrument | Insolvenzrechtliche Stellung |
|---|---|---|
| Persönliche Haftung eines Dritten | Bürgschaft §§ 765 ff. BGB; Schuldbeitritt; Garantie | Forderung gegen den Bürgen, insolvenzfest |
| Gelieferte Ware | Eigentumsvorbehalt § 449 BGB | Aussonderung § 47 InsO (einfacher EV) |
| Weiterverkaufte Ware / Forderung daraus | Verlängerter Eigentumsvorbehalt | Absonderung § 51 Nr. 1 InsO |
| Maschinen, Fuhrpark, Warenlager | Sicherungsübereignung §§ 929, 930 BGB | Absonderung § 51 Nr. 1 InsO |
| Forderungen aus Lieferung und Leistung | Sicherungsabtretung § 398 BGB, Globalzession | Absonderung § 51 Nr. 1 InsO |
| Grundstück | Grundschuld, Hypothek §§ 1113 ff., 1191 ff. BGB | Absonderung § 49 InsO |

**Akzessorisch** (Bürgschaft, Hypothek) heißt: Die Sicherheit teilt das Schicksal der Hauptforderung. **Nicht akzessorisch** (Sicherungsübereignung, Sicherungsabtretung, Grundschuld) heißt: Die Bindung an die Forderung folgt nur aus der schuldrechtlichen **Sicherungsabrede** — diese muss ausdrücklich vereinbart werden.

### 2. Bürgschaft — Begriff und Form ([§ 765 BGB](https://www.gesetze-im-internet.de/bgb/__765.html), [§ 766 BGB](https://www.gesetze-im-internet.de/bgb/__766.html))

Durch den Bürgschaftsvertrag verpflichtet sich der Bürge gegenüber dem **Gläubiger eines Dritten**, für die Erfüllung von dessen Verbindlichkeit einzustehen. Die Bürgschaft kann auch für eine künftige oder bedingte Verbindlichkeit übernommen werden (§ 765 Abs. 2 BGB).

**Form (§ 766 BGB):** Zur Gültigkeit ist die **schriftliche Erteilung** der Bürgschaftserklärung erforderlich. Die Erteilung in **elektronischer Form ist ausgeschlossen** — eine per E-Mail oder mit qualifizierter elektronischer Signatur erteilte Bürgschaft ist formnichtig (§ 125 BGB). Der Formmangel wird geheilt, soweit der Bürge die Hauptverbindlichkeit erfüllt (§ 766 S. 3 BGB).

**Ausnahme für Kaufleute ([§ 350 HGB](https://www.gesetze-im-internet.de/hgb/__350.html)):** Ist die Bürgschaft auf Seiten des Bürgen ein **Handelsgeschäft**, findet § 766 BGB keine Anwendung — die Bürgschaft ist dann formfrei wirksam.

### 3. Bürgschaft — Einreden und Ausgestaltung ([§ 771 BGB](https://www.gesetze-im-internet.de/bgb/__771.html), [§ 773 BGB](https://www.gesetze-im-internet.de/bgb/__773.html))

- **Einrede der Vorausklage** (§ 771 BGB): Der Bürge kann die Befriedigung verweigern, solange der Gläubiger nicht eine **Zwangsvollstreckung gegen den Hauptschuldner ohne Erfolg versucht** hat. Das macht die einfache Bürgschaft für den Gläubiger praktisch wertlos.
- **Selbstschuldnerische Bürgschaft** ([§ 773 Abs. 1 Nr. 1 BGB](https://www.gesetze-im-internet.de/bgb/__773.html)): Die Einrede der Vorausklage entfällt, wenn der Bürge **auf sie verzichtet**, insbesondere wenn er sich als **Selbstschuldner** verbürgt. Kraft Gesetzes entfällt sie auch, wenn die Bürgschaft für den Bürgen ein Handelsgeschäft ist (§ 349 HGB).
- **Akzessorische Einreden** (§ 768 BGB): Der Bürge kann die dem Hauptschuldner zustehenden Einreden geltend machen, auch die Verjährungseinrede — und zwar selbst dann, wenn der Hauptschuldner auf sie verzichtet hat.
- **Einrede der Anfechtbarkeit und Aufrechenbarkeit** (§ 770 BGB).
- **Legalzession** (§ 774 BGB): Soweit der Bürge den Gläubiger befriedigt, geht die Forderung auf ihn über.

**Klauselbaustein Höchstbetragsbürgschaft:**

> „Der Bürge verbürgt sich hiermit selbstschuldnerisch unter **Verzicht auf die Einrede der Vorausklage (§ 771 BGB)** für alle bestehenden und künftigen Ansprüche des Gläubigers gegen [Hauptschuldner] aus [konkrete Bezeichnung des Rechtsverhältnisses]. Die Bürgschaft ist auf einen **Höchstbetrag von [Betrag] EUR** zuzüglich Zinsen und Kosten begrenzt. Die Bürgschaft ist befristet bis zum [Datum]; nach Fristablauf haftet der Bürge nur für bis dahin entstandene Ansprüche."

**Die Höchstbetragsangabe ist bei Bürgschaften von Privatpersonen, insbesondere von Gesellschafter-Geschäftsführern und Angehörigen, praktisch unverzichtbar.** Eine Globalbürgschaft „für alle bestehenden und künftigen Ansprüche" ohne Betragsgrenze ist in AGB regelmäßig nach § 307 BGB unwirksam. Bei einer **Angehörigenbürgschaft** ohne wirtschaftliches Eigeninteresse und bei krasser finanzieller Überforderung kommt zudem Sittenwidrigkeit nach § 138 Abs. 1 BGB in Betracht `[unverifiziert – prüfen]`.

### 4. Eigentumsvorbehalt ([§ 449 BGB](https://www.gesetze-im-internet.de/bgb/__449.html))

Hat sich der Verkäufer einer beweglichen Sache das Eigentum bis zur Zahlung des Kaufpreises vorbehalten, ist im Zweifel anzunehmen, dass das Eigentum unter der **aufschiebenden Bedingung** vollständiger Zahlung übertragen wird (§ 449 Abs. 1 BGB). Der Vorbehalt muss **spätestens bei Übergabe** vereinbart sein — ein erst auf der Rechnung erscheinender Vorbehalt geht ins Leere.

| Form | Inhalt | Grenze |
|---|---|---|
| **Einfacher EV** | Eigentum bis zur Zahlung des Kaufpreises dieser Lieferung | Aussonderung § 47 InsO |
| **Verlängerter EV** | Vorausabtretung der Forderung aus dem Weiterverkauf + Verarbeitungsklausel (§ 950 BGB) | Kollision mit Globalzession der Bank |
| **Erweiterter EV** | Eigentum bis zur Tilgung **aller** Forderungen aus der Geschäftsverbindung („Kontokorrentvorbehalt") | Zulässig im B2B; **Konzernvorbehalt unwirksam** (§ 449 Abs. 3 BGB) |

**§ 449 Abs. 3 BGB:** Die Vereinbarung eines Eigentumsvorbehalts ist **nichtig**, soweit der Eigentumsübergang davon abhängig gemacht wird, dass der Käufer Forderungen eines **Dritten**, insbesondere eines mit dem Verkäufer verbundenen Unternehmens, erfüllt (Verbot des Konzernvorbehalts).

**Klauselbaustein verlängerter Eigentumsvorbehalt:**

> „(1) Die gelieferte Ware bleibt bis zur vollständigen Bezahlung sämtlicher Forderungen aus der Geschäftsverbindung Eigentum des Verkäufers. (2) Der Käufer ist berechtigt, die Vorbehaltsware im ordentlichen Geschäftsgang weiterzuveräußern. Er tritt bereits jetzt sämtliche Forderungen aus der Weiterveräußerung in Höhe des Rechnungsendbetrags der Vorbehaltsware an den Verkäufer ab; der Verkäufer nimmt die Abtretung an. (3) Der Käufer bleibt zur Einziehung der abgetretenen Forderungen ermächtigt, solange er seinen Zahlungsverpflichtungen nachkommt. (4) Verarbeitet der Käufer die Vorbehaltsware, so erfolgt die Verarbeitung für den Verkäufer als Hersteller im Sinne des § 950 BGB; der Verkäufer erwirbt Miteigentum im Verhältnis des Rechnungswerts der Vorbehaltsware zum Wert der neuen Sache."

### 5. Sicherungsübereignung ([§§ 929, 930 BGB](https://www.gesetze-im-internet.de/bgb/__930.html))

Die Übereignung erfolgt nach § 929 S. 1 BGB, wobei die Übergabe durch ein **Besitzkonstitut** nach [§ 930 BGB](https://www.gesetze-im-internet.de/bgb/__930.html) ersetzt wird: Der Sicherungsgeber bleibt unmittelbarer Besitzer und darf die Sache weiter nutzen. Voraussetzungen:

- **Bestimmtheitsgrundsatz:** Der Sicherungsgegenstand muss für jeden Dritten allein anhand der Vereinbarung **eindeutig identifizierbar** sein. Bei Warenlagern genügt die **Raumsicherungsübereignung** („sämtliche im Lagerraum A des Betriebsgrundstücks [Adresse] befindlichen Waren"); eine Umschreibung nach Wertgrenzen („Waren im Wert von 100.000 EUR") ist **unbestimmt und damit unwirksam**.
- **Konkretes Besitzmittlungsverhältnis** (Verwahrung, Leihe) — nicht bloß „der Sicherungsgeber verwahrt für den Sicherungsnehmer".
- **Sicherungsabrede** mit Verwertungsbedingungen, Verwertungserlösabrechnung und Rückübertragungsanspruch.
- **Gutgläubiger Erwerb** durch den Sicherungsnehmer nach § 933 BGB scheidet bei § 930 BGB praktisch aus, weil er die Übergabe voraussetzt — bei fremden Sachen im Lager (Vorbehaltsware!) erwirbt der Sicherungsnehmer nichts.

### 6. Sicherungsabtretung und Globalzession ([§ 398 BGB](https://www.gesetze-im-internet.de/bgb/__398.html))

Die Sicherungsabtretung überträgt die Forderung mit dinglicher Wirkung; die Zweckbindung folgt aus der Sicherungsabrede. **Stille Zession** (ohne Anzeige an den Drittschuldner) ist der Regelfall — der Schuldnerschutz des § 407 BGB gilt dann zugunsten des Drittschuldners.

**Globalzession** ist die Abtretung aller gegenwärtigen und künftigen Forderungen aus einem bestimmten Geschäftskreis. Anforderungen:

- **Bestimmbarkeit** der abgetretenen Forderungen im Zeitpunkt ihrer Entstehung (Kundenkreis, Zeitraum, Rechtsgrund).
- **Konflikt mit dem verlängerten Eigentumsvorbehalt:** Eine Globalzession, die auch die Forderungen aus dem Weiterverkauf von Vorbehaltsware erfasst, verleitet den Sicherungsgeber zum **Vertragsbruch** gegenüber seinen Lieferanten und ist deshalb nach § 138 Abs. 1 BGB **sittenwidrig und nichtig**, sofern sie keine **dingliche Teilverzichtsklausel** enthält, die die Vorbehaltsforderungen von vornherein ausnimmt `[unverifiziert – prüfen]`. Eine bloß schuldrechtliche Freigabeverpflichtung genügt nach h.M. nicht.

### 7. Übersicherung und Freigabeanspruch

- **Anfängliche Übersicherung:** Steht bereits bei Vertragsschluss fest, dass der realisierbare Wert der Sicherheiten die gesicherte Forderung erheblich übersteigt, ist die Sicherungsabrede nach § 138 Abs. 1 BGB **nichtig**.
- **Nachträgliche Übersicherung:** Entsteht das Missverhältnis erst später (typisch bei revolvierenden Sicherheiten wie Warenlager und Globalzession), folgt aus der Sicherungsabrede ein **ermessensunabhängiger Freigabeanspruch** — auch ohne ausdrückliche Freigabeklausel. Als Deckungsgrenze werden in der Praxis rund **110 % des Nennwerts** der gesicherten Forderung (bezogen auf den realisierbaren Wert) diskutiert `[unverifiziert – prüfen]`.
- Eine Freigabeklausel, die die Freigabe in das **Ermessen des Sicherungsnehmers** stellt oder eine Deckungsgrenze nach Nennwerten deutlich oberhalb dieses Rahmens festsetzt, ist nach § 307 BGB unwirksam.

**Klauselbaustein Freigabe:** „Übersteigt der realisierbare Wert der Sicherheiten die gesicherten Forderungen um mehr als 10 %, ist der Sicherungsnehmer auf Verlangen des Sicherungsgebers verpflichtet, Sicherheiten nach seiner Wahl in Höhe des übersteigenden Betrags **freizugeben**."

## Quellen

### Statute

- [§ 765 BGB](https://www.gesetze-im-internet.de/bgb/__765.html), [§ 766 BGB](https://www.gesetze-im-internet.de/bgb/__766.html), [§ 767 BGB](https://www.gesetze-im-internet.de/bgb/__767.html), [§ 768 BGB](https://www.gesetze-im-internet.de/bgb/__768.html), [§ 771 BGB](https://www.gesetze-im-internet.de/bgb/__771.html), [§ 773 BGB](https://www.gesetze-im-internet.de/bgb/__773.html), [§ 778 BGB](https://www.gesetze-im-internet.de/bgb/__778.html)
- [§ 449 BGB](https://www.gesetze-im-internet.de/bgb/__449.html) (Eigentumsvorbehalt)
- [§ 398 BGB](https://www.gesetze-im-internet.de/bgb/__398.html), [§ 929 BGB](https://www.gesetze-im-internet.de/bgb/__929.html), [§ 930 BGB](https://www.gesetze-im-internet.de/bgb/__930.html), [§ 932 BGB](https://www.gesetze-im-internet.de/bgb/__932.html)
- [§ 138 BGB](https://www.gesetze-im-internet.de/bgb/__138.html), [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html)
- [§ 350 HGB](https://www.gesetze-im-internet.de/hgb/__350.html)

### Kommentare

- Grüneberg, BGB, 83. Aufl. 2024, §§ 449, 765, 766, 930 Rn. 1 ff. `[unverifiziert – Auflagenstand prüfen]`
- Habersack, in: MüKoBGB, 8. Aufl. 2020, § 765 Rn. 1 ff., § 766 Rn. 1 ff.
- Ganter, in: Schimansky/Bunte/Lwowski, Bankrechts-Handbuch, 6. Aufl. 2022, §§ 90 ff. (Sicherungsübereignung, Globalzession)

### Rechtsprechung

- BGH (Großer Senat für Zivilsachen), Beschl. v. 27.11.1997 – GSZ 1/97 und GSZ 2/97 (nachträgliche Übersicherung, ermessensunabhängiger Freigabeanspruch) `[unverifiziert – prüfen]`
- BGH, Urt. v. 09.02.1994 – VIII ZR 176/92 (Vertragsbruchtheorie, Kollision Globalzession / verlängerter Eigentumsvorbehalt) `[unverifiziert – prüfen]`

> Beide Fundstellen vor Verwendung in juris / Beck-Online prüfen. Die Deckungsgrenzen und die Vertragsbruchtheorie sind hier nach dem Stand der Kommentarliteratur wiedergegeben; die konkrete Prozentgrenze ist einzelfallabhängig.

## Ausgabeformat

```
SICHERHEITEN — <Forderung / Mandat> — <Datum>

I.    Zu sichernde Forderung          <Betrag, Rechtsgrund, Laufzeit>
II.   Gewähltes Instrument            [Bürgschaft / EV / Sicherungsübereignung / Zession / Grundpfandrecht]
        Akzessorisch:                 [ja / nein — Sicherungsabrede erforderlich]
III.  Bürgschaft                      [selbstschuldnerisch § 773 / einfach § 771]
        Form § 766 / § 350 HGB:       [✅ Schriftform / ❌ elektronisch / N/A Handelsgeschäft]
        Höchstbetrag:                 <Betrag> / ❌ unbegrenzt
IV.   Eigentumsvorbehalt (§ 449)      [einfach / verlängert / erweitert]
        Konzernvorbehalt § 449 III:   [❌ nicht enthalten / 🔴 unwirksam]
V.    Sicherungsübereignung           [Bestimmtheit ✅/❌ — Raumsicherung?]
        Besitzkonstitut § 930:        <konkretes Rechtsverhältnis>
VI.   Sicherungsabtretung / Zession   [still / offen; Global-/Einzelzession]
        Kollision verlängerter EV:    [🔴 ohne dingliche Teilverzichtsklausel / ✅ enthalten]
        § 354a HGB einschlägig:       [ja / nein]
VII.  Übersicherung                   [anfänglich 🔴 / nachträglich — Deckungsgrenze <…> %]
        Freigabeklausel:              [✅ ermessensunabhängig / ❌ Ermessen]
VIII. Insolvenzfestigkeit             [Aussonderung § 47 InsO / Absonderung § 51 InsO]

Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Tatsachen: <Liste>
```

## Risiken / typische Fehler

- **Bürgschaft per E-Mail eingeholt** — § 766 S. 2 BGB schließt die elektronische Form aus; die Bürgschaft ist formnichtig, außer § 350 HGB greift.
- **Einrede der Vorausklage nicht abbedungen** — ohne selbstschuldnerische Ausgestaltung (§ 773 Abs. 1 Nr. 1 BGB) muss der Gläubiger erst erfolglos gegen den Hauptschuldner vollstrecken.
- **Globalbürgschaft ohne Höchstbetrag** — in AGB nach § 307 BGB unwirksam; bei Angehörigen kommt Sittenwidrigkeit nach § 138 Abs. 1 BGB hinzu.
- **Eigentumsvorbehalt erst auf der Rechnung** vereinbart — er muss spätestens bei Übergabe bestehen und geht sonst ins Leere.
- **Konzernvorbehalt vereinbart** — nach § 449 Abs. 3 BGB nichtig, soweit der Eigentumsübergang von Forderungen eines verbundenen Unternehmens abhängig gemacht wird.
- **Sicherungsübereignung nach Wertgrenzen** statt nach Raum oder Bestand formuliert — Verstoß gegen den Bestimmtheitsgrundsatz, die Sicherheit ist unwirksam.
- **Globalzession ohne dingliche Teilverzichtsklausel** — Kollision mit dem verlängerten Eigentumsvorbehalt der Lieferanten, Nichtigkeit nach § 138 Abs. 1 BGB.

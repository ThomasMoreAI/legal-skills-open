---
name: immobiliarvollstreckung-zvg-borghei
title: /zwangsvollstreckung:immobiliarvollstreckung-zvg
description: Zwangsvollstreckung in das unbewegliche Vermögen nach dem ZVG – Anordnung der Zwangsversteigerung § 15 ZVG, Beitritt § 27 ZVG, Verkehrswertfestsetzung § 74a Abs. 5 ZVG, geringstes Gebot und Deckungsgrundsatz §§ 44, 52 ZVG, Zuschlag § 81 ZVG, die 7/10-Grenze § 74a und die 5/10-Grenze § 85a ZVG, Versagungsgründe § 83 ZVG, einstweilige Einstellung § 30a ZVG, Zwangsverwaltung §§ 146 ff. ZVG, Zwangshypothek § 867 ZPO sowie die Teilungsversteigerung § 180 ZVG bei Erbengemeinschaft und Scheidung. Use when aus einem Titel oder einer Grundschuld in Grundbesitz vollstreckt, ein Versteigerungstermin vorbereitet oder abgewehrt oder eine Gemeinschaft durch Teilungsversteigerung aufgelöst werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/zwangsvollstreckung/skills/immobiliarvollstreckung-zvg
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /zwangsvollstreckung:immobiliarvollstreckung-zvg

## Zweck

Die Immobiliarvollstreckung ist die langsamste, aber die durchsetzungsstärkste Zugriffsform: Sie erfasst den regelmäßig wertvollsten Vermögensgegenstand und endet mit einem Zuschlag, der Eigentum überträgt. Ihr Verfahren folgt nicht der ZPO, sondern dem **ZVG** — mit eigenen Fristen, eigenen Wertgrenzen und einem Rangsystem, das über Erfolg oder Totalausfall des Gläubigers entscheidet. Dieser Skill plant das Verfahren aus Gläubigersicht, entwickelt die Verteidigungslinien des Schuldners und behandelt die Teilungsversteigerung als eigenständigen Auflösungsmechanismus.

## Eingaben

- **Verfahrensziel**: Zwangsversteigerung, Zwangsverwaltung, Zwangshypothek, Teilungsversteigerung
- **Titel** und Vollstreckungsvoraussetzungen — geprüft nach `/zwangsvollstreckung:vollstreckungsvoraussetzungen`; bei dinglicher Vollstreckung die Grundschuldurkunde mit Unterwerfung
- **Grundbuchauszug** vollständig: Bestandsverzeichnis, Abteilung I, II und III mit Rangfolge und Valutastand
- **Verkehrswert**: vorhandenes Gutachten, Festsetzungsbeschluss, eigene Einschätzung
- **Nutzung**: selbstgenutzt, vermietet (Mietverträge, Kautionen), gewerblich, unbebaut
- Bei Teilungsversteigerung: Gemeinschaftsverhältnis (Erbengemeinschaft, Bruchteil, Gütergemeinschaft), Beteiligte, Verfügungsbeschränkungen
- Auf Schuldnerseite: Zahlungsfähigkeit, Verkaufsbemühungen, gesundheitliche und soziale Umstände

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) beschafft das ZVG mit URL, die flankierenden ZPO-Normen und Kommentarstellen (Stöber ZVG, Dassler/Schiffhauer, Böttcher).
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt Versteigerungs-, Beitritts- oder Einstellungsantrag und die Terminvorbereitung.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Rang, geringstes Gebot, Wertgrenzen, Fristen und Versagungsgründe.

## Ablauf

### 1. Anordnung der Zwangsversteigerung ([§ 15 ZVG](https://www.gesetze-im-internet.de/zvg/__15.html))

Die Zwangsversteigerung wird vom **Vollstreckungsgericht** — dem Amtsgericht der belegenen Sache — auf Antrag angeordnet. Der Antrag setzt die allgemeinen Vollstreckungsvoraussetzungen voraus; bei der **dinglichen** Vollstreckung aus einer Grundschuld tritt an die Stelle des Urteils die notarielle Urkunde mit Unterwerfungserklärung nach § 794 Abs. 1 Nr. 5 ZPO (Querverweis: `/immobilien-grundbuchrecht:grundschuld-sicherungsrecht`). Die Anordnung wirkt als **Beschlagnahme** ([§ 20 ZVG](https://www.gesetze-im-internet.de/zvg/__20.html)); sie wird im Grundbuch als **Versteigerungsvermerk** eingetragen und erfasst das Grundstück nebst Zubehör und den Miet- und Pachtzinsforderungen. Verfügungen des Schuldners nach der Beschlagnahme sind dem betreibenden Gläubiger gegenüber relativ unwirksam.

Als milderes Mittel steht die **Zwangshypothek** ([§ 867 ZPO](https://www.gesetze-im-internet.de/zpo/__867.html)) zur Verfügung: Sie sichert den Rang, ohne das Verfahren zu betreiben, und ist ab dem gesetzlichen Mindestbetrag eintragungsfähig.

### 2. Beitritt ([§ 27 ZVG](https://www.gesetze-im-internet.de/zvg/__27.html))

Ist das Verfahren bereits angeordnet, tritt ein weiterer Gläubiger durch **Beitritt** bei; der Beitritt steht der Anordnung gleich und bewirkt eine eigene Beschlagnahme zu seinen Gunsten. Das ist strategisch entscheidend: Der Beitretende ist nicht mehr davon abhängig, ob der zuerst betreibende Gläubiger sein Verfahren fortführt oder zurücknimmt. Wer nur zusieht, verliert bei Rücknahme alles und muss neu anordnen lassen — mit neuem Rang.

### 3. Verkehrswertfestsetzung ([§ 74a Abs. 5 ZVG](https://www.gesetze-im-internet.de/zvg/__74a.html))

Das Gericht setzt den **Verkehrswert** durch Beschluss fest, regelmäßig nach Einholung eines Sachverständigengutachtens; die Beteiligten sind zuvor zu hören. Der Beschluss ist mit der **sofortigen Beschwerde** anfechtbar. Er ist die Bezugsgröße für beide Wertgrenzen des Verfahrens — ein zu niedrig festgesetzter Wert senkt die Schwellen, unterhalb derer der Zuschlag zu versagen ist, und schadet damit unmittelbar dem Schuldner und den nachrangigen Gläubigern. Die Einwendungen gegen das Gutachten (Bausubstanz, Mietsituation, Vergleichswerte) gehören deshalb **in das Festsetzungsverfahren**, nicht in den Versteigerungstermin.

### 4. Geringstes Gebot und Deckungsgrundsatz ([§ 44 ZVG](https://www.gesetze-im-internet.de/zvg/__44.html), [§ 52 ZVG](https://www.gesetze-im-internet.de/zvg/__52.html))

Es wird nur ein Gebot zugelassen, durch das die dem Anspruch des betreibenden Gläubigers **vorgehenden Rechte** sowie die Verfahrenskosten gedeckt werden — das **geringste Gebot** (§ 44 Abs. 1 ZVG). Es besteht aus zwei Teilen:

- dem **bar zu zahlenden Teil**: Verfahrenskosten und vorrangige Ansprüche der Rangklassen des [§ 10 ZVG](https://www.gesetze-im-internet.de/zvg/__10.html), die auf Geld gerichtet sind — darunter in Rangklasse 2 die Hausgeldansprüche der Wohnungseigentümergemeinschaft im gesetzlich begrenzten Umfang und in Rangklasse 3 die öffentlichen Lasten,
- dem **bestehen bleibenden Teil**: die dem betreibenden Anspruch vorgehenden Rechte in Abteilung II und III bleiben nach § 52 ZVG bestehen und sind vom Ersteher zu übernehmen.

Daraus folgt die praktische Kernregel: **Der Rang entscheidet.** Ein nachrangiger Gläubiger, dessen Recht hinter hohen valutierenden Grundschulden steht, betreibt ein Verfahren, in dem das geringste Gebot bereits über dem Verkehrswert liegen kann — dann findet sich kein Bieter, und das Verfahren ist wirtschaftlich sinnlos. Vor jedem Antrag ist deshalb das geringste Gebot aus dem Grundbuch zu rekonstruieren.

### 5. Die Wertgrenzen: 7/10 und 5/10 ([§ 74a ZVG](https://www.gesetze-im-internet.de/zvg/__74a.html), [§ 85a ZVG](https://www.gesetze-im-internet.de/zvg/__85a.html))

Zwei Schutzschwellen begrenzen die Verschleuderung im **ersten** Termin:

- **7/10-Grenze (§ 74a ZVG):** Bleibt das Meistgebot einschließlich des Kapitalwerts der bestehen bleibenden Rechte unter **sieben Zehnteln des Verkehrswerts**, kann ein Beteiligter, dessen Recht durch den Zuschlag ganz oder teilweise erlöschen würde und der bei Verteilung nicht voll gedeckt wäre, die **Versagung des Zuschlags** beantragen. Der Antrag ist im Termin zu stellen.
- **5/10-Grenze (§ 85a ZVG):** Bleibt das Meistgebot unter **fünf Zehnteln des Verkehrswerts**, ist der Zuschlag **von Amts wegen** zu versagen. Kein Antrag erforderlich.

Beide Grenzen gelten nur im ersten Termin: Wird der Zuschlag aus diesen Gründen versagt, entfallen sie im **neuen Termin** (§ 74a Abs. 4, § 85a Abs. 2 ZVG). Genau darin liegt die häufigste Fehlvorstellung — die Grenzen schützen den Schuldner nicht dauerhaft, sondern verschaffen ihm nur eine zweite Chance, in der er das Objekt freihändig verkaufen oder die Forderung ablösen muss.

### 6. Zuschlag und Versagungsgründe ([§ 81 ZVG](https://www.gesetze-im-internet.de/zvg/__81.html), [§ 83 ZVG](https://www.gesetze-im-internet.de/zvg/__83.html))

Der **Zuschlag** ist dem Meistbietenden zu erteilen (§ 81 Abs. 1 ZVG); er ist **Hoheitsakt** und überträgt das Eigentum originär — nicht abgeleitet vom Schuldner. Deshalb erwirbt der Ersteher lastenfrei, soweit die Rechte nicht nach § 52 ZVG bestehen bleiben, und § 91 ZVG lässt die erlöschenden Rechte untergehen. Der Zuschlagsbeschluss ist zugleich **Räumungstitel** gegen den Schuldner ([§ 93 ZVG](https://www.gesetze-im-internet.de/zvg/__93.html)); bestehende **Mietverhältnisse** gehen nach § 566 BGB über, der Ersteher hat aber ein Sonderkündigungsrecht nach § 57a ZVG.

§ 83 ZVG zählt die **Versagungsgründe** auf, darunter Verfahrensfehler bei Terminsbestimmung und Bekanntmachung, die fehlende Zulassung eines Beteiligten, die Nichtbeachtung des geringsten Gebots und der Fall des § 85a ZVG. Gegen den Zuschlag ist die **sofortige Beschwerde** nach [§ 96 ZVG](https://www.gesetze-im-internet.de/zvg/__96.html) statthaft; die Frist beträgt zwei Wochen. Nach Rechtskraft wird der Erlös im **Verteilungstermin** nach den Rangklassen des § 10 ZVG verteilt.

### 7. Einstweilige Einstellung ([§ 30a ZVG](https://www.gesetze-im-internet.de/zvg/__30a.html)) und Zwangsverwaltung ([§ 146 ZVG](https://www.gesetze-im-internet.de/zvg/__146.html))

**§ 30a ZVG** ist die wichtigste Verteidigungslinie des Schuldners: Das Verfahren wird auf Antrag **einstweilen eingestellt**, wenn Aussicht besteht, dass durch die Einstellung die Versteigerung vermieden wird, und die Einstellung dem Gläubiger unter Berücksichtigung seiner wirtschaftlichen Verhältnisse zuzumuten ist. Die Einstellung erfolgt für höchstens **sechs Monate**; der Antrag ist innerhalb von **zwei Wochen** ab Zustellung des Anordnungsbeschlusses zu stellen (§ 30b ZVG). Typische Begründung: ein konkret belegter freihändiger Verkauf zu einem Preis über dem zu erwartenden Versteigerungserlös. Daneben bleibt der allgemeine Vollstreckungsschutz nach [§ 765a ZPO](https://www.gesetze-im-internet.de/zpo/__765a.html) anwendbar.

**Zwangsverwaltung** (§§ 146 ff. ZVG): Statt das Objekt zu verwerten, greift der Gläubiger auf die **Nutzungen** zu. Ein gerichtlich bestellter Zwangsverwalter zieht Mieten ein, bewirtschaftet das Objekt und schüttet nach Abzug der Kosten an die Gläubiger aus. Sinnvoll bei ertragsstarken vermieteten Objekten, bei ungünstigem Marktumfeld und **kumulativ** neben der Zwangsversteigerung — beide Verfahren können nebeneinander laufen.

### 8. Teilungsversteigerung ([§ 180 ZVG](https://www.gesetze-im-internet.de/zvg/__180.html))

Die Teilungsversteigerung ist keine Vollstreckung gegen einen Schuldner, sondern die **Aufhebung einer Gemeinschaft** an einem Grundstück durch Verwertung — sie setzt deshalb **keinen Titel** voraus, sondern nur die Stellung als Miteigentümer oder Miterbe. Antragsberechtigt ist jeder Teilhaber; Grundlage ist der Anspruch auf Aufhebung der Gemeinschaft nach [§ 749 BGB](https://www.gesetze-im-internet.de/bgb/__749.html) bzw. [§ 2042 BGB](https://www.gesetze-im-internet.de/bgb/__2042.html).

Zwei Konstellationen dominieren:

- **Erbengemeinschaft**: Ein Miterbe erzwingt die Auseinandersetzung über das Nachlassgrundstück. Zu prüfen sind Teilungsanordnungen des Erblassers, ein Auseinandersetzungsverbot nach [§ 2044 BGB](https://www.gesetze-im-internet.de/bgb/__2044.html) und die Testamentsvollstreckung. Vertiefung: `/erbrecht:gesetzliche-erbfolge`.
- **Scheidung / Trennung**: Ein Ehegatte betreibt die Versteigerung des gemeinsamen Hauses. Hier greift die **Verfügungsbeschränkung des § 1365 BGB**: Das Zustimmungserfordernis zur Gesamtvermögensverfügung gilt auch für den Antrag auf Anordnung der Teilungsversteigerung (BGH, Beschl. v. 14.06.2007 – V ZB 102/06 — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2007-06-14&Aktenzeichen=V%20ZB%20102/06). Fehlt die Zustimmung, ist der Antrag zurückzuweisen. Daneben ist § 1353 BGB als Schranke gegen die Unzeit zu prüfen. Vertiefung: `/familienrecht:scheidung-zugewinnausgleich`.

Verfahrensbesonderheiten: Nach [§ 182 ZVG](https://www.gesetze-im-internet.de/zvg/__182.html) bleiben grundsätzlich **alle eingetragenen Rechte bestehen** — das geringste Gebot ist entsprechend hoch. Nach [§ 181 ZVG](https://www.gesetze-im-internet.de/zvg/__181.html) finden die Vorschriften über die Zwangsversteigerung entsprechende Anwendung. Der Erlös tritt an die Stelle des Grundstücks und wird unter den Teilhabern verteilt; jeder Teilhaber darf **mitbieten** und so das Objekt erwerben. Die Wertgrenzen der §§ 74a, 85a ZVG gelten hier nicht in gleicher Weise — das ist der Grund, weshalb die Teilungsversteigerung als Druckmittel gefürchtet ist und weshalb eine einvernehmliche Lösung fast immer wirtschaftlich überlegen ist.

## Deterministische Berechnung

Die Verfahrensfristen des ZVG sind **Ereignisfristen** nach [§ 187 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__187.html); das Fristende verschiebt sich nach [§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html) auf den nächsten Werktag. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur die Arithmetik** — Zustellung des Anordnungsbeschlusses und Terminsbekanntmachung bleiben juristische Eingaben und sind gesondert nachzuweisen.

```bash
# Zwei-Wochen-Frist des Einstellungsantrags § 30b ZVG ab Zustellung der Anordnung
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 2 --einheit wochen --land BY

# Sofortige Beschwerde gegen den Zuschlag § 96 ZVG
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 2 --einheit wochen --land BY

# Höchstdauer der einstweiligen Einstellung § 30a ZVG
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 6 --einheit monate --land BY

# Kosten eines Verfahrens über die Aufhebung der Gemeinschaft (Geschäftswert)
python -m scripts.legal_calc.cli gkg --wert 320000 --faktor 3.0
```

**Nicht mit dem Rechner zu ermitteln** sind der Verkehrswert, das geringste Gebot und die Kapitalisierung bestehen bleibender Rechte. Die 7/10- und 5/10-Grenzen sind einfache Prozentsätze des **festgesetzten** Verkehrswerts; maßgeblich ist stets der Festsetzungsbeschluss nach § 74a Abs. 5 ZVG, nicht eine eigene Schätzung. Die ZVG-Gerichtskosten folgen dem GKG-Kostenverzeichnis für Zwangsversteigerungssachen und sind gesondert abzulesen.

## Quellen

### Statute

- [§ 15 ZVG](https://www.gesetze-im-internet.de/zvg/__15.html), [§ 20 ZVG](https://www.gesetze-im-internet.de/zvg/__20.html), [§ 27 ZVG](https://www.gesetze-im-internet.de/zvg/__27.html), [§ 30a ZVG](https://www.gesetze-im-internet.de/zvg/__30a.html), [§ 33 ZVG](https://www.gesetze-im-internet.de/zvg/__33.html)
- [§ 10 ZVG](https://www.gesetze-im-internet.de/zvg/__10.html), [§ 44 ZVG](https://www.gesetze-im-internet.de/zvg/__44.html), [§ 52 ZVG](https://www.gesetze-im-internet.de/zvg/__52.html), [§ 74a ZVG](https://www.gesetze-im-internet.de/zvg/__74a.html), [§ 81 ZVG](https://www.gesetze-im-internet.de/zvg/__81.html), [§ 83 ZVG](https://www.gesetze-im-internet.de/zvg/__83.html), [§ 85a ZVG](https://www.gesetze-im-internet.de/zvg/__85a.html), [§ 91 ZVG](https://www.gesetze-im-internet.de/zvg/__91.html)
- [§ 146 ZVG](https://www.gesetze-im-internet.de/zvg/__146.html) (Zwangsverwaltung), [§ 180 ZVG](https://www.gesetze-im-internet.de/zvg/__180.html), [§ 181 ZVG](https://www.gesetze-im-internet.de/zvg/__181.html), [§ 182 ZVG](https://www.gesetze-im-internet.de/zvg/__182.html)
- [§ 867 ZPO](https://www.gesetze-im-internet.de/zpo/__867.html) (Zwangshypothek), [§ 765a ZPO](https://www.gesetze-im-internet.de/zpo/__765a.html); [§ 749 BGB](https://www.gesetze-im-internet.de/bgb/__749.html), [§ 2042 BGB](https://www.gesetze-im-internet.de/bgb/__2042.html), [§ 2044 BGB](https://www.gesetze-im-internet.de/bgb/__2044.html), [§ 1365 BGB](https://www.gesetze-im-internet.de/bgb/__1365.html)

### Kommentare

- Stöber, ZVG, 23. Aufl. 2022, § 44 Rn. 1 ff.; § 74a Rn. 1 ff.; § 180 Rn. 1 ff.
- Dassler/Schiffhauer/Hintzen, ZVG, 16. Aufl. 2020, § 30a Rn. 1 ff.
- Böttcher, ZVG, 7. Aufl. 2022, § 85a Rn. 1 ff.
- Kindl/Meller-Hannich, Gesamtes Recht der Zwangsvollstreckung, 4. Aufl. 2021, § 180 ZVG Rn. 1 ff.

### Rechtsprechung

- BGH, Beschl. v. 14.06.2007 – V ZB 102/06 (Zustimmungserfordernis des § 1365 Abs. 1 BGB gilt auch für den Antrag auf Anordnung der Teilungsversteigerung; § 181 ZVG) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2007-06-14&Aktenzeichen=V%20ZB%20102/06
- Zu den Anforderungen an die Erfolgsaussicht eines freihändigen Verkaufs im Rahmen des § 30a ZVG ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.
- Zur Anwendung der Wertgrenzen der §§ 74a, 85a ZVG im wiederholten Termin ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`. Kein Aktenzeichen ohne eigene Verifikation in juris / Beck-Online übernehmen.

## Formulierungshilfe — Versteigerungs-, Einstellungs- und Teilungsversteigerungsantrag

```
An das Amtsgericht <Ort> — Vollstreckungsgericht —

Antrag auf Anordnung der Zwangsversteigerung (§ 15 ZVG)

Gläubigerin: <…>            Schuldner: <…>
Grundbesitz: Grundbuch von <Gemarkung>, Blatt <Nr.>, Flurstück <…>

Die Gläubigerin betreibt die Zwangsvollstreckung aus <Titel / Grundschuld
Abt. III lfd. Nr. <…>, notarielle Urkunde vom <Datum>, UR-Nr. <…>, mit
Unterwerfungserklärung nach § 794 Abs. 1 Nr. 5 ZPO>. Die vollstreckbare
Ausfertigung nebst Zustellungsnachweis ist beigefügt; die Zustellung
erfolgte am <Datum>.

Es wird beantragt,
  1. die Zwangsversteigerung des vorbezeichneten Grundbesitzes wegen
     eines Anspruchs von <Betrag> EUR nebst <…> % Zinsen seit <Datum>
     anzuordnen,
  2. den Versteigerungsvermerk im Grundbuch eintragen zu lassen,
  3. den Verkehrswert nach § 74a Abs. 5 ZVG festzusetzen.

Hilfsweise wird der Beitritt zu dem bereits anhängigen Verfahren
<Az.> nach § 27 ZVG erklärt.
```

```
Antrag auf einstweilige Einstellung (§ 30a ZVG)

Der Anordnungsbeschluss wurde dem Schuldner am <Datum> zugestellt; die
Frist des § 30b ZVG ist gewahrt.

Es besteht Aussicht, dass durch die Einstellung die Versteigerung
vermieden wird: Der Schuldner hat den Grundbesitz mit notariell
beurkundetem Kaufvertrag vom <Datum> zu einem Kaufpreis von <Betrag> EUR
veräußert; die Finanzierungsbestätigung des Käufers vom <Datum> liegt vor
(Anlagen). Der Kaufpreis übersteigt den festgesetzten Verkehrswert von
<Betrag> EUR und deckt die Forderung der Gläubigerin vollständig. Die
Einstellung ist der Gläubigerin daher unter Berücksichtigung ihrer
wirtschaftlichen Verhältnisse zuzumuten.

Es wird beantragt, das Verfahren für die Dauer von sechs Monaten
einstweilen einzustellen.
```

```
Antrag auf Anordnung der Teilungsversteigerung (§ 180 ZVG)

Die Antragstellerin ist zu 1/2 Miteigentümerin des im Grundbuch von
<…> eingetragenen Grundbesitzes; Miteigentümer zu 1/2 ist der
Antragsgegner. Ein Titel ist nicht erforderlich; das Recht folgt aus
§ 749 BGB / § 2042 BGB.

Eine Vereinbarung über den Ausschluss der Aufhebung besteht nicht; ein
Auseinandersetzungsverbot nach § 2044 BGB liegt nicht vor.
<Bei Eheleuten:> Die Zustimmung des Antragsgegners nach § 1365 BGB liegt
vor / ist entbehrlich, weil der Grundbesitz nicht das gesamte Vermögen
der Antragstellerin ausmacht (Vermögensaufstellung, Anlage).

Es wird beantragt, die Zwangsversteigerung des vorbezeichneten
Grundbesitzes zum Zwecke der Aufhebung der Gemeinschaft anzuordnen.
Es wird darauf hingewiesen, dass nach § 182 ZVG die eingetragenen Rechte
bestehen bleiben und in das geringste Gebot aufzunehmen sind.
```

## Ausgabeformat

```
IMMOBILIARVOLLSTRECKUNG / ZVG — <Gläubiger / Schuldner / Teilhaber> — <Datum>

I.    Verfahrensziel              [Versteigerung / Verwaltung / Zwangshypothek
                                   / Teilungsversteigerung § 180 ZVG]
II.   Vollstreckungsvoraussetzung  [Titel / dingliche Urkunde § 794 I Nr. 5]
                                   Teilungsversteigerung: kein Titel nötig
III.  Anordnung § 15 ZVG           Beschluss vom <Datum>
      Beschlagnahme § 20 ZVG       Versteigerungsvermerk eingetragen <Datum>
      Beitritt § 27 ZVG            [N/A / erklärt am <Datum>]
IV.   Grundbuchlage / Rang         Abt. II: <…>   Abt. III: <…>
      Rangklasse § 10 ZVG          betreibender Anspruch: Klasse <…>
V.    Verkehrswert § 74a V ZVG     festgesetzt am <Datum>: <Betrag> EUR
      Beschwerde                   [N/A / eingelegt am <Datum>]
VI.   Geringstes Gebot §§ 44, 52   bar: <Betrag>  bestehen bleibend: <…>
      Wirtschaftlichkeit           [🟢 tragfähig / 🔴 über Verkehrswert]
VII.  Wertgrenzen                  7/10 = <Betrag>  (Antrag § 74a ZVG im Termin)
                                   5/10 = <Betrag>  (Versagung von Amts wegen)
                                   Gelten nur im ERSTEN Termin
VIII. Zuschlag § 81 ZVG            Termin <Datum>
      Versagungsgründe § 83 ZVG    <…>
      Beschwerde § 96 ZVG          Frist zwei Wochen bis <Datum>
IX.   Schuldnerschutz              § 30a ZVG Antragsfrist bis <Datum>
                                   § 765a ZPO [N/A / geltend gemacht]
X.    Zwangsverwaltung §§ 146 ff.  [N/A / parallel beantragt]
XI.   Teilungsversteigerung § 180  Gemeinschaft: [Erben / Bruchteil]
      § 1365 BGB Zustimmung        [N/A / vorliegend / 🔴 fehlt]
      §§ 2042, 2044 BGB            [N/A / Auseinandersetzungsverbot]
      § 182 ZVG                    Rechte bleiben bestehen
      Querverweise                 /erbrecht, /familienrecht
XII.  Fristen / Kosten             s. Deterministische Berechnung

Ergebnis: <antragsreif / wirtschaftlich sinnlos / Einstellung geboten>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Geringstes Gebot nicht vorab rekonstruiert** — steht der betreibende Anspruch hinter hohen valutierenden Grundschulden, liegt das geringste Gebot über dem Verkehrswert; das Verfahren findet keinen Bieter und kostet nur Geld.
- **Wertgrenzen für dauerhaft gehalten** — die 7/10- und 5/10-Grenzen der §§ 74a, 85a ZVG gelten nur im ersten Termin; im Wiederholungstermin fallen sie weg.
- **Antragsfrist des § 30b ZVG versäumt** — der Einstellungsantrag nach § 30a ZVG ist binnen zwei Wochen ab Zustellung der Anordnung zu stellen und mit einem konkret belegten Verkauf zu begründen, nicht mit allgemeiner Zahlungsbereitschaft.
- **Beitritt § 27 ZVG unterlassen** — wer nur zusieht statt beizutreten, verliert bei Rücknahme des betreibenden Gläubigers seinen Rang und muss neu anordnen lassen.
- **Einwendungen gegen den Verkehrswert erst im Termin erhoben** — sie gehören in das Festsetzungsverfahren nach § 74a Abs. 5 ZVG und in die sofortige Beschwerde gegen den Festsetzungsbeschluss.
- **§ 1365 BGB bei der Teilungsversteigerung übersehen** — betreibt ein getrennt lebender Ehegatte die Teilungsversteigerung über sein nahezu gesamtes Vermögen, ist die Zustimmung des anderen erforderlich; ohne sie ist der Antrag zurückzuweisen.
- **§ 182 ZVG verkannt** — in der Teilungsversteigerung bleiben die eingetragenen Rechte bestehen; das geringste Gebot ist entsprechend hoch, und der Erlös fällt geringer aus als erwartet.
- **Mietverhältnisse und Sonderkündigungsrecht übersehen** — der Ersteher tritt nach § 566 BGB in laufende Mietverträge ein; das Sonderkündigungsrecht des § 57a ZVG ist fristgebunden.

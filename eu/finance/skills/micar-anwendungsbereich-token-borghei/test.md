---
skill: krypto-mikar/micar-anwendungsbereich-token
fact_pattern: |
  Ein Berliner Start-up plant drei Produkte: (1) einen an den Euro
  gekoppelten Stablecoin mit jederzeitigem Rücktauschrecht, ausgegeben
  durch eine GmbH ohne Bank- oder E-Geld-Institutslizenz; (2) einen Token,
  der einen Anspruch auf anteiligen Gewinn eines Immobilienportfolios
  verbrieft und frei handelbar sein soll; (3) eine Serie von 10.000
  bildgleichen "Sammel-NFTs" mit fortlaufender Nummer, die auf einer
  Handelsplattform gelistet werden sollen. Die Geschäftsführung meint,
  alles falle unter die MiCAR und NFTs seien ohnehin ausgenommen. Eine
  BaFin-Abstimmung hat nicht stattgefunden.

must_cite:
  - "Art. 1"
  - "Art. 2"
  - "Art. 3"
  - "Art. 16"
  - "Art. 48"
  - "§ 1 KMAG"
  - "§ 5 KMAG"
  - "§ 9 KMAG"

must_appear:
  - "Finanzinstrument"
  - "vermögenswertreferenzierte"
  - "E-Geld-Token"
  - "nicht fungibel"
  - "Kreditinstitut"
  - "BaFin"
  - "sofortige"
  - "unerlaubte"
  - "legal_calc"

must_flag:
  - "MiCAR geprüft, obwohl ein Finanzinstrument vorliegt"
  - "NFT-Ausnahme pauschal bejaht"
  - "EMT und ART verwechselt"
  - "Emittentenvorbehalt des Art. 48 übersehen"
  - "§ 9 KMAG unterschätzt"
---

# Test — micar-anwendungsbereich-token

Struktureller Smoke-Test. Die Ausgabe muss Produkt (1) als E-Geld-Token einordnen und am Emittentenvorbehalt des Art. 48 scheitern lassen, Produkt (2) in der Vorrangprüfung als mögliches Finanzinstrument bzw. Investmentvermögen aus der MiCAR herausnehmen und auf MiFID II, WpHG, WpIG und KAGB verweisen, und Produkt (3) an der tatsächlichen Fungibilität der Serie messen, statt die NFT-Ausnahme des Art. 2 Abs. 3, 4 pauschal zu bejahen. Die Risiken nach § 9 KMAG einschließlich der persönlichen Adressierbarkeit von Gesellschaftern und Organen sowie die sofortige Vollziehbarkeit nach § 5 KMAG sind zu benennen.

Run: `python ../../../scripts/eval.py --skill krypto-mikar/skills/micar-anwendungsbereich-token`

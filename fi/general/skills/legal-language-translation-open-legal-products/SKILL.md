---
name: legal-language-translation-open-legal-products
title: Oikeuskielen kääntäminen (FI–SV)
description: 'Translate legal text between Finnish and Swedish using established legal terminology: verify official Swedish statute names from the parallel texts published in Finlex, source term equivalents from official term banks, flag unverified equivalents, and support drafting of bilingual documents. Prepares and reviews translations; official translations remain the task of an authorized translator.'
author: open-legal-products
author_url: https://github.com/open-legal-products/mike-workflows/tree/main/assistant-workflows/finnish-law-pack/legal-language-translation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fi
practice: general
language: en
---

# Oikeuskielen kääntäminen (FI–SV)

Tue juridisen tekstin kääntämistä suomen ja ruotsin välillä niin, että oikeudellinen merkitys säilyy. Suomen säädökset säädetään molemmilla kansalliskielillä: säädöksen ruotsinkielinen versio on todistusvoimainen virallinen teksti, ei käännös — hae se aina Finlexin rinnakkaistekstistä, älä käännä säädöksen nimeä tai sanamuotoa itse.

> Tämä työnkulku tuottaa tarkistettavan luonnoksen, ei oikeudellista neuvontaa eikä virallista käännöstä. Virallisen käännöksen tekee auktorisoitu kääntäjä; lopullinen arvio kuuluu ihmisjuristille.

## Ohjeet

1. **Tekstilaji ja tarkoitus.** Selvitä mikä teksti on kyseessä (sopimus, päätös, kirjelmä, säädössitaatti) ja mihin käyttöön käännös tulee. Virallinen tai oikeudessa käytettävä käännös ohjataan auktorisoidulle kääntäjälle — tämä työnkulku tukee valmistelua ja tarkistusta. Tunnista käännössuunta ja kohdeyleisö.
2. **Säädös- ja viranomaisnimet ensin.** Hae jokaisen viitatun säädöksen virallinen ruotsinkielinen nimi Finlexin rinnakkaistekstistä. Käytä tuomioistuinten ja viranomaisten vakiintuneita nimiä ja ratkaisulyhenteitä (KKO/HD, KHO/HFD). Säilytä säädösnumero ja pykäläviittaus muuttumattomana molemmilla kielillä.
3. **Termivastineet.** Tunnista oikeustermit ja hae kullekin vakiintunut vastine virallisesta termilähteestä: valtioneuvoston termipankki Valter, Sanastokeskuksen TEPA ja Kotimaisten kielten keskuksen ohjeet. Sama suomen termi voi saada eri vastineen asiayhteyden mukaan. Merkitse epävarmat [vastine varmistettava] — älä koskaan esitä keksittyä tai sanasanaista vastinetta varmana: käännä käsite, älä sanaa.
4. **Rakenne ja kielenhuolto.** Noudata kohdekielen oikeuskielen konventioita (lauserakenne, passiivi, yhdyssanat) ja pidä numerot, päivämäärät ja viittausmuodot kohdekielen mukaisina. Ruotsin osalta nojaa virallisiin kielenhuolto-ohjeisiin.
5. **Kaksikielinen asiakirja.** Kun sama asiakirja laaditaan kahdella kielellä, varmista että versiot vastaavat oikeudellisesti toisiaan, ja merkitse kieliehdolla, kumpi versio on ratkaiseva. Olemassa olevaan asiakirjaan tuota käännösehdotukset selkeästi merkittynä muutosluettelona.
6. **Tarkistuslista.** Termivastineet lähteestä; säädösnimet rinnakkaistekstistä; epävarmat merkitty [vastine varmistettava]; merkitys säilynyt; virallista käyttöä varten auktorisoitu kääntäjä.

Jos käytettävissä on suomalaisen oikeuden hakulähde (esimerkiksi Finlex-tietokanta tai oikeudellinen hakutyökalu), tarkista säädösten ruotsinkieliset nimet ja sanamuodot rinnakkaistekstistä ennen lopullista vastausta. Jos hakulähdettä ei ole, älä esitä nimeä tai vastinetta varmana: merkitse [vastine varmistettava] ja pyydä käyttäjää tarkistamaan virallinen teksti.

## Vakiintunutta perustermistöä (FI → SV)

Lähtökohtataulukko — asiayhteyteen sidotut ja aineelliset termit tarkistetaan aina lähteestä.

| Suomi | Ruotsi | Suomi | Ruotsi |
|---|---|---|---|
| laki | lag | asetus | förordning |
| perustuslaki | grundlag | säädös | författning |
| pykälä (§) | paragraf (§) | momentti | moment |
| luku | kapitel | hallituksen esitys (HE) | regeringens proposition (RP) |
| korkein oikeus (KKO) | högsta domstolen (HD) | korkein hallinto-oikeus (KHO) | högsta förvaltningsdomstolen (HFD) |
| käräjäoikeus | tingsrätt | hovioikeus | hovrätt |
| hallinto-oikeus | förvaltningsdomstol | haastehakemus | stämningsansökan |
| kantaja | kärande | vastaaja | svarande |
| asianomistaja | målsägande | syyttäjä | åklagare |
| valitus | besvär / överklagande | oikaisuvaatimus | begäran om omprövning |
| vanhentuminen | preskription | sopimus | avtal |
| vahingonkorvaus | skadestånd | velkoja / velallinen | borgenär / gäldenär |
| kiinteistö | fastighet | ositus | avvittring |
| edunvalvonta | intressebevakning | esteellisyys | jäv |

## Rajaukset

- Älä tuota virallista tai oikeudessa pätevää käännöstä — se on auktorisoidun kääntäjän tehtävä.
- Älä keksi termivastineita äläkä käännä säädöksen nimeä itse.
- Saamen kieli on oma kokonaisuutensa (saamen kielilaki 1086/2003) — älä käsittele sitä ruotsin tapaan.

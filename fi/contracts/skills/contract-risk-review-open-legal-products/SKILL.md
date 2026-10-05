---
name: contract-risk-review-open-legal-products
title: Sopimuksen tarkistus — lausekekohtainen riskiarvio
description: 'Clause-by-clause contract risk review under Finnish contract law with a traffic-light classification (GREEN / YELLOW / RED): identify one-sided or unconscionable terms, liability cap problems, mandatory-law conflicts, and produce concrete amendment proposals.'
author: open-legal-products
author_url: https://github.com/open-legal-products/mike-workflows/tree/main/assistant-workflows/finnish-law-pack/contract-risk-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fi
practice: contracts
language: en
---

# Sopimuksen tarkistus — lausekekohtainen riskiarvio

## Ohjeet

Arvioi sopimus Suomen sopimusoikeuden näkökulmasta ja luokittele se, jotta huomio kohdistuu oikeisiin kohtiin. Tämä työnkulku tuottaa tarkistettavan riskiarvion, ei oikeudellista neuvontaa eikä lopullista kantaa sopimuksen pätevyydestä — lopullinen arvio kuuluu ihmisjuristille.

Jos käytettävissä on suomalaisen oikeuden hakulähde (esimerkiksi Finlex-tietokanta tai oikeudellinen hakutyökalu), tarkista keskeiset säädös- ja pykäläviittaukset (mm. oikeustoimilaki (228/1929) 36 §, kuluttajansuojalaki (38/1978)) ajantasaisesta lähteestä ennen lopullista vastausta. Jos hakulähdettä ei ole käytettävissä, älä esitä pykälän sisältöä varmana: merkitse viittaus muotoon [tarkistettava] ja pyydä käyttäjää toimittamaan ajantasainen säädösteksti.

### Vaihe 1: Asemoi sopimus

- Sopimustyyppi (toimitus, palvelu, salassapito, lisenssi, vuokra, työ jne.).
- Kumman osapuolen näkökulmasta arvioidaan — riski näyttää erilaiselta toimittajalle ja tilaajalle.
- Onko osapuolena kuluttaja tai työntekijä? Jos on, pakottava lainsäädäntö (kuluttajansuojalaki (38/1978), työsopimuslaki) rajoittaa ehtoja, ja heikomman vahingoksi poikkeavat ehdot voivat olla pätemättömiä — nosta tämä aina esiin.

### Vaihe 2: Käy lausekkeet läpi

Tarkista vähintään seuraavat ja merkitse kunkin riskitaso:

| Lauseke | Tarkasta | Tyypillinen riski |
|---|---|---|
| Sopimuksen kohde / laajuus | Onko suoritus määritelty yksiselitteisesti? | Tulkinnanvara → riidat |
| Hinta ja maksuehdot | Maksuaika, viivästyskorko, yksipuoliset korotukset | Avoin hinnankorotusoikeus |
| Vastuu ja vastuunrajoitus | Onko vastuu rajattu kohtuuttomasti? Tahallisuus ja törkeä huolimattomuus rajauksen ulkopuolella? | Rajaus myös tahallisuudesta tai törkeästä huolimattomuudesta on vakiintuneesti tehoton; toispuolinen rajaus |
| Vahingonkorvaus | Välitön vs. välillinen vahinko eroteltu? Yläraja selkeä? | Rajaton vastuu tai epäselvä jako |
| Sopimussakko | Onko sakko kohtuullinen? | Kohtuuton sakko → sovittelu (OikTL 36 §) |
| Immateriaalioikeudet | Kenelle oikeudet syntyvät tai siirtyvät? Käyttöoikeuden laajuus? | Oikeuksien tahaton siirtyminen |
| Salassapito | Laajuus, kesto, poikkeukset symmetrisiä? | Toispuolinen tai päättymätön velvoite |
| Kilpailukielto / rekrytointikielto | Kesto, maantieteellinen laajuus, korvaus | Kohtuuton rajoitus → sovittelu tai pätemättömyys |
| Irtisanominen ja purku | Oikeudet symmetrisiä? Irtisanomisaika, purkuperusteet | Toispuolinen exit, lukkiutuminen |
| Yksipuolinen muutosoikeus | Saako toinen muuttaa ehtoja tai hintaa yksin? | Avoin muutosoikeus heikomman vahingoksi |
| Sovellettava laki ja riidanratkaisu | Suomen laki? Käräjäoikeus yksilöity vai välimiesmenettely (kustannus)? | Epäedullinen forum, puuttuva lainvalinta |
| Liitteet ja pätevyysjärjestys | Onko ristiriitojen etusija määritelty? | Ristiriitaiset asiakirjat |

Sovittelun yleislippu: räikeän yksipuolinen ehto heikomman osapuolen vahingoksi altistuu kohtuullistamiselle (oikeustoimilain (228/1929) 36 §; kuluttajasopimuksissa kuluttajansuojalaki).

### Vaihe 3: Luokittele

- VIHREÄ — voi edetä allekirjoitukseen: ehdot tasapainoisia, vastuunrajoitukset asianmukaisia, ei pakottavan lain ongelmia eikä kohtuuttomia ehtoja arvioivan osapuolen vahingoksi.
- KELTAINEN — neuvoteltavaa: yksittäisiä epäedullisia tai epäselviä ehtoja, jotka kannattaa neuvotella tai täsmentää. Nimeä ne ja ehdota muotoilu.
- PUNAINEN — älä allekirjoita ilman juristin arviota: rajaton tai kohtuuttomasti toispuolinen vastuu, pakottavan lain vastainen kuluttaja- tai työsuhde-ehto, oikeuksien tahaton menettäminen, lukkiutuminen ilman exit-oikeutta, vastuun rajaaminen törkeästä huolimattomuudesta.

### Vaihe 4: Raportoi

1. Luokitus (VIHREÄ / KELTAINEN / PUNAINEN) ja yhden lauseen perustelu.
2. Keskeiset löydökset taulukkona: lauseke · riski · vakavuus · korjausehdotus.
3. Konkreettiset muutosehdotukset kriittisimpiin kohtiin valmiina korvaavana muotoiluna.
4. Mitä vaatii juristin arvion — merkitse [varmista — juristin arvioitava].

Liitä jokaiseen lakiviittaukseen lähde ja merkitse tulkinnanvaraiset kohdat. Jos sopimus on erillisenä asiakirjana, tuota muutosehdotukset selkeästi merkittynä luettelona (kohta, nykyinen muotoilu, ehdotettu muotoilu, perustelu), jotta tarkistaja voi viedä ne asiakirjaan.

## Viittaustapa

Viittaa säädöksiin muodossa: lain nimi ja säädösnumero ensimaininnassa (esim. kuluttajansuojalaki (38/1978)), sen jälkeen vakiintunut lyhyt muoto ja tarkka kohta (esim. OikTL 36 §). Merkitse epävarmat viittaukset [tarkistettava].

## Rajaukset

- Ei päätä, voiko sopimuksen allekirjoittaa — PUNAINEN ja lopullinen pätevyyskanta kuuluvat juristille.
- Ei vahvista sovellettavan lain pykäliä muistista — lähteestä tai [tarkistettava].
- Ei laadi sopimusta tai puuttuvia lausekkeita alusta — arvioi olemassa olevaa tekstiä ja ehdottaa korvaavia muotoiluja.
- Ei korvaa riidan ratkaisua — jos sopimus on jo riitautunut tai rikottu, prosessuaaliset toimet kuuluvat riidanratkaisuun.

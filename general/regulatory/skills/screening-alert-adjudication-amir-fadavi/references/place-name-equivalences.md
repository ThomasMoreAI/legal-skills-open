# Place-name equivalences

Cities, countries, and regions are sometimes renamed for political, post-colonial, or post-Soviet reasons. The same physical place can appear under different names in different time periods or different sources. When comparing places of birth, addresses, or jurisdictions across two sides of a screening alert, naive string comparison will fail on these cases.

This reference catalogs documented equivalences relevant to sanctions and screening contexts. Use it in:
- **Tier 0 parsing** — when extracting POB and address fields, normalize against this list
- **Tier 2 TP-2 firing** — POB city-level match accepts documented equivalences as the same city
- **Tier 3 research** — when searching for context, try both names of a place to broaden coverage

A match on a documented equivalence is treated as a city-level match for TP-2 purposes — the political-entity difference (USSR vs. Russia, Belgian Congo vs. DRC) is context, not a different place.

## Soviet-era and post-Soviet renamings

These are the highest-frequency cases in sanctions work given the volume of Russia/CIS designations.

**Cities:**
- Leningrad ↔ St. Petersburg (Saint Petersburg; Sankt-Peterburg; СПб; pre-1924: Petrograd, before that Saint Petersburg)
- Stalingrad ↔ Volgograd
- Gorky ↔ Nizhny Novgorod
- Sverdlovsk ↔ Yekaterinburg (Ekaterinburg)
- Kuibyshev ↔ Samara
- Kalinin ↔ Tver
- Sergiyev Posad ↔ Zagorsk (Soviet-era name)
- Ordzhonikidze ↔ Vladikavkaz
- Frunze ↔ Bishkek (capital of Kyrgyzstan)
- Alma-Ata ↔ Almaty (Kazakhstan)
- Tselinograd ↔ Akmola ↔ Astana ↔ Nur-Sultan ↔ Astana (Kazakhstan capital; renamed multiple times)
- Ashkhabad ↔ Ashgabat (Turkmenistan capital)
- Stalinabad ↔ Dushanbe (Tajikistan capital)
- Tiraspol (unchanged but disputed political status — Transnistria)

**Countries / regions:**
- USSR / Soviet Union ↔ encompasses 15 successor states (Russia, Ukraine, Belarus, Kazakhstan, Uzbekistan, Turkmenistan, Tajikistan, Kyrgyzstan, Azerbaijan, Armenia, Georgia, Moldova, Lithuania, Latvia, Estonia). A POB listed as "USSR" with a city should be matched to the modern country containing that city.
- Russian SFSR ↔ Russia (Russian Federation)
- Belorussian SSR ↔ Belarus
- Ukrainian SSR ↔ Ukraine
- Kazakh SSR ↔ Kazakhstan

## Post-colonial and political renamings

**Cities:**
- Bombay ↔ Mumbai (1995)
- Madras ↔ Chennai (1996)
- Calcutta ↔ Kolkata (2001)
- Bangalore ↔ Bengaluru (2014, official; both still in common use)
- Cawnpore ↔ Kanpur
- Rangoon ↔ Yangon (Myanmar; renamed 1989)
- Saigon ↔ Ho Chi Minh City (Vietnam; renamed 1975; "Saigon" still in common use for the central districts)
- Peking ↔ Beijing (transliteration update; same city, Wade-Giles vs. Pinyin)
- Canton ↔ Guangzhou (English exonym vs. Pinyin)
- Constantinople ↔ Istanbul (renaming 1930, though Istanbul was in use earlier)
- Salisbury ↔ Harare (Zimbabwe capital; renamed 1982)
- Lourenço Marques ↔ Maputo (Mozambique capital)
- Leopoldville ↔ Kinshasa (DRC capital)
- Stanleyville ↔ Kisangani (DRC)
- Élisabethville ↔ Lubumbashi (DRC)
- Persia (older Western exonym) ↔ Iran (Persia was renamed Iran in international usage in 1935)

**Countries:**
- Burma ↔ Myanmar (renamed 1989; US government continued using "Burma" for years; both seen in screening data)
- Ceylon ↔ Sri Lanka (1972)
- Rhodesia ↔ Zimbabwe (1980)
- Upper Volta ↔ Burkina Faso (1984)
- Zaire ↔ Democratic Republic of the Congo / DRC / Congo-Kinshasa (1997)
- Belgian Congo ↔ DRC (older form)
- Persia ↔ Iran (international usage post-1935; "Persia" still encountered in older documents)
- Siam ↔ Thailand (1939; reverted briefly; final renaming 1949)
- Dahomey ↔ Benin (1975)
- Swaziland ↔ Eswatini (2018)
- Czechoslovakia ↔ split into Czech Republic (now Czechia) and Slovakia (1993)
- Yugoslavia ↔ split into Bosnia and Herzegovina, Croatia, Kosovo, Montenegro, North Macedonia, Serbia, Slovenia
- Macedonia ↔ North Macedonia (2019 renaming, post-Prespa Agreement)
- East Germany / GDR / DDR ↔ now part of Germany (reunification 1990)
- West Germany / FRG ↔ now part of Germany

**Notes on disputed territories:**
- Crimea is internationally recognized as Ukrainian but administered de facto by Russia since 2014. A POB stating "Crimea, Russia" vs. "Crimea, Ukraine" refers to the same territory under contested political claims.
- Taiwan / Republic of China vs. PRC: distinct jurisdictions in screening practice. Do not equate.
- North Korea / DPRK and South Korea / ROK: distinct jurisdictions. Do not equate.
- Western Sahara: contested between Morocco and SADR.

## Major Middle East and North Africa equivalences

- Mecca ↔ Makkah (transliteration variants — same city)
- Medina ↔ Madinah
- Jeddah ↔ Jiddah ↔ Jedda
- Damascus ↔ Dimashq (Arabic) ↔ Sham (regional name)
- Aleppo ↔ Halab
- Cairo ↔ Al-Qahirah (Arabic)
- Alexandria ↔ Al-Iskandariyah
- Tehran ↔ Teheran (older spelling; same city)
- Baghdad ↔ Baghdād
- Mosul ↔ Al-Mawsil
- Tripoli (Libya) vs. Tripoli (Lebanon) — two different cities; never equate

## Major East Asia equivalences

- Beijing ↔ Peking ↔ Beiping (1928–1949 name) — same city
- Nanjing ↔ Nanking — same city
- Chongqing ↔ Chungking — same city
- Tianjin ↔ Tientsin — same city
- Hong Kong ↔ 香港 ↔ Xianggang (Pinyin) — same city
- Macau ↔ Macao ↔ Aomen (Pinyin) — same city
- Pyongyang ↔ P'yŏngyang (McCune-Reischauer)
- Seoul ↔ 서울 (Korean) — no Latin variant; Hanja form 京城 is the colonial-era name "Keijō", same city
- Mumbai (already covered above)

## Africa, sub-Saharan equivalences

- Beyond the country-level renamings above:
- Côte d'Ivoire ↔ Ivory Coast (official since 1985 is "Côte d'Ivoire" in all languages, but "Ivory Coast" remains common in English sources)
- Cape Verde ↔ Cabo Verde (the country officially uses "Cabo Verde" since 2013)
- Eswatini ↔ Swaziland (already noted)

## How to apply this reference

**At Tier 0 parsing:** When ingesting POB or address fields, record both the literal value as provided and a normalized form. Normalization preserves the original; the alternate name is held alongside.

Example: POB on listed entry = "Leningrad, USSR"; normalized form = "Leningrad" + alternate "St. Petersburg" + country = Russia (via successor-state mapping).

**At Tier 2 TP-2:** POB match is satisfied if either name on one side matches either name on the other side. A screened party with POB "St. Petersburg, Russia" and a listed party with POB "Leningrad, USSR" produces a TP-2 city-level match.

**At Tier 3 research:** When constructing search queries that include a place name, try the modern name first (more search engine coverage) and the historical name as a fallback if the listed entry uses the historical form. Old archival sources may only index the historical name.

## When in doubt

If a place-name equivalence is not in this reference but you have reason to believe two names refer to the same place, treat the equivalence as unverified and downgrade the POB match from "city-level" to "country-level if applicable, otherwise escalation". Do not invent equivalences. Conservative posture: a missed equivalence sends a case to escalation; an invented equivalence creates a false TP, which is worse.

## Limits

This is not a gazetteer. It covers the equivalences most likely to surface in screening adjudications driven by Soviet, post-colonial, and major Asian renaming events. Less common equivalences — village-level renamings, minor reorganizations, alternate exonyms in less-common languages — should be looked up at Tier 3 when they matter, not memorized here.

# Transliteration variants

The same source-language name can produce multiple Latin spellings depending on which transliteration system was used (academic, journalistic, immigration document, sound-based). When comparing two Latin-script names that originate from a non-Latin source, spelling differences may not indicate different identities — they may just indicate different transliterations.

This reference catalogs documented variant patterns. Use it in:
- **Tier 0 parsing** — when assessing whether two name components are the same or different
- **FP-2, FP-6, FP-7 firing decisions** — these rules require unambiguous difference, not just different spelling
- **Tier 3 Rung 4** — variant sweep cycles through documented spellings

## Arabic-origin names

**Mohammed and variants** — all from محمد:
- Mohammed, Mohammad, Muhammad, Mohamad, Mohamed, Mohamet, Mehmed (Turkish), Mehmet (Turkish), Mahomet (archaic French/Spanish)

**Ahmed / Ahmad** — from أحمد:
- Ahmed, Ahmad, Achmed, Achmad

**Hassan / Hasan** — from حسن:
- Hassan, Hasan, Hassen

**Hussein / Hussain / Husayn** — from حسين:
- Hussein, Hussain, Husayn, Husein, Hosein, Hossein (Persian rendering)

**Khalid / Khaled** — from خالد:
- Khalid, Khaled, Halid, Halit (Turkish)

**Yusuf / Yousef / Yousaf** — from يوسف:
- Yusuf, Yousef, Yousaf, Yousuf, Yousif, Youcef (French rendering for Maghreb)

**Abdullah / Abdallah** — from عبد الله:
- Abdullah, Abdallah, Abdulla, Abdalla, Abdul (truncated)

**Abdul + [attribute]** — these are compound names where "Abd" = servant, "ul/al" = the, and the attribute is a name of God. Treat the whole compound as a single anchor:
- Abdul Rahman / Abdurrahman / Abdulrahman / Abd ar-Rahman — all the same name
- Abdul Aziz / Abdulaziz / Abd al-Aziz
- Abdul Karim / Abdulkarim / Abd al-Karim

**Saleh / Salah / Saleh** — from صالح:
- Saleh, Salih, Salah (different name from الصلاح but transliteration can collide)

**Omar / Umar** — from عمر:
- Omar, Umar, Oumar (French rendering)

**Ali** — from علي:
- Usually Ali; sometimes Aly. Common across Arabic, Persian, Turkish, South Asian — treat as such.

**Definite article "Al-" / "El-" / "Ul-"**: prefix variations are stylistic and never indicate different identity. "Al-Tikriti" = "El-Tikriti" = "At-Tikriti" (sun-letter assimilation in transliteration).

**Definite article hyphenation and capitalization**: "Al-Qaeda" = "al-Qaeda" = "Al Qaeda" = "AlQaeda". Variants are equivalent.

## Persian-origin names

Persian uses an extended Arabic script with additional letters (پ گ چ ژ). Transliteration sometimes follows Arabic conventions (losing distinctive Persian letters) and sometimes preserves Persian sounds.

**Pourya / Puria / Pouria** — from پوریا:
- Pourya, Puria, Pouria, Porya

**Behzad** — from بهزاد:
- Behzad, Behzaad

**Reza** — from رضا:
- Reza, Ridha (Arabic rendering), Riza (Turkish rendering)

**Hossein** (Persian rendering of حسين):
- Hossein, Hosein, Hussein (when Arabicized)

**Family name suffixes:**
- -zadeh ("son of") = -zada, -zade in Turkic-influenced transliterations
- -pour = -pur, -poor (transliteration of پور)

## Cyrillic-origin names (Russian, Ukrainian, Belarusian, Bulgarian, Serbian, etc.)

**Alexander** — from Александр:
- Aleksandr (modern transliteration), Alexander (anglicized), Aleksander, Alexandr, Olexandr (Ukrainian)

**Vladimir** — from Владимир:
- Vladimir; sometimes Volodymyr (Ukrainian rendering of the same Slavic root)

**Yury / Yuri / Iurii** — from Юрий:
- Yury, Yuri, Yurii, Iurii (academic transliteration), Iouri (French rendering)

**Mikhail / Michael** — from Михаил:
- Mikhail; rarely Michael (when anglicized)

**Surname endings:**
- Russian: -ov (male) / -ova (female), -ev (male) / -eva (female) — the male and female forms refer to the same family
- Ukrainian: -enko, -uk, -chuk
- Belarusian: -onok, -enka
- Polish (Slavic but Latin-script natively): -ski / -ska, -cki / -cka

**The "э" / "е" / "ё" question:** Russian ё is often transliterated as e (because ё is rarely written even in Russian). "Gorbachev" / "Gorbachëv" — equivalent.

**The hard sign (ъ) and soft sign (ь):** Often dropped in transliteration. Don't penalize their absence.

## Chinese-origin names

Multiple transliteration systems exist. The same name can produce very different Latin spellings depending on which system was used and which Chinese language (Mandarin, Cantonese, Hokkien, etc.) was being transliterated.

**Pinyin (PRC standard, used in most modern contexts):**
- 王 → Wang; 李 → Li; 张 → Zhang; 陈 → Chen; 刘 → Liu

**Wade-Giles (older, used in Taiwan and pre-1979 sources):**
- 王 → Wang; 李 → Li; 张/張 → Chang (not Zhang); 陳 → Ch'en; 劉 → Liu

**Cantonese transliterations (Hong Kong, Macau, diaspora):**
- 陈/陳 → Chan (not Chen); 黄/黃 → Wong (not Huang); 刘/劉 → Lau (not Liu); 周 → Chow (not Zhou); 张/張 → Cheung (not Zhang)

**The same person's name can appear in screening data as Pinyin OR Wade-Giles OR Cantonese**, depending on what documentation was used. Treat these as variants when context supports it:
- A PRC-passported person: expect Pinyin
- A Hong Kong–passported or Singapore-passported person: expect Cantonese or Hokkien renderings
- A Taiwan-passported person: expect Wade-Giles or modified Wade-Giles

**Tone marks (ā á ǎ à):** Almost never preserved in Latin transliterations of names. Ignore.

## Korean-origin names

Multiple romanization systems: Revised Romanization (current South Korean standard, 2000+), McCune-Reischauer (older, still used in some contexts), and individual spellings on passports.

- 김 → Kim (universal)
- 이 → Lee, Yi, Rhee, Ri (North Korean rendering), I
- 박 → Park, Pak, Bak
- 정 → Jung, Jeong, Chung, Chong
- 강 → Kang, Gang
- 조 → Cho, Jo, Joh

Korean passports often retain spellings the holder prefers, including older McCune-Reischauer forms. "Lee" / "Yi" / "Rhee" can all be the same family name.

## Japanese-origin names

Mostly stable in Hepburn romanization. Watch for:
- Long-vowel marks: ō / ou / oh. "Saitō" / "Saitou" / "Saito" / "Saitoh" — same name.
- "Tu" vs "Tsu": "Matsumoto" / "Matumoto" (older Nihon-shiki). Latter is rare in modern documents.

## South Asian-origin names

Highly variable. Same name from Hindi, Urdu, Punjabi, Bengali, Tamil, etc., can transliterate many ways. Religious and regional patterns:

- "Singh" — male Sikh surname, very common
- "Kaur" — female Sikh surname
- "Khan" — pan-Islamic, used across South Asian Muslim communities
- "Rahman" / "Rehman" / "Ur-Rehman" — variant transliterations of رحمن

## Hebrew-origin names

- "Yehuda" / "Yehudah" / "Judah" / "Juda"
- "Yosef" / "Yossef" / "Joseph"
- "Avraham" / "Abraham" / "Abram"
- "Yitzhak" / "Yitschak" / "Yitzchak" / "Isaac"

Modern Israeli passports use English-influenced spellings; older religious documents use academic Hebrew transliteration.

## How to use this reference in rule firing

**FP-2 / FP-6 firing decisions:** When the non-matching anchor component on one side is a documented transliteration variant of the component on the other side, the components are **not** unambiguously different. The rule does NOT fire.

Example: screened "Muhammad Yousef" matched against listed "Mohammed Yusuf". Both anchors (Yousef / Yusuf) are documented variants of the same Arabic name. The "difference" is transliteration, not identity. FP-2/FP-6 do NOT fire on the Yusuf/Yousef difference. Proceed to higher tiers.

**Tier 3 Rung 4 variant sweep:** Cycle through documented variants of the anchor name + same context terms. The list above is the documented-variants source. Don't invent variants that aren't documented here.

## When in doubt

If a difference between two anchor components might be transliteration but you're not sure, treat it as ambiguous (don't fire FP rules on it) and let Tier 2/3 evidence resolve. Conservative posture: the cost of escalating an FP is much lower than the cost of clearing a TP.

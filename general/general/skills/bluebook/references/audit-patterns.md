# Bluebook Footnote Audit Patterns (22e)

An audit checklist for law review manuscripts, rebuilt against the **22nd edition (22e)** rule text
extracted to `scratch/bb22/corpus.txt`. Every check below names the rule it enforces and quotes or
paraphrases the 22e sentence that creates the duty. A check that could not be traced to the corpus is
kept — an unchecked heuristic is still useful — but is labelled so no one mistakes it for a rule.

**Status legend**

| Marker | Meaning |
|---|---|
| *(rule N.N)* | The check restates a sentence present in the extracted 22e text for that rule. |
| **UNVERIFIED** | Local practice or tooling advice with no Bluebook authority behind it. Do not cite it to a source-checker as Bluebook authority. |

**What the extraction covers.** All twenty-three rules and all sixteen tables. Rule 2's body is
present in full — 2.1 (*22e pp. 73–74*), 2.2 (*22e pp. 74–76*) and 2.3 (*22e p. 76*) — so the
per-source typeface calls are checkable here (D12, D15, D16). T1 carries its five subtables: T1.1
federal judicial and legislative (*22e pp. 257–60*), T1.2 federal administrative (*22e p. 260*),
T1.3 as fifty-one individual jurisdiction pages each with its own page range (Alabama at
*22e pp. 272–73*), T1.4 other U.S. jurisdictions (*22e p. 325*), T1.5 tribal nations
(*22e p. 328*). T2 carries forty-seven foreign-jurisdiction entries (*22e p. 328*). Rules 7, 8, 9,
11, 19 and 22 and tables T3 (*22e p. 329*), T4 (*22e p. 332*), T5 (*22e p. 333*), T9
(*22e pp. 339–40*), T15 (*22e pp. 349–53*) and T16 (*22e pp. 353–54*) are all present, so where a
rule cross-references them this file now states the referenced content rather than the bare
cross-reference.

**The residual gaps.** Ten of the corpus's 280 captured pages open without their heading, and they
divide into two kinds rather than one.

*Four are empty.* The capture recorded the literal marker `[EMPTY]` and no body at all: rule 3.2
(Pages, Footnotes, Endnotes, and Graphical Materials), rule 21.2 (Non-English-Language Documents),
and the first captures of T12 and T13. T12 and T13 were each captured a second time in full, and that
second T13 capture (slug `t13-periodicals`) supplies the *22e pp. 346–48* cite in D8. Rules 3.2 and
21.2 have **no** second capture, so the "all twenty-three rules" claim above holds at the rule level
only — those two subsections are wholly absent from the corpus, not merely headerless. No check in
this file cites either.

*Six are genuine mid-text truncations*, having lost the heading, the page number, and whatever
sentence ran into the first surviving character: rules 3.4, 6.1, 11, 15.7 and 22.2, and table T2.9.
Two of the six bear on this file. Rule 11's page begins with a bare `:` running straight into
`U.S. Const. art. I, § 9, cl. 2.`, and rule 6.1's begins `). ` — so C10 (rule 11) and D14
(rule 6.1) carry no `22e p.` cite, and the omission is an extraction failure rather than an
oversight. Both bodies are otherwise substantive and quotable, but the corpus cannot establish that
only the heading was lost.

---

## A. Signals, parentheticals, and citation structure (rule 1)

| # | Check | Rule |
|---|---|---|
| A1 | Every footnote call number sits **after** the punctuation it follows — comma, semicolon, period — **except** before a dash or a colon *(rule 1.1(a))*. | 1.1 |
| A2 | A pincite is present on every citation **except** one introduced by "see generally" *(rule 1.2(f): "Pincites are required for all citations except for those introduced by 'see generally.'")*. | 1.2 |
| A3 | An explanatory parenthetical is present after every "see also", "cf.", "but cf.", "see generally", and after **each** authority in a "compare ... with" or "contrast ... with" — the 22e states the parenthetical is *required* for each of these *(rule 1.2(a)–(d), 1.5)*. | 1.2, 1.5 |
| A4 | "But" is dropped from "but see" and "but cf." when the signal follows another negative signal *(rule 1.2(c))*. | 1.2 |
| A5 | When "e.g.," is attached to another signal it is preceded by an *italicized* comma and followed by a **non**-italicized comma *(rule 1.2(a))*. | 1.2 |
| A6 | A signal used as the verb of a textual sentence is **not** italicized *(rule 1.2(e), citing rule 2.1(d))*; "cf." becomes "compare" and "e.g." becomes "for example" in that use. | 1.2, 2.1 |
| A7 | Signals appear in the order listed in rule 1.2; when "e.g.," is combined with another signal, the **other** signal's position governs *(rule 1.3)*. | 1.3 |
| A8 | Signals of the **same** basic type (supportive / comparative / contradictory / background) are strung in one citation sentence separated by semicolons; signals of **different** types are split into separate citation sentences *(rule 1.3)*. Inside a citation **clause**, mixed types in one string are permitted *(rule 1.3, 1.1)*. | 1.3, 1.1 |
| A9 | Authorities within a signal are separated by semicolons, and a markedly more helpful or authoritative source precedes the others; short-form cites are ordered as though cited in full *(rule 1.4)*. | 1.4 |
| A10 | A parenthetical that does **not** quote begins with a present participle and **never** with a capital letter; one that quotes a full sentence begins with a capital and carries closing punctuation *(rule 1.5(a)(i)–(ii))*. Omissions inside such a quote are marked per rule 5.3(b) *(22e pp. 90–91)*: a dropped beginning takes a capitalized (bracketed if necessary) first letter and **no** ellipsis; a dropped middle takes an ellipsis; a dropped end takes an ellipsis before the sentence's final punctuation; matter deleted after that final punctuation is not marked at all. | 1.5, 5.3 |
| A11 | Multiple parentheticals follow the fixed 22e order: (date) [hereinafter] (en banc) (Lastname, J., concurring) (plurality opinion) (per curiam) (alteration in original) (emphasis added) (footnote omitted) (citations omitted) (quoting ...) (citing ...), URL (last visited) (explanatory), then prior or subsequent history *(rule 1.5(b))*. | 1.5 |
| A12 | Explanatory parentheticals **precede** any subsequent-history or related-authority phrase *(rule 1.5(b), 1.6)*. | 1.5, 1.6 |
| A13 | A quoting/citing parenthetical covering several sources uses "first ...; and then ..." for two and "first ...; then ...; and then ..." for three or more *(rule 1.5(b))*. | 1.5 |
| A14 | Related-authority phrases ("reprinted in", "construed in", "quoted in") are italicized and appended without parentheses *(rule 1.6(a), (c))*; a work the primary authority itself discusses goes in a parenthetical instead *(rule 1.6(c))*. | 1.6 |

---

## B. Short forms: "id.", "supra", "hereinafter" (rules 4.1, 4.2)

| # | Check | Rule |
|---|---|---|
| B1 | In law review footnotes, "id." is valid only for the immediately preceding authority **within the same footnote**, or in the immediately preceding footnote **when that footnote contains only one authority** *(rule 4.1)*. | 4.1 |
| B2 | An "id." following a multi-source footnote is an error; replace with a short form naming the source *(rule 4.1, which gives the corrected example "See Chalfin, 233 A.2d at 570." in place of "See id. at 570.")*. | 4.1 |
| B3 | **Counting authorities correctly is the whole game.** Sources appearing in explanatory parentheticals, explanatory phrases, or prior/subsequent history are **ignored** when deciding whether the preceding footnote "contains only one authority" *(rule 4.1)*. A naive source-counter that counts a `(quoting X)` or an `aff'd, Y` as a second authority will emit false positives on correct footnotes. | 4.1 |
| B4 | "Id." is never used for an internal cross-reference; "See supra text accompanying note N" is repeated instead of "See supra id." *(rule 4.1, referring to rule 3.5, 22e pp. 82–83, which supplies the "supra"/"infra" cross-reference forms — "See supra text accompanying notes 305–07", "See cases cited supra note 22")*. | 4.1, 3.5 |
| B5 | The period in "id." is italicized *(rule 4.1)*. | 4.1 |
| B6 | Where the first citation was to a shorter work inside a larger authority, a later citation to the **whole** authority takes "supra", not "id." *(rule 4.1, pointing to rule 4.2(a))*. | 4.1, 4.2 |
| B7 | "Supra"/"hereinafter" are **not** used for cases, statutes, constitutions, legislative materials or debates (other than hearings), restatements, model codes, or regulations, except in extraordinary circumstances such as an extremely long name *(rule 4.2)*. Flag every `Case v. Case, supra note N`. | 4.2 |
| B8 | The supra form is the author's last name; for an institutional author use the **full institutional name**; with no author, the title, or for unsigned student-written material the designation *(rule 4.2(a), citing rule 16.7.1(b))*. | 4.2, 16.7.1 |
| B9 | "Supra" carries the footnote number of the full citation **unless** the full citation is in the same footnote, where "supra" appears bare *(rule 4.2(a))*. | 4.2 |
| B10 | "Hereinafter" is placed after the first citation of the authority but **before** any explanatory parenthetical, in brackets, in the same typeface as the full citation *(rule 4.2(b))*. | 4.2 |
| B11 | "Hereinafter" is not used where a plain "supra" would do *(rule 4.2(b): "Do not use the 'hereinafter' form when a simple 'supra' form is adequate")* — but **is** used to separate two works by one author appearing in the same footnote *(rule 4.2(b))*. | 4.2 |
| B12 | Once a hereinafter form exists, later cites use that form in place of the author's name or title *(rule 4.2(b), 16.9(b))*. | 4.2, 16.9 |
| B13 | Moving a hereinafter definition earlier requires rewriting every citation between the old and new positions, and leaves no orphaned bracket. **UNVERIFIED** — a repair procedure, not a 22e rule. | — |

---

## C. Source-specific short forms

| # | Check | Rule |
|---|---|---|
| C1 | A case short form is permitted only if the case is cited in the **same footnote** or in **one of the preceding five footnotes** (in full or short form, including "id."); otherwise a full citation is required *(rule 10.9(a))*. This five-footnote window is the check most manuscripts fail. | 10.9 |
| C2 | A one-party short form must be unambiguous and is italicized; do not shorten to a geographical or government unit, a government official, or another common litigant — "Patterson", not "NAACP" or "Alabama" *(rule 10.9(a)(i))*. | 10.9 |
| C3 | A short cite to an entire decision (no pincite) keeps the shortened name, volume, reporter and first page, and **drops** the court/date parenthetical *(rule 10.9(a)(i))*. | 10.9 |
| C4 | A statute short form is permitted when the statute was cited in the same footnote or can be readily found in one of the **preceding five footnotes** *(rule 12.10(b))*. | 12.10 |
| C5 | "Section" and "paragraph" are spelled out in the text — main text or footnote text — of law review pieces, **except** when referring to a provision of the U.S. Code *(rule 12.10(c))* or a federal regulation *(rule 14.6)*; in citations the "§" and "¶" symbols are used, except when citing session laws amending prior acts *(rule 12.4(d))*. The first word of any sentence is spelled out regardless. A space follows the symbol *(rule 6.2(c), 22e pp. 93–94)*. **T16** supplies the same split from the table side: "sec., secs." in an amending act and "§, §§" in all other contexts; "¶, ¶¶" where the symbol appears in the source and "para., paras." where it does not; and a space between the abbreviation and the number or letter in every subdivision abbreviation **except** "n." *(T16, 22e pp. 353–54)*. | 12.10, 6.2, T16 |
| C6 | "Infra" is **never** used for books, reports and other nonperiodic materials *(rule 15.10)*. Forward references to those sources are an error, not a resolution problem. | 15.10 |
| C7 | For a shorter work in a collection: "id." only if the shorter work was the immediately preceding authority in the same footnote or the sole authority in the preceding footnote, and never "id." to the collection as a whole while citing a different work in it; the collection takes a supra form built on its **title** *(rule 15.10.1)*. | 15.10 |
| C8 | A periodical supra form always gives the page cited **except** when citing the work in its entirety *(rule 16.9(b))*. A bare `Author, supra note N` on a pincited proposition is a defect. | 16.9 |
| C9 | For materials available only online, use the normal short form appropriate for the source; a URL **need not** be repeated after a full citation *(rules 12.10(d), 15.10, 16.9(b), which carry that sentence identically)*. The permission runs one way only — omitting the URL from the short form is correct, and **repeating it is not an error**. Do not flag a short form that carries the URL. The 22e's own worked example under 12.10(d): "Utah Code § 4-30-108 (2017), http://le.utah.gov/xcode/Title4/Chapter30/4-30-S108.html [https://perma.cc/7UHX-R44Z]." becomes "§ 4-30-108." | 12.10, 15.10, 16.9 |
| C10 | Constitutions take **no** short citation form other than "id." *(rule 11)*. Where the reference is to several amendments, to sections within one article, or to clauses within one section, a single citation clause may carry them ("U.S. Const. amends. V, XIV"); otherwise the second citation uses "id." rather than repeating the constitution's name ("U.S. Const. art. I, § 8; id. art. II, § 2") *(rule 11)*. A `U.S. Const., supra note N` is therefore an error, not a style choice. | 11 |
| C11 | A service short form for a case follows rule 10.9, keeps the **complete** volume designation for the service binder, and substitutes paragraph or section numbers for page numbers where appropriate; to cite the entire case in short form, give the paragraph or section number, or the first page, **without** "at" — "See [1987–1989 Transfer Binder] Bankr. L. Rep. (CCH) ¶ 72,447." *(rule 19.2(a), 22e pp. 206–07)*. Statutes, regulations, articles and commentaries found in a service follow their own source rule instead *(rule 19.2(b))*. | 19.2 |
| C12 | Tribal short forms follow the short form for the source's type: rule 10.9 for Tribal cases, rule 11 for Tribal constitutions, rule 12.10 for Tribal codes, orders, ordinances and resolutions, and rule 21.17(a) for Tribal treaties *(rule 22.3, 22e p. 249)*. There is no separate Tribal short-form grammar to audit against. | 22.3 |

---

## D. Abbreviation and typeface

| # | Check | Rule |
|---|---|---|
| D1 | In citations, abbreviate any word listed in **T6** even when it is the first word of a party's name — unless that word is part of a state, country or other geographical unit that is the **entire** name of the party ("South Dakota v. Dole", not "S. Dakota v. Dole") *(rule 10.2.2)*. | 10.2.2, T6 |
| D2 | Geographical units in case names are abbreviated as indicated in **T10**, unless the geographical unit is the whole party name — including "United States" *(rule 10.2.2)*. T10 covers U.S. states, cities and territories (T10.1, *22e pp. 340–42*), Australian, Canadian and U.K. units (T10.2) and countries and regions (T10.3); a country, territory, province or city **omitted** from T10.2 or T10.3 is **not** abbreviated, except as table T6 otherwise provides *(T10 introduction, 22e p. 340)*. | 10.2.2, T10 |
| D3 | Other words of eight letters or more may be abbreviated where substantial space is saved and the result is unambiguous *(rule 10.2.2; T6's introduction states the same allowance)*. | 10.2.2, T6 |
| D4 | Case names in **text** follow rule 10.2.1 only; the further abbreviation of rule 10.2.2 applies to citations. "Southern Pacific Co. v. Jensen" in text, "S. Pac. Co. v. Jensen" in a citation *(rule 10.2)*. An audit that abbreviates textual case names is introducing the error. | 10.2, 10.2.1 |
| D5 | Where the textual sentence names the case in full, the case name may be omitted from the citation *(rule 10.2.2)*. | 10.2.2 |
| D6 | Possessives abbreviate as "Emps.'" (plural) and "Emp.'s" (singular); plurals otherwise add "s" *(T6 introduction)*. | T6 |
| D7 | For periodical titles only: "University" abbreviates to "U."; "a", "at", "in", "of" and "the" are omitted but "on" is retained; and if one word survives that omission it is **not** abbreviated *(T6 introduction)*. | T6 |
| D8 | Periodical names are set in small capitals and abbreviated per **T6**, **T13** and **T10** *(rule 16.1)*. The tables are consulted in order: common institutional names (law schools, professional organizations, geographic units in institutional names) come from T13; a name not listed there is abbreviated word by word from T6 and T10; a word in none of them is left in full *(T13 introduction, 22e pp. 346–48)*. Always use the title as it appears on the title page of the issue cited, even if the title has since changed; where the title itself contains an abbreviation, keep it ("IMF Surv.", not "Int'l Monetary Fund Surv.") *(T13)*. | 16.1, T6, T13, T10 |
| D9 | An institutional author is abbreviated **only if the result is completely unambiguous**, using T6 and T10, dropping "Inc." / "Ltd." where a word like "Ass'n" or "Co." already marks it a firm *(rule 15.1(e))*. Note the tension an auditor must respect: T6 says abbreviate any listed word, 15.1(e) subordinates that to unambiguity. | 15.1, T6, T10 |
| D10 | A book or report author's full name is given on first citation, in small capitals, keeping "Jr." or "III" and dropping "Dr.", "Prof.", "Judge", "Justice" *(rule 15.1)*. | 15.1 |
| D11 | Website main page titles are in small capitals, abbreviated per T6, T10 and T13 *(rule 18.2.2(b)(i))*. | 18.2.2, T6 |
| D12 | Law reviews run two typeface conventions — one for citations *(rule 2.1, 22e pp. 73–74)* and one for textual material *(rule 2.2, 22e pp. 74–76)*; unless otherwise noted, the examples throughout the Bluebook follow the law review **footnote** convention *(rule 2, 22e p. 72)*. The per-source calls in a citation: case names in a **full** citation are ordinary roman, except procedural phrases, which are always italicized, while the **short** form of a case citation is italicized ("Lochner, 198 U.S. at 50") *(rule 2.1(a))*; books take small capitals for **both** author and title *(rule 2.1(b))*; periodicals take an italicized article title, a small-capital periodical name, and an author's name in ordinary **roman** *(rule 2.1(c))*; introductory signals are italicized inside citation sentences and clauses *(rule 2.1(d))*; explanatory phrases are italicized, but the phrases inside related-authority parentheticals — "(quoting . . .)", "(citing . . .)", "(translating . . .)" — are **not** *(rule 2.1(e))*. | 2.1, 2.2 |
| D13 | Procedural phrases in a case name are always italicized regardless of the rest of the name *(rule 10.2.1)*; the parentheses in a citation are never italicized *(rule 2.1(f), as stated in rule 10.2)*. | 10.2.1, 2.1 |
| D14 | Spacing of abbreviations follows rule 6.1(a) *(so stated in the T6 introduction)*: close up adjacent single capitals ("N.W.", "S.D.N.Y.") but not a single capital against a longer abbreviation ("D. Mass.", "S. Ct."). In periodical names, close up adjacent single capitals **except** where a capital refers to an institutional entity, which is set off by a space ("Geo. L.J.", but "B.C. L. Rev.", "N.Y.U. L. Rev.", "S. Ill. U. L.J."). Numerals and ordinals count as single capitals ("F.3d", "S.E.2d"), but a space precedes any abbreviation of two or more letters ("So. 2d", "F. Supp. 2d") *(rule 6.1(a))*. | T6, 6.1 |
| D15 | A case name in **footnote text** is italicized when it is grammatically part of the sentence ("In Loving v. Virginia, the Court invalidated . . .") but takes the citation convention of rule 2.1(a) when it sits in a citation clause embedded in that sentence ("The Court has upheld race-specific statutes . . . , e.g., Korematsu v. United States, 323 U.S. 214 (1944), but . . .") *(rule 2.2(b)(i))*. For any **other** authority, the citation typeface applies whenever full or short-form citation information is given ("Learned Hand, The Bill of Rights (1958), and Holmes, supra note 2"), and the main-text convention applies where the reference appears without it ("Judge Hand explained his philosophy of judicial review in The Bill of Rights.") *(rule 2.2(b)(ii))*. In an explanatory parenthetical, use the case-name convention for citation text when a full citation clause is included *(rule 2.2(b)(iii))*. | 2.2, 2.1 |
| D16 | Commas, semicolons and other punctuation are italicized **only** when they are part of the italicized material, never when they merely belong to the surrounding sentence or citation *(rules 2.1(f), 2.2(c))*. Ellipses and brackets marking an alteration are always romanized, even where the quoted matter is italic, underlined or bold *(rules 2.1(g), 2.2(d))*. One space follows punctuation in a proportional font; double-space only after a monospaced font such as Courier, Menlo or Consolas *(rule 2.3, 22e p. 76)*. | 2.1, 2.2, 2.3 |
| D17 | "Id." is **always** italicized, and procedural phrases in case names ("In re", "ex rel.") are always italicized *(rule 7(b), citing rules 2.1(d) and 10.2.1(b))*. Non-English words are italicized unless absorbed into common English usage: Latin common in legal writing is **not** italicized — "res judicata", "amicus curiae", "prima facie", "en banc", "certiorari", "e.g.", "i.e." — while very long, obsolete or uncommon Latin stays italic ("expressio unius est exclusio alterius"). Text in a non-Roman alphabet is never italicized *(rule 7(b), 22e pp. 95–96)*. Also italicized: the lowercase "l" used as a subdivision ("§ 23 (l)", "cmt. l") *(rule 7(d))*. | 7 |
| D18 | Capitalization: in a heading or title, capitalize the initial word, any word immediately after a colon, and every word except articles, conjunctions and prepositions of four or fewer letters *(rule 8(a), 22e pp. 96–99)*. Internet main page titles and URLs keep the source's own capitalization, in text and footnotes alike *(rule 8(b))*. An author's last name is capitalized as the periodical's table of contents or the work's title page gives it — "van Dorn, supra note 12" or "Van Dorn, supra note 12", whichever the source shows *(rule 8(c))*; an auditor normalizing this is introducing the error. "Court" is capitalized when a court is named in full or the U.S. Supreme Court is meant, "Act" when a specific act is meant, and parts of a constitution are capitalized in **textual** sentences but not in citations *(rule 8(d)(ii))*. | 8 |
| D19 | Judges and officials: "Justice Gorsuch", "Chief Justice Roberts", "Judge Readler", "Chief Judge Smith"; parenthetical references are "Kagan, J." and "Breyer & Kagan, JJ.", abbreviated as **T11** indicates. First names are omitted unless the court has two individuals with the same last name, in which case the first name appears on first reference *(rule 9(a), 22e p. 99)*. A Supreme Court Term is designated by the year in which it **began**, not the year it ended *(rule 9(c))*. | 9, T11 |

---

## E. Internet sources and archiving (rule 18.2)

| # | Check | Rule |
|---|---|---|
| E1 | **All** online content cited is captured and stored permanently — via an archival tool, or by saving a fixed copy such as a PDF on file *(rule 18.2.1(d))*. This is a requirement, not a courtesy. | 18.2.1 |
| E2 | An archive URL is appended to the full citation **in brackets**; a source saved on file instead gets a parenthetical after the URL saying where it lives *(rule 18.2.1(d))*. | 18.2.1 |
| E3 | The archival link immediately **follows** the URL *(rule 1.5(b), 18.2.1(d))*. | 1.5, 18.2.1 |
| E4 | Where an authenticated, official, or exact copy (e.g. a paginated PDF) is available online, cite as if to the print source with **no URL appended** *(rule 18.2.1(a))*. | 18.2.1 |
| E5 | Where an online source merely shares print characteristics, cite as the print source and append the URL *(rule 18.2.1(b)(ii))*; the URL then immediately precedes the explanatory parenthetical *(rule 1.5(b))* and follows format and related-authority parentheticals *(rule 18.2.1(c))*. | 18.2.1, 1.5 |
| E6 | A DOI may be appended in brackets as a rule 18.2.1(d) archival tool *(rule 16.8)*. | 18.2.1, 16.8 |
| E7 | Public open-source repositories are exempt: no archival parenthetical or permanent URL is required *(rule 18.11)*. | 18.11 |
| E8 | A web-based source's citation carries title, pagination and publication date as they appear on the page, and points at the most stable location available *(rule 18.2.2)*; an institutional author is abbreviated per rule 15.1(e) and omitted where domain ownership is obvious from the title *(rule 18.2.2(a))*. | 18.2.2, 15.1 |

---

## F. Known false positives — do not "fix" these

| # | Pattern | Why it is correct |
|---|---|---|
| F1 | "id." after a footnote that visibly names several cases | Sources in parentheticals, explanatory phrases and history do not count toward the one-authority limit *(rule 4.1)*. |
| F2 | A bare "supra" with no note number | Correct when the full citation is in the same footnote *(rules 4.2(a), 16.9(b))*. |
| F3 | An unabbreviated case name in the running text | Rule 10.2.2's further abbreviation applies to citations, not text *(rule 10.2)*. |
| F4 | "Compare ... with ..." carrying a parenthetical on every authority | Required, not redundant *(rule 1.2(b))*. |
| F5 | A print-form citation to an online PDF with no URL | Correct for an authenticated, official, or exact copy *(rule 18.2.1(a))*. |
| F6 | A signal-as-verb set in roman | Signals are not italicized when used as verbs *(rule 1.2(e))*. |
| F7 | An author's name in ordinary roman beside a small-capital periodical name | Correct: periodical citations take roman authors, italic article titles and small-capital periodical names *(rule 2.1(c))*; small caps for the author are the **book** convention *(rule 2.1(b))*. |
| F8 | An italicized case name inside an article title left un-italicized | Correct — a case name within an article title is not italicized, even where it is the whole title, as in "Owen M. Fiss, Dombrowski, 86 Yale L.J. 1103 (1977)" *(rule 2.1(a))*. |
| F9 | A lowercase author surname such as "van Dorn, supra note 12" | Correct where the source's own table of contents or title page capitalizes it that way *(rule 8(c))*. |
| F10 | "res judicata", "en banc" or "prima facie" set in roman | Correct: Latin in common legal usage is not italicized *(rule 7(b))*. Only long, obsolete or uncommon Latin stays italic. |

---

## G. Pipeline and tooling — **UNVERIFIED** (local practice, no Bluebook authority)

Everything in this section is operational experience with the audit toolchain. None of it is a 22e
rule and none of it was traced to the corpus; it is kept because it is useful, and marked because an
unmarked heuristic is what this file exists to eliminate.

**Stage order.** Mechanical regex and chain checks first; per-footnote model audit second;
cross-footnote registry pass third; DOCX XML corrections fourth; archiving last. Each stage catches a
different error class, and the later stages are expensive.

**Formatted text is essential for a model audit.** Plain-text footnotes produce mass false positives —
in one run, 414 flagged issues from 239 footnotes, the great majority spurious. Without typeface
information the model cannot tell an italicized case name from roman text, small caps from roman, or
an italicized signal from the same word used in a sentence. Convert runs to inline markup first:
`*text*` italic, `[SC]text[/SC]` small caps, `**text**` bold, `***text***` bold italic. Pandoc is not
a substitute — Markdown has no small-caps representation, and the typeface distinction is exactly
what checks A6, D8, D10, D11, D12 and D15–D17 depend on.

**Per-footnote prompt.** Send the formatted footnote, its number, and the preceding footnote's
formatted text (B1 and C1 cannot be judged without it), and request structured JSON —
`{issue, rule, severity, suggested_fix}`. A five-footnote lookback window is needed for C1 and C4.

**Cross-footnote registry.** Build a map of hereinafter definitions and of author to cited works
before resolving any supra. Where one author has several works, an author-plus-note match is not
enough — the note number must resolve to the right title. Grade matches high / medium / low and
auto-fix only the high tier.

**Perma.cc.** Free accounts are capped (10 links/month) and unusable for a law review manuscript;
institutional accounts archive into an organization folder, and the folder id must be passed on
creation or the request falls back to the personal cap. Deduplicate URLs before archiving, persist
the `{url: guid}` map after every success so a mid-run failure resumes, and space requests about a
second apart. Insert as `https://www.example.com/report.pdf [https://perma.cc/ABCD-1234].` — bracket
placement is the part that is a rule, and it is E2, not this section.

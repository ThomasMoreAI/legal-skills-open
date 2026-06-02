---
name: screen-trademark
title: Screen Trademark
description: Screen proposed trademark → conflicts + distinctiveness pre-filing. TM DB search (TMview, WIPO, USPTO TESS), Abercrombie spectrum, likelihood-of-confusion (DuPont|EUIPO), common law rights, goods/services overlap. Produces conflict report w/ risk matrix. Use → pre-adopt new brand|logo|slogan — distinct from patent prior art (diff DBs, legal frame, methods).
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/caveman-ultra/skills/screen-trademark
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: ip
language: en
---

# Screen Trademark

Screen proposed mark → conflicts + assess distinctiveness pre-filing. Search registries, eval Abercrombie, analyze confusion w/ priors, produce report w/ risk ratings.

## Use When

- Pre-adopt new brand|product|service mark
- Rebrand|expand into new goods/services class
- Pre-file TM application (national|EU|intl)
- Eval acquisition w/ TM portfolios
- Pre-launch product new geo w/ existing brand
- C&D received → assess exposure

## In

- **Required**: Proposed mark (word|figurative|both)
- **Required**: Goods/services covered (plain desc)
- **Required**: Geo scope (US|EU|specific|global)
- **Optional**: Nice classification classes if known
- **Optional**: First-use date (US common law priority)
- **Optional**: Known competing marks
- **Optional**: Word|figurative|composite

## Do

### Step 1: Define Mark + Goods/Services

Establish exact what + which classes.

1. Record mark precisely:
   - Word: text as appears (case for figurative)
   - Figurative: visual elements, colors, stylization
   - Composite: both
2. Describe goods/services plain
3. Nice classification:
   - TMclass (https://tmclass.tmdn.org/)
   - Search keyword → correct class + acceptable terms
   - Most marks 1-3 classes; ID all relevant
   - Adjacent (Class 9 software vs Class 42 SaaS)
4. Geo scope:
   - US (USPTO), EU (EUIPO), intl (WIPO Madrid), national offices
   - US = first-to-use; EU = first-to-file

→ Record of mark, goods/services, Nice classes, jurisdictions. Defines search scope.

If err: Nice ambiguous → err on more classes. Broader screen safer than missing adjacent conflict.

### Step 2: Search TM Databases

Identical + similar across registries.

1. **Identical** first:
   - **TMview** (https://www.tmdn.org/tmview/): EU + national
   - **WIPO Global Brand DB** (https://branddb.wipo.int/): intl regs
   - **USPTO TESS / Trademark Center** (https://tsdr.uspto.gov/): US
   - **National**: DPMAregister (DE), UKIPO (UK), CIPO (CA)
2. **Similar** — expand:
   - Phonetic ("Kool" vs "Cool", "Lyft" vs "Lift")
   - Visual ("Adidaz" vs "Adidas")
   - Transliterations + translations
   - Common prefix|suffix added|removed
   - Plurals, possessives, abbrev
3. Filter:
   - Status: live|registered + pending (ignore dead|cancelled)
   - Goods/services: same|related Nice
   - Geo: target jurisdictions
4. Per potential conflict record:
   - Mark text + reg/app number
   - Owner + jurisdiction
   - Nice classes + goods/services
   - Status (registered, pending, opposed) + dates
   - Identical|similar (and how: phonetic|visual|conceptual)

→ List of potential conflicts from ≥2 DBs, identical+similar in relevant classes+jurisdictions. Each w/ enough detail for Step 4.

If err: DB unavailable → note gap, proceed w/ available. Common word → large result; prioritize same|closely related Nice before expanding.

### Step 3: Distinctiveness

Where on Abercrombie spectrum.

1. **Abercrombie** (weak→strong):
   - **Generic**: Common name ("Computer Software" for software). Unregistrable
   - **Descriptive**: Directly describes ("Quick Print"). Registrable only w/ secondary meaning
   - **Suggestive**: Suggests but needs imagination ("Netflix"). Inherently distinctive
   - **Arbitrary**: Real word in unrelated ctx ("Apple"). Strong inherent
   - **Fanciful**: Coined w/ no prior meaning ("Xerox", "Kodak"). Strongest
2. Secondary meaning if descriptive:
   - Duration + extent of use
   - Ad spend + consumer exposure
   - Surveys|declarations
   - Media + unsolicited recognition
3. Genericide check:
   - Was once distinctive but now common? ("escalator", "aspirin" US)
4. Document w/ reasoning

→ Clear classification w/ rationale. Descriptive → assess if secondary meaning achievable. Suggestive|arbitrary|fanciful proceed confident.

If err: generic-descriptive border = significant risk. Recommend modify → push toward suggestive (add twist, combine unrelated) or prepare secondary meaning evidence strategy.

### Step 4: Likelihood of Confusion

Eval if proposed likely confused w/ priors found Step 2.

1. Per prior, assess **DuPont** (US) | **EUIPO relative grounds**:
   - **Mark similarity**:
     - Visual: side-by-side, letters, length, structure
     - Phonetic: pronunciation, syllables, stress, vowels
     - Conceptual: meaning, connotation, commercial impression
   - **Goods/services similarity**:
     - Same Nice = strong indicator not conclusive
     - Related goods diff classes can conflict
     - Trade channels + typical buyers
   - **Prior strength**:
     - Famous → broader (dilution doctrine)
     - Weak|descriptive → narrower
     - Market presence, ad spend, recognition
   - **Actual confusion evidence**:
     - Customer complaints, misdirected comms
     - Social media confusion
     - Prior opposition|cancellation
2. Weigh holistically:
   - No single factor dispositive; balancing
   - Strong mark sim can offset weak goods sim
   - Famous tips toward confusion easier
3. Rate per conflict:
   - **Blocking**: Near-identical same goods, strong prior
   - **High**: Similar same|related goods, or identical related
   - **Mod**: Similar related, or identical distant
   - **Low**: Weak similarity, distant goods, or weak prior

→ Rated conflict list w/ analysis. Most serious (blocking|high) w/ specific reasoning.

If err: borderline → conservative (higher risk). Safer to flag manageable than miss blocker.

### Step 5: Common Law Rights

Unregistered rights not in DB searches.

1. Search prior unreg use:
   - Business name registries + state|provincial DBs
   - Domain (WHOIS)
   - Social handles + business profiles
   - Industry directories + trade pubs
   - Google + general web for commercial use
2. Jurisdictional rules:
   - **US**: First-to-use → prior commercial use creates rights w/o reg
   - **EU**: First-to-file → reg priority but prior use limited defenses
   - **UK**: Passing off doctrine protects unreg w/ goodwill
3. Scope assessment:
   - Geo reach of prior user's market
   - Duration + consistency
   - Goodwill built?
4. Document + impact on overall risk

→ Supplementary unreg use list could create conflicts not visible in registry. Especially important US.

If err: common law overwhelming (common word) → focus same industry|category. Common law typically narrow scope — local bakery "Sunrise" doesn't block software "Sunrise."

### Step 6: Goods/Services Overlap

Competitive proximity detail.

1. Compare Nice vs each prior:
   - Same class: presumptive overlap (not auto — classes broad)
   - Adjacent: complementary or competitive?
   - Distant: typically safe unless prior famous
2. Trade channels:
   - Sold via same retailers|platforms?
   - Same demographic?
   - Buyer assume common source?
3. Expansion likelihood:
   - Prior likely expand into proposed?
   - "Zone of natural expansion" (US)
4. Document w/ reasoning

→ Clear goods/services proximity per conflict, strengthening|weakening Step 4 ratings.

If err: relationship unclear (novel categories, convergent industries) → reasonable consumer test: typical buyer seeing both assume same source?

### Step 7: Conflict Report

Compile all → structured actionable report.

1. **TM Conflict Report** sections:
   - **Exec summary**: proposed mark, key findings, overall risk
   - **Mark + scope**: desc, Nice, jurisdictions
   - **Distinctiveness**: Abercrombie, registration implications
   - **Conflict matrix**: all conflicts + risk

```
Conflict Risk Matrix:
+----+-------------------+----------+---------+-------+---------+
| #  | Prior Mark        | Classes  | Juris.  | Type  | Risk    |
+----+-------------------+----------+---------+-------+---------+
| 1  | ACMESOFT          | 9, 42    | US, EU  | Ident | BLOCK   |
| 2  | ACME SOLUTIONS    | 42       | US      | Sim   | HIGH    |
| 3  | ACMEX             | 35       | EU      | Phon  | MOD     |
| 4  | ACM               | 16       | US      | Vis   | LOW     |
+----+-------------------+----------+---------+-------+---------+
Risk: BLOCK = blocking | HIGH | MOD = moderate | LOW | CLEAR
Type: Ident = identical | Sim = similar | Phon = phonetic | Vis = visual
```

   - **Common law findings**: relevant unreg use
   - **Goods/services analysis**: per conflict overlap
   - **Recommendations** — overall conclusion:
     - **Clear**: No significant conflicts → proceed file
     - **Low**: Minor conflicts unlikely block → proceed monitor
     - **Mod**: Conflicts manageable → coexistence|modify|narrow goods
     - **High**: Likely opposition|refusal → modify substantial or alt mark
     - **Blocking**: Near-identical prior same goods → don't proceed w/o counsel
2. Limitations + caveats:
   - Screen ≠ legal opinion; consult counsel pre-file
   - Common law may exist beyond DB
   - Figurative similarity needs visual inspection (beyond text search)

→ Complete report w/ ratings, distinctiveness, recommendations. Enables go/no-go.

If err: inconclusive (mixed cross jurisdictions|classes) → present by jurisdiction; let decision-maker weigh business + legal. Qualified "proceed w/ caution" valid.

## Check

- [ ] Mark + goods/services documented w/ Nice
- [ ] ≥2 TM DBs searched (TMview + USPTO TESS)
- [ ] Identical + similar searched (phon, vis, conceptual)
- [ ] Distinctiveness on Abercrombie w/ reasoning
- [ ] Confusion analyzed via DuPont|EUIPO
- [ ] Common law investigated (biz names, domains, web)
- [ ] Goods/services overlap per conflict
- [ ] Conflict matrix w/ ratings
- [ ] Overall recommendation (clear|low|mod|high|blocking)
- [ ] Limitations stated (screen vs legal opinion, DB gaps)

## Traps

- **Identical-only search**: Misses dangerous — phonetic|visual sim trigger confusion. Always variants.
- **Ignore related classes**: Software (9) can conflict SaaS (42)|consulting (35). Nice = guidelines not walls.
- **Skip common law**: US — unreg w/ prior use trumps later federal reg. DB alone insufficient.
- **Distinctiveness ≠ availability**: Highly distinctive (fanciful) mark can conflict existing identical reg. Separate questions.
- **Single-jurisdiction bias**: Clear US may block EU. Always screen actual-use jurisdictions.
- **Treat screen as legal opinion**: Skill produces structured risk, not legal advice. Blocking|high warrant counsel review.

## →

- `assess-ip-landscape` — broader IP landscape mapping w/in full IP strategy
- `search-prior-art` — patent-focused prior art (diff DBs + legal: novelty|obviousness vs confusion)
- `file-trademark` — filing post-screen (not yet avail)

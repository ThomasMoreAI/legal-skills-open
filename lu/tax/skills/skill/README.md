<p align="center">
  <img src="assets/banner.png" alt="Paperasse Lux" width="100%">
</p>

<h1 align="center">Paperasse Lux</h1>

<p align="center">
  <b>Des skills pour agents IA spécialisés dans la bureaucratie luxembourgeoise.</b>
</p>

<p align="center">
  <i>Parce que la paperasse luxembourgeoise est aussi rigoureuse que les frites du Bouneweger Stuff sont fondantes.</i>
</p>

<p align="center">
  <a href="https://github.com/gregherbe76/Luxembourg-Paperasse/stargazers"><img src="https://img.shields.io/github/stars/gregherbe76/Luxembourg-Paperasse" alt="GitHub stars"></a>
  <img src="https://img.shields.io/badge/skills-6-red" alt="6 skills">
  <img src="https://img.shields.io/badge/assistant-administratif-ED2939" alt="Assistant administratif">
  <img src="https://img.shields.io/badge/pays-Luxembourg-ED2939" alt="Pays Luxembourg">
  <img src="https://img.shields.io/badge/veille-Légilux_RSS-008751" alt="Veille Légilux RSS">
  <a href="https://github.com/gregherbe76/Luxembourg-Paperasse/blob/main/LICENSE"><img src="https://img.shields.io/github/license/gregherbe76/Luxembourg-Paperasse?style=flat&color=blue" alt="License"></a>
  <a href="https://github.com/gregherbe76/Luxembourg-Paperasse/actions/workflows/tests.yml"><img src="https://github.com/gregherbe76/Luxembourg-Paperasse/actions/workflows/tests.yml/badge.svg" alt="Tests"></a>
  <a href="https://github.com/gregherbe76/Luxembourg-Paperasse/actions/workflows/validate.yml"><img src="https://github.com/gregherbe76/Luxembourg-Paperasse/actions/workflows/validate.yml/badge.svg" alt="Validate"></a>
  <a href="https://agentskill.sh/@gregherbe76"><img src="https://img.shields.io/badge/AgentSkill.sh-@gregherbe76-8b5cf6?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDIgN2wxMCA1IDEwLTUtMTAtNXptMCAxMy41TDIgMTBsMTAgNSAxMC01LTEwIDUuNXoiLz48L3N2Zz4=" alt="AgentSkill.sh"></a>
</p>

<br />

---

## Qu'est-ce que Paperasse Lux ?

<b>Paperasse Lux est une collection de skills pour agents IA ([Claude Code](https://claude.com/product/claude-code), [Claude Cowork](https://claude.com/product/cowork), [Codex](https://openai.com/codex/), [Mistral Vibe](https://vibe.mistral.ai), [Cursor](https://cursor.com), [Windsurf](https://windsurf.com), [Cline](https://cline.bot), [Aider](https://aider.chat)) spécialisés dans la comptabilité, la fiscalité, la facturation, le notariat et l'audit des entreprises et particuliers au Grand-Duché de Luxembourg.</b>

Chaque skill transforme votre agent en copilote expert d'un métier de la paperasse luxembourgeoise : comptabilité (PCN, TVA Lux, IRC + ICC + IF, FAIA, eCDF, dépôt RCS), facturation (mentions obligatoires, Peppol BIS 3.0, e-invoicing B2G obligatoire), contrôle fiscal (ACD/AED), audit (réviseur d'entreprises agréé, normes ISA-LUX), fiscalité des particuliers (RTS, classes 1/1a/2 avec splitting, abattements, prime participative, stock-options, retraite, frontaliers), droit notarial (Bëllegen Akt 40 000 €/personne depuis oct. 2024, droits d'enregistrement, successions ligne directe exonérées, donations, contrat de mariage, PACS), et gestion de copropriété (loi du 16 mai 1975 modifiée par la loi du 16 décembre 2019).

Les skills connaissent les textes (LIR, LITL, LCC, loi modifiée du 12 février 1979 sur la TVA, loi du 10 août 1915 sur les sociétés commerciales, loi du 19 décembre 2002 RCS, loi du 16 mai 1975 copropriété), les formulaires, les échéances, et ne se trompent pas de case dans la déclaration eCDF.

Les skills sont du Markdown. Ils fonctionnent avec tout agent ou outil capable de lire des fichiers. Paperasse Lux inclut aussi un **flux de veille du Journal Officiel** (4 RSS Légilux : Mémorial A, B, A+B, projets de loi) pour rester à jour des publications légales en temps réel.

---

## Assistant administratif

Au-delà des calculateurs, Paperasse Lux embarque un **assistant administratif** (skill racine [`SKILL.md`](SKILL.md)) qui relie une *situation* ou un *courrier* à ses **obligations**, échéances, risques et **sources officielles**, puis propose checklist, courrier-projet et rappels. Il **n'effectue jamais de démarche** : il aide à comprendre et à préparer, l'utilisateur valide et agit.

Principe cardinal : **aucune obligation, aucun délai, aucun montant n'est affiché sans source + date de vérification + niveau de confiance** ; toute information incertaine est signalée comme à revérifier.

```bash
# Assistant conversationnel
paperasse assistant "J'ai reçu une lettre de l'AED, que faire ?" --doc courrier.txt
paperasse assistant "Je suis frontalier français et je télétravaille 2 jours/semaine" --profil '{"paysResidence":"FR","joursHorsLU":40}'

# Diagnostic, questionnaire dynamique, tableau de bord (fr/en/de/lb)
paperasse diagnostic questionnaire
paperasse diagnostic dashboard --json '{"regimeTVA":"normal","frequenceTVA":"mensuelle","statut":"actif"}' --langue en

# Parcours métier
paperasse tva-suivi calendrier --freq mensuelle --debut 2026-01-15
paperasse entreprise parcours --exercice 2025-12-31
paperasse particulier frontalier --pays FR --brut 5000 --jours 40
paperasse residence installation --nationalite US --arrivee 2026-03-01
paperasse logement acheteur --prix 600000 --acquereurs 2

# Analyse de courrier, courriers-projets, rappels, base de connaissances, RGPD
paperasse diagnostic document --file courrier-aed.txt
paperasse courriers reponse --file courrier-aed.txt --json '{"expediteur":"Jean Test"}'
paperasse rappels societe
paperasse connaissances citer --id obl_tva_declaration_mensuelle
paperasse rgpd masquer --file donnees.json
```

Le moteur (`lib/diagnostic`, `lib/documents`, `lib/tva`, `lib/entreprise`, `lib/particulier`, `lib/residence`, `lib/logement`, `lib/courriers`, `lib/rappels`, `lib/connaissances`, `lib/rgpd`, `lib/i18n`, `lib/conversation`) est **zéro-dépendance** et couvert par une suite de tests déterministes (dont 15 scénarios de bout en bout). Voir la [feuille de route de l'assistant](https://gregherbe76.github.io/Luxembourg-Paperasse/assistant-administratif.html).

---

## AgentSkill.sh

Profil et collection de skills publiés par l'auteur :

**[https://agentskill.sh/@gregherbe76](https://agentskill.sh/@gregherbe76)**

Vous y retrouvez les skills Paperasse Lux indexés et prêts à être installés en un clic dans votre agent IA, ainsi que les autres skills publiés par [@gregherbe76](https://agentskill.sh/@gregherbe76).

---

## Documentation

📖 **Site complet : [gregherbe76.github.io/Luxembourg-Paperasse](https://gregherbe76.github.io/Luxembourg-Paperasse/)** — démarrage rapide, fiche par module (FAIA, RTS, Bëllegen Akt, eCDF, LBR, STATEC…), sources officielles, FAQ.

## Installation en une commande (à venir sur npm)

```bash
npm install -g paperasse-lux
paperasse rts --brut 5000 --classe 1
paperasse statec ssm
paperasse bellegen-akt --prix 600000 --acquereurs 2
```

## Installation rapide

### Option 1 : installation via GitHub (recommandé)

Copiez-collez ces instructions dans votre agent IA :

```
Installe tous les skills du repo github https://github.com/gregherbe76/Luxembourg-Paperasse
Lance ensuite le setup pour la gestion de toute ma paperasse luxembourgeoise
```

L'agent va cloner le repo, installer les skills, et lancer le setup guidé qui vous posera quelques questions (raison sociale, numéro RCS Luxembourg, matricule TVA, forme juridique, exercice, comptes bancaires LU) pour configurer votre environnement.

### Option 2 : installation manuelle

Clonez le repo et copiez les skills dans le dossier de votre agent :

```bash
git clone https://github.com/gregherbe76/Luxembourg-Paperasse
cp -r Luxembourg-Paperasse/{comptable,controleur-fiscal,commissaire-aux-comptes,fiscaliste,notaire,syndic} ~/.claude/skills/
cp Luxembourg-Paperasse/company.example.json ~/company.json  # à éditer ensuite
```

---

## Les 6 skills

| Skill | Rôle | Ce qu'il fait |
|-------|------|---------------|
| **`comptable`** | Expert-Comptable Luxembourg | Écritures comptables (PCN — Règlement grand-ducal du 12 sept. 2019), TVA Lux (17 / 14 / 8 / 3 %), IRC + 7 % chômage + ICC (~6,75 % Lux-Ville), IF, clôture annuelle, FAIA, eCDF, dépôt RCS dans 7 mois, facturation conforme (mentions, Peppol BIS 3.0, e-invoicing B2G obligatoire depuis 2023) |
| **`controleur-fiscal`** | Contrôleur ACD/AED | Simulation de contrôle fiscal sur 8 axes (TVA, IRC, ICC, IF, prix de transfert, frais de personnel, amortissements, provisions), chefs de redressement avec base légale et montants |
| **`commissaire-aux-comptes`** | Réviseur d'entreprises agréé | Audit en 7 phases selon ISA-LUX, validation FAIA / bilan / CR / eCDF, opinion motivée, dépôt RCS |
| **`fiscaliste`** | Fiscaliste Particuliers | RTS, classes 1 / 1a / 2 (splitting), barème progressif IRPP, crédits d'impôt, stock-options, prime participative, RTSI, retraite (PER lux), frontaliers (FR / BE / DE) |
| **`notaire`** | Notaire | Frais d'acte (droits d'enregistrement 6 % + transcription 1 %), abattement Bëllegen Akt 40 000 €/personne depuis 1ᵉʳ oct. 2024, successions (exonération en ligne directe), donations, SCI, contrat de mariage (art. 1400 + règlement UE 2016/1103), PACS, vente immobilière |
| **`syndic`** | Syndic de Copropriété | Gestion selon loi du 16 mai 1975 modifiée par la loi du 16 décembre 2019 : AG, appels de fonds, fonds de prévoyance, état daté, contentieux et recouvrement, comptabilité copropriété |

---

## Exemples d'utilisation

```
> Voici mes transactions BCEE. Catégorise-les et génère les écritures PCN.

> Fais la clôture annuelle de ma SARL luxembourgeoise pour l'exercice 2025.

> Simule un contrôle ACD sur ma TVA 2024.

> Audite mes comptes annuels avant dépôt RCS.

> Calcule les frais d'acte pour un appartement à 650 000 € à Luxembourg-Ville (premier achat, célibataire).

> Mon père est décédé, nous sommes 3 enfants en ligne directe. Quels droits de succession ?

> Rédige les statuts d'une SARL-S (1 €) avec 2 associés.

> Prépare la convocation de l'AG annuelle de ma copropriété de 12 lots.

> Génère une facture conforme Lux pour mon client (avec champ Peppol B2G).

> Suis-je concerné par la franchise PME 50 000 € depuis 2025 ?

> Frontalier français : 80 % au Lux, 20 % télétravail FR. Comment ça se déclare ?

> J'ai vesté 50 000 € de stock-options en 2025. Régime fiscal ?

> Ma copro a 12 lots, charges annuelles 45 000 €. Prépare l'AG annuelle.
```

---

## Workflow : de zéro à la clôture annuelle

```
Fais la clôture annuelle de ma société luxembourgeoise
```

Les 4 skills s'enchaînent pour couvrir tout le cycle :

1. **Comptabilité courante** (`comptable`) : classification, écritures PCN, TVA, rapprochement bancaire (BCEE, BIL, BGL BNP Paribas, ING, Raiffeisen)
2. **Clôture annuelle** (`comptable`) : cut-off, amortissements, provisions, IRC + ICC + IF, FAIA, eCDF, dépôt RCS
3. **Audit** (`commissaire-aux-comptes`) : vérification FAIA, contrôle bilan / CR / eCDF, opinion (si seuils audit dépassés)
4. **Contrôle fiscal** (`controleur-fiscal`) : simulation ACD sur 8 axes

---

## Veille du Journal Officiel (Légilux)

Paperasse Lux intègre une veille en temps réel des **4 flux RSS du Service Central de Législation** :

| Flux | URL |
|---|---|
| Mémorial A — Législation | `https://data.legilux.public.lu/api/rss-leg.xml` |
| Mémorial B — Administration | `https://data.legilux.public.lu/api/rss-adm.xml` |
| Mémorials A + B (tout) | `https://data.legilux.public.lu/api/rss.xml` |
| Projets de loi | `https://data.legilux.public.lu/api/rss-draft.xml` |

Les skills consultent ces flux avant de produire un livrable, pour détecter une évolution légale récente. Voir [`references/legilux-flux-rss.md`](./references/legilux-flux-rss.md) pour la documentation complète et les mots-clés de filtrage par skill.

---

## Scripts et templates

Le repo inclut des scripts Node.js et des templates pour la génération de documents :

```bash
npm install
cp company.example.json company.json   # puis remplir vos infos
npm run closing                        # génère états financiers + FAIA + PDFs
```

| Script / Template | Génère |
|-------------------|--------|
| `scripts/calc.js` | Calculs déterministes (IRPP, IRC + ICC + IF, TVA, Bëllegen Akt, prorata) |
| `scripts/generate-statements.js` | Bilan, Compte de Résultat, Balance au format PCN |
| `scripts/generate-faia.js` | Fichier d'Audit Informatisé AED (FAIA) depuis JSON |
| `scripts/generate-pdfs.js` | Conversion des états en PDF A4 avec en-tête société |
| `scripts/generate-facture-lux.js` | Facture PDF conforme LU avec champ Peppol B2G |
| `scripts/validate-facture.js` | Vérification mentions obligatoires (TVA LU, RCS, IBAN, Peppol B2G) |
| `templates/facture-lux.html` | Template facture conforme Lux |
| `templates/declaration-tva-100-checklist.md` | Checklist déclaration TVA 100 |
| `templates/pv-approbation-comptes.md` | PV d'approbation des comptes annuels |
| `templates/convocation-ag-copropriete.md` | Convocation d'AG de copropriété (loi 16 mai 1975) |

---

## Intégrations (banques LU, Stripe, Peppol B2G)

Connecteurs pour récupérer transactions et paiements automatiquement.

```bash
npm run fetch          # Récupère Tink (PSD2) + Stripe
npm run fetch:tink     # Banques LU (BCEE, BIL, BGL, ING, Raiffeisen) via Tink
npm run fetch:stripe   # Stripe (multi-comptes + Connect)
```

Au Luxembourg, pas d'équivalent direct à Qonto avec API publique : on passe par un agrégateur PSD2 (Tink, Salt Edge, Klarna Kosma) qui parle à toutes les banques LU. Configuration et clés API : voir [`integrations/`](./integrations/) et `.env.example`.

Pour la facturation électronique B2G (obligatoire vers le secteur public LU depuis 2023, loi du 13 décembre 2021), voir [`integrations/peppol/`](./integrations/peppol/) — format Peppol BIS 3.0 obligatoire, à émettre via un point d'accès agréé (Storecove, Pagero, Unifiedpost…).

---

## Evaluations

Chaque skill est évalué automatiquement avec et sans le `SKILL.md` pour mesurer sa valeur ajoutée. Le runner utilise un grading LLM-as-judge avec rubrique luxembourgeoise (chiffres exacts, articles cités, contexte LU vs FR).

```bash
# Toute la suite (~10-15 min, requiert ANTHROPIC_API_KEY)
uv run --project evals python evals/run_evals.py

# Un seul skill
uv run --project evals python evals/run_evals.py --skill notaire

# Réutiliser le cache des runs précédents
uv run --project evals python evals/run_evals.py --reuse-cache

# Voir les résultats dans le navigateur
uv run --project evals python evals/generate_review.py evals-workspace/iteration-latest/

# Tableau comparatif sur toutes les itérations
uv run --project evals python evals/aggregate_benchmark.py
```

14 cas de test couvrent à ce jour les 6 skills (TVA Lux 2025, IRC+ICC+IF, dépôt RCS, prescription, prix de transfert, classes d'impôt + splitting, frontalier 34 jours, Bëllegen Akt 40 000 €, succession ligne directe, PACS, AG copropriété, fonds de prévoyance 2019…). Voir [`evals/tests/`](./evals/tests/).

---

## Garde-fous

- **Contexte entreprise** : chaque skill vérifie les informations minimales (raison sociale, numéro RCS Luxembourg, matricule TVA si assujetti, forme juridique, exercice) avant de procéder. Si `company.json` existe, il est lu automatiquement. Sinon, le skill pose les questions.

- **Échéances fiscales** : le skill comptable affiche les prochaines échéances (TVA mensuelle/trimestrielle/annuelle selon CA, acomptes IRC, dépôt RCS dans 7 mois après clôture).

- **Fraîcheur des données** : chaque skill a une date `last_updated`. Le législateur luxembourgeois change moins souvent que le français, mais les seuils (TVA, classes d'impôt, Bëllegen Akt) bougent. L'agent vérifie le flux Légilux et les sources officielles si la donnée a plus de 6 mois.

- **Données sourcées** : chaque affirmation chiffrée cite sa source primaire (Mémorial via lien ELI `data.legilux.public.lu/eli/...`, guichet.lu, impotsdirects.public.lu, aed.public.lu, lbr.lu, cssf.lu).

---

## Installation manuelle (par plateforme)

Les skills sont du Markdown. Ils marchent partout où un agent peut lire des fichiers.

| Plateforme | Où copier les skills |
|------------|---------------------|
| **Claude Code** | `~/.claude/skills/` |
| **Cursor** | `~/.cursor/skills/` |
| **Windsurf** | `~/.windsurf/skills/` |
| **Codex** | `~/.codex/skills/` |
| **Mistral Vibe** | `~/.vibe/skills/` |
| **Cline** | `~/.cline/skills/` |
| **Aider** | `~/.aider/skills/` |

---

## Différences clés avec la France

| Domaine | France | Luxembourg |
|--------|--------|-----------|
| Plan comptable | PCG | PCN (Règlement grand-ducal du 12 sept. 2019) |
| TVA standard | 20 % | 17 % |
| IS / IRC | 25 % | 17 % IRC + 7 % contribution chômage + ICC (~6,75 % Lux-Ville) ≈ 24,94 % |
| Liasse | Liasse 2050 etc. | eCDF (déclaration électronique) |
| FEC | FEC | FAIA (Fichier d'Audit Informatisé AED) |
| Régulateur audit | H3C | CSSF + IRE (Institut des Réviseurs d'Entreprises) |
| Impôt particuliers | IR + IFI | RTS + décompte annuel (3 classes), pas d'IFI |
| Droits succession enfant | Abattement 100 k€ + barème | Exonération en ligne directe (Lux) |
| Notaire vente | ~7-8 % | 7 % (Lux-Ville : 10 % avec surtaxe communale 3 %), abattement Bëllegen Akt 40 000 €/personne (loi 2024) |
| Copropriété | Loi 10 juillet 1965 | Loi 16 mai 1975 modifiée |
| Facturation électronique | Obligatoire 2026 (B2B) | Obligatoire B2G depuis 2023, B2B en cours |

---

## Sources et textes de référence

- **LIR** — Loi du 4 décembre 1967 concernant l'impôt sur le revenu
- **LITL** — Loi du 1ᵉʳ décembre 1936 concernant l'impôt commercial
- **LCC** — Loi du 19 décembre 2008 sur les comptes consolidés
- **Loi du 10 août 1915** sur les sociétés commerciales (modifiée)
- **Loi du 19 décembre 2002** concernant le RCS, la comptabilité et les comptes annuels
- **Loi modifiée du 12 février 1979** concernant la taxe sur la valeur ajoutée
- **Loi du 16 mai 1975** portant statut de la copropriété des immeubles bâtis (mod. loi du 16 déc. 2019)
- **Règlement grand-ducal du 12 septembre 2019** déterminant le PCN

Sources et flux de veille documentés dans [`data/sources.json`](./data/sources.json) et [`references/legilux-flux-rss.md`](./references/legilux-flux-rss.md).

---

## Avertissement légal

**Ces skills ne remplacent pas un expert-comptable membre de l'OEC, un réviseur d'entreprises agréé inscrit à l'IRE, un avocat inscrit au barreau de Luxembourg, ou un notaire en exercice.** Ils sont conçus comme outils d'aide à la décision et de préparation.

Pour les situations complexes (litiges, montages fiscaux, contrôles ACD/AED en cours, successions transfrontalières, copropriétés en contentieux), consultez un professionnel agréé au Grand-Duché de Luxembourg avec une assurance RC Pro.

---

## Contribuer

Vous avez un métier de la paperasse luxembourgeoise que vous aimeriez voir automatisé (avocat d'affaires, huissier, agent immobilier IFE, géomètre, family office) ? Consultez le [guide de contribution](CONTRIBUTING.md).

Les contributions de mises à jour de seuils légaux (suite à publication au Mémorial), nouveaux templates, ou corrections d'articles cités sont particulièrement bienvenues.

---

## Remerciements

- **Le Service Central de Législation** — Pour le Légilux, le Mémorial en ligne et les flux RSS publics
- **L'Administration des Contributions Directes (ACD)** — Pour la rigueur du barème IRPP
- **L'Administration de l'Enregistrement, des Domaines et de la TVA (AED)** — Pour la TVA Lux et le FAIA
- **Le Plan Comptable Normalisé** — Plus court que le PCG français, et c'est tant mieux
- **[Romain Simon](https://github.com/romainsimon)** — Pour le projet [Paperasse](https://github.com/romainsimon/paperasse) original qui a inspiré cette adaptation

---

<p align="center">
  <i>Au Luxembourg, la paperasse parle 3 langues. Heureusement, l'IA aussi.</i>
  <br>
  — Personne de célèbre, jamais
</p>

---

<a href="https://www.star-history.com/?repos=gregherbe76%2FLuxembourg-Paperasse&type=date&legend=bottom-right">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=gregherbe76/Luxembourg-Paperasse&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=gregherbe76/Luxembourg-Paperasse&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=gregherbe76/Luxembourg-Paperasse&type=date&legend=top-left" />
 </picture>
</a>

---

<p align="center">
  Fait avec des kniddelen et beaucoup de café au Grand-Duché de Luxembourg | <a href="LICENSE">Licence MIT</a>
</p>

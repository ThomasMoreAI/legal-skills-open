#!/usr/bin/env python3
"""Repère les fautes mécaniques d'un texte normatif français (langue, présentation, formules proscrites).

Usage :
    python3 lint_legistique.py projet.txt            # tableau Markdown des constats
    python3 lint_legistique.py projet.txt --json     # constats en JSON
    python3 lint_legistique.py projet.txt --refs [--source demande.txt]
                                                     # liste des références juridiques citées ;
                                                     # avec --source, marque celles absentes de la demande
    python3 lint_legistique.py reponse.md --markdown # fichier Markdown : seuls les blocs ``` (ou, à défaut,
                                                     # le texte hors titres et tableaux) sont contrôlés ;
                                                     # option implicite pour un fichier .md
    python3 lint_legistique.py projet.txt --sans-structure
                                                     # contrôles ligne à ligne seulement
    cat projet.txt | python3 lint_legistique.py -    # lecture sur l'entrée standard

Deux familles de contrôles :
- ligne à ligne (langue, présentation, formules proscrites) ;
- structure du texte entier (règles « structure-… ») : numérotation des articles, article d'exécution
  absent ou mal placé, entrée en vigueur après l'article d'exécution, visas ou article d'exécution dans
  une loi, ordre des visas, « susvisé » (code, loi, texte absent des visas, disposition insérée), même
  article du texte modifié touché par plusieurs dispositions du projet.

Le script ne fait que signaler des candidats : chaque constat se relit dans son contexte avant d'être
retenu. Il ne regarde pas :
- les mots cités d'un texte existant (« les mots : « … » sont remplacés ») : ils reproduisent le texte en
  vigueur et ne se corrigent pas ;
- le futur de la formule de publication (« qui sera publié au Journal officiel ») ;
- « visé » et « notamment » dans les visas (lignes « Vu … »), où ils sont d'usage.
Seule la bibliothèque standard de Python 3.8+ est utilisée.
"""
import argparse
import json
import re
import sys

# (identifiant, motif, message, fiche, gravité par défaut, options)
# Gravité : B bloquant, R recommandé, S style (voir references/grille-de-relecture.md).
RULES = [
    # --- Formules proscrites et renvois ---
    ("dispositions-contraires", r"\btoutes? (?:les )?dispositions? contraires?\b",
     "abrogation « balai » sans effet : recenser et abroger explicitement", "3.8.3", "B", {}),
    ("renvoi-modalites", r"\bmodalités d'application du présent (?:décret|arrêté)\b",
     "renvoi non encadré : préciser l'objet exact du texte d'application", "3.5.3", "B", {}),
    ("date-par-arrete", r"\bà une date fixée par (?:arrêté|décret)\b(?![^.]*au plus tard)",
     "date d'entrée en vigueur laissée à un autre texte sans borne", "3.8.1", "B", {}),
    ("abroge-et-remplace", r"\babrogée?s? et remplacée?s?\b",
     "écrire « est remplacé par les dispositions suivantes » (règlement) ou « est ainsi rédigé » (loi)", "3.4.1", "R", {}),
    ("redige-ainsi", r"\b(?:rédigée?s? ainsi qu'il suit|ainsi conçue?s?)\b",
     "formule proscrite : « ainsi rédigé »", "3.4.1", "R", {}),
    ("renvoi-relatif", r"\b(?:alinéa|article|paragraphe)s? (?:précédent|suivant)e?s?\b",
     "renvoi relatif : désigner l'alinéa ou l'article par son rang ou son numéro", "3.2.2", "R", {}),
    ("etc", r"\betc\b\.?", "« etc. » : énumérer de façon exhaustive ou employer une catégorie", "3.3.1", "R", {}),
    ("jorf", r"\bJORF\b|\bJ\.\s?O\.",
     "écrire « Journal officiel de la République française »", "annexe typo", "R", {}),

    ("non-normatif",
     r"\b(?:a|ont) pour (?:objectifs?|ambition|vocation|finalité)\b|\bvisent? à\b|\bs'efforcen?t?\b"
     r"|\bencouragen?t?\b|\bfavorisen?t?\b|\bpromeu(?:t|vent)\b|\breconna(?:ît|issent)\b|\bLa Nation\b"
     r"|\bil (?:est|serait) souhaitable\b|\bdans (?:toute )?la mesure du possible\b|\b(?:une|par la) loi ultérieure\b",
     "formule sans portée normative probable : dire qui doit, peut ou ne peut pas faire quoi, ou reporter "
     "dans l'exposé des motifs ou la notice", "1.2.1", "S", {"skip_visas": True, "skip_notice": True}),

    # --- Temps, mode, renfort ---
    ("doit", r"\b(?:doit|doivent)\b", "« doit » : le présent de l'indicatif suffit à obliger", "3.3.1", "R", {}),
    ("futur", r"\b(?:sera|seront|devra|devront|pourra|pourront|fera|feront|aura|auront|ira|iront)\b"
              r"|\b\w{3,}(?:eront|iront)\b|\b\w{3,}(?<!cam)(?<!op)(?<!chim)era\b|\b\w{2,}(?:ra|ront)\b",
     "futur : employer le présent de l'indicatif", "3.3.1", "R", {"futur": True}),
    ("renfort", r"\b(?:impérativement|obligatoirement|rigoureusement|strictement)\b",
     "adverbe de renfort inutile", "3.3.1", "R", {}),

    # --- Phrases et vocabulaire ---
    ("et-ou", r"\bet ?/ ?ou\b", "« et/ou » : écrire « ou », qui n'est pas exclusif en droit", "3.3.1", "R", {}),
    ("le-ou-les", r"\b(?:le|la|l'|du|de la|au|à la) ou (?:les|des|aux)\b",
     "« le ou les » : le singulier générique suffit", "3.3.1", "R", {}),
    ("ledit", r"\b(?:ledit|ladite|lesdits|lesdites|dudit|de ladite|desdits|desdites|auxdits|auxdites)\b",
     "« ledit » : écrire « ce », « cet », « cette », « ces »", "3.3.2", "S", {}),
    ("sus", r"\b(?:susdite?s?|susnommée?s?|susmentionnée?s?|sus-mentionnée?s?)\b",
     "écrire « mentionné ci-dessus » (« susvisé » seulement pour un texte des visas)", "3.3.2", "S", {}),
    ("latin", r"\b(?:in fine|in situ|a contrario|a priori|a posteriori|de jure|de facto|ex nihilo|supra|infra)\b",
     "locution latine : employer l'équivalent français", "3.3.1", "R", {}),
    ("en-charge", r"\ben charge (?:de|du|des)\b", "« en charge de » : écrire « chargé de »", "3.3.1", "R", {}),
    ("anglicisme", r"\b(?:impact(?:er|e|ent|é|ée|és|ées|ant)|initi(?:er|e|ent|é|ée|és|ées)|finalis(?:er|e|ent|é|ée|és|ées)|en capacité de)\b",
     "anglicisme : affecter, engager, achever, compétent pour…", "3.3.1", "R", {}),
    ("concerne", r"(?<!Publics )\b(?:concernée?s?|concernant)\b",
     "« concerné » : intéressé, en cause ; « concernant » : relatif à", "3.3.2", "S", {}),
    ("passe-partout", r"\b(?:effectu(?:er|e|ent|é|ée|és|ées)|dans le cadre d[eu']|au niveau d[eu']|déclin(?:er|e|é|ée))\b",
     "mot passe-partout : employer le verbe ou la préposition précis", "3.3.2", "S", {}),
    ("vise", r"\bvisée?s? (?:à|au|aux|par|ci-dessus)\b",
     "« visé » est réservé aux visas : écrire « mentionné », « prévu », « défini »", "3.3.2", "R", {"skip_visas": True}),
    ("et-notamment", r"\bet notamment\b", "« et notamment » : écrire « notamment »", "3.3.2", "S", {}),
    ("notamment", r"(?<!et )\bnotamment\b",
     "« notamment » : vérifier qu'il n'élargit pas une obligation, une interdiction ou une sanction",
     "3.3.2", "S", {"skip_visas": True, "notamment": True}),
    ("mademoiselle", r"\b(?:Mademoiselle|nom de jeune fille|nom d'épouse?)\b",
     "écrire « Madame », « nom de famille », « nom d'usage »", "3.3.2", "R", {}),

    # --- Présentation et nombres ---
    ("article-1", r"^\s*Article 1\s*$|^\s*Art(?:icle|\.) 1(?:\.| –| -)",
     "tête d'article : « Article 1er »", "annexe typo", "R", {}),
    ("article-1-corps", r"\barticle 1(?!er|\d|[-.,]\d)\b", "renvoi : « article 1er »", "annexe typo", "R", {}),
    ("alinea-chiffre", r"\balinéas? \d+\b|\b\d+(?:e|è|ème|er|ère)s? alinéas?\b",
     "alinéa désigné en lettres : « deuxième alinéa »", "annexe typo", "R", {}),
    ("ordinal-abrege", r"\b\d+(?:ème|ère|è)\b", "ordinal abrégé : écrire en lettres", "annexe typo", "S", {}),
    ("duree-chiffres", r"\b(?P<n>\d{1,2}) (?:jours?|semaines?|mois|ans?|années?|heures?|fois|membres?|représentants?|personnes?|exemplaires?)\b",
     "durée ou quantité inférieure à cent : l'écrire en lettres", "annexe typo", "R", {}),
    ("guillemets-droits", r"[\"“”]", "guillemets français « » (guillemets anglais seulement dans une citation)",
     "annexe typo", "R", {}),
    ("pour-cent", r"\b(?:p\. ?cent|pour cent)\b", "écrire « % »", "annexe typo", "S", {}),
    ("milliers-point", r"\b\d{1,3}\.\d{3}\b", "séparateur de milliers : espace insécable, pas de point", "annexe typo", "S", {}),
    ("parentheses", r"\((?!le reste sans changement\))(?!section )(?![^()]*https?:)[^()\n]{1,120}\)",
     "parenthèse dans le dispositif : l'intégrer à la phrase ou la supprimer", "3.3.1", "R", {}),
    ("sigle", r"\b[A-Z][A-Z0-9]{1,}(?:-[A-Z0-9]+)*\b",
     "sigle : désigner l'organisme en toutes lettres (tolérés dans la notice)", "3.3.1", "R", {"sigle": True}),
    ("tiret-enumeration", r"^\s*(?:[-–—•*])\s+\S",
     "énumération à tirets : préférer 1°, 2°, 3° puis a), b)", "3.2.2", "S", {}),
    ("deux-points-colles", r"[^\s«:/]:(?:\s|$)", "espace avant le deux-points", "annexe typo", "S", {}),
]

# Règles où la casse compte (sigles, têtes d'article, abréviations).
CASE_SENSITIVE = {"sigle", "article-1", "article-1-corps", "jorf", "guillemets-droits", "deux-points-colles", "tiret-enumeration"}

# Mots en capitales qui ne sont pas des sigles à signaler.
NOT_SIGLES = {
    "NOR", "LO", "TITRE", "CHAPITRE", "SECTION", "LIVRE", "PARTIE", "DISPOSITIONS", "GÉNÉRALES",
    "GENERALES", "FINALES", "TRANSITOIRES", "PÉNALES", "PENALES", "DIVERSES", "ANNEXE", "PREMIER",
    "PRELIMINAIRE", "PRÉLIMINAIRE", "UNIQUE", "RF", "ER",
}
# Mots en -ra / -ront qui ne sont pas des futurs.
FUTUR_EXCLUS = {
    "front", "affront", "opéra", "caméra", "choléra", "extra", "ultra", "intra", "contra", "mantra", "cobra",
    "agora", "flora", "sahara", "sierra", "véra", "zébra", "para", "hydra", "tiara", "supra", "infra",
    "confront",
}
ROMAN = re.compile(r"^(?=[MDCLXVI]+$)M{0,3}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})$")
SANCTION = re.compile(
    r"\b(?:sanction\w*|amende\w*|puni\w*|pénal\w*|interdi\w*|infraction\w*|contravention\w*|délit\w*|"
    r"retir\w*|retrait|suspen\w*|reversement|rembours\w*|manquement\w*|méconn\w*)\b", re.I)
# Amendement : le chapeau désigne les alinéas par leur numéro de pastille (« Alinéa 4 », « après l'alinéa 4 »).
AMENDEMENT = re.compile(r"^\s*(?:AMENDEMENT\b|EXPOSÉ SOMMAIRE\b)", re.M)
CHAPEAU = re.compile(r"\b(?:[Ss]upprimer|[Rr]édiger ainsi|[Ss]ubstituer|[Rr]emplacer|[Ii]nsérer|[Cc]ompléter|[Rr]établir)\b"
                     r"|^\s*Alinéas? \d+")
NOTICE = re.compile(r"^(?:Publics? concernés?|Objet|Entrée en vigueur|Notice|Références|Application)\s*:")
PUBLICATION = re.compile(r"\bsera publiée? (?:au|dans le) (?:Journal officiel|JORF|J\.\s?O\.|bulletin officiel|recueil des actes)", re.I)

# Passages cités d'un texte existant : « les mots : « … » », « la phrase : « … » », etc., sauf après « par ».
CITED_INTRO = re.compile(
    r"(?<!par )(?:les|le|la|l')\s*(?:mots?|phrases?|références?|chiffres?|nombres?|sommes?|dates?|taux|"
    r"montants?|années?|expressions?|termes?)\s*:?\s*$", re.I)


def quoted_spans(text):
    """Renvoie les segments « … » (imbrication gérée) avec le texte qui les précède."""
    spans, stack = [], []
    for i, ch in enumerate(text):
        if ch == "«":
            stack.append(i)
        elif ch == "»" and stack:
            start = stack.pop()
            if not stack:
                spans.append((start, i + 1))
    return spans


def cited_ranges(text):
    """Plages de texte à ignorer : mots cités du texte en vigueur."""
    ranges = []
    for start, end in quoted_spans(text):
        before = text[max(0, start - 60):start]
        if CITED_INTRO.search(before):
            ranges.append((start, end))
    return ranges


def in_ranges(pos, ranges):
    return any(a <= pos < b for a, b in ranges)


def lint(text):
    findings = []
    ignore = cited_ranges(text)
    amendement = bool(AMENDEMENT.search(text))
    lines = text.split("\n")
    offset = 0
    for lineno, line in enumerate(lines, 1):
        stripped = line.strip()
        is_visa = bool(re.match(r"^[«\s]*Vu\b", stripped))
        is_heading = bool(stripped) and stripped == stripped.upper() and len(stripped) > 3
        for rid, pattern, message, fiche, grav, opts in RULES:
            if opts.get("skip_visas") and is_visa:
                continue
            if opts.get("skip_notice") and NOTICE.match(stripped):
                continue
            flags = re.M if pattern.startswith("^") else 0
            if rid not in CASE_SENSITIVE:
                flags |= re.I
            for m in re.finditer(pattern, line, flags):
                pos = offset + m.start()
                if in_ranges(pos, ignore):
                    continue
                word = m.group(0)
                g = grav
                if opts.get("futur") and (PUBLICATION.search(line[max(0, m.start() - 5):m.end() + 40])
                                          or word.lower() in FUTUR_EXCLUS):
                    continue
                if opts.get("sigle"):
                    if is_heading or word in NOT_SIGLES or ROMAN.match(word) or word == "JORF":
                        continue
                    if re.match(r"^[LRDA]\d|^LO$", word):
                        continue
                if rid == "alinea-chiffre" and amendement and CHAPEAU.search(line):
                    continue
                if rid == "duree-chiffres" and int(m.group("n")) >= 100:
                    continue
                if opts.get("notamment"):
                    sentence = re.split(r"(?<=[.;])\s", line[m.start():])[0]
                    before = re.split(r"[.;]\s", line[:m.start()])[-1]
                    if SANCTION.search(before + " " + sentence):
                        g = "B"
                        message = ("« notamment » dans une obligation, une interdiction ou une sanction : "
                                   "énoncer les cas de façon limitative")
                    else:
                        message = "« notamment » : vérifier qu'il n'élargit pas une obligation ou une sanction"
                if rid == "deux-points-colles" and re.search(r"\d:\d|https?:", line[max(0, m.start() - 6):m.end() + 2]):
                    continue
                excerpt = line[max(0, m.start() - 30):m.end() + 30].strip()
                findings.append({
                    "ligne": lineno, "regle": rid, "trouve": word, "extrait": excerpt,
                    "message": message, "fiche": fiche, "gravite": g,
                })
        offset += len(line) + 1
    return findings


# --- Contrôles de structure (sur l'ensemble du texte, pas ligne à ligne) ---

ARTICLE_HEAD = re.compile(r"^\s*Article (?P<num>\d+)(?P<er>er)?(?: (?P<suffixe>bis|ter|quater))?\s*$|^\s*Article unique\s*$")
OPENING = re.compile(r"^\s*(?:Décrète|Arrête|Arrêtent|Ordonne)\s*:\s*$", re.M)
EXECUTION = re.compile(r"\b(?:est|sont) chargée?s?,?(?: chacun en ce qui (?:le|la) concerne,)? de l'exécution\b")
EN_VIGUEUR = re.compile(r"\b(?:entre|entrent|entrera|entreront) en vigueur\b|\bprend(?:nent|ra|ront)? effet\b")
OPERATION = re.compile(
    r"\b(?:est|sont) (?:ainsi (?:modifiée?s?|rédigée?s?)|abrogée?s?|remplacée?s?|complétée?s?|supprimée?s?|"
    r"insérée?s?|rétablie?s?|ajoutée?s?)\b|\b(?:il est|sont) (?:inséré|ajouté|rétabli)")
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre",
        "novembre", "décembre"]
DATE = re.compile(r"\b(\d{1,2})(?:er)? (" + "|".join(MOIS) + r") (\d{4})\b")

# Rangs des visas (fiche 3.1.5) : textes par rang hiérarchique, puis consultations, Conseil
# constitutionnel, Conseil d'Etat, conseil des ministres, urgence.
VISA_RANGS = [
    (0, "Constitution", r"^vu la constitution|^vu la charte de l'environnement"),
    (1, "convention internationale", r"^vu (?:la |le |l')?(?:convention|traité|accord|protocole|pacte)\b"),
    (2, "règlement de l'Union", r"^vu le règlement (?:\((?:ue|ce|cee|euratom)\)|n° ?\d+/\d+|délégué|d'exécution)"),
    (3, "directive de l'Union", r"^vu la directive\b"),
    (4, "loi organique", r"^vu (?:la )?loi organique|^vu l'ordonnance n° ?\S+ du .{0,30}portant loi organique"),
    (5, "code", r"^vu (?:le )?code\b|^vu le livre des procédures fiscales"),
    (6, "loi ou ordonnance", r"^vu (?:la )?loi\b|^vu l'ordonnance\b"),
    (7, "décret", r"^vu (?:le )?décret\b"),
    (8, "arrêté", r"^vu (?:l')?arrêté\b"),
    (9, "consultation", r"^vu (?:l'avis|les avis|la délibération|les délibérations|la lettre|les lettres|"
                        r"les observations|la saisine|la notification|les notifications|la communication)"),
    (10, "décision du Conseil constitutionnel", r"^vu la décision\b"),
    (11, "Conseil d'Etat", r"^le conseil d'etat\b.*entendu|^après avis du conseil d'etat|^sur l'avis conforme du conseil d'etat"),
    (12, "conseil des ministres", r"^le conseil des ministres entendu"),
    (13, "urgence", r"^vu l'urgence"),
]
CHRONO = {4, 6, 7, 8}  # catégories classées par ordre chronologique


def visa_rang(line):
    low = line.strip().lower()
    for rang, nom, pat in VISA_RANGS:
        if re.match(pat, low):
            return rang, nom
    return None, None


def date_key(line):
    m = DATE.search(line)
    return (int(m.group(3)), MOIS.index(m.group(2)) + 1, int(m.group(1))) if m else None


def finding(lineno, regle, trouve, extrait, message, fiche, gravite):
    return {"ligne": lineno, "regle": regle, "trouve": trouve, "extrait": extrait.strip()[:90],
            "message": message, "fiche": fiche, "gravite": gravite}


def split_articles(lines, quoted):
    """Articles du projet (têtes hors guillemets) : liste de (index de ligne, libellé, num, lignes)."""
    heads = []
    offset = 0
    for i, line in enumerate(lines):
        m = ARTICLE_HEAD.match(line)
        if m and not in_ranges(offset, quoted) and not line.lstrip().startswith("«"):
            heads.append((i, line.strip(), m))
        offset += len(line) + 1
    articles = []
    for k, (i, label, m) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        for j in range(i + 1, end):  # le bloc de signature clôt le dernier article
            if re.match(r"^\s*Fait (?:le|à)\b", lines[j]):
                end = j
                break
        articles.append({"index": i, "label": label, "m": m, "body": lines[i + 1:end]})
    return articles


def unquoted(text):
    """Le texte sans les passages entre guillemets français (dispositions insérées, mots cités)."""
    out, depth = [], 0
    for ch in text:
        if ch == "«":
            depth += 1
        elif ch == "»" and depth:
            depth -= 1
        elif depth == 0:
            out.append(ch)
    return "".join(out)


def structure(text):
    """Contrôles de structure : numérotation, article d'exécution, entrée en vigueur, ordre des visas,
    « susvisé », article modifié deux fois. Mêmes champs que lint()."""
    findings = []
    lines = text.split("\n")
    quoted = [span for span in quoted_spans(text)]
    articles = split_articles(lines, quoted)
    reglementaire = bool(OPENING.search(text))
    loi = not reglementaire and bool(re.search(
        r"\b(?:Projet|Proposition) de loi\b|\bLa présente loi\b|^\s*Loi(?: organique)? n°", text, re.M))

    # 1. Numérotation des articles du projet
    attendu = 1
    for a in articles:
        m = a["m"]
        if m.group("num") is None:  # Article unique
            if len(articles) > 1:
                findings.append(finding(a["index"] + 1, "structure-article-unique", a["label"], a["label"],
                                        "« Article unique » alors que le texte compte plusieurs articles",
                                        "annexe typo", "R"))
            continue
        if m.group("suffixe"):
            continue
        n = int(m.group("num"))
        if n != attendu:
            findings.append(finding(a["index"] + 1, "structure-numerotation", a["label"], a["label"],
                                    f"numérotation discontinue : article {attendu} attendu", "3.2.2", "R"))
        attendu = n + 1

    # 2. Article d'exécution et entrée en vigueur
    def matches(article, pattern):
        return bool(pattern.search(re.sub(r"\s+", " ", unquoted("\n".join(article["body"])))))

    exec_idx = [k for k, a in enumerate(articles) if matches(a, EXECUTION)]
    vig_idx = [k for k, a in enumerate(articles) if matches(a, EN_VIGUEUR)]
    if reglementaire and articles:
        if not exec_idx:
            findings.append(finding(articles[-1]["index"] + 1, "structure-execution-absente", "", articles[-1]["label"],
                                    "décret ou arrêté sans article d'exécution (« … est chargé de l'exécution "
                                    "du présent décret, qui sera publié au Journal officiel… »)", "3.9.1", "R"))
        elif exec_idx[-1] != len(articles) - 1:
            a = articles[exec_idx[-1]]
            findings.append(finding(a["index"] + 1, "structure-execution-place", a["label"], a["label"],
                                    "l'article d'exécution doit être le dernier article", "3.2.1", "R"))
        if exec_idx:
            for k in vig_idx:
                if k > exec_idx[-1]:
                    a = articles[k]
                    findings.append(finding(a["index"] + 1, "structure-vigueur-apres-execution", a["label"],
                                            a["label"], "l'entrée en vigueur se place avant l'article d'exécution",
                                            "3.8.1", "R"))
    if loi:
        for k in exec_idx:
            a = articles[k]
            findings.append(finding(a["index"] + 1, "structure-loi-execution", a["label"], a["label"],
                                    "une loi n'a pas d'article d'exécution (la formule est ajoutée à la "
                                    "promulgation)", "3.1.5", "R"))

    # 3. Visas : présence dans une loi, ordre
    visa_lines = []
    if reglementaire:
        end = OPENING.search(text).start()
        start = 0
        for i, line in enumerate(lines):
            if start >= end:
                break
            rang, nom = visa_rang(line)
            if rang is not None:
                visa_lines.append((i, line, rang, nom))
            start += len(line) + 1
    elif loi:
        for i, line in enumerate(lines):
            if re.match(r"^\s*Vu\b", line):
                findings.append(finding(i + 1, "structure-loi-visas", "Vu", line,
                                        "une loi n'a pas de visas", "3.1.5", "R"))
    prev = None
    for i, line, rang, nom in visa_lines:
        if prev is not None:
            p_rang, p_nom, p_line = prev
            if rang < p_rang:
                findings.append(finding(i + 1, "structure-ordre-visas", nom, line,
                                        f"ordre des visas : un visa de catégorie « {nom} » se place avant "
                                        f"les visas de catégorie « {p_nom} »", "3.1.5", "R"))
                continue
            if rang == p_rang and rang in CHRONO:
                d, pd = date_key(line), date_key(p_line)
                if d and pd and d < pd:
                    findings.append(finding(i + 1, "structure-ordre-visas", nom, line,
                                            "ordre des visas : dans une même catégorie, ordre chronologique",
                                            "3.1.5", "S"))
            if rang == p_rang == 5:
                nom_code = lambda l: re.sub(r"^vu (?:le )?code (?:de la |de l'|du |des |de |d')?", "", l.strip().lower())
                a, b = nom_code(p_line), nom_code(line)
                if b < a:
                    findings.append(finding(i + 1, "structure-ordre-visas", nom, line,
                                            "ordre des visas : les codes se citent par ordre alphabétique",
                                            "3.1.5", "S"))
        prev = (rang, nom, line)

    # 4. « susvisé »
    visa_text = "\n".join(l for _, l, _, _ in visa_lines)
    offset = 0
    for i, line in enumerate(lines):
        if re.match(r"^[«\s]*Vu\b", line):
            offset += len(line) + 1
            continue
        for m in re.finditer(r"\bsusvisée?s?\b", line):
            before = line[max(0, m.start() - 90):m.start()]
            designation = re.split(r"\b(?:du|de la|de l'|le|la|l')\s+(?=(?:code|décret|loi|arrêté|ordonnance)\b)",
                                   before)[-1]
            inside = in_ranges(offset + m.start(), quoted)
            if re.match(r"code\b", designation):
                findings.append(finding(i + 1, "structure-susvise-code", "susvisé", line[max(0, m.start() - 40):m.end()],
                                        "un code ne se désigne jamais « susvisé » : intitulé exact, puis « du même code »",
                                        "3.4.1", "B"))
                continue
            if loi:
                findings.append(finding(i + 1, "structure-susvise-loi", "susvisé", line[max(0, m.start() - 40):m.end()],
                                        "une loi n'a pas de visas : intitulé complet à la première mention, puis "
                                        "« mentionné ci-dessus »", "3.4.1", "R"))
                continue
            if inside:
                findings.append(finding(i + 1, "structure-susvise-insere", "susvisé", line[max(0, m.start() - 40):m.end()],
                                        "« susvisé » dans une disposition insérée : seulement si le texte figure dans "
                                        "les visas d'origine du texte modifié ; sinon intitulé complet", "3.4.1", "R"))
                continue
            if not visa_lines:
                continue
            num = re.search(r"n° ?(\d{2,4}-\d+)", designation)
            date = DATE.search(designation)
            if num or date:
                ident = num.group(1) if num else date.group(0)
                if norm(ident) not in norm(visa_text):
                    findings.append(finding(i + 1, "structure-susvise-absent", "susvisé",
                                            line[max(0, m.start() - 40):m.end()],
                                            f"texte désigné « susvisé » ({ident}) absent des visas", "3.4.1", "R"))
            else:
                genre = re.match(r"(décret|loi|arrêté|ordonnance)\b", designation)
                if genre:
                    n = sum(1 for l in visa_text.split("\n") if re.match(rf"^\s*Vu (?:le |la |l')?{genre.group(1)}\b", l, re.I))
                    if n != 1:
                        findings.append(finding(i + 1, "structure-susvise-ambigu", "susvisé",
                                                line[max(0, m.start() - 40):m.end()],
                                                f"« {genre.group(1)} susvisé » : {n} texte(s) de ce type dans les visas ; "
                                                "préciser la date", "3.4.1", "R"))
        offset += len(line) + 1

    # 5. Même article modifié par plusieurs dispositions du projet
    findings.extend(double_modification(articles))
    return findings


TARGET = re.compile(
    r"(?<!après )(?<!avant )(?<!Après )(?<!Avant )(?<!un )(?<!Un )"
    r"\b(?:l'|L')article (?P<art>(?:(?:L|R|D|A|LO)\.?\s?)?\d+(?:er)?(?:-\d+)*(?: (?:bis|ter|quater))?)"
    r"(?P<suite>[^,:;]{0,90})")
DESIGNATION = re.compile(r"^\s*(?:du|de la|de l')\s+(?P<texte>(?:même )?(?:code|décret|loi|arrêté|ordonnance)[^,:;]*?)"
                         r"(?=\s+(?:est|sont|il est|,|:|;|$)|$)")


def text_key(designation, current):
    """Clé du texte modifié : code par son intitulé, autres textes par leur nature."""
    if designation is None:
        return current
    d = designation.strip().lower()
    if d.startswith("même"):
        return current
    code = re.match(r"(code (?:de |du |des |d')?[^,;:]+?)(?:\s+(?:est|sont)\b|$)", d)
    if code:
        return code.group(1).strip()
    genre = re.match(r"(décret|loi|arrêté|ordonnance)", d)
    return genre.group(1) if genre else current


def double_modification(articles):
    findings, seen = [], {}
    current = None
    for a in articles:
        for j, raw in enumerate(a["body"]):
            line = unquoted(raw)
            ctx = re.match(r"^\s*(?:Le|La|L')\s*(code [^,:;]+?|décret[^:;]*?|loi[^:;]*?|arrêté[^:;]*?|ordonnance[^:;]*?)"
                           r" est ainsi modifiée?", line)
            if ctx:
                current = text_key(ctx.group(1), current)
            if not OPERATION.search(line) and not re.search(r"\b(?:Au|À|A|Aux|Dans)\b", line):
                continue
            for m in TARGET.finditer(line):
                des = DESIGNATION.match(m.group("suite"))
                key_text = text_key(des.group("texte") if des else None, current)
                if des and not des.group("texte").lower().startswith("même"):
                    current = key_text
                key = (key_text, m.group("art").replace(" ", "").replace(".", ""))
                if not OPERATION.search(line[m.start():]) and not re.search(r"\b(?:Au|À|A|Aux|Dans)\b", line[:m.start()]):
                    continue
                if key in seen and seen[key][0] != (a["index"], j):
                    first_label = seen[key][1]
                    findings.append(finding(a["index"] + 2 + j, "structure-double-modification", f"article {m.group('art')}",
                                            raw, f"article {m.group('art')} ({key_text or 'texte modifié'}) déjà modifié "
                                            f"par {first_label} : regrouper les modifications d'un même article",
                                            "3.4.1", "B"))
                else:
                    seen.setdefault(key, ((a["index"], j), a["label"]))
    return findings


def markdown_lintable(text):
    """Garde les lignes du projet dans un fichier Markdown, en préservant les numéros de ligne : le contenu
    des blocs ``` s'il y en a ; sinon les lignes citées (« > ») s'il y en a ; sinon tout, sauf titres,
    lignes de tableau et règles horizontales. Les marques d'emphase (« * », « ** ») sont retirées."""
    lines = text.split("\n")
    clean = lambda l: re.sub(r"\*{1,2}(?=\S)|(?<=\S)\*{1,2}", "", l)
    fences = [i for i, l in enumerate(lines) if l.strip().startswith("```")]
    out = []
    if len(fences) >= 2:
        inside = False
        for l in lines:
            if l.strip().startswith("```"):
                inside = not inside
                out.append("")
            else:
                out.append(l if inside else "")
        return "\n".join(out)
    if any(re.match(r"^\s*>", l) for l in lines):
        return "\n".join(clean(re.sub(r"^\s*>\s?", "", l)) if re.match(r"^\s*>", l) else "" for l in lines)
    for l in lines:
        s = l.strip()
        if s.startswith("#") or s.startswith("|") or re.match(r"^[-*_]{3,}$", s):
            out.append("")
        else:
            out.append(clean(l))
    return "\n".join(out)


REF_PATTERNS = [
    # articles de code (L., R., D., A., LO), seuls ou en plage
    r"\b(?:L\.|R\.|D\.|A\.|LO) ?\d+(?:-\d+)*(?: (?:et|à) (?:L\.|R\.|D\.|A\.|LO) ?\d+(?:-\d+)*)?",
    # textes numérotés
    r"\b(?:loi organique|loi|décret|ordonnance|arrêté) n° ?\d{2,4}-\d+(?: du \d{1,2}(?:er)? \w+ \d{4})?",
    # actes de l'Union européenne
    r"\b(?:règlement|directive|décision) (?:\((?:UE|CE|CEE|Euratom)\) )?(?:n° ?)?\d{2,4}/\d+(?:/(?:UE|CE|CEE))?",
    # décisions de justice datées
    r"\b(?:CE|Cons\. const\.|Conseil constitutionnel|Cass\.[^,]{0,15}|CAA [A-Z]\w+)[ ,]+(?:Ass\.|Sect\.)?[^.;|\n]{0,25}?\d{1,2}(?:er)? (?:janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre) \d{4}",
]


def references(text):
    refs = []
    seen = set()
    for lineno, line in enumerate(text.split("\n"), 1):
        for pat in REF_PATTERNS:
            for m in re.finditer(pat, line):
                r = re.sub(r"\s+", " ", m.group(0)).strip(" ,")
                key = norm(r).replace(" ", "")
                if key not in seen:
                    seen.add(key)
                    refs.append({"reference": r, "ligne": lineno})
    return refs


def norm(s):
    return re.sub(r"\s+", " ", s.replace("\u00a0", " ").replace("\u202f", " ")).lower()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fichier", help="texte à contrôler (« - » pour l'entrée standard)")
    ap.add_argument("--json", action="store_true", help="sortie JSON")
    ap.add_argument("--refs", action="store_true", help="lister les références juridiques citées (articles de "
                    "code, textes numérotés, actes de l'Union, décisions datées)")
    ap.add_argument("--source", help="avec --refs : demande ou texte fourni par l'utilisateur, pour repérer "
                                     "les références ajoutées")
    ap.add_argument("--markdown", action="store_true", help="ne contrôler que le projet dans un fichier Markdown "
                    "(blocs ``` ou texte hors titres et tableaux) ; implicite pour un fichier .md")
    ap.add_argument("--sans-structure", action="store_true", help="ne pas lancer les contrôles de structure")
    args = ap.parse_args()
    text = sys.stdin.read() if args.fichier == "-" else open(args.fichier, encoding="utf-8").read()
    if args.markdown or args.fichier.lower().endswith(".md"):
        text = markdown_lintable(text)

    if args.refs:
        refs = references(text)
        src = norm(open(args.source, encoding="utf-8").read()).replace(" ", "") if args.source else None
        for r in refs:
            r["origine"] = ("fournie" if src is not None and norm(r["reference"]).replace(" ", "") in src
                            else "ajoutée" if src is not None else "?")
        if args.json:
            print(json.dumps(refs, ensure_ascii=False, indent=2))
        else:
            print("| Référence | Ligne | Origine |\n|---|---|---|")
            for r in refs:
                print(f"| {r['reference']} | {r['ligne']} | {r['origine']} |")
            if src is not None:
                n = sum(r["origine"] == "ajoutée" for r in refs)
                print(f"\n{n} référence(s) absente(s) de la demande : à vérifier ou à marquer « à vérifier ».")
        return

    findings = lint(text)
    if not args.sans_structure:
        findings += structure(text)
    if args.json:
        print(json.dumps(findings, ensure_ascii=False, indent=2))
        return
    if not findings:
        print("Aucun constat mécanique ni structurel. La relecture de fond reste à faire (grille-de-relecture.md).")
        return
    order = {"B": 0, "R": 1, "S": 2}
    print("| Ligne | Trouvé | Extrait | Constat | Fiche | Gravité |\n|---|---|---|---|---|---|")
    for f in sorted(findings, key=lambda f: (order[f["gravite"]], f["ligne"])):
        ext = f["extrait"].replace("|", "\\|")
        print(f"| {f['ligne']} | {f['trouve']} | {ext} | {f['message']} | {f['fiche']} | {f['gravite']} |")
    counts = {g: sum(f["gravite"] == g for f in findings) for g in "BRS"}
    print(f"\n{len(findings)} constat(s) : {counts['B']} B, {counts['R']} R, {counts['S']} S. "
          "Candidats à relire dans leur contexte, pas des verdicts.")


if __name__ == "__main__":
    main()

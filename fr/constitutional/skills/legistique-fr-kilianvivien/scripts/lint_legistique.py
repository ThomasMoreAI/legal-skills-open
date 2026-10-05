#!/usr/bin/env python3
"""Repère les fautes mécaniques d'un texte normatif français (langue, présentation, formules proscrites).

Usage :
    python3 lint_legistique.py projet.txt            # tableau Markdown des constats
    python3 lint_legistique.py projet.txt --json     # constats en JSON
    python3 lint_legistique.py projet.txt --refs [--source demande.txt]
                                                     # liste des références juridiques citées ;
                                                     # avec --source, marque celles absentes de la demande
    cat projet.txt | python3 lint_legistique.py -    # lecture sur l'entrée standard

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

    # --- Temps, mode, renfort ---
    ("doit", r"\b(?:doit|doivent)\b", "« doit » : le présent de l'indicatif suffit à obliger", "3.3.1", "R", {}),
    ("futur", r"\b(?:sera|seront|devra|devront|pourra|pourront|fera|feront|aura|auront|ira|iront)\b"
              r"|\b\w{3,}(?:eront|iront)\b|\b\w{3,}(?<!cam)(?<!op)(?<!chim)era\b",
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
ROMAN = re.compile(r"^(?=[MDCLXVI]+$)M{0,3}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})$")
SANCTION = re.compile(
    r"\b(?:sanction\w*|amende\w*|puni\w*|pénal\w*|interdi\w*|infraction\w*|contravention\w*|délit\w*|"
    r"retir\w*|retrait|suspen\w*|reversement|rembours\w*|manquement\w*|méconn\w*)\b", re.I)
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
    lines = text.split("\n")
    offset = 0
    for lineno, line in enumerate(lines, 1):
        stripped = line.strip()
        is_visa = bool(re.match(r"^[«\s]*Vu\b", stripped))
        is_heading = bool(stripped) and stripped == stripped.upper() and len(stripped) > 3
        for rid, pattern, message, fiche, grav, opts in RULES:
            if opts.get("skip_visas") and is_visa:
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
                if opts.get("futur") and PUBLICATION.search(line[max(0, m.start() - 5):m.end() + 40]):
                    continue
                if opts.get("sigle"):
                    if is_heading or word in NOT_SIGLES or ROMAN.match(word) or word == "JORF":
                        continue
                    if re.match(r"^[LRDA]\d|^LO$", word):
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
    args = ap.parse_args()
    text = sys.stdin.read() if args.fichier == "-" else open(args.fichier, encoding="utf-8").read()

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
    if args.json:
        print(json.dumps(findings, ensure_ascii=False, indent=2))
        return
    if not findings:
        print("Aucun constat mécanique. La relecture de fond reste à faire (grille-de-relecture.md).")
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

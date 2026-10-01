---
name: freelance-invoice-generator-khalilbenaz
title: Invoice Generator
description: Aide à créer des factures conformes, gérer les mentions légales obligatoires et suivre les relances de paiement. Se déclenche avec "facture", "facturation", "mentions légales", "relance paiement", "devis freelance". Also triggers on "create an invoice", "invoice a client", "payment reminder".
author: khalilbenaz
author_url: https://github.com/khalilbenaz/claude-skills-collection/tree/main/skills/freelance-invoice-generator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: commercial
language: fr
---

# Invoice Generator

## Étape 1 — Identifier le statut juridique

Le régime détermine les mentions obligatoires et la TVA applicable.

| Statut | TVA | Mention spécifique |
|---|---|---|
| Micro-entrepreneur (France) | Non collectée si CA < seuils | "TVA non applicable, art. 293 B du CGI" |
| EURL / SASU soumise à IS | Oui (20 % standard) | Numéro de TVA intracommunautaire obligatoire |
| Auto-entrepreneur Maroc | Non (exonéré 36 mois) | RC + ICE + Patente + IF |
| Freelance UE → client UE | Autoliquidation | "Autoliquidation — art. 283-2 du CGI" |

## Étape 2 — Mentions légales obligatoires

**Bloc prestataire**
- Nom / raison sociale, adresse complète
- SIRET (France) ou RC + ICE (Maroc)
- Code APE/NAF (France)
- Numéro de TVA intracommunautaire si assujetti

**Bloc client**
- Raison sociale et adresse de facturation
- Numéro de TVA intracommunautaire si applicable (B2B UE)

**Bloc facturation**
- Numéro de facture : format chronologique sans rupture (`2026-001`, `2026-002`, ...)
- Date d'émission
- Date d'échéance (ex : "30 jours nets" → date explicite)
- Désignation précise de chaque prestation
- Quantité + prix unitaire HT + taux TVA + montant TVA + total TTC

**Mentions légales pied de facture (France)**
```
Pénalités de retard : taux directeur BCE + 10 points (soit X % à la date d'émission).
Indemnité forfaitaire de recouvrement : 40 EUR (art. L441-10 C. Com.).
Escompte pour paiement anticipé : aucun.
```

## Étape 3 — Modèle de facture (Markdown → PDF)

```markdown
# FACTURE N° 2026-042

**Émetteur**               **Client**
Khalil BENAZZOUZ           ACME SAS
12 rue des Devs, Paris     5 av. du Client, Lyon
SIRET : 123 456 789 00010  TVA : FR 12 345678901
TVA : FR 00 123456789

---
| Description                  | Qté | PU HT   | TVA  | Total HT |
|------------------------------|-----|---------|------|----------|
| Développement API REST       |  10 | 650,00  | 20 % | 6 500,00 |
| Audit sécurité OWASP         |   1 | 800,00  | 20 % |   800,00 |

**Total HT** : 7 300,00 €
**TVA 20 %** : 1 460,00 €
**Total TTC** : 8 760,00 €

Date d'échéance : 2026-07-24 (30 jours nets)

IBAN : FR76 1234 5678 9012 3456 7890 123  |  BIC : BNPAFRPP
```

Convertir en PDF avec un outil CLI :
```bash
# Option 1 — pandoc + LaTeX
pandoc facture-2026-042.md -o facture-2026-042.pdf --pdf-engine=xelatex

# Option 2 — wkhtmltopdf (HTML → PDF)
wkhtmltopdf --page-size A4 facture-2026-042.html facture-2026-042.pdf
```

## Étape 4 — Numérotation et séquence

- Format recommandé : `AAAA-NNN` (ex. `2026-001`)
- La séquence doit être continue et sans trou sur l'exercice comptable
- En cas d'erreur sur une facture émise : **émettre un avoir** (prefix `AV-`) puis réémettre
- Tenir un registre CSV minimal :

```csv
numero,date_emission,client,ht,tva,ttc,echeance,statut
2026-001,2026-01-15,ACME SAS,7300,1460,8760,2026-02-14,PAYE
2026-002,2026-02-01,Beta Corp,2000,400,2400,2026-03-03,EN_ATTENTE
```

## Étape 5 — Processus de relance

```
J+0   Envoi facture PDF par email (accusé de lecture si possible)
J+7   après échéance → Relance amiable (email courtois, PJ facture)
J+15  → Relance ferme (email + appel téléphonique)
J+30  → Mise en demeure par LRAR (mentionner pénalités de retard)
J+45  → Injonction de payer (tribunal compétent) ou cabinet de recouvrement
```

Template relance amiable :
```
Objet : Rappel facture n° 2026-042 — échéance dépassée

Bonjour,

Sauf erreur de ma part, la facture n° 2026-042 d'un montant de 8 760,00 €
est arrivée à échéance le 2026-07-24. Pourriez-vous me confirmer la date
de règlement prévue ?

Cordialement,
```

## Étape 6 — Tableau de bord trésorerie

Script Python minimal pour résumer le registre CSV :
```python
import csv, datetime
from collections import defaultdict

with open("factures.csv") as f:
    rows = list(csv.DictReader(f))

total_en_attente = sum(float(r["ttc"]) for r in rows if r["statut"] == "EN_ATTENTE")
en_retard = [
    r for r in rows
    if r["statut"] == "EN_ATTENTE"
    and datetime.date.fromisoformat(r["echeance"]) < datetime.date.today()
]
print(f"En attente : {total_en_attente:.2f} €")
print(f"En retard  : {len(en_retard)} facture(s)")
for r in en_retard:
    print(f"  → {r['numero']} / {r['client']} / {r['ttc']} € / éch. {r['echeance']}")
```

## Garde-fous et pièges fréquents

| Piège | Conséquence | Correctif |
|---|---|---|
| Modifier une facture émise | Fraude fiscale | Avoir + nouvelle facture |
| Numérotation avec saut ou doublon | Rejet comptable, redressement | Audit du registre avant émission |
| Oublier la mention d'exonération TVA | Facture non conforme | Ajouter "TVA non applicable, art. 293 B CGI" |
| Date d'échéance absente | Délai légal 30 j s'applique par défaut | Toujours dater l'échéance explicitement |
| Envoi sans accusé de réception | Preuve difficile en cas de litige | Email avec tracking ou LRAR pour gros montants |
| TVA intracommunautaire client absent | Autoliquidation refusée | Vérifier le numéro sur vies.europa.eu |

## Bonnes pratiques 2026

- **Facturation électronique (France)** : Depuis 2026, les grandes entreprises sont obligées de recevoir des factures au format Factur-X (PDF/A-3 + XML embarqué). Les PME/TPE doivent s'y conformer progressivement — privilégier Factur-X dès maintenant.
- **Archivage numérique probant** : Utiliser un coffre-fort numérique certifié (NF Z42-020) ou signature électronique qualifiée eIDAS pour valeur légale sans impression.
- **Clause de réserve de propriété** : Pour les livraisons de livrables (code, maquettes), stipuler que la propriété est transférée à réception du paiement intégral.
- **Acompte** : Facturer 30–50 % à la commande pour les missions > 3 000 € ; émettre une facture d'acompte distincte.
- **Harmonisation des conditions de paiement** : Standardiser à 30 jours nets fin de mois ou 45 jours date de facture (plafond légal France B2B).


## Communication Rules — MANDATORY

- Ultra-concise. No filler, no preamble, no pleasantries.
- Never say "happy to help", "sure!", "great question", "let me", or similar.
- Tool first, talk second. Act before explaining.
- Result first. Lead with outcome, not process.
- Stop when done. No summary, no recap, no trailing commentary.
- No politeness wrappers. Direct and blunt.
- Minimum words. If one word works, do not use ten.
- No unsolicited explanations.
- No emoji unless asked.

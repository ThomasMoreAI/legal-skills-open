# Templates en allemand — Paperasse Luxembourg

Versions allemandes des courriers et actes les plus courants pour résidents et entreprises germanophones du Luxembourg (vallée de la Sûre, Norden, frontaliers DE/BE).

## Fichiers disponibles

| Fichier | Équivalent français | Usage |
|---|---|---|
| `einberufung-gesellschafterversammlung.md` | `templates/syndic/convocation-ag.md` | Convocation à l'assemblée générale d'une SARL |
| `einberufung-hauptversammlung.md` | — | Convocation à l'AG ordinaire d'une SA |
| `einberufung-eigentuemerversammlung.md` | `templates/convocation-ag-copropriete.md` | Convocation AG copropriété |
| `mahnung.md` | `templates/syndic/mise-en-demeure.md` | Lettre de relance/mise en demeure |
| `rechnung-luxemburg.md` | `templates/comptable/facture.md` | Facture conforme TVA luxembourgeoise |
| `kuendigung-mietvertrag.md` | — | Résiliation de bail |

## Rendu via CLI

```bash
paperasse de einberufung-gesellschafterversammlung examples/de/sarl-ag.json
paperasse de mahnung examples/de/mahnung-input.json --out=mahnung-001.md
paperasse de rechnung-luxemburg examples/de/rechnung.json
```

## Substitutions

Les templates utilisent une syntaxe `{{ variable }}` simple. Le moteur de rendu (`lib/templates-de/`) :
- Remplace `{{ x }}` par la valeur de `x` dans le JSON d'entrée
- Supporte les sous-objets : `{{ gesellschaft.name }}`
- Boucles : `{% for ligne in positionen %} ... {% endfor %}`
- Conditions : `{% if mwst_befreit %} ... {% endif %}`

## Mentions légales et conformité

Les références juridiques pointent vers la **loi luxembourgeoise applicable**, même quand le texte est en allemand :
- Loi modifiée du 10 août 1915 (sociétés commerciales)
- Loi modifiée du 19 décembre 2002 (comptabilité)
- Loi du 21 septembre 2006 (bail à usage d'habitation)
- Code de commerce et loi TVA luxembourgeoise (art. 61 et suivants pour mentions facture)

## À valider

Pour usage en contexte officiel (notarial, judiciaire), faire valider la traduction par un traducteur juré assermenté au Luxembourg (liste sur https://justice.public.lu/).

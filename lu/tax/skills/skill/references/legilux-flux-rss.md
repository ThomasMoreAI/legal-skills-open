# Veille légale — Flux RSS du Journal Officiel luxembourgeois

Le **Service Central de Législation (SCL)** publie en temps réel les modifications du Journal Officiel via 4 flux RSS publics. Tout skill doit consulter ces flux pour détecter une évolution légale avant de produire un livrable.

## Endpoints officiels

| Flux | URL | Contenu |
|---|---|---|
| Mémorial A — Législation | `https://data.legilux.public.lu/api/rss-leg.xml` | Lois, règlements grand-ducaux, arrêtés ministériels, traités |
| Mémorial B — Administration | `https://data.legilux.public.lu/api/rss-adm.xml` | Actes administratifs, nominations, avis |
| Mémorials A + B (tout) | `https://data.legilux.public.lu/api/rss.xml` | Agrégat complet |
| Projets de loi | `https://data.legilux.public.lu/api/rss-draft.xml` | Textes en cours d'examen à la Chambre |

> ⚠️ Les anciennes URLs `legilux.public.lu/api/rss-*.xml` (sans le sous-domaine `data.`) renvoient **404 depuis la migration**. Utiliser exclusivement `data.legilux.public.lu`.

## Format de réponse

RSS 2.0 standard. Chaque `<item>` contient :
- `<title>` — intitulé complet du texte (ex. *« Loi du 5 mai 2026 concernant des mesures destinées à assurer un niveau élevé de cybersécurité... »*)
- `<description>` — généralement identique au titre
- `<pubDate>` — date de publication au JO (`YYYY-MM-DD`)
- `<link>` — URL ELI vers la fiche : `data.legilux.public.lu/eli/etat/leg/{type}/{YYYY}/{MM}/{DD}/{slug}/jo`

## Mots-clés de filtrage par skill

| Skill | Termes à surveiller |
|---|---|
| `comptable` | TVA, PCN, plan comptable, FAIA, eCDF, Peppol, IRC, ICC, impôt sur la fortune, amortissement, exercice, liasse |
| `controleur-fiscal` | contrôle fiscal, ACD, AED, enregistrement, domaines, sanction, amende, fraude, abus de droit, pénalité |
| `commissaire-aux-comptes` | audit, réviseur, CSSF, ISA, contrôle légal, certification, CNCC |
| `fiscaliste` | impôt sur le revenu, IRPP, RTS, frontalier, retraite, pension, abattement, classe d'impôt, barème, déduction |
| `notaire` | notaire, notarial, acte authentique, enregistrement, hypothèque, succession, donation, mariage, PACS, Bëllegen, émolument |
| `syndic` | copropriété, syndic, immeuble, bâtiment, logement, location, bail, fonds de prévoyance, loi du 16 mai 1975 |

## Consommation côté app

L'app Paperasse Lux expose ces flux via la route serveur :

```
GET /api/legilux/feed?type=leg|adm|all|draft
```

Cache mémoire : 1 heure. Réponse JSON normalisée :

```json
{
  "type": "leg",
  "source": "https://data.legilux.public.lu/api/rss-leg.xml",
  "fetchedAt": "2026-05-09T15:00:00.000Z",
  "cached": false,
  "count": 25,
  "items": [
    { "title": "...", "description": "...", "pubDate": "2026-05-08", "link": "https://..." }
  ]
}
```

Page interactive : **Veille JO** (sidebar de l'app).

## Bonnes pratiques

1. Toujours indiquer dans un livrable la **date de la dernière consultation** du flux.
2. Si une publication récente (< 30 jours) modifie un texte cité dans une référence du skill, **mettre à jour la référence** avant production.
3. Pour les projets de loi (`draft`), signaler en commentaire « texte non encore publié au Mémorial — applicabilité conditionnelle ».
4. Ne jamais cacher plus d'1 h côté app : le SCL publie en continu.

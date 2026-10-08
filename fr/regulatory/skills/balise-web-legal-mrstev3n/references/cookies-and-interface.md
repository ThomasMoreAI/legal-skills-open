# Cookies, traceurs et interface de choix

## Qualification

Inclure cookies, stockage web, identifiants mobiles, pixels, liens de suivi, empreinte du terminal, SDK, contenus embarqués et autres lectures ou écritures. Vérifier la définition propre à la juridiction; ne pas transposer automatiquement l'exemption européenne des traceurs strictement nécessaires.

## Audit du comportement

Tester au minimum :

1. arrivée sans choix antérieur;
2. refus global;
3. acceptation globale;
4. choix par finalité ou acteur;
5. retrait ou modification;
6. expiration du choix;
7. utilisateur connecté sur plusieurs appareils si la fonction existe;
8. activation d'un contenu tiers;
9. navigation mobile et application.

Capturer les requêtes et stockages avant et après chaque état. Un texte de bandeau ne prouve pas qu'un script est bloqué.

## Contenu du tableau

Pour chaque traceur : nom, technologie, déposant, domaine, finalité, catégorie, déclencheur, données ou identifiant, destinataire, durée observée et durée déclarée, statut de consentement, transfert et source.

## Interface

Lorsque le consentement est exigé : fournir une information claire avant activation, un choix réel, une granularité adaptée, une preuve du choix et un retrait accessible. Vérifier localement si accepter et refuser doivent être aussi simples, si une exemption existe et combien de temps le choix peut être conservé.

## Routage UE/France

Si le routeur confirme le droit UE ou français, lire [international-overlays.md](international-overlays.md), vérifier les sources officielles qui y sont indiquées et actualiser les règles en ligne. Ne pas réutiliser une durée ou une catégorie issue d'un autre régime comme norme universelle.

## Livrables

- inventaire technique observé;
- classification juridique par juridiction;
- texte de premier niveau du bandeau;
- texte du centre de préférences;
- politique détaillée;
- écarts entre déclarations et comportement;
- tickets techniques pour blocage, preuve, retrait et synchronisation.

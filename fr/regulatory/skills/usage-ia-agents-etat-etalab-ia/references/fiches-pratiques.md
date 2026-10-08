# Fiches pratiques

## Les 5 règles d'or du bon prompt

> Un bon prompt = **contexte + document de référence (si nécessaire) + consigne précise + format attendu**.
>
> Rédiger un bon prompt, c'est comme briefer une personne en stage : donner le contexte, préciser l'attendu, être explicite sur le format.

1. **Soyez précis sans être trop long.**
   - Trop vague : « Écris un mail professionnel. »
   - Juste : « Rédige un courriel de 5 lignes pour reporter une réunion du 15 au 17 janvier. Ton formel. »
2. **Donnez du contexte.** Qui êtes-vous (rôle, service) ? Pour qui (destinataire) ? Quel objectif ? Fournissez un document de référence si nécessaire (pièce jointe ou copier-coller du texte source). Astuce : donnez un rôle à l'IA (« Tu es un agent d'une préfecture. Tu dois expliquer… »).
3. **Précisez le format attendu** : longueur, structure, ton. Ex. « Résume ce rapport en 5 points clés, sous forme de liste. » ; « Crée un tableau comparatif en 3 colonnes. » ; « Propose 3 versions : courte, moyenne, longue. »
4. **Demandez des révisions** : « Raccourcis de moitié. » ; « Ton plus formel. » ; « Sois plus exhaustif sur le point 3. » ; « Reformule en évitant le jargon. »
5. **Demandez à l'IA de vous poser des questions** quand le besoin est complexe : « …Pose-moi des questions pour être sûr de bien comprendre mon besoin avant de commencer. »

**Et n'oubliez jamais de :** vérifier le résultat avec un œil critique, adapter au contexte spécifique, relire avant de diffuser.

## Cas d'usage par famille de métier

Le guide propose des scénarios concrets (profil, besoin, contexte, outil, prompt, résultat, points de vigilance). L'outil cité dans les exemples est l'**Assistant IA interministériel** ou un outil ministériel autorisé.

- **RH et gestion du personnel** : reformuler une circulaire RH pour les managers ; créer une FAQ à partir d'un règlement interne.
- **Gestion de projets et réunions** : transcrire et résumer une réunion avec Visio ; transformer des notes éparses en ordre du jour structuré ; enregistrer et transcrire une réunion en présentiel.
- **Communication interne et externe** : créer des publications pour les réseaux sociaux internes (Tchap, intranet).
- **Développement et numérique** : documenter du code ou une procédure technique ; générer des tests/cas d'usage à partir de spécifications ; traduire de la documentation technique.
- **Juridique et réglementation** : résumer un texte de loi ou une jurisprudence ; vulgariser un document juridique pour les agents.
- **Finances et gestion budgétaire** : résumer un rapport d'audit ou de contrôle ; préparer une note de synthèse sur l'exécution budgétaire.
- **Management et encadrement** : préparer une réponse à une question parlementaire à partir de notes existantes ; rédiger un retour constructif pour un entretien annuel.

### Exemples de prompts orientés développement / numérique

**Documenter une procédure technique** (pour des agents non développeurs) :
```
Je suis chef de projet numérique dans une administration.
Voici une procédure technique et des extraits de scripts de déploiement et de maintenance
d'un outil interne : [copier-coller de la procédure et des extraits de code].
À partir de ces éléments, rédige une documentation opérationnelle à destination d'agents
non développeurs.
Structure attendue :
- Objectif de la procédure
- Prérequis techniques
- Étapes détaillées pas à pas
- Points d'attention et erreurs fréquentes
Ton clair, pédagogique et professionnel. Ne modifie pas le fonctionnement technique existant.
```
*Vigilance :* vérifier la conformité technique de chaque étape ; s'assurer que commandes, chemins et paramètres sont strictement identiques à la production ; garder la documentation alignée avec la version réelle du code ; mentionner en en-tête qu'une première version a été générée avec l'assistance d'une IA puis validée techniquement.

**Générer des cas de tests à partir de spécifications :**
```
Je suis responsable produit numérique dans une administration.
Voici les spécifications fonctionnelles d'un service numérique : [copier-coller].
À partir de ces éléments, génère une liste de cas de tests fonctionnels et de scénarios d'usage.
Pour chaque cas de test, indique : le contexte ; l'action réalisée par l'utilisateur ; le résultat attendu.
Regroupe les cas par fonctionnalité, et n'invente pas de fonctionnalités absentes des spécifications.
```
*Vigilance :* vérifier que tous les cas correspondent à des fonctionnalités existantes ; compléter par des cas limites ; faire une revue métier avant validation ; indiquer aux destinataires que la première liste a été générée avec l'aide d'une IA.

> Une astuce récurrente des prompts du guide : terminer par **« N'invente aucune règle / ne complète pas avec des informations absentes du document »** pour limiter les hallucinations sur les contenus administratifs.

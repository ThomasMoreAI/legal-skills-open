# Choisir l'outil selon les données

Tous les outils d'IA n'offrent pas les mêmes garanties de protection des données. Trois grandes catégories, du plus sécurisé au moins sécurisé.

## 1. Les outils des administrations publiques (à privilégier)

Développés ou déployés par l'État, premier choix pour les usages professionnels. Privilégier ceux **explicitement approuvés par votre administration de rattachement**.

**Outils interministériels :**
- **Assistant IA interministériel** — `assistant.numerique.gouv.fr` : assistant conversationnel sécurisé (rédaction, résumé, reformulation).
- **Assistant Transcripts** — `transcripts.numerique.gouv.fr` : enregistrement et transcription de réunions en présentiel.
- **Visio** — `visio.numerique.gouv.fr` : transcription automatique et résumé de visioconférences.

**Outils ministériels :** certains ministères disposent d'outils propres (ex. GenIAl), dans une trajectoire de convergence avec les offres mutualisées de l'État.

## 2. Les outils commerciaux payants mis à disposition par l'administration (avec précautions)

Licences achetées par l'administration (versions payantes de ChatGPT, Claude, outils spécialisés d'aide juridique ou de création graphique…), avec garanties contractuelles renforcées : engagements de non-réutilisation des données, meilleur niveau de sécurité, support dédié.

- **Même avec une licence payante**, vérifier auprès de la **DSI** ou du responsable les types de données autorisés.
- Vérifier la **maîtrise juridique et opérationnelle de l'hébergement** : la localisation des serveurs ne suffit pas. Examiner le pays d'établissement du fournisseur, sa structure capitalistique, les entités opérant le service et les sous-traitants. Un service hébergé dans l'UE peut rester soumis à une législation étrangère (ex. **Cloud Act** américain). Pour les usages sensibles, privilégier des solutions à fortes garanties, idéalement **qualifiées SecNumCloud par l'ANSSI**.

## 3. Les outils commerciaux gratuits (usage très limité voire interdit)

Accessibles librement sur Internet, parfois sans compte : versions gratuites de ChatGPT, Claude, Gemini, NotebookLM, Vibe (ex Le Chat de Mistral AI)…

**Conditions strictes :**
- vérifier que le ministère **autorise** leur accès et leur usage professionnel (parfois bloqués sur le réseau) ;
- ne les utiliser que pour des **données publiables** (pas de données personnelles ni sensibles) ;
- éviter l'usage professionnel via un **compte personnel**.

**Le réflexe :** « Est-ce que je pourrais publier ces informations sur un site Internet accessible à tous ? » Si non, ne pas utiliser un outil grand public. En cas d'hésitation, utiliser uniquement un outil de l'administration.

- **Usages possibles :** résumer un texte de loi ou un rapport déjà public, reformuler un document accessible en ligne, générer une image d'illustration, créer un questionnaire de formation à partir de contenus publics, travailler sur du code « ouvert » ou non sensible.
- **Usages interdits :** analyser un dossier d'usager, résumer un compte-rendu de réunion interne, traiter des données RH ou médicales, traiter des informations couvertes par le secret professionnel.

## Catégories de données et niveau d'exigence

- **Données personnelles (RGPD)** : protéger, n'utiliser que les données strictement nécessaires. Usage régulier → vérifier l'inscription au **registre des traitements** avec le DPD.
- **Informations professionnelles non publiques** : notes en cours d'arbitrage, projets confidentiels, secret des délibérations gouvernementales, données stratégiques ou économiques sensibles. **Ne pas confier à un outil commercial grand public.**
- **Données classifiées ou à mention de protection** : Diffusion Restreinte, Secret, Très Secret, toute donnée relevant de l'**IGI 1300** → **seuls les outils explicitement homologués** peuvent être employés.

## Le cadre juridique qui vous protège

- **RGPD** : protéger les données personnelles, minimiser les données utilisées.
- **Règlement européen sur l'IA (RIA)** : encadre les usages à haut risque (annexe III) — ex. tri/évaluation de candidatures, prise de décision automatisée affectant les droits des personnes (RH, justice, santé, maintien de l'ordre). En l'absence de cadre formellement validé, **s'abstenir**.
- **Secret professionnel** : interdiction de divulguer des informations couvertes par le secret.

> Règle pratique : pas besoin de maîtriser tous ces textes. **En cas de doute sur une donnée, utiliser l'outil de l'administration ou s'abstenir.**

## En cas de doute, trois réflexes

1. Utiliser l'outil de l'administration plutôt qu'un outil commercial.
2. Ne pas confondre **pseudonymisation** et **anonymisation** : remplacer un nom (« Madame X ») laisse des données personnelles au sens du RGPD — seule une anonymisation irréversible (impossible à reconstituer, y compris par recoupement) rend les données publiables, et elle est rarement atteignable pour un dossier complet.
3. Demander conseil : hiérarchie, DSI, DPD, référent cybersécurité.

## Exemples pratiques

| Situation | Nature des données | Outil |
|---|---|---|
| Résumer un rapport parlementaire public | Document public, pas de données personnelles | Outil commercial (si autorisé) **ou** outil de l'administration |
| Préparer un compte-rendu de réunion interne (noms, positions) | Noms + informations internes | **Uniquement** l'outil de l'administration (ou un outil commercial autorisé par la DSI pour ce type de données) |
| Comparer des candidatures pour un recrutement | Usage à haut risque (RIA, annexe III) | **S'abstenir** sans cadre formellement validé |

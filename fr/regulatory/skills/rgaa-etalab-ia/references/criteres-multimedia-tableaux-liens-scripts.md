# RGAA — Thèmes 4 à 7 : Multimédia, Tableaux, Liens, Scripts

## Thème 4 — Multimédia (13 critères)

### Critères principaux

| Critère | Exigence |
|---------|----------|
| 4.1 | Média pré-enregistré : transcription textuelle ou audiodescription |
| 4.2 | Transcription/audiodescription pertinente |
| 4.3 | Sous-titres synchronisés pour média synchronisé pré-enregistré |
| 4.4 | Sous-titres pertinents |
| 4.5 | Audiodescription synchronisée si nécessaire |
| 4.6 | Audiodescription pertinente |
| 4.7 | Média clairement identifiable (texte adjacent) |
| 4.8 | Média non temporel : alternative accessible |
| 4.9 | Alternative pertinente |
| 4.10 | Son automatique contrôlable (≤3s ou stop/volume) |
| 4.11 | Contrôle clavier : lecture, pause, son, sous-titres, audiodescription |
| 4.12 | Média non temporel contrôlable au clavier |
| 4.13 | Compatible technologies d'assistance (API accessibilité) |

**Test 4.1/4.3 :** Vérifier que chaque `<video>` pré-enregistré a une `<track kind="captions">` et/ou un lien vers une transcription textuelle complète.
**Non-conformité type :** `<video>` sans `<track>` ; transcription absente ou accessible uniquement après téléchargement.
**Priorité 4.1/4.3 :** 🔴 Bloquant

**Test 4.10 :** Vérifier qu'aucun son ne se déclenche automatiquement au chargement de la page, ou que sa durée est ≤ 3 secondes, ou qu'un mécanisme de contrôle est accessible dès le début de la page.
**Non-conformité type :** Vidéo ou audio en autoplay sans contrôle de volume/pause accessible.
**Priorité 4.10 :** 🟠 Majeur

**Test 4.11 :** Vérifier que tous les contrôles du lecteur (lecture, pause, volume, sous-titres) sont accessibles au clavier.
**Non-conformité type :** Lecteur vidéo custom dont les boutons ne sont pas focusables au clavier.
**Priorité 4.11 :** 🔴 Bloquant

```tsx
<figure>
  <video controls>
    <source src="/video.mp4" type="video/mp4" />
    <track kind="captions" src="/sous-titres.vtt" srcLang="fr" label="Français" default />
    <track kind="descriptions" src="/audiodesc.vtt" srcLang="fr" label="Audiodescription" />
  </video>
  <figcaption>Présentation du service — <a href="/transcription">Transcription textuelle</a></figcaption>
</figure>
```

**Points clés :**
- `<track kind="captions">` (pas `subtitles`) pour les sous-titres d'accessibilité
- Son automatique interdit sauf ≤ 3 secondes ou contrôle immédiat
- Tout contrôle (lecture, pause, volume) doit être accessible au clavier

---

## Thème 5 — Tableaux (8 critères)

### 5.1–5.2 Tableau complexe : résumé présent et pertinent

Un tableau complexe (en-têtes multi-niveaux) nécessite un résumé expliquant sa structure.

**Test :** Identifier les tableaux avec en-têtes sur plusieurs lignes/colonnes. Vérifier qu'un résumé de structure est fourni via `aria-describedby` ou un passage de texte adjacent.
**Non-conformité type :** Tableau avec en-têtes croisés sans aucun résumé de lecture.
**Priorité :** 🟠 Majeur

---

### 5.3 Tableau de mise en forme : contenu linéarisé compréhensible

Tableau de mise en forme : `role="presentation"` obligatoire, pas de `<th>`, `<caption>`, `<thead>`, `<tfoot>`.

**Test :** Identifier les `<table>` utilisés pour la mise en page (non pour des données). Vérifier qu'ils ont `role="presentation"` et ne contiennent pas de `<th>`, `<caption>`, `<thead>` ou `<tfoot>`.
**Non-conformité type :** `<table>` de mise en page sans `role="presentation"` ; utilisation de `<th>` dans un tableau de présentation.
**Priorité :** 🟠 Majeur

---

### 5.4–5.5 Titre de tableau correctement associé et pertinent

Via `<caption>`, `aria-label`, `aria-labelledby` ou `title`.

**Test :** Vérifier que chaque tableau de données a un titre accessible via `<caption>` ou `aria-label`. Vérifier que ce titre décrit clairement le contenu du tableau.
**Non-conformité type :** Tableau de données sans `<caption>` ni `aria-label` ; `<caption>Tableau 1</caption>` non descriptif.
**Priorité :** 🟡 Mineur

---

### 5.6–5.7 En-têtes correctement déclarés et associés

- En-têtes de colonnes : `<th scope="col">`
- En-têtes de lignes : `<th scope="row">`
- Tableaux complexes : `<th id="...">` + `<td headers="...">`

**Test :** Vérifier que chaque cellule d'en-tête utilise `<th>` avec `scope="col"` ou `scope="row"`. Pour les tableaux complexes, vérifier les attributs `id`/`headers`.
**Non-conformité type :** En-têtes de colonnes en `<td>` stylés en gras au lieu de `<th scope="col">` ; absence de `scope` sur les `<th>`.
**Priorité :** 🟠 Majeur

---

### 5.8 Tableau de mise en forme sans éléments de données

**Test :** Vérifier l'absence de `<th>`, `<caption>`, `<thead>`, `<tfoot>`, `summary` dans les tableaux de présentation.
**Non-conformité type :** `<table>` de mise en page contenant des `<th>`.
**Priorité :** 🟠 Majeur

```tsx
<table>
  <caption>Liste des agents par département</caption>
  <thead>
    <tr>
      <th scope="col">Nom</th>
      <th scope="col">Département</th>
      <th scope="col">Rôle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Dupont</td>
      <td>Paris</td>
      <td>Admin</td>
    </tr>
  </tbody>
</table>
```

---

## Thème 6 — Liens (2 critères)

### 6.1 Chaque lien est-il explicite ?

L'intitulé du lien (seul ou avec son contexte) doit permettre de comprendre sa fonction et sa destination.

**Contexte valide :** phrase englobante, paragraphe, élément de liste, titre précédent, cellule d'en-tête de tableau.

**Test :** Identifier tous les `<a href>`. Lire leur texte seul (hors contexte). Si ambigu ("cliquez ici", "en savoir plus", "lire la suite"), vérifier que le contexte immédiat (phrase, `aria-label`, `aria-labelledby`) lève l'ambiguïté.
**Non-conformité type :** `<a href="/rapport">En savoir plus</a>` sans contexte permettant de comprendre de quel rapport il s'agit.
**Priorité :** 🟠 Majeur

```tsx
// ❌ Mauvais
<a href="/rapport">Cliquez ici</a>
<a href="/rapport">En savoir plus</a>

// ✅ Bon
<a href="/rapport">Consulter le rapport annuel 2024 (PDF, 2 Mo)</a>

// ✅ Acceptable avec contexte
<p>Le rapport annuel est disponible. <a href="/rapport">Télécharger le rapport (PDF, 2 Mo)</a></p>

// ✅ Lien image : alt pertinent
<a href="/accueil"><img src="/logo.png" alt="Retour à l'accueil" /></a>
```

---

### 6.2 Chaque lien a-t-il un intitulé ?

Tout lien (`<a href>` ou `role="link"`) doit avoir un contenu accessible (texte, alt d'image, aria-label).

**Test :** Vérifier que chaque `<a>` a du texte visible, un `alt` si l'enfant est une image, ou un `aria-label`. Repérer les liens contenant uniquement une icône SVG sans texte ni aria.
**Non-conformité type :** `<a href="/page"><svg>...</svg></a>` sans `aria-label` ni texte.
**Priorité :** 🔴 Bloquant

```tsx
// ❌ Lien vide
<a href="/page"></a>

// ✅ Lien avec aria-label
<a href="/page" aria-label="Accéder à la page détails">
  <svg aria-hidden="true">...</svg>
</a>
```

---

## Thème 7 — Scripts (5 critères)

### 7.1 Script compatible avec les technologies d'assistance

Tout composant généré par script doit exposer : nom, rôle, valeur, paramétrage et changements d'états via l'API d'accessibilité.

**Test :** Vérifier que les composants interactifs custom (accordéon, onglets, menu déroulant, carrousel) ont les rôles ARIA appropriés (`role`, `aria-expanded`, `aria-selected`, `aria-controls`...).
**Non-conformité type :** Accordéon custom sans `aria-expanded` sur le bouton ; menu déroulant sans `aria-haspopup`.
**Priorité :** 🟠 Majeur

```tsx
<button
  aria-expanded={isOpen}
  aria-controls="panel-1"
  onClick={() => setIsOpen(!isOpen)}
>
  Détails
</button>
<div id="panel-1" role="region" hidden={!isOpen}>
  Contenu du panneau
</div>
```

---

### 7.2 Alternative pertinente au script

Si JavaScript est désactivé, une alternative équivalente doit être disponible (via `<noscript>` ou rendu serveur).

**Test :** Désactiver JavaScript et vérifier que le contenu principal reste accessible.
**Non-conformité type :** Page entière en JavaScript sans rendu serveur ni `<noscript>`.
**Priorité :** 🟠 Majeur

---

### 7.3 Script contrôlable au clavier

Tout élément interactif créé par script doit être focusable et activable au clavier.

**Test :** Parcourir la page au clavier (Tab, Entrée, Espace, flèches). Vérifier que tous les éléments interactifs sont atteignables et utilisables sans souris. Repérer les `<div onClick>` ou `<span onClick>` non focusables.
**Non-conformité type :** `<div onClick={handleClick}>Action</div>` non focusable ; composant React custom non opérable au clavier.
**Priorité :** 🔴 Bloquant

```tsx
// ❌ Mauvais : div cliquable non accessible
<div onClick={handleClick}>Action</div>

// ✅ Bon : bouton natif
<button onClick={handleClick}>Action</button>

// ✅ Si div nécessaire : rôle + tabindex + clavier
<div
  role="button"
  tabIndex={0}
  onClick={handleClick}
  onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') handleClick(); }}
>
  Action
</div>
```

---

### 7.4 Changement de contexte : utilisateur averti ou en contrôle

Ne pas déclencher de changement de contexte (navigation, ouverture fenêtre, changement de focus) sans action explicite de l'utilisateur (clic sur bouton/lien).

**Test :** Vérifier qu'aucun changement de page, ouverture de modale ou rechargement ne se déclenche au simple focus ou survol d'un élément (sans activation).
**Non-conformité type :** Soumission automatique d'un formulaire au changement de valeur d'un `<select>` sans bouton de validation.
**Priorité :** 🟠 Majeur

---

### 7.5 Messages de statut restitués

| Type de message | Attribut ARIA |
|---|---|
| Succès, résultat d'action | `role="status"` ou `aria-live="polite" aria-atomic="true"` |
| Erreur, avertissement | `role="alert"` ou `aria-live="assertive" aria-atomic="true"` |
| Progression | `role="progressbar"` ou `role="log"` ou `role="status"` |

**Test :** Identifier les messages dynamiques (confirmation d'envoi, erreurs, résultats de recherche chargés dynamiquement). Vérifier qu'ils ont `role="status"` ou `role="alert"` pour être annoncés par les lecteurs d'écran.
**Non-conformité type :** Message de confirmation "Formulaire envoyé" apparaissant visuellement mais sans `role="status"` ni `aria-live`.
**Priorité :** 🟠 Majeur

```tsx
// Message de succès
<div role="status">Formulaire envoyé avec succès.</div>

// Message d'erreur
<div role="alert">Erreur : le champ email est invalide.</div>

// Barre de progression
<div role="progressbar" aria-valuenow={75} aria-valuemin={0} aria-valuemax={100}>
  75%
</div>
```

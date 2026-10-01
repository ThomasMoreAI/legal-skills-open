# RGAA — Thèmes 1 à 3 : Images, Cadres, Couleurs

## Thème 1 — Images (9 critères)

### 1.1 Chaque image porteuse d'information a-t-elle une alternative textuelle ?

Balises concernées : `<img>`, `role="img"`, `<area>`, `<input type="image">`, `<svg>`, `<object type="image/...">`, `<embed type="image/...">`, `<canvas>`.

- `<img>` / `role="img"` : alternative via `alt`, `aria-label`, `aria-labelledby` ou `title`
- `<svg>` : doit avoir `role="img"` + alternative textuelle
- `<input type="image">` : attribut `alt`

**Test :** Vérifier que chaque `<img>` informatif possède un attribut `alt` non vide et présent. Vérifier que chaque `<svg>` informatif a `role="img"` + `aria-label` ou un `<title>` enfant. Vérifier que `<input type="image">` a un `alt`.
**Non-conformité type :** `<img src="chart.png">` sans attribut `alt` ; `<svg>` sans `role="img"` ni `aria-label`.
**Priorité :** 🔴 Bloquant

```tsx
// Image porteuse d'information
<img src="/chart.png" alt="Évolution du chiffre d'affaires 2024 : +15%" />

// SVG porteuse d'information
<svg role="img" aria-label="Logo du service">...</svg>

// Bouton image
<input type="image" src="/search.png" alt="Rechercher" />
```

---

### 1.2 Chaque image de décoration est-elle correctement ignorée ?

- `<img>` : `alt=""` (vide, pas absent)
- `<svg>` : `aria-hidden="true"` + pas de `role="img"`
- Ou `role="presentation"` sur l'image

**Test :** Vérifier que chaque `<img>` décoratif a `alt=""` (attribut présent mais vide). Vérifier que les `<svg>` décoratifs ont `aria-hidden="true"`.
**Non-conformité type :** `<img src="decoration.png">` sans attribut `alt` (attribut absent) ; `<svg>` décoratif sans `aria-hidden`.
**Priorité :** 🔴 Bloquant

```tsx
// Image décorative
<img src="/decoration.png" alt="" />

// SVG décorative
<svg aria-hidden="true" focusable="false">...</svg>

// Icône décorative dans un bouton avec texte
<button>
  <svg aria-hidden="true" focusable="false">...</svg>
  Rechercher
</button>
```

---

### 1.3 L'alternative textuelle est-elle pertinente ?

L'alternative doit être courte, concise (≤80 caractères recommandé) et décrire la fonction ou l'information de l'image, pas son apparence.

**Test :** Lire les valeurs `alt` et vérifier qu'elles transmettent l'information utile (pas "image", "photo", le nom du fichier, ni une redite du texte adjacent).
**Non-conformité type :** `alt="image"`, `alt="logo.png"`, `alt="Photo"`, ou `alt` reprenant mot pour mot le texte adjacent.
**Priorité :** 🟠 Majeur

---

### 1.4 CAPTCHA : l'alternative identifie-t-elle la nature et la fonction ?

Alternative type : "Code de sécurité anti-spam" (pas la réponse au CAPTCHA).

**Test :** Vérifier que l'image CAPTCHA a un `alt` décrivant ce qu'elle est ("Code de vérification visuel") sans en révéler la réponse.
**Non-conformité type :** CAPTCHA sans `alt`, ou `alt` vide.
**Priorité :** 🔴 Bloquant

---

### 1.5 CAPTCHA : une solution d'accès alternatif existe-t-elle ?

Au moins une alternative d'un autre type (audio si visuel, etc.).

**Test :** Vérifier qu'un CAPTCHA visuel propose un CAPTCHA audio ou une autre méthode accessible.
**Non-conformité type :** CAPTCHA visuel unique sans alternative.
**Priorité :** 🔴 Bloquant

---

### 1.6 Image porteuse d'information : description détaillée si nécessaire ?

Pour les images complexes (graphiques, schémas, cartes), fournir une description détaillée via :
- `aria-describedby` référençant un passage de texte
- Lien/bouton adjacent vers la description
- Description adjacente visible

**Test :** Identifier les images complexes (graphiques, tableaux en image, infographies). Vérifier qu'elles ont une description détaillée accessible via `aria-describedby`, un lien adjacent ou un texte visible.
**Non-conformité type :** Graphique complexe avec seulement `alt="Graphique d'évolution"` sans description des données.
**Priorité :** 🟠 Majeur

---

### 1.7 La description détaillée est-elle pertinente ?

La description détaillée doit contenir toute l'information véhiculée par l'image.

**Test :** Lire la description détaillée et vérifier qu'elle retranscrit toutes les données/informations de l'image (valeurs, tendances, légendes...).
**Non-conformité type :** Description qui mentionne le titre du graphique mais pas les valeurs.
**Priorité :** 🟠 Majeur

---

### 1.8 Les images texte sont-elles remplacées par du texte stylé ?

Préférer du texte CSS quand c'est possible. Exception : logos, marques.

**Test :** Repérer les `<img>` contenant du texte (bannières, titres en image). Vérifier qu'elles ne peuvent pas être reproduites en CSS/HTML.
**Non-conformité type :** Titre de section rendu comme image PNG au lieu d'un `<h2>` stylé.
**Priorité :** 🟡 Mineur

---

### 1.9 Chaque légende d'image est-elle correctement reliée ?

Utiliser `<figure>` + `<figcaption>`.

**Test :** Vérifier que les images accompagnées d'une légende sont dans un `<figure>` avec un `<figcaption>` enfant.
**Non-conformité type :** `<img>` suivi d'un `<p>` comme légende sans structure `<figure>`.
**Priorité :** 🟡 Mineur

```tsx
<figure>
  <img src="/photo.jpg" alt="Vue du bâtiment" />
  <figcaption>Le nouveau siège inauguré en 2024</figcaption>
</figure>
```

---

## Thème 2 — Cadres (2 critères)

### 2.1 Chaque cadre a-t-il un titre ?

Chaque `<iframe>` doit avoir un attribut `title`.

**Test :** Vérifier que chaque `<iframe>` dans le code a un attribut `title` présent et non vide.
**Non-conformité type :** `<iframe src="/map">` sans attribut `title`.
**Priorité :** 🔴 Bloquant

---

### 2.2 Le titre de cadre est-il pertinent ?

Le titre doit décrire le contenu du cadre.

**Test :** Lire les valeurs `title` des `<iframe>` et vérifier qu'elles décrivent le contenu (pas "iframe", "frame", "cadre").
**Non-conformité type :** `title="iframe1"` ou `title="Cadre"`.
**Priorité :** 🟠 Majeur

```tsx
<iframe src="/map" title="Carte interactive de localisation des agences" />
```

---

## Thème 3 — Couleurs (3 critères)

### 3.1 L'information n'est pas donnée uniquement par la couleur

Toute information véhiculée par la couleur doit aussi être accessible par un autre moyen (texte, icône, motif, épaisseur de bordure...).

**Test :** Identifier les éléments dont l'état ou l'information est signalé uniquement par une couleur (rouge = erreur, vert = succès, champ obligatoire en rouge...). Vérifier qu'un autre indicateur visuel est présent.
**Non-conformité type :** Erreur de formulaire signalée uniquement par un fond rouge, sans icône ni texte explicatif.
**Priorité :** 🟠 Majeur

```tsx
// ❌ Statut uniquement par couleur
<span style={{ color: "red" }}>Erreur</span>

// ✅ Couleur + texte + icône
<span style={{ color: "red" }}>
  <svg aria-hidden="true">...</svg> Erreur : champ obligatoire
</span>
```

---

### 3.2 Contraste texte/arrière-plan suffisant

| Type de texte | Ratio minimum |
|---|---|
| Texte < 24px (ou < 18.5px gras) | **4.5:1** |
| Texte ≥ 24px (ou ≥ 18.5px gras) | **3:1** |

**Test :** Identifier les couleurs de texte et d'arrière-plan dans le CSS. Calculer le ratio de contraste (outil : WebAIM Contrast Checker). Vérifier les seuils selon la taille et le graissage. Les textes sur images ou dégradés nécessitent une vérification visuelle.
**Non-conformité type :** Texte gris clair `#999` sur fond blanc `#fff` (ratio ≈ 2.8:1, insuffisant pour texte normal).
**Priorité :** 🟠 Majeur

---

### 3.3 Contraste des composants d'interface et éléments graphiques

Ratio minimum **3:1** entre :
- Les couleurs d'un composant d'interface et son arrière-plan
- Les couleurs contiguës d'un élément graphique porteur d'information

**Test :** Vérifier le contraste des bordures de champs de formulaire, boutons, icônes informatives, et éléments graphiques par rapport à leur arrière-plan.
**Non-conformité type :** Bordure de champ de formulaire `#ccc` sur fond blanc `#fff` (ratio ≈ 1.6:1, insuffisant).
**Priorité :** 🟠 Majeur

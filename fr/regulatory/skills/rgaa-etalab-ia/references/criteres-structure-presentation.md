# RGAA — Thèmes 8 à 10 : Éléments obligatoires, Structure, Présentation

## Thème 8 — Éléments obligatoires (10 critères)

### 8.1 Doctype présent et valide

**Test :** Vérifier que `<!DOCTYPE html>` est présent en première ligne du document HTML, avant la balise `<html>`.
**Non-conformité type :** DOCTYPE absent ou malformé (`<!DOCTYPE HTML PUBLIC ...>` en lieu et place de `<!DOCTYPE html>`).
**Priorité :** 🟠 Majeur

```html
<!DOCTYPE html>
```

---

### 8.2 Code source valide

- Balises correctement imbriquées et fermées
- Attributs `id` uniques dans la page
- Pas d'attributs dupliqués sur un même élément
- Valeurs d'attributs entre guillemets

**Test :** Passer le code dans le validateur W3C ou chercher les `id` dupliqués dans le code (`document.querySelectorAll('[id]')` en console). Vérifier l'imbrication des balises.
**Non-conformité type :** Deux éléments avec le même `id` dans la page ; balises non fermées.
**Priorité :** 🟠 Majeur

---

### 8.3–8.4 Langue par défaut présente et pertinente

**Test :** Vérifier la présence de l'attribut `lang` sur la balise `<html>` et que sa valeur est un code de langue valide (ISO 639-1 : `fr`, `en`, `de`...).
**Non-conformité type :** `<html>` sans `lang` ; `lang="français"` au lieu de `lang="fr"`.
**Priorité :** 🔴 Bloquant

```html
<html lang="fr">
```

---

### 8.5–8.6 Titre de page présent et pertinent

**Test :** Vérifier la présence d'une balise `<title>` non vide. Vérifier que son contenu identifie clairement la page et inclut le nom du site (format recommandé : "Nom de la page - Nom du site").
**Non-conformité type :** `<title>` absent ; `<title>Index</title>` ou `<title>Page</title>` non descriptif ; même `<title>` sur toutes les pages.
**Priorité :** 🔴 Bloquant

```html
<title>Nom de la page - Nom du site</title>
```

---

### 8.7–8.8 Changements de langue indiqués et pertinents

**Test :** Identifier les passages de texte dans une langue différente de la langue par défaut. Vérifier qu'ils ont un attribut `lang` avec la bonne valeur.
**Non-conformité type :** Citation ou terme en anglais sans `lang="en"` ; `lang` avec une valeur incorrecte.
**Priorité :** 🟡 Mineur

```tsx
<p>Le service est disponible en <span lang="en">open source</span>.</p>
```

**Exceptions :** noms propres, termes techniques sans traduction courante.

---

### 8.9 Balises non utilisées uniquement à des fins de présentation

**Test :** Vérifier que les balises sémantiques (`<h1>`–`<h6>`, `<blockquote>`, `<ul>`, `<strong>`, `<em>`...) ne sont utilisées que pour leur sens, pas pour leur rendu visuel.
**Non-conformité type :** `<h3>` utilisé pour augmenter la taille d'un texte sans signification de titre ; `<blockquote>` pour indenter visuellement.
**Priorité :** 🟠 Majeur

---

### 8.10 Sens de lecture signalé

**Test :** Vérifier que les passages de texte en langue à écriture de droite à gauche (arabe, hébreu...) ont `dir="rtl"`.
**Non-conformité type :** Texte arabe affiché sans `dir="rtl"` entraînant un affichage incorrect.
**Priorité :** 🟡 Mineur

```tsx
<p lang="ar" dir="rtl">نص بالعربية</p>
```

---

## Thème 9 — Structuration de l'information (4 critères)

### 9.1 Hiérarchie des titres pertinente

- Utiliser `<h1>` à `<h6>` dans l'ordre hiérarchique
- Un seul `<h1>` par page (bonne pratique)
- Pas de saut de niveau (h1 → h3 sans h2)
- Le contenu de chaque titre doit être pertinent

**Test :** Extraire tous les titres (`<h1>`–`<h6>`) et reconstituer la hiérarchie. Vérifier l'absence de sauts de niveaux et la cohérence logique de l'arborescence.
**Non-conformité type :** `<h1>` suivi directement d'un `<h3>` ; plusieurs `<h1>` ; `<h2>` utilisé pour le style sans signification de section.
**Priorité :** 🟠 Majeur

```tsx
<h1>Titre principal de la page</h1>
  <h2>Section</h2>
    <h3>Sous-section</h3>
  <h2>Autre section</h2>
```

---

### 9.2 Structure du document cohérente

**Test :** Vérifier la présence des landmarks HTML5 : `<header>` unique en tête, `<nav>` pour les navigations, `<main>` unique et visible, `<footer>` en pied. Vérifier que `<main>` n'est pas utilisé plusieurs fois ou caché.
**Non-conformité type :** Absence de `<main>` ; plusieurs `<main>` visibles ; `<nav>` utilisé pour tout groupe de liens.
**Priorité :** 🟠 Majeur

```tsx
<header>  {/* Zone d'en-tête — role="banner" implicite */}
<nav>     {/* Navigation principale et secondaire */}
<main>    {/* Contenu principal — unique et visible */}
<footer>  {/* Pied de page — role="contentinfo" implicite */}
```

---

### 9.3 Listes correctement structurées

**Test :** Identifier les listes visuelles (puces, numérotées, de définitions). Vérifier qu'elles utilisent `<ul>`, `<ol>` ou `<dl>` selon le type, et que les enfants directs sont des `<li>` ou `<dt>`/`<dd>`.
**Non-conformité type :** Liste de liens en navigation codée avec des `<div>` au lieu de `<ul><li>` ; liste ordonnée codée en `<ul>`.
**Priorité :** 🟡 Mineur

---

### 9.4 Citations correctement indiquées

**Test :** Identifier les citations dans le contenu. Vérifier que les citations courtes utilisent `<q>` et les blocs de citation `<blockquote>`.
**Non-conformité type :** Citation longue dans un `<p>` stylé en italique sans `<blockquote>`.
**Priorité :** 🟡 Mineur

---

## Thème 10 — Présentation de l'information (14 critères)

### 10.1 Présentation contrôlée par CSS

**Test :** Vérifier l'absence de balises de présentation dépréciées (`<center>`, `<font>`, `<big>`, `<blink>`, `<marquee>`) et d'attributs de présentation (`align`, `bgcolor`, `border`, `color`, `valign`...) dans le HTML.
**Non-conformité type :** `<font color="red">texte</font>` ; `<td align="center">`.
**Priorité :** 🟡 Mineur

---

### 10.2–10.3 Contenu présent et compréhensible sans CSS

**Test :** Désactiver les CSS et vérifier que le contenu textuel reste lisible et que l'information n'est pas transmise uniquement via des pseudo-éléments CSS (`::before`/`::after`) ou des `background-image`.
**Non-conformité type :** Icône informative affichée uniquement via `background-image` CSS ; texte généré uniquement via `::before`.
**Priorité :** 🟠 Majeur

---

### 10.4 Texte lisible à 200% de zoom

**Test :** Zoomer à 200% dans le navigateur (Ctrl/Cmd + zoom ou réglages d'accessibilité). Vérifier que le texte reste lisible, que les contenus ne se chevauchent pas et que les fonctionnalités restent utilisables.
**Non-conformité type :** Texte tronqué ou contenu caché à 200% de zoom ; boutons dont le texte déborde du conteneur.
**Priorité :** 🟠 Majeur

---

### 10.5 Couleurs de fond et de texte couplées

**Test :** Vérifier que les règles CSS définissant `color` définissent aussi `background-color` sur le même élément ou son ancêtre, et vice versa.
**Non-conformité type :** `.texte-blanc { color: white; }` sans `background-color` défini, rendant le texte illisible selon le fond de l'utilisateur.
**Priorité :** 🟠 Majeur

---

### 10.6 Liens visibles par rapport au texte

**Test :** Identifier les liens dans du texte courant. Si leur distinction par rapport au texte est uniquement colorimétrique, vérifier : contraste lien/texte ≥ 3:1 ET présence d'un soulignement ou autre indicateur au survol/focus.
**Non-conformité type :** Lien dans un paragraphe différencié uniquement par la couleur bleue sans soulignement.
**Priorité :** 🟠 Majeur

---

### 10.7 Focus visible

**Test :** Parcourir la page au clavier (Tab). Vérifier que chaque élément focusé a un indicateur visuel clairement visible (outline, bordure, surlignage). Vérifier l'absence de `outline: none` sans remplacement.
**Non-conformité type :** `*:focus { outline: none; }` dans le CSS sans focus personnalisé de remplacement.
**Priorité :** 🔴 Bloquant

```css
/* ❌ Ne jamais faire */
*:focus { outline: none; }

/* ✅ Personnaliser le focus visiblement */
:focus-visible {
  outline: 2px solid #000091;
  outline-offset: 2px;
}
```

---

### 10.8 Contenus cachés correctement gérés

**Test :** Vérifier que les contenus masqués visuellement mais destinés aux AT utilisent bien `.sr-only`/`.visually-hidden` (et non `display:none`). Vérifier que les contenus cachés aux AT utilisent `aria-hidden="true"` ou `display:none`.
**Non-conformité type :** Texte alternatif pour icône caché avec `display:none` (inaccessible aux lecteurs d'écran) ; contenu décoratif non marqué `aria-hidden`.
**Priorité :** 🟠 Majeur

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

---

### 10.9–10.10 Information pas uniquement par forme, taille ou position

**Test :** Vérifier que l'information n'est pas transmise uniquement par la position ("le bouton à droite"), la forme ou la taille (élément "plus grand" = important).
**Non-conformité type :** Instructions "Cliquez sur le bouton rond" sans autre identification ; "Remplissez les champs en rouge" sans autre indicateur.
**Priorité :** 🟠 Majeur

---

### 10.11 Reflow : pas de scroll horizontal à 320px / vertical à 256px

**Test :** Réduire la fenêtre à 320px de largeur (ou utiliser les DevTools). Vérifier que le contenu ne nécessite pas de défilement horizontal. Exception : tableaux de données, cartes interactives, interfaces nécessitant deux dimensions.
**Non-conformité type :** Barre de navigation horizontale qui déborde à 320px ; tableau de données forçant le scroll horizontal sans alternative.
**Priorité :** 🟠 Majeur

---

### 10.12 Espacement du texte modifiable

**Test :** Appliquer via les DevTools : `line-height: 1.5em; letter-spacing: 0.12em; word-spacing: 0.16em;` sur `body`. Vérifier que le contenu reste lisible et que rien ne se cache ou se chevauche.
**Non-conformité type :** Conteneur avec hauteur fixe en pixels qui tronque le texte quand l'interligne augmente.
**Priorité :** 🟠 Majeur

---

### 10.13 Contenus additionnels (tooltips) contrôlables

**Test :** Identifier les tooltips et contenus apparaissant au survol ou au focus. Vérifier qu'ils peuvent être masqués sans déplacer le focus (touche Échap), qu'ils persistent lors du survol souris, et qu'ils restent visibles tant que nécessaire.
**Non-conformité type :** Tooltip disparaissant immédiatement quand la souris le survole ; tooltip ne pouvant pas être fermé par Échap.
**Priorité :** 🟠 Majeur

---

### 10.14 Contenus CSS additionnels accessibles au clavier

**Test :** Pour chaque élément révélant du contenu au `:hover`, vérifier que le même contenu est accessible au `:focus` (ou via un mécanisme clavier équivalent).
**Non-conformité type :** Menu déroulant qui s'ouvre au `:hover` CSS mais pas au focus clavier.
**Priorité :** 🔴 Bloquant

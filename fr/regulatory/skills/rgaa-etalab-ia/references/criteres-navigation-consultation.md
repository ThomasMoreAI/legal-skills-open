# RGAA — Thèmes 12–13 : Navigation, Consultation

## Thème 12 — Navigation (11 critères)

### 12.1 Deux systèmes de navigation minimum

Chaque ensemble de pages doit proposer au moins deux parmi :
- Menu de navigation
- Plan du site
- Moteur de recherche

**Test :** Vérifier la présence d'au moins deux systèmes de navigation distincts accessibles depuis chaque page (menu principal, plan du site, barre de recherche).
**Non-conformité type :** Site sans plan du site ni moteur de recherche, avec uniquement un menu de navigation.
**Priorité :** 🟠 Majeur

---

### 12.2 Menu et barres de navigation à la même place

**Test :** Comparer la position et l'ordre du menu principal sur plusieurs pages du site. Ils doivent être identiques.
**Non-conformité type :** Menu en haut sur la page d'accueil, en latéral sur les pages intérieures ; ordre des items qui change selon les pages.
**Priorité :** 🟠 Majeur

---

### 12.3–12.5 Plan du site et moteur de recherche

- Plan du site pertinent et représentatif de l'architecture
- Liens fonctionnels et cohérents
- Accessibles depuis une fonctionnalité identique sur toutes les pages

**Test :** Vérifier que le lien vers le plan du site (ou la barre de recherche) est présent et accessible depuis toutes les pages. Vérifier que le plan du site liste les pages principales de manière représentative.
**Non-conformité type :** Plan du site incomplet ou avec des liens cassés ; moteur de recherche absent sur certaines pages.
**Priorité :** 🟡 Mineur

---

### 12.6 Zones de regroupement identifiables

Chaque zone principale doit être identifiable via landmark ARIA ou titre.

**Test :** Vérifier que les zones principales (en-tête, navigation, contenu, pied de page, recherche) sont identifiables par les landmarks HTML5 ou les rôles ARIA. Vérifier que plusieurs `<nav>` sont différenciés par `aria-label`.
**Non-conformité type :** Page sans landmark `<main>` ; deux `<nav>` sans `aria-label` pour les distinguer.
**Priorité :** 🟠 Majeur

```tsx
<header role="banner">...</header>
<nav role="navigation" aria-label="Menu principal">...</nav>
<main role="main">...</main>
<footer role="contentinfo">...</footer>
<form role="search" aria-label="Recherche">...</form>
```

**Plusieurs `<nav>` :** différencier avec `aria-label` :
```tsx
<nav aria-label="Menu principal">...</nav>
<nav aria-label="Menu secondaire">...</nav>
<nav aria-label="Fil d'Ariane">...</nav>
```

---

### 12.7 Lien d'évitement vers le contenu principal

**Test :** Vérifier que le premier lien de la page (ou le premier lien visible au focus) est un lien "Aller au contenu principal" pointant vers l'`id` du `<main>`. Tester en appuyant sur Tab dès le chargement de la page.
**Non-conformité type :** Absence totale de lien d'évitement ; lien d'évitement présent mais pointant vers un `id` inexistant.
**Priorité :** 🔴 Bloquant

```tsx
<body>
  <a href="#contenu" className="skip-link">Aller au contenu principal</a>
  <header>...</header>
  <nav>...</nav>
  <main id="contenu">...</main>
</body>
```

```css
.skip-link {
  position: absolute;
  left: -9999px;
}
.skip-link:focus {
  position: static;
}
```

---

### 12.8 Ordre de tabulation cohérent

**Test :** Parcourir la page à la touche Tab et vérifier que l'ordre de focus suit l'ordre logique de lecture (gauche → droite, haut → bas). Vérifier l'absence de `tabindex` avec valeur positive (> 0) qui perturbe l'ordre naturel.
**Non-conformité type :** `tabindex="5"` sur un élément qui capte le focus avant les éléments précédents dans le DOM ; focus sautant d'une zone à l'autre de façon imprévisible.
**Priorité :** 🟠 Majeur

---

### 12.9 Pas de piège au clavier

**Test :** Naviguer dans les composants interactifs (modales, menus, widgets) uniquement au clavier. Vérifier que Tab/Shift+Tab permettent toujours de sortir de chaque composant. Les modales ouvertes doivent piéger le focus à l'intérieur (acceptable) mais permettre la fermeture via Échap.
**Non-conformité type :** Modale ouverte dont le focus s'échappe vers le fond de la page ; widget dans lequel Tab ne permet pas de sortir.
**Priorité :** 🔴 Bloquant

---

### 12.10 Raccourcis clavier mono-touche contrôlables

**Test :** Identifier si des raccourcis clavier à touche unique (lettre, chiffre, ponctuation sans modificateur) sont implémentés. Vérifier qu'ils peuvent être désactivés ou reconfigurés par l'utilisateur.
**Non-conformité type :** Application SPA avec raccourcis `j`/`k` pour naviguer qui interfèrent avec la saisie dans un champ de recherche.
**Priorité :** 🟠 Majeur

---

### 12.11 Contenus additionnels atteignables au clavier

**Test :** Vérifier que les contenus apparaissant au survol ou au focus (tooltips, sous-menus) sont atteignables et consultables au clavier sans disparaître.
**Non-conformité type :** Sous-menu qui s'ouvre au survol mais se ferme dès qu'on essaie de le parcourir au clavier.
**Priorité :** 🟠 Majeur

---

## Thème 13 — Consultation (12 critères)

### 13.1 Limites de temps contrôlables

**Test :** Identifier les sessions avec expiration ou les contenus avec rafraîchissement automatique. Vérifier que l'utilisateur est averti 20 secondes avant l'expiration et peut prolonger ou désactiver la limite de temps.
**Non-conformité type :** Formulaire de démarche en ligne qui expire après 30 minutes sans avertissement préalable.
**Priorité :** 🔴 Bloquant

---

### 13.2 Pas d'ouverture de fenêtre sans action utilisateur

**Test :** Vérifier qu'aucune popup ou nouvelle fenêtre ne s'ouvre automatiquement au chargement de la page. Vérifier que les liens ouvrant une nouvelle fenêtre (`target="_blank"`) l'indiquent clairement dans leur intitulé ou via un texte masqué.
**Non-conformité type :** Popup publicitaire ou d'alerte s'ouvrant au chargement ; lien `target="_blank"` sans indication "nouvelle fenêtre".
**Priorité :** 🟡 Mineur

```tsx
<a href="/doc.pdf" target="_blank" title="Télécharger le rapport (nouvelle fenêtre)">
  Rapport annuel (PDF, 2 Mo)
  <span className="sr-only"> - nouvelle fenêtre</span>
</a>
```

---

### 13.3–13.4 Documents bureautiques accessibles

**Test :** Identifier les fichiers en téléchargement (PDF, DOCX, ODS...). Vérifier qu'ils sont accessibles (PDF balisé avec titre, lang, structure) ou qu'une alternative HTML/texte est proposée.
**Non-conformité type :** PDF scanné sans OCR ni balises d'accessibilité ; DOCX sans structure de titres.
**Priorité :** 🟠 Majeur

---

### 13.5–13.6 Contenus cryptiques avec alternative pertinente

**Test :** Identifier les émoticônes, art ASCII ou syntaxes cryptiques dans le contenu. Vérifier qu'ils ont une alternative textuelle via `title`, `aria-label` ou contexte adjacent.
**Non-conformité type :** Émoticône `:-)` sans alternative ; art ASCII sans description.
**Priorité :** 🟡 Mineur

```tsx
<span title="Content">:-)</span>
// ou
<span role="img" aria-label="Content">:-)</span>
```

---

### 13.7 Pas de flash dangereux

**Test :** Vérifier l'absence d'animations ou de clignotements dépassant 3 fois par seconde sur une zone supérieure à 21 824 pixels.
**Non-conformité type :** Animation de chargement clignotant plus de 3 fois/seconde ; effet stroboscopique dans une vidéo.
**Priorité :** 🔴 Bloquant

---

### 13.8 Contenus en mouvement contrôlables

**Test :** Identifier les animations, carrousels et contenus en défilement automatique. Vérifier que leur durée est ≤ 5 secondes ou qu'un mécanisme pause/stop est accessible. Vérifier le respect de `prefers-reduced-motion`.
**Non-conformité type :** Carrousel défilant automatiquement sans bouton pause ; animation continue sans respect de `prefers-reduced-motion`.
**Priorité :** 🟠 Majeur

```css
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}
```

---

### 13.9 Contenu consultable en portrait et paysage

**Test :** Tester la page en orientation portrait et paysage (DevTools > rotation). Vérifier que le contenu est accessible dans les deux orientations.
**Non-conformité type :** Application bloquée en mode portrait avec message "Veuillez tourner votre appareil" sans justification fonctionnelle.
**Priorité :** 🟠 Majeur

---

### 13.10 Gestes complexes doublés par gestes simples

**Test :** Identifier les fonctionnalités utilisant des gestes multipoint (pinch to zoom, swipe) ou des trajectoires. Vérifier qu'une alternative par tap ou clic simple est disponible.
**Non-conformité type :** Carrousel navigable uniquement par swipe sans boutons précédent/suivant.
**Priorité :** 🟠 Majeur

---

### 13.11 Actions annulables

**Test :** Vérifier que les actions déclenchées par clic/tap le sont au relâchement (`mouseup`/`touchend`), pas à la pression (`mousedown`), ou qu'un mécanisme d'annulation est proposé.
**Non-conformité type :** Bouton de suppression déclenché au `mousedown` sans confirmation possible.
**Priorité :** 🟠 Majeur

---

### 13.12 Fonctionnalités basées sur le mouvement de l'appareil

**Test :** Identifier les fonctionnalités activées par le mouvement (secousse, inclinaison). Vérifier qu'une alternative via interface est disponible et que la détection de mouvement peut être désactivée.
**Non-conformité type :** Fonctionnalité "secouer pour annuler" sans bouton équivalent dans l'interface.
**Priorité :** 🟠 Majeur

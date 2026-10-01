# RGAA — Thème 11 : Formulaires (13 critères)

## 11.1 Chaque champ a une étiquette

Chaque champ de formulaire doit avoir une étiquette associée via (ordre de priorité) :
1. `aria-labelledby` référençant un passage de texte
2. `aria-label`
3. `<label for="id">` associé au champ
4. `title`

**Test :** Vérifier que chaque `<input>`, `<select>`, `<textarea>` a un `<label for>` associé, un `aria-label` ou un `aria-labelledby`. Les placeholders seuls ne constituent pas une étiquette valide.
**Non-conformité type :** `<input type="text" placeholder="Votre nom">` sans `<label>`, ni `aria-label`.
**Priorité :** 🔴 Bloquant

```tsx
// ✅ Label explicite avec for/id
<label htmlFor="email">Email</label>
<input id="email" type="email" />

// ✅ aria-label (si pas de label visible)
<input type="search" aria-label="Rechercher sur le site" />

// ✅ aria-labelledby
<span id="label-tel">Téléphone</span>
<span id="hint-tel">Format : 01 23 45 67 89</span>
<input aria-labelledby="label-tel hint-tel" type="tel" />
```

---

## 11.2 Étiquette pertinente

L'étiquette doit permettre de comprendre la fonction exacte du champ. Si un intitulé visible existe, le nom accessible doit le contenir.

**Test :** Lire les labels et vérifier qu'ils décrivent précisément le champ (pas "Saisir", "Champ 1"). Si un `aria-label` est présent, vérifier qu'il contient le texte visible du label.
**Non-conformité type :** `<label>Saisir :</label>` ; `aria-label="field1"` alors que le label visible dit "Adresse email".
**Priorité :** 🟠 Majeur

---

## 11.3 Étiquettes cohérentes

Les champs de même fonction (ex: "Email" dans formulaire de contact et d'inscription) doivent avoir des étiquettes formulées de manière cohérente.

**Test :** Comparer les étiquettes de champs de même type sur différentes pages ou formulaires du site.
**Non-conformité type :** "Adresse email" sur une page, "Courriel" sur une autre pour le même type de champ.
**Priorité :** 🟡 Mineur

---

## 11.4 Étiquette et champ accolés

- Champs texte/select : étiquette au-dessus ou à gauche
- Checkbox/radio : étiquette en-dessous ou à droite

**Test :** Vérifier visuellement et dans le code la proximité entre chaque label et son champ. Le label et le champ doivent être contigus dans le DOM.
**Non-conformité type :** Label en haut de page référençant un champ en bas de page ; label séparé du champ par un autre élément.
**Priorité :** 🟠 Majeur

---

## 11.5–11.7 Regroupement de champs

Regrouper les champs de même nature avec `<fieldset>` + `<legend>`.

**Test :** Identifier les groupes logiques de champs (cases à cocher, boutons radio, adresse en plusieurs champs). Vérifier qu'ils sont enveloppés dans un `<fieldset>` avec une `<legend>` pertinente, ou un `role="group"` + `aria-label`.
**Non-conformité type :** Groupe de boutons radio sans `<fieldset>` ; groupe de champs d'adresse sans légende de groupe.
**Priorité :** 🟠 Majeur

```tsx
<fieldset>
  <legend>Adresse de livraison</legend>
  <label htmlFor="rue">Rue</label>
  <input id="rue" type="text" />
  <label htmlFor="ville">Ville</label>
  <input id="ville" type="text" />
</fieldset>

// Radio buttons obligatoirement groupés
<fieldset>
  <legend>Civilité</legend>
  <input type="radio" id="mme" name="civilite" value="mme" />
  <label htmlFor="mme">Madame</label>
  <input type="radio" id="m" name="civilite" value="m" />
  <label htmlFor="m">Monsieur</label>
</fieldset>
```

Alternative ARIA : `role="group"` + `aria-label` ou `role="radiogroup"`.

---

## 11.8 Items de liste de choix regroupés

**Test :** Vérifier que les `<select>` avec de nombreuses options utilisent `<optgroup>` pour les regrouper par catégorie logique si nécessaire.
**Non-conformité type :** `<select>` avec 20+ options sans aucun `<optgroup>` alors que les options relèvent de catégories distinctes.
**Priorité :** 🟡 Mineur

```tsx
<select>
  <optgroup label="Île-de-France">
    <option value="75">Paris</option>
    <option value="92">Hauts-de-Seine</option>
  </optgroup>
  <optgroup label="Auvergne-Rhône-Alpes">
    <option value="69">Rhône</option>
  </optgroup>
</select>
```

---

## 11.9 Intitulé de bouton pertinent

Chaque bouton doit avoir un intitulé décrivant son action.

**Test :** Vérifier que chaque `<button>` et `<input type="submit/reset/button">` a un texte ou `aria-label` décrivant précisément son action dans le contexte du formulaire.
**Non-conformité type :** `<button>OK</button>` ; `<button>Envoyer</button>` quand plusieurs formulaires sont présents sur la page.
**Priorité :** 🟠 Majeur

```tsx
// ❌ Mauvais
<button>OK</button>

// ✅ Bon
<button type="submit">Envoyer ma demande de contact</button>
<button type="reset">Réinitialiser le formulaire</button>
```

---

## 11.10 Contrôle de saisie

### Champs obligatoires

**Test :** Vérifier que les champs obligatoires ont une indication visible (astérisque ou texte) ET `required` ou `aria-required="true"`.
**Non-conformité type :** Champ obligatoire sans `required` ; obligation signalée visuellement (couleur seule) sans attribut ARIA.
**Priorité :** 🔴 Bloquant

```tsx
<label htmlFor="nom">
  Nom <span aria-hidden="true">*</span>
</label>
<input id="nom" required aria-required="true" />
<p className="sr-only">Les champs marqués d'un * sont obligatoires</p>
```

### Messages d'erreur

**Test :** Vérifier que les erreurs de validation sont associées au champ via `aria-describedby`, que le champ a `aria-invalid="true"`, et que le message d'erreur est visible et descriptif.
**Non-conformité type :** Message d'erreur visible mais pas lié au champ via `aria-describedby` ; `aria-invalid` absent.
**Priorité :** 🔴 Bloquant

```tsx
<label htmlFor="email">Email</label>
<input
  id="email"
  type="email"
  aria-invalid="true"
  aria-describedby="error-email"
/>
<p id="error-email" role="alert">
  Erreur : veuillez saisir une adresse email valide (ex: nom@domaine.fr)
</p>
```

### Indications de format

**Test :** Vérifier que le format attendu est indiqué avant ou au moment de la saisie (pas seulement après erreur), et lié au champ via `aria-describedby`.
**Non-conformité type :** Champ de date sans indication du format attendu (JJ/MM/AAAA).
**Priorité :** 🟠 Majeur

```tsx
<label htmlFor="tel">Téléphone</label>
<p id="hint-tel">Format attendu : 01 23 45 67 89</p>
<input id="tel" type="tel" aria-describedby="hint-tel" />
```

---

## 11.11 Suggestions de correction

En cas d'erreur, suggérer le type de données attendu et donner un exemple.

**Test :** Vérifier que les messages d'erreur contiennent une suggestion de correction concrète (exemple de valeur valide, format attendu).
**Non-conformité type :** Message "Format invalide" sans préciser le format attendu.
**Priorité :** 🟠 Majeur

```tsx
<p id="error-date" role="alert">
  Erreur : format de date invalide. Saisissez une date au format JJ/MM/AAAA (ex: 15/03/2024).
</p>
```

---

## 11.12 Données modifiables/récupérables (conséquences financières/juridiques)

Pour les formulaires avec conséquences financières, juridiques ou de suppression :
- Permettre de modifier/annuler après validation
- OU étape de vérification/confirmation avant envoi
- OU case à cocher de confirmation explicite

**Test :** Identifier les formulaires à conséquences irréversibles (paiement, suppression de compte, soumission juridique). Vérifier qu'un mécanisme de vérification ou d'annulation est proposé.
**Non-conformité type :** Formulaire de paiement sans étape de confirmation ni possibilité d'annulation.
**Priorité :** 🔴 Bloquant

```tsx
<h2>Vérifiez vos informations avant envoi</h2>
<dl>
  <dt>Nom</dt><dd>{nom}</dd>
  <dt>Email</dt><dd>{email}</dd>
</dl>
<button onClick={goBack}>Modifier</button>
<button onClick={submit}>Confirmer et envoyer</button>
```

---

## 11.13 Autocomplete pour les champs utilisateur

Champs concernant l'utilisateur : attribut `autocomplete` avec la bonne valeur.

**Test :** Vérifier que les champs demandant des données personnelles (nom, prénom, email, téléphone, adresse...) ont l'attribut `autocomplete` avec la valeur normalisée correspondante.
**Non-conformité type :** `<input type="email" name="email">` sans `autocomplete="email"`.
**Priorité :** 🟡 Mineur

```tsx
<input type="text" autoComplete="given-name" name="prenom" />
<input type="text" autoComplete="family-name" name="nom" />
<input type="email" autoComplete="email" name="email" />
<input type="tel" autoComplete="tel" name="telephone" />
<input type="text" autoComplete="street-address" name="adresse" />
<input type="text" autoComplete="postal-code" name="cp" />
<input type="text" autoComplete="address-level2" name="ville" />
```

**Valeurs courantes :** `name`, `given-name`, `family-name`, `email`, `tel`, `street-address`, `postal-code`, `address-level2` (ville), `country-name`, `organization`, `username`, `new-password`, `current-password`, `bday`, `cc-number`, `cc-exp`, `cc-name`.

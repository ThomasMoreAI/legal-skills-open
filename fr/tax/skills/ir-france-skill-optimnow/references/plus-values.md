# Plus-values

## Table des matières

1. [Plus-values de valeurs mobilières](#valeurs-mobilieres)
2. [Plus-values immobilières](#immobilieres)
3. [Crypto-actifs](#crypto)
4. [Cas particuliers](#cas-particuliers)

---

## Plus-values de valeurs mobilières {#valeurs-mobilieres}

### Régime PFU (défaut)
- Taux : 30 % (12,8 % IR + 17,2 % PS)
- Case : **3VG** (plus-value nette) ou **3VH** (moins-value nette)
- Pas d'abattement pour durée de détention sous PFU

### Option barème (case 2OP)
Si option barème choisie, possibilité d'appliquer les abattements pour durée de détention
**uniquement pour les titres acquis avant le 1er janvier 2018** :
- 50 % si détention >= 2 ans et < 8 ans
- 65 % si détention >= 8 ans

Abattement renforcé (PME < 10 ans lors de la souscription) :
- 50 % si détention >= 1 an et < 4 ans
- 65 % si détention >= 4 ans et < 8 ans
- 85 % si détention >= 8 ans

### Imputation des moins-values
- Les moins-values sont imputables sur les plus-values de même nature
- Report possible sur les 10 années suivantes
- Case **3VH** pour les moins-values nettes de l'année
- Cases pour les reports antérieurs : vérifier l'annexe 2074

### Source des montants
- IFU des banques et courtiers
- Pour les comptes étrangers (Interactive Brokers, Degiro, etc.) : calcul manuel souvent nécessaire
- Attention à la méthode de calcul du prix de revient moyen pondéré (PRMP)

---

## Plus-values immobilières {#immobilieres}

### Principe
Les plus-values immobilières sont imposées lors de la vente, avec prélèvement par le notaire.
Elles ne figurent PAS sur la déclaration 2042 sauf dans certains cas.

### Taux
- IR : 19 %
- Prélèvements sociaux : 17,2 %
- Surtaxe si PV > 50 000 EUR (de 2 % à 6 %)

### Abattements pour durée de détention

**Abattement IR :**
- 6 % par an de la 6e à la 21e année
- 4 % la 22e année
- Exonération totale après 22 ans

**Abattement PS :**
- 1,65 % par an de la 6e à la 21e année
- 1,60 % la 22e année
- 9 % par an de la 23e à la 30e année
- Exonération totale après 30 ans

### Exonérations
- Résidence principale : exonération totale
- Première cession d'un logement autre que la résidence principale (sous conditions)
- Prix de cession <= 15 000 EUR
- Expropriation (sous conditions de remploi)

### Cases
- **3VZ** : plus-values immobilières (pour le calcul du RFR)
- Le paiement de l'impôt est effectué par le notaire, mais le montant entre dans le RFR

---

## Crypto-actifs {#crypto}

### Régime fiscal (depuis 2019)

#### Cessions occasionnelles (particuliers)
- PFU à 30 % sur la plus-value globale annuelle
- Case : **3AN** (plus-value) ou **3BN** (moins-value)
- Formulaire annexe : **2086**
- Option barème possible (case 2OP, s'applique à tous les revenus de capitaux)

#### Calcul de la plus-value
La plus-value est calculée globalement :

```
PV = Prix de cession - (Prix total d'acquisition x Prix de cession / Valeur globale du portefeuille)
```

Chaque cession (y compris échange crypto-crypto si passage par un stablecoin)
est un fait générateur. Les échanges crypto-crypto directs (sans passage par euros/stablecoin)
ne sont en principe pas imposables (doctrine administrative à vérifier).

#### Seuil d'imposition
Les cessions dont le total annuel est inférieur à 305 EUR sont exonérées.

#### Activité professionnelle (mineurs, traders actifs)
Si l'activité est considérée comme professionnelle (fréquence, montants, moyens mis en oeuvre),
les gains relèvent des BIC ou BNC. Critères d'appréciation par l'administration fiscale.

### Obligations déclaratives
1. Déclarer chaque compte sur plateforme étrangère : formulaire **3916-bis** (Binance, Kraken, etc.)
2. Remplir l'annexe **2086** (détail de chaque cession)
3. Reporter le résultat net en case 3AN ou 3BN

### Points de vigilance
- Le non-déclaration des comptes étrangers (3916-bis) est sanctionnée (amende de 750 EUR par compte,
  ou 1 500 EUR si solde > 50 000 EUR)
- Les airdrops et le staking ont un traitement fiscal incertain -- consulter un fiscaliste
- Le DeFi (yield farming, liquidity providing) : pas de doctrine claire, prudence
- Les NFTs : traitement fiscal non stabilisé, peut relever des plus-values sur biens meubles
  ou du régime crypto selon l'analyse

---

## Cas particuliers {#cas-particuliers}

### Plus-values en report ou sursis d'imposition
- Apport de titres à une holding (art. 150-0 B ter CGI) : report d'imposition
- Cases 3WH, 3WI, etc. selon le cas
- Le report tombe en cas de cession des titres reçus en échange (sauf réinvestissement)

### Cession de titres de PME (départ en retraite)
- Abattement fixe de 500 000 EUR sous conditions
- Le dirigeant doit partir en retraite dans les 2 ans
- Conditions d'ancienneté et de participation au capital

### Exit tax
- Pour les contribuables transférant leur domicile fiscal hors de France
- S'applique si détention >= 50 % d'une société ou patrimoine titres > 800 000 EUR
- Sursis automatique au sein de l'UE/EEE (mais déclaration obligatoire)

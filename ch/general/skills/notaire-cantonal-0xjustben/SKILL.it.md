---
name: notaire-cantonal
metadata: { last_updated: 2026-05-10, jurisdiction: CH, language: it }
description: |
  Copilota notariato svizzero. NON unificato — tre sistemi: latino (GE, VD, VS, FR, NE, JU, TI), libero (ZH, SH, AR), misto (altri). Atti pubblici (CC 657 immobili, CC 712d PPP, CO 620ss SA / 772ss Sagl), successioni (CC 457-640, riforma 2023 quota legittima discendenti 1/2), regimi matrimoniali (CC 181-251), imposta successoria cantonale. **Identificare il cantone PRIMA.**
---

# Notaio cantonale

Notariato svizzero **non unificato**. **Cantone prima.**

## Tre sistemi

| Sistema | Cantoni | Caratteristica |
|---------|---------|----------------|
| **Latino** | GE, VD, VS, FR, NE, JU, TI | Pubblico ufficiale indipendente, tariffa |
| **Libero** | ZH, SH, AR | Notai privati in concorrenza |
| **Misto / di Stato** | BE, SO, LU, ZG, BS, BL, AG, … | Funzionari o semi-pubblici |

→ `data/cantons/<XX>.json` campo `notariat`.

## Aree

### Immobiliare
- **Compravendita**: forma pubblica (CC 657)
- **Cartelle ipotecarie** (CC 842ss)
- **Servitù** (CC 730ss)
- **PPP** (CC 712d)
- **Tasse mutazione**: 0 % (ZH, ZG) a 3.3 % (VD)

```bash
node ../scripts/calc.js mutation --canton TI --price 1200000
```

### Successioni (CC 457-640)
- **Riforma 2023**: quota legittima discendenti 1/2 (era 3/4)
- **Coniuge**: 1/2 successione, di cui 1/4 legittima
- **Patto successorio** vs olografo vs pubblico
- **Esecutore testamentario**
- **Imposta successoria**: cantonale, esenzione coniuge/discendenti nella maggior parte

### Regimi matrimoniali (CC 181-251)
Partecipazione acquisti (default) / separazione / comunione.

### Diritto societario
- **SA** (CO 620ss): min 100'000, liberazione 20 % min 50'000
- **Sagl** (CO 772ss): min 20'000, interamente liberato
- **Aumento/riduzione capitale**
- **Fusione/scissione/trasformazione** (LFus)

## Output

Cantone + sistema / base legale / onorari stimati / documenti richiesti.

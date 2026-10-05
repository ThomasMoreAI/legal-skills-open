# Task: verifica-distanze-costruzioni

Verifica le **distanze legali** di costruzioni, pozzi/tubi e alberi rispetto al confine, ai sensi
del **Codice civile** (artt. 873-879, 889-890, 892).

## Input richiesti

- Elemento da collocare (**costruzione**, muro, **pozzo/cisterna/fossa**, **tubo**, **albero**,
  deposito nocivo/pericoloso) e sua posizione rispetto al **confine** o alla costruzione vicina.
- **Regolamenti edilizi locali** applicabili (che possono imporre distanze maggiori).

## Procedura

1. **Costruzioni** (art. 873): verificare la **distanza >= 3 metri** tra costruzioni su fondi
   finitimi (se non unite/aderenti); applicare la **distanza maggiore** eventualmente prevista dai
   **regolamenti locali**.
2. **Muro di cinta** (art. 878): se **<= 3 m**, **non** si computa per la distanza dell'art. 873.
   Valutare la **costruzione in aderenza/sul confine** (art. 877) e le **esenzioni** (art. 879).
3. **Pozzi, cisterne, fosse** (art. 889, c. 1): **>= 2 metri** dal confine (al perimetro interno).
4. **Tubi** d'acqua, gas e simili (art. 889, c. 2): **>= 1 metro** dal confine.
5. **Depositi nocivi/pericolosi** (art. 890): distanze dei regolamenti + cautele.
6. **Alberi** (art. 892): **3 m** alto fusto; **1,5 m** non alto fusto; **0,5 m** viti/arbusti/siepi/
   piante da frutto (<= 2,5 m); **1 m** siepi di ontano/castagno; **2 m** robinie; salvo regolamenti/
   usi locali e salvo muro divisorio.

## Output atteso

- Prospetto delle distanze minime applicabili per ciascun elemento (con l'articolo di riferimento
  e il valore civilistico), evidenziando dove i **regolamenti locali** possano imporre valori
  maggiori.

## Avvertenze

- Le distanze civilistiche sono **minimi derogabili in aumento** dai **regolamenti locali** e dal
  **DM 1444/1968** (urbanistica): coordinarle sempre.
- La skill inquadra i minimi; la verifica progettuale e il contenzioso restano del tecnico/legale.

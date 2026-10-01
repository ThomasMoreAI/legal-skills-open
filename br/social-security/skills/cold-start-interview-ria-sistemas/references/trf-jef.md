# Tribunais Regionais Federais e Juizados Especiais Federais

Lista oficial dos 6 TRFs brasileiros (com a criacao do TRF-6 em 2022) com jurisdicao e principais JEFs. Usada pela skill cold-start-interview pra validar entrada do advogado e sugerir TRF a partir da UF base.

## TRFs e jurisdicoes

| TRF | Sede | UFs cobertas |
|---|---|---|
| TRF-1 | Brasilia/DF | AC, AM, AP, BA, DF, GO, MA, MT, PA, PI, RO, RR, TO |
| TRF-2 | Rio de Janeiro/RJ | RJ, ES |
| TRF-3 | Sao Paulo/SP | SP, MS |
| TRF-4 | Porto Alegre/RS | RS, SC, PR |
| TRF-5 | Recife/PE | AL, CE, PB, PE, RN, SE |
| TRF-6 | Belo Horizonte/MG | MG (criado em 2022 — Lei 14.226/2021, instalado em 19/08/2022) |

## JEFs (Juizados Especiais Federais)

Cada Secao Judiciaria tem JEFs em comarcas principais. Sao competentes pra causas previdenciarias de ate 60 salarios minimos (Lei 10.259/2001 art. 3o). Acima desse teto, vai pra Vara Federal comum.

Principais JEFs por TRF:

### TRF-1
- JEF Brasilia/DF
- JEF Goiania/GO
- JEF Belem/PA
- JEF Manaus/AM
- JEF Salvador/BA
- JEF Sao Luis/MA

### TRF-2
- JEF Rio de Janeiro/RJ (Capital)
- JEF Vitoria/ES
- JEFs em Campos, Petropolis, Niteroi, Volta Redonda, etc.

### TRF-3
- JEF Sao Paulo Capital (varios)
- JEF Campinas/SP
- JEF Ribeirao Preto/SP
- JEF Santos/SP
- JEF Campo Grande/MS

### TRF-4
- JEF Porto Alegre/RS
- JEF Curitiba/PR
- JEF Florianopolis/SC
- JEFs no interior — Caxias do Sul, Maringa, Joinville, etc.

### TRF-5
- JEF Recife/PE
- JEF Fortaleza/CE
- JEF Joao Pessoa/PB
- JEF Natal/RN
- JEF Maceio/AL
- JEF Aracaju/SE

### TRF-6
- JEF Belo Horizonte/MG (Capital)
- JEFs no interior — Uberlandia, Juiz de Fora, Montes Claros, Uberaba, etc.

## Mapa UF -> TRF (sugestao default)

Quando o advogado informa UF base, sugere automaticamente o TRF correspondente:

- **AC, AM, AP, BA, DF, GO, MA, MT, PA, PI, RO, RR, TO** -> TRF-1
- **ES, RJ** -> TRF-2
- **MS, SP** -> TRF-3
- **PR, RS, SC** -> TRF-4
- **AL, CE, PB, PE, RN, SE** -> TRF-5
- **MG** -> TRF-6

## Recursos e instancias

```
JEF (1a inst.)
  -> Turma Recursal (vinculada ao TRF da regiao)
     -> Turma Regional de Uniformizacao (TRU)
        -> Turma Nacional de Uniformizacao (TNU)
           -> STJ (recurso especial em algumas hipoteses — Lei 10.259/2001 art. 14)
              -> STF (em materia constitucional — RE)

Vara Federal comum (1a inst.)
  -> TRF (apelacao)
     -> STJ (recurso especial)
        -> STF (RE)
```

**Atencao:** materia previdenciaria pode chegar ao STJ via REsp tanto pela linha JEF -> TR -> TNU quanto pela linha Vara Federal -> TRF. Mas hipoteses de cabimento mudam (na linha JEF, e mais restrito — Lei 10.259/2001 art. 14).

**Lei 8.213/91 art. 109:** competencia em geral e da Justica Federal pra acoes contra o INSS, exceto quando a Vara Federal nao existir na comarca — ai vai pra Vara Estadual com competencia delegada (CF art. 109 paragrafo 3o).

# Tribunais Regionais do Trabalho — 24 Regioes

Lista oficial dos TRTs brasileiros, com sede e jurisdicao. Usada pela skill cold-start-interview pra validar entrada do advogado e sugerir TRT a partir da UF base.

| TRT | Sede | Jurisdicao (UF / regiao) |
|---|---|---|
| TRT-1 | Rio de Janeiro/RJ | Estado do Rio de Janeiro |
| TRT-2 | Sao Paulo/SP | Capital + Grande Sao Paulo + Baixada Santista |
| TRT-3 | Belo Horizonte/MG | Estado de Minas Gerais |
| TRT-4 | Porto Alegre/RS | Estado do Rio Grande do Sul |
| TRT-5 | Salvador/BA | Estado da Bahia |
| TRT-6 | Recife/PE | Estado de Pernambuco |
| TRT-7 | Fortaleza/CE | Estado do Ceara |
| TRT-8 | Belem/PA | Estados do Para e Amapa |
| TRT-9 | Curitiba/PR | Estado do Parana |
| TRT-10 | Brasilia/DF | Distrito Federal e Tocantins |
| TRT-11 | Manaus/AM | Estados do Amazonas e Roraima |
| TRT-12 | Florianopolis/SC | Estado de Santa Catarina |
| TRT-13 | Joao Pessoa/PB | Estado da Paraiba |
| TRT-14 | Porto Velho/RO | Estados de Rondonia e Acre |
| TRT-15 | Campinas/SP | Interior de Sao Paulo (exceto regiao do TRT-2) |
| TRT-16 | Sao Luis/MA | Estado do Maranhao |
| TRT-17 | Vitoria/ES | Estado do Espirito Santo |
| TRT-18 | Goiania/GO | Estado de Goias |
| TRT-19 | Maceio/AL | Estado de Alagoas |
| TRT-20 | Aracaju/SE | Estado de Sergipe |
| TRT-21 | Natal/RN | Estado do Rio Grande do Norte |
| TRT-22 | Teresina/PI | Estado do Piaui |
| TRT-23 | Cuiaba/MT | Estado do Mato Grosso |
| TRT-24 | Campo Grande/MS | Estado do Mato Grosso do Sul |

## Mapa UF -> TRT (sugestao default)

Quando o advogado informa UF base, sugere automaticamente o TRT correspondente:

- **AC** -> TRT-14
- **AL** -> TRT-19
- **AM** -> TRT-11
- **AP** -> TRT-8
- **BA** -> TRT-5
- **CE** -> TRT-7
- **DF** -> TRT-10
- **ES** -> TRT-17
- **GO** -> TRT-18
- **MA** -> TRT-16
- **MG** -> TRT-3
- **MS** -> TRT-24
- **MT** -> TRT-23
- **PA** -> TRT-8
- **PB** -> TRT-13
- **PE** -> TRT-6
- **PI** -> TRT-22
- **PR** -> TRT-9
- **RJ** -> TRT-1
- **RN** -> TRT-21
- **RO** -> TRT-14
- **RR** -> TRT-11
- **RS** -> TRT-4
- **SC** -> TRT-12
- **SE** -> TRT-20
- **SP** (capital/grande SP/santos) -> TRT-2
- **SP** (interior) -> TRT-15
- **TO** -> TRT-10

**Observacao:** SP tem dois TRTs. Se a UF for SP, pergunta de quais cidades o advogado pratica mais antes de sugerir TRT-2 ou TRT-15.

**Recursos superiores:** acima de qualquer TRT, recurso de revista vai ao TST (Brasilia). Acima do TST em materia constitucional, RE ao STF.

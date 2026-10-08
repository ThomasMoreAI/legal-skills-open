# Estrutura dos Arquivos CSV do COAF — Exemplos Reais

## Características Técnicas dos Arquivos

- **Encoding**: ISO-8859-1 (Latin-1) — pode variar para UTF-8 ou CP1252
- **Separador**: Ponto-e-vírgula (;) — pode variar para vírgula
- **Quebra de linha**: CRLF (Windows)
- **Campos string**: Podem conter acentos, cedilha e caracteres especiais

## RIF_Envolvidos.csv

### Colunas
```
Indexador;cpfCnpjEnvolvido;nomeEnvolvido;tipoEnvolvido;agenciaEnvolvido;contaEnvolvido;DataAberturaConta;DataAtualizacaoConta;bitPepCitado;bitPessoaObrigadaCitado;intServidorCitado
```

### Exemplo de dados
```
1;222.333.444-99;GUSTAVO GONCALVES NETO;Sacador;-;-;-;-;Não;Não;Não
1;222.333.444-99;GUSTAVO GONCALVES NETO;Responsável;-;-;-;-;-;Não;-
1;222.333.444-99;GUSTAVO GONCALVES NETO;Titular;1234;999999;11/05/2010;07/02/2020;-;Não;-
2;500.500.500-55;TITO SILVEIRA;Responsável;-;-;-;-;Não;Não;Não
2;88.888.888/0001-35;EMPRESA Y;Titular;-;-;-;-;-;Não;-
```

### Observações
- Uma mesma pessoa pode aparecer múltiplas vezes com diferentes tipoEnvolvido no MESMO indexador
- Campos com "-" indicam informação não disponível
- bitPepCitado, bitPessoaObrigadaCitado, intServidorCitado: "Sim", "Não" ou "-"
- tipoEnvolvido possíveis: Titular, Sacador, Depositante, Responsável, Sócio, Beneficiário, Outros

## RIF_Comunicacoes.csv

### Colunas
```
Indexador;idComunicacao;NumeroOcorrenciaBC;Data_do_Recebimento;Data_da_operacao;DataFimFato;cpfCnpjComunicante;nomeComunicante;CidadeAgencia;UFAgencia;NomeAgencia;NumeroAgencia;informacoesAdicionais;CampoA;CampoB;CampoC;CampoD;CampoE;CodigoSegmento
```

### Exemplo de dados válidos (indexadores numéricos)
```
1;12345678;151894515;06/03/2019 14:56;01/03/2019;01/03/2019;191;Banco do Brasil;BELEM;PA;PSO BELEM;3;SAQUE;270.000,00;0;270.000,00;0;0;42
2;33333333;8942154484;12/09/2019 14:15;11/09/2019;11/09/2019;191;Banco do Brasil;CARAUARI;AM;CARAUARI;1386;DEPÓSITO;50.000,00;50.000,00;0;0;0;42
```

### Exemplo de linhas NÃO-INDEXADORAS (a ignorar na análise)
```
[linha em branco]
#COMENTÁRIOS SOBRE OS CAMPOS DE VALORES
42 - SFN - Espécie: CampoA = Total, CampoB = Valor a Crédito, CampoC = Valor a Débito...
41 - SFN - Atípicas: CampoA = Total, CampoB = Valor a Crédito...
21 - COAF - Cartões de crédito: CampoA = Valor da(s) operação(ões)...
[hash aleatório: 51b55c9edf039edfe30f4a47ab8dd0c2]
```

### IMPORTANTE sobre as linhas não-indexadoras
As linhas com formato "XX - Nome do Segmento: CampoA = ..." são **legendas** que explicam o significado dos campos de valores para cada CodigoSegmento. EXTRAIR essas legendas antes de descartá-las é essencial para interpretar corretamente os valores.

## RIF_Ocorrencias.csv

### Colunas
```
Indexador;idOcorrencia;Ocorrencia
```

### Exemplo de dados válidos
```
1;1159;Saque em espécie de valor igual ou superior a R$50.000,00 (cinquenta mil reais). Banco Central do Brasil - Circular nº 3.978/2020, art. 49-I
2;1161;Depósito em espécie de valor igual ou superior a R$50.000,00 (cinquenta mil reais). Banco Central do Brasil - Circular nº 3.978/2020, art. 49-I
5;1045;IV-a) movimentação de recursos incompatível com o patrimônio, a atividade econômica ou a ocupação profissional e a capacidade financeira do cliente. Banco Central do Brasil - Carta-Circular nº 4.001/2020, art. 1º
```

### Exemplo de linhas NÃO-INDEXADORAS (a ignorar)
```
[linha em branco]
71aad70da0ec00f807bc1791ed7d7d76  (hash aleatório)
```

## Relação entre os Arquivos

```
Indexador 1 ──┬── Envolvidos: Gustavo (Sacador, Responsável, Titular)
              ├── Comunicação: id=12345678, Saque de R$270.000, Belém/PA
              └── Ocorrência: 1159 - Saque >= R$50.000

Indexador 2 ──┬── Envolvidos: Tito (Responsável), Empresa Y (Titular), Gustavo (Depositante)
              ├── Comunicação: id=33333333, Depósito de R$50.000, Carauari/AM
              └── Ocorrência: 1161 - Depósito >= R$50.000
```

## Códigos de Segmento Frequentes

| Código | Segmento | Tipo de Comunicação |
|--------|----------|-------------------|
| 41 | SFN - Atípicas | Comunicação de Operação Suspeita (COS) |
| 42 | SFN - Espécie | Comunicação de Operação em Espécie (COE) |
| 17 | SEFEL - Loterias | Operações com loterias |
| 19 | Jóias/pedras/metais | Operações com itens de alto valor |
| 21 | Cartões de crédito | Operações com cartões |
| 24 | COFECI - Imobiliária | Transações imobiliárias |
| 37 | SUSEP - Seguros | Operações no mercado segurador |
| 44 | CVM - Valores Mobiliários | Operações em bolsa/mercado de capitais |

## Tipos de Ocorrência Mais Comuns

| idOcorrencia | Descrição Resumida | Normativa |
|-------------|-------------------|-----------|
| 1159 | Saque em espécie >= R$50.000 | Circular 3.978/2020, art. 49-I |
| 1161 | Depósito em espécie >= R$50.000 | Circular 3.978/2020, art. 49-I |
| 1045 | Movimentação incompatível com patrimônio/atividade (IV-a) | CC 4.001/2020, art. 1º |
| Outros 10XX | Diversas situações da CC 4.001/2020 | Varia por tipo |

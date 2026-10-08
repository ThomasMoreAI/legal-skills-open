# RELATÓRIO DE INQUÉRITO POLICIAL — TEMPLATE

## Estrutura do Documento .docx

Este template define a estrutura e conteúdo obrigatório do relatório final.
O documento deve ser gerado usando docx-js (npm) conforme a skill docx.

### Configurações do Documento

```
Página: A4 (11906 x 16838 DXA)
Margens: Superior 1440, Inferior 1440, Esquerda 1800, Direita 1080
Fonte: Arial 12pt
Espaçamento: 1,5 entrelinhas (line: 360)
Alinhamento padrão: Justificado
Fonte títulos: Arial Bold
```

### Cabeçalho
```
[Logo da Delegacia — se fornecido]
DELEGACIA DE POLÍCIA CIVIL DE [NOME DA CIDADE]
[NOME DA UNIDADE POLICIAL]
```

### Endereçamento
```
EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) PROMOTOR(A) DE JUSTIÇA
[da Xª Promotoria de Justiça de ____]
```

### Dados do Inquérito (em negrito)
```
Inquérito Policial nº: ___
Investigado: ___
Crime: ___
Data de instauração: ___
Data do relatório: ___
```

### Preâmbulo
```
O DELEGADO(A) DE POLÍCIA CIVIL [nome], matrícula nº [nº],
lotado(a) na [unidade], no exercício de suas atribuições legais
e em cumprimento ao disposto no art. 10, §1º, do Código de
Processo Penal, vem, respeitosamente, à presença de Vossa
Excelência apresentar o RELATÓRIO FINAL do Inquérito Policial
em epígrafe, nos termos que seguem:
```

### Seções Obrigatórias

#### I - ORIGEM DA INVESTIGAÇÃO
- Boletim de Ocorrência / Auto de Prisão em Flagrante / Requisição MP / Requisição judicial / Denúncia anônima / Outras
- Resumo da notícia-crime

#### II - QUALIFICAÇÃO DO(S) INVESTIGADO(S)
- Nome completo, alcunha, filiação, nascimento, idade, estado civil
- Profissão, naturalidade, nacionalidade, RG, CPF
- Endereço, telefone
- Antecedentes criminais
- Situação processual

#### III - QUALIFICAÇÃO DA(S) VÍTIMA(S)
- Mesmos campos do investigado (quando aplicável)

#### IV - DESCRIÇÃO DOS FATOS
- Narrativa cronológica e detalhada
- Data, horário e local
- Circunstâncias e modus operandi
- Consequências e prejuízos

#### V - TIPIFICAÇÃO PENAL
- Crime principal: tipo penal + artigo + lei + pena
- Crimes conexos
- Qualificadoras aplicáveis
- Agravantes aplicáveis
- **ANÁLISE DE LEI APLICÁVEL**: Se houve alteração legislativa, analisar lei do tempo do fato vs. lei atual, aplicando a mais benéfica

#### VI - DILIGÊNCIAS REALIZADAS
Subseções:
- A) Oitivas e Depoimentos (com datas, nomes, qualificação, folhas)
- B) Perícias Realizadas
- C) Buscas e Apreensões
- D) Quebras de Sigilo
- E) Outras Diligências

#### VII - MATERIALIDADE DELITIVA
- Elementos probatórios enumerados com descrição e localização nos autos

#### VIII - AUTORIA
- A) Indícios de Autoria: enumerados com descrição detalhada
- B) Análise da Autoria: grau de certeza, consistência, contradições

#### IX - ANÁLISE DAS PROVAS
- A) Provas Testemunhais: credibilidade e consistência
- B) Provas Periciais: relevância dos laudos
- C) Provas Documentais: análise dos documentos
- D) Provas Digitais (quando houver): dados eletrônicos

#### X - TESES DEFENSIVAS
- Argumentos da defesa (se apresentados)
- Análise de consistência com as provas

#### XI - DILIGÊNCIAS PENDENTES
- Opção 1: Não há pendências
- Opção 2: Lista de pendências com justificativa

#### XII - CONCLUSÃO
- Opção 1: INDICIAMENTO (com fundamentação detalhada, citando art. 2º, §6º, Lei 12.830/2013)
- Opção 2: NÃO INDICIAMENTO (com fundamentação)
- Opção 3: INDICIAMENTO PARCIAL (por quais crimes sim, por quais não)

#### XIII - SUGESTÃO DE ENCAMINHAMENTO
- Oferecimento de denúncia
- Arquivamento
- Diligências complementares
- Remessa (se incompetência)

#### XIV - DISPOSIÇÕES FINAIS
```
O presente inquérito policial foi conduzido com observância
aos princípios constitucionais e legais aplicáveis, garantindo-se
o contraditório e a ampla defesa sempre que possível.

Todos os elementos probatórios colhidos encontram-se devidamente
documentados nos autos, com a indicação precisa de sua localização.

Coloco-me à disposição de Vossa Excelência para quaisquer
esclarecimentos que se fizerem necessários.
```

### Fechamento
```
É o relatório.

[Cidade], [data por extenso].

[Nome do Delegado de Polícia]
Delegado(a) de Polícia Civil
[Unidade Policial]
```

## Mapeamento de Campos para Automação

Quando os dados vierem de planilha, mapear conforme tabela:

| Campo no Relatório | Origem | Exemplo |
|-------------------|--------|---------|
| Nº Inquérito | Coluna "Nº Inquérito" | "156/2025" |
| Nome Investigado | Coluna "Nome Investigado" | "Fernando Alves Costa" |
| Tipo Penal | Coluna "Crime" | "Estelionato" |
| Data Instauração | Coluna "Data Instauração" | "10/01/2025" |
| Data Relatório | Data atual ou informada | "30/01/2025" |
| Nº BO | Coluna "Nº BO" | "2025.001.234" |
| Qualificação completa | Colunas de dados pessoais | Conforme seção II |
| Descrição dos fatos | Coluna "Descrição Fatos" | Narrativa da investigação |
| Tipificação | Colunas "Crime" + "Artigo" | "Art. 171, CP" |
| Diligências | Colunas "Data Diligência X" | Com folhas dos autos |
| Conclusão | Coluna "Sugestão" | "Indiciamento" / "Arquivamento" |

## Observações para Geração Automática

1. **Idade**: Calcular automaticamente a partir da data de nascimento
2. **Data por extenso**: Converter data numérica para extenso em português
3. **Prescrição**: Calcular automaticamente com base na pena máxima
4. **Formatação de valores**: Usar formato brasileiro (R$ 1.000,00)
5. **Completude**: Nunca deixar campos em branco — marcar como "Não informado" ou "Não aplicável"
6. **Referência de folhas**: Sempre que possível, indicar folhas dos autos

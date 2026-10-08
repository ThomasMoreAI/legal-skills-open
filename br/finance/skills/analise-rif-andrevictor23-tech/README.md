# analise-rif

> Analisa Relatórios de Inteligência Financeira (RIF) do COAF a partir dos 3 CSVs oficiais e gera o Relatório de Análise Financeira (RAF) em .docx profissional.

**English summary:** Parses the three official CSV files of a Financial Intelligence Report (RIF) issued by COAF (Brazil's financial intelligence unit), cross-references entities by index key, deduplicates communications, applies money-laundering typologies from Central Bank Circular Letter 4.001/2020, and generates a professional Financial Analysis Report (.docx) for criminal investigations. Ships with a fully fictional evaluation dataset.

## O que faz

A skill assume a persona de Investigador Financeiro Policial Sênior e processa os dados brutos do COAF com metodologia relacional rigorosa. A entrada são os **três CSVs do RIF**: `RIF_[Nº]_Envolvidos.csv` (pessoas físicas/jurídicas, dados cadastrais e tipo de envolvimento), `RIF_[Nº]_Comunicacoes.csv` (comunicações financeiras, valores e períodos) e `RIF_[Nº]_Ocorrencias.csv` (irregularidades e normativas aplicáveis).

O pipeline é fixo: validação estrutural e carregamento com tratamento de encoding (latin-1/utf-8, separador `;`), **filtragem de indexadores reais** (o COAF mistura legendas, hashes e comentários nos arquivos), **deduplicação por idComunicacao** (zero tolerância a contagem dupla, inclusive entre múltiplos RIFs), **cruzamento relacional por Indexador** entre os três arquivos, conversão de valores no formato brasileiro e interpretação dos campos de valores (CampoA a CampoE) conforme o CodigoSegmento.

Sobre os dados limpos, a skill identifica titulares, verifica quais alvos da investigação constam (e em que condição: titular, depositante, sacador, sócio etc.; correspondência só por CPF/CNPJ), mapeia as correlações entre envolvidos por Indexador — hipóteses de vínculo a confirmar, não vínculo provado — e busca tipologias de lavagem nas três fases (colocação, ocultação, integração), **correlacionando as ocorrências com os incisos da Carta Circular BACEN nº 4.001/2020** (17 categorias de situações suspeitas). Diretriz inviolável: nenhuma conclusão fora dos dados dos CSVs; o que não consta é declarado como não constante.

Antes da entrega, o RAF passa obrigatoriamente pela skill `revisao-contradicoes` — um subagente independente que recalcula somas a partir das tabelas, procura contradições internas, vínculos sem sustentação e duplicidades residuais.

## Quando usar

- O usuário envia os CSVs do COAF (`RIF_Envolvidos`, `RIF_Comunicacoes`, `RIF_Ocorrencias`);
- Pedidos de análise de dados financeiros do COAF, identificação de indícios de lavagem de dinheiro, análise de vínculos financeiros ou mapeamento de redes de movimentação;
- Geração de relatório técnico de inteligência financeira (RAF);
- Investigações de lavagem de dinheiro, crimes financeiros, organização criminosa, corrupção, evasão de divisas e crimes com movimentação financeira atípica.

Para relatório final de inquérito, use `relatorio-final-ip`; esta skill é específica para RIF/COAF.

## Como usar

> "Analisa esses três CSVs do RIF 12345 do COAF. IP nº 55.4.2026.678, alvos: Fulano (CPF ...) e a empresa X (CNPJ ...)."

> "Cruza os dados do RIF e me diz quais alvos da investigação constam nas comunicações e em qual condição."

> "Identifica indícios de lavagem de dinheiro nessas movimentações, com base na Carta Circular 4.001/2020."

> "Recebi dois RIFs sobre o mesmo alvo; consolida sem contar comunicação duas vezes e mapeia os vínculos."

> "Gera o RAF completo em Word para juntar ao inquérito."

## O que a skill entrega

- **Apresentação interativa no chat**: resumo executivo, dashboard (comunicações, valores totais, período), status dos alvos (constam/não constam) e alertas de padrões suspeitos;
- **RAF em .docx profissional** (gerado com a skill `docx`): 9 seções obrigatórias — Introdução, COAF, Metodologia, Conceitos, Informações Gerais, Análise Individual dos Titulares (7 subseções por titular), Considerações Finais, Anexo com envolvidos e Informações Complementares — com sumário, tabelas, numeração de páginas e rodapé com classificação SIGILOSO;
- Valores sempre em formato brasileiro (R$ X.XXX,XX) e datas em dd/mm/aaaa, com rastreabilidade total entre dados brutos e análises.

## Estrutura da pasta

| Item | Papel |
|---|---|
| `SKILL.md` | Instruções completas: persona, diretrizes éticas e pipeline em 7 fases |
| `scripts/processar_rif.py` | Tratamento de dados das FASES 1 a 5: carga, filtragem, deduplicação, conversão de valores, período, cruzamento por Indexador, titulares, correlações e verificação de alvos |
| `references/carta_circular_4001_2020.md` | Referência das 17 categorias de situações suspeitas do BACEN |
| `references/csv_structure_examples.md` | Exemplos da estrutura real dos CSVs do COAF |
| `references/modelo_raf_v1.md` | Modelo oficial do RAF com as 9 seções obrigatórias |

## Requisitos

- **Python 3 com pandas** para carregar, limpar, deduplicar e cruzar os CSVs;
- **Arquivos de entrada**: os 3 CSVs do COAF (Envolvidos, Comunicacoes, Ocorrencias); se o material vier em PDF (extratos bancários), o extrator local Docling + EasyOCR em `~/.claude/tools/` faz a conversão antes da leitura;
- **Informações do procedimento**: número do IP/PCNET, nomes e CPFs/CNPJs dos alvos, unidade policial e autoridade solicitante;
- Skill `docx` para a geração do RAF em Word.

## Avisos

- **A minuta do RAF exige revisão da Autoridade Policial**: as recomendações investigativas e medidas cautelares sugeridas são técnicas; a decisão final é sempre da Autoridade.
- **Os dados do RIF/COAF são SIGILOSOS** e não devem ser colados em ambientes não autorizados; o documento é formatado com classificação SIGILOSO e os dados brutos não devem circular fora da estrutura do relatório técnico.
- Tratamento de dados pessoais sujeito à **LGPD** (Lei 13.709/2018); somente análises compatíveis com a finalidade investigativa/legal são permitidas.
- A skill segue as convenções da **Delegacia de Alta Floresta/MT** (modelo de RAF, fraseologia e fluxo com as skills irmãs); precisa de adaptação para uso em outras unidades.
- Conferir valores extraídos por OCR contra o original antes de somar: OCR erra dígito.

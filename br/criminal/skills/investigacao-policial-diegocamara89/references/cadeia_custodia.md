# Cadeia de Custodia de Provas Digitais

Regras e procedimentos para garantir a integridade e admissibilidade das provas digitais coletadas durante a investigacao.

## Fundamento Legal

A Lei 13.964/2019 (Pacote Anticrime) inseriu os artigos 158-A a 158-F no Codigo de Processo Penal, regulamentando a cadeia de custodia:

- **Art. 158-A**: Cadeia de custodia e o conjunto de todos os procedimentos utilizados para manter e documentar a historia cronologica do vestigio coletado
- **Art. 158-B**: O agente publico que reconhecer um elemento como de potencial interesse devera preserva-lo
- **Art. 158-C**: A coleta de vestigios devera ser realizada preferencialmente por perito oficial

## Regras para Provas Digitais

### 1. Hash de Integridade (Obrigatorio)

Toda prova digital deve ter seu hash gerado **no momento da coleta**. O hash prova que o arquivo nao foi alterado depois.

| Algoritmo | Comando (Windows) | Comando (Linux/Mac) |
|-----------|-------------------|---------------------|
| MD5 | `certutil -hashfile arquivo.pdf MD5` | `md5sum arquivo.pdf` |
| SHA256 | `certutil -hashfile arquivo.pdf SHA256` | `sha256sum arquivo.pdf` |

**Gerar AMBOS** (MD5 e SHA256) para cada arquivo. Registrar os hashes em documento formal (termo de apreensao, certidao, ou corpo do oficio).

### 2. Extracao Forense vs. Extracao Manual

| Metodo | O que e | Quando usar | Valor probatorio |
|--------|---------|-------------|-----------------|
| **Forense** | Uso de ferramenta certificada (Cellebrite, UFED, Axiom) com laudo | Quando disponivel e o caso for complexo | Alto — dificilmente contestavel |
| **Manual** | Exportacao pelo proprio app (ex: "Exportar conversa" no WhatsApp) | Quando nao ha ferramenta forense disponivel | Medio — aceitavel se acompanhado de hash e documentacao |
| **Screenshot** | Captura de tela com hash | Complementar ou quando nao ha outra opcao | Baixo se isolado — aceito se acompanhado de hash |

### 3. Screenshots com Autenticidade

Para que screenshots tenham valor probatorio:

1. Capturar a tela mostrando o **conteudo completo** (nao cortar)
2. Salvar o arquivo original (PNG/JPG)
3. Gerar hash MD5 e SHA256 do arquivo
4. Registrar: data/hora da captura, dispositivo usado, quem capturou
5. Anexar ao IP com certidao descrevendo o procedimento

### 4. Exportacao de Conversas WhatsApp

A exportacao completa e preferivel a screenshots isolados:

1. No WhatsApp: Configuracoes > Conversas > Exportar conversa > **Com midia**
2. Isso gera um arquivo .zip contendo:
   - Arquivo .txt com todas as mensagens e timestamps
   - Todas as midias (fotos, videos, audios)
3. Gerar hash do .zip completo
4. **Nao** editar ou renomear o conteudo antes de gerar o hash
5. Armazenar copia em local seguro (HD externo, nuvem institucional)

### 5. Nomenclatura de Arquivos

Padrao recomendado para organizar os arquivos de prova:

```
[BO/IP]_[TIPO]_[FONTE]_[DATA].[ext]

Exemplos:
IP-00123_whatsapp_vitima-joao_20250315.zip
IP-00123_extrato_banco-bradesco_20250301-20250315.pdf
IP-00123_screenshot_pje-acesso_20250310.png
IP-00123_hash_provas-digitais_20250320.txt
```

### 6. Registro de Cadeia de Custodia

Para cada prova digital, documentar:

| Campo | Descricao |
|-------|-----------|
| Descricao do vestigio | Ex: "Exportacao completa de conversa WhatsApp entre vitima e suspeito" |
| Data/hora da coleta | Quando foi coletado |
| Responsavel pela coleta | Nome e matricula do agente |
| Metodo de coleta | Forense, manual, screenshot |
| Hash MD5 | [valor] |
| Hash SHA256 | [valor] |
| Local de armazenamento | Onde esta guardado (HD, servidor, nuvem) |
| Transferencias | Quem recebeu, quando, por que |

### 7. Erros que Comprometem a Prova

| Erro | Consequencia |
|------|-------------|
| Nao gerar hash no momento da coleta | Defesa pode alegar adulteracao |
| Editar arquivo antes de gerar hash | Hash nao corresponde ao original |
| Coletar apenas screenshots sem exportacao completa | Defesa pode alegar selecao tendenciosa |
| Nao documentar quem coletou e quando | Quebra da cadeia de custodia |
| Armazenar em local sem controle de acesso | Risco de adulteracao ou extravio |
| Repassar prova sem registro formal | Lacuna na cadeia de custodia |

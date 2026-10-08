# Requisitos Judiciais por Tipo de Dado

Referencia rapida para o agente de policia saber o que pode requisitar diretamente (via oficio da autoridade policial) e o que exige ordem judicial previa. Carregar quando for elaborar oficios ou planejar coleta de provas (Fase 2).

> **ATENCAO**: Esta tabela reflete o entendimento predominante da jurisprudencia e doutrina ate 2025. Consultar o delegado responsavel em caso de duvida — a responsabilidade pela legalidade da requisicao e da autoridade policial, nao da ferramenta.

## Tabela de Requisitos

| Tipo de dado | Ordem judicial? | Fundamento legal | Observacoes |
|---|---|---|---|
| **Dados cadastrais** de operadora (nome, CPF, endereco do titular) | NAO | Art. 10, §3º, Marco Civil (Lei 12.965/2014) | Requisicao direta pela autoridade policial |
| **Dados cadastrais** de provedor de aplicacao (nome, email de cadastro) | NAO | Art. 10, §3º, Marco Civil | Requisicao direta. Nao inclui conteudo |
| **Dados cadastrais** bancarios (titular, data abertura, agencia) | NAO | Art. 17-B, Lei 9.613/1998 (lavagem) + LC 105/2001, art. 1º, §3º, IV | Requisicao direta em investigacao criminal |
| **Registros de conexao** (IP + timestamp do provedor de acesso) | SIM | Art. 10, caput + Art. 22, Marco Civil | Ordem judicial obrigatoria. Retencao: 1 ano |
| **Registros de acesso a aplicacao** (IP + timestamp do app) | SIM | Art. 10, caput + Art. 22, Marco Civil | Ordem judicial obrigatoria. Retencao: 6 meses |
| **Conteudo de comunicacoes** (mensagens, emails, arquivos) | SIM | Art. 7º, III + Art. 10, §2º, Marco Civil; CF art. 5º, XII | Ordem judicial obrigatoria. Interceptacao: Lei 9.296/1996 |
| **Dados de ERB/geolocalizacao** (torres de celular) | SIM | Art. 5º, XII, CF + jurisprudencia STJ | Ordem judicial. Dados retroativos de ERB = quebra de sigilo |
| **IMEI e historico de linhas** vinculadas ao aparelho | SIM | Art. 10, Marco Civil (por analogia) + jurisprudencia | Geralmente via ordem judicial (dado telematico) |
| **Extrato bancario / movimentacao financeira** | SIM | LC 105/2001, art. 1º, §4º | Quebra de sigilo bancario — ordem judicial obrigatoria |
| **Dados COAF/RIF** | NAO (acesso via sistema) | Lei 9.613/1998, art. 15 | Acesso pelo delegado via sistema proprio (Siscoaf). Nao depende de ordem judicial |
| **Dados de acesso ao PJe/TJRN** (logs de consulta processual) | SIM | Art. 5º, XII, CF + regulamento interno TJ | Requisicao ao TJ via oficio; TJ pode exigir ordem judicial |
| **Selfie biometrica / foto de abertura de conta** | SIM | Dado bancario sigiloso — LC 105/2001 | Incluir no pedido de quebra de sigilo bancario |
| **Dados de marketplace** (Mercado Livre, OLX, etc.) | SIM | Art. 22, Marco Civil | Provedor de aplicacao — ordem judicial para registros de acesso |
| **Dados de redes sociais** (perfil, conexoes, posts publicos) | DEPENDE | Art. 10, §3º (cadastrais = nao) + Art. 22 (registros = sim) | Cadastrais: requisicao direta. Registros/conteudo: ordem judicial |

## Regras Praticas

1. **Cadastrais = requisicao direta**: nome, CPF, endereco, email de cadastro, data de abertura. Nao precisa de ordem judicial em nenhum provedor.

2. **Registros (logs) = ordem judicial**: IPs de acesso, timestamps de login, historico de conexao. Sempre ordem judicial, independente do provedor.

3. **Conteudo = ordem judicial + requisitos extras**: mensagens, arquivos, fotos. Alem de ordem judicial, interceptacao em tempo real exige os requisitos da Lei 9.296/1996 (crime com pena de reclusao, indispensabilidade, etc.).

4. **Financeiro = ordem judicial (exceto COAF)**: qualquer dado bancario alem do cadastral exige quebra de sigilo. COAF/RIF e excecao — acesso direto pelo delegado.

5. **Na duvida, peca ordem judicial**: e melhor ter uma ordem judicial desnecessaria do que uma prova anulada por ilicitude. O custo de pedir e baixo; o custo de perder a prova e alto.

## Como Usar na Skill

Ao planejar coleta (Fase 2), para cada item do Painel de Status marcado como pendente:
1. Consultar esta tabela para saber se precisa de ordem judicial
2. Se NAO precisa: gerar oficio de requisicao direta (skill `/oficios`)
3. Se SIM precisa: gerar representacao cautelar (skill `/representacoes-cautelares`) para o delegado encaminhar ao Juizo
4. Registrar no Painel de Status qual tipo de requisicao foi usada

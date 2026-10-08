# Categorias de Provas Digitais (A-I)

Catalogo completo das 9 categorias de provas digitais essenciais para investigacao de fraudes. Para cada categoria: o que e, como obter, de quem solicitar, o que constitui uma versao valida, e urgencia.

---

## A — Conversas WhatsApp Completas

**O que e**: Extracao completa do dialogo entre vitima e fraudador, incluindo todas as midias (fotos, audios, videos), datas e timestamps.

**Como obter**:
- **Via vitima**: solicitar que exporte a conversa completa (WhatsApp > Conversa > Exportar > Com midia). Gerar hash MD5 e SHA256 do .zip resultante
- **Via extracao forense**: se o aparelho da vitima estiver disponivel, preferir Cellebrite/UFED/Axiom
- **Via Meta/Facebook**: quebra de sigilo telematico por ordem judicial — retorna logs de acesso, IPs, e dados da conta

**O que constitui versao valida**: exportacao completa (nao screenshots avulsos), com hash gerado no momento da coleta, sem edicao previa.

**De quem solicitar**: vitima (exportacao), Meta (logs de acesso e IPs)

**Urgencia**: 🔴 **Iminente** — vitima pode apagar conversa; Meta pode rotacionar logs

---

## B — Screenshots com Hash de Autenticidade

**O que e**: Capturas de tela de conversas, transacoes, acessos ou documentos relevantes, acompanhadas de hash criptografico para garantir integridade.

**Como obter**:
1. Capturar a tela mostrando o conteudo completo
2. Salvar o arquivo original (PNG/JPG) sem editar
3. Gerar hash MD5 e SHA256 imediatamente
4. Documentar: data/hora, dispositivo, quem capturou

**O que constitui versao valida**: imagem original + hash gerado no ato + identificacao do responsavel.

**De quem solicitar**: vitima, advogado, investigador

**Urgencia**: 🟡 **Curto prazo** — screenshots complementam, nao substituem a exportacao completa

---

## C — Comprovantes de Transferencia/Pix/TED

**O que e**: Documentos, extratos bancarios ou recibos que comprovam as transacoes financeiras feitas pela vitima para a conta do fraudador.

**Como obter**:
- **Via vitima**: solicitar comprovante do app bancario (PDF ou screenshot com hash)
- **Via banco da vitima**: oficio requisitando extrato do periodo com detalhamento de Pix/TED
- **Via BACENJUD/SISBAJUD**: consulta judicial para identificar transacoes

**O que constitui versao valida**: comprovante mostrando: data/hora, valor, conta de origem, conta de destino (banco, agencia, conta, nome do titular), tipo de operacao (Pix, TED, boleto).

**De quem solicitar**: vitima, banco da vitima

**Urgencia**: 🟢 **Estavel** — registros bancarios sao preservados por 5-10 anos

---

## D — Identificacao da Conta Bancaria Destino

**O que e**: Dados completos da conta que recebeu os valores da fraude — banco, agencia, numero da conta, tipo, titular (nome e CPF).

**Como obter**:
- **Via comprovante da vitima**: o comprovante de Pix/TED geralmente traz o nome do favorecido
- **Via banco da vitima**: oficio pedindo detalhes completos da transacao
- **Via BACENJUD/CCS**: consulta para localizar todas as contas do CPF do titular

**O que constitui versao valida**: identificacao completa — banco, agencia, conta, tipo, nome do titular, CPF.

**De quem solicitar**: banco da vitima (via transacao), banco destino (via oficio judicial)

**Urgencia**: 🟡 **Curto prazo** — conta pode ser encerrada; valores podem ser sacados/transferidos. Se possivel, solicitar bloqueio cautelar imediato

---

## E — Dados da Conta WhatsApp do Suspeito

**O que e**: Informacoes sobre a conta WhatsApp usada para o contato ilicito — numero(s) vinculado(s), data de criacao, IPs de acesso.

**Como obter**: quebra de sigilo telematico via ordem judicial dirigida a Meta/Facebook

**O que requisitar no oficio**:
- Numero(s) de telefone vinculado(s) a conta
- Data de criacao da conta
- IPs de acesso com data, hora, minuto, segundo e fuso horario
- Tipo de dispositivo (modelo, SO)
- Ultima atividade

**O que constitui versao valida**: resposta oficial da Meta com todos os campos acima preenchidos.

**De quem solicitar**: Meta/Facebook (unica fonte)

**Urgencia**: 🔴 **Iminente** — logs de acesso tem prazo de retencao limitado (Marco Civil: 6 meses para registros de aplicacao)

---

## F — Dados da Linha Telefonica (IMEI e Cadastro)

**O que e**: Informacoes sobre a linha telefonica usada pelo suspeito — titular, IMEI do aparelho, tipo de plano.

**Como obter**: quebra de sigilo telefonico e de dados via ordem judicial dirigida a operadora

**O que requisitar no oficio**:
- Dados cadastrais do titular da linha
- Historico de IMEIs vinculados no periodo investigado
- Tipo de plano (pre-pago ou pos-pago)
- Data de ativacao
- Se pre-pago: data e local da recarga mais recente

**O que constitui versao valida**: resposta oficial da operadora com todos os campos. IMEI permite rastrear o aparelho fisico e encontrar outras linhas que usaram o mesmo dispositivo.

**De quem solicitar**: operadoras (Claro, Vivo, Tim, Oi, MVNOs)

**Urgencia**: 🟡 **Curto prazo** — dados cadastrais sao estaveis; IMEI tem retencao longa (5+ anos na maioria das operadoras)

---

## G — Relatorios de Acesso de Terceiros ao Processo Judicial

**O que e**: Logs de quem acessou o processo judicial da vitima no sistema do Tribunal (PJe, e-SAJ), incluindo IP, data/hora e usuario.

**Como obter**: requisicao direta ao Tribunal de Justica (nao exige quebra de sigilo — e dado do proprio tribunal)

**O que requisitar**:
- Lista de todos os acessos ao processo n. [numero] no periodo [data inicio] a [data fim]
- Para cada acesso: IP, data, hora, minuto, segundo, fuso horario, usuario logado (OAB, nome)
- Acessos de advogados, partes e terceiros

**O que constitui versao valida**: relatorio oficial do TJ com todos os acessos e IPs.

**De quem solicitar**: TJRN, TJSP, ou o TJ competente

**Urgencia**: 🔴 **Iminente** — logs de acesso ao PJe podem ter retencao limitada. Requisitar o mais rapido possivel

**ALERTA**: acesso ao processo ≠ autoria do golpe. O terceiro que acessou pode ser intermediario, funcionario de escritorio, ou alguem que vendeu os dados. Sempre cruzar com outras fontes antes de concluir

---

## H — Tabela Comparativa de IPs (Cruzamento Multi-Fonte)

**O que e**: Tabela consolidada cruzando todos os IPs obtidos de diferentes fontes (WhatsApp, banco, TJ, operadora) para identificar convergencias.

**Como produzir**: nao e uma prova a ser "coletada", mas sim um produto de analise. Usar o template `templates/tabela_ip_cruzamento.md`.

**Fontes de dados**:
1. **WhatsApp (Meta)**: IPs de acesso a conta usada no golpe
2. **Banco**: IPs de acesso a conta destino / app
3. **TJRN/PJe**: IPs de consulta ao processo
4. **Operadora**: identificacao do titular de cada IP
5. **Email (Google/MS)**: IPs de acesso ao email usado na fraude

**O que constitui analise valida**: tabela com todos os IPs, timestamps completos (com segundos e fuso), tipo de IP (IPv4/6), e marcacao de convergencias.

**Urgencia**: 🟢 **Estrategico** — depende de ter recebido as respostas das outras requisicoes primeiro

---

## I — Provas Complementares

**O que e**: qualquer outro elemento que suporte a materialidade ou autoria e que nao se encaixe nas categorias anteriores.

**Exemplos**:
- Notificacoes bancarias / SMS recebidos pela vitima
- Emails de phishing (com headers completos para analise de IP)
- Gravacoes de audio ou video das ligacoes fraudulentas
- Boletos falsos emitidos pelo fraudador
- Sites falsos criados para a fraude (com registro WHOIS)
- Posts em redes sociais do suspeito ostentando patrimonio
- Dados de geolocalizacao (ERBs, Google Timeline)
- Registros WHOIS de dominios usados na fraude
- Dados de plataformas intermediarias (iFood, Uber, Mercado Livre)

**Como obter**: varia conforme o tipo — requisicao judicial, coleta direta, consulta publica

**Urgencia**: varia — sites podem sair do ar rapidamente (🔴), posts podem ser apagados (🔴), registros WHOIS sao estaveis (🟢)

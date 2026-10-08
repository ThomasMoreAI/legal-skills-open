# Brazilian Legal Document Types — Detection Guide

Reference for identifying document types in digitized Brazilian legal PDFs (processos judiciais).

## Detection Strategy

Each page in a Brazilian court PDF has:
1. **fls. number** — top-right margin (folha number in court filing system)
2. **Court header** — tribunal logo/name, comarca, vara
3. **Document type banner** — centered title (SENTENCA, DECISAO, DESPACHO, etc.)
4. **Digital signature stamp** — right margin with protocol info

Scan these 4 areas to classify each page.

---

## Document Categories

### 1. Decisoes Judiciais (Judicial Decisions)

#### Sentenca
- **Marker:** "SENTENCA" banner below court header
- **Court header:** "TRIBUNAL DE JUSTICA DO ESTADO DE [UF]", Comarca, Foro, Vara
- **Key content:** "Processo Digital n:", "Classe - Assunto:", "Requerente:", "Requerido:"
- **Dispositivo markers:** "JULGO PROCEDENTE", "JULGO PARCIALMENTE PROCEDENTE", "JULGO IMPROCEDENTE"
- **Ending:** "PRI." or "P.R.I.", date, "DOCUMENTO ASSINADO DIGITALMENTE"
- **Lauda numbering:** "[processo] - lauda N" at page bottom
- **Extract:** juiz, data, dispositivo, periodos reconhecidos/nao reconhecidos, honorarios, fundamentacao legal

#### Acordao (Appellate Decision)
- **Marker:** Federal court seal (Republica Federativa do Brasil), "PODER JUDICIARIO", "Tribunal Regional Federal da Xa Regiao", Turma
- **Document type:** "DECISAO" banner (monocratica) or "ACORDAO"
- **Key content:** "APELACAO CIVEL (xxx) N:", "RELATOR:", "APELANTE:", "APELADO:"
- **Structure:** "E o relatorio.", "Decido.", dispositivo
- **Dispositivo markers:** "NEGO PROVIMENTO", "DOU PROVIMENTO", "PARCIAL PROVIMENTO"
- **Extract:** tribunal, turma, relator, numero, dispositivo (per apelacao), fundamentacao, temas STJ

#### Decisao Interlocutoria
- **Marker:** "DECISAO" banner in court header (1st instance)
- **Key content:** Processo Digital n, Classe-Assunto, Exequente, Executado
- **Smaller scope:** Does not resolve the merit, addresses procedural matters
- **Common types:** deferindo cumprimento, custas, calculos, MLE/alvara
- **Extract:** juiz, data, dispositivo items, determinacoes

#### Despacho
- **Marker:** "DESPACHO" banner
- **Simpler than decisao:** Usually "Vistos. [instruction]. Intime-se."
- **Extract:** juiz, data, instrucao

### 2. Recursos (Appeals/Motions)

#### Embargos de Declaracao
- **Marker:** Same court header as acordao + "embargos de declaracao" in text
- **Key content:** "Trata-se de embargos de declaracao", embargante, alegacao
- **Dispositivo markers:** "REJEITO OS EMBARGOS", "ACOLHO OS EMBARGOS"
- **Extract:** embargante, alegacao (contradicao/omissao/obscuridade), resultado

### 3. Certidoes (Certificates)

#### Certidao de Transito em Julgado
- **Marker:** "CERTIDAO" banner below federal court header
- **Key text:** "Certifico que a R. decisao retro transitou em julgado em DD/MM/YYYY"
- **Critical field:** data_transito
- **Extract:** data do transito, data da certidao, local

#### Certidao de Remessa de Relacao
- **Marker:** "CERTIDAO DE REMESSA DE RELACAO"
- **Content:** Advogado names/OAB, forma (D.J.E / DJEN), teor do ato
- **Extract:** relacao number, advogados, teor do ato

#### Certidao de Publicacao de Relacao
- **Marker:** "CERTIDAO DE PUBLICACAO DE RELACAO"
- **Content:** Relacao number, data disponibilizacao DJE, data publicacao, prorrogacoes
- **Extract:** datas, prorrogacoes

#### Certidao de Remessa para Portal Eletronico
- **Marker:** "CERTIDAO DE REMESSA PARA O PORTAL ELETRONICO"
- **Content:** "CERTIFICA-SE que em DD/MM/YYYY o ato abaixo foi encaminhado ao Portal Eletronico do(a): PRF3 - INSS"
- **Extract:** data, destinatario, teor do ato

#### Certidao de Decurso de Prazo
- **Marker:** "CERTIDAO - DECURSO DE PRAZO PARA CONSULTA/CONFIRMACAO"
- **Content:** Portal Eletronico, intimacao automatica, prazo
- **Extract:** data inicio intimacao, teor do ato

#### Certidao de Publicacao (DJE Nacional)
- **Marker:** "Poder Judiciario", "Tribunal de Justica do Estado de Sao Paulo", "Diario de Justica Eletronico Nacional"
- **Content:** Numero do processo, Classe, Tribunal, Orgao, Tipo de documento, QR code
- **Extract:** numero publicacao, data disponibilizacao, teor da comunicacao

### 4. Execucao (Execution Phase)

#### Cumprimento de Sentenca (Peticao)
- **Marker:** "CUMPRIMENTO DE SENTENCA", "DISTRIBUICAO POR DEPENDENCIA AO PROCESSO N"
- **Content:** Petitioning text, pedidos (a, b, c, d), assinatura advogado
- **Extract:** data protocolo, pedidos, advogado assinante

#### Calculos de Liquidacao
- **Marker:** "CONTA FACIL PREV" or "RESUMO DO CALCULO DE LIQUIDACAO DE SENTENCA"
- **Structure:** Tables with columns (Data, Valor, Coef. Corr., Principal Corrigido, Juros, Selic, Total)
- **Sections:** I-PARTES, II-SUCUMBENCIAS, III-TOTALIZACAO, DEMONSTRATIVO DE PARCELAS
- **Key values:** Principal corrigido, juros moratorios, SELIC, total, sucumbencias, total geral
- **Footer:** "Calculo elaborado por: [nome]", local, data, versao sistema
- **Extract:** all monetary values, parcelas period, RMI, criterios, elaborador

#### Oficio Requisitorio (PRECWEB)
- **Marker:** "PRECWEB", "Visualizar Requisicao", "Requisicao incluida com sucesso!"
- **Key fields:** OFICIO REQUISITORIO n, Tipo de Procedimento (Precatorio/RPV), valores
- **Structure:** Dados Gerais, Valores e Datas, Autor, Reu, Advogado, Requerente, Movimentacoes
- **Extract:** numero, tipo, valores (total, principal, juros, SELIC), datas transito, status

#### Requisicao de Pagamentos
- **Marker:** "Requisicao de Pagamentos" from web.trf3.jus.br
- **Structure:** Procedimento, Numero, CNJ, datas, valores, advogado, banco
- **Extract:** numero requisicao, situacao (REGISTRADA/PAGO TOTAL), valores

#### Extrato de Pagamento
- **Marker:** "EXTRATO DE PAGAMENTO DE REQUISITORIO" or "EXTRATO DE PAGAMENTO DE PRECATORIOS E REQUISICOES DE PEQUENO VALOR"
- **Content:** Dados Gerais (procedimento, ano, mes), Dados dos Beneficiarios, banco, conta
- **Extract:** data pagamento, valor pago total/principal/juros, beneficiario, banco, conta, status

#### Alvara
- **Marker:** "ALVARA - LEVANTAMENTO DE VALORES"
- **Content:** "VALOR A TRANSFERIR: R$ xx.xxx,xx", conta judicial, banco destino, beneficiario
- **Extract:** valor, conta judicial, data deposito, banco/agencia/conta destino, beneficiario

### 5. Documentos Pessoais e Administrativos

#### Procuracao Ad Judicia
- **Marker:** "PROCURACAO AD JUDICIA ET EXTRA" (often in a box)
- **Content:** OUTORGANTE (handwritten), OUTORGADO(S) (typed), PODERES
- **Extract:** outorgante dados, outorgados (nome, OAB), poderes, data

#### Declaracao de Hipossuficiencia
- **Marker:** "DECLARACAO", "DECLARA, para os devidos fins de direito"
- **Content:** Statement of poverty/inability to pay costs
- **Extract:** declarante, data

#### Documento de Identidade (RG/CPF)
- **Marker:** "REPUBLICA FEDERATIVA DO BRASIL", "CARTEIRA DE IDENTIDADE"
- **Content:** Scanned ID card with foto, nome, RG, CPF, filiacao, naturalidade, data nascimento
- **Extract:** nome, RG, CPF, data nascimento, naturalidade, filiacao

#### DARE-SP (Custas)
- **Marker:** "DARE-SP", "Governo do Estado de Sao Paulo, Secretaria da Fazenda"
- **Content:** Nome, endereco, CPF, codigo receita, valor, data vencimento
- **Extract:** nome, CPF, valor, data emissao/vencimento

#### Comprovante de Pagamento
- **Marker:** "pagamento realizado" (app banking screenshot)
- **Content:** Valor, destinatario, pagador, data, ID transacao
- **Extract:** valor, data, pagador, destinatario

### 6. Comunicacoes

#### Oficio INSS/Central
- **Marker:** INSS seal, "Oficio INSS/Central de Analise de Beneficio"
- **Content:** Processo, Vara, dados do cumprimento, NB, DIB, DIP, RMI
- **Extract:** NB, DIB, DIP, RMI, tipo assunto

#### CONBAS (Informacoes do Beneficio)
- **Marker:** "Instituto Nacional do Seguro Social", "INFORMACOES DA CONCESSAO DO BENEFICIO (CONBAS)"
- **Content:** NB, DIB, DER, DIP, RMI, especie, situacao, OL, ramo atividade, tempo, CNIS
- **Extract:** All fields — comprehensive benefit data

#### Emails (Outlook)
- **Marker:** Outlook logo, email headers (De/Para/Data/Assunto)
- **Content:** Email body, attachments list
- **Extract:** remetente, destinatario, data, assunto, resumo

#### Ato Ordinatorio
- **Marker:** "ATO ORDINATORIO" banner in court header
- **Content:** Certidao with art. 203 §4 CPC reference, instructions
- **Extract:** data, instrucao, servidor

#### Ciencia da Intimacao
- **Marker:** TJ-SP seal, "CIENCIA DA INTIMACAO"
- **Content:** Autos n, Foro, data intimacao, prazo, intimado, teor do ato
- **Extract:** data intimacao, prazo, intimado, teor

#### Formulario de Resgate (Handwritten)
- **Marker:** "Formulario de Solicitacao de Resgate de Deposito Judicial / Precatorio"
- **Content:** Beneficiario, banco, agencia, conta, tipo (CC/Poupanca)
- **Extract:** beneficiario, CPF, banco, agencia, conta (cross-reference with typed docs)

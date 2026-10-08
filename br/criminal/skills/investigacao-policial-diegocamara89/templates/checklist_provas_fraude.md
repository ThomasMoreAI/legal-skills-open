# Checklist de Provas — Fraude Generica

Checklist aplicavel a qualquer tipo de fraude (estelionato, falso advogado, fraude eletronica, Pix, conta laranja). Marcar o status de cada item conforme a investigacao avanca.

**Legenda**: ✅ Obtido | ❌ Nao obtido | 🔄 Em andamento | ⏳ Aguardando resposta | N/A Nao aplicavel

---

## Tabela 1 — Materialidade (provar que o crime aconteceu)

| # | Item de Prova | Status | Fonte | Data | Observacao |
|---|--------------|--------|-------|------|------------|
| 1 | Boletim de Ocorrencia (BO) | | Delegacia | | |
| 2 | Comprovante de transferencia/Pix/TED | | Vitima | | Valor, data, conta destino |
| 3 | Extrato bancario da vitima (mostrando debito) | | Vitima/Banco | | |
| 4 | Conversa WhatsApp completa (exportacao forense) | | Vitima/Meta | | Com hash MD5/SHA256 |
| 5 | Screenshots com hash de autenticidade | | Vitima | | MD5 ou SHA256 |
| 6 | Identificacao da conta destino (banco+agencia+conta+titular) | | Banco/BACENJUD | | |
| 7 | Extrato da conta destino (mostrando credito) | | Banco | | Confirma recebimento |
| 8 | Emails fraudulentos recebidos | | Vitima | | Headers completos |
| 9 | Documentos falsos utilizados na fraude | | Vitima | | Procuracoes, contratos, boletos |
| 10 | Relatorio de materialidade (se elaborado pelo advogado/vitima) | | Advogado | | Nome vitima, processo, prints |

## Tabela 2 — Autoria (provar quem fez)

| # | Item de Prova | Status | Fonte | Data | Suspeito |
|---|--------------|--------|-------|------|----------|
| 1 | IP do WhatsApp no momento do contato fraudulento | | Meta/Facebook | | |
| 2 | IP do banco no momento da transacao/abertura de conta | | Instituicao financeira | | |
| 3 | IP do TJRN/PJe no momento de consulta processual indevida | | TJRN | | |
| 4 | Dados da linha telefonica (titular, IMEI, tipo) | | Operadora | | |
| 5 | Identificacao do titular do IP pela operadora de internet | | ISP/Operadora | | |
| 6 | Selfie biometrica de abertura da conta destino | | Banco | | |
| 7 | Dados cadastrais da chave Pix destino | | Banco/BCB | | |
| 8 | Logs de email (criacao, acesso, telefone vinculado) | | Google/Microsoft | | |
| 9 | Cruzamento de IPs convergindo no mesmo individuo | | Multi-fonte | | |
| 10 | Consulta a bancos de dados policiais (INFOSEG, estadual) | | INFOSEG/SISP | | |

## Tabela 3 — Expansao de Rede (mapear a organizacao)

| # | Item | Status | Fonte | Resultado |
|---|------|--------|-------|-----------|
| 1 | Todas as chaves Pix da conta destino | | Banco | |
| 2 | IMEI dos aparelhos vinculados a linha suspeita | | Operadora | |
| 3 | Outras linhas que usaram o mesmo IMEI | | Operadora | |
| 4 | Outras contas bancarias do suspeito | | BACENJUD/CCS | |
| 5 | Vinculos societarios do suspeito | | Receita Federal | |
| 6 | Historico de reclamacoes/bloqueios da conta | | Banco | |
| 7 | Outras vitimas do mesmo modus operandi | | Delegacia/SISP | |

---

## Resumo de Status

| Categoria | Total | ✅ | ❌ | 🔄 | ⏳ |
|-----------|-------|----|----|----|----|
| Materialidade | 10 | | | | |
| Autoria | 10 | | | | |
| Expansao de Rede | 7 | | | | |
| **TOTAL** | **27** | | | | |

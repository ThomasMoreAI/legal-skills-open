# Tabela de Cruzamento de IPs

Tabela para cruzar IPs obtidos de fontes independentes e identificar convergencias. Preencher uma linha para cada IP obtido, independente da fonte.

**Objetivo**: quando o mesmo IP (ou mesma operadora/bloco) aparece em fontes diferentes com timestamps proximos, isso e um **ponto de convergencia** — forte indicio de que o mesmo individuo operava os sistemas naquele momento.

---

## Dados do Caso

| Campo | Valor |
|-------|-------|
| BO/IP n. | [preencher] |
| Periodo investigado | [data inicio] a [data fim] |
| Suspeito(s) sob analise | [nome(s), se identificado(s)] |

## Tabela de Cruzamento

| # | Fonte | IP | Data | Hora:Min:Seg | Fuso | IPv4/6 | Porta | Titular (via operadora) | Convergencia |
|---|-------|-----|------|-------------|------|--------|-------|------------------------|-------------|
| 1 | WhatsApp (Meta) | | | | America/Fortaleza | | N/A | | |
| 2 | Banco (transacao) | | | | | | | | |
| 3 | TJRN/PJe (consulta) | | | | | | | | |
| 4 | Operadora (resposta) | | | | | | | | |
| 5 | Email (Google/MS) | | | | | | | | |
| 6 | Outro: [especificar] | | | | | | | | |

[Adicionar mais linhas conforme necessario]

## Legenda da Coluna "Convergencia"

| Simbolo | Significado |
|---------|-------------|
| ✅ CONVERGENTE | Mesmo IP em 2+ fontes com timestamps proximos — forte indicio |
| 🔶 PARCIAL | Mesmo bloco de IP ou mesma operadora, mas sem confirmacao exata |
| ❌ DIVERGENTE | IPs diferentes entre fontes — investigar se ha NAT ou multiplos dispositivos |
| ⏳ PENDENTE | Aguardando resposta da operadora/provedor |

## Alertas Importantes

### Sobre IPv4 e NAT
- Um IPv4 **sozinho** (sem porta logica) **NAO individualiza** o usuario
- Se voce so tem o IPv4, precisa requisitar a operadora os dados em **dois horarios distintos**
- Sempre perguntar ao provedor (Meta, banco) se ha **porta logica** no log

### Sobre IPv6
- IPv6 **individualiza** o dispositivo — nao precisa de porta
- Um unico timestamp basta para requisitar a operadora

### Campos Obrigatorios em Todo Oficio de IP
Todo oficio requisitando identificacao de titular de IP **deve conter**:
1. Endereco IP completo
2. Data
3. Hora
4. Minuto
5. Segundo
6. Fuso horario (America/Fortaleza, UTC, etc.)

Falta de qualquer desses campos pode invalidar a resposta da operadora.

## Analise de Convergencia

[Apos preencher a tabela, descrever aqui as convergencias encontradas:]

- **Convergencia 1**: [descrever — ex: IP X.X.X.X aparece no WhatsApp (14:32:17) e no banco (14:35:02) no mesmo dia, intervalo de 2min45s]
- **Convergencia 2**: [descrever]

**Conclusao preliminar sobre autoria**: [descrever o grau de confianca baseado nas convergencias]

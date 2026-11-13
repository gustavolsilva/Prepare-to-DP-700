# Exercício Prático: Implementar RLS, CLS e Mitigar Direct Lake Fallback

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Cenário de Negócio
Implementar segurança granular com Row-Level Security (RLS) e Column-Level Security (CLS) no SQL Analytics Endpoint e compreender o comportamento de Direct Lake Fallback no Power BI.

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo do Laboratório

#### Tarefa 1: Criar a Função Predicado e a Política de Segurança (RLS)
1. No SQL Analytics Endpoint ou Warehouse, abra uma consulta SQL.
2. Crie a função inline table-valued que valida o usuário conectado via USER_NAME().
3. Aplique a SECURITY POLICY com FILTER PREDICATE sobre a tabela de vendas.

#### Tarefa 2: Diagnosticar o Fallback de Direct Lake para DirectQuery
1. Conecte um relatório do Power BI no Modo Direct Lake.
2. Abra o Performance Analyzer e observe que a consulta sofre Fallback para DirectQuery porque o motor VertiPaq não processa RLS nativo do SQL Endpoint.
3. Compreenda a recomendação do Fabric: para manter Direct Lake puro com subsegundo, configure o RLS diretamente no Modelo Semântico do Power BI.

---

## ⚠️ Ponto Crítico para o Exame DP-700
Regra Fundamental do Exame DP-700: RLS ou CLS habilitados na camada SQL do Fabric provocam Fallback silencioso de Direct Lake para DirectQuery no Power BI. Para manter o modo Direct Lake de memória pura, implemente as regras de segurança no próprio Modelo Semântico.

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/0012-security-governance-rls-cls-fallback/lab_simulation.py
```

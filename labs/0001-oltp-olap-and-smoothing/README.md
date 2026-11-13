# Exercício Prático: Provisionar Capacidade Fabric e Explorar Lakehouse vs Warehouse

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Cenário de Negócio
A Contoso Global Retail está migrando sua arquitetura legado para o Microsoft Fabric. Como Engenheiro de Dados, você deve criar um Workspace sob uma capacidade Fabric, provisionar um Lakehouse para ingestão de dados em arquivos Delta e um Data Warehouse para relatórios analíticos corporativos com transações T-SQL ACID.

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo do Laboratório

#### Tarefa 1: Acessar o Portal e Criar o Workspace com Capacidade Fabric
1. Acesse o portal do Microsoft Fabric e efetue login.
2. No canto inferior esquerdo, clique no ícone de Engenharia de Dados (Data Engineering).
3. No menu lateral, clique em Workspaces e crie um novo workspace nomeado DP700_Foundations_Lab.
4. Nas configurações avançadas, assegure-se de vincular o workspace a uma Capacidade Fabric (Trial ou F-SKU).
5. Clique em Aplicar.

#### Tarefa 2: Criar o Lakehouse e Ingerir Arquivos Brutos via PySpark
1. Dentro do workspace, clique em + Novo item e selecione Lakehouse.
2. Nomeie como lh_retail_raw e clique em Criar.
3. Clique em Abrir notebook &gt; Novo notebook.
4. Execute o código PySpark abaixo para carregar dados brutos e salvá-los como tabela Delta:

```python
# Ingestão de dados brutos de vendas no Lakehouse
dados = [
    (1, "Notebook Gamer", 4500.00, "Sul"),
    (2, "Monitor UltraWide", 1800.00, "Sudeste"),
    (3, "Teclado Mecânico", 350.00, "Sul")
]
colunas = ["ProdutoID", "NomeProduto", "Preco", "Regiao"]

df = spark.createDataFrame(dados, colunas)
df.write.format("delta").mode("overwrite").saveAsTable("raw_produtos")
print("✅ Tabela raw_produtos gravada com sucesso em Delta Lake!")
```

#### Tarefa 3: Criar o Data Warehouse e Executar Transações T-SQL ACID
1. Retorne ao workspace, clique em + Novo item e selecione Data Warehouse.
2. Nomeie como dw_retail_corporate e clique em Criar.
3. Na barra de ferramentas, clique em Nova consulta SQL e execute o script T-SQL com suporte a transações multi-tabela:

```t-sql
-- Criação de tabela relacional com integridade no Warehouse
CREATE TABLE dbo.DimProduto (
    ProdutoID INT NOT NULL,
    NomeProduto VARCHAR(100) NOT NULL,
    Preco DECIMAL(10,2) NOT NULL,
    Regiao VARCHAR(50) NOT NULL
);

-- Transação ACID atômica
BEGIN TRANSACTION;
INSERT INTO dbo.DimProduto (ProdutoID, NomeProduto, Preco, Regiao)
VALUES (1, 'Notebook Gamer', 4500.00, 'Sul'),
       (2, 'Monitor UltraWide', 1800.00, 'Sudeste');
COMMIT TRANSACTION;

SELECT Regiao, SUM(Preco) AS TotalVendas FROM dbo.DimProduto GROUP BY Regiao;
```

---

## ⚠️ Ponto Crítico para o Exame DP-700
No exame DP-700, lembre-se: o Lakehouse é focado em arquivos e manipulação de Big Data com Spark (possuindo SQL Endpoint somente leitura), enquanto o Data Warehouse oferece suporte transacional completo DDL/DML, multi-table transactions ACID e segurança avançada (RLS/CLS).

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/0001-oltp-olap-and-smoothing/lab_simulation.py
```

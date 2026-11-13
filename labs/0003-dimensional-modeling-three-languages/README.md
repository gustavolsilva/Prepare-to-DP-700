# Exercício Prático: Modelagem Dimensional em Star Schema com T-SQL, PySpark e KQL

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Cenário de Negócio
A Fabrikam precisa estruturar um modelo dimensional em Star Schema (Tabela Fato e Dimensões) e comparar a performance e custo de consulta analítica entre as três linguagens fundamentais do Fabric: T-SQL, PySpark e KQL.

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo do Laboratório

#### Tarefa 1: Modelar o Star Schema no Fabric Warehouse via T-SQL
1. No Fabric Data Warehouse dw_sales_enterprise, clique em Nova consulta SQL.
2. Execute o script de criação da Fato e Dimensões com chaves substitutas (Surrogate Keys):

```t-sql
-- 1. Criação das Dimensões
CREATE TABLE dbo.DimCliente (
    ClienteSK INT IDENTITY(1,1) NOT NULL,
    ClienteBK VARCHAR(50) NOT NULL,
    NomeCliente VARCHAR(100) NOT NULL,
    Regiao VARCHAR(50) NOT NULL
);

-- 2. Tabela Fato
CREATE TABLE dbo.FactVendas (
    VendaID BIGINT NOT NULL,
    ClienteSK INT NOT NULL,
    DataKey INT NOT NULL,
    ValorTotal DECIMAL(12,2) NOT NULL,
    Quantidade INT NOT NULL
);
```

#### Tarefa 2: Transformar Dados e Gerar Chaves no PySpark
1. Abra o Notebook Spark vinculado ao Lakehouse.
2. Execute a célula PySpark gerando Surrogate Keys usando funções analíticas de janela (Window Functions):

```python
from pyspark.sql.functions import monotonically_increasing_id, row_number
from pyspark.sql.window import Window

df_raw = spark.table("raw_clientes")
windowSpec = Window.orderBy("ClienteBK")
df_dim_cliente = df_raw.withColumn("ClienteSK", row_number().over(windowSpec))

df_dim_cliente.write.format("delta").mode("overwrite").saveAsTable("dim_cliente_gold")
print("✅ Dimensão com Surrogate Key gerada com sucesso!")
```

#### Tarefa 3: Consultar Telemetria com KQL no Eventhouse
1. Acesse o Eventhouse evh_iot_telemetry.
2. Abra o KQL Queryset e execute uma consulta analítica de série temporal de alta frequência:

```kql
RawTelemetry
| where Timestamp > ago(24h)
| summarize MediaTemperatura = avg(Temperature), Pico = max(Temperature) by bin(Timestamp, 15m), DeviceId
| top 5 by Pico desc
```

---

## ⚠️ Ponto Crítico para o Exame DP-700
Lembre-se para a prova: T-SQL é o motor padrão para Star Schema e joins relacionais; PySpark é ideal para transformações de dados semiestruturados e geração distribuída de chaves; KQL é o motor imbatível para séries temporais e telemetria de alta frequência.

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/0003-dimensional-modeling-three-languages/lab_simulation.py
```

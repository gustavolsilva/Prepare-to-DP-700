# Laboratório Prático 0002: Delta Lake, Medallion Architecture & Time Travel

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Objetivo
Aprender a implementar uma arquitetura Medallion sobre o **OneLake** no **Microsoft Fabric**, gravar tabelas Delta Lake gerenciadas com otimização **V-Order**, auditar o histórico de commits na pasta `_delta_log/`, executar consultas com **Time Travel** e realizar manutenção periódica com `OPTIMIZE` e `VACUUM`.

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo

#### Tarefa 1: Criar o Lakehouse
1. Selecione a experiência **Engenharia de Dados (Data Engineering)** no canto inferior esquerdo.
2. Acesse seu Workspace e clique em **+ Novo item** > **Lakehouse**.
3. Nomeie como `lh_sales_medallion` e clique em **Criar**.

#### Tarefa 2: Criar o Notebook PySpark
1. Na barra superior do Lakehouse, clique em **Abrir notebook** > **Novo notebook**.
2. Confirme o Lakehouse anexado e renomeie o notebook para `02_Delta_Medallion_HandsOn`.

#### Tarefa 3: Ingerir Dados e Gravar Tabela Delta (Commit V0)
Execute em uma célula PySpark:
```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

schema_vendas = StructType([
    StructField("PedidoID", IntegerType(), False),
    StructField("Cliente", StringType(), False),
    StructField("Produto", StringType(), False),
    StructField("Quantidade", IntegerType(), False),
    StructField("ValorUnitario", DoubleType(), False),
    StructField("DataPedido", StringType(), False)
])

dados_lote_1 = [
    (101, "Contoso", "Surface Laptop Studio", 2, 1999.00, "2026-01-10"),
    (102, "Fabrikam", "Licença Fabric F64", 1, 8400.00, "2026-01-11"),
    (103, "Litware", "Xbox Series X Console", 4, 499.00, "2026-01-12")
]

df_vendas_v0 = spark.createDataFrame(dados_lote_1, schema_vendas)

df_vendas_v0.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("silver_vendas")

print("✅ Tabela silver_vendas criada com sucesso no OneLake!")
```

#### Tarefa 4: Inserir Novos Dados e Auditar o `_delta_log` (Commit V1)
```python
dados_lote_2 = [
    (104, "AdventureWorks", "Headset Microsoft Teams", 10, 89.90, "2026-01-15"),
    (105, "Northwind", "Monitor 4K 32 polegadas", 3, 650.00, "2026-01-16")
]

df_novos = spark.createDataFrame(dados_lote_2, schema_vendas)
df_novos.write.format("delta").mode("append").saveAsTable("silver_vendas")

# Inspecionar histórico do log
display(spark.sql("DESCRIBE HISTORY silver_vendas").select("version", "timestamp", "operation", "operationMetrics.numOutputRows"))
```

#### Tarefa 5: Consultas com Time Travel
```python
# Consulta snapshot histórico (Versão 0)
df_v0 = spark.read.format("delta").option("versionAsOf", 0).table("silver_vendas")
display(df_v0)

# Consulta estado atual (HEAD)
display(spark.table("silver_vendas"))
```

#### Tarefa 6: Manutenção da Tabela (OPTIMIZE e VACUUM)
```sql
%%sql
OPTIMIZE silver_vendas;
VACUUM silver_vendas RETAIN 168 HOURS;
```

#### Tarefa 7: Validação no SQL Analytics Endpoint
Alterne para o **SQL analytics endpoint** no canto superior direito e execute:
```sql
SELECT 
    Cliente,
    COUNT(PedidoID) AS TotalPedidos,
    SUM(Quantidade * ValorUnitario) AS ReceitaTotal
FROM silver_vendas
GROUP BY Cliente
ORDER BY ReceitaTotal DESC;
```

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/0002-parquet-delta-medallion/lab_simulation.py
```
Esse script gera localmente os arquivos colunares Parquet e a pasta `_delta_log` com arquivos JSON de commit para inspeção dos metadados.


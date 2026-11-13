#!/usr/bin/env python3
"""
Laboratório Hands-On: Modelagem Dimensional & As Três Linguagens do DP-700
Compara a resolução analítica de um mesmo problema em T-SQL, PySpark e KQL.
Executa dentro do .venv/ sem dependências externas pesadas.
"""

import sqlite3
import pandas as pd

def run_simulation():
    print("=" * 75)
    print("DEMO PRÁTICA: MODELAGEM DIMENSIONAL & AS 3 LINGUAGENS DO EXAME DP-700")
    print("=" * 75)

    # 1. Criação do Modelo Estrela em Memória (Fato Vendas + Dimensão Cliente + Dimensão Produto)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE DimCustomer (
        CustomerKey INTEGER PRIMARY KEY,
        CustomerId VARCHAR(10),
        CustomerName VARCHAR(50),
        Region VARCHAR(20)
    );
    """)

    cur.execute("""
    CREATE TABLE FactSales (
        SalesKey INTEGER PRIMARY KEY,
        CustomerKey INTEGER,
        SalesAmount DECIMAL(10,2),
        TransactionDate DATE,
        FOREIGN KEY (CustomerKey) REFERENCES DimCustomer(CustomerKey)
    );
    """)

    cur.executemany("INSERT INTO DimCustomer VALUES (?, ?, ?, ?)", [
        (1, "C001", "Acme Corp", "Sul"),
        (2, "C002", "Global Tech", "Sudeste"),
        (3, "C003", "Mega Varejo", "Sul"),
    ])

    cur.executemany("INSERT INTO FactSales VALUES (?, ?, ?, ?)", [
        (101, 1, 1500.00, "2026-11-01"),
        (102, 1, 2300.50, "2026-11-02"),
        (103, 2, 890.00, "2026-11-02"),
        (104, 3, 4200.00, "2026-11-03"),
        (105, 2, 1150.00, "2026-11-04"),
    ])
    conn.commit()

    print("\n1. [LINGUAGEM 1: T-SQL no Fabric Data Warehouse]")
    print("Consulta analítica agregada com JOIN relacional e GROUP BY:")
    tsql_query = """
    SELECT 
        c.Region,
        COUNT(f.SalesKey) AS TotalTransactions,
        SUM(f.SalesAmount) AS TotalRevenue,
        AVG(f.SalesAmount) AS AvgTicket
    FROM FactSales f
    INNER JOIN DimCustomer c ON f.CustomerKey = c.CustomerKey
    GROUP BY c.Region
    ORDER BY TotalRevenue DESC;
    """
    df_tsql = pd.read_sql_query(tsql_query, conn)
    print(df_tsql.to_string(index=False))

    print("\n2. [LINGUAGEM 2: PySpark no Fabric Lakehouse]")
    print("Transformação equivalente expressa na sintaxe do Apache Spark DataFrame API:")
    pyspark_equivalent = """
    # df_fact.join(df_customer, df_fact.CustomerKey == df_customer.CustomerKey, "inner") \\
    #   .groupBy("Region") \\
    #   .agg(
    #       count("SalesKey").alias("TotalTransactions"),
    #       sum("SalesAmount").alias("TotalRevenue"),
    #       avg("SalesAmount").alias("AvgTicket")
    #   ).orderBy(col("TotalRevenue").desc())
    """
    print(pyspark_equivalent.strip())
    print("-> Resultado gerado idêntico, porém escalável sobre petabytes no cluster Spark.")

    print("\n3. [LINGUAGEM 3: KQL no Fabric Eventhouse]")
    print("Consulta equivalente expressa com o operador pipe (|) do Kusto Query Language:")
    kql_equivalent = """
    FactSales
    | lookup DimCustomer on CustomerKey
    | summarize 
        TotalTransactions = count(),
        TotalRevenue = sum(SalesAmount),
        AvgTicket = avg(SalesAmount)
      by Region
    | order by TotalRevenue desc
    """
    print(kql_equivalent.strip())
    print("-> Processamento colunar indexado nativo em memória para streaming e telemetria.")

    print("\n" + "=" * 75)
    print("RESUMO PARA O EXAME DP-700:")
    print("• T-SQL: Escolha prioritária para Data Warehouse, relatórios relacionais e Star Schema.")
    print("• PySpark: Escolha prioritária para Lakehouse, limpeza complexa em batch e streaming distribuído.")
    print("• KQL: Escolha prioritária para Eventhouse, logs, time-series e telemetria em tempo real.")
    print("=" * 75)

if __name__ == "__main__":
    run_simulation()


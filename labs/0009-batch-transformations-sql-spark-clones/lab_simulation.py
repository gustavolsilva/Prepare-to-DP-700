#!/usr/bin/env python3
"""
Laboratório Hands-On: Transformações Batch em PySpark & T-SQL, Schema Evolution e Zero-Copy Clones
Curso Preparatório DP-700: Microsoft Fabric Data Engineer Associate
Simula operações atômicas de MERGE, evolução de esquema Delta e clonagem zero-copy.
"""

import json

def run_batch_simulation():
    print("=" * 80)
    print("LABORATÓRIO: TRANSFORMAÇÕES BATCH, SCHEMA EVOLUTION E TABLE CLONES (DP-700)")
    print("=" * 80)

    # 1. Simulação do Comando MERGE INTO (Upsert Atômico)
    print("\n1. [INSTRUÇÃO MERGE INTO: SINCRONIZAÇÃO ATÔMICA]")
    print("Sintaxe T-SQL no Fabric Data Warehouse:")
    tsql_merge = """
    MERGE INTO DimProduct AS target
    USING StgProduct AS source
    ON target.ProductSKU = source.ProductSKU
    WHEN MATCHED AND target.Price <> source.Price THEN
        UPDATE SET target.Price = source.Price, target.LastUpdated = GETUTCDATE()
    WHEN NOT MATCHED THEN
        INSERT (ProductSKU, ProductName, Price, LastUpdated)
        VALUES (source.ProductSKU, source.ProductName, source.Price, GETUTCDATE());
    """
    print(tsql_merge.strip())
    print("✅ Operação de inserção de novos registros e atualização de existentes em transação ACID única.")

    # 2. Simulação de Schema Evolution (mergeSchema no PySpark)
    print("\n2. [SCHEMA EVOLUTION EM TABELAS DELTA LAKE]")
    print("No PySpark dentro do Lakehouse, se os dados de entrada tiverem colunas novas,")
    print("o Delta Lake rejeita a gravação por padrão para proteger a integridade.")
    print("A opção '.option(\"mergeSchema\", \"true\")' permite a expansão segura do esquema:")
    
    spark_schema_evolution = """
    # Gravação com evolução automática de colunas
    df_new_orders.write \\
        .format("delta") \\
        .mode("append") \\
        .option("mergeSchema", "true") \\
        .saveAsTable("silver_orders")
    """
    print(spark_schema_evolution.strip())
    print("✅ Novas colunas são adicionadas automaticamente ao log Delta com valor NULL para linhas antigas.")

    # 3. Simulação de Zero-Copy Table Clone no Fabric Warehouse
    print("\n3. [ZERO-COPY TABLE CLONES: CREATE TABLE AS CLONE OF]")
    print("Sintaxe no Fabric Data Warehouse para criar ambiente de homologação instantâneo:")
    clone_sql = """
    -- Cria um clone instantâneo sem copiar terabytes de dados no OneLake
    CREATE TABLE FactSales_Testing
    AS CLONE OF FactSales;
    """
    print(clone_sql.strip())
    print("✅ Benefício: Cria novos metadados apontando para os mesmos arquivos Parquet.")
    print("   Custos de armazenamento adicionais: R$ 0,00 até que linhas sejam modificadas no clone!")

    print("\n" + "=" * 80)
    print("PONTOS CRÍTICOS PARA O EXAME DP-700:")
    print("1. Zero-Copy Clone: No Warehouse, use 'CREATE TABLE ... AS CLONE OF' para testes.")
    print("2. Schema Evolution: No Lakehouse, ative 'mergeSchema=true' no Spark para tolerar novas colunas.")
    print("3. Ingestão Rápida em T-SQL: Use 'COPY INTO' para carregar arquivos Parquet/CSV externos")
    print("   diretamente em tabelas do Warehouse com alto paralelismo nativo.")
    print("=" * 80)

if __name__ == "__main__":
    run_batch_simulation()


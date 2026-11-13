#!/usr/bin/env python3
"""
Laboratório Hands-On: Orquestração de Dados, DAG de Execução e Dataflows Gen2 vs Pipelines
Curso Preparatório DP-700: Microsoft Fabric Data Engineer Associate
Simula um Directed Acyclic Graph (DAG) com orquestração de dependências e mssparkutils.
"""

import time
import json

def simulate_pipeline_orchestration():
    print("=" * 80)
    print("LABORATÓRIO: ORQUESTRAÇÃO DE DADOS, DAGS & DATA FACTORY NO FABRIC (DP-700)")
    print("=" * 80)

    # 1. Definição do DAG de Execução em Grafo Acíclico Dirigido
    dag_definition = {
        "pipeline_name": "PL_Ingest_And_Transform_Sales",
        "activities": [
            {"id": "act_1", "name": "Copy_Raw_ERP_To_Bronze", "type": "CopyActivity", "dependsOn": []},
            {"id": "act_2", "name": "Ingest_S3_Customer_Shortcuts", "type": "ScriptActivity", "dependsOn": []},
            {"id": "act_3", "name": "Run_Silver_Cleansing_Notebook", "type": "TridentNotebook", "dependsOn": ["act_1", "act_2"]},
            {"id": "act_4", "name": "DataflowGen2_Transform_Gold_Dims", "type": "DataflowGen2", "dependsOn": ["act_3"]},
            {"id": "act_5", "name": "Run_Gold_Fact_Aggregation", "type": "TridentNotebook", "dependsOn": ["act_4"]},
        ]
    }

    print("\n1. [ESTRUTURA DO DAG DO DATA FACTORY NO FABRIC]")
    for act in dag_definition["activities"]:
        deps = ", ".join(act["dependsOn"]) if act["dependsOn"] else "Nenhuma (Início em Paralelo)"
        print(f"• Atividade: {act['name']:<35} Tipo: {act['type']:<18} Depende de: {deps}")

    # 2. Simulação da Execução Concorrente com mssparkutils.notebook.runMultiple
    print("\n2. [SIMULAÇÃO DE MSSPARKUTILS.NOTEBOOK.RUNMULTIPLE]")
    print("No PySpark dentro do Fabric, é possível disparar DAGs complexos de múltiplos")
    print("notebooks com dependências e controle estrito de concorrência:")
    
    dag_spark_code = """
    DAG = {
        "activities": [
            { "name": "Bronze_Orders", "path": "nb_bronze_orders", "timeoutPerCellInSeconds": 300 },
            { "name": "Bronze_Customers", "path": "nb_bronze_customers", "timeoutPerCellInSeconds": 300 },
            { 
                "name": "Silver_Merge", 
                "path": "nb_silver_merge", 
                "dependencies": ["Bronze_Orders", "Bronze_Customers"] 
            }
        ],
        "concurrency": 2
    }
    mssparkutils.notebook.runMultiple(DAG)
    """
    print(dag_spark_code.strip())

    # 3. Matriz Comparativa: Dataflows Gen2 vs Data Factory Pipelines vs Notebooks
    print("\n3. [MATRIZ DE DECISÃO DE ORQUESTRAÇÃO PARA O DP-700]")
    matrix = [
        ("Dataflows Gen2", "Power Query M / Low-Code", "Limpeza visual, mesclagem e cargas com staging Lakehouse."),
        ("Data Factory Pipelines", "Orquestrador de Atividades", "Controle de fluxo (If, ForEach, Until, WebHook, Failures) e triggers."),
        ("Spark Notebooks", "PySpark / Scala / SQL", "Grandes volumes, Machine Learning, Delta Lake merges e paralelismo C++."),
        ("Copy Job", "Ingestão Rápida sem código", "Assistente de cópia simples e direto para fontes de dados populares.")
    ]

    for item, lang, use in matrix:
        print(f"• {item:<24} | {lang:<28} | {use}")

    print("\n" + "=" * 80)
    print("REGRA CRÍTICA PARA O EXAME DP-700:")
    print("Dataflows Gen2 utilizam um Lakehouse de Staging oculto para acelerar transformações")
    print("Power Query M. Se a questão pedir ETL visual baseado em interface gráfica, use Dataflows Gen2.")
    print("Se a questão pedir orquestração com tratamento de falhas e laços de repetição, use Pipelines!")
    print("=" * 80)

if __name__ == "__main__":
    simulate_pipeline_orchestration()


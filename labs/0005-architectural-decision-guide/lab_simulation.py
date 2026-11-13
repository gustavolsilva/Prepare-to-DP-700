#!/usr/bin/env python3
"""
Laboratório Hands-On: Matriz de Decisão Arquitetural do Microsoft Fabric
Compara as capacidades de Lakehouse, Warehouse, Eventhouse e SQL Database
Executa 100% isolado no .venv/.
"""

def run_decision_engine():
    print("=" * 80)
    print("GUIA INTERATIVO DE DECISÃO ARQUITETURAL: LAKEHOUSE vs WAREHOUSE vs EVENTHOUSE")
    print("Exame DP-700: Microsoft Certified Fabric Data Engineer Associate")
    print("=" * 80)

    engines = {
        "Fabric Lakehouse": {
            "primary_engine": "Apache Spark (PySpark / Scala / SQL) + SQL Endpoint",
            "write_capabilities": "Spark (Append, Overwrite, Merge). SQL Endpoint é READ-ONLY.",
            "data_types": "Estruturados, semiestruturados (JSON/Parquet/Avro), não estruturados (Files).",
            "acid_support": "Sim, garantido pelo protocolo Delta Lake.",
            "ideal_persona": "Engenheiros de Dados, Cientistas de Dados, Desenvolvedores Spark.",
            "best_use_case": "Carga inicial, limpeza pesada Bronze/Silver, Machine Learning e ETL em larga escala."
        },
        "Fabric Data Warehouse": {
            "primary_engine": "Polaris T-SQL Distributed Relational Engine",
            "write_capabilities": "T-SQL DML completo (INSERT, UPDATE, DELETE, MERGE, CTAS, Clone).",
            "data_types": "Dados estruturados relacionais padronizados com schema estrito.",
            "acid_support": "Sim, transações ACID relacionais de múltiplos comandos nativas.",
            "ideal_persona": "Data Warehousing Engineers, DBA SQL, Desenvolvedores BI e Analistas.",
            "best_use_case": "Camada Gold analítica, Star Schema corporativo, lógica complexa T-SQL e migração de DWs legados."
        },
        "Fabric Eventhouse": {
            "primary_engine": "Kusto Engine (KQL - Kusto Query Language)",
            "write_capabilities": "Ingestão contínua de streaming (Eventstreams, Kafka, REST API).",
            "data_types": "Séries temporais, telemetria de sensores, logs de sistemas, dados semiestruturados dinâmicos.",
            "acid_support": "Ingestão transacional via Update Policies.",
            "ideal_persona": "Engenheiros de Real-Time, Operações (SecOps/DevOps), Arquitetos IoT.",
            "best_use_case": "Análise de logs de servidores, monitoramento em tempo real de frotas e séries temporais."
        },
        "Fabric SQL Database (Preview/Novo)": {
            "primary_engine": "Azure SQL Database Serverless Engine integrado ao OneLake",
            "write_capabilities": "T-SQL OLTP completo para aplicações transacionais nativas em nuvem.",
            "data_types": "Bancos relacionais operacionais transacionais com replicação automática.",
            "acid_support": "Transações ACID completas para leitura e gravação transacional.",
            "ideal_persona": "Desenvolvedores de Aplicações, Engenheiros de Software.",
            "best_use_case": "Bancos operacionais de backends de aplicativos que sincronizam dados no OneLake sem ETL."
        }
    }

    for name, specs in engines.items():
        print(f"\n📦 [{name.upper()}]")
        print(f"• Motor Principal:     {specs['primary_engine']}")
        print(f"• Escrita / DML:       {specs['write_capabilities']}")
        print(f"• Tipos de Dados:      {specs['data_types']}")
        print(f"• Persona Principal:   {specs['ideal_persona']}")
        print(f"• Caso de Uso Canônico: {specs['best_use_case']}")

    print("\n" + "=" * 80)
    print("⚡ SIMULADOR DE PERGUNTA DE PROVA DP-700:")
    print("Cenário: A equipe precisa criar uma tabela na camada Gold. Os analistas exigem")
    print("executar comandos 'UPDATE' e 'DELETE' via scripts T-SQL existentes do SSMS.")
    print("Se você criar no Lakehouse via SQL Endpoint, a operação falhará porque o SQL Endpoint")
    print("do Lakehouse é SOMENTE LEITURA. A resposta correta do exame é o FABRIC DATA WAREHOUSE!")
    print("=" * 80)

if __name__ == "__main__":
    run_decision_engine()


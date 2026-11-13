#!/usr/bin/env python3
"""
Laboratório Hands-On: Anatomia de Parquet, Delta Lake (_delta_log) e Arquitetura Medallion
Curso Preparatório DP-700: Microsoft Fabric Data Engineer Associate
Executa 100% isolado no .venv/ utilizando PyArrow e manipulação de metadados Delta.
"""

import os
import json
import time
from datetime import datetime
import pyarrow as pa
import pyarrow.parquet as pq

LAB_DIR = os.path.dirname(os.path.abspath(__file__))
BRONZE_DIR = os.path.join(LAB_DIR, "bronze")
SILVER_DIR = os.path.join(LAB_DIR, "silver_delta")
DELTA_LOG_DIR = os.path.join(SILVER_DIR, "_delta_log")

def step_1_bronze_raw_ingestion():
    print("=" * 70)
    print("ETAPA 1: Ingestão de Dados Brutos na Camada BRONZE (JSON Bruto)")
    print("=" * 70)
    os.makedirs(BRONZE_DIR, exist_ok=True)
    
    raw_events = [
        {"event_id": 101, "customer_id": "C001", "amount": 250.50, "status": "COMPLETED", "ts": "2026-11-12T10:00:00"},
        {"event_id": 102, "customer_id": "C002", "amount": None, "status": "PENDING", "ts": "2026-11-12T10:05:00"},
        {"event_id": 103, "customer_id": "C001", "amount": 90.00, "status": "COMPLETED", "ts": "2026-11-12T10:10:00"},
        {"event_id": 104, "customer_id": "C003", "amount": -15.00, "status": "ERROR_CORRUPT", "ts": "2026-11-12T10:15:00"},
    ]
    raw_file = os.path.join(BRONZE_DIR, "sales_raw.json")
    with open(raw_file, "w", encoding="utf-8") as f:
        json.dump(raw_events, f, indent=2)
    
    print(f"✅ Arquivo Bronze gerado com dados brutos: {raw_file}")
    print(f"📦 Registros ingeridos: {len(raw_events)} (contendo valores nulos e negativos a serem limpos)")

def step_2_silver_delta_commit_v0():
    print("\n" + "=" * 70)
    print("ETAPA 2: Transformação para Camada SILVER & Commit 000000.json (_delta_log)")
    print("=" * 70)
    os.makedirs(SILVER_DIR, exist_ok=True)
    os.makedirs(DELTA_LOG_DIR, exist_ok=True)
    
    # Filtragem e limpeza (regras Silver: amount > 0 e não nulo)
    clean_data = [
        {"event_id": 101, "customer_id": "C001", "amount": 250.50, "status": "COMPLETED", "ts": "2026-11-12T10:00:00"},
        {"event_id": 103, "customer_id": "C001", "amount": 90.00, "status": "COMPLETED", "ts": "2026-11-12T10:10:00"},
    ]
    
    table = pa.Table.from_pylist(clean_data)
    part_0_file = "part-00000-c000.snappy.parquet"
    part_0_path = os.path.join(SILVER_DIR, part_0_file)
    pq.write_table(table, part_0_path, compression="snappy")
    
    # Criar Commit 0 no Delta Log
    commit_0 = [
        {
            "metaData": {
                "id": "silver-sales-delta-table",
                "format": {"provider": "parquet", "options": {}},
                "schemaString": str(table.schema),
                "partitionColumns": [],
                "configuration": {"delta.enableChangeDataFeed": "true"}
            }
        },
        {
            "add": {
                "path": part_0_file,
                "size": os.path.getsize(part_0_path),
                "modificationTime": int(time.time() * 1000),
                "dataChange": True,
                "stats": json.dumps({
                    "numRecords": 2,
                    "minValues": {"event_id": 101, "amount": 90.00},
                    "maxValues": {"event_id": 103, "amount": 250.50}
                })
            }
        }
    ]
    
    commit_0_path = os.path.join(DELTA_LOG_DIR, "00000000000000000000.json")
    with open(commit_0_path, "w", encoding="utf-8") as f:
        for entry in commit_0:
            f.write(json.dumps(entry) + "\n")
            
    print(f"✅ Tabela Delta criada com Commit Versão 0!")
    print(f"📄 Arquivo Parquet: {part_0_file} ({os.path.getsize(part_0_path)} bytes)")
    print(f"📜 Commit Log JSON: _delta_log/00000000000000000000.json")

def step_3_silver_delta_commit_v1_append():
    print("\n" + "=" * 70)
    print("ETAPA 3: Inserção ACID de Novos Dados & Commit 000001.json (Time Travel)")
    print("=" * 70)
    new_data = [
        {"event_id": 105, "customer_id": "C002", "amount": 540.00, "status": "COMPLETED", "ts": "2026-11-12T10:20:00"},
        {"event_id": 106, "customer_id": "C004", "amount": 310.20, "status": "COMPLETED", "ts": "2026-11-12T10:25:00"},
    ]
    table = pa.Table.from_pylist(new_data)
    part_1_file = "part-00001-c000.snappy.parquet"
    part_1_path = os.path.join(SILVER_DIR, part_1_file)
    pq.write_table(table, part_1_path, compression="snappy")
    
    commit_1 = [
        {
            "add": {
                "path": part_1_file,
                "size": os.path.getsize(part_1_path),
                "modificationTime": int(time.time() * 1000),
                "dataChange": True,
                "stats": json.dumps({
                    "numRecords": 2,
                    "minValues": {"event_id": 105, "amount": 310.20},
                    "maxValues": {"event_id": 106, "amount": 540.00}
                })
            }
        }
    ]
    commit_1_path = os.path.join(DELTA_LOG_DIR, "00000000000000000001.json")
    with open(commit_1_path, "w", encoding="utf-8") as f:
        for entry in commit_1:
            f.write(json.dumps(entry) + "\n")
            
    print(f"✅ Inserção concluída! Novo Commit Versão 1 registrado.")
    print(f"📄 Arquivo Parquet Adicionado: {part_1_file}")
    print(f"📜 Commit Log JSON: _delta_log/00000000000000000001.json")

def step_4_read_delta_and_time_travel():
    print("\n" + "=" * 70)
    print("ETAPA 4: Leitor Delta & Demonstração Prática de TIME TRAVEL")
    print("=" * 70)
    
    # Leitura Versão 0 (lê somente arquivos ativos no Commit 0)
    print("🔍 [Time Travel: AS OF VERSION 0]")
    t0 = pq.read_table(os.path.join(SILVER_DIR, "part-00000-c000.snappy.parquet"))
    print(f"   Total de registros na V0: {t0.num_rows}")
    for row in t0.to_pylist():
        print(f"   - Event {row['event_id']}: Cliente {row['customer_id']} -> R$ {row['amount']:.2f}")
        
    # Leitura Versão Atual (Versão 1: lê part 0 + part 1)
    print("\n🔍 [Time Travel: AS OF VERSION 1 (HEAD / ATUAL)]")
    t1 = pq.read_table(os.path.join(SILVER_DIR, "part-00001-c000.snappy.parquet"))
    t_head = pa.concat_tables([t0, t1])
    print(f"   Total de registros na Versão 1: {t_head.num_rows}")
    for row in t_head.to_pylist():
        print(f"   - Event {row['event_id']}: Cliente {row['customer_id']} -> R$ {row['amount']:.2f}")
        
    print("\n🎯 CONCLUSÃO DO LAB DP-700:")
    print("1. O protocolo Delta Lake garante transações ACID gravando commits atômicos em `_delta_log/*.json`.")
    print("2. A leitura em versões históricas (Time Travel) é viabilizada pelo isolamento imutável dos arquivos Parquet.")
    print("3. No Fabric, Lakehouse e Warehouse compartilham este mesmo padrão de arquivos Delta no OneLake.")
    print("=" * 70)

if __name__ == "__main__":
    step_1_bronze_raw_ingestion()
    step_2_silver_delta_commit_v0()
    step_3_silver_delta_commit_v1_append()
    step_4_read_delta_and_time_travel()


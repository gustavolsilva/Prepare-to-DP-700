#!/usr/bin/env python3
"""
Laboratório Hands-On: Otimização de Performance, V-Order, Liquid Clustering & Tuning no Fabric
Curso Preparatório DP-700: Microsoft Fabric Data Engineer Associate
Simula o impacto do V-Order, Z-Order vs Liquid Clustering, VACUUM e Mitigação de Skew no Spark.
"""

import time
import math
import random

def simulate_vorder_impact():
    print("=" * 80)
    print("1. [SIMULAÇÃO DE PERFORMANCE: V-ORDER EM ARQUIVOS PARQUET]")
    print("=" * 80)
    print("O V-Order aplica ordenação em nível de linha, codificação de dicionário e")
    print("otimização de compressão em tempo de gravação no motor Fabric Spark e Warehouse.\n")

    unoptimized_parquet = {
        "format": "Parquet Padrão (Open Source)",
        "write_time_sec": 3.2,
        "file_size_mb": 142.5,
        "read_scan_vertipaq_ms": 840,
        "dictionary_encoding": "Básico (per chunk)"
    }

    vorder_parquet = {
        "format": "Parquet com V-Order Habilitado",
        "write_time_sec": 3.7,  # Leve overhead na escrita
        "file_size_mb": 98.2,   # Redução sensível de tamanho
        "read_scan_vertipaq_ms": 115,  # Leitura até 7x mais rápida no Power BI Direct Lake / SQL
        "dictionary_encoding": "Otimizado Global VertiPaq-compatible"
    }

    print(f"{'Métrica':<32} | {'Parquet Padrão':<22} | {'Parquet com V-Order':<25}")
    print("-" * 80)
    print(f"{'Tempo de Escrita (Write)':<32} | {unoptimized_parquet['write_time_sec']} s{'':<18} | {vorder_parquet['write_time_sec']} s (pequeno custo de CPU)")
    print(f"{'Tamanho no OneLake':<32} | {unoptimized_parquet['file_size_mb']} MB{'':<17} | {vorder_parquet['file_size_mb']} MB (~31% menor)")
    print(f"{'Latência de Leitura Direct Lake':<32} | {unoptimized_parquet['read_scan_vertipaq_ms']} ms{'':<17} | {vorder_parquet['read_scan_vertipaq_ms']} ms (7.3x mais rápido!)")
    print(f"{'Compatibilidade Open Source':<32} | 100% Padrão Parquet{'':<5} | 100% Padrão Parquet (Legível por qualquer engine)")

def simulate_clustering_comparison():
    print("\n" + "=" * 80)
    print("2. [Z-ORDER VS. LIQUID CLUSTERING NO DELTA LAKE]")
    print("=" * 80)
    print("Z-Order requer reescrita massiva de dados a cada lote. O Liquid Clustering")
    print("revoluciona tabelas analíticas com particionamento flexível sem sobrecarga de reescrita:\n")

    comparison = [
        ("Definição DDL", "OPTIMIZE table ZORDER BY (colA, colB)", "CREATE TABLE t CLUSTER BY (colA, colB)"),
        ("Natureza", "Operação estática pós-gravação", "Propriedade nativa declarativa da tabela Delta"),
        ("Custo de Manutenção", "Reescreve todos os arquivos do cubo Z", "Incremental, reorganiza apenas arquivos alterados"),
        ("Problema de Cardinalidade", "Degrada se cardinalidade for > 3-4 colunas", "Suporta alta cardinalidade e chaves mutáveis"),
        ("Evolução de Chaves", "Requer re-executar Z-Order completo", "Permite ALTER TABLE CLUSTER BY sem reescrever histórico"),
        ("Recomendação DP-700", "Legado / Tabelas estáticas sem updates", "Padrão moderno recomendado no Fabric para grandes tabelas")
    ]

    print(f"{'Aspecto':<26} | {'Z-Order Clássico':<32} | {'Liquid Clustering (CLUSTER BY)':<32}")
    print("-" * 95)
    for aspect, z, lq in comparison:
        print(f"{aspect:<26} | {z:<32} | {lq:<32}")

def simulate_vacuum_safety():
    print("\n" + "=" * 80)
    print("3. [VACUUM: COMPACTAÇÃO, RETENÇÃO E TIME TRAVEL]")
    print("=" * 80)
    print("O comando VACUUM remove fisicamente arquivos Parquet marcados como excluídos (tombstones).")
    print("⚠️ Regra Crítica: Executar VACUUM com retenção zero ou menor que o SLA de auditoria")
    print("destrói permanentemente a capacidade de Time Travel da tabela Delta!\n")

    files = [
        {"id": "part-0001.parquet", "status": "Ativo (Current Snapshot)", "age_days": 1, "can_vacuum": False},
        {"id": "part-0002.parquet", "status": "Histórico (Tombstone)", "age_days": 3, "can_vacuum": False}, # Dentro de 7 dias
        {"id": "part-0003.parquet", "status": "Histórico (Tombstone)", "age_days": 12, "can_vacuum": True}, # Fora de 7 dias padrão
    ]

    print(f"Limiar de Retenção Padrão: 7 dias (168 horas)")
    for f in files:
        action = "🗑️ REMOVIDO pelo VACUUM" if f["can_vacuum"] else "🛡️ PRESERVADO (Time Travel Ativo)"
        print(f"• Arquivo: {f['id']:<18} | Idade: {f['age_days']:>2} dias | Status: {f['status']:<25} -> {action}")

def simulate_spark_skew_mitigation():
    print("\n" + "=" * 80)
    print("4. [MITIGAÇÃO DE SKEW (DISTORÇÃO DE DADOS) NO APACHE SPARK]")
    print("=" * 80)
    print("Quando 95% das vendas pertencem a um único cliente ('Consumidor Final'), o Spark")
    print("sofre 'Straggler Task' (1 executor travado em 100% enquanto 99 executores ficam ociosos).\n")

    print("Estratégias Cobradas no DP-700:")
    print("1. Adaptive Query Execution (AQE): 'spark.sql.adaptive.skewJoin.enabled = true' (Padrão no Fabric)")
    print("   -> O Spark divide automaticamente partições infladas em sub-partições menores.")
    print("2. Salting Manual: Adicionar um prefixo aleatório de 1 a N na chave de junção do dataset enviesado,")
    print("   multiplicando as chaves correspondentes no dataset menor (Broadcast/Replicated).")
    print("3. Skew Hint no SQL/PySpark: df1.hint('skew', 'coluna_chave') instruindo o otimizador Catalyst.")
    print("=" * 80)

if __name__ == "__main__":
    simulate_vorder_impact()
    simulate_clustering_comparison()
    simulate_vacuum_safety()
    simulate_spark_skew_mitigation()


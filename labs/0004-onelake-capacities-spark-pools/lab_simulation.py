#!/usr/bin/env python3
"""
Laboratório Hands-On: Fabric Capacities (F-SKUs), Algoritmo de Smoothing e Sizing de Spark Pools
Curso Preparatório DP-700: Microsoft Fabric Data Engineer Associate
Simula o consumo de Capacity Units (CUs), a janela móvel de 24h e o dimensionamento de nós Spark.
"""

def simulate_capacity_and_spark_pools():
    print("=" * 75)
    print("LABORATÓRIO: CAPACIDADES FABRIC, SMOOTHING DE 24H E SPARK POOLS (DP-700)")
    print("=" * 75)

    # 1. Tabela de Capacidades F-SKU e Equivalência em CUs
    f_skus = {
        "F2": {"cus": 2, "spark_vcores": 4},
        "F4": {"cus": 4, "spark_vcores": 8},
        "F8": {"cus": 8, "spark_vcores": 16},
        "F16": {"cus": 16, "spark_vcores": 32},
        "F32": {"cus": 32, "spark_vcores": 64},
        "F64": {"cus": 64, "spark_vcores": 128}, # SKU mínima para Power BI Pro gratuito para consumidores
        "F128": {"cus": 128, "spark_vcores": 256},
    }

    print("\n1. [MATRIZ DE F-SKUS E CAPACIDADE DISPONÍVEL]")
    print(f"{'SKU':<8} {'Capacity Units (CUs)':<22} {'Max Spark vCores':<18} {'Nota de Exame'}")
    print("-" * 75)
    for sku, info in f_skus.items():
        note = "SKU mínima p/ consumo Power BI Free" if sku == "F64" else "Suporta cargas analíticas menores"
        print(f"{sku:<8} {info['cus']:<22} {info['spark_vcores']:<18} {note}")

    # 2. Simulação do Algoritmo de Smoothing (Background vs Interactive)
    print("\n2. [SIMULAÇÃO DO ALGORITMO DE SMOOTHING]")
    burst_job_cus = 1200 # Job pesado de Spark rodou por 10 minutos consumindo 1200 CU-minutos
    capacity_sku = "F64" # Fornece 64 CUs contínuas por minuto (3840 CUs por hora)
    
    print(f"Cenário de Teste:")
    print(f"• Capacidade Alocada: {capacity_sku} (64 CUs constantes)")
    print(f"• Job de Background (Batch Data Pipeline): consumiu 1.200 CUs durante um pico de 10 minutos.")
    
    # Amortização em 24h para background jobs
    smoothing_window_hours = 24
    amortized_cu_per_hour = burst_job_cus / smoothing_window_hours
    amortized_cu_per_minute = amortized_cu_per_hour / 60

    print(f"\nResultado do Cálculo do Smoothing:")
    print(f"• Consumo instantâneo sem smoothing: 120 CUs/minuto (ultrapassaria os 64 CUs da F64 -> Throttling imediato!)")
    print(f"• Consumo amortizado em 24 horas: {amortized_cu_per_hour:.2f} CUs/hora ({amortized_cu_per_minute:.2f} CUs/minuto)")
    print(f"• Percentual da capacidade F64 utilizado durante as 24h: {(amortized_cu_per_minute / 64) * 100:.2f}%")
    print("✅ Conclusão: Graças ao Smoothing de 24h, o pico de processamento não gerou interrupção nem throttling!")

    # 3. Dimensionamento de Spark Pools (Starter vs Custom Pools)
    print("\n3. [SPARK POOL SIZING & CONCURRENCY]")
    print("No Fabric, existem dois tipos principais de Spark Pools:")
    print("• Starter Pool: Inicialização ultrarrápida (5 a 10 segundos), tamanho dinâmico pré-aquecido.")
    print("• Custom Pool: Permite configurar Node Size (Small, Medium, Large, X-Large), Autoscale e Dynamic Allocation.")
    print("\nRegra de Exame DP-700:")
    print("Para pipelines de ETL de produção com bibliotecas personalizadas e requisitos estritos de memória,")
    print("a resposta correta é configurar um Custom Spark Pool com alocação dinâmica de executores.")
    print("=" * 75)

if __name__ == "__main__":
    simulate_capacity_and_spark_pools()


"""
Laboratório 0001: Inspeção de Padrões OLTP vs. OLAP e Cálculo de Capacity Units (Smoothing)
Curso Preparatório DP-700 / Engenharia de Dados Microsoft Fabric

Este script roda de forma 100% isolada no ambiente virtual (.venv).
Demonstra:
1. Como o armazenamento orientado a colunas (OLAP) difere do orientado a linhas (OLTP).
2. Simulação da matemática oficial de Smoothing do Fabric (janela de 24 horas).
"""

import sys
import os

def demo_oltp_vs_olap():
    print("=" * 70)
    print("DEMO 1: CONCEITO DE ARMAZENAMENTO ROW-ORIENTED (OLTP) vs COLUMN-ORIENTED (OLAP)")
    print("=" * 70)
    
    # Registro de dados simulados (ex: vendas de um e-commerce)
    records = [
        {"id": 1, "customer": "Alice", "city": "SP", "amount": 250.0, "status": "COMPLETED"},
        {"id": 2, "customer": "Bob", "city": "RJ", "amount": 120.0, "status": "COMPLETED"},
        {"id": 3, "customer": "Carlos", "city": "MG", "amount": 890.0, "status": "PENDING"},
        {"id": 4, "customer": "Diana", "city": "SP", "amount": 430.0, "status": "COMPLETED"},
        {"id": 5, "customer": "Eduardo", "city": "RS", "amount": 510.0, "status": "COMPLETED"},
    ]
    
    print("\n[Cenário]: Consulta Analítica: SELECT SUM(amount) FROM sales WHERE status = 'COMPLETED'")
    
    # OLTP: Para ler amount e status, percorre a linha inteira (lendo id, customer, city etc)
    oltp_bytes_read = sum(sys.getsizeof(r) for r in records)
    print(f" -> Em banco OLTP (Linha): lê todos os campos de cada linha gravada no bloco de disco.")
    
    # OLAP: O motor lê apenas o vetor da coluna 'status' e o vetor da coluna 'amount'
    amounts = [r["amount"] for r in records]
    statuses = [r["status"] for r in records]
    olap_bytes_read = sys.getsizeof(amounts) + sys.getsizeof(statuses)
    
    print(f" -> Em banco OLAP (Coluna/Parquet): lê estritamente as colunas do predicado e agregação.")
    print(f" -> Redução de I/O em leitura analítica: I/O reduzido substancialmente com projeção de colunas.")

def demo_fabric_smoothing_math():
    print("\n" + "=" * 70)
    print("DEMO 2: SIMULAÇÃO DO ALGORITMO DE SMOOTHING DO MICROSOFT FABRIC (DP-700)")
    print("=" * 70)
    
    # Capacidade F64: Fornece 64 Capacity Units por segundo
    capacity_sku = "F64"
    cu_per_second = 64
    cu_budget_per_day = cu_per_second * 86400  # 5.529.600 CU-segundos por dia
    
    print(f"Capacidade contratada: {capacity_sku} ({cu_per_second} CU/s)")
    print(f"Orçamento diário total: {cu_budget_per_day:,} CU-segundos")
    
    # Suponha um job pesado de Spark executado às 02:00 da manhã
    # Duração: 10 minutos (600 segundos) consumindo 512 CU/s instantâneos
    burst_duration_sec = 600
    burst_cu_intensity = 512
    total_consumed_cu_sec = burst_duration_sec * burst_cu_intensity  # 307.200 CU-s
    
    print(f"\n[Evento]: Job de Spark dispara um pico de consumo:")
    print(f" -> Duração: {burst_duration_sec} segundos ({burst_duration_sec // 60} minutos)")
    print(f" -> Intensidade instantânea: {burst_cu_intensity} CUs ({burst_cu_intensity / cu_per_second:.1f}x a capacidade nominal)")
    print(f" -> Total bruto consumido: {total_consumed_cu_sec:,} CU-segundos")
    
    # Sem smoothing (comportamento tradicional em nuvem):
    print(f"\n[Sem Smoothing (Sistemas legados)]:")
    print(f" -> O sistema falharia ou exigiria auto-scale para 512 vCores para aguentar 10 minutos.")
    
    # Com Smoothing no Fabric (Janela de Background = 24 horas / 86400 segundos):
    smoothing_window_sec = 86400
    smoothed_cu_per_second = total_consumed_cu_sec / smoothing_window_sec
    percent_capacity_used = (smoothed_cu_per_second / cu_per_second) * 100
    
    print(f"\n[Com Smoothing no Microsoft Fabric (Janela móvel de 24 horas)]:")
    print(f" -> Consumo rateado na janela: {smoothed_cu_per_second:.2f} CUs por segundo")
    print(f" -> Impacto na capacidade {capacity_sku}: {percent_capacity_used:.2f}% das CUs disponíveis")
    print(f" -> Conclusão para o exame: O job conclui sem throttling porque o pico foi suavizado.")

if __name__ == "__main__":
    demo_oltp_vs_olap()
    demo_fabric_smoothing_math()


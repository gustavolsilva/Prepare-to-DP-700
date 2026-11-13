#!/usr/bin/env python3
"""
Laboratório Hands-On: Monitoramento, Troubleshooting, Fabric Capacity Metrics App & DMVs
Curso Preparatório DP-700: Microsoft Fabric Data Engineer Associate
Simula métricas de capacidade (Interactive vs Background), estágios de Throttling e DMVs de Query Insights.
"""

def simulate_capacity_metrics_app():
    print("=" * 80)
    print("LABORATÓRIO: MONITORAMENTO, FABRIC CAPACITY METRICS APP & DMVs (DP-700)")
    print("=" * 80)

    # 1. Distinção Crucial do Exame: Operações Interativas vs. Background
    print("\n1. [FABRIC CAPACITY METRICS APP: CLASSIFICAÇÃO DE CARGAS]")
    print("No Capacity Metrics App, as operações são categorizadas em dois grupos com janelas de suavização distintas:\n")

    workload_types = [
        ("Operações Interativas", "Power BI DAX, Notebooks interativos, consultas SQL ad-hoc", "5 minutos", "Interactive Delay (atraso de 60s) -> Rejeição Total de consultas"),
        ("Operações em Background", "Data Factory Pipelines, Jobs agendados Spark, Dataflows Gen2", "24 horas", "Rejeição de novos disparos de pipelines agendados")
    ]

    print(f"{'Tipo de Operação':<26} | {'Exemplos de Carga':<35} | {'Janela Smoothing':<18} | {'Impacto do Throttling'}")
    print("-" * 110)
    for w_type, examples, window, impact in workload_types:
        print(f"{w_type:<26} | {examples:<35} | {window:<18} | {impact}")

    # 2. Estágios Progressivos de Throttling (Estrangulamento)
    print("\n2. [ESTÁGIOS PROGRESSIVOS DE THROTTLING NA CAPACIDADE (DP-700)]")
    stages = [
        ("Estágio 1: Interactive Delay", "Consumo cumulativo excede 100% da cota futura", "Adiciona atraso artificial de ~60 segundos a consultas interativas para desestimular uso simultâneo."),
        ("Estágio 2: Interactive Rejection", "Consumo cumulativo atinge limite crítico", "Novas consultas do Power BI ou SQL Analytics Endpoint são rejeitadas imediatamente com erro de capacidade."),
        ("Estágio 3: Background Rejection", "Esgotamento severo da capacidade em 24h", "Pipelines e notebooks agendados falham imediatamente ao iniciar até que a capacidade recupere fôlego.")
    ]
    for s_name, trigger, action in stages:
        print(f"⚠️ {s_name:<30} -> {trigger}\n   Ação do Fabric: {action}\n")

    # 3. T-SQL Query Insights Views no Fabric Data Warehouse
    print("=" * 80)
    print("3. [T-SQL QUERY INSIGHTS & DMVs PARA IDENTIFICAR GARGALOS]")
    print("=" * 80)
    print("O Fabric Data Warehouse oferece o schema 'queryinsights' para auditoria e troubleshooting sem impactar o catálogo de produção:\n")

    views = [
        ("queryinsights.exec_requests_history", "Histórico detalhado de cada consulta executada, duração em ms, status e alocação de CUs."),
        ("queryinsights.frequently_run_queries", "Consultas com maior frequência de execução para identificar padrões de pooling ou loops."),
        ("queryinsights.long_running_queries", "Top consultas que excederam o tempo médio esperado, apontando falta de estatísticas ou joins cartesianos."),
        ("sys.dm_exec_requests", "Visão em tempo real de consultas ativas no momento presente, permitindo identificar bloqueios e waits.")
    ]

    for v_name, v_desc in views:
        print(f"🔍 {v_name:<38} -> {v_desc}")

    # 4. Exemplo de Query T-SQL para Troubleshooting
    print("\n[EXEMPLO PRÁTICO: CONSULTA DE TROUBLESHOOTING DE ALTO CONSUMO]")
    tsql_sample = """SELECT TOP 5
    distributed_statement_id,
    batch_sql_string,
    total_elapsed_time_ms,
    allocated_cpu_time_ms,
    row_count
FROM queryinsights.exec_requests_history
WHERE status = 'Completed'
ORDER BY allocated_cpu_time_ms DESC;"""
    print(tsql_sample)
    print("=" * 80)

if __name__ == "__main__":
    simulate_capacity_metrics_app()


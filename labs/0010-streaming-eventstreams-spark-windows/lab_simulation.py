#!/usr/bin/env python3
"""
Laboratório Hands-On: Engenharia de Streaming, Eventstreams e Janelas Temporais no Fabric
Curso Preparatório DP-700: Microsoft Fabric Data Engineer Associate
Simula janelas Tumbling, Hopping, Sliding e o controle de dados atrasados via Watermarking.
"""

from datetime import datetime, timedelta

def simulate_streaming_windows():
    print("=" * 80)
    print("LABORATÓRIO: ENGENHARIA DE STREAMING, EVENTSTREAMS E JANELAS (DP-700)")
    print("=" * 80)

    # 1. Matriz de Janelas Temporais de Streaming
    print("\n1. [MATRIZ DE JANELAS TEMPORAIS EM STREAMING]")
    windows = [
        ("Tumbling Window", "Janela Fixa Não Sobreposta", "window(ts, '5 minutes')", "Agregações periódicas sem sobreposição (ex: total de vendas a cada 5 min)."),
        ("Hopping Window", "Janela com Salto / Sobreposição", "window(ts, '10 minutes', '5 minutes')", "Média móvel de 10 minutos recalculada a cada 5 minutos."),
        ("Sliding Window", "Janela Deslizante por Evento", "Baseada em eventos dentro de um limiar", "Dispara quando a contagem dentro da janela de 2 min ultrapassa limite."),
        ("Session Window", "Janela de Sessão por Inatividade", "session_window(ts, '15 minutes')", "Agrupa interações de um mesmo usuário até 15 min de inatividade.")
    ]

    for name, desc, syntax, use in windows:
        print(f"• {name:<18} | {desc:<30} | {use}")

    # 2. Simulação de Spark Structured Streaming com withWatermark
    print("\n2. [SPARK STRUCTURED STREAMING COM WATERMARK (DADOS ATRASADOS)]")
    print("Sintaxe oficial PySpark no Fabric Lakehouse:")
    spark_stream_code = """
    streaming_df = spark.readStream \\
        .format("delta") \\
        .table("bronze_iot_telemetry") \\
        .withWatermark("event_timestamp", "10 minutes") \\
        .groupBy(
            window("event_timestamp", "5 minutes"),
            "device_id"
        ) \\
        .agg(
            avg("temperature").alias("avg_temp"),
            max("temperature").alias("max_temp")
        )

    # Gravação contínua na camada Silver
    query = streaming_df.writeStream \\
        .format("delta") \\
        .outputMode("append") \\
        .option("checkpointLocation", "/Files/checkpoints/silver_iot") \\
        .toTable("silver_iot_aggregated")
    """
    print(spark_stream_code.strip())

    # 3. Simulação de Eventstreams no Fabric
    print("\n3. [FABRIC EVENTSTREAMS: INGESTÃO VISUAL EM TEMPO REAL]")
    print("No Fabric Real-Time Intelligence, o item 'Eventstreams' permite:")
    print("• Origens Nativas: Azure Event Hubs, Apache Kafka, IoT Hub, Custom App (REST API).")
    print("• Processador de Eventos: Filtros, transformações e janelas sem código.")
    print("• Destinos Suportados: Eventhouse (KQL), Lakehouse (Tabelas Delta) ou Derived Stream.")

    print("\n" + "=" * 80)
    print("REGRA DE EXAME DP-700:")
    print("1. withWatermark('timestamp', '10 minutes'): Permite que o motor Spark espere")
    print("   até 10 minutos por eventos atrasados de rede antes de fechar a janela em memória.")
    print("2. Tumbling vs Hopping: Se a janela NÃO tem sobreposição, é TUMBLING.")
    print("   Se a janela TEM sobreposição (ex: dura 10 min e avança a cada 5 min), é HOPPING.")
    print("=" * 80)

if __name__ == "__main__":
    simulate_streaming_windows()


#!/usr/bin/env python3
"""
Laboratório Hands-On: KQL (Kusto Query Language), Eventhouse e Update Policies
Curso Preparatório DP-700: Microsoft Fabric Data Engineer Associate
Demonstra operadores essenciais KQL, parsing dinâmico de JSON e políticas transacionais.
"""

def simulate_kql_eventhouse():
    print("=" * 80)
    print("LABORATÓRIO: KQL, EVENTHOUSE, UPDATE POLICIES & MATERIALIZED VIEWS (DP-700)")
    print("=" * 80)

    # 1. Matriz de Operadores Críticos KQL no Exame DP-700
    print("\n1. [OPERADORES CRÍTICOS DO KQL NO EVENTHOUSE]")
    operators = [
        ("summarize arg_max()", "Captura a linha inteira correspondente ao maior carimbo de tempo por dispositivo."),
        ("make-series", "Gera séries temporais preenchendo automaticamente lacunas de tempo (gaps) com zero ou null."),
        ("parse_json() / mv-expand", "Converte strings JSON em estruturas dinâmicas e expande arrays em múltiplas linhas."),
        ("has vs. contains", "'has' busca palavras inteiras indexadas (ultra-rápido); 'contains' faz scan de substrings (lento)."),
        ("lookup", "Enriquece tabelas de streaming em tempo real com dados dimensionais estáticos.")
    ]

    for op, desc in operators:
        print(f"• {op:<24} | {desc}")

    # 2. Sintaxe de uma Update Policy Transacional no Eventhouse
    print("\n2. [UPDATE POLICY TRANSACIONAL: TRANSFORMANDO STREAMING NA INGESTÃO]")
    print("Uma Update Policy executa uma função KQL automaticamente no momento em que novos")
    print("dados são ingeridos na tabela de origem (RawLogs), persistindo o resultado na tabela limpa:")
    
    kql_update_policy = """
    // 1. Função KQL que executa a transformação e parsing
    .create-or-alter function TransformRawTelemetry() {
        RawTelemetry
        | where isnotnull(RawPayload)
        | extend Parsed = parse_json(RawPayload)
        | project
            DeviceTimestamp = todatetime(Parsed.timestamp),
            DeviceId = tostring(Parsed.deviceId),
            Temperature = todouble(Parsed.metrics.temp),
            Pressure = todouble(Parsed.metrics.pressure)
    }

    // 2. Anexar a política de atualização à tabela de destino
    .alter table CuratedTelemetry policy update
    @'[{ "IsEnabled": true, "Source": "RawTelemetry", "Query": "TransformRawTelemetry()", "IsTransactional": true }]'
    """
    print(kql_update_policy.strip())

    # 3. Materialized Views em KQL
    print("\n3. [MATERIALIZED VIEWS NO KQL]")
    print("Ao contrário de Views comuns que recalculam a agregação a cada consulta,")
    print("uma Materialized View em KQL mantém o cálculo pré-computado incrementalmente:")
    
    kql_mat_view = """
    .create materialized-view HourlyDeviceStats on table CuratedTelemetry
    {
        CuratedTelemetry
        | summarize 
            AvgTemp = avg(Temperature),
            MaxTemp = max(Temperature),
            EventCount = count()
          by DeviceId, bin(DeviceTimestamp, 1h)
    }
    """
    print(kql_mat_view.strip())

    print("\n" + "=" * 80)
    print("PONTOS DE ATENÇÃO PARA O EXAME DP-700:")
    print("1. Update Policy: É a resposta certa quando o cenário exige enriquecer ou filtrar")
    print("   dados de streaming diretamente no Eventhouse sem pipelines externos.")
    print("2. has vs contains: Em perguntas de performance sobre filtros de texto,")
    print("   SEMPRE prefira 'has' (usa índice invertido) a 'contains' (varredura de texto).")
    print("3. arg_max(ts, *): Retorna a tupla completa do evento mais recente.")
    print("=" * 80)

if __name__ == "__main__":
    simulate_kql_eventhouse()


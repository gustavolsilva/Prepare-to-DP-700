#!/usr/bin/env python3
"""
Laboratório Hands-On: Carga Incremental, Watermarking e Slowly Changing Dimensions (SCD 1 e 2)
Curso Preparatório DP-700: Microsoft Fabric Data Engineer Associate
Simula o rastreamento por marca d'água (High Watermark) e a evolução temporal SCD Tipo 2 em Delta/Python.
"""

from datetime import datetime

def run_scd_simulation():
    print("=" * 80)
    print("LABORATÓRIO: CARGA INCREMENTAL, WATERMARKING E SCD TIPO 1 E TIPO 2 (DP-700)")
    print("=" * 80)

    # 1. Simulação de Watermarking (Marca d'Água de Data/Hora)
    print("\n1. [PADRÃO HIGH WATERMARKING PARA CARGA INCREMENTAL]")
    last_watermark = "2026-11-10T00:00:00"
    print(f"• Última Marca d'Água registrada no catálogo de controle: {last_watermark}")

    source_records = [
        {"id": 1, "name": "Alice Silva", "city": "Curitiba", "updated_at": "2026-11-09T14:30:00"},
        {"id": 2, "name": "Bruno Costa", "city": "São Paulo", "updated_at": "2026-11-11T10:15:00"},
        {"id": 3, "name": "Carla Dias", "city": "Belo Horizonte", "updated_at": "2026-11-12T08:00:00"},
    ]

    incremental_batch = [r for r in source_records if r["updated_at"] > last_watermark]
    new_watermark = max(r["updated_at"] for r in incremental_batch)
    print(f"• Registros filtrados pelo predicado (updated_at > last_watermark): {len(incremental_batch)}")
    for r in incremental_batch:
        print(f"   -> Cliente {r['id']} ({r['name']}) alterado em {r['updated_at']}")
    print(f"• Nova Marca d'Água promovida: {new_watermark}")

    # 2. Simulação de SCD Tipo 1 (Sobrescrita Simples / In-Place Update)
    print("\n2. [SLOWLY CHANGING DIMENSION (SCD TIPO 1: SOBRESCRITA)]")
    dim_scd1 = {
        101: {"customer_id": "C01", "name": "Carlos Lima", "city": "Porto Alegre"}
    }
    print(f"• Estado Inicial SCD1: {dim_scd1[101]}")
    # Chega atualização: Carlos mudou para Florianópolis
    dim_scd1[101]["city"] = "Florianópolis"
    print(f"• Estado Atualizado SCD1: {dim_scd1[101]}")
    print("⚠️ Nota: O histórico da cidade anterior foi perdido permanentemente!")

    # 3. Simulação de SCD Tipo 2 (Histórico Completo com IsCurrent e Effective Dates)
    print("\n3. [SLOWLY CHANGING DIMENSION (SCD TIPO 2: HISTÓRICO TEMPORAL COMPLETO)]")
    dim_scd2 = [
        {
            "surrogate_key": 1,
            "customer_id": "C01",
            "name": "Carlos Lima",
            "city": "Porto Alegre",
            "valid_from": "2025-01-01",
            "valid_to": "9999-12-31",
            "is_current": True
        }
    ]
    print(f"• Registro Original Ativo (V1):")
    print(f"  SK={dim_scd2[0]['surrogate_key']} | Cidade={dim_scd2[0]['city']} | De={dim_scd2[0]['valid_from']} Até={dim_scd2[0]['valid_to']} | Ativo={dim_scd2[0]['is_current']}")

    # Evento de Mudança de Endereço em 2026-11-13
    change_date = "2026-11-13"
    # Fecha o registro antigo
    dim_scd2[0]["valid_to"] = change_date
    dim_scd2[0]["is_current"] = False

    # Insere nova linha com nova Surrogate Key
    dim_scd2.append({
        "surrogate_key": 2,
        "customer_id": "C01",
        "name": "Carlos Lima",
        "city": "Florianópolis",
        "valid_from": change_date,
        "valid_to": "9999-12-31",
        "is_current": True
    })

    print(f"\n• Tabela após aplicação do SCD Tipo 2:")
    for row in dim_scd2:
        status = "🟢 ATUAL" if row['is_current'] else "🔴 EXPIRADO"
        print(f"  SK={row['surrogate_key']} | Cidade={row['city']:<14} | De={row['valid_from']} Até={row['valid_to']} | {status}")

    print("\n" + "=" * 80)
    print("RESUMO PARA O EXAME DP-700:")
    print("1. SCD Tipo 1: Sobrescreve valores existentes. Não preserva histórico.")
    print("2. SCD Tipo 2: Cria uma nova linha com nova Surrogate Key, colunas de data")
    print("   (ValidFrom/ValidTo) e flag booleana IsCurrent=True/False. Preserva histórico.")
    print("3. No Fabric, o comando T-SQL MERGE ou Delta Lake merge() em PySpark são os")
    print("   mecanismos canônicos para implementar SCD Tipo 2 de forma atômica.")
    print("=" * 80)

if __name__ == "__main__":
    run_scd_simulation()


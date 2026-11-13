#!/usr/bin/env python3
"""
Laboratório Hands-On: Anatomia de OneLake Shortcuts e Database Mirroring
Curso Preparatório DP-700: Microsoft Fabric Data Engineer Associate
Simula ponteiros simbólicos virtuais (Shortcuts) e replicação contínua CDC (Mirroring).
"""

import os
import json

def simulate_shortcuts_and_mirroring():
    print("=" * 75)
    print("LABORATÓRIO: ONELAKE SHORTCUTS & DATABASE MIRRORING (DP-700)")
    print("=" * 75)

    lab_dir = os.path.dirname(os.path.abspath(__file__))
    lakehouse_dir = os.path.join(lab_dir, "lakehouse_onelake")
    external_s3 = os.path.join(lab_dir, "external_aws_s3_bucket")
    external_adls = os.path.join(lab_dir, "external_adls_gen2")
    mirroring_dir = os.path.join(lab_dir, "mirrored_azure_sql")

    os.makedirs(lakehouse_dir, exist_ok=True)
    os.makedirs(external_s3, exist_ok=True)
    os.makedirs(external_adls, exist_ok=True)
    os.makedirs(mirroring_dir, exist_ok=True)

    # 1. Simulação do OneLake Shortcut
    print("\n1. [ONELAKE SHORTCUTS: INTEGRAÇÃO ZERO-COPY]")
    # Origem externa S3 com 50GB de dados
    s3_data_file = os.path.join(external_s3, "orders_2026.parquet")
    with open(s3_data_file, "w") as f:
        f.write("DADOS_PARQUET_NO_AWS_S3_SEM_COPIAR_PARA_O_ONELAKE")
    
    # Criando o Shortcut (metadado de link simbólico no OneLake)
    shortcut_meta = {
        "shortcutName": "aws_s3_orders",
        "target": {
            "type": "AmazonS3",
            "bucket": "s3://enterprise-data-lake-us-east-1/orders/",
            "region": "us-east-1",
            "authentication": "IAM_Role_Delegation",
            "caching": {"enabled": False}
        },
        "onelake_path": "/Tables/aws_s3_orders"
    }
    shortcut_file = os.path.join(lakehouse_dir, "aws_s3_orders.shortcut.json")
    with open(shortcut_file, "w") as f:
        json.dump(shortcut_meta, f, indent=2)

    print(f"✅ Shortcut OneLake criado para Amazon S3:")
    print(f"• Ponteiro Virtual: {shortcut_meta['onelake_path']}")
    print(f"• Destino Físico:   {shortcut_meta['target']['bucket']}")
    print(f"• Custo de Cópia:  R$ 0,00 (Zero bytes replicados localmente!)")

    # 2. Simulação do Database Mirroring (CDC Zero-ETL)
    print("\n2. [DATABASE MIRRORING: REPLICAÇÃO CDC ZERO-ETL]")
    # Simula um evento de Change Data Capture em banco relacional
    cdc_events = [
        {"op": "INSERT", "table": "SalesOrder", "order_id": 901, "customer": "Acme", "status": "APPROVED"},
        {"op": "UPDATE", "table": "SalesOrder", "order_id": 901, "customer": "Acme", "status": "SHIPPED"},
    ]
    mirror_log = os.path.join(mirroring_dir, "cdc_stream_manifest.json")
    with open(mirror_log, "w") as f:
        json.dump(cdc_events, f, indent=2)

    print("✅ Replicação via Mirroring configurada:")
    print("• Origem: Azure SQL Database com CDC habilitado.")
    print("• Destino: OneLake Delta Parquet em formato aberto.")
    print("• Latência: Segundos (sem necessidade de agendar pipelines periódicos de batch).")

    print("\n" + "=" * 75)
    print("PONTOS CRÍTICOS PARA O EXAME DP-700:")
    print("1. Shortcuts: Use para conectar ADLS Gen2, Amazon S3, Google Cloud Storage ou")
    print("   Dataverse diretamente ao Lakehouse sem criar pipelines de cópia de dados.")
    print("2. Mirroring: Use para bancos relacionais (Azure SQL, Snowflake, Cosmos DB)")
    print("   onde é exigido sincronização contínua com latência mínima e zero pipelines.")
    print("=" * 75)

if __name__ == "__main__":
    simulate_shortcuts_and_mirroring()


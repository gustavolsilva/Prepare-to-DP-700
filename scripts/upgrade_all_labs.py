#!/usr/bin/env python3
"""
Script de atualização massiva dos laboratórios práticos para o padrão Microsoft Learn.
Aplica roteiro guiado passo-a-passo, pré-requisitos, capturas de tela do portal,
alertas de exame DP-700 e opção de simulação local em todas as lições.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS_DIR = os.path.join(BASE_DIR, "lessons")
LABS_DIR = os.path.join(BASE_DIR, "labs")

LAB_DEFINITIONS = {
    "0001-data-engineering-foundations-oltp-olap-fabric.html": {
        "folder": "0001-oltp-olap-and-smoothing",
        "title": "Exercício Prático: Provisionar Capacidade Fabric e Explorar Lakehouse vs Warehouse",
        "duration": "~25 minutos",
        "domain": "Domínio 1",
        "scenario": "A Contoso Global Retail está migrando sua arquitetura legado para o Microsoft Fabric. Como Engenheiro de Dados, você deve criar um Workspace sob uma capacidade Fabric, provisionar um Lakehouse para ingestão de dados em arquivos Delta e um Data Warehouse para relatórios analíticos corporativos com transações T-SQL ACID.",
        "tasks": [
            {
                "num": 1,
                "title": "Acessar o Portal e Criar o Workspace com Capacidade Fabric",
                "steps": [
                    "Acesse o portal do <a href='https://app.fabric.microsoft.com/' target='_blank' rel='noopener noreferrer'>Microsoft Fabric</a> e efetue login.",
                    "No canto inferior esquerdo, clique no ícone de <strong>Engenharia de Dados (Data Engineering)</strong>.",
                    "No menu lateral, clique em <strong>Workspaces</strong> e crie um novo workspace nomeado <code>DP700_Foundations_Lab</code>.",
                    "Nas configurações avançadas, assegure-se de vincular o workspace a uma <strong>Capacidade Fabric (Trial ou F-SKU)</strong>.",
                    "Clique em <strong>Aplicar</strong>."
                ],
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/new-workspace",
                    "svg": "../assets/images/fabric-ui-01-create-lakehouse.svg",
                    "caption": "Configurando workspace vinculado à capacidade Fabric e selecionando a experiência de Engenharia de Dados."
                }
            },
            {
                "num": 2,
                "title": "Criar o Lakehouse e Ingerir Arquivos Brutos via PySpark",
                "steps": [
                    "Dentro do workspace, clique em <strong>+ Novo item</strong> e selecione <strong>Lakehouse</strong>.",
                    "Nomeie como <code>lh_retail_raw</code> e clique em <strong>Criar</strong>.",
                    "Clique em <strong>Abrir notebook</strong> &gt; <strong>Novo notebook</strong>.",
                    "Execute o código PySpark abaixo para carregar dados brutos e salvá-los como tabela Delta:"
                ],
                "code": {
                    "lang": "PYTHON (PYSPARK) — LAKEHOUSE NOTEBOOK",
                    "content": """# Ingestão de dados brutos de vendas no Lakehouse
dados = [
    (1, "Notebook Gamer", 4500.00, "Sul"),
    (2, "Monitor UltraWide", 1800.00, "Sudeste"),
    (3, "Teclado Mecânico", 350.00, "Sul")
]
colunas = ["ProdutoID", "NomeProduto", "Preco", "Regiao"]

df = spark.createDataFrame(dados, colunas)
df.write.format("delta").mode("overwrite").saveAsTable("raw_produtos")
print("✅ Tabela raw_produtos gravada com sucesso em Delta Lake!")"""
                }
            },
            {
                "num": 3,
                "title": "Criar o Data Warehouse e Executar Transações T-SQL ACID",
                "steps": [
                    "Retorne ao workspace, clique em <strong>+ Novo item</strong> e selecione <strong>Data Warehouse</strong>.",
                    "Nomeie como <code>dw_retail_corporate</code> e clique em <strong>Criar</strong>.",
                    "Na barra de ferramentas, clique em <strong>Nova consulta SQL</strong> e execute o script T-SQL com suporte a transações multi-tabela:"
                ],
                "code": {
                    "lang": "T-SQL — FABRIC DATA WAREHOUSE",
                    "content": """-- Criação de tabela relacional com integridade no Warehouse
CREATE TABLE dbo.DimProduto (
    ProdutoID INT NOT NULL,
    NomeProduto VARCHAR(100) NOT NULL,
    Preco DECIMAL(10,2) NOT NULL,
    Regiao VARCHAR(50) NOT NULL
);

-- Transação ACID atômica
BEGIN TRANSACTION;
INSERT INTO dbo.DimProduto (ProdutoID, NomeProduto, Preco, Regiao)
VALUES (1, 'Notebook Gamer', 4500.00, 'Sul'),
       (2, 'Monitor UltraWide', 1800.00, 'Sudeste');
COMMIT TRANSACTION;

SELECT Regiao, SUM(Preco) AS TotalVendas FROM dbo.DimProduto GROUP BY Regiao;"""
                },
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/dw_retail_corporate/editor",
                    "svg": "../assets/images/fabric-ui-04-data-warehouse-editor.svg",
                    "caption": "Executando consultas transacionais T-SQL e comandos DDL/DML nativos no Fabric Data Warehouse."
                }
            }
        ],
        "exam_note": "No exame DP-700, lembre-se: o Lakehouse é focado em arquivos e manipulação de Big Data com Spark (possuindo SQL Endpoint somente leitura), enquanto o Data Warehouse oferece suporte transacional completo DDL/DML, multi-table transactions ACID e segurança avançada (RLS/CLS)."
    },

    "0003-dimensional-modeling-and-three-languages-sql-spark-kql.html": {
        "folder": "0003-dimensional-modeling-three-languages",
        "title": "Exercício Prático: Modelagem Dimensional em Star Schema com T-SQL, PySpark e KQL",
        "duration": "~30 minutos",
        "domain": "Domínio 1 & 2",
        "scenario": "A Fabrikam precisa estruturar um modelo dimensional em Star Schema (Tabela Fato e Dimensões) e comparar a performance e custo de consulta analítica entre as três linguagens fundamentais do Fabric: T-SQL, PySpark e KQL.",
        "tasks": [
            {
                "num": 1,
                "title": "Modelar o Star Schema no Fabric Warehouse via T-SQL",
                "steps": [
                    "No Fabric Data Warehouse <code>dw_sales_enterprise</code>, clique em <strong>Nova consulta SQL</strong>.",
                    "Execute o script de criação da Fato e Dimensões com chaves substitutas (Surrogate Keys):"
                ],
                "code": {
                    "lang": "T-SQL — STAR SCHEMA",
                    "content": """-- 1. Criação das Dimensões
CREATE TABLE dbo.DimCliente (
    ClienteSK INT IDENTITY(1,1) NOT NULL,
    ClienteBK VARCHAR(50) NOT NULL,
    NomeCliente VARCHAR(100) NOT NULL,
    Regiao VARCHAR(50) NOT NULL
);

-- 2. Tabela Fato
CREATE TABLE dbo.FactVendas (
    VendaID BIGINT NOT NULL,
    ClienteSK INT NOT NULL,
    DataKey INT NOT NULL,
    ValorTotal DECIMAL(12,2) NOT NULL,
    Quantidade INT NOT NULL
);"""
                },
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/dw_sales_enterprise/star-schema",
                    "svg": "../assets/images/fabric-ui-04-data-warehouse-editor.svg",
                    "caption": "Editor T-SQL do Warehouse com o modelo dimensional em Star Schema e integridade de chaves."
                }
            },
            {
                "num": 2,
                "title": "Transformar Dados e Gerar Chaves no PySpark",
                "steps": [
                    "Abra o Notebook Spark vinculado ao Lakehouse.",
                    "Execute a célula PySpark gerando Surrogate Keys usando funções analíticas de janela (Window Functions):"
                ],
                "code": {
                    "lang": "PYTHON (PYSPARK) — NOTEBOOK",
                    "content": """from pyspark.sql.functions import monotonically_increasing_id, row_number
from pyspark.sql.window import Window

df_raw = spark.table("raw_clientes")
windowSpec = Window.orderBy("ClienteBK")
df_dim_cliente = df_raw.withColumn("ClienteSK", row_number().over(windowSpec))

df_dim_cliente.write.format("delta").mode("overwrite").saveAsTable("dim_cliente_gold")
print("✅ Dimensão com Surrogate Key gerada com sucesso!")"""
                }
            },
            {
                "num": 3,
                "title": "Consultar Telemetria com KQL no Eventhouse",
                "steps": [
                    "Acesse o Eventhouse <code>evh_iot_telemetry</code>.",
                    "Abra o KQL Queryset e execute uma consulta analítica de série temporal de alta frequência:"
                ],
                "code": {
                    "lang": "KQL — EVENTHOUSE QUERYSET",
                    "content": """RawTelemetry
| where Timestamp > ago(24h)
| summarize MediaTemperatura = avg(Temperature), Pico = max(Temperature) by bin(Timestamp, 15m), DeviceId
| top 5 by Pico desc"""
                },
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/evh_iot_telemetry/queryset",
                    "svg": "../assets/images/fabric-ui-08-eventhouse-kql-query.svg",
                    "caption": "KQL Queryset executando agregações de subsegundo sobre telemetria e séries temporais no Eventhouse."
                }
            }
        ],
        "exam_note": "Lembre-se para a prova: T-SQL é o motor padrão para Star Schema e joins relacionais; PySpark é ideal para transformações de dados semiestruturados e geração distribuída de chaves; KQL é o motor imbatível para séries temporais e telemetria de alta frequência."
    },

    "0004-onelake-capacities-smoothing-domains-spark-pools.html": {
        "folder": "0004-onelake-capacities-spark-pools",
        "title": "Exercício Prático: Gerenciar Capacidade OneLake, Starter Pools do Spark e Domínios",
        "duration": "~25 minutos",
        "domain": "Domínio 1",
        "scenario": "A corporação precisa estruturar a governança de múltiplos times (Vendas, RH e Logística), associando workspaces a Domínios do Fabric e configurando Starter Pools de inicialização rápida para Spark, sem estourar o limite de CUs.",
        "tasks": [
            {
                "num": 1,
                "title": "Configurar Domínios de Governança no Admin Portal",
                "steps": [
                    "Acesse o <strong>Portal de Administração (Admin Portal)</strong> do Fabric.",
                    "No menu lateral, selecione <strong>Domínios (Domains)</strong>.",
                    "Clique em <strong>+ Novo domínio</strong>, insira o nome <code>Vendas_Corporativo</code> e atribua o administrador.",
                    "Vincule os workspaces do departamento de vendas a este domínio para delegação descentralizada."
                ]
            },
            {
                "num": 2,
                "title": "Configurar Starter Pools e Custom Spark Pools",
                "steps": [
                    "Acesse as <strong>Configurações do Workspace</strong> &gt; <strong>Engenharia de Dados/Computação</strong>.",
                    "Ative a opção de <strong>Starter Pools</strong> para inicialização imediata (&lt; 10s).",
                    "Crie um Pool Personalizado com alocação máxima de 8 nós executores e parada automática após 15 minutos de inatividade."
                ]
            },
            {
                "num": 3,
                "title": "Analisar a Curva de Smoothing no Capacity Metrics App",
                "steps": [
                    "Abra o <strong>Microsoft Fabric Capacity Metrics App</strong>.",
                    "Analise a métrica de utilização da capacidade F64.",
                    "Identifique como picos instantâneos de Spark de 180% são normalizados pela janela de Smoothing de 24 horas, evitando throttling."
                ],
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/admin/capacity-metrics",
                    "svg": "../assets/images/fabric-ui-12-capacity-metrics-app.svg",
                    "caption": "Métricas da capacidade Fabric exibindo amortização de picos de carga pelo algoritmo de Smoothing de 24 horas."
                }
            }
        ],
        "exam_note": "Atenção DP-700: Os Starter Pools são instâncias pré-aquecidas gerenciadas pela Microsoft que entram em execução quase instantaneamente; trabalhos interativos sofrem amortização de 5 minutos, enquanto operações em segundo plano (como pipelines agendados) são suavizadas em uma janela contínua de 24 horas."
    },

    "0005-architectural-decision-guide-lakehouse-warehouse-eventhouse.html": {
        "folder": "0005-architectural-decision-guide",
        "title": "Exercício Prático: Matriz Decisória - Lakehouse vs Warehouse vs Eventhouse",
        "duration": "~25 minutos",
        "domain": "Domínio 1",
        "scenario": "Construir uma prova de conceito com os três tipos de armazenamento analítico no Fabric, testando qual motor deve ser recomendado para cada caso de uso corporativo.",
        "tasks": [
            {
                "num": 1,
                "title": "Provisionar os Três Motores no Mesmo Workspace",
                "steps": [
                    "No workspace, crie um item <strong>Lakehouse</strong> (<code>lh_telemetry_files</code>).",
                    "Crie um item <strong>Data Warehouse</strong> (<code>dw_financial_acid</code>).",
                    "Crie um item <strong>Eventhouse</strong> (<code>evh_sensor_live</code>)."
                ],
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/workspace/new-items",
                    "svg": "../assets/images/fabric-ui-01-create-lakehouse.svg",
                    "caption": "Criando e organizando Lakehouses, Warehouses e Eventhouses no mesmo ambiente corporativo OneLake."
                }
            },
            {
                "num": 2,
                "title": "Comparar Capacidades de Escrita e Latência",
                "steps": [
                    "No Warehouse, execute comandos relacionais transacionais com <code>BEGIN TRANSACTION</code> e <code>MERGE</code>.",
                    "No Lakehouse, execute transformações em arquivos Parquet com Spark Notebook.",
                    "No Eventhouse, ingira streaming em alta velocidade e execute consultas KQL de latência de milissegundos."
                ],
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/workspace/t-sql-vs-kql",
                    "svg": "../assets/images/fabric-ui-04-data-warehouse-editor.svg",
                    "caption": "Comparativo operacional de execução entre T-SQL relacional no Warehouse e KQL no Eventhouse."
                }
            }
        ],
        "exam_note": "Decisão de Exame: Se o requisito exigir DDL/DML nativo, integridade transacional multi-tabela e RLS/CLS, escolha WAREHOUSE. Se exigir engenharia em Python/Scala com arquivos não estruturados, escolha LAKEHOUSE. Se exigir ingestão contínua de telemetria em tempo real e consultas temporais, escolha EVENTHOUSE."
    },

    "0006-shortcuts-and-mirroring-zero-copy-integration.html": {
        "folder": "0006-shortcuts-and-mirroring",
        "title": "Exercício Prático: Criar Atalhos (Shortcuts) no OneLake e Mirroring Zero-Copy",
        "duration": "~25 minutos",
        "domain": "Domínio 1 & 2",
        "scenario": "A empresa possui dados legados no Amazon S3 e no Azure Data Lake Storage Gen2. Em vez de criar pipelines caros de cópia, você criará atalhos (Shortcuts) no OneLake permitindo consultas diretas em subsegundo.",
        "tasks": [
            {
                "num": 1,
                "title": "Criar um Atalho (Shortcut) para o Amazon S3",
                "steps": [
                    "Abra o Lakehouse <code>lh_global_enterprise</code>.",
                    "Passe o mouse sobre a pasta <strong>Tables</strong>, clique nos três pontos (<strong>...</strong>) e selecione <strong>Novo atalho (New shortcut)</strong>.",
                    "Selecione o provedor <strong>Amazon S3</strong>.",
                    "Preencha o caminho do bucket (ex: <code>s3://corp-telemetry-data/</code>) e as credenciais de acesso.",
                    "Nomeie o atalho como <code>s3_telemetria_shortcut</code> e clique em <strong>Criar</strong>."
                ],
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/lh_global_enterprise/shortcuts",
                    "svg": "../assets/images/fabric-ui-05-shortcuts-modal.svg",
                    "caption": "Assistente de criação de atalhos (Shortcuts) para fontes internas OneLake, ADLS Gen2 e Amazon S3."
                }
            },
            {
                "num": 2,
                "title": "Consultar o Atalho Diretamente sem Duplicação",
                "steps": [
                    "Abra o Notebook Spark vinculado ao Lakehouse.",
                    "Leia os dados da tabela criada pelo atalho exatamente como se fosse uma tabela local:",
                    "<code>df_s3 = spark.table('s3_telemetria_shortcut'); display(df_s3.limit(10))</code>",
                    "Observe que o OneLake busca os dados sob demanda sem transferir armazenamento permanente."
                ]
            }
        ],
        "exam_note": "Pegadinha de Exame: Os atalhos não copiam arquivos físicos; eles apenas criam metadados apontando para a fonte externa. Se a credencial na AWS/Azure expirar ou os dados forem deletados no bucket de origem, o atalho no Fabric apresentará falha de leitura."
    },

    "0007-orchestration-pipelines-dataflows-dag.html": {
        "folder": "0007-orchestration-pipelines-dataflows-dag",
        "title": "Exercício Prático: Orquestrar Pipelines de Dados com Atividades DAG e Dataflows Gen2",
        "duration": "~30 minutos",
        "domain": "Domínio 2",
        "scenario": "Construir um pipeline de dados corporativo no Data Factory encadeando uma atividade de extração rápida (Fast Copy), um Dataflow Gen2 de higienização e um Notebook Spark final para alimentar a camada Gold.",
        "tasks": [
            {
                "num": 1,
                "title": "Criar o Pipeline de Dados no Data Factory",
                "steps": [
                    "No workspace, selecione <strong>+ Novo item</strong> &gt; <strong>Data pipeline</strong>.",
                    "Nomeie como <code>pl_daily_enterprise_etl</code> e clique em <strong>Criar</strong>.",
                    "No menu de atividades superior, adicione uma atividade <strong>Copy data</strong>.",
                    "Adicione uma atividade <strong>Dataflow Gen2</strong> e conecte a seta verde (Sucesso) da Copy data nela.",
                    "Adicione uma atividade <strong>Notebook</strong> conectada à saída com sucesso do Dataflow Gen2."
                ],
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/pipelines/pl_daily_enterprise_etl",
                    "svg": "../assets/images/fabric-ui-06-data-factory-pipeline.svg",
                    "caption": "Canvas visual de orquestração no Data Factory montando o Grafo Acíclico Direcionado (DAG)."
                }
            },
            {
                "num": 2,
                "title": "Depurar e Monitorar a Execução das Atividades",
                "steps": [
                    "Na barra de ferramentas, clique em <strong>▶ Depurar (Debug)</strong>.",
                    "Acompanhe na aba inferior <strong>Saída (Output)</strong> o status de cada nó da DAG, taxa de transferência e tempo de execução.",
                    "Configure um gatilho de agendamento (Schedule Trigger) diário para às 02:00 AM UTC."
                ]
            }
        ],
        "exam_note": "No exame DP-700: Fast Copy acelera cargas maciças de dados para o Lakehouse; Dataflows Gen2 trazem o poder do Power Query M com suporte a transações e staging em Lakehouse; e Pipelines fornecem controle de fluxo com If Condition, ForEach e tratamento de erros."
    },

    "0008-incremental-loading-watermark-scd.html": {
        "folder": "0008-incremental-loading-watermark-scd",
        "title": "Exercício Prático: Carga Incremental com Coluna Watermark e SCD Tipo 2",
        "duration": "~30 minutos",
        "domain": "Domínio 2",
        "scenario": "Implementar um pipeline eficiente de carga delta diária utilizando coluna de corte temporal (Watermark) e processar alterações cadastrais mantendo histórico via Slowly Changing Dimension (SCD Tipo 2).",
        "tasks": [
            {
                "num": 1,
                "title": "Configurar Tabela de Controle de Watermark",
                "steps": [
                    "No Fabric Warehouse, crie a tabela de controle com o registro da última data processada:",
                    "<code>CREATE TABLE dbo.WatermarkControl (TableName VARCHAR(50), LastWatermark DATETIME2);</code>",
                    "Insira o marco inicial: <code>INSERT INTO dbo.WatermarkControl VALUES ('Clientes', '2026-01-01 00:00:00');</code>"
                ]
            },
            {
                "num": 2,
                "title": "Executar o MERGE de SCD Tipo 2 no Notebook Spark",
                "steps": [
                    "No Notebook Spark, execute o código de SCD Tipo 2 para fechar os registros antigos e inserir a nova versão ativa:",
                    "Use o método <code>df.write.format('delta')</code> ou comandos SQL <code>MERGE INTO DimCliente ...</code>",
                    "Atualize a tabela de controle com o novo timestamp de corte."
                ],
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/dw/scd2-merge",
                    "svg": "../assets/images/fabric-ui-04-data-warehouse-editor.svg",
                    "caption": "Execução de comandos atômicos MERGE para atualização de SCD Tipo 2 mantendo histórico temporal."
                }
            }
        ],
        "exam_note": "Atenção para o exame: O padrão SCD Tipo 1 apenas sobrescreve registros sem salvar histórico; o SCD Tipo 2 cria uma nova linha com campos de vigência (DataInicio, DataFim e FlagAtivo = 1/0) para preservar a rastreabilidade histórica completa."
    },

    "0009-batch-transformations-sql-spark-clones.html": {
        "folder": "0009-batch-transformations-sql-spark-clones",
        "title": "Exercício Prático: Transformações em Lote com PySpark, Views T-SQL e Table Clones",
        "duration": "~25 minutos",
        "domain": "Domínio 2",
        "scenario": "Executar rotinas analíticas em lote no Fabric e aplicar cópias de zero-custo via comandos CLONE TABLE no Warehouse para testar atualizações destrutivas em ambiente isolado sem duplicar dados.",
        "tasks": [
            {
                "num": 1,
                "title": "Criar um Clone de Tabela (Zero-Copy Clone)",
                "steps": [
                    "No Fabric Warehouse, abra uma nova consulta SQL.",
                    "Execute o comando: <code>CREATE TABLE dbo.FactVendas_Homolog AS CLONE dbo.FactVendas;</code>",
                    "Observe que o clone é criado em subsegundo, apontando para os mesmos arquivos físicos Delta Parquet no OneLake."
                ],
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/dw/clone-table",
                    "svg": "../assets/images/fabric-ui-04-data-warehouse-editor.svg",
                    "caption": "Criação de Clone de Tabela (Zero-Copy) para homologação rápida de código analítico."
                }
            },
            {
                "num": 2,
                "title": "Testar Alterações Isoladas no Clone",
                "steps": [
                    "Execute alterações pontuais ou deletes de teste na tabela clonada: <code>DELETE FROM dbo.FactVendas_Homolog WHERE Ano = 2024;</code>",
                    "Consulte a tabela original <code>dbo.FactVendas</code> e confirme que ela continua íntegra e sem modificações."
                ]
            }
        ],
        "exam_note": "Conceito de Prova: No Microsoft Fabric, o comando CLONE TABLE opera como Shallow Clone (cópia lógica instantânea de metadados). Apenas quando o clone sofre escrita é que novos arquivos de dados são gerados isoladamente."
    },

    "0010-streaming-eventstreams-spark-windows.html": {
        "folder": "0010-streaming-eventstreams-spark-windows",
        "title": "Exercício Prático: Ingestão de Streaming em Tempo Real com Eventstreams e Janelas Spark",
        "duration": "~30 minutos",
        "domain": "Domínio 2",
        "scenario": "Capturar fluxos de telemetria IoT de turbinas em tempo real, aplicar filtros de anomalia térmica e agregação temporal usando janelas de streaming antes de persistir no OneLake.",
        "tasks": [
            {
                "num": 1,
                "title": "Criar o Eventstream no Microsoft Fabric",
                "steps": [
                    "No workspace, selecione <strong>+ Novo item</strong> &gt; <strong>Eventstream</strong>.",
                    "Nomeie como <code>es_iot_telemetry_stream</code> e abra o designer visual.",
                    "Adicione uma <strong>Nova fonte (New source)</strong> selecionando <em>Azure Event Hub</em> ou <em>Custom endpoint</em>.",
                    "Adicione um operador de transformação para filtrar <code>Temperature &gt; 80</code> e agregar por janela Tumbling de 1 minuto."
                ],
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/eventstreams/es_iot_telemetry_stream",
                    "svg": "../assets/images/fabric-ui-07-realtime-eventstream.svg",
                    "caption": "Designer visual do Eventstream conectando fontes de streaming, filtros de anomalia e múltiplos destinos."
                }
            },
            {
                "num": 2,
                "title": "Roteamento Duplo: Eventhouse e Lakehouse Bronze",
                "steps": [
                    "Conecte uma saída para o <strong>Eventhouse</strong> para permitir alertas imediatos no dashboard.",
                    "Conecte outra saída para a tabela Delta do <strong>Lakehouse</strong> para persistência de longo prazo.",
                    "Abra a aba de Pré-visualização de Dados e veja os eventos chegando em tempo real."
                ]
            }
        ],
        "exam_note": "Tipos de Janelas de Streaming no DP-700: Tumbling (janelas contíguas sem sobreposição), Sliding (janelas com sobreposição contínua) e Session (janelas abertas por atividade e fechadas por período de inatividade/timeout)."
    },

    "0011-kql-eventhouse-update-policies-materialized-views.html": {
        "folder": "0011-kql-eventhouse-update-policies",
        "title": "Exercício Prático: Eventhouse KQL - Update Policies e Materialized Views",
        "duration": "~25 minutos",
        "domain": "Domínio 2",
        "scenario": "Criar um banco KQL no Eventhouse que recebe eventos brutos em alta frequência e aplica Update Policies atômicas para pré-agregar métricas sem a necessidade de rotinas periódicas de ETL.",
        "tasks": [
            {
                "num": 1,
                "title": "Criar Tabelas de Origem e Destino no KQL Database",
                "steps": [
                    "Abra o KQL Database <code>evh_iot_telemetry</code>.",
                    "Crie a tabela de dados brutos: <code>.create table RawTelemetry (Timestamp: datetime, DeviceId: string, Temperature: real);</code>",
                    "Crie a tabela agregada de destino: <code>.create table AggregatedSensors1m (Timestamp: datetime, DeviceId: string, AvgTemp: real, EventCount: long);</code>"
                ]
            },
            {
                "num": 2,
                "title": "Definir a Função e a Política de Atualização (Update Policy)",
                "steps": [
                    "Crie a função de agregação que processa novos lotes de dados:",
                    "<code>.create function TransformTelemetry() { RawTelemetry | summarize AvgTemp=avg(Temperature), EventCount=count() by bin(Timestamp, 1m), DeviceId }</code>",
                    "Ative a política de atualização na tabela de destino vinculando à função criada."
                ],
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/eventhouse/kql-editor",
                    "svg": "../assets/images/fabric-ui-08-eventhouse-kql-query.svg",
                    "caption": "KQL Database Explorer com tabela de telemetria bruta e Update Policy de agregação automática."
                }
            }
        ],
        "exam_note": "Importante para o exame: As Update Policies no KQL agem como gatilhos transacionais automáticos durante a ingestão do lote, transformando e gravando dados na tabela de destino sem custos de computação de agendamento em lote."
    },

    "0012-security-governance-rls-cls-direct-lake-fallback.html": {
        "folder": "0012-security-governance-rls-cls-fallback",
        "title": "Exercício Prático: Implementar RLS, CLS e Mitigar Direct Lake Fallback",
        "duration": "~30 minutos",
        "domain": "Domínio 3",
        "scenario": "Implementar segurança granular com Row-Level Security (RLS) e Column-Level Security (CLS) no SQL Analytics Endpoint e compreender o comportamento de Direct Lake Fallback no Power BI.",
        "tasks": [
            {
                "num": 1,
                "title": "Criar a Função Predicado e a Política de Segurança (RLS)",
                "steps": [
                    "No SQL Analytics Endpoint ou Warehouse, abra uma consulta SQL.",
                    "Crie a função inline table-valued que valida o usuário conectado via <code>USER_NAME()</code>.",
                    "Aplique a <code>SECURITY POLICY</code> com <code>FILTER PREDICATE</code> sobre a tabela de vendas."
                ],
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/security/rls-policy",
                    "svg": "../assets/images/fabric-ui-09-security-rls-governance.svg",
                    "caption": "Definição de Security Policy em T-SQL e diagnóstico visual do efeito de Direct Lake Fallback."
                }
            },
            {
                "num": 2,
                "title": "Diagnosticar o Fallback de Direct Lake para DirectQuery",
                "steps": [
                    "Conecte um relatório do Power BI no Modo Direct Lake.",
                    "Abra o Performance Analyzer e observe que a consulta sofre Fallback para DirectQuery porque o motor VertiPaq não processa RLS nativo do SQL Endpoint.",
                    "Compreenda a recomendação do Fabric: para manter Direct Lake puro com subsegundo, configure o RLS diretamente no Modelo Semântico do Power BI."
                ]
            }
        ],
        "exam_note": "Regra Fundamental do Exame DP-700: RLS ou CLS habilitados na camada SQL do Fabric provocam Fallback silencioso de Direct Lake para DirectQuery no Power BI. Para manter o modo Direct Lake de memória pura, implemente as regras de segurança no próprio Modelo Semântico."
    },

    "0013-cicd-git-deployment-pipelines-sqlproj.html": {
        "folder": "0013-cicd-git-deployment-pipelines",
        "title": "Exercício Prático: CI/CD com Integração Git e Deployment Pipelines",
        "duration": "~30 minutos",
        "domain": "Domínio 3",
        "scenario": "Configurar o ciclo de vida de desenvolvimento de software (DevOps) no Fabric, conectando workspaces ao Git e utilizando Deployment Pipelines de 3 estágios (Dev &gt; Test &gt; Prod) com regras de parâmetros de conexão.",
        "tasks": [
            {
                "num": 1,
                "title": "Vincular o Workspace ao Repositório Git",
                "steps": [
                    "Nas configurações do Workspace, clique em <strong>Integração com Git (Git integration)</strong>.",
                    "Conecte à sua conta do Azure DevOps ou GitHub, selecione o repositório e a branch <code>dev</code>.",
                    "Observe a barra de status de sincronização indicando alterações pendentes de commit."
                ]
            },
            {
                "num": 2,
                "title": "Configurar o Pipeline de Implantação de 3 Estágios",
                "steps": [
                    "Crie um novo <strong>Deployment Pipeline</strong>.",
                    "Atribua o workspace de Desenvolvimento ao estágio 1 (Dev), Teste ao estágio 2 (Test) e Produção ao estágio 3 (Prod).",
                    "Configure <strong>Deployment Rules</strong> para substituir conexões de banco de dados e nomes de Lakehouses entre os estágios.",
                    "Execute a promoção de artefatos de Dev para Test com validação automática."
                ],
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/deployment-pipelines/cicd",
                    "svg": "../assets/images/fabric-ui-10-git-deployment-pipeline.svg",
                    "caption": "Pipeline de implantação com 3 estágios (Desenvolvimento, Teste e Produção) e integração com Git."
                }
            }
        ],
        "exam_note": "Atenção para o exame: Deployment Pipelines facilitam a transição entre ambientes; as Regras de Parâmetros garantem que o código em Produção aponte automaticamente para o Lakehouse de Produção sem necessidade de editar manualmente os scripts."
    },

    "0014-performance-vorder-liquid-clustering-tuning.html": {
        "folder": "0014-performance-vorder-liquid-clustering",
        "title": "Exercício Prático: Otimização Extrema com V-Order, Liquid Clustering e Compaction",
        "duration": "~25 minutos",
        "domain": "Domínio 3",
        "scenario": "Otimizar uma tabela analítica de bilhões de registros que sofria degradação de performance por sobrecarga de arquivos pequenos, aplicando Liquid Clustering (CLUSTER BY) e ordenação V-Order no OneLake.",
        "tasks": [
            {
                "num": 1,
                "title": "Criar Tabela com Liquid Clustering (Delta 3.0)",
                "steps": [
                    "No Notebook Spark, crie a tabela particionada logicamente via Liquid Clustering:",
                    "<code>df.write.format('delta').clusterBy('DataVenda', 'RegiaoId').saveAsTable('gold_telemetria_clustered')</code>",
                    "Observe que o Liquid Clustering elimina a proliferação excessiva de pastas físicas em disco."
                ]
            },
            {
                "num": 2,
                "title": "Executar Compactação e Avaliar Métricas de Data Skipping",
                "steps": [
                    "Execute o comando: <code>%%sql OPTIMIZE gold_telemetria_clustered;</code>",
                    "Analise a métrica de execução do Spark: veja que consultas com filtro em <code>RegiaoId</code> saltam mais de 95% dos arquivos lidos.",
                    "Comprove a aceleração de leitura em modo Direct Lake no Power BI."
                ],
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/performance/liquid-clustering",
                    "svg": "../assets/images/fabric-ui-11-liquid-clustering-vorder.svg",
                    "caption": "Métricas de aceleração por Liquid Clustering e V-Order exibindo redução de 98% na leitura de I/O de disco."
                }
            }
        ],
        "exam_note": "Conceito Chave do DP-700: O Liquid Clustering substitui o particionamento tradicional (Partition By) e o Z-Order. Ele permite alterar as colunas de clusterização sem a necessidade de reescrever toda a tabela histórica existente."
    },

    "0015-monitoring-hub-capacity-metrics-troubleshooting.html": {
        "folder": "0015-monitoring-capacity-metrics-dmvs",
        "title": "Exercício Prático: Monitoramento de Capacidade, Análise de CU e Solução de Gargalos",
        "duration": "~25 minutos",
        "domain": "Domínio 3",
        "scenario": "Auditar uma capacidade Fabric corporativa utilizando o Capacity Metrics App e o Monitoring Hub, identificando consultas de Spark e Warehouse que causaram consumo anormal de Capacity Units.",
        "tasks": [
            {
                "num": 1,
                "title": "Inspecionar Jobs Ativos no Monitoring Hub",
                "steps": [
                    "No menu de navegação lateral esquerdo, clique no ícone do <strong>Monitoring Hub</strong>.",
                    "Filtre os jobs das últimas 24 horas por Status (Falha / Em Andamento / Êxito) e Tipo de Item.",
                    "Inspecione a duração, usuário solicitante e logs detalhados de diagnóstico da execução."
                ]
            },
            {
                "num": 2,
                "title": "Diagnosticar Queima de CU no Capacity Metrics App",
                "steps": [
                    "Abra o <strong>Microsoft Fabric Capacity Metrics App</strong>.",
                    "Verifique o gráfico de consumo: analise a proporção entre operações interativas e operações em segundo plano.",
                    "Identifique se a capacidade entrou em estado de sobrecarga ou se o algoritmo de Smoothing absorveu com segurança o pico de processamento."
                ],
                "screenshot": {
                    "url": "https://app.fabric.microsoft.com/groups/monitoring/capacity-app",
                    "svg": "../assets/images/fabric-ui-12-capacity-metrics-app.svg",
                    "caption": "Análise de métricas no Capacity Metrics App identificando jobs ofensores e prevenindo Throttling da capacidade."
                }
            }
        ],
        "exam_note": "Regra Crítica para o Exame: Operações interativas (como consultas de relatórios do Power BI e notebooks executados em tempo real) amortizam em 5 minutos; operações em segundo plano (background jobs como pipelines agendados do Data Factory) amortizam em 24 horas."
    }
}


def build_mslearn_html(lab_def):
    folder = lab_def["folder"]
    title = lab_def["title"]
    duration = lab_def["duration"]
    domain = lab_def["domain"]
    scenario = lab_def["scenario"]
    tasks = lab_def["tasks"]
    exam_note = lab_def["exam_note"]

    html = f"""      <!-- SEÇÃO KINESTHETIC: LAB PRÁTICO ESTILO MICROSOFT LEARN -->
      <section id="bloco-pratica" style="margin-top: 3.5rem;">
        <div class="mslearn-lab-box">
          
          <!-- Cabeçalho do Exercício -->
          <div class="mslearn-header">
            <div class="mslearn-badge-row">
              <span class="mslearn-badge mslearn-badge-portal">🛠️ Microsoft Fabric Hands-on Lab</span>
              <span class="mslearn-badge mslearn-badge-duration">⏱️ {duration}</span>
              <span class="mslearn-badge mslearn-badge-role">👤 Engenheiro de Dados • {domain}</span>
              <span class="vark-badge badge-k" style="margin-left: auto;">K - Prática Guiada</span>
            </div>
            <h2 style="margin: 0.25rem 0 0.5rem 0; font-family: var(--font-display); color: var(--text-primary); font-size: 1.6rem;">
              {title}
            </h2>
            <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">
              Guia passo a passo para executar diretamente na plataforma em nuvem do <strong>Microsoft Fabric</strong> (ou em simulação local).
            </p>
          </div>

          <!-- Cenário de Negócio Oficial -->
          <div class="mslearn-scenario-card">
            <h4 style="margin: 0 0 0.5rem 0; color: var(--brand-blue); font-family: var(--font-display);">
              📋 Cenário do Laboratório
            </h4>
            <p style="margin: 0; font-size: 0.92rem; color: var(--text-primary); line-height: 1.55;">
              {scenario}
            </p>
          </div>

          <!-- Pré-requisitos -->
          <div class="mslearn-prereqs-card">
            <h4 style="margin: 0 0 0.4rem 0; color: #0078d4; font-family: var(--font-display);">
              🔑 Pré-requisitos para Execução no Portal
            </h4>
            <ul style="margin: 0; padding-left: 1.25rem; font-size: 0.9rem; color: var(--text-primary); line-height: 1.5;">
              <li>Navegador web moderno (Edge, Chrome ou Firefox).</li>
              <li>Acesso ao portal <a href="https://app.fabric.microsoft.com/" target="_blank" rel="noopener noreferrer" style="color: #0078d4; font-weight: 600; text-decoration: underline;">Microsoft Fabric (app.fabric.microsoft.com)</a>.</li>
              <li>Capacidade ativa do Fabric (licença <strong>Fabric Trial</strong> gratuita ou capacidade corporativa).</li>
              <li>Um Workspace configurado no modo de capacidade Fabric.</li>
            </ul>
          </div>
"""

    for task in tasks:
        num = task["num"]
        t_title = task["title"]
        steps = task["steps"]
        code = task.get("code")
        screenshot = task.get("screenshot")

        html += f"""
          <!-- Tarefa {num} -->
          <div class="mslearn-task-card">
            <div class="mslearn-task-header">
              <div class="mslearn-task-number">{num}</div>
              <h3 class="mslearn-task-title">{t_title}</h3>
            </div>
            <ol class="mslearn-step-list">
"""
        for step in steps:
            html += f"              <li>{step}</li>\n"
        html += "            </ol>\n"

        if code:
            c_lang = code["lang"]
            c_content = code["content"]
            html += f"""
            <div class="mslearn-code-header">
              <span>{c_lang}</span>
              <span>MICROSOFT FABRIC CODE EDITOR</span>
            </div>
            <pre class="mslearn-code-box"><code>{c_content}</code></pre>
"""

        if screenshot:
            s_url = screenshot["url"]
            s_svg = screenshot["svg"]
            s_caption = screenshot["caption"]
            html += f"""
            <!-- Captura de Tela da Tarefa {num} -->
            <div class="portal-screenshot-frame">
              <div class="portal-window-bar">
                <div class="portal-window-dots">
                  <span class="portal-window-dot dot-red"></span>
                  <span class="portal-window-dot dot-yellow"></span>
                  <span class="portal-window-dot dot-green"></span>
                </div>
                <div class="portal-address-bar">
                  🔒 {s_url}
                </div>
              </div>
              <img src="{s_svg}" alt="{t_title}" loading="lazy" />
              <div class="portal-screenshot-caption">
                📸 <strong>Captura do Portal:</strong> {s_caption}
              </div>
            </div>
"""

        html += "          </div>\n"

    # Alerta de exame
    html += f"""
          <!-- Alerta de Exame DP-700 -->
          <div class="mslearn-exam-note" style="margin-top: 1.5rem;">
            <strong>⚠️ Atenção para o Exame DP-700:</strong><br>
            {exam_note}
          </div>

          <!-- Fallback: Simulação Local Offline -->
          <div class="mslearn-local-box">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.6rem;">
              <h4 style="margin: 0; color: var(--brand-teal); font-family: var(--font-display);">
                💻 Opção Alternativa: Executar Simulação Local Offline no seu Terminal
              </h4>
              <span style="font-size: 0.8rem; background: var(--bg-surface-alt); padding: 3px 8px; border-radius: 6px; color: var(--text-secondary);">Sem necessidade de conta Fabric</span>
            </div>
            <p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 0.75rem;">
              Se você não possui uma assinatura ativa do Fabric no momento, criamos um simulador completo em Python no seu repositório local que reproduz a execução deste laboratório:
            </p>
            <pre><code style="font-family: var(--font-mono); font-size: 0.88rem; display: block; background: var(--bg-surface-alt); padding: 0.85rem 1rem; border-radius: 8px; border: 1px solid var(--border-color); overflow-x: auto;"># Execute este comando no terminal para reproduzir o lab:
./.venv/bin/python labs/{folder}/lab_simulation.py</code></pre>
            <div style="margin-top: 0.75rem; font-size: 0.85rem; color: var(--text-secondary);">
              📁 Diretório do laboratório prático local: <code>labs/{folder}/</code>
            </div>
          </div>

        </div>
      </section>"""

    return html


def update_lesson_file(filename, lab_def):
    filepath = os.path.join(LESSONS_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_section = build_mslearn_html(lab_def)

    # Localiza o bloco-pratica existente
    pattern = r'(<section id=["\']bloco-pratica["\'].*?</section>)'
    if not re.search(pattern, content, re.DOTALL):
        print(f"❌ Não foi possível encontrar #bloco-pratica em {filename}")
        return False

    updated_content = re.sub(pattern, new_section, content, flags=re.DOTALL)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"✅ Atualizado com sucesso: {filename}")
    return True


def create_lab_readme(lab_def):
    folder = lab_def["folder"]
    title = lab_def["title"]
    scenario = lab_def["scenario"]
    tasks = lab_def["tasks"]
    exam_note = lab_def["exam_note"]

    lab_dir = os.path.join(LABS_DIR, folder)
    os.makedirs(lab_dir, exist_ok=True)
    readme_path = os.path.join(lab_dir, "README.md")

    md = f"""# {title}

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Cenário de Negócio
{scenario}

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo do Laboratório
"""

    for task in tasks:
        num = task["num"]
        t_title = task["title"]
        steps = task["steps"]
        code = task.get("code")

        md += f"\n#### Tarefa {num}: {t_title}\n"
        for i, s in enumerate(steps, 1):
            clean_s = re.sub(r'<[^>]+>', '', s)
            md += f"{i}. {clean_s}\n"

        if code:
            md += f"\n```{code['lang'].split()[0].lower()}\n{code['content']}\n```\n"

    md += f"""
---

## ⚠️ Ponto Crítico para o Exame DP-700
{exam_note}

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/{folder}/lab_simulation.py
```
"""

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"📝 README.md criado: labs/{folder}/README.md")


def main():
    print("Iniciando atualização massiva de laboratórios para o padrão Microsoft Learn...")
    count = 0
    for filename, lab_def in LAB_DEFINITIONS.items():
        if update_lesson_file(filename, lab_def):
            create_lab_readme(lab_def)
            count += 1
    print(f"\n🎉 Concluído! {count} lições e laboratórios atualizados com sucesso.")


if __name__ == "__main__":
    main()


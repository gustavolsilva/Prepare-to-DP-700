# Exercício Prático: Carga Incremental com Coluna Watermark e SCD Tipo 2

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Cenário de Negócio
Implementar um pipeline eficiente de carga delta diária utilizando coluna de corte temporal (Watermark) e processar alterações cadastrais mantendo histórico via Slowly Changing Dimension (SCD Tipo 2).

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo do Laboratório

#### Tarefa 1: Configurar Tabela de Controle de Watermark
1. No Fabric Warehouse, crie a tabela de controle com o registro da última data processada:
2. CREATE TABLE dbo.WatermarkControl (TableName VARCHAR(50), LastWatermark DATETIME2);
3. Insira o marco inicial: INSERT INTO dbo.WatermarkControl VALUES ('Clientes', '2026-01-01 00:00:00');

#### Tarefa 2: Executar o MERGE de SCD Tipo 2 no Notebook Spark
1. No Notebook Spark, execute o código de SCD Tipo 2 para fechar os registros antigos e inserir a nova versão ativa:
2. Use o método df.write.format('delta') ou comandos SQL MERGE INTO DimCliente ...
3. Atualize a tabela de controle com o novo timestamp de corte.

---

## ⚠️ Ponto Crítico para o Exame DP-700
Atenção para o exame: O padrão SCD Tipo 1 apenas sobrescreve registros sem salvar histórico; o SCD Tipo 2 cria uma nova linha com campos de vigência (DataInicio, DataFim e FlagAtivo = 1/0) para preservar a rastreabilidade histórica completa.

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/0008-incremental-loading-watermark-scd/lab_simulation.py
```

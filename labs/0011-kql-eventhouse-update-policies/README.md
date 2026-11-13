# Exercício Prático: Eventhouse KQL - Update Policies e Materialized Views

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Cenário de Negócio
Criar um banco KQL no Eventhouse que recebe eventos brutos em alta frequência e aplica Update Policies atômicas para pré-agregar métricas sem a necessidade de rotinas periódicas de ETL.

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo do Laboratório

#### Tarefa 1: Criar Tabelas de Origem e Destino no KQL Database
1. Abra o KQL Database evh_iot_telemetry.
2. Crie a tabela de dados brutos: .create table RawTelemetry (Timestamp: datetime, DeviceId: string, Temperature: real);
3. Crie a tabela agregada de destino: .create table AggregatedSensors1m (Timestamp: datetime, DeviceId: string, AvgTemp: real, EventCount: long);

#### Tarefa 2: Definir a Função e a Política de Atualização (Update Policy)
1. Crie a função de agregação que processa novos lotes de dados:
2. .create function TransformTelemetry() { RawTelemetry | summarize AvgTemp=avg(Temperature), EventCount=count() by bin(Timestamp, 1m), DeviceId }
3. Ative a política de atualização na tabela de destino vinculando à função criada.

---

## ⚠️ Ponto Crítico para o Exame DP-700
Importante para o exame: As Update Policies no KQL agem como gatilhos transacionais automáticos durante a ingestão do lote, transformando e gravando dados na tabela de destino sem custos de computação de agendamento em lote.

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/0011-kql-eventhouse-update-policies/lab_simulation.py
```

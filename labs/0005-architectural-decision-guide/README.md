# Exercício Prático: Matriz Decisória - Lakehouse vs Warehouse vs Eventhouse

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Cenário de Negócio
Construir uma prova de conceito com os três tipos de armazenamento analítico no Fabric, testando qual motor deve ser recomendado para cada caso de uso corporativo.

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo do Laboratório

#### Tarefa 1: Provisionar os Três Motores no Mesmo Workspace
1. No workspace, crie um item Lakehouse (lh_telemetry_files).
2. Crie um item Data Warehouse (dw_financial_acid).
3. Crie um item Eventhouse (evh_sensor_live).

#### Tarefa 2: Comparar Capacidades de Escrita e Latência
1. No Warehouse, execute comandos relacionais transacionais com BEGIN TRANSACTION e MERGE.
2. No Lakehouse, execute transformações em arquivos Parquet com Spark Notebook.
3. No Eventhouse, ingira streaming em alta velocidade e execute consultas KQL de latência de milissegundos.

---

## ⚠️ Ponto Crítico para o Exame DP-700
Decisão de Exame: Se o requisito exigir DDL/DML nativo, integridade transacional multi-tabela e RLS/CLS, escolha WAREHOUSE. Se exigir engenharia em Python/Scala com arquivos não estruturados, escolha LAKEHOUSE. Se exigir ingestão contínua de telemetria em tempo real e consultas temporais, escolha EVENTHOUSE.

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/0005-architectural-decision-guide/lab_simulation.py
```

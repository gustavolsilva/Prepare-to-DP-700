# Exercício Prático: Orquestrar Pipelines de Dados com Atividades DAG e Dataflows Gen2

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Cenário de Negócio
Construir um pipeline de dados corporativo no Data Factory encadeando uma atividade de extração rápida (Fast Copy), um Dataflow Gen2 de higienização e um Notebook Spark final para alimentar a camada Gold.

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo do Laboratório

#### Tarefa 1: Criar o Pipeline de Dados no Data Factory
1. No workspace, selecione + Novo item &gt; Data pipeline.
2. Nomeie como pl_daily_enterprise_etl e clique em Criar.
3. No menu de atividades superior, adicione uma atividade Copy data.
4. Adicione uma atividade Dataflow Gen2 e conecte a seta verde (Sucesso) da Copy data nela.
5. Adicione uma atividade Notebook conectada à saída com sucesso do Dataflow Gen2.

#### Tarefa 2: Depurar e Monitorar a Execução das Atividades
1. Na barra de ferramentas, clique em ▶ Depurar (Debug).
2. Acompanhe na aba inferior Saída (Output) o status de cada nó da DAG, taxa de transferência e tempo de execução.
3. Configure um gatilho de agendamento (Schedule Trigger) diário para às 02:00 AM UTC.

---

## ⚠️ Ponto Crítico para o Exame DP-700
No exame DP-700: Fast Copy acelera cargas maciças de dados para o Lakehouse; Dataflows Gen2 trazem o poder do Power Query M com suporte a transações e staging em Lakehouse; e Pipelines fornecem controle de fluxo com If Condition, ForEach e tratamento de erros.

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/0007-orchestration-pipelines-dataflows-dag/lab_simulation.py
```

# Exercício Prático: Monitoramento de Capacidade, Análise de CU e Solução de Gargalos

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Cenário de Negócio
Auditar uma capacidade Fabric corporativa utilizando o Capacity Metrics App e o Monitoring Hub, identificando consultas de Spark e Warehouse que causaram consumo anormal de Capacity Units.

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo do Laboratório

#### Tarefa 1: Inspecionar Jobs Ativos no Monitoring Hub
1. No menu de navegação lateral esquerdo, clique no ícone do Monitoring Hub.
2. Filtre os jobs das últimas 24 horas por Status (Falha / Em Andamento / Êxito) e Tipo de Item.
3. Inspecione a duração, usuário solicitante e logs detalhados de diagnóstico da execução.

#### Tarefa 2: Diagnosticar Queima de CU no Capacity Metrics App
1. Abra o Microsoft Fabric Capacity Metrics App.
2. Verifique o gráfico de consumo: analise a proporção entre operações interativas e operações em segundo plano.
3. Identifique se a capacidade entrou em estado de sobrecarga ou se o algoritmo de Smoothing absorveu com segurança o pico de processamento.

---

## ⚠️ Ponto Crítico para o Exame DP-700
Regra Crítica para o Exame: Operações interativas (como consultas de relatórios do Power BI e notebooks executados em tempo real) amortizam em 5 minutos; operações em segundo plano (background jobs como pipelines agendados do Data Factory) amortizam em 24 horas.

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/0015-monitoring-capacity-metrics-dmvs/lab_simulation.py
```

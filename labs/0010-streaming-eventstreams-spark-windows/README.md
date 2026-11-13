# Exercício Prático: Ingestão de Streaming em Tempo Real com Eventstreams e Janelas Spark

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Cenário de Negócio
Capturar fluxos de telemetria IoT de turbinas em tempo real, aplicar filtros de anomalia térmica e agregação temporal usando janelas de streaming antes de persistir no OneLake.

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo do Laboratório

#### Tarefa 1: Criar o Eventstream no Microsoft Fabric
1. No workspace, selecione + Novo item &gt; Eventstream.
2. Nomeie como es_iot_telemetry_stream e abra o designer visual.
3. Adicione uma Nova fonte (New source) selecionando Azure Event Hub ou Custom endpoint.
4. Adicione um operador de transformação para filtrar Temperature &gt; 80 e agregar por janela Tumbling de 1 minuto.

#### Tarefa 2: Roteamento Duplo: Eventhouse e Lakehouse Bronze
1. Conecte uma saída para o Eventhouse para permitir alertas imediatos no dashboard.
2. Conecte outra saída para a tabela Delta do Lakehouse para persistência de longo prazo.
3. Abra a aba de Pré-visualização de Dados e veja os eventos chegando em tempo real.

---

## ⚠️ Ponto Crítico para o Exame DP-700
Tipos de Janelas de Streaming no DP-700: Tumbling (janelas contíguas sem sobreposição), Sliding (janelas com sobreposição contínua) e Session (janelas abertas por atividade e fechadas por período de inatividade/timeout).

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/0010-streaming-eventstreams-spark-windows/lab_simulation.py
```

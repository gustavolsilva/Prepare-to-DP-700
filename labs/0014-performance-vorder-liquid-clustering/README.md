# Exercício Prático: Otimização Extrema com V-Order, Liquid Clustering e Compaction

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Cenário de Negócio
Otimizar uma tabela analítica de bilhões de registros que sofria degradação de performance por sobrecarga de arquivos pequenos, aplicando Liquid Clustering (CLUSTER BY) e ordenação V-Order no OneLake.

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo do Laboratório

#### Tarefa 1: Criar Tabela com Liquid Clustering (Delta 3.0)
1. No Notebook Spark, crie a tabela particionada logicamente via Liquid Clustering:
2. df.write.format('delta').clusterBy('DataVenda', 'RegiaoId').saveAsTable('gold_telemetria_clustered')
3. Observe que o Liquid Clustering elimina a proliferação excessiva de pastas físicas em disco.

#### Tarefa 2: Executar Compactação e Avaliar Métricas de Data Skipping
1. Execute o comando: %%sql OPTIMIZE gold_telemetria_clustered;
2. Analise a métrica de execução do Spark: veja que consultas com filtro em RegiaoId saltam mais de 95% dos arquivos lidos.
3. Comprove a aceleração de leitura em modo Direct Lake no Power BI.

---

## ⚠️ Ponto Crítico para o Exame DP-700
Conceito Chave do DP-700: O Liquid Clustering substitui o particionamento tradicional (Partition By) e o Z-Order. Ele permite alterar as colunas de clusterização sem a necessidade de reescrever toda a tabela histórica existente.

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/0014-performance-vorder-liquid-clustering/lab_simulation.py
```

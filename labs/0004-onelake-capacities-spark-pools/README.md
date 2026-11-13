# Exercício Prático: Gerenciar Capacidade OneLake, Starter Pools do Spark e Domínios

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Cenário de Negócio
A corporação precisa estruturar a governança de múltiplos times (Vendas, RH e Logística), associando workspaces a Domínios do Fabric e configurando Starter Pools de inicialização rápida para Spark, sem estourar o limite de CUs.

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo do Laboratório

#### Tarefa 1: Configurar Domínios de Governança no Admin Portal
1. Acesse o Portal de Administração (Admin Portal) do Fabric.
2. No menu lateral, selecione Domínios (Domains).
3. Clique em + Novo domínio, insira o nome Vendas_Corporativo e atribua o administrador.
4. Vincule os workspaces do departamento de vendas a este domínio para delegação descentralizada.

#### Tarefa 2: Configurar Starter Pools e Custom Spark Pools
1. Acesse as Configurações do Workspace &gt; Engenharia de Dados/Computação.
2. Ative a opção de Starter Pools para inicialização imediata (&lt; 10s).
3. Crie um Pool Personalizado com alocação máxima de 8 nós executores e parada automática após 15 minutos de inatividade.

#### Tarefa 3: Analisar a Curva de Smoothing no Capacity Metrics App
1. Abra o Microsoft Fabric Capacity Metrics App.
2. Analise a métrica de utilização da capacidade F64.
3. Identifique como picos instantâneos de Spark de 180% são normalizados pela janela de Smoothing de 24 horas, evitando throttling.

---

## ⚠️ Ponto Crítico para o Exame DP-700
Atenção DP-700: Os Starter Pools são instâncias pré-aquecidas gerenciadas pela Microsoft que entram em execução quase instantaneamente; trabalhos interativos sofrem amortização de 5 minutos, enquanto operações em segundo plano (como pipelines agendados) são suavizadas em uma janela contínua de 24 horas.

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/0004-onelake-capacities-spark-pools/lab_simulation.py
```

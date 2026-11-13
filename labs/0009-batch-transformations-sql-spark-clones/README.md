# Exercício Prático: Transformações em Lote com PySpark, Views T-SQL e Table Clones

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Cenário de Negócio
Executar rotinas analíticas em lote no Fabric e aplicar cópias de zero-custo via comandos CLONE TABLE no Warehouse para testar atualizações destrutivas em ambiente isolado sem duplicar dados.

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo do Laboratório

#### Tarefa 1: Criar um Clone de Tabela (Zero-Copy Clone)
1. No Fabric Warehouse, abra uma nova consulta SQL.
2. Execute o comando: CREATE TABLE dbo.FactVendas_Homolog AS CLONE dbo.FactVendas;
3. Observe que o clone é criado em subsegundo, apontando para os mesmos arquivos físicos Delta Parquet no OneLake.

#### Tarefa 2: Testar Alterações Isoladas no Clone
1. Execute alterações pontuais ou deletes de teste na tabela clonada: DELETE FROM dbo.FactVendas_Homolog WHERE Ano = 2024;
2. Consulte a tabela original dbo.FactVendas e confirme que ela continua íntegra e sem modificações.

---

## ⚠️ Ponto Crítico para o Exame DP-700
Conceito de Prova: No Microsoft Fabric, o comando CLONE TABLE opera como Shallow Clone (cópia lógica instantânea de metadados). Apenas quando o clone sofre escrita é que novos arquivos de dados são gerados isoladamente.

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/0009-batch-transformations-sql-spark-clones/lab_simulation.py
```

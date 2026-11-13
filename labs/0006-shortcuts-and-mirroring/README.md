# Exercício Prático: Criar Atalhos (Shortcuts) no OneLake e Mirroring Zero-Copy

> **Padrão Oficial Microsoft Learn • Preparatório Microsoft Fabric Data Engineer Associate (DP-700)**

---

## 🎯 Cenário de Negócio
A empresa possui dados legados no Amazon S3 e no Azure Data Lake Storage Gen2. Em vez de criar pipelines caros de cópia, você criará atalhos (Shortcuts) no OneLake permitindo consultas diretas em subsegundo.

---

## ☁️ Opção 1: Execução no Portal Microsoft Fabric (`app.fabric.microsoft.com`)

### Pré-requisitos
- Conta no [portal do Microsoft Fabric](https://app.fabric.microsoft.com/) com licença **Fabric Trial** ativa ou capacidade F-SKU.
- Um Workspace associado à capacidade.

### Passo a Passo do Laboratório

#### Tarefa 1: Criar um Atalho (Shortcut) para o Amazon S3
1. Abra o Lakehouse lh_global_enterprise.
2. Passe o mouse sobre a pasta Tables, clique nos três pontos (...) e selecione Novo atalho (New shortcut).
3. Selecione o provedor Amazon S3.
4. Preencha o caminho do bucket (ex: s3://corp-telemetry-data/) e as credenciais de acesso.
5. Nomeie o atalho como s3_telemetria_shortcut e clique em Criar.

#### Tarefa 2: Consultar o Atalho Diretamente sem Duplicação
1. Abra o Notebook Spark vinculado ao Lakehouse.
2. Leia os dados da tabela criada pelo atalho exatamente como se fosse uma tabela local:
3. df_s3 = spark.table('s3_telemetria_shortcut'); display(df_s3.limit(10))
4. Observe que o OneLake busca os dados sob demanda sem transferir armazenamento permanente.

---

## ⚠️ Ponto Crítico para o Exame DP-700
Pegadinha de Exame: Os atalhos não copiam arquivos físicos; eles apenas criam metadados apontando para a fonte externa. Se a credencial na AWS/Azure expirar ou os dados forem deletados no bucket de origem, o atalho no Fabric apresentará falha de leitura.

---

## 💻 Opção 2: Simulação Local no Terminal (Offline)

Caso não possua acesso ao Microsoft Fabric no momento, execute a simulação Python inclusa no repositório:
```bash
./.venv/bin/python labs/0006-shortcuts-and-mirroring/lab_simulation.py
```

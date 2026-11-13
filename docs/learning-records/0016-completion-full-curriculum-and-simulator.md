# Registro de Aprendizado 0016: Conclusão Integral do Currículo DP-700 & Expansão do Simulador

- **Data:** 13 de Novembro de 2026
- **Status:** Concluído com Sucesso

## 1. Escopo e Entregas Realizadas

### A. Finalização do Módulo 3 (Governança, CI/CD, Otimização e Monitoramento)
1. **Lição 0013 (`lessons/0013-cicd-git-deployment-pipelines-sqlproj.html`):**
   - CI/CD corporativo com Git Integration (Azure DevOps e GitHub), branches individuais, serialização declarativa de artefatos Fabric.
   - Deployment Pipelines com estágios DEV -> TEST -> PROD e configuração de **Deployment Rules** (Parameter Rules e Data Source Rules) para remapeamento sem intervenção manual.
   - Projetos de banco de dados SQL (`.sqlproj`) e pacotes DACPAC para o Fabric Data Warehouse.
   - Lab Python: `labs/0013-cicd-git-deployment-pipelines/lab_simulation.py`.
   - Áudio Neural: `assets/audio/lesson-0013-pt.mp3` com dicionário fonético auditado.

2. **Lição 0014 (`lessons/0014-performance-vorder-liquid-clustering-tuning.html`):**
   - Algoritmo de compressão e ordenação em tempo de escrita **V-Order** (100% aderente ao padrão Parquet aberto, aceleração de até 7x em Direct Lake).
   - Migração de particionamento estático e Z-Order para **Liquid Clustering** (`CLUSTER BY`) em tabelas Delta de alta cardinalidade com reescrita incremental.
   - Regras de segurança do comando `VACUUM` (limiar padrão de 7 dias / 168 horas e prevenção contra perda de Time Travel).
   - Mitigação de Data Skew no Apache Spark com Adaptive Query Execution (AQE `skewJoin`) e Salting.
   - Lab Python: `labs/0014-performance-vorder-liquid-clustering/lab_simulation.py`.
   - Áudio Neural: `assets/audio/lesson-0014-pt.mp3`.

3. **Lição 0015 (`lessons/0015-monitoring-hub-capacity-metrics-troubleshooting.html`):**
   - Observabilidade integrada com Monitoring Hub e Spark History Server.
   - Fabric Capacity Metrics App: categorização de operações interativas (janela de smoothing de 5 min) vs background (janela de 24h).
   - Estágios progressivos de Throttling: Interactive Delay (60s) -> Interactive Rejection -> Background Rejection.
   - T-SQL Dynamic Management Views (DMVs) e o schema `queryinsights` (`exec_requests_history`, `frequently_run_queries`, `long_running_queries`, `sys.dm_exec_requests`).
   - Lab Python: `labs/0015-monitoring-capacity-metrics-dmvs/lab_simulation.py`.
   - Áudio Neural: `assets/audio/lesson-0015-pt.mp3`.

### B. Expansão Integral do Banco de Questões do Simulador DP-700 (`assets/exam-questions.js`)
- **Total de 23 itens de avaliação:**
  - 15 questões de Escolha Única (Single-Choice).
  - 8 questões de Múltipla Escolha (Multi-Select, exigindo exatamente 2 alternativas corretas).
  - 3 Estudos de Caso Corporativos completos em Split-Screen com abas navegáveis de requisitos (`Overview`, `Existing Environment`, `Data Requirements`, `Technical Requirements`):
    - **Estudo de Caso 1:** *Contoso Global Retail* (Direct Lake Fallback, Shortcuts S3, Mirroring Azure SQL).
    - **Estudo de Caso 2:** *Litware Smart IoT Energy Grid* (Eventhouse, Update Policy KQL, Eventstream, has vs contains, arg_max).
    - **Estudo de Caso 3:** *Fabrikam Financial Services* (Dynamic Data Masking, RLS, .sqlproj DACPAC, Deployment Rules).

### C. Folhas de Referência Prontas para Impressão (`reference/`)
- `01-glossary-and-fundamentals-visual-guide.html`: Glossário e Capacidades.
- `02-storage-delta-medallion-shortcuts-guide.html`: Storage, Delta Lake, Medallion e Zero-Copy.
- `03-architectural-engines-decision-matrix.html`: Matriz Decisória de Motores (Lakehouse vs Warehouse vs Eventhouse vs SQL DB).
- `04-three-languages-sql-pyspark-kql-cheatsheet.html`: As Três Linguagens (T-SQL vs PySpark vs KQL) com sintaxe comparada.
- `05-security-governance-purview-fallback-guide.html`: Segurança, Governança, Purview e Direct Lake Fallback.
- `06-performance-vorder-clustering-monitoring-cheatsheet.html`: Otimização, V-Order, Liquid Clustering, Smoothing e DMVs.


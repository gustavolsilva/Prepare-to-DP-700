# Registro de Aprendizado 0019: Expansão do Banco para 182 Questões e Arquitetura do Simulador Pearson VUE Oficial

- **Data:** 13 de Novembro de 2026
- **Status:** Concluído com Sucesso

## 1. Motivação e Objetivos
O Centro Oficial de Simulados DP-700 continha originalmente 58 questões. O usuário solicitou que o banco fosse expandido para **pelo menos o triplo (mínimo de 174 questões)**, cobrindo com profundidade técnica e rigor os 3 domínios oficiais da Microsoft, com formato idêntico ao ambiente oficial de testes da **Pearson VUE**, incluindo explicações aprofundadas com know-how prático e múltiplos estudos de caso em Split-Screen.

## 2. Implementações Realizadas

### 2.1. Expansão do Banco para 182 Questões
O banco foi arquitetado de forma modular sob `scripts/exam_data/`:
1. **`domain1.py` (38 questões):** Domínio 1 (15-20% do exame) — Capacidades F-SKU, Smoothing, Burndown, Throttling, RBAC, ODAR, Shortcuts (S3, GCS, ADLS, Dataverse Link), RLS/CLS, Direct Lake Fallback, Purview e CI/CD.
2. **`domain2.py` (82 questões):** Domínio 2 (40-45% do exame) — Data Factory (Fast Copy, Lookup 5k, ForEach concorrência 50, WebHook assíncrono), Dataflows Gen2 (Staging Lakehouse), Apache Spark (Starter vs Custom Pools, Velox C++, AQE Skew Join, Broadcast 10MB, Streaming `availableNow=True` e Watermarking), Delta Lake (`_delta_log`, checkpoints a cada 10 commits, ACID OCC, Time Travel, RESTORE, VACUUM retenção 7 dias, OPTIMIZE bin-packing, Liquid Clustering, Z-Order, Merge SCD1/2, Clones), Fabric Warehouse T-SQL (3-part naming, `NOT ENFORCED`, CTAS, COPY INTO) e Real-Time Intelligence (Eventstream CDC/Kafka/IoT Hub, Eventhouse KQL Update Policies, Hot vs Cold Cache, `arg_max()`, `has` vs `contains`, Data Activator Reflex).
3. **`domain3.py` (38 questões):** Domínio 3 (20-25% do exame) — Capacity Metrics App (Timepoints de 30s, Background Rejection), Query Insights (`queryinsights.exec_requests_history`, `frequently_run_queries`, `long_running_queries`, `sys.dm_exec_sessions`), Spark UI (Spill to Disk, Garbage Collection > 10%, Data Skew visual), Delta Data Skipping (Min/Max estatísticas até 32 colunas), e Power BI Direct Lake Performance (Direct Lake Framing, detecção de Fallback silencioso no DAX Studio, estouro de memória, propriedade `DirectLakeBehavior = DirectLakeOnly`, Cold vs Warm Cache).
4. **`case_studies.py` (24 questões em 8 Casos de Estudo):** Cenários corporativos em tela dividida (Split-Screen) com 4 abas obrigatórias de contexto cada (*Visão Geral*, *Ambiente Atual*, *Requisitos de Dados* e *Requisitos Técnicos*): Contoso, Litware, Fabrikam, Woodgrove, AdventureWorks, Tailwind, Northwind e Alpine Ski.

### 2.2. Compilador Oficial `scripts/build_full_180_exam_bank.py`
- Compila os dados modulares em `assets/exam-questions.js`, gerando o array JavaScript unificado com chaves sem aspas para atender aos requisitos estritos dos testes unitários em `tests/test_exam_questions.py`.
- Total de questões jogáveis: **182 questões** (165 Single-Choice, 17 Multi-Select, 8 Case Studies, 199 alternativas corretas, 533 distratores analisados).

### 2.3. Recursos Pearson VUE Integrados em `assets/exam-simulator.js`
- 🚩 **Flag for Review:** Marcação visual persistente de questões duvidosas (atalho `R`).
- 📋 **Question Matrix Modal:** Modal com grade de 182 posições com estados de cor (Respondida, Em Branco, Marcada para Revisão, Correta, Incorreta).
- 🎛️ **Filtros por Domínio e Formato:** Permite treinar por domínios específicos ou tipos de questão no Modo Treino.
- ⏱️ **Modo Exame Oficial (100 minutos):** Temporizador regressivo oficial com aviso nos últimos 5 minutos.
- 📊 **Placar Oficial Escalado (0 a 1000) com Breakdown por Domínio:** Barra de progresso comparativa de acertos nos Domínios 1, 2 e 3.
- 🔍 **Modo Revisão Pós-Exame:** Navegação questão por questão exibindo a tríade explicativa (`✅ Por que a correta está certa`, `❌ Análise dos Distratores`, `💡 Dica de Prova DP-700`).
- 🎲 **Randomização de Alternativas:** Embaralhamento dinâmico em cada execução para eliminar vícios de posição.


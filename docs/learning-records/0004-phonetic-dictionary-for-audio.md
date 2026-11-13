# Padrão de Síntese de Áudio: Dicionário Fonético Auditado (Plain Text + Regex Boundary)

## Causa Raiz dos Problemas Anteriores
1. O `edge-tts` escapa tags XML internamente (`xml.sax.saxutils.escape`), o que fazia qualquer tag SSML (`<lang>`, `<speak>`) ser lida em voz alta.
2. Na remoção das tags SSML, o script anterior havia aplicado `.replace()` em apenas 6 siglas (`T-SQL`, `SQL Analytics Endpoint`, `DP 700`, `DML`, `ACID`, `BI`), deixando palavras em inglês como `Warehouse`, `Lakehouse`, `OneLake`, `Azure Data Factory`, `Databricks`, `Synapse`, `Snowflake`, `Analysis Services`, `Direct Lake` e `Smoothing` sem mapeamento fonético.

## Solução Centralizada (`labs/generate_audio.py`)
Criamos o gerador centralizado [`labs/generate_audio.py`](../labs/generate_audio.py) usando substituição por expressão regular com fronteira de palavra (`(?<![A-Za-zÀ-ÿ])termo(?![A-Za-zÀ-ÿ])`), ordenado do termo composto mais longo para o mais curto:

| Termo Original no Texto | Grafia Fonética Enviada ao Motor Neural (`pt-BR-AntonioNeural`) |
| :--- | :--- |
| `Microsoft Fabric Data Engineer Associate` | `Máicrosoft Fébrick Dêita Endjiníer Assôuci-êit` |
| `SQL Analytics Endpoint` | `Síquel Analítics Énd-point` |
| `Fabric Data Warehouse` | `Fébrick Dêita Uér-rause` |
| `Azure Data Factory` | `Éjur Dêita Féctori` |
| `Analysis Services` | `Análisis Sêrvices` |
| `Data Warehouses` / `Data Warehouse` | `Dêita Uér-rauses` / `Dêita Uér-rause` |
| `Warehouse` | `Uér-rause` |
| `Lakehouse` | `Lêik-rause` |
| `OneLake` | `Uan-Lêik` |
| `Direct Lake` | `Dairéct Lêik` |
| `Data Lakes` / `Data Lake` | `Dêita Lêiks` / `Dêita Lêik` |
| `Delta Parquet` / `Parquet` | `Délta Parkêi` / `Parkêi` |
| `Power BI` / `BI` | `Páuer Bi-Ái` / `Bi-Ái` |
| `Microsoft Fabric` / `Microsoft` / `Fabric` | `Máicrosoft Fébrick` / `Máicrosoft` / `Fébrick` |
| `Databricks` | `Dêita-bríks` |
| `Snowflake` | `Isnôu-flêik` |
| `Synapse` | `Sínaps` |
| `Smoothing` | `Ismú-dhin` |
| `PySpark` / `Spark` | `Pai-Spárk` / `Spárk` |
| `clusters` / `cluster` | `clâsters` / `clâster` |
| `scripts` | `iscrípts` |
| `V-Order` | `Vê-Órder` |
| `T-SQL` / `SQL` | `Tchi-Síquel` / `Síquel` |
| `DML` / `DDL` | `Dê-Eme-Éle` / `Dê-Dê-Éle` |
| `ACID` / `SaaS` | `Ácid` / `Sáss` |
| `DP-700` / `DP 700` | `Dê-Pê setecentos` |

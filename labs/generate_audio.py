"""
Gerador Centralizado de Áudio Neural para o Curso DP-700
Garante que 100% dos termos técnicos em inglês sejam pronunciados com a fonética correta
em inglês técnico, enquanto o texto em português mantém a naturalidade nativa.
"""

import asyncio
import re
import edge_tts

# Dicionário Fonético Completo (ordenado do termo mais longo para o mais curto para evitar substituições parciais)
PHONETIC_DICTIONARY = [
    ("Microsoft Fabric Data Engineer Associate", "Máicrosoft Fébrick Dêita Endjiníer Assôuci-êit"),
    ("SQL Analytics Endpoint", "Síquel Analítics Énd-point"),
    ("Fabric Data Warehouse", "Fébrick Dêita Uér-rause"),
    ("Azure Data Factory", "Éjur Dêita Féctori"),
    ("Analysis Services", "Análisis Sêrvices"),
    ("Data Warehouses", "Dêita Uér-rauses"),
    ("Data Warehouse", "Dêita Uér-rause"),
    ("Data Engineer", "Dêita Endjiníer"),
    ("Delta Parquet", "Délta Parkêi"),
    ("Direct Lake", "Dairéct Lêik"),
    ("Data Lakes", "Dêita Lêiks"),
    ("Data Lake", "Dêita Lêik"),
    ("Power BI", "Páuer Bi-Ái"),
    ("Microsoft Fabric", "Máicrosoft Fébrick"),
    ("Microsoft", "Máicrosoft"),
    ("Databricks", "Dêita-bríks"),
    ("Warehouse", "Uér-rause"),
    ("Lakehouse", "Lêik-rause"),
    ("Snowflake", "Isnôu-flêik"),
    ("Smoothing", "Ismú-dhin"),
    ("Associate", "Assôuci-êit"),
    ("OneLake", "Uan-Lêik"),
    ("PySpark", "Pai-Spárk"),
    ("Synapse", "Sínaps"),
    ("clusters", "clâsters"),
    ("cluster", "clâster"),
    ("scripts", "iscrípts"),
    ("Fabric Capacity Metrics App", "Fébrick Capáciti Métrics Épp"),
    ("Monitoring Hub", "Monitôring Râb"),
    ("Spark History Server", "Spárk Rístori Sêrver"),
    ("Interactive Delay", "Interáctive Dilêi"),
    ("Interactive Rejection", "Interáctive Ridjécshon"),
    ("Background Rejection", "Béc-gráund Ridjécshon"),
    ("queryinsights", "Cuéri-In-saits"),
    ("DMVs", "Dê-Eme-Vês"),
    ("DMV", "Dê-Eme-Vê"),
    ("Liquid Clustering", "Líquid Clâstering"),
    ("Adaptive Query Execution", "Adéptive Cuéri Execúshon"),
    ("AQE", "Á-Kyu-Í"),
    ("Data Skew", "Dêita Isquiú"),
    ("CLUSTER BY", "Clâster Bái"),
    ("Z-Order", "Zê-Órder"),
    ("OPTIMIZE", "Óptimaiz"),
    ("VACUUM", "Váquiuum"),
    ("Time Travel", "Taim Trével"),
    ("Straggler", "Istrégler"),
    ("Salting", "Sólting"),
    ("V-Order", "Vê-Órder"),
    ("Parquet", "Parkêi"),
    ("Fabric", "Fébrick"),
    ("Spark", "Spárk"),
    ("Delta", "Délta"),
    ("T-SQL", "Tchi-Síquel"),
    ("DP-700", "Dê-Pê setecentos"),
    ("DP 700", "Dê-Pê setecentos"),
    ("DML", "Dê-Eme-Éle"),
    ("DDL", "Dê-Dê-Éle"),
    ("ACID", "Ácid"),
    ("CI/CD", "Cê-Í Cê-Dê"),
    ("Deployment Pipelines", "Diplóiment Páipli-nês"),
    ("Deployment Pipeline", "Diplóiment Páipli-ne"),
    ("Deployment Rules", "Diplóiment Rúls"),
    ("Deployment Rule", "Diplóiment Rúl"),
    ("Git Integration", "Guíti Integuêishon"),
    ("Azure DevOps", "Éjur Dév-Óps"),
    ("GitHub", "Guít-Râb"),
    ("DACPAC", "Dék-Pék"),
    ("sqlproj", "Síquel-Pródj"),
    ("Direct Lake Fallback", "Dairéct Lêik Fóll-bék"),
    ("DirectQuery Fallback", "Dairéct-Cuéri Fóll-bék"),
    ("Fallback", "Fóll-bék"),
    ("OneLake Data Access Roles", "Uan-Lêik Dêita Ácsess Rôuls"),
    ("Dynamic Data Masking", "Dainémic Dêita Máskin"),
    ("DDM", "Dê-Dê-Eme"),
    ("Row-Level Security", "Rôu-Lével Secúriti"),
    ("Column-Level Security", "Cólumn-Lével Secúriti"),
    ("RLS", "Érre-Éle-Ésse"),
    ("CLS", "Cê-Éle-Ésse"),
    ("Microsoft Purview", "Máicrosoft Púrvíú"),
    ("Purview", "Púrvíú"),
    ("Sensitivity Labels", "Sensitíviti Lêibels"),
    ("Sensitivity Label", "Sensitíviti Lêibel"),
    ("Endorsement", "Endórsement"),
    ("Promoted", "Promôuted"),
    ("Certified", "Cêrtifáid"),
    ("Update Policies", "Âp-dêit Pólissis"),
    ("Update Policy", "Âp-dêit Pólissi"),
    ("Materialized Views", "Matiríalaizd Viús"),
    ("Materialized View", "Matiríalaizd Viú"),
    ("mv-expand", "Eme-Vê Expênd"),
    ("parse_json", "Párse Jêi-som"),
    ("make-series", "Mêik-Séris"),
    ("arg_max", "Árg-Méx"),
    ("Spark Structured Streaming", "Spárk Strâctchurd Strímin"),
    ("Structured Streaming", "Strâctchurd Strímin"),
    ("withWatermark", "Uídh-Uáter-márk"),
    ("Tumbling Window", "Tâmblin Uíndou"),
    ("Tumbling Windows", "Tâmblin Uíndous"),
    ("Hopping Window", "Róppin Uíndou"),
    ("Hopping Windows", "Róppin Uíndous"),
    ("Sliding Window", "Sláidin Uíndou"),
    ("Sliding Windows", "Sláidin Uíndous"),
    ("Session Window", "Sêshon Uíndou"),
    ("Session Windows", "Sêshon Uíndous"),
    ("MERGE INTO", "Mêrdj Íntu"),
    ("COPY INTO", "Cópi Íntu"),
    ("CTAS", "Cê-Tás"),
    ("Schema Evolution", "Squíma Évolushon"),
    ("mergeSchema", "Mêrdj-Squíma"),
    ("Table Clones", "Têibol Clôuns"),
    ("Table Clone", "Têibol Clôun"),
    ("AS CLONE OF", "Éz Clôun Óv"),
    ("Watermarking", "Uáter-márkin"),
    ("Watermark", "Uáter-márk"),
    ("High Watermark", "Rái Uáter-márk"),
    ("Slowly Changing Dimensions", "Islôuli Tchêndjin Dimênshons"),
    ("Slowly Changing Dimension", "Islôuli Tchêndjin Dimênshon"),
    ("SCD Tipo 1", "Ésse-Cê-Dê Tipo Um"),
    ("SCD Tipo 2", "Ésse-Cê-Dê Tipo Dois"),
    ("SCD Tipo 3", "Ésse-Cê-Dê Tipo Três"),
    ("SCD", "Ésse-Cê-Dê"),
    ("IsCurrent", "Íz Cârrênt"),
    ("ValidFrom", "Vélid Frôm"),
    ("ValidTo", "Vélid Tú"),
    ("Dataflows Gen2", "Dêita-flôus Guêm dois"),
    ("Dataflow Gen2", "Dêita-flôu Guêm dois"),
    ("Copy Job", "Cópi Jób"),
    ("Copy Jobs", "Cópi Jóbs"),
    ("mssparkutils", "Eme-Ésse-Spárk-Iútils"),
    ("runMultiple", "Rãn-Múltipol"),
    ("DAG", "Dég"),
    ("DAGs", "Dégs"),
    ("Power Query", "Páuer Cuéri"),
    ("Shortcuts", "Shórt-câts"),
    ("Shortcut", "Shórt-cât"),
    ("Mirroring", "Mírrorin"),
    ("Cosmos DB", "Cózmos Dê-Bê"),
    ("ADLS Gen2", "Á-Dê-Éle-Ésse Guêm dois"),
    ("Amazon S3", "Ámazon Ésse-três"),
    ("Google Cloud Storage", "Gúgol Cláud Stóridj"),
    ("Dataverse", "Dêita-vêrse"),
    ("CDC", "Cê-Dê-Cê"),
    ("Zero-Copy", "Zíro-Cópi"),
    ("Zero-ETL", "Zíro-Ê-Tê-Éle"),
    ("Polaris", "Poláris"),
    ("Decision Guide", "Decíjon Gáid"),
    ("SQL Database", "Síquel Dêitabêis"),
    ("Read-Only", "Ríid Ônli"),
    ("Capacity Units", "Capáciti Iúnits"),
    ("Capacity Unit", "Capáciti Iúnit"),
    ("CUs", "Cê-Ús"),
    ("CU", "Cê-Ú"),
    ("F-SKU", "Éfe-És-Ká-Ú"),
    ("F-SKUs", "Éfe-És-Ká-Ús"),
    ("F64", "Éfe sessenta e quatro"),
    ("Starter Pools", "Stárter Púls"),
    ("Starter Pool", "Stárter Púl"),
    ("Custom Pools", "Câstom Púls"),
    ("Custom Pool", "Câstom Púl"),
    ("Autoscale", "Óuto-squêil"),
    ("Throttling", "Trótlin"),
    ("Data Mesh", "Dêita Mésh"),
    ("Domains", "Domêins"),
    ("Domain", "Domêin"),
    ("KQL", "Ká-Kyu-Éle"),
    ("Kusto Query Language", "Cústo Cuéri Lêngüidj"),
    ("Star Schema", "Stár Squíma"),
    ("Surrogate Key", "Surroguêit Quí"),
    ("Surrogate Keys", "Surroguêit Quís"),
    ("FactSales", "Féct-Sêils"),
    ("DimCustomer", "Dím-Câstomer"),
    ("Eventhouse", "Ivênt-rause"),
    ("Eventhouses", "Ivênt-rauses"),
    ("Eventstreams", "Ivênt-stríms"),
    ("Eventstream", "Ivênt-strím"),
    ("Delta Lake", "Délta Lêik"),
    ("Time Travel", "Táim Trével"),
    ("Medallion", "Medálion"),
    ("Bronze", "Brônze"),
    ("Silver", "Sílver"),
    ("Gold", "Gôuld"),
    ("checkpoint", "tchéck-point"),
    ("checkpoints", "tchéck-points"),
    ("JSON", "Jêi-som"),
    ("commit", "cômit"),
    ("commits", "cômits"),
    ("VACUUM", "Véquium"),
    ("OPTIMIZE", "Óptimaiz"),
    ("SaaS", "Sáss"),
    ("SQL", "Síquel"),
    ("BI", "Bi-Ái"),
]


def apply_phonetic_dictionary(text: str) -> str:
    """
    Substitui todos os termos técnicos em inglês pela grafia fonética exata
    para a voz neural pt-BR-AntonioNeural, usando word boundaries seguros.
    """
    result = text
    for term, phonetic in PHONETIC_DICTIONARY:
        # Usa regex com fronteira de palavra para não alterar sub-strings indevidas
        pattern = r'(?<![A-Za-zÀ-ÿ])' + re.escape(term) + r'(?![A-Za-zÀ-ÿ])'
        result = re.sub(pattern, phonetic, result)
    return result


LESSON_0001_SCRIPT = (
    "Lição zero zero zero um: Fundamentos de Engenharia de Dados e o Ecossistema Microsoft Fabric. "
    "A Crise dos Silos de Dados e o Pesadelo da Replicação. "
    "Imagine o seguinte cenário em uma grande corporação: "
    "O time de ingestão usa Azure Data Factory para carregar dados brutos em um Data Lake. "
    "O time de engenharia usa Databricks para limpar esses dados e gerar tabelas Delta. "
    "Depois, outro time roda scripts para carregar essas tabelas dentro de um Data Warehouse dedicado, como Synapse ou Snowflake, "
    "para que os analistas de negócios consigam rodar consultas T-SQL. "
    "Por fim, o time de BI cria relatórios no Power BI que precisam importar tudo de novo para a memória do Analysis Services às seis horas da manhã. "
    "O resultado? Os mesmos dados são copiados e pagos quatro vezes em contas de armazenamento diferentes. "
    "O Microsoft Fabric foi criado pela Microsoft exatamente para acabar com essa fragmentação. "
    "Ele estabelece o formato aberto Delta Parquet como padrão universal sobre o OneLake. "
    "Isso permite processar com PySpark no Lakehouse, consultar via T-SQL no Data Warehouse, e visualizar no Power BI com Direct Lake na memória, "
    "sem nunca mover ou duplicar um único arquivo. "
    "Pontos críticos para o Exame DP-700: "
    "Primeiro: O OneLake é o pilar central e elimina a cópia redundante de dados. "
    "Segundo: O SQL Analytics Endpoint do Lakehouse é estritamente somente leitura. "
    "Se o cenário exigir comandos DML e transações ACID via T-SQL, a escolha correta é sempre o Fabric Data Warehouse. "
    "Terceiro: O mecanismo de Smoothing amortiza operações de segundo plano em uma janela móvel de vinte e quatro horas. "
    "Quarto: O modo Direct Lake no Power BI lê diretamente os arquivos Delta do OneLake sem necessidade de atualizações periódicas de importação."
)


LESSON_0002_SCRIPT = (
    "Lição zero zero zero dois: Fundamentos de Armazenamento, Parquet, Delta Lake e a Arquitetura Medallion. "
    "O Que Torna o Armazenamento no Microsoft Fabric Tão Rápido e Confiável? "
    "Para entender o OneLake, precisamos primeiro dissecar a evolução dos formatos de dados. "
    "Arquivos tradicionais como CSV e JSON armazenam dados linha por linha. "
    "Se você executa uma consulta analítica que soma valores em uma tabela com cinquenta colunas e milhões de linhas, "
    "um formato de linha força o disco a ler todas as quarenta e nove colunas irrelevantes. "
    "O Apache Parquet revoluciona isso organizando os dados em colunas e grupos de linhas. "
    "Ele armazena metadados estatísticos com valores mínimos e máximos por coluna, permitindo que o motor pule arquivos inteiros sem ler o conteúdo. "
    "No entanto, arquivos Parquet puros têm limitações críticas: eles não suportam transações ACID, nem atualizações pontuais, nem Time Travel. "
    "É exatamente aqui que entra o Delta Lake. "
    "O Delta Lake adiciona uma camada de governança e transações ACID sobre os arquivos Parquet por meio da pasta _delta_log. "
    "Cada inserção, atualização ou exclusão gera um novo arquivo de log JSON atômico e imutável. "
    "A cada dez commits, o Delta gera um checkpoint em Parquet consolidando o estado do log para manter a leitura ultraveloz. "
    "No Fabric, esses conceitos convergem na Arquitetura Medallion. "
    "A camada Bronze preserva o dado bruto na sua fidelidade original. "
    "A camada Silver limpa, valida tipos, remove duplicatas e aplica regras de qualidade. "
    "A camada Gold agrega os dados em modelos estrela dimensionais prontos para consumo pelo Power BI via Direct Lake. "
    "Três regras de ouro para o Exame DP-700: "
    "Primeiro: A pasta _delta_log é a única fonte da verdade para o estado da tabela. Arquivos Parquet soltos sem commit no log são ignorados pelos leitores. "
    "Segundo: O comando VACUUM remove arquivos Parquet antigos que já saíram do período de retenção do Time Travel. Nunca execute VACUUM com retenção zero em tabelas com leitores concorrentes ativos. "
    "Terceiro: O Microsoft Fabric aplica automaticamente a otimização V-Order ao gravar arquivos Delta, acelerando as leituras no SQL Endpoint e no Power BI."
)


async def generate_lesson_0001():
    phonetic_text = apply_phonetic_dictionary(LESSON_0001_SCRIPT)
    print("=== TEXTO FONÉTICO FINAL (LIÇÃO 1) ===")
    print(phonetic_text)
    print("======================================")
    communicate = edge_tts.Communicate(phonetic_text, "pt-BR-AntonioNeural")
    await communicate.save("assets/audio/lesson-0001-pt.mp3")
    print("Arquivo salvo com sucesso em assets/audio/lesson-0001-pt.mp3")


async def generate_lesson_0002():
    phonetic_text = apply_phonetic_dictionary(LESSON_0002_SCRIPT)
    print("=== TEXTO FONÉTICO FINAL (LIÇÃO 2) ===")
    print(phonetic_text)
    print("======================================")
    communicate = edge_tts.Communicate(phonetic_text, "pt-BR-AntonioNeural")
    await communicate.save("assets/audio/lesson-0002-pt.mp3")
    print("Arquivo salvo com sucesso em assets/audio/lesson-0002-pt.mp3")


LESSON_0003_SCRIPT = (
    "Lição zero zero zero três: Modelagem Dimensional, Star Schema e o Mapa das Três Linguagens do Exame DP-700. "
    "Por Que a Prova Exige T-SQL, PySpark e KQL em um Único Engenheiro de Dados? "
    "No ecossistema unificado do Microsoft Fabric, cada motor analítico foi desenhado para resolver uma classe específica de problema. "
    "Para ser aprovado no DP-700, você precisa dominar quando usar cada uma das três linguagens oficiais da plataforma. "
    "Primeiro: T-SQL. É a linguagem canônica do Fabric Data Warehouse e dos modelos dimensionais em Star Schema. "
    "Se você precisa criar tabelas de fatos e dimensões, aplicar surrogate keys numéricas, gerenciar transações ACID complexas e expor dados para analistas de negócios, T-SQL é a escolha mandatória. "
    "Segundo: PySpark. É a linguagem dominante no Fabric Lakehouse. "
    "Usamos PySpark para transformações em lote de dados semiestruturados, grandes volumes de JSON, limpeza de texto, particionamento avançado e pipelines de machine learning sobre clusters distribuídos. "
    "Terceiro: KQL, ou Kusto Query Language. É a linguagem de alta performance do Eventhouse e Real-Time Intelligence. "
    "O KQL utiliza o operador pipe para encadear filtros e agregações sobre séries temporais, logs de servidores e telemetria de IoT, entregando respostas em milissegundos sobre bilhões de eventos. "
    "Pontos críticos para o Exame DP-700: "
    "Primeiro: Em modelagem dimensional, o Star Schema é o padrão recomendado pela Microsoft tanto para Data Warehouse quanto para consumo pelo Power BI Direct Lake. "
    "Segundo: Use sempre surrogate keys inteiras geradas sequencialmente em vez de business keys textuais para otimizar os joins e as estruturas colunares do VertiPaq. "
    "Terceiro: No KQL, os operadores summarize, make-series e arg_max aparecem com frequência em questões de telemetria e agregação de streaming."
)


async def generate_lesson_0003():
    phonetic_text = apply_phonetic_dictionary(LESSON_0003_SCRIPT)
    print("=== TEXTO FONÉTICO FINAL (LIÇÃO 3) ===")
    print(phonetic_text)
    print("======================================")
    communicate = edge_tts.Communicate(phonetic_text, "pt-BR-AntonioNeural")
    await communicate.save("assets/audio/lesson-0003-pt.mp3")
    print("Arquivo salvo com sucesso em assets/audio/lesson-0003-pt.mp3")


LESSON_0004_SCRIPT = (
    "Lição zero zero zero quatro: OneLake, Capacidades F-SKU, Smoothing, Domínios e Configuração de Spark Pools. "
    "Como o Microsoft Fabric Governa e Dimensiona a Computação na Nuvem? "
    "No coração financeiro e operacional do Microsoft Fabric está o conceito de Capacidade. "
    "Diferente dos serviços em nuvem legados onde você paga por máquinas virtuais ociosas, o Fabric unifica toda a cobrança em Capacity Units, ou CUs, por meio das F-SKUs. "
    "Todas as cargas de trabalho — pipelines do Data Factory, notebooks de PySpark, consultas no Data Warehouse e relatórios no Power BI — consomem da mesma piscina compartilhada de CUs. "
    "Para evitar que picos repentinos de processamento interrompam as consultas dos usuários, o Fabric implementa a tecnologia de Smoothing. "
    "Operações em segundo plano, como pipelines de ingestão e notebooks agendados, têm seu consumo diluído em uma janela móvel de vinte e quatro horas. "
    "Já operações interativas de curta duração são amortizadas em uma janela de cinco minutos. "
    "Se o consumo acumulado ultrapassar consistentemente cem por cento da capacidade, a plataforma entra em estágios graduais de Throttling, iniciando pela rejeição de novas tarefas interativas. "
    "Na governança empresarial, o OneLake implementa a arquitetura de Data Mesh por meio de Domínios. "
    "Domínios permitem agrupar workspaces logicamente por unidades de negócio, como Finanças, Vendas ou Recursos Humanos, permitindo descentralizar a gestão sem fragmentar o lago único de dados. "
    "Por fim, na camada de computação Spark, a Microsoft disponibiliza dois tipos de pools: "
    "As Starter Pools oferecem inicialização quase instantânea de cinco segundos com nós pré-aquecidos para exploração rápida. "
    "Já as Custom Pools permitem definir o tamanho exato dos nós de memória e CPU, autoscale automático e alocação dinâmica de executores para cargas de produção. "
    "Pontos críticos para o Exame DP-700: "
    "Primeiro: A SKU F64 é a menor capacidade que permite que usuários sem licença individual do Power BI Pro visualizem relatórios compartilhados. "
    "Segundo: Se um job de processamento pesado causar picos de consumo, o mecanismo de Smoothing protege a capacidade evitando cancelamentos imediatos. "
    "Terceiro: Para pipelines de ETL de produção com dependências de pacotes Python específicos e requisitos de memória dedicada, a configuração recomendada é sempre uma Custom Spark Pool."
)


async def generate_lesson_0004():
    phonetic_text = apply_phonetic_dictionary(LESSON_0004_SCRIPT)
    print("=== TEXTO FONÉTICO FINAL (LIÇÃO 4) ===")
    print(phonetic_text)
    print("======================================")
    communicate = edge_tts.Communicate(phonetic_text, "pt-BR-AntonioNeural")
    await communicate.save("assets/audio/lesson-0004-pt.mp3")
    print("Arquivo salvo com sucesso em assets/audio/lesson-0004-pt.mp3")


LESSON_0005_SCRIPT = (
    "Lição zero zero zero cinco: Guia de Decisão Arquitetural: Lakehouse, Data Warehouse, Eventhouse e SQL Database. "
    "A Decisão de Arquitetura Mais Importante do Exame DP-700. "
    "Uma das habilidades mais cobradas pela Microsoft na certificação é a capacidade de escolher o item correto de armazenamento e processamento para cada caso de negócio. "
    "Muitos profissionais falham na prova por presumirem que o Lakehouse e o Data Warehouse são intercambiáveis, mas eles possuem características fundamentais distintas. "
    "O Fabric Lakehouse é centralizado no motor Apache Spark. "
    "Ele suporta arquivos estruturados, semiestruturados e não estruturados em pastas Files e Tables. "
    "Sua principal característica no exame é: gravação de dados via PySpark. "
    "O Lakehouse possui um SQL Analytics Endpoint que permite consultar as tabelas Delta via T-SQL, mas este endpoint é estritamente somente leitura. "
    "O Fabric Data Warehouse, por sua vez, é alimentado pelo motor relacional distribuído Polaris. "
    "Ele oferece suporte nativo e completo a comandos T-SQL DML, como INSERT, UPDATE, DELETE e transações multi-tabela com MERGE. "
    "Se o seu cenário exige que analistas de BI alterem registros usando T-SQL tradicional, a escolha mandatória é sempre o Data Warehouse. "
    "O Fabric Eventhouse foi desenhado especificamente para Real-Time Intelligence e séries temporais com KQL. "
    "Ele indexa automaticamente textos e telemetria de sensores IoT e logs de servidores, oferecendo tempos de resposta em milissegundos onde motores relacionais tradicionais sofreriam gargalos. "
    "Por fim, o novo Fabric SQL Database atende a aplicações transacionais operacionais OLTP, espelhando os dados automaticamente para o OneLake. "
    "Três regras de ouro para o Exame DP-700: "
    "Primeiro: Se o enunciado exigir comandos UPDATE ou DELETE via T-SQL, elimine imediatamente a opção Lakehouse SQL Endpoint. "
    "Segundo: Se o cenário envolver cientistas de dados rodando modelos de Machine Learning sobre arquivos não estruturados como imagens e áudios, escolha o Lakehouse. "
    "Terceiro: Para telemetria de alta frequência com agregação contínua por janelas de tempo, a resposta correta é sempre o Eventhouse."
)


async def generate_lesson_0005():
    phonetic_text = apply_phonetic_dictionary(LESSON_0005_SCRIPT)
    print("=== TEXTO FONÉTICO FINAL (LIÇÃO 5) ===")
    print(phonetic_text)
    print("======================================")
    communicate = edge_tts.Communicate(phonetic_text, "pt-BR-AntonioNeural")
    await communicate.save("assets/audio/lesson-0005-pt.mp3")
    print("Arquivo salvo com sucesso em assets/audio/lesson-0005-pt.mp3")


LESSON_0006_SCRIPT = (
    "Lição zero zero zero seis: Integração Zero-Copy: OneLake Shortcuts e Database Mirroring. "
    "Como Integrar Dados Multi-Cloud e Bancos Relacionais Sem Copiar um Único Byte. "
    "Em arquiteturas de dados tradicionais, integrar fontes externas significava criar dezenas de pipelines no Data Factory para extrair, transferir pela rede e duplicar arquivos no armazenamento local. "
    "Isso gerava custos astronômicos de transferência de dados e atrasos na disponibilidade. "
    "O Microsoft Fabric resolve isso através de dois pilares revolucionários: Shortcuts e Mirroring. "
    "Os OneLake Shortcuts são objetos de metadados que funcionam como links simbólicos ou pontes virtuais diretas para armazenamentos externos. "
    "Você pode criar um Shortcut no seu Lakehouse apontando para um bucket do Amazon S3, uma conta do ADLS Gen2, o Google Cloud Storage ou o Dataverse. "
    "Para os motores PySpark, SQL Analytics Endpoint e Power BI Direct Lake, a pasta externa aparece como uma tabela local no OneLake, sem que nenhum arquivo seja movido ou duplicado. "
    "Já o Database Mirroring é a abordagem moderna de Zero-ETL para bancos relacionais operacionais como Azure SQL Database, Snowflake e Cosmos DB. "
    "O Mirroring utiliza a tecnologia de Change Data Capture, ou CDC, para ler as transações dos bancos de origem continuamente e replicá-las em arquivos Delta Parquet no OneLake em poucos segundos. "
    "Isso elimina totalmente a necessidade de engenheiros construírem pipelines complexos de carga incremental. "
    "Pontos críticos para o Exame DP-700: "
    "Primeiro: Se a questão exigir disponibilizar dados de um bucket Amazon S3 no Lakehouse minimizando custos de armazenamento e eliminando a duplicação física, a resposta é sempre criar um OneLake Shortcut. "
    "Segundo: Shortcuts internos entre workspaces no Fabric permitem que múltiplos times compartilhem a mesma tabela Silver ou Gold sem duplicar os arquivos Delta subjacentes. "
    "Terceiro: No Database Mirroring, o banco de dados operacional precisa ter o CDC habilitado e a retenção de log configurada adequadamente para garantir a sincronização contínua."
)


async def generate_lesson_0006():
    phonetic_text = apply_phonetic_dictionary(LESSON_0006_SCRIPT)
    print("=== TEXTO FONÉTICO FINAL (LIÇÃO 6) ===")
    print(phonetic_text)
    print("======================================")
    communicate = edge_tts.Communicate(phonetic_text, "pt-BR-AntonioNeural")
    await communicate.save("assets/audio/lesson-0006-pt.mp3")
    print("Arquivo salvo com sucesso em assets/audio/lesson-0006-pt.mp3")


LESSON_0007_SCRIPT = (
    "Lição zero zero zero sete: Orquestração de Dados: Data Factory Pipelines, Copy Job, Dataflows Gen2 e Notebooks em DAG. "
    "Como Construir Fluxos de Dados Confiáveis, Resilientes e Escaláveis no Microsoft Fabric. "
    "A ingestão e transformação de dados em escala empresarial exige muito mais do que escrever scripts isolados: exige orquestração. "
    "No Microsoft Fabric, você dispõe de quatro ferramentas principais de ingestão e fluxo de dados. "
    "Primeiro: O Copy Job. É o recurso mais simples e rápido para ingestão sem código, ideal para trazer tabelas brutas de fontes comuns diretamente para a camada Bronze. "
    "Segundo: Os Dataflows Gen2. São a evolução em nuvem do Power Query M. "
    "Eles são ideais para profissionais que preferem uma interface visual de baixo código para mesclar, filtrar e aplicar tipagem em dados. "
    "Um diferencial crucial dos Dataflows Gen2 no Fabric é o uso de um Lakehouse interno de Staging, que permite processar grandes transformações com alto desempenho e gravar o resultado final diretamente no OneLake. "
    "Terceiro: Os Data Factory Pipelines. Eles são a espinha dorsal de orquestração do ecossistema. "
    "Pipelines não apenas executam atividades de cópia, mas gerenciam o fluxo de controle com laços ForEach, condições If-Else, chamadas de WebHooks para APIs e políticas de repetição contra falhas transientes. "
    "Quarto: A orquestração avançada em PySpark via mssparkutils. "
    "A biblioteca utilitária do Spark no Fabric oferece a função notebook.runMultiple, que permite definir e disparar um Grafo Acíclico Dirigido, ou DAG, "
    "executando múltiplos notebooks em paralelo com limites de concorrência e dependências sequenciais. "
    "Pontos críticos para o Exame DP-700: "
    "Primeiro: Se a questão descrever um cenário de transformação com interface visual amigável para analistas de negócios, a resposta é Dataflows Gen2. "
    "Segundo: Se for exigido controle rigoroso de falhas, notificações e orquestração de atividades sequenciais dependentes, utilize um Data Factory Pipeline. "
    "Terceiro: Para orquestrar dezenas de notebooks Spark respeitando dependências entre camadas Bronze, Silver e Gold em lote, a solução oficial é a função mssparkutils.notebook.runMultiple."
)


async def generate_lesson_0007():
    phonetic_text = apply_phonetic_dictionary(LESSON_0007_SCRIPT)
    print("=== TEXTO FONÉTICO FINAL (LIÇÃO 7) ===")
    print(phonetic_text)
    print("======================================")
    communicate = edge_tts.Communicate(phonetic_text, "pt-BR-AntonioNeural")
    await communicate.save("assets/audio/lesson-0007-pt.mp3")
    print("Arquivo salvo com sucesso em assets/audio/lesson-0007-pt.mp3")


LESSON_0008_SCRIPT = (
    "Lição zero zero zero oito: Padrões de Carga Incremental, Watermarking, Change Data Capture e SCD Tipo Um, Dois e Três. "
    "Como Processar Apenas Dados Novos e Preservar o Histórico do Negócio. "
    "Em cenários de produção com bilhões de registros, recarregar a base inteira todos os dias é proibitivo em tempo e custo computacional. "
    "A solução padrão da engenharia de dados é a Carga Incremental. "
    "O método mais adotado é o High Watermarking. "
    "Uma tabela de controle de metadados armazena o último valor de data e hora ou número sequencial extraído com sucesso. "
    "Na próxima execução do pipeline, a consulta extrai apenas os registros com data superior à marca d'água anterior, atualizando o marcador ao final do processo. "
    "Uma alternativa ainda mais eficiente é o Change Data Capture, ou CDC, que intercepta inserções, atualizações e exclusões lendo diretamente os logs transacionais do banco de dados na origem sem onerar os índices. "
    "Após a ingestão, os dados dimensionais sofrem alterações ao longo do tempo, o que é resolvido pelo padrão Slowly Changing Dimensions, ou SCD. "
    "No SCD Tipo Um, o valor antigo é simplesmente sobrescrito pelo valor novo. O custo de armazenamento é mínimo, mas perde-se todo o histórico anterior. "
    "No SCD Tipo Dois, o histórico completo é preservado. Quando um cliente muda de endereço, o registro anterior tem sua data de expiração ValidTo preenchida e a flag IsCurrent alterada para falso. "
    "Em seguida, uma nova linha é inserida com uma nova Surrogate Key inteira e IsCurrent verdadeiro. "
    "Pontos críticos para o Exame DP-700: "
    "Primeiro: Se o cenário de negócio exigir rastreabilidade de vendas históricas atribuídas ao endereço que o cliente residia no momento da compra, a resposta obrigatória é implementar SCD Tipo Dois. "
    "Segundo: A instrução T-SQL MERGE no Fabric Data Warehouse ou o comando Delta merge em PySpark são as ferramentas recomendadas para implementar SCD Tipo Dois de forma atômica e consistente. "
    "Terceiro: Para cargas incrementais baseadas em data com múltiplos fusos horários, padronize sempre a marca d'água no fuso UTC para evitar perda ou duplicação de dados durante transições de horário de verão."
)


async def generate_lesson_0008():
    phonetic_text = apply_phonetic_dictionary(LESSON_0008_SCRIPT)
    print("=== TEXTO FONÉTICO FINAL (LIÇÃO 8) ===")
    print(phonetic_text)
    print("======================================")
    communicate = edge_tts.Communicate(phonetic_text, "pt-BR-AntonioNeural")
    await communicate.save("assets/audio/lesson-0008-pt.mp3")
    print("Arquivo salvo com sucesso em assets/audio/lesson-0008-pt.mp3")


LESSON_0009_SCRIPT = (
    "Lição zero zero zero nove: Transformações Batch em PySpark e T-SQL: MERGE INTO, COPY INTO, CTAS, Schema Evolution e Zero-Copy Table Clones. "
    "Mecanismos Avançados de Transformação e Carga em Lote no Microsoft Fabric. "
    "A etapa de transformação é onde os dados brutos da camada Bronze são purificados e agregados para alimentar modelos analíticos de negócio. "
    "No Microsoft Fabric, você conta com um arsenal robusto de comandos tanto no motor relacional Polaris do Warehouse quanto no motor Apache Spark do Lakehouse. "
    "No Fabric Data Warehouse, o comando COPY INTO é o padrão de excelência para carregar centenas de gigabytes de arquivos externos em tabelas relacionais com alto paralelismo nativo. "
    "Para criar tabelas agregadas derivadas, a instrução CTAS, ou CREATE TABLE AS SELECT, compila e persiste o resultado de consultas analíticas pesadas diretamente em novos arquivos Delta. "
    "Quando novos dados chegam contendo registros existentes atualizados e registros inéditos, a instrução MERGE INTO realiza a reconciliação em uma única transação atômica. "
    "Já no Lakehouse, a evolução das estruturas de negócio é administrada pelo recurso de Schema Evolution do Delta Lake. "
    "Ao configurar a opção mergeSchema igual a true no PySpark, novas colunas detectadas no fluxo de entrada são incorporadas automaticamente ao esquema da tabela sem interromper o pipeline. "
    "Por fim, para ambientes de homologação e validação de relatórios, o Fabric Data Warehouse disponibiliza a funcionalidade de Zero-Copy Table Clone por meio da sintaxe CREATE TABLE AS CLONE OF. "
    "Um clone de tabela copia instantaneamente apenas os metadados do OneLake, permitindo testes sem duplicar o custo de armazenamento. "
    "Pontos críticos para o Exame DP-700: "
    "Primeiro: Para clonar uma tabela de produção para um ambiente de testes no Warehouse sem incorrer em custos adicionais de armazenamento no OneLake, a resposta é CREATE TABLE AS CLONE OF. "
    "Segundo: Se um pipeline em PySpark falhar ao ingerir um arquivo Delta devido a novas colunas adicionadas na origem, resolva ativando a opção mergeSchema igual a true. "
    "Terceiro: No Fabric Data Warehouse, utilize a instrução MERGE INTO para realizar operações combinadas de inserção e atualização atômica em uma única etapa."
)


async def generate_lesson_0009():
    phonetic_text = apply_phonetic_dictionary(LESSON_0009_SCRIPT)
    print("=== TEXTO FONÉTICO FINAL (LIÇÃO 9) ===")
    print(phonetic_text)
    print("======================================")
    communicate = edge_tts.Communicate(phonetic_text, "pt-BR-AntonioNeural")
    await communicate.save("assets/audio/lesson-0009-pt.mp3")
    print("Arquivo salvo com sucesso em assets/audio/lesson-0009-pt.mp3")


LESSON_0010_SCRIPT = (
    "Lição zero zero um zero: Engenharia de Streaming: Eventstreams e Spark Structured Streaming. "
    "Como Processar Fluxos Contínuos de Alta Velocidade e Gerenciar Janelas Temporais no Fabric. "
    "A necessidade de tomar decisões em tempo real exige que a engenharia de dados migre de rotinas batch diárias para arquiteturas contínuas de streaming. "
    "No Microsoft Fabric, você dispõe de duas ferramentas complementares para lidar com fluxos de eventos em alta velocidade. "
    "Primeiro: O Fabric Eventstreams. É a solução no-code e low-code do ecossistema de Real-Time Intelligence. "
    "Ele se conecta nativamente a hubs como Azure Event Hubs, Apache Kafka e IoT Hub, permitindo filtrar, transformar e rotear eventos sem escrever uma linha de código, "
    "enviando os dados diretamente para um Eventhouse em KQL ou para tabelas Delta no Lakehouse. "
    "Segundo: O Spark Structured Streaming no Fabric Lakehouse. "
    "É a solução de código para transformações complexas de streaming utilizando a API DataFrame do PySpark. "
    "Para calcular métricas agregadas sobre fluxos contínuos, a Microsoft cobra o domínio rigoroso dos tipos de janelas temporais. "
    "A Tumbling Window divide o tempo em blocos fixos e contíguos sem sobreposição, como a cada cinco minutos exatos. "
    "A Hopping Window cria janelas que se sobrepõem, como uma janela de dez minutos que avança a cada cinco minutos, ideal para médias móveis. "
    "A Sliding Window avalia dados continuamente quando um novo evento chega. "
    "E a Session Window agrupa eventos por períodos de atividade, fechando a janela após um tempo estipulado de inatividade do usuário. "
    "Para lidar com dados que chegam atrasados devido a falhas de rede, o Spark utiliza a cláusula withWatermark. "
    "O watermark define quanto tempo o motor deve manter o estado em memória aguardando eventos atrasados antes de descartá-los e liberar recursos. "
    "Pontos críticos para o Exame DP-700: "
    "Primeiro: Se a questão exigir calcular agregações em janelas temporais fixas sem qualquer sobreposição entre períodos, selecione Tumbling Window. "
    "Segundo: Para calcular médias móveis onde cada período de dez minutos se sobrepõe ao anterior avançando a cada cinco minutos, selecione Hopping Window. "
    "Terceiro: Para tolerar atrasos de rede de até quinze minutos em pipelines de PySpark Structured Streaming, configure a função withWatermark com quinze minutos."
)


async def generate_lesson_0010():
    phonetic_text = apply_phonetic_dictionary(LESSON_0010_SCRIPT)
    print("=== TEXTO FONÉTICO FINAL (LIÇÃO 10) ===")
    print(phonetic_text)
    print("=======================================")
    communicate = edge_tts.Communicate(phonetic_text, "pt-BR-AntonioNeural")
    await communicate.save("assets/audio/lesson-0010-pt.mp3")
    print("Arquivo salvo com sucesso em assets/audio/lesson-0010-pt.mp3")


LESSON_0011_SCRIPT = (
    "Lição zero zero um um: Domínio de KQL, Eventhouse, Update Policies e Materialized Views. "
    "Consultas Analíticas em Milissegundos e Transformação de Streaming em Tempo Real. "
    "O ecossistema de Real-Time Intelligence no Microsoft Fabric é alimentado pelo Kusto Engine, operado por meio da linguagem KQL, ou Kusto Query Language. "
    "Diferente do T-SQL relacional ou do processamento em lotes do PySpark, o KQL foi projetado para consultar bilhões de eventos de telemetria, logs de auditoria e séries temporais com latências de milissegundos. "
    "O segredo da velocidade do KQL reside na indexação automática de texto completo e na compressão colunar nativa em memória. "
    "Para transformar dados de streaming no momento exato em que chegam ao Eventhouse sem depender de pipelines externos no Data Factory, o Fabric disponibiliza as Update Policies. "
    "Uma Update Policy é anexada à tabela destino e executa uma função KQL de forma transacional toda vez que um lote de mensagens é ingerido na tabela de origem. "
    "Isso permite converter strings de JSON usando parse_json, expandir arrays com mv-expand e tipar colunas sem gerar latência perceptível. "
    "Para cálculos analíticos pesados e frequentes, como médias horárias e contadores por dispositivo, a solução recomendada são as Materialized Views. "
    "Ao contrário de views comuns que recalculam tudo do zero a cada consulta, as Materialized Views mantêm o resultado pré-computado de forma incremental à medida que novos dados chegam. "
    "Pontos críticos para o Exame DP-700: "
    "Primeiro: Quando o enunciado exigir transformar e limpar dados de streaming na ingestão de um Eventhouse sem usar pipelines adicionais, a resposta é Update Policy. "
    "Segundo: Em filtros de texto, o operador has busca termos completos utilizando o índice invertido, sendo ordens de magnitude mais rápido que o operador contains, que realiza varredura linear lenta. "
    "Terceiro: Para capturar a leitura mais recente de cada sensor IoT em uma tabela com centenas de milhões de linhas, utilize o operador summarize arg_max."
)


async def generate_lesson_0011():
    phonetic_text = apply_phonetic_dictionary(LESSON_0011_SCRIPT)
    print("=== TEXTO FONÉTICO FINAL (LIÇÃO 11) ===")
    print(phonetic_text)
    print("=======================================")
    communicate = edge_tts.Communicate(phonetic_text, "pt-BR-AntonioNeural")
    await communicate.save("assets/audio/lesson-0011-pt.mp3")
    print("Arquivo salvo com sucesso em assets/audio/lesson-0011-pt.mp3")


LESSON_0012_SCRIPT = (
    "Lição zero zero um dois: Segurança Fim a Fim, Governança, RLS, CLS, DDM e a Prevenção do Direct Lake Fallback. "
    "Protegendo Dados Corporativos e Garantindo Máxima Performance no Power BI. "
    "No ecossistema unificado do Microsoft Fabric, a segurança deve operar em múltiplas camadas harmonizadas, desde o acesso ao workspace até o nível de células e linhas de tabelas. "
    "Na governança de acesso aos workspaces, existem quatro papéis fundamentais: "
    "Admin tem controle total de configuração e exclusão. "
    "Member pode criar itens e conceder permissões a outros usuários. "
    "Contributor pode criar e executar pipelines e notebooks, mas não altera permissões do workspace. "
    "E Viewer tem permissão estritamente de somente leitura nos relatórios e dados servidos. "
    "Para segurança granular nos motores relacionais do Fabric Data Warehouse, você dispõe de recursos consagrados do T-SQL: "
    "Row-Level Security, ou RLS, que filtra linhas com base na identidade do usuário logado; "
    "Column-Level Security, ou CLS, que restringe colunas confidenciais como salários ou CPFs; "
    "E Dynamic Data Masking, ou DDM, que mascara dados sensíveis em tempo de execução sem alterar os arquivos físicos no OneLake. "
    "No entanto, para o Exame DP-700, o tópico mais crítico de segurança é o Direct Lake Fallback no Power BI. "
    "O modo Direct Lake carrega arquivos Delta Parquet do OneLake diretamente para a memória do motor VertiPaq, entregando relatórios instantâneos. "
    "Porém, se você configurar RLS diretamente na tabela Delta via SQL Analytics Endpoint do Lakehouse, "
    "o Power BI perde a capacidade de carregar os dados puros em memória e sofre Fallback automático para o modo DirectQuery, tornando as consultas lentas. "
    "Para aplicar restrições de RLS preservando a velocidade ultrarrápida do Direct Lake, "
    "a Microsoft recomenda configurar o RLS diretamente no Modelo Semântico do Power BI, utilizando uma identidade fixa para ler a tabela no Lakehouse. "
    "Pontos críticos para o Exame DP-700: "
    "Primeiro: Para permitir que um desenvolvedor execute e crie notebooks sem conceder privilégio de gerenciar acessos ao workspace, atribua o papel de Contributor. "
    "Segundo: A aplicação de RLS no SQL Endpoint do Lakehouse força o Fallback do Power BI Direct Lake para DirectQuery. "
    "Terceiro: Para governança empresarial, utilize rótulos de sensibilidade do Microsoft Purview para rastrear e criptografar automaticamente artefatos confidenciais em todo o tenant."
)


async def generate_lesson_0012():
    phonetic_text = apply_phonetic_dictionary(LESSON_0012_SCRIPT)
    print("=== TEXTO FONÉTICO FINAL (LIÇÃO 12) ===")
    print(phonetic_text)
    print("=======================================")
    communicate = edge_tts.Communicate(phonetic_text, "pt-BR-AntonioNeural")
    await communicate.save("assets/audio/lesson-0012-pt.mp3")
    print("Arquivo salvo com sucesso em assets/audio/lesson-0012-pt.mp3")


LESSON_0013_SCRIPT = (
    "Lição zero zero um três: Integração Contínua e Entrega Contínua, Integração com Git e Pipelines de Implantação. "
    "Gerenciando o Ciclo de Vida da Engenharia de Dados em Escala Empresarial. "
    "O desenvolvimento profissional de engenharia de dados em grandes organizações não permite edições manuais e descontroladas diretamente no ambiente de produção. "
    "O Microsoft Fabric implementa o ciclo de vida de desenvolvimento por meio de dois pilares integrados: a integração com Git e os Deployment Pipelines. "
    "Com a integração nativa com Git, você pode conectar o seu workspace do Fabric diretamente a um repositório no Azure DevOps ou no GitHub. "
    "Cada artefato do Fabric — sejam notebooks PySpark, definições de Data Factory Pipelines, esquemas de Data Warehouse ou modelos semânticos — "
    "é serializado em arquivos de metadados declarativos em formato legível no repositório. "
    "Isso viabiliza a criação de branches individuais para desenvolvedores, rastreamento de alterações com histórico de commits e revisão formal de código por meio de Pull Requests. "
    "Para a promoção controlada de artefatos entre estágios, o Fabric disponibiliza os Deployment Pipelines, organizados nas fases de Desenvolvimento, Teste e Produção. "
    "Um dos recursos mais exigidos no Exame DP-700 são as Deployment Rules, ou Regras de Implantação. "
    "As Deployment Rules permitem que, ao promover um relatório ou pipeline para o ambiente de produção, "
    "as conexões de bancos de dados e parâmetros de consulta sejam automaticamente remapeados para os servidores produtivos sem que você precise editar uma única linha de código. "
    "Pontos críticos para o Exame DP-700: "
    "Primeiro: A integração com Git sincroniza o workspace com branches do Azure DevOps ou GitHub, permitindo controle de versão e reconciliação de diferenças com os botões Commit e Update. "
    "Segundo: Para alterar automaticamente a cadeia de conexão de um banco SQL de desenvolvimento para o servidor de produção durante a publicação, configure uma Deployment Rule no Deployment Pipeline. "
    "Terceiro: Para gerenciar o ciclo de vida declarativo de tabelas e esquemas de um Fabric Data Warehouse com compilação e validação prévia de integridade, utilize Database Projects com arquivos sqlproj."
)


LESSON_0014_SCRIPT = (
    "Lição zero zero um quatro: Otimização de Performance, V-Order, Liquid Clustering e Tuning de Consultas. "
    "Atingindo o Estado da Arte em Eficiência e Subsegundo no Microsoft Fabric. "
    "Em arquiteturas de Lakehouse e Data Warehouse no Fabric, a velocidade das consultas analíticas e o consumo de Capacity Units dependem diretamente de como os dados são organizados no OneLake. "
    "O primeiro grande acelerador é o V-Order. O V-Order é uma otimização no nível de gravação do formato Parquet que reordena linhas e aplica dicionários especializados para coincidir perfeitamente com o algoritmo de compressão in-memory do VertiPaq no Power BI e do motor T-SQL. Com o V-Order habilitado por padrão em todos os motores do Fabric, o modo Direct Lake alcança tempos de resposta de subsegundo sem necessidade de importação. "
    "Para a organização física de tabelas Delta de grande porte, o Fabric introduziu o Liquid Clustering. Diferente do particionamento rígido tradicional por pastas de data ou do Z-Order clássico — que exigia reescrever todos os dados com o comando OPTIMIZE —, o Liquid Clustering com a cláusula CLUSTER BY reestrutura os dados incrementalmente sem reescrever partições inteiras e suporta colunas de alta cardinalidade. "
    "Para a manutenção do OneLake, o comando VACUUM limpa arquivos físicos obsoletos marcados como excluídos. Atenção crítica: O limiar padrão do VACUUM é de sete dias. Reduzir a retenção para zero impede permanentemente consultas históricas via Time Travel. "
    "Pontos críticos para o Exame DP-700: "
    "Primeiro: O V-Order otimiza arquivos Parquet em tempo de escrita, reduzindo tamanho em disco e maximizando leituras no Direct Lake sem quebrar a compatibilidade aberta do formato. "
    "Segundo: Para tabelas Delta massivas com padrões de consulta imprevisíveis e mutáveis, adote Liquid Clustering com CLUSTER BY em vez de particionamento estático. "
    "Terceiro: Para mitigar desbalanceamento de partições e tarefas lentas por Data Skew no Apache Spark, habilite o Adaptive Query Execution com skewJoin ou aplique Salting manual na chave de junção."
)


async def generate_lesson_0013():
    phonetic_text = apply_phonetic_dictionary(LESSON_0013_SCRIPT)
    print("=== TEXTO FONÉTICO FINAL (LIÇÃO 13) ===")
    print(phonetic_text)
    print("=======================================")
    communicate = edge_tts.Communicate(phonetic_text, "pt-BR-AntonioNeural")
    await communicate.save("assets/audio/lesson-0013-pt.mp3")
    print("Arquivo salvo com sucesso em assets/audio/lesson-0013-pt.mp3")


LESSON_0015_SCRIPT = (
    "Lição zero zero um cinco: Monitoramento, Diagnóstico de Falhas, Fabric Capacity Metrics App e DMVs de Consulta. "
    "Garantindo Alta Disponibilidade e Observabilidade na Engenharia de Dados do Microsoft Fabric. "
    "Manter pipelines analíticos em produção exige observabilidade contínua tanto no nível do cluster quanto no nível da capacidade corporativa. "
    "O Microsoft Fabric disponibiliza o Monitoring Hub como painel central unificado para rastrear o status de cada execução de Data Pipeline, notebook Spark e fluxo do Dataflows Gen2, com acesso direto a logs detalhados de erros e ao Spark History Server. "
    "Para a governança de consumo de recursos computacionais, o Fabric Capacity Metrics App é a ferramenta definitiva exigida no Exame DP-700. O aplicativo categoriza o consumo em operações interativas — como consultas visuais do Power BI e notebooks ad-hoc, suavizadas em janelas curtas de cinco minutos — e operações em background — como pipelines agendados e ingestão pesada, suavizadas em vinte e quatro horas. "
    "Quando a capacidade entra em sobrecarga, o Fabric aciona três estágios progressivos de estrangulamento: primeiro, o Interactive Delay, aplicando um atraso de sessenta segundos para desestimular consultas simultâneas; segundo, o Interactive Rejection, rejeitando imediatamente novas consultas interativas; e terceiro, o Background Rejection, impedindo a inicialização de novos pipelines agendados. "
    "Para diagnosticar consultas lentas ou que consom excesso de CPU no Fabric Data Warehouse, utilize o esquema nativo de queryinsights, consultando as visões exec_requests_history, frequently_run_queries e long_running_queries. "
    "Pontos críticos para o Exame DP-700: "
    "Primeiro: O Fabric Capacity Metrics App distingue operações interativas com janela de cinco minutos de operações em background com janela de vinte e quatro horas. "
    "Segundo: O primeiro sintoma de sobrecarga de capacidade é o Interactive Delay, atrasando consultas antes de começar a rejeitá-las. "
    "Terceiro: Para identificar quais consultas T-SQL consumiram maior tempo de CPU no Data Warehouse, consulte a view queryinsights.exec_requests_history ordenando por allocated_cpu_time_ms."
)


async def generate_lesson_0014():
    phonetic_text = apply_phonetic_dictionary(LESSON_0014_SCRIPT)
    print("=== TEXTO FONÉTICO FINAL (LIÇÃO 14) ===")
    print(phonetic_text)
    print("=======================================")
    communicate = edge_tts.Communicate(phonetic_text, "pt-BR-AntonioNeural")
    await communicate.save("assets/audio/lesson-0014-pt.mp3")
    print("Arquivo salvo com sucesso em assets/audio/lesson-0014-pt.mp3")


async def generate_lesson_0015():
    phonetic_text = apply_phonetic_dictionary(LESSON_0015_SCRIPT)
    print("=== TEXTO FONÉTICO FINAL (LIÇÃO 15) ===")
    print(phonetic_text)
    print("=======================================")
    communicate = edge_tts.Communicate(phonetic_text, "pt-BR-AntonioNeural")
    await communicate.save("assets/audio/lesson-0015-pt.mp3")
    print("Arquivo salvo com sucesso em assets/audio/lesson-0015-pt.mp3")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "0002":
        asyncio.run(generate_lesson_0002())
    elif len(sys.argv) > 1 and sys.argv[1] == "0003":
        asyncio.run(generate_lesson_0003())
    elif len(sys.argv) > 1 and sys.argv[1] == "0004":
        asyncio.run(generate_lesson_0004())
    elif len(sys.argv) > 1 and sys.argv[1] == "0005":
        asyncio.run(generate_lesson_0005())
    elif len(sys.argv) > 1 and sys.argv[1] == "0006":
        asyncio.run(generate_lesson_0006())
    elif len(sys.argv) > 1 and sys.argv[1] == "0007":
        asyncio.run(generate_lesson_0007())
    elif len(sys.argv) > 1 and sys.argv[1] == "0008":
        asyncio.run(generate_lesson_0008())
    elif len(sys.argv) > 1 and sys.argv[1] == "0009":
        asyncio.run(generate_lesson_0009())
    elif len(sys.argv) > 1 and sys.argv[1] == "0010":
        asyncio.run(generate_lesson_0010())
    elif len(sys.argv) > 1 and sys.argv[1] == "0011":
        asyncio.run(generate_lesson_0011())
    elif len(sys.argv) > 1 and sys.argv[1] == "0012":
        asyncio.run(generate_lesson_0012())
    elif len(sys.argv) > 1 and sys.argv[1] == "0013":
        asyncio.run(generate_lesson_0013())
    elif len(sys.argv) > 1 and sys.argv[1] == "0014":
        asyncio.run(generate_lesson_0014())
    elif len(sys.argv) > 1 and sys.argv[1] == "0015":
        asyncio.run(generate_lesson_0015())
    else:
        asyncio.run(generate_lesson_0001())














"""
DOMÍNIO 2: INGERIR E TRANSFORMAR DADOS (40-45%)
82 Questões Completas (Single-Choice e Multi-Select)
Padrão Oficial Pearson VUE DP-700
"""

def make_explanation(correct_text, distractors_list, tip_text):
    dist_html = "".join([f"<li>{d}</li>" for d in distractors_list])
    return f"""<div class="explanation-correct"><strong>✅ Por que a alternativa correta está certa:</strong> {correct_text}</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
{dist_html}
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> {tip_text}</div>"""

DOMAIN_2_QUESTIONS = [
    # --- DATA FACTORY & PIPELINES (Questões 1 a 18) ---
    {
        "id": "d2_q01",
        "domain": "domain2",
        "type": "single",
        "title": "Limite Máximo da Atividade Lookup no Data Factory",
        "question": "Um engenheiro de dados está criando um Data Pipeline no Microsoft Fabric para carregar uma lista de tabelas a serem processadas usando uma atividade Lookup. Quantas linhas no máximo a atividade Lookup pode retornar em uma única execução?",
        "options": [
            {"id": "A", "text": "1.000 linhas", "isCorrect": False},
            {"id": "B", "text": "5.000 linhas", "isCorrect": True},
            {"id": "C", "text": "50.000 linhas", "isCorrect": False},
            {"id": "D", "text": "100.000 linhas", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A atividade Lookup nos Data Pipelines do Microsoft Fabric possui um limite rígido documentado de no máximo 5.000 linhas (ou 4 MB de dados). Se o conjunto de dados retornado ultrapassar esse volume, apenas as primeiras 5.000 linhas são retornadas.",
            [
                "<strong>A (1.000 linhas):</strong> Menor do que o limite da atividade.",
                "<strong>C e D (50.000 e 100.000 linhas):</strong> Limites inexistentes para a atividade Lookup. Cargas volumosas exigem processamento via Script, Dataflow ou Spark."
            ],
            "Limite do Lookup: 5.000 linhas ou 4 MB de tamanho de buffer JSON."
        )
    },
    {
        "id": "d2_q02",
        "domain": "domain2",
        "type": "single",
        "title": "Paralelismo Máximo na Atividade ForEach",
        "question": "Ao iterar sobre um conjunto de 100 arquivos usando a atividade ForEach em um Data Pipeline do Fabric, qual é o valor máximo permitido para a propriedade `batchCount` (paralelismo simultâneo)?",
        "options": [
            {"id": "A", "text": "10", "isCorrect": False},
            {"id": "B", "text": "20", "isCorrect": False},
            {"id": "C", "text": "50", "isCorrect": True},
            {"id": "D", "text": "100", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A atividade ForEach suporta execução paralela com um `batchCount` máximo de 50 iterações simultâneas. Se o switch 'Sequential' estiver ativado, o batchCount é ignorado e executa 1 por 1.",
            [
                "<strong>A e B:</strong> Valores válidos, mas não representam o teto máximo permitido de concorrência.",
                "<strong>D:</strong> O Fabric limita a concorrência a no máximo 50 para evitar esgotamento prematuro de recursos."
            ],
            "ForEach batchCount máximo = 50 iterações concorrentes."
        )
    },
    {
        "id": "d2_q03",
        "domain": "domain2",
        "type": "single",
        "title": "Diferença entre Atividade Web e Atividade WebHook",
        "question": "Você precisa integrar um Data Pipeline com um serviço externo de aprovação assíncrono que leva até 40 minutos para responder com um token de liberação. Qual atividade de pipeline deve ser utilizada?",
        "options": [
            {"id": "A", "text": "Atividade Web com timeout de 1 minuto.", "isCorrect": False},
            {"id": "B", "text": "Atividade WebHook, pois ela envia uma URL de callback e aguarda até que o serviço externo faça uma requisição POST de volta com o status concluído.", "isCorrect": True},
            {"id": "C", "text": "Atividade Get Metadata conectada a uma pasta vazia.", "isCorrect": False},
            {"id": "D", "text": "Atividade Copy em loop infinito.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A atividade WebHook é projetada especificamente para processos assíncronos de longa duração. Ao invocar a API de destino, ela inclui uma URL de retorno (`callBackUri`). A execução do pipeline pausa até que o serviço externo chame essa URL de volta com o payload de resposta.",
            [
                "<strong>A:</strong> A atividade Web é síncrona e possui timeout estrito de requisição HTTP (geralmente até 10 minutos).",
                "<strong>C e D:</strong> Atividades que não realizam integração de callback HTTP."
            ],
            "Web = Chamada síncrona imediata; WebHook = Chamada assíncrona com espera de callBackUri."
        )
    },
    {
        "id": "d2_q04",
        "domain": "domain2",
        "type": "single",
        "title": "Mecanismo de Fast Copy nos Dataflows Gen2",
        "question": "Qual é a principal função do recurso 'Fast Copy' (Cópia Rápida) nos Dataflows Gen2 do Microsoft Fabric?",
        "options": [
            {"id": "A", "text": "Utilizar a engine distribuída de ingestão do backend (semelhante à Copy Activity) para carregar grandes volumes de dados de fontes externas diretamente para o Staging Lakehouse sem sobrecarregar a engine de Mashup do Power Query.", "isCorrect": True},
            {"id": "B", "text": "Ignorar a validação de tipos de dados e inserir registros corrompidos na tabela final.", "isCorrect": False},
            {"id": "C", "text": "Excluir os dados da fonte original após a leitura.", "isCorrect": False},
            {"id": "D", "text": "Comprimir todos os dados em arquivos MP3 para economizar espaço.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fast Copy nos Dataflows Gen2 contorna as limitações de memória do motor local de Mashup do Power Query ao delegar a cópia de grandes tabelas relacionais ou arquivos para a infraestrutura escalável do Data Factory, gravando em alta velocidade no Lakehouse de Staging.",
            [
                "<strong>B, C e D:</strong> Efeitos incorretos e sem embasamento técnico."
            ],
            "Fast Copy no Dataflow Gen2 acelera a ingestão massiva gravando em Staging antes das transformações do Power Query."
        )
    },
    {
        "id": "d2_q05",
        "domain": "domain2",
        "type": "single",
        "title": "Lakehouse de Preparo (Staging Lakehouse) dos Dataflows Gen2",
        "question": "Ao criar e executar um Dataflow Gen2 em um Workspace do Fabric, dois artefatos adicionais com sufixos técnicos são criados automaticamente no Workspace. Quais são esses artefatos e qual a sua finalidade?",
        "options": [
            {"id": "A", "text": "Dois bancos de dados SQL Server Express locais.", "isCorrect": False},
            {"id": "B", "text": "Um Lakehouse de Staging e um SQL Analytics Endpoint de Staging, utilizados internamente pelo motor do Fabric para materializar dados intermediários e acelerar transformações com compute SQL.", "isCorrect": True},
            {"id": "C", "text": "Dois relatórios visuais de demonstração do Power BI.", "isCorrect": False},
            {"id": "D", "text": "Duas conexões ODBC legadas com o MS Access.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Os Dataflows Gen2 utilizam um Lakehouse de Staging dedicado (e seu respectivo SQL Endpoint). As etapas de transformação do Power Query são materializadas no OneLake em Delta Parquet, e as consultas subsequentes utilizam o motor T-SQL do SQL Endpoint para executar query folding acelerado por hardware.",
            [
                "<strong>A, C e D:</strong> Artefatos que não fazem parte da arquitetura interna dos Dataflows Gen2."
            ],
            "Dataflows Gen2 geram automaticamente um Lakehouse e SQL Endpoint de Staging para computação intermediária acelerada."
        )
    },
    {
        "id": "d2_q06",
        "domain": "domain2",
        "type": "single",
        "title": "Dataflows Gen2 vs Apache Spark Notebooks",
        "question": "Uma organização tem dois perfis de profissionais de dados: analistas de negócios que dominam Power Query e engenheiros de dados que desenvolvem pipelines analíticos de alta complexidade com machine learning e tratamento de petabytes. Qual é a recomendação oficial de uso no Fabric?",
        "options": [
            {"id": "A", "text": "Usar Dataflows Gen2 para transformações no-code/low-code em nível departamental e Spark Notebooks para engenharia de dados em grande escala e transformações complexas com PySpark/Scala.", "isCorrect": True},
            {"id": "B", "text": "Proibir o uso de Spark e forçar todos a usar apenas Dataflows Gen2.", "isCorrect": False},
            {"id": "C", "text": "Usar apenas T-SQL e descartar Notebooks e Dataflows.", "isCorrect": False},
            {"id": "D", "text": "Exportar os dados para planilhas manuais compartilhadas por e-mail.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A Microsoft recomenda Dataflows Gen2 para usuários que preferem desenvolvimento visual baseado em Power Query com facilidade de manutenção para volumes médios. Para grandes volumes (TB/PB), algoritmos complexos, machine learning e concorrência massiva, Spark Notebooks é a ferramenta primordial.",
            [
                "<strong>B, C e D:</strong> Recomendações contrárias às diretrizes oficiais do exame DP-700."
            ],
            "Diretriz oficial: Low-Code/Power Query -> Dataflows Gen2; Big Data/PySpark/Escalabilidade -> Spark Notebooks."
        )
    },
    {
        "id": "d2_q07",
        "domain": "domain2",
        "type": "single",
        "title": "Carga Incremental com Tabela de Watermark em Pipelines",
        "question": "Um pipeline do Fabric precisa realizar carga incremental a cada hora lendo dados de uma tabela SQL corporativa de 500 milhões de registros. Como o padrão de Watermark com a atividade Lookup e Copy deve ser implementado?",
        "options": [
            {"id": "A", "text": "Fazer SELECT * sem cláusula WHERE e sobrescrever a tabela de destino inteira a cada hora.", "isCorrect": False},
            {"id": "B", "text": "Consultar a última data/hora processada na tabela de controle (Watermark), buscar novos registros com `WHERE DataModificacao > @UltimaData`, gravar no destino e atualizar a tabela de controle com o novo timestamp.", "isCorrect": True},
            {"id": "C", "text": "Apagar a tabela SQL de origem após cada execução.", "isCorrect": False},
            {"id": "D", "text": "Executar o pipeline apenas uma vez por ano.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O padrão Watermark é a técnica padrão de engenharia para cargas incrementais: 1) Lookup lê a última marca d'água (`OldWatermark`), 2) Lookup calcula a nova marca máxima (`NewWatermark`), 3) Copy transfere dados entre `OldWatermark` e `NewWatermark`, 4) Script/Stored Procedure atualiza a tabela de controle.",
            [
                "<strong>A:</strong> Carga plena horária em 500M de linhas causa sobrecarga severa e desperdício de CUs.",
                "<strong>C:</strong> Deletar dados da fonte de origem é inaceitável em ambientes corporativos."
            ],
            "Padrão Watermark: Old Watermark -> Copy Delta -> Update New Watermark."
        )
    },
    {
        "id": "d2_q08",
        "domain": "domain2",
        "type": "single",
        "title": "VNet Data Gateway vs On-Premises Data Gateway",
        "question": "Sua empresa possui um banco de dados Azure SQL Database protegido dentro de uma Rede Virtual (VNet) sem IP público. Qual solução de gateway nativa de nuvem elimina a necessidade de gerenciar máquinas virtuais locais para conexões do Data Factory e Dataflows?",
        "options": [
            {"id": "A", "text": "On-Premises Data Gateway em modo pessoal.", "isCorrect": False},
            {"id": "B", "text": "Virtual Network (VNet) Data Gateway gerenciado pela Microsoft.", "isCorrect": True},
            {"id": "C", "text": "Cabo crossover Ethernet conectado ao datacenter.", "isCorrect": False},
            {"id": "D", "text": "Habilitar portas 1433 abertas para toda a internet sem autenticação.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O VNet Data Gateway é um recurso totalmente gerenciado (PaaS) que conecta serviços de nuvem do Fabric (Data Factory, Dataflows Gen2) a serviços protegidos por VNets do Azure sem a necessidade de instalar, manter ou aplicar patches em máquinas virtuais de gateway locais.",
            [
                "<strong>A:</strong> O gateway On-Premises exige manutenção e hosting de VMs dedicadas pelo cliente.",
                "<strong>C e D:</strong> Inseguros e inviáveis em nuvem."
            ],
            "VNet Data Gateway = Conectividade segura e gerenciada para fontes protegidas por VNets do Azure sem gerenciar VMs."
        )
    },
    {
        "id": "d2_q09",
        "domain": "domain2",
        "type": "multi",
        "title": "Variáveis do Sistema em Expressões de Pipelines de Dados",
        "question": "Quais DUAS variáveis de sistema do Fabric Data Factory podem ser acessadas dinamicamente dentro de expressões de pipeline via sintaxe `@pipeline()....`? (Selecione 2 alternativas)",
        "options": [
            {"id": "A", "text": "`@pipeline().DataFactory`", "isCorrect": True},
            {"id": "B", "text": "`@pipeline().TriggerTime`", "isCorrect": True},
            {"id": "C", "text": "`@pipeline().UserPassword`", "isCorrect": False},
            {"id": "D", "text": "`@pipeline().WindowsKernelVersion`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O mecanismo de expressões de pipelines expõe variáveis do sistema sob o namespace `@pipeline()`, incluindo `@pipeline().Pipeline`, `@pipeline().RunId`, `@pipeline().TriggerTime` e `@pipeline().DataFactory`. Senhas e versões de kernel nunca são expostas.",
            [
                "<strong>C e D:</strong> Não são variáveis válidas de sistema."
            ],
            "Variáveis do sistema comuns: `RunId`, `TriggerTime`, `Pipeline`, `DataFactory`."
        )
    },
    {
        "id": "d2_q10",
        "domain": "domain2",
        "type": "single",
        "title": "Tratamento de Falhas com Bloco Try-Catch em Pipelines",
        "question": "Como um engenheiro de dados deve modelar o equivalente a um bloco 'Try-Catch' para capturar erros em uma atividade de Pipeline e enviar uma notificação para o Teams caso ocorra falha?",
        "options": [
            {"id": "A", "text": "Adicionar um bloco try-catch em JavaScript no navegador.", "isCorrect": False},
            {"id": "B", "text": "Conectar a atividade de execução (Try) a uma atividade de notificação (Catch) utilizando o conector de dependência condicional 'Upon Failure' (vermelho).", "isCorrect": True},
            {"id": "C", "text": "Configurar o pipeline para reiniciar em loop infinito sempre que der erro.", "isCorrect": False},
            {"id": "D", "text": "Não é possível tratar erros em pipelines do Fabric.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Em Data Pipelines do Fabric, o fluxo de controle utiliza conectores condicionais de dependência: Verde (Upon Success), Vermelho (Upon Failure), Azul (Upon Completion) e Cinza (Upon Skip). Para criar tratamento de erro, conecta-se a saída 'Upon Failure' à atividade que envia o alerta ou executa rollback.",
            [
                "<strong>A, C e D:</strong> Métodos inválidos no modelo de orquestração de Data Factory."
            ],
            "Conectores de Pipeline: Upon Success (Verde), Upon Failure (Vermelho), Upon Completion (Azul)."
        )
    },
    {
        "id": "d2_q11",
        "domain": "domain2",
        "type": "single",
        "title": "Passagem de Parâmetros de Pipeline para Notebook Spark",
        "question": "Um engenheiro de dados deseja parametrizar um Notebook Spark para que o ano de processamento seja fornecido dinamicamente pela atividade 'Notebook' em um Data Pipeline. O que deve ser configurado no Notebook Spark para receber esse parâmetro?",
        "options": [
            {"id": "A", "text": "Marcar a primeira célula de código do Notebook com a tag de célula 'parameters'.", "isCorrect": True},
            {"id": "B", "text": "Escrever a variável no arquivo `config.ini` no disco C: do servidor.", "isCorrect": False},
            {"id": "C", "text": "Instalar o pacote `sys.argv` via prompt do MS-DOS.", "isCorrect": False},
            {"id": "D", "text": "O Fabric não suporta passagem de parâmetros para Notebooks.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "No Apache Spark do Fabric (assim como no Databricks/Synapse), a parametrização de Notebooks é realizada aplicando a tag de célula 'parameters' na célula onde as variáveis padrão são declaradas. O pipeline injeta uma célula subsequente com os valores passados em tempo de execução.",
            [
                "<strong>B, C e D:</strong> Práticas incorretas; o padrão oficial de parametrização é a tag 'parameters'."
            ],
            "Parametrização de Notebooks no Fabric: Ativar o painel de propriedades da célula e adicionar a tag 'parameters'."
        )
    },
    {
        "id": "d2_q12",
        "domain": "domain2",
        "type": "single",
        "title": "Atividade Until para Polling de Status",
        "question": "Um pipeline do Fabric precisa disparar um processo em uma API REST e aguardar em loop periódico (a cada 30 segundos) até que um endpoint retorne o status `'COMPLETED'`. Qual atividade de controle de fluxo é a mais indicada?",
        "options": [
            {"id": "A", "text": "Atividade If Condition sem ramificação.", "isCorrect": False},
            {"id": "B", "text": "Atividade Until contendo uma atividade Web e uma atividade Wait em seu corpo, iterando até que a expressão booleana de conclusão seja avaliada como verdadeira.", "isCorrect": True},
            {"id": "C", "text": "Atividade Switch com 50 opções estáticas.", "isCorrect": False},
            {"id": "D", "text": "Atividade Fail para forçar a parada do locatário.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A atividade Until funciona como um loop `do-until`: ela executa as atividades internas e avalia uma condição ao final. Se a condição for falsa, repete a execução até atingir o critério de parada (ou timeout configurado), sendo o padrão ideal para polling com Wait intermediário.",
            [
                "<strong>A e C:</strong> Estruturas de ramificação simples que não realizam repetições em loop.",
                "<strong>D:</strong> A atividade Fail aborta o pipeline deliberadamente com erro."
            ],
            "Loop de espera/polling em pipeline: Atividade Until com atividades Web + Wait."
        )
    },
    {
        "id": "d2_q13",
        "domain": "domain2",
        "type": "single",
        "title": "Atividade Invoke Pipeline (Execute Pipeline)",
        "question": "Para criar uma arquitetura modular de orquestração de dados, você deseja que um 'Pipeline Mestre' chame múltiplos 'Pipelines Filhos'. Qual propriedade na atividade Execute Pipeline define se o pipeline pai aguarda ou não o término do pipeline filho?",
        "options": [
            {"id": "A", "text": "Wait on completion (Aguardar conclusão - booleano)", "isCorrect": True},
            {"id": "B", "text": "Auto restart on error", "isCorrect": False},
            {"id": "C", "text": "Direct Lake Acceleration mode", "isCorrect": False},
            {"id": "D", "text": "Run in background thread only", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Na atividade Execute Pipeline (Invoke Pipeline), a opção 'Wait on completion' determina se a execução é síncrona (o pipeline pai aguarda o pipeline filho finalizar para seguir para a próxima atividade) ou assíncrona ('fire-and-forget').",
            [
                "<strong>B, C e D:</strong> Propriedades inexistentes ou irrelevantes nessa atividade."
            ],
            "Execute Pipeline: 'Wait on completion' ativado = síncrono; desativado = assíncrono."
        )
    },
    {
        "id": "d2_q14",
        "domain": "domain2",
        "type": "single",
        "title": "Gatilhos de Agendamento vs Gatilhos de Janela de Queda (Tumbling Window)",
        "question": "Um engenheiro de dados precisa reprocessar dados históricos fatiados fatia por fatia (slice-by-slice) respeitando rigorosamente a ordem cronológica do passado e garantindo concorrência máxima de 1 fatia por vez. Qual tipo de gatilho (Trigger) deve ser configurado no pipeline?",
        "options": [
            {"id": "A", "text": "Gatilho de Agendamento Básico (Schedule Trigger)", "isCorrect": False},
            {"id": "B", "text": "Gatilho de Janela de Queda (Tumbling Window Trigger) com dependência de auto-concorrência (`maxConcurrency = 1`).", "isCorrect": True},
            {"id": "C", "text": "Gatilho de Evento de Armazenamento (Storage Event Trigger)", "isCorrect": False},
            {"id": "D", "text": "Disparo manual via botão 'Run Now' no navegador.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Tumbling Window Triggers disparam em intervalos contíguos e não sobrepostos. Possuem recursos exclusivos para cenários de reprocessamento histórico (backfill) e dependências temporais estritas (ex: a fatia de 11:00 só roda após a conclusão da fatia de 10:00 com maxConcurrency=1).",
            [
                "<strong>A:</strong> Schedule Triggers disparam em horários fixos sem rastreamento de fatias históricas.",
                "<strong>C:</strong> Storage Event Triggers reagem à chegada de novos arquivos (blobs criados/deletados).",
                "<strong>D:</strong> Inviável para repetição cronológica sistemática."
            ],
            "Backfill e execução sequencial rigorosa de fatias temporais = Tumbling Window Trigger."
        )
    },
    {
        "id": "d2_q15",
        "domain": "domain2",
        "type": "single",
        "title": "Criptografia de Credenciais e Azure Key Vault nos Conectores",
        "question": "Ao criar uma conexão para um banco de dados externo Oracle em um Data Pipeline, qual é a melhor prática recomendada pela Microsoft para gerenciar a senha do usuário sem expô-la na interface nem gravá-la em código?",
        "options": [
            {"id": "A", "text": "Armazenar a senha no Azure Key Vault e referenciar o segredo na conexão do pipeline utilizando uma Identidade Gerenciada ou Service Principal.", "isCorrect": True},
            {"id": "B", "text": "Escrever a senha na descrição pública da tabela no OneLake.", "isCorrect": False},
            {"id": "C", "text": "Gravar a senha no arquivo `.gitignore` do repositório.", "isCorrect": False},
            {"id": "D", "text": "Criar um usuário com senha vazia no banco Oracle.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A prática padrão de segurança corporativa é armazenar segredos no Azure Key Vault. O Fabric pode se conectar ao Key Vault para obter credenciais dinamicamente em tempo de execução sem persistir senhas em texto puro nos artefatos.",
            [
                "<strong>B, C e D:</strong> Práticas inseguras que violam os padrões de conformidade."
            ],
            "Gestão de senhas e segredos no Fabric = Azure Key Vault integration."
        )
    },
    {
        "id": "d2_q16",
        "domain": "domain2",
        "type": "multi",
        "title": "Formatos de Destino Suportados Nativamente na Copy Activity",
        "question": "Quais DOIS destinos analíticos internos do Microsoft Fabric podem receber dados gravados diretamente por uma atividade Copy em um Data Pipeline? (Selecione 2 alternativas)",
        "options": [
            {"id": "A", "text": "Tabelas do Lakehouse (Delta Parquet)", "isCorrect": True},
            {"id": "B", "text": "Tabelas do Fabric Warehouse (via ingestão relacional otimizada)", "isCorrect": True},
            {"id": "C", "text": "Arquivo binário executável `.EXE` do Windows", "isCorrect": False},
            {"id": "D", "text": "Disquete magnético de 3,5 polegadas virtual", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A Copy Activity do Fabric Data Factory possui conectores nativos de destino otimizados para: Lakehouse (gravando diretamente em tabelas Delta ou arquivos), Warehouse (usando ingestão relacional massiva), KQL Database e Mirrored Databases.",
            [
                "<strong>C e D:</strong> Formatos não suportados e fictícios."
            ],
            "Destinos primários de pipeline no Fabric: Lakehouse, Warehouse e KQL Database."
        )
    },
    {
        "id": "d2_q17",
        "domain": "domain2",
        "type": "single",
        "title": "Mapeamento Dinâmico de Esquema na Copy Activity",
        "question": "Um pipeline precisa copiar dados de 50 tabelas de origens diferentes para o Lakehouse de destino sem que o desenvolvedor tenha que configurar o mapeamento coluna por coluna para cada tabela individualmente. Qual recurso da Copy Activity permite essa flexibilidade?",
        "options": [
            {"id": "A", "text": "Mapeamento Automático de Esquema (Auto-mapping / Schema Drift) sem mapeamento estático explícito na guia Mapping.", "isCorrect": True},
            {"id": "B", "text": "Obrigatoriedade de escrever 50 arquivos XML com esquemas XSD.", "isCorrect": False},
            {"id": "C", "text": "Criação de um trigger T-SQL para cada coluna da tabela.", "isCorrect": False},
            {"id": "D", "text": "Não é possível copiar tabelas sem mapear todas as colunas manualmente.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Ao deixar a guia de mapeamento vazia ou utilizar parâmetros dinâmicos na Copy Activity, o motor adota o mapeamento automático por nome de coluna (Auto-mapping) e suporta Schema Drift, permitindo reutilizar uma única atividade Copy genérica para dezenas de tabelas.",
            [
                "<strong>B, C e D:</strong> Afirmações incorretas sobre as capacidades do Data Factory."
            ],
            "Pipelines genéricos de cópia utilizam Auto-mapping / Schema Drift para reutilização de atividades."
        )
    },
    {
        "id": "d2_q18",
        "domain": "domain2",
        "type": "single",
        "title": "Atividade Script vs Stored Procedure em Pipelines",
        "question": "Quando um desenvolvedor deve preferir a atividade 'Script' em vez da atividade 'Stored Procedure' ao executar comandos SQL no Fabric Warehouse a partir de um Data Pipeline?",
        "options": [
            {"id": "A", "text": "Quando precisa executar comandos DDL/DML arbitrários (como `CREATE TABLE AS SELECT`, `TRUNCATE`, ou múltiplos comandos em lote) sem a necessidade de criar previamente um objeto de stored procedure permanente no banco.", "isCorrect": True},
            {"id": "B", "text": "Quando quer compilar código C# nativo no banco.", "isCorrect": False},
            {"id": "C", "text": "Quando precisa reiniciar a máquina do servidor SQL.", "isCorrect": False},
            {"id": "D", "text": "A atividade Script foi descontinuada e não deve ser usada.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A atividade 'Script' é versátil: ela aceita consultas T-SQL diretas, múltiplos comandos DDL/DML, instruções como `CREATE TABLE AS SELECT (CTAS)` e pode retornar conjuntos de resultados, dispensando a criação e manutenção de objetos de procedure persistidos quando não forem necessários.",
            [
                "<strong>B, C e D:</strong> Falsas declarações sem suporte na documentação oficial."
            ],
            "Atividade Script = Execução de SQL direto, DDL flexível e batches T-SQL no Warehouse."
        )
    },

    # --- APACHE SPARK & NOTEBOOKS (Questões 19 a 38) ---
    {
        "id": "d2_q19",
        "domain": "domain2",
        "type": "single",
        "title": "Starter Pools vs Custom Pools no Fabric Spark",
        "question": "Por que os Starter Pools (pools iniciais gerenciados pela Microsoft) oferecem um tempo de inicialização de sessão de Notebook quase instantâneo (< 10 segundos) em comparação com Custom Pools?",
        "options": [
            {"id": "A", "text": "Porque eles mantêm nós computacionais previamente aquecidos e provisionados em standby com tamanhos de nós padronizados.", "isCorrect": True},
            {"id": "B", "text": "Porque eles não usam o Apache Spark, apenas uma biblioteca Python compilada.", "isCorrect": False},
            {"id": "C", "text": "Porque eles nunca executam código real no cluster.", "isCorrect": False},
            {"id": "D", "text": "Porque os dados são salvos em memória flash do navegador.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Os Starter Pools são pools elásticos gerenciados pelo Fabric que mantêm máquinas virtuais pré-alocadas e aquecidas em background. Quando um usuário anexa uma sessão de notebook a um Starter Pool, os executores Spark inicializam em poucos segundos sem o tempo habitual de provisionamento de VM (que pode levar de 3 a 5 minutos em pools customizados).",
            [
                "<strong>B, C e D:</strong> Afirmações incorretas sobre a arquitetura do Spark no Fabric."
            ],
            "Starter Pools no Fabric = Clusters Spark pré-aquecidos para inicialização em menos de 10 segundos."
        )
    },
    {
        "id": "d2_q20",
        "domain": "domain2",
        "type": "single",
        "title": "Mecanismo Velox (Native Execution Engine)",
        "question": "O que é o Native Execution Engine (baseado no projeto Velox) no Apache Spark do Microsoft Fabric e qual é o seu principal benefício de desempenho?",
        "options": [
            {"id": "A", "text": "É uma biblioteca JavaScript para desenhar gráficos 3D no notebook.", "isCorrect": False},
            {"id": "B", "text": "É uma engine de vetorização de baixo nível escrita em C++ que substitui os operadores tradicionais da JVM por execução colunar nativa com instruções SIMD, acelerando consultas e reduzindo o consumo de CUs.", "isCorrect": True},
            {"id": "C", "text": "É um antivírus embutido no Spark para verificar arquivos corrompidos.", "isCorrect": False},
            {"id": "D", "text": "É uma extensão do Excel instalada no nó mestre do cluster.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Native Execution Engine do Fabric Spark é construído sobre o Velox (motor open-source C++ colunar). Ele executa planos de consulta Spark SQL diretamente em código nativo de máquina usando vetorização SIMD de CPU, contornando a sobrecarga do garbage collector e interpretação de bytecode da JVM (Java Virtual Machine), acelerando drasticamente consultas analíticas pesadas.",
            [
                "<strong>A, C e D:</strong> Falsas analogias técnicas."
            ],
            "Velox Native Execution Engine = Execução nativa colunar em C++ com instruções SIMD no Spark do Fabric."
        )
    },
    {
        "id": "d2_q21",
        "domain": "domain2",
        "type": "single",
        "title": "Estratégia de Broadcast Hash Join e Limite Padrão",
        "question": "Em uma consulta PySpark que realiza a junção de uma tabela de fatos com 1 bilhão de linhas e uma tabela de dimensão com 8 MB de tamanho, o Spark opta automaticamente por um Broadcast Hash Join. Qual é o limite de tamanho de tabela padrão (`spark.sql.autoBroadcastJoinThreshold`) para essa decisão automática?",
        "options": [
            {"id": "A", "text": "1 MB", "isCorrect": False},
            {"id": "B", "text": "10 MB", "isCorrect": True},
            {"id": "C", "text": "1 GB", "isCorrect": False},
            {"id": "D", "text": "10 GB", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O parâmetro `spark.sql.autoBroadcastJoinThreshold` tem o valor padrão de 10 MB (10.485.760 bytes). Quando uma das tabelas de junção for menor ou igual a esse tamanho, o Spark transmite a tabela inteira para todos os executores, eliminando a dispendiosa fase de Shuffle da tabela de fatos.",
            [
                "<strong>A:</strong> 1 MB é muito conservador.",
                "<strong>C e D:</strong> Fazer broadcast de 1 GB ou 10 GB sobrecarregaria a memória do Driver e causaria erros de OutOfMemory (OOM)."
            ],
            "`autoBroadcastJoinThreshold` padrão no Spark = 10 MB. Broadcast Join evita Shuffle de dados na rede."
        )
    },
    {
        "id": "d2_q22",
        "domain": "domain2",
        "type": "single",
        "title": "Adaptive Query Execution (AQE) e Tratamento de Skew Join",
        "question": "Durante a execução de um Sort Merge Join em um job Spark no Fabric, uma partição contém 80% de todas as chaves de junção, fazendo com que um único executor trabalhe por horas enquanto os demais ficam ociosos. Qual recurso do Spark 3.x resolve essa assimetria de partição automaticamente em tempo de execução?",
        "options": [
            {"id": "A", "text": "AQE Skew Join (`spark.sql.adaptive.skewJoin.enabled = true`), que divide a partição assimétrica em sub-partições menores dinamicamente.", "isCorrect": True},
            {"id": "B", "text": "Desativar o cluster Spark e ligar uma máquina física com mais núcleos.", "isCorrect": False},
            {"id": "C", "text": "Usar a função `RAND()` na chave primária da tabela relacional.", "isCorrect": False},
            {"id": "D", "text": "Substituir o PySpark por código puro em linguagem Pascal.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Adaptive Query Execution (AQE) com detecção de Skew Join identifica partições desbalanceadas após a fase de shuffle e divide automaticamente as partições pesadas em pedaços menores (sub-partições), distribuindo-os uniformemente entre múltiplos executores sem alteração manual no código.",
            [
                "<strong>B, C e D:</strong> Soluções inviáveis e incorretas."
            ],
            "AQE Skew Join resolve o gargalo de assimetria de partições (Data Skew) dividindo partições volumosas dinamicamente."
        )
    },
    {
        "id": "d2_q23",
        "domain": "domain2",
        "type": "single",
        "title": "Gatilho `availableNow = True` no Spark Structured Streaming",
        "question": "Um engenheiro de dados quer processar dados de streaming incrementalmente em um pipeline em lote agendado a cada 6 horas. O objetivo é processar todos os dados novos que chegaram desde a última execução e então finalizar a sessão Spark para economizar custos de capacidade. Qual configuração de Trigger deve ser usada?",
        "options": [
            {"id": "A", "text": "`.trigger(processingTime='10 seconds')`", "isCorrect": False},
            {"id": "B", "text": "`.trigger(availableNow=True)`", "isCorrect": True},
            {"id": "C", "text": "`.trigger(continuous='1 second')`", "isCorrect": False},
            {"id": "D", "text": "Não definir nenhum trigger e matar o processo manualmente no Azure Portal.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O gatilho `trigger(availableNow=True)` processa todos os micro-lotes de dados disponíveis no momento da execução respeitando os limites de taxa configurados e depois encerra a stream com segurança. É o sucessor moderno e superior de `trigger(once=True)`.",
            [
                "<strong>A e C:</strong> Mantêm a stream rodando continuamente em loop infinito, consumindo CUs sem parar.",
                "<strong>D:</strong> Matar o processo abruptamente pode corromper checkpoints ou deixar transações incompletas."
            ],
            "Incremental Batch com Streaming: Use `.trigger(availableNow=True)` para processar tudo o que estiver disponível e desligar."
        )
    },
    {
        "id": "d2_q24",
        "domain": "domain2",
        "type": "single",
        "title": "Mecanismo de Watermarking no Spark Streaming",
        "question": "Ao agregar eventos em janelas temporais de 15 minutos em uma stream contínua do Spark, como o desenvolvedor garante que dados que cheguem com atraso de até 10 minutos sejam aceitos na agregação, mas que o estado da memória não cresça infinitamente?",
        "options": [
            {"id": "A", "text": "Utilizando a função `.withWatermark('event_time', '10 minutes')`.", "isCorrect": True},
            {"id": "B", "text": "Aumentando a memória física de todos os nós em 128 Terabytes.", "isCorrect": False},
            {"id": "C", "text": "Deletando todos os eventos anteriores a cada 5 segundos.", "isCorrect": False},
            {"id": "D", "text": "Ignorando os horários de evento e usando apenas a hora do relógio local do cluster.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O método `.withWatermark('timestamp_col', 'delay_threshold')` define o teto aceitável de dados atrasados (late data). O Spark mantém o estado em memória para eventos que cheguem dentro do intervalo de watermark; ultrapassado esse limiar, a janela é fechada e o estado é descartado da memória RAM.",
            [
                "<strong>B, C e D:</strong> Abordagens inviáveis que causariam OutOfMemory ou perda massiva de dados analíticos válidos."
            ],
            "Watermarking no Spark Streaming descarta o estado antigo da memória após o tempo limite de atraso."
        )
    },
    {
        "id": "d2_q25",
        "domain": "domain2",
        "type": "single",
        "title": "Diferença entre Janelas Tumbling e Sliding",
        "question": "Em uma análise de telemetria de sensores, a equipe de operações precisa calcular a temperatura média a cada 5 minutos em blocos fechados e independentes (sem sobreposição: 10:00-10:05, 10:05-10:10). Qual tipo de janela temporal do Spark atende a essa regra?",
        "options": [
            {"id": "A", "text": "Janela Tumbling (Tumbling Window / Janela de Salto Fixo sem sobreposição)", "isCorrect": True},
            {"id": "B", "text": "Janela Sliding (Janela Deslizante com sobreposição contínua)", "isCorrect": False},
            {"id": "C", "text": "Janela de Sessão dinâmica baseada em inatividade de 48 horas", "isCorrect": False},
            {"id": "D", "text": "Janela aleatória gerada por sorteio de números", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Janelas Tumbling (janelas em bloco) possuem duração fixa e não se sobrepõem: cada evento pertence a exatamente uma janela. Janelas Sliding (deslizantes) avançam em passos menores que sua duração total (ex: janela de 10 minutos a cada 2 minutos), gerando sobreposição.",
            [
                "<strong>B:</strong> Janela Sliding gera sobreposição de eventos entre janelas vizinhas.",
                "<strong>C e D:</strong> Tipos de janela inadequados para o caso de uso."
            ],
            "Tumbling Window = Janelas fixas sem sobreposição (`window(time, '5 minutes')`)."
        )
    },
    {
        "id": "d2_q26",
        "domain": "domain2",
        "type": "single",
        "title": "Modos de Saída (Output Modes) no Spark Streaming",
        "question": "Qual modo de saída (`outputMode`) do Spark Structured Streaming deve ser utilizado quando a consulta de streaming realiza uma agregação com marca d'água (watermark) e você deseja gravar apenas as linhas consolidadas das janelas de tempo definitivamente fechadas?",
        "options": [
            {"id": "A", "text": "`outputMode('append')`", "isCorrect": True},
            {"id": "B", "text": "`outputMode('complete')`", "isCorrect": False},
            {"id": "C", "text": "`outputMode('update')`", "isCorrect": False},
            {"id": "D", "text": "`outputMode('delete')`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Em consultas de agregação agregadas com watermark, o modo `append` emite linhas para o sink de destino apenas quando a marca d'água ultrapassa o término da janela temporal (quando o resultado daquela janela é final e imutável), evitando a regravação contínua da tabela inteira.",
            [
                "<strong>B:</strong> O modo `complete` regrava a tabela de saída inteira a cada micro-lote, sendo inviável para tabelas de fatos volumosas.",
                "<strong>C:</strong> O modo `update` emite registros sempre que o valor de agregação é atualizado na janela aberta.",
                "<strong>D:</strong> O modo 'delete' não existe no Spark Structured Streaming."
            ],
            "Agregações consolidadas com Watermark em Delta Lake exigem `outputMode('append')`."
        )
    },
    {
        "id": "d2_q27",
        "domain": "domain2",
        "type": "single",
        "title": "Alta Simultaneidade (High Concurrency Mode) em Notebooks",
        "question": "Em uma equipe de 10 engenheiros de dados que executam Notebooks de exploração ao mesmo tempo, como o recurso de 'High Concurrency' do Fabric Spark reduz o tempo de espera e otimiza o uso de Capacity Units?",
        "options": [
            {"id": "A", "text": "Permite que múltiplos notebooks compartilhem a mesma sessão e o mesmo cluster Spark ativo com isolamento de contexto de usuário, evitando o tempo e o custo de iniciar clusters individuais para cada engenheiro.", "isCorrect": True},
            {"id": "B", "text": "Transforma o Spark em um servidor web Apache Tomcat.", "isCorrect": False},
            {"id": "C", "text": "Apaga os notebooks que levarem mais de 3 minutos para responder.", "isCorrect": False},
            {"id": "D", "text": "Executa todos os comandos em ordem alfabética.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O modo High Concurrency permite compartilhar um cluster Spark ativo entre múltiplos usuários e notebooks em tempo real. Cada usuário mantém seu próprio REPL e espaço de variáveis isolado, mas compartilha os executores já alocados, acelerando a inicialização e reduzindo o consumo de CUs.",
            [
                "<strong>B, C e D:</strong> Descrições sem sentido prático ou técnico."
            ],
            "High Concurrency Spark = Compartilhamento de sessão e computação entre múltiplos notebooks e usuários simultâneos."
        )
    },
    {
        "id": "d2_q28",
        "domain": "domain2",
        "type": "single",
        "title": "Gerenciamento de Dependências com 'Ambientes' (Environments)",
        "question": "Um projeto corporativo de dados requer versões específicas de bibliotecas Python (`scikit-learn==1.4.2`, `polars==0.20.15`) em todos os Notebooks e Jobs Spark do Workspace. Qual é o método recomendado pelo Fabric para gerenciar e versionar essas dependências sem executar comandos `%pip install` no início de cada notebook?",
        "options": [
            {"id": "A", "text": "Criar um item do tipo 'Environment' (Ambiente) no Fabric Workspace, configurar as bibliotecas customizadas e associá-lo como o ambiente padrão do Workspace ou Notebook.", "isCorrect": True},
            {"id": "B", "text": "Instalar os pacotes Python no disco local do notebook pessoal do desenvolvedor.", "isCorrect": False},
            {"id": "C", "text": "Modificar os arquivos binários do sistema operacional Linux da nuvem da Microsoft.", "isCorrect": False},
            {"id": "D", "text": "Substituir todas as bibliotecas por fórmulas do Microsoft Excel.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Os 'Environments' (Ambientes) do Fabric são itens gerenciados de workspace que permitem configurar pools de nós, propriedades Spark (`spark-defaults.conf`) e bibliotecas personalizadas (via Conda, Pip ou arquivos `.whl`). Eles são compilados uma única vez e anexados aos notebooks e pipelines com inicialização instantânea.",
            [
                "<strong>B, C e D:</strong> Práticas incorretas que não escalam em ambientes de engenharia de dados em nuvem."
            ],
            "Gestão centralizada de bibliotecas no Fabric Spark = Item 'Environment' (Ambiente)."
        )
    },

    # --- DELTA LAKE INTERNALS & SCD (Questões 29 a 48) ---
    {
        "id": "d2_q29",
        "domain": "domain2",
        "type": "single",
        "title": "Estrutura do Diretório `_delta_log` e Frequência de Checkpoint",
        "question": "Em uma tabela Delta no OneLake, a cada transação ACID é gravado um arquivo JSON de commit sequencial (`000000.json`, `000001.json`). Com que frequência padrão o motor Delta gera um arquivo consolidado de Checkpoint em formato Parquet (`.checkpoint.parquet`)?",
        "options": [
            {"id": "A", "text": "A cada 5 commits", "isCorrect": False},
            {"id": "B", "text": "A cada 10 commits", "isCorrect": True},
            {"id": "C", "text": "A cada 100 commits", "isCorrect": False},
            {"id": "D", "text": "Apenas quando a tabela atinge 1 Terabyte", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Por padrão na especificação Delta Lake, a cada 10 commits (transações concluídas com sucesso), o motor grava um arquivo de checkpoint Parquet consolidado (ex: `00000000000000000010.checkpoint.parquet`). Isso permite que futuros leitores carreguem o estado atual da tabela em uma única leitura sem precisar reprocessar centenas de arquivos JSON individuais.",
            [
                "<strong>A, C e D:</strong> Intervalos incorretos segundo o protocolo Delta Lake oficial."
            ],
            "Delta Log: Checkpoint Parquet é gerado a cada 10 commits JSON para consolidar o estado."
        )
    },
    {
        "id": "d2_q30",
        "domain": "domain2",
        "type": "single",
        "title": "Comando VACUUM e Período de Retenção Padrão",
        "question": "Um engenheiro de dados executou o comando `VACUUM TabelaVendas` sem especificar argumentos de tempo. O que acontece com os arquivos Parquet antigos que não estão mais referenciados no estado ativo da tabela?",
        "options": [
            {"id": "A", "text": "Todos os arquivos são deletados imediatamente, inclusive os modificados há 1 segundo.", "isCorrect": False},
            {"id": "B", "text": "Apenas os arquivos órfãos com idade superior ao período de retenção padrão de 7 dias (168 horas) são fisicamente removidos do OneLake.", "isCorrect": True},
            {"id": "C", "text": "O comando VACUUM apenas compacta arquivos pequenos sem excluir nenhum byte.", "isCorrect": False},
            {"id": "D", "text": "O comando falha porque o VACUUM exige senha de administrador de locatário.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O comando VACUUM remove arquivos de dados Parquet que não estão mais no commit mais recente e que foram excluídos/substituídos há mais tempo do que a janela de retenção de segurança (padrão de 168 horas / 7 dias). Isso preserva a capacidade de Time Travel para os últimos 7 dias.",
            [
                "<strong>A:</strong> O VACUUM possui uma trava de segurança de retenção padrão de 7 dias para não quebrar leitores ativos nem Time Travel recente.",
                "<strong>C:</strong> Compactação de arquivos é responsabilidade do comando `OPTIMIZE`, não do `VACUUM`.",
                "<strong>D:</strong> VACUUM é uma operação de manutenção DDL/DML padrão."
            ],
            "VACUUM no Delta Lake: Período de retenção padrão = 7 dias (168 horas). Remove arquivos obsoletos após esse prazo."
        )
    },
    {
        "id": "d2_q31",
        "domain": "domain2",
        "type": "single",
        "title": "Impacto do VACUUM no Time Travel",
        "question": "Após a execução bem-sucedida de um comando `VACUUM Clientes RETAIN 0 HOURS` (com a trava de segurança desativada), o que acontece quando um analista tenta executar uma consulta com Time Travel: `spark.read.format('delta').option('versionAsOf', 1).load(...)`?",
        "options": [
            {"id": "A", "text": "A consulta falha com erro de arquivo não encontrado (`FileNotFoundException`), pois os arquivos Parquet da versão 1 foram excluídos fisicamente pelo VACUUM.", "isCorrect": True},
            {"id": "B", "text": "A consulta executa normalmente recuperando os arquivos a partir da memória cache da CPU.", "isCorrect": False},
            {"id": "C", "text": "O Fabric baixa os arquivos automaticamente a partir de um backup em fita magnética.", "isCorrect": False},
            {"id": "D", "text": "O Time Travel ignora o VACUUM e sintetiza os dados usando inteligência artificial.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Time Travel depende da existência física dos arquivos Parquet nos quais as versões antigas se baseiam. Se o VACUUM remover esses arquivos físicos do disco/OneLake, qualquer tentativa de ler versões anteriores que dependam desses arquivos resultará em erro fatal de `FileNotFoundException`.",
            [
                "<strong>B, C e D:</strong> Uma vez deletados fisicamente pelo VACUUM, os dados não podem ser reconstruídos por cache nem IA."
            ],
            "Consequência crítica do VACUUM: Destrói a capacidade de realizar Time Travel para períodos anteriores ao limite de retenção aplicado."
        )
    },
    {
        "id": "d2_q32",
        "domain": "domain2",
        "type": "single",
        "title": "Comando RESTORE TABLE para Recuperação de Desastres",
        "question": "Um script executou acidentalmente um comando `DELETE FROM Pedidos WHERE 1=1`, apagando todos os registros de uma tabela Delta crítica no Lakehouse. Qual comando permite restaurar a tabela instantaneamente ao seu estado exato de 15 minutos atrás sem restaurar backups?",
        "options": [
            {"id": "A", "text": "`RESTORE TABLE Pedidos TO TIMESTAMP AS OF '<timestamp_anterior>';`", "isCorrect": True},
            {"id": "B", "text": "`UNDELETE ALL FROM Pedidos;`", "isCorrect": False},
            {"id": "C", "text": "`ROLLBACK TRANSACTION IMMEDIATE;`", "isCorrect": False},
            {"id": "D", "text": "`DROP TABLE Pedidos;`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Delta Lake possui o comando nativo `RESTORE TABLE <tabela> TO VERSION AS OF <v>` ou `TO TIMESTAMP AS OF <ts>`. Como as transações Delta são baseadas em log imutável, o RESTORE simplesmente grava um novo commit no `_delta_log` apontando o ponteiro oficial de volta para o estado dos arquivos da versão desejada.",
            [
                "<strong>B e C:</strong> Comandos não existentes no dialeto Delta Lake.",
                "<strong>D:</strong> Excluiria a tabela e agravaria o incidente."
            ],
            "Recuperação instantânea no Delta Lake: `RESTORE TABLE <tabela> TO VERSION AS OF <n>`."
        )
    },
    {
        "id": "d2_q33",
        "domain": "domain2",
        "type": "single",
        "title": "Liquid Clustering (`CLUSTER BY`) vs Particionamento Tradicional",
        "question": "Qual é a principal vantagem do Liquid Clustering (`CLUSTER BY (col1, col2)`) em comparação com o particionamento tradicional em pastas no estilo Hive (`PARTITION BY col1`) no Microsoft Fabric?",
        "options": [
            {"id": "A", "text": "Liquid Clustering evita problemas graves de particionamento excessivo (overpartitioning) e arquivos minúsculos (small files), permitindo alterar as chaves de agrupamento sem precisar reescrever os dados históricos da tabela inteira.", "isCorrect": True},
            {"id": "B", "text": "Liquid Clustering transforma arquivos Parquet em arquivos binários criptografados proprietários.", "isCorrect": False},
            {"id": "C", "text": "Liquid Clustering só funciona em tabelas com menos de 10 linhas.", "isCorrect": False},
            {"id": "D", "text": "Liquid Clustering desativa o suporte a transações ACID.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O particionamento tradicional em pastas cria subpastas físicas rígidas, causando milhares de arquivos minúsculos quando a cardinalidade é alta. O Liquid Clustering (`CLUSTER BY`) usa curvas de preenchimento de espaço (Space-Filling Curves / Z-Order flexível) nos próprios arquivos de dados, permitindo mudar as chaves de clusterização a qualquer momento sem recriar ou reescrever partições históricas.",
            [
                "<strong>B, C e D:</strong> Declarações tecnicamente falsas."
            ],
            "Liquid Clustering é a recomendação oficial moderna do Fabric para substituir o particionamento Hive rígido em tabelas Delta."
        )
    },
    {
        "id": "d2_q34",
        "domain": "domain2",
        "type": "single",
        "title": "Ordenação V-Order e Leitura no Power BI Direct Lake",
        "question": "Qual é a função do algoritmo de otimização 'V-Order' aplicado nativamente pelo Microsoft Fabric na gravação de arquivos Parquet?",
        "options": [
            {"id": "A", "text": "Reordenar os dados e aplicar esquemas de codificação e compressão em nível de row group para proporcionar leitura ultrarrápida em memória pelo motor VertiPaq do Power BI e pelo SQL Endpoint.", "isCorrect": True},
            {"id": "B", "text": "Criptografar os arquivos com senha para proteger contra pirataria.", "isCorrect": False},
            {"id": "C", "text": "Converter todos os valores numéricos em decimais de 128 bits.", "isCorrect": False},
            {"id": "D", "text": "Enviar uma cópia de cada linha para o Microsoft Teams.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O V-Order é uma otimização de formato de arquivo no padrão Parquet 100% aberto. Ele classifica e codifica os dados dentro dos row groups de acordo com padrões de acesso colunares, permitindo que a engine VertiPaq (Direct Lake) e a engine de consultas T-SQL leiam os blocos de dados na memória quase sem overhead de decodificação.",
            [
                "<strong>B, C e D:</strong> Falsas declarações sem base tecnológica."
            ],
            "V-Order = Otimização colunar de row groups para desempenho máximo de leitura no Direct Lake e T-SQL."
        )
    },
    {
        "id": "d2_q35",
        "domain": "domain2",
        "type": "single",
        "title": "Implementação de Slowly Changing Dimensions (SCD Tipo 2) com Delta MERGE",
        "question": "Em uma arquitetura de Data Warehouse Medallion, qual é a principal característica de uma Dimensão de Alteração Lenta do Tipo 2 (SCD Tipo 2) implementada via comando MERGE no Delta Lake?",
        "options": [
            {"id": "A", "text": "Sobrescrever o registro existente sem guardar nenhum histórico de alterações anteriores.", "isCorrect": False},
            {"id": "B", "text": "Preservar o histórico completo de versões adicionando uma nova linha para cada alteração com colunas de controle como `DataInicio`, `DataFim` e flag `IsCurrent = True/False`.", "isCorrect": True},
            {"id": "C", "text": "Deletar a tabela inteira e recriar com os dados do dia.", "isCorrect": False},
            {"id": "D", "text": "Criar uma nova coluna na tabela para cada dia do ano.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "SCD Tipo 2 é o padrão de modelagem dimensional para manter histórico temporal: a linha existente recebe data de término (`DataFim`) e flag `IsCurrent = False`, e um novo registro é inserido com o novo valor, `DataInicio` atual e `IsCurrent = True`.",
            [
                "<strong>A:</strong> Essa é a definição de SCD Tipo 1 (sobrescrita sem histórico).",
                "<strong>C e D:</strong> Práticas incorretas e inviáveis."
            ],
            "SCD Tipo 1 = Sobrescreve (sem histórico). SCD Tipo 2 = Nova linha com controle de datas e flag ativo (com histórico completo)."
        )
    },
    {
        "id": "d2_q36",
        "domain": "domain2",
        "type": "single",
        "title": "Clonagem de Tabelas: Deep Clone vs Shallow Clone",
        "question": "Um cientista de dados precisa criar um ambiente de teste isolado para testar um algoritmo de machine learning sobre uma tabela de 5 Terabytes. Ele precisa de uma cópia instantânea sem custo adicional de armazenamento e sem copiar os arquivos físicos. Qual comando deve ser usado?",
        "options": [
            {"id": "A", "text": "`CREATE TABLE TabelaTeste SHALLOW CLONE TabelaProducao;`", "isCorrect": True},
            {"id": "B", "text": "`CREATE TABLE TabelaTeste DEEP CLONE TabelaProducao;`", "isCorrect": False},
            {"id": "C", "text": "`SELECT * INTO TabelaTeste FROM TabelaProducao;`", "isCorrect": False},
            {"id": "D", "text": "Copiar a pasta no Windows Explorer pelo OneLake File Explorer.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O `SHALLOW CLONE` (clone raso ou zero-copy clone) cria uma nova tabela nos metadados apontando para os mesmos arquivos Parquet de dados da tabela original. A criação é praticamente instantânea e consome zero armazenamento adicional até que novas gravações sejam feitas. O `DEEP CLONE` duplicaria todos os 5 TB físicos.",
            [
                "<strong>B:</strong> DEEP CLONE copia fisicamente todos os 5 Terabytes de dados, consumindo tempo e armazenamento duplicado.",
                "<strong>C e D:</strong> Também realizam cópia física completa de dados."
            ],
            "Zero-Copy Clone = `SHALLOW CLONE`. Cópia física independente = `DEEP CLONE`."
        )
    },
    {
        "id": "d2_q37",
        "domain": "domain2",
        "type": "multi",
        "title": "Benefícios do Comando `OPTIMIZE` em Tabelas Delta",
        "question": "Quais DOIS benefícios fundamentais são proporcionados pela execução periódica do comando `OPTIMIZE` em tabelas Delta no Lakehouse? (Selecione 2 alternativas)",
        "options": [
            {"id": "A", "text": "Compactação de milhares de arquivos Parquet minúsculos (small files) em arquivos maiores e mais eficientes (~1 GB).", "isCorrect": True},
            {"id": "B", "text": "Reorganização multidimensional de dados via Z-Order ou aplicação de Liquid Clustering para otimizar data skipping nas consultas.", "isCorrect": True},
            {"id": "C", "text": "Exclusão permanente dos dados confidenciais de clientes sem deixar histórico.", "isCorrect": False},
            {"id": "D", "text": "Conversão do Lakehouse em um servidor Apache Kafka.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O comando `OPTIMIZE` realiza a compactação binária (Bin-Packing) consolidando múltiplos arquivos pequenos em arquivos ideais de tamanho próximo a 1 GB e reordena colunas de filtro frequentemente consultadas via Z-Order ou Liquid Clustering para acelerar data skipping.",
            [
                "<strong>C:</strong> Exclusão física é responsabilidade do `VACUUM` após o período de retenção.",
                "<strong>D:</strong> Incorreto; OPTIMIZE é puramente uma operação de manutenção Delta."
            ],
            "OPTIMIZE = Compactação de arquivos pequenos (Compaction) + Reordenação de dados (Z-Order/Clustering)."
        )
    },
    {
        "id": "d2_q38",
        "domain": "domain2",
        "type": "single",
        "title": "Controle de Concorrência Otimista (OCC) e Conflitos de Gravação",
        "question": "O que acontece no Delta Lake quando dois jobs Spark concorrentes tentam realizar operações de `MERGE` na mesma tabela Delta exatamente no mesmo segundo?",
        "options": [
            {"id": "A", "text": "A tabela fica permanentemente corrompida e inacessível.", "isCorrect": False},
            {"id": "B", "text": "O Delta Lake utiliza Controle de Concorrência Otimista (OCC): a primeira transação comita com sucesso; a segunda transação verifica se houve sobreposição nos arquivos modificados e, se houver conflito, falha com `ConcurrentModificationException` ou tenta novamente.", "isCorrect": True},
            {"id": "C", "text": "O Fabric desliga automaticamente o locatário inteiro para proteger os dados.", "isCorrect": False},
            {"id": "D", "text": "Os dados de ambos os jobs são misturados aleatoriamente no mesmo arquivo sem controle de integridade.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Delta Lake assegura integridade ACID por meio de Optimistic Concurrency Control (OCC). Cada transação supõe que concluirá sem interferência; no momento do commit no `_delta_log`, se outra transação tiver modificado os mesmos arquivos lógicos, é detectado conflito de concorrência e a transação conflitante é abortada com segurança.",
            [
                "<strong>A, C e D:</strong> Falsas declarações; o modelo OCC foi desenhado especificamente para impedir corrupção e desastres de concorrência."
            ],
            "Delta Lake ACID = Optimistic Concurrency Control (OCC) garante transações atômicas e isoladas."
        )
    },

    # --- FABRIC WAREHOUSE & T-SQL (Questões 39 a 58) ---
    {
        "id": "d2_q39",
        "domain": "domain2",
        "type": "single",
        "title": "Consultas Cross-Database com Nomenclatura de Três Partes",
        "question": "No Fabric, um analista conectado a um Warehouse precisa cruzar dados com uma tabela de um Lakehouse localizado no mesmo Workspace. Como essa consulta T-SQL deve referenciar as tabelas?",
        "options": [
            {"id": "A", "text": "Exportando ambas as tabelas para arquivos texto no disco C: do cliente.", "isCorrect": False},
            {"id": "B", "text": "Utilizando a sintaxe de nomenclatura de três partes (Three-Part Naming): `SELECT * FROM MeuLakehouse.dbo.TabelaA JOIN MeuWarehouse.dbo.TabelaB ON ...`", "isCorrect": True},
            {"id": "C", "text": "Criando um servidor vinculado (Linked Server) via OLE DB com endereço IP fixo.", "isCorrect": False},
            {"id": "D", "text": "Não é possível cruzar tabelas de Lakehouse e Warehouse em uma única consulta T-SQL.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O motor T-SQL do Fabric suporta consultas entre diferentes bancos e itens analíticos no mesmo Workspace (ou entre workspaces) utilizando a nomenclatura padrão de três partes: `[NomeDoBanco].[Esquema].[NomeDaTabela]`. Isso permite cruzar dados entre múltiplos Lakehouses e Warehouses nativamente em uma única consulta.",
            [
                "<strong>A, C e D:</strong> Não condizem com as capacidades modernas do motor de consulta relacional do Fabric."
            ],
            "Consultas entre Lakehouse e Warehouse no Fabric: Use nomenclatura de 3 partes `[Item].[Schema].[Tabela]`."
        )
    },
    {
        "id": "d2_q40",
        "domain": "domain2",
        "type": "single",
        "title": "Chaves Primárias e Estrangeiras no Fabric Warehouse (`NOT ENFORCED`)",
        "question": "Ao criar uma restrição de Chave Primária (PRIMARY KEY) ou Chave Estrangeira (FOREIGN KEY) em uma tabela do Microsoft Fabric Warehouse com a cláusula `NOT ENFORCED`, qual é o papel dessa restrição?",
        "options": [
            {"id": "A", "text": "O banco rejeita inserções de valores duplicados ou órfãos com erro de violação de chave.", "isCorrect": False},
            {"id": "B", "text": "A restrição é puramente informacional: o banco não valida a integridade referencial durante a inserção, mas o otimizador de consultas utiliza essa informação de esquema para gerar planos de execução mais eficientes.", "isCorrect": True},
            {"id": "C", "text": "A restrição bloqueia todas as consultas de leitura na tabela.", "isCorrect": False},
            {"id": "D", "text": "A cláusula NOT ENFORCED é proibida no Fabric Warehouse.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "No Fabric Warehouse, restrições como PRIMARY KEY, UNIQUE e FOREIGN KEY devem ser declaradas obrigatoriamente com `NOT ENFORCED`. Isso significa que o motor não despende recursos checando unicidade ou integridade durante inserções massivas, cabendo aos pipelines garantir a qualidade dos dados; contudo, o otimizador usa esses metadados para otimizar JOINs e agregações.",
            [
                "<strong>A:</strong> Restrições `NOT ENFORCED` nunca rejeitam dados durante a inserção.",
                "<strong>C e D:</strong> Afirmações incorretas."
            ],
            "No Fabric Warehouse: Chaves Primárias e Estrangeiras são informacionais (`NOT ENFORCED`) e auxiliam na otimização de consultas."
        )
    },
    {
        "id": "d2_q41",
        "domain": "domain2",
        "type": "single",
        "title": "Restrições de Recursos T-SQL Não Suportados no Warehouse",
        "question": "Qual dos seguintes recursos tradicionais do SQL Server NÃO é suportado no Fabric Warehouse?",
        "options": [
            {"id": "A", "text": "Triggers (Gatilhos DML `AFTER INSERT / UPDATE / DELETE`)", "isCorrect": True},
            {"id": "B", "text": "Cláusula `GROUP BY` em instruções SELECT", "isCorrect": False},
            {"id": "C", "text": "Common Table Expressions (CTEs / Cláusula `WITH`)", "isCorrect": False},
            {"id": "D", "text": "Transações ACID com `BEGIN TRANSACTION` e `COMMIT`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric Warehouse é otimizado para cargas analíticas colunares de grande escala. Recursos orientados a OLTP transacional de linha por linha, como Triggers, cursores avançados pesados e colunas `IDENTITY` tradicionais, não são suportados.",
            [
                "<strong>B, C e D:</strong> CTEs, GROUP BY e Transações ACID completas são 100% suportadas no Fabric Warehouse."
            ],
            "Não suportado no Fabric Warehouse: Triggers, IDENTITY tradicional e cursores linha-a-linha."
        )
    },
    {
        "id": "d2_q42",
        "domain": "domain2",
        "type": "single",
        "title": "Comando `CREATE TABLE AS SELECT` (CTAS)",
        "question": "Um engenheiro de dados precisa criar uma nova tabela consolidada no Fabric Warehouse contendo dados agregados de vendas por região a partir de uma tabela de 200 milhões de linhas. Qual comando T-SQL realiza a criação da tabela e inserção dos dados em uma única operação paralela otimizada?",
        "options": [
            {"id": "A", "text": "`CREATE TABLE AS SELECT (CTAS)`", "isCorrect": True},
            {"id": "B", "text": "`EXPORT TO CSV` seguido de importação manual.", "isCorrect": False},
            {"id": "C", "text": "`INSERT INTO ... VALUES` com um loop WHILE em T-SQL.", "isCorrect": False},
            {"id": "D", "text": "`ALTER DATABASE ADD REGION;`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O comando `CREATE TABLE <NovaTabela> AS SELECT ...` (CTAS) cria a definição da nova tabela e popula os dados diretamente a partir do resultado do SELECT em uma única operação distribuída e paralelizada, sendo a técnica preferida para materialização analítica no Warehouse.",
            [
                "<strong>B:</strong> Exportar para CSV e reimportar gera latência extrema e duplicação desnecessária.",
                "<strong>C:</strong> Loop WHILE linha-a-linha com VALUES é extremamente ineficiente em bancos colunares analíticos."
            ],
            "CTAS (`CREATE TABLE AS SELECT`) é a forma mais rápida e eficiente de criar e popular tabelas no Fabric Warehouse."
        )
    },
    {
        "id": "d2_q43",
        "domain": "domain2",
        "type": "single",
        "title": "Comando `COPY INTO` para Ingestão Massiva no Warehouse",
        "question": "Qual comando T-SQL nativo do Fabric Warehouse é recomendado para ingerir rapidamente milhões de registros armazenados em arquivos Parquet ou CSV em uma conta do Azure Data Lake Storage Gen2 diretamente para uma tabela existente?",
        "options": [
            {"id": "A", "text": "`COPY INTO`", "isCorrect": True},
            {"id": "B", "text": "`BULK INSERT` legado do SQL Server 2000", "isCorrect": False},
            {"id": "C", "text": "`BCP IN` via prompt de comando MS-DOS", "isCorrect": False},
            {"id": "D", "text": "`OPENROWSET` sem parâmetros", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A instrução T-SQL `COPY INTO` é a primitiva de alta performance no Fabric Warehouse para ingerir arquivos externos (Parquet e CSV) diretamente do Azure Storage para tabelas do Warehouse de forma totalmente paralelizada.",
            [
                "<strong>B, C e D:</strong> Métodos antigos e não otimizados para a arquitetura de nuvem do Fabric Warehouse."
            ],
            "Ingestão T-SQL de alto desempenho no Warehouse: Comando `COPY INTO`."
        )
    },
    {
        "id": "d2_q44",
        "domain": "domain2",
        "type": "single",
        "title": "Gerenciamento de Estatísticas Automáticas no Warehouse",
        "question": "Como o Fabric Warehouse gerencia estatísticas de colunas para garantir que o otimizador de consultas gere planos de execução eficientes?",
        "options": [
            {"id": "A", "text": "As estatísticas devem ser calculadas manualmente executando scripts a cada 10 minutos.", "isCorrect": False},
            {"id": "B", "text": "O Fabric Warehouse cria e atualiza estatísticas automaticamente em segundo plano quando as consultas são executadas (`AUTO_CREATE_STATISTICS` e `AUTO_UPDATE_STATISTICS`).", "isCorrect": True},
            {"id": "C", "text": "O Fabric não utiliza estatísticas em suas consultas.", "isCorrect": False},
            {"id": "D", "text": "As estatísticas são enviadas por fax para o suporte do Azure.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric Warehouse possui criação e atualização automática de estatísticas (Auto-Stats). Quando uma consulta faz predicados de filtro ou junção em uma coluna sem estatísticas recentes, o motor gera e atualiza as estatísticas em segundo plano de forma transparente.",
            [
                "<strong>A, C e D:</strong> Falsas declarações sem embasamento técnico."
            ],
            "Estatísticas no Fabric Warehouse: Atualização automática e dinâmica por padrão pelo motor analítico."
        )
    },
    {
        "id": "d2_q45",
        "domain": "domain2",
        "type": "single",
        "title": "Diferença entre Lakehouse (SQL Analytics Endpoint) e Warehouse",
        "question": "Qual é a diferença fundamental no controle de gravação entre o SQL Analytics Endpoint de um Lakehouse e um Fabric Warehouse?",
        "options": [
            {"id": "A", "text": "O SQL Analytics Endpoint do Lakehouse é estritamente somente-leitura (Read-Only) para comandos T-SQL; já o Warehouse suporta operações T-SQL completas de leitura e gravação (DDL e DML: INSERT, UPDATE, DELETE, CREATE TABLE).", "isCorrect": True},
            {"id": "B", "text": "O SQL Endpoint permite gravar dados com INSERT, mas o Warehouse é somente-leitura.", "isCorrect": False},
            {"id": "C", "text": "Ambos são somente-leitura e não aceitam novos dados.", "isCorrect": False},
            {"id": "D", "text": "Não há nenhuma diferença técnica entre os dois itens.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "No Lakehouse, gravações em tabelas Delta são feitas via Apache Spark ou pipelines; o SQL Endpoint exposto fornece apenas uma camada de leitura relacional T-SQL (Read-Only). O Fabric Warehouse, por outro lado, é um data warehouse completo com suporte nativo a comandos T-SQL DML de gravação (`INSERT`, `UPDATE`, `DELETE`, `MERGE`).",
            [
                "<strong>B, C e D:</strong> Inversões e declarações tecnicamente incorretas."
            ],
            "Diferença essencial: SQL Endpoint do Lakehouse = Read-Only no T-SQL. Fabric Warehouse = Read + Write completo no T-SQL."
        )
    },
    {
        "id": "d2_q46",
        "domain": "domain2",
        "type": "multi",
        "title": "Técnicas de Carregamento de Dados Sem Sobrecarga de Log Transacional",
        "question": "Quais DUAS práticas em T-SQL reduzem o bloqueio e otimizam a performance durante o carregamento de grandes massas de dados no Fabric Warehouse? (Selecione 2 alternativas)",
        "options": [
            {"id": "A", "text": "Utilizar `TRUNCATE TABLE` em vez de `DELETE FROM Tabela` sem cláusula WHERE para esvaziar tabelas de staging.", "isCorrect": True},
            {"id": "B", "text": "Utilizar comandos massivos `CREATE TABLE AS SELECT (CTAS)` ou `INSERT INTO ... SELECT` em vez de loops individuais com `INSERT ... VALUES`.", "isCorrect": True},
            {"id": "C", "text": "Inserir 1 registro por transação com `COMMIT TRANSACTION` a cada linha.", "isCorrect": False},
            {"id": "D", "text": "Desativar a conexão de rede durante o insert.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "`TRUNCATE TABLE` é uma operação DDL de desvinculação de metadados quase instantânea no OneLake, muito mais rápida e leve que o `DELETE`. Operações massivas em lote (`CTAS`, `INSERT ... SELECT`) aproveitam a paralelização colunar do motor distribuído.",
            [
                "<strong>C:</strong> Inserir linha por linha gera sobrecarga severa de transações e commits no log.",
                "<strong>D:</strong> Inviável operacionalmente."
            ],
            "Performance T-SQL: Use TRUNCATE em vez de DELETE; use CTAS ou INSERT-SELECT massivo em vez de inserts linha a linha."
        )
    },
    {
        "id": "d2_q47",
        "domain": "domain2",
        "type": "single",
        "title": "Views Indexadas e Particionamento no Fabric Warehouse",
        "question": "Um DBA sênior acostumado com SQL Server on-premises tenta criar um índice clusterizado tradicional (`CREATE CLUSTERED INDEX`) em uma tabela do Fabric Warehouse. Qual será o resultado?",
        "options": [
            {"id": "A", "text": "O comando falha com erro de sintaxe ou instrução não suportada, pois o Fabric Warehouse armazena dados colunarmente no formato Parquet aberto sem suporte a índices de árvore B (B-Tree) tradicionais.", "isCorrect": True},
            {"id": "B", "text": "O índice é criado instantaneamente em disco rígido SCSI.", "isCorrect": False},
            {"id": "C", "text": "A tabela é convertida em um arquivo Microsoft Word.", "isCorrect": False},
            {"id": "D", "text": "O servidor SQL é reinicializado automaticamente.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric Warehouse não utiliza índices B-Tree clássicos nem índices clusterizados físicos tradicionais do SQL Server. A indexação é inerente à estrutura colunar Parquet/Delta, com ordenação por V-Order e estatísticas de limites de colunas (Min/Max data skipping).",
            [
                "<strong>B, C e D:</strong> Falsas declarações."
            ],
            "No Fabric Warehouse: Não existem índices B-Tree tradicionais (`CREATE INDEX`). A performance vem do Parquet colunar e V-Order."
        )
    },
    {
        "id": "d2_q48",
        "domain": "domain2",
        "type": "single",
        "title": "Mecanismo de Desconexão Automática e Ociosidade no Warehouse",
        "question": "Como o Fabric Warehouse gerencia a computação quando nenhuma consulta T-SQL é executada por um período prolongado?",
        "options": [
            {"id": "A", "text": "Os recursos computacionais são suspensos dinamicamente para liberar capacidade na F-SKU, sem que nenhum dado seja perdido no OneLake.", "isCorrect": True},
            {"id": "B", "text": "Todas as tabelas são apagadas após 1 hora de inatividade.", "isCorrect": False},
            {"id": "C", "text": "O usuário recebe uma multa por inatividade no portal do Azure.", "isCorrect": False},
            {"id": "D", "text": "O Warehouse é convertido em um arquivo PDF.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A arquitetura serverless do Fabric Warehouse é desacoplada do OneLake: quando não há consultas ativas, os nós computacionais ficam ociosos ou liberados, poupando Capacity Units do F-SKU compartilhado.",
            [
                "<strong>B, C e D:</strong> Declarações absurdas e incorretas."
            ],
            "Computação Serverless no Warehouse: Computação sob demanda liberando CUs quando não há consultas ativas."
        )
    },

    # --- REAL-TIME INTELLIGENCE, EVENTSTREAM & EVENTHOUSE (Questões 49 a 70) ---
    {
        "id": "d2_q49",
        "domain": "domain2",
        "type": "single",
        "title": "Fontes Nativas Suportadas pelo Eventstream",
        "question": "Qual das seguintes opções representa uma fonte de dados de streaming em tempo real suportada nativamente para ingestão contínua em um Fabric Eventstream?",
        "options": [
            {"id": "A", "text": "Azure Event Hubs / IoT Hub", "isCorrect": True},
            {"id": "B", "text": "Disquete magnético ZipDrive", "isCorrect": False},
            {"id": "C", "text": "Arquivo CSV estático em CD-ROM", "isCorrect": False},
            {"id": "D", "text": "Tabela de impressão do Windows 95", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric Eventstream suporta ingestão contínua a partir de fontes como: Azure Event Hubs, Azure IoT Hub, clusters Apache Kafka externos, Azure SQL Database CDC (Change Data Capture) e Custom Endpoints para envio via API REST.",
            [
                "<strong>B, C e D:</strong> Falsos e sem relevância em nuvem."
            ],
            "Fontes nativas de Eventstream: Event Hubs, IoT Hub, Apache Kafka e CDC de bancos de dados."
        )
    },
    {
        "id": "d2_q50",
        "domain": "domain2",
        "type": "single",
        "title": "Destinos Nativos do Eventstream",
        "question": "Em um fluxo de dados em tempo real montado no Fabric Eventstream, para quais destinos os eventos processados podem ser despachados diretamente?",
        "options": [
            {"id": "A", "text": "Tabela Delta no Lakehouse, KQL Database (Eventhouse), Custom App e Reflex (Data Activator)", "isCorrect": True},
            {"id": "B", "text": "Apenas para uma impressora térmica de cupons fiscais.", "isCorrect": False},
            {"id": "C", "text": "Apenas para arquivos compactados em fita DAT.", "isCorrect": False},
            {"id": "D", "text": "Apenas para o Bloco de Notas do Windows.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Eventstream é um roteador de eventos de alta taxa: ele pode entregar os dados simultaneamente para um KQL Database (Eventhouse) para consultas em tempo real, para um Lakehouse (tabela Delta Parquet) para histórico, para o Data Activator (Reflex) para alertas automatizados, ou para um Custom Endpoint.",
            [
                "<strong>B, C e D:</strong> Destinos fictícios sem relevância analítica."
            ],
            "Destinos de Eventstream: Lakehouse (Delta), Eventhouse (KQL), Reflex (Data Activator) e Custom Endpoints."
        )
    },
    {
        "id": "d2_q51",
        "domain": "domain2",
        "type": "single",
        "title": "Políticas de Atualização em KQL (Update Policies)",
        "question": "Como uma Política de Atualização (Update Policy) em uma tabela de um banco KQL (Eventhouse) viabiliza transformações em tempo real durante a ingestão?",
        "options": [
            {"id": "A", "text": "Executa uma função KQL automaticamente sempre que novos dados são ingeridos na tabela de origem (Raw), inserindo os dados transformados na tabela de destino transacionalmente.", "isCorrect": True},
            {"id": "B", "text": "Exige a execução manual de um job Spark a cada minuto.", "isCorrect": False},
            {"id": "C", "text": "Apaga os dados da tabela de destino se houver registros repetidos.", "isCorrect": False},
            {"id": "D", "text": "Desliga o servidor KQL se a consulta demorar mais de 1 segundo.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "As Update Policies do KQL funcionam como 'triggers' transacionais de ingestão: quando novos lotes de eventos entram na tabela bruta de ingestão, o motor executa uma consulta/função KQL nos novos dados e insere o resultado limpo e transformado na tabela de destino em tempo real sem sobrecarga de pipelines adicionais.",
            [
                "<strong>B, C e D:</strong> Falsas declarações sem base na arquitetura do KQL."
            ],
            "KQL Update Policy = Transformação de streaming acionada na ingestão, populando tabelas derivadas em tempo real."
        )
    },
    {
        "id": "d2_q52",
        "domain": "domain2",
        "type": "single",
        "title": "Cache Dinâmico no Eventhouse: Hot Cache vs Cold Cache",
        "question": "Em uma base de dados KQL com 50 Terabytes de logs de telemetria dos últimos 3 anos, os analistas consultam com frequência apenas os dados dos últimos 7 dias. Qual política de retenção e cache deve ser configurada na tabela para otimizar custos e manter tempos de resposta em milissegundos?",
        "options": [
            {"id": "A", "text": "Hot Cache Policy = 7 dias; Soft Delete (Retention Policy) = 1095 dias (3 anos).", "isCorrect": True},
            {"id": "B", "text": "Hot Cache Policy = 1095 dias; Retention Policy = 7 dias.", "isCorrect": False},
            {"id": "C", "text": "Desativar o cache completamente e ler os dados por fita magnética.", "isCorrect": False},
            {"id": "D", "text": "Apagar os dados após 24 horas para não gastar memória.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "No KQL Database (Eventhouse), os dados em 'Hot Cache' são mantidos em discos SSD ultra-rápidos e memória RAM local nos nós para consultas em milissegundos. Dados em 'Cold Storage' permanecem no OneLake/Blob a custo baixíssimo e são lidos sob demanda. Configurar Hot Cache = 7 dias e Soft Delete = 3 anos atende perfeitamente ao requisito com mínimo custo.",
            [
                "<strong>B:</strong> Inverteu a lógica; manter 3 anos em Hot Cache custaria excessivamente em memória e SSDs.",
                "<strong>C e D:</strong> Não atendem aos requisitos de negócio."
            ],
            "KQL Caching: Hot Cache = Período de consulta frequente (em SSD/RAM); Retention = Tempo total de vida dos dados."
        )
    },
    {
        "id": "d2_q53",
        "domain": "domain2",
        "type": "single",
        "title": "Função KQL `arg_max()` para Desduplicação de Eventos",
        "question": "Em uma tabela KQL que recebe múltiplos eventos de status de dispositivos IoT com atualizações contínuas, qual operador KQL deve ser utilizado para recuperar o registro mais recente de cada dispositivo pelo campo `Timestamp`?",
        "options": [
            {"id": "A", "text": "`Tabela | summarize arg_max(Timestamp, *) by DeviceId`", "isCorrect": True},
            {"id": "B", "text": "`Tabela | order by Timestamp desc | take 1`", "isCorrect": False},
            {"id": "C", "text": "`Tabela | where DeviceId == max(Timestamp)`", "isCorrect": False},
            {"id": "D", "text": "`Tabela | delete duplicates where Timestamp < now()`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O operador de agregação `summarize arg_max(Timestamp, *) by DeviceId` em KQL encontra o valor máximo da coluna de tempo para cada chave de agrupamento (`DeviceId`) e projeta todas as outras colunas correspondentes àquela linha específica, sendo a forma idiomática e mais eficiente de desduplicação e obtenção do último estado em KQL.",
            [
                "<strong>B:</strong> `take 1` retornaria apenas 1 único dispositivo em toda a tabela.",
                "<strong>C:</strong> Sintaxe inválida em KQL.",
                "<strong>D:</strong> O KQL não possui o comando DML `delete duplicates`."
            ],
            "Obter o estado mais recente em KQL: `summarize arg_max(Timestamp, *) by EntidadeId`."
        )
    },
    {
        "id": "d2_q54",
        "domain": "domain2",
        "type": "single",
        "title": "Operadores de String em KQL: `has` vs `contains`",
        "question": "Ao pesquisar um termo específico em uma coluna de texto livre contendo bilhões de logs de mensagens de erro no KQL, por que a documentação oficial recomenda fortemente o uso do operador `has` em vez de `contains`?",
        "options": [
            {"id": "A", "text": "`has` busca por termos indexados de palavras inteiras usando o índice de inversão colunar (infinidades de vezes mais rápido), enquanto `contains` realiza varredura linear de substrings sem usar o índice.", "isCorrect": True},
            {"id": "B", "text": "`contains` foi descontinuado e gera erro de sintaxe.", "isCorrect": False},
            {"id": "C", "text": "`has` aceita apenas números inteiros positivos.", "isCorrect": False},
            {"id": "D", "text": "Ambos possuem o mesmo plano de execução e o mesmo tempo de resposta.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "No Kusto Query Language (KQL), colunas de texto são indexadas por termos compostos por caracteres alfanuméricos. O operador `has` utiliza o índice invertido para localizar a palavra exata em microssegundos. Já o operador `contains` busca substrings arbitrárias (semelhante a `LIKE '%termo%'` no SQL), ignorando o índice e forçando a varredura linear de todos os textos.",
            [
                "<strong>B:</strong> `contains` é válido, mas deve ser evitado por questões de desempenho em big data.",
                "<strong>C e D:</strong> Falsas declarações sobre os operadores de string do KQL."
            ],
            "Desempenho KQL: Use `has` para busca de termos indexados (palavras inteiras). Evite `contains` em grandes volumes."
        )
    },
    {
        "id": "d2_q55",
        "domain": "domain2",
        "type": "single",
        "title": "Ingestion Batching Policy no KQL Database",
        "question": "Um banco de dados KQL está recebendo milhares de pequenas mensagens por segundo via streaming. Como a 'Ingestion Batching Policy' gerencia a formação de arquivos de dados no backend?",
        "options": [
            {"id": "A", "text": "Agrupa os eventos com base em limiares configuráveis de tempo (ex: 5 minutos), tamanho de buffer (ex: 1 GB) ou quantidade de itens (ex: 1.000 itens), otimizando a criação de extensões de dados (shards/extents).", "isCorrect": True},
            {"id": "B", "text": "Cria um arquivo Parquet separado para cada evento de 100 bytes recebido.", "isCorrect": False},
            {"id": "C", "text": "Bloqueia a rede até que 10 milhões de eventos estejam na memória.", "isCorrect": False},
            {"id": "D", "text": "Rejeita qualquer mensagem com menos de 1 Megabyte.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A política de loteamento de ingestão (`IngestionBatching`) define quando o motor KQL deve consolidar os dados em trânsito e comitá-los em extents permanentes. Ela é governada por três limites: tempo máximo de espera, tamanho máximo de dados não comprimidos e número máximo de registros.",
            [
                "<strong>B:</strong> Criar um arquivo por mensagem causaria degradação severa por excesso de pequenos arquivos.",
                "<strong>C e D:</strong> Valores e regras que não existem na arquitetura do Kusto."
            ],
            "Ingestion Batching Policy no KQL: Agrupa dados em trânsito por tempo, tamanho ou contagem antes de gravar extents."
        )
    },
    {
        "id": "d2_q56",
        "domain": "domain2",
        "type": "single",
        "title": "Agrupamento Temporal com a Função `bin()` em KQL",
        "question": "Qual consulta KQL abaixo agrupa corretamente a quantidade total de requisições de API recebidas em intervalos contíguos de 15 minutos?",
        "options": [
            {"id": "A", "text": "`ApiLogs | summarize Total = count() by bin(Timestamp, 15m)`", "isCorrect": True},
            {"id": "B", "text": "`ApiLogs | group by Timestamp every 15 minutes`", "isCorrect": False},
            {"id": "C", "text": "`ApiLogs | select count() partition by round(Timestamp, 15)`", "isCorrect": False},
            {"id": "D", "text": "`ApiLogs | sum(Timestamp) / 15`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Em KQL, o agrupamento por intervalos de tempo ou faixas numéricas é feito com a função `bin(expressao, tamanho_do_intervalo)` combinada com a instrução `summarize ... by ...`. O intervalo de 15 minutos é expresso como `15m`.",
            [
                "<strong>B, C e D:</strong> Sintaxes inválidas no Kusto Query Language."
            ],
            "Agrupamento temporal em KQL: `summarize count() by bin(Timestamp, 15m)`."
        )
    },
    {
        "id": "d2_q57",
        "domain": "domain2",
        "type": "single",
        "title": "Integração do Data Activator (Reflex) com Eventhouse",
        "question": "Qual é a principal função do Data Activator (Reflex) quando conectado a streams em tempo real no Microsoft Fabric?",
        "options": [
            {"id": "A", "text": "Monitorar dados e disparar ações automatizadas (como alertas no Microsoft Teams, e-mails pelo Outlook ou chamadas de webhook) quando regras e limiares de condição são atingidos em tempo real.", "isCorrect": True},
            {"id": "B", "text": "Desligar o gerador de energia elétrica do escritório.", "isCorrect": False},
            {"id": "C", "text": "Substituir o firewall corporativo por um roteador Wi-Fi doméstico.", "isCorrect": False},
            {"id": "D", "text": "Converter código Python em código assembly de 8 bits.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Data Activator (Reflex) é a solução no-code/low-code do Fabric para detecção de condições e disparo de ações em tempo real. Ele rastreia métricas e eventos vindos do Eventstream, Eventhouse ou relatórios do Power BI e dispara notificações (Teams, Email) ou pipelines.",
            [
                "<strong>B, C e D:</strong> Definições absurdas e irrelevantes."
            ],
            "Data Activator (Reflex) = Automação acionada por eventos e alertas em tempo real baseados em regras de negócio."
        )
    },
    {
        "id": "d2_q58",
        "domain": "domain2",
        "type": "single",
        "title": "Extensões de Dados (Extents) e Sharding no KQL Database",
        "question": "Como os dados são fisicamente organizados e compactados internamente dentro de uma tabela de banco de dados KQL (Eventhouse)?",
        "options": [
            {"id": "A", "text": "Em estruturas imutáveis chamadas 'Extents' (ou Shards), que armazenam dados colunarmente compactados e indexados de forma independente.", "isCorrect": True},
            {"id": "B", "text": "Em um único arquivo texto `.txt` sequencial compartilhado por todos os nós.", "isCorrect": False},
            {"id": "C", "text": "Em tabelas B-Tree bloqueadas com lock exclusivo de banco de dados.", "isCorrect": False},
            {"id": "D", "text": "Em planilhas de cálculo vinculadas via OLE.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O motor Kusto organiza o armazenamento de tabelas em fragmentos independentes e imutáveis chamados 'Extents' (ou shards). Cada extent contém colunas comprimidas e índices de texto invertidos. Consultas KQL processam extents em paralelo massivo nos nós do cluster.",
            [
                "<strong>B, C e D:</strong> Falsas noções sobre a arquitetura colunar distribuída do Kusto."
            ],
            "KQL Storage Architecture: Tabelas são coleções de fragmentos colunares imutáveis chamados 'Extents'."
        )
    },

    # --- MIRRORING & CDC (Questões 59 a 68) ---
    {
        "id": "d2_q59",
        "domain": "domain2",
        "type": "single",
        "title": "Mecanismo de Mirroring no Microsoft Fabric",
        "question": "Qual é a principal proposta de valor do recurso 'Fabric Mirroring' para bancos de dados como Azure SQL Database, Snowflake ou Cosmos DB?",
        "options": [
            {"id": "A", "text": "Replicar dados continuamente em tempo quase real para o OneLake em formato Delta Parquet aberto sem criar pipelines manuais complexos de ETL e sem impactar a capacidade computacional da fonte transacional com consultas pesadas.", "isCorrect": True},
            {"id": "B", "text": "Substituir o banco transacional e apagar as tabelas da fonte de origem.", "isCorrect": False},
            {"id": "C", "text": "Fazer backup dos dados em fita magnética física para envio postal.", "isCorrect": False},
            {"id": "D", "text": "Obrigar os desenvolvedores a reescrever todas as aplicações em linguagem C.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric Mirroring oferece replicação contínua (CDC nativo) de bases de dados transacionais externas diretamente para tabelas Delta no OneLake. Os dados replicados ficam disponíveis imediatamente para consultas T-SQL, Spark e Power BI Direct Lake sem custos de ETL contínuo.",
            [
                "<strong>B, C e D:</strong> Incorretos e contrários aos objetivos do Mirroring."
            ],
            "Fabric Mirroring = Zero-ETL / CDC contínuo de fontes transacionais diretamente para tabelas Delta no OneLake."
        )
    },
    {
        "id": "d2_q60",
        "domain": "domain2",
        "type": "single",
        "title": "Pré-requisito de CDC para Espelhamento de Azure SQL Database",
        "question": "Para habilitar o Mirroring de um banco de dados Azure SQL Database no Microsoft Fabric, qual recurso deve estar previamente habilitado no banco transacional de origem?",
        "options": [
            {"id": "A", "text": "Change Data Capture (CDC) e uma chave de identidade gerenciada/permissão de leitura para o Fabric.", "isCorrect": True},
            {"id": "B", "text": "Desativação de todos os índices clusterizados.", "isCorrect": False},
            {"id": "C", "text": "Remoção de todas as senhas dos administradores.", "isCorrect": False},
            {"id": "D", "text": "Instalação do Microsoft Office 2003 no servidor de banco de dados.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Mirroring para Azure SQL Database baseia-se na captura contínua de alterações via Change Data Capture (CDC) ou Change Tracking nativo do SQL Server. Sem o CDC ativado e as permissões de acesso adequadas concedidas ao Fabric, o serviço de espelhamento não consegue ler o log de transações.",
            [
                "<strong>B, C e D:</strong> Requisitos falsos e prejudiciais à segurança."
            ],
            "Pré-requisito de Mirroring no SQL: CDC ativado e permissões de conexão apropriadas."
        )
    },
    {
        "id": "d2_q61",
        "domain": "domain2",
        "type": "single",
        "title": "Consulta aos Dados Espelhados via SQL Endpoint",
        "question": "Como os analistas corporativos consultam os dados de um banco de dados que foi espelhado (Mirrored Database) no Fabric?",
        "options": [
            {"id": "A", "text": "Conectando-se ao SQL Analytics Endpoint gerado automaticamente para o Mirrored Database, executando consultas T-SQL padrão com desempenho colunar.", "isCorrect": True},
            {"id": "B", "text": "Fazendo login direto no console SSH da máquina virtual do banco original.", "isCorrect": False},
            {"id": "C", "text": "Solicitando os dados por telefone para o suporte da Microsoft.", "isCorrect": False},
            {"id": "D", "text": "Os dados espelhados não podem ser consultados por T-SQL.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Cada Mirrored Database criado no Fabric gera automaticamente um SQL Analytics Endpoint correspondente. Os analistas podem conectar ferramentas como SSMS, Power BI ou Azure Data Studio para consultar as tabelas Delta espelhadas via T-SQL sem tocar no banco transacional original.",
            [
                "<strong>B, C e D:</strong> Incorretos."
            ],
            "Mirrored Database inclui automaticamente um SQL Analytics Endpoint para leitura T-SQL no OneLake."
        )
    },
    {
        "id": "d2_q62",
        "domain": "domain2",
        "type": "single",
        "title": "Latência Típica de Replicação no Fabric Mirroring",
        "question": "Qual é a latência esperada na sincronização de dados alterados na origem quando o Fabric Mirroring está em execução saudável?",
        "options": [
            {"id": "A", "text": "Latência quase em tempo real (tipicamente de segundos a poucos minutos).", "isCorrect": True},
            {"id": "B", "text": "Latência fixa de 24 horas (uma vez por noite).", "isCorrect": False},
            {"id": "C", "text": "Latência fixa de 30 dias.", "isCorrect": False},
            {"id": "D", "text": "Sincronização instantânea na velocidade da luz sem nenhum nanosegundo de atraso.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric Mirroring opera em modelo de replicação quase em tempo real (near real-time): as alterações registradas no log transacional são continuamente lidas, formatadas em Delta Parquet e comitadas no OneLake com latência típica de poucos segundos a minutos.",
            [
                "<strong>B e C:</strong> Descreveriam processos de lote tradicionais diários/mensais, não espelhamento.",
                "<strong>D:</strong> Não existe replicação distribuída com latência zero física absoluta."
            ],
            "Fabric Mirroring opera em near real-time (segundos a poucos minutos de latência)."
        )
    },
    {
        "id": "d2_q63",
        "domain": "domain2",
        "type": "single",
        "title": "Snowflake Mirroring para Microsoft Fabric",
        "question": "Uma organização tem dados históricos críticos no Snowflake e deseja consolidá-los no OneLake do Fabric para cruzamento analítico com dados do Power BI. O que o Mirroring para Snowflake realiza?",
        "options": [
            {"id": "A", "text": "Replica de forma transparente e contínua os dados do Snowflake para tabelas Delta Parquet no OneLake gerenciado pelo Fabric.", "isCorrect": True},
            {"id": "B", "text": "Cancela o contrato da Snowflake e migra os servidores físicos para a Microsoft.", "isCorrect": False},
            {"id": "C", "text": "Transforma todas as tabelas em arquivos CSV compartilhados na rede local.", "isCorrect": False},
            {"id": "D", "text": "Bloqueia o acesso a qualquer usuário fora da rede interna.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Mirroring para Snowflake conecta-se à conta Snowflake e sincroniza os esquemas e dados selecionados diretamente para o OneLake no formato Delta Lake, permitindo análise unificada no Fabric sem duplicação manual de pipelines de engenharia.",
            [
                "<strong>B, C e D:</strong> Declarações sem sentido técnico."
            ],
            "Snowflake Mirroring = Sincronização contínua de bases Snowflake diretamente para o OneLake em Delta Parquet."
        )
    },
    {
        "id": "d2_q64",
        "domain": "domain2",
        "type": "single",
        "title": "Isolamento de Carga Transacional via Mirroring",
        "question": "Por que a equipe de infraestrutura de TI aprova o uso do Fabric Mirroring em vez de permitir que analistas de BI conectem o Power BI diretamente ao banco de dados transacional de produção em modo DirectQuery?",
        "options": [
            {"id": "A", "text": "Porque o Mirroring lê apenas os logs de transação (CDC) de forma assíncrona e transfere as consultas analíticas pesadas para o Fabric, eliminando a concorrência e o risco de lentidão ou travamento na aplicação OLTP.", "isCorrect": True},
            {"id": "B", "text": "Porque o Power BI não consegue se conectar a bancos SQL.", "isCorrect": False},
            {"id": "C", "text": "Porque o Fabric apaga o banco transacional periodicamente.", "isCorrect": False},
            {"id": "D", "text": "Porque consultas DirectQuery em bancos SQL são ilegais.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Consultas analíticas pesadas (relatórios de BI com agregações de milhões de linhas) executadas diretamente em bancos transacionais (OLTP) causam bloqueios de tabela (`LOCKS`), contenção de recursos e travamentos nas aplicações de negócios. O Mirroring isola completamente a carga de consulta no OneLake.",
            [
                "<strong>B, C e D:</strong> Falsas declarações."
            ],
            "Vantagem do Mirroring: Isola a aplicação de produção contra gargalos de relatórios de BI pesados."
        )
    },

    # --- MODELAGEM MEDALLION & QUALIDADE DE DADOS (Questões 65 a 82) ---
    {
        "id": "d2_q65",
        "domain": "domain2",
        "type": "single",
        "title": "Camadas da Arquitetura Medallion: Bronze, Prata e Ouro",
        "question": "Na arquitetura Medallion implementada no Microsoft Fabric, qual é o papel específico da camada 'Silver' (Prata)?",
        "options": [
            {"id": "A", "text": "Armazenar dados brutos exatamente como vieram da fonte original sem nenhuma limpeza ou tipagem.", "isCorrect": False},
            {"id": "B", "text": "Armazenar dados limpos, enriquecidos, validados e padronizados com esquema consistente (Enterprise View / Visão Corporativa da Verdade).", "isCorrect": True},
            {"id": "C", "text": "Conter agregados de negócios prontos para consumo com medidas DAX e modelos estrela estritos.", "isCorrect": False},
            {"id": "D", "text": "Guardar backups de e-mails de desenvolvedores aposentados.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Na arquitetura Medallion: 1) Bronze = Dados brutos imutáveis (Raw); 2) Silver = Dados limpos, filtrados, padronizados e enriquecidos com tipagem de esquema consistente; 3) Gold = Modelagem dimensional final (Star Schema), agregações de negócios e dados prontos para relatórios corporativos.",
            [
                "<strong>A:</strong> Essa é a definição da camada Bronze.",
                "<strong>C:</strong> Essa é a definição da camada Gold.",
                "<strong>D:</strong> Incorreto."
            ],
            "Arquitetura Medallion: Bronze = Raw / Bruto; Silver = Cleaned & Conformed / Limpo; Gold = Business Aggregated / Dimensional."
        )
    },
    {
        "id": "d2_q66",
        "domain": "domain2",
        "type": "single",
        "title": "Modelagem Estrela (Star Schema) na Camada Gold",
        "question": "Por que a Microsoft recomenda a modelagem dimensional em esquema estrela (Star Schema) na camada Gold para consumo pelo Power BI em modo Direct Lake?",
        "options": [
            {"id": "A", "text": "Porque o esquema estrela com tabelas de fatos e dimensões desacopladas permite que o motor VertiPaq realize junções colunares com o menor custo de memória e excelente compressão colunar por dicionário.", "isCorrect": True},
            {"id": "B", "text": "Porque o Direct Lake só funciona se todas as tabelas tiverem apenas 3 colunas.", "isCorrect": False},
            {"id": "C", "text": "Porque tabelas desnormalizadas gigantescas com 500 colunas são sempre mais rápidas no Power BI.", "isCorrect": False},
            {"id": "D", "text": "O esquema estrela foi abandonado pela indústria de BI.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Star Schema (esquema estrela) organiza dados em tabelas de fatos numéricas estreitas ligadas a dimensões descritivas. O motor analítico colunar do Power BI (VertiPaq) é amplamente otimizado para essa topologia, atingindo taxas máximas de compressão por dicionário e planos de junção simplificados.",
            [
                "<strong>B e C:</strong> Falsos conceitos de modelagem.",
                "<strong>D:</strong> O Star Schema continua sendo o padrão de ouro oficial da engenharia analítica da Microsoft."
            ],
            "Diretriz oficial: Sempre modele a camada Gold em Star Schema (Fatos + Dimensões) para máxima performance no Direct Lake."
        )
    },
    {
        "id": "d2_q67",
        "domain": "domain2",
        "type": "multi",
        "title": "Validação de Qualidade de Dados com PySpark na Camada Silver",
        "question": "Quais DUAS ações comumente implementadas via código PySpark em um Notebook garantem a integridade dos dados durante a promoção da camada Bronze para a camada Silver? (Selecione 2 alternativas)",
        "options": [
            {"id": "A", "text": "Desduplicação de registros por chave primária de negócio usando `dropDuplicates(['id'])`.", "isCorrect": True},
            {"id": "B", "text": "Aplicação de regras de validação e descarte/quarentena de registros com campos obrigatórios nulos (`filter(col('data').isNotNull())`).", "isCorrect": True},
            {"id": "C", "text": "Criptografia dos nomes de todas as colunas com chave privada RSA.", "isCorrect": False},
            {"id": "D", "text": "Substituição de todas as datas pelo dia 1º de Janeiro de 1900.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A transformação da camada Bronze para Silver tem como foco a qualidade de dados: desduplicação por chaves naturais de negócio, validação de tipos de dados, descarte ou isolamento em quarentena de registros com valores nulos críticos ou fora dos limites de conformidade.",
            [
                "<strong>C e D:</strong> Práticas incorretas que destruiriam a usabilidade e qualidade dos dados analíticos."
            ],
            "Silver Layer: Foco em limpeza, desduplicação (`dropDuplicates`), validação de nulos e conformidade de esquema."
        )
    },
    {
        "id": "d2_q68",
        "domain": "domain2",
        "type": "single",
        "title": "Estrutura de Quarentena para Dados Inválidos",
        "question": "Ao ingerir dados brutos de pedidos na camada Bronze, alguns registros chegam com valores monetários negativos inválidos. Qual padrão arquitetural preserva o fluxo de dados dos pedidos sadios sem perder o registro dos pedidos com erro para auditoria?",
        "options": [
            {"id": "A", "text": "Padrão Quarentena (Dead-Letter Queue / Bad Records Table): os registros sadios são promovidos para a camada Silver normalmente, enquanto os registros com erro são roteados para uma tabela Delta separada de 'Quarentena' para auditoria e retificação.", "isCorrect": True},
            {"id": "B", "text": "Abortar o pipeline inteiro e não processar nenhum pedido válido.", "isCorrect": False},
            {"id": "C", "text": "Multiplicar o valor negativo por zero e comitar silenciosamente.", "isCorrect": False},
            {"id": "D", "text": "Desligar o banco de dados da empresa.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O padrão de Quarentena (Dead-Letter / Quarantine Table) separa os dados em dois fluxos condicionais: dados conformes seguem viagem para a camada Silver; registros violadores de regras são gravados em uma tabela isolada de quarentena com o motivo da falha anotado, permitindo que o negócio audite e reingira os registros retificados.",
            [
                "<strong>B:</strong> Abortar o pipeline penalizaria os 99% de pedidos válidos.",
                "<strong>C:</strong> Alterar silenciosamente o dado sem registro gera inconsistência contábil gravíssima."
            ],
            "Padrão de Quarentena no DP-700: Dados válidos avançam; dados inválidos são isolados em tabela de quarentena para auditoria."
        )
    },
    {
        "id": "d2_q69",
        "domain": "domain2",
        "type": "single",
        "title": "Manejo de Dados Semi-Estruturados (JSON) com PySpark",
        "question": "Um Lakehouse recebe arquivos JSON aninhados na camada Bronze. Qual função nativa do PySpark permite expandir um array de objetos JSON contido em uma coluna para que cada elemento do array se torne uma linha independente na tabela resultante?",
        "options": [
            {"id": "A", "text": "`explode()`", "isCorrect": True},
            {"id": "B", "text": "`collapse()`", "isCorrect": False},
            {"id": "C", "text": "`shrink()`", "isCorrect": False},
            {"id": "D", "text": "`concat_ws()`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A função `pyspark.sql.functions.explode(coluna_array)` extrai cada elemento de uma lista ou array presente em uma coluna e cria uma nova linha para cada elemento, duplicando os valores das demais colunas escalares correspondentes.",
            [
                "<strong>B e C:</strong> Funções inexistentes para esse propósito no PySpark.",
                "<strong>D:</strong> `concat_ws()` une strings separadas por delimitador em uma única linha."
            ],
            "Manipulação de arrays e JSON no Spark: Use `explode()` para transformar itens de uma lista em múltiplas linhas."
        )
    },
    {
        "id": "d2_q70",
        "domain": "domain2",
        "type": "single",
        "title": "Parseamento de Strings JSON com `from_json()`",
        "question": "Uma coluna de texto em uma tabela Delta contém strings com conteúdo no formato JSON (`{\"cliente\": \"Ana\", \"valor\": 150.0}`). Qual combinação de funções do PySpark deve ser utilizada para transformar essa string em uma coluna de estrutura fortemente tipada (StructType)?",
        "options": [
            {"id": "A", "text": "`from_json(col('json_string'), schema)` onde `schema` é um `StructType` definido com os campos e tipos esperados.", "isCorrect": True},
            {"id": "B", "text": "`to_json()` sem esquema definido.", "isCorrect": False},
            {"id": "C", "text": "`split(col('json_string'), ',')` com conversão forçada para inteiro.", "isCorrect": False},
            {"id": "D", "text": "`substring()` com índices fixos de 1 a 10.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A função `from_json(col, schema)` interpreta uma string com dados JSON e a converte em uma estrutura colunar Spark do tipo `StructType` de acordo com o esquema fornecido, permitindo acessar os campos internos com a notação de ponto (`coluna.cliente`).",
            [
                "<strong>B:</strong> `to_json()` faz o caminho inverso: converte uma estrutura colunar em string JSON.",
                "<strong>C e D:</strong> Manipulações de string frágeis e propensas a quebra."
            ],
            "String JSON para Colunas Fortemente Tipadas: `from_json(col, schema)`."
        )
    },
    {
        "id": "d2_q71",
        "domain": "domain2",
        "type": "single",
        "title": "Identificação de Mudanças de Esquema (Schema Evolution)",
        "question": "Ao gravar novos lotes de dados em uma tabela Delta existente via PySpark, uma nova coluna chamada `CanalVenda` foi adicionada na fonte. Como o desenvolvedor instrui o comando `write` a adicionar essa nova coluna na tabela Delta automaticamente sem falhar a execução?",
        "options": [
            {"id": "A", "text": "Adicionar a opção `.option('mergeSchema', 'true')` no comando de escrita do DataFrame.", "isCorrect": True},
            {"id": "B", "text": "Adicionar a opção `.option('forceOverwrite', 'true')` para apagar a tabela.", "isCorrect": False},
            {"id": "C", "text": "Excluir manualmente a pasta `_delta_log` no OneLake.", "isCorrect": False},
            {"id": "D", "text": "Renomear a coluna para ter o mesmo nome de uma coluna existente.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Por padrão, o Delta Lake protege contra inserções acidentais com esquemas diferentes (Schema Enforcement). Para permitir a evolução controlada do esquema com adição de novas colunas, utiliza-se a opção `.option('mergeSchema', 'true')` ou configura-se `spark.databricks.delta.schema.autoMerge.enabled = true`.",
            [
                "<strong>B:</strong> Sobrescrever a tabela apagaria todo o histórico existente.",
                "<strong>C:</strong> Destruiria a integridade transacional do Delta Lake."
            ],
            "Evolução de Esquema no Delta Lake: Use `.option('mergeSchema', 'true')` para adicionar novas colunas com segurança."
        )
    },
    {
        "id": "d2_q72",
        "domain": "domain2",
        "type": "single",
        "title": "Particionamento no Spark vs Particionamento Delta",
        "question": "Qual comando PySpark particiona um DataFrame na memória com reembaralhamento total de dados na rede (Full Shuffle) para garantir distribuição uniforme antes de operações pesadas?",
        "options": [
            {"id": "A", "text": "`df.repartition(numParticoes)`", "isCorrect": True},
            {"id": "B", "text": "`df.coalesce(numParticoes)`", "isCorrect": False},
            {"id": "C", "text": "`df.drop()`", "isCorrect": False},
            {"id": "D", "text": "`df.sample()`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "`repartition(n)` força um Full Shuffle na rede para redistribuir os dados em exatamente `n` partições de tamanho homogêneo, aumentando ou diminuindo o paralelismo. O método `coalesce(n)` apenas reduz o número de partições combinando partições existentes sem realizar full shuffle.",
            [
                "<strong>B:</strong> `coalesce` não faz full shuffle e não consegue aumentar o número de partições.",
                "<strong>C e D:</strong> Não têm relação com o particionamento de DataFrames."
            ],
            "`repartition()` = Redefine número de partições com Full Shuffle na rede. `coalesce()` = Reduz partições sem full shuffle."
        )
    },
    {
        "id": "d2_q73",
        "domain": "domain2",
        "type": "single",
        "title": "Uso de Broadcast Variables no PySpark",
        "question": "Em um algoritmo PySpark customizado, você possui um dicionário Python estático com 5.000 códigos postais e nomes de cidades (50 KB). Como disponibilizar esse dicionário de forma eficiente para que todas as tarefas dos executores acessem o mapa sem enviá-lo repetidamente em cada tarefa individual?",
        "options": [
            {"id": "A", "text": "Criar uma Variável de Transmissão (Broadcast Variable) usando `sc.broadcast(dicionario)`.", "isCorrect": True},
            {"id": "B", "text": "Gravar o dicionário em um banco de dados relacional e fazer uma consulta SELECT por registro.", "isCorrect": False},
            {"id": "C", "text": "Enviar o dicionário por e-mail para todos os nós.", "isCorrect": False},
            {"id": "D", "text": "Converter o dicionário em um arquivo MP4.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Broadcast Variables (`sc.broadcast(v)`) enviam uma única cópia em cache de uma variável somente-leitura para cada nó executor do cluster, em vez de empacotar uma cópia junto com cada tarefa individual. Isso reduz drasticamente a sobrecarga de serialização e tráfego de rede.",
            [
                "<strong>B, C e D:</strong> Falsas soluções que violam a eficiência computacional distribuída."
            ],
            "Compartilhamento estático de lookups no Spark: Use `sc.broadcast()` para distribuir cópias em cache nos nós."
        )
    },
    {
        "id": "d2_q74",
        "domain": "domain2",
        "type": "single",
        "title": "Persistência em Cache no Spark: `cache()` vs `persist()`",
        "question": "Qual é a diferença entre os métodos `df.cache()` e `df.persist()` no Apache Spark?",
        "options": [
            {"id": "A", "text": "`cache()` armazena os dados com o nível padrão de armazenamento (`MEMORY_AND_DISK`), enquanto `persist()` permite especificar explicitamente níveis de armazenamento (como `MEMORY_ONLY`, `DISK_ONLY`, ou opções serializadas).", "isCorrect": True},
            {"id": "B", "text": "`cache()` deleta o DataFrame e `persist()` salva no OneDrive.", "isCorrect": False},
            {"id": "C", "text": "`cache()` foi descontinuado no Spark 3.0.", "isCorrect": False},
            {"id": "D", "text": "Ambos salvam os dados em arquivos CSV no desktop local.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "`df.cache()` é simplesmente um atalho de conveniência que chama `persist(StorageLevel.MEMORY_AND_DISK)`. O método `df.persist(storageLevel)` oferece controle granular sobre onde o DataFrame será retido na memória ou disco durante a execução do job.",
            [
                "<strong>B, C e D:</strong> Declarações falsas sem fundamentação técnica."
            ],
            "`cache()` = persistência com nível padrão (`MEMORY_AND_DISK`). `persist(level)` = permite configurar o StorageLevel."
        )
    },
    {
        "id": "d2_q75",
        "domain": "domain2",
        "type": "single",
        "title": "Limpeza de Recursos em Cache com `unpersist()`",
        "question": "Após a conclusão das transformações pesadas que utilizaram um DataFrame mantido em cache com `df.cache()`, qual método deve ser invocado para liberar imediatamente a memória RAM dos nós executores?",
        "options": [
            {"id": "A", "text": "`df.unpersist()`", "isCorrect": True},
            {"id": "B", "text": "`df.delete()`", "isCorrect": False},
            {"id": "C", "text": "`df.drop()`", "isCorrect": False},
            {"id": "D", "text": "`del df` apenas no Python sem avisar o cluster Spark.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O método `df.unpersist()` instrui explicitamente os executores Spark a removerem os blocos do DataFrame armazenados na memória e disco, liberando espaço para futuras tarefas e prevenindo erros de OutOfMemory (OOM).",
            [
                "<strong>B e C:</strong> Métodos que alteram colunas ou não existem para limpeza de cache.",
                "<strong>D:</strong> A instrução `del df` no Python remove apenas a referência local no Driver, sem liberar o cache distribuído nos nós."
            ],
            "Liberação de memória de cache no Spark: Sempre execute `df.unpersist()` após o término das etapas dependentes."
        )
    },
    {
        "id": "d2_q76",
        "domain": "domain2",
        "type": "single",
        "title": "Funções de Janela SQL (Window Functions) com PySpark",
        "question": "Um engenheiro precisa calcular a média móvel de vendas dos últimos 3 dias para cada produto. Qual especificação de janela (`Window.partitionBy(...).orderBy(...)`) do PySpark define corretamente essa moldura de linhas (frame)?",
        "options": [
            {"id": "A", "text": "`Window.partitionBy('ProdutoId').orderBy('DataVenda').rowsBetween(-2, 0)`", "isCorrect": True},
            {"id": "B", "text": "`Window.all().rows(3)`", "isCorrect": False},
            {"id": "C", "text": "`Window.orderBy('Preco').limit(3)`", "isCorrect": False},
            {"id": "D", "text": "`Window.partitionBy('Tudo').filter(3)`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Para calcular a média incluindo o dia atual e os 2 dias imediatamente anteriores (totalizando 3 dias), utiliza-se `Window.partitionBy('ProdutoId').orderBy('DataVenda').rowsBetween(-2, 0)` ou `Window.rangeBetween(-2, 0)`. Isso delimita o frame de agregação da função de janela.",
            [
                "<strong>B, C e D:</strong> Sintaxes inválidas na API de Janelas do PySpark."
            ],
            "Window Functions: `rowsBetween(-2, 0)` inclui a linha atual (0) e as duas anteriores (-2)."
        )
    },
    {
        "id": "d2_q77",
        "domain": "domain2",
        "type": "single",
        "title": "Tratamento de Arquivos Delta Corrompidos com `FSCK REPAIR LIBRARIES`",
        "question": "Em caso de falha de gravação ou inconsistência na tabela de catálogo, qual comando de manutenção verifica a integridade de arquivos do catálogo Metastore do Spark?",
        "options": [
            {"id": "A", "text": "`MSCK REPAIR TABLE <tabela>`", "isCorrect": True},
            {"id": "B", "text": "`SCAN HARD DISK C:`", "isCorrect": False},
            {"id": "C", "text": "`FORMAT DRIVE FAT32`", "isCorrect": False},
            {"id": "D", "text": "`REBOOT WORKSPACE`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "`MSCK REPAIR TABLE` atualiza o catálogo de metadados identificando novas partições que foram gravadas diretamente no armazenamento físico e sincronizando o metastore.",
            [
                "<strong>B, C e D:</strong> Comandos sem qualquer relação com a governança de metadados do Spark."
            ],
            "Sincronização de catálogo e partições no Metastore: `MSCK REPAIR TABLE`."
        )
    },
    {
        "id": "d2_q78",
        "domain": "domain2",
        "type": "single",
        "title": "Uso do Operador `CASE WHEN` em PySpark e T-SQL",
        "question": "Qual é a função do PySpark equivalente à instrução SQL `CASE WHEN condicao THEN valor1 ELSE valor2 END` para categorização condicional de colunas em um DataFrame?",
        "options": [
            {"id": "A", "text": "`when(condicao, valor1).otherwise(valor2)`", "isCorrect": True},
            {"id": "B", "text": "`if_then_else(condicao, valor1, valor2)`", "isCorrect": False},
            {"id": "C", "text": "`switch_case(valor1, valor2)`", "isCorrect": False},
            {"id": "D", "text": "`choose(condicao, 1, 2)`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "No PySpark, a avaliação condicional em colunas utiliza a combinação encadeada de funções `pyspark.sql.functions.when(condicao, valor).when(...).otherwise(valor_padrao)`.",
            [
                "<strong>B, C e D:</strong> Funções inexistentes na biblioteca oficial de funções do Spark SQL."
            ],
            "Condicional no PySpark: `when(cond, val).otherwise(default)`."
        )
    },
    {
        "id": "d2_q79",
        "domain": "domain2",
        "type": "single",
        "title": "Geração de Coluna com Timestamp de Ingestão e Criptografia HASH",
        "question": "Durante a ingestão na camada Bronze, a política de auditoria exige que cada linha gravada contenha um timestamp da execução e um hash criptográfico das colunas identificadoras para verificação de duplicidade. Quais funções PySpark atendem a esse requisito?",
        "options": [
            {"id": "A", "text": "`.withColumn('IngestionTime', current_timestamp()).withColumn('RowHash', sha2(concat_ws('||', col('id'), col('codigo')), 256))`", "isCorrect": True},
            {"id": "B", "text": "`.withColumn('Time', 'now').withColumn('Hash', '123')`", "isCorrect": False},
            {"id": "C", "text": "`.add_date().add_random()`", "isCorrect": False},
            {"id": "D", "text": "`.append_system_metrics()`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "`current_timestamp()` gera o carimbo de data e hora do momento da execução. A função `sha2(col, 256)` gera a assinatura SHA-256 (com 256 bits) para garantir integridade e detectar alterações em registros combinados via `concat_ws`.",
            [
                "<strong>B, C e D:</strong> Sintaxes incorretas ou literais estáticos sem cálculo real de hash."
            ],
            "Padrão de auditoria de dados: `current_timestamp()` e `sha2(concat_ws(...), 256)`."
        )
    },
    {
        "id": "d2_q80",
        "domain": "domain2",
        "type": "single",
        "title": "Mapeamento de Tipos de Dados complexos com `MapType`",
        "question": "Um desenvolvedor precisa armazenar atributos flexíveis de produtos no formato chave-valor (`cor: azul`, `tamanho: G`, `voltagem: 220v`) em uma única coluna sem criar centenas de colunas esparsas na tabela. Qual tipo de dado do Spark SQL é o mais indicado?",
        "options": [
            {"id": "A", "text": "`MapType(StringType(), StringType())`", "isCorrect": True},
            {"id": "B", "text": "`IntegerType()`", "isCorrect": False},
            {"id": "C", "text": "`BooleanType()`", "isCorrect": False},
            {"id": "D", "text": "`BinaryType()` sem decodificação", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "`MapType(keyType, valueType)` permite armazenar coleções de pares chave-valor dentro de uma coluna única. As chaves podem ser consultadas nativamente com notação de colchetes (`coluna['cor']`), preservando flexibilidade de esquema.",
            [
                "<strong>B e C:</strong> Tipos primitivos escalares que não suportam dicionários de múltiplos atributos.",
                "<strong>D:</strong> Armazenar binário bruto impediria consultas colunares eficientes sem decodificação."
            ],
            "Pares Chave-Valor no Spark: `MapType(StringType(), StringType())`."
        )
    },
    {
        "id": "d2_q81",
        "domain": "domain2",
        "type": "single",
        "title": "Leitura de Dados Incrementais com Delta Change Data Feed (CDF)",
        "question": "Qual recurso nativo do Delta Lake permite aos consumidores lerem apenas as linhas que foram inseridas, atualizadas ou deletadas em uma tabela Delta, incluindo os valores 'antes' e 'depois' das atualizações (`_change_type`)?",
        "options": [
            {"id": "A", "text": "Delta Change Data Feed (CDF / `readChangeFeed`)", "isCorrect": True},
            {"id": "B", "text": "Comparação manual de backups de fita magnética a cada 10 minutos.", "isCorrect": False},
            {"id": "C", "text": "Exclusão diária de toda a base para forçar recarga integral.", "isCorrect": False},
            {"id": "D", "text": "Envio de cópias por fax para a equipe de controle.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Delta Change Data Feed (CDF) rastreia alterações em nível de linha na tabela Delta. Ao habilitar `delta.enableChangeDataFeed = true`, consumidores podem ler via `readChangeFeed` os registros de inserção (`insert`), exclusão (`delete`) e valores antes/depois de modificação (`update_preimage`, `update_postimage`).",
            [
                "<strong>B, C e D:</strong> Práticas ultrapassadas e não tecnológicas."
            ],
            "Delta Change Data Feed (CDF) expõe o histórico de alterações (Insert, Update, Delete) com metadados `_change_type`."
        )
    },
    {
        "id": "d2_q82",
        "domain": "domain2",
        "type": "single",
        "title": "Sincronização de Esquema com `ALTER TABLE ... SYNC METADATA`",
        "question": "Quando uma tabela Delta tem arquivos Parquet adicionados diretamente no OneLake por um processo externo ou via atalho (Shortcut), qual comando no SQL Analytics Endpoint garante que os metadados do catálogo estejam sincronizados com os arquivos físicos mais recentes?",
        "options": [
            {"id": "A", "text": "A sincronização é executada automaticamente pelo Fabric Metadata Sync em segundo plano, ou pode ser forçada executando uma consulta no SQL Endpoint.", "isCorrect": True},
            {"id": "B", "text": "É necessário reiniciar todos os roteadores de rede da Microsoft.", "isCorrect": False},
            {"id": "C", "text": "A tabela deve ser deletada e recriada do zero impreterivelmente.", "isCorrect": False},
            {"id": "D", "text": "O Fabric não reconhece arquivos adicionados externamente.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric possui um serviço de Metadata Sync que atualiza continuamente o catálogo relacional do SQL Analytics Endpoint sempre que novos commits são adicionados ao `_delta_log` no OneLake. A consulta ao SQL Endpoint atualiza a visão mais recente de forma consistente.",
            [
                "<strong>B, C e D:</strong> Afirmações incorretas."
            ],
            "Sincronização de Metadados: O Fabric sincroniza automaticamente os metadados do Delta Log para o SQL Analytics Endpoint."
        )
    }
]

def get_domain2_questions():
    return DOMAIN_2_QUESTIONS

if __name__ == "__main__":
    qs = get_domain2_questions()
    print(f"Domain 2: {len(qs)} questões carregadas.")


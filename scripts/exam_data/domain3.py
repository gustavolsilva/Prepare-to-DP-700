"""
DOMÍNIO 3: MONITORAR E OTIMIZAR UMA SOLUÇÃO ANALÍTICA (20-25%)
38 Questões Completas (Single-Choice e Multi-Select)
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

DOMAIN_3_QUESTIONS = [
    # --- CAPACITY METRICS APP & SMOOTHING (Questões 1 a 12) ---
    {
        "id": "d3_q01",
        "domain": "domain3",
        "type": "single",
        "title": "Diagnóstico de Picos com o Fabric Capacity Metrics App",
        "question": "Um administrador de capacidade nota lentidão generalizada no workspace corporativo e abre o Microsoft Fabric Capacity Metrics App. Qual visão gráfica no aplicativo permite identificar o momento exato em que o consumo de CUs ultrapassou 100% e detalhar as operações responsáveis?",
        "options": [
            {"id": "A", "text": "A exibição de ponto no tempo (Timepoint Drill-Through / Visualização de Timepoint de 30 segundos).", "isCorrect": True},
            {"id": "B", "text": "O monitor de processos do Gerenciador de Tarefas do Windows 11.", "isCorrect": False},
            {"id": "C", "text": "A listagem de e-mails recebidos na caixa de entrada do Outlook.", "isCorrect": False},
            {"id": "D", "text": "O gráfico de tráfego de rede Wi-Fi do roteador local.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "No Fabric Capacity Metrics App, ao clicar em qualquer ponto da curva de utilização na linha do tempo, a ferramenta abre o 'Timepoint drill-through' (análise de ponto no tempo com granularidade de 30 segundos). Essa visão discrimina as operações de Interactive e Background e exibe exatamente quais itens, usuários e operações consumiram CUs naquele instante.",
            [
                "<strong>B, C e D:</strong> Ferramentas locais ou não relacionadas à infraestrutura de capacidade do Fabric."
            ],
            "Fabric Capacity Metrics App: O 'Timepoint view' decompõe o consumo de CUs em 30 segundos por item e operação."
        )
    },
    {
        "id": "d3_q02",
        "domain": "domain3",
        "type": "single",
        "title": "Diferença entre Operações Interativas e de Segundo Plano nas Métricas",
        "question": "No Capacity Metrics App, as operações são categorizadas em 'Interactive' e 'Background'. Como essa categorização afeta o cálculo de uso de CUs e o mecanismo de Smoothing (suavização)?",
        "options": [
            {"id": "A", "text": "Operações interativas (como DAX e consultas visuais de relatórios) são distribuídas em uma janela móvel de 5 minutos, enquanto operações em segundo plano (como Spark jobs e Data Pipelines) são distribuídas em uma janela móvel de 24 horas.", "isCorrect": True},
            {"id": "B", "text": "Operações interativas são gratuitas e operações de segundo plano são faturadas em dobro.", "isCorrect": False},
            {"id": "C", "text": "Ambas as operações são avaliadas exatamente em 1 segundo sem qualquer suavização.", "isCorrect": False},
            {"id": "D", "text": "Operações de segundo plano são bloqueadas automaticamente às 18:00 horas.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O mecanismo de Smoothing é assimétrico por design: cargas interativas (geradas por usuários interagindo em relatórios) são suavizadas em janelas curtas de 5 minutos; cargas de segundo plano (ETL, pipelines pesados, batches de Spark) são amortizadas ao longo de 24 horas completas para absorver o impacto de bursts noturnos.",
            [
                "<strong>B, C e D:</strong> Conceitos incorretos de faturamento e suavização."
            ],
            "Regra crítica de métricas: Interactive = 5 minutos de Smoothing; Background = 24 horas de Smoothing."
        )
    },
    {
        "id": "d3_q03",
        "domain": "domain3",
        "type": "single",
        "title": "Métrica de Armazenamento no OneLake vs Capacidade Computacional",
        "question": "O Capacity Metrics App reporta um consumo elevado de 'OneLake Storage (GB)'. Como o armazenamento do OneLake é faturado no Microsoft Fabric em relação às Capacity Units (CUs)?",
        "options": [
            {"id": "A", "text": "O armazenamento é faturado como uma taxa separada por Gigabyte/Mês (baseada na taxa padrão de ADLS Gen2), não consumindo as CUs computacionais do F-SKU adquirido.", "isCorrect": True},
            {"id": "B", "text": "Cada 1 GB de armazenamento consome permanentemente 10 CUs da capacidade contratada.", "isCorrect": False},
            {"id": "C", "text": "O armazenamento é 100% gratuito e ilimitado para sempre sem nenhum custo.", "isCorrect": False},
            {"id": "D", "text": "O armazenamento só pode ser pago com Bitcoins.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "No Microsoft Fabric, Computação e Armazenamento são faturados separadamente. O F-SKU cobre as Capacity Units de processamento computacional. O armazenamento do OneLake (tabelas Delta e arquivos) é tarifado com base no volume de dados em GB por mês, à mesma tarifa atrativa do Azure Data Lake Storage Gen2.",
            [
                "<strong>B:</strong> Armazenamento não consome nem diminui as CUs de computação do F-SKU.",
                "<strong>C e D:</strong> Falsas noções financeiras."
            ],
            "No Fabric: F-SKU = Computação (CUs); OneLake = Armazenamento separado faturado por GB/mês (sem consumir CUs)."
        )
    },
    {
        "id": "d3_q04",
        "domain": "domain3",
        "type": "single",
        "title": "Estágio 1 de Throttling: Interactive Delay",
        "question": "Quando uma capacidade F16 atinge 100% de sobrecarga cumulativa na janela móvel, qual é o sintoma imediato experimentado pelos usuários corporativos que acessam relatórios do Power BI durante o Estágio 1 de Throttling (Interactive Delay)?",
        "options": [
            {"id": "A", "text": "As consultas visuais continuam funcionando, mas um atraso artificial progressivo (delay) de alguns segundos é adicionado à resposta de cada interação para desestimular o consumo excessivo.", "isCorrect": True},
            {"id": "B", "text": "Todos os computadores da empresa são desligados.", "isCorrect": False},
            {"id": "C", "text": "Os relatórios exibem mensagens de erro 500 imediatamente sem carregar nenhum dado.", "isCorrect": False},
            {"id": "D", "text": "Os dados de vendas são apagados do banco de dados.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Estágio 1 (Interactive Delay) é uma medida preventiva de throttling: o Fabric não rejeita as consultas interativas de imediato, mas injeta um atraso gradual nas respostas visuais. Se a sobrecarga persistir e alcançar o limite do estágio 2, aí sim ocorre a Rejeição Interativa (Interactive Rejection).",
            [
                "<strong>B e D:</strong> Consequências absurdas.",
                "<strong>C:</strong> Erros de rejeição só acontecem a partir do Estágio 2 (Interactive Rejection)."
            ],
            "Throttling Estágio 1: Introduz atraso (Delay) sem rejeitar requisições interativas."
        )
    },
    {
        "id": "d3_q05",
        "domain": "domain3",
        "type": "multi",
        "title": "Ações de Remediação para Sobrecarga Contínua de Capacidade",
        "question": "Quais DUAS ações administrativas são recomendadas para mitigar uma sobrecarga contínua de capacidade identificada no Capacity Metrics App? (Selecione 2 alternativas)",
        "options": [
            {"id": "A", "text": "Fazer um upgrade temporário ou permanente do F-SKU no portal do Azure (ex: de F32 para F64) para aumentar o número de CUs disponíveis.", "isCorrect": True},
            {"id": "B", "text": "Reescalonar ou escalonar a execução de Data Pipelines pesados e jobs Spark para horários de menor movimento em vez de concentrá-los todos simultaneamente à meia-noite.", "isCorrect": True},
            {"id": "C", "text": "Deletar todos os workspaces de produção imediatamente.", "isCorrect": False},
            {"id": "D", "text": "Desativar o firewall do Windows em todos os computadores da empresa.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A mitigação de sobrecarga envolve: 1) Dimensionamento vertical (scale-up de F-SKU no Azure) e 2) Otimização operacional das cargas de trabalho (orquestração distribuída no tempo, evitando que todos os pipelines e jobs Spark concorram no mesmo instante).",
            [
                "<strong>C e D:</strong> Práticas destrutivas que não resolvem o problema de arquitetura."
            ],
            "Remediação de Capacidade: Aumentar F-SKU ou redistribuir pipelines pesados ao longo das 24 horas."
        )
    },
    {
        "id": "d3_q06",
        "domain": "domain3",
        "type": "single",
        "title": "Identificação de 'Top Consumers' no Capacity Metrics App",
        "question": "Na guia de detalhes de itens do Capacity Metrics App, qual métrica quantifica exatamente o percentual de CUs consumido por um Lakehouse ou Warehouse específico em relação à capacidade total contratada?",
        "options": [
            {"id": "A", "text": "`CU %` (Percentual de CU consumido) e `Total CU (s)` (Total de segundos de CU acumulados).", "isCorrect": True},
            {"id": "B", "text": "Número de cliques de mouse no relatório.", "isCorrect": False},
            {"id": "C", "text": "Quantidade de caracteres no código SQL.", "isCorrect": False},
            {"id": "D", "text": "Tamanho da janela do monitor em pixels.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Capacity Metrics App resume o consumo computacional de cada artefato usando `Total CU (s)` (Capacity Unit Seconds) e o respectivo `CU %` da capacidade disponível, permitindo ranquear com precisão quais itens são os maiores consumidores ('Top Consumers') de recursos.",
            [
                "<strong>B, C e D:</strong> Métricas irrelevantes e inexistentes."
            ],
            "Top Consumers são ranqueados por `Total CU (s)` e `CU %` no Capacity Metrics App."
        )
    },
    {
        "id": "d3_q07",
        "domain": "domain3",
        "type": "single",
        "title": "Monitoramento de Operações de Autoscale (Capacidades Power BI Premium)",
        "question": "Em locatários com capacidade que possuem o recurso de Autoscale ativado, como o sistema reage quando ocorre um pico que ultrapassa a capacidade base por um período contínuo?",
        "options": [
            {"id": "A", "text": "Acrescenta automaticamente 1 vCore adicional por períodos de 24 horas para evitar throttling, cobrando o valor correspondente no Azure.", "isCorrect": True},
            {"id": "B", "text": "Rejeita imediatamente todas as operações de gravação.", "isCorrect": False},
            {"id": "C", "text": "Desliga os servidores durante o fim de semana.", "isCorrect": False},
            {"id": "D", "text": "Envia uma carta impressa pelo correio.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O recurso de Autoscale em capacidades corporativas do Power BI / Fabric aloca automaticamente vCores sob demanda para absorver picos extremos que não puderam ser amortizados pelo smoothing, garantindo que usuários finais não sofram rejeição de consultas.",
            [
                "<strong>B, C e D:</strong> Incorretos."
            ],
            "Autoscale: Adiciona nós/núcleos sob demanda para evitar rejeição e throttling durante picos extremos."
        )
    },
    {
        "id": "d3_q08",
        "domain": "domain3",
        "type": "single",
        "title": "Integração do Fabric com Azure Monitor e Log Analytics",
        "question": "Uma organização deseja centralizar os logs de execução de Notebooks, Pipelines e consultas SQL do Fabric em um workspace do Azure Log Analytics para retenção histórica de 2 anos e criação de alertas no KQL. Como essa integração é habilitada?",
        "options": [
            {"id": "A", "text": "Configurando as opções de 'Azure Log Analytics' nas configurações do Workspace do Fabric e conectando ao Log Analytics Workspace de destino no Azure.", "isCorrect": True},
            {"id": "B", "text": "Copiando e colando os logs em arquivos `.log` no Notepad diariamente.", "isCorrect": False},
            {"id": "C", "text": "Instalando um agente do Windows 98 em cada nó do Fabric.", "isCorrect": False},
            {"id": "D", "text": "O Fabric não se integra com o Azure Monitor.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric suporta integração nativa de auditoria com o Azure Monitor / Log Analytics. Nas configurações do Workspace (Workspace Settings -> Azure Integration -> Log Analytics), o administrador vincula o workspace a uma instância do Azure Log Analytics para exportação contínua de telemetria.",
            [
                "<strong>B, C e D:</strong> Falsas noções técnicas."
            ],
            "Exportação contínua de telemetria corporativa: Conectar Workspace Settings ao Azure Log Analytics."
        )
    },
    {
        "id": "d3_q09",
        "domain": "domain3",
        "type": "single",
        "title": "Diferença entre Capacity Units (CUs) e vCores no Fabric",
        "question": "Qual é a relação matemática e técnica oficial entre 1 Capacity Unit (CU) e vCores computacionais nas capacidades F-SKU do Microsoft Fabric?",
        "options": [
            {"id": "A", "text": "2 CUs equivalem aproximadamente ao poder computacional de 1 vCore de computação do Azure (ex: F64 fornece 64 CUs, equivalentes a 32 vCores).", "isCorrect": True},
            {"id": "B", "text": "1 CU equivale a 1.000 vCores.", "isCorrect": False},
            {"id": "C", "text": "1 CU é igual a 1 Terabyte de memória RAM.", "isCorrect": False},
            {"id": "D", "text": "CUs e vCores são grandezas sem nenhuma relação.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Na documentação oficial do Microsoft Fabric: 2 CUs correspondem ao poder de processamento equivalente a 1 vCore tradicional de nuvem. Logo, um SKU F64 fornece 64 CUs, o equivalente computacional a 32 vCores (exatamente a mesma potência de um nó P1 do Power BI Premium).",
            [
                "<strong>B, C e D:</strong> Proporções e definições errôneas."
            ],
            "Equivalência oficial do Fabric: 2 CUs = 1 vCore (ex: F64 = 32 vCores)."
        )
    },
    {
        "id": "d3_q10",
        "domain": "domain3",
        "type": "single",
        "title": "Identificação de Usuários Ofensores no Capacity Metrics App",
        "question": "No drill-through de uma operação de sobrecarga no Capacity Metrics App, qual campo indica qual usuário ou conta de serviço (Service Principal) disparou a consulta causadora do pico?",
        "options": [
            {"id": "A", "text": "`User` (UPN do usuário ou ID da Identidade de Serviço / Service Principal)", "isCorrect": True},
            {"id": "B", "text": "`HardwareMACAddress` do monitor do computador", "isCorrect": False},
            {"id": "C", "text": "`MotherboardSerialNumber` do servidor", "isCorrect": False},
            {"id": "D", "text": "O nome do fabricante do mouse", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O campo `User` na tabela de detalhamento do Timepoint exibe o User Principal Name (UPN) do usuário corporativo ou o Application ID do Service Principal responsável pela submissão do job ou consulta geradora de consumo.",
            [
                "<strong>B, C e D:</strong> Metadados inexistentes e absurdos."
            ],
            "Rastreamento de usuários: O campo `User` identifica quem disparou a operação causadora de consumo no Fabric."
        )
    },
    {
        "id": "d3_q11",
        "domain": "domain3",
        "type": "single",
        "title": "Métrica de Rejeição em Segundo Plano (Background Rejection)",
        "question": "Qual é a consequência técnica quando o Capacity Metrics App indica que a capacidade atingiu o Estágio 3 de Throttling (Background Rejection)?",
        "options": [
            {"id": "A", "text": "Qualquer novo job em segundo plano (como execuções de Data Pipelines, agendamento de Dataflows e jobs Spark) falha imediatamente no início com erro de rejeição por capacidade esgotada.", "isCorrect": True},
            {"id": "B", "text": "A Microsoft apaga todos os workspaces da assinatura.", "isCorrect": False},
            {"id": "C", "text": "Os pipelines continuam funcionando sem interrupção.", "isCorrect": False},
            {"id": "D", "text": "O portal do Fabric muda de cor para verde.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Estágio 3 é o nível mais severo de proteção: para impedir que a sobrecarga comprometa a estabilidade do datacenter e a fila acumulada, todas as novas tarefas e pipelines em segundo plano são rejeitadas sumariamente até que o consumo caia abaixo de 100%.",
            [
                "<strong>B, C e D:</strong> Falsas declarações."
            ],
            "Estágio 3 de Throttling (Background Rejection): Falha imediata de novos pipelines, dataflows e jobs Spark."
        )
    },
    {
        "id": "d3_q12",
        "domain": "domain3",
        "type": "single",
        "title": "Notificações por E-mail de Sobrecarga de Capacidade",
        "question": "Como os administradores de capacidade podem receber alertas automáticos por e-mail antes que a capacidade atinja os estágios severos de throttling?",
        "options": [
            {"id": "A", "text": "Configurando alertas de capacidade no portal de administração do Fabric (Admin Portal) definindo limiares percentuais de utilização (ex: 80%, 90% de uso).", "isCorrect": True},
            {"id": "B", "text": "Instalando um plugin de terceiros não homologado no navegador.", "isCorrect": False},
            {"id": "C", "text": "Pedindo para os usuários ligarem por telefone sempre que sentirem lentidão.", "isCorrect": False},
            {"id": "D", "text": "Não é possível configurar alertas de capacidade no Fabric.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O portal de administração do Fabric permite aos administradores definir políticas de notificação por e-mail quando a utilização da capacidade atinge limiares predeterminados de advertência, possibilitando ações preventivas antes do throttling.",
            [
                "<strong>B, C e D:</strong> Falsas noções de gestão de capacidade."
            ],
            "Alertas de Capacidade: Configurados no Admin Portal com notificações proativas baseadas em limiares de uso."
        )
    },

    # --- QUERY INSIGHTS & DMVs NO WAREHOUSE / SQL ENDPOINT (Questões 13 a 24) ---
    {
        "id": "d3_q13",
        "domain": "domain3",
        "type": "single",
        "title": "Schema `queryinsights` no Fabric Warehouse",
        "question": "No Fabric Warehouse e no SQL Analytics Endpoint, qual esquema especial de sistema fornece exibições pré-construídas para analisar o histórico de consultas, durações e consumo de recursos?",
        "options": [
            {"id": "A", "text": "`sys` apenas", "isCorrect": False},
            {"id": "B", "text": "`queryinsights`", "isCorrect": True},
            {"id": "C", "text": "`information_schema` apenas", "isCorrect": False},
            {"id": "D", "text": "`dbo.perf_logs`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric Warehouse disponibiliza o schema nativo `queryinsights`, contendo exibições otimizadas prontas para uso: `queryinsights.exec_requests_history`, `queryinsights.frequently_run_queries` e `queryinsights.long_running_queries`.",
            [
                "<strong>A e C:</strong> Esquemas padrão ANSI/SQL tradicionais que não trazem as métricas agregadas específicas do Fabric.",
                "<strong>D:</strong> Nome fictício."
            ],
            "Diagnóstico de Consultas no Fabric: Schema oficial `queryinsights`."
        )
    },
    {
        "id": "d3_q14",
        "domain": "domain3",
        "type": "single",
        "title": "Identificação de Consultas Lentas com `queryinsights.long_running_queries`",
        "question": "Um engenheiro de dados precisa identificar as 10 consultas T-SQL que tiveram a maior duração média de execução nos últimos 7 dias no Fabric Warehouse. Qual consulta T-SQL fornece essa informação diretamente?",
        "options": [
            {"id": "A", "text": "`SELECT TOP 10 * FROM queryinsights.long_running_queries ORDER BY median_total_elapsed_time_ms DESC;`", "isCorrect": True},
            {"id": "B", "text": "`SELECT * FROM sys.tables WHERE is_slow = 1;`", "isCorrect": False},
            {"id": "C", "text": "`KILL ALL SLOW QUERIES;`", "isCorrect": False},
            {"id": "D", "text": "`DBCC CHECKALLOC;`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A view `queryinsights.long_running_queries` agrega consultas T-SQL históricas calculando métricas como mediana e máximo de tempo decorrido em milissegundos (`median_total_elapsed_time_ms`), sendo a ferramenta ideal para localizar queries ofensivas.",
            [
                "<strong>B, C e D:</strong> Sintaxes inexistentes ou comandos que não analisam histórico de execução."
            ],
            "Consultas lentas no Warehouse: `queryinsights.long_running_queries`."
        )
    },
    {
        "id": "d3_q15",
        "domain": "domain3",
        "type": "single",
        "title": "Diagnóstico de Texto de Consulta e Sessão com `exec_requests_history`",
        "question": "Para auditar o texto exato do comando SQL executado, o ID da sessão e a contagem de linhas retornadas de consultas executadas nas últimas 24 horas no Warehouse, qual exibição do schema `queryinsights` deve ser consultada?",
        "options": [
            {"id": "A", "text": "`queryinsights.exec_requests_history`", "isCorrect": True},
            {"id": "B", "text": "`queryinsights.user_passwords`", "isCorrect": False},
            {"id": "C", "text": "`dbo.QueryLogFile`", "isCorrect": False},
            {"id": "D", "text": "`sys.dm_os_memory_nodes`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "`queryinsights.exec_requests_history` registra cada comando T-SQL executado no Fabric Warehouse/SQL Endpoint, contendo colunas essenciais como `command`, `session_id`, `status`, `row_count`, `start_time` e `total_elapsed_time_ms`.",
            [
                "<strong>B, C e D:</strong> Inexistentes ou não aplicáveis para auditoria de requisições no Fabric."
            ],
            "Histórico individual de comandos: `queryinsights.exec_requests_history`."
        )
    },
    {
        "id": "d3_q16",
        "domain": "domain3",
        "type": "single",
        "title": "Consultas Frequentes com `queryinsights.frequently_run_queries`",
        "question": "Como um arquiteto pode verificar quais consultas são executadas centenas de vezes ao dia pelo Power BI, visando criar tabelas agregadas ou aceleradores para economizar computação?",
        "options": [
            {"id": "A", "text": "Consultando a view `queryinsights.frequently_run_queries` e ordenando pela coluna `execution_count` descendente.", "isCorrect": True},
            {"id": "B", "text": "Perguntando para cada funcionário quantas vezes ele clicou no relatório.", "isCorrect": False},
            {"id": "C", "text": "Desconectando o Power BI do Warehouse.", "isCorrect": False},
            {"id": "D", "text": "Lendo os arquivos de log do IIS do servidor web local.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "`queryinsights.frequently_run_queries` consolida padrões de consulta idênticos e expõe o `execution_count`. Consultas com alta frequência de execução e alto tempo cumulativo são as candidatas ideais para materialização prévia na camada Gold.",
            [
                "<strong>B, C e D:</strong> Abordagens inviáveis ou sem sentido técnico."
            ],
            "Consultas repetitivas: `queryinsights.frequently_run_queries` ordenado por `execution_count`."
        )
    },
    {
        "id": "d3_q17",
        "domain": "domain3",
        "type": "single",
        "title": "DMV `sys.dm_exec_sessions` para Sessões Ativas",
        "question": "Um DBA precisa inspecionar em tempo real quais conexões e usuários estão conectados no momento presente ao Fabric Warehouse. Qual Dynamic Management View (DMV) de sistema padrão fornece essa informação?",
        "options": [
            {"id": "A", "text": "`sys.dm_exec_sessions`", "isCorrect": True},
            {"id": "B", "text": "`sys.dm_hardware_inventory`", "isCorrect": False},
            {"id": "C", "text": "`sys.all_active_users_worldwide`", "isCorrect": False},
            {"id": "D", "text": "`sp_who_is_active_on_internet`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "`sys.dm_exec_sessions` é uma DMV nativa suportada pelo Fabric Warehouse que retorna informações sobre todas as sessões autenticadas ativas, incluindo `session_id`, `login_name`, `client_interface_name` e horários de conexão.",
            [
                "<strong>B, C e D:</strong> DMVs inexistentes."
            ],
            "Sessões ativas no Warehouse: `SELECT * FROM sys.dm_exec_sessions`."
        )
    },
    {
        "id": "d3_q18",
        "domain": "domain3",
        "type": "single",
        "title": "Cancelamento de Consultas em Execução com `KILL`",
        "question": "Uma consulta mal formulada por um analista está executando há 3 horas sem parar, consumindo recursos excessivos do Fabric Warehouse. Qual comando T-SQL deve ser executado pelo administrador para cancelar essa sessão específica?",
        "options": [
            {"id": "A", "text": "`KILL '<session_id>';`", "isCorrect": True},
            {"id": "B", "text": "`DROP USER '<login>';`", "isCorrect": False},
            {"id": "C", "text": "`STOP SERVER IMMEDIATE;`", "isCorrect": False},
            {"id": "D", "text": "`DELETE FROM sys.dm_exec_requests;`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O comando padrão `KILL <session_id>` é suportado no Fabric Warehouse para abortar a execução de uma sessão específica e forçar o cancelamento imediato de sua consulta ativa, liberando os recursos associados.",
            [
                "<strong>B:</strong> Excluir o usuário não encerra a transação já em andamento e causa problemas de segurança.",
                "<strong>C e D:</strong> Sintaxes incorretas; DMVs são somente leitura e não aceitam comando DELETE."
            ],
            "Abortar sessão travada no Warehouse: Comando T-SQL `KILL <session_id>`."
        )
    },
    {
        "id": "d3_q19",
        "domain": "domain3",
        "type": "multi",
        "title": "Colunas Críticas da View `queryinsights.exec_requests_history`",
        "question": "Quais DUAS colunas presentes na view `queryinsights.exec_requests_history` são fundamentais para diagnosticar se uma consulta falhou e qual erro foi gerado? (Selecione 2 alternativas)",
        "options": [
            {"id": "A", "text": "`status` (indicando se a consulta está Completed, Failed ou Canceled)", "isCorrect": True},
            {"id": "B", "text": "`error_message` (detalhando a mensagem descritiva do erro que causou a falha)", "isCorrect": True},
            {"id": "C", "text": "`user_home_address`", "isCorrect": False},
            {"id": "D", "text": "`credit_card_balance`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A view `queryinsights.exec_requests_history` traz as colunas `status` (que assume valores como 'Completed', 'Failed', 'Canceled') e `error_message`, permitindo diagnosticar a causa exata de consultas com erro sem depender de reprodução manual.",
            [
                "<strong>C e D:</strong> Colunas fictícias."
            ],
            "Diagnóstico de erros no SQL Endpoint/Warehouse: `status` e `error_message` na `exec_requests_history`."
        )
    },
    {
        "id": "d3_q20",
        "domain": "domain3",
        "type": "single",
        "title": "Monitoramento de Bloqueios e Esperas (Wait Statistics)",
        "question": "Ao analisar a lentidão de uma consulta no Fabric Warehouse, qual informação do plano de execução distribuído auxilia a identificar se a consulta ficou presa aguardando dados da rede do OneLake?",
        "options": [
            {"id": "A", "text": "Métricas de tempos de espera de I/O de armazenamento remoto (Remote Storage I/O Waits) no plano de consulta do motor distribuído.", "isCorrect": True},
            {"id": "B", "text": "A velocidade de rotação do disco mecânico do servidor.", "isCorrect": False},
            {"id": "C", "text": "A marca da placa-mãe do Azure.", "isCorrect": False},
            {"id": "D", "text": "A temperatura do processador da estação do usuário.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "No motor distribuído do Fabric Warehouse, a leitura e gravação acontecem no OneLake sobre rede. Tempos anormais de I/O remoto nos planos de execução indicam gargalos de rede ou arquivos excessivamente pequenos exigindo alto número de requisições HTTPS GET para o armazenamento.",
            [
                "<strong>B, C e D:</strong> Detalhes físicos irrelevantes na computação em nuvem gerenciada."
            ],
            "Performance de I/O no Warehouse: Monitorar tempos de I/O de armazenamento remoto no plano distribuído."
        )
    },
    {
        "id": "d3_q21",
        "domain": "domain3",
        "type": "single",
        "title": "View `queryinsights.frequently_run_queries` e Agregações de Desempenho",
        "question": "Qual métrica na view `queryinsights.frequently_run_queries` reflete a variação (inconsistência) no tempo de resposta de uma consulta ao longo de múltiplas execuções?",
        "options": [
            {"id": "A", "text": "A discrepância entre `min_total_elapsed_time_ms` e `max_total_elapsed_time_ms` (indicando oscilação de concorrência ou flutuação de cache).", "isCorrect": True},
            {"id": "B", "text": "A taxa de compressão do arquivo ZIP gerado.", "isCorrect": False},
            {"id": "C", "text": "O número de cores usadas no gráfico do Power BI.", "isCorrect": False},
            {"id": "D", "text": "A data de expiração da assinatura do Office 365.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A grande diferença entre `min_total_elapsed_time_ms` e `max_total_elapsed_time_ms` para uma mesma consulta frequente indica instabilidade de performance gerada por bloqueios concorrentes, contenção de recursos ou diferenças entre leitura em cold cache vs warm cache.",
            [
                "<strong>B, C e D:</strong> Falsos fatores sem impacto no tempo de consulta T-SQL."
            ],
            "Oscilação de performance: Analisar dispersão entre `min` e `max_total_elapsed_time_ms`."
        )
    },
    {
        "id": "d3_q22",
        "domain": "domain3",
        "type": "single",
        "title": "Tamanho de Resultados e `row_count` no Histórico",
        "question": "Um relatório do Power BI em DirectQuery está sobrecarregando a capacidade. Ao analisar `queryinsights.exec_requests_history`, você nota consultas que retornam `row_count` superior a 5 milhões de linhas para a interface visual. Qual é o problema arquitetural evidente?",
        "options": [
            {"id": "A", "text": "O relatório está solicitando dados analíticos em nível transacional sem aplicar filtros nem agregações adequadas, transferindo milhões de linhas desnecessárias para o cliente em vez de resumir no banco.", "isCorrect": True},
            {"id": "B", "text": "O Fabric Warehouse não suporta consultas com mais de 100 linhas.", "isCorrect": False},
            {"id": "C", "text": "O monitor do usuário não tem resolução suficiente.", "isCorrect": False},
            {"id": "D", "text": "A tabela Delta do OneLake está corrompida.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Relatórios de BI devem solicitar dados sumarizados. Quando uma consulta visual transfere milhões de linhas sem agregação (`row_count` extremo), consome quantidades massivas de memória de rede e CUs desnecessariamente. A solução é filtrar e agregar no modelo semântico.",
            [
                "<strong>B, C e D:</strong> Falsas declarações; o Warehouse suporta bilhões de linhas, mas a má prática está no consumo indevido de relatórios visuais."
            ],
            "Boas práticas de BI: Consultas de relatórios devem retornar dados agregados, evitando transferir milhões de linhas brutas para os visuais."
        )
    },
    {
        "id": "d3_q23",
        "domain": "domain3",
        "type": "single",
        "title": "Retenção Padrão dos Dados no Schema `queryinsights`",
        "question": "Por quantos dias o Microsoft Fabric Warehouse retém o histórico de consultas no schema `queryinsights` por padrão?",
        "options": [
            {"id": "A", "text": "30 dias", "isCorrect": True},
            {"id": "B", "text": "1 hora apenas", "isCorrect": False},
            {"id": "C", "text": "10 anos", "isCorrect": False},
            {"id": "D", "text": "Os dados são apagados imediatamente após o término da consulta.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric Warehouse retém automaticamente as métricas de histórico de consultas no schema `queryinsights` por uma janela contínua de 30 dias. Para retenção superior a 30 dias, recomenda-se exportar os dados para o Azure Log Analytics.",
            [
                "<strong>B, C e D:</strong> Valores incorretos de retenção padrão."
            ],
            "Retenção nativa do `queryinsights`: 30 dias de histórico contínuo."
        )
    },
    {
        "id": "d3_q24",
        "domain": "domain3",
        "type": "single",
        "title": "Identificação de Consultas Canceladas por Usuários",
        "question": "Como identificar no Fabric se usuários estão cancelando consultas manualmente no navegador devido à impaciência com lentidão?",
        "options": [
            {"id": "A", "text": "Filtrando `queryinsights.exec_requests_history` com `WHERE status = 'Canceled'` e analisando o tempo decorrido antes do cancelamento.", "isCorrect": True},
            {"id": "B", "text": "Verificando se o usuário clicou no botão 'X' do Windows.", "isCorrect": False},
            {"id": "C", "text": "Lendo as gravações de áudio do microfone do analista.", "isCorrect": False},
            {"id": "D", "text": "Não há registro de cancelamento no Fabric.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Quando uma aplicação cliente encerra a conexão antes do término da consulta ou o usuário clica em cancelar, o Fabric registra o registro com `status = 'Canceled'` em `queryinsights.exec_requests_history`, permitindo diagnosticar abandono de consultas.",
            [
                "<strong>B, C e D:</strong> Falsas alegações."
            ],
            "Rastreamento de cancelamento: `status = 'Canceled'` na view `exec_requests_history`."
        )
    },

    # --- SPARK PERFORMANCE & SPARK UI (Questões 25 a 32) ---
    {
        "id": "d3_q25",
        "domain": "domain3",
        "type": "single",
        "title": "Identificação de Spill to Disk no Spark UI",
        "question": "Ao analisar um estágio lento de um job Spark no Fabric Spark UI, o engenheiro observa valores significativos nas métricas `Spill (Memory)` e `Spill (Disk)`. O que essas métricas indicam e como resolver?",
        "options": [
            {"id": "A", "text": "Indicam que a memória alocada para as tarefas do executor foi insuficiente para manter os dados intermediários de shuffle/agregação, forçando o Spark a gravar dados temporários no disco SSD local (gerando alta lentidão de I/O). A solução é aumentar a memória dos nós ou otimizar o particionamento.", "isCorrect": True},
            {"id": "B", "text": "Indicam que o disco rígido do cluster está fisicamente quebrado.", "isCorrect": False},
            {"id": "C", "text": "Indicam que os arquivos de dados foram excluídos pelo antivírus.", "isCorrect": False},
            {"id": "D", "text": "Spill to Disk é uma otimização desejável e acelera as consultas.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O fenômeno de 'Spill' ocorre quando os buffers de execução da JVM excedem a RAM disponível durante operações de Shuffle, Sort ou Join. O Spark descarrega blocos para o disco local (`Spill to Disk`), gerando severa penalidade de I/O. Soluções: aumentar a memória do nó executor, diminuir o tamanho das partições aumentando a contagem de partições, ou eliminar skewed keys.",
            [
                "<strong>B e C:</strong> Falsas causas físicas.",
                "<strong>D:</strong> O Spill degrada severamente o desempenho e deve ser eliminado sempre que possível."
            ],
            "Spark Spill to Disk: Falta de RAM forçando gravação em disco durante Shuffle/Sort. Resolva particionando melhor ou aumentando os nós."
        )
    },
    {
        "id": "d3_q26",
        "domain": "domain3",
        "type": "single",
        "title": "Diagnóstico de Garbage Collection (GC) no Spark UI",
        "question": "No Spark UI, uma tarefa levou 10 minutos para concluir, e a métrica 'Task Deserialization / GC Time' reportou 7 minutos de tempo de Garbage Collection. Qual é a causa raiz desse comportamento?",
        "options": [
            {"id": "A", "text": "A criação excessiva de milhões de objetos Python/Java de curta duração na memória heap da JVM, provocando pausas contínuas do Garbage Collector para limpeza de memória.", "isCorrect": True},
            {"id": "B", "text": "O cluster Spark estava sem conexão à internet.", "isCorrect": False},
            {"id": "C", "text": "O arquivo Parquet estava criptografado com senha errada.", "isCorrect": False},
            {"id": "D", "text": "O código Spark estava compilado em linguagem COBOL.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Tempos de Garbage Collection (GC) que ultrapassam 10% do tempo total da tarefa sinalizam pressão extrema na memória heap da JVM, gerada por criação excessiva de objetos em loops Python RDD (em vez de usar DataFrames Spark vetorizados nativos) ou partições grandes demais.",
            [
                "<strong>B, C e D:</strong> Falsas noções sem base no funcionamento da JVM Spark."
            ],
            "GC Time elevado no Spark (> 10%): Pressão excessiva no heap da JVM. Use Spark DataFrames vetorizados em vez de loops RDD Python."
        )
    },
    {
        "id": "d3_q27",
        "domain": "domain3",
        "type": "single",
        "title": "Identificação Visual de Data Skew no Spark UI",
        "question": "Como um engenheiro de dados identifica graficamente uma assimetria severa de partição (Data Skew) ao inspecionar a aba 'Stages' do Apache Spark UI?",
        "options": [
            {"id": "A", "text": "Na tabela de distribuição de tarefas (Event Timeline / Summary Metrics), 99 tarefas terminam em 5 segundos (percentil 75% muito baixo), enquanto 1 única tarefa leva 45 minutos (Max Duration desproporcional com Shuffle Read Size gigantesco).", "isCorrect": True},
            {"id": "B", "text": "Todas as barras do gráfico ficam vermelhas e o navegador trava.", "isCorrect": False},
            {"id": "C", "text": "O Spark UI exibe uma janela pop-up solicitando reinicialização do modem.", "isCorrect": False},
            {"id": "D", "text": "Todas as tarefas levam exatamente o mesmo número de milissegundos.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O sintoma clássico de Data Skew no Spark UI é o contraste extremo entre as tarefas de um mesmo estágio: enquanto a grande maioria das tarefas termina em poucos segundos, uma ou poucas tarefas no percentil máximo (`Max`) continuam executando sozinhas por dezenas de minutos com volume desproporcional de bytes lidos no Shuffle.",
            [
                "<strong>B e C:</strong> Falsas descrições visuais.",
                "<strong>D:</strong> Se todas as tarefas levassem o mesmo tempo, os dados estariam perfeitamente balanceados (sem skew)."
            ],
            "Identificação de Skew no Spark UI: Discrepância gritante entre a duração das tarefas no percentil 75% vs percentil Max."
        )
    },
    {
        "id": "d3_q28",
        "domain": "domain3",
        "type": "single",
        "title": "Otimização de Pequenos Arquivos no Spark Ingest",
        "question": "Um pipeline de streaming no Spark grava novos micro-lotes a cada 10 segundos no OneLake. Após 3 dias de operação contínua, as consultas analíticas sobre essa tabela ficaram 50 vezes mais lentas. Qual é o motivo dessa degradação e como saná-lo?",
        "options": [
            {"id": "A", "text": "Problema dos Pequenos Arquivos (Small File Problem): foram gerados mais de 25.000 micro-arquivos Parquet de poucos kilobytes, sobrecarregando as listagens no OneLake. Solução: Executar periodicamente o comando `OPTIMIZE <tabela>` para consolidar os arquivos em blocos de tamanho ideal (~1 GB).", "isCorrect": True},
            {"id": "B", "text": "A capacidade F-SKU expirou e precisa ser recarregada com moedas virtuais.", "isCorrect": False},
            {"id": "C", "text": "O formato Parquet não é compatível com streaming contínuo.", "isCorrect": False},
            {"id": "D", "text": "O OneLake só consegue armazenar até 100 arquivos no total.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A ingestão contínua em streaming gera milhares de pequenos arquivos Parquet fragmentados ('small files'). O overhead de metadados e requisições HTTP GET para abrir cada arquivo destrói o desempenho das consultas. A compactação via `OPTIMIZE` reagrupa os arquivos em tamanhos eficientes (~1 GB).",
            [
                "<strong>B, C e D:</strong> Incorretos; Parquet e OneLake suportam petabytes, mas a fragmentação em micro-arquivos causa sobrecarga de metadados."
            ],
            "Small File Problem: Ingestão de streaming fragmentada; resolva executando periodicamente `OPTIMIZE` para compactação binária."
        )
    },
    {
        "id": "d3_q29",
        "domain": "domain3",
        "type": "single",
        "title": "Benefício do Data Skipping em Tabelas Delta",
        "question": "Como o mecanismo de Data Skipping do Delta Lake acelera consultas analíticas filtradas por colunas que possuem estatísticas calculadas?",
        "options": [
            {"id": "A", "text": "Lê os valores mínimos e máximos (`minValues`, `maxValues`) de cada coluna armazenados no cabeçalho do `_delta_log` e ignora completamente a leitura de arquivos Parquet cujos intervalos não contêm os valores solicitados na cláusula WHERE.", "isCorrect": True},
            {"id": "B", "text": "Pula a validação de segurança de usuários não autenticados.", "isCorrect": False},
            {"id": "C", "text": "Exclui as linhas que não forem lidas durante a consulta.", "isCorrect": False},
            {"id": "D", "text": "Desativa a verificação de tipos de dados numéricos.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Delta Lake coleta automaticamente estatísticas das primeiras 32 colunas de cada arquivo (contagem de linhas, nulos, min e max). Ao executar uma consulta com predicado `WHERE Ano = 2024`, o motor consulta o log de metadados e 'pula' (skips) os arquivos onde `maxValues.Ano < 2024` ou `minValues.Ano > 2024`, lendo apenas os arquivos relevantes.",
            [
                "<strong>B, C e D:</strong> Falsas noções sobre data skipping."
            ],
            "Data Skipping no Delta Lake: Usa estatísticas Min/Max no log para ignorar leitura de arquivos Parquet desnecessários."
        )
    },
    {
        "id": "d3_q30",
        "domain": "domain3",
        "type": "single",
        "title": "Limite Padrão de Colunas Indexadas para Estatísticas Delta",
        "question": "Por padrão, para quantas colunas de uma tabela Delta o Apache Spark coleta estatísticas automáticas de Min/Max para Data Skipping?",
        "options": [
            {"id": "A", "text": "Apenas para a primeira coluna.", "isCorrect": False},
            {"id": "B", "text": "Para as primeiras 32 colunas (`spark.databricks.delta.properties.defaults.dataSkippingNumIndexedCols = 32`).", "isCorrect": True},
            {"id": "C", "text": "Para todas as 1.000 colunas da tabela obrigatoriamente.", "isCorrect": False},
            {"id": "D", "text": "O Spark não coleta estatísticas automáticas.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A propriedade `delta.dataSkippingNumIndexedCols` tem o valor padrão de 32 colunas. Se uma coluna usada frequentemente em filtros de consulta estiver na posição 35 de uma tabela larga (wide table), ela não terá estatísticas Min/Max coletadas a menos que essa propriedade seja aumentada ou as colunas sejam reordenadas.",
            [
                "<strong>A, C e D:</strong> Valores e afirmações incorretas."
            ],
            "Data Skipping padrão: Primeiras 32 colunas indexadas por padrão (`dataSkippingNumIndexedCols`)."
        )
    },
    {
        "id": "d3_q31",
        "domain": "domain3",
        "type": "single",
        "title": "Efeito do Z-Order em Múltiplas Colunas",
        "question": "Quando um engenheiro executa o comando `OPTIMIZE Vendas ZORDER BY (ClienteId, DataVenda)`, qual é o efeito nos dados físicos armazenados?",
        "options": [
            {"id": "A", "text": "Os dados são mapeados usando curvas de preenchimento de espaço multidimensionais (Curva de Peano/Hilbert), garantindo que dados correlacionados por Cliente e Data sejam agrupados fisicamente nos mesmos arquivos Parquet para maximizar o Data Skipping em ambas as colunas.", "isCorrect": True},
            {"id": "B", "text": "A tabela é ordenada alfabeticamente apenas pela primeira coluna e a segunda coluna é apagada.", "isCorrect": False},
            {"id": "C", "text": "Os dados são compactados em formato `.ZIP` com senha.", "isCorrect": False},
            {"id": "D", "text": "A tabela só pode ser consultada por usuários com permissão de Administrador.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A técnica Z-Order (Curva de Z / Espaço-Filling Curve) distribui a ordenação de forma equilibrada entre até 2 a 4 colunas de alta cardinalidade sem dar prioridade linear à primeira coluna (ao contrário da ordenação hierárquica tradicional), permitindo Data Skipping de alta eficiência em consultas filtradas por qualquer combinação dessas colunas.",
            [
                "<strong>B, C e D:</strong> Afirmações incorretas sem fundamento técnico."
            ],
            "Z-Order: Curva de preenchimento espacial para agrupamento físico multidimensional e máximo Data Skipping."
        )
    },
    {
        "id": "d3_q32",
        "domain": "domain3",
        "type": "single",
        "title": "Manutenção Automática do Fabric (Automatic Compaction)",
        "question": "Qual recurso em segundo plano do Microsoft Fabric realiza compactação de arquivos menores em tabelas Delta de forma automatizada sem a necessidade de agendar comandos manuais de `OPTIMIZE` em todos os workspaces?",
        "options": [
            {"id": "A", "text": "Auto Compaction (Compactação Automática) durante as gravações e manutenção otimizada de tabelas gerenciada pelo ecossistema Fabric.", "isCorrect": True},
            {"id": "B", "text": "O desfragmentador de disco do Windows 95.", "isCorrect": False},
            {"id": "C", "text": "Um script em shell executado por um operador físico.", "isCorrect": False},
            {"id": "D", "text": "O Fabric não possui nenhum mecanismo automático de compactação.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric inclui recursos nativos de Auto-Compaction e Optimize Write habilitados por padrão no motor Spark e pipelines, consolidando arquivos pequenos durante o processo de escrita e reduzindo a necessidade de intervenções manuais de manutenção.",
            [
                "<strong>B, C e D:</strong> Falsas noções técnicas."
            ],
            "Auto Compaction no Fabric: Consolida automaticamente pequenos arquivos Parquet durante a escrita de dados."
        )
    },

    # --- POWER BI DIRECT LAKE DIAGNOSTICS & SYNC (Questões 33 a 38) ---
    {
        "id": "d3_q33",
        "domain": "domain3",
        "type": "single",
        "title": "Diagnóstico de Fallback no Performance Analyzer e DAX Studio",
        "question": "Um desenvolvedor de BI está usando o DAX Studio e a janela do Performance Analyzer para diagnosticar o desempenho de um visual do Power BI conectado a um modelo semântico em modo Direct Lake. Qual indício nos eventos de Server Timings confirma que a consulta permaneceu em Direct Lake puro sem sofrer Fallback para DirectQuery?",
        "options": [
            {"id": "A", "text": "O evento de consulta do Storage Engine é registrado como `Direct Lake` no motor VertiPaq, sem a emissão de instruções SQL com a tag `DirectQuery` enviadas ao SQL Endpoint.", "isCorrect": True},
            {"id": "B", "text": "O relatório exibe um alerta de erro em fonte vermelha.", "isCorrect": False},
            {"id": "C", "text": "O visual leva mais de 2 minutos para renderizar.", "isCorrect": False},
            {"id": "D", "text": "O Power BI fecha repentinamente sem salvar.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "No DAX Studio (Server Timings), consultas em modo Direct Lake puro são executadas pelo VertiPaq Storage Engine diretamente sobre os arquivos Parquet carregados na memória, rotuladas como `Direct Lake`. Se ocorrer fallback, o DAX Studio exibe uma consulta SQL enviada via `DirectQuery` para o SQL Endpoint do Fabric.",
            [
                "<strong>B, C e D:</strong> Comportamentos anômalos que não correspondem ao diagnóstico formal de Direct Lake."
            ],
            "Diagnóstico de Direct Lake: No DAX Studio / Server Timings, a consulta deve indicar Storage Engine `Direct Lake` (sem eventos DirectQuery)."
        )
    },
    {
        "id": "d3_q34",
        "domain": "domain3",
        "type": "single",
        "title": "Sincronização de Modelo Semântico e Framing no Direct Lake",
        "question": "Após a conclusão da ingestão de novos dados em uma tabela Delta pelo Spark, os relatórios em Direct Lake ainda exibem os dados antigos por alguns minutos. Qual processo governa a visibilidade das novas transações no modelo semântico Direct Lake?",
        "options": [
            {"id": "A", "text": "O processo de Framing e Sincronização de Metadados do Modelo Semântico (que atualiza o ponteiro de versão Delta para a versão mais recente comitada).", "isCorrect": True},
            {"id": "B", "text": "O envio de uma cópia dos dados por correio eletrônico.", "isCorrect": False},
            {"id": "C", "text": "A reinicialização física dos switches de fibra óptica.", "isCorrect": False},
            {"id": "D", "text": "O Direct Lake nunca atualiza dados novos sem excluir o relatório.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Modelos Semânticos em modo Direct Lake utilizam o conceito de 'Framing' (enquadramento de versão): o modelo se conecta a uma versão específica do Delta Log para manter consistência de leitura durante sessões ativas de usuários. Uma sincronização (Refresh/Sync do modelo) move o quadro para a versão mais recente da tabela Delta.",
            [
                "<strong>B, C e D:</strong> Falsas declarações sem embasamento na arquitetura do Direct Lake."
            ],
            "Framing no Direct Lake: Mantém a versão Delta consistente e avança para a versão mais recente mediante sincronização (Sync/Refresh)."
        )
    },
    {
        "id": "d3_q35",
        "domain": "domain3",
        "type": "single",
        "title": "Comportamento de Fallback por Limite de Memória da Capacidade",
        "question": "O que ocorre se o volume total de colunas solicitadas por relatórios Power BI em uma tabela física em modo Direct Lake ultrapassar o limite de memória RAM alocado para o modelo no F-SKU contratado?",
        "options": [
            {"id": "A", "text": "O modelo realiza Fallback gracioso para DirectQuery para atender às consultas que não couberem na memória, garantindo que o relatório responda aos usuários sem falha fatal.", "isCorrect": True},
            {"id": "B", "text": "O locatário inteiro do Fabric é desativado pela Microsoft por 48 horas.", "isCorrect": False},
            {"id": "C", "text": "O banco de dados transacional de origem é excluído.", "isCorrect": False},
            {"id": "D", "text": "Todas as senhas dos diretores são resetadas.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O mecanismo de Fallback do Direct Lake foi projetado como uma rede de segurança: caso os limites de memória da capacidade sejam excedidos para aquele modelo, o motor direciona as consultas para o modo DirectQuery, consumindo capacidade computacional via SQL Endpoint para não quebrar os visuais dos usuários de negócio.",
            [
                "<strong>B, C e D:</strong> Consequências falsas e alarmistas."
            ],
            "Fallback do Direct Lake: Mecanismo de resiliência que desvia para DirectQuery caso os limites de memória do F-SKU sejam estourados."
        )
    },
    {
        "id": "d3_q36",
        "domain": "domain3",
        "type": "single",
        "title": "Configuração da Propriedade `DirectLakeBehavior`",
        "question": "Um arquiteto de dados corporativo determinou que os relatórios do Power BI NUNCA devem fazer Fallback silencioso para DirectQuery, pois consultas lentas em DirectQuery podem gerar sobrecarga inesperada de CUs no SQL Endpoint. Qual configuração da propriedade `DirectLakeBehavior` no Modelo Semântico deve ser aplicada?",
        "options": [
            {"id": "A", "text": "`DirectLakeOnly`", "isCorrect": True},
            {"id": "B", "text": "`Automatic`", "isCorrect": False},
            {"id": "C", "text": "`DirectQueryOnly`", "isCorrect": False},
            {"id": "D", "text": "`Disabled`", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A propriedade `DirectLakeBehavior` aceita opções como `Automatic` (comportamento padrão: tenta Direct Lake e faz fallback para DirectQuery se necessário) e `DirectLakeOnly` (bloqueia estritamente o fallback; se a consulta não puder ser atendida pelo Direct Lake nativo na memória, retorna erro explícito em vez de degradar para DirectQuery).",
            [
                "<strong>B:</strong> `Automatic` permite o fallback para DirectQuery silenciosamente.",
                "<strong>C:</strong> `DirectQueryOnly` desativa o Direct Lake forçando sempre consultas relacionais T-SQL.",
                "<strong>D:</strong> Incorreto."
            ],
            "Controle de Fallback: Configure `DirectLakeBehavior = DirectLakeOnly` para impedir fallback silencioso para DirectQuery."
        )
    },
    {
        "id": "d3_q37",
        "domain": "domain3",
        "type": "single",
        "title": "Impacto de Tipos de Dados Não Suportados no Direct Lake",
        "question": "Qual dos seguintes tipos de dados de coluna em uma tabela Delta pode impedir que a coluna seja lida em modo Direct Lake puro no Power BI, induzindo fallback?",
        "options": [
            {"id": "A", "text": "Tipos binários arbitrários complexos não estruturados ou tipos com precisão decimal superior a 38 dígitos não suportados pelo Analysis Services.", "isCorrect": True},
            {"id": "B", "text": "Colunas do tipo `Integer` (números inteiros de 32 bits).", "isCorrect": False},
            {"id": "C", "text": "Colunas do tipo `String` (texto padronizado UTF-8).", "isCorrect": False},
            {"id": "D", "text": "Colunas do tipo `Date` (datas no calendário gregoriano).", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Analysis Services VertiPaq suporta os tipos analíticos padrão (Integer, BigInt, String, Double, Decimal até 4 casas fixas, DateTime, Boolean). Tipos não convencionais ou tipos binários brutos complexos não mapeáveis diretamente no VertiPaq podem forçar a consulta a fazer fallback para DirectQuery.",
            [
                "<strong>B, C e D:</strong> Tipos de dados primitivos 100% suportados no Direct Lake com máxima performance."
            ],
            "Compatibilidade Direct Lake: Garanta tipos analíticos padrão (Int, String, DateTime, Decimal) nas tabelas Gold."
        )
    },
    {
        "id": "d3_q38",
        "domain": "domain3",
        "type": "single",
        "title": "Medição de Tempo de Inicialização (Cold vs Warm Cache) no VertiPaq",
        "question": "Quando um relatório em Direct Lake é acessado pela primeira vez na manhã após uma atualização noturna, o primeiro visual leva 4 segundos para carregar, mas todas as interações seguintes de filtros respondem em menos de 100 milissegundos. Qual é a explicação técnica para essa diferença?",
        "options": [
            {"id": "A", "text": "O primeiro acesso incorre em 'Cold Cache' (paginação dos arquivos Parquet do OneLake para a memória RAM do Analysis Services). Uma vez na RAM ('Warm Cache'), as interações seguintes acontecem na velocidade nativa do VertiPaq em memória.", "isCorrect": True},
            {"id": "B", "text": "O computador do usuário estava esquentando a placa de vídeo.", "isCorrect": False},
            {"id": "C", "text": "O Fabric cobra mais caro pelo primeiro clique do dia.", "isCorrect": False},
            {"id": "D", "text": "A Microsoft reinicia todos os roteadores mundiais às 08:00 horas.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "No modo Direct Lake, os arquivos Parquet com V-Order residem no OneLake. Na primeira consulta (Cold Cache), as colunas requisitadas são mapeadas e paginadas sob demanda para a memória RAM do serviço (Analysis Services). Consultas subsequentes encontram os blocos já residentes na memória ('Warm Cache'), proporcionando respostas quase instantâneas.",
            [
                "<strong>B, C e D:</strong> Falsas noções sem fundamentação em engenharia de sistemas analíticos."
            ],
            "Cold Cache vs Warm Cache no Direct Lake: Primeiro carregamento pagina dados do OneLake para a RAM; acessos seguintes operam 100% em memória."
        )
    }
]

def get_domain3_questions():
    return DOMAIN_3_QUESTIONS

if __name__ == "__main__":
    qs = get_domain3_questions()
    print(f"Domain 3: {len(qs)} questões carregadas.")


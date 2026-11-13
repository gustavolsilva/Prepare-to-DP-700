"""
Casos de Estudo Corporativos do Exame DP-700
8 Casos de Estudo com Split-Screen e 4 abas obrigatórias de contexto (Overview, Existing Env, Data Req, Tech Req)
Cada caso de estudo contém 3 questões comentadas (24 questões no total).
"""

def get_case_studies():
    return [
        # CASO DE ESTUDO 1: CONTOSO GLOBAL RETAIL
        {
            "id": "cs1",
            "type": "case_study",
            "domain": "Estudo de Caso Corporativo: Contoso Global Retail",
            "caseTitle": "Contoso Global Retail: Modernização Analítica com Microsoft Fabric",
            "tabs": [
                {
                    "id": "overview",
                    "title": "Visão Geral",
                    "content": """<h4>Perfil da Empresa</h4>
<p>A Contoso Global Retail é uma grande rede multinacional de varejo com mais de 1.200 lojas físicas e uma plataforma de e-commerce global em rápida expansão.</p>
<h4>Objetivo de Negócio</h4>
<p>A diretoria de tecnologia aprovou a migração da arquitetura analítica legada (baseada em SQL Server on-premises e data lakes isolados) para o <strong>Microsoft Fabric</strong> sobre uma capacidade dedicada <strong>F64</strong>.</p>"""
                },
                {
                    "id": "existing_env",
                    "title": "Ambiente Atual",
                    "content": """<h4>Infraestrutura e Origens</h4>
<ul>
<li><strong>ERP Operacional:</strong> Banco de dados relacional transacional (OLTP) em Azure SQL Database com 4 TB de dados de pedidos e clientes.</li>
<li><strong>Histórico de Vendas Externo:</strong> 25 TB de dados em formato Parquet armazenados em um bucket do <strong>Amazon S3 (Região us-east-1)</strong>.</li>
<li><strong>Workspaces Fabric:</strong> Um workspace de produção denominado <code>WS_Prod_Contoso</code> atribuído à capacidade F64.</li>
<li><strong>Segurança:</strong> O acesso dos analistas deve respeitar políticas estritas de isolamento por filial regional.</li>
</ul>"""
                },
                {
                    "id": "data_req",
                    "title": "Requisitos de Dados",
                    "content": """<h4>Padrão de Ingestão e Processamento</h4>
<ul>
<li>Os dados do ERP Azure SQL devem ser sincronizados continuamente para o OneLake sem que nenhuma consulta pesada de extração degrade a performance do banco operacional.</li>
<li>Os dados do bucket Amazon S3 precisam ser acessados imediatamente pelos notebooks de ciência de dados sem incorrer em custos de egress de duplicação física.</li>
<li>A tabela de clientes deve manter o histórico completo de mudanças de endereço e categoria (SCD Tipo 2).</li>
</ul>"""
                },
                {
                    "id": "tech_req",
                    "title": "Requisitos Técnicos",
                    "content": """<h4>Restrições Mandatórias da Segurança e Governança</h4>
<ul>
<li><strong>Minimizar Esforço de Desenvolvimento:</strong> Sempre priorizar recursos nativos do Fabric gerenciados pela Microsoft.</li>
<li><strong>Segurança a Nível de Linha (RLS):</strong> Gerentes regionais só podem visualizar vendas correspondentes à sua região geográfica (coluna <code>RegionCode</code>).</li>
<li><strong>Relatórios Power BI:</strong> Os relatórios executivos devem utilizar o modo <strong>Direct Lake</strong> para evitar tempos de atualização agendada às 06:00.</li>
<li><strong>Importante:</strong> Se uma regra de RLS for aplicada diretamente na tabela Delta do Lakehouse, o Power BI Direct Lake pode sofrer fallback para DirectQuery. A equipe exige que o relatório mantenha a performance em memória do Direct Lake.</li>
</ul>"""
                }
            ],
            "questions": [
                {
                    "id": "cs1_q1",
                    "type": "single",
                    "prompt": "Com base nas seções 'Ambiente Atual' e 'Requisitos de Dados', qual tecnologia do Microsoft Fabric você deve implementar para sincronizar continuamente as tabelas do ERP Azure SQL Database para o OneLake com o menor esforço de desenvolvimento e sem degradar a performance operacional?",
                    "options": [
                        { "id": "A", "text": "Configurar Fabric Database Mirroring para o Azure SQL Database.", "isCorrect": True },
                        { "id": "B", "text": "Criar um pipeline no Data Factory agendado a cada 10 minutos.", "isCorrect": False },
                        { "id": "C", "text": "Exportar scripts BCP diariamente usando máquinas virtuais Azure.", "isCorrect": False },
                        { "id": "D", "text": "Utilizar Dataflow Gen2 com carga incremental via Power Query M.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> O <strong>Database Mirroring</strong> no Fabric é a solução nativa zero-ETL da Microsoft que lê os logs de transação do Azure SQL Database via Change Data Capture (CDC) e replica continuamente para tabelas Delta no OneLake sem impacto nas transações operacionais.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B e D:</strong> Pipelines e Dataflows exigem desenvolvimento manual e geram consultas pesadas que causam locks no banco operacional.</li>
<li><strong>C:</strong> Scripts BCP manuais não são gerenciados e exigem infraestrutura externa.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> Para replicação zero-ETL quase em tempo real de Azure SQL Database, Snowflake ou Cosmos DB para o OneLake, a resposta oficial é <strong>Database Mirroring</strong>.</div>"""
                },
                {
                    "id": "cs1_q2",
                    "type": "single",
                    "prompt": "Com base nas seções 'Requisitos de Dados' e 'Requisitos Técnicos', como os dados de 25 TB armazenados no bucket Amazon S3 devem ser disponibilizados no Lakehouse do workspace WS_Prod_Contoso?",
                    "options": [
                        { "id": "A", "text": "Criar um OneLake Shortcut apontando para o bucket do Amazon S3.", "isCorrect": True },
                        { "id": "B", "text": "Executar uma atividade Copy Data no Data Factory para duplicar os arquivos.", "isCorrect": False },
                        { "id": "C", "text": "Baixar os arquivos via FTP e fazer upload manual no Lakehouse Files.", "isCorrect": False },
                        { "id": "D", "text": "Criar um cluster Databricks dedicado fora da capacidade do Fabric.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> Os <strong>OneLake Shortcuts</strong> para Amazon S3 atendem perfeitamente aos requisitos de eliminar a duplicação física e evitar custos de transferência e esforço de desenvolvimento, expondo os dados instantaneamente no Lakehouse.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B:</strong> Duplicar 25 TB via Copy Data gera custo de egress na AWS e duplica custos de armazenamento.</li>
<li><strong>C e D:</strong> São soluções frágeis ou externas que contrariam o uso do Microsoft Fabric.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> Shortcuts para o Amazon S3 suportam tanto IAM Roles quanto Chaves de Acesso (Access Key / Secret Key).</div>"""
                },
                {
                    "id": "cs1_q3",
                    "type": "multi",
                    "prompt": "Considere as restrições da seção 'Requisitos Técnicos' relativas ao Power BI Direct Lake e Segurança a Nível de Linha (RLS). Quais DUAS ações a equipe de arquitetura deve adotar para garantir a governança de acesso regional sem forçar o fallback do Direct Lake para o modo DirectQuery? (Escolha duas alternativas).",
                    "options": [
                        { "id": "A", "text": "Implementar as regras de RLS dentro do Modelo Semântico do Power BI.", "isCorrect": True },
                        { "id": "B", "text": "Garantir que a identidade do relatório acesse o Lakehouse via permissão Read.", "isCorrect": True },
                        { "id": "C", "text": "Aplicar RLS nativo no SQL Analytics Endpoint do Lakehouse.", "isCorrect": False },
                        { "id": "D", "text": "Configurar o modelo do Power BI para o modo de Importação diária.", "isCorrect": False },
                        { "id": "E", "text": "Desabilitar a criptografia de dados em repouso no Azure Storage.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que as alternativas A e B estão corretas:</strong> Para que o Power BI opere em modo Direct Lake puro com RLS sem sofrer Fallback para DirectQuery, as funções de Row-Level Security devem ser definidas <em>dentro do próprio Modelo Semântico do Power BI</em> (Semantic Model RLS), e a identidade do modelo precisa de permissão de leitura (Read) sobre o Lakehouse de origem.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>C:</strong> Aplicar RLS no SQL Endpoint é exatamente o que força o fallback silencioso para DirectQuery!</li>
<li><strong>D:</strong> O modo Importação viola o requisito explícito de usar Direct Lake sem atualização agendada.</li>
<li><strong>E:</strong> Desabilitar criptografia viola segurança corporativa e não afeta o modo de consulta.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> RLS no SQL Endpoint = DirectQuery Fallback. RLS no Semantic Model = Direct Lake Puro preservado.</div>"""
                }
            ]
        },

        # CASO DE ESTUDO 2: LITWARE SMART IOT ENERGY GRID
        {
            "id": "cs2",
            "type": "case_study",
            "domain": "Estudo de Caso Corporativo: Litware Smart IoT Energy Grid",
            "caseTitle": "Litware Inc.: Plataforma de Telemetria e Streaming em Tempo Real com Eventhouse",
            "tabs": [
                {
                    "id": "overview",
                    "title": "Visão Geral",
                    "content": """<h4>Perfil da Empresa</h4>
<p>A Litware Inc. opera uma rede inteligente de distribuição elétrica (Smart Grid) cobrindo mais de 500.000 medidores inteligentes conectados em áreas metropolitanas.</p>
<h4>Objetivo do Projeto</h4>
<p>Implantar uma arquitetura de telemetria analítica no <strong>Microsoft Fabric</strong> sobre uma capacidade <strong>F128</strong> capaz de processar 50.000 eventos por segundo com latência de subsegundo para alertas de emergência e persistência histórica fria de 5 anos no OneLake.</p>"""
                },
                {
                    "id": "existing_env",
                    "title": "Ambiente Atual",
                    "content": """<h4>Infraestrutura e Origens</h4>
<ul>
<li><strong>Ingestão de Streaming:</strong> Clusters de Azure Event Hubs recebem fluxos massivos de telemetria em formato JSON com campos <code>MeterId</code>, <code>TimestampUtc</code>, <code>Voltage</code>, <code>CurrentAmp</code> e <code>ErrorCode</code>.</li>
<li><strong>Capacidade Fabric:</strong> Capacidade dedicada F128 associada aos workspaces <code>WS_IoT_RealTime</code> e <code>WS_IoT_Analytics</code>.</li>
<li><strong>Workload Híbrido:</strong> O centro de controle exige visualização em telas de tempo real (latência < 2s), enquanto a equipe de ciência de dados treina modelos em batch no Spark Lakehouse.</li>
</ul>"""
                },
                {
                    "id": "data_req",
                    "title": "Requisitos de Dados",
                    "content": """<h4>Processamento e Transformação Contínua</h4>
<ul>
<li>A tabela de telemetria bruta (<code>RawTelemetry</code>) deve ser agregada a cada janela de 5 minutos, gravando médias e picos de voltagem por medidor na tabela <code>AggregatedMetrics</code> de forma transacional e síncrona na chegada dos dados.</li>
<li>Todos os dados brutos de streaming devem ser roteados e persistidos em formato Delta Parquet na camada Bronze do Lakehouse para conformidade regulatória de 5 anos com custo reduzido.</li>
</ul>"""
                },
                {
                    "id": "tech_req",
                    "title": "Requisitos Técnicos",
                    "content": """<h4>Mecanismos de Consulta e Governança</h4>
<ul>
<li><strong>Consultas Ultra-Rápidas:</strong> As buscas por códigos de falha em strings de log devem responder em milissegundos utilizando o motor de indexação invertida do KQL.</li>
<li><strong>Último Estado do Medidor:</strong> Os operadores precisam obter instantaneamente a leitura mais recente de cada medidor sem realizar varreduras completas de tabelas históricas.</li>
<li><strong>Zero Código para Roteamento:</strong> Priorizar componentes visuais do Fabric para direcionar o stream do Event Hub simultaneamente para o Eventhouse e para o Lakehouse.</li>
</ul>"""
                }
            ],
            "questions": [
                {
                    "id": "cs2_q1",
                    "type": "single",
                    "prompt": "Com base nas seções 'Visão Geral' e 'Requisitos de Dados', qual recurso nativo do KQL no Eventhouse deve ser configurado para transformar e agregar as mensagens em janelas de 5 minutos na tabela AggregatedMetrics no momento exato em que os dados são ingeridos na tabela RawTelemetry?",
                    "options": [
                        { "id": "A", "text": "Uma Update Policy vinculada a uma função KQL de agregação.", "isCorrect": True },
                        { "id": "B", "text": "Um pipeline do Data Factory com gatilho de agendamento a cada 5 minutos.", "isCorrect": False },
                        { "id": "C", "text": "Uma exibição normal criada com instrução CREATE VIEW em T-SQL.", "isCorrect": False },
                        { "id": "D", "text": "Um notebook PySpark executado manualmente pelo operador de plantão.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> As <strong>Update Policies</strong> no KQL (Eventhouse) são o mecanismo transacional nativo para processar dados de streaming na ingestão, permitindo filtrar, transformar e agregar registros síncrona ou assincronamente direto para uma tabela destino sem pipelines externos.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B:</strong> Agendar pipelines a cada 5 minutos introduz atraso e sobrecarga de computação desnecessária.</li>
<li><strong>C e D:</strong> Views e execuções manuais não persistem dados agregados de forma contínua e em tempo real.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> Update Policies no Eventhouse são atômicas: a transformação ocorre durante o processo de append no stream.</div>"""
                },
                {
                    "id": "cs2_q2",
                    "type": "single",
                    "prompt": "Com base na seção 'Requisitos Técnicos', qual componente do Microsoft Fabric você deve utilizar para ingerir o fluxo do Azure Event Hubs e roteá-lo simultaneamente para o Eventhouse (para análise em tempo real) e para o Lakehouse (em Delta Parquet para histórico de 5 anos) com configuração visual e sem escrever código?",
                    "options": [
                        { "id": "A", "text": "Configurar um Fabric Eventstream com múltiplos destinos gerenciados.", "isCorrect": True },
                        { "id": "B", "text": "Criar scripts Python em máquinas virtuais fora da nuvem da Microsoft.", "isCorrect": False },
                        { "id": "C", "text": "Executar o utilitário AzCopy via prompt de comando uma vez por semana.", "isCorrect": False },
                        { "id": "D", "text": "Exportar arquivos CSV do Event Hub manualmente via portal do Azure.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> O <strong>Fabric Eventstream</strong> é o serviço nativo sem código para captura, transformação e roteamento de fluxos de eventos em tempo real para múltiplos destinos do Fabric, incluindo Eventhouse (KQL Database) e Lakehouse (tabelas Delta).</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B, C e D:</strong> São soluções manuais ou externas que violam a premissa de usar ferramentas SaaS gerenciadas do Microsoft Fabric.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> O Eventstream suporta múltiplos destinos e transformações visuais inline (Filter, Aggregate, Expand JSON).</div>"""
                },
                {
                    "id": "cs2_q3",
                    "type": "multi",
                    "prompt": "Considere a necessidade de consultar os logs de telemetria com alta performance no Eventhouse e identificar o último estado reportado de cada medidor conforme os 'Requisitos Técnicos'. Quais DUAS instruções ou operadores KQL atendem a essas demandas com máxima eficiência? (Escolha duas alternativas).",
                    "options": [
                        { "id": "A", "text": "Utilizar o operador 'has' para buscas otimizadas de strings indexadas.", "isCorrect": True },
                        { "id": "B", "text": "Utilizar a função 'arg_max(TimestampUtc, *)' agrupada por MeterId.", "isCorrect": True },
                        { "id": "C", "text": "Utilizar o operador 'contains' que força varredura completa caractere a caractere.", "isCorrect": False },
                        { "id": "D", "text": "Executar o comando VACUUM com retenção zero para acelerar a leitura.", "isCorrect": False },
                        { "id": "E", "text": "Converter a tabela KQL para uma pasta de arquivos texto descompactados.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que as alternativas A e B estão corretas:</strong> No KQL, o operador <code>has</code> utiliza o índice invertido de termos com velocidade centenas de vezes superior ao <code>contains</code> (que faz regex scan linha a linha). Para obter a linha mais recente de cada entidade, a função de agregação <code>arg_max(Timestamp, *)</code> é a forma canônica e de mais alta performance.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>C:</strong> O operador <code>contains</code> ignora o índice de termos e realiza varredura exaustiva lenta.</li>
<li><strong>D e E:</strong> O comando VACUUM e arquivos texto são inadequados para motores KQL de alta velocidade.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> Prefira sempre <code>has</code> a <code>contains</code> quando buscar palavras inteiras ou termos indexados em KQL.</div>"""
                }
            ]
        },

        # CASO DE ESTUDO 3: FABRIKAM FINANCIAL SERVICES
        {
            "id": "cs3",
            "type": "case_study",
            "domain": "Estudo de Caso Corporativo: Fabrikam Financial Services",
            "caseTitle": "Fabrikam Wealth: Governança, Segurança Granular e CI/CD no Fabric Data Warehouse",
            "tabs": [
                {
                    "id": "overview",
                    "title": "Visão Geral",
                    "content": """<h4>Perfil da Empresa</h4>
<p>A Fabrikam Financial Services gerencia carteiras de investimentos e patrimônio para mais de 100.000 clientes de alta renda em múltiplos países.</p>
<h4>Desafio de Governança</h4>
<p>A instituição precisa consolidar seu repositório analítico corporativo em um <strong>Fabric Data Warehouse</strong> garantindo conformidade rigorosa com normas de proteção de dados bancários (PCI-DSS e LGPD/GDPR), com controle total de versionamento via CI/CD.</p>"""
                },
                {
                    "id": "existing_env",
                    "title": "Ambiente Atual",
                    "content": """<h4>Workspaces e Estrutura</h4>
<ul>
<li><strong>Workspaces Separados:</strong> Três workspaces distintos no Fabric: <code>WS_Finance_Dev</code>, <code>WS_Finance_Test</code> e <code>WS_Finance_Prod</code>.</li>
<li><strong>Data Warehouse Central:</strong> Tabela <code>FactTransactions</code> com 2 bilhões de linhas e tabela dimensional <code>DimAccount</code> contendo números de cartões de crédito e saldo financeiro.</li>
<li><strong>Repositório Git:</strong> Projeto no Azure DevOps para versionamento de código e pipelines de integração contínua.</li>
</ul>"""
                },
                {
                    "id": "data_req",
                    "title": "Requisitos de Dados",
                    "content": """<h4>Privacidade e Mascaramento</h4>
<ul>
<li>Analistas de suporte júnior não podem visualizar o número completo do cartão de crédito (coluna <code>CreditCardNumber</code>), devendo visualizar apenas os últimos 4 dígitos mascarados no formato <code>XXXX-XXXX-XXXX-1234</code>.</li>
<li>Auditores de conformidade autorizados devem ter permissão explícita para visualizar os dados reais desmascarados.</li>
<li>Gerentes de agência regional só podem visualizar contas vinculadas à sua respectiva agência através de Row-Level Security (RLS).</li>
</ul>"""
                },
                {
                    "id": "tech_req",
                    "title": "Requisitos Técnicos",
                    "content": """<h4>Automação de CI/CD e Implantação</h4>
<ul>
<li>O esquema do Data Warehouse (tabelas, views e procedures) deve ser versionado como código declarativo em um projeto de banco de dados compilado.</li>
<li>A promoção de relatórios e pipelines entre DEV, TEST e PROD deve ser realizada através de <strong>Deployment Pipelines</strong>.</li>
<li>Ao implantar em PROD, a cadeia de conexão dos pipelines deve ser remapeada automaticamente para o banco de dados produtivo sem intervenção humana no código.</li>
</ul>"""
                }
            ],
            "questions": [
                {
                    "id": "cs3_q1",
                    "type": "single",
                    "prompt": "Com base nas seções 'Visão Geral' e 'Requisitos de Dados', qual recurso de segurança do T-SQL no Fabric Data Warehouse deve ser aplicado na coluna CreditCardNumber para exibir apenas os últimos 4 dígitos aos analistas de suporte, permitindo que auditores autorizados visualizem o número original?",
                    "options": [
                        { "id": "A", "text": "Dynamic Data Masking utilizando a função partial: partial(0, 'XXXX-XXXX-XXXX-', 4).", "isCorrect": True },
                        { "id": "B", "text": "Criptografar permanentemente o disco físico apagando as chaves de acesso.", "isCorrect": False },
                        { "id": "C", "text": "Excluir fisicamente a coluna CreditCardNumber de todas as tabelas analíticas.", "isCorrect": False },
                        { "id": "D", "text": "Substituir a tabela por um arquivo JSON público armazenado na pasta Files.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> O <strong>Dynamic Data Masking (DDM)</strong> no Fabric Data Warehouse permite ofuscar dados sensíveis em tempo de consulta sem alterar os dados gravados no disco, usando funções como <code>partial(prefix, padding, suffix)</code>. Usuários com permissão <code>UNMASK</code> visualizam os dados originais.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B, C e D:</strong> Destruir dados ou expor arquivos publicamente viola as diretrizes de governança bancária.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> DDM ofusca dados em tempo de leitura. Para conceder acesso a auditores, execute: <code>GRANT UNMASK TO [Auditor]</code>.</div>"""
                },
                {
                    "id": "cs3_q2",
                    "type": "single",
                    "prompt": "Com base na seção 'Requisitos Técnicos', qual abordagem é a recomendada oficialmente pela Microsoft para gerenciar o esquema DDL do Fabric Data Warehouse com versionamento no Git e compilação automatizada no Azure DevOps?",
                    "options": [
                        { "id": "A", "text": "Utilizar SQL Database Projects (.sqlproj) e implantação via pacote DACPAC.", "isCorrect": True },
                        { "id": "B", "text": "Executar cópias manuais de tabelas através do menu do navegador todo domingo.", "isCorrect": False },
                        { "id": "C", "text": "Armazenar scripts T-SQL não testados diretamente no bloco de notas da máquina local.", "isCorrect": False },
                        { "id": "D", "text": "Desabilitar o controle de versão e permitir edições concorrentes em produção.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> <strong>SQL Database Projects (.sqlproj)</strong> fornecem suporte declarativo completo para esquemas de banco de dados, possibilitando validação de sintaxe, controle de branches no Git e compilação em pacotes DACPAC para automação via pipelines do Azure DevOps.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B, C e D:</strong> Processos manuais sem versionamento ferem as diretrizes de CI/CD corporativas.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> Projetos .sqlproj compilam esquemas em arquivos .dacpac, suportando Schema Compare e DacDeploy.</div>"""
                },
                {
                    "id": "cs3_q3",
                    "type": "multi",
                    "prompt": "Considere a exigência de promover artefatos do estágio WS_Finance_Test para WS_Finance_Prod via Deployment Pipelines conforme a seção 'Requisitos Técnicos'. Quais DUAS configurações de Deployment Rules garantem que conexões de dados e variáveis de ambiente sejam atualizadas automaticamente para o ambiente produtivo? (Escolha duas alternativas).",
                    "options": [
                        { "id": "A", "text": "Configurar Data Source Rules no pipeline para remapear servidores de banco.", "isCorrect": True },
                        { "id": "B", "text": "Configurar Parameter Rules no pipeline para atualizar variáveis de ambiente.", "isCorrect": True },
                        { "id": "C", "text": "Editar manualmente os arquivos JSON de metadados diretamente no branch main.", "isCorrect": False },
                        { "id": "D", "text": "Executar o comando VACUUM com retenção zero em todas as tabelas do workspace.", "isCorrect": False },
                        { "id": "E", "text": "Desativar o protocolo de segurança TLS em todas as conexões de rede.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que as alternativas A e B estão corretas:</strong> As <strong>Deployment Rules</strong> em Deployment Pipelines do Fabric incluem <strong>Data Source Rules</strong> (para alterar instâncias de banco de dados ou workspaces alvo) e <strong>Parameter Rules</strong> (para atualizar valores de parâmetros de relatórios e pipelines como 'PROD' sem editar o código).</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>C, D e E:</strong> Editar JSON manualmente, executar VACUUM zero ou desativar TLS violam as boas práticas de DevOps e segurança.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> As regras de implantação são sempre configuradas no estágio de destino (Target Stage).</div>"""
                }
            ]
        },

        # CASO DE ESTUDO 4: WOODGROVE BANK & INSURANCE
        {
            "id": "cs4",
            "type": "case_study",
            "domain": "Estudo de Caso Corporativo: Woodgrove Bank & Insurance",
            "caseTitle": "Woodgrove Financial: Arquitetura Medalhão, Liquid Clustering e Otimização de Capacidade",
            "tabs": [
                {
                    "id": "overview",
                    "title": "Visão Geral",
                    "content": """<h4>Perfil da Organização</h4>
<p>O Woodgrove Bank & Insurance é um conglomerado financeiro com operações de varejo bancário, seguros de automóveis e fundos de previdência.</p>
<h4>Desafio de Modernização</h4>
<p>A instituição está migrando seu Data Lake corporativo de 200 TB para o <strong>Microsoft Fabric</strong> em uma capacidade dedicada <strong>F128</strong>, com objetivo de reduzir custos de computação, eliminar o problema de small files e fornecer dashboards executivos de subsegundo.</p>"""
                },
                {
                    "id": "existing_env",
                    "title": "Ambiente Atual",
                    "content": """<h4>Infraestrutura e Origens</h4>
<ul>
<li><strong>Data Lakes Existentes:</strong> Contas ADLS Gen2 em múltiplas regiões do Azure contendo arquivos Parquet brutos ingeridos diariamente.</li>
<li><strong>Capacidade Fabric:</strong> F128 atribuída aos workspaces <code>WS_Woodgrove_Bronze</code>, <code>WS_Woodgrove_Silver</code> e <code>WS_Woodgrove_Gold</code>.</li>
<li><strong>Volume da Tabela Principal:</strong> A tabela de apólices e sinistros (<code>FactClaims</code>) possui mais de 8 bilhões de linhas com alta dispersão de consultas por <code>DataSinistro</code> e <code>TipoSeguro</code>.</li>
</ul>"""
                },
                {
                    "id": "data_req",
                    "title": "Requisitos de Dados",
                    "content": """<h4>Processamento na Arquitetura Medalhão</h4>
<ul>
<li><strong>Camada Bronze:</strong> Ingestão append-only dos dados brutos através de OneLake Shortcuts para o ADLS Gen2 externo sem replicação física de arquivos.</li>
<li><strong>Camada Silver:</strong> Limpeza, tipagem e deduplicação utilizando PySpark com gravação Delta Lake e ordenação V-Order ativada por padrão.</li>
<li><strong>Camada Gold:</strong> Modelagem Star Schema com a tabela <code>FactClaims</code> clusterizada para permitir que consultas analíticas realizem data skipping de mais de 95% dos arquivos.</li>
</ul>"""
                },
                {
                    "id": "tech_req",
                    "title": "Requisitos Técnicos",
                    "content": """<h4>Prevenção de Throttling e Performance</h4>
<ul>
<li><strong>Controle de CUs:</strong> Durante as cargas noturnas pesadas, a utilização de computação ultrapassa 150% da capacidade F128. O sistema deve amortizar o consumo sem rejeitar consultas interativas de operadores de plantão.</li>
<li><strong>Eliminação de Small Files:</strong> A tabela FactClaims não deve utilizar particionamento físico por data que gere milhares de diretórios vazios.</li>
<li><strong>Governança de Exclusão:</strong> Operações de conformidade LGPD que excluem sinistros a pedido do cliente devem permitir auditoria de Time Travel por 14 dias antes do expurgo físico definitivo.</li>
</ul>"""
                }
            ],
            "questions": [
                {
                    "id": "cs4_q1",
                    "type": "single",
                    "prompt": "Com base na seção 'Requisitos de Dados', qual técnica de otimização do Delta Lake 3.0 você deve aplicar na tabela FactClaims na camada Gold para maximizar o Data Skipping e evitar o problema de particionamento excessivo em diretórios físicos?",
                    "options": [
                        { "id": "A", "text": "Liquid Clustering com a sintaxe CLUSTER BY (DataSinistro, TipoSeguro).", "isCorrect": True },
                        { "id": "B", "text": "Particionamento físico em diretórios por ano, mês, dia e hora.", "isCorrect": False },
                        { "id": "C", "text": "Conversão da tabela para formato CSV sem indexação.", "isCorrect": False },
                        { "id": "D", "text": "Desativação dos metadados de estatísticas Min/Max no _delta_log.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> O <strong>Liquid Clustering</strong> (ativado com <code>CLUSTER BY</code>) é a solução oficial da Microsoft para tabelas multibilionárias no Fabric. Ele organiza dados em múltiplos eixos sem criar diretórios físicos no OneLake, eliminando o problema de arquivos pequenos e maximizando o <em>Data Skipping</em> através dos metadados Min/Max do <code>_delta_log</code>.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B:</strong> Particionar fisicamente por hora cria dezenas de milhares de arquivos minúsculos que degradam o desempenho.</li>
<li><strong>C e D:</strong> Formato CSV e desativação de estatísticas anulam o poder do motor analítico.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> O Liquid Clustering substitui o particionamento Hive clássico e permite executar re-clusterização incremental via <code>OPTIMIZE table</code>.</div>"""
                },
                {
                    "id": "cs4_q2",
                    "type": "single",
                    "prompt": "Com base na seção 'Requisitos Técnicos', como o mecanismo de Smoothing do Microsoft Fabric trata a carga pesada de 150% de CUs gerada pelos pipelines noturnos de background na capacidade F128?",
                    "options": [
                        { "id": "A", "text": "Amortiza o pico de consumo de background em uma janela móvel de 24 horas.", "isCorrect": True },
                        { "id": "B", "text": "Cancela sumariamente todos os pipelines quando a utilização atinge 101%.", "isCorrect": False },
                        { "id": "C", "text": "Gera cobrança imediata de multas na fatura de cartão de crédito do Azure.", "isCorrect": False },
                        { "id": "D", "text": "Pausa a capacidade automaticamente exigindo reinício manual do servidor.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> No Fabric, jobs de background (como pipelines do Data Factory e rotinas Spark) têm seu consumo médio distribuído ao longo de uma <strong>janela de 24 horas</strong>. Graças ao <em>Bursting</em> e <em>Smoothing</em>, um pico noturno de 150% não causa throttling imediato caso a capacidade média das últimas 24h permaneça dentro de 100%.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B, C e D:</strong> O Fabric não cancela jobs arbitrariamente, não aplica multas e não desliga a capacidade por picos normais de processamento.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> Background Smoothing = 24 horas. Interactive Smoothing = 5 minutos.</div>"""
                },
                {
                    "id": "cs4_q3",
                    "type": "single",
                    "prompt": "Com base na exigência de conformidade LGPD da seção 'Requisitos Técnicos', qual comando de manutenção do Delta Lake deve ser agendado com o parâmetro de retenção de 14 dias (336 horas) para expurgar fisicamente os arquivos tombstoned obsoletos após o período de auditoria?",
                    "options": [
                        { "id": "A", "text": "VACUUM FactClaims RETAIN 336 HOURS;", "isCorrect": True },
                        { "id": "B", "text": "DROP TABLE FactClaims WITH PURGE;", "isCorrect": False },
                        { "id": "C", "text": "DELETE FROM FactClaims WHERE 1=1;", "isCorrect": False },
                        { "id": "D", "text": "OPTIMIZE FactClaims ZORDER BY (ClaimId);", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> O comando <code>VACUUM FactClaims RETAIN 336 HOURS</code> (14 dias * 24 horas = 336 horas) remove fisicamente os arquivos Parquet que foram marcados como obsoletos (tombstoned) por operações de exclusão ou atualização há mais de 14 dias, liberando espaço em disco e garantindo que o Time Travel permaneça acessível exatamente durante a janela de auditoria requerida.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B e C:</strong> <code>DROP TABLE</code> ou <code>DELETE FROM 1=1</code> destroem a tabela inteira e seus registros ativos.</li>
<li><strong>D:</strong> <code>OPTIMIZE</code> compacta arquivos, mas não remove arquivos tombstoned antigos.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> O período padrão de retenção do VACUUM é de 168 horas (7 dias). Para reter por 14 dias, use explicitamente <code>RETAIN 336 HOURS</code>.</div>"""
                }
            ]
        },

        # CASO DE ESTUDO 5: ADVENTUREWORKS E-COMMERCE & LOGÍSTICA
        {
            "id": "cs5",
            "type": "case_study",
            "domain": "Estudo de Caso Corporativo: AdventureWorks E-Commerce & Logística",
            "caseTitle": "AdventureWorks: Ingestão de Alta Concorrência, Watermarking e Cargas SCD Tipo 2",
            "tabs": [
                {
                    "id": "overview",
                    "title": "Visão Geral",
                    "content": """<h4>Perfil da Empresa</h4>
<p>A AdventureWorks é uma fabricante e distribuidora global de bicicletas e equipamentos esportivos com vendas diretas ao consumidor (B2C) e atacado (B2B).</p>
<h4>Desafio do Projeto</h4>
<p>A empresa precisa substituir seus fluxos de integração SSIS legados por uma arquitetura moderna no <strong>Microsoft Fabric Data Factory</strong> e <strong>Notebooks Spark</strong> para processar 30 milhões de transações diárias distribuídas em 120 tabelas relacionais.</p>"""
                },
                {
                    "id": "existing_env",
                    "title": "Ambiente Atual",
                    "content": """<h4>Fontes de Dados</h4>
<ul>
<li><strong>Bancos Operacionais:</strong> Múltiplas instâncias de Azure SQL Database e PostgreSQL on-premises conectadas via On-premises Data Gateway.</li>
<li><strong>Destino:</strong> Workspace de Produção no Fabric associado a uma capacidade F64.</li>
<li><strong>Tabelas Críticas:</strong> Tabelas de <code>Clientes</code>, <code>Pedidos</code> e <code>RastreamentoLogistico</code>.</li>
</ul>"""
                },
                {
                    "id": "data_req",
                    "title": "Requisitos de Dados",
                    "content": """<h4>Carga Incremental e Idempotência</h4>
<ul>
<li>A ingestão das 120 tabelas deve ocorrer em paralelo com no máximo 25 execuções simultâneas para não derrubar os pools de conexão dos bancos operacionais.</li>
<li>Apenas dados alterados desde a última carga bem-sucedida devem ser extraídos utilizando uma tabela de controle de Watermark em UTC.</li>
<li>A dimensão de clientes deve registrar mudanças de endereço mantendo a versão antiga com data de encerramento e inserindo a nova versão com data de vigência aberta (SCD Tipo 2).</li>
</ul>"""
                },
                {
                    "id": "tech_req",
                    "title": "Requisitos Técnicos",
                    "content": """<h4>Resiliência e Tolerância a Falhas</h4>
<ul>
<li>Falhas transitórias de conexão de rede não devem interromper o pipeline; cada atividade de cópia deve tentar se reconectar até 3 vezes com intervalo de 30 segundos.</li>
<li>A lógica de carga na camada Silver deve ser estritamente idempotente (reexecuções não podem duplicar linhas).</li>
</ul>"""
                }
            ],
            "questions": [
                {
                    "id": "cs5_q1",
                    "type": "single",
                    "prompt": "Com base nas seções 'Visão Geral' e 'Requisitos de Dados', como você deve estruturar o pipeline do Fabric Data Factory para iterar sobre as 120 tabelas garantindo concorrência máxima de 25 cópias simultâneas?",
                    "options": [
                        { "id": "A", "text": "Utilizar uma atividade ForEach com 'Sequential' desmarcado e 'Batch count' configurado em 25.", "isCorrect": True },
                        { "id": "B", "text": "Utilizar uma atividade ForEach com 'Sequential' marcado e tempo limite de 25 minutos.", "isCorrect": False },
                        { "id": "C", "text": "Criar 120 atividades de Copy Data conectadas manualmente em série.", "isCorrect": False },
                        { "id": "D", "text": "Utilizar uma atividade Until com condição booleana infinita.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> A atividade <strong>ForEach</strong> no Data Factory suporta execução concorrente desmarcando a opção <code>Sequential</code> e definindo o <code>Batch count</code> com o número desejado de threads paralelas (25). Isso otimiza o tempo total sem estourar as conexões de banco de dados.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B:</strong> 'Sequential' força execução estritamente sequencial (1 thread).</li>
<li><strong>C:</strong> Desenhar 120 atividades manuais é impraticável e não escalável.</li>
<li><strong>D:</strong> Until é uma estrutura de loop condicional, não de iteração de lista.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> O limite máximo de <code>Batch count</code> na atividade ForEach é de 50 threads simultâneas.</div>"""
                },
                {
                    "id": "cs5_q2",
                    "type": "single",
                    "prompt": "Com base na exigência de resiliência da seção 'Requisitos Técnicos', como as falhas transitórias de rede devem ser tratadas nas atividades de Copy Data do Data Factory?",
                    "options": [
                        { "id": "A", "text": "Configurar a propriedade 'Retry' com o valor 3 e o 'Retry interval (sec)' com 30.", "isCorrect": True },
                        { "id": "B", "text": "Adicionar uma atividade Wait de 4 horas antes de cada Copy Data.", "isCorrect": False },
                        { "id": "C", "text": "Excluir o workspace do Fabric e recriá-lo a cada falha de rede.", "isCorrect": False },
                        { "id": "D", "text": "Desativar o firewall do Azure e permitir acesso público irrestrito.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> As atividades do Data Factory possuem propriedades nativas de política de execução (Policy), onde configurar <code>Retry = 3</code> e <code>Retry interval (sec) = 30</code> instrui o serviço a tentar automaticamente a execução até 3 vezes com pausa de 30 segundos entre tentativas antes de registrar falha definitiva.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B:</strong> Esperar 4 horas atrasa o pipeline desnecessariamente.</li>
<li><strong>C e D:</strong> Destruir workspaces ou desativar segurança são soluções absurdas.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> Políticas de repetição (Retry Policies) são a melhor prática oficial para mitigar erros transitórios (código HTTP 429, 503 ou timeouts breves de rede).</div>"""
                },
                {
                    "id": "cs5_q3",
                    "type": "single",
                    "prompt": "Considerando o requisito de SCD Tipo 2 na dimensão de clientes na camada Silver, qual tecnologia e instrução garantem que a atualização das linhas antigas e a inserção das novas versões ocorram de forma atômica e idempotente?",
                    "options": [
                        { "id": "A", "text": "Delta Lake MERGE executado via PySpark ou SQL com cláusulas MATCHED e NOT MATCHED.", "isCorrect": True },
                        { "id": "B", "text": "Instrução TRUNCATE TABLE seguida de INSERT INTO completo.", "isCorrect": False },
                        { "id": "C", "text": "Comando DROP TABLE executado antes de cada carga incremental.", "isCorrect": False },
                        { "id": "D", "text": "Exportação manual de dados para planilhas eletrônicas locais.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> A instrução <strong>Delta MERGE</strong> é o padrão canônico para SCD Tipo 2 no Fabric. Ela permite correlacionar a chave de negócio do cliente, atualizar a linha ativa anterior (marcando a data de encerramento e status inativo) e inserir o novo registro com vigência atual em uma única transação atômica ACID.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B e C:</strong> TRUNCATE e DROP destroem o histórico temporal de versões anteriores.</li>
<li><strong>D:</strong> Planilhas manuais violam os princípios de engenharia de dados corporativa.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> No Spark, utilize <code>deltaTable.alias('target').merge(...)</code> para implementar SCD Tipo 2 com idempotência garantida.</div>"""
                }
            ]
        },

        # CASO DE ESTUDO 6: TAILWIND TRADERS MULTI-CLOUD ANALYTICS
        {
            "id": "cs6",
            "type": "case_study",
            "domain": "Estudo de Caso Corporativo: Tailwind Traders Multi-Cloud Analytics",
            "caseTitle": "Tailwind Traders: Arquitetura Zero-Copy Multi-Cloud e Governança com Purview",
            "tabs": [
                {
                    "id": "overview",
                    "title": "Visão Geral",
                    "content": """<h4>Perfil da Empresa</h4>
<p>A Tailwind Traders é uma varejista global que adquiriu recentemente duas empresas concorrentes operando em diferentes provedores de nuvem pública (AWS e Google Cloud Platform).</p>
<h4>Objetivo de Unificação</h4>
<p>Consolidar um único Data Lake corporativo no <strong>Microsoft Fabric OneLake</strong> conectando dados distribuídos em múltiplas nuvens sem custos de egress e com rastreabilidade total de governança via <strong>Microsoft Purview</strong>.</p>"""
                },
                {
                    "id": "existing_env",
                    "title": "Ambiente Atual",
                    "content": """<h4>Armazenamento Multi-Cloud</h4>
<ul>
<li><strong>AWS:</strong> 80 TB de dados históricos em formato Delta Lake armazenados em buckets do <strong>Amazon S3</strong>.</li>
<li><strong>GCP:</strong> 40 TB de logs de navegação em formato Parquet armazenados no <strong>Google Cloud Storage (GCS)</strong>.</li>
<li><strong>Microsoft:</strong> Dados de vendas de CRM corporativo hospedados no <strong>Microsoft Dataverse (Dynamics 365)</strong>.</li>
</ul>"""
                },
                {
                    "id": "data_req",
                    "title": "Requisitos de Dados",
                    "content": """<h4>Acesso e Zero-Copy</h4>
<ul>
<li>Nenhum dado das contas AWS ou GCP pode ser copiado fisicamente para o Azure para evitar custos proibitivos de transferência de rede (egress fees).</li>
<li>Os dados do Dataverse devem ser acessados pelos engenheiros no OneLake com sincronização contínua sem que a equipe precise construir pipelines de extração ETL.</li>
</ul>"""
                },
                {
                    "id": "tech_req",
                    "title": "Requisitos Técnicos",
                    "content": """<h4>Segurança e Rótulos de Sensibilidade</h4>
<ul>
<li>Rótulos de sensibilidade 'Confidencial' do Microsoft Purview aplicados ao Lakehouse devem se propagar automaticamente para todos os modelos semânticos e relatórios derivados.</li>
<li>Políticas de Data Loss Prevention (DLP) devem impedir que relatórios contendo números de previdência social (SSN) sejam exportados para o formato Excel por usuários comuns.</li>
</ul>"""
                }
            ],
            "questions": [
                {
                    "id": "cs6_q1",
                    "type": "multi",
                    "prompt": "Com base nas seções 'Ambiente Atual' e 'Requisitos de Dados', quais DOIS tipos de OneLake Shortcuts devem ser configurados no Lakehouse para expor os dados da AWS e do GCP sem movimentação física? (Escolha duas alternativas).",
                    "options": [
                        { "id": "A", "text": "OneLake Shortcut apontando para o bucket do Amazon S3.", "isCorrect": True },
                        { "id": "B", "text": "OneLake Shortcut apontando para o bucket do Google Cloud Storage (GCS).", "isCorrect": True },
                        { "id": "C", "text": "Pipeline de Copy Data com transferência por FTP seguro.", "isCorrect": False },
                        { "id": "D", "text": "Exportação manual de arquivos CSV via navegador web.", "isCorrect": False },
                        { "id": "E", "text": "Servidor NFS montado em máquina virtual local.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que as alternativas A e B estão corretas:</strong> O Microsoft OneLake oferece suporte nativo a <strong>Shortcuts para Amazon S3</strong> e <strong>Shortcuts para Google Cloud Storage (GCS)</strong>. Esses atalhos funcionam como ponteiros virtuais que permitem aos motores analíticos do Fabric consultar dados diretamente nos storages de terceiros sem cobrança de cópia e sem mover arquivos fisicamente.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>C, D e E:</strong> Envolvem cópias físicas de arquivos que geram altos custos de transferência e manutenção.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> O OneLake suporta atalhos para: <strong>ADLS Gen2</strong>, <strong>Amazon S3</strong>, <strong>Google Cloud Storage</strong> e <strong>Dataverse</strong>.</div>"""
                },
                {
                    "id": "cs6_q2",
                    "type": "single",
                    "prompt": "Com base na seção 'Requisitos de Dados', qual funcionalidade da plataforma Microsoft atende à exigência de disponibilizar os dados do Microsoft Dataverse (Dynamics 365) no OneLake com sincronização contínua e esforço zero de ETL?",
                    "options": [
                        { "id": "A", "text": "Habilitar o Fabric Link no portal do Microsoft Dataverse.", "isCorrect": True },
                        { "id": "B", "text": "Criar um Dataflow Gen2 executado a cada 1 minuto.", "isCorrect": False },
                        { "id": "C", "text": "Escrever scripts em linguagem C# compilados em console apps.", "isCorrect": False },
                        { "id": "D", "text": "Exportar os dados para fita magnética e fazer upload físico.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> O <strong>Fabric Link for Dataverse</strong> conecta diretamente as tabelas do Dynamics 365 e Power Apps ao OneLake em formato Delta Parquet. Uma vez ativado, o Dataverse mantém atalhos no OneLake atualizados continuamente de forma transparente e gerenciada pela Microsoft.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B, C e D:</strong> São soluções custosas, complexas e manuais que contrariam o uso do recurso nativo Fabric Link.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> O Fabric Link cria tabelas Delta no OneLake sem que o desenvolvedor precise construir pipelines no Data Factory.</div>"""
                },
                {
                    "id": "cs6_q3",
                    "type": "single",
                    "prompt": "Com base na seção 'Requisitos Técnicos', como os rótulos de confidencialidade do Microsoft Purview aplicados no Lakehouse protegem os artefatos downstream no Fabric e Power BI?",
                    "options": [
                        { "id": "A", "text": "Através da herança automática downstream para modelos semânticos e relatórios filhos.", "isCorrect": True },
                        { "id": "B", "text": "Excluindo o relatório do Power BI caso contenha mais de 10 páginas.", "isCorrect": False },
                        { "id": "C", "text": "Bloqueando o acesso de qualquer usuário durante os finais de semana.", "isCorrect": False },
                        { "id": "D", "text": "Exigindo que o analista digite uma senha de 64 dígitos a cada clique.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> A <strong>Herança Downstream de Rótulos de Sensibilidade</strong> do Purview assegura que, quando um item de dados original (Lakehouse ou Warehouse) é rotulado como 'Confidencial', todos os modelos semânticos e relatórios gerados a partir dele herdam automaticamente a classificação e suas restrições (como bloqueio de exportação DLP).</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B, C e D:</strong> São comportamentos inexistentes e absurdos na governança do Purview.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> Rótulos do Purview acompanham os dados inclusive quando exportados para arquivos Excel ou PDF, mantendo a criptografia de proteção.</div>"""
                }
            ]
        },

        # CASO DE ESTUDO 7: NORTHWIND HEALTH DIAGNOSTICS
        {
            "id": "cs7",
            "type": "case_study",
            "domain": "Estudo de Caso Corporativo: Northwind Health Diagnostics",
            "caseTitle": "Northwind Health: Diagnósticos em Tempo Real, CDC e Alta Disponibilidade com Eventhouse",
            "tabs": [
                {
                    "id": "overview",
                    "title": "Visão Geral",
                    "content": """<h4>Perfil da Instituição</h4>
<p>A Northwind Health Diagnostics opera uma rede de 80 laboratórios de análises clínicas e hospitais de alta complexidade realizando mais de 1 milhão de exames laboratoriais por dia.</p>
<h4>Desafio Crítico</h4>
<p>Resultados críticos de exames (como troponina para infarto agudo do miocárdio ou hemograma com alterações severas) precisam disparar alertas para os médicos em menos de 5 segundos a partir da liberação no banco de dados operacional.</p>"""
                },
                {
                    "id": "existing_env",
                    "title": "Ambiente Atual",
                    "content": """<h4>Infraestrutura de TI</h4>
<ul>
<li><strong>Sistema Laboratorial (LIS):</strong> Banco de dados relacional transacional em <strong>Azure SQL Database</strong> com Change Data Capture (CDC) habilitado na tabela <code>ExamesLiberados</code>.</li>
<li><strong>Capacidade Fabric:</strong> F64 compartilhada entre o workspace de alertas clínicos e o workspace de BI gerencial.</li>
<li><strong>Consumo:</strong> Médicos utilizam um painel de alerta em tempo real; diretores médicos utilizam relatórios analíticos consolidados no Power BI.</li>
</ul>"""
                },
                {
                    "id": "data_req",
                    "title": "Requisitos de Dados",
                    "content": """<h4>Fluxo de Dados em Tempo Real</h4>
<ul>
<li>As alterações na tabela do Azure SQL Database devem ser capturadas continuamente pelo Fabric sem impactar a performance das transações de gravação dos biomédicos.</li>
<li>Os eventos devem ser ingeridos em uma tabela de streaming no <strong>Eventhouse (KQL Database)</strong> com retenção de cache quente de 7 dias para buscas instantâneas.</li>
<li>Exames com mais de 7 dias devem ser retidos em armazenamento frio de baixo custo por 10 anos para conformidade legal.</li>
</ul>"""
                },
                {
                    "id": "tech_req",
                    "title": "Requisitos Técnicos",
                    "content": """<h4>Segurança de Prontuários (HIPAA / LGPD)</h4>
<ul>
<li>Médicos só podem visualizar exames de pacientes internados em sua respectiva unidade hospitalar (coluna <code>HospitalUnitId</code>).</li>
<li>A diretoria exige relatórios em <strong>Power BI Direct Lake</strong> sem que a regra de segurança cause fallback para DirectQuery.</li>
</ul>"""
                }
            ],
            "questions": [
                {
                    "id": "cs7_q1",
                    "type": "single",
                    "prompt": "Com base na seção 'Ambiente Atual' e 'Requisitos de Dados', qual conector de origem do Fabric Eventstream deve ser configurado para capturar continuamente as alterações na tabela ExamesLiberados do Azure SQL Database sem escrever código de polling?",
                    "options": [
                        { "id": "A", "text": "Azure SQL Database Change Data Capture (CDC) connector no Eventstream.", "isCorrect": True },
                        { "id": "B", "text": "Pipeline agendado no Data Factory executando SELECT a cada 1 segundo.", "isCorrect": False },
                        { "id": "C", "text": "Exportação manual de dados via Assistente de Importação e Exportação do SSMS.", "isCorrect": False },
                        { "id": "D", "text": "Triggers que enviam emails SMTP para uma caixa postal do Gmail.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> O conector nativo <strong>Azure SQL Database (CDC)</strong> no Fabric Eventstream lê de forma assíncrona as tabelas de Change Data Capture geradas pelo SQL Server, capturando inserções, alterações e exclusões em tempo real sem degradar as transações operacionais do sistema hospitalar.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B:</strong> Polling a cada 1 segundo satura a CPU do banco de dados relacional e gera locks.</li>
<li><strong>C e D:</strong> Processos manuais e emails são incompatíveis com alertas de emergência médica em subsegundo.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> O conector CDC do Eventstream transmite eventos nos formatos JSON contendo os metadados da operação (Insert, Update, Delete) e os valores de colunas anteriores e posteriores.</div>"""
                },
                {
                    "id": "cs7_q2",
                    "type": "single",
                    "prompt": "Com base na seção 'Requisitos de Dados', como as políticas de Caching e Retenção do KQL Database no Eventhouse devem ser configuradas para atender aos requisitos de 7 dias de alerta e 10 anos de histórico legal?",
                    "options": [
                        { "id": "A", "text": "Hot Cache Policy = 7 dias e Retention Policy = 3650 dias (10 anos).", "isCorrect": True },
                        { "id": "B", "text": "Hot Cache Policy = 3650 dias e Retention Policy = 7 dias.", "isCorrect": False },
                        { "id": "C", "text": "Desativar a política de retenção para expurgar dados a cada 24 horas.", "isCorrect": False },
                        { "id": "D", "text": "Configurar o cache quente em memória RAM para 5 minutos e excluir o restante.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> A <strong>Hot Cache Policy</strong> define o período em que os dados residem em armazenamento SSD/RAM local para consultas em milissegundos (7 dias), enquanto a <strong>Retention Policy</strong> define o prazo total de existência dos dados antes do descarte permanente (3650 dias / 10 anos no storage durável OneLake).</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B:</strong> Inverter os parâmetros reteria apenas 7 dias de histórico e sobrecarregaria a memória com 10 anos de cache.</li>
<li><strong>C e D:</strong> Excluir dados viola o prazo legal obrigatório de 10 anos para prontuários médicos.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> Hot Cache = performance imediata; Soft Delete / Retention Policy = ciclo de vida total dos dados.</div>"""
                },
                {
                    "id": "cs7_q3",
                    "type": "single",
                    "prompt": "Com base na seção 'Requisitos Técnicos', onde a regra de Row-Level Security (RLS) por HospitalUnitId deve ser implementada para assegurar que os médicos vejam apenas exames de sua unidade sem que os relatórios do Power BI sofram Fallback do modo Direct Lake?",
                    "options": [
                        { "id": "A", "text": "Dentro do Modelo Semântico do Power BI (Semantic Model RLS).", "isCorrect": True },
                        { "id": "B", "text": "Diretamente no SQL Analytics Endpoint do Lakehouse.", "isCorrect": False },
                        { "id": "C", "text": "No arquivo hosts do computador pessoal do médico.", "isCorrect": False },
                        { "id": "D", "text": "Em uma planilha de senhas compartilhada no Microsoft Teams.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> Para manter a performance in-memory do <strong>Power BI Direct Lake</strong> sem sofrer Fallback automático para consultas DirectQuery T-SQL, as regras de Row-Level Security devem ser configuradas <em>dentro do Modelo Semântico do Power BI</em>.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B:</strong> RLS configurada no SQL Analytics Endpoint do Lakehouse causa Fallback obrigatório para DirectQuery.</li>
<li><strong>C e D:</strong> São práticas inseguras e sem efeito sobre permissões de dados.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> Essa é a regra mais importante de Direct Lake: <strong>Semantic Model RLS = Direct Lake permitido</strong>; <strong>SQL Endpoint RLS = Fallback to DirectQuery</strong>.</div>"""
                }
            ]
        },

        # CASO DE ESTUDO 8: ALPINE SKI & RESORTS REAL-TIME INTELLIGENCE
        {
            "id": "cs8",
            "type": "case_study",
            "domain": "Estudo de Caso Corporativo: Alpine Ski & Resorts Real-Time Intelligence",
            "caseTitle": "Alpine Ski Resorts: Telemetria de Sensores de Pista, Detecção de Riscos e Testes Zero-Copy",
            "tabs": [
                {
                    "id": "overview",
                    "title": "Visão Geral",
                    "content": """<h4>Perfil da Empresa</h4>
<p>A Alpine Ski & Resorts opera 15 estações de esqui e esportes de inverno de classe mundial com mais de 2.000 sensores IoT instalados em pistas, teleféricos e encostas com risco de avalanche.</p>
<h4>Desafio Operacional</h4>
<p>Monitorar temperatura da neve, velocidade do vento e estabilidade do solo em tempo real no <strong>Microsoft Fabric</strong> para emitir alertas de evacuação instantâneos e analisar padrões climáticos históricos de longo prazo.</p>"""
                },
                {
                    "id": "existing_env",
                    "title": "Ambiente Atual",
                    "content": """<h4>Estrutura Tecnológica</h4>
<ul>
<li><strong>Dispositivos IoT:</strong> 2.000 sensores transmitindo via protocolo MQTT para <strong>Azure IoT Hub</strong> mensagens a cada 5 segundos.</li>
<li><strong>Workspaces Fabric:</strong> <code>WS_Alpine_LiveOps</code> (para tempo real) e <code>WS_Alpine_DataLab</code> (para homologação e ciência de dados).</li>
<li><strong>Capacidade:</strong> Capacidade dedicada F64.</li>
</ul>"""
                },
                {
                    "id": "data_req",
                    "title": "Requisitos de Dados",
                    "content": """<h4>Processamento de Streaming e Lotes</h4>
<ul>
<li>Um streaming Spark Structured Streaming no Fabric deve ler os dados do IoT Hub em janelas de tempo não sobrepostas de 10 minutos (Tumbling Windows) para calcular a média de rajadas de vento por encosta.</li>
<li>Para tolerar instabilidade de sinal nas montanhas, mensagens com até 20 minutos de atraso devem ser aceitas e integradas ao cálculo da janela correta através de Watermarking.</li>
</ul>"""
                },
                {
                    "id": "tech_req",
                    "title": "Requisitos Técnicos",
                    "content": """<h4>Ambiente de Homologação e Testes Rápidos</h4>
<ul>
<li>A equipe de cientistas de dados no workspace <code>WS_Alpine_DataLab</code> precisa clonar instantaneamente a tabela histórica de 10 bilhões de linhas de telemetria para treinar modelos preditivos de avalanche sem incorrer em novos custos de armazenamento de dados.</li>
<li>A tabela de homologação deve permitir alterações destrutivas sem afetar os dados oficiais de produção.</li>
</ul>"""
                }
            ],
            "questions": [
                {
                    "id": "cs8_q1",
                    "type": "single",
                    "prompt": "Com base na seção 'Requisitos de Dados', qual tipo de janela de tempo e qual cláusula do Spark Structured Streaming atendem ao cálculo de médias de rajadas de vento a cada 10 minutos sem sobreposição aceitando dados atrasados em até 20 minutos?",
                    "options": [
                        { "id": "A", "text": "Tumbling Window de 10 minutos combinada com .withWatermark('EventTime', '20 minutes').", "isCorrect": True },
                        { "id": "B", "text": "Sliding Window de 10 minutos com avanço a cada 1 segundo sem watermark.", "isCorrect": False },
                        { "id": "C", "text": "Session Window baseada em 24 horas de inatividade total de sinal.", "isCorrect": False },
                        { "id": "D", "text": "Execução em lote único diário desativando o streaming.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> As <strong>Tumbling Windows</strong> são janelas de tempo fixas e não sobrepostas (ex: 10:00-10:10, 10:10-10:20). A combinação com <code>.withWatermark('EventTime', '20 minutes')</code> instrui o Spark a manter o estado da janela em memória e aceitar mensagens que cheguem com até 20 minutos de atraso em relação ao tempo máximo observado.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B:</strong> Sliding Window com avanço de 1 segundo gera sobreposição e não trata o atraso sem watermark.</li>
<li><strong>C:</strong> Session windows dependem de inatividade, não sendo adequadas para janelas regulares de 10 minutos.</li>
<li><strong>D:</strong> Carga em lote diário viola o requisito de alertas de emergência em tempo real.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> <strong>Tumbling</strong> = blocos fixos contínuos sem sobreposição; <strong>Hopping/Sliding</strong> = blocos sobrepostos com salto regular; <strong>Session</strong> = agrupamento por períodos de atividade.</div>"""
                },
                {
                    "id": "cs8_q2",
                    "type": "single",
                    "prompt": "Com base na seção 'Requisitos Técnicos', qual funcionalidade do Fabric permite aos cientistas de dados clonar a tabela histórica de 10 bilhões de linhas instantaneamente para testes isolados sem duplicar o volume físico de armazenamento no OneLake?",
                    "options": [
                        { "id": "A", "text": "Zero-Copy Table Clone utilizando a sintaxe CREATE TABLE ... AS CLONE OF.", "isCorrect": True },
                        { "id": "B", "text": "Executar um pipeline Copy Data duplicando fisicamente os arquivos Parquet.", "isCorrect": False },
                        { "id": "C", "text": "Exportar toda a tabela para arquivos CSV compactados em formato ZIP.", "isCorrect": False },
                        { "id": "D", "text": "Executar o comando VACUUM com tempo de retenção zero em produção.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> O recurso <strong>Zero-Copy Table Clone</strong> (<code>CREATE TABLE Tabela_Teste AS CLONE OF Tabela_Prod</code>) cria uma cópia em nível de metadados que aponta para os mesmos arquivos Parquet imutáveis no OneLake. Os testes e modificações feitos pelos cientistas na tabela clonada gravam novos arquivos Delta sem alterar a tabela de produção e sem duplicar o storage dos dados inalterados.</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B:</strong> Duplicar 10 bilhões de linhas fisicamente consome horas de processamento e dobra os custos de storage.</li>
<li><strong>C:</strong> Exportar para ZIP perde o formato colunar e quebra a performance.</li>
<li><strong>D:</strong> VACUUM limpa arquivos obsoletos e não cria clones para testes.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> Clones no Fabric suportam tanto clones do estado atual quanto clones de um ponto no passado (Time Travel Clone) usando a cláusula <code>AS OF</code>.</div>"""
                },
                {
                    "id": "cs8_q3",
                    "type": "single",
                    "prompt": "Como os cientistas de dados devem garantir que as operações de gravação e treinamento de modelos no workspace WS_Alpine_DataLab não causem throttling ou esgotem as CUs das operações de segurança em tempo real do WS_Alpine_LiveOps durante horários críticos?",
                    "options": [
                        { "id": "A", "text": "Associar o workspace de testes WS_Alpine_DataLab a uma capacidade Fabric dedicada separada.", "isCorrect": True },
                        { "id": "B", "text": "Configurar a prioridade do Windows Task Manager na máquina dos cientistas.", "isCorrect": False },
                        { "id": "C", "text": "Desativar o firewall de rede durante a execução dos modelos.", "isCorrect": False },
                        { "id": "D", "text": "Forçar os operadores de pista a desligarem os sensores em dias de tempestade.", "isCorrect": False }
                    ],
                    "explanation": """<div class="explanation-correct"><strong>✅ Por que a alternativa A está correta:</strong> No Microsoft Fabric, o isolamento rigoroso de computação (evitando que cargas de testes ou ciência de dados consumam CUs de operações críticas) é realizado <strong>atribuindo workspaces diferentes a capacidades Fabric diferentes</strong> (ex: uma capacidade dedicada para produção e outra para desenvolvimento/testes, que pode ser pausada quando ociosa).</div>
<div class="explanation-distractors"><strong>❌ Análise dos Distratores:</strong>
<ul>
<li><strong>B, C e D:</strong> Gerenciador de tarefas local, desativar firewall ou desligar sensores são ações sem sentido que violam a operação do resort.</li>
</ul></div>
<div class="explanation-tip"><strong>💡 Dica de Prova DP-700:</strong> A fronteira de governança e isolamento de computação (CUs) no Fabric é a <strong>Capacidade (Capacity)</strong>, e não o workspace. Workspaces na mesma capacidade compartilham o mesmo pool de CUs.</div>"""
                }
            ]
        }
    ]


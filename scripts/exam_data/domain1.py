"""
DOMÍNIO 1: IMPLEMENTAR E GERENCIAR UM AMBIENTE ANALÍTICO (15-20%)
38 Questões Completas (26 Single-Choice, 12 Multi-Select)
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

DOMAIN_1_QUESTIONS = [
    # --- SKU & CAPACIDADE (Questões 1 a 6) ---
    {
        "id": "d1_q01",
        "domain": "domain1",
        "type": "single",
        "title": "Dimensionamento de F-SKU e Suporte a Copilot",
        "question": "Sua organização planeja implantar o Microsoft Fabric para atender cargas de trabalho de Data Engineering e utilizar os recursos generativos do Copilot para criação automatizada de pipelines e consultas em Notebooks. Qual é a capacidade mínima (F-SKU) necessária para habilitar os recursos nativos do Copilot no locatário do Fabric?",
        "options": [
            {"id": "A", "text": "F16", "isCorrect": False},
            {"id": "B", "text": "F32", "isCorrect": False},
            {"id": "C", "text": "F64", "isCorrect": True},
            {"id": "D", "text": "F128", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A Microsoft exige no mínimo uma capacidade F64 (ou P1 no Power BI Premium) para habilitar e utilizar os recursos do Copilot no Microsoft Fabric. Capacidades menores que F64 não suportam o consumo de tokens de IA generativa do Copilot.",
            [
                "<strong>A e B (F16 e F32):</strong> Suportam todas as cargas analíticas normais (Spark, Warehouse, Data Factory), mas não atendem ao pré-requisito mínimo oficial para habilitar o Copilot.",
                "<strong>D (F128):</strong> Embora suporte o Copilot, não é o requisito mínimo para ativação."
            ],
            "Guarde a regra: Copilot no Fabric exige no mínimo F64 ou P1. Abaixo disso, o toggle do Copilot nas configurações de locatário permanece desativado ou restrito."
        )
    },
    {
        "id": "d1_q02",
        "domain": "domain1",
        "type": "single",
        "title": "Mecanismo de Smoothing e Janelas de Agregação de CUs",
        "question": "Um engenheiro de dados executou um job Spark de alto processamento que consumiu 1.200 Capacity Unit Seconds (CU-s) durante um pico repentino de 1 minuto em uma capacidade F16. Como o mecanismo de Smoothing (suavização) do Microsoft Fabric gerencia esse consumo para evitar a limitação imediata (throttling)?",
        "options": [
            {"id": "A", "text": "Rejeita imediatamente os jobs seguintes porque o limite do minuto foi ultrapassado.", "isCorrect": False},
            {"id": "B", "text": "Distribui o consumo de jobs interativos em 5 minutos e de jobs em segundo plano (background jobs) em uma janela de 24 horas.", "isCorrect": True},
            {"id": "C", "text": "Converte automaticamente a capacidade F16 para F32 por meio de autoescala elástica instantânea sem intervenção.", "isCorrect": False},
            {"id": "D", "text": "Pausa a capacidade por 15 minutos até que o saldo de CUs seja regenerado no Azure Portal.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O mecanismo de Smoothing calcula médias móveis do consumo de CUs para evitar picos abruptos: operações interativas (consultas SQL interativas, DAX, relatórios) são distribuídas em janelas de 5 minutos, enquanto operações em segundo plano (background jobs como Spark jobs, Data Pipelines e Dataflows) são distribuídas em uma janela móvel de 24 horas.",
            [
                "<strong>A:</strong> O Smoothing existe especificamente para não rejeitar picos repentinos de curto prazo.",
                "<strong>C:</strong> Fabric não altera automaticamente o SKU contratado sem configuração de regras explícitas de automação ou escalabilidade externa.",
                "<strong>D:</strong> A capacidade não é pausada automaticamente pelo motor de smoothing; apenas ocorre throttling em fases se o consumo cumulativo exceder 100% da capacidade ao longo da janela."
            ],
            "No exame DP-700, lembre-se: Background = 24 horas; Interactive = 5 minutos. Isso é questão recorrente de arquitetura de capacidade!"
        )
    },
    {
        "id": "d1_q03",
        "domain": "domain1",
        "type": "single",
        "title": "Estágios de Limitação (Throttling) por Sobrecarga",
        "question": "Uma capacidade F32 esteve em sobrecarga contínua por 48 horas devido a pipelines em loop. Quais são os três estágios progressivos de throttling aplicados pelo Microsoft Fabric nessa ordem de severidade?",
        "options": [
            {"id": "A", "text": "Advertência por E-mail -> Suspensão de Workspaces -> Exclusão de Itens", "isCorrect": False},
            {"id": "B", "text": "Atraso Interativo (Interactive Delay) -> Rejeição Interativa (Interactive Rejection) -> Rejeição Total / Segundo Plano (Background Rejection)", "isCorrect": True},
            {"id": "C", "text": "Desligamento do Spark -> Bloqueio de Leitura no OneLake -> Exclusão da Assinatura Azure", "isCorrect": False},
            {"id": "D", "text": "Redução para F16 -> Descarte de Arquivos Parquet -> Cancelamento de Licença", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric aplica limitação em três etapas sucessivas: 1) Interactive Delay (introduz pequenos atrasos em consultas visuais para desestimular uso excessivo), 2) Interactive Rejection (novas consultas de relatórios e DAX são rejeitadas com erro de capacidade esgotada), 3) Background Rejection (jobs de Spark, Pipelines e ingestão em background passam a falhar totalmente).",
            [
                "<strong>A, C e D:</strong> Itens, arquivos e licenças nunca são excluídos ou suspensos por sobrecarga de capacidade; apenas o processamento computacional é throttled."
            ],
            "Sequência exata do Throttling: Interactive Delay -> Interactive Rejection -> Background Rejection."
        )
    },
    {
        "id": "d1_q04",
        "domain": "domain1",
        "type": "single",
        "title": "Pausa e Retomada de F-SKU no Azure Portal",
        "question": "Um arquiteto de dados deseja reduzir custos de desenvolvimento pausando a capacidade F32 do Fabric durante fins de semana. O que acontece com os dados armazenados no OneLake durante o período em que a capacidade está em estado 'Paused'?",
        "options": [
            {"id": "A", "text": "Os dados são excluídos após 24 horas de inatividade da capacidade.", "isCorrect": False},
            {"id": "B", "text": "Os dados do OneLake continuam preservados com segurança e cobrados apenas pela taxa padrão de armazenamento (Storage CUs/GB), mas as operações computacionais ficam inacessíveis.", "isCorrect": True},
            {"id": "C", "text": "Os dados são automaticamente movidos para uma camada de Archive no Blob Storage e exigem 12 horas para reidratação.", "isCorrect": False},
            {"id": "D", "text": "O acesso a consultas de leitura via SQL Endpoint permanece disponível gratuitamente durante a pausa.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Quando uma capacidade F-SKU é pausada no portal do Azure, o faturamento da capacidade computacional é interrompido. No entanto, o armazenamento do OneLake é desacoplado da computação e continua existindo com segurança, sendo cobrado à taxa padrão de armazenamento por GB. Nenhuma computação (Spark, SQL Endpoint, Pipelines) pode ser executada.",
            [
                "<strong>A:</strong> Os dados nunca são deletados por pausa de capacidade.",
                "<strong>C:</strong> Não há migração para archive nem tempo de reidratação; ao retomar a capacidade, o acesso aos arquivos é imediato.",
                "<strong>D:</strong> O SQL Endpoint depende da capacidade computacional ativa; se a capacidade estiver pausada, nenhuma consulta T-SQL responde."
            ],
            "No Fabric, Storage e Compute são totalmente desacoplados. Pausar a capacidade zera o custo de compute, mas o storage do OneLake continua sendo cobrado normalmente."
        )
    },
    {
        "id": "d1_q05",
        "domain": "domain1",
        "type": "multi",
        "title": "Associação de Workspaces a Múltiplas Capacidades",
        "question": "Você é administrador de um locatário corporativo e precisa organizar ambientes de Desenvolvimento, Teste e Produção. Quais DUAS afirmações sobre a governança de Workspaces e Capacidades no Microsoft Fabric estão corretas? (Selecione 2 alternativas)",
        "options": [
            {"id": "A", "text": "Um único Workspace pode ser associado a múltiplas capacidades Fabric simultaneamente para balancear a carga.", "isCorrect": False},
            {"id": "B", "text": "Um Workspace só pode pertencer a exatamente uma capacidade por vez (ou à capacidade compartilhada de avaliação).", "isCorrect": True},
            {"id": "C", "text": "Uma única capacidade Fabric pode hospedar múltiplos Workspaces até o limite de consumo de suas CUs.", "isCorrect": True},
            {"id": "D", "text": "Ao alterar a capacidade de um workspace, todos os Lakehouses existentes perdem seus arquivos e exigem reindexação.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A relação entre Workspace e Capacidade é de muitos-para-um: cada Workspace só pode estar associado a uma única capacidade em um dado instante, mas uma capacidade pode abrigar dezenas ou centenas de Workspaces. A alteração de capacidade é uma operação puramente lógica de governança e não deleta dados.",
            [
                "<strong>A:</strong> Um workspace não pode ter balanceamento multik-capacidade simultâneo; a atribuição é 1:1.",
                "<strong>D:</strong> Os dados residem no OneLake e são independentes da capacidade atribuída ao workspace."
            ],
            "Regra de relacionamento: 1 Capacidade -> N Workspaces. 1 Workspace -> 1 Capacidade ativa."
        )
    },
    {
        "id": "d1_q06",
        "domain": "domain1",
        "type": "single",
        "title": "Efeito do Burndown e Carry Forward de CUs",
        "question": "Quando um pico de uso excede a capacidade nominal do F-SKU contratado, o Fabric permite o processamento imediato gerando um déficit de CUs acumulado chamado 'Carry Forward'. Como esse débito é amortizado (burndown) pelo sistema?",
        "options": [
            {"id": "A", "text": "O débito é faturado diretamente como custo extraordinário no cartão de crédito do Azure.", "isCorrect": False},
            {"id": "B", "text": "O débito é consumido gradativamente durante períodos subsequentes de menor utilização da capacidade, quando as CUs ficariam ociosas.", "isCorrect": True},
            {"id": "C", "text": "O saldo negativo é perdoado automaticamente à meia-noite em ponto no fuso UTC.", "isCorrect": False},
            {"id": "D", "text": "Exige que o administrador faça um pagamento manual de créditos no Microsoft 365 Admin Center.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O mecanismo de Burndown consome o saldo de Carry Forward acumulado sempre que a capacidade estiver executando cargas de trabalho abaixo de 100% de sua taxa nominal de CUs. O tempo ocioso é usado para pagar o débito sem custos adicionais de licenciamento.",
            [
                "<strong>A e D:</strong> Não há cobrança extra imediata nem recarga manual; o custo da capacidade fixa já cobre a recuperação durante períodos ociosos.",
                "<strong>C:</strong> O débito não expira arbitrariamente à meia-noite; ele persiste na janela móvel de 24 horas até ser amortizado ou atingir o limite de throttling."
            ],
            "Carry Forward = débito gerado pelo burst; Burndown = pagamento do débito durante períodos de folga computacional."
        )
    },

    # --- SEGURANÇA E WORKSPACE RBAC (Questões 7 a 14) ---
    {
        "id": "d1_q07",
        "domain": "domain1",
        "type": "single",
        "title": "Privilégios da Função 'Contributor' em Workspaces Fabric",
        "question": "Qual é a principal restrição aplicada a um usuário com a função de 'Contributor' (Colaborador) em um Workspace do Fabric em comparação com um usuário com a função 'Member' (Membro)?",
        "options": [
            {"id": "A", "text": "Contributors não podem criar nem editar Notebooks e Pipelines de Dados.", "isCorrect": False},
            {"id": "B", "text": "Contributors podem criar, editar e excluir itens do workspace, mas não podem publicar novos apps, atualizar metadados do workspace nem conceder permissões a outros usuários.", "isCorrect": True},
            {"id": "C", "text": "Contributors têm acesso apenas de leitura (Read-Only) em tabelas Delta do Lakehouse.", "isCorrect": False},
            {"id": "D", "text": "Contributors não têm permissão para executar consultas no SQL Analytics Endpoint.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A função Contributor tem plenos direitos de criação, edição e exclusão de artefatos analíticos (Lakehouses, Warehouses, Pipelines, Notebooks), mas não possui permissões administrativas do Workspace: não pode adicionar novos membros, não pode republicar Apps do Power BI e não pode alterar configurações do workspace.",
            [
                "<strong>A:</strong> Contributors podem criar e editar Notebooks e Pipelines normalmente.",
                "<strong>C e D:</strong> Contributors têm permissão de gravação/leitura no workspace e executam consultas normalmente."
            ],
            "Hierarquia de papéis no Workspace Fabric: Admin > Member > Contributor > Viewer. Apenas Admin e Member podem gerenciar permissões e publicar Apps."
        )
    },
    {
        "id": "d1_q08",
        "domain": "domain1",
        "type": "single",
        "title": "Permissões Granulares em Nível de Item: ReadData vs ReadAll",
        "question": "Um engenheiro de dados precisa compartilhar um Lakehouse com uma equipe de analistas para que eles possam ler os dados subjacentes via SQL Endpoint e Power BI, mas sem permitir que eles acessem o lakehouse com permissões de administrador do workspace. Qual permissão granular de item deve ser concedida no Lakehouse?",
        "options": [
            {"id": "A", "text": "Atribuir a função de 'Viewer' no Workspace inteiro.", "isCorrect": False},
            {"id": "B", "text": "Conceder a permissão 'ReadData' (ou ReadAll) especificamente no item Lakehouse compartilhado.", "isCorrect": True},
            {"id": "C", "text": "Criar um token SAS de conta do Azure Storage com acesso de superusuário.", "isCorrect": False},
            {"id": "D", "text": "Adicionar todos os analistas ao grupo de administradores da capacidade F-SKU.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O compartilhamento de itens permite conceder permissões granulares sem dar acesso a todo o workspace. A permissão 'ReadData' permite ao usuário ler o conteúdo dos dados das tabelas gerenciadas e atalhos, enquanto 'ReadAll' permite ler todos os dados no OneLake associados ao item.",
            [
                "<strong>A:</strong> Atribuir Viewer no workspace daria visibilidade a todos os outros artefatos do workspace, violando o princípio do menor privilégio.",
                "<strong>C:</strong> OneLake é gerenciado nativamente pelo Fabric; criar tokens SAS manuais viola a governança nativa e muitas vezes é bloqueado.",
                "<strong>D:</strong> Administrador de capacidade é um privilégio excessivo de infraestrutura."
            ],
            "Para exames: Item Sharing + 'ReadData' / 'ReadAll' é a resposta correta para acesso granular a um único Lakehouse/Warehouse."
        )
    },
    {
        "id": "d1_q09",
        "domain": "domain1",
        "type": "single",
        "title": "OneLake Data Access Roles (ODAR / RBAC Preview)",
        "question": "Qual é a principal vantagem dos OneLake Data Access Roles em comparação com a segurança tradicional de Workspace baseada em Viewer/Contributor?",
        "options": [
            {"id": "A", "text": "Permite definir regras de acesso granulares (RBAC) diretamente em pastas e tabelas específicas dentro do Lakehouse, aplicando-se de forma consistente tanto ao Spark quanto ao SQL Endpoint.", "isCorrect": True},
            {"id": "B", "text": "Permite executar consultas SQL no Lakehouse sem consumir nenhuma Capacity Unit (CU).", "isCorrect": False},
            {"id": "C", "text": "Substitui completamente o Active Directory por autenticação biométrica.", "isCorrect": False},
            {"id": "D", "text": "Permite converter tabelas Delta em arquivos CSV legados em tempo real.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Os OneLake Data Access Roles (ODAR) trazem controle de acesso granular baseado em funções diretamente no nível de armazenamento do OneLake (pastas e tabelas Delta). Isso garante que permissões de segurança sejam respeitadas universalmente, independentemente do motor de computação utilizado (Spark, T-SQL ou API do OneLake).",
            [
                "<strong>B:</strong> ODAR é um mecanismo de segurança e não afeta o faturamento de CUs das consultas.",
                "<strong>C e D:</strong> Afirmações incorretas sem fundamento técnico."
            ],
            "ODAR (OneLake Data Access Roles) = Segurança granular em pastas e tabelas do Lakehouse respeitada por múltiplos motores (Spark, SQL, etc.)."
        )
    },
    {
        "id": "d1_q10",
        "domain": "domain1",
        "type": "single",
        "title": "Row-Level Security (RLS) e o Efeito no Direct Lake",
        "question": "Um arquiteto de BI configurou uma política de Row-Level Security (RLS) usando `CREATE SECURITY POLICY` no SQL Analytics Endpoint de um Lakehouse corporativo. O que acontece quando os usuários corporativos abrem relatórios do Power BI conectados ao Modelo Semântico padrão em modo Direct Lake?",
        "options": [
            {"id": "A", "text": "O relatório carrega com alto desempenho nativo no Direct Lake, ignorando a política de segurança silenciosamente.", "isCorrect": False},
            {"id": "B", "text": "O relatório falha imediatamente com código de erro 403 Forbidden.", "isCorrect": False},
            {"id": "C", "text": "Ocorre um Fallback silencioso para o modo DirectQuery, executando consultas T-SQL contra o SQL Endpoint para cada interação visual.", "isCorrect": True},
            {"id": "D", "text": "O relatório converte o dataset automaticamente para o modo de Importação com agendamento diário.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O modo Direct Lake lê arquivos Parquet diretamente do OneLake para a memória do Analysis Services (VertiPaq) sem passar pelo motor relacional. Quando RLS, CLS ou Data Masking são aplicados no SQL Analytics Endpoint ou Warehouse, o Direct Lake não consegue aplicar a regra no Parquet puro e sofre Fallback para DirectQuery, gerando overhead de consultas T-SQL.",
            [
                "<strong>A:</strong> A segurança nunca é ignorada no Fabric; o motor preserva a restrição forçando DirectQuery.",
                "<strong>B:</strong> O relatório não falha; ele funciona, porém em modo DirectQuery com desempenho inferior.",
                "<strong>D:</strong> O Fabric não altera o modo de armazenamento para Importação sem intervenção manual do usuário."
            ],
            "Conceito chave do DP-700: RLS / CLS no SQL Endpoint força o Direct Lake a fazer Fallback para DirectQuery! Para manter Direct Lake puro com RLS, defina RLS diretamente no Modelo Semântico do Power BI."
        )
    },
    {
        "id": "d1_q11",
        "domain": "domain1",
        "type": "single",
        "title": "Column-Level Security (CLS) e Mascaramento Dinâmico (DDM)",
        "question": "Um engenheiro de dados precisa impedir que a equipe de análise financeira visualize os números de cartões de crédito dos clientes na tabela `FatoVendas` do Warehouse. Os analistas devem poder consultar a tabela, mas o número do cartão deve aparecer como `XXXX-XXXX-XXXX-1234`. Qual recurso nativo do T-SQL no Fabric Warehouse deve ser utilizado?",
        "options": [
            {"id": "A", "text": "Dynamic Data Masking (DDM) com uma função `FUNCTION = 'partial(0, \"XXXX-XXXX-XXXX-\", 4)'` na coluna.", "isCorrect": True},
            {"id": "B", "text": "Triggers `INSTEAD OF SELECT` para reescrever o texto do cartão.", "isCorrect": False},
            {"id": "C", "text": "Uma stored procedure criptografada com certificado assimétrico RSA de 4096 bits.", "isCorrect": False},
            {"id": "D", "text": "Excluir fisicamente a coluna da tabela e salvar em um arquivo CSV local.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric Warehouse suporta Dynamic Data Masking (DDM) em nível de coluna. Ao aplicar `ALTER TABLE FatoVendas ALTER COLUMN NumeroCartao ADD MASKED WITH (FUNCTION = 'partial(0, \"XXXX-XXXX-XXXX-\", 4)')`, usuários sem a permissão `UNMASK` visualizam os dados ofuscados em tempo de consulta sem alterar os dados físicos no OneLake.",
            [
                "<strong>B:</strong> O Fabric Warehouse não suporta Triggers.",
                "<strong>C:</strong> Solução inviável e desnecessária para visualização em tabelas relacionais do Warehouse.",
                "<strong>D:</strong> Viola a integridade e necessidade de negócio."
            ],
            "Dynamic Data Masking (DDM) mascara dados confidenciais para usuários sem privilégio UNMASK, mantendo os dados originais inalterados no armazenamento."
        )
    },
    {
        "id": "d1_q12",
        "domain": "domain1",
        "type": "multi",
        "title": "Causas de Fallback de Direct Lake para DirectQuery",
        "question": "Quais DUAS condições abaixo causam o Fallback automático de um relatório Power BI em modo Direct Lake para DirectQuery no Microsoft Fabric? (Selecione 2 alternativas)",
        "options": [
            {"id": "A", "text": "A consulta do relatório referencia uma Exibição (View) SQL criada no SQL Analytics Endpoint em vez de uma tabela Delta física.", "isCorrect": True},
            {"id": "B", "text": "O tamanho total dos arquivos Parquet da tabela física excede o limite de memória da capacidade F-SKU configurada.", "isCorrect": True},
            {"id": "C", "text": "A tabela Delta foi otimizada com a ordenação V-Order ativada no Spark.", "isCorrect": False},
            {"id": "D", "text": "O Lakehouse está localizado na mesma região geográfica da capacidade Fabric.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Direct Lake lê tabelas Delta Parquet físicas. Se o modelo semântico referenciar Views T-SQL do SQL Endpoint (que exigem computação relacional T-SQL em tempo de execução) ou se o volume de dados da tabela exceder o teto de memória RAM do VertiPaq do F-SKU, o motor executa Fallback para DirectQuery.",
            [
                "<strong>C:</strong> V-Order é altamente recomendado e nativo do Fabric, otimizando o carregamento do Direct Lake; nunca causa fallback.",
                "<strong>D:</strong> Estar na mesma região é o cenário ideal e reduz latência."
            ],
            "Gatilhos de Fallback no Direct Lake: Views SQL, RLS no SQL Endpoint, estouro de memória da capacidade e tipos de dados incompatíveis no Parquet."
        )
    },
    {
        "id": "d1_q13",
        "domain": "domain1",
        "type": "single",
        "title": "Rótulos de Sensibilidade do Microsoft Purview no Fabric",
        "question": "Como os Rótulos de Sensibilidade (Sensitivity Labels) do Microsoft Purview Information Protection se propagam no ecossistema do Microsoft Fabric quando aplicados a um Lakehouse?",
        "options": [
            {"id": "A", "text": "Eles não se propagam e devem ser recriados manualmente em cada relatório e notebook.", "isCorrect": False},
            {"id": "B", "text": "Eles herdam downstream (a jusante) automaticamente para modelos semânticos e relatórios do Power BI criados a partir do Lakehouse.", "isCorrect": True},
            {"id": "C", "text": "Eles exigem a execução manual de um script PowerShell a cada hora.", "isCorrect": False},
            {"id": "D", "text": "Eles bloqueiam qualquer conexão externa proveniente do Azure Databricks.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric possui integração profunda com o Microsoft Purview: rótulos de sensibilidade aplicados a itens upstream (como um Lakehouse ou Warehouse) se propagam automaticamente downstream para os Modelos Semânticos e Relatórios gerados a partir desses dados, garantindo proteção e criptografia de ponta a ponta.",
            [
                "<strong>A e C:</strong> A herança é automática e nativa da plataforma.",
                "<strong>D:</strong> O rótulo governa classificação e direitos digitais, não o bloqueio de rede arbitrário de engines externas."
            ],
            "Purview no Fabric: Suporte a herança downstream automática de rótulos de sensibilidade de Lakehouses -> Semantics Models -> Relatórios."
        )
    },
    {
        "id": "d1_q14",
        "domain": "domain1",
        "type": "single",
        "title": "Identidade de Workspace e Acesso a Recursos Confiáveis do Azure",
        "question": "Você precisa configurar um Data Pipeline no Fabric para acessar um Azure Data Lake Storage Gen2 (ADLS Gen2) protegido por firewall de rede privada (sem acesso público). Qual método de autenticação e rede deve ser utilizado para permitir a conexão segura sem expor chaves de conta nos pipelines?",
        "options": [
            {"id": "A", "text": "Desativar temporariamente o firewall do ADLS Gen2 durante a execução do pipeline.", "isCorrect": False},
            {"id": "B", "text": "Configurar uma Identidade de Workspace (Workspace Identity) no Fabric e habilitar a exceção de serviço confiável (Trusted Microsoft Services) nas regras de rede do ADLS Gen2.", "isCorrect": True},
            {"id": "C", "text": "Gravar a Shared Key do storage em texto puro em um Notebook Python compartilhado.", "isCorrect": False},
            {"id": "D", "text": "Configurar uma VPN ponto a ponto em cada laptop de desenvolvedor conectado ao Fabric.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Microsoft Fabric permite atribuir uma Identidade Gerenciada ao Workspace (Workspace Identity). Combinada com a regra de firewall de 'Trusted Microsoft Services' no ADLS Gen2, o Fabric estabelece comunicação segura pela espinha dorsal da Microsoft sem necessidade de IP público ou chaves estáticas.",
            [
                "<strong>A e C:</strong> Práticas inseguras que violam os requisitos de segurança e compliance.",
                "<strong>D:</strong> A computação do Fabric roda na nuvem gerenciada, não na máquina local do usuário."
            ],
            "Workspace Identity + Trusted Service Access no Azure Storage = Conexão segura sem chaves e com firewall ativado."
        )
    },

    # --- ONELAKE SHORTCUTS E INTEROPERABILIDADE (Questões 15 a 22) ---
    {
        "id": "d1_q15",
        "domain": "domain1",
        "type": "single",
        "title": "Criação de Atalho (Shortcut) para AWS S3",
        "question": "Uma empresa possui um data lake existente no Amazon Web Services S3 contendo tabelas no formato Delta Parquet. A gerência determinou que os analistas devem consultar esses dados no Microsoft Fabric sem duplicar o armazenamento nem incorrer em custos recorrentes de cópia de dados. Qual solução atende a essa exigência?",
        "options": [
            {"id": "A", "text": "Criar um OneLake Shortcut na pasta 'Tables' do Lakehouse apontando para o bucket S3 de origem.", "isCorrect": True},
            {"id": "B", "text": "Criar um Data Pipeline com atividade Copy para baixar os dados do S3 a cada 30 minutos.", "isCorrect": False},
            {"id": "C", "text": "Exportar os dados do S3 em arquivos compactados .ZIP e fazer upload manual via portal do OneLake.", "isCorrect": False},
            {"id": "D", "text": "Migrar todo o bucket S3 para um banco de dados relacional SQL Server em máquina virtual.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Os OneLake Shortcuts criam ponteiros simbólicos no OneLake apontando para fontes externas como AWS S3, ADLS Gen2 ou Google Cloud Storage. Ao criar um atalho na pasta 'Tables' de um Lakehouse, o Fabric trata os arquivos Delta externos como tabelas nativas sem cópia física de dados (Zero-ETL).",
            [
                "<strong>B:</strong> A atividade Copy duplica o armazenamento e gera custos contínuos de egresso e computação.",
                "<strong>C e D:</strong> Soluções inviáveis, manuais e contrárias aos requisitos do exame."
            ],
            "OneLake Shortcuts = Virtualização de dados (Zero-ETL / Zero-Copy) apontando para AWS S3, Google Cloud Storage, Dataverse ou ADLS Gen2."
        )
    },
    {
        "id": "d1_q16",
        "domain": "domain1",
        "type": "single",
        "title": "Diferença Crítica entre Atalhos em 'Tables' vs 'Files'",
        "question": "Ao criar um OneLake Shortcut dentro de um Lakehouse, um engenheiro acidentalmente criou o atalho dentro da pasta `Files/` em vez de `Tables/`. Qual é o impacto direto dessa ação nas consultas analíticas?",
        "options": [
            {"id": "A", "text": "O atalho não funciona e retorna erro de rede na AWS.", "isCorrect": False},
            {"id": "B", "text": "Os dados ficam acessíveis via Notebook Spark por caminhos de arquivo, mas a tabela Delta não é registrada no catálogo Metastore nem exposta no SQL Analytics Endpoint automaticamente.", "isCorrect": True},
            {"id": "C", "text": "O Lakehouse inteiro é corrompido e deve ser excluído.", "isCorrect": False},
            {"id": "D", "text": "O SQL Endpoint converte automaticamente os arquivos em tabelas temporárias na memória RAM.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "No Lakehouse do Fabric: a pasta `Tables/` contém dados gerenciados ou atalhos Delta que são registrados automaticamente no catálogo metastore e expostos como tabelas relacionais no SQL Analytics Endpoint. A pasta `Files/` contém arquivos brutos (não estruturados ou semiestruturados) que podem ser lidos por Spark/Notebooks, mas não aparecem como tabelas no SQL Endpoint.",
            [
                "<strong>A e C:</strong> O atalho funciona perfeitamente para leitura de arquivos, não ocorre corrupção nem erro.",
                "<strong>D:</strong> O SQL Endpoint não converte automaticamente arquivos soltos da pasta `Files/`."
            ],
            "Regra de ouro do Lakehouse: `Tables/` = Tabelas no Catálogo + SQL Endpoint. `Files/` = Arquivos brutos apenas para Notebooks/Spark."
        )
    },
    {
        "id": "d1_q17",
        "domain": "domain1",
        "type": "multi",
        "title": "Provedores de Nuvem Suportados Nativamente por OneLake Shortcuts",
        "question": "Quais DUAS fontes de nuvem externas possuem suporte oficial direto para criação de OneLake Shortcuts nativos no Microsoft Fabric? (Selecione 2 alternativas)",
        "options": [
            {"id": "A", "text": "Amazon Web Services (AWS) S3", "isCorrect": True},
            {"id": "B", "text": "Google Cloud Storage (GCS)", "isCorrect": True},
            {"id": "C", "text": "Oracle Cloud Infrastructure (OCI) Object Storage nativo sem S3-compatibility", "isCorrect": False},
            {"id": "D", "text": "Alibaba Cloud OSS nativo sem conectores", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Microsoft Fabric suporta nativamente OneLake Shortcuts para: 1) OneLake (atalhos internos entre lakehouses e workspaces), 2) Azure Data Lake Storage Gen2 (ADLS Gen2), 3) Amazon S3, 4) Google Cloud Storage (GCS) e 5) Microsoft Dataverse (via Fabric Link).",
            [
                "<strong>C e D:</strong> Provedores sem conectores nativos de atalho direto no OneLake."
            ],
            "Provedores oficiais de Shortcuts externos no DP-700: ADLS Gen2, AWS S3, Google Cloud Storage (GCS) e Dataverse."
        )
    },
    {
        "id": "d1_q18",
        "domain": "domain1",
        "type": "single",
        "title": "Dataverse Link para Microsoft Fabric",
        "question": "Uma organização utiliza o Microsoft Dynamics 365 e deseja disponibilizar todas as entidades do Dataverse no Microsoft Fabric sem pipelines de extração diários. Como o recurso Microsoft Dataverse Link para Fabric viabiliza essa integração?",
        "options": [
            {"id": "A", "text": "Executa uma exportação diária em formato BCP para um servidor FTP.", "isCorrect": False},
            {"id": "B", "text": "Sincroniza continuamente as tabelas do Dataverse em formato Delta Parquet gerenciado, disponibilizando-as automaticamente no OneLake via atalhos sem pipelines ETL.", "isCorrect": True},
            {"id": "C", "text": "Obriga o uso de uma gateway local instalada em cada estação de trabalho.", "isCorrect": False},
            {"id": "D", "text": "Converte todas as tabelas em bancos de dados Access locais.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Dataverse Link para Microsoft Fabric utiliza a tecnologia Synapse Link integrada ao OneLake. O Dataverse escreve e atualiza os dados diretamente em formato Delta Parquet no OneLake, disponibilizando atalhos automáticos no Workspace do Fabric sem a necessidade de criar pipelines manuais de extração.",
            [
                "<strong>A, C e D:</strong> Métodos legados que não utilizam a integração nativa SaaS do Fabric Link."
            ],
            "Dataverse Link = Zero-ETL para Dynamics 365 e Power Apps direto no OneLake em formato Delta Parquet."
        )
    },
    {
        "id": "d1_q19",
        "domain": "domain1",
        "type": "single",
        "title": "Autenticação em Atalhos do Google Cloud Storage (GCS)",
        "question": "Ao criar um OneLake Shortcut apontando para um bucket no Google Cloud Storage (GCS), qual credencial de segurança é exigida para autorizar a conexão entre o Fabric e o GCS?",
        "options": [
            {"id": "A", "text": "Uma chave de API (API Key) do Google Maps.", "isCorrect": False},
            {"id": "B", "text": "Chave de Conta de Serviço (GCS HMAC Key / Access Key ID e Secret Access Key) ou credencial federada configurada no GCP.", "isCorrect": True},
            {"id": "C", "text": "A senha pessoal de login do Gmail de um engenheiro de dados.", "isCorrect": False},
            {"id": "D", "text": "Um certificado SSL autoassinado gerado no Windows Notepad.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Para conectar o OneLake Shortcut ao Google Cloud Storage, o Fabric utiliza a API compatível com S3 do Google Cloud, exigindo um par de chaves HMAC (Access Key ID e Secret Access Key) gerado para uma Conta de Serviço (Service Account) no Google Cloud Console com permissões de leitura no bucket.",
            [
                "<strong>A, C e D:</strong> Credenciais inválidas e sem aderência aos padrões de segurança em nuvem."
            ],
            "Shortcuts GCS utilizam HMAC Keys geradas no Google Cloud Storage Console para autenticação segura."
        )
    },
    {
        "id": "d1_q20",
        "domain": "domain1",
        "type": "single",
        "title": "Comportamento de Exclusão em Atalhos (Delete Shortcut vs Delete Data)",
        "question": "Um usuário com papel de Contributor acessa a interface web do Lakehouse e clica com o botão direito em uma pasta de atalho (Shortcut) do AWS S3 e seleciona 'Delete'. O que acontece com os arquivos originais localizados no bucket S3 da AWS?",
        "options": [
            {"id": "A", "text": "Todos os arquivos do bucket S3 da AWS são permanentemente excluídos.", "isCorrect": False},
            {"id": "B", "text": "Apenas o atalho (ponteiro lógico) no OneLake é removido; os dados físicos no bucket S3 da AWS permanecem totalmente intactos.", "isCorrect": True},
            {"id": "C", "text": "O bucket S3 entra em estado de bloqueio e exige chamado na AWS para liberação.", "isCorrect": False},
            {"id": "D", "text": "Os dados são movidos para a lixeira do Windows do usuário.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "A exclusão de um atalho (Shortcut) no Fabric remove apenas o link simbólico nos metadados do OneLake. O Fabric nunca emite comandos de exclusão na fonte externa (AWS S3, ADLS Gen2 ou GCS) durante a deleção do atalho.",
            [
                "<strong>A:</strong> Os atalhos são ponteiros de virtualização; deletar o ponteiro não deleta a origem.",
                "<strong>C e D:</strong> Afirmações incorretas sem sentido técnico."
            ],
            "Cuidado em prova: Deletar um Shortcut NÃO deleta os dados na origem externa (S3, ADLS, GCS)."
        )
    },
    {
        "id": "d1_q21",
        "domain": "domain1",
        "type": "single",
        "title": "OneLake File Explorer no Windows",
        "question": "Qual é a principal função da ferramenta cliente 'OneLake File Explorer' para Windows no fluxo de trabalho de engenharia de dados?",
        "options": [
            {"id": "A", "text": "Compilar código Scala em arquivos executáveis para o Apache Spark.", "isCorrect": False},
            {"id": "B", "text": "Sincronizar e mapear os workspaces e lakehouses do OneLake diretamente no Windows Explorer como se fossem pastas locais, facilitando upload e download rápido de arquivos.", "isCorrect": True},
            {"id": "C", "text": "Executar consultas SQL no Warehouse sem conexão com a internet.", "isCorrect": False},
            {"id": "D", "text": "Substituir o Azure Portal na gestão de cobrança de cartões de crédito.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O OneLake File Explorer integra o OneLake nativamente ao Windows File Explorer (semelhante ao cliente OneDrive), permitindo que desenvolvedores naveguem por workspaces, lakehouses e pastas, arrastando e soltando arquivos diretamente para o OneLake sem precisar de scripts de upload.",
            [
                "<strong>A, C e D:</strong> Funções não relacionadas ao OneLake File Explorer."
            ],
            "OneLake File Explorer = Cliente desktop para sincronização de arquivos e pastas no Windows Explorer."
        )
    },
    {
        "id": "d1_q22",
        "domain": "domain1",
        "type": "single",
        "title": "Shortcuts Internos entre Workspaces e Segurança",
        "question": "O Workspace 'Engenharia_Dados' possui um Lakehouse com tabelas limpas. O Workspace 'Vendas_Analise' precisa ler uma dessas tabelas via OneLake Shortcut interno. Como o Fabric valida as permissões quando um usuário do Workspace 'Vendas_Analise' consulta o atalho?",
        "options": [
            {"id": "A", "text": "O usuário precisa ter pelo menos permissão de leitura ('Read' ou 'ReadData') no Lakehouse de origem do Workspace 'Engenharia_Dados'.", "isCorrect": True},
            {"id": "B", "text": "Qualquer usuário pode ler qualquer atalho interno sem nenhuma permissão no workspace de origem.", "isCorrect": False},
            {"id": "C", "text": "O workspace de destino deve pagar uma taxa de licenciamento duplicada à Microsoft.", "isCorrect": False},
            {"id": "D", "text": "O atalho interno requer autenticação por Kerberos local.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Em atalhos internos do OneLake entre workspaces, a segurança é delegada: o usuário que executa a consulta através do atalho precisa ter permissões de acesso aos dados ('ReadData') no item de origem subjacente. Sem isso, a consulta falha por acesso negado.",
            [
                "<strong>B:</strong> Violaria totalmente os princípios de governança e isolamento de dados corporativos.",
                "<strong>C e D:</strong> Inexistentes no modelo de governança do OneLake."
            ],
            "Shortcuts internos respeitam as permissões do item de origem: o consumidor precisa ter acesso concedido no item original."
        )
    },

    # --- CI/CD, GIT INTEGRATION E DEPLOYMENT PIPELINES (Questões 23 a 30) ---
    {
        "id": "d1_q23",
        "domain": "domain1",
        "type": "single",
        "title": "Provedores de Git Suportados Nativamente na Integração do Fabric",
        "question": "Quais são os dois sistemas de controle de versão em nuvem que possuem suporte oficial nativo para integração direta com Workspaces do Microsoft Fabric?",
        "options": [
            {"id": "A", "text": "Azure DevOps Repos (Git) e GitHub", "isCorrect": True},
            {"id": "B", "text": "GitLab Self-Hosted e Bitbucket Cloud", "isCorrect": False},
            {"id": "C", "text": "Subversion (SVN) e Mercurial", "isCorrect": False},
            {"id": "D", "text": "AWS CodeCommit e SourceForge", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Microsoft Fabric oferece suporte nativo à integração Git para Azure DevOps Repos e GitHub. Permite sincronizar metadados de itens do workspace bidirecionalmente com branches de repositórios Git.",
            [
                "<strong>B, C e D:</strong> Não possuem integração nativa de sincronização direta na interface de administração do Fabric."
            ],
            "Git no Fabric: Azure DevOps Repos e GitHub são os dois provedores suportados nativamente."
        )
    },
    {
        "id": "d1_q24",
        "domain": "domain1",
        "type": "single",
        "title": "Arquivos de Metadados `.platform` na Integração Git",
        "question": "Ao sincronizar um Workspace do Fabric com um repositório Git, uma pasta é criada para cada item, contendo um arquivo chamado `.platform`. Qual é a finalidade desse arquivo?",
        "options": [
            {"id": "A", "text": "Armazenar uma cópia compactada de todos os dados Parquet das tabelas.", "isCorrect": False},
            {"id": "B", "text": "Conter as configurações e metadados de infraestrutura do item do Fabric (como tipo de item, id de exibição e vínculos lógicos) necessários para o Fabric reconstruir o artefato.", "isCorrect": True},
            {"id": "C", "text": "Guardar as senhas e chaves de acesso dos desenvolvedores em formato Base64.", "isCorrect": False},
            {"id": "D", "text": "Instalar o compilador Java no Azure DevOps durante o build.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O arquivo `.platform` é gerado automaticamente pelo Fabric em cada pasta de item rastreado pelo Git. Ele contém metadados de plataforma essenciais (identificador do tipo de item, schema version e propriedades de integração) para que o serviço do Fabric reconheça o diretório como um artefato gerenciado.",
            [
                "<strong>A:</strong> O Git armazena apenas definições e metadados de código, nunca dados físicos de tabelas.",
                "<strong>C:</strong> Credenciais e segredos nunca são salvos em arquivos `.platform` no Git.",
                "<strong>D:</strong> Não tem relação com o compilador Java."
            ],
            "Arquivo `.platform` = Metadados de plataforma essenciais para o Fabric rastrear e instanciar o item a partir do repositório Git."
        )
    },
    {
        "id": "d1_q25",
        "domain": "domain1",
        "type": "multi",
        "title": "Itens do Fabric com Suporte Oficial a Git Integration",
        "question": "Quais DUAS classes de itens analíticos do Microsoft Fabric possuem suporte nativo à sincronização e versionamento via Git Integration? (Selecione 2 alternativas)",
        "options": [
            {"id": "A", "text": "Notebooks Spark", "isCorrect": True},
            {"id": "B", "text": "Pipelines de Dados (Data Pipelines)", "isCorrect": True},
            {"id": "C", "text": "Conjuntos de dados de streaming legado (Legacy Push Datasets)", "isCorrect": False},
            {"id": "D", "text": "Arquivos de backup físico do SQL Server (.BAK)", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric expandiu o suporte ao Git para incluir: Notebooks, Data Pipelines, Lakehouses (metadados), Warehouses (definições DDL), Modelos Semânticos (TMDL/BIM), Relatórios (PBIR), Ambientes (Environments) e Eventstreams.",
            [
                "<strong>C e D:</strong> Não são itens modernos compatíveis com o ciclo de vida DevOps do Fabric."
            ],
            "Itens suportados no Git do Fabric: Notebooks, Data Pipelines, Warehouses, Lakehouses, Semantic Models, Reports e Environments."
        )
    },
    {
        "id": "d1_q26",
        "domain": "domain1",
        "type": "single",
        "title": "Regras de Implantação (Deployment Rules) em Pipelines de Implantação",
        "question": "Ao utilizar os Deployment Pipelines do Fabric para promover itens do estágio de 'Desenvolvimento' para 'Produção', como um engenheiro de dados garante que os relatórios em Produção apontem para o Lakehouse de Produção sem precisar editar o código manualmente?",
        "options": [
            {"id": "A", "text": "Criar regras de implantação de parâmetros ou fontes de dados (Deployment Rules) no estágio de destino.", "isCorrect": True},
            {"id": "B", "text": "Editar manualmente o script SQL em produção após cada implantação.", "isCorrect": False},
            {"id": "C", "text": "Renomear o Lakehouse de produção para ter o mesmo identificador GUID de desenvolvimento.", "isCorrect": False},
            {"id": "D", "text": "Desativar a segurança em desenvolvimento para que produção acesse a mesma base.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Os Deployment Pipelines do Fabric oferecem o recurso 'Deployment Rules' (Regras de Implantação). Elas permitem substituir automaticamente parâmetros ou mapeamentos de fontes de dados (como apontar de `Lakehouse_Dev` para `Lakehouse_Prod`) sempre que um artefato é implantado no estágio superior.",
            [
                "<strong>B:</strong> A edição manual em produção viola as práticas de DevOps e gera risco de downtime e erro humano.",
                "<strong>C:</strong> GUIDs são imutáveis e exclusivos no Fabric.",
                "<strong>D:</strong> Misturar ambientes e desativar segurança viola regras básicas de governança."
            ],
            "Deployment Rules = Mapeamento automático de fontes de dados e parâmetros entre estágios de Dev, Test e Prod."
        )
    },
    {
        "id": "d1_q27",
        "domain": "domain1",
        "type": "single",
        "title": "Projetos de Banco de Dados SQL (`.sqlproj`) para Fabric Warehouse",
        "question": "Uma equipe de desenvolvedores SQL quer adotar uma abordagem 'State-First' baseada em código para gerenciar o esquema do Fabric Warehouse no Visual Studio Code e no Azure DevOps. Qual tecnologia padrão deve ser utilizada para compilar e implantar o esquema via CI/CD?",
        "options": [
            {"id": "A", "text": "Projetos de Banco de Dados SQL (extensão SQL Database Projects / `.sqlproj` com DacFx) direcionados ao Microsoft Fabric Warehouse.", "isCorrect": True},
            {"id": "B", "text": "Scripts manuais em arquivos `.bat` no Prompt de Comando.", "isCorrect": False},
            {"id": "C", "text": "Exportação periódica de arquivos `.xlsx` com a lista de tabelas.", "isCorrect": False},
            {"id": "D", "text": "Execução de comandos `DUMP DATABASE` não documentados.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Microsoft Fabric Warehouse suporta projetos de banco de dados SQL (`.sqlproj`) através da extensão SQL Database Projects no VS Code ou Azure Data Studio. Isso permite versionar o DDL de tabelas, views e procedures, gerando arquivos `.dacpac` compilados para automação de CI/CD.",
            [
                "<strong>B, C e D:</strong> Métodos manuais ou não suportados para governança corporativa de banco de dados."
            ],
            "Fabric Warehouse CI/CD = SQL Database Projects (`.sqlproj`) + Dacpac para desenvolvimento state-first."
        )
    },
    {
        "id": "d1_q28",
        "domain": "domain1",
        "type": "single",
        "title": "Backward Deployment em Pipelines de Implantação",
        "question": "Um desenvolvedor fez uma alteração emergencial diretamente no Workspace do estágio de 'Teste' de um Deployment Pipeline e precisa sincronizar essa alteração de volta para o estágio de 'Desenvolvimento'. Esse procedimento é suportado pelo Fabric?",
        "options": [
            {"id": "A", "text": "Não, os pipelines do Fabric só permitem implantações estritamente para a frente (Dev -> Test -> Prod).", "isCorrect": False},
            {"id": "B", "text": "Sim, o Fabric suporta 'Backward Deployment' (implantação retroativa) entre estágios vizinhos (por exemplo, de Teste para Desenvolvimento).", "isCorrect": True},
            {"id": "C", "text": "Sim, mas exige a exclusão do workspace de desenvolvimento.", "isCorrect": False},
            {"id": "D", "text": "Apenas se a capacidade for maior que F512.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Os Deployment Pipelines do Fabric suportam implantação retroativa (Backward Deployment). Se for realizada uma alteração em um estágio posterior (como Teste), o administrador pode implantar a versão de volta para o estágio anterior (Desenvolvimento), garantindo sincronismo entre ambientes.",
            [
                "<strong>A:</strong> Ao contrário de ferramentas legadas unidirecionais, o Fabric suporta backward deployment explicitamente.",
                "<strong>C e D:</strong> Não há destruição de workspaces nem exigência de SKUs de grande porte."
            ],
            "Recurso oficial do Fabric: Backward deployment permite sincronizar alterações de Teste de volta para Desenvolvimento."
        )
    },
    {
        "id": "d1_q29",
        "domain": "domain1",
        "type": "single",
        "title": "Resolução de Conflitos na Sincronização Git do Fabric",
        "question": "Ao tentar sincronizar as alterações de uma branch Git para o Workspace do Fabric, a interface indica um conflito de versão ('Conflict Detected'). Qual é a ação padrão recomendada na interface do Fabric para resolver o conflito?",
        "options": [
            {"id": "A", "text": "O usuário deve escolher entre sobrescrever o workspace com o conteúdo do Git ('Accept incoming / Git') ou atualizar o Git com o conteúdo atual do workspace ('Keep local / Workspace').", "isCorrect": True},
            {"id": "B", "text": "O Fabric exclui imediatamente o repositório Git para evitar inconsistências.", "isCorrect": False},
            {"id": "C", "text": "A capacidade F-SKU é colocada em quarentena por 24 horas.", "isCorrect": False},
            {"id": "D", "text": "O conflito só pode ser resolvido com uma chamada de suporte à Microsoft.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Quando ocorrem alterações concorrentes no Git e no Workspace do Fabric, a interface de controle de código detecta o conflito e exige que o desenvolvedor resolva selecionando explicitamente se deseja aceitar os itens do Git (sobrescrevendo o workspace) ou manter os itens do workspace (gerando commit no Git).",
            [
                "<strong>B, C e D:</strong> Falsos alarmes que não correspondem ao fluxo de controle de versão do Fabric."
            ],
            "Conflito no Git do Fabric: Escolha explícita entre 'Accept Git' ou 'Keep Workspace'."
        )
    },
    {
        "id": "d1_q30",
        "domain": "domain1",
        "type": "multi",
        "title": "Artefatos NÃO Suportados por Deployment Pipelines",
        "question": "Embora os Deployment Pipelines suportem a maioria dos artefatos do Fabric, alguns itens possuem restrições ou exigem gestão diferenciada. Quais DOIS itens abaixo possuem limitações ou não são promovidos da mesma forma que relatórios e modelos semânticos padrão? (Selecione 2 alternativas)",
        "options": [
            {"id": "A", "text": "Dados físicos reais de tabelas armazenados no Lakehouse (apenas o esquema/metadados e atalhos são gerenciados no pipeline de ciclo de vida).", "isCorrect": True},
            {"id": "B", "text": "Conexões locais de Gateway de Dados Pessoal (Personal Gateway)", "isCorrect": True},
            {"id": "C", "text": "Modelos Semânticos do Power BI", "isCorrect": False},
            {"id": "D", "text": "Relatórios Paginados e Relatórios Power BI", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Pipelines de implantação gerenciam definições e metadados de código analítico. Dados físicos reais em tabelas Delta do Lakehouse nunca são copiados entre ambientes de Dev e Prod pelo Deployment Pipeline (os dados pertencem ao armazenamento do estágio). Gateways de dados pessoais também não são gerenciáveis em pipelines corporativos.",
            [
                "<strong>C e D:</strong> Modelos Semânticos e Relatórios são 100% suportados por Deployment Pipelines desde a versão inicial."
            ],
            "Deployment Pipelines promovem METADADOS e CÓDIGO, não dados de tabelas físicas!"
        )
    },

    # --- GOVERNANÇA, DOMÍNIOS E DESCOBERTA (Questões 31 a 38) ---
    {
        "id": "d1_q31",
        "domain": "domain1",
        "type": "single",
        "title": "Conceito de 'Domínios' (Fabric Domains) e Arquitetura Data Mesh",
        "question": "Uma corporação multinacional deseja implementar uma arquitetura Data Mesh descentralizada no Microsoft Fabric, agrupando workspaces por unidades de negócio (ex: 'Finanças', 'Vendas', 'Operações') e delegando a administração aos responsáveis de negócio. Qual recurso nativo do Fabric atende a essa governança?",
        "options": [
            {"id": "A", "text": "Domínios do Fabric (Fabric Domains)", "isCorrect": True},
            {"id": "B", "text": "Grupos de distribuição de e-mail do Microsoft Exchange", "isCorrect": False},
            {"id": "C", "text": "Pastas compartilhadas no OneDrive comercial", "isCorrect": False},
            {"id": "D", "text": "Políticas de bloqueio de IP no Azure Active Directory", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Os Domínios do Fabric (Fabric Domains) foram criados especificamente para viabilizar arquiteturas Data Mesh. Eles permitem agrupar múltiplos Workspaces sob um domínio lógico de negócio (ex: Marketing, RH), permitindo que administradores de domínio definam proprietários, aprovem certificações de itens e gerenciem permissões de forma descentralizada.",
            [
                "<strong>B, C e D:</strong> Não têm relação com o agrupamento lógico de workspaces analíticos no Fabric."
            ],
            "Data Mesh no Fabric = Fabric Domains. Agrupa workspaces por área de negócio com administradores de domínio dedicados."
        )
    },
    {
        "id": "d1_q32",
        "domain": "domain1",
        "type": "single",
        "title": "Certificação vs Promoção de Itens no OneLake Data Hub",
        "question": "No OneLake Data Hub, usuários corporativos precisam distinguir dados validados oficialmente pela equipe corporativa de dados de artefatos criados livremente por usuários para estudos rápidos. Quais são os dois níveis de endosso (Endorsement) disponíveis no Fabric e qual deles exige permissões administrativas para atribuição?",
        "options": [
            {"id": "A", "text": "'Promovido' (Promoted - acessível a autores) e 'Certificado' (Certified - requer permissão explícita concedida pelo administrador do locatário).", "isCorrect": True},
            {"id": "B", "text": "'Bronze' e 'Ouro', ambos atribuíveis por qualquer usuário Viewer.", "isCorrect": False},
            {"id": "C", "text": "'Público' e 'Confidencial', controlados pelo firewall do Windows.", "isCorrect": False},
            {"id": "D", "text": "'Aprovado' e 'Rejeitado', definidos automaticamente pelo antivírus.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric possui dois níveis de Endorsement: 1) Promoted: qualquer proprietário do item pode promover para destacar o artefato na organização; 2) Certified: o mais alto selo de confiança institucional, cuja permissão de aplicação é estritamente restrita a usuários autorizados configurados pelo Administrador de Locatário (Tenant Admin).",
            [
                "<strong>B:</strong> Bronze e Ouro são camadas de arquitetura Medallion, não status de endosso de catálogo.",
                "<strong>C e D:</strong> Conceitos inexistentes no catálogo do OneLake Data Hub."
            ],
            "Níveis de Endosso: Promoted (livre para donos do item) e Certified (exige autorização do Tenant Admin)."
        )
    },
    {
        "id": "d1_q33",
        "domain": "domain1",
        "type": "single",
        "title": "OneLake Data Hub como Ponto Central de Descoberta",
        "question": "Um cientista de dados precisa encontrar todos os dados de vendas disponíveis na organização para treinar um modelo de machine learning, sem saber em quais workspaces esses dados residem. Onde ele deve pesquisar no portal do Microsoft Fabric?",
        "options": [
            {"id": "A", "text": "No OneLake Data Hub, filtrando por tipo de item, endosso (Certified) ou domínio de negócio.", "isCorrect": True},
            {"id": "B", "text": "Abrindo todos os arquivos `.json` da pasta `_delta_log` no Notepad.", "isCorrect": False},
            {"id": "C", "text": "Verificando as tabelas temporárias na instância local do SQL Express.", "isCorrect": False},
            {"id": "D", "text": "Enviando um e-mail em massa para toda a empresa solicitando planilhas.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O OneLake Data Hub é o catálogo unificado de descoberta de dados do Fabric. Ele exibe todos os Lakehouses, Warehouses e Modelos Semânticos aos quais o usuário tem acesso ou que foram promovidos/certificados em qualquer workspace, permitindo filtragem por domínio, proprietário e rótulos de sensibilidade.",
            [
                "<strong>B, C e D:</strong> Práticas antiquadas que desconsideram o catálogo corporativo nativo do Fabric."
            ],
            "OneLake Data Hub = Catálogo central de descoberta de dados e governança no Fabric."
        )
    },
    {
        "id": "d1_q34",
        "domain": "domain1",
        "type": "multi",
        "title": "Configurações de Locatário (Tenant Settings) Críticas para Governança",
        "question": "Quais DUAS configurações de locatário (Tenant Settings) no portal de administração do Fabric devem ser restringidas para garantir que dados corporativos não sejam exportados externamente sem controle? (Selecione 2 alternativas)",
        "options": [
            {"id": "A", "text": "Exportação de dados para arquivos Excel ou CSV (`Export data to Excel`)", "isCorrect": True},
            {"id": "B", "text": "Publicar na Web aberta sem autenticação (`Publish to web (public)`)", "isCorrect": True},
            {"id": "C", "text": "Ativar o tema escuro na interface web do Fabric", "isCorrect": False},
            {"id": "D", "text": "Visualizar relatórios na tela do monitor do usuário", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Para evitar vazamento ou exfiltração de dados sensíveis, administradores de governança devem restringir: 1) 'Publish to web' (que cria links públicos anônimos na internet aberta sem credenciais) e 2) 'Export data to Excel / CSV' (que permite download local de tabelas analíticas).",
            [
                "<strong>C e D:</strong> Opções de interface e consumo básico que não apresentam risco de vazamento de dados."
            ],
            "Governança de dados no Admin Portal: Desativar 'Publish to web' e restringir 'Export to Excel' para grupos de segurança específicos."
        )
    },
    {
        "id": "d1_q35",
        "domain": "domain1",
        "type": "single",
        "title": "Subdomínios (Subdomains) no Fabric",
        "question": "Uma organização já estruturou o Domínio principal de 'Finanças'. Dentro de Finanças, existem equipes com necessidades distintas de governança: 'Contabilidade' e 'Planejamento Tributário'. Como o Fabric permite representar essa hierarquia dentro da governança de domínios?",
        "options": [
            {"id": "A", "text": "Criando Subdomínios (Subdomains) subordinados ao domínio Finanças, herdando políticas e permitindo delegar administradores locais.", "isCorrect": True},
            {"id": "B", "text": "Criando assinaturas separadas do Azure para cada departamento.", "isCorrect": False},
            {"id": "C", "text": "Instalando instâncias diferentes do Windows Server na nuvem.", "isCorrect": False},
            {"id": "D", "text": "O Fabric não suporta níveis hierárquicos dentro de domínios.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O Fabric suporta Subdomínios (Subdomains). Um domínio pai pode conter subdomínios filhos para refletir a estrutura organizacional interna de uma diretoria, herdando a governança superior e permitindo administradores dedicados em cada subdivisão.",
            [
                "<strong>B, C e D:</strong> Incorretos; subdomínios são nativamente suportados na governança do Fabric."
            ],
            "Subdomínios permitem modelar estruturas corporativas complexas (ex: Finanças -> Contabilidade e Controladoria)."
        )
    },
    {
        "id": "d1_q36",
        "domain": "domain1",
        "type": "single",
        "title": "Auditoria de Atividades com Unified Audit Logs do Microsoft 365 / Purview",
        "question": "Um auditor de segurança precisa inspecionar quem executou comandos de exclusão ou alteração de permissões em um Lakehouse crítico nos últimos 30 dias. Onde essas atividades administrativas do Fabric são registradas centralizadamente?",
        "options": [
            {"id": "A", "text": "No Microsoft Purview Audit (Logs Unificados de Auditoria do Microsoft 365 / Fabric Activity Events API).", "isCorrect": True},
            {"id": "B", "text": "No arquivo `c:\\windows\\system32\\drivers\\etc\\hosts` dos analistas.", "isCorrect": False},
            {"id": "C", "text": "Na tabela temporária de log do SQL Server 2008.", "isCorrect": False},
            {"id": "D", "text": "No histórico do navegador Google Chrome do desenvolvedor.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "Todas as ações do Microsoft Fabric (criação, edição, exclusão de itens, execução de consultas, exportações e alterações de permissões) são registradas nos Logs Unificados de Auditoria do Microsoft Purview / Microsoft 365 e podem ser consultadas via portal de conformidade ou pela API Fabric Activity Events.",
            [
                "<strong>B, C e D:</strong> Locais locais e sem relação com a governança corporativa em nuvem."
            ],
            "Auditoria do Fabric = Microsoft Purview Unified Audit Log e Fabric Activity Events REST API."
        )
    },
    {
        "id": "d1_q37",
        "domain": "domain1",
        "type": "single",
        "title": "Prevenção contra Perda de Dados (DLP) para Fabric",
        "question": "Como as Políticas de Prevenção contra Perda de Dados (DLP Policies) do Microsoft Purview protegem dados confidenciais (ex: números de previdência social, cartões de crédito) dentro do Microsoft Fabric?",
        "options": [
            {"id": "A", "text": "Detectam automaticamente informações confidenciais em Lakehouses e modelos semânticos, gerando alertas no portal de segurança e bloqueando o compartilhamento não autorizado.", "isCorrect": True},
            {"id": "B", "text": "Deletam o Lakehouse automaticamente se encontrarem qualquer número de CPF.", "isCorrect": False},
            {"id": "C", "text": "Desconectam os servidores da Microsoft da rede elétrica mundial.", "isCorrect": False},
            {"id": "D", "text": "Formatam o disco rígido do computador do usuário que fez o upload.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "As políticas de DLP do Microsoft Purview examinam os metadados e conteúdos do Fabric para identificar tipos de informações confidenciais (SITs). Ao detectar violações, a política aplica ações como dicas de política (Policy Tips), alertas de compliance e restrições de compartilhamento externo.",
            [
                "<strong>B, C e D:</strong> Efeitos destrutivos e absurdos."
            ],
            "DLP no Fabric = Detecção automática de dados confidenciais (PII, PCI) com alertas de conformidade e restrições de compartilhamento."
        )
    },
    {
        "id": "d1_q38",
        "domain": "domain1",
        "type": "single",
        "title": "Regra de Resiliência de Armazenamento e BCDR no OneLake",
        "question": "O OneLake armazena dados em múltiplos datacenters para garantir durabilidade e alta disponibilidade contra desastres geográficos. Qual é a configuração padrão de redundância de armazenamento subjacente utilizada pelo OneLake nas regiões primárias do Azure?",
        "options": [
            {"id": "A", "text": "LRS (Locally Redundant Storage) ou ZRS (Zone-Redundant Storage) com suporte a failover geográfico de capacidade de acordo com a região.", "isCorrect": True},
            {"id": "B", "text": "Um único disco rígido magnético conectado via cabo USB 2.0 em um rack em Redmond.", "isCorrect": False},
            {"id": "C", "text": "Fita magnética LTO-4 sem backup secundário.", "isCorrect": False},
            {"id": "D", "text": "Memória volátil que é zerada a cada reinicialização semanal do cluster.", "isCorrect": False}
        ],
        "explanation": make_explanation(
            "O OneLake é construído sobre a infraestrutura do Azure Data Lake Storage Gen2 (ADLS Gen2), oferecendo redundância de nível corporativo (LRS ou ZRS com 3 cópias em zonas de disponibilidade separadas) e integração com estratégias de BCDR (Business Continuity & Disaster Recovery).",
            [
                "<strong>B, C e D:</strong> Descrições sem qualquer fundamento técnico."
            ],
            "OneLake BCDR = Infraestrutura de armazenamento baseada em ADLS Gen2 com replicação por zonas (ZRS/LRS) e alta disponibilidade."
        )
    }
]

def get_domain1_questions():
    return DOMAIN_1_QUESTIONS

if __name__ == "__main__":
    qs = get_domain1_questions()
    print(f"Domain 1: {len(qs)} questões carregadas.")


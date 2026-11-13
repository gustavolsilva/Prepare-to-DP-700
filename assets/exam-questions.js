// Banco de Questões do Simulado Oficial DP-700
// Microsoft Certified: Fabric Data Engineer Associate
// Contém 182 questões comentadas em padrão Pearson VUE
// Gerado automaticamente com 3x o volume original

window.DP700_QUESTION_BANK = [
  {
    id: "d1_q01",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Dimensionamento de F-SKU e Suporte a Copilot",
    question: "Sua organização planeja implantar o Microsoft Fabric para atender cargas de trabalho de Data Engineering e utilizar os recursos generativos do Copilot para criação automatizada de pipelines e consultas em Notebooks. Qual é a capacidade mínima (F-SKU) necessária para habilitar os recursos nativos do Copilot no locatário do Fabric?",
    options: [
      {
        id: "A",
        text: "F16",
        isCorrect: false
      },
      {
        id: "B",
        text: "F32",
        isCorrect: false
      },
      {
        id: "C",
        text: "F64",
        isCorrect: true
      },
      {
        id: "D",
        text: "F128",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A Microsoft exige no mínimo uma capacidade F64 (ou P1 no Power BI Premium) para habilitar e utilizar os recursos do Copilot no Microsoft Fabric. Capacidades menores que F64 não suportam o consumo de tokens de IA generativa do Copilot.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A e B (F16 e F32):</strong> Suportam todas as cargas analíticas normais (Spark, Warehouse, Data Factory), mas não atendem ao pré-requisito mínimo oficial para habilitar o Copilot.</li><li><strong>D (F128):</strong> Embora suporte o Copilot, não é o requisito mínimo para ativação.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Guarde a regra: Copilot no Fabric exige no mínimo F64 ou P1. Abaixo disso, o toggle do Copilot nas configurações de locatário permanece desativado ou restrito.</div>",
    prompt: "Sua organização planeja implantar o Microsoft Fabric para atender cargas de trabalho de Data Engineering e utilizar os recursos generativos do Copilot para criação automatizada de pipelines e consultas em Notebooks. Qual é a capacidade mínima (F-SKU) necessária para habilitar os recursos nativos do Copilot no locatário do Fabric?"
  },
  {
    id: "d1_q02",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Mecanismo de Smoothing e Janelas de Agregação de CUs",
    question: "Um engenheiro de dados executou um job Spark de alto processamento que consumiu 1.200 Capacity Unit Seconds (CU-s) durante um pico repentino de 1 minuto em uma capacidade F16. Como o mecanismo de Smoothing (suavização) do Microsoft Fabric gerencia esse consumo para evitar a limitação imediata (throttling)?",
    options: [
      {
        id: "A",
        text: "Rejeita imediatamente os jobs seguintes porque o limite do minuto foi ultrapassado.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Distribui o consumo de jobs interativos em 5 minutos e de jobs em segundo plano (background jobs) em uma janela de 24 horas.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Converte automaticamente a capacidade F16 para F32 por meio de autoescala elástica instantânea sem intervenção.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Pausa a capacidade por 15 minutos até que o saldo de CUs seja regenerado no Azure Portal.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O mecanismo de Smoothing calcula médias móveis do consumo de CUs para evitar picos abruptos: operações interativas (consultas SQL interativas, DAX, relatórios) são distribuídas em janelas de 5 minutos, enquanto operações em segundo plano (background jobs como Spark jobs, Data Pipelines e Dataflows) são distribuídas em uma janela móvel de 24 horas.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> O Smoothing existe especificamente para não rejeitar picos repentinos de curto prazo.</li><li><strong>C:</strong> Fabric não altera automaticamente o SKU contratado sem configuração de regras explícitas de automação ou escalabilidade externa.</li><li><strong>D:</strong> A capacidade não é pausada automaticamente pelo motor de smoothing; apenas ocorre throttling em fases se o consumo cumulativo exceder 100% da capacidade ao longo da janela.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> No exame DP-700, lembre-se: Background = 24 horas; Interactive = 5 minutos. Isso é questão recorrente de arquitetura de capacidade!</div>",
    prompt: "Um engenheiro de dados executou um job Spark de alto processamento que consumiu 1.200 Capacity Unit Seconds (CU-s) durante um pico repentino de 1 minuto em uma capacidade F16. Como o mecanismo de Smoothing (suavização) do Microsoft Fabric gerencia esse consumo para evitar a limitação imediata (throttling)?"
  },
  {
    id: "d1_q03",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Estágios de Limitação (Throttling) por Sobrecarga",
    question: "Uma capacidade F32 esteve em sobrecarga contínua por 48 horas devido a pipelines em loop. Quais são os três estágios progressivos de throttling aplicados pelo Microsoft Fabric nessa ordem de severidade?",
    options: [
      {
        id: "A",
        text: "Advertência por E-mail -> Suspensão de Workspaces -> Exclusão de Itens",
        isCorrect: false
      },
      {
        id: "B",
        text: "Atraso Interativo (Interactive Delay) -> Rejeição Interativa (Interactive Rejection) -> Rejeição Total / Segundo Plano (Background Rejection)",
        isCorrect: true
      },
      {
        id: "C",
        text: "Desligamento do Spark -> Bloqueio de Leitura no OneLake -> Exclusão da Assinatura Azure",
        isCorrect: false
      },
      {
        id: "D",
        text: "Redução para F16 -> Descarte de Arquivos Parquet -> Cancelamento de Licença",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric aplica limitação em três etapas sucessivas: 1) Interactive Delay (introduz pequenos atrasos em consultas visuais para desestimular uso excessivo), 2) Interactive Rejection (novas consultas de relatórios e DAX são rejeitadas com erro de capacidade esgotada), 3) Background Rejection (jobs de Spark, Pipelines e ingestão em background passam a falhar totalmente).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A, C e D:</strong> Itens, arquivos e licenças nunca são excluídos ou suspensos por sobrecarga de capacidade; apenas o processamento computacional é throttled.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Sequência exata do Throttling: Interactive Delay -> Interactive Rejection -> Background Rejection.</div>",
    prompt: "Uma capacidade F32 esteve em sobrecarga contínua por 48 horas devido a pipelines em loop. Quais são os três estágios progressivos de throttling aplicados pelo Microsoft Fabric nessa ordem de severidade?"
  },
  {
    id: "d1_q04",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Pausa e Retomada de F-SKU no Azure Portal",
    question: "Um arquiteto de dados deseja reduzir custos de desenvolvimento pausando a capacidade F32 do Fabric durante fins de semana. O que acontece com os dados armazenados no OneLake durante o período em que a capacidade está em estado 'Paused'?",
    options: [
      {
        id: "A",
        text: "Os dados são excluídos após 24 horas de inatividade da capacidade.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Os dados do OneLake continuam preservados com segurança e cobrados apenas pela taxa padrão de armazenamento (Storage CUs/GB), mas as operações computacionais ficam inacessíveis.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Os dados são automaticamente movidos para uma camada de Archive no Blob Storage e exigem 12 horas para reidratação.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O acesso a consultas de leitura via SQL Endpoint permanece disponível gratuitamente durante a pausa.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Quando uma capacidade F-SKU é pausada no portal do Azure, o faturamento da capacidade computacional é interrompido. No entanto, o armazenamento do OneLake é desacoplado da computação e continua existindo com segurança, sendo cobrado à taxa padrão de armazenamento por GB. Nenhuma computação (Spark, SQL Endpoint, Pipelines) pode ser executada.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> Os dados nunca são deletados por pausa de capacidade.</li><li><strong>C:</strong> Não há migração para archive nem tempo de reidratação; ao retomar a capacidade, o acesso aos arquivos é imediato.</li><li><strong>D:</strong> O SQL Endpoint depende da capacidade computacional ativa; se a capacidade estiver pausada, nenhuma consulta T-SQL responde.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> No Fabric, Storage e Compute são totalmente desacoplados. Pausar a capacidade zera o custo de compute, mas o storage do OneLake continua sendo cobrado normalmente.</div>",
    prompt: "Um arquiteto de dados deseja reduzir custos de desenvolvimento pausando a capacidade F32 do Fabric durante fins de semana. O que acontece com os dados armazenados no OneLake durante o período em que a capacidade está em estado 'Paused'?"
  },
  {
    id: "d1_q05",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "multi",
    title: "Associação de Workspaces a Múltiplas Capacidades",
    question: "Você é administrador de um locatário corporativo e precisa organizar ambientes de Desenvolvimento, Teste e Produção. Quais DUAS afirmações sobre a governança de Workspaces e Capacidades no Microsoft Fabric estão corretas? (Selecione 2 alternativas)",
    options: [
      {
        id: "A",
        text: "Um único Workspace pode ser associado a múltiplas capacidades Fabric simultaneamente para balancear a carga.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Um Workspace só pode pertencer a exatamente uma capacidade por vez (ou à capacidade compartilhada de avaliação).",
        isCorrect: true
      },
      {
        id: "C",
        text: "Uma única capacidade Fabric pode hospedar múltiplos Workspaces até o limite de consumo de suas CUs.",
        isCorrect: true
      },
      {
        id: "D",
        text: "Ao alterar a capacidade de um workspace, todos os Lakehouses existentes perdem seus arquivos e exigem reindexação.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A relação entre Workspace e Capacidade é de muitos-para-um: cada Workspace só pode estar associado a uma única capacidade em um dado instante, mas uma capacidade pode abrigar dezenas ou centenas de Workspaces. A alteração de capacidade é uma operação puramente lógica de governança e não deleta dados.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> Um workspace não pode ter balanceamento multik-capacidade simultâneo; a atribuição é 1:1.</li><li><strong>D:</strong> Os dados residem no OneLake e são independentes da capacidade atribuída ao workspace.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Regra de relacionamento: 1 Capacidade -> N Workspaces. 1 Workspace -> 1 Capacidade ativa.</div>",
    prompt: "Você é administrador de um locatário corporativo e precisa organizar ambientes de Desenvolvimento, Teste e Produção. Quais DUAS afirmações sobre a governança de Workspaces e Capacidades no Microsoft Fabric estão corretas? (Selecione 2 alternativas)"
  },
  {
    id: "d1_q06",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Efeito do Burndown e Carry Forward de CUs",
    question: "Quando um pico de uso excede a capacidade nominal do F-SKU contratado, o Fabric permite o processamento imediato gerando um déficit de CUs acumulado chamado 'Carry Forward'. Como esse débito é amortizado (burndown) pelo sistema?",
    options: [
      {
        id: "A",
        text: "O débito é faturado diretamente como custo extraordinário no cartão de crédito do Azure.",
        isCorrect: false
      },
      {
        id: "B",
        text: "O débito é consumido gradativamente durante períodos subsequentes de menor utilização da capacidade, quando as CUs ficariam ociosas.",
        isCorrect: true
      },
      {
        id: "C",
        text: "O saldo negativo é perdoado automaticamente à meia-noite em ponto no fuso UTC.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Exige que o administrador faça um pagamento manual de créditos no Microsoft 365 Admin Center.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O mecanismo de Burndown consome o saldo de Carry Forward acumulado sempre que a capacidade estiver executando cargas de trabalho abaixo de 100% de sua taxa nominal de CUs. O tempo ocioso é usado para pagar o débito sem custos adicionais de licenciamento.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A e D:</strong> Não há cobrança extra imediata nem recarga manual; o custo da capacidade fixa já cobre a recuperação durante períodos ociosos.</li><li><strong>C:</strong> O débito não expira arbitrariamente à meia-noite; ele persiste na janela móvel de 24 horas até ser amortizado ou atingir o limite de throttling.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Carry Forward = débito gerado pelo burst; Burndown = pagamento do débito durante períodos de folga computacional.</div>",
    prompt: "Quando um pico de uso excede a capacidade nominal do F-SKU contratado, o Fabric permite o processamento imediato gerando um déficit de CUs acumulado chamado 'Carry Forward'. Como esse débito é amortizado (burndown) pelo sistema?"
  },
  {
    id: "d1_q07",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Privilégios da Função 'Contributor' em Workspaces Fabric",
    question: "Qual é a principal restrição aplicada a um usuário com a função de 'Contributor' (Colaborador) em um Workspace do Fabric em comparação com um usuário com a função 'Member' (Membro)?",
    options: [
      {
        id: "A",
        text: "Contributors não podem criar nem editar Notebooks e Pipelines de Dados.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Contributors podem criar, editar e excluir itens do workspace, mas não podem publicar novos apps, atualizar metadados do workspace nem conceder permissões a outros usuários.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Contributors têm acesso apenas de leitura (Read-Only) em tabelas Delta do Lakehouse.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Contributors não têm permissão para executar consultas no SQL Analytics Endpoint.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A função Contributor tem plenos direitos de criação, edição e exclusão de artefatos analíticos (Lakehouses, Warehouses, Pipelines, Notebooks), mas não possui permissões administrativas do Workspace: não pode adicionar novos membros, não pode republicar Apps do Power BI e não pode alterar configurações do workspace.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> Contributors podem criar e editar Notebooks e Pipelines normalmente.</li><li><strong>C e D:</strong> Contributors têm permissão de gravação/leitura no workspace e executam consultas normalmente.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Hierarquia de papéis no Workspace Fabric: Admin > Member > Contributor > Viewer. Apenas Admin e Member podem gerenciar permissões e publicar Apps.</div>",
    prompt: "Qual é a principal restrição aplicada a um usuário com a função de 'Contributor' (Colaborador) em um Workspace do Fabric em comparação com um usuário com a função 'Member' (Membro)?"
  },
  {
    id: "d1_q08",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Permissões Granulares em Nível de Item: ReadData vs ReadAll",
    question: "Um engenheiro de dados precisa compartilhar um Lakehouse com uma equipe de analistas para que eles possam ler os dados subjacentes via SQL Endpoint e Power BI, mas sem permitir que eles acessem o lakehouse com permissões de administrador do workspace. Qual permissão granular de item deve ser concedida no Lakehouse?",
    options: [
      {
        id: "A",
        text: "Atribuir a função de 'Viewer' no Workspace inteiro.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Conceder a permissão 'ReadData' (ou ReadAll) especificamente no item Lakehouse compartilhado.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Criar um token SAS de conta do Azure Storage com acesso de superusuário.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Adicionar todos os analistas ao grupo de administradores da capacidade F-SKU.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O compartilhamento de itens permite conceder permissões granulares sem dar acesso a todo o workspace. A permissão 'ReadData' permite ao usuário ler o conteúdo dos dados das tabelas gerenciadas e atalhos, enquanto 'ReadAll' permite ler todos os dados no OneLake associados ao item.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> Atribuir Viewer no workspace daria visibilidade a todos os outros artefatos do workspace, violando o princípio do menor privilégio.</li><li><strong>C:</strong> OneLake é gerenciado nativamente pelo Fabric; criar tokens SAS manuais viola a governança nativa e muitas vezes é bloqueado.</li><li><strong>D:</strong> Administrador de capacidade é um privilégio excessivo de infraestrutura.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Para exames: Item Sharing + 'ReadData' / 'ReadAll' é a resposta correta para acesso granular a um único Lakehouse/Warehouse.</div>",
    prompt: "Um engenheiro de dados precisa compartilhar um Lakehouse com uma equipe de analistas para que eles possam ler os dados subjacentes via SQL Endpoint e Power BI, mas sem permitir que eles acessem o lakehouse com permissões de administrador do workspace. Qual permissão granular de item deve ser concedida no Lakehouse?"
  },
  {
    id: "d1_q09",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "OneLake Data Access Roles (ODAR / RBAC Preview)",
    question: "Qual é a principal vantagem dos OneLake Data Access Roles em comparação com a segurança tradicional de Workspace baseada em Viewer/Contributor?",
    options: [
      {
        id: "A",
        text: "Permite definir regras de acesso granulares (RBAC) diretamente em pastas e tabelas específicas dentro do Lakehouse, aplicando-se de forma consistente tanto ao Spark quanto ao SQL Endpoint.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Permite executar consultas SQL no Lakehouse sem consumir nenhuma Capacity Unit (CU).",
        isCorrect: false
      },
      {
        id: "C",
        text: "Substitui completamente o Active Directory por autenticação biométrica.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Permite converter tabelas Delta em arquivos CSV legados em tempo real.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Os OneLake Data Access Roles (ODAR) trazem controle de acesso granular baseado em funções diretamente no nível de armazenamento do OneLake (pastas e tabelas Delta). Isso garante que permissões de segurança sejam respeitadas universalmente, independentemente do motor de computação utilizado (Spark, T-SQL ou API do OneLake).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> ODAR é um mecanismo de segurança e não afeta o faturamento de CUs das consultas.</li><li><strong>C e D:</strong> Afirmações incorretas sem fundamento técnico.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> ODAR (OneLake Data Access Roles) = Segurança granular em pastas e tabelas do Lakehouse respeitada por múltiplos motores (Spark, SQL, etc.).</div>",
    prompt: "Qual é a principal vantagem dos OneLake Data Access Roles em comparação com a segurança tradicional de Workspace baseada em Viewer/Contributor?"
  },
  {
    id: "d1_q10",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Row-Level Security (RLS) e o Efeito no Direct Lake",
    question: "Um arquiteto de BI configurou uma política de Row-Level Security (RLS) usando `CREATE SECURITY POLICY` no SQL Analytics Endpoint de um Lakehouse corporativo. O que acontece quando os usuários corporativos abrem relatórios do Power BI conectados ao Modelo Semântico padrão em modo Direct Lake?",
    options: [
      {
        id: "A",
        text: "O relatório carrega com alto desempenho nativo no Direct Lake, ignorando a política de segurança silenciosamente.",
        isCorrect: false
      },
      {
        id: "B",
        text: "O relatório falha imediatamente com código de erro 403 Forbidden.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Ocorre um Fallback silencioso para o modo DirectQuery, executando consultas T-SQL contra o SQL Endpoint para cada interação visual.",
        isCorrect: true
      },
      {
        id: "D",
        text: "O relatório converte o dataset automaticamente para o modo de Importação com agendamento diário.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O modo Direct Lake lê arquivos Parquet diretamente do OneLake para a memória do Analysis Services (VertiPaq) sem passar pelo motor relacional. Quando RLS, CLS ou Data Masking são aplicados no SQL Analytics Endpoint ou Warehouse, o Direct Lake não consegue aplicar a regra no Parquet puro e sofre Fallback para DirectQuery, gerando overhead de consultas T-SQL.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> A segurança nunca é ignorada no Fabric; o motor preserva a restrição forçando DirectQuery.</li><li><strong>B:</strong> O relatório não falha; ele funciona, porém em modo DirectQuery com desempenho inferior.</li><li><strong>D:</strong> O Fabric não altera o modo de armazenamento para Importação sem intervenção manual do usuário.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Conceito chave do DP-700: RLS / CLS no SQL Endpoint força o Direct Lake a fazer Fallback para DirectQuery! Para manter Direct Lake puro com RLS, defina RLS diretamente no Modelo Semântico do Power BI.</div>",
    prompt: "Um arquiteto de BI configurou uma política de Row-Level Security (RLS) usando `CREATE SECURITY POLICY` no SQL Analytics Endpoint de um Lakehouse corporativo. O que acontece quando os usuários corporativos abrem relatórios do Power BI conectados ao Modelo Semântico padrão em modo Direct Lake?"
  },
  {
    id: "d1_q11",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Column-Level Security (CLS) e Mascaramento Dinâmico (DDM)",
    question: "Um engenheiro de dados precisa impedir que a equipe de análise financeira visualize os números de cartões de crédito dos clientes na tabela `FatoVendas` do Warehouse. Os analistas devem poder consultar a tabela, mas o número do cartão deve aparecer como `XXXX-XXXX-XXXX-1234`. Qual recurso nativo do T-SQL no Fabric Warehouse deve ser utilizado?",
    options: [
      {
        id: "A",
        text: "Dynamic Data Masking (DDM) com uma função `FUNCTION = 'partial(0, \"XXXX-XXXX-XXXX-\", 4)'` na coluna.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Triggers `INSTEAD OF SELECT` para reescrever o texto do cartão.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Uma stored procedure criptografada com certificado assimétrico RSA de 4096 bits.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Excluir fisicamente a coluna da tabela e salvar em um arquivo CSV local.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric Warehouse suporta Dynamic Data Masking (DDM) em nível de coluna. Ao aplicar `ALTER TABLE FatoVendas ALTER COLUMN NumeroCartao ADD MASKED WITH (FUNCTION = 'partial(0, \"XXXX-XXXX-XXXX-\", 4)')`, usuários sem a permissão `UNMASK` visualizam os dados ofuscados em tempo de consulta sem alterar os dados físicos no OneLake.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> O Fabric Warehouse não suporta Triggers.</li><li><strong>C:</strong> Solução inviável e desnecessária para visualização em tabelas relacionais do Warehouse.</li><li><strong>D:</strong> Viola a integridade e necessidade de negócio.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Dynamic Data Masking (DDM) mascara dados confidenciais para usuários sem privilégio UNMASK, mantendo os dados originais inalterados no armazenamento.</div>",
    prompt: "Um engenheiro de dados precisa impedir que a equipe de análise financeira visualize os números de cartões de crédito dos clientes na tabela `FatoVendas` do Warehouse. Os analistas devem poder consultar a tabela, mas o número do cartão deve aparecer como `XXXX-XXXX-XXXX-1234`. Qual recurso nativo do T-SQL no Fabric Warehouse deve ser utilizado?"
  },
  {
    id: "d1_q12",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "multi",
    title: "Causas de Fallback de Direct Lake para DirectQuery",
    question: "Quais DUAS condições abaixo causam o Fallback automático de um relatório Power BI em modo Direct Lake para DirectQuery no Microsoft Fabric? (Selecione 2 alternativas)",
    options: [
      {
        id: "A",
        text: "A consulta do relatório referencia uma Exibição (View) SQL criada no SQL Analytics Endpoint em vez de uma tabela Delta física.",
        isCorrect: true
      },
      {
        id: "B",
        text: "O tamanho total dos arquivos Parquet da tabela física excede o limite de memória da capacidade F-SKU configurada.",
        isCorrect: true
      },
      {
        id: "C",
        text: "A tabela Delta foi otimizada com a ordenação V-Order ativada no Spark.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O Lakehouse está localizado na mesma região geográfica da capacidade Fabric.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Direct Lake lê tabelas Delta Parquet físicas. Se o modelo semântico referenciar Views T-SQL do SQL Endpoint (que exigem computação relacional T-SQL em tempo de execução) ou se o volume de dados da tabela exceder o teto de memória RAM do VertiPaq do F-SKU, o motor executa Fallback para DirectQuery.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C:</strong> V-Order é altamente recomendado e nativo do Fabric, otimizando o carregamento do Direct Lake; nunca causa fallback.</li><li><strong>D:</strong> Estar na mesma região é o cenário ideal e reduz latência.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Gatilhos de Fallback no Direct Lake: Views SQL, RLS no SQL Endpoint, estouro de memória da capacidade e tipos de dados incompatíveis no Parquet.</div>",
    prompt: "Quais DUAS condições abaixo causam o Fallback automático de um relatório Power BI em modo Direct Lake para DirectQuery no Microsoft Fabric? (Selecione 2 alternativas)"
  },
  {
    id: "d1_q13",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Rótulos de Sensibilidade do Microsoft Purview no Fabric",
    question: "Como os Rótulos de Sensibilidade (Sensitivity Labels) do Microsoft Purview Information Protection se propagam no ecossistema do Microsoft Fabric quando aplicados a um Lakehouse?",
    options: [
      {
        id: "A",
        text: "Eles não se propagam e devem ser recriados manualmente em cada relatório e notebook.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Eles herdam downstream (a jusante) automaticamente para modelos semânticos e relatórios do Power BI criados a partir do Lakehouse.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Eles exigem a execução manual de um script PowerShell a cada hora.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Eles bloqueiam qualquer conexão externa proveniente do Azure Databricks.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric possui integração profunda com o Microsoft Purview: rótulos de sensibilidade aplicados a itens upstream (como um Lakehouse ou Warehouse) se propagam automaticamente downstream para os Modelos Semânticos e Relatórios gerados a partir desses dados, garantindo proteção e criptografia de ponta a ponta.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A e C:</strong> A herança é automática e nativa da plataforma.</li><li><strong>D:</strong> O rótulo governa classificação e direitos digitais, não o bloqueio de rede arbitrário de engines externas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Purview no Fabric: Suporte a herança downstream automática de rótulos de sensibilidade de Lakehouses -> Semantics Models -> Relatórios.</div>",
    prompt: "Como os Rótulos de Sensibilidade (Sensitivity Labels) do Microsoft Purview Information Protection se propagam no ecossistema do Microsoft Fabric quando aplicados a um Lakehouse?"
  },
  {
    id: "d1_q14",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Identidade de Workspace e Acesso a Recursos Confiáveis do Azure",
    question: "Você precisa configurar um Data Pipeline no Fabric para acessar um Azure Data Lake Storage Gen2 (ADLS Gen2) protegido por firewall de rede privada (sem acesso público). Qual método de autenticação e rede deve ser utilizado para permitir a conexão segura sem expor chaves de conta nos pipelines?",
    options: [
      {
        id: "A",
        text: "Desativar temporariamente o firewall do ADLS Gen2 durante a execução do pipeline.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Configurar uma Identidade de Workspace (Workspace Identity) no Fabric e habilitar a exceção de serviço confiável (Trusted Microsoft Services) nas regras de rede do ADLS Gen2.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Gravar a Shared Key do storage em texto puro em um Notebook Python compartilhado.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Configurar uma VPN ponto a ponto em cada laptop de desenvolvedor conectado ao Fabric.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Microsoft Fabric permite atribuir uma Identidade Gerenciada ao Workspace (Workspace Identity). Combinada com a regra de firewall de 'Trusted Microsoft Services' no ADLS Gen2, o Fabric estabelece comunicação segura pela espinha dorsal da Microsoft sem necessidade de IP público ou chaves estáticas.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A e C:</strong> Práticas inseguras que violam os requisitos de segurança e compliance.</li><li><strong>D:</strong> A computação do Fabric roda na nuvem gerenciada, não na máquina local do usuário.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Workspace Identity + Trusted Service Access no Azure Storage = Conexão segura sem chaves e com firewall ativado.</div>",
    prompt: "Você precisa configurar um Data Pipeline no Fabric para acessar um Azure Data Lake Storage Gen2 (ADLS Gen2) protegido por firewall de rede privada (sem acesso público). Qual método de autenticação e rede deve ser utilizado para permitir a conexão segura sem expor chaves de conta nos pipelines?"
  },
  {
    id: "d1_q15",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Criação de Atalho (Shortcut) para AWS S3",
    question: "Uma empresa possui um data lake existente no Amazon Web Services S3 contendo tabelas no formato Delta Parquet. A gerência determinou que os analistas devem consultar esses dados no Microsoft Fabric sem duplicar o armazenamento nem incorrer em custos recorrentes de cópia de dados. Qual solução atende a essa exigência?",
    options: [
      {
        id: "A",
        text: "Criar um OneLake Shortcut na pasta 'Tables' do Lakehouse apontando para o bucket S3 de origem.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Criar um Data Pipeline com atividade Copy para baixar os dados do S3 a cada 30 minutos.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Exportar os dados do S3 em arquivos compactados .ZIP e fazer upload manual via portal do OneLake.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Migrar todo o bucket S3 para um banco de dados relacional SQL Server em máquina virtual.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Os OneLake Shortcuts criam ponteiros simbólicos no OneLake apontando para fontes externas como AWS S3, ADLS Gen2 ou Google Cloud Storage. Ao criar um atalho na pasta 'Tables' de um Lakehouse, o Fabric trata os arquivos Delta externos como tabelas nativas sem cópia física de dados (Zero-ETL).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> A atividade Copy duplica o armazenamento e gera custos contínuos de egresso e computação.</li><li><strong>C e D:</strong> Soluções inviáveis, manuais e contrárias aos requisitos do exame.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> OneLake Shortcuts = Virtualização de dados (Zero-ETL / Zero-Copy) apontando para AWS S3, Google Cloud Storage, Dataverse ou ADLS Gen2.</div>",
    prompt: "Uma empresa possui um data lake existente no Amazon Web Services S3 contendo tabelas no formato Delta Parquet. A gerência determinou que os analistas devem consultar esses dados no Microsoft Fabric sem duplicar o armazenamento nem incorrer em custos recorrentes de cópia de dados. Qual solução atende a essa exigência?"
  },
  {
    id: "d1_q16",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Diferença Crítica entre Atalhos em 'Tables' vs 'Files'",
    question: "Ao criar um OneLake Shortcut dentro de um Lakehouse, um engenheiro acidentalmente criou o atalho dentro da pasta `Files/` em vez de `Tables/`. Qual é o impacto direto dessa ação nas consultas analíticas?",
    options: [
      {
        id: "A",
        text: "O atalho não funciona e retorna erro de rede na AWS.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Os dados ficam acessíveis via Notebook Spark por caminhos de arquivo, mas a tabela Delta não é registrada no catálogo Metastore nem exposta no SQL Analytics Endpoint automaticamente.",
        isCorrect: true
      },
      {
        id: "C",
        text: "O Lakehouse inteiro é corrompido e deve ser excluído.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O SQL Endpoint converte automaticamente os arquivos em tabelas temporárias na memória RAM.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> No Lakehouse do Fabric: a pasta `Tables/` contém dados gerenciados ou atalhos Delta que são registrados automaticamente no catálogo metastore e expostos como tabelas relacionais no SQL Analytics Endpoint. A pasta `Files/` contém arquivos brutos (não estruturados ou semiestruturados) que podem ser lidos por Spark/Notebooks, mas não aparecem como tabelas no SQL Endpoint.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A e C:</strong> O atalho funciona perfeitamente para leitura de arquivos, não ocorre corrupção nem erro.</li><li><strong>D:</strong> O SQL Endpoint não converte automaticamente arquivos soltos da pasta `Files/`.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Regra de ouro do Lakehouse: `Tables/` = Tabelas no Catálogo + SQL Endpoint. `Files/` = Arquivos brutos apenas para Notebooks/Spark.</div>",
    prompt: "Ao criar um OneLake Shortcut dentro de um Lakehouse, um engenheiro acidentalmente criou o atalho dentro da pasta `Files/` em vez de `Tables/`. Qual é o impacto direto dessa ação nas consultas analíticas?"
  },
  {
    id: "d1_q17",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "multi",
    title: "Provedores de Nuvem Suportados Nativamente por OneLake Shortcuts",
    question: "Quais DUAS fontes de nuvem externas possuem suporte oficial direto para criação de OneLake Shortcuts nativos no Microsoft Fabric? (Selecione 2 alternativas)",
    options: [
      {
        id: "A",
        text: "Amazon Web Services (AWS) S3",
        isCorrect: true
      },
      {
        id: "B",
        text: "Google Cloud Storage (GCS)",
        isCorrect: true
      },
      {
        id: "C",
        text: "Oracle Cloud Infrastructure (OCI) Object Storage nativo sem S3-compatibility",
        isCorrect: false
      },
      {
        id: "D",
        text: "Alibaba Cloud OSS nativo sem conectores",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Microsoft Fabric suporta nativamente OneLake Shortcuts para: 1) OneLake (atalhos internos entre lakehouses e workspaces), 2) Azure Data Lake Storage Gen2 (ADLS Gen2), 3) Amazon S3, 4) Google Cloud Storage (GCS) e 5) Microsoft Dataverse (via Fabric Link).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C e D:</strong> Provedores sem conectores nativos de atalho direto no OneLake.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Provedores oficiais de Shortcuts externos no DP-700: ADLS Gen2, AWS S3, Google Cloud Storage (GCS) e Dataverse.</div>",
    prompt: "Quais DUAS fontes de nuvem externas possuem suporte oficial direto para criação de OneLake Shortcuts nativos no Microsoft Fabric? (Selecione 2 alternativas)"
  },
  {
    id: "d1_q18",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Dataverse Link para Microsoft Fabric",
    question: "Uma organização utiliza o Microsoft Dynamics 365 e deseja disponibilizar todas as entidades do Dataverse no Microsoft Fabric sem pipelines de extração diários. Como o recurso Microsoft Dataverse Link para Fabric viabiliza essa integração?",
    options: [
      {
        id: "A",
        text: "Executa uma exportação diária em formato BCP para um servidor FTP.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Sincroniza continuamente as tabelas do Dataverse em formato Delta Parquet gerenciado, disponibilizando-as automaticamente no OneLake via atalhos sem pipelines ETL.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Obriga o uso de uma gateway local instalada em cada estação de trabalho.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Converte todas as tabelas em bancos de dados Access locais.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Dataverse Link para Microsoft Fabric utiliza a tecnologia Synapse Link integrada ao OneLake. O Dataverse escreve e atualiza os dados diretamente em formato Delta Parquet no OneLake, disponibilizando atalhos automáticos no Workspace do Fabric sem a necessidade de criar pipelines manuais de extração.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A, C e D:</strong> Métodos legados que não utilizam a integração nativa SaaS do Fabric Link.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Dataverse Link = Zero-ETL para Dynamics 365 e Power Apps direto no OneLake em formato Delta Parquet.</div>",
    prompt: "Uma organização utiliza o Microsoft Dynamics 365 e deseja disponibilizar todas as entidades do Dataverse no Microsoft Fabric sem pipelines de extração diários. Como o recurso Microsoft Dataverse Link para Fabric viabiliza essa integração?"
  },
  {
    id: "d1_q19",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Autenticação em Atalhos do Google Cloud Storage (GCS)",
    question: "Ao criar um OneLake Shortcut apontando para um bucket no Google Cloud Storage (GCS), qual credencial de segurança é exigida para autorizar a conexão entre o Fabric e o GCS?",
    options: [
      {
        id: "A",
        text: "Uma chave de API (API Key) do Google Maps.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Chave de Conta de Serviço (GCS HMAC Key / Access Key ID e Secret Access Key) ou credencial federada configurada no GCP.",
        isCorrect: true
      },
      {
        id: "C",
        text: "A senha pessoal de login do Gmail de um engenheiro de dados.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Um certificado SSL autoassinado gerado no Windows Notepad.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Para conectar o OneLake Shortcut ao Google Cloud Storage, o Fabric utiliza a API compatível com S3 do Google Cloud, exigindo um par de chaves HMAC (Access Key ID e Secret Access Key) gerado para uma Conta de Serviço (Service Account) no Google Cloud Console com permissões de leitura no bucket.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A, C e D:</strong> Credenciais inválidas e sem aderência aos padrões de segurança em nuvem.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Shortcuts GCS utilizam HMAC Keys geradas no Google Cloud Storage Console para autenticação segura.</div>",
    prompt: "Ao criar um OneLake Shortcut apontando para um bucket no Google Cloud Storage (GCS), qual credencial de segurança é exigida para autorizar a conexão entre o Fabric e o GCS?"
  },
  {
    id: "d1_q20",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Comportamento de Exclusão em Atalhos (Delete Shortcut vs Delete Data)",
    question: "Um usuário com papel de Contributor acessa a interface web do Lakehouse e clica com o botão direito em uma pasta de atalho (Shortcut) do AWS S3 e seleciona 'Delete'. O que acontece com os arquivos originais localizados no bucket S3 da AWS?",
    options: [
      {
        id: "A",
        text: "Todos os arquivos do bucket S3 da AWS são permanentemente excluídos.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Apenas o atalho (ponteiro lógico) no OneLake é removido; os dados físicos no bucket S3 da AWS permanecem totalmente intactos.",
        isCorrect: true
      },
      {
        id: "C",
        text: "O bucket S3 entra em estado de bloqueio e exige chamado na AWS para liberação.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Os dados são movidos para a lixeira do Windows do usuário.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A exclusão de um atalho (Shortcut) no Fabric remove apenas o link simbólico nos metadados do OneLake. O Fabric nunca emite comandos de exclusão na fonte externa (AWS S3, ADLS Gen2 ou GCS) durante a deleção do atalho.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> Os atalhos são ponteiros de virtualização; deletar o ponteiro não deleta a origem.</li><li><strong>C e D:</strong> Afirmações incorretas sem sentido técnico.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Cuidado em prova: Deletar um Shortcut NÃO deleta os dados na origem externa (S3, ADLS, GCS).</div>",
    prompt: "Um usuário com papel de Contributor acessa a interface web do Lakehouse e clica com o botão direito em uma pasta de atalho (Shortcut) do AWS S3 e seleciona 'Delete'. O que acontece com os arquivos originais localizados no bucket S3 da AWS?"
  },
  {
    id: "d1_q21",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "OneLake File Explorer no Windows",
    question: "Qual é a principal função da ferramenta cliente 'OneLake File Explorer' para Windows no fluxo de trabalho de engenharia de dados?",
    options: [
      {
        id: "A",
        text: "Compilar código Scala em arquivos executáveis para o Apache Spark.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Sincronizar e mapear os workspaces e lakehouses do OneLake diretamente no Windows Explorer como se fossem pastas locais, facilitando upload e download rápido de arquivos.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Executar consultas SQL no Warehouse sem conexão com a internet.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Substituir o Azure Portal na gestão de cobrança de cartões de crédito.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O OneLake File Explorer integra o OneLake nativamente ao Windows File Explorer (semelhante ao cliente OneDrive), permitindo que desenvolvedores naveguem por workspaces, lakehouses e pastas, arrastando e soltando arquivos diretamente para o OneLake sem precisar de scripts de upload.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A, C e D:</strong> Funções não relacionadas ao OneLake File Explorer.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> OneLake File Explorer = Cliente desktop para sincronização de arquivos e pastas no Windows Explorer.</div>",
    prompt: "Qual é a principal função da ferramenta cliente 'OneLake File Explorer' para Windows no fluxo de trabalho de engenharia de dados?"
  },
  {
    id: "d1_q22",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Shortcuts Internos entre Workspaces e Segurança",
    question: "O Workspace 'Engenharia_Dados' possui um Lakehouse com tabelas limpas. O Workspace 'Vendas_Analise' precisa ler uma dessas tabelas via OneLake Shortcut interno. Como o Fabric valida as permissões quando um usuário do Workspace 'Vendas_Analise' consulta o atalho?",
    options: [
      {
        id: "A",
        text: "O usuário precisa ter pelo menos permissão de leitura ('Read' ou 'ReadData') no Lakehouse de origem do Workspace 'Engenharia_Dados'.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Qualquer usuário pode ler qualquer atalho interno sem nenhuma permissão no workspace de origem.",
        isCorrect: false
      },
      {
        id: "C",
        text: "O workspace de destino deve pagar uma taxa de licenciamento duplicada à Microsoft.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O atalho interno requer autenticação por Kerberos local.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Em atalhos internos do OneLake entre workspaces, a segurança é delegada: o usuário que executa a consulta através do atalho precisa ter permissões de acesso aos dados ('ReadData') no item de origem subjacente. Sem isso, a consulta falha por acesso negado.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Violaria totalmente os princípios de governança e isolamento de dados corporativos.</li><li><strong>C e D:</strong> Inexistentes no modelo de governança do OneLake.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Shortcuts internos respeitam as permissões do item de origem: o consumidor precisa ter acesso concedido no item original.</div>",
    prompt: "O Workspace 'Engenharia_Dados' possui um Lakehouse com tabelas limpas. O Workspace 'Vendas_Analise' precisa ler uma dessas tabelas via OneLake Shortcut interno. Como o Fabric valida as permissões quando um usuário do Workspace 'Vendas_Analise' consulta o atalho?"
  },
  {
    id: "d1_q23",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Provedores de Git Suportados Nativamente na Integração do Fabric",
    question: "Quais são os dois sistemas de controle de versão em nuvem que possuem suporte oficial nativo para integração direta com Workspaces do Microsoft Fabric?",
    options: [
      {
        id: "A",
        text: "Azure DevOps Repos (Git) e GitHub",
        isCorrect: true
      },
      {
        id: "B",
        text: "GitLab Self-Hosted e Bitbucket Cloud",
        isCorrect: false
      },
      {
        id: "C",
        text: "Subversion (SVN) e Mercurial",
        isCorrect: false
      },
      {
        id: "D",
        text: "AWS CodeCommit e SourceForge",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Microsoft Fabric oferece suporte nativo à integração Git para Azure DevOps Repos e GitHub. Permite sincronizar metadados de itens do workspace bidirecionalmente com branches de repositórios Git.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Não possuem integração nativa de sincronização direta na interface de administração do Fabric.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Git no Fabric: Azure DevOps Repos e GitHub são os dois provedores suportados nativamente.</div>",
    prompt: "Quais são os dois sistemas de controle de versão em nuvem que possuem suporte oficial nativo para integração direta com Workspaces do Microsoft Fabric?"
  },
  {
    id: "d1_q24",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Arquivos de Metadados `.platform` na Integração Git",
    question: "Ao sincronizar um Workspace do Fabric com um repositório Git, uma pasta é criada para cada item, contendo um arquivo chamado `.platform`. Qual é a finalidade desse arquivo?",
    options: [
      {
        id: "A",
        text: "Armazenar uma cópia compactada de todos os dados Parquet das tabelas.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Conter as configurações e metadados de infraestrutura do item do Fabric (como tipo de item, id de exibição e vínculos lógicos) necessários para o Fabric reconstruir o artefato.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Guardar as senhas e chaves de acesso dos desenvolvedores em formato Base64.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Instalar o compilador Java no Azure DevOps durante o build.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O arquivo `.platform` é gerado automaticamente pelo Fabric em cada pasta de item rastreado pelo Git. Ele contém metadados de plataforma essenciais (identificador do tipo de item, schema version e propriedades de integração) para que o serviço do Fabric reconheça o diretório como um artefato gerenciado.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> O Git armazena apenas definições e metadados de código, nunca dados físicos de tabelas.</li><li><strong>C:</strong> Credenciais e segredos nunca são salvos em arquivos `.platform` no Git.</li><li><strong>D:</strong> Não tem relação com o compilador Java.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Arquivo `.platform` = Metadados de plataforma essenciais para o Fabric rastrear e instanciar o item a partir do repositório Git.</div>",
    prompt: "Ao sincronizar um Workspace do Fabric com um repositório Git, uma pasta é criada para cada item, contendo um arquivo chamado `.platform`. Qual é a finalidade desse arquivo?"
  },
  {
    id: "d1_q25",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "multi",
    title: "Itens do Fabric com Suporte Oficial a Git Integration",
    question: "Quais DUAS classes de itens analíticos do Microsoft Fabric possuem suporte nativo à sincronização e versionamento via Git Integration? (Selecione 2 alternativas)",
    options: [
      {
        id: "A",
        text: "Notebooks Spark",
        isCorrect: true
      },
      {
        id: "B",
        text: "Pipelines de Dados (Data Pipelines)",
        isCorrect: true
      },
      {
        id: "C",
        text: "Conjuntos de dados de streaming legado (Legacy Push Datasets)",
        isCorrect: false
      },
      {
        id: "D",
        text: "Arquivos de backup físico do SQL Server (.BAK)",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric expandiu o suporte ao Git para incluir: Notebooks, Data Pipelines, Lakehouses (metadados), Warehouses (definições DDL), Modelos Semânticos (TMDL/BIM), Relatórios (PBIR), Ambientes (Environments) e Eventstreams.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C e D:</strong> Não são itens modernos compatíveis com o ciclo de vida DevOps do Fabric.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Itens suportados no Git do Fabric: Notebooks, Data Pipelines, Warehouses, Lakehouses, Semantic Models, Reports e Environments.</div>",
    prompt: "Quais DUAS classes de itens analíticos do Microsoft Fabric possuem suporte nativo à sincronização e versionamento via Git Integration? (Selecione 2 alternativas)"
  },
  {
    id: "d1_q26",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Regras de Implantação (Deployment Rules) em Pipelines de Implantação",
    question: "Ao utilizar os Deployment Pipelines do Fabric para promover itens do estágio de 'Desenvolvimento' para 'Produção', como um engenheiro de dados garante que os relatórios em Produção apontem para o Lakehouse de Produção sem precisar editar o código manualmente?",
    options: [
      {
        id: "A",
        text: "Criar regras de implantação de parâmetros ou fontes de dados (Deployment Rules) no estágio de destino.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Editar manualmente o script SQL em produção após cada implantação.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Renomear o Lakehouse de produção para ter o mesmo identificador GUID de desenvolvimento.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Desativar a segurança em desenvolvimento para que produção acesse a mesma base.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Os Deployment Pipelines do Fabric oferecem o recurso 'Deployment Rules' (Regras de Implantação). Elas permitem substituir automaticamente parâmetros ou mapeamentos de fontes de dados (como apontar de `Lakehouse_Dev` para `Lakehouse_Prod`) sempre que um artefato é implantado no estágio superior.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> A edição manual em produção viola as práticas de DevOps e gera risco de downtime e erro humano.</li><li><strong>C:</strong> GUIDs são imutáveis e exclusivos no Fabric.</li><li><strong>D:</strong> Misturar ambientes e desativar segurança viola regras básicas de governança.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Deployment Rules = Mapeamento automático de fontes de dados e parâmetros entre estágios de Dev, Test e Prod.</div>",
    prompt: "Ao utilizar os Deployment Pipelines do Fabric para promover itens do estágio de 'Desenvolvimento' para 'Produção', como um engenheiro de dados garante que os relatórios em Produção apontem para o Lakehouse de Produção sem precisar editar o código manualmente?"
  },
  {
    id: "d1_q27",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Projetos de Banco de Dados SQL (`.sqlproj`) para Fabric Warehouse",
    question: "Uma equipe de desenvolvedores SQL quer adotar uma abordagem 'State-First' baseada em código para gerenciar o esquema do Fabric Warehouse no Visual Studio Code e no Azure DevOps. Qual tecnologia padrão deve ser utilizada para compilar e implantar o esquema via CI/CD?",
    options: [
      {
        id: "A",
        text: "Projetos de Banco de Dados SQL (extensão SQL Database Projects / `.sqlproj` com DacFx) direcionados ao Microsoft Fabric Warehouse.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Scripts manuais em arquivos `.bat` no Prompt de Comando.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Exportação periódica de arquivos `.xlsx` com a lista de tabelas.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Execução de comandos `DUMP DATABASE` não documentados.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Microsoft Fabric Warehouse suporta projetos de banco de dados SQL (`.sqlproj`) através da extensão SQL Database Projects no VS Code ou Azure Data Studio. Isso permite versionar o DDL de tabelas, views e procedures, gerando arquivos `.dacpac` compilados para automação de CI/CD.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Métodos manuais ou não suportados para governança corporativa de banco de dados.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Fabric Warehouse CI/CD = SQL Database Projects (`.sqlproj`) + Dacpac para desenvolvimento state-first.</div>",
    prompt: "Uma equipe de desenvolvedores SQL quer adotar uma abordagem 'State-First' baseada em código para gerenciar o esquema do Fabric Warehouse no Visual Studio Code e no Azure DevOps. Qual tecnologia padrão deve ser utilizada para compilar e implantar o esquema via CI/CD?"
  },
  {
    id: "d1_q28",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Backward Deployment em Pipelines de Implantação",
    question: "Um desenvolvedor fez uma alteração emergencial diretamente no Workspace do estágio de 'Teste' de um Deployment Pipeline e precisa sincronizar essa alteração de volta para o estágio de 'Desenvolvimento'. Esse procedimento é suportado pelo Fabric?",
    options: [
      {
        id: "A",
        text: "Não, os pipelines do Fabric só permitem implantações estritamente para a frente (Dev -> Test -> Prod).",
        isCorrect: false
      },
      {
        id: "B",
        text: "Sim, o Fabric suporta 'Backward Deployment' (implantação retroativa) entre estágios vizinhos (por exemplo, de Teste para Desenvolvimento).",
        isCorrect: true
      },
      {
        id: "C",
        text: "Sim, mas exige a exclusão do workspace de desenvolvimento.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Apenas se a capacidade for maior que F512.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Os Deployment Pipelines do Fabric suportam implantação retroativa (Backward Deployment). Se for realizada uma alteração em um estágio posterior (como Teste), o administrador pode implantar a versão de volta para o estágio anterior (Desenvolvimento), garantindo sincronismo entre ambientes.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> Ao contrário de ferramentas legadas unidirecionais, o Fabric suporta backward deployment explicitamente.</li><li><strong>C e D:</strong> Não há destruição de workspaces nem exigência de SKUs de grande porte.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Recurso oficial do Fabric: Backward deployment permite sincronizar alterações de Teste de volta para Desenvolvimento.</div>",
    prompt: "Um desenvolvedor fez uma alteração emergencial diretamente no Workspace do estágio de 'Teste' de um Deployment Pipeline e precisa sincronizar essa alteração de volta para o estágio de 'Desenvolvimento'. Esse procedimento é suportado pelo Fabric?"
  },
  {
    id: "d1_q29",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Resolução de Conflitos na Sincronização Git do Fabric",
    question: "Ao tentar sincronizar as alterações de uma branch Git para o Workspace do Fabric, a interface indica um conflito de versão ('Conflict Detected'). Qual é a ação padrão recomendada na interface do Fabric para resolver o conflito?",
    options: [
      {
        id: "A",
        text: "O usuário deve escolher entre sobrescrever o workspace com o conteúdo do Git ('Accept incoming / Git') ou atualizar o Git com o conteúdo atual do workspace ('Keep local / Workspace').",
        isCorrect: true
      },
      {
        id: "B",
        text: "O Fabric exclui imediatamente o repositório Git para evitar inconsistências.",
        isCorrect: false
      },
      {
        id: "C",
        text: "A capacidade F-SKU é colocada em quarentena por 24 horas.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O conflito só pode ser resolvido com uma chamada de suporte à Microsoft.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Quando ocorrem alterações concorrentes no Git e no Workspace do Fabric, a interface de controle de código detecta o conflito e exige que o desenvolvedor resolva selecionando explicitamente se deseja aceitar os itens do Git (sobrescrevendo o workspace) ou manter os itens do workspace (gerando commit no Git).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsos alarmes que não correspondem ao fluxo de controle de versão do Fabric.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Conflito no Git do Fabric: Escolha explícita entre 'Accept Git' ou 'Keep Workspace'.</div>",
    prompt: "Ao tentar sincronizar as alterações de uma branch Git para o Workspace do Fabric, a interface indica um conflito de versão ('Conflict Detected'). Qual é a ação padrão recomendada na interface do Fabric para resolver o conflito?"
  },
  {
    id: "d1_q30",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "multi",
    title: "Artefatos NÃO Suportados por Deployment Pipelines",
    question: "Embora os Deployment Pipelines suportem a maioria dos artefatos do Fabric, alguns itens possuem restrições ou exigem gestão diferenciada. Quais DOIS itens abaixo possuem limitações ou não são promovidos da mesma forma que relatórios e modelos semânticos padrão? (Selecione 2 alternativas)",
    options: [
      {
        id: "A",
        text: "Dados físicos reais de tabelas armazenados no Lakehouse (apenas o esquema/metadados e atalhos são gerenciados no pipeline de ciclo de vida).",
        isCorrect: true
      },
      {
        id: "B",
        text: "Conexões locais de Gateway de Dados Pessoal (Personal Gateway)",
        isCorrect: true
      },
      {
        id: "C",
        text: "Modelos Semânticos do Power BI",
        isCorrect: false
      },
      {
        id: "D",
        text: "Relatórios Paginados e Relatórios Power BI",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Pipelines de implantação gerenciam definições e metadados de código analítico. Dados físicos reais em tabelas Delta do Lakehouse nunca são copiados entre ambientes de Dev e Prod pelo Deployment Pipeline (os dados pertencem ao armazenamento do estágio). Gateways de dados pessoais também não são gerenciáveis em pipelines corporativos.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C e D:</strong> Modelos Semânticos e Relatórios são 100% suportados por Deployment Pipelines desde a versão inicial.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Deployment Pipelines promovem METADADOS e CÓDIGO, não dados de tabelas físicas!</div>",
    prompt: "Embora os Deployment Pipelines suportem a maioria dos artefatos do Fabric, alguns itens possuem restrições ou exigem gestão diferenciada. Quais DOIS itens abaixo possuem limitações ou não são promovidos da mesma forma que relatórios e modelos semânticos padrão? (Selecione 2 alternativas)"
  },
  {
    id: "d1_q31",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Conceito de 'Domínios' (Fabric Domains) e Arquitetura Data Mesh",
    question: "Uma corporação multinacional deseja implementar uma arquitetura Data Mesh descentralizada no Microsoft Fabric, agrupando workspaces por unidades de negócio (ex: 'Finanças', 'Vendas', 'Operações') e delegando a administração aos responsáveis de negócio. Qual recurso nativo do Fabric atende a essa governança?",
    options: [
      {
        id: "A",
        text: "Domínios do Fabric (Fabric Domains)",
        isCorrect: true
      },
      {
        id: "B",
        text: "Grupos de distribuição de e-mail do Microsoft Exchange",
        isCorrect: false
      },
      {
        id: "C",
        text: "Pastas compartilhadas no OneDrive comercial",
        isCorrect: false
      },
      {
        id: "D",
        text: "Políticas de bloqueio de IP no Azure Active Directory",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Os Domínios do Fabric (Fabric Domains) foram criados especificamente para viabilizar arquiteturas Data Mesh. Eles permitem agrupar múltiplos Workspaces sob um domínio lógico de negócio (ex: Marketing, RH), permitindo que administradores de domínio definam proprietários, aprovem certificações de itens e gerenciem permissões de forma descentralizada.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Não têm relação com o agrupamento lógico de workspaces analíticos no Fabric.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Data Mesh no Fabric = Fabric Domains. Agrupa workspaces por área de negócio com administradores de domínio dedicados.</div>",
    prompt: "Uma corporação multinacional deseja implementar uma arquitetura Data Mesh descentralizada no Microsoft Fabric, agrupando workspaces por unidades de negócio (ex: 'Finanças', 'Vendas', 'Operações') e delegando a administração aos responsáveis de negócio. Qual recurso nativo do Fabric atende a essa governança?"
  },
  {
    id: "d1_q32",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Certificação vs Promoção de Itens no OneLake Data Hub",
    question: "No OneLake Data Hub, usuários corporativos precisam distinguir dados validados oficialmente pela equipe corporativa de dados de artefatos criados livremente por usuários para estudos rápidos. Quais são os dois níveis de endosso (Endorsement) disponíveis no Fabric e qual deles exige permissões administrativas para atribuição?",
    options: [
      {
        id: "A",
        text: "'Promovido' (Promoted - acessível a autores) e 'Certificado' (Certified - requer permissão explícita concedida pelo administrador do locatário).",
        isCorrect: true
      },
      {
        id: "B",
        text: "'Bronze' e 'Ouro', ambos atribuíveis por qualquer usuário Viewer.",
        isCorrect: false
      },
      {
        id: "C",
        text: "'Público' e 'Confidencial', controlados pelo firewall do Windows.",
        isCorrect: false
      },
      {
        id: "D",
        text: "'Aprovado' e 'Rejeitado', definidos automaticamente pelo antivírus.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric possui dois níveis de Endorsement: 1) Promoted: qualquer proprietário do item pode promover para destacar o artefato na organização; 2) Certified: o mais alto selo de confiança institucional, cuja permissão de aplicação é estritamente restrita a usuários autorizados configurados pelo Administrador de Locatário (Tenant Admin).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Bronze e Ouro são camadas de arquitetura Medallion, não status de endosso de catálogo.</li><li><strong>C e D:</strong> Conceitos inexistentes no catálogo do OneLake Data Hub.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Níveis de Endosso: Promoted (livre para donos do item) e Certified (exige autorização do Tenant Admin).</div>",
    prompt: "No OneLake Data Hub, usuários corporativos precisam distinguir dados validados oficialmente pela equipe corporativa de dados de artefatos criados livremente por usuários para estudos rápidos. Quais são os dois níveis de endosso (Endorsement) disponíveis no Fabric e qual deles exige permissões administrativas para atribuição?"
  },
  {
    id: "d1_q33",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "OneLake Data Hub como Ponto Central de Descoberta",
    question: "Um cientista de dados precisa encontrar todos os dados de vendas disponíveis na organização para treinar um modelo de machine learning, sem saber em quais workspaces esses dados residem. Onde ele deve pesquisar no portal do Microsoft Fabric?",
    options: [
      {
        id: "A",
        text: "No OneLake Data Hub, filtrando por tipo de item, endosso (Certified) ou domínio de negócio.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Abrindo todos os arquivos `.json` da pasta `_delta_log` no Notepad.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Verificando as tabelas temporárias na instância local do SQL Express.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Enviando um e-mail em massa para toda a empresa solicitando planilhas.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O OneLake Data Hub é o catálogo unificado de descoberta de dados do Fabric. Ele exibe todos os Lakehouses, Warehouses e Modelos Semânticos aos quais o usuário tem acesso ou que foram promovidos/certificados em qualquer workspace, permitindo filtragem por domínio, proprietário e rótulos de sensibilidade.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Práticas antiquadas que desconsideram o catálogo corporativo nativo do Fabric.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> OneLake Data Hub = Catálogo central de descoberta de dados e governança no Fabric.</div>",
    prompt: "Um cientista de dados precisa encontrar todos os dados de vendas disponíveis na organização para treinar um modelo de machine learning, sem saber em quais workspaces esses dados residem. Onde ele deve pesquisar no portal do Microsoft Fabric?"
  },
  {
    id: "d1_q34",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "multi",
    title: "Configurações de Locatário (Tenant Settings) Críticas para Governança",
    question: "Quais DUAS configurações de locatário (Tenant Settings) no portal de administração do Fabric devem ser restringidas para garantir que dados corporativos não sejam exportados externamente sem controle? (Selecione 2 alternativas)",
    options: [
      {
        id: "A",
        text: "Exportação de dados para arquivos Excel ou CSV (`Export data to Excel`)",
        isCorrect: true
      },
      {
        id: "B",
        text: "Publicar na Web aberta sem autenticação (`Publish to web (public)`)",
        isCorrect: true
      },
      {
        id: "C",
        text: "Ativar o tema escuro na interface web do Fabric",
        isCorrect: false
      },
      {
        id: "D",
        text: "Visualizar relatórios na tela do monitor do usuário",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Para evitar vazamento ou exfiltração de dados sensíveis, administradores de governança devem restringir: 1) 'Publish to web' (que cria links públicos anônimos na internet aberta sem credenciais) e 2) 'Export data to Excel / CSV' (que permite download local de tabelas analíticas).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C e D:</strong> Opções de interface e consumo básico que não apresentam risco de vazamento de dados.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Governança de dados no Admin Portal: Desativar 'Publish to web' e restringir 'Export to Excel' para grupos de segurança específicos.</div>",
    prompt: "Quais DUAS configurações de locatário (Tenant Settings) no portal de administração do Fabric devem ser restringidas para garantir que dados corporativos não sejam exportados externamente sem controle? (Selecione 2 alternativas)"
  },
  {
    id: "d1_q35",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Subdomínios (Subdomains) no Fabric",
    question: "Uma organização já estruturou o Domínio principal de 'Finanças'. Dentro de Finanças, existem equipes com necessidades distintas de governança: 'Contabilidade' e 'Planejamento Tributário'. Como o Fabric permite representar essa hierarquia dentro da governança de domínios?",
    options: [
      {
        id: "A",
        text: "Criando Subdomínios (Subdomains) subordinados ao domínio Finanças, herdando políticas e permitindo delegar administradores locais.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Criando assinaturas separadas do Azure para cada departamento.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Instalando instâncias diferentes do Windows Server na nuvem.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O Fabric não suporta níveis hierárquicos dentro de domínios.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric suporta Subdomínios (Subdomains). Um domínio pai pode conter subdomínios filhos para refletir a estrutura organizacional interna de uma diretoria, herdando a governança superior e permitindo administradores dedicados em cada subdivisão.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Incorretos; subdomínios são nativamente suportados na governança do Fabric.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Subdomínios permitem modelar estruturas corporativas complexas (ex: Finanças -> Contabilidade e Controladoria).</div>",
    prompt: "Uma organização já estruturou o Domínio principal de 'Finanças'. Dentro de Finanças, existem equipes com necessidades distintas de governança: 'Contabilidade' e 'Planejamento Tributário'. Como o Fabric permite representar essa hierarquia dentro da governança de domínios?"
  },
  {
    id: "d1_q36",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Auditoria de Atividades com Unified Audit Logs do Microsoft 365 / Purview",
    question: "Um auditor de segurança precisa inspecionar quem executou comandos de exclusão ou alteração de permissões em um Lakehouse crítico nos últimos 30 dias. Onde essas atividades administrativas do Fabric são registradas centralizadamente?",
    options: [
      {
        id: "A",
        text: "No Microsoft Purview Audit (Logs Unificados de Auditoria do Microsoft 365 / Fabric Activity Events API).",
        isCorrect: true
      },
      {
        id: "B",
        text: "No arquivo `c:\\windows\\system32\\drivers\\etc\\hosts` dos analistas.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Na tabela temporária de log do SQL Server 2008.",
        isCorrect: false
      },
      {
        id: "D",
        text: "No histórico do navegador Google Chrome do desenvolvedor.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Todas as ações do Microsoft Fabric (criação, edição, exclusão de itens, execução de consultas, exportações e alterações de permissões) são registradas nos Logs Unificados de Auditoria do Microsoft Purview / Microsoft 365 e podem ser consultadas via portal de conformidade ou pela API Fabric Activity Events.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Locais locais e sem relação com a governança corporativa em nuvem.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Auditoria do Fabric = Microsoft Purview Unified Audit Log e Fabric Activity Events REST API.</div>",
    prompt: "Um auditor de segurança precisa inspecionar quem executou comandos de exclusão ou alteração de permissões em um Lakehouse crítico nos últimos 30 dias. Onde essas atividades administrativas do Fabric são registradas centralizadamente?"
  },
  {
    id: "d1_q37",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Prevenção contra Perda de Dados (DLP) para Fabric",
    question: "Como as Políticas de Prevenção contra Perda de Dados (DLP Policies) do Microsoft Purview protegem dados confidenciais (ex: números de previdência social, cartões de crédito) dentro do Microsoft Fabric?",
    options: [
      {
        id: "A",
        text: "Detectam automaticamente informações confidenciais em Lakehouses e modelos semânticos, gerando alertas no portal de segurança e bloqueando o compartilhamento não autorizado.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Deletam o Lakehouse automaticamente se encontrarem qualquer número de CPF.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Desconectam os servidores da Microsoft da rede elétrica mundial.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Formatam o disco rígido do computador do usuário que fez o upload.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> As políticas de DLP do Microsoft Purview examinam os metadados e conteúdos do Fabric para identificar tipos de informações confidenciais (SITs). Ao detectar violações, a política aplica ações como dicas de política (Policy Tips), alertas de compliance e restrições de compartilhamento externo.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Efeitos destrutivos e absurdos.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> DLP no Fabric = Detecção automática de dados confidenciais (PII, PCI) com alertas de conformidade e restrições de compartilhamento.</div>",
    prompt: "Como as Políticas de Prevenção contra Perda de Dados (DLP Policies) do Microsoft Purview protegem dados confidenciais (ex: números de previdência social, cartões de crédito) dentro do Microsoft Fabric?"
  },
  {
    id: "d1_q38",
    domain: "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)",
    type: "single",
    title: "Regra de Resiliência de Armazenamento e BCDR no OneLake",
    question: "O OneLake armazena dados em múltiplos datacenters para garantir durabilidade e alta disponibilidade contra desastres geográficos. Qual é a configuração padrão de redundância de armazenamento subjacente utilizada pelo OneLake nas regiões primárias do Azure?",
    options: [
      {
        id: "A",
        text: "LRS (Locally Redundant Storage) ou ZRS (Zone-Redundant Storage) com suporte a failover geográfico de capacidade de acordo com a região.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Um único disco rígido magnético conectado via cabo USB 2.0 em um rack em Redmond.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Fita magnética LTO-4 sem backup secundário.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Memória volátil que é zerada a cada reinicialização semanal do cluster.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O OneLake é construído sobre a infraestrutura do Azure Data Lake Storage Gen2 (ADLS Gen2), oferecendo redundância de nível corporativo (LRS ou ZRS com 3 cópias em zonas de disponibilidade separadas) e integração com estratégias de BCDR (Business Continuity & Disaster Recovery).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Descrições sem qualquer fundamento técnico.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> OneLake BCDR = Infraestrutura de armazenamento baseada em ADLS Gen2 com replicação por zonas (ZRS/LRS) e alta disponibilidade.</div>",
    prompt: "O OneLake armazena dados em múltiplos datacenters para garantir durabilidade e alta disponibilidade contra desastres geográficos. Qual é a configuração padrão de redundância de armazenamento subjacente utilizada pelo OneLake nas regiões primárias do Azure?"
  },
  {
    id: "d2_q01",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Limite Máximo da Atividade Lookup no Data Factory",
    question: "Um engenheiro de dados está criando um Data Pipeline no Microsoft Fabric para carregar uma lista de tabelas a serem processadas usando uma atividade Lookup. Quantas linhas no máximo a atividade Lookup pode retornar em uma única execução?",
    options: [
      {
        id: "A",
        text: "1.000 linhas",
        isCorrect: false
      },
      {
        id: "B",
        text: "5.000 linhas",
        isCorrect: true
      },
      {
        id: "C",
        text: "50.000 linhas",
        isCorrect: false
      },
      {
        id: "D",
        text: "100.000 linhas",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A atividade Lookup nos Data Pipelines do Microsoft Fabric possui um limite rígido documentado de no máximo 5.000 linhas (ou 4 MB de dados). Se o conjunto de dados retornado ultrapassar esse volume, apenas as primeiras 5.000 linhas são retornadas.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A (1.000 linhas):</strong> Menor do que o limite da atividade.</li><li><strong>C e D (50.000 e 100.000 linhas):</strong> Limites inexistentes para a atividade Lookup. Cargas volumosas exigem processamento via Script, Dataflow ou Spark.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Limite do Lookup: 5.000 linhas ou 4 MB de tamanho de buffer JSON.</div>",
    prompt: "Um engenheiro de dados está criando um Data Pipeline no Microsoft Fabric para carregar uma lista de tabelas a serem processadas usando uma atividade Lookup. Quantas linhas no máximo a atividade Lookup pode retornar em uma única execução?"
  },
  {
    id: "d2_q02",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Paralelismo Máximo na Atividade ForEach",
    question: "Ao iterar sobre um conjunto de 100 arquivos usando a atividade ForEach em um Data Pipeline do Fabric, qual é o valor máximo permitido para a propriedade `batchCount` (paralelismo simultâneo)?",
    options: [
      {
        id: "A",
        text: "10",
        isCorrect: false
      },
      {
        id: "B",
        text: "20",
        isCorrect: false
      },
      {
        id: "C",
        text: "50",
        isCorrect: true
      },
      {
        id: "D",
        text: "100",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A atividade ForEach suporta execução paralela com um `batchCount` máximo de 50 iterações simultâneas. Se o switch 'Sequential' estiver ativado, o batchCount é ignorado e executa 1 por 1.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A e B:</strong> Valores válidos, mas não representam o teto máximo permitido de concorrência.</li><li><strong>D:</strong> O Fabric limita a concorrência a no máximo 50 para evitar esgotamento prematuro de recursos.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> ForEach batchCount máximo = 50 iterações concorrentes.</div>",
    prompt: "Ao iterar sobre um conjunto de 100 arquivos usando a atividade ForEach em um Data Pipeline do Fabric, qual é o valor máximo permitido para a propriedade `batchCount` (paralelismo simultâneo)?"
  },
  {
    id: "d2_q03",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Diferença entre Atividade Web e Atividade WebHook",
    question: "Você precisa integrar um Data Pipeline com um serviço externo de aprovação assíncrono que leva até 40 minutos para responder com um token de liberação. Qual atividade de pipeline deve ser utilizada?",
    options: [
      {
        id: "A",
        text: "Atividade Web com timeout de 1 minuto.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Atividade WebHook, pois ela envia uma URL de callback e aguarda até que o serviço externo faça uma requisição POST de volta com o status concluído.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Atividade Get Metadata conectada a uma pasta vazia.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Atividade Copy em loop infinito.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A atividade WebHook é projetada especificamente para processos assíncronos de longa duração. Ao invocar a API de destino, ela inclui uma URL de retorno (`callBackUri`). A execução do pipeline pausa até que o serviço externo chame essa URL de volta com o payload de resposta.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> A atividade Web é síncrona e possui timeout estrito de requisição HTTP (geralmente até 10 minutos).</li><li><strong>C e D:</strong> Atividades que não realizam integração de callback HTTP.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Web = Chamada síncrona imediata; WebHook = Chamada assíncrona com espera de callBackUri.</div>",
    prompt: "Você precisa integrar um Data Pipeline com um serviço externo de aprovação assíncrono que leva até 40 minutos para responder com um token de liberação. Qual atividade de pipeline deve ser utilizada?"
  },
  {
    id: "d2_q04",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Mecanismo de Fast Copy nos Dataflows Gen2",
    question: "Qual é a principal função do recurso 'Fast Copy' (Cópia Rápida) nos Dataflows Gen2 do Microsoft Fabric?",
    options: [
      {
        id: "A",
        text: "Utilizar a engine distribuída de ingestão do backend (semelhante à Copy Activity) para carregar grandes volumes de dados de fontes externas diretamente para o Staging Lakehouse sem sobrecarregar a engine de Mashup do Power Query.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Ignorar a validação de tipos de dados e inserir registros corrompidos na tabela final.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Excluir os dados da fonte original após a leitura.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Comprimir todos os dados em arquivos MP3 para economizar espaço.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fast Copy nos Dataflows Gen2 contorna as limitações de memória do motor local de Mashup do Power Query ao delegar a cópia de grandes tabelas relacionais ou arquivos para a infraestrutura escalável do Data Factory, gravando em alta velocidade no Lakehouse de Staging.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Efeitos incorretos e sem embasamento técnico.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Fast Copy no Dataflow Gen2 acelera a ingestão massiva gravando em Staging antes das transformações do Power Query.</div>",
    prompt: "Qual é a principal função do recurso 'Fast Copy' (Cópia Rápida) nos Dataflows Gen2 do Microsoft Fabric?"
  },
  {
    id: "d2_q05",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Lakehouse de Preparo (Staging Lakehouse) dos Dataflows Gen2",
    question: "Ao criar e executar um Dataflow Gen2 em um Workspace do Fabric, dois artefatos adicionais com sufixos técnicos são criados automaticamente no Workspace. Quais são esses artefatos e qual a sua finalidade?",
    options: [
      {
        id: "A",
        text: "Dois bancos de dados SQL Server Express locais.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Um Lakehouse de Staging e um SQL Analytics Endpoint de Staging, utilizados internamente pelo motor do Fabric para materializar dados intermediários e acelerar transformações com compute SQL.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Dois relatórios visuais de demonstração do Power BI.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Duas conexões ODBC legadas com o MS Access.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Os Dataflows Gen2 utilizam um Lakehouse de Staging dedicado (e seu respectivo SQL Endpoint). As etapas de transformação do Power Query são materializadas no OneLake em Delta Parquet, e as consultas subsequentes utilizam o motor T-SQL do SQL Endpoint para executar query folding acelerado por hardware.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A, C e D:</strong> Artefatos que não fazem parte da arquitetura interna dos Dataflows Gen2.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Dataflows Gen2 geram automaticamente um Lakehouse e SQL Endpoint de Staging para computação intermediária acelerada.</div>",
    prompt: "Ao criar e executar um Dataflow Gen2 em um Workspace do Fabric, dois artefatos adicionais com sufixos técnicos são criados automaticamente no Workspace. Quais são esses artefatos e qual a sua finalidade?"
  },
  {
    id: "d2_q06",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Dataflows Gen2 vs Apache Spark Notebooks",
    question: "Uma organização tem dois perfis de profissionais de dados: analistas de negócios que dominam Power Query e engenheiros de dados que desenvolvem pipelines analíticos de alta complexidade com machine learning e tratamento de petabytes. Qual é a recomendação oficial de uso no Fabric?",
    options: [
      {
        id: "A",
        text: "Usar Dataflows Gen2 para transformações no-code/low-code em nível departamental e Spark Notebooks para engenharia de dados em grande escala e transformações complexas com PySpark/Scala.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Proibir o uso de Spark e forçar todos a usar apenas Dataflows Gen2.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Usar apenas T-SQL e descartar Notebooks e Dataflows.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Exportar os dados para planilhas manuais compartilhadas por e-mail.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A Microsoft recomenda Dataflows Gen2 para usuários que preferem desenvolvimento visual baseado em Power Query com facilidade de manutenção para volumes médios. Para grandes volumes (TB/PB), algoritmos complexos, machine learning e concorrência massiva, Spark Notebooks é a ferramenta primordial.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Recomendações contrárias às diretrizes oficiais do exame DP-700.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Diretriz oficial: Low-Code/Power Query -> Dataflows Gen2; Big Data/PySpark/Escalabilidade -> Spark Notebooks.</div>",
    prompt: "Uma organização tem dois perfis de profissionais de dados: analistas de negócios que dominam Power Query e engenheiros de dados que desenvolvem pipelines analíticos de alta complexidade com machine learning e tratamento de petabytes. Qual é a recomendação oficial de uso no Fabric?"
  },
  {
    id: "d2_q07",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Carga Incremental com Tabela de Watermark em Pipelines",
    question: "Um pipeline do Fabric precisa realizar carga incremental a cada hora lendo dados de uma tabela SQL corporativa de 500 milhões de registros. Como o padrão de Watermark com a atividade Lookup e Copy deve ser implementado?",
    options: [
      {
        id: "A",
        text: "Fazer SELECT * sem cláusula WHERE e sobrescrever a tabela de destino inteira a cada hora.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Consultar a última data/hora processada na tabela de controle (Watermark), buscar novos registros com `WHERE DataModificacao > @UltimaData`, gravar no destino e atualizar a tabela de controle com o novo timestamp.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Apagar a tabela SQL de origem após cada execução.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Executar o pipeline apenas uma vez por ano.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O padrão Watermark é a técnica padrão de engenharia para cargas incrementais: 1) Lookup lê a última marca d'água (`OldWatermark`), 2) Lookup calcula a nova marca máxima (`NewWatermark`), 3) Copy transfere dados entre `OldWatermark` e `NewWatermark`, 4) Script/Stored Procedure atualiza a tabela de controle.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> Carga plena horária em 500M de linhas causa sobrecarga severa e desperdício de CUs.</li><li><strong>C:</strong> Deletar dados da fonte de origem é inaceitável em ambientes corporativos.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Padrão Watermark: Old Watermark -> Copy Delta -> Update New Watermark.</div>",
    prompt: "Um pipeline do Fabric precisa realizar carga incremental a cada hora lendo dados de uma tabela SQL corporativa de 500 milhões de registros. Como o padrão de Watermark com a atividade Lookup e Copy deve ser implementado?"
  },
  {
    id: "d2_q08",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "VNet Data Gateway vs On-Premises Data Gateway",
    question: "Sua empresa possui um banco de dados Azure SQL Database protegido dentro de uma Rede Virtual (VNet) sem IP público. Qual solução de gateway nativa de nuvem elimina a necessidade de gerenciar máquinas virtuais locais para conexões do Data Factory e Dataflows?",
    options: [
      {
        id: "A",
        text: "On-Premises Data Gateway em modo pessoal.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Virtual Network (VNet) Data Gateway gerenciado pela Microsoft.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Cabo crossover Ethernet conectado ao datacenter.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Habilitar portas 1433 abertas para toda a internet sem autenticação.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O VNet Data Gateway é um recurso totalmente gerenciado (PaaS) que conecta serviços de nuvem do Fabric (Data Factory, Dataflows Gen2) a serviços protegidos por VNets do Azure sem a necessidade de instalar, manter ou aplicar patches em máquinas virtuais de gateway locais.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> O gateway On-Premises exige manutenção e hosting de VMs dedicadas pelo cliente.</li><li><strong>C e D:</strong> Inseguros e inviáveis em nuvem.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> VNet Data Gateway = Conectividade segura e gerenciada para fontes protegidas por VNets do Azure sem gerenciar VMs.</div>",
    prompt: "Sua empresa possui um banco de dados Azure SQL Database protegido dentro de uma Rede Virtual (VNet) sem IP público. Qual solução de gateway nativa de nuvem elimina a necessidade de gerenciar máquinas virtuais locais para conexões do Data Factory e Dataflows?"
  },
  {
    id: "d2_q09",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "multi",
    title: "Variáveis do Sistema em Expressões de Pipelines de Dados",
    question: "Quais DUAS variáveis de sistema do Fabric Data Factory podem ser acessadas dinamicamente dentro de expressões de pipeline via sintaxe `@pipeline()....`? (Selecione 2 alternativas)",
    options: [
      {
        id: "A",
        text: "`@pipeline().DataFactory`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`@pipeline().TriggerTime`",
        isCorrect: true
      },
      {
        id: "C",
        text: "`@pipeline().UserPassword`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`@pipeline().WindowsKernelVersion`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O mecanismo de expressões de pipelines expõe variáveis do sistema sob o namespace `@pipeline()`, incluindo `@pipeline().Pipeline`, `@pipeline().RunId`, `@pipeline().TriggerTime` e `@pipeline().DataFactory`. Senhas e versões de kernel nunca são expostas.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C e D:</strong> Não são variáveis válidas de sistema.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Variáveis do sistema comuns: `RunId`, `TriggerTime`, `Pipeline`, `DataFactory`.</div>",
    prompt: "Quais DUAS variáveis de sistema do Fabric Data Factory podem ser acessadas dinamicamente dentro de expressões de pipeline via sintaxe `@pipeline()....`? (Selecione 2 alternativas)"
  },
  {
    id: "d2_q10",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Tratamento de Falhas com Bloco Try-Catch em Pipelines",
    question: "Como um engenheiro de dados deve modelar o equivalente a um bloco 'Try-Catch' para capturar erros em uma atividade de Pipeline e enviar uma notificação para o Teams caso ocorra falha?",
    options: [
      {
        id: "A",
        text: "Adicionar um bloco try-catch em JavaScript no navegador.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Conectar a atividade de execução (Try) a uma atividade de notificação (Catch) utilizando o conector de dependência condicional 'Upon Failure' (vermelho).",
        isCorrect: true
      },
      {
        id: "C",
        text: "Configurar o pipeline para reiniciar em loop infinito sempre que der erro.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Não é possível tratar erros em pipelines do Fabric.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Em Data Pipelines do Fabric, o fluxo de controle utiliza conectores condicionais de dependência: Verde (Upon Success), Vermelho (Upon Failure), Azul (Upon Completion) e Cinza (Upon Skip). Para criar tratamento de erro, conecta-se a saída 'Upon Failure' à atividade que envia o alerta ou executa rollback.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A, C e D:</strong> Métodos inválidos no modelo de orquestração de Data Factory.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Conectores de Pipeline: Upon Success (Verde), Upon Failure (Vermelho), Upon Completion (Azul).</div>",
    prompt: "Como um engenheiro de dados deve modelar o equivalente a um bloco 'Try-Catch' para capturar erros em uma atividade de Pipeline e enviar uma notificação para o Teams caso ocorra falha?"
  },
  {
    id: "d2_q11",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Passagem de Parâmetros de Pipeline para Notebook Spark",
    question: "Um engenheiro de dados deseja parametrizar um Notebook Spark para que o ano de processamento seja fornecido dinamicamente pela atividade 'Notebook' em um Data Pipeline. O que deve ser configurado no Notebook Spark para receber esse parâmetro?",
    options: [
      {
        id: "A",
        text: "Marcar a primeira célula de código do Notebook com a tag de célula 'parameters'.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Escrever a variável no arquivo `config.ini` no disco C: do servidor.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Instalar o pacote `sys.argv` via prompt do MS-DOS.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O Fabric não suporta passagem de parâmetros para Notebooks.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> No Apache Spark do Fabric (assim como no Databricks/Synapse), a parametrização de Notebooks é realizada aplicando a tag de célula 'parameters' na célula onde as variáveis padrão são declaradas. O pipeline injeta uma célula subsequente com os valores passados em tempo de execução.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Práticas incorretas; o padrão oficial de parametrização é a tag 'parameters'.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Parametrização de Notebooks no Fabric: Ativar o painel de propriedades da célula e adicionar a tag 'parameters'.</div>",
    prompt: "Um engenheiro de dados deseja parametrizar um Notebook Spark para que o ano de processamento seja fornecido dinamicamente pela atividade 'Notebook' em um Data Pipeline. O que deve ser configurado no Notebook Spark para receber esse parâmetro?"
  },
  {
    id: "d2_q12",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Atividade Until para Polling de Status",
    question: "Um pipeline do Fabric precisa disparar um processo em uma API REST e aguardar em loop periódico (a cada 30 segundos) até que um endpoint retorne o status `'COMPLETED'`. Qual atividade de controle de fluxo é a mais indicada?",
    options: [
      {
        id: "A",
        text: "Atividade If Condition sem ramificação.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Atividade Until contendo uma atividade Web e uma atividade Wait em seu corpo, iterando até que a expressão booleana de conclusão seja avaliada como verdadeira.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Atividade Switch com 50 opções estáticas.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Atividade Fail para forçar a parada do locatário.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A atividade Until funciona como um loop `do-until`: ela executa as atividades internas e avalia uma condição ao final. Se a condição for falsa, repete a execução até atingir o critério de parada (ou timeout configurado), sendo o padrão ideal para polling com Wait intermediário.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A e C:</strong> Estruturas de ramificação simples que não realizam repetições em loop.</li><li><strong>D:</strong> A atividade Fail aborta o pipeline deliberadamente com erro.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Loop de espera/polling em pipeline: Atividade Until com atividades Web + Wait.</div>",
    prompt: "Um pipeline do Fabric precisa disparar um processo em uma API REST e aguardar em loop periódico (a cada 30 segundos) até que um endpoint retorne o status `'COMPLETED'`. Qual atividade de controle de fluxo é a mais indicada?"
  },
  {
    id: "d2_q13",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Atividade Invoke Pipeline (Execute Pipeline)",
    question: "Para criar uma arquitetura modular de orquestração de dados, você deseja que um 'Pipeline Mestre' chame múltiplos 'Pipelines Filhos'. Qual propriedade na atividade Execute Pipeline define se o pipeline pai aguarda ou não o término do pipeline filho?",
    options: [
      {
        id: "A",
        text: "Wait on completion (Aguardar conclusão - booleano)",
        isCorrect: true
      },
      {
        id: "B",
        text: "Auto restart on error",
        isCorrect: false
      },
      {
        id: "C",
        text: "Direct Lake Acceleration mode",
        isCorrect: false
      },
      {
        id: "D",
        text: "Run in background thread only",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Na atividade Execute Pipeline (Invoke Pipeline), a opção 'Wait on completion' determina se a execução é síncrona (o pipeline pai aguarda o pipeline filho finalizar para seguir para a próxima atividade) ou assíncrona ('fire-and-forget').</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Propriedades inexistentes ou irrelevantes nessa atividade.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Execute Pipeline: 'Wait on completion' ativado = síncrono; desativado = assíncrono.</div>",
    prompt: "Para criar uma arquitetura modular de orquestração de dados, você deseja que um 'Pipeline Mestre' chame múltiplos 'Pipelines Filhos'. Qual propriedade na atividade Execute Pipeline define se o pipeline pai aguarda ou não o término do pipeline filho?"
  },
  {
    id: "d2_q14",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Gatilhos de Agendamento vs Gatilhos de Janela de Queda (Tumbling Window)",
    question: "Um engenheiro de dados precisa reprocessar dados históricos fatiados fatia por fatia (slice-by-slice) respeitando rigorosamente a ordem cronológica do passado e garantindo concorrência máxima de 1 fatia por vez. Qual tipo de gatilho (Trigger) deve ser configurado no pipeline?",
    options: [
      {
        id: "A",
        text: "Gatilho de Agendamento Básico (Schedule Trigger)",
        isCorrect: false
      },
      {
        id: "B",
        text: "Gatilho de Janela de Queda (Tumbling Window Trigger) com dependência de auto-concorrência (`maxConcurrency = 1`).",
        isCorrect: true
      },
      {
        id: "C",
        text: "Gatilho de Evento de Armazenamento (Storage Event Trigger)",
        isCorrect: false
      },
      {
        id: "D",
        text: "Disparo manual via botão 'Run Now' no navegador.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Tumbling Window Triggers disparam em intervalos contíguos e não sobrepostos. Possuem recursos exclusivos para cenários de reprocessamento histórico (backfill) e dependências temporais estritas (ex: a fatia de 11:00 só roda após a conclusão da fatia de 10:00 com maxConcurrency=1).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> Schedule Triggers disparam em horários fixos sem rastreamento de fatias históricas.</li><li><strong>C:</strong> Storage Event Triggers reagem à chegada de novos arquivos (blobs criados/deletados).</li><li><strong>D:</strong> Inviável para repetição cronológica sistemática.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Backfill e execução sequencial rigorosa de fatias temporais = Tumbling Window Trigger.</div>",
    prompt: "Um engenheiro de dados precisa reprocessar dados históricos fatiados fatia por fatia (slice-by-slice) respeitando rigorosamente a ordem cronológica do passado e garantindo concorrência máxima de 1 fatia por vez. Qual tipo de gatilho (Trigger) deve ser configurado no pipeline?"
  },
  {
    id: "d2_q15",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Criptografia de Credenciais e Azure Key Vault nos Conectores",
    question: "Ao criar uma conexão para um banco de dados externo Oracle em um Data Pipeline, qual é a melhor prática recomendada pela Microsoft para gerenciar a senha do usuário sem expô-la na interface nem gravá-la em código?",
    options: [
      {
        id: "A",
        text: "Armazenar a senha no Azure Key Vault e referenciar o segredo na conexão do pipeline utilizando uma Identidade Gerenciada ou Service Principal.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Escrever a senha na descrição pública da tabela no OneLake.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Gravar a senha no arquivo `.gitignore` do repositório.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Criar um usuário com senha vazia no banco Oracle.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A prática padrão de segurança corporativa é armazenar segredos no Azure Key Vault. O Fabric pode se conectar ao Key Vault para obter credenciais dinamicamente em tempo de execução sem persistir senhas em texto puro nos artefatos.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Práticas inseguras que violam os padrões de conformidade.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Gestão de senhas e segredos no Fabric = Azure Key Vault integration.</div>",
    prompt: "Ao criar uma conexão para um banco de dados externo Oracle em um Data Pipeline, qual é a melhor prática recomendada pela Microsoft para gerenciar a senha do usuário sem expô-la na interface nem gravá-la em código?"
  },
  {
    id: "d2_q16",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "multi",
    title: "Formatos de Destino Suportados Nativamente na Copy Activity",
    question: "Quais DOIS destinos analíticos internos do Microsoft Fabric podem receber dados gravados diretamente por uma atividade Copy em um Data Pipeline? (Selecione 2 alternativas)",
    options: [
      {
        id: "A",
        text: "Tabelas do Lakehouse (Delta Parquet)",
        isCorrect: true
      },
      {
        id: "B",
        text: "Tabelas do Fabric Warehouse (via ingestão relacional otimizada)",
        isCorrect: true
      },
      {
        id: "C",
        text: "Arquivo binário executável `.EXE` do Windows",
        isCorrect: false
      },
      {
        id: "D",
        text: "Disquete magnético de 3,5 polegadas virtual",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A Copy Activity do Fabric Data Factory possui conectores nativos de destino otimizados para: Lakehouse (gravando diretamente em tabelas Delta ou arquivos), Warehouse (usando ingestão relacional massiva), KQL Database e Mirrored Databases.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C e D:</strong> Formatos não suportados e fictícios.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Destinos primários de pipeline no Fabric: Lakehouse, Warehouse e KQL Database.</div>",
    prompt: "Quais DOIS destinos analíticos internos do Microsoft Fabric podem receber dados gravados diretamente por uma atividade Copy em um Data Pipeline? (Selecione 2 alternativas)"
  },
  {
    id: "d2_q17",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Mapeamento Dinâmico de Esquema na Copy Activity",
    question: "Um pipeline precisa copiar dados de 50 tabelas de origens diferentes para o Lakehouse de destino sem que o desenvolvedor tenha que configurar o mapeamento coluna por coluna para cada tabela individualmente. Qual recurso da Copy Activity permite essa flexibilidade?",
    options: [
      {
        id: "A",
        text: "Mapeamento Automático de Esquema (Auto-mapping / Schema Drift) sem mapeamento estático explícito na guia Mapping.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Obrigatoriedade de escrever 50 arquivos XML com esquemas XSD.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Criação de um trigger T-SQL para cada coluna da tabela.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Não é possível copiar tabelas sem mapear todas as colunas manualmente.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Ao deixar a guia de mapeamento vazia ou utilizar parâmetros dinâmicos na Copy Activity, o motor adota o mapeamento automático por nome de coluna (Auto-mapping) e suporta Schema Drift, permitindo reutilizar uma única atividade Copy genérica para dezenas de tabelas.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Afirmações incorretas sobre as capacidades do Data Factory.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Pipelines genéricos de cópia utilizam Auto-mapping / Schema Drift para reutilização de atividades.</div>",
    prompt: "Um pipeline precisa copiar dados de 50 tabelas de origens diferentes para o Lakehouse de destino sem que o desenvolvedor tenha que configurar o mapeamento coluna por coluna para cada tabela individualmente. Qual recurso da Copy Activity permite essa flexibilidade?"
  },
  {
    id: "d2_q18",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Atividade Script vs Stored Procedure em Pipelines",
    question: "Quando um desenvolvedor deve preferir a atividade 'Script' em vez da atividade 'Stored Procedure' ao executar comandos SQL no Fabric Warehouse a partir de um Data Pipeline?",
    options: [
      {
        id: "A",
        text: "Quando precisa executar comandos DDL/DML arbitrários (como `CREATE TABLE AS SELECT`, `TRUNCATE`, ou múltiplos comandos em lote) sem a necessidade de criar previamente um objeto de stored procedure permanente no banco.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Quando quer compilar código C# nativo no banco.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Quando precisa reiniciar a máquina do servidor SQL.",
        isCorrect: false
      },
      {
        id: "D",
        text: "A atividade Script foi descontinuada e não deve ser usada.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A atividade 'Script' é versátil: ela aceita consultas T-SQL diretas, múltiplos comandos DDL/DML, instruções como `CREATE TABLE AS SELECT (CTAS)` e pode retornar conjuntos de resultados, dispensando a criação e manutenção de objetos de procedure persistidos quando não forem necessários.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas declarações sem suporte na documentação oficial.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Atividade Script = Execução de SQL direto, DDL flexível e batches T-SQL no Warehouse.</div>",
    prompt: "Quando um desenvolvedor deve preferir a atividade 'Script' em vez da atividade 'Stored Procedure' ao executar comandos SQL no Fabric Warehouse a partir de um Data Pipeline?"
  },
  {
    id: "d2_q19",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Starter Pools vs Custom Pools no Fabric Spark",
    question: "Por que os Starter Pools (pools iniciais gerenciados pela Microsoft) oferecem um tempo de inicialização de sessão de Notebook quase instantâneo (< 10 segundos) em comparação com Custom Pools?",
    options: [
      {
        id: "A",
        text: "Porque eles mantêm nós computacionais previamente aquecidos e provisionados em standby com tamanhos de nós padronizados.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Porque eles não usam o Apache Spark, apenas uma biblioteca Python compilada.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Porque eles nunca executam código real no cluster.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Porque os dados são salvos em memória flash do navegador.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Os Starter Pools são pools elásticos gerenciados pelo Fabric que mantêm máquinas virtuais pré-alocadas e aquecidas em background. Quando um usuário anexa uma sessão de notebook a um Starter Pool, os executores Spark inicializam em poucos segundos sem o tempo habitual de provisionamento de VM (que pode levar de 3 a 5 minutos em pools customizados).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Afirmações incorretas sobre a arquitetura do Spark no Fabric.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Starter Pools no Fabric = Clusters Spark pré-aquecidos para inicialização em menos de 10 segundos.</div>",
    prompt: "Por que os Starter Pools (pools iniciais gerenciados pela Microsoft) oferecem um tempo de inicialização de sessão de Notebook quase instantâneo (< 10 segundos) em comparação com Custom Pools?"
  },
  {
    id: "d2_q20",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Mecanismo Velox (Native Execution Engine)",
    question: "O que é o Native Execution Engine (baseado no projeto Velox) no Apache Spark do Microsoft Fabric e qual é o seu principal benefício de desempenho?",
    options: [
      {
        id: "A",
        text: "É uma biblioteca JavaScript para desenhar gráficos 3D no notebook.",
        isCorrect: false
      },
      {
        id: "B",
        text: "É uma engine de vetorização de baixo nível escrita em C++ que substitui os operadores tradicionais da JVM por execução colunar nativa com instruções SIMD, acelerando consultas e reduzindo o consumo de CUs.",
        isCorrect: true
      },
      {
        id: "C",
        text: "É um antivírus embutido no Spark para verificar arquivos corrompidos.",
        isCorrect: false
      },
      {
        id: "D",
        text: "É uma extensão do Excel instalada no nó mestre do cluster.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Native Execution Engine do Fabric Spark é construído sobre o Velox (motor open-source C++ colunar). Ele executa planos de consulta Spark SQL diretamente em código nativo de máquina usando vetorização SIMD de CPU, contornando a sobrecarga do garbage collector e interpretação de bytecode da JVM (Java Virtual Machine), acelerando drasticamente consultas analíticas pesadas.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A, C e D:</strong> Falsas analogias técnicas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Velox Native Execution Engine = Execução nativa colunar em C++ com instruções SIMD no Spark do Fabric.</div>",
    prompt: "O que é o Native Execution Engine (baseado no projeto Velox) no Apache Spark do Microsoft Fabric e qual é o seu principal benefício de desempenho?"
  },
  {
    id: "d2_q21",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Estratégia de Broadcast Hash Join e Limite Padrão",
    question: "Em uma consulta PySpark que realiza a junção de uma tabela de fatos com 1 bilhão de linhas e uma tabela de dimensão com 8 MB de tamanho, o Spark opta automaticamente por um Broadcast Hash Join. Qual é o limite de tamanho de tabela padrão (`spark.sql.autoBroadcastJoinThreshold`) para essa decisão automática?",
    options: [
      {
        id: "A",
        text: "1 MB",
        isCorrect: false
      },
      {
        id: "B",
        text: "10 MB",
        isCorrect: true
      },
      {
        id: "C",
        text: "1 GB",
        isCorrect: false
      },
      {
        id: "D",
        text: "10 GB",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O parâmetro `spark.sql.autoBroadcastJoinThreshold` tem o valor padrão de 10 MB (10.485.760 bytes). Quando uma das tabelas de junção for menor ou igual a esse tamanho, o Spark transmite a tabela inteira para todos os executores, eliminando a dispendiosa fase de Shuffle da tabela de fatos.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> 1 MB é muito conservador.</li><li><strong>C e D:</strong> Fazer broadcast de 1 GB ou 10 GB sobrecarregaria a memória do Driver e causaria erros de OutOfMemory (OOM).</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> `autoBroadcastJoinThreshold` padrão no Spark = 10 MB. Broadcast Join evita Shuffle de dados na rede.</div>",
    prompt: "Em uma consulta PySpark que realiza a junção de uma tabela de fatos com 1 bilhão de linhas e uma tabela de dimensão com 8 MB de tamanho, o Spark opta automaticamente por um Broadcast Hash Join. Qual é o limite de tamanho de tabela padrão (`spark.sql.autoBroadcastJoinThreshold`) para essa decisão automática?"
  },
  {
    id: "d2_q22",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Adaptive Query Execution (AQE) e Tratamento de Skew Join",
    question: "Durante a execução de um Sort Merge Join em um job Spark no Fabric, uma partição contém 80% de todas as chaves de junção, fazendo com que um único executor trabalhe por horas enquanto os demais ficam ociosos. Qual recurso do Spark 3.x resolve essa assimetria de partição automaticamente em tempo de execução?",
    options: [
      {
        id: "A",
        text: "AQE Skew Join (`spark.sql.adaptive.skewJoin.enabled = true`), que divide a partição assimétrica em sub-partições menores dinamicamente.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Desativar o cluster Spark e ligar uma máquina física com mais núcleos.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Usar a função `RAND()` na chave primária da tabela relacional.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Substituir o PySpark por código puro em linguagem Pascal.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Adaptive Query Execution (AQE) com detecção de Skew Join identifica partições desbalanceadas após a fase de shuffle e divide automaticamente as partições pesadas em pedaços menores (sub-partições), distribuindo-os uniformemente entre múltiplos executores sem alteração manual no código.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Soluções inviáveis e incorretas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> AQE Skew Join resolve o gargalo de assimetria de partições (Data Skew) dividindo partições volumosas dinamicamente.</div>",
    prompt: "Durante a execução de um Sort Merge Join em um job Spark no Fabric, uma partição contém 80% de todas as chaves de junção, fazendo com que um único executor trabalhe por horas enquanto os demais ficam ociosos. Qual recurso do Spark 3.x resolve essa assimetria de partição automaticamente em tempo de execução?"
  },
  {
    id: "d2_q23",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Gatilho `availableNow = True` no Spark Structured Streaming",
    question: "Um engenheiro de dados quer processar dados de streaming incrementalmente em um pipeline em lote agendado a cada 6 horas. O objetivo é processar todos os dados novos que chegaram desde a última execução e então finalizar a sessão Spark para economizar custos de capacidade. Qual configuração de Trigger deve ser usada?",
    options: [
      {
        id: "A",
        text: "`.trigger(processingTime='10 seconds')`",
        isCorrect: false
      },
      {
        id: "B",
        text: "`.trigger(availableNow=True)`",
        isCorrect: true
      },
      {
        id: "C",
        text: "`.trigger(continuous='1 second')`",
        isCorrect: false
      },
      {
        id: "D",
        text: "Não definir nenhum trigger e matar o processo manualmente no Azure Portal.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O gatilho `trigger(availableNow=True)` processa todos os micro-lotes de dados disponíveis no momento da execução respeitando os limites de taxa configurados e depois encerra a stream com segurança. É o sucessor moderno e superior de `trigger(once=True)`.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A e C:</strong> Mantêm a stream rodando continuamente em loop infinito, consumindo CUs sem parar.</li><li><strong>D:</strong> Matar o processo abruptamente pode corromper checkpoints ou deixar transações incompletas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Incremental Batch com Streaming: Use `.trigger(availableNow=True)` para processar tudo o que estiver disponível e desligar.</div>",
    prompt: "Um engenheiro de dados quer processar dados de streaming incrementalmente em um pipeline em lote agendado a cada 6 horas. O objetivo é processar todos os dados novos que chegaram desde a última execução e então finalizar a sessão Spark para economizar custos de capacidade. Qual configuração de Trigger deve ser usada?"
  },
  {
    id: "d2_q24",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Mecanismo de Watermarking no Spark Streaming",
    question: "Ao agregar eventos em janelas temporais de 15 minutos em uma stream contínua do Spark, como o desenvolvedor garante que dados que cheguem com atraso de até 10 minutos sejam aceitos na agregação, mas que o estado da memória não cresça infinitamente?",
    options: [
      {
        id: "A",
        text: "Utilizando a função `.withWatermark('event_time', '10 minutes')`.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Aumentando a memória física de todos os nós em 128 Terabytes.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Deletando todos os eventos anteriores a cada 5 segundos.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Ignorando os horários de evento e usando apenas a hora do relógio local do cluster.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O método `.withWatermark('timestamp_col', 'delay_threshold')` define o teto aceitável de dados atrasados (late data). O Spark mantém o estado em memória para eventos que cheguem dentro do intervalo de watermark; ultrapassado esse limiar, a janela é fechada e o estado é descartado da memória RAM.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Abordagens inviáveis que causariam OutOfMemory ou perda massiva de dados analíticos válidos.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Watermarking no Spark Streaming descarta o estado antigo da memória após o tempo limite de atraso.</div>",
    prompt: "Ao agregar eventos em janelas temporais de 15 minutos em uma stream contínua do Spark, como o desenvolvedor garante que dados que cheguem com atraso de até 10 minutos sejam aceitos na agregação, mas que o estado da memória não cresça infinitamente?"
  },
  {
    id: "d2_q25",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Diferença entre Janelas Tumbling e Sliding",
    question: "Em uma análise de telemetria de sensores, a equipe de operações precisa calcular a temperatura média a cada 5 minutos em blocos fechados e independentes (sem sobreposição: 10:00-10:05, 10:05-10:10). Qual tipo de janela temporal do Spark atende a essa regra?",
    options: [
      {
        id: "A",
        text: "Janela Tumbling (Tumbling Window / Janela de Salto Fixo sem sobreposição)",
        isCorrect: true
      },
      {
        id: "B",
        text: "Janela Sliding (Janela Deslizante com sobreposição contínua)",
        isCorrect: false
      },
      {
        id: "C",
        text: "Janela de Sessão dinâmica baseada em inatividade de 48 horas",
        isCorrect: false
      },
      {
        id: "D",
        text: "Janela aleatória gerada por sorteio de números",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Janelas Tumbling (janelas em bloco) possuem duração fixa e não se sobrepõem: cada evento pertence a exatamente uma janela. Janelas Sliding (deslizantes) avançam em passos menores que sua duração total (ex: janela de 10 minutos a cada 2 minutos), gerando sobreposição.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Janela Sliding gera sobreposição de eventos entre janelas vizinhas.</li><li><strong>C e D:</strong> Tipos de janela inadequados para o caso de uso.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Tumbling Window = Janelas fixas sem sobreposição (`window(time, '5 minutes')`).</div>",
    prompt: "Em uma análise de telemetria de sensores, a equipe de operações precisa calcular a temperatura média a cada 5 minutos em blocos fechados e independentes (sem sobreposição: 10:00-10:05, 10:05-10:10). Qual tipo de janela temporal do Spark atende a essa regra?"
  },
  {
    id: "d2_q26",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Modos de Saída (Output Modes) no Spark Streaming",
    question: "Qual modo de saída (`outputMode`) do Spark Structured Streaming deve ser utilizado quando a consulta de streaming realiza uma agregação com marca d'água (watermark) e você deseja gravar apenas as linhas consolidadas das janelas de tempo definitivamente fechadas?",
    options: [
      {
        id: "A",
        text: "`outputMode('append')`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`outputMode('complete')`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`outputMode('update')`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`outputMode('delete')`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Em consultas de agregação agregadas com watermark, o modo `append` emite linhas para o sink de destino apenas quando a marca d'água ultrapassa o término da janela temporal (quando o resultado daquela janela é final e imutável), evitando a regravação contínua da tabela inteira.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> O modo `complete` regrava a tabela de saída inteira a cada micro-lote, sendo inviável para tabelas de fatos volumosas.</li><li><strong>C:</strong> O modo `update` emite registros sempre que o valor de agregação é atualizado na janela aberta.</li><li><strong>D:</strong> O modo 'delete' não existe no Spark Structured Streaming.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Agregações consolidadas com Watermark em Delta Lake exigem `outputMode('append')`.</div>",
    prompt: "Qual modo de saída (`outputMode`) do Spark Structured Streaming deve ser utilizado quando a consulta de streaming realiza uma agregação com marca d'água (watermark) e você deseja gravar apenas as linhas consolidadas das janelas de tempo definitivamente fechadas?"
  },
  {
    id: "d2_q27",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Alta Simultaneidade (High Concurrency Mode) em Notebooks",
    question: "Em uma equipe de 10 engenheiros de dados que executam Notebooks de exploração ao mesmo tempo, como o recurso de 'High Concurrency' do Fabric Spark reduz o tempo de espera e otimiza o uso de Capacity Units?",
    options: [
      {
        id: "A",
        text: "Permite que múltiplos notebooks compartilhem a mesma sessão e o mesmo cluster Spark ativo com isolamento de contexto de usuário, evitando o tempo e o custo de iniciar clusters individuais para cada engenheiro.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Transforma o Spark em um servidor web Apache Tomcat.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Apaga os notebooks que levarem mais de 3 minutos para responder.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Executa todos os comandos em ordem alfabética.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O modo High Concurrency permite compartilhar um cluster Spark ativo entre múltiplos usuários e notebooks em tempo real. Cada usuário mantém seu próprio REPL e espaço de variáveis isolado, mas compartilha os executores já alocados, acelerando a inicialização e reduzindo o consumo de CUs.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Descrições sem sentido prático ou técnico.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> High Concurrency Spark = Compartilhamento de sessão e computação entre múltiplos notebooks e usuários simultâneos.</div>",
    prompt: "Em uma equipe de 10 engenheiros de dados que executam Notebooks de exploração ao mesmo tempo, como o recurso de 'High Concurrency' do Fabric Spark reduz o tempo de espera e otimiza o uso de Capacity Units?"
  },
  {
    id: "d2_q28",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Gerenciamento de Dependências com 'Ambientes' (Environments)",
    question: "Um projeto corporativo de dados requer versões específicas de bibliotecas Python (`scikit-learn==1.4.2`, `polars==0.20.15`) em todos os Notebooks e Jobs Spark do Workspace. Qual é o método recomendado pelo Fabric para gerenciar e versionar essas dependências sem executar comandos `%pip install` no início de cada notebook?",
    options: [
      {
        id: "A",
        text: "Criar um item do tipo 'Environment' (Ambiente) no Fabric Workspace, configurar as bibliotecas customizadas e associá-lo como o ambiente padrão do Workspace ou Notebook.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Instalar os pacotes Python no disco local do notebook pessoal do desenvolvedor.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Modificar os arquivos binários do sistema operacional Linux da nuvem da Microsoft.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Substituir todas as bibliotecas por fórmulas do Microsoft Excel.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Os 'Environments' (Ambientes) do Fabric são itens gerenciados de workspace que permitem configurar pools de nós, propriedades Spark (`spark-defaults.conf`) e bibliotecas personalizadas (via Conda, Pip ou arquivos `.whl`). Eles são compilados uma única vez e anexados aos notebooks e pipelines com inicialização instantânea.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Práticas incorretas que não escalam em ambientes de engenharia de dados em nuvem.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Gestão centralizada de bibliotecas no Fabric Spark = Item 'Environment' (Ambiente).</div>",
    prompt: "Um projeto corporativo de dados requer versões específicas de bibliotecas Python (`scikit-learn==1.4.2`, `polars==0.20.15`) em todos os Notebooks e Jobs Spark do Workspace. Qual é o método recomendado pelo Fabric para gerenciar e versionar essas dependências sem executar comandos `%pip install` no início de cada notebook?"
  },
  {
    id: "d2_q29",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Estrutura do Diretório `_delta_log` e Frequência de Checkpoint",
    question: "Em uma tabela Delta no OneLake, a cada transação ACID é gravado um arquivo JSON de commit sequencial (`000000.json`, `000001.json`). Com que frequência padrão o motor Delta gera um arquivo consolidado de Checkpoint em formato Parquet (`.checkpoint.parquet`)?",
    options: [
      {
        id: "A",
        text: "A cada 5 commits",
        isCorrect: false
      },
      {
        id: "B",
        text: "A cada 10 commits",
        isCorrect: true
      },
      {
        id: "C",
        text: "A cada 100 commits",
        isCorrect: false
      },
      {
        id: "D",
        text: "Apenas quando a tabela atinge 1 Terabyte",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Por padrão na especificação Delta Lake, a cada 10 commits (transações concluídas com sucesso), o motor grava um arquivo de checkpoint Parquet consolidado (ex: `00000000000000000010.checkpoint.parquet`). Isso permite que futuros leitores carreguem o estado atual da tabela em uma única leitura sem precisar reprocessar centenas de arquivos JSON individuais.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A, C e D:</strong> Intervalos incorretos segundo o protocolo Delta Lake oficial.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Delta Log: Checkpoint Parquet é gerado a cada 10 commits JSON para consolidar o estado.</div>",
    prompt: "Em uma tabela Delta no OneLake, a cada transação ACID é gravado um arquivo JSON de commit sequencial (`000000.json`, `000001.json`). Com que frequência padrão o motor Delta gera um arquivo consolidado de Checkpoint em formato Parquet (`.checkpoint.parquet`)?"
  },
  {
    id: "d2_q30",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Comando VACUUM e Período de Retenção Padrão",
    question: "Um engenheiro de dados executou o comando `VACUUM TabelaVendas` sem especificar argumentos de tempo. O que acontece com os arquivos Parquet antigos que não estão mais referenciados no estado ativo da tabela?",
    options: [
      {
        id: "A",
        text: "Todos os arquivos são deletados imediatamente, inclusive os modificados há 1 segundo.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Apenas os arquivos órfãos com idade superior ao período de retenção padrão de 7 dias (168 horas) são fisicamente removidos do OneLake.",
        isCorrect: true
      },
      {
        id: "C",
        text: "O comando VACUUM apenas compacta arquivos pequenos sem excluir nenhum byte.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O comando falha porque o VACUUM exige senha de administrador de locatário.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O comando VACUUM remove arquivos de dados Parquet que não estão mais no commit mais recente e que foram excluídos/substituídos há mais tempo do que a janela de retenção de segurança (padrão de 168 horas / 7 dias). Isso preserva a capacidade de Time Travel para os últimos 7 dias.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> O VACUUM possui uma trava de segurança de retenção padrão de 7 dias para não quebrar leitores ativos nem Time Travel recente.</li><li><strong>C:</strong> Compactação de arquivos é responsabilidade do comando `OPTIMIZE`, não do `VACUUM`.</li><li><strong>D:</strong> VACUUM é uma operação de manutenção DDL/DML padrão.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> VACUUM no Delta Lake: Período de retenção padrão = 7 dias (168 horas). Remove arquivos obsoletos após esse prazo.</div>",
    prompt: "Um engenheiro de dados executou o comando `VACUUM TabelaVendas` sem especificar argumentos de tempo. O que acontece com os arquivos Parquet antigos que não estão mais referenciados no estado ativo da tabela?"
  },
  {
    id: "d2_q31",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Impacto do VACUUM no Time Travel",
    question: "Após a execução bem-sucedida de um comando `VACUUM Clientes RETAIN 0 HOURS` (com a trava de segurança desativada), o que acontece quando um analista tenta executar uma consulta com Time Travel: `spark.read.format('delta').option('versionAsOf', 1).load(...)`?",
    options: [
      {
        id: "A",
        text: "A consulta falha com erro de arquivo não encontrado (`FileNotFoundException`), pois os arquivos Parquet da versão 1 foram excluídos fisicamente pelo VACUUM.",
        isCorrect: true
      },
      {
        id: "B",
        text: "A consulta executa normalmente recuperando os arquivos a partir da memória cache da CPU.",
        isCorrect: false
      },
      {
        id: "C",
        text: "O Fabric baixa os arquivos automaticamente a partir de um backup em fita magnética.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O Time Travel ignora o VACUUM e sintetiza os dados usando inteligência artificial.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Time Travel depende da existência física dos arquivos Parquet nos quais as versões antigas se baseiam. Se o VACUUM remover esses arquivos físicos do disco/OneLake, qualquer tentativa de ler versões anteriores que dependam desses arquivos resultará em erro fatal de `FileNotFoundException`.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Uma vez deletados fisicamente pelo VACUUM, os dados não podem ser reconstruídos por cache nem IA.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Consequência crítica do VACUUM: Destrói a capacidade de realizar Time Travel para períodos anteriores ao limite de retenção aplicado.</div>",
    prompt: "Após a execução bem-sucedida de um comando `VACUUM Clientes RETAIN 0 HOURS` (com a trava de segurança desativada), o que acontece quando um analista tenta executar uma consulta com Time Travel: `spark.read.format('delta').option('versionAsOf', 1).load(...)`?"
  },
  {
    id: "d2_q32",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Comando RESTORE TABLE para Recuperação de Desastres",
    question: "Um script executou acidentalmente um comando `DELETE FROM Pedidos WHERE 1=1`, apagando todos os registros de uma tabela Delta crítica no Lakehouse. Qual comando permite restaurar a tabela instantaneamente ao seu estado exato de 15 minutos atrás sem restaurar backups?",
    options: [
      {
        id: "A",
        text: "`RESTORE TABLE Pedidos TO TIMESTAMP AS OF '<timestamp_anterior>';`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`UNDELETE ALL FROM Pedidos;`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`ROLLBACK TRANSACTION IMMEDIATE;`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`DROP TABLE Pedidos;`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Delta Lake possui o comando nativo `RESTORE TABLE <tabela> TO VERSION AS OF <v>` ou `TO TIMESTAMP AS OF <ts>`. Como as transações Delta são baseadas em log imutável, o RESTORE simplesmente grava um novo commit no `_delta_log` apontando o ponteiro oficial de volta para o estado dos arquivos da versão desejada.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B e C:</strong> Comandos não existentes no dialeto Delta Lake.</li><li><strong>D:</strong> Excluiria a tabela e agravaria o incidente.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Recuperação instantânea no Delta Lake: `RESTORE TABLE <tabela> TO VERSION AS OF <n>`.</div>",
    prompt: "Um script executou acidentalmente um comando `DELETE FROM Pedidos WHERE 1=1`, apagando todos os registros de uma tabela Delta crítica no Lakehouse. Qual comando permite restaurar a tabela instantaneamente ao seu estado exato de 15 minutos atrás sem restaurar backups?"
  },
  {
    id: "d2_q33",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Liquid Clustering (`CLUSTER BY`) vs Particionamento Tradicional",
    question: "Qual é a principal vantagem do Liquid Clustering (`CLUSTER BY (col1, col2)`) em comparação com o particionamento tradicional em pastas no estilo Hive (`PARTITION BY col1`) no Microsoft Fabric?",
    options: [
      {
        id: "A",
        text: "Liquid Clustering evita problemas graves de particionamento excessivo (overpartitioning) e arquivos minúsculos (small files), permitindo alterar as chaves de agrupamento sem precisar reescrever os dados históricos da tabela inteira.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Liquid Clustering transforma arquivos Parquet em arquivos binários criptografados proprietários.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Liquid Clustering só funciona em tabelas com menos de 10 linhas.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Liquid Clustering desativa o suporte a transações ACID.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O particionamento tradicional em pastas cria subpastas físicas rígidas, causando milhares de arquivos minúsculos quando a cardinalidade é alta. O Liquid Clustering (`CLUSTER BY`) usa curvas de preenchimento de espaço (Space-Filling Curves / Z-Order flexível) nos próprios arquivos de dados, permitindo mudar as chaves de clusterização a qualquer momento sem recriar ou reescrever partições históricas.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Declarações tecnicamente falsas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Liquid Clustering é a recomendação oficial moderna do Fabric para substituir o particionamento Hive rígido em tabelas Delta.</div>",
    prompt: "Qual é a principal vantagem do Liquid Clustering (`CLUSTER BY (col1, col2)`) em comparação com o particionamento tradicional em pastas no estilo Hive (`PARTITION BY col1`) no Microsoft Fabric?"
  },
  {
    id: "d2_q34",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Ordenação V-Order e Leitura no Power BI Direct Lake",
    question: "Qual é a função do algoritmo de otimização 'V-Order' aplicado nativamente pelo Microsoft Fabric na gravação de arquivos Parquet?",
    options: [
      {
        id: "A",
        text: "Reordenar os dados e aplicar esquemas de codificação e compressão em nível de row group para proporcionar leitura ultrarrápida em memória pelo motor VertiPaq do Power BI e pelo SQL Endpoint.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Criptografar os arquivos com senha para proteger contra pirataria.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Converter todos os valores numéricos em decimais de 128 bits.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Enviar uma cópia de cada linha para o Microsoft Teams.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O V-Order é uma otimização de formato de arquivo no padrão Parquet 100% aberto. Ele classifica e codifica os dados dentro dos row groups de acordo com padrões de acesso colunares, permitindo que a engine VertiPaq (Direct Lake) e a engine de consultas T-SQL leiam os blocos de dados na memória quase sem overhead de decodificação.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas declarações sem base tecnológica.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> V-Order = Otimização colunar de row groups para desempenho máximo de leitura no Direct Lake e T-SQL.</div>",
    prompt: "Qual é a função do algoritmo de otimização 'V-Order' aplicado nativamente pelo Microsoft Fabric na gravação de arquivos Parquet?"
  },
  {
    id: "d2_q35",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Implementação de Slowly Changing Dimensions (SCD Tipo 2) com Delta MERGE",
    question: "Em uma arquitetura de Data Warehouse Medallion, qual é a principal característica de uma Dimensão de Alteração Lenta do Tipo 2 (SCD Tipo 2) implementada via comando MERGE no Delta Lake?",
    options: [
      {
        id: "A",
        text: "Sobrescrever o registro existente sem guardar nenhum histórico de alterações anteriores.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Preservar o histórico completo de versões adicionando uma nova linha para cada alteração com colunas de controle como `DataInicio`, `DataFim` e flag `IsCurrent = True/False`.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Deletar a tabela inteira e recriar com os dados do dia.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Criar uma nova coluna na tabela para cada dia do ano.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> SCD Tipo 2 é o padrão de modelagem dimensional para manter histórico temporal: a linha existente recebe data de término (`DataFim`) e flag `IsCurrent = False`, e um novo registro é inserido com o novo valor, `DataInicio` atual e `IsCurrent = True`.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> Essa é a definição de SCD Tipo 1 (sobrescrita sem histórico).</li><li><strong>C e D:</strong> Práticas incorretas e inviáveis.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> SCD Tipo 1 = Sobrescreve (sem histórico). SCD Tipo 2 = Nova linha com controle de datas e flag ativo (com histórico completo).</div>",
    prompt: "Em uma arquitetura de Data Warehouse Medallion, qual é a principal característica de uma Dimensão de Alteração Lenta do Tipo 2 (SCD Tipo 2) implementada via comando MERGE no Delta Lake?"
  },
  {
    id: "d2_q36",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Clonagem de Tabelas: Deep Clone vs Shallow Clone",
    question: "Um cientista de dados precisa criar um ambiente de teste isolado para testar um algoritmo de machine learning sobre uma tabela de 5 Terabytes. Ele precisa de uma cópia instantânea sem custo adicional de armazenamento e sem copiar os arquivos físicos. Qual comando deve ser usado?",
    options: [
      {
        id: "A",
        text: "`CREATE TABLE TabelaTeste SHALLOW CLONE TabelaProducao;`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`CREATE TABLE TabelaTeste DEEP CLONE TabelaProducao;`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`SELECT * INTO TabelaTeste FROM TabelaProducao;`",
        isCorrect: false
      },
      {
        id: "D",
        text: "Copiar a pasta no Windows Explorer pelo OneLake File Explorer.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O `SHALLOW CLONE` (clone raso ou zero-copy clone) cria uma nova tabela nos metadados apontando para os mesmos arquivos Parquet de dados da tabela original. A criação é praticamente instantânea e consome zero armazenamento adicional até que novas gravações sejam feitas. O `DEEP CLONE` duplicaria todos os 5 TB físicos.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> DEEP CLONE copia fisicamente todos os 5 Terabytes de dados, consumindo tempo e armazenamento duplicado.</li><li><strong>C e D:</strong> Também realizam cópia física completa de dados.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Zero-Copy Clone = `SHALLOW CLONE`. Cópia física independente = `DEEP CLONE`.</div>",
    prompt: "Um cientista de dados precisa criar um ambiente de teste isolado para testar um algoritmo de machine learning sobre uma tabela de 5 Terabytes. Ele precisa de uma cópia instantânea sem custo adicional de armazenamento e sem copiar os arquivos físicos. Qual comando deve ser usado?"
  },
  {
    id: "d2_q37",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "multi",
    title: "Benefícios do Comando `OPTIMIZE` em Tabelas Delta",
    question: "Quais DOIS benefícios fundamentais são proporcionados pela execução periódica do comando `OPTIMIZE` em tabelas Delta no Lakehouse? (Selecione 2 alternativas)",
    options: [
      {
        id: "A",
        text: "Compactação de milhares de arquivos Parquet minúsculos (small files) em arquivos maiores e mais eficientes (~1 GB).",
        isCorrect: true
      },
      {
        id: "B",
        text: "Reorganização multidimensional de dados via Z-Order ou aplicação de Liquid Clustering para otimizar data skipping nas consultas.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Exclusão permanente dos dados confidenciais de clientes sem deixar histórico.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Conversão do Lakehouse em um servidor Apache Kafka.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O comando `OPTIMIZE` realiza a compactação binária (Bin-Packing) consolidando múltiplos arquivos pequenos em arquivos ideais de tamanho próximo a 1 GB e reordena colunas de filtro frequentemente consultadas via Z-Order ou Liquid Clustering para acelerar data skipping.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C:</strong> Exclusão física é responsabilidade do `VACUUM` após o período de retenção.</li><li><strong>D:</strong> Incorreto; OPTIMIZE é puramente uma operação de manutenção Delta.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> OPTIMIZE = Compactação de arquivos pequenos (Compaction) + Reordenação de dados (Z-Order/Clustering).</div>",
    prompt: "Quais DOIS benefícios fundamentais são proporcionados pela execução periódica do comando `OPTIMIZE` em tabelas Delta no Lakehouse? (Selecione 2 alternativas)"
  },
  {
    id: "d2_q38",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Controle de Concorrência Otimista (OCC) e Conflitos de Gravação",
    question: "O que acontece no Delta Lake quando dois jobs Spark concorrentes tentam realizar operações de `MERGE` na mesma tabela Delta exatamente no mesmo segundo?",
    options: [
      {
        id: "A",
        text: "A tabela fica permanentemente corrompida e inacessível.",
        isCorrect: false
      },
      {
        id: "B",
        text: "O Delta Lake utiliza Controle de Concorrência Otimista (OCC): a primeira transação comita com sucesso; a segunda transação verifica se houve sobreposição nos arquivos modificados e, se houver conflito, falha com `ConcurrentModificationException` ou tenta novamente.",
        isCorrect: true
      },
      {
        id: "C",
        text: "O Fabric desliga automaticamente o locatário inteiro para proteger os dados.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Os dados de ambos os jobs são misturados aleatoriamente no mesmo arquivo sem controle de integridade.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Delta Lake assegura integridade ACID por meio de Optimistic Concurrency Control (OCC). Cada transação supõe que concluirá sem interferência; no momento do commit no `_delta_log`, se outra transação tiver modificado os mesmos arquivos lógicos, é detectado conflito de concorrência e a transação conflitante é abortada com segurança.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A, C e D:</strong> Falsas declarações; o modelo OCC foi desenhado especificamente para impedir corrupção e desastres de concorrência.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Delta Lake ACID = Optimistic Concurrency Control (OCC) garante transações atômicas e isoladas.</div>",
    prompt: "O que acontece no Delta Lake quando dois jobs Spark concorrentes tentam realizar operações de `MERGE` na mesma tabela Delta exatamente no mesmo segundo?"
  },
  {
    id: "d2_q39",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Consultas Cross-Database com Nomenclatura de Três Partes",
    question: "No Fabric, um analista conectado a um Warehouse precisa cruzar dados com uma tabela de um Lakehouse localizado no mesmo Workspace. Como essa consulta T-SQL deve referenciar as tabelas?",
    options: [
      {
        id: "A",
        text: "Exportando ambas as tabelas para arquivos texto no disco C: do cliente.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Utilizando a sintaxe de nomenclatura de três partes (Three-Part Naming): `SELECT * FROM MeuLakehouse.dbo.TabelaA JOIN MeuWarehouse.dbo.TabelaB ON ...`",
        isCorrect: true
      },
      {
        id: "C",
        text: "Criando um servidor vinculado (Linked Server) via OLE DB com endereço IP fixo.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Não é possível cruzar tabelas de Lakehouse e Warehouse em uma única consulta T-SQL.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O motor T-SQL do Fabric suporta consultas entre diferentes bancos e itens analíticos no mesmo Workspace (ou entre workspaces) utilizando a nomenclatura padrão de três partes: `[NomeDoBanco].[Esquema].[NomeDaTabela]`. Isso permite cruzar dados entre múltiplos Lakehouses e Warehouses nativamente em uma única consulta.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A, C e D:</strong> Não condizem com as capacidades modernas do motor de consulta relacional do Fabric.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Consultas entre Lakehouse e Warehouse no Fabric: Use nomenclatura de 3 partes `[Item].[Schema].[Tabela]`.</div>",
    prompt: "No Fabric, um analista conectado a um Warehouse precisa cruzar dados com uma tabela de um Lakehouse localizado no mesmo Workspace. Como essa consulta T-SQL deve referenciar as tabelas?"
  },
  {
    id: "d2_q40",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Chaves Primárias e Estrangeiras no Fabric Warehouse (`NOT ENFORCED`)",
    question: "Ao criar uma restrição de Chave Primária (PRIMARY KEY) ou Chave Estrangeira (FOREIGN KEY) em uma tabela do Microsoft Fabric Warehouse com a cláusula `NOT ENFORCED`, qual é o papel dessa restrição?",
    options: [
      {
        id: "A",
        text: "O banco rejeita inserções de valores duplicados ou órfãos com erro de violação de chave.",
        isCorrect: false
      },
      {
        id: "B",
        text: "A restrição é puramente informacional: o banco não valida a integridade referencial durante a inserção, mas o otimizador de consultas utiliza essa informação de esquema para gerar planos de execução mais eficientes.",
        isCorrect: true
      },
      {
        id: "C",
        text: "A restrição bloqueia todas as consultas de leitura na tabela.",
        isCorrect: false
      },
      {
        id: "D",
        text: "A cláusula NOT ENFORCED é proibida no Fabric Warehouse.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> No Fabric Warehouse, restrições como PRIMARY KEY, UNIQUE e FOREIGN KEY devem ser declaradas obrigatoriamente com `NOT ENFORCED`. Isso significa que o motor não despende recursos checando unicidade ou integridade durante inserções massivas, cabendo aos pipelines garantir a qualidade dos dados; contudo, o otimizador usa esses metadados para otimizar JOINs e agregações.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> Restrições `NOT ENFORCED` nunca rejeitam dados durante a inserção.</li><li><strong>C e D:</strong> Afirmações incorretas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> No Fabric Warehouse: Chaves Primárias e Estrangeiras são informacionais (`NOT ENFORCED`) e auxiliam na otimização de consultas.</div>",
    prompt: "Ao criar uma restrição de Chave Primária (PRIMARY KEY) ou Chave Estrangeira (FOREIGN KEY) em uma tabela do Microsoft Fabric Warehouse com a cláusula `NOT ENFORCED`, qual é o papel dessa restrição?"
  },
  {
    id: "d2_q41",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Restrições de Recursos T-SQL Não Suportados no Warehouse",
    question: "Qual dos seguintes recursos tradicionais do SQL Server NÃO é suportado no Fabric Warehouse?",
    options: [
      {
        id: "A",
        text: "Triggers (Gatilhos DML `AFTER INSERT / UPDATE / DELETE`)",
        isCorrect: true
      },
      {
        id: "B",
        text: "Cláusula `GROUP BY` em instruções SELECT",
        isCorrect: false
      },
      {
        id: "C",
        text: "Common Table Expressions (CTEs / Cláusula `WITH`)",
        isCorrect: false
      },
      {
        id: "D",
        text: "Transações ACID com `BEGIN TRANSACTION` e `COMMIT`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric Warehouse é otimizado para cargas analíticas colunares de grande escala. Recursos orientados a OLTP transacional de linha por linha, como Triggers, cursores avançados pesados e colunas `IDENTITY` tradicionais, não são suportados.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> CTEs, GROUP BY e Transações ACID completas são 100% suportadas no Fabric Warehouse.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Não suportado no Fabric Warehouse: Triggers, IDENTITY tradicional e cursores linha-a-linha.</div>",
    prompt: "Qual dos seguintes recursos tradicionais do SQL Server NÃO é suportado no Fabric Warehouse?"
  },
  {
    id: "d2_q42",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Comando `CREATE TABLE AS SELECT` (CTAS)",
    question: "Um engenheiro de dados precisa criar uma nova tabela consolidada no Fabric Warehouse contendo dados agregados de vendas por região a partir de uma tabela de 200 milhões de linhas. Qual comando T-SQL realiza a criação da tabela e inserção dos dados em uma única operação paralela otimizada?",
    options: [
      {
        id: "A",
        text: "`CREATE TABLE AS SELECT (CTAS)`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`EXPORT TO CSV` seguido de importação manual.",
        isCorrect: false
      },
      {
        id: "C",
        text: "`INSERT INTO ... VALUES` com um loop WHILE em T-SQL.",
        isCorrect: false
      },
      {
        id: "D",
        text: "`ALTER DATABASE ADD REGION;`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O comando `CREATE TABLE <NovaTabela> AS SELECT ...` (CTAS) cria a definição da nova tabela e popula os dados diretamente a partir do resultado do SELECT em uma única operação distribuída e paralelizada, sendo a técnica preferida para materialização analítica no Warehouse.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Exportar para CSV e reimportar gera latência extrema e duplicação desnecessária.</li><li><strong>C:</strong> Loop WHILE linha-a-linha com VALUES é extremamente ineficiente em bancos colunares analíticos.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> CTAS (`CREATE TABLE AS SELECT`) é a forma mais rápida e eficiente de criar e popular tabelas no Fabric Warehouse.</div>",
    prompt: "Um engenheiro de dados precisa criar uma nova tabela consolidada no Fabric Warehouse contendo dados agregados de vendas por região a partir de uma tabela de 200 milhões de linhas. Qual comando T-SQL realiza a criação da tabela e inserção dos dados em uma única operação paralela otimizada?"
  },
  {
    id: "d2_q43",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Comando `COPY INTO` para Ingestão Massiva no Warehouse",
    question: "Qual comando T-SQL nativo do Fabric Warehouse é recomendado para ingerir rapidamente milhões de registros armazenados em arquivos Parquet ou CSV em uma conta do Azure Data Lake Storage Gen2 diretamente para uma tabela existente?",
    options: [
      {
        id: "A",
        text: "`COPY INTO`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`BULK INSERT` legado do SQL Server 2000",
        isCorrect: false
      },
      {
        id: "C",
        text: "`BCP IN` via prompt de comando MS-DOS",
        isCorrect: false
      },
      {
        id: "D",
        text: "`OPENROWSET` sem parâmetros",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A instrução T-SQL `COPY INTO` é a primitiva de alta performance no Fabric Warehouse para ingerir arquivos externos (Parquet e CSV) diretamente do Azure Storage para tabelas do Warehouse de forma totalmente paralelizada.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Métodos antigos e não otimizados para a arquitetura de nuvem do Fabric Warehouse.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Ingestão T-SQL de alto desempenho no Warehouse: Comando `COPY INTO`.</div>",
    prompt: "Qual comando T-SQL nativo do Fabric Warehouse é recomendado para ingerir rapidamente milhões de registros armazenados em arquivos Parquet ou CSV em uma conta do Azure Data Lake Storage Gen2 diretamente para uma tabela existente?"
  },
  {
    id: "d2_q44",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Gerenciamento de Estatísticas Automáticas no Warehouse",
    question: "Como o Fabric Warehouse gerencia estatísticas de colunas para garantir que o otimizador de consultas gere planos de execução eficientes?",
    options: [
      {
        id: "A",
        text: "As estatísticas devem ser calculadas manualmente executando scripts a cada 10 minutos.",
        isCorrect: false
      },
      {
        id: "B",
        text: "O Fabric Warehouse cria e atualiza estatísticas automaticamente em segundo plano quando as consultas são executadas (`AUTO_CREATE_STATISTICS` e `AUTO_UPDATE_STATISTICS`).",
        isCorrect: true
      },
      {
        id: "C",
        text: "O Fabric não utiliza estatísticas em suas consultas.",
        isCorrect: false
      },
      {
        id: "D",
        text: "As estatísticas são enviadas por fax para o suporte do Azure.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric Warehouse possui criação e atualização automática de estatísticas (Auto-Stats). Quando uma consulta faz predicados de filtro ou junção em uma coluna sem estatísticas recentes, o motor gera e atualiza as estatísticas em segundo plano de forma transparente.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A, C e D:</strong> Falsas declarações sem embasamento técnico.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Estatísticas no Fabric Warehouse: Atualização automática e dinâmica por padrão pelo motor analítico.</div>",
    prompt: "Como o Fabric Warehouse gerencia estatísticas de colunas para garantir que o otimizador de consultas gere planos de execução eficientes?"
  },
  {
    id: "d2_q45",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Diferença entre Lakehouse (SQL Analytics Endpoint) e Warehouse",
    question: "Qual é a diferença fundamental no controle de gravação entre o SQL Analytics Endpoint de um Lakehouse e um Fabric Warehouse?",
    options: [
      {
        id: "A",
        text: "O SQL Analytics Endpoint do Lakehouse é estritamente somente-leitura (Read-Only) para comandos T-SQL; já o Warehouse suporta operações T-SQL completas de leitura e gravação (DDL e DML: INSERT, UPDATE, DELETE, CREATE TABLE).",
        isCorrect: true
      },
      {
        id: "B",
        text: "O SQL Endpoint permite gravar dados com INSERT, mas o Warehouse é somente-leitura.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Ambos são somente-leitura e não aceitam novos dados.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Não há nenhuma diferença técnica entre os dois itens.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> No Lakehouse, gravações em tabelas Delta são feitas via Apache Spark ou pipelines; o SQL Endpoint exposto fornece apenas uma camada de leitura relacional T-SQL (Read-Only). O Fabric Warehouse, por outro lado, é um data warehouse completo com suporte nativo a comandos T-SQL DML de gravação (`INSERT`, `UPDATE`, `DELETE`, `MERGE`).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Inversões e declarações tecnicamente incorretas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Diferença essencial: SQL Endpoint do Lakehouse = Read-Only no T-SQL. Fabric Warehouse = Read + Write completo no T-SQL.</div>",
    prompt: "Qual é a diferença fundamental no controle de gravação entre o SQL Analytics Endpoint de um Lakehouse e um Fabric Warehouse?"
  },
  {
    id: "d2_q46",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "multi",
    title: "Técnicas de Carregamento de Dados Sem Sobrecarga de Log Transacional",
    question: "Quais DUAS práticas em T-SQL reduzem o bloqueio e otimizam a performance durante o carregamento de grandes massas de dados no Fabric Warehouse? (Selecione 2 alternativas)",
    options: [
      {
        id: "A",
        text: "Utilizar `TRUNCATE TABLE` em vez de `DELETE FROM Tabela` sem cláusula WHERE para esvaziar tabelas de staging.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Utilizar comandos massivos `CREATE TABLE AS SELECT (CTAS)` ou `INSERT INTO ... SELECT` em vez de loops individuais com `INSERT ... VALUES`.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Inserir 1 registro por transação com `COMMIT TRANSACTION` a cada linha.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Desativar a conexão de rede durante o insert.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> `TRUNCATE TABLE` é uma operação DDL de desvinculação de metadados quase instantânea no OneLake, muito mais rápida e leve que o `DELETE`. Operações massivas em lote (`CTAS`, `INSERT ... SELECT`) aproveitam a paralelização colunar do motor distribuído.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C:</strong> Inserir linha por linha gera sobrecarga severa de transações e commits no log.</li><li><strong>D:</strong> Inviável operacionalmente.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Performance T-SQL: Use TRUNCATE em vez de DELETE; use CTAS ou INSERT-SELECT massivo em vez de inserts linha a linha.</div>",
    prompt: "Quais DUAS práticas em T-SQL reduzem o bloqueio e otimizam a performance durante o carregamento de grandes massas de dados no Fabric Warehouse? (Selecione 2 alternativas)"
  },
  {
    id: "d2_q47",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Views Indexadas e Particionamento no Fabric Warehouse",
    question: "Um DBA sênior acostumado com SQL Server on-premises tenta criar um índice clusterizado tradicional (`CREATE CLUSTERED INDEX`) em uma tabela do Fabric Warehouse. Qual será o resultado?",
    options: [
      {
        id: "A",
        text: "O comando falha com erro de sintaxe ou instrução não suportada, pois o Fabric Warehouse armazena dados colunarmente no formato Parquet aberto sem suporte a índices de árvore B (B-Tree) tradicionais.",
        isCorrect: true
      },
      {
        id: "B",
        text: "O índice é criado instantaneamente em disco rígido SCSI.",
        isCorrect: false
      },
      {
        id: "C",
        text: "A tabela é convertida em um arquivo Microsoft Word.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O servidor SQL é reinicializado automaticamente.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric Warehouse não utiliza índices B-Tree clássicos nem índices clusterizados físicos tradicionais do SQL Server. A indexação é inerente à estrutura colunar Parquet/Delta, com ordenação por V-Order e estatísticas de limites de colunas (Min/Max data skipping).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas declarações.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> No Fabric Warehouse: Não existem índices B-Tree tradicionais (`CREATE INDEX`). A performance vem do Parquet colunar e V-Order.</div>",
    prompt: "Um DBA sênior acostumado com SQL Server on-premises tenta criar um índice clusterizado tradicional (`CREATE CLUSTERED INDEX`) em uma tabela do Fabric Warehouse. Qual será o resultado?"
  },
  {
    id: "d2_q48",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Mecanismo de Desconexão Automática e Ociosidade no Warehouse",
    question: "Como o Fabric Warehouse gerencia a computação quando nenhuma consulta T-SQL é executada por um período prolongado?",
    options: [
      {
        id: "A",
        text: "Os recursos computacionais são suspensos dinamicamente para liberar capacidade na F-SKU, sem que nenhum dado seja perdido no OneLake.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Todas as tabelas são apagadas após 1 hora de inatividade.",
        isCorrect: false
      },
      {
        id: "C",
        text: "O usuário recebe uma multa por inatividade no portal do Azure.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O Warehouse é convertido em um arquivo PDF.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A arquitetura serverless do Fabric Warehouse é desacoplada do OneLake: quando não há consultas ativas, os nós computacionais ficam ociosos ou liberados, poupando Capacity Units do F-SKU compartilhado.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Declarações absurdas e incorretas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Computação Serverless no Warehouse: Computação sob demanda liberando CUs quando não há consultas ativas.</div>",
    prompt: "Como o Fabric Warehouse gerencia a computação quando nenhuma consulta T-SQL é executada por um período prolongado?"
  },
  {
    id: "d2_q49",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Fontes Nativas Suportadas pelo Eventstream",
    question: "Qual das seguintes opções representa uma fonte de dados de streaming em tempo real suportada nativamente para ingestão contínua em um Fabric Eventstream?",
    options: [
      {
        id: "A",
        text: "Azure Event Hubs / IoT Hub",
        isCorrect: true
      },
      {
        id: "B",
        text: "Disquete magnético ZipDrive",
        isCorrect: false
      },
      {
        id: "C",
        text: "Arquivo CSV estático em CD-ROM",
        isCorrect: false
      },
      {
        id: "D",
        text: "Tabela de impressão do Windows 95",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric Eventstream suporta ingestão contínua a partir de fontes como: Azure Event Hubs, Azure IoT Hub, clusters Apache Kafka externos, Azure SQL Database CDC (Change Data Capture) e Custom Endpoints para envio via API REST.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsos e sem relevância em nuvem.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Fontes nativas de Eventstream: Event Hubs, IoT Hub, Apache Kafka e CDC de bancos de dados.</div>",
    prompt: "Qual das seguintes opções representa uma fonte de dados de streaming em tempo real suportada nativamente para ingestão contínua em um Fabric Eventstream?"
  },
  {
    id: "d2_q50",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Destinos Nativos do Eventstream",
    question: "Em um fluxo de dados em tempo real montado no Fabric Eventstream, para quais destinos os eventos processados podem ser despachados diretamente?",
    options: [
      {
        id: "A",
        text: "Tabela Delta no Lakehouse, KQL Database (Eventhouse), Custom App e Reflex (Data Activator)",
        isCorrect: true
      },
      {
        id: "B",
        text: "Apenas para uma impressora térmica de cupons fiscais.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Apenas para arquivos compactados em fita DAT.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Apenas para o Bloco de Notas do Windows.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Eventstream é um roteador de eventos de alta taxa: ele pode entregar os dados simultaneamente para um KQL Database (Eventhouse) para consultas em tempo real, para um Lakehouse (tabela Delta Parquet) para histórico, para o Data Activator (Reflex) para alertas automatizados, ou para um Custom Endpoint.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Destinos fictícios sem relevância analítica.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Destinos de Eventstream: Lakehouse (Delta), Eventhouse (KQL), Reflex (Data Activator) e Custom Endpoints.</div>",
    prompt: "Em um fluxo de dados em tempo real montado no Fabric Eventstream, para quais destinos os eventos processados podem ser despachados diretamente?"
  },
  {
    id: "d2_q51",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Políticas de Atualização em KQL (Update Policies)",
    question: "Como uma Política de Atualização (Update Policy) em uma tabela de um banco KQL (Eventhouse) viabiliza transformações em tempo real durante a ingestão?",
    options: [
      {
        id: "A",
        text: "Executa uma função KQL automaticamente sempre que novos dados são ingeridos na tabela de origem (Raw), inserindo os dados transformados na tabela de destino transacionalmente.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Exige a execução manual de um job Spark a cada minuto.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Apaga os dados da tabela de destino se houver registros repetidos.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Desliga o servidor KQL se a consulta demorar mais de 1 segundo.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> As Update Policies do KQL funcionam como 'triggers' transacionais de ingestão: quando novos lotes de eventos entram na tabela bruta de ingestão, o motor executa uma consulta/função KQL nos novos dados e insere o resultado limpo e transformado na tabela de destino em tempo real sem sobrecarga de pipelines adicionais.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas declarações sem base na arquitetura do KQL.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> KQL Update Policy = Transformação de streaming acionada na ingestão, populando tabelas derivadas em tempo real.</div>",
    prompt: "Como uma Política de Atualização (Update Policy) em uma tabela de um banco KQL (Eventhouse) viabiliza transformações em tempo real durante a ingestão?"
  },
  {
    id: "d2_q52",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Cache Dinâmico no Eventhouse: Hot Cache vs Cold Cache",
    question: "Em uma base de dados KQL com 50 Terabytes de logs de telemetria dos últimos 3 anos, os analistas consultam com frequência apenas os dados dos últimos 7 dias. Qual política de retenção e cache deve ser configurada na tabela para otimizar custos e manter tempos de resposta em milissegundos?",
    options: [
      {
        id: "A",
        text: "Hot Cache Policy = 7 dias; Soft Delete (Retention Policy) = 1095 dias (3 anos).",
        isCorrect: true
      },
      {
        id: "B",
        text: "Hot Cache Policy = 1095 dias; Retention Policy = 7 dias.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Desativar o cache completamente e ler os dados por fita magnética.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Apagar os dados após 24 horas para não gastar memória.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> No KQL Database (Eventhouse), os dados em 'Hot Cache' são mantidos em discos SSD ultra-rápidos e memória RAM local nos nós para consultas em milissegundos. Dados em 'Cold Storage' permanecem no OneLake/Blob a custo baixíssimo e são lidos sob demanda. Configurar Hot Cache = 7 dias e Soft Delete = 3 anos atende perfeitamente ao requisito com mínimo custo.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Inverteu a lógica; manter 3 anos em Hot Cache custaria excessivamente em memória e SSDs.</li><li><strong>C e D:</strong> Não atendem aos requisitos de negócio.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> KQL Caching: Hot Cache = Período de consulta frequente (em SSD/RAM); Retention = Tempo total de vida dos dados.</div>",
    prompt: "Em uma base de dados KQL com 50 Terabytes de logs de telemetria dos últimos 3 anos, os analistas consultam com frequência apenas os dados dos últimos 7 dias. Qual política de retenção e cache deve ser configurada na tabela para otimizar custos e manter tempos de resposta em milissegundos?"
  },
  {
    id: "d2_q53",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Função KQL `arg_max()` para Desduplicação de Eventos",
    question: "Em uma tabela KQL que recebe múltiplos eventos de status de dispositivos IoT com atualizações contínuas, qual operador KQL deve ser utilizado para recuperar o registro mais recente de cada dispositivo pelo campo `Timestamp`?",
    options: [
      {
        id: "A",
        text: "`Tabela | summarize arg_max(Timestamp, *) by DeviceId`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`Tabela | order by Timestamp desc | take 1`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`Tabela | where DeviceId == max(Timestamp)`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`Tabela | delete duplicates where Timestamp < now()`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O operador de agregação `summarize arg_max(Timestamp, *) by DeviceId` em KQL encontra o valor máximo da coluna de tempo para cada chave de agrupamento (`DeviceId`) e projeta todas as outras colunas correspondentes àquela linha específica, sendo a forma idiomática e mais eficiente de desduplicação e obtenção do último estado em KQL.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> `take 1` retornaria apenas 1 único dispositivo em toda a tabela.</li><li><strong>C:</strong> Sintaxe inválida em KQL.</li><li><strong>D:</strong> O KQL não possui o comando DML `delete duplicates`.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Obter o estado mais recente em KQL: `summarize arg_max(Timestamp, *) by EntidadeId`.</div>",
    prompt: "Em uma tabela KQL que recebe múltiplos eventos de status de dispositivos IoT com atualizações contínuas, qual operador KQL deve ser utilizado para recuperar o registro mais recente de cada dispositivo pelo campo `Timestamp`?"
  },
  {
    id: "d2_q54",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Operadores de String em KQL: `has` vs `contains`",
    question: "Ao pesquisar um termo específico em uma coluna de texto livre contendo bilhões de logs de mensagens de erro no KQL, por que a documentação oficial recomenda fortemente o uso do operador `has` em vez de `contains`?",
    options: [
      {
        id: "A",
        text: "`has` busca por termos indexados de palavras inteiras usando o índice de inversão colunar (infinidades de vezes mais rápido), enquanto `contains` realiza varredura linear de substrings sem usar o índice.",
        isCorrect: true
      },
      {
        id: "B",
        text: "`contains` foi descontinuado e gera erro de sintaxe.",
        isCorrect: false
      },
      {
        id: "C",
        text: "`has` aceita apenas números inteiros positivos.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Ambos possuem o mesmo plano de execução e o mesmo tempo de resposta.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> No Kusto Query Language (KQL), colunas de texto são indexadas por termos compostos por caracteres alfanuméricos. O operador `has` utiliza o índice invertido para localizar a palavra exata em microssegundos. Já o operador `contains` busca substrings arbitrárias (semelhante a `LIKE '%termo%'` no SQL), ignorando o índice e forçando a varredura linear de todos os textos.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> `contains` é válido, mas deve ser evitado por questões de desempenho em big data.</li><li><strong>C e D:</strong> Falsas declarações sobre os operadores de string do KQL.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Desempenho KQL: Use `has` para busca de termos indexados (palavras inteiras). Evite `contains` em grandes volumes.</div>",
    prompt: "Ao pesquisar um termo específico em uma coluna de texto livre contendo bilhões de logs de mensagens de erro no KQL, por que a documentação oficial recomenda fortemente o uso do operador `has` em vez de `contains`?"
  },
  {
    id: "d2_q55",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Ingestion Batching Policy no KQL Database",
    question: "Um banco de dados KQL está recebendo milhares de pequenas mensagens por segundo via streaming. Como a 'Ingestion Batching Policy' gerencia a formação de arquivos de dados no backend?",
    options: [
      {
        id: "A",
        text: "Agrupa os eventos com base em limiares configuráveis de tempo (ex: 5 minutos), tamanho de buffer (ex: 1 GB) ou quantidade de itens (ex: 1.000 itens), otimizando a criação de extensões de dados (shards/extents).",
        isCorrect: true
      },
      {
        id: "B",
        text: "Cria um arquivo Parquet separado para cada evento de 100 bytes recebido.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Bloqueia a rede até que 10 milhões de eventos estejam na memória.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Rejeita qualquer mensagem com menos de 1 Megabyte.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A política de loteamento de ingestão (`IngestionBatching`) define quando o motor KQL deve consolidar os dados em trânsito e comitá-los em extents permanentes. Ela é governada por três limites: tempo máximo de espera, tamanho máximo de dados não comprimidos e número máximo de registros.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Criar um arquivo por mensagem causaria degradação severa por excesso de pequenos arquivos.</li><li><strong>C e D:</strong> Valores e regras que não existem na arquitetura do Kusto.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Ingestion Batching Policy no KQL: Agrupa dados em trânsito por tempo, tamanho ou contagem antes de gravar extents.</div>",
    prompt: "Um banco de dados KQL está recebendo milhares de pequenas mensagens por segundo via streaming. Como a 'Ingestion Batching Policy' gerencia a formação de arquivos de dados no backend?"
  },
  {
    id: "d2_q56",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Agrupamento Temporal com a Função `bin()` em KQL",
    question: "Qual consulta KQL abaixo agrupa corretamente a quantidade total de requisições de API recebidas em intervalos contíguos de 15 minutos?",
    options: [
      {
        id: "A",
        text: "`ApiLogs | summarize Total = count() by bin(Timestamp, 15m)`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`ApiLogs | group by Timestamp every 15 minutes`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`ApiLogs | select count() partition by round(Timestamp, 15)`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`ApiLogs | sum(Timestamp) / 15`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Em KQL, o agrupamento por intervalos de tempo ou faixas numéricas é feito com a função `bin(expressao, tamanho_do_intervalo)` combinada com a instrução `summarize ... by ...`. O intervalo de 15 minutos é expresso como `15m`.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Sintaxes inválidas no Kusto Query Language.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Agrupamento temporal em KQL: `summarize count() by bin(Timestamp, 15m)`.</div>",
    prompt: "Qual consulta KQL abaixo agrupa corretamente a quantidade total de requisições de API recebidas em intervalos contíguos de 15 minutos?"
  },
  {
    id: "d2_q57",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Integração do Data Activator (Reflex) com Eventhouse",
    question: "Qual é a principal função do Data Activator (Reflex) quando conectado a streams em tempo real no Microsoft Fabric?",
    options: [
      {
        id: "A",
        text: "Monitorar dados e disparar ações automatizadas (como alertas no Microsoft Teams, e-mails pelo Outlook ou chamadas de webhook) quando regras e limiares de condição são atingidos em tempo real.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Desligar o gerador de energia elétrica do escritório.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Substituir o firewall corporativo por um roteador Wi-Fi doméstico.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Converter código Python em código assembly de 8 bits.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Data Activator (Reflex) é a solução no-code/low-code do Fabric para detecção de condições e disparo de ações em tempo real. Ele rastreia métricas e eventos vindos do Eventstream, Eventhouse ou relatórios do Power BI e dispara notificações (Teams, Email) ou pipelines.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Definições absurdas e irrelevantes.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Data Activator (Reflex) = Automação acionada por eventos e alertas em tempo real baseados em regras de negócio.</div>",
    prompt: "Qual é a principal função do Data Activator (Reflex) quando conectado a streams em tempo real no Microsoft Fabric?"
  },
  {
    id: "d2_q58",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Extensões de Dados (Extents) e Sharding no KQL Database",
    question: "Como os dados são fisicamente organizados e compactados internamente dentro de uma tabela de banco de dados KQL (Eventhouse)?",
    options: [
      {
        id: "A",
        text: "Em estruturas imutáveis chamadas 'Extents' (ou Shards), que armazenam dados colunarmente compactados e indexados de forma independente.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Em um único arquivo texto `.txt` sequencial compartilhado por todos os nós.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Em tabelas B-Tree bloqueadas com lock exclusivo de banco de dados.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Em planilhas de cálculo vinculadas via OLE.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O motor Kusto organiza o armazenamento de tabelas em fragmentos independentes e imutáveis chamados 'Extents' (ou shards). Cada extent contém colunas comprimidas e índices de texto invertidos. Consultas KQL processam extents em paralelo massivo nos nós do cluster.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas noções sobre a arquitetura colunar distribuída do Kusto.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> KQL Storage Architecture: Tabelas são coleções de fragmentos colunares imutáveis chamados 'Extents'.</div>",
    prompt: "Como os dados são fisicamente organizados e compactados internamente dentro de uma tabela de banco de dados KQL (Eventhouse)?"
  },
  {
    id: "d2_q59",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Mecanismo de Mirroring no Microsoft Fabric",
    question: "Qual é a principal proposta de valor do recurso 'Fabric Mirroring' para bancos de dados como Azure SQL Database, Snowflake ou Cosmos DB?",
    options: [
      {
        id: "A",
        text: "Replicar dados continuamente em tempo quase real para o OneLake em formato Delta Parquet aberto sem criar pipelines manuais complexos de ETL e sem impactar a capacidade computacional da fonte transacional com consultas pesadas.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Substituir o banco transacional e apagar as tabelas da fonte de origem.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Fazer backup dos dados em fita magnética física para envio postal.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Obrigar os desenvolvedores a reescrever todas as aplicações em linguagem C.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric Mirroring oferece replicação contínua (CDC nativo) de bases de dados transacionais externas diretamente para tabelas Delta no OneLake. Os dados replicados ficam disponíveis imediatamente para consultas T-SQL, Spark e Power BI Direct Lake sem custos de ETL contínuo.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Incorretos e contrários aos objetivos do Mirroring.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Fabric Mirroring = Zero-ETL / CDC contínuo de fontes transacionais diretamente para tabelas Delta no OneLake.</div>",
    prompt: "Qual é a principal proposta de valor do recurso 'Fabric Mirroring' para bancos de dados como Azure SQL Database, Snowflake ou Cosmos DB?"
  },
  {
    id: "d2_q60",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Pré-requisito de CDC para Espelhamento de Azure SQL Database",
    question: "Para habilitar o Mirroring de um banco de dados Azure SQL Database no Microsoft Fabric, qual recurso deve estar previamente habilitado no banco transacional de origem?",
    options: [
      {
        id: "A",
        text: "Change Data Capture (CDC) e uma chave de identidade gerenciada/permissão de leitura para o Fabric.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Desativação de todos os índices clusterizados.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Remoção de todas as senhas dos administradores.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Instalação do Microsoft Office 2003 no servidor de banco de dados.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Mirroring para Azure SQL Database baseia-se na captura contínua de alterações via Change Data Capture (CDC) ou Change Tracking nativo do SQL Server. Sem o CDC ativado e as permissões de acesso adequadas concedidas ao Fabric, o serviço de espelhamento não consegue ler o log de transações.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Requisitos falsos e prejudiciais à segurança.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Pré-requisito de Mirroring no SQL: CDC ativado e permissões de conexão apropriadas.</div>",
    prompt: "Para habilitar o Mirroring de um banco de dados Azure SQL Database no Microsoft Fabric, qual recurso deve estar previamente habilitado no banco transacional de origem?"
  },
  {
    id: "d2_q61",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Consulta aos Dados Espelhados via SQL Endpoint",
    question: "Como os analistas corporativos consultam os dados de um banco de dados que foi espelhado (Mirrored Database) no Fabric?",
    options: [
      {
        id: "A",
        text: "Conectando-se ao SQL Analytics Endpoint gerado automaticamente para o Mirrored Database, executando consultas T-SQL padrão com desempenho colunar.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Fazendo login direto no console SSH da máquina virtual do banco original.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Solicitando os dados por telefone para o suporte da Microsoft.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Os dados espelhados não podem ser consultados por T-SQL.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Cada Mirrored Database criado no Fabric gera automaticamente um SQL Analytics Endpoint correspondente. Os analistas podem conectar ferramentas como SSMS, Power BI ou Azure Data Studio para consultar as tabelas Delta espelhadas via T-SQL sem tocar no banco transacional original.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Incorretos.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Mirrored Database inclui automaticamente um SQL Analytics Endpoint para leitura T-SQL no OneLake.</div>",
    prompt: "Como os analistas corporativos consultam os dados de um banco de dados que foi espelhado (Mirrored Database) no Fabric?"
  },
  {
    id: "d2_q62",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Latência Típica de Replicação no Fabric Mirroring",
    question: "Qual é a latência esperada na sincronização de dados alterados na origem quando o Fabric Mirroring está em execução saudável?",
    options: [
      {
        id: "A",
        text: "Latência quase em tempo real (tipicamente de segundos a poucos minutos).",
        isCorrect: true
      },
      {
        id: "B",
        text: "Latência fixa de 24 horas (uma vez por noite).",
        isCorrect: false
      },
      {
        id: "C",
        text: "Latência fixa de 30 dias.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Sincronização instantânea na velocidade da luz sem nenhum nanosegundo de atraso.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric Mirroring opera em modelo de replicação quase em tempo real (near real-time): as alterações registradas no log transacional são continuamente lidas, formatadas em Delta Parquet e comitadas no OneLake com latência típica de poucos segundos a minutos.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B e C:</strong> Descreveriam processos de lote tradicionais diários/mensais, não espelhamento.</li><li><strong>D:</strong> Não existe replicação distribuída com latência zero física absoluta.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Fabric Mirroring opera em near real-time (segundos a poucos minutos de latência).</div>",
    prompt: "Qual é a latência esperada na sincronização de dados alterados na origem quando o Fabric Mirroring está em execução saudável?"
  },
  {
    id: "d2_q63",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Snowflake Mirroring para Microsoft Fabric",
    question: "Uma organização tem dados históricos críticos no Snowflake e deseja consolidá-los no OneLake do Fabric para cruzamento analítico com dados do Power BI. O que o Mirroring para Snowflake realiza?",
    options: [
      {
        id: "A",
        text: "Replica de forma transparente e contínua os dados do Snowflake para tabelas Delta Parquet no OneLake gerenciado pelo Fabric.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Cancela o contrato da Snowflake e migra os servidores físicos para a Microsoft.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Transforma todas as tabelas em arquivos CSV compartilhados na rede local.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Bloqueia o acesso a qualquer usuário fora da rede interna.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Mirroring para Snowflake conecta-se à conta Snowflake e sincroniza os esquemas e dados selecionados diretamente para o OneLake no formato Delta Lake, permitindo análise unificada no Fabric sem duplicação manual de pipelines de engenharia.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Declarações sem sentido técnico.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Snowflake Mirroring = Sincronização contínua de bases Snowflake diretamente para o OneLake em Delta Parquet.</div>",
    prompt: "Uma organização tem dados históricos críticos no Snowflake e deseja consolidá-los no OneLake do Fabric para cruzamento analítico com dados do Power BI. O que o Mirroring para Snowflake realiza?"
  },
  {
    id: "d2_q64",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Isolamento de Carga Transacional via Mirroring",
    question: "Por que a equipe de infraestrutura de TI aprova o uso do Fabric Mirroring em vez de permitir que analistas de BI conectem o Power BI diretamente ao banco de dados transacional de produção em modo DirectQuery?",
    options: [
      {
        id: "A",
        text: "Porque o Mirroring lê apenas os logs de transação (CDC) de forma assíncrona e transfere as consultas analíticas pesadas para o Fabric, eliminando a concorrência e o risco de lentidão ou travamento na aplicação OLTP.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Porque o Power BI não consegue se conectar a bancos SQL.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Porque o Fabric apaga o banco transacional periodicamente.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Porque consultas DirectQuery em bancos SQL são ilegais.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Consultas analíticas pesadas (relatórios de BI com agregações de milhões de linhas) executadas diretamente em bancos transacionais (OLTP) causam bloqueios de tabela (`LOCKS`), contenção de recursos e travamentos nas aplicações de negócios. O Mirroring isola completamente a carga de consulta no OneLake.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas declarações.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Vantagem do Mirroring: Isola a aplicação de produção contra gargalos de relatórios de BI pesados.</div>",
    prompt: "Por que a equipe de infraestrutura de TI aprova o uso do Fabric Mirroring em vez de permitir que analistas de BI conectem o Power BI diretamente ao banco de dados transacional de produção em modo DirectQuery?"
  },
  {
    id: "d2_q65",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Camadas da Arquitetura Medallion: Bronze, Prata e Ouro",
    question: "Na arquitetura Medallion implementada no Microsoft Fabric, qual é o papel específico da camada 'Silver' (Prata)?",
    options: [
      {
        id: "A",
        text: "Armazenar dados brutos exatamente como vieram da fonte original sem nenhuma limpeza ou tipagem.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Armazenar dados limpos, enriquecidos, validados e padronizados com esquema consistente (Enterprise View / Visão Corporativa da Verdade).",
        isCorrect: true
      },
      {
        id: "C",
        text: "Conter agregados de negócios prontos para consumo com medidas DAX e modelos estrela estritos.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Guardar backups de e-mails de desenvolvedores aposentados.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Na arquitetura Medallion: 1) Bronze = Dados brutos imutáveis (Raw); 2) Silver = Dados limpos, filtrados, padronizados e enriquecidos com tipagem de esquema consistente; 3) Gold = Modelagem dimensional final (Star Schema), agregações de negócios e dados prontos para relatórios corporativos.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A:</strong> Essa é a definição da camada Bronze.</li><li><strong>C:</strong> Essa é a definição da camada Gold.</li><li><strong>D:</strong> Incorreto.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Arquitetura Medallion: Bronze = Raw / Bruto; Silver = Cleaned & Conformed / Limpo; Gold = Business Aggregated / Dimensional.</div>",
    prompt: "Na arquitetura Medallion implementada no Microsoft Fabric, qual é o papel específico da camada 'Silver' (Prata)?"
  },
  {
    id: "d2_q66",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Modelagem Estrela (Star Schema) na Camada Gold",
    question: "Por que a Microsoft recomenda a modelagem dimensional em esquema estrela (Star Schema) na camada Gold para consumo pelo Power BI em modo Direct Lake?",
    options: [
      {
        id: "A",
        text: "Porque o esquema estrela com tabelas de fatos e dimensões desacopladas permite que o motor VertiPaq realize junções colunares com o menor custo de memória e excelente compressão colunar por dicionário.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Porque o Direct Lake só funciona se todas as tabelas tiverem apenas 3 colunas.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Porque tabelas desnormalizadas gigantescas com 500 colunas são sempre mais rápidas no Power BI.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O esquema estrela foi abandonado pela indústria de BI.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Star Schema (esquema estrela) organiza dados em tabelas de fatos numéricas estreitas ligadas a dimensões descritivas. O motor analítico colunar do Power BI (VertiPaq) é amplamente otimizado para essa topologia, atingindo taxas máximas de compressão por dicionário e planos de junção simplificados.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B e C:</strong> Falsos conceitos de modelagem.</li><li><strong>D:</strong> O Star Schema continua sendo o padrão de ouro oficial da engenharia analítica da Microsoft.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Diretriz oficial: Sempre modele a camada Gold em Star Schema (Fatos + Dimensões) para máxima performance no Direct Lake.</div>",
    prompt: "Por que a Microsoft recomenda a modelagem dimensional em esquema estrela (Star Schema) na camada Gold para consumo pelo Power BI em modo Direct Lake?"
  },
  {
    id: "d2_q67",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "multi",
    title: "Validação de Qualidade de Dados com PySpark na Camada Silver",
    question: "Quais DUAS ações comumente implementadas via código PySpark em um Notebook garantem a integridade dos dados durante a promoção da camada Bronze para a camada Silver? (Selecione 2 alternativas)",
    options: [
      {
        id: "A",
        text: "Desduplicação de registros por chave primária de negócio usando `dropDuplicates(['id'])`.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Aplicação de regras de validação e descarte/quarentena de registros com campos obrigatórios nulos (`filter(col('data').isNotNull())`).",
        isCorrect: true
      },
      {
        id: "C",
        text: "Criptografia dos nomes de todas as colunas com chave privada RSA.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Substituição de todas as datas pelo dia 1º de Janeiro de 1900.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A transformação da camada Bronze para Silver tem como foco a qualidade de dados: desduplicação por chaves naturais de negócio, validação de tipos de dados, descarte ou isolamento em quarentena de registros com valores nulos críticos ou fora dos limites de conformidade.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C e D:</strong> Práticas incorretas que destruiriam a usabilidade e qualidade dos dados analíticos.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Silver Layer: Foco em limpeza, desduplicação (`dropDuplicates`), validação de nulos e conformidade de esquema.</div>",
    prompt: "Quais DUAS ações comumente implementadas via código PySpark em um Notebook garantem a integridade dos dados durante a promoção da camada Bronze para a camada Silver? (Selecione 2 alternativas)"
  },
  {
    id: "d2_q68",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Estrutura de Quarentena para Dados Inválidos",
    question: "Ao ingerir dados brutos de pedidos na camada Bronze, alguns registros chegam com valores monetários negativos inválidos. Qual padrão arquitetural preserva o fluxo de dados dos pedidos sadios sem perder o registro dos pedidos com erro para auditoria?",
    options: [
      {
        id: "A",
        text: "Padrão Quarentena (Dead-Letter Queue / Bad Records Table): os registros sadios são promovidos para a camada Silver normalmente, enquanto os registros com erro são roteados para uma tabela Delta separada de 'Quarentena' para auditoria e retificação.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Abortar o pipeline inteiro e não processar nenhum pedido válido.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Multiplicar o valor negativo por zero e comitar silenciosamente.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Desligar o banco de dados da empresa.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O padrão de Quarentena (Dead-Letter / Quarantine Table) separa os dados em dois fluxos condicionais: dados conformes seguem viagem para a camada Silver; registros violadores de regras são gravados em uma tabela isolada de quarentena com o motivo da falha anotado, permitindo que o negócio audite e reingira os registros retificados.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Abortar o pipeline penalizaria os 99% de pedidos válidos.</li><li><strong>C:</strong> Alterar silenciosamente o dado sem registro gera inconsistência contábil gravíssima.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Padrão de Quarentena no DP-700: Dados válidos avançam; dados inválidos são isolados em tabela de quarentena para auditoria.</div>",
    prompt: "Ao ingerir dados brutos de pedidos na camada Bronze, alguns registros chegam com valores monetários negativos inválidos. Qual padrão arquitetural preserva o fluxo de dados dos pedidos sadios sem perder o registro dos pedidos com erro para auditoria?"
  },
  {
    id: "d2_q69",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Manejo de Dados Semi-Estruturados (JSON) com PySpark",
    question: "Um Lakehouse recebe arquivos JSON aninhados na camada Bronze. Qual função nativa do PySpark permite expandir um array de objetos JSON contido em uma coluna para que cada elemento do array se torne uma linha independente na tabela resultante?",
    options: [
      {
        id: "A",
        text: "`explode()`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`collapse()`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`shrink()`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`concat_ws()`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A função `pyspark.sql.functions.explode(coluna_array)` extrai cada elemento de uma lista ou array presente em uma coluna e cria uma nova linha para cada elemento, duplicando os valores das demais colunas escalares correspondentes.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B e C:</strong> Funções inexistentes para esse propósito no PySpark.</li><li><strong>D:</strong> `concat_ws()` une strings separadas por delimitador em uma única linha.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Manipulação de arrays e JSON no Spark: Use `explode()` para transformar itens de uma lista em múltiplas linhas.</div>",
    prompt: "Um Lakehouse recebe arquivos JSON aninhados na camada Bronze. Qual função nativa do PySpark permite expandir um array de objetos JSON contido em uma coluna para que cada elemento do array se torne uma linha independente na tabela resultante?"
  },
  {
    id: "d2_q70",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Parseamento de Strings JSON com `from_json()`",
    question: "Uma coluna de texto em uma tabela Delta contém strings com conteúdo no formato JSON (`{\"cliente\": \"Ana\", \"valor\": 150.0}`). Qual combinação de funções do PySpark deve ser utilizada para transformar essa string em uma coluna de estrutura fortemente tipada (StructType)?",
    options: [
      {
        id: "A",
        text: "`from_json(col('json_string'), schema)` onde `schema` é um `StructType` definido com os campos e tipos esperados.",
        isCorrect: true
      },
      {
        id: "B",
        text: "`to_json()` sem esquema definido.",
        isCorrect: false
      },
      {
        id: "C",
        text: "`split(col('json_string'), ',')` com conversão forçada para inteiro.",
        isCorrect: false
      },
      {
        id: "D",
        text: "`substring()` com índices fixos de 1 a 10.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A função `from_json(col, schema)` interpreta uma string com dados JSON e a converte em uma estrutura colunar Spark do tipo `StructType` de acordo com o esquema fornecido, permitindo acessar os campos internos com a notação de ponto (`coluna.cliente`).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> `to_json()` faz o caminho inverso: converte uma estrutura colunar em string JSON.</li><li><strong>C e D:</strong> Manipulações de string frágeis e propensas a quebra.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> String JSON para Colunas Fortemente Tipadas: `from_json(col, schema)`.</div>",
    prompt: "Uma coluna de texto em uma tabela Delta contém strings com conteúdo no formato JSON (`{\"cliente\": \"Ana\", \"valor\": 150.0}`). Qual combinação de funções do PySpark deve ser utilizada para transformar essa string em uma coluna de estrutura fortemente tipada (StructType)?"
  },
  {
    id: "d2_q71",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Identificação de Mudanças de Esquema (Schema Evolution)",
    question: "Ao gravar novos lotes de dados em uma tabela Delta existente via PySpark, uma nova coluna chamada `CanalVenda` foi adicionada na fonte. Como o desenvolvedor instrui o comando `write` a adicionar essa nova coluna na tabela Delta automaticamente sem falhar a execução?",
    options: [
      {
        id: "A",
        text: "Adicionar a opção `.option('mergeSchema', 'true')` no comando de escrita do DataFrame.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Adicionar a opção `.option('forceOverwrite', 'true')` para apagar a tabela.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Excluir manualmente a pasta `_delta_log` no OneLake.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Renomear a coluna para ter o mesmo nome de uma coluna existente.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Por padrão, o Delta Lake protege contra inserções acidentais com esquemas diferentes (Schema Enforcement). Para permitir a evolução controlada do esquema com adição de novas colunas, utiliza-se a opção `.option('mergeSchema', 'true')` ou configura-se `spark.databricks.delta.schema.autoMerge.enabled = true`.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Sobrescrever a tabela apagaria todo o histórico existente.</li><li><strong>C:</strong> Destruiria a integridade transacional do Delta Lake.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Evolução de Esquema no Delta Lake: Use `.option('mergeSchema', 'true')` para adicionar novas colunas com segurança.</div>",
    prompt: "Ao gravar novos lotes de dados em uma tabela Delta existente via PySpark, uma nova coluna chamada `CanalVenda` foi adicionada na fonte. Como o desenvolvedor instrui o comando `write` a adicionar essa nova coluna na tabela Delta automaticamente sem falhar a execução?"
  },
  {
    id: "d2_q72",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Particionamento no Spark vs Particionamento Delta",
    question: "Qual comando PySpark particiona um DataFrame na memória com reembaralhamento total de dados na rede (Full Shuffle) para garantir distribuição uniforme antes de operações pesadas?",
    options: [
      {
        id: "A",
        text: "`df.repartition(numParticoes)`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`df.coalesce(numParticoes)`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`df.drop()`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`df.sample()`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> `repartition(n)` força um Full Shuffle na rede para redistribuir os dados em exatamente `n` partições de tamanho homogêneo, aumentando ou diminuindo o paralelismo. O método `coalesce(n)` apenas reduz o número de partições combinando partições existentes sem realizar full shuffle.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> `coalesce` não faz full shuffle e não consegue aumentar o número de partições.</li><li><strong>C e D:</strong> Não têm relação com o particionamento de DataFrames.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> `repartition()` = Redefine número de partições com Full Shuffle na rede. `coalesce()` = Reduz partições sem full shuffle.</div>",
    prompt: "Qual comando PySpark particiona um DataFrame na memória com reembaralhamento total de dados na rede (Full Shuffle) para garantir distribuição uniforme antes de operações pesadas?"
  },
  {
    id: "d2_q73",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Uso de Broadcast Variables no PySpark",
    question: "Em um algoritmo PySpark customizado, você possui um dicionário Python estático com 5.000 códigos postais e nomes de cidades (50 KB). Como disponibilizar esse dicionário de forma eficiente para que todas as tarefas dos executores acessem o mapa sem enviá-lo repetidamente em cada tarefa individual?",
    options: [
      {
        id: "A",
        text: "Criar uma Variável de Transmissão (Broadcast Variable) usando `sc.broadcast(dicionario)`.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Gravar o dicionário em um banco de dados relacional e fazer uma consulta SELECT por registro.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Enviar o dicionário por e-mail para todos os nós.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Converter o dicionário em um arquivo MP4.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Broadcast Variables (`sc.broadcast(v)`) enviam uma única cópia em cache de uma variável somente-leitura para cada nó executor do cluster, em vez de empacotar uma cópia junto com cada tarefa individual. Isso reduz drasticamente a sobrecarga de serialização e tráfego de rede.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas soluções que violam a eficiência computacional distribuída.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Compartilhamento estático de lookups no Spark: Use `sc.broadcast()` para distribuir cópias em cache nos nós.</div>",
    prompt: "Em um algoritmo PySpark customizado, você possui um dicionário Python estático com 5.000 códigos postais e nomes de cidades (50 KB). Como disponibilizar esse dicionário de forma eficiente para que todas as tarefas dos executores acessem o mapa sem enviá-lo repetidamente em cada tarefa individual?"
  },
  {
    id: "d2_q74",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Persistência em Cache no Spark: `cache()` vs `persist()`",
    question: "Qual é a diferença entre os métodos `df.cache()` e `df.persist()` no Apache Spark?",
    options: [
      {
        id: "A",
        text: "`cache()` armazena os dados com o nível padrão de armazenamento (`MEMORY_AND_DISK`), enquanto `persist()` permite especificar explicitamente níveis de armazenamento (como `MEMORY_ONLY`, `DISK_ONLY`, ou opções serializadas).",
        isCorrect: true
      },
      {
        id: "B",
        text: "`cache()` deleta o DataFrame e `persist()` salva no OneDrive.",
        isCorrect: false
      },
      {
        id: "C",
        text: "`cache()` foi descontinuado no Spark 3.0.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Ambos salvam os dados em arquivos CSV no desktop local.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> `df.cache()` é simplesmente um atalho de conveniência que chama `persist(StorageLevel.MEMORY_AND_DISK)`. O método `df.persist(storageLevel)` oferece controle granular sobre onde o DataFrame será retido na memória ou disco durante a execução do job.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Declarações falsas sem fundamentação técnica.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> `cache()` = persistência com nível padrão (`MEMORY_AND_DISK`). `persist(level)` = permite configurar o StorageLevel.</div>",
    prompt: "Qual é a diferença entre os métodos `df.cache()` e `df.persist()` no Apache Spark?"
  },
  {
    id: "d2_q75",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Limpeza de Recursos em Cache com `unpersist()`",
    question: "Após a conclusão das transformações pesadas que utilizaram um DataFrame mantido em cache com `df.cache()`, qual método deve ser invocado para liberar imediatamente a memória RAM dos nós executores?",
    options: [
      {
        id: "A",
        text: "`df.unpersist()`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`df.delete()`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`df.drop()`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`del df` apenas no Python sem avisar o cluster Spark.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O método `df.unpersist()` instrui explicitamente os executores Spark a removerem os blocos do DataFrame armazenados na memória e disco, liberando espaço para futuras tarefas e prevenindo erros de OutOfMemory (OOM).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B e C:</strong> Métodos que alteram colunas ou não existem para limpeza de cache.</li><li><strong>D:</strong> A instrução `del df` no Python remove apenas a referência local no Driver, sem liberar o cache distribuído nos nós.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Liberação de memória de cache no Spark: Sempre execute `df.unpersist()` após o término das etapas dependentes.</div>",
    prompt: "Após a conclusão das transformações pesadas que utilizaram um DataFrame mantido em cache com `df.cache()`, qual método deve ser invocado para liberar imediatamente a memória RAM dos nós executores?"
  },
  {
    id: "d2_q76",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Funções de Janela SQL (Window Functions) com PySpark",
    question: "Um engenheiro precisa calcular a média móvel de vendas dos últimos 3 dias para cada produto. Qual especificação de janela (`Window.partitionBy(...).orderBy(...)`) do PySpark define corretamente essa moldura de linhas (frame)?",
    options: [
      {
        id: "A",
        text: "`Window.partitionBy('ProdutoId').orderBy('DataVenda').rowsBetween(-2, 0)`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`Window.all().rows(3)`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`Window.orderBy('Preco').limit(3)`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`Window.partitionBy('Tudo').filter(3)`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Para calcular a média incluindo o dia atual e os 2 dias imediatamente anteriores (totalizando 3 dias), utiliza-se `Window.partitionBy('ProdutoId').orderBy('DataVenda').rowsBetween(-2, 0)` ou `Window.rangeBetween(-2, 0)`. Isso delimita o frame de agregação da função de janela.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Sintaxes inválidas na API de Janelas do PySpark.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Window Functions: `rowsBetween(-2, 0)` inclui a linha atual (0) e as duas anteriores (-2).</div>",
    prompt: "Um engenheiro precisa calcular a média móvel de vendas dos últimos 3 dias para cada produto. Qual especificação de janela (`Window.partitionBy(...).orderBy(...)`) do PySpark define corretamente essa moldura de linhas (frame)?"
  },
  {
    id: "d2_q77",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Tratamento de Arquivos Delta Corrompidos com `FSCK REPAIR LIBRARIES`",
    question: "Em caso de falha de gravação ou inconsistência na tabela de catálogo, qual comando de manutenção verifica a integridade de arquivos do catálogo Metastore do Spark?",
    options: [
      {
        id: "A",
        text: "`MSCK REPAIR TABLE <tabela>`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`SCAN HARD DISK C:`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`FORMAT DRIVE FAT32`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`REBOOT WORKSPACE`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> `MSCK REPAIR TABLE` atualiza o catálogo de metadados identificando novas partições que foram gravadas diretamente no armazenamento físico e sincronizando o metastore.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Comandos sem qualquer relação com a governança de metadados do Spark.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Sincronização de catálogo e partições no Metastore: `MSCK REPAIR TABLE`.</div>",
    prompt: "Em caso de falha de gravação ou inconsistência na tabela de catálogo, qual comando de manutenção verifica a integridade de arquivos do catálogo Metastore do Spark?"
  },
  {
    id: "d2_q78",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Uso do Operador `CASE WHEN` em PySpark e T-SQL",
    question: "Qual é a função do PySpark equivalente à instrução SQL `CASE WHEN condicao THEN valor1 ELSE valor2 END` para categorização condicional de colunas em um DataFrame?",
    options: [
      {
        id: "A",
        text: "`when(condicao, valor1).otherwise(valor2)`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`if_then_else(condicao, valor1, valor2)`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`switch_case(valor1, valor2)`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`choose(condicao, 1, 2)`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> No PySpark, a avaliação condicional em colunas utiliza a combinação encadeada de funções `pyspark.sql.functions.when(condicao, valor).when(...).otherwise(valor_padrao)`.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Funções inexistentes na biblioteca oficial de funções do Spark SQL.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Condicional no PySpark: `when(cond, val).otherwise(default)`.</div>",
    prompt: "Qual é a função do PySpark equivalente à instrução SQL `CASE WHEN condicao THEN valor1 ELSE valor2 END` para categorização condicional de colunas em um DataFrame?"
  },
  {
    id: "d2_q79",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Geração de Coluna com Timestamp de Ingestão e Criptografia HASH",
    question: "Durante a ingestão na camada Bronze, a política de auditoria exige que cada linha gravada contenha um timestamp da execução e um hash criptográfico das colunas identificadoras para verificação de duplicidade. Quais funções PySpark atendem a esse requisito?",
    options: [
      {
        id: "A",
        text: "`.withColumn('IngestionTime', current_timestamp()).withColumn('RowHash', sha2(concat_ws('||', col('id'), col('codigo')), 256))`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`.withColumn('Time', 'now').withColumn('Hash', '123')`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`.add_date().add_random()`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`.append_system_metrics()`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> `current_timestamp()` gera o carimbo de data e hora do momento da execução. A função `sha2(col, 256)` gera a assinatura SHA-256 (com 256 bits) para garantir integridade e detectar alterações em registros combinados via `concat_ws`.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Sintaxes incorretas ou literais estáticos sem cálculo real de hash.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Padrão de auditoria de dados: `current_timestamp()` e `sha2(concat_ws(...), 256)`.</div>",
    prompt: "Durante a ingestão na camada Bronze, a política de auditoria exige que cada linha gravada contenha um timestamp da execução e um hash criptográfico das colunas identificadoras para verificação de duplicidade. Quais funções PySpark atendem a esse requisito?"
  },
  {
    id: "d2_q80",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Mapeamento de Tipos de Dados complexos com `MapType`",
    question: "Um desenvolvedor precisa armazenar atributos flexíveis de produtos no formato chave-valor (`cor: azul`, `tamanho: G`, `voltagem: 220v`) em uma única coluna sem criar centenas de colunas esparsas na tabela. Qual tipo de dado do Spark SQL é o mais indicado?",
    options: [
      {
        id: "A",
        text: "`MapType(StringType(), StringType())`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`IntegerType()`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`BooleanType()`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`BinaryType()` sem decodificação",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> `MapType(keyType, valueType)` permite armazenar coleções de pares chave-valor dentro de uma coluna única. As chaves podem ser consultadas nativamente com notação de colchetes (`coluna['cor']`), preservando flexibilidade de esquema.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B e C:</strong> Tipos primitivos escalares que não suportam dicionários de múltiplos atributos.</li><li><strong>D:</strong> Armazenar binário bruto impediria consultas colunares eficientes sem decodificação.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Pares Chave-Valor no Spark: `MapType(StringType(), StringType())`.</div>",
    prompt: "Um desenvolvedor precisa armazenar atributos flexíveis de produtos no formato chave-valor (`cor: azul`, `tamanho: G`, `voltagem: 220v`) em uma única coluna sem criar centenas de colunas esparsas na tabela. Qual tipo de dado do Spark SQL é o mais indicado?"
  },
  {
    id: "d2_q81",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Leitura de Dados Incrementais com Delta Change Data Feed (CDF)",
    question: "Qual recurso nativo do Delta Lake permite aos consumidores lerem apenas as linhas que foram inseridas, atualizadas ou deletadas em uma tabela Delta, incluindo os valores 'antes' e 'depois' das atualizações (`_change_type`)?",
    options: [
      {
        id: "A",
        text: "Delta Change Data Feed (CDF / `readChangeFeed`)",
        isCorrect: true
      },
      {
        id: "B",
        text: "Comparação manual de backups de fita magnética a cada 10 minutos.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Exclusão diária de toda a base para forçar recarga integral.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Envio de cópias por fax para a equipe de controle.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Delta Change Data Feed (CDF) rastreia alterações em nível de linha na tabela Delta. Ao habilitar `delta.enableChangeDataFeed = true`, consumidores podem ler via `readChangeFeed` os registros de inserção (`insert`), exclusão (`delete`) e valores antes/depois de modificação (`update_preimage`, `update_postimage`).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Práticas ultrapassadas e não tecnológicas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Delta Change Data Feed (CDF) expõe o histórico de alterações (Insert, Update, Delete) com metadados `_change_type`.</div>",
    prompt: "Qual recurso nativo do Delta Lake permite aos consumidores lerem apenas as linhas que foram inseridas, atualizadas ou deletadas em uma tabela Delta, incluindo os valores 'antes' e 'depois' das atualizações (`_change_type`)?"
  },
  {
    id: "d2_q82",
    domain: "Domínio 2: Ingerir e transformar dados (40-45%)",
    type: "single",
    title: "Sincronização de Esquema com `ALTER TABLE ... SYNC METADATA`",
    question: "Quando uma tabela Delta tem arquivos Parquet adicionados diretamente no OneLake por um processo externo ou via atalho (Shortcut), qual comando no SQL Analytics Endpoint garante que os metadados do catálogo estejam sincronizados com os arquivos físicos mais recentes?",
    options: [
      {
        id: "A",
        text: "A sincronização é executada automaticamente pelo Fabric Metadata Sync em segundo plano, ou pode ser forçada executando uma consulta no SQL Endpoint.",
        isCorrect: true
      },
      {
        id: "B",
        text: "É necessário reiniciar todos os roteadores de rede da Microsoft.",
        isCorrect: false
      },
      {
        id: "C",
        text: "A tabela deve ser deletada e recriada do zero impreterivelmente.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O Fabric não reconhece arquivos adicionados externamente.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric possui um serviço de Metadata Sync que atualiza continuamente o catálogo relacional do SQL Analytics Endpoint sempre que novos commits são adicionados ao `_delta_log` no OneLake. A consulta ao SQL Endpoint atualiza a visão mais recente de forma consistente.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Afirmações incorretas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Sincronização de Metadados: O Fabric sincroniza automaticamente os metadados do Delta Log para o SQL Analytics Endpoint.</div>",
    prompt: "Quando uma tabela Delta tem arquivos Parquet adicionados diretamente no OneLake por um processo externo ou via atalho (Shortcut), qual comando no SQL Analytics Endpoint garante que os metadados do catálogo estejam sincronizados com os arquivos físicos mais recentes?"
  },
  {
    id: "d3_q01",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Diagnóstico de Picos com o Fabric Capacity Metrics App",
    question: "Um administrador de capacidade nota lentidão generalizada no workspace corporativo e abre o Microsoft Fabric Capacity Metrics App. Qual visão gráfica no aplicativo permite identificar o momento exato em que o consumo de CUs ultrapassou 100% e detalhar as operações responsáveis?",
    options: [
      {
        id: "A",
        text: "A exibição de ponto no tempo (Timepoint Drill-Through / Visualização de Timepoint de 30 segundos).",
        isCorrect: true
      },
      {
        id: "B",
        text: "O monitor de processos do Gerenciador de Tarefas do Windows 11.",
        isCorrect: false
      },
      {
        id: "C",
        text: "A listagem de e-mails recebidos na caixa de entrada do Outlook.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O gráfico de tráfego de rede Wi-Fi do roteador local.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> No Fabric Capacity Metrics App, ao clicar em qualquer ponto da curva de utilização na linha do tempo, a ferramenta abre o 'Timepoint drill-through' (análise de ponto no tempo com granularidade de 30 segundos). Essa visão discrimina as operações de Interactive e Background e exibe exatamente quais itens, usuários e operações consumiram CUs naquele instante.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Ferramentas locais ou não relacionadas à infraestrutura de capacidade do Fabric.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Fabric Capacity Metrics App: O 'Timepoint view' decompõe o consumo de CUs em 30 segundos por item e operação.</div>",
    prompt: "Um administrador de capacidade nota lentidão generalizada no workspace corporativo e abre o Microsoft Fabric Capacity Metrics App. Qual visão gráfica no aplicativo permite identificar o momento exato em que o consumo de CUs ultrapassou 100% e detalhar as operações responsáveis?"
  },
  {
    id: "d3_q02",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Diferença entre Operações Interativas e de Segundo Plano nas Métricas",
    question: "No Capacity Metrics App, as operações são categorizadas em 'Interactive' e 'Background'. Como essa categorização afeta o cálculo de uso de CUs e o mecanismo de Smoothing (suavização)?",
    options: [
      {
        id: "A",
        text: "Operações interativas (como DAX e consultas visuais de relatórios) são distribuídas em uma janela móvel de 5 minutos, enquanto operações em segundo plano (como Spark jobs e Data Pipelines) são distribuídas em uma janela móvel de 24 horas.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Operações interativas são gratuitas e operações de segundo plano são faturadas em dobro.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Ambas as operações são avaliadas exatamente em 1 segundo sem qualquer suavização.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Operações de segundo plano são bloqueadas automaticamente às 18:00 horas.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O mecanismo de Smoothing é assimétrico por design: cargas interativas (geradas por usuários interagindo em relatórios) são suavizadas em janelas curtas de 5 minutos; cargas de segundo plano (ETL, pipelines pesados, batches de Spark) são amortizadas ao longo de 24 horas completas para absorver o impacto de bursts noturnos.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Conceitos incorretos de faturamento e suavização.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Regra crítica de métricas: Interactive = 5 minutos de Smoothing; Background = 24 horas de Smoothing.</div>",
    prompt: "No Capacity Metrics App, as operações são categorizadas em 'Interactive' e 'Background'. Como essa categorização afeta o cálculo de uso de CUs e o mecanismo de Smoothing (suavização)?"
  },
  {
    id: "d3_q03",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Métrica de Armazenamento no OneLake vs Capacidade Computacional",
    question: "O Capacity Metrics App reporta um consumo elevado de 'OneLake Storage (GB)'. Como o armazenamento do OneLake é faturado no Microsoft Fabric em relação às Capacity Units (CUs)?",
    options: [
      {
        id: "A",
        text: "O armazenamento é faturado como uma taxa separada por Gigabyte/Mês (baseada na taxa padrão de ADLS Gen2), não consumindo as CUs computacionais do F-SKU adquirido.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Cada 1 GB de armazenamento consome permanentemente 10 CUs da capacidade contratada.",
        isCorrect: false
      },
      {
        id: "C",
        text: "O armazenamento é 100% gratuito e ilimitado para sempre sem nenhum custo.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O armazenamento só pode ser pago com Bitcoins.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> No Microsoft Fabric, Computação e Armazenamento são faturados separadamente. O F-SKU cobre as Capacity Units de processamento computacional. O armazenamento do OneLake (tabelas Delta e arquivos) é tarifado com base no volume de dados em GB por mês, à mesma tarifa atrativa do Azure Data Lake Storage Gen2.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Armazenamento não consome nem diminui as CUs de computação do F-SKU.</li><li><strong>C e D:</strong> Falsas noções financeiras.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> No Fabric: F-SKU = Computação (CUs); OneLake = Armazenamento separado faturado por GB/mês (sem consumir CUs).</div>",
    prompt: "O Capacity Metrics App reporta um consumo elevado de 'OneLake Storage (GB)'. Como o armazenamento do OneLake é faturado no Microsoft Fabric em relação às Capacity Units (CUs)?"
  },
  {
    id: "d3_q04",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Estágio 1 de Throttling: Interactive Delay",
    question: "Quando uma capacidade F16 atinge 100% de sobrecarga cumulativa na janela móvel, qual é o sintoma imediato experimentado pelos usuários corporativos que acessam relatórios do Power BI durante o Estágio 1 de Throttling (Interactive Delay)?",
    options: [
      {
        id: "A",
        text: "As consultas visuais continuam funcionando, mas um atraso artificial progressivo (delay) de alguns segundos é adicionado à resposta de cada interação para desestimular o consumo excessivo.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Todos os computadores da empresa são desligados.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Os relatórios exibem mensagens de erro 500 imediatamente sem carregar nenhum dado.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Os dados de vendas são apagados do banco de dados.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Estágio 1 (Interactive Delay) é uma medida preventiva de throttling: o Fabric não rejeita as consultas interativas de imediato, mas injeta um atraso gradual nas respostas visuais. Se a sobrecarga persistir e alcançar o limite do estágio 2, aí sim ocorre a Rejeição Interativa (Interactive Rejection).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B e D:</strong> Consequências absurdas.</li><li><strong>C:</strong> Erros de rejeição só acontecem a partir do Estágio 2 (Interactive Rejection).</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Throttling Estágio 1: Introduz atraso (Delay) sem rejeitar requisições interativas.</div>",
    prompt: "Quando uma capacidade F16 atinge 100% de sobrecarga cumulativa na janela móvel, qual é o sintoma imediato experimentado pelos usuários corporativos que acessam relatórios do Power BI durante o Estágio 1 de Throttling (Interactive Delay)?"
  },
  {
    id: "d3_q05",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "multi",
    title: "Ações de Remediação para Sobrecarga Contínua de Capacidade",
    question: "Quais DUAS ações administrativas são recomendadas para mitigar uma sobrecarga contínua de capacidade identificada no Capacity Metrics App? (Selecione 2 alternativas)",
    options: [
      {
        id: "A",
        text: "Fazer um upgrade temporário ou permanente do F-SKU no portal do Azure (ex: de F32 para F64) para aumentar o número de CUs disponíveis.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Reescalonar ou escalonar a execução de Data Pipelines pesados e jobs Spark para horários de menor movimento em vez de concentrá-los todos simultaneamente à meia-noite.",
        isCorrect: true
      },
      {
        id: "C",
        text: "Deletar todos os workspaces de produção imediatamente.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Desativar o firewall do Windows em todos os computadores da empresa.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A mitigação de sobrecarga envolve: 1) Dimensionamento vertical (scale-up de F-SKU no Azure) e 2) Otimização operacional das cargas de trabalho (orquestração distribuída no tempo, evitando que todos os pipelines e jobs Spark concorram no mesmo instante).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C e D:</strong> Práticas destrutivas que não resolvem o problema de arquitetura.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Remediação de Capacidade: Aumentar F-SKU ou redistribuir pipelines pesados ao longo das 24 horas.</div>",
    prompt: "Quais DUAS ações administrativas são recomendadas para mitigar uma sobrecarga contínua de capacidade identificada no Capacity Metrics App? (Selecione 2 alternativas)"
  },
  {
    id: "d3_q06",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Identificação de 'Top Consumers' no Capacity Metrics App",
    question: "Na guia de detalhes de itens do Capacity Metrics App, qual métrica quantifica exatamente o percentual de CUs consumido por um Lakehouse ou Warehouse específico em relação à capacidade total contratada?",
    options: [
      {
        id: "A",
        text: "`CU %` (Percentual de CU consumido) e `Total CU (s)` (Total de segundos de CU acumulados).",
        isCorrect: true
      },
      {
        id: "B",
        text: "Número de cliques de mouse no relatório.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Quantidade de caracteres no código SQL.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Tamanho da janela do monitor em pixels.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Capacity Metrics App resume o consumo computacional de cada artefato usando `Total CU (s)` (Capacity Unit Seconds) e o respectivo `CU %` da capacidade disponível, permitindo ranquear com precisão quais itens são os maiores consumidores ('Top Consumers') de recursos.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Métricas irrelevantes e inexistentes.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Top Consumers são ranqueados por `Total CU (s)` e `CU %` no Capacity Metrics App.</div>",
    prompt: "Na guia de detalhes de itens do Capacity Metrics App, qual métrica quantifica exatamente o percentual de CUs consumido por um Lakehouse ou Warehouse específico em relação à capacidade total contratada?"
  },
  {
    id: "d3_q07",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Monitoramento de Operações de Autoscale (Capacidades Power BI Premium)",
    question: "Em locatários com capacidade que possuem o recurso de Autoscale ativado, como o sistema reage quando ocorre um pico que ultrapassa a capacidade base por um período contínuo?",
    options: [
      {
        id: "A",
        text: "Acrescenta automaticamente 1 vCore adicional por períodos de 24 horas para evitar throttling, cobrando o valor correspondente no Azure.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Rejeita imediatamente todas as operações de gravação.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Desliga os servidores durante o fim de semana.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Envia uma carta impressa pelo correio.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O recurso de Autoscale em capacidades corporativas do Power BI / Fabric aloca automaticamente vCores sob demanda para absorver picos extremos que não puderam ser amortizados pelo smoothing, garantindo que usuários finais não sofram rejeição de consultas.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Incorretos.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Autoscale: Adiciona nós/núcleos sob demanda para evitar rejeição e throttling durante picos extremos.</div>",
    prompt: "Em locatários com capacidade que possuem o recurso de Autoscale ativado, como o sistema reage quando ocorre um pico que ultrapassa a capacidade base por um período contínuo?"
  },
  {
    id: "d3_q08",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Integração do Fabric com Azure Monitor e Log Analytics",
    question: "Uma organização deseja centralizar os logs de execução de Notebooks, Pipelines e consultas SQL do Fabric em um workspace do Azure Log Analytics para retenção histórica de 2 anos e criação de alertas no KQL. Como essa integração é habilitada?",
    options: [
      {
        id: "A",
        text: "Configurando as opções de 'Azure Log Analytics' nas configurações do Workspace do Fabric e conectando ao Log Analytics Workspace de destino no Azure.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Copiando e colando os logs em arquivos `.log` no Notepad diariamente.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Instalando um agente do Windows 98 em cada nó do Fabric.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O Fabric não se integra com o Azure Monitor.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric suporta integração nativa de auditoria com o Azure Monitor / Log Analytics. Nas configurações do Workspace (Workspace Settings -> Azure Integration -> Log Analytics), o administrador vincula o workspace a uma instância do Azure Log Analytics para exportação contínua de telemetria.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas noções técnicas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Exportação contínua de telemetria corporativa: Conectar Workspace Settings ao Azure Log Analytics.</div>",
    prompt: "Uma organização deseja centralizar os logs de execução de Notebooks, Pipelines e consultas SQL do Fabric em um workspace do Azure Log Analytics para retenção histórica de 2 anos e criação de alertas no KQL. Como essa integração é habilitada?"
  },
  {
    id: "d3_q09",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Diferença entre Capacity Units (CUs) e vCores no Fabric",
    question: "Qual é a relação matemática e técnica oficial entre 1 Capacity Unit (CU) e vCores computacionais nas capacidades F-SKU do Microsoft Fabric?",
    options: [
      {
        id: "A",
        text: "2 CUs equivalem aproximadamente ao poder computacional de 1 vCore de computação do Azure (ex: F64 fornece 64 CUs, equivalentes a 32 vCores).",
        isCorrect: true
      },
      {
        id: "B",
        text: "1 CU equivale a 1.000 vCores.",
        isCorrect: false
      },
      {
        id: "C",
        text: "1 CU é igual a 1 Terabyte de memória RAM.",
        isCorrect: false
      },
      {
        id: "D",
        text: "CUs e vCores são grandezas sem nenhuma relação.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Na documentação oficial do Microsoft Fabric: 2 CUs correspondem ao poder de processamento equivalente a 1 vCore tradicional de nuvem. Logo, um SKU F64 fornece 64 CUs, o equivalente computacional a 32 vCores (exatamente a mesma potência de um nó P1 do Power BI Premium).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Proporções e definições errôneas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Equivalência oficial do Fabric: 2 CUs = 1 vCore (ex: F64 = 32 vCores).</div>",
    prompt: "Qual é a relação matemática e técnica oficial entre 1 Capacity Unit (CU) e vCores computacionais nas capacidades F-SKU do Microsoft Fabric?"
  },
  {
    id: "d3_q10",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Identificação de Usuários Ofensores no Capacity Metrics App",
    question: "No drill-through de uma operação de sobrecarga no Capacity Metrics App, qual campo indica qual usuário ou conta de serviço (Service Principal) disparou a consulta causadora do pico?",
    options: [
      {
        id: "A",
        text: "`User` (UPN do usuário ou ID da Identidade de Serviço / Service Principal)",
        isCorrect: true
      },
      {
        id: "B",
        text: "`HardwareMACAddress` do monitor do computador",
        isCorrect: false
      },
      {
        id: "C",
        text: "`MotherboardSerialNumber` do servidor",
        isCorrect: false
      },
      {
        id: "D",
        text: "O nome do fabricante do mouse",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O campo `User` na tabela de detalhamento do Timepoint exibe o User Principal Name (UPN) do usuário corporativo ou o Application ID do Service Principal responsável pela submissão do job ou consulta geradora de consumo.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Metadados inexistentes e absurdos.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Rastreamento de usuários: O campo `User` identifica quem disparou a operação causadora de consumo no Fabric.</div>",
    prompt: "No drill-through de uma operação de sobrecarga no Capacity Metrics App, qual campo indica qual usuário ou conta de serviço (Service Principal) disparou a consulta causadora do pico?"
  },
  {
    id: "d3_q11",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Métrica de Rejeição em Segundo Plano (Background Rejection)",
    question: "Qual é a consequência técnica quando o Capacity Metrics App indica que a capacidade atingiu o Estágio 3 de Throttling (Background Rejection)?",
    options: [
      {
        id: "A",
        text: "Qualquer novo job em segundo plano (como execuções de Data Pipelines, agendamento de Dataflows e jobs Spark) falha imediatamente no início com erro de rejeição por capacidade esgotada.",
        isCorrect: true
      },
      {
        id: "B",
        text: "A Microsoft apaga todos os workspaces da assinatura.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Os pipelines continuam funcionando sem interrupção.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O portal do Fabric muda de cor para verde.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Estágio 3 é o nível mais severo de proteção: para impedir que a sobrecarga comprometa a estabilidade do datacenter e a fila acumulada, todas as novas tarefas e pipelines em segundo plano são rejeitadas sumariamente até que o consumo caia abaixo de 100%.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas declarações.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Estágio 3 de Throttling (Background Rejection): Falha imediata de novos pipelines, dataflows e jobs Spark.</div>",
    prompt: "Qual é a consequência técnica quando o Capacity Metrics App indica que a capacidade atingiu o Estágio 3 de Throttling (Background Rejection)?"
  },
  {
    id: "d3_q12",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Notificações por E-mail de Sobrecarga de Capacidade",
    question: "Como os administradores de capacidade podem receber alertas automáticos por e-mail antes que a capacidade atinja os estágios severos de throttling?",
    options: [
      {
        id: "A",
        text: "Configurando alertas de capacidade no portal de administração do Fabric (Admin Portal) definindo limiares percentuais de utilização (ex: 80%, 90% de uso).",
        isCorrect: true
      },
      {
        id: "B",
        text: "Instalando um plugin de terceiros não homologado no navegador.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Pedindo para os usuários ligarem por telefone sempre que sentirem lentidão.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Não é possível configurar alertas de capacidade no Fabric.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O portal de administração do Fabric permite aos administradores definir políticas de notificação por e-mail quando a utilização da capacidade atinge limiares predeterminados de advertência, possibilitando ações preventivas antes do throttling.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas noções de gestão de capacidade.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Alertas de Capacidade: Configurados no Admin Portal com notificações proativas baseadas em limiares de uso.</div>",
    prompt: "Como os administradores de capacidade podem receber alertas automáticos por e-mail antes que a capacidade atinja os estágios severos de throttling?"
  },
  {
    id: "d3_q13",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Schema `queryinsights` no Fabric Warehouse",
    question: "No Fabric Warehouse e no SQL Analytics Endpoint, qual esquema especial de sistema fornece exibições pré-construídas para analisar o histórico de consultas, durações e consumo de recursos?",
    options: [
      {
        id: "A",
        text: "`sys` apenas",
        isCorrect: false
      },
      {
        id: "B",
        text: "`queryinsights`",
        isCorrect: true
      },
      {
        id: "C",
        text: "`information_schema` apenas",
        isCorrect: false
      },
      {
        id: "D",
        text: "`dbo.perf_logs`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric Warehouse disponibiliza o schema nativo `queryinsights`, contendo exibições otimizadas prontas para uso: `queryinsights.exec_requests_history`, `queryinsights.frequently_run_queries` e `queryinsights.long_running_queries`.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A e C:</strong> Esquemas padrão ANSI/SQL tradicionais que não trazem as métricas agregadas específicas do Fabric.</li><li><strong>D:</strong> Nome fictício.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Diagnóstico de Consultas no Fabric: Schema oficial `queryinsights`.</div>",
    prompt: "No Fabric Warehouse e no SQL Analytics Endpoint, qual esquema especial de sistema fornece exibições pré-construídas para analisar o histórico de consultas, durações e consumo de recursos?"
  },
  {
    id: "d3_q14",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Identificação de Consultas Lentas com `queryinsights.long_running_queries`",
    question: "Um engenheiro de dados precisa identificar as 10 consultas T-SQL que tiveram a maior duração média de execução nos últimos 7 dias no Fabric Warehouse. Qual consulta T-SQL fornece essa informação diretamente?",
    options: [
      {
        id: "A",
        text: "`SELECT TOP 10 * FROM queryinsights.long_running_queries ORDER BY median_total_elapsed_time_ms DESC;`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`SELECT * FROM sys.tables WHERE is_slow = 1;`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`KILL ALL SLOW QUERIES;`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`DBCC CHECKALLOC;`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A view `queryinsights.long_running_queries` agrega consultas T-SQL históricas calculando métricas como mediana e máximo de tempo decorrido em milissegundos (`median_total_elapsed_time_ms`), sendo a ferramenta ideal para localizar queries ofensivas.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Sintaxes inexistentes ou comandos que não analisam histórico de execução.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Consultas lentas no Warehouse: `queryinsights.long_running_queries`.</div>",
    prompt: "Um engenheiro de dados precisa identificar as 10 consultas T-SQL que tiveram a maior duração média de execução nos últimos 7 dias no Fabric Warehouse. Qual consulta T-SQL fornece essa informação diretamente?"
  },
  {
    id: "d3_q15",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Diagnóstico de Texto de Consulta e Sessão com `exec_requests_history`",
    question: "Para auditar o texto exato do comando SQL executado, o ID da sessão e a contagem de linhas retornadas de consultas executadas nas últimas 24 horas no Warehouse, qual exibição do schema `queryinsights` deve ser consultada?",
    options: [
      {
        id: "A",
        text: "`queryinsights.exec_requests_history`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`queryinsights.user_passwords`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`dbo.QueryLogFile`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`sys.dm_os_memory_nodes`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> `queryinsights.exec_requests_history` registra cada comando T-SQL executado no Fabric Warehouse/SQL Endpoint, contendo colunas essenciais como `command`, `session_id`, `status`, `row_count`, `start_time` e `total_elapsed_time_ms`.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Inexistentes ou não aplicáveis para auditoria de requisições no Fabric.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Histórico individual de comandos: `queryinsights.exec_requests_history`.</div>",
    prompt: "Para auditar o texto exato do comando SQL executado, o ID da sessão e a contagem de linhas retornadas de consultas executadas nas últimas 24 horas no Warehouse, qual exibição do schema `queryinsights` deve ser consultada?"
  },
  {
    id: "d3_q16",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Consultas Frequentes com `queryinsights.frequently_run_queries`",
    question: "Como um arquiteto pode verificar quais consultas são executadas centenas de vezes ao dia pelo Power BI, visando criar tabelas agregadas ou aceleradores para economizar computação?",
    options: [
      {
        id: "A",
        text: "Consultando a view `queryinsights.frequently_run_queries` e ordenando pela coluna `execution_count` descendente.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Perguntando para cada funcionário quantas vezes ele clicou no relatório.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Desconectando o Power BI do Warehouse.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Lendo os arquivos de log do IIS do servidor web local.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> `queryinsights.frequently_run_queries` consolida padrões de consulta idênticos e expõe o `execution_count`. Consultas com alta frequência de execução e alto tempo cumulativo são as candidatas ideais para materialização prévia na camada Gold.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Abordagens inviáveis ou sem sentido técnico.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Consultas repetitivas: `queryinsights.frequently_run_queries` ordenado por `execution_count`.</div>",
    prompt: "Como um arquiteto pode verificar quais consultas são executadas centenas de vezes ao dia pelo Power BI, visando criar tabelas agregadas ou aceleradores para economizar computação?"
  },
  {
    id: "d3_q17",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "DMV `sys.dm_exec_sessions` para Sessões Ativas",
    question: "Um DBA precisa inspecionar em tempo real quais conexões e usuários estão conectados no momento presente ao Fabric Warehouse. Qual Dynamic Management View (DMV) de sistema padrão fornece essa informação?",
    options: [
      {
        id: "A",
        text: "`sys.dm_exec_sessions`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`sys.dm_hardware_inventory`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`sys.all_active_users_worldwide`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`sp_who_is_active_on_internet`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> `sys.dm_exec_sessions` é uma DMV nativa suportada pelo Fabric Warehouse que retorna informações sobre todas as sessões autenticadas ativas, incluindo `session_id`, `login_name`, `client_interface_name` e horários de conexão.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> DMVs inexistentes.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Sessões ativas no Warehouse: `SELECT * FROM sys.dm_exec_sessions`.</div>",
    prompt: "Um DBA precisa inspecionar em tempo real quais conexões e usuários estão conectados no momento presente ao Fabric Warehouse. Qual Dynamic Management View (DMV) de sistema padrão fornece essa informação?"
  },
  {
    id: "d3_q18",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Cancelamento de Consultas em Execução com `KILL`",
    question: "Uma consulta mal formulada por um analista está executando há 3 horas sem parar, consumindo recursos excessivos do Fabric Warehouse. Qual comando T-SQL deve ser executado pelo administrador para cancelar essa sessão específica?",
    options: [
      {
        id: "A",
        text: "`KILL '<session_id>';`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`DROP USER '<login>';`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`STOP SERVER IMMEDIATE;`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`DELETE FROM sys.dm_exec_requests;`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O comando padrão `KILL <session_id>` é suportado no Fabric Warehouse para abortar a execução de uma sessão específica e forçar o cancelamento imediato de sua consulta ativa, liberando os recursos associados.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Excluir o usuário não encerra a transação já em andamento e causa problemas de segurança.</li><li><strong>C e D:</strong> Sintaxes incorretas; DMVs são somente leitura e não aceitam comando DELETE.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Abortar sessão travada no Warehouse: Comando T-SQL `KILL <session_id>`.</div>",
    prompt: "Uma consulta mal formulada por um analista está executando há 3 horas sem parar, consumindo recursos excessivos do Fabric Warehouse. Qual comando T-SQL deve ser executado pelo administrador para cancelar essa sessão específica?"
  },
  {
    id: "d3_q19",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "multi",
    title: "Colunas Críticas da View `queryinsights.exec_requests_history`",
    question: "Quais DUAS colunas presentes na view `queryinsights.exec_requests_history` são fundamentais para diagnosticar se uma consulta falhou e qual erro foi gerado? (Selecione 2 alternativas)",
    options: [
      {
        id: "A",
        text: "`status` (indicando se a consulta está Completed, Failed ou Canceled)",
        isCorrect: true
      },
      {
        id: "B",
        text: "`error_message` (detalhando a mensagem descritiva do erro que causou a falha)",
        isCorrect: true
      },
      {
        id: "C",
        text: "`user_home_address`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`credit_card_balance`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A view `queryinsights.exec_requests_history` traz as colunas `status` (que assume valores como 'Completed', 'Failed', 'Canceled') e `error_message`, permitindo diagnosticar a causa exata de consultas com erro sem depender de reprodução manual.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C e D:</strong> Colunas fictícias.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Diagnóstico de erros no SQL Endpoint/Warehouse: `status` e `error_message` na `exec_requests_history`.</div>",
    prompt: "Quais DUAS colunas presentes na view `queryinsights.exec_requests_history` são fundamentais para diagnosticar se uma consulta falhou e qual erro foi gerado? (Selecione 2 alternativas)"
  },
  {
    id: "d3_q20",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Monitoramento de Bloqueios e Esperas (Wait Statistics)",
    question: "Ao analisar a lentidão de uma consulta no Fabric Warehouse, qual informação do plano de execução distribuído auxilia a identificar se a consulta ficou presa aguardando dados da rede do OneLake?",
    options: [
      {
        id: "A",
        text: "Métricas de tempos de espera de I/O de armazenamento remoto (Remote Storage I/O Waits) no plano de consulta do motor distribuído.",
        isCorrect: true
      },
      {
        id: "B",
        text: "A velocidade de rotação do disco mecânico do servidor.",
        isCorrect: false
      },
      {
        id: "C",
        text: "A marca da placa-mãe do Azure.",
        isCorrect: false
      },
      {
        id: "D",
        text: "A temperatura do processador da estação do usuário.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> No motor distribuído do Fabric Warehouse, a leitura e gravação acontecem no OneLake sobre rede. Tempos anormais de I/O remoto nos planos de execução indicam gargalos de rede ou arquivos excessivamente pequenos exigindo alto número de requisições HTTPS GET para o armazenamento.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Detalhes físicos irrelevantes na computação em nuvem gerenciada.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Performance de I/O no Warehouse: Monitorar tempos de I/O de armazenamento remoto no plano distribuído.</div>",
    prompt: "Ao analisar a lentidão de uma consulta no Fabric Warehouse, qual informação do plano de execução distribuído auxilia a identificar se a consulta ficou presa aguardando dados da rede do OneLake?"
  },
  {
    id: "d3_q21",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "View `queryinsights.frequently_run_queries` e Agregações de Desempenho",
    question: "Qual métrica na view `queryinsights.frequently_run_queries` reflete a variação (inconsistência) no tempo de resposta de uma consulta ao longo de múltiplas execuções?",
    options: [
      {
        id: "A",
        text: "A discrepância entre `min_total_elapsed_time_ms` e `max_total_elapsed_time_ms` (indicando oscilação de concorrência ou flutuação de cache).",
        isCorrect: true
      },
      {
        id: "B",
        text: "A taxa de compressão do arquivo ZIP gerado.",
        isCorrect: false
      },
      {
        id: "C",
        text: "O número de cores usadas no gráfico do Power BI.",
        isCorrect: false
      },
      {
        id: "D",
        text: "A data de expiração da assinatura do Office 365.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A grande diferença entre `min_total_elapsed_time_ms` e `max_total_elapsed_time_ms` para uma mesma consulta frequente indica instabilidade de performance gerada por bloqueios concorrentes, contenção de recursos ou diferenças entre leitura em cold cache vs warm cache.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsos fatores sem impacto no tempo de consulta T-SQL.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Oscilação de performance: Analisar dispersão entre `min` e `max_total_elapsed_time_ms`.</div>",
    prompt: "Qual métrica na view `queryinsights.frequently_run_queries` reflete a variação (inconsistência) no tempo de resposta de uma consulta ao longo de múltiplas execuções?"
  },
  {
    id: "d3_q22",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Tamanho de Resultados e `row_count` no Histórico",
    question: "Um relatório do Power BI em DirectQuery está sobrecarregando a capacidade. Ao analisar `queryinsights.exec_requests_history`, você nota consultas que retornam `row_count` superior a 5 milhões de linhas para a interface visual. Qual é o problema arquitetural evidente?",
    options: [
      {
        id: "A",
        text: "O relatório está solicitando dados analíticos em nível transacional sem aplicar filtros nem agregações adequadas, transferindo milhões de linhas desnecessárias para o cliente em vez de resumir no banco.",
        isCorrect: true
      },
      {
        id: "B",
        text: "O Fabric Warehouse não suporta consultas com mais de 100 linhas.",
        isCorrect: false
      },
      {
        id: "C",
        text: "O monitor do usuário não tem resolução suficiente.",
        isCorrect: false
      },
      {
        id: "D",
        text: "A tabela Delta do OneLake está corrompida.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Relatórios de BI devem solicitar dados sumarizados. Quando uma consulta visual transfere milhões de linhas sem agregação (`row_count` extremo), consome quantidades massivas de memória de rede e CUs desnecessariamente. A solução é filtrar e agregar no modelo semântico.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas declarações; o Warehouse suporta bilhões de linhas, mas a má prática está no consumo indevido de relatórios visuais.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Boas práticas de BI: Consultas de relatórios devem retornar dados agregados, evitando transferir milhões de linhas brutas para os visuais.</div>",
    prompt: "Um relatório do Power BI em DirectQuery está sobrecarregando a capacidade. Ao analisar `queryinsights.exec_requests_history`, você nota consultas que retornam `row_count` superior a 5 milhões de linhas para a interface visual. Qual é o problema arquitetural evidente?"
  },
  {
    id: "d3_q23",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Retenção Padrão dos Dados no Schema `queryinsights`",
    question: "Por quantos dias o Microsoft Fabric Warehouse retém o histórico de consultas no schema `queryinsights` por padrão?",
    options: [
      {
        id: "A",
        text: "30 dias",
        isCorrect: true
      },
      {
        id: "B",
        text: "1 hora apenas",
        isCorrect: false
      },
      {
        id: "C",
        text: "10 anos",
        isCorrect: false
      },
      {
        id: "D",
        text: "Os dados são apagados imediatamente após o término da consulta.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric Warehouse retém automaticamente as métricas de histórico de consultas no schema `queryinsights` por uma janela contínua de 30 dias. Para retenção superior a 30 dias, recomenda-se exportar os dados para o Azure Log Analytics.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Valores incorretos de retenção padrão.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Retenção nativa do `queryinsights`: 30 dias de histórico contínuo.</div>",
    prompt: "Por quantos dias o Microsoft Fabric Warehouse retém o histórico de consultas no schema `queryinsights` por padrão?"
  },
  {
    id: "d3_q24",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Identificação de Consultas Canceladas por Usuários",
    question: "Como identificar no Fabric se usuários estão cancelando consultas manualmente no navegador devido à impaciência com lentidão?",
    options: [
      {
        id: "A",
        text: "Filtrando `queryinsights.exec_requests_history` com `WHERE status = 'Canceled'` e analisando o tempo decorrido antes do cancelamento.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Verificando se o usuário clicou no botão 'X' do Windows.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Lendo as gravações de áudio do microfone do analista.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Não há registro de cancelamento no Fabric.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Quando uma aplicação cliente encerra a conexão antes do término da consulta ou o usuário clica em cancelar, o Fabric registra o registro com `status = 'Canceled'` em `queryinsights.exec_requests_history`, permitindo diagnosticar abandono de consultas.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas alegações.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Rastreamento de cancelamento: `status = 'Canceled'` na view `exec_requests_history`.</div>",
    prompt: "Como identificar no Fabric se usuários estão cancelando consultas manualmente no navegador devido à impaciência com lentidão?"
  },
  {
    id: "d3_q25",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Identificação de Spill to Disk no Spark UI",
    question: "Ao analisar um estágio lento de um job Spark no Fabric Spark UI, o engenheiro observa valores significativos nas métricas `Spill (Memory)` e `Spill (Disk)`. O que essas métricas indicam e como resolver?",
    options: [
      {
        id: "A",
        text: "Indicam que a memória alocada para as tarefas do executor foi insuficiente para manter os dados intermediários de shuffle/agregação, forçando o Spark a gravar dados temporários no disco SSD local (gerando alta lentidão de I/O). A solução é aumentar a memória dos nós ou otimizar o particionamento.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Indicam que o disco rígido do cluster está fisicamente quebrado.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Indicam que os arquivos de dados foram excluídos pelo antivírus.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Spill to Disk é uma otimização desejável e acelera as consultas.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O fenômeno de 'Spill' ocorre quando os buffers de execução da JVM excedem a RAM disponível durante operações de Shuffle, Sort ou Join. O Spark descarrega blocos para o disco local (`Spill to Disk`), gerando severa penalidade de I/O. Soluções: aumentar a memória do nó executor, diminuir o tamanho das partições aumentando a contagem de partições, ou eliminar skewed keys.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B e C:</strong> Falsas causas físicas.</li><li><strong>D:</strong> O Spill degrada severamente o desempenho e deve ser eliminado sempre que possível.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Spark Spill to Disk: Falta de RAM forçando gravação em disco durante Shuffle/Sort. Resolva particionando melhor ou aumentando os nós.</div>",
    prompt: "Ao analisar um estágio lento de um job Spark no Fabric Spark UI, o engenheiro observa valores significativos nas métricas `Spill (Memory)` e `Spill (Disk)`. O que essas métricas indicam e como resolver?"
  },
  {
    id: "d3_q26",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Diagnóstico de Garbage Collection (GC) no Spark UI",
    question: "No Spark UI, uma tarefa levou 10 minutos para concluir, e a métrica 'Task Deserialization / GC Time' reportou 7 minutos de tempo de Garbage Collection. Qual é a causa raiz desse comportamento?",
    options: [
      {
        id: "A",
        text: "A criação excessiva de milhões de objetos Python/Java de curta duração na memória heap da JVM, provocando pausas contínuas do Garbage Collector para limpeza de memória.",
        isCorrect: true
      },
      {
        id: "B",
        text: "O cluster Spark estava sem conexão à internet.",
        isCorrect: false
      },
      {
        id: "C",
        text: "O arquivo Parquet estava criptografado com senha errada.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O código Spark estava compilado em linguagem COBOL.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Tempos de Garbage Collection (GC) que ultrapassam 10% do tempo total da tarefa sinalizam pressão extrema na memória heap da JVM, gerada por criação excessiva de objetos em loops Python RDD (em vez de usar DataFrames Spark vetorizados nativos) ou partições grandes demais.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas noções sem base no funcionamento da JVM Spark.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> GC Time elevado no Spark (> 10%): Pressão excessiva no heap da JVM. Use Spark DataFrames vetorizados em vez de loops RDD Python.</div>",
    prompt: "No Spark UI, uma tarefa levou 10 minutos para concluir, e a métrica 'Task Deserialization / GC Time' reportou 7 minutos de tempo de Garbage Collection. Qual é a causa raiz desse comportamento?"
  },
  {
    id: "d3_q27",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Identificação Visual de Data Skew no Spark UI",
    question: "Como um engenheiro de dados identifica graficamente uma assimetria severa de partição (Data Skew) ao inspecionar a aba 'Stages' do Apache Spark UI?",
    options: [
      {
        id: "A",
        text: "Na tabela de distribuição de tarefas (Event Timeline / Summary Metrics), 99 tarefas terminam em 5 segundos (percentil 75% muito baixo), enquanto 1 única tarefa leva 45 minutos (Max Duration desproporcional com Shuffle Read Size gigantesco).",
        isCorrect: true
      },
      {
        id: "B",
        text: "Todas as barras do gráfico ficam vermelhas e o navegador trava.",
        isCorrect: false
      },
      {
        id: "C",
        text: "O Spark UI exibe uma janela pop-up solicitando reinicialização do modem.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Todas as tarefas levam exatamente o mesmo número de milissegundos.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O sintoma clássico de Data Skew no Spark UI é o contraste extremo entre as tarefas de um mesmo estágio: enquanto a grande maioria das tarefas termina em poucos segundos, uma ou poucas tarefas no percentil máximo (`Max`) continuam executando sozinhas por dezenas de minutos com volume desproporcional de bytes lidos no Shuffle.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B e C:</strong> Falsas descrições visuais.</li><li><strong>D:</strong> Se todas as tarefas levassem o mesmo tempo, os dados estariam perfeitamente balanceados (sem skew).</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Identificação de Skew no Spark UI: Discrepância gritante entre a duração das tarefas no percentil 75% vs percentil Max.</div>",
    prompt: "Como um engenheiro de dados identifica graficamente uma assimetria severa de partição (Data Skew) ao inspecionar a aba 'Stages' do Apache Spark UI?"
  },
  {
    id: "d3_q28",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Otimização de Pequenos Arquivos no Spark Ingest",
    question: "Um pipeline de streaming no Spark grava novos micro-lotes a cada 10 segundos no OneLake. Após 3 dias de operação contínua, as consultas analíticas sobre essa tabela ficaram 50 vezes mais lentas. Qual é o motivo dessa degradação e como saná-lo?",
    options: [
      {
        id: "A",
        text: "Problema dos Pequenos Arquivos (Small File Problem): foram gerados mais de 25.000 micro-arquivos Parquet de poucos kilobytes, sobrecarregando as listagens no OneLake. Solução: Executar periodicamente o comando `OPTIMIZE <tabela>` para consolidar os arquivos em blocos de tamanho ideal (~1 GB).",
        isCorrect: true
      },
      {
        id: "B",
        text: "A capacidade F-SKU expirou e precisa ser recarregada com moedas virtuais.",
        isCorrect: false
      },
      {
        id: "C",
        text: "O formato Parquet não é compatível com streaming contínuo.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O OneLake só consegue armazenar até 100 arquivos no total.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A ingestão contínua em streaming gera milhares de pequenos arquivos Parquet fragmentados ('small files'). O overhead de metadados e requisições HTTP GET para abrir cada arquivo destrói o desempenho das consultas. A compactação via `OPTIMIZE` reagrupa os arquivos em tamanhos eficientes (~1 GB).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Incorretos; Parquet e OneLake suportam petabytes, mas a fragmentação em micro-arquivos causa sobrecarga de metadados.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Small File Problem: Ingestão de streaming fragmentada; resolva executando periodicamente `OPTIMIZE` para compactação binária.</div>",
    prompt: "Um pipeline de streaming no Spark grava novos micro-lotes a cada 10 segundos no OneLake. Após 3 dias de operação contínua, as consultas analíticas sobre essa tabela ficaram 50 vezes mais lentas. Qual é o motivo dessa degradação e como saná-lo?"
  },
  {
    id: "d3_q29",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Benefício do Data Skipping em Tabelas Delta",
    question: "Como o mecanismo de Data Skipping do Delta Lake acelera consultas analíticas filtradas por colunas que possuem estatísticas calculadas?",
    options: [
      {
        id: "A",
        text: "Lê os valores mínimos e máximos (`minValues`, `maxValues`) de cada coluna armazenados no cabeçalho do `_delta_log` e ignora completamente a leitura de arquivos Parquet cujos intervalos não contêm os valores solicitados na cláusula WHERE.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Pula a validação de segurança de usuários não autenticados.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Exclui as linhas que não forem lidas durante a consulta.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Desativa a verificação de tipos de dados numéricos.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Delta Lake coleta automaticamente estatísticas das primeiras 32 colunas de cada arquivo (contagem de linhas, nulos, min e max). Ao executar uma consulta com predicado `WHERE Ano = 2024`, o motor consulta o log de metadados e 'pula' (skips) os arquivos onde `maxValues.Ano < 2024` ou `minValues.Ano > 2024`, lendo apenas os arquivos relevantes.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas noções sobre data skipping.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Data Skipping no Delta Lake: Usa estatísticas Min/Max no log para ignorar leitura de arquivos Parquet desnecessários.</div>",
    prompt: "Como o mecanismo de Data Skipping do Delta Lake acelera consultas analíticas filtradas por colunas que possuem estatísticas calculadas?"
  },
  {
    id: "d3_q30",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Limite Padrão de Colunas Indexadas para Estatísticas Delta",
    question: "Por padrão, para quantas colunas de uma tabela Delta o Apache Spark coleta estatísticas automáticas de Min/Max para Data Skipping?",
    options: [
      {
        id: "A",
        text: "Apenas para a primeira coluna.",
        isCorrect: false
      },
      {
        id: "B",
        text: "Para as primeiras 32 colunas (`spark.databricks.delta.properties.defaults.dataSkippingNumIndexedCols = 32`).",
        isCorrect: true
      },
      {
        id: "C",
        text: "Para todas as 1.000 colunas da tabela obrigatoriamente.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O Spark não coleta estatísticas automáticas.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A propriedade `delta.dataSkippingNumIndexedCols` tem o valor padrão de 32 colunas. Se uma coluna usada frequentemente em filtros de consulta estiver na posição 35 de uma tabela larga (wide table), ela não terá estatísticas Min/Max coletadas a menos que essa propriedade seja aumentada ou as colunas sejam reordenadas.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>A, C e D:</strong> Valores e afirmações incorretas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Data Skipping padrão: Primeiras 32 colunas indexadas por padrão (`dataSkippingNumIndexedCols`).</div>",
    prompt: "Por padrão, para quantas colunas de uma tabela Delta o Apache Spark coleta estatísticas automáticas de Min/Max para Data Skipping?"
  },
  {
    id: "d3_q31",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Efeito do Z-Order em Múltiplas Colunas",
    question: "Quando um engenheiro executa o comando `OPTIMIZE Vendas ZORDER BY (ClienteId, DataVenda)`, qual é o efeito nos dados físicos armazenados?",
    options: [
      {
        id: "A",
        text: "Os dados são mapeados usando curvas de preenchimento de espaço multidimensionais (Curva de Peano/Hilbert), garantindo que dados correlacionados por Cliente e Data sejam agrupados fisicamente nos mesmos arquivos Parquet para maximizar o Data Skipping em ambas as colunas.",
        isCorrect: true
      },
      {
        id: "B",
        text: "A tabela é ordenada alfabeticamente apenas pela primeira coluna e a segunda coluna é apagada.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Os dados são compactados em formato `.ZIP` com senha.",
        isCorrect: false
      },
      {
        id: "D",
        text: "A tabela só pode ser consultada por usuários com permissão de Administrador.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A técnica Z-Order (Curva de Z / Espaço-Filling Curve) distribui a ordenação de forma equilibrada entre até 2 a 4 colunas de alta cardinalidade sem dar prioridade linear à primeira coluna (ao contrário da ordenação hierárquica tradicional), permitindo Data Skipping de alta eficiência em consultas filtradas por qualquer combinação dessas colunas.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Afirmações incorretas sem fundamento técnico.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Z-Order: Curva de preenchimento espacial para agrupamento físico multidimensional e máximo Data Skipping.</div>",
    prompt: "Quando um engenheiro executa o comando `OPTIMIZE Vendas ZORDER BY (ClienteId, DataVenda)`, qual é o efeito nos dados físicos armazenados?"
  },
  {
    id: "d3_q32",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Manutenção Automática do Fabric (Automatic Compaction)",
    question: "Qual recurso em segundo plano do Microsoft Fabric realiza compactação de arquivos menores em tabelas Delta de forma automatizada sem a necessidade de agendar comandos manuais de `OPTIMIZE` em todos os workspaces?",
    options: [
      {
        id: "A",
        text: "Auto Compaction (Compactação Automática) durante as gravações e manutenção otimizada de tabelas gerenciada pelo ecossistema Fabric.",
        isCorrect: true
      },
      {
        id: "B",
        text: "O desfragmentador de disco do Windows 95.",
        isCorrect: false
      },
      {
        id: "C",
        text: "Um script em shell executado por um operador físico.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O Fabric não possui nenhum mecanismo automático de compactação.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Fabric inclui recursos nativos de Auto-Compaction e Optimize Write habilitados por padrão no motor Spark e pipelines, consolidando arquivos pequenos durante o processo de escrita e reduzindo a necessidade de intervenções manuais de manutenção.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas noções técnicas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Auto Compaction no Fabric: Consolida automaticamente pequenos arquivos Parquet durante a escrita de dados.</div>",
    prompt: "Qual recurso em segundo plano do Microsoft Fabric realiza compactação de arquivos menores em tabelas Delta de forma automatizada sem a necessidade de agendar comandos manuais de `OPTIMIZE` em todos os workspaces?"
  },
  {
    id: "d3_q33",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Diagnóstico de Fallback no Performance Analyzer e DAX Studio",
    question: "Um desenvolvedor de BI está usando o DAX Studio e a janela do Performance Analyzer para diagnosticar o desempenho de um visual do Power BI conectado a um modelo semântico em modo Direct Lake. Qual indício nos eventos de Server Timings confirma que a consulta permaneceu em Direct Lake puro sem sofrer Fallback para DirectQuery?",
    options: [
      {
        id: "A",
        text: "O evento de consulta do Storage Engine é registrado como `Direct Lake` no motor VertiPaq, sem a emissão de instruções SQL com a tag `DirectQuery` enviadas ao SQL Endpoint.",
        isCorrect: true
      },
      {
        id: "B",
        text: "O relatório exibe um alerta de erro em fonte vermelha.",
        isCorrect: false
      },
      {
        id: "C",
        text: "O visual leva mais de 2 minutos para renderizar.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O Power BI fecha repentinamente sem salvar.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> No DAX Studio (Server Timings), consultas em modo Direct Lake puro são executadas pelo VertiPaq Storage Engine diretamente sobre os arquivos Parquet carregados na memória, rotuladas como `Direct Lake`. Se ocorrer fallback, o DAX Studio exibe uma consulta SQL enviada via `DirectQuery` para o SQL Endpoint do Fabric.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Comportamentos anômalos que não correspondem ao diagnóstico formal de Direct Lake.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Diagnóstico de Direct Lake: No DAX Studio / Server Timings, a consulta deve indicar Storage Engine `Direct Lake` (sem eventos DirectQuery).</div>",
    prompt: "Um desenvolvedor de BI está usando o DAX Studio e a janela do Performance Analyzer para diagnosticar o desempenho de um visual do Power BI conectado a um modelo semântico em modo Direct Lake. Qual indício nos eventos de Server Timings confirma que a consulta permaneceu em Direct Lake puro sem sofrer Fallback para DirectQuery?"
  },
  {
    id: "d3_q34",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Sincronização de Modelo Semântico e Framing no Direct Lake",
    question: "Após a conclusão da ingestão de novos dados em uma tabela Delta pelo Spark, os relatórios em Direct Lake ainda exibem os dados antigos por alguns minutos. Qual processo governa a visibilidade das novas transações no modelo semântico Direct Lake?",
    options: [
      {
        id: "A",
        text: "O processo de Framing e Sincronização de Metadados do Modelo Semântico (que atualiza o ponteiro de versão Delta para a versão mais recente comitada).",
        isCorrect: true
      },
      {
        id: "B",
        text: "O envio de uma cópia dos dados por correio eletrônico.",
        isCorrect: false
      },
      {
        id: "C",
        text: "A reinicialização física dos switches de fibra óptica.",
        isCorrect: false
      },
      {
        id: "D",
        text: "O Direct Lake nunca atualiza dados novos sem excluir o relatório.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> Modelos Semânticos em modo Direct Lake utilizam o conceito de 'Framing' (enquadramento de versão): o modelo se conecta a uma versão específica do Delta Log para manter consistência de leitura durante sessões ativas de usuários. Uma sincronização (Refresh/Sync do modelo) move o quadro para a versão mais recente da tabela Delta.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas declarações sem embasamento na arquitetura do Direct Lake.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Framing no Direct Lake: Mantém a versão Delta consistente e avança para a versão mais recente mediante sincronização (Sync/Refresh).</div>",
    prompt: "Após a conclusão da ingestão de novos dados em uma tabela Delta pelo Spark, os relatórios em Direct Lake ainda exibem os dados antigos por alguns minutos. Qual processo governa a visibilidade das novas transações no modelo semântico Direct Lake?"
  },
  {
    id: "d3_q35",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Comportamento de Fallback por Limite de Memória da Capacidade",
    question: "O que ocorre se o volume total de colunas solicitadas por relatórios Power BI em uma tabela física em modo Direct Lake ultrapassar o limite de memória RAM alocado para o modelo no F-SKU contratado?",
    options: [
      {
        id: "A",
        text: "O modelo realiza Fallback gracioso para DirectQuery para atender às consultas que não couberem na memória, garantindo que o relatório responda aos usuários sem falha fatal.",
        isCorrect: true
      },
      {
        id: "B",
        text: "O locatário inteiro do Fabric é desativado pela Microsoft por 48 horas.",
        isCorrect: false
      },
      {
        id: "C",
        text: "O banco de dados transacional de origem é excluído.",
        isCorrect: false
      },
      {
        id: "D",
        text: "Todas as senhas dos diretores são resetadas.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O mecanismo de Fallback do Direct Lake foi projetado como uma rede de segurança: caso os limites de memória da capacidade sejam excedidos para aquele modelo, o motor direciona as consultas para o modo DirectQuery, consumindo capacidade computacional via SQL Endpoint para não quebrar os visuais dos usuários de negócio.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Consequências falsas e alarmistas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Fallback do Direct Lake: Mecanismo de resiliência que desvia para DirectQuery caso os limites de memória do F-SKU sejam estourados.</div>",
    prompt: "O que ocorre se o volume total de colunas solicitadas por relatórios Power BI em uma tabela física em modo Direct Lake ultrapassar o limite de memória RAM alocado para o modelo no F-SKU contratado?"
  },
  {
    id: "d3_q36",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Configuração da Propriedade `DirectLakeBehavior`",
    question: "Um arquiteto de dados corporativo determinou que os relatórios do Power BI NUNCA devem fazer Fallback silencioso para DirectQuery, pois consultas lentas em DirectQuery podem gerar sobrecarga inesperada de CUs no SQL Endpoint. Qual configuração da propriedade `DirectLakeBehavior` no Modelo Semântico deve ser aplicada?",
    options: [
      {
        id: "A",
        text: "`DirectLakeOnly`",
        isCorrect: true
      },
      {
        id: "B",
        text: "`Automatic`",
        isCorrect: false
      },
      {
        id: "C",
        text: "`DirectQueryOnly`",
        isCorrect: false
      },
      {
        id: "D",
        text: "`Disabled`",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> A propriedade `DirectLakeBehavior` aceita opções como `Automatic` (comportamento padrão: tenta Direct Lake e faz fallback para DirectQuery se necessário) e `DirectLakeOnly` (bloqueia estritamente o fallback; se a consulta não puder ser atendida pelo Direct Lake nativo na memória, retorna erro explícito em vez de degradar para DirectQuery).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> `Automatic` permite o fallback para DirectQuery silenciosamente.</li><li><strong>C:</strong> `DirectQueryOnly` desativa o Direct Lake forçando sempre consultas relacionais T-SQL.</li><li><strong>D:</strong> Incorreto.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Controle de Fallback: Configure `DirectLakeBehavior = DirectLakeOnly` para impedir fallback silencioso para DirectQuery.</div>",
    prompt: "Um arquiteto de dados corporativo determinou que os relatórios do Power BI NUNCA devem fazer Fallback silencioso para DirectQuery, pois consultas lentas em DirectQuery podem gerar sobrecarga inesperada de CUs no SQL Endpoint. Qual configuração da propriedade `DirectLakeBehavior` no Modelo Semântico deve ser aplicada?"
  },
  {
    id: "d3_q37",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Impacto de Tipos de Dados Não Suportados no Direct Lake",
    question: "Qual dos seguintes tipos de dados de coluna em uma tabela Delta pode impedir que a coluna seja lida em modo Direct Lake puro no Power BI, induzindo fallback?",
    options: [
      {
        id: "A",
        text: "Tipos binários arbitrários complexos não estruturados ou tipos com precisão decimal superior a 38 dígitos não suportados pelo Analysis Services.",
        isCorrect: true
      },
      {
        id: "B",
        text: "Colunas do tipo `Integer` (números inteiros de 32 bits).",
        isCorrect: false
      },
      {
        id: "C",
        text: "Colunas do tipo `String` (texto padronizado UTF-8).",
        isCorrect: false
      },
      {
        id: "D",
        text: "Colunas do tipo `Date` (datas no calendário gregoriano).",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> O Analysis Services VertiPaq suporta os tipos analíticos padrão (Integer, BigInt, String, Double, Decimal até 4 casas fixas, DateTime, Boolean). Tipos não convencionais ou tipos binários brutos complexos não mapeáveis diretamente no VertiPaq podem forçar a consulta a fazer fallback para DirectQuery.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Tipos de dados primitivos 100% suportados no Direct Lake com máxima performance.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Compatibilidade Direct Lake: Garanta tipos analíticos padrão (Int, String, DateTime, Decimal) nas tabelas Gold.</div>",
    prompt: "Qual dos seguintes tipos de dados de coluna em uma tabela Delta pode impedir que a coluna seja lida em modo Direct Lake puro no Power BI, induzindo fallback?"
  },
  {
    id: "d3_q38",
    domain: "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)",
    type: "single",
    title: "Medição de Tempo de Inicialização (Cold vs Warm Cache) no VertiPaq",
    question: "Quando um relatório em Direct Lake é acessado pela primeira vez na manhã após uma atualização noturna, o primeiro visual leva 4 segundos para carregar, mas todas as interações seguintes de filtros respondem em menos de 100 milissegundos. Qual é a explicação técnica para essa diferença?",
    options: [
      {
        id: "A",
        text: "O primeiro acesso incorre em 'Cold Cache' (paginação dos arquivos Parquet do OneLake para a memória RAM do Analysis Services). Uma vez na RAM ('Warm Cache'), as interações seguintes acontecem na velocidade nativa do VertiPaq em memória.",
        isCorrect: true
      },
      {
        id: "B",
        text: "O computador do usuário estava esquentando a placa de vídeo.",
        isCorrect: false
      },
      {
        id: "C",
        text: "O Fabric cobra mais caro pelo primeiro clique do dia.",
        isCorrect: false
      },
      {
        id: "D",
        text: "A Microsoft reinicia todos os roteadores mundiais às 08:00 horas.",
        isCorrect: false
      }
    ],
    explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa correta está certa:</strong> No modo Direct Lake, os arquivos Parquet com V-Order residem no OneLake. Na primeira consulta (Cold Cache), as colunas requisitadas são mapeadas e paginadas sob demanda para a memória RAM do serviço (Analysis Services). Consultas subsequentes encontram os blocos já residentes na memória ('Warm Cache'), proporcionando respostas quase instantâneas.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Falsas noções sem fundamentação em engenharia de sistemas analíticos.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Cold Cache vs Warm Cache no Direct Lake: Primeiro carregamento pagina dados do OneLake para a RAM; acessos seguintes operam 100% em memória.</div>",
    prompt: "Quando um relatório em Direct Lake é acessado pela primeira vez na manhã após uma atualização noturna, o primeiro visual leva 4 segundos para carregar, mas todas as interações seguintes de filtros respondem em menos de 100 milissegundos. Qual é a explicação técnica para essa diferença?"
  },
  {
    id: "cs1",
    type: "case_study",
    domain: "Estudo de Caso Corporativo: Contoso Global Retail",
    caseTitle: "Contoso Global Retail: Modernização Analítica com Microsoft Fabric",
    tabs: [
      {
        id: "overview",
        title: "Visão Geral",
        content: "<h4>Perfil da Empresa</h4>\n<p>A Contoso Global Retail é uma grande rede multinacional de varejo com mais de 1.200 lojas físicas e uma plataforma de e-commerce global em rápida expansão.</p>\n<h4>Objetivo de Negócio</h4>\n<p>A diretoria de tecnologia aprovou a migração da arquitetura analítica legada (baseada em SQL Server on-premises e data lakes isolados) para o <strong>Microsoft Fabric</strong> sobre uma capacidade dedicada <strong>F64</strong>.</p>"
      },
      {
        id: "existing_env",
        title: "Ambiente Atual",
        content: "<h4>Infraestrutura e Origens</h4>\n<ul>\n<li><strong>ERP Operacional:</strong> Banco de dados relacional transacional (OLTP) em Azure SQL Database com 4 TB de dados de pedidos e clientes.</li>\n<li><strong>Histórico de Vendas Externo:</strong> 25 TB de dados em formato Parquet armazenados em um bucket do <strong>Amazon S3 (Região us-east-1)</strong>.</li>\n<li><strong>Workspaces Fabric:</strong> Um workspace de produção denominado <code>WS_Prod_Contoso</code> atribuído à capacidade F64.</li>\n<li><strong>Segurança:</strong> O acesso dos analistas deve respeitar políticas estritas de isolamento por filial regional.</li>\n</ul>"
      },
      {
        id: "data_req",
        title: "Requisitos de Dados",
        content: "<h4>Padrão de Ingestão e Processamento</h4>\n<ul>\n<li>Os dados do ERP Azure SQL devem ser sincronizados continuamente para o OneLake sem que nenhuma consulta pesada de extração degrade a performance do banco operacional.</li>\n<li>Os dados do bucket Amazon S3 precisam ser acessados imediatamente pelos notebooks de ciência de dados sem incorrer em custos de egress de duplicação física.</li>\n<li>A tabela de clientes deve manter o histórico completo de mudanças de endereço e categoria (SCD Tipo 2).</li>\n</ul>"
      },
      {
        id: "tech_req",
        title: "Requisitos Técnicos",
        content: "<h4>Restrições Mandatórias da Segurança e Governança</h4>\n<ul>\n<li><strong>Minimizar Esforço de Desenvolvimento:</strong> Sempre priorizar recursos nativos do Fabric gerenciados pela Microsoft.</li>\n<li><strong>Segurança a Nível de Linha (RLS):</strong> Gerentes regionais só podem visualizar vendas correspondentes à sua região geográfica (coluna <code>RegionCode</code>).</li>\n<li><strong>Relatórios Power BI:</strong> Os relatórios executivos devem utilizar o modo <strong>Direct Lake</strong> para evitar tempos de atualização agendada às 06:00.</li>\n<li><strong>Importante:</strong> Se uma regra de RLS for aplicada diretamente na tabela Delta do Lakehouse, o Power BI Direct Lake pode sofrer fallback para DirectQuery. A equipe exige que o relatório mantenha a performance em memória do Direct Lake.</li>\n</ul>"
      }
    ],
    questions: [
      {
        id: "cs1_q1",
        type: "single",
        prompt: "Com base nas seções 'Ambiente Atual' e 'Requisitos de Dados', qual tecnologia do Microsoft Fabric você deve implementar para sincronizar continuamente as tabelas do ERP Azure SQL Database para o OneLake com o menor esforço de desenvolvimento e sem degradar a performance operacional?",
        options: [
          {
            id: "A",
            text: "Configurar Fabric Database Mirroring para o Azure SQL Database.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Criar um pipeline no Data Factory agendado a cada 10 minutos.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Exportar scripts BCP diariamente usando máquinas virtuais Azure.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Utilizar Dataflow Gen2 com carga incremental via Power Query M.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> O <strong>Database Mirroring</strong> no Fabric é a solução nativa zero-ETL da Microsoft que lê os logs de transação do Azure SQL Database via Change Data Capture (CDC) e replica continuamente para tabelas Delta no OneLake sem impacto nas transações operacionais.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B e D:</strong> Pipelines e Dataflows exigem desenvolvimento manual e geram consultas pesadas que causam locks no banco operacional.</li>\n<li><strong>C:</strong> Scripts BCP manuais não são gerenciados e exigem infraestrutura externa.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Para replicação zero-ETL quase em tempo real de Azure SQL Database, Snowflake ou Cosmos DB para o OneLake, a resposta oficial é <strong>Database Mirroring</strong>.</div>",
        question: "Com base nas seções 'Ambiente Atual' e 'Requisitos de Dados', qual tecnologia do Microsoft Fabric você deve implementar para sincronizar continuamente as tabelas do ERP Azure SQL Database para o OneLake com o menor esforço de desenvolvimento e sem degradar a performance operacional?",
        title: "Com base nas seções 'Ambiente Atual' e 'Requisitos de Dados'..."
      },
      {
        id: "cs1_q2",
        type: "single",
        prompt: "Com base nas seções 'Requisitos de Dados' e 'Requisitos Técnicos', como os dados de 25 TB armazenados no bucket Amazon S3 devem ser disponibilizados no Lakehouse do workspace WS_Prod_Contoso?",
        options: [
          {
            id: "A",
            text: "Criar um OneLake Shortcut apontando para o bucket do Amazon S3.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Executar uma atividade Copy Data no Data Factory para duplicar os arquivos.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Baixar os arquivos via FTP e fazer upload manual no Lakehouse Files.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Criar um cluster Databricks dedicado fora da capacidade do Fabric.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> Os <strong>OneLake Shortcuts</strong> para Amazon S3 atendem perfeitamente aos requisitos de eliminar a duplicação física e evitar custos de transferência e esforço de desenvolvimento, expondo os dados instantaneamente no Lakehouse.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Duplicar 25 TB via Copy Data gera custo de egress na AWS e duplica custos de armazenamento.</li>\n<li><strong>C e D:</strong> São soluções frágeis ou externas que contrariam o uso do Microsoft Fabric.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Shortcuts para o Amazon S3 suportam tanto IAM Roles quanto Chaves de Acesso (Access Key / Secret Key).</div>",
        question: "Com base nas seções 'Requisitos de Dados' e 'Requisitos Técnicos', como os dados de 25 TB armazenados no bucket Amazon S3 devem ser disponibilizados no Lakehouse do workspace WS_Prod_Contoso?",
        title: "Com base nas seções 'Requisitos de Dados' e 'Requisitos Técn..."
      },
      {
        id: "cs1_q3",
        type: "multi",
        prompt: "Considere as restrições da seção 'Requisitos Técnicos' relativas ao Power BI Direct Lake e Segurança a Nível de Linha (RLS). Quais DUAS ações a equipe de arquitetura deve adotar para garantir a governança de acesso regional sem forçar o fallback do Direct Lake para o modo DirectQuery? (Escolha duas alternativas).",
        options: [
          {
            id: "A",
            text: "Implementar as regras de RLS dentro do Modelo Semântico do Power BI.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Garantir que a identidade do relatório acesse o Lakehouse via permissão Read.",
            isCorrect: true
          },
          {
            id: "C",
            text: "Aplicar RLS nativo no SQL Analytics Endpoint do Lakehouse.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Configurar o modelo do Power BI para o modo de Importação diária.",
            isCorrect: false
          },
          {
            id: "E",
            text: "Desabilitar a criptografia de dados em repouso no Azure Storage.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que as alternativas A e B estão corretas:</strong> Para que o Power BI opere em modo Direct Lake puro com RLS sem sofrer Fallback para DirectQuery, as funções de Row-Level Security devem ser definidas <em>dentro do próprio Modelo Semântico do Power BI</em> (Semantic Model RLS), e a identidade do modelo precisa de permissão de leitura (Read) sobre o Lakehouse de origem.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C:</strong> Aplicar RLS no SQL Endpoint é exatamente o que força o fallback silencioso para DirectQuery!</li>\n<li><strong>D:</strong> O modo Importação viola o requisito explícito de usar Direct Lake sem atualização agendada.</li>\n<li><strong>E:</strong> Desabilitar criptografia viola segurança corporativa e não afeta o modo de consulta.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> RLS no SQL Endpoint = DirectQuery Fallback. RLS no Semantic Model = Direct Lake Puro preservado.</div>",
        question: "Considere as restrições da seção 'Requisitos Técnicos' relativas ao Power BI Direct Lake e Segurança a Nível de Linha (RLS). Quais DUAS ações a equipe de arquitetura deve adotar para garantir a governança de acesso regional sem forçar o fallback do Direct Lake para o modo DirectQuery? (Escolha duas alternativas).",
        title: "Considere as restrições da seção 'Requisitos Técnicos' relat..."
      }
    ]
  },
  {
    id: "cs2",
    type: "case_study",
    domain: "Estudo de Caso Corporativo: Litware Smart IoT Energy Grid",
    caseTitle: "Litware Inc.: Plataforma de Telemetria e Streaming em Tempo Real com Eventhouse",
    tabs: [
      {
        id: "overview",
        title: "Visão Geral",
        content: "<h4>Perfil da Empresa</h4>\n<p>A Litware Inc. opera uma rede inteligente de distribuição elétrica (Smart Grid) cobrindo mais de 500.000 medidores inteligentes conectados em áreas metropolitanas.</p>\n<h4>Objetivo do Projeto</h4>\n<p>Implantar uma arquitetura de telemetria analítica no <strong>Microsoft Fabric</strong> sobre uma capacidade <strong>F128</strong> capaz de processar 50.000 eventos por segundo com latência de subsegundo para alertas de emergência e persistência histórica fria de 5 anos no OneLake.</p>"
      },
      {
        id: "existing_env",
        title: "Ambiente Atual",
        content: "<h4>Infraestrutura e Origens</h4>\n<ul>\n<li><strong>Ingestão de Streaming:</strong> Clusters de Azure Event Hubs recebem fluxos massivos de telemetria em formato JSON com campos <code>MeterId</code>, <code>TimestampUtc</code>, <code>Voltage</code>, <code>CurrentAmp</code> e <code>ErrorCode</code>.</li>\n<li><strong>Capacidade Fabric:</strong> Capacidade dedicada F128 associada aos workspaces <code>WS_IoT_RealTime</code> e <code>WS_IoT_Analytics</code>.</li>\n<li><strong>Workload Híbrido:</strong> O centro de controle exige visualização em telas de tempo real (latência < 2s), enquanto a equipe de ciência de dados treina modelos em batch no Spark Lakehouse.</li>\n</ul>"
      },
      {
        id: "data_req",
        title: "Requisitos de Dados",
        content: "<h4>Processamento e Transformação Contínua</h4>\n<ul>\n<li>A tabela de telemetria bruta (<code>RawTelemetry</code>) deve ser agregada a cada janela de 5 minutos, gravando médias e picos de voltagem por medidor na tabela <code>AggregatedMetrics</code> de forma transacional e síncrona na chegada dos dados.</li>\n<li>Todos os dados brutos de streaming devem ser roteados e persistidos em formato Delta Parquet na camada Bronze do Lakehouse para conformidade regulatória de 5 anos com custo reduzido.</li>\n</ul>"
      },
      {
        id: "tech_req",
        title: "Requisitos Técnicos",
        content: "<h4>Mecanismos de Consulta e Governança</h4>\n<ul>\n<li><strong>Consultas Ultra-Rápidas:</strong> As buscas por códigos de falha em strings de log devem responder em milissegundos utilizando o motor de indexação invertida do KQL.</li>\n<li><strong>Último Estado do Medidor:</strong> Os operadores precisam obter instantaneamente a leitura mais recente de cada medidor sem realizar varreduras completas de tabelas históricas.</li>\n<li><strong>Zero Código para Roteamento:</strong> Priorizar componentes visuais do Fabric para direcionar o stream do Event Hub simultaneamente para o Eventhouse e para o Lakehouse.</li>\n</ul>"
      }
    ],
    questions: [
      {
        id: "cs2_q1",
        type: "single",
        prompt: "Com base nas seções 'Visão Geral' e 'Requisitos de Dados', qual recurso nativo do KQL no Eventhouse deve ser configurado para transformar e agregar as mensagens em janelas de 5 minutos na tabela AggregatedMetrics no momento exato em que os dados são ingeridos na tabela RawTelemetry?",
        options: [
          {
            id: "A",
            text: "Uma Update Policy vinculada a uma função KQL de agregação.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Um pipeline do Data Factory com gatilho de agendamento a cada 5 minutos.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Uma exibição normal criada com instrução CREATE VIEW em T-SQL.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Um notebook PySpark executado manualmente pelo operador de plantão.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> As <strong>Update Policies</strong> no KQL (Eventhouse) são o mecanismo transacional nativo para processar dados de streaming na ingestão, permitindo filtrar, transformar e agregar registros síncrona ou assincronamente direto para uma tabela destino sem pipelines externos.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Agendar pipelines a cada 5 minutos introduz atraso e sobrecarga de computação desnecessária.</li>\n<li><strong>C e D:</strong> Views e execuções manuais não persistem dados agregados de forma contínua e em tempo real.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Update Policies no Eventhouse são atômicas: a transformação ocorre durante o processo de append no stream.</div>",
        question: "Com base nas seções 'Visão Geral' e 'Requisitos de Dados', qual recurso nativo do KQL no Eventhouse deve ser configurado para transformar e agregar as mensagens em janelas de 5 minutos na tabela AggregatedMetrics no momento exato em que os dados são ingeridos na tabela RawTelemetry?",
        title: "Com base nas seções 'Visão Geral' e 'Requisitos de Dados', q..."
      },
      {
        id: "cs2_q2",
        type: "single",
        prompt: "Com base na seção 'Requisitos Técnicos', qual componente do Microsoft Fabric você deve utilizar para ingerir o fluxo do Azure Event Hubs e roteá-lo simultaneamente para o Eventhouse (para análise em tempo real) e para o Lakehouse (em Delta Parquet para histórico de 5 anos) com configuração visual e sem escrever código?",
        options: [
          {
            id: "A",
            text: "Configurar um Fabric Eventstream com múltiplos destinos gerenciados.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Criar scripts Python em máquinas virtuais fora da nuvem da Microsoft.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Executar o utilitário AzCopy via prompt de comando uma vez por semana.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Exportar arquivos CSV do Event Hub manualmente via portal do Azure.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> O <strong>Fabric Eventstream</strong> é o serviço nativo sem código para captura, transformação e roteamento de fluxos de eventos em tempo real para múltiplos destinos do Fabric, incluindo Eventhouse (KQL Database) e Lakehouse (tabelas Delta).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> São soluções manuais ou externas que violam a premissa de usar ferramentas SaaS gerenciadas do Microsoft Fabric.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> O Eventstream suporta múltiplos destinos e transformações visuais inline (Filter, Aggregate, Expand JSON).</div>",
        question: "Com base na seção 'Requisitos Técnicos', qual componente do Microsoft Fabric você deve utilizar para ingerir o fluxo do Azure Event Hubs e roteá-lo simultaneamente para o Eventhouse (para análise em tempo real) e para o Lakehouse (em Delta Parquet para histórico de 5 anos) com configuração visual e sem escrever código?",
        title: "Com base na seção 'Requisitos Técnicos', qual componente do ..."
      },
      {
        id: "cs2_q3",
        type: "multi",
        prompt: "Considere a necessidade de consultar os logs de telemetria com alta performance no Eventhouse e identificar o último estado reportado de cada medidor conforme os 'Requisitos Técnicos'. Quais DUAS instruções ou operadores KQL atendem a essas demandas com máxima eficiência? (Escolha duas alternativas).",
        options: [
          {
            id: "A",
            text: "Utilizar o operador 'has' para buscas otimizadas de strings indexadas.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Utilizar a função 'arg_max(TimestampUtc, *)' agrupada por MeterId.",
            isCorrect: true
          },
          {
            id: "C",
            text: "Utilizar o operador 'contains' que força varredura completa caractere a caractere.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Executar o comando VACUUM com retenção zero para acelerar a leitura.",
            isCorrect: false
          },
          {
            id: "E",
            text: "Converter a tabela KQL para uma pasta de arquivos texto descompactados.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que as alternativas A e B estão corretas:</strong> No KQL, o operador <code>has</code> utiliza o índice invertido de termos com velocidade centenas de vezes superior ao <code>contains</code> (que faz regex scan linha a linha). Para obter a linha mais recente de cada entidade, a função de agregação <code>arg_max(Timestamp, *)</code> é a forma canônica e de mais alta performance.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C:</strong> O operador <code>contains</code> ignora o índice de termos e realiza varredura exaustiva lenta.</li>\n<li><strong>D e E:</strong> O comando VACUUM e arquivos texto são inadequados para motores KQL de alta velocidade.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Prefira sempre <code>has</code> a <code>contains</code> quando buscar palavras inteiras ou termos indexados em KQL.</div>",
        question: "Considere a necessidade de consultar os logs de telemetria com alta performance no Eventhouse e identificar o último estado reportado de cada medidor conforme os 'Requisitos Técnicos'. Quais DUAS instruções ou operadores KQL atendem a essas demandas com máxima eficiência? (Escolha duas alternativas).",
        title: "Considere a necessidade de consultar os logs de telemetria c..."
      }
    ]
  },
  {
    id: "cs3",
    type: "case_study",
    domain: "Estudo de Caso Corporativo: Fabrikam Financial Services",
    caseTitle: "Fabrikam Wealth: Governança, Segurança Granular e CI/CD no Fabric Data Warehouse",
    tabs: [
      {
        id: "overview",
        title: "Visão Geral",
        content: "<h4>Perfil da Empresa</h4>\n<p>A Fabrikam Financial Services gerencia carteiras de investimentos e patrimônio para mais de 100.000 clientes de alta renda em múltiplos países.</p>\n<h4>Desafio de Governança</h4>\n<p>A instituição precisa consolidar seu repositório analítico corporativo em um <strong>Fabric Data Warehouse</strong> garantindo conformidade rigorosa com normas de proteção de dados bancários (PCI-DSS e LGPD/GDPR), com controle total de versionamento via CI/CD.</p>"
      },
      {
        id: "existing_env",
        title: "Ambiente Atual",
        content: "<h4>Workspaces e Estrutura</h4>\n<ul>\n<li><strong>Workspaces Separados:</strong> Três workspaces distintos no Fabric: <code>WS_Finance_Dev</code>, <code>WS_Finance_Test</code> e <code>WS_Finance_Prod</code>.</li>\n<li><strong>Data Warehouse Central:</strong> Tabela <code>FactTransactions</code> com 2 bilhões de linhas e tabela dimensional <code>DimAccount</code> contendo números de cartões de crédito e saldo financeiro.</li>\n<li><strong>Repositório Git:</strong> Projeto no Azure DevOps para versionamento de código e pipelines de integração contínua.</li>\n</ul>"
      },
      {
        id: "data_req",
        title: "Requisitos de Dados",
        content: "<h4>Privacidade e Mascaramento</h4>\n<ul>\n<li>Analistas de suporte júnior não podem visualizar o número completo do cartão de crédito (coluna <code>CreditCardNumber</code>), devendo visualizar apenas os últimos 4 dígitos mascarados no formato <code>XXXX-XXXX-XXXX-1234</code>.</li>\n<li>Auditores de conformidade autorizados devem ter permissão explícita para visualizar os dados reais desmascarados.</li>\n<li>Gerentes de agência regional só podem visualizar contas vinculadas à sua respectiva agência através de Row-Level Security (RLS).</li>\n</ul>"
      },
      {
        id: "tech_req",
        title: "Requisitos Técnicos",
        content: "<h4>Automação de CI/CD e Implantação</h4>\n<ul>\n<li>O esquema do Data Warehouse (tabelas, views e procedures) deve ser versionado como código declarativo em um projeto de banco de dados compilado.</li>\n<li>A promoção de relatórios e pipelines entre DEV, TEST e PROD deve ser realizada através de <strong>Deployment Pipelines</strong>.</li>\n<li>Ao implantar em PROD, a cadeia de conexão dos pipelines deve ser remapeada automaticamente para o banco de dados produtivo sem intervenção humana no código.</li>\n</ul>"
      }
    ],
    questions: [
      {
        id: "cs3_q1",
        type: "single",
        prompt: "Com base nas seções 'Visão Geral' e 'Requisitos de Dados', qual recurso de segurança do T-SQL no Fabric Data Warehouse deve ser aplicado na coluna CreditCardNumber para exibir apenas os últimos 4 dígitos aos analistas de suporte, permitindo que auditores autorizados visualizem o número original?",
        options: [
          {
            id: "A",
            text: "Dynamic Data Masking utilizando a função partial: partial(0, 'XXXX-XXXX-XXXX-', 4).",
            isCorrect: true
          },
          {
            id: "B",
            text: "Criptografar permanentemente o disco físico apagando as chaves de acesso.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Excluir fisicamente a coluna CreditCardNumber de todas as tabelas analíticas.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Substituir a tabela por um arquivo JSON público armazenado na pasta Files.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> O <strong>Dynamic Data Masking (DDM)</strong> no Fabric Data Warehouse permite ofuscar dados sensíveis em tempo de consulta sem alterar os dados gravados no disco, usando funções como <code>partial(prefix, padding, suffix)</code>. Usuários com permissão <code>UNMASK</code> visualizam os dados originais.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Destruir dados ou expor arquivos publicamente viola as diretrizes de governança bancária.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> DDM ofusca dados em tempo de leitura. Para conceder acesso a auditores, execute: <code>GRANT UNMASK TO [Auditor]</code>.</div>",
        question: "Com base nas seções 'Visão Geral' e 'Requisitos de Dados', qual recurso de segurança do T-SQL no Fabric Data Warehouse deve ser aplicado na coluna CreditCardNumber para exibir apenas os últimos 4 dígitos aos analistas de suporte, permitindo que auditores autorizados visualizem o número original?",
        title: "Com base nas seções 'Visão Geral' e 'Requisitos de Dados', q..."
      },
      {
        id: "cs3_q2",
        type: "single",
        prompt: "Com base na seção 'Requisitos Técnicos', qual abordagem é a recomendada oficialmente pela Microsoft para gerenciar o esquema DDL do Fabric Data Warehouse com versionamento no Git e compilação automatizada no Azure DevOps?",
        options: [
          {
            id: "A",
            text: "Utilizar SQL Database Projects (.sqlproj) e implantação via pacote DACPAC.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Executar cópias manuais de tabelas através do menu do navegador todo domingo.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Armazenar scripts T-SQL não testados diretamente no bloco de notas da máquina local.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Desabilitar o controle de versão e permitir edições concorrentes em produção.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> <strong>SQL Database Projects (.sqlproj)</strong> fornecem suporte declarativo completo para esquemas de banco de dados, possibilitando validação de sintaxe, controle de branches no Git e compilação em pacotes DACPAC para automação via pipelines do Azure DevOps.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Processos manuais sem versionamento ferem as diretrizes de CI/CD corporativas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Projetos .sqlproj compilam esquemas em arquivos .dacpac, suportando Schema Compare e DacDeploy.</div>",
        question: "Com base na seção 'Requisitos Técnicos', qual abordagem é a recomendada oficialmente pela Microsoft para gerenciar o esquema DDL do Fabric Data Warehouse com versionamento no Git e compilação automatizada no Azure DevOps?",
        title: "Com base na seção 'Requisitos Técnicos', qual abordagem é a ..."
      },
      {
        id: "cs3_q3",
        type: "multi",
        prompt: "Considere a exigência de promover artefatos do estágio WS_Finance_Test para WS_Finance_Prod via Deployment Pipelines conforme a seção 'Requisitos Técnicos'. Quais DUAS configurações de Deployment Rules garantem que conexões de dados e variáveis de ambiente sejam atualizadas automaticamente para o ambiente produtivo? (Escolha duas alternativas).",
        options: [
          {
            id: "A",
            text: "Configurar Data Source Rules no pipeline para remapear servidores de banco.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Configurar Parameter Rules no pipeline para atualizar variáveis de ambiente.",
            isCorrect: true
          },
          {
            id: "C",
            text: "Editar manualmente os arquivos JSON de metadados diretamente no branch main.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Executar o comando VACUUM com retenção zero em todas as tabelas do workspace.",
            isCorrect: false
          },
          {
            id: "E",
            text: "Desativar o protocolo de segurança TLS em todas as conexões de rede.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que as alternativas A e B estão corretas:</strong> As <strong>Deployment Rules</strong> em Deployment Pipelines do Fabric incluem <strong>Data Source Rules</strong> (para alterar instâncias de banco de dados ou workspaces alvo) e <strong>Parameter Rules</strong> (para atualizar valores de parâmetros de relatórios e pipelines como 'PROD' sem editar o código).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C, D e E:</strong> Editar JSON manualmente, executar VACUUM zero ou desativar TLS violam as boas práticas de DevOps e segurança.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> As regras de implantação são sempre configuradas no estágio de destino (Target Stage).</div>",
        question: "Considere a exigência de promover artefatos do estágio WS_Finance_Test para WS_Finance_Prod via Deployment Pipelines conforme a seção 'Requisitos Técnicos'. Quais DUAS configurações de Deployment Rules garantem que conexões de dados e variáveis de ambiente sejam atualizadas automaticamente para o ambiente produtivo? (Escolha duas alternativas).",
        title: "Considere a exigência de promover artefatos do estágio WS_Fi..."
      }
    ]
  },
  {
    id: "cs4",
    type: "case_study",
    domain: "Estudo de Caso Corporativo: Woodgrove Bank & Insurance",
    caseTitle: "Woodgrove Financial: Arquitetura Medalhão, Liquid Clustering e Otimização de Capacidade",
    tabs: [
      {
        id: "overview",
        title: "Visão Geral",
        content: "<h4>Perfil da Organização</h4>\n<p>O Woodgrove Bank & Insurance é um conglomerado financeiro com operações de varejo bancário, seguros de automóveis e fundos de previdência.</p>\n<h4>Desafio de Modernização</h4>\n<p>A instituição está migrando seu Data Lake corporativo de 200 TB para o <strong>Microsoft Fabric</strong> em uma capacidade dedicada <strong>F128</strong>, com objetivo de reduzir custos de computação, eliminar o problema de small files e fornecer dashboards executivos de subsegundo.</p>"
      },
      {
        id: "existing_env",
        title: "Ambiente Atual",
        content: "<h4>Infraestrutura e Origens</h4>\n<ul>\n<li><strong>Data Lakes Existentes:</strong> Contas ADLS Gen2 em múltiplas regiões do Azure contendo arquivos Parquet brutos ingeridos diariamente.</li>\n<li><strong>Capacidade Fabric:</strong> F128 atribuída aos workspaces <code>WS_Woodgrove_Bronze</code>, <code>WS_Woodgrove_Silver</code> e <code>WS_Woodgrove_Gold</code>.</li>\n<li><strong>Volume da Tabela Principal:</strong> A tabela de apólices e sinistros (<code>FactClaims</code>) possui mais de 8 bilhões de linhas com alta dispersão de consultas por <code>DataSinistro</code> e <code>TipoSeguro</code>.</li>\n</ul>"
      },
      {
        id: "data_req",
        title: "Requisitos de Dados",
        content: "<h4>Processamento na Arquitetura Medalhão</h4>\n<ul>\n<li><strong>Camada Bronze:</strong> Ingestão append-only dos dados brutos através de OneLake Shortcuts para o ADLS Gen2 externo sem replicação física de arquivos.</li>\n<li><strong>Camada Silver:</strong> Limpeza, tipagem e deduplicação utilizando PySpark com gravação Delta Lake e ordenação V-Order ativada por padrão.</li>\n<li><strong>Camada Gold:</strong> Modelagem Star Schema com a tabela <code>FactClaims</code> clusterizada para permitir que consultas analíticas realizem data skipping de mais de 95% dos arquivos.</li>\n</ul>"
      },
      {
        id: "tech_req",
        title: "Requisitos Técnicos",
        content: "<h4>Prevenção de Throttling e Performance</h4>\n<ul>\n<li><strong>Controle de CUs:</strong> Durante as cargas noturnas pesadas, a utilização de computação ultrapassa 150% da capacidade F128. O sistema deve amortizar o consumo sem rejeitar consultas interativas de operadores de plantão.</li>\n<li><strong>Eliminação de Small Files:</strong> A tabela FactClaims não deve utilizar particionamento físico por data que gere milhares de diretórios vazios.</li>\n<li><strong>Governança de Exclusão:</strong> Operações de conformidade LGPD que excluem sinistros a pedido do cliente devem permitir auditoria de Time Travel por 14 dias antes do expurgo físico definitivo.</li>\n</ul>"
      }
    ],
    questions: [
      {
        id: "cs4_q1",
        type: "single",
        prompt: "Com base na seção 'Requisitos de Dados', qual técnica de otimização do Delta Lake 3.0 você deve aplicar na tabela FactClaims na camada Gold para maximizar o Data Skipping e evitar o problema de particionamento excessivo em diretórios físicos?",
        options: [
          {
            id: "A",
            text: "Liquid Clustering com a sintaxe CLUSTER BY (DataSinistro, TipoSeguro).",
            isCorrect: true
          },
          {
            id: "B",
            text: "Particionamento físico em diretórios por ano, mês, dia e hora.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Conversão da tabela para formato CSV sem indexação.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Desativação dos metadados de estatísticas Min/Max no _delta_log.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> O <strong>Liquid Clustering</strong> (ativado com <code>CLUSTER BY</code>) é a solução oficial da Microsoft para tabelas multibilionárias no Fabric. Ele organiza dados em múltiplos eixos sem criar diretórios físicos no OneLake, eliminando o problema de arquivos pequenos e maximizando o <em>Data Skipping</em> através dos metadados Min/Max do <code>_delta_log</code>.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Particionar fisicamente por hora cria dezenas de milhares de arquivos minúsculos que degradam o desempenho.</li>\n<li><strong>C e D:</strong> Formato CSV e desativação de estatísticas anulam o poder do motor analítico.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> O Liquid Clustering substitui o particionamento Hive clássico e permite executar re-clusterização incremental via <code>OPTIMIZE table</code>.</div>",
        question: "Com base na seção 'Requisitos de Dados', qual técnica de otimização do Delta Lake 3.0 você deve aplicar na tabela FactClaims na camada Gold para maximizar o Data Skipping e evitar o problema de particionamento excessivo em diretórios físicos?",
        title: "Com base na seção 'Requisitos de Dados', qual técnica de oti..."
      },
      {
        id: "cs4_q2",
        type: "single",
        prompt: "Com base na seção 'Requisitos Técnicos', como o mecanismo de Smoothing do Microsoft Fabric trata a carga pesada de 150% de CUs gerada pelos pipelines noturnos de background na capacidade F128?",
        options: [
          {
            id: "A",
            text: "Amortiza o pico de consumo de background em uma janela móvel de 24 horas.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Cancela sumariamente todos os pipelines quando a utilização atinge 101%.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Gera cobrança imediata de multas na fatura de cartão de crédito do Azure.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Pausa a capacidade automaticamente exigindo reinício manual do servidor.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> No Fabric, jobs de background (como pipelines do Data Factory e rotinas Spark) têm seu consumo médio distribuído ao longo de uma <strong>janela de 24 horas</strong>. Graças ao <em>Bursting</em> e <em>Smoothing</em>, um pico noturno de 150% não causa throttling imediato caso a capacidade média das últimas 24h permaneça dentro de 100%.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> O Fabric não cancela jobs arbitrariamente, não aplica multas e não desliga a capacidade por picos normais de processamento.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Background Smoothing = 24 horas. Interactive Smoothing = 5 minutos.</div>",
        question: "Com base na seção 'Requisitos Técnicos', como o mecanismo de Smoothing do Microsoft Fabric trata a carga pesada de 150% de CUs gerada pelos pipelines noturnos de background na capacidade F128?",
        title: "Com base na seção 'Requisitos Técnicos', como o mecanismo de..."
      },
      {
        id: "cs4_q3",
        type: "single",
        prompt: "Com base na exigência de conformidade LGPD da seção 'Requisitos Técnicos', qual comando de manutenção do Delta Lake deve ser agendado com o parâmetro de retenção de 14 dias (336 horas) para expurgar fisicamente os arquivos tombstoned obsoletos após o período de auditoria?",
        options: [
          {
            id: "A",
            text: "VACUUM FactClaims RETAIN 336 HOURS;",
            isCorrect: true
          },
          {
            id: "B",
            text: "DROP TABLE FactClaims WITH PURGE;",
            isCorrect: false
          },
          {
            id: "C",
            text: "DELETE FROM FactClaims WHERE 1=1;",
            isCorrect: false
          },
          {
            id: "D",
            text: "OPTIMIZE FactClaims ZORDER BY (ClaimId);",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> O comando <code>VACUUM FactClaims RETAIN 336 HOURS</code> (14 dias * 24 horas = 336 horas) remove fisicamente os arquivos Parquet que foram marcados como obsoletos (tombstoned) por operações de exclusão ou atualização há mais de 14 dias, liberando espaço em disco e garantindo que o Time Travel permaneça acessível exatamente durante a janela de auditoria requerida.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B e C:</strong> <code>DROP TABLE</code> ou <code>DELETE FROM 1=1</code> destroem a tabela inteira e seus registros ativos.</li>\n<li><strong>D:</strong> <code>OPTIMIZE</code> compacta arquivos, mas não remove arquivos tombstoned antigos.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> O período padrão de retenção do VACUUM é de 168 horas (7 dias). Para reter por 14 dias, use explicitamente <code>RETAIN 336 HOURS</code>.</div>",
        question: "Com base na exigência de conformidade LGPD da seção 'Requisitos Técnicos', qual comando de manutenção do Delta Lake deve ser agendado com o parâmetro de retenção de 14 dias (336 horas) para expurgar fisicamente os arquivos tombstoned obsoletos após o período de auditoria?",
        title: "Com base na exigência de conformidade LGPD da seção 'Requisi..."
      }
    ]
  },
  {
    id: "cs5",
    type: "case_study",
    domain: "Estudo de Caso Corporativo: AdventureWorks E-Commerce & Logística",
    caseTitle: "AdventureWorks: Ingestão de Alta Concorrência, Watermarking e Cargas SCD Tipo 2",
    tabs: [
      {
        id: "overview",
        title: "Visão Geral",
        content: "<h4>Perfil da Empresa</h4>\n<p>A AdventureWorks é uma fabricante e distribuidora global de bicicletas e equipamentos esportivos com vendas diretas ao consumidor (B2C) e atacado (B2B).</p>\n<h4>Desafio do Projeto</h4>\n<p>A empresa precisa substituir seus fluxos de integração SSIS legados por uma arquitetura moderna no <strong>Microsoft Fabric Data Factory</strong> e <strong>Notebooks Spark</strong> para processar 30 milhões de transações diárias distribuídas em 120 tabelas relacionais.</p>"
      },
      {
        id: "existing_env",
        title: "Ambiente Atual",
        content: "<h4>Fontes de Dados</h4>\n<ul>\n<li><strong>Bancos Operacionais:</strong> Múltiplas instâncias de Azure SQL Database e PostgreSQL on-premises conectadas via On-premises Data Gateway.</li>\n<li><strong>Destino:</strong> Workspace de Produção no Fabric associado a uma capacidade F64.</li>\n<li><strong>Tabelas Críticas:</strong> Tabelas de <code>Clientes</code>, <code>Pedidos</code> e <code>RastreamentoLogistico</code>.</li>\n</ul>"
      },
      {
        id: "data_req",
        title: "Requisitos de Dados",
        content: "<h4>Carga Incremental e Idempotência</h4>\n<ul>\n<li>A ingestão das 120 tabelas deve ocorrer em paralelo com no máximo 25 execuções simultâneas para não derrubar os pools de conexão dos bancos operacionais.</li>\n<li>Apenas dados alterados desde a última carga bem-sucedida devem ser extraídos utilizando uma tabela de controle de Watermark em UTC.</li>\n<li>A dimensão de clientes deve registrar mudanças de endereço mantendo a versão antiga com data de encerramento e inserindo a nova versão com data de vigência aberta (SCD Tipo 2).</li>\n</ul>"
      },
      {
        id: "tech_req",
        title: "Requisitos Técnicos",
        content: "<h4>Resiliência e Tolerância a Falhas</h4>\n<ul>\n<li>Falhas transitórias de conexão de rede não devem interromper o pipeline; cada atividade de cópia deve tentar se reconectar até 3 vezes com intervalo de 30 segundos.</li>\n<li>A lógica de carga na camada Silver deve ser estritamente idempotente (reexecuções não podem duplicar linhas).</li>\n</ul>"
      }
    ],
    questions: [
      {
        id: "cs5_q1",
        type: "single",
        prompt: "Com base nas seções 'Visão Geral' e 'Requisitos de Dados', como você deve estruturar o pipeline do Fabric Data Factory para iterar sobre as 120 tabelas garantindo concorrência máxima de 25 cópias simultâneas?",
        options: [
          {
            id: "A",
            text: "Utilizar uma atividade ForEach com 'Sequential' desmarcado e 'Batch count' configurado em 25.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Utilizar uma atividade ForEach com 'Sequential' marcado e tempo limite de 25 minutos.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Criar 120 atividades de Copy Data conectadas manualmente em série.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Utilizar uma atividade Until com condição booleana infinita.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> A atividade <strong>ForEach</strong> no Data Factory suporta execução concorrente desmarcando a opção <code>Sequential</code> e definindo o <code>Batch count</code> com o número desejado de threads paralelas (25). Isso otimiza o tempo total sem estourar as conexões de banco de dados.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> 'Sequential' força execução estritamente sequencial (1 thread).</li>\n<li><strong>C:</strong> Desenhar 120 atividades manuais é impraticável e não escalável.</li>\n<li><strong>D:</strong> Until é uma estrutura de loop condicional, não de iteração de lista.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> O limite máximo de <code>Batch count</code> na atividade ForEach é de 50 threads simultâneas.</div>",
        question: "Com base nas seções 'Visão Geral' e 'Requisitos de Dados', como você deve estruturar o pipeline do Fabric Data Factory para iterar sobre as 120 tabelas garantindo concorrência máxima de 25 cópias simultâneas?",
        title: "Com base nas seções 'Visão Geral' e 'Requisitos de Dados', c..."
      },
      {
        id: "cs5_q2",
        type: "single",
        prompt: "Com base na exigência de resiliência da seção 'Requisitos Técnicos', como as falhas transitórias de rede devem ser tratadas nas atividades de Copy Data do Data Factory?",
        options: [
          {
            id: "A",
            text: "Configurar a propriedade 'Retry' com o valor 3 e o 'Retry interval (sec)' com 30.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Adicionar uma atividade Wait de 4 horas antes de cada Copy Data.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Excluir o workspace do Fabric e recriá-lo a cada falha de rede.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Desativar o firewall do Azure e permitir acesso público irrestrito.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> As atividades do Data Factory possuem propriedades nativas de política de execução (Policy), onde configurar <code>Retry = 3</code> e <code>Retry interval (sec) = 30</code> instrui o serviço a tentar automaticamente a execução até 3 vezes com pausa de 30 segundos entre tentativas antes de registrar falha definitiva.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Esperar 4 horas atrasa o pipeline desnecessariamente.</li>\n<li><strong>C e D:</strong> Destruir workspaces ou desativar segurança são soluções absurdas.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Políticas de repetição (Retry Policies) são a melhor prática oficial para mitigar erros transitórios (código HTTP 429, 503 ou timeouts breves de rede).</div>",
        question: "Com base na exigência de resiliência da seção 'Requisitos Técnicos', como as falhas transitórias de rede devem ser tratadas nas atividades de Copy Data do Data Factory?",
        title: "Com base na exigência de resiliência da seção 'Requisitos Té..."
      },
      {
        id: "cs5_q3",
        type: "single",
        prompt: "Considerando o requisito de SCD Tipo 2 na dimensão de clientes na camada Silver, qual tecnologia e instrução garantem que a atualização das linhas antigas e a inserção das novas versões ocorram de forma atômica e idempotente?",
        options: [
          {
            id: "A",
            text: "Delta Lake MERGE executado via PySpark ou SQL com cláusulas MATCHED e NOT MATCHED.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Instrução TRUNCATE TABLE seguida de INSERT INTO completo.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Comando DROP TABLE executado antes de cada carga incremental.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Exportação manual de dados para planilhas eletrônicas locais.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> A instrução <strong>Delta MERGE</strong> é o padrão canônico para SCD Tipo 2 no Fabric. Ela permite correlacionar a chave de negócio do cliente, atualizar a linha ativa anterior (marcando a data de encerramento e status inativo) e inserir o novo registro com vigência atual em uma única transação atômica ACID.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B e C:</strong> TRUNCATE e DROP destroem o histórico temporal de versões anteriores.</li>\n<li><strong>D:</strong> Planilhas manuais violam os princípios de engenharia de dados corporativa.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> No Spark, utilize <code>deltaTable.alias('target').merge(...)</code> para implementar SCD Tipo 2 com idempotência garantida.</div>",
        question: "Considerando o requisito de SCD Tipo 2 na dimensão de clientes na camada Silver, qual tecnologia e instrução garantem que a atualização das linhas antigas e a inserção das novas versões ocorram de forma atômica e idempotente?",
        title: "Considerando o requisito de SCD Tipo 2 na dimensão de client..."
      }
    ]
  },
  {
    id: "cs6",
    type: "case_study",
    domain: "Estudo de Caso Corporativo: Tailwind Traders Multi-Cloud Analytics",
    caseTitle: "Tailwind Traders: Arquitetura Zero-Copy Multi-Cloud e Governança com Purview",
    tabs: [
      {
        id: "overview",
        title: "Visão Geral",
        content: "<h4>Perfil da Empresa</h4>\n<p>A Tailwind Traders é uma varejista global que adquiriu recentemente duas empresas concorrentes operando em diferentes provedores de nuvem pública (AWS e Google Cloud Platform).</p>\n<h4>Objetivo de Unificação</h4>\n<p>Consolidar um único Data Lake corporativo no <strong>Microsoft Fabric OneLake</strong> conectando dados distribuídos em múltiplas nuvens sem custos de egress e com rastreabilidade total de governança via <strong>Microsoft Purview</strong>.</p>"
      },
      {
        id: "existing_env",
        title: "Ambiente Atual",
        content: "<h4>Armazenamento Multi-Cloud</h4>\n<ul>\n<li><strong>AWS:</strong> 80 TB de dados históricos em formato Delta Lake armazenados em buckets do <strong>Amazon S3</strong>.</li>\n<li><strong>GCP:</strong> 40 TB de logs de navegação em formato Parquet armazenados no <strong>Google Cloud Storage (GCS)</strong>.</li>\n<li><strong>Microsoft:</strong> Dados de vendas de CRM corporativo hospedados no <strong>Microsoft Dataverse (Dynamics 365)</strong>.</li>\n</ul>"
      },
      {
        id: "data_req",
        title: "Requisitos de Dados",
        content: "<h4>Acesso e Zero-Copy</h4>\n<ul>\n<li>Nenhum dado das contas AWS ou GCP pode ser copiado fisicamente para o Azure para evitar custos proibitivos de transferência de rede (egress fees).</li>\n<li>Os dados do Dataverse devem ser acessados pelos engenheiros no OneLake com sincronização contínua sem que a equipe precise construir pipelines de extração ETL.</li>\n</ul>"
      },
      {
        id: "tech_req",
        title: "Requisitos Técnicos",
        content: "<h4>Segurança e Rótulos de Sensibilidade</h4>\n<ul>\n<li>Rótulos de sensibilidade 'Confidencial' do Microsoft Purview aplicados ao Lakehouse devem se propagar automaticamente para todos os modelos semânticos e relatórios derivados.</li>\n<li>Políticas de Data Loss Prevention (DLP) devem impedir que relatórios contendo números de previdência social (SSN) sejam exportados para o formato Excel por usuários comuns.</li>\n</ul>"
      }
    ],
    questions: [
      {
        id: "cs6_q1",
        type: "multi",
        prompt: "Com base nas seções 'Ambiente Atual' e 'Requisitos de Dados', quais DOIS tipos de OneLake Shortcuts devem ser configurados no Lakehouse para expor os dados da AWS e do GCP sem movimentação física? (Escolha duas alternativas).",
        options: [
          {
            id: "A",
            text: "OneLake Shortcut apontando para o bucket do Amazon S3.",
            isCorrect: true
          },
          {
            id: "B",
            text: "OneLake Shortcut apontando para o bucket do Google Cloud Storage (GCS).",
            isCorrect: true
          },
          {
            id: "C",
            text: "Pipeline de Copy Data com transferência por FTP seguro.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Exportação manual de arquivos CSV via navegador web.",
            isCorrect: false
          },
          {
            id: "E",
            text: "Servidor NFS montado em máquina virtual local.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que as alternativas A e B estão corretas:</strong> O Microsoft OneLake oferece suporte nativo a <strong>Shortcuts para Amazon S3</strong> e <strong>Shortcuts para Google Cloud Storage (GCS)</strong>. Esses atalhos funcionam como ponteiros virtuais que permitem aos motores analíticos do Fabric consultar dados diretamente nos storages de terceiros sem cobrança de cópia e sem mover arquivos fisicamente.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>C, D e E:</strong> Envolvem cópias físicas de arquivos que geram altos custos de transferência e manutenção.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> O OneLake suporta atalhos para: <strong>ADLS Gen2</strong>, <strong>Amazon S3</strong>, <strong>Google Cloud Storage</strong> e <strong>Dataverse</strong>.</div>",
        question: "Com base nas seções 'Ambiente Atual' e 'Requisitos de Dados', quais DOIS tipos de OneLake Shortcuts devem ser configurados no Lakehouse para expor os dados da AWS e do GCP sem movimentação física? (Escolha duas alternativas).",
        title: "Com base nas seções 'Ambiente Atual' e 'Requisitos de Dados'..."
      },
      {
        id: "cs6_q2",
        type: "single",
        prompt: "Com base na seção 'Requisitos de Dados', qual funcionalidade da plataforma Microsoft atende à exigência de disponibilizar os dados do Microsoft Dataverse (Dynamics 365) no OneLake com sincronização contínua e esforço zero de ETL?",
        options: [
          {
            id: "A",
            text: "Habilitar o Fabric Link no portal do Microsoft Dataverse.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Criar um Dataflow Gen2 executado a cada 1 minuto.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Escrever scripts em linguagem C# compilados em console apps.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Exportar os dados para fita magnética e fazer upload físico.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> O <strong>Fabric Link for Dataverse</strong> conecta diretamente as tabelas do Dynamics 365 e Power Apps ao OneLake em formato Delta Parquet. Uma vez ativado, o Dataverse mantém atalhos no OneLake atualizados continuamente de forma transparente e gerenciada pela Microsoft.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> São soluções custosas, complexas e manuais que contrariam o uso do recurso nativo Fabric Link.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> O Fabric Link cria tabelas Delta no OneLake sem que o desenvolvedor precise construir pipelines no Data Factory.</div>",
        question: "Com base na seção 'Requisitos de Dados', qual funcionalidade da plataforma Microsoft atende à exigência de disponibilizar os dados do Microsoft Dataverse (Dynamics 365) no OneLake com sincronização contínua e esforço zero de ETL?",
        title: "Com base na seção 'Requisitos de Dados', qual funcionalidade..."
      },
      {
        id: "cs6_q3",
        type: "single",
        prompt: "Com base na seção 'Requisitos Técnicos', como os rótulos de confidencialidade do Microsoft Purview aplicados no Lakehouse protegem os artefatos downstream no Fabric e Power BI?",
        options: [
          {
            id: "A",
            text: "Através da herança automática downstream para modelos semânticos e relatórios filhos.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Excluindo o relatório do Power BI caso contenha mais de 10 páginas.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Bloqueando o acesso de qualquer usuário durante os finais de semana.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Exigindo que o analista digite uma senha de 64 dígitos a cada clique.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> A <strong>Herança Downstream de Rótulos de Sensibilidade</strong> do Purview assegura que, quando um item de dados original (Lakehouse ou Warehouse) é rotulado como 'Confidencial', todos os modelos semânticos e relatórios gerados a partir dele herdam automaticamente a classificação e suas restrições (como bloqueio de exportação DLP).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> São comportamentos inexistentes e absurdos na governança do Purview.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Rótulos do Purview acompanham os dados inclusive quando exportados para arquivos Excel ou PDF, mantendo a criptografia de proteção.</div>",
        question: "Com base na seção 'Requisitos Técnicos', como os rótulos de confidencialidade do Microsoft Purview aplicados no Lakehouse protegem os artefatos downstream no Fabric e Power BI?",
        title: "Com base na seção 'Requisitos Técnicos', como os rótulos de ..."
      }
    ]
  },
  {
    id: "cs7",
    type: "case_study",
    domain: "Estudo de Caso Corporativo: Northwind Health Diagnostics",
    caseTitle: "Northwind Health: Diagnósticos em Tempo Real, CDC e Alta Disponibilidade com Eventhouse",
    tabs: [
      {
        id: "overview",
        title: "Visão Geral",
        content: "<h4>Perfil da Instituição</h4>\n<p>A Northwind Health Diagnostics opera uma rede de 80 laboratórios de análises clínicas e hospitais de alta complexidade realizando mais de 1 milhão de exames laboratoriais por dia.</p>\n<h4>Desafio Crítico</h4>\n<p>Resultados críticos de exames (como troponina para infarto agudo do miocárdio ou hemograma com alterações severas) precisam disparar alertas para os médicos em menos de 5 segundos a partir da liberação no banco de dados operacional.</p>"
      },
      {
        id: "existing_env",
        title: "Ambiente Atual",
        content: "<h4>Infraestrutura de TI</h4>\n<ul>\n<li><strong>Sistema Laboratorial (LIS):</strong> Banco de dados relacional transacional em <strong>Azure SQL Database</strong> com Change Data Capture (CDC) habilitado na tabela <code>ExamesLiberados</code>.</li>\n<li><strong>Capacidade Fabric:</strong> F64 compartilhada entre o workspace de alertas clínicos e o workspace de BI gerencial.</li>\n<li><strong>Consumo:</strong> Médicos utilizam um painel de alerta em tempo real; diretores médicos utilizam relatórios analíticos consolidados no Power BI.</li>\n</ul>"
      },
      {
        id: "data_req",
        title: "Requisitos de Dados",
        content: "<h4>Fluxo de Dados em Tempo Real</h4>\n<ul>\n<li>As alterações na tabela do Azure SQL Database devem ser capturadas continuamente pelo Fabric sem impactar a performance das transações de gravação dos biomédicos.</li>\n<li>Os eventos devem ser ingeridos em uma tabela de streaming no <strong>Eventhouse (KQL Database)</strong> com retenção de cache quente de 7 dias para buscas instantâneas.</li>\n<li>Exames com mais de 7 dias devem ser retidos em armazenamento frio de baixo custo por 10 anos para conformidade legal.</li>\n</ul>"
      },
      {
        id: "tech_req",
        title: "Requisitos Técnicos",
        content: "<h4>Segurança de Prontuários (HIPAA / LGPD)</h4>\n<ul>\n<li>Médicos só podem visualizar exames de pacientes internados em sua respectiva unidade hospitalar (coluna <code>HospitalUnitId</code>).</li>\n<li>A diretoria exige relatórios em <strong>Power BI Direct Lake</strong> sem que a regra de segurança cause fallback para DirectQuery.</li>\n</ul>"
      }
    ],
    questions: [
      {
        id: "cs7_q1",
        type: "single",
        prompt: "Com base na seção 'Ambiente Atual' e 'Requisitos de Dados', qual conector de origem do Fabric Eventstream deve ser configurado para capturar continuamente as alterações na tabela ExamesLiberados do Azure SQL Database sem escrever código de polling?",
        options: [
          {
            id: "A",
            text: "Azure SQL Database Change Data Capture (CDC) connector no Eventstream.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Pipeline agendado no Data Factory executando SELECT a cada 1 segundo.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Exportação manual de dados via Assistente de Importação e Exportação do SSMS.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Triggers que enviam emails SMTP para uma caixa postal do Gmail.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> O conector nativo <strong>Azure SQL Database (CDC)</strong> no Fabric Eventstream lê de forma assíncrona as tabelas de Change Data Capture geradas pelo SQL Server, capturando inserções, alterações e exclusões em tempo real sem degradar as transações operacionais do sistema hospitalar.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Polling a cada 1 segundo satura a CPU do banco de dados relacional e gera locks.</li>\n<li><strong>C e D:</strong> Processos manuais e emails são incompatíveis com alertas de emergência médica em subsegundo.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> O conector CDC do Eventstream transmite eventos nos formatos JSON contendo os metadados da operação (Insert, Update, Delete) e os valores de colunas anteriores e posteriores.</div>",
        question: "Com base na seção 'Ambiente Atual' e 'Requisitos de Dados', qual conector de origem do Fabric Eventstream deve ser configurado para capturar continuamente as alterações na tabela ExamesLiberados do Azure SQL Database sem escrever código de polling?",
        title: "Com base na seção 'Ambiente Atual' e 'Requisitos de Dados', ..."
      },
      {
        id: "cs7_q2",
        type: "single",
        prompt: "Com base na seção 'Requisitos de Dados', como as políticas de Caching e Retenção do KQL Database no Eventhouse devem ser configuradas para atender aos requisitos de 7 dias de alerta e 10 anos de histórico legal?",
        options: [
          {
            id: "A",
            text: "Hot Cache Policy = 7 dias e Retention Policy = 3650 dias (10 anos).",
            isCorrect: true
          },
          {
            id: "B",
            text: "Hot Cache Policy = 3650 dias e Retention Policy = 7 dias.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Desativar a política de retenção para expurgar dados a cada 24 horas.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Configurar o cache quente em memória RAM para 5 minutos e excluir o restante.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> A <strong>Hot Cache Policy</strong> define o período em que os dados residem em armazenamento SSD/RAM local para consultas em milissegundos (7 dias), enquanto a <strong>Retention Policy</strong> define o prazo total de existência dos dados antes do descarte permanente (3650 dias / 10 anos no storage durável OneLake).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Inverter os parâmetros reteria apenas 7 dias de histórico e sobrecarregaria a memória com 10 anos de cache.</li>\n<li><strong>C e D:</strong> Excluir dados viola o prazo legal obrigatório de 10 anos para prontuários médicos.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Hot Cache = performance imediata; Soft Delete / Retention Policy = ciclo de vida total dos dados.</div>",
        question: "Com base na seção 'Requisitos de Dados', como as políticas de Caching e Retenção do KQL Database no Eventhouse devem ser configuradas para atender aos requisitos de 7 dias de alerta e 10 anos de histórico legal?",
        title: "Com base na seção 'Requisitos de Dados', como as políticas d..."
      },
      {
        id: "cs7_q3",
        type: "single",
        prompt: "Com base na seção 'Requisitos Técnicos', onde a regra de Row-Level Security (RLS) por HospitalUnitId deve ser implementada para assegurar que os médicos vejam apenas exames de sua unidade sem que os relatórios do Power BI sofram Fallback do modo Direct Lake?",
        options: [
          {
            id: "A",
            text: "Dentro do Modelo Semântico do Power BI (Semantic Model RLS).",
            isCorrect: true
          },
          {
            id: "B",
            text: "Diretamente no SQL Analytics Endpoint do Lakehouse.",
            isCorrect: false
          },
          {
            id: "C",
            text: "No arquivo hosts do computador pessoal do médico.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Em uma planilha de senhas compartilhada no Microsoft Teams.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> Para manter a performance in-memory do <strong>Power BI Direct Lake</strong> sem sofrer Fallback automático para consultas DirectQuery T-SQL, as regras de Row-Level Security devem ser configuradas <em>dentro do Modelo Semântico do Power BI</em>.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> RLS configurada no SQL Analytics Endpoint do Lakehouse causa Fallback obrigatório para DirectQuery.</li>\n<li><strong>C e D:</strong> São práticas inseguras e sem efeito sobre permissões de dados.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Essa é a regra mais importante de Direct Lake: <strong>Semantic Model RLS = Direct Lake permitido</strong>; <strong>SQL Endpoint RLS = Fallback to DirectQuery</strong>.</div>",
        question: "Com base na seção 'Requisitos Técnicos', onde a regra de Row-Level Security (RLS) por HospitalUnitId deve ser implementada para assegurar que os médicos vejam apenas exames de sua unidade sem que os relatórios do Power BI sofram Fallback do modo Direct Lake?",
        title: "Com base na seção 'Requisitos Técnicos', onde a regra de Row..."
      }
    ]
  },
  {
    id: "cs8",
    type: "case_study",
    domain: "Estudo de Caso Corporativo: Alpine Ski & Resorts Real-Time Intelligence",
    caseTitle: "Alpine Ski Resorts: Telemetria de Sensores de Pista, Detecção de Riscos e Testes Zero-Copy",
    tabs: [
      {
        id: "overview",
        title: "Visão Geral",
        content: "<h4>Perfil da Empresa</h4>\n<p>A Alpine Ski & Resorts opera 15 estações de esqui e esportes de inverno de classe mundial com mais de 2.000 sensores IoT instalados em pistas, teleféricos e encostas com risco de avalanche.</p>\n<h4>Desafio Operacional</h4>\n<p>Monitorar temperatura da neve, velocidade do vento e estabilidade do solo em tempo real no <strong>Microsoft Fabric</strong> para emitir alertas de evacuação instantâneos e analisar padrões climáticos históricos de longo prazo.</p>"
      },
      {
        id: "existing_env",
        title: "Ambiente Atual",
        content: "<h4>Estrutura Tecnológica</h4>\n<ul>\n<li><strong>Dispositivos IoT:</strong> 2.000 sensores transmitindo via protocolo MQTT para <strong>Azure IoT Hub</strong> mensagens a cada 5 segundos.</li>\n<li><strong>Workspaces Fabric:</strong> <code>WS_Alpine_LiveOps</code> (para tempo real) e <code>WS_Alpine_DataLab</code> (para homologação e ciência de dados).</li>\n<li><strong>Capacidade:</strong> Capacidade dedicada F64.</li>\n</ul>"
      },
      {
        id: "data_req",
        title: "Requisitos de Dados",
        content: "<h4>Processamento de Streaming e Lotes</h4>\n<ul>\n<li>Um streaming Spark Structured Streaming no Fabric deve ler os dados do IoT Hub em janelas de tempo não sobrepostas de 10 minutos (Tumbling Windows) para calcular a média de rajadas de vento por encosta.</li>\n<li>Para tolerar instabilidade de sinal nas montanhas, mensagens com até 20 minutos de atraso devem ser aceitas e integradas ao cálculo da janela correta através de Watermarking.</li>\n</ul>"
      },
      {
        id: "tech_req",
        title: "Requisitos Técnicos",
        content: "<h4>Ambiente de Homologação e Testes Rápidos</h4>\n<ul>\n<li>A equipe de cientistas de dados no workspace <code>WS_Alpine_DataLab</code> precisa clonar instantaneamente a tabela histórica de 10 bilhões de linhas de telemetria para treinar modelos preditivos de avalanche sem incorrer em novos custos de armazenamento de dados.</li>\n<li>A tabela de homologação deve permitir alterações destrutivas sem afetar os dados oficiais de produção.</li>\n</ul>"
      }
    ],
    questions: [
      {
        id: "cs8_q1",
        type: "single",
        prompt: "Com base na seção 'Requisitos de Dados', qual tipo de janela de tempo e qual cláusula do Spark Structured Streaming atendem ao cálculo de médias de rajadas de vento a cada 10 minutos sem sobreposição aceitando dados atrasados em até 20 minutos?",
        options: [
          {
            id: "A",
            text: "Tumbling Window de 10 minutos combinada com .withWatermark('EventTime', '20 minutes').",
            isCorrect: true
          },
          {
            id: "B",
            text: "Sliding Window de 10 minutos com avanço a cada 1 segundo sem watermark.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Session Window baseada em 24 horas de inatividade total de sinal.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Execução em lote único diário desativando o streaming.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> As <strong>Tumbling Windows</strong> são janelas de tempo fixas e não sobrepostas (ex: 10:00-10:10, 10:10-10:20). A combinação com <code>.withWatermark('EventTime', '20 minutes')</code> instrui o Spark a manter o estado da janela em memória e aceitar mensagens que cheguem com até 20 minutos de atraso em relação ao tempo máximo observado.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Sliding Window com avanço de 1 segundo gera sobreposição e não trata o atraso sem watermark.</li>\n<li><strong>C:</strong> Session windows dependem de inatividade, não sendo adequadas para janelas regulares de 10 minutos.</li>\n<li><strong>D:</strong> Carga em lote diário viola o requisito de alertas de emergência em tempo real.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> <strong>Tumbling</strong> = blocos fixos contínuos sem sobreposição; <strong>Hopping/Sliding</strong> = blocos sobrepostos com salto regular; <strong>Session</strong> = agrupamento por períodos de atividade.</div>",
        question: "Com base na seção 'Requisitos de Dados', qual tipo de janela de tempo e qual cláusula do Spark Structured Streaming atendem ao cálculo de médias de rajadas de vento a cada 10 minutos sem sobreposição aceitando dados atrasados em até 20 minutos?",
        title: "Com base na seção 'Requisitos de Dados', qual tipo de janela..."
      },
      {
        id: "cs8_q2",
        type: "single",
        prompt: "Com base na seção 'Requisitos Técnicos', qual funcionalidade do Fabric permite aos cientistas de dados clonar a tabela histórica de 10 bilhões de linhas instantaneamente para testes isolados sem duplicar o volume físico de armazenamento no OneLake?",
        options: [
          {
            id: "A",
            text: "Zero-Copy Table Clone utilizando a sintaxe CREATE TABLE ... AS CLONE OF.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Executar um pipeline Copy Data duplicando fisicamente os arquivos Parquet.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Exportar toda a tabela para arquivos CSV compactados em formato ZIP.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Executar o comando VACUUM com tempo de retenção zero em produção.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> O recurso <strong>Zero-Copy Table Clone</strong> (<code>CREATE TABLE Tabela_Teste AS CLONE OF Tabela_Prod</code>) cria uma cópia em nível de metadados que aponta para os mesmos arquivos Parquet imutáveis no OneLake. Os testes e modificações feitos pelos cientistas na tabela clonada gravam novos arquivos Delta sem alterar a tabela de produção e sem duplicar o storage dos dados inalterados.</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B:</strong> Duplicar 10 bilhões de linhas fisicamente consome horas de processamento e dobra os custos de storage.</li>\n<li><strong>C:</strong> Exportar para ZIP perde o formato colunar e quebra a performance.</li>\n<li><strong>D:</strong> VACUUM limpa arquivos obsoletos e não cria clones para testes.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> Clones no Fabric suportam tanto clones do estado atual quanto clones de um ponto no passado (Time Travel Clone) usando a cláusula <code>AS OF</code>.</div>",
        question: "Com base na seção 'Requisitos Técnicos', qual funcionalidade do Fabric permite aos cientistas de dados clonar a tabela histórica de 10 bilhões de linhas instantaneamente para testes isolados sem duplicar o volume físico de armazenamento no OneLake?",
        title: "Com base na seção 'Requisitos Técnicos', qual funcionalidade..."
      },
      {
        id: "cs8_q3",
        type: "single",
        prompt: "Como os cientistas de dados devem garantir que as operações de gravação e treinamento de modelos no workspace WS_Alpine_DataLab não causem throttling ou esgotem as CUs das operações de segurança em tempo real do WS_Alpine_LiveOps durante horários críticos?",
        options: [
          {
            id: "A",
            text: "Associar o workspace de testes WS_Alpine_DataLab a uma capacidade Fabric dedicada separada.",
            isCorrect: true
          },
          {
            id: "B",
            text: "Configurar a prioridade do Windows Task Manager na máquina dos cientistas.",
            isCorrect: false
          },
          {
            id: "C",
            text: "Desativar o firewall de rede durante a execução dos modelos.",
            isCorrect: false
          },
          {
            id: "D",
            text: "Forçar os operadores de pista a desligarem os sensores em dias de tempestade.",
            isCorrect: false
          }
        ],
        explanation: "<div class=\"explanation-correct\"><strong>✅ Por que a alternativa A está correta:</strong> No Microsoft Fabric, o isolamento rigoroso de computação (evitando que cargas de testes ou ciência de dados consumam CUs de operações críticas) é realizado <strong>atribuindo workspaces diferentes a capacidades Fabric diferentes</strong> (ex: uma capacidade dedicada para produção e outra para desenvolvimento/testes, que pode ser pausada quando ociosa).</div>\n<div class=\"explanation-distractors\"><strong>❌ Análise dos Distratores:</strong>\n<ul>\n<li><strong>B, C e D:</strong> Gerenciador de tarefas local, desativar firewall ou desligar sensores são ações sem sentido que violam a operação do resort.</li>\n</ul></div>\n<div class=\"explanation-tip\"><strong>💡 Dica de Prova DP-700:</strong> A fronteira de governança e isolamento de computação (CUs) no Fabric é a <strong>Capacidade (Capacity)</strong>, e não o workspace. Workspaces na mesma capacidade compartilham o mesmo pool de CUs.</div>",
        question: "Como os cientistas de dados devem garantir que as operações de gravação e treinamento de modelos no workspace WS_Alpine_DataLab não causem throttling ou esgotem as CUs das operações de segurança em tempo real do WS_Alpine_LiveOps durante horários críticos?",
        title: "Como os cientistas de dados devem garantir que as operações ..."
      }
    ]
  }
];

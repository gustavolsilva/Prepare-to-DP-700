#!/usr/bin/env python3
"""
standardize_all_quizzes.py
Padroniza todas as lições (0002 a 0015) para o layout de excelência da Lição 0001:
- Container <section id="bloco-quiz" class="totc-card">
- Cabeçalho "Pontos Críticos para a Prática e para o Exame DP-700"
- Cartão de síntese de pontos críticos (.summary-card) com 4 tópicos essenciais
- Cartão de Desafio (.quiz-card) com botões (.quiz-option-btn), data-correct e feedback
- Rodapé de navegação unificado conectando à Folha de Referência e Próxima Lição
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS_DIR = os.path.join(BASE_DIR, "lessons")

LESSON_METADATA = {
    "0002": {
        "file": "0002-storage-fundamentals-parquet-delta-medallion.html",
        "ref_link": "../reference/02-storage-delta-medallion-shortcuts-guide.html",
        "ref_title": "Folha de Referência 02 (Storage, Delta & Medallion)",
        "next_link": "0003-dimensional-modeling-and-three-languages-sql-spark-kql.html",
        "next_title": "0003 (Modelagem Dimensional e Três Linguagens)",
        "summary": [
            ("Apache Parquet vs Delta Lake", "Parquet oferece compressão colunar e estatísticas de row group (Predicate Pushdown), enquanto o Delta Lake adiciona transações ACID atômicas através da pasta <code>_delta_log</code>."),
            ("Arquitetura Medallion", "Bronze preserva dados brutos imutáveis; Silver limpa, deduplica e conforma; Gold expõe modelos dimensionais prontos para Direct Lake de subsegundo no Power BI."),
            ("Time Travel & VACUUM", "Consultas históricas utilizam <code>VERSION AS OF</code>. Executar <code>VACUUM</code> com retenção inferior ao intervalo desejado apaga os arquivos Parquet físicos antigos, causando <code>FileNotFoundException</code>."),
            ("Otimização V-Order", "Tecnologia exclusiva do Fabric que reordena dicionários colunares para aceleração instantânea em memória pelos motores VertiPaq e SQL Endpoint.")
        ]
    },
    "0003": {
        "file": "0003-dimensional-modeling-and-three-languages-sql-spark-kql.html",
        "ref_link": "../reference/04-three-languages-sql-pyspark-kql-cheatsheet.html",
        "ref_title": "Folha de Referência 04 (T-SQL, PySpark & KQL Cheatsheet)",
        "next_link": "0004-onelake-capacities-smoothing-domains-spark-pools.html",
        "next_title": "0004 (Capacidades, Smoothing e Spark Pools)",
        "summary": [
            ("Modelagem Star Schema", "Fatos registram métricas numéricas acumuladas; Dimensões fornecem contexto filtrável com Chaves Substitutas (Surrogate Keys) geradas de forma sequencial ou hash."),
            ("T-SQL no Warehouse", "Linguagem obrigatória para transações ACID completas, integridade relacional, comandos MERGE atômicos e governança com RLS/CLS."),
            ("PySpark no Lakehouse", "Motor ideal para transformação distribuída de grandes volumes, processamento de dados semiestruturados (JSON) e engenharia de dados em lote."),
            ("KQL no Eventhouse", "Linguagem analítica imbatível para telemetria de IoT, logs e séries temporais com indexação total e consultas em milissegundos.")
        ]
    },
    "0004": {
        "file": "0004-onelake-capacities-smoothing-domains-spark-pools.html",
        "ref_link": "../reference/03-architectural-engines-decision-matrix.html",
        "ref_title": "Folha de Referência 03 (Matriz Decisória de Motores)",
        "next_link": "0005-architectural-decision-guide-lakehouse-warehouse-eventhouse.html",
        "next_title": "0005 (Guia Decisório: Lakehouse vs Warehouse vs Eventhouse)",
        "summary": [
            ("Capacity Units (CUs)", "Toda a computação do Fabric é mensurada em CUs; SKUs a partir de F64 dispensam licenças Pro individuais para visualizadores no Power BI."),
            ("Algoritmo de Smoothing", "Operações interativas amortizam consumo em 5 minutos; operações em segundo plano (background jobs) são diluídas em uma janela contínua de 24 horas."),
            ("Starter Pools vs Custom Pools", "Starter Pools iniciam em menos de 10 segundos com instâncias pré-aquecidas; pools personalizados oferecem nós dedicados mas demoram 2-3 minutos de boot."),
            ("Domínios de Governança", "Permitem agrupar workspaces por unidades de negócio (Finanças, Vendas) para auditoria e controle de custos descentralizado.")
        ]
    },
    "0005": {
        "file": "0005-architectural-decision-guide-lakehouse-warehouse-eventhouse.html",
        "ref_link": "../reference/03-architectural-engines-decision-matrix.html",
        "ref_title": "Folha de Referência 03 (Matriz Decisória de Motores)",
        "next_link": "0006-shortcuts-and-mirroring-zero-copy-integration.html",
        "next_title": "0006 (Atalhos e Espelhamento Zero-Copy)",
        "summary": [
            ("Lakehouse (Foco em Arquivos & Spark)", "Ideal para engenheiros Python/Scala e dados não estruturados; SQL Endpoint fornece acesso analítico somente leitura."),
            ("Warehouse (Foco em T-SQL & ACID)", "Exigido quando o cenário necessita de transações ACID multi-tabela, Stored Procedures, DDL/DML nativo e segurança RLS/CLS no banco."),
            ("Eventhouse (Foco em Streaming & KQL)", "Projetado para ingestão contínua em tempo real de logs, telemetria de sensores e consultas temporais ultrarrápidas."),
            ("Fundação OneLake Compartilhada", "Todos os três motores leem e gravam em tabelas Delta abertas sem cópias ou movimentação física de dados.")
        ]
    },
    "0006": {
        "file": "0006-shortcuts-and-mirroring-zero-copy-integration.html",
        "ref_link": "../reference/02-storage-delta-medallion-shortcuts-guide.html",
        "ref_title": "Folha de Referência 02 (Storage, Delta & Shortcuts)",
        "next_link": "0007-orchestration-pipelines-dataflows-dag.html",
        "next_title": "0007 (Orquestração: Pipelines e Dataflows Gen2)",
        "summary": [
            ("Conceito de Shortcuts (Atalhos)", "Ponteiros lógicos no OneLake que referenciam dados em fontes externas (ADLS Gen2, Amazon S3, Dataverse) sem duplicar armazenamento."),
            ("Zero-Copy Architecture", "Consultas analíticas executadas no Fabric leem os dados diretamente na nuvem de origem, reduzindo custos de tráfego de rede e tempo de ETL."),
            ("Shortcuts Internos", "Permitem reutilizar tabelas entre diferentes Lakehouses e Warehouses sem quebrar limites de workspace ou duplicar dados."),
            ("Mirroring no Fabric", "Replicação automática e contínua de bancos relacionais (Cosmos DB, Azure SQL, Snowflake) em formato Delta Parquet no OneLake.")
        ]
    },
    "0007": {
        "file": "0007-orchestration-pipelines-dataflows-dag.html",
        "ref_link": "../reference/04-three-languages-sql-pyspark-kql-cheatsheet.html",
        "ref_title": "Folha de Referência 04 (Linguagens & Orquestração)",
        "next_link": "0008-incremental-loading-watermark-scd.html",
        "next_title": "0008 (Carga Incremental e SCD Tipo 2)",
        "summary": [
            ("Data Pipelines (DAG)", "Orquestrador corporativo com suporte a dependências (Sucesso, Falha, Conclusão), atividades de fluxo (ForEach, If Condition, Until) e parâmetros dinâmicos."),
            ("Fast Copy no Data Factory", "Acelera transferências massivas de bancos relacionais e arquivos para o Lakehouse com paralelismo otimizado em rede."),
            ("Dataflows Gen2", "Transformação visual e baseada em código Power Query M com suporte a transações e staging automático em Lakehouse."),
            ("Tratamento de Exceções", "Pipelines devem implementar branches de falha enviando notificações via Web Activity ou integrando com o Azure Monitor.")
        ]
    },
    "0008": {
        "file": "0008-incremental-loading-watermark-scd.html",
        "ref_link": "../reference/04-three-languages-sql-pyspark-kql-cheatsheet.html",
        "ref_title": "Folha de Referência 04 (Padrões de Carga Incremental)",
        "next_link": "0009-batch-transformations-sql-spark-clones.html",
        "next_title": "0009 (Transformações em Lote e Table Clones)",
        "summary": [
            ("Padrão de Coluna Watermark", "Utiliza carimbos de data/hora (Timestamp) para extrair estritamente registros criados ou modificados desde a última execução."),
            ("Change Data Capture (CDC)", "Captura eventos pontuais de INSERT, UPDATE e DELETE diretamente dos logs transacionais do banco relacional de origem."),
            ("SCD Tipo 1 vs Tipo 2", "SCD Tipo 1 sobrescreve o valor antigo; SCD Tipo 2 preserva a rastreabilidade histórica completa criando novas linhas ativas com datas de vigência."),
            ("Operações MERGE no Delta Lake", "O comando MERGE realiza operações atômicas de UPSERT (Update + Insert) em uma única transação ACID no OneLake.")
        ]
    },
    "0009": {
        "file": "0009-batch-transformations-sql-spark-clones.html",
        "ref_link": "../reference/04-three-languages-sql-pyspark-kql-cheatsheet.html",
        "ref_title": "Folha de Referência 04 (Transformações em Lote)",
        "next_link": "0010-streaming-eventstreams-spark-windows.html",
        "next_title": "0010 (Streaming em Tempo Real com Eventstreams)",
        "summary": [
            ("Transformações Vetorizadas no Spark", "O Native Execution Engine vetorizado em C++ executa operações relacionais em memória sem a sobrecarga do compilador JVM."),
            ("Views Relacionais no Warehouse", "Permitem abstrair transformações complexas de negócios sem custos de armazenamento adicional ou duplicação de dados."),
            ("Table Clones (CLONE TABLE)", "O comando <code>AS CLONE</code> cria uma cópia quase instantânea de zero-custo (Shallow Clone) apontando para os mesmos arquivos físicos."),
            ("Isolamento para Homologação", "Permite que times de QA executem testes destrutivos em tabelas clonadas de terabytes sem afetar a produção.")
        ]
    },
    "0010": {
        "file": "0010-streaming-eventstreams-spark-windows.html",
        "ref_link": "../reference/04-three-languages-sql-pyspark-kql-cheatsheet.html",
        "ref_title": "Folha de Referência 04 (Streaming e Janelas Temporais)",
        "next_link": "0011-kql-eventhouse-update-policies-materialized-views.html",
        "next_title": "0011 (Eventhouse KQL e Update Policies)",
        "summary": [
            ("Microsoft Fabric Eventstreams", "Hub centralizado sem código para captura, roteamento e transformação em tempo real de fluxos contínuos de eventos."),
            ("Janelas Tumbling", "Janelas temporais de tamanho fixo e contíguas que nunca se sobrepõem (ex: agregando a cada bloco de 5 minutos)."),
            ("Janelas Sliding", "Janelas temporais deslizantes que avançam continuamente com sobreposição (ex: janela de 5 minutos calculada a cada 1 minuto)."),
            ("Roteamento Multidestino", "Um único Eventstream alimenta simultaneamente o Eventhouse (para alertas instantâneos) e o Lakehouse (para histórico analítico).")
        ]
    },
    "0011": {
        "file": "0011-kql-eventhouse-update-policies-materialized-views.html",
        "ref_link": "../reference/04-three-languages-sql-pyspark-kql-cheatsheet.html",
        "ref_title": "Folha de Referência 04 (KQL e Eventhouse)",
        "next_link": "0012-security-governance-rls-cls-direct-lake-fallback.html",
        "next_title": "0012 (Segurança, Governança e Direct Lake Fallback)",
        "summary": [
            ("Update Policies no KQL", "Gatilhos nativos acionados no momento da ingestão do lote que executam funções de transformação e gravam na tabela agregada sem jobs de ETL."),
            ("Materialized Views", "Tabelas de agregação contínua gerenciadas pelo motor que expõem resultados consolidados sempre atualizados em tempo de consulta."),
            ("Indexação Total no Eventhouse", "Todas as colunas de texto e números são indexadas automaticamente pelo motor Kusto, viabilizando buscas em bilhões de linhas em milissegundos."),
            ("Políticas de Retenção e Caching", "Permitem balancear dados quentes (em cache SSD veloz) e dados frios (arquivados em OneLake) para otimização de custos de CUs.")
        ]
    },
    "0012": {
        "file": "0012-security-governance-rls-cls-direct-lake-fallback.html",
        "ref_link": "../reference/05-security-governance-purview-fallback-guide.html",
        "ref_title": "Folha de Referência 05 (Segurança & Fallback Guide)",
        "next_link": "0013-cicd-git-deployment-pipelines-sqlproj.html",
        "next_title": "0013 (CI/CD, Git e Deployment Pipelines)",
        "summary": [
            ("Row-Level Security (RLS)", "Restringe quais registros um usuário pode visualizar com base em predicados de segurança (ex: região ou filial)."),
            ("Column-Level Security (CLS)", "Oculta ou bloqueia colunas sensíveis (como salários, CPF ou margens de lucro) de usuários não autorizados."),
            ("Direct Lake Fallback", "A presença de RLS ou CLS no SQL Endpoint força o Power BI a cair silenciosamente para o modo DirectQuery T-SQL, aumentando o consumo de CUs."),
            ("Arquitetura Recomendada", "Para preservar a performance de subsegundo do Direct Lake, aplique as regras de RLS no próprio Modelo Semântico do Power BI.")
        ]
    },
    "0013": {
        "file": "0013-cicd-git-deployment-pipelines-sqlproj.html",
        "ref_link": "../reference/05-security-governance-purview-fallback-guide.html",
        "ref_title": "Folha de Referência 05 (Governança e DevOps)",
        "next_link": "0014-performance-vorder-liquid-clustering-tuning.html",
        "next_title": "0014 (Performance, V-Order e Liquid Clustering)",
        "summary": [
            ("Integração Nativa com Git", "Permite sincronizar workspaces do Fabric com branches do Azure DevOps ou GitHub, rastreando alterações de código como código-fonte."),
            ("Deployment Pipelines (3 Estágios)", "Automatiza a promoção controlada de artefatos entre os ambientes de Desenvolvimento (Dev), Teste (Test) e Produção (Prod)."),
            ("Deployment Rules (Regras de Parâmetros)", "Substitui automaticamente variáveis de conexão e nomes de Lakehouses para que o ambiente de teste aponte para dados de teste."),
            ("Projetos SQL (SQL Projects)", "Permitem versionamento declarativo de esquemas do Data Warehouse com compilação e deploy via arquivos .sqlproj e dacpacs.")
        ]
    },
    "0014": {
        "file": "0014-performance-vorder-liquid-clustering-tuning.html",
        "ref_link": "../reference/06-performance-vorder-clustering-monitoring-cheatsheet.html",
        "ref_title": "Folha de Referência 06 (Performance & Tuning Cheatsheet)",
        "next_link": "0015-monitoring-hub-capacity-metrics-troubleshooting.html",
        "next_title": "0015 (Monitoring Hub e Capacity Metrics App)",
        "summary": [
            ("Liquid Clustering (CLUSTER BY)", "Substitui o particionamento Hive e Z-Order. Elimina problemas de arquivos pequenos e permite alterar chaves de agrupamento sem reescrever dados."),
            ("Otimização V-Order", "Ordena internamente os valores dentro de cada Row Group do arquivo Parquet, maximizando o Data Skipping no Power BI Direct Lake."),
            ("Compactação com OPTIMIZE", "Agrupa arquivos minúsculos em blocos ideais de 1GB (Bin-Packing), reduzindo o overhead de metadados em consultas analíticas."),
            ("Limpeza Controlada com VACUUM", "Remove fisicamente do disco arquivos obsoletos após expirar a janela de retenção, liberando espaço sem corromper transações ativas.")
        ]
    },
    "0015": {
        "file": "0015-monitoring-hub-capacity-metrics-troubleshooting.html",
        "ref_link": "../reference/06-performance-vorder-clustering-monitoring-cheatsheet.html",
        "ref_title": "Folha de Referência 06 (Monitoramento e Métricas)",
        "next_link": "../simulados/index.html",
        "next_title": "Simulador Oficial de Exame Pearson VUE DP-700",
        "summary": [
            ("Monitoring Hub do Fabric", "Painel unificado para rastrear o status, tempo de execução e logs de erro de todos os jobs de pipelines, notebooks e dataflows."),
            ("Fabric Capacity Metrics App", "Ferramenta essencial para inspecionar consumo de CUs, picos instantâneos e comportamento da curva de Smoothing de 24 horas."),
            ("Prevenção de Throttling", "Identificar proativamente operações que excedem 100% da capacidade e aplicar otimizações antes que o sistema aplique atrasos ou bloqueios."),
            ("Dynamic Management Views (DMVs)", "Permitem consultar via T-SQL no Warehouse as conexões ativas, consultas em execução e estatísticas de consumo de CPU.")
        ]
    }
}


def extract_quiz_info(content, lesson_num):
    # Encontra seção bloco-quiz
    quiz_sec = re.search(r'<section id=["\']bloco-quiz["\'].*?</section>', content, re.DOTALL)
    if not quiz_sec:
        return None

    sec_text = quiz_sec.group(0)

    # Extrai pergunta
    p_matches = re.findall(r'<p[^>]*>(.*?)</p>', sec_text, re.DOTALL)
    q_text = ""
    for p in p_matches:
        clean = p.strip()
        if len(clean) > 50 and not clean.startswith("Questão elaborada"):
            q_text = clean
            break

    # Extrai opções
    options = []
    opt_matches = re.findall(r'value=["\']([A-D])["\'].*?<span>(.*?)</span>', sec_text, re.DOTALL)
    if opt_matches:
        options = opt_matches
    else:
        # Tenta pegar de quiz-option-btn caso já estivesse parcialmente formatado
        btn_matches = re.findall(r'<button class=["\']quiz-option-btn["\']\s+data-correct=["\'](true|false)["\']>\s*([A-D]\).*?)\s*</button>', sec_text, re.DOTALL)
        if btn_matches:
            options = [(b[1][:1], b[1][3:]) for b in btn_matches]

    # Extrai resposta correta e explicação da função JavaScript
    fn_name = f"checkDP700Quiz{lesson_num}"
    script_match = re.search(rf'function {fn_name}\(\).*?selected\.value === [\'"]([A-D])[\'"].*?feedback\.innerHTML = [\'"]<strong>.*?</strong> (.*?)\";', content, re.DOTALL)

    correct_val = "B"
    explanation = ""

    if script_match:
        correct_val = script_match.group(1)
        explanation = script_match.group(2)
    else:
        # Procura genérico
        gen_match = re.search(r'selected\.value === [\'"]([A-D])[\'"].*?feedback\.innerHTML = [\'"]<strong>.*?</strong> (.*?)\";', content, re.DOTALL)
        if gen_match:
            correct_val = gen_match.group(1)
            explanation = gen_match.group(2)
        else:
            # Pega de data-explanation
            data_exp = re.search(r'data-explanation=["\'](.*?)["\']', sec_text, re.DOTALL)
            if data_exp:
                explanation = data_exp.group(1)

    return {
        "question": q_text,
        "options": options,
        "correct": correct_val,
        "explanation": explanation
    }


def build_standard_quiz_html(meta, quiz_info):
    ref_link = meta["ref_link"]
    ref_title = meta["ref_title"]
    next_link = meta["next_link"]
    next_title = meta["next_title"]
    summary_items = meta["summary"]

    q_text = quiz_info["question"]
    options = quiz_info["options"]
    correct_val = quiz_info["correct"]
    explanation = quiz_info["explanation"].replace('"', '&quot;')

    html = f"""        <section id="bloco-quiz" class="totc-card">
          <h2 style="margin-top: 0;">Pontos Críticos para a Prática e para o Exame DP-700</h2>

          <div class="summary-card">
            <h3 style="margin-top: 0; color: var(--brand-teal);">📝 Síntese dos Pontos Críticos Aprendidos:</h3>
            <ol style="margin-bottom: 0;">
"""
    for title, desc in summary_items:
        html += f"              <li><strong>{title}:</strong> {desc}</li>\n"

    html += f"""            </ol>
          </div>

          <div style="margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid var(--border-color);">
            <h3>🎯 Desafio de Exame DP-700</h3>
            <p>Questão elaborada no padrão da Microsoft com alternativas isomórficas:</p>

            <div class="quiz-card" data-explanation="{explanation}">
              <p><strong style="color: var(--text-primary);">Cenário de Exame DP-700:</strong> {q_text}</p>
              
              <ul class="quiz-options">
"""
    for letter, opt_text in options:
        is_correct = "true" if letter == correct_val else "false"
        clean_text = re.sub(r'^[A-D]\)\s*', '', opt_text.strip())
        html += f"""                <li>
                  <button class="quiz-option-btn" data-correct="{is_correct}">
                    {letter}) {clean_text}
                  </button>
                </li>
"""

    html += f"""              </ul>
              <div class="quiz-feedback"></div>
            </div>
          </div>

          <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 2rem; padding-top: 1.25rem; border-top: 1px solid var(--border-color); flex-wrap: wrap; gap: 1rem;">
            <a href="{ref_link}" style="font-weight: 600;">
              📑 Abrir {ref_title}
            </a>
            <a href="{next_link}" class="audio-btn" style="color: #fff !important;">
              Próxima Lição: {next_title} →
            </a>
          </div>
        </section>"""

    return html


def process_lesson(lesson_num, meta):
    filename = meta["file"]
    filepath = os.path.join(LESSONS_DIR, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    quiz_info = extract_quiz_info(content, lesson_num)
    if not quiz_info or not quiz_info["options"]:
        print(f"❌ Falha ao extrair dados do quiz da lição {lesson_num} ({filename})")
        return False

    new_quiz_html = build_standard_quiz_html(meta, quiz_info)

    # Substitui a seção bloco-quiz
    content = re.sub(r'<section id=["\']bloco-quiz["\'].*?</section>', new_quiz_html, content, flags=re.DOTALL)

    # Remove o footer legado se existir fora do bloco-quiz
    content = re.sub(r'<!-- RODAPÉ DE NAVEGAÇÃO ENTRE LIÇÕES -->\s*<footer.*?>.*?</footer>', '', content, flags=re.DOTALL)

    # Remove a função legada de validação de quiz em JS
    fn_name = f"checkDP700Quiz{lesson_num}"
    content = re.sub(rf'<script>\s*function {fn_name}\(\).*?</script>', '', content, flags=re.DOTALL)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Lição {lesson_num} ({filename}) padronizada com sucesso!")
    return True


def main():
    print("Iniciando padronização de todos os Desafios (bloco-quiz) para o padrão Lição 0001...")
    count = 0
    for num, meta in sorted(LESSON_METADATA.items()):
        if process_lesson(num, meta):
            count += 1
    print(f"\n🎉 Concluído! {count} lições padronizadas com sucesso no layout de excelência.")


if __name__ == "__main__":
    main()


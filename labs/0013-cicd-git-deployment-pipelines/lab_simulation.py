#!/usr/bin/env python3
"""
Laboratório Hands-On: CI/CD, Git Integration e Deployment Pipelines no Microsoft Fabric
Curso Preparatório DP-700: Microsoft Fabric Data Engineer Associate
Simula branches Git, commit de definições PBIP/JSON e regras de implantação em pipelines.
"""

def simulate_cicd_lifecycle():
    print("=" * 80)
    print("LABORATÓRIO: CI/CD, GIT INTEGRATION & DEPLOYMENT PIPELINES (DP-700)")
    print("=" * 80)

    # 1. Estrutura de Branches e Integração Git no Fabric
    print("\n1. [TOPOLOGIA RECOMENDADA DE GIT INTEGRATION NO FABRIC]")
    topology = [
        ("Feature Branch", "Workspace Pessoal do Dev", "Desenvolvimento isolado, testes pontuais de notebooks e pipelines."),
        ("Development (main/dev)", "Workspace Dev Compartilhado", "Sincronizado automaticamente via commit no repositório Azure DevOps/GitHub."),
        ("Test / QA", "Workspace de Homologação", "Promovido via Deployment Pipeline; validação de dados com Zero-Copy Clones."),
        ("Production (prod)", "Workspace de Produção", "Capacidade dedicada (F64+), governança estrita e relatórios corporativos.")
    ]
    for branch, ws, desc in topology:
        print(f"• {branch:<20} | {ws:<26} | {desc}")

    # 2. Definição Declarativa de Itens do Fabric (Fabric Git Items)
    print("\n2. [ANATOMIA DOS ITENS DO FABRIC NO REPOSITÓRIO GIT]")
    print("No Fabric, cada item sincronizado gera uma pasta no Git com arquivos declarativos:")
    print("• Notebook:       'item.metadata.json' + código fonte Python/Spark em formato '.py' ou '.ipynb'.")
    print("• Data Pipeline:  'pipeline-content.json' descrevendo o DAG de atividades e parâmetros.")
    print("• Semantic Model: 'model.bim' / formato PBIP (Power BI Project) em texto legível para diffs.")
    print("• Data Warehouse: '.sqlproj' e arquivos DDL de schemas e tabelas para migrações DACPAC.")

    # 3. Deployment Rules (Regras de Implantação) no Deployment Pipeline
    print("\n3. [DEPLOYMENT RULES: PARAMETRIZAÇÃO ENTRE AMBIENTES]")
    print("Ao promover um item de Desenvolvimento para Teste ou Produção, as")
    print("Deployment Rules substituem automaticamente parâmetros de conexão sem alterar o código:")
    
    rules = [
        ("Regra de Parâmetro", "p_Environment = 'DEV' -> alterado automaticamente para 'PROD'."),
        ("Regra de Fonte de Dados", "SQL Server 'srv-dev.database.windows.net' -> 'srv-prod.database.windows.net'."),
        ("Regra de Workspace", "Atalhos (Shortcuts) remapeados para o Lakehouse de Produção correspondente.")
    ]
    for r_type, example in rules:
        print(f"✅ {r_type:<22} -> {example}")

    print("\n" + "=" * 80)
    print("REGRAS DE OURO PARA O EXAME DP-700:")
    print("1. Git Integration: Conecta workspaces individuais a branches de repositórios")
    print("   no Azure DevOps ou GitHub para controle de versão granular e PRs.")
    print("2. Deployment Pipelines: Gerenciam o ciclo de vida de 3 estágios (Dev -> Test -> Prod),")
    print("   aplicando Deployment Rules para trocar conexões e parâmetros sem alterar o código.")
    print("3. Resolução de Conflitos: Se houver divergência entre o workspace e o branch Git,")
    print("   o Fabric exige sincronizar (Commit to Git ou Update from Git) antes de novas edições.")
    print("=" * 80)

if __name__ == "__main__":
    simulate_cicd_lifecycle()


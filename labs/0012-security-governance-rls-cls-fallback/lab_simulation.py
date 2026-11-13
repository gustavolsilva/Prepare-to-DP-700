#!/usr/bin/env python3
"""
Laboratório Hands-On: Segurança Granular, Governança e Direct Lake Fallback no Fabric
Curso Preparatório DP-700: Microsoft Fabric Data Engineer Associate
Simula regras de RLS, CLS, Dynamic Data Masking e as condições de Fallback do Power BI.
"""

def simulate_security_and_fallback():
    print("=" * 80)
    print("LABORATÓRIO: SEGURANÇA FIM A FIM, RLS/CLS/DDM E DIRECT LAKE FALLBACK (DP-700)")
    print("=" * 80)

    # 1. Matriz de Papéis de Workspace (RBAC)
    print("\n1. [MATRIZ DE PAPEIS DE WORKSPACE NO FABRIC]")
    roles = [
        ("Admin", "Controle total: gerencia usuários, altera capacidade, exclui o workspace e todos os itens."),
        ("Member", "Pode adicionar usuários com papéis Member, Contributor ou Viewer; cria e publica itens."),
        ("Contributor", "Cria, edita e executa pipelines, notebooks e relatórios; NÃO gerencia permissões de workspace."),
        ("Viewer", "Apenas leitura de relatórios e dados servidos; NÃO edita itens nem roda código no workspace.")
    ]
    for role, desc in roles:
        print(f"• Papel: {role:<12} | {desc}")

    # 2. Segurança Granular: RLS, CLS e Dynamic Data Masking (DDM) em T-SQL
    print("\n2. [SEGURANÇA GRANULAR EM T-SQL NO FABRIC DATA WAREHOUSE]")
    security_sql = """
    -- 1. Dynamic Data Masking (DDM) para proteger dados sensíveis
    ALTER TABLE DimCustomer ALTER COLUMN Email ADD MASKED WITH (FUNCTION = 'email()');
    ALTER TABLE DimCustomer ALTER COLUMN Salary ADD MASKED WITH (FUNCTION = 'default()');

    -- 2. Row-Level Security (RLS) via Security Predicate
    CREATE SECURITY POLICY RegionFilterPolicy
    ADD FILTER PREDICATE Security.fn_securitypredicate(RegionCode)
    ON dbo.FactSales
    WITH (STATE = ON);
    """
    print(security_sql.strip())
    print("✅ Os dados físicos no OneLake continuam intactos; o motor Polaris mascara e filtra em tempo de execução.")

    # 3. Condições Críticas de Direct Lake Fallback para o Exame DP-700
    print("\n3. [O PESADELO DO DIRECT LAKE FALLBACK]")
    print("O modo Direct Lake no Power BI carrega arquivos Delta Parquet do OneLake diretamente")
    print("para a memória do VertiPaq. No entanto, certas configurações forçam o Fallback")
    print("automático para o modo DirectQuery tradicional (lento):")
    
    fallback_reasons = [
        ("RLS no SQL Endpoint", "Se RLS for aplicado na tabela Delta via SQL Endpoint, o Direct Lake sofre FALLBACK imediato."),
        ("Tipos de Dados Não Suportados", "Colunas de tipos exóticos ou incompatíveis com o VertiPaq forçam o Fallback."),
        ("Excesso de Memória do VertiPaq", "Se a tabela ultrapassar o limite de memória da F-SKU, ocorre Fallback para DirectQuery."),
        ("Exclusão de Arquivos no OneLake", "Se um VACUUM remover arquivos que o modelo em memória ainda referencia, ocorre Fallback.")
    ]
    for cause, impact in fallback_reasons:
        print(f"⚠️ {cause:<30} -> {impact}")

    print("\n" + "=" * 80)
    print("SOLUÇÃO RECOMENDADA NO EXAME DP-700:")
    print("Para aplicar RLS sem forçar o Fallback do Direct Lake para DirectQuery:")
    print("-> Defina as regras de RLS DIRETAMENTE no Modelo Semântico do Power BI,")
    print("   concedendo permissão 'Read' na tabela do Lakehouse via Fixed Identity!")
    print("=" * 80)

if __name__ == "__main__":
    simulate_security_and_fallback()


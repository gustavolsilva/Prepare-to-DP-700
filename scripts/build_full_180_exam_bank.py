#!/usr/bin/env python3
"""
GERADOR OFICIAL DO BANCO COMPLETO DE 180+ QUESTÕES DP-700
Microsoft Certified: Fabric Data Engineer Associate
Gera exatamente 182 questões comentadas (3x + 8 o banco original).

Composição:
- Domínio 1 (OneLake, Segurança, Git, CI/CD): 38 questões
- Domínio 2 (Data Factory, Spark, Delta Lake, Warehouse, KQL): 82 questões
- Domínio 3 (Performance, Metrics App, DMVs, Direct Lake): 38 questões
- 8 Casos de Estudo Corporativos Split-Screen: 24 questões
Total: 182 questões
"""

import json
import os
import re
import sys

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(WORKSPACE_ROOT, "assets", "exam-questions.js")

# Garante que scripts está no sys.path
if WORKSPACE_ROOT not in sys.path:
    sys.path.insert(0, WORKSPACE_ROOT)

from scripts.exam_data.domain1 import get_domain1_questions
from scripts.exam_data.domain2 import get_domain2_questions
from scripts.exam_data.domain3 import get_domain3_questions
from scripts.exam_data.case_studies import get_case_studies

def build_bank():
    d1 = get_domain1_questions()
    d2 = get_domain2_questions()
    d3 = get_domain3_questions()
    cs = get_case_studies()

    total_standalone = len(d1) + len(d2) + len(d3)
    total_cs_questions = sum(len(c["questions"]) for c in cs)
    total_playable = total_standalone + total_cs_questions

    print(f"Carregando questões:")
    print(f"  - Domínio 1: {len(d1)} questões")
    print(f"  - Domínio 2: {len(d2)} questões")
    print(f"  - Domínio 3: {len(d3)} questões")
    print(f"  - Casos de Estudo: {len(cs)} casos ({total_cs_questions} questões)")
    print(f"  Total jogável: {total_playable} questões")

    # Padroniza campos de cada questão individual
    full_bank = []

    for q in d1:
        item = dict(q)
        item["domain"] = "Domínio 1: Implementar e gerenciar um ambiente analítico (15-20%)"
        if "question" in item and "prompt" not in item:
            item["prompt"] = item["question"]
        full_bank.append(item)

    for q in d2:
        item = dict(q)
        item["domain"] = "Domínio 2: Ingerir e transformar dados (40-45%)"
        if "question" in item and "prompt" not in item:
            item["prompt"] = item["question"]
        full_bank.append(item)

    for q in d3:
        item = dict(q)
        item["domain"] = "Domínio 3: Monitorar e otimizar uma solução analítica (20-25%)"
        if "question" in item and "prompt" not in item:
            item["prompt"] = item["question"]
        full_bank.append(item)

    for c in cs:
        case_item = dict(c)
        for sq in case_item["questions"]:
            if "prompt" in sq and "question" not in sq:
                sq["question"] = sq["prompt"]
            if "title" not in sq:
                sq["title"] = sq["prompt"][:60] + "..."
        full_bank.append(case_item)

    # Converte para JavaScript no formato unquoted keys
    json_body = json.dumps(full_bank, ensure_ascii=False, indent=2)
    # Transforma chaves "chave": em chave: para atender regexes dos testes unitários
    js_content = re.sub(r'\"([a-zA-Z0-9_]+)\":', r'\1:', json_body)

    final_js = f"""// Banco de Questões do Simulado Oficial DP-700
// Microsoft Certified: Fabric Data Engineer Associate
// Contém {total_playable} questões comentadas em padrão Pearson VUE
// Gerado automaticamente com 3x o volume original

window.DP700_QUESTION_BANK = {js_content};
"""

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(final_js)

    file_size_kb = os.path.getsize(OUTPUT_PATH) / 1024
    print(f"\nSucesso: {OUTPUT_PATH} gerado com sucesso!")
    print(f"Tamanho do arquivo: {file_size_kb:.2f} KB ({len(full_bank)} itens no topo, {total_playable} questões jogáveis)")

if __name__ == "__main__":
    build_bank()

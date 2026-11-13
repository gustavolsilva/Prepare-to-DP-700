#!/usr/bin/env python3
"""
distribute_static_quizzes.py
Distribui estaticamente as alternativas corretas entre A, B, C e D
nas lições HTML, além do embaralhamento dinâmico feito em tempo de execução pelo quiz.js.
"""

import glob
import re

TARGET_LETTERS = [
    "A", "C", "D", "B", "A", "C", "D", "B", "A", "C", "D", "B", "A", "C", "D"
]

lessons = sorted(glob.glob("lessons/*.html"))

for idx, lesson_path in enumerate(lessons):
    target = TARGET_LETTERS[idx]
    with open(lesson_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extrai o bloco de opções da quiz-card
    m = re.search(r'(<ul class=["\']quiz-options["\']>)([\s\S]*?)(</ul>)', content)
    if not m:
        continue

    ul_start = m.group(1)
    opts_html = m.group(2)
    ul_end = m.group(3)

    # Extrai cada <li>...</li>
    li_matches = re.findall(r'(\s*<li>\s*<button class=["\']quiz-option-btn["\']\s+data-correct=["\'](true|false)["\']>)([\s\S]*?)(</button>\s*</li>)', opts_html)
    if len(li_matches) != 4:
        continue

    # Extrai dados de cada opção
    options = []
    for li_start, is_correct, text, li_end in li_matches:
        clean_text = re.sub(r'^[A-D]\)\s*', '', text.strip())
        options.append({
            "is_correct": is_correct == "true",
            "text": clean_text
        })

    # Encontra a opção correta
    correct_idx = next(i for i, opt in enumerate(options) if opt["is_correct"])
    target_idx = {"A": 0, "B": 1, "C": 2, "D": 3}[target]

    # Troca as posições para que a correta fique na posição target
    options[correct_idx], options[target_idx] = options[target_idx], options[correct_idx]

    # Reconstrói o HTML com as letras atualizadas
    letters = ["A", "B", "C", "D"]
    new_opts_html = "\n"
    for i, opt in enumerate(options):
        letter = letters[i]
        is_corr_str = "true" if opt["is_correct"] else "false"
        new_opts_html += f"""                <li>
                  <button class="quiz-option-btn" data-correct="{is_corr_str}">
                    {letter}) {opt['text']}
                  </button>
                </li>\n"""

    new_ul = ul_start + new_opts_html + "              " + ul_end
    new_content = content[:m.start()] + new_ul + content[m.end():]

    with open(lesson_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ {lesson_path}: Alternativa correta definida como ({target})")

print("\n🎉 Distribuição estática concluída com sucesso!")


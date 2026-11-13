/**
 * quiz.js - Motor interativo de Quizzes no estilo DP-700 (Compatível com Light e Dark Mode)
 * - Randomização dinâmica das alternativas a cada carregamento de lição
 * - Reatribuição automática das letras sequenciais (A, B, C, D)
 * - Feedback imediato e detalhado com justificativa técnica
 */
document.addEventListener('DOMContentLoaded', () => {
  const quizCards = document.querySelectorAll('.quiz-card');

  quizCards.forEach(card => {
    const optionsList = card.querySelector('.quiz-options');
    
    // 1. Embaralhamento dinâmico das alternativas a cada visita
    if (optionsList) {
      const items = Array.from(optionsList.querySelectorAll('li'));
      
      // Armazena o texto limpo sem a letra anterior (A, B, C, D)
      items.forEach(li => {
        const btn = li.querySelector('.quiz-option-btn');
        if (btn) {
          const rawText = btn.innerHTML.trim();
          btn.dataset.cleanText = rawText.replace(/^[A-D]\)\s*/i, '');
        }
      });

      // Algoritmo Fisher-Yates de embaralhamento uniforme
      for (let i = items.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [items[i], items[j]] = [items[j], items[i]];
      }

      // Reatribui as letras A), B), C), D) na nova ordem aleatória
      const letters = ['A', 'B', 'C', 'D'];
      items.forEach((li, index) => {
        const btn = li.querySelector('.quiz-option-btn');
        if (btn && btn.dataset.cleanText) {
          const letter = letters[index] || '';
          btn.innerHTML = `${letter}) ${btn.dataset.cleanText}`;
        }
        optionsList.appendChild(li);
      });
    }

    // 2. Configuração dos eventos de interação e feedback
    const buttons = card.querySelectorAll('.quiz-option-btn');
    const feedback = card.querySelector('.quiz-feedback');
    const explanation = card.dataset.explanation || '';

    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        buttons.forEach(b => {
          b.disabled = true;
          if (b.dataset.correct === "true") {
            b.classList.add('correct');
          }
        });

        if (btn.dataset.correct === "true") {
          btn.classList.add('correct');
          feedback.style.display = 'block';
          feedback.style.background = 'rgba(34, 197, 94, 0.14)';
          feedback.style.color = 'var(--text-primary)';
          feedback.style.border = '1px solid rgba(34, 197, 94, 0.45)';
          feedback.innerHTML = `<strong style="color: #16a34a;">✅ Correto!</strong> ${explanation}`;
        } else {
          btn.classList.add('incorrect');
          feedback.style.display = 'block';
          feedback.style.background = 'rgba(239, 68, 68, 0.14)';
          feedback.style.color = 'var(--text-primary)';
          feedback.style.border = '1px solid rgba(239, 68, 68, 0.45)';
          feedback.innerHTML = `<strong style="color: #ef4444;">❌ Incorreto.</strong> A alternativa selecionada não atende ao requisito. <br><br><strong>Gabarito e Justificativa:</strong> ${explanation}`;
        }
      });
    });
  });
});

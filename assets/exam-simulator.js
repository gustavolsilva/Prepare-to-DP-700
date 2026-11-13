/**
 * MOTOR DO SIMULADOR OFICIAL DO EXAME DP-700 (PEARSON VUE ARCHITECTURE)
 * Microsoft Certified: Fabric Data Engineer Associate
 * 
 * Funcionalidades Completas:
 * 1. Modo Treino (Feedback explicativo imediato por alternativa com filtros de Domínio)
 * 2. Modo Exame Cronometrado (100 minutos, escala 0-1000, corte 700 pontos)
 * 3. Mapa de Questões (Question Review Matrix com status: respondida, não respondida, marcada)
 * 4. Marcar para Revisão (Flag for Review) idêntico ao Pearson VUE
 * 5. Casos de Uso com tela dividida (Split-Screen) e 4 abas de contexto
 * 6. Relatório de Desempenho por Domínio e Modo de Revisão Pós-Exame
 */

class DP700ExamEngine {
  constructor(questionBank, containerId) {
    this.rawQuestionBank = questionBank;
    this.container = document.getElementById(containerId);
    this.allQuestions = this.flattenQuestions(this.rawQuestionBank);
    
    // Filtros de Treino
    this.filterDomain = "all";
    this.filterType = "all";
    this.flattenedQuestions = this.getFilteredQuestions();
    
    this.currentQuestionIndex = 0;
    this.answers = {}; // qId -> [selectedOptionIds]
    this.flaggedQuestions = new Set(); // qIds marcados para revisão
    
    // Estados do Motor
    this.isExamMode = false;
    this.isReviewMode = false;
    this.isMatrixOpen = false;
    
    // Cronômetro do Exame
    this.timeRemainingSeconds = 100 * 60; // 100 minutos
    this.timerInterval = null;
  }

  flattenQuestions(bank) {
    const list = [];
    bank.forEach((item) => {
      if (item.type === "case_study") {
        item.questions.forEach((q, qIdx) => {
          list.push({
            isCaseStudy: true,
            parentCase: item,
            caseQuestionIndex: qIdx,
            totalCaseQuestions: item.questions.length,
            ...q,
            domain: item.domain || "Estudo de Caso Corporativo"
          });
        });
      } else {
        list.push({
          isCaseStudy: false,
          ...item
        });
      }
    });
    return list;
  }

  getFilteredQuestions() {
    if (this.isExamMode) {
      // No modo exame oficial, utiliza todas as questões do exame
      return [...this.allQuestions];
    }

    return this.allQuestions.filter((q) => {
      // Filtro de Domínio
      let domainMatch = true;
      if (this.filterDomain !== "all") {
        const d = (q.domain || "").toLowerCase();
        if (this.filterDomain === "domain1") {
          domainMatch = d.includes("domínio 1") || d.includes("dominio 1") || d.includes("domain1") || (q.isCaseStudy && (d.includes("contoso") || d.includes("fabrikam") || d.includes("tailwind")));
        } else if (this.filterDomain === "domain2") {
          domainMatch = d.includes("domínio 2") || d.includes("dominio 2") || d.includes("domain2") || (q.isCaseStudy && (d.includes("litware") || d.includes("adventureworks") || d.includes("alpine")));
        } else if (this.filterDomain === "domain3") {
          domainMatch = d.includes("domínio 3") || d.includes("dominio 3") || d.includes("domain3") || (q.isCaseStudy && (d.includes("woodgrove") || d.includes("northwind")));
        } else {
          domainMatch = d.includes(this.filterDomain.toLowerCase());
        }
      }

      // Filtro de Tipo
      let typeMatch = true;
      if (this.filterType === "single") {
        typeMatch = q.type === "single" && !q.isCaseStudy;
      } else if (this.filterType === "multi") {
        typeMatch = q.type === "multi" && !q.isCaseStudy;
      } else if (this.filterType === "case_study") {
        typeMatch = q.isCaseStudy === true;
      }

      return domainMatch && typeMatch;
    });
  }

  init() {
    this.renderQuestion();
  }

  startOfficialExam() {
    this.isExamMode = true;
    this.isReviewMode = false;
    this.flattenedQuestions = [...this.allQuestions];
    this.currentQuestionIndex = 0;
    this.answers = {};
    this.flaggedQuestions.clear();
    this.timeRemainingSeconds = 100 * 60;
    
    if (this.timerInterval) clearInterval(this.timerInterval);
    this.timerInterval = setInterval(() => {
      this.timeRemainingSeconds--;
      this.updateTimerDisplay();
      if (this.timeRemainingSeconds <= 0) {
        clearInterval(this.timerInterval);
        alert("O tempo do exame de 100 minutos expirou! Submetendo respostas...");
        this.submitFinalExam();
      }
    }, 1000);

    this.renderQuestion();
  }

  updateTimerDisplay() {
    const timerEl = document.getElementById("exam-timer-display");
    if (!timerEl) return;
    const mins = Math.floor(this.timeRemainingSeconds / 60);
    const secs = this.timeRemainingSeconds % 60;
    timerEl.innerText = `⏱️ ${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  }

  setDomainFilter(domain) {
    this.filterDomain = domain;
    this.flattenedQuestions = this.getFilteredQuestions();
    this.currentQuestionIndex = 0;
    this.renderQuestion();
  }

  setTypeFilter(type) {
    this.filterType = type;
    this.flattenedQuestions = this.getFilteredQuestions();
    this.currentQuestionIndex = 0;
    this.renderQuestion();
  }

  toggleFlag(qId) {
    if (this.flaggedQuestions.has(qId)) {
      this.flaggedQuestions.delete(qId);
    } else {
      this.flaggedQuestions.add(qId);
    }
    this.renderQuestion();
  }

  openMatrixModal() {
    this.isMatrixOpen = true;
    this.renderQuestion();
  }

  closeMatrixModal() {
    this.isMatrixOpen = false;
    this.renderQuestion();
  }

  jumpToQuestion(index) {
    if (index >= 0 && index < this.flattenedQuestions.length) {
      this.currentQuestionIndex = index;
      this.isMatrixOpen = false;
      this.renderQuestion();
    }
  }

  renderQuestion() {
    if (!this.container) return;
    const q = this.flattenedQuestions[this.currentQuestionIndex];
    if (!q) {
      this.container.innerHTML = `
        <div style="text-align: center; padding: 3rem;">
          <p>Nenhuma questão encontrada para os filtros selecionados.</p>
          <button class="btn-primary" onclick="window.dp700Engine.setDomainFilter('all'); window.dp700Engine.setTypeFilter('all');">Limpar Filtros</button>
        </div>
      `;
      return;
    }

    const answeredCount = Object.keys(this.answers).filter(id => (this.answers[id] || []).length > 0).length;
    const isFlagged = this.flaggedQuestions.has(q.id);

    let html = `
      <!-- BARRA SUPERIOR DO SIMULADOR -->
      <div class="exam-top-bar">
        <div>
          <div style="display: flex; align-items: center; gap: 0.75rem;">
            <span class="exam-mode-badge ${this.isExamMode ? 'badge-official' : (this.isReviewMode ? 'badge-official' : 'badge-study')}">
              ${this.isExamMode ? 'Modo Exame Oficial (Pearson VUE)' : (this.isReviewMode ? 'Revisão Pós-Exame' : 'Modo Treino Comentado')}
            </span>
            <button class="btn-flag ${isFlagged ? 'active' : ''}" onclick="window.dp700Engine.toggleFlag('${q.id}')" title="Marcar para Revisão">
              <span>${isFlagged ? '🚩 Marcada' : '🏳️ Marcar p/ Revisão'}</span>
            </button>
          </div>
          <div style="font-size: 0.88rem; color: var(--text-secondary); margin-top: 0.4rem;">
            Questão <strong>${this.currentQuestionIndex + 1}</strong> de <strong>${this.flattenedQuestions.length}</strong> 
            • Respondidas: <strong>${answeredCount}/${this.flattenedQuestions.length}</strong>
          </div>
        </div>

        <div style="display: flex; align-items: center; gap: 0.75rem;">
          ${this.isExamMode ? '<div id="exam-timer-display" class="exam-timer">⏱️ 100:00</div>' : ''}
          <button class="btn-secondary" style="font-size: 0.85rem; padding: 0.45rem 0.9rem;" onclick="window.dp700Engine.openMatrixModal()">
            📋 Mapa de Questões
          </button>
          ${!this.isReviewMode ? `
            <button class="btn-secondary" style="font-size: 0.85rem; padding: 0.45rem 0.9rem;" onclick="window.dp700Engine.toggleMode()">
              ${this.isExamMode ? 'Sair do Exame' : 'Iniciar Simulado Oficial'}
            </button>
          ` : `
            <button class="btn-primary" style="font-size: 0.85rem; padding: 0.45rem 0.9rem;" onclick="window.dp700Engine.exitReviewMode()">
              Voltar ao Placar
            </button>
          `}
        </div>
      </div>
    `;

    // Filtros de Treino (apenas no modo treino)
    if (!this.isExamMode && !this.isReviewMode) {
      html += `
        <div class="exam-filter-bar">
          <span class="exam-filter-label">🔍 Filtros de Estudo:</span>
          <div>
            <select class="exam-filter-select" onchange="window.dp700Engine.setDomainFilter(this.value)">
              <option value="all" ${this.filterDomain === 'all' ? 'selected' : ''}>Todos os Domínios (Completo)</option>
              <option value="Domínio 1" ${this.filterDomain === 'Domínio 1' ? 'selected' : ''}>Domínio 1: Implementar & Gerenciar (OneLake, Segurança, CI/CD)</option>
              <option value="Domínio 2" ${this.filterDomain === 'Domínio 2' ? 'selected' : ''}>Domínio 2: Ingerir & Transformar (Data Factory, Spark, Warehouse, KQL)</option>
              <option value="Domínio 3" ${this.filterDomain === 'Domínio 3' ? 'selected' : ''}>Domínio 3: Monitorar & Otimizar (V-Order, Smoothing, Direct Lake)</option>
            </select>
          </div>
          <div>
            <select class="exam-filter-select" onchange="window.dp700Engine.setTypeFilter(this.value)">
              <option value="all" ${this.filterType === 'all' ? 'selected' : ''}>Todos os Formatos de Questão</option>
              <option value="single" ${this.filterType === 'single' ? 'selected' : ''}>Escolha Única (Single-Choice)</option>
              <option value="multi" ${this.filterType === 'multi' ? 'selected' : ''}>Múltipla Resposta (Escolha Duas)</option>
              <option value="case_study" ${this.filterType === 'case_study' ? 'selected' : ''}>Estudos de Caso (Split-Screen)</option>
            </select>
          </div>
        </div>
      `;
    }

    if (q.isCaseStudy) {
      html += this.renderCaseStudyQuestion(q);
    } else {
      html += this.renderStandardQuestion(q);
    }

    // Modal Mapa de Questões (se aberto)
    if (this.isMatrixOpen) {
      html += this.renderMatrixModal();
    }

    this.container.innerHTML = html;
    this.updateTimerDisplay();

    // Se estiver em modo de revisão, exibe feedback automático
    if (this.isReviewMode) {
      this.displayReviewFeedback(q);
    }
  }

  renderCaseStudyQuestion(q) {
    const parentCase = q.parentCase;
    const tabsHtml = parentCase.tabs.map((tab, idx) => `
      <button class="scenario-tab-btn ${idx === 0 ? 'active' : ''}" onclick="window.dp700Engine.switchScenarioTab(this, '${tab.id}')">
        ${tab.title}
      </button>
    `).join('');

    const tabsContentHtml = parentCase.tabs.map((tab, idx) => `
      <div id="tab-content-${tab.id}" class="scenario-tab-content" style="${idx === 0 ? '' : 'display: none;'}">
        ${tab.content}
      </div>
    `).join('');

    return `
      <div class="case-study-split">
        <!-- PAINEL ESQUERDO: CONTEXTO DO ESTUDO DE CASO -->
        <div class="case-scenario-pane">
          <div class="scenario-tab-bar">
            ${tabsHtml}
          </div>
          ${tabsContentHtml}
        </div>

        <!-- PAINEL DIREITO: QUESTÃO DO CASO DE USO -->
        <div class="case-question-pane">
          <div class="question-header">
            <div>
              <div class="question-title">${parentCase.caseTitle}</div>
              <div class="question-domain">${q.domain} • Questão ${q.caseQuestionIndex + 1} de ${q.totalCaseQuestions}</div>
            </div>
            <span class="vark-badge badge-k">Estudo de Caso</span>
          </div>

          <div class="question-prompt">
            ${q.prompt}
          </div>

          <div class="question-options-list">
            ${this.renderOptions(q)}
          </div>

          ${this.renderFeedbackBlock(q)}

          <div class="exam-nav-footer">
            <button class="btn-secondary" ${this.currentQuestionIndex === 0 ? 'disabled' : ''} onclick="window.dp700Engine.prevQuestion()">
              ← Anterior
            </button>
            ${!this.isExamMode && !this.isReviewMode ? `<button class="btn-primary" onclick="window.dp700Engine.checkAnswer()">Verificar Resposta</button>` : ''}
            ${this.currentQuestionIndex < this.flattenedQuestions.length - 1 
              ? `<button class="btn-primary" onclick="window.dp700Engine.nextQuestion()">Próxima →</button>`
              : (this.isReviewMode ? `<button class="btn-primary" onclick="window.dp700Engine.exitReviewMode()">Voltar ao Placar</button>` : `<button class="btn-primary" style="background: var(--brand-coral);" onclick="window.dp700Engine.confirmSubmitFinalExam()">Finalizar Exame</button>`)
            }
          </div>
        </div>
      </div>
    `;
  }

  renderStandardQuestion(q) {
    return `
      <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 16px; padding: 2rem; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
        <div class="question-header">
          <div>
            <div class="question-domain">${q.domain}</div>
            <div class="question-title">${q.title || (q.type === 'multi' ? 'Múltipla Resposta (Escolha DUAS alternativas)' : 'Múltipla Escolha (1 alternativa correta)')}</div>
          </div>
          <span class="vark-badge ${q.type === 'multi' ? 'badge-orange' : 'badge-teal'}">
            ${q.type === 'multi' ? '2 Corretas' : '1 Correta'}
          </span>
        </div>

        <div class="question-prompt">
          ${q.prompt || q.question}
        </div>

        <div class="question-options-list">
          ${this.renderOptions(q)}
        </div>

        ${this.renderFeedbackBlock(q)}

        <div class="exam-nav-footer">
          <button class="btn-secondary" ${this.currentQuestionIndex === 0 ? 'disabled' : ''} onclick="window.dp700Engine.prevQuestion()">
            ← Anterior
          </button>
          ${!this.isExamMode && !this.isReviewMode ? `<button class="btn-primary" onclick="window.dp700Engine.checkAnswer()">Verificar Resposta</button>` : ''}
          ${this.currentQuestionIndex < this.flattenedQuestions.length - 1 
            ? `<button class="btn-primary" onclick="window.dp700Engine.nextQuestion()">Próxima →</button>`
            : (this.isReviewMode ? `<button class="btn-primary" onclick="window.dp700Engine.exitReviewMode()">Voltar ao Placar</button>` : `<button class="btn-primary" style="background: var(--brand-coral);" onclick="window.dp700Engine.confirmSubmitFinalExam()">Finalizar Exame</button>`)
          }
        </div>
      </div>
    `;
  }

  renderOptions(q) {
    const isMulti = q.type === "multi";
    const saved = this.answers[q.id] || [];
    const inputType = isMulti ? "checkbox" : "radio";

    return q.options.map((opt) => {
      const isChecked = saved.includes(opt.id);
      let reviewClass = "";
      if (this.isReviewMode) {
        if (opt.isCorrect) reviewClass = "style='border-color: #10b981; background: rgba(16, 185, 129, 0.1);'";
        else if (isChecked && !opt.isCorrect) reviewClass = "style='border-color: #ef4444; background: rgba(239, 68, 68, 0.1);'";
      }

      return `
        <label class="exam-option-card ${isChecked ? 'selected' : ''}" ${reviewClass} onclick="window.dp700Engine.onOptionSelect('${q.id}', '${opt.id}', ${isMulti}, this)">
          <input type="${inputType}" name="opt_${q.id}" value="${opt.id}" ${isChecked ? 'checked' : ''} ${this.isReviewMode ? 'disabled' : ''}>
          <div style="flex: 1;">
            <strong>${opt.id})</strong> ${opt.text}
            ${this.isReviewMode && opt.isCorrect ? '<span style="color: #059669; font-weight: bold; margin-left: 0.5rem;">[Correta Oficial]</span>' : ''}
            ${this.isReviewMode && isChecked && !opt.isCorrect ? '<span style="color: #dc2626; font-weight: bold; margin-left: 0.5rem;">[Sua Escolha Incorreta]</span>' : ''}
          </div>
        </label>
      `;
    }).join('');
  }

  renderFeedbackBlock(q) {
    return `
      <div id="feedback-box-${q.id}" class="quiz-feedback-box" style="display: none; margin-bottom: 1.5rem;"></div>
    `;
  }

  renderMatrixModal() {
    const cellsHtml = this.flattenedQuestions.map((q, idx) => {
      const isCurrent = idx === this.currentQuestionIndex;
      const isAnswered = (this.answers[q.id] || []).length > 0;
      const isFlagged = this.flaggedQuestions.has(q.id);

      let statusClass = "";
      if (this.isReviewMode) {
        const userSelected = this.answers[q.id] || [];
        const correctIds = q.options.filter(o => o.isCorrect).map(o => o.id);
        const isCorrect = correctIds.length === userSelected.length && correctIds.every(id => userSelected.includes(id));
        statusClass = isCorrect ? "cell-correct" : "cell-wrong";
      } else {
        if (isAnswered) statusClass = "cell-answered";
      }
      if (isCurrent) statusClass += " cell-current";
      if (isFlagged) statusClass += " cell-flagged";

      return `
        <button class="matrix-cell ${statusClass}" onclick="window.dp700Engine.jumpToQuestion(${idx})" title="Questão ${idx + 1} (${q.type})">
          ${idx + 1}
        </button>
      `;
    }).join('');

    return `
      <div class="matrix-modal-backdrop" onclick="if(event.target === this) window.dp700Engine.closeMatrixModal()">
        <div class="matrix-modal-box">
          <div class="matrix-modal-header">
            <h3>📋 Mapa de Questões do Exame DP-700</h3>
            <button class="btn-secondary" style="padding: 0.2rem 0.6rem;" onclick="window.dp700Engine.closeMatrixModal()">✕</button>
          </div>
          <div class="matrix-modal-body">
            <div class="matrix-legend">
              <div class="legend-item"><span class="legend-badge" style="background: var(--badge-teal-bg); border: 1.5px solid var(--brand-teal);"></span> Respondida</div>
              <div class="legend-item"><span class="legend-badge" style="background: var(--bg-surface); border: 1.5px solid var(--border-color);"></span> Não Respondida</div>
              <div class="legend-item"><span class="legend-badge" style="border: 2px solid var(--brand-teal);"></span> Questão Atual</div>
              <div class="legend-item"><span>🚩</span> Marcada para Revisão</div>
            </div>
            <div class="matrix-grid">
              ${cellsHtml}
            </div>
          </div>
        </div>
      </div>
    `;
  }

  onOptionSelect(qId, optId, isMulti, cardEl) {
    if (this.isReviewMode) return; // Não permite edição durante a revisão pós-exame

    if (!this.answers[qId]) {
      this.answers[qId] = [];
    }

    if (isMulti) {
      const idx = this.answers[qId].indexOf(optId);
      if (idx > -1) {
        this.answers[qId].splice(idx, 1);
        cardEl.classList.remove('selected');
        const input = cardEl.querySelector('input');
        if (input) input.checked = false;
      } else {
        if (this.answers[qId].length >= 2) {
          alert("Esta questão de Múltipla Resposta permite exatamente DUAS alternativas. Desmarque uma para escolher outra.");
          return;
        }
        this.answers[qId].push(optId);
        cardEl.classList.add('selected');
        const input = cardEl.querySelector('input');
        if (input) input.checked = true;
      }
    } else {
      this.answers[qId] = [optId];
      const siblings = cardEl.parentElement.querySelectorAll('.exam-option-card');
      siblings.forEach(s => s.classList.remove('selected'));
      cardEl.classList.add('selected');
      const input = cardEl.querySelector('input');
      if (input) input.checked = true;
    }
  }

  switchScenarioTab(btnEl, tabId) {
    const container = btnEl.closest('.case-scenario-pane');
    container.querySelectorAll('.scenario-tab-btn').forEach(b => b.classList.remove('active'));
    container.querySelectorAll('.scenario-tab-content').forEach(c => c.style.display = 'none');

    btnEl.classList.add('active');
    const targetContent = container.querySelector(`#tab-content-${tabId}`);
    if (targetContent) targetContent.style.display = 'block';
  }

  checkAnswer() {
    const q = this.flattenedQuestions[this.currentQuestionIndex];
    const userSelected = this.answers[q.id] || [];
    const feedbackEl = document.getElementById(`feedback-box-${q.id}`);
    if (!feedbackEl) return;

    if (userSelected.length === 0) {
      alert("Por favor, selecione ao menos uma resposta antes de verificar.");
      return;
    }

    if (q.type === 'multi' && userSelected.length !== 2) {
      alert("Esta questão exige a seleção de exatamente DUAS alternativas.");
      return;
    }

    const correctIds = q.options.filter(o => o.isCorrect).map(o => o.id);
    const isAllCorrect = correctIds.length === userSelected.length && correctIds.every(id => userSelected.includes(id));

    feedbackEl.style.display = 'block';
    if (isAllCorrect) {
      feedbackEl.className = 'quiz-feedback-box feedback-correct';
      feedbackEl.innerHTML = `
        <div style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.75rem; color: #047857;">
          ✅ Parabéns! Resposta Correta (${correctIds.join(', ')})
        </div>
        ${q.explanation}
      `;
    } else {
      feedbackEl.className = 'quiz-feedback-box feedback-incorrect';
      feedbackEl.innerHTML = `
        <div style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.75rem; color: #b91c1c;">
          ❌ Resposta Incorreta. A(s) alternativa(s) correta(s) é/são: <strong>${correctIds.join(', ')}</strong>.
        </div>
        ${q.explanation}
      `;
    }
  }

  displayReviewFeedback(q) {
    const userSelected = this.answers[q.id] || [];
    const feedbackEl = document.getElementById(`feedback-box-${q.id}`);
    if (!feedbackEl) return;

    const correctIds = q.options.filter(o => o.isCorrect).map(o => o.id);
    const isAllCorrect = correctIds.length === userSelected.length && correctIds.every(id => userSelected.includes(id));

    feedbackEl.style.display = 'block';
    feedbackEl.className = isAllCorrect ? 'quiz-feedback-box feedback-correct' : 'quiz-feedback-box feedback-incorrect';
    feedbackEl.innerHTML = `
      <div style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.75rem; color: ${isAllCorrect ? '#047857' : '#b91c1c'};">
        ${isAllCorrect ? `✅ Você ACERTOU esta questão (${correctIds.join(', ')})!` : `❌ Você ERROU esta questão. Alternativa(s) correta(s): ${correctIds.join(', ')}.`}
      </div>
      ${q.explanation}
    `;
  }

  nextQuestion() {
    if (this.currentQuestionIndex < this.flattenedQuestions.length - 1) {
      this.currentQuestionIndex++;
      this.renderQuestion();
    }
  }

  prevQuestion() {
    if (this.currentQuestionIndex > 0) {
      this.currentQuestionIndex--;
      this.renderQuestion();
    }
  }

  toggleMode() {
    if (this.isExamMode) {
      if (confirm("Deseja cancelar o modo oficial cronometrado e retornar ao modo treino?")) {
        this.isExamMode = false;
        if (this.timerInterval) clearInterval(this.timerInterval);
        this.flattenedQuestions = this.getFilteredQuestions();
        this.currentQuestionIndex = 0;
        this.renderQuestion();
      }
    } else {
      if (confirm("Iniciar o Simulado Oficial DP-700? O cronômetro de 100 minutos será iniciado e as explicações só serão exibidas após o envio.")) {
        this.startOfficialExam();
      }
    }
  }

  confirmSubmitFinalExam() {
    const total = this.flattenedQuestions.length;
    const answeredCount = Object.keys(this.answers).filter(id => (this.answers[id] || []).length > 0).length;
    const unanswered = total - answeredCount;
    const flaggedCount = this.flaggedQuestions.size;

    let msg = `Tem certeza que deseja finalizar o exame?\n\n`;
    msg += `• Total de Questões: ${total}\n`;
    msg += `• Respondidas: ${answeredCount}\n`;
    msg += `• Não Respondidas: ${unanswered}\n`;
    msg += `• Marcadas para Revisão: ${flaggedCount}\n\n`;
    msg += `Após a finalização, sua nota oficial (escala 0-1000) será calculada.`;

    if (confirm(msg)) {
      this.submitFinalExam();
    }
  }

  submitFinalExam() {
    if (this.timerInterval) clearInterval(this.timerInterval);

    let totalPoints = 0;
    const maxPoints = 1000;
    const pointsPerQuestion = maxPoints / this.flattenedQuestions.length;
    let correctCount = 0;

    // Métricas por Domínio
    const domainStats = {
      "Domínio 1": { total: 0, correct: 0, label: "Domínio 1: Implementar & Gerenciar (OneLake, Segurança, CI/CD)" },
      "Domínio 2": { total: 0, correct: 0, label: "Domínio 2: Ingerir & Transformar (Data Factory, Spark, Warehouse, KQL)" },
      "Domínio 3": { total: 0, correct: 0, label: "Domínio 3: Monitorar & Otimizar (V-Order, Smoothing, Direct Lake)" }
    };

    this.flattenedQuestions.forEach(q => {
      const userSelected = this.answers[q.id] || [];
      const correctIds = q.options.filter(o => o.isCorrect).map(o => o.id);
      const isCorrect = correctIds.length === userSelected.length && correctIds.every(id => userSelected.includes(id));
      
      if (isCorrect) {
        correctCount++;
        totalPoints += pointsPerQuestion;
      }

      // Identifica o domínio
      let domKey = "Domínio 2";
      if (q.domain.includes("Domínio 1") || q.domain.includes("Contoso") || q.domain.includes("Fabrikam") || q.domain.includes("Tailwind")) domKey = "Domínio 1";
      else if (q.domain.includes("Domínio 3") || q.domain.includes("Woodgrove") || q.domain.includes("Northwind")) domKey = "Domínio 3";

      if (domainStats[domKey]) {
        domainStats[domKey].total++;
        if (isCorrect) domainStats[domKey].correct++;
      }
    });

    const scaledScore = Math.round(totalPoints);
    const isPassed = scaledScore >= 700;

    const domainCardsHtml = Object.keys(domainStats).map(key => {
      const s = domainStats[key];
      const pct = s.total > 0 ? Math.round((s.correct / s.total) * 100) : 0;
      const barColor = pct >= 70 ? "#10b981" : (pct >= 50 ? "#f59e0b" : "#ef4444");

      return `
        <div class="domain-card">
          <div class="domain-card-header">
            <span>${s.label}</span>
            <span>${pct}% (${s.correct}/${s.total})</span>
          </div>
          <div class="domain-progress-bar">
            <div class="domain-progress-fill" style="width: ${pct}%; background: ${barColor};"></div>
          </div>
        </div>
      `;
    }).join('');

    this.container.innerHTML = `
      <div class="exam-score-banner">
        <h2 style="font-family: var(--font-display); margin-top: 0;">Resultado Oficial da Avaliação DP-700</h2>
        <div class="score-number ${isPassed ? 'score-pass' : 'score-fail'}">
          ${scaledScore} / 1000
        </div>
        <div style="font-size: 1.35rem; font-weight: 700; color: ${isPassed ? '#2e7d32' : '#d32f2f'}; margin-bottom: 0.5rem;">
          ${isPassed ? '🎉 APROVADO! Parabéns, você atingiu o índice oficial da Microsoft.' : '⚠️ NÃO APROVADO. A pontuação mínima é de 700 pontos.'}
        </div>
        <p style="color: var(--text-secondary); max-width: 650px; margin: 0 auto 1.5rem auto;">
          Você acertou <strong>${correctCount}</strong> de <strong>${this.flattenedQuestions.length}</strong> questões avaliadas no exame.
        </p>

        <!-- Detalhamento por Domínio Oficial -->
        <div class="domain-breakdown-container">
          <div style="font-size: 0.95rem; font-weight: 700; color: var(--text-secondary); text-transform: uppercase; margin-bottom: 0.25rem;">
            Desempenho por Domínio Oficial da Certificação:
          </div>
          ${domainCardsHtml}
        </div>

        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <button class="btn-primary" onclick="window.dp700Engine.enterReviewMode()">🔍 Revisar Todas as Questões com Comentários</button>
          <button class="btn-secondary" onclick="window.dp700Engine.startOfficialExam()">Refazer Simulado Cronometrado</button>
          <button class="btn-secondary" onclick="window.dp700Engine.exitReviewModeToStudy()">Ir para Modo Treino</button>
          <a href="../index.html?v=totc6" class="btn-secondary">Voltar ao Portal</a>
        </div>
      </div>
    `;
  }

  enterReviewMode() {
    this.isReviewMode = true;
    this.isExamMode = false;
    this.currentQuestionIndex = 0;
    this.renderQuestion();
  }

  exitReviewMode() {
    this.submitFinalExam();
  }

  exitReviewModeToStudy() {
    this.isReviewMode = false;
    this.isExamMode = false;
    this.flattenedQuestions = this.getFilteredQuestions();
    this.currentQuestionIndex = 0;
    this.renderQuestion();
  }
}

// Inicialização Global do Simulador
document.addEventListener("DOMContentLoaded", () => {
  if (window.DP700_QUESTION_BANK && document.getElementById("exam-simulator-mount")) {
    window.dp700Engine = new DP700ExamEngine(window.DP700_QUESTION_BANK, "exam-simulator-mount");
    window.dp700Engine.init();
  }
});

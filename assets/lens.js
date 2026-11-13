/**
 * lens.js - Controle Global de Nível (Lente) & Tema (Light / Dark Mode)
 * - Salva no localStorage para manter a escolha em todas as páginas do curso
 * - Suporta as lentes: unificado, junior, pleno, senior, staff, clevel
 * - Suporta os temas: light (padrão Figma TOTC) e dark (Midnight Edition)
 */

const GLOBAL_LENS_KEY = 'fabric_dp700_global_lens';
const GLOBAL_THEME_KEY = 'fabric_dp700_theme';

function applyThemeToDOM(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  if (document.body) {
    document.body.setAttribute('data-theme', theme);
  }
  try {
    localStorage.setItem(GLOBAL_THEME_KEY, theme);
  } catch (e) {}

  const themeButtons = document.querySelectorAll('.theme-toggle-btn');
  themeButtons.forEach(btn => {
    if (theme === 'dark') {
      btn.innerHTML = '☀️ Modo Light';
      btn.setAttribute('title', 'Alternar para Modo Claro');
    } else {
      btn.innerHTML = '🌙 Modo Dark';
      btn.setAttribute('title', 'Alternar para Modo Escuro');
    }
  });
}

window.toggleAppTheme = function() {
  const current = document.documentElement.getAttribute('data-theme') || 'light';
  const next = current === 'dark' ? 'light' : 'dark';
  applyThemeToDOM(next);
};

// Inicialização imediata antes da pintura
(function initThemeEarly() {
  try {
    const savedTheme = localStorage.getItem(GLOBAL_THEME_KEY) || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
  } catch (e) {}
})();

document.addEventListener('DOMContentLoaded', () => {
  const initialTheme = localStorage.getItem(GLOBAL_THEME_KEY) || 'light';
  applyThemeToDOM(initialTheme);

  // Vincular evento a botões que não tenham onclick inline
  const themeButtons = document.querySelectorAll('.theme-toggle-btn');
  themeButtons.forEach(btn => {
    if (!btn.getAttribute('onclick')) {
      btn.addEventListener('click', () => window.toggleAppTheme());
    }
  });

  // -------------------------------------------------------------------------
  // CONTROLE GLOBAL DE NÍVEL / LENTE (Suporta .lens-btn, .lens-tab, .lens-panel, .lens-text-content)
  // -------------------------------------------------------------------------
  const lensButtons = document.querySelectorAll('.lens-btn, .lens-tab');
  const lensTexts = document.querySelectorAll('.lens-text-content, .lens-panel, [data-lens-content]');

  function setGlobalLens(lens) {
    try {
      localStorage.setItem(GLOBAL_LENS_KEY, lens);
    } catch (e) {}

    lensButtons.forEach(btn => {
      const btnLens = btn.dataset.lens || btn.getAttribute('data-lens');
      btn.classList.toggle('active', btnLens === lens);
    });

    lensTexts.forEach(el => {
      const elLens = el.dataset.lensContent || el.dataset.lens || el.getAttribute('data-lens-content') || el.getAttribute('data-lens');
      if (elLens === lens) {
        el.style.display = 'block';
        el.style.opacity = '1';
      } else {
        el.style.display = 'none';
      }
    });

    const currentLensIndicator = document.getElementById('current-profile-label');
    if (currentLensIndicator) {
      const labels = {
        'unificado': 'Visão Unificada Completa',
        'junior': 'Júnior (Fundamentos do Zero)',
        'pleno': 'Pleno (Implementação Prática & Pipelines)',
        'senior': 'Sênior (DP-700 & Arquitetura Avançada)',
        'staff': 'Staff / Especialista (Sob o Capô & Escala)',
        'clevel': 'C-Level / Head (Estratégia & FinOps)'
      };
      currentLensIndicator.textContent = labels[lens] || lens;
    }
  }

  lensButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetLens = btn.dataset.lens || btn.getAttribute('data-lens');
      if (targetLens) {
        setGlobalLens(targetLens);
      }
    });
  });

  const savedLens = localStorage.getItem(GLOBAL_LENS_KEY) || 'unificado';
  setGlobalLens(savedLens);

  // -------------------------------------------------------------------------
  // CONTROLE REMISSIVO E ADAPTATIVO DA BARRA LATERAL (AUTOHIDE / DRAWER)
  // -------------------------------------------------------------------------
  const GLOBAL_SIDEBAR_KEY = 'fabric_dp700_sidebar_collapsed';
  const shell = document.querySelector('.course-app-shell');
  const sidebar = document.querySelector('.course-sidebar');

  if (shell && sidebar) {
    // 1. Cria ou reutiliza o backdrop escuro para mobile
    let backdrop = document.querySelector('.sidebar-backdrop');
    if (!backdrop) {
      backdrop = document.createElement('div');
      backdrop.className = 'sidebar-backdrop';
      backdrop.setAttribute('aria-hidden', 'true');
      shell.appendChild(backdrop);
    }

    // 2. Cria botão de fechar dentro do topo da sidebar se não existir
    const sidebarTopNav = sidebar.querySelector('.sidebar-top-nav');
    if (sidebarTopNav && !sidebarTopNav.querySelector('.sidebar-close-btn')) {
      const closeBtn = document.createElement('button');
      closeBtn.className = 'sidebar-close-btn';
      closeBtn.type = 'button';
      closeBtn.setAttribute('title', 'Recolher Sumário (Foco na Leitura)');
      closeBtn.innerHTML = '◀';
      closeBtn.addEventListener('click', () => window.toggleCourseSidebar(false));
      sidebarTopNav.appendChild(closeBtn);
    }

    // 3. Insere botão de sumário no banner superior de cada lição
    const headerBanner = document.querySelector('.course-header-banner');
    if (headerBanner) {
      let actionsGroup = headerBanner.querySelector('.header-actions-group');
      if (!actionsGroup) {
        actionsGroup = document.createElement('div');
        actionsGroup.className = 'header-actions-group';
        headerBanner.appendChild(actionsGroup);
      }
      
      const existingThemeContainer = headerBanner.querySelector('.theme-toggle-container');
      if (existingThemeContainer && existingThemeContainer.parentElement !== actionsGroup) {
        actionsGroup.appendChild(existingThemeContainer);
      }

      if (!actionsGroup.querySelector('.sidebar-toggle-btn')) {
        const toggleBtn = document.createElement('button');
        toggleBtn.className = 'sidebar-toggle-btn';
        toggleBtn.type = 'button';
        toggleBtn.innerHTML = '☰ Sumário da Lição';
        toggleBtn.setAttribute('title', 'Alternar Exibição do Sumário');
        toggleBtn.addEventListener('click', () => window.toggleCourseSidebar());
        actionsGroup.prepend(toggleBtn);
      }
    }

    // 4. Cria botão flutuante discreto no canto inferior esquerdo para reabrir enquanto rola
    if (!document.querySelector('.floating-sidebar-toggle')) {
      const floatingBtn = document.createElement('button');
      floatingBtn.className = 'floating-sidebar-toggle';
      floatingBtn.type = 'button';
      floatingBtn.innerHTML = '☰ Sumário';
      floatingBtn.setAttribute('title', 'Abrir Sumário da Lição');
      floatingBtn.addEventListener('click', () => window.toggleCourseSidebar(true));
      document.body.appendChild(floatingBtn);
    }

    // 5. Função de Toggle Global
    window.toggleCourseSidebar = function(forceOpen) {
      const isMobile = window.innerWidth <= 1150;
      if (isMobile) {
        if (typeof forceOpen === 'boolean') {
          shell.classList.toggle('sidebar-open', forceOpen);
        } else {
          shell.classList.toggle('sidebar-open');
        }
      } else {
        if (typeof forceOpen === 'boolean') {
          shell.classList.toggle('sidebar-collapsed', !forceOpen);
        } else {
          shell.classList.toggle('sidebar-collapsed');
        }
        const isCollapsed = shell.classList.contains('sidebar-collapsed');
        try {
          localStorage.setItem(GLOBAL_SIDEBAR_KEY, isCollapsed ? 'true' : 'false');
        } catch (e) {}
      }
      syncSidebarButtonLabels();
    };

    function syncSidebarButtonLabels() {
      const isMobile = window.innerWidth <= 1150;
      const isOpen = isMobile 
        ? shell.classList.contains('sidebar-open') 
        : !shell.classList.contains('sidebar-collapsed');

      document.querySelectorAll('.sidebar-toggle-btn').forEach(btn => {
        btn.innerHTML = isOpen ? '◀ Ocultar Sumário' : '☰ Sumário da Lição';
      });
    }

    // Fecha ao clicar no backdrop (mobile)
    backdrop.addEventListener('click', () => window.toggleCourseSidebar(false));

    // Fecha ao pressionar ESC
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        window.toggleCourseSidebar(false);
      }
    });

    // Fecha automaticamente no mobile ao clicar em qualquer pílula de navegação da lição
    sidebar.querySelectorAll('.curriculum-pill').forEach(pill => {
      pill.addEventListener('click', () => {
        if (window.innerWidth <= 1150) {
          window.toggleCourseSidebar(false);
        }
      });
    });

    // Inicialização da preferência do usuário no desktop
    if (window.innerWidth > 1150) {
      const savedCollapsed = localStorage.getItem(GLOBAL_SIDEBAR_KEY);
      if (savedCollapsed === 'true') {
        shell.classList.add('sidebar-collapsed');
      }
    }
    syncSidebarButtonLabels();
  }
});

/**
 * vark.js - Suporte Interativo VARK com Player de Áudio Nativo HTML5 (MP3)
 * - Visual: Hotspots interativos no SVG com detalhes contextuais
 * - Aural: Player de Áudio MP3 em Português nativo e profissional (com barra de progresso e controles padrão)
 * - Kinesthetic: Simulador dinâmico de Capacity Units e Smoothing em tempo real
 */

document.addEventListener('DOMContentLoaded', () => {
  // -------------------------------------------------------------------------
  // 1. AURAL (AUDITIVO): Player de Áudio HTML5 Nativo e Controles Modernos
  // -------------------------------------------------------------------------
  // Suporte para a versão moderna (Lições 0002-0015)
  const varkAudio = document.getElementById('vark-audio-element');
  const varkPlayBtn = document.getElementById('audio-play-btn');
  const varkProgressBar = document.getElementById('audio-progress-bar');
  const varkTimeLabel = document.getElementById('audio-time-label');

  function formatTime(seconds) {
    if (isNaN(seconds) || seconds < 0) return "00:00";
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  }

  if (varkAudio && varkPlayBtn) {
    varkPlayBtn.addEventListener('click', () => {
      if (varkAudio.paused) {
        varkAudio.play();
        varkPlayBtn.textContent = '⏸ Pausar Aula';
        varkPlayBtn.classList.add('playing');
      } else {
        varkAudio.pause();
        varkPlayBtn.textContent = '▶ Reproduzir Aula';
        varkPlayBtn.classList.remove('playing');
      }
    });

    varkAudio.addEventListener('timeupdate', () => {
      if (varkProgressBar && varkAudio.duration) {
        const pct = (varkAudio.currentTime / varkAudio.duration) * 100;
        varkProgressBar.style.width = `${pct}%`;
      }
      if (varkTimeLabel && varkAudio.duration) {
        varkTimeLabel.textContent = `${formatTime(varkAudio.currentTime)} / ${formatTime(varkAudio.duration)}`;
      }
    });

    varkAudio.addEventListener('ended', () => {
      varkPlayBtn.textContent = '▶ Reproduzir Novamente';
      varkPlayBtn.classList.remove('playing');
      if (varkProgressBar) varkProgressBar.style.width = '0%';
    });

    // Permite clicar na barra de progresso para avançar ou retroceder
    const scrubberTrack = document.querySelector('.audio-scrubber-track');
    if (scrubberTrack) {
      scrubberTrack.addEventListener('click', (e) => {
        const rect = scrubberTrack.getBoundingClientRect();
        const clickPos = (e.clientX - rect.left) / rect.width;
        if (varkAudio.duration) {
          varkAudio.currentTime = clickPos * varkAudio.duration;
        }
      });
    }
  }

  // Suporte legado para Lição 0001
  const audioPlayer = document.getElementById('lesson-audio-player');
  const customPlayBtn = document.getElementById('btn-custom-play');
  const audioStatus = document.getElementById('audio-playback-status');

  if (audioPlayer && customPlayBtn) {
    customPlayBtn.addEventListener('click', () => {
      if (audioPlayer.paused) {
        audioPlayer.play().then(() => {
          customPlayBtn.innerHTML = '⏸️ Pausar Áudio';
          if (audioStatus) audioStatus.textContent = '🔊 Reproduzindo narração da lição em português...';
        }).catch(err => {
          if (audioStatus) audioStatus.textContent = `Erro ao reproduzir: ${err.message}`;
        });
      } else {
        audioPlayer.pause();
        customPlayBtn.innerHTML = '▶️ Reproduzir Áudio';
        if (audioStatus) audioStatus.textContent = 'Áudio pausado.';
      }
    });

    audioPlayer.addEventListener('ended', () => {
      customPlayBtn.innerHTML = '▶️ Reproduzir Novamente';
      if (audioStatus) audioStatus.textContent = '✅ Áudio concluído com sucesso.';
    });

    audioPlayer.addEventListener('play', () => {
      customPlayBtn.innerHTML = '⏸️ Pausar Áudio';
    });

    audioPlayer.addEventListener('pause', () => {
      customPlayBtn.innerHTML = '▶️ Reproduzir Áudio';
    });
  }

  // -------------------------------------------------------------------------
  // 2. KINESTHETIC: Simulador Dinâmico de Capacidade & Smoothing
  // -------------------------------------------------------------------------
  const skuSelect = document.getElementById('sim-sku-select');
  const durationSlider = document.getElementById('sim-duration-slider');
  const intensitySlider = document.getElementById('sim-intensity-slider');

  const durationValDisplay = document.getElementById('sim-duration-val');
  const intensityValDisplay = document.getElementById('sim-intensity-val');

  const metricPeakCu = document.getElementById('metric-peak-cu');
  const metricTotalCuSec = document.getElementById('metric-total-cu-sec');
  const metricSmoothedCu = document.getElementById('metric-smoothed-cu');
  const metricCapPercent = document.getElementById('metric-cap-percent');
  const simVerdict = document.getElementById('sim-verdict');
  const gaugeFill = document.getElementById('sim-gauge-fill');

  function updateSimulation() {
    if (!skuSelect || !durationSlider || !intensitySlider) return;

    const baseCu = parseInt(skuSelect.value, 10);
    const durationMinutes = parseInt(durationSlider.value, 10);
    const durationSeconds = durationMinutes * 60;
    const peakCuMultiplier = parseFloat(intensitySlider.value);
    const peakCuInstant = Math.round(baseCu * peakCuMultiplier);

    if (durationValDisplay) durationValDisplay.textContent = `${durationMinutes} min (${durationSeconds}s)`;
    if (intensityValDisplay) intensityValDisplay.textContent = `${peakCuInstant} CUs (${peakCuMultiplier}x)`;

    const totalCuSeconds = durationSeconds * peakCuInstant;
    const smoothingWindow = 86400; // Janela móvel de 24h
    const smoothedCuPerSec = totalCuSeconds / smoothingWindow;
    const capacityPercent = (smoothedCuPerSec / baseCu) * 100;

    if (metricPeakCu) metricPeakCu.textContent = `${peakCuInstant} CUs`;
    if (metricTotalCuSec) metricTotalCuSec.textContent = totalCuSeconds.toLocaleString('pt-BR');
    if (metricSmoothedCu) metricSmoothedCu.textContent = `${smoothedCuPerSec.toFixed(2)} CU/s`;
    if (metricCapPercent) metricCapPercent.textContent = `${capacityPercent.toFixed(1)}%`;

    if (gaugeFill) {
      const clampedPercent = Math.min(capacityPercent, 100);
      gaugeFill.setAttribute('width', `${clampedPercent * 4.5}`);
      if (capacityPercent <= 40) gaugeFill.setAttribute('fill', '#22c55e');
      else if (capacityPercent <= 85) gaugeFill.setAttribute('fill', '#eab308');
      else gaugeFill.setAttribute('fill', '#ef4444');
    }

    if (simVerdict) {
      simVerdict.className = 'sim-verdict-box';
      if (capacityPercent < 35) {
        simVerdict.classList.add('ok');
        simVerdict.innerHTML = `✅ <strong>Operação Suavizada (Sem Throttling):</strong> O pico foi amortizado na janela de 24h consumindo apenas ${capacityPercent.toFixed(1)}% da capacidade média.`;
      } else if (capacityPercent <= 85) {
        simVerdict.classList.add('warning');
        simVerdict.innerHTML = `⚠️ <strong>Atenção de FinOps:</strong> O job compromete ${capacityPercent.toFixed(1)}% do orçamento diário. Picos concomitantes podem forçar a capacidade ao limite.`;
      } else {
        simVerdict.classList.add('danger');
        simVerdict.innerHTML = `🚨 <strong>Risco de Throttling Imediato:</strong> Este job consome ${capacityPercent.toFixed(1)}% do orçamento diário! O Fabric aplicará atraso interativo de 60 segundos e rejeição de novos jobs!`;
      }
    }
  }

  if (skuSelect && durationSlider && intensitySlider) {
    skuSelect.addEventListener('change', updateSimulation);
    durationSlider.addEventListener('input', updateSimulation);
    intensitySlider.addEventListener('input', updateSimulation);
    updateSimulation();
  }

  // -------------------------------------------------------------------------
  // 3. VISUAL INTERATIVO: Hotspots no Diagrama SVG
  // -------------------------------------------------------------------------
  const diagramCards = document.querySelectorAll('.interactive-hotspot');
  const visualInfoBox = document.getElementById('hotspot-details-box');

  diagramCards.forEach(hotspot => {
    const rect = hotspot.querySelector('rect');
    if (rect && !rect.dataset.origStroke) {
      rect.dataset.origStroke = rect.getAttribute('stroke') || '#49BBBD';
    }

    hotspot.addEventListener('click', () => {
      diagramCards.forEach(h => {
        const r = h.querySelector('rect');
        if (r && r.dataset.origStroke) {
          r.style.stroke = r.dataset.origStroke;
          r.style.strokeWidth = r.getAttribute('stroke-width') || '1.5px';
        }
      });
      const currentRect = hotspot.querySelector('rect');
      if (currentRect) {
        currentRect.style.stroke = '#F59E0B';
        currentRect.style.strokeWidth = '3px';
      }

      if (visualInfoBox && hotspot.dataset.title) {
        visualInfoBox.innerHTML = `
          <strong>🔍 Componente Selecionado: ${hotspot.dataset.title}</strong><br>
          <p style="margin: 0.35rem 0 0 0; font-size: 0.95rem;">${hotspot.dataset.desc || ''}</p>
        `;
        visualInfoBox.style.display = 'block';
      }
    });
  });
});

import { setupEventListeners } from './ui/eventListeners.js';
import { copyToClipboard, loadExample } from './ui/examplesHandlers.js';
import { updateFooterYear } from './ui/domHandlers.js';


// Adiciona as funções ao escopo global para os botões do HTML
window.copyToClipboard = copyToClipboard;
window.loadExample = loadExample;

document.addEventListener("DOMContentLoaded", () => {
  const fileInput = document.getElementById('fileInput');
  const emailText = document.getElementById('emailText');
  const processBtn = document.getElementById('processBtn');
  const loading = document.getElementById('loading');
  const results = document.getElementById('results');
  const error = document.getElementById('error');

  // Atualiza o ano no rodapé usando a função do domHandlers
  updateFooterYear();

  setupEventListeners(fileInput, emailText, processBtn, loading, results, error);
});

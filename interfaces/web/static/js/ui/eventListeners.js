import { processEmailInput } from '../adapters/emailProcessor.js';
import { showLoading, hideLoading, showError, displayResults } from './domHandlers.js';

export function setupEventListeners(fileInput, emailText, processBtn, loading, results, error) {
  fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    const fileInfo = document.getElementById('fileInfo');
    if (file) {
      fileInfo.style.display = 'block';
      fileInfo.textContent = `Arquivo selecionado: ${file.name} (${(file.size / 1024).toFixed(1)} KB)`;
      emailText.value = '';
    } else {
      fileInfo.style.display = 'none';
    }
  });

  processBtn.addEventListener('click', async () => {
    try {
      showLoading(loading, processBtn, results, error);
      const file = fileInput.files[0];
      const text = emailText.value.trim();
      const result = await processEmailInput(file, text);
      displayResults(result);
    } catch (err) {
      showError(err.message, error);
    } finally {
      hideLoading(loading, processBtn);
    }
  });
}

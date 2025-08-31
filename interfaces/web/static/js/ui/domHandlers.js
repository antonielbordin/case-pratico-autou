export function showLoading(loading, processBtn, results, error) {
  loading.style.display = 'block';
  results.style.display = 'none';
  error.style.display = 'none';
  processBtn.disabled = true;
}

export function hideLoading(loading, processBtn) {
  loading.style.display = 'none';
  processBtn.disabled = false;
}

export function showError(message, error) {
  error.textContent = message;
  error.style.display = 'block';
}

export function displayResults(result) {
  const results = document.getElementById('results');
  const classificationBadge = document.getElementById('classificationBadge');
  const confidenceMeter = document.getElementById('confidenceMeter');
  const confidenceValue = document.getElementById('confidenceValue');
  const suggestedResponse = document.getElementById('suggestedResponse');

  classificationBadge.textContent = result.classification;
  classificationBadge.className = 'classification-badge ' + 
    (result.classification === 'Produtivo' ? 'classified-productive' : 'classified-unproductive');
  
  const confidencePercent = Math.round(result.confidence * 100);
  confidenceMeter.style.width = confidencePercent + '%';
  confidenceValue.textContent = confidencePercent + '%';
  
  suggestedResponse.textContent = result.suggestedResponse;
  results.style.display = 'block';
  results.scrollIntoView({ behavior: 'smooth' });
}

export function updateFooterYear() {
  const yearSpan = document.getElementById("toDate");
  if (!yearSpan) return;

  const createdYear = 2025;
  const currentYear = new Date().getFullYear();

  yearSpan.textContent = currentYear === createdYear
    ? createdYear
    : `${createdYear} - ${currentYear}`;
}
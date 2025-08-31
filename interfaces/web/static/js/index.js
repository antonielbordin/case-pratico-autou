import { setupEventListeners } from './ui/eventListeners.js';

document.addEventListener("DOMContentLoaded", () => {
  const fileInput = document.getElementById('fileInput');
  const emailText = document.getElementById('emailText');
  const processBtn = document.getElementById('processBtn');
  const loading = document.getElementById('loading');
  const results = document.getElementById('results');
  const error = document.getElementById('error');

  setupEventListeners(fileInput, emailText, processBtn, loading, results, error);
});

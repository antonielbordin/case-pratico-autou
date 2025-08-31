import { classifyEmail } from '../core/classifyEmail.js';

export async function processEmailInput(file, text) {
  if (!file && !text) {
    throw new Error('Por favor, selecione um arquivo ou digite o texto do email.');
  }

  let emailContent = '';
  let typeEmail = '';
  if (file) {
    emailContent = await readFile(file);
    typeEmail = 'file'
  } else {
    emailContent = text;
    typeEmail = 'text'
  }

  return classifyEmail(emailContent, typeEmail);
}

function readFile(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (e) => resolve(e.target.result);
    reader.onerror = () => reject(new Error('Erro ao ler arquivo'));
    reader.readAsText(file);
  });
}

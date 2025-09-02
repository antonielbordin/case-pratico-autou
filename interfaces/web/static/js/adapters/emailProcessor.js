import { classifyEmail } from '../core/classifyEmail.js';

export async function processEmailInput(file, text) {
  if (!file && !text) {
    throw new Error('Por favor, selecione um arquivo ou digite o texto do email.');
  }

  let emailContent = '';
  let typeEmail = '';
  let fileType = '';

  if (file) {
    emailContent = await fileToBase64(file);
    typeEmail = 'file';
    fileType = file.type;
  } else {
    emailContent = text;
    typeEmail = 'text'

    console.log('is text')
  }

  return classifyEmail(emailContent, typeEmail, fileType);
}

function readFile(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (e) => resolve(e.target.result);
    reader.onerror = () => reject(new Error('Erro ao ler arquivo'));
    reader.readAsText(file);
  });
}

async function fileToBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      const base64 = e.target.result.split(',')[1];
      resolve(base64);
    };
    reader.onerror = () => reject(new Error('Erro ao ler arquivo'));
    reader.readAsDataURL(file);
  });
}

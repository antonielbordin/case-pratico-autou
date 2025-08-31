import { generateResponse } from './generateResponse.js';

export async function classifyEmail(content) {
  await new Promise(resolve => setTimeout(resolve, 2000)); // Simula API

  const productiveKeywords = [
    'suporte', 'problema', 'erro', 'status', 'processo', 'urgente',
    'solicitação', 'dúvida', 'questão', 'atualização', 'prazo',
    'impedimento', 'resolver', 'retorno', 'informar'
  ];

  const unproductiveKeywords = [
    'parabéns', 'feliz', 'aniversário', 'obrigado', 'agradecimento',
    'natal', 'ano novo', 'férias', 'abraços', 'carinho'
  ];

  const contentLower = content.toLowerCase();
  
  let productiveScore = 0;
  let unproductiveScore = 0;

  productiveKeywords.forEach(keyword => {
    if (contentLower.includes(keyword)) productiveScore++;
  });

  unproductiveKeywords.forEach(keyword => {
    if (contentLower.includes(keyword)) unproductiveScore++;
  });

  const isProductive = productiveScore > unproductiveScore;

  return {
    classification: isProductive ? 'Produtivo' : 'Improdutivo',
    confidence: Math.max(0.7, Math.random() * 0.3 + 0.7),
    suggestedResponse: generateResponse(isProductive, content)
  };
}

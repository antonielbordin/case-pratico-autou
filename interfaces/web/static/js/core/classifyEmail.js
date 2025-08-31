import { generateResponse } from './generateResponse.js';

export async function classifyEmail(content, typeEmail) {
  try {
    // Faz a chamada para o endpoint Flask
    const response = await fetch('/process-email', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ 
        content: content,
        type: typeEmail
      })
    });

    if (!response.ok) {
      throw new Error(`Erro no servidor: ${response.status}`);
    }

    const result = await response.json();

    if (result.error) {
      throw new Error(result.error);
    }

    return {
      classification: result.classification,
      confidence: result.confidence,
      suggestedResponse: result.suggestedResponse
    };

  } catch (error) {
    console.error('Erro na chamada API:', error);
    
    // Fallback para classificação local se a API falhar
    return await localClassifyEmail(content);
  }
}

// Função de fallback para classificação local
async function localClassifyEmail(content) {
  await new Promise(resolve => setTimeout(resolve, 1000)); // Simula processamento

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




  // await new Promise(resolve => setTimeout(resolve, 2000)); // Simula API
  
  // const productiveKeywords = [
  //   'suporte', 'problema', 'erro', 'status', 'processo', 'urgente',
  //   'solicitação', 'dúvida', 'questão', 'atualização', 'prazo',
  //   'impedimento', 'resolver', 'retorno', 'informar'
  // ];

  // const unproductiveKeywords = [
  //   'parabéns', 'feliz', 'aniversário', 'obrigado', 'agradecimento',
  //   'natal', 'ano novo', 'férias', 'abraços', 'carinho'
  // ];

  // const contentLower = content.toLowerCase();
  
  // let productiveScore = 0;
  // let unproductiveScore = 0;

  // productiveKeywords.forEach(keyword => {
  //   if (contentLower.includes(keyword)) productiveScore++;
  // });

  // unproductiveKeywords.forEach(keyword => {
  //   if (contentLower.includes(keyword)) unproductiveScore++;
  // });

  // const isProductive = productiveScore > unproductiveScore;

  // return {
  //   classification: isProductive ? 'Produtivo' : 'Improdutivo',
  //   confidence: Math.max(0.7, Math.random() * 0.3 + 0.7),
  //   suggestedResponse: generateResponse(isProductive, content)
  // };

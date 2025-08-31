export function generateResponse(isProductive, content) {
  const contentLower = content.toLowerCase();

  if (isProductive) {
    if (contentLower.includes('suporte') || contentLower.includes('problema') || contentLower.includes('erro')) {
      return `Prezado(a),

Recebemos sua solicitação de suporte e a mesma foi registrada em nosso sistema...`;
    } 
    if (contentLower.includes('status') || contentLower.includes('processo') || contentLower.includes('andamento')) {
      return `Prezado(a),

Agradecemos seu contato. Iremos verificar o status do processo mencionado...`;
    } 
    return `Prezado(a),

Recebemos sua mensagem e iremos analisar sua solicitação...`;
  } else {
    return `Prezado(a),

Agradecemos sua mensagem! Ficamos felizes em receber seu contato...`;
  }
}

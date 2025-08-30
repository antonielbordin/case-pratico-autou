// Exemplos de emails para teste
const examples = {
  'produtivo1': `Assunto: Solicitação de Suporte - Sistema de Pagamentos

Prezados,

Estou enfrentando problemas no sistema de pagamentos desde ontem. Quando tento processar transações acima de R$ 1000, o sistema retorna erro 500. Preciso urgentemente de suporte para resolver esta questão, pois está impactando nossos clientes.

Detalhes:
- Erro começou dia 27/08/2025 às 14:30
- Afeta apenas transações > R$ 1000
- Outros valores processam normalmente

Aguardo retorno urgente.

Atenciosamente,
João Silva
Gerente Financeiro`,

  'produtivo2': `Assunto: Status do Processo 2025-0847

Boa tarde,

Gostaria de verificar o status atual do processo 2025-0847 que foi aberto na semana passada. O cliente está cobrando uma resposta e preciso atualizar sobre o andamento.

Podem me informar:
1. Em que etapa o processo se encontra?
2. Qual o prazo previsto para conclusão?
3. Se há algum impedimento?

Agradeço a atenção.

Best regards,
Maria Santos`,

  'improdutivo1': `Assunto: Feliz Aniversário!

Oi pessoal!

Só queria desejar um feliz aniversário para nossa querida colega Ana! 🎉🎂

Que este novo ano traga muitas alegrias, realizações e sucessos!

Parabéns! 🎈

Com carinho,
Pedro Oliveira`,

  'improdutivo2': `Assunto: Obrigado pela ajuda!

Pessoal,

Muito obrigado pela ajuda de ontem com a apresentação. Ficou perfeita e o cliente aprovou tudo!

Vocês são demais! 😊

Abraços,
Carlos Lima`
};

// Elementos DOM
const fileInput = document.getElementById('fileInput');
const emailText = document.getElementById('emailText');
const processBtn = document.getElementById('processBtn');
const loading = document.getElementById('loading');

const error = document.getElementById('error');
const fileInfo = document.getElementById('fileInfo');

document.addEventListener("DOMContentLoaded", function () {
  const yearSpan = document.getElementById("toDate");
  if (!yearSpan) return;

  const createdYear = 2025;
  const currentYear = new Date().getFullYear();

  yearSpan.textContent = currentYear === createdYear
    ? createdYear
    : `${createdYear} - ${currentYear}`;
});

// Event listeners
fileInput.addEventListener('change', handleFileSelect);
processBtn.addEventListener('click', processEmail);



function handleFileSelect(event) {
  const file = event.target.files[0];
  if (file) {
    fileInfo.style.display = 'block';
    fileInfo.textContent = `Arquivo selecionado: ${file.name} (${(file.size / 1024).toFixed(1)} KB)`;
    
    // Limpar textarea quando arquivo é selecionado
    emailText.value = '';
  } else {
    fileInfo.style.display = 'none';
  }
}

function loadExample(exampleKey) {
  emailText.value = examples[exampleKey];
  fileInput.value = ''; // Limpar arquivo quando exemplo é carregado
  fileInfo.style.display = 'none';
}

async function processEmail() {
  // Validar entrada
  const file = fileInput.files[0];
  const text = emailText.value.trim();
  
  if (!file && !text) {
    showError('Por favor, selecione um arquivo ou digite o texto do email.');
    return;
  }

  // Mostrar loading
  loading.style.display = 'block';
  results.style.display = 'none';
  error.style.display = 'none';
  processBtn.disabled = true;

  try {
    let emailContent = '';
    
    if (file) {
      emailContent = await readFile(file);
    } else {
      emailContent = text;
    }

    // Simular chamada para API/backend
    const result = await classifyEmail(emailContent);
    
    displayResults(result);
      
  } catch (err) {
    showError(`Erro ao processar email: ${err.message}`);
  } finally {
    loading.style.display = 'none';
    processBtn.disabled = false;
  }
}

function displayResults(result) {
  console.log(result);
  // const classification = document.getElementById('classification');
  // const suggestedResponse = document.getElementById('suggestedResponse');
  // classification.textContent = result.classification;
  // classification.className = `classification ${result.classification.toLowerCase()}`;
  // suggestedResponse.textContent = result.suggestedResponse;
  // results.style.display = 'block';

  const results = document.getElementById('results');
  const classificationBadge = document.getElementById('classificationBadge');
  const confidenceMeter = document.getElementById('confidenceMeter');
  const confidenceValue = document.getElementById('confidenceValue');
  const suggestedResponse = document.getElementById('suggestedResponse');
  
  // Atualizar categoria
  classificationBadge.textContent = result.classification;
  classificationBadge.className = 'classification-badge ' + 
      (result.classification === 'Produtivo' ? 'classified-productive' : 'classified-unproductive');
  
  // Atualizar confiança
  const confidencePercent = Math.round(result.confidence * 100);
  confidenceMeter.style.width = confidencePercent + '%';
  confidenceValue.textContent = confidencePercent + '%';
  
  // Atualizar resposta
  suggestedResponse.textContent = result.suggestedResponse;
  
  // Mostrar resultados
  results.style.display = 'block';
  
  // Scroll para resultados
  results.scrollIntoView({ behavior: 'smooth' });

}

async function readFile(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (e) => resolve(e.target.result);
    reader.onerror = (e) => reject(new Error('Erro ao ler arquivo'));
    reader.readAsText(file);
  });
}

// Simulação da classificação (na implementação real, seria uma chamada para o backend)
async function classifyEmail(content) {
  // Simular delay da API
  await new Promise(resolve => setTimeout(resolve, 2000));

  // Lógica simples de classificação para demonstração
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

function generateResponse(isProductive, content) {
  if (isProductive) {
    // Detectar tipo de solicitação
    const contentLower = content.toLowerCase();
    
    if (contentLower.includes('suporte') || contentLower.includes('problema') || contentLower.includes('erro')) {
      return `Prezado(a),

Recebemos sua solicitação de suporte e a mesma foi registrada em nosso sistema. Nossa equipe técnica irá analisar o problema reportado e retornará com uma solução em até 24 horas úteis.

Caso seja urgente, por favor entre em contato através do telefone (11) 3000-0000.

Atenciosamente,
Equipe de Suporte Técnico`;
    } else if (contentLower.includes('status') || contentLower.includes('processo') || contentLower.includes('andamento')) {
      return `Prezado(a),

Agradecemos seu contato. Iremos verificar o status do processo mencionado e retornaremos com as informações atualizadas em até 2 horas úteis.

Atenciosamente,
Equipe de Atendimento`;
    } else {
      return `Prezado(a),

Recebemos sua mensagem e iremos analisar sua solicitação. Nossa equipe retornará com as informações necessárias em breve.

Atenciosamente,
Equipe de Atendimento`;
    }
  } else {
    return `Prezado(a),

Agradecemos sua mensagem! Ficamos felizes em receber seu contato.

Tenha um excelente dia!

Atenciosamente,
Equipe de Relacionamento`;
  }
}

function showError(message) {
  error.textContent = message;
  error.style.display = 'block';
}
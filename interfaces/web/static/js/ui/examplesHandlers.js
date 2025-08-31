export function copyToClipboard() {
  const suggestedResponse = document.getElementById('suggestedResponse');
  navigator.clipboard.writeText(suggestedResponse.textContent)
    .then(() => {
      alert('Resposta copiada para a área de transferência!');
    })
    .catch(err => {
      console.error('Erro ao copiar texto: ', err);
    });
}

export function loadExample(type) {
  const emailText = document.getElementById('emailText');
  const fileInput = document.getElementById('fileInput');
  
  // Limpa o file input
  fileInput.value = '';
  document.getElementById('fileInfo').style.display = 'none';
  
  const examples = {
    produtivo1: `Assunto: Solicitação de Suporte Técnico

Prezados,

Estou enfrentando problemas com o sistema de relatórios. Não consigo gerar os relatórios mensais desde a última atualização.

Podem verificar urgentemente? Preciso disso para o fechamento do mês.

Atenciosamente,
João Silva`,

    produtivo2: `Assunto: Status do Processo #12345

Bom dia,

Gostaria de saber o status atual do processo de aprovação do projeto X. Precisamos dessa informação para prosseguir com as próximas etapas.

Há algum impedimento?

Obrigado,
Maria Santos`,

    improdutivo1: `Assunto: Parabéns pelo Trabalho!

Olá equipe,

Gostaria de parabenizar a todos pelo excelente trabalho no último projeto. Ficou realmente incrível!

Estou muito orgulhoso da nossa equipe.

Abraços,
Carlos Oliveira`,

    improdutivo2: `Assunto: Agradecimento

Caros colegas,

Quero agradecer a todos pelo apoio durante minha ausência. Vocês são demais!

Um forte abraço,
Ana Costa`
  };

  emailText.value = examples[type] || '';
}
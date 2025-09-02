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

    improdutivo1: `Assunto: Parabéns pelo Aniversário!

Oi João,

Queria te desejar muitas felicidades pelo seu aniversário! Espero que seu dia seja incrível, cheio de alegria e bons momentos com a família e os amigos.

Vamos marcar um almoço para comemorar?

Abraços,
Carla Costa`,

    improdutivo2: `Assunto: Mensagem de Agradecimento Especial

Olá equipe,

Gostaria apenas de deixar registrado meu carinho e gratidão pelo apoio que recebi nos últimos dias. Vocês são incríveis e tornaram tudo muito mais leve.

Abraços calorosos,
Mariana Lopes`
  };

  emailText.value = examples[type] || '';
}
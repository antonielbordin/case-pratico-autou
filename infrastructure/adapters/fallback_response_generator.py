from core.entities.email import Email
from core.ports.response_generation import ResponseGenerator

class FallbackResponseGenerator(ResponseGenerator):
  """Gerador de resposta baseado em templates"""
  
  def generate_response(self, email: Email) -> Email:
    if email.classification == "produtivo":
      email.suggested_response = """Prezado(a),

Agradecemos pelo seu contato. Sua solicitação foi recebida e está sendo processada pela nossa equipe.

Em breve retornaremos com mais informações.

Atenciosamente,
Equipe de Suporte"""
    else:
      email.suggested_response = """Prezado(a),

Agradecemos sua mensagem e pelos sentimentos expressos.

Retornaremos em breve caso haja necessidade de algum assunto produtivo.

Atenciosamente,
Equipe"""
        
    return email
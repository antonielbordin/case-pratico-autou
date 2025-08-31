import re
from core.entities.email import Email
from core.ports.classification import EmailClassifier

class FallbackClassifier(EmailClassifier):
  """Classificador fallback baseado em palavras-chave"""
  
  def __init__(self):
    self.productive_keywords = [
      'problema', 'erro', 'ajuda', 'suporte', 'solicitação', 'urgente',
      'importante', 'necessito', 'preciso', 'dúvida', 'questão', 'assunto',
      'resolver', 'solucionar', 'atendimento', 'chamado', 'ticket'
    ]
    
    self.unproductive_keywords = [
      'obrigado', 'agradeço', 'parabéns', 'feliz', 'natal', 'ano novo',
      'comemoração', 'festividade', 'saudações', 'cumprimentos', 'abraço',
      'saudação', 'felicitações'
    ]
  
  def classify(self, email: Email) -> Email:
    content = email.content.lower()
    
    productive_count = sum(1 for word in self.productive_keywords if word in content)
    unproductive_count = sum(1 for word in self.unproductive_keywords if word in content)
    
    if productive_count > unproductive_count:
      email.classification = "produtivo"
      email.confidence = 0.7
    elif unproductive_count > productive_count:
      email.classification = "improdutivo"
      email.confidence = 0.7
    else:
      email.classification = "produtivo"  # Default
      email.confidence = 0.5
    
    return email
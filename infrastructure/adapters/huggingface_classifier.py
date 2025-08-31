import requests
from core.entities.email import Email
from core.ports.classification import EmailClassifier
# from config.settings import HF_API_KEY

class HuggingFaceClassifier(EmailClassifier):
  """Adaptador para classificação usando Hugging Face"""
  
  def classify(self, email: Email) -> Email:
    try:

      # Simula um erro forçando uma exceção
      raise Exception("Erro intencional para testar fallback")
            
    except Exception as e:
      # Fallback para outro classificador
      fallback = FallbackClassifier()
      return fallback.classify(email)
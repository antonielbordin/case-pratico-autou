# import openai
from core.entities.email import Email
from core.ports.response_generation import ResponseGenerator
from infrastructure.adapters.fallback_response_generator import FallbackResponseGenerator
# from config.settings import OPENAI_API_KEY

class OpenAiResponseGenerator(ResponseGenerator):
  """Adaptador para geração de resposta usando OpenAI"""
  
  def generate_response(self, email: Email) -> Email:
    try:
       
      # Simula um erro forçando uma exceção
      raise Exception("Erro intencional para testar fallback")
        
    except Exception as e:
      # Fallback para template
      fallback = FallbackResponseGenerator()
      return fallback.generate_response(email)
from core.entities.email import Email
from core.ports.response_generation import ResponseGenerator

class GenerateResponseUseCase:
  """Caso de uso para geração de resposta"""
  
  def __init__(self, response_generator: ResponseGenerator):
    self.response_generator = response_generator
  
  def execute(self, email: Email) -> Email:
    return self.response_generator.generate_response(email)
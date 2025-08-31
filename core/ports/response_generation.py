from abc import ABC, abstractmethod
from core.entities.email import Email

class ResponseGenerator(ABC):
  """Porta para geração de respostas"""
  
  @abstractmethod
  def generate_response(self, email: Email) -> Email:
    pass
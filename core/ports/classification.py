from abc import ABC, abstractmethod
from core.entities.email import Email

class EmailClassifier(ABC):
  """Porta para classificação de emails"""
  
  @abstractmethod
  def classify(self, email: Email) -> Email:
    pass
from abc import ABC, abstractmethod
from core.entities.email import Email

class FileProcessor(ABC):
  """Porta para processamento de arquivos"""
  
  @abstractmethod
  def process_file(self, file_content: bytes, filename: str) -> Email:
    pass
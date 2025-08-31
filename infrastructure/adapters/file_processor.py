import PyPDF2
import io
from core.entities.email import Email
from core.ports.file_processor import FileProcessor

class TextFileProcessor(FileProcessor):
  """Processador de arquivos de texto"""
  
  def process_file(self, file_content: bytes, filename: str) -> Email:
    content = file_content.decode('utf-8')
    return Email(content=content)

class PdfFileProcessor(FileProcessor):
  """Processador de arquivos PDF"""
  
  def process_file(self, file_content: bytes, filename: str) -> Email:
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_content))
    text = ""
    for page in pdf_reader.pages:
      text += page.extract_text() + "\n"
    return Email(content=text)

class FileProcessorFactory:
  """Factory para criar processadores de arquivo"""
  
  @staticmethod
  def get_processor(filename: str) -> FileProcessor:
    if filename.endswith('.txt'):
      return TextFileProcessor()
    elif filename.endswith('.pdf'):
      return PdfFileProcessor()
    else:
      raise ValueError(f"Formato de arquivo não suportado: {filename}")
from flask import request, jsonify
import base64
import io
import PyPDF2
from core.entities.email import Email
from core.use_cases.classification import ClassifyEmailUseCase
from core.use_cases.response_generation import GenerateResponseUseCase

# Import da factory
from infrastructure.adapters.classifier_factory import get_classifier
from infrastructure.adapters.response_generator_factory import get_response_generator

class EmailController:
  """Controlador para processamento de emails"""

  def __init__(self):
    self.classifier = get_classifier()  # Usa o padrão (huggingface)
    self.response_generator = get_response_generator() # Usa o padrão (openai)

  def process_email(self):
    try:
      if request.is_json:
        data = request.get_json()
        content = data.get('content', '')
        type_email = data.get('type', 'text')
        file_type = data.get('file_type', '')
        
        if not content.strip():
          return jsonify({'error': 'Conteúdo vazio'}), 400
        
        if type_email == 'file':
          try:
            # Decodificar base64
            file_bytes = base64.b64decode(content)
            
            # Verificar o tipo de arquivo pela extensão
            if file_type == 'application/pdf':
              email_content = self.extract_text_from_pdf(file_bytes)
            elif file_type.startswith('text/'):
              # Para TXT, decodificar os bytes para string
              email_content = file_bytes.decode('utf-8')
            else:
              return jsonify({'error': 'Formato de arquivo não suportado'}), 400
            
            email = Email(content=email_content)

          except Exception as e:
            return jsonify({'error': f'Erro ao processar arquivo: {str(e)}'}), 400
        
        else:
            email = Email(content=content)
        
      else:
        return jsonify({'error': 'Formato não suportado'}), 400
      
      # Resto do processamento (classificação e resposta)
      classify_use_case = ClassifyEmailUseCase(self.classifier)
      email = classify_use_case.execute(email)

      response_use_case = GenerateResponseUseCase(self.response_generator)
      email = response_use_case.execute(email)
      
      return jsonify({
        'classification': email.classification,
        'confidence': float(email.confidence),
        'suggestedResponse': email.suggested_response
      })
    except Exception as e:
      return jsonify({'error': str(e)}), 500
    

  def extract_text_from_pdf(self, pdf_bytes):
    """Extrai texto de conteúdo PDF"""
    try:
      pdf_file = io.BytesIO(pdf_bytes)
      pdf_reader = PyPDF2.PdfReader(pdf_file)
      
      text = ""
      for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
      
      return text.strip()
        
    except Exception as e:
      raise Exception(f"Erro ao extrair texto do PDF: {str(e)}")
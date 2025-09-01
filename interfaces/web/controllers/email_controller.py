from flask import request, jsonify
from core.entities.email import Email
from core.use_cases.classification import ClassifyEmailUseCase
from core.use_cases.response_generation import GenerateResponseUseCase
from infrastructure.adapters.huggingface_classifier import HuggingFaceClassifier
from infrastructure.adapters.openai_response_generator import OpenAiResponseGenerator
from infrastructure.adapters.file_processor import FileProcessorFactory

from infrastructure.adapters.deepseek_classifier import DeepSeekClassifier
from infrastructure.adapters.openai_classifier import OpenAIClassifier

class EmailController:
  """Controlador para processamento de emails"""

  def __init__(self):
    self.classifier = OpenAIClassifier()
    self.response_generator = OpenAiResponseGenerator()

  def process_email(self):
    try:
      # Tenta como FormData (arquivo)
      if 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
          processor = FileProcessorFactory.get_processor(file.filename)
          email = processor.process_file(file.read(), file.filename)
        else:
          return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
      # Tenta como JSON (texto)
      elif request.is_json:
        data = request.get_json()
        content = data.get('content', '')
        if not content.strip():
          return jsonify({'error': 'Texto vazio'}), 400
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
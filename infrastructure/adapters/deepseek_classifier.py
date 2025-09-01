import requests
import json
from core.entities.email import Email
from core.ports.classification import EmailClassifier
from infrastructure.adapters.fallback_classifier import FallbackClassifier
from config.settings import DEEPSEEK_API_KEY

class DeepSeekClassifier(EmailClassifier):
  """Classificador usando API da DeepSeek"""

  def __init__(self):
    self.fallback = FallbackClassifier()

  def _map_classification(self, label: str, confidence: float) -> tuple[str, float]:
    """Mapeia a classificação para produtivo/improdutivo"""
    productive_keywords = ["work", "profissional", "productive", "trabalho"]
    is_productive = any(keyword in label.lower() for keyword in productive_keywords)
    return "produtivo" if is_productive else "improdutivo", confidence

  def classify(self, email: Email) -> Email:
    try:
      API_URL = "https://api.deepseek.com/v1/chat/completions"
      headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
      }
      
      prompt = f"""
      Classifique o seguinte e-mail como 'produtivo' ou 'improdutivo' para o ambiente de trabalho.
      Um e-mail produtivo é aquele relacionado a tarefas, projetos, decisões ou informações relevantes para o trabalho.
      Um e-mail improdutivo é aquele pessoal, de entretenimento, spam ou não relacionado ao trabalho.
      
      Responda APENAS com JSON no formato: {{"classification": "produtivo" ou "improdutivo", "confidence": 0.0 a 1.0}}
      
      E-mail para classificar:
      {email.content}
      """
      
      payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
        "max_tokens": 100
      }
      
      response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
      response.raise_for_status()
      result = response.json()
      
      # Extrai a resposta e converte para JSON
      response_content = result["choices"][0]["message"]["content"]
      classification_data = json.loads(response_content)
      
      email.classification = classification_data["classification"]
      email.confidence = classification_data["confidence"]
      return email
          
    except Exception as e:
      print(f"Erro na classificação com DeepSeek: {str(e)}")
      return self.fallback.classify(email)
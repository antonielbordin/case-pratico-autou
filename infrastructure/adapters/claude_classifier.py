# claude_classifier.py
import requests
import json
from core.entities.email import Email
from core.ports.classification import EmailClassifier
from infrastructure.adapters.fallback_classifier import FallbackClassifier
from config.settings import CLAUDE_API_KEY

class ClaudeClassifier(EmailClassifier):
  """Classificador usando API da Anthropic (Claude)"""

  def __init__(self):
    self.fallback = FallbackClassifier()

  def _map_classification(self, label: str, confidence: float) -> tuple[str, float]:
    """Mapeia a classificação para produtivo/improdutivo"""
    productive_keywords = ["work", "profissional", "productive", "trabalho"]
    is_productive = any(keyword in label.lower() for keyword in productive_keywords)
    return "produtivo" if is_productive else "improdutivo", confidence

  def classify(self, email: Email) -> Email:
    try:
      API_URL = "https://api.anthropic.com/v1/messages"
      headers = {
        "x-api-key": CLAUDE_API_KEY,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
      }
      
      prompt = f"""
      Classifique o seguinte e-mail como 'produtivo' ou 'improdutivo' para o ambiente de trabalho.
      Responda APENAS com JSON no formato: {{"classification": "produtivo" ou "improdutivo", "confidence": 0.0 a 1.0}}
      
      E-mail:
      {email.content}
      """
      
      payload = {
        "model": "claude-3-sonnet-20240229",
        "max_tokens": 100,
        "temperature": 0.1,
        "messages": [{"role": "user", "content": prompt}]
      }
      
      response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
      response.raise_for_status()
      result = response.json()
      
      response_content = result["content"][0]["text"]
      classification_data = json.loads(response_content)
      
      email.classification = classification_data["classification"]
      email.confidence = classification_data["confidence"]
      return email
          
    except Exception as e:
      print(f"Erro na classificação com Claude: {str(e)}")
      return self.fallback.classify(email)
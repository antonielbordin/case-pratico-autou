import re
import json
import unicodedata
from core.entities.email import Email
from core.ports.classification import EmailClassifier

class FallbackClassifier(EmailClassifier):
  """Classificador baseado em palavras-chave e frases de intenção com pesos configuráveis"""

  def __init__(self, keywords_path="infrastructure/config/keywords.json"):
    with open(keywords_path, 'r', encoding='utf-8') as f:
      data = json.load(f)
    self.weights = data.get("weights", {"productive": 2.0, "unproductive": 1.0, "intent_phrase": 3.0})
    self.productive_keywords = data.get("productive", [])
    self.unproductive_keywords = data.get("unproductive", [])
    self.intent_phrases = data.get("intent_phrases", [])

  def normalize_text(self, text: str) -> str:
    """Remove acentos e converte para minúsculas."""
    text = unicodedata.normalize('NFKD', text)
    text = ''.join([c for c in text if not unicodedata.combining(c)])
    return text.lower()

  def count_keywords(self, patterns: list, content: str, weight: float = 1.0) -> float:
    """Conta quantas palavras-chave aparecem no texto e aplica peso."""
    return sum(weight for pattern in patterns if re.search(pattern, content))

  def count_phrases(self, phrases: list, content: str, weight: float = 1.0) -> float:
    """Verifica se frases de intenção aparecem no texto e aplica peso."""
    return sum(weight for phrase in phrases if phrase in content)

  def classify(self, email: Email) -> Email:
    content = self.normalize_text(email.content)

    productive_count = self.count_keywords(
      self.productive_keywords, content, self.weights.get("productive", 2.0)
    )
    unproductive_count = self.count_keywords(
      self.unproductive_keywords, content, self.weights.get("unproductive", 1.0)
    )
    intent_score = self.count_phrases(
      self.intent_phrases, content, self.weights.get("intent_phrase", 3.0)
    )

    # Soma frases de intenção ao score produtivo
    productive_count += intent_score

    if productive_count > unproductive_count:
      email.classification = "produtivo"
      email.confidence = min(0.5 + 0.05 * productive_count, 0.95)
    elif unproductive_count > productive_count:
      email.classification = "improdutivo"
      email.confidence = min(0.5 + 0.05 * unproductive_count, 0.95)
    else:
      email.classification = "produtivo"
      email.confidence = 0.5

    return email

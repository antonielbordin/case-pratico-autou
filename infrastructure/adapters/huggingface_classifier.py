import re
import requests
from deep_translator import GoogleTranslator
from core.entities.email import Email
from core.ports.classification import EmailClassifier
from infrastructure.adapters.fallback_classifier import FallbackClassifier
from config.settings import HF_API_KEY
import logging

logger = logging.getLogger(__name__)

class HuggingFaceClassifier(EmailClassifier):
  """Adaptador para classificação de emails usando Hugging Face (BART-MNLI) com prompt simplificado"""

  def __init__(self):
    self.bart_url = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
    self.xlmr_url = "https://api-inference.huggingface.co/models/joeddav/xlm-roberta-large-xnli"
    self.headers = {"Authorization": f"Bearer {HF_API_KEY}"}

  def _preprocess_email(self, email: Email) -> str:
    """Remove assinaturas, emails, telefones e excesso de espaços"""
    content = email.content
    patterns = [
        r"(?s)best regards.*",
        r"(?s)atenciosamente.*",
        r"(?s)grato.*",
        r"(?s)thanks.*",
        r"(?s)regards.*",
        r"(?s)assinado.*",
        r"(?s)sent from my.*",
        r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    ]
    for pattern in patterns:
      content = re.sub(pattern, "", content, flags=re.IGNORECASE)
    content = re.sub(r'\s+', ' ', content).strip()
    return content[:2000]  # Limite de tamanho para evitar timeout

  def _classify_with_model(self, email: Email, model_url: str, use_translation: bool = False) -> Email:
    """Classifica email usando um modelo específico com prompt direto"""
    try:
      content = self._preprocess_email(email)

      # Tradução se necessário
      if use_translation:
        try:
          content = GoogleTranslator(source='auto', target='en').translate(content)
        except Exception as e:
          logger.warning(f"Falha na tradução: {e}")

      # Prompt direto
      prompt = (
        f"O e-mail a seguir é produtivo ou improdutivo? "
        f"Responda apenas com 'produtivo' ou 'improdutivo'.\n\nE-mail: {content}"
      )

      payload = {
        "inputs": prompt,
        "parameters": {
          "candidate_labels": ["produtivo", "improdutivo"]
        },
        "options": {"wait_for_model": True}
      }

      response = requests.post(model_url, headers=self.headers, json=payload, timeout=45)
      response.raise_for_status()
      result = response.json()

      if isinstance(result, dict) and 'error' in result:
        raise RuntimeError(result['error'])

      # Resultado do modelo
      if isinstance(result, list) and len(result) > 0:
        label = result[0].get('label') or result[0].get('generated_text', '').lower()
        score = result[0].get('score', 0.5)

        if "produtivo" in label.lower():
          email.classification = "produtivo"
          email.confidence = score
        else:
          email.classification = "improdutivo"
          email.confidence = score
        return email

      # Fallback se resposta inválida
      fallback = FallbackClassifier()
      return fallback.classify(email)

    except Exception as e:
      logger.error(f"Falha na classificação: {e}")
      fallback = FallbackClassifier()
      return fallback.classify(email)

  def _classifyBart(self, email: Email) -> Email:
    """Classifica usando BART-MNLI"""
    return self._classify_with_model(email, self.bart_url, use_translation=False)

  def _classifyXLMR(self, email: Email) -> Email:
    """Classifica usando XLM-RoBERTa"""
    return self._classify_with_model(email, self.xlmr_url, use_translation=True)

  def classify(self, email: Email) -> Email:
    """Classifica usando ambos os modelos e faz consenso"""
    try:
      bart_result = self._classifyBart(email)
      xlmr_result = self._classifyXLMR(email)

      if bart_result.classification == xlmr_result.classification:
        email.classification = bart_result.classification
        email.confidence = (bart_result.confidence + xlmr_result.confidence) / 2
      else:
        # Em caso de discordância, escolhe o de maior confiança
        if bart_result.confidence >= xlmr_result.confidence:
          email.classification = bart_result.classification
          email.confidence = bart_result.confidence
        else:
          email.classification = xlmr_result.classification
          email.confidence = xlmr_result.confidence

      return email

    except Exception as e:
      logger.error(f"Falha no consenso de classificação: {e}")
      return self._classifyBart(email)

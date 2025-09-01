import re
import requests
from deep_translator import GoogleTranslator
from core.entities.email import Email
from core.ports.classification import EmailClassifier
from infrastructure.adapters.fallback_classifier import FallbackClassifier
from config.settings import HF_API_KEY

class HuggingFaceClassifier(EmailClassifier):
  """Adaptador para classificação usando Hugging Face"""

  def _classifyBart(self, email: Email) -> Email:
    """Classificação usando facebook/bart-large-mnli (multilíngue)"""
    try:
      API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
      headers = {"Authorization": f"Bearer {HF_API_KEY}"}

      USE_TRANSLATION = False  # mude para False se quiser testar PT direto

      categories_en = ["work", "personal"]
      categories_pt = ["profissional", "pessoal"]

      if USE_TRANSLATION:
        try:
          translated_content = GoogleTranslator(source='auto', target='en').translate(email.content)
          inputs = translated_content
          categories = categories_en
        except Exception:
          inputs = email.content
          categories = categories_pt
      else:
        inputs = email.content
        categories = categories_pt

      payload = {
        "inputs": inputs,
        "parameters": {
          "candidate_labels": categories,
          "multi_label": False
        },
        "options": {"wait_for_model": True}
      }

      response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
      response.raise_for_status()
      result = response.json()

      if isinstance(result, dict) and 'error' in result:
        raise RuntimeError(result['error'])

      labels = result['labels']
      scores = result['scores']

      max_score_index = max(range(len(scores)), key=lambda i: scores[i])
      selected_label = labels[max_score_index]
      confidence = scores[max_score_index]

      # Mapeia para produtivo x improdutivo conforme o idioma usado
      if USE_TRANSLATION:
        is_productive = (selected_label == "work")
      else:
        is_productive = (selected_label == "profissional")

      email.classification = "produtivo" if is_productive else "improdutivo"
      email.confidence = confidence
      return email

    except Exception:
      # Fallback para outro classificador
      fallback = FallbackClassifier()
      return fallback.classify(email)

  def _classifyXLMR(self, email: Email) -> Email:
    """Classificação usando joeddav/xlm-roberta-large-xnli (multilíngue)"""
    try:
      API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
      headers = {"Authorization": f"Bearer {HF_API_KEY}"}

      USE_TRANSLATION = True  # mude para False se quiser testar PT direto

      categories_en = ["work", "personal"]
      categories_pt = ["profissional", "pessoal"]

      if USE_TRANSLATION:
        # Tenta traduzir; se falhar, cai para PT
        try:
          translated_content = GoogleTranslator(source='auto', target='en').translate(email.content)
          inputs = translated_content
          categories = categories_en
        except Exception:
          inputs = email.content
          categories = categories_pt
      else:
        inputs = email.content
        categories = categories_pt

      payload = {
        "inputs": inputs,
        "parameters": {
          "candidate_labels": categories,
          "multi_label": False
        },
        "options": {"wait_for_model": True}
      }

      response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
      response.raise_for_status()
      result = response.json()

      if isinstance(result, dict) and 'error' in result:
        raise RuntimeError(result['error'])
      
      labels = result['labels']
      scores = result['scores']
      
      max_score_index = max(range(len(scores)), key=lambda i: scores[i])
      selected_label = labels[max_score_index]
      confidence = scores[max_score_index]

      # Mapeia para produtivo x improdutivo conforme o idioma usado
      if USE_TRANSLATION:
        is_productive = (selected_label == "work")
      else:
        is_productive = (selected_label == "profissional")

      email.classification = "produtivo" if is_productive else "improdutivo"
      email.confidence = confidence
      return email
      
    except Exception:
      # Fallback para outro classificador
      fallback = FallbackClassifier()
      return fallback.classify(email)
 
  def classify(self, email: Email) -> Email:
    return self._classifyXLMR(email)
    #return self._classifyBart(email)

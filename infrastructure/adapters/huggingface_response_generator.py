import requests
from core.entities.email import Email
from core.ports.response_generation import ResponseGenerator
from infrastructure.adapters.fallback_response_generator import FallbackResponseGenerator
from config.settings import HF_API_KEY

class HuggingFaceResponseGenerator(ResponseGenerator):
  """Adaptador para geração de resposta usando API do Hugging Face"""
  
  def __init__(self):
    self.model_url = "https://api-inference.huggingface.co/models/facebook/blenderbot-3B"
    self.headers = {"Authorization": f"Bearer {HF_API_KEY}"}
      
  def generate_response(self, email: Email) -> Email:
    try:      
      prompt = (
        f"O e-mail a seguir precisa de uma resposta breve e profissional. "
        f"Não use mais de 3 frases e seja educado e direto.\n\n"
        f"Email: {email.content}\n\n"
        f"Resposta:"
      )
      
      payload = {
        "inputs": prompt,
        "parameters": {
          "max_length": 80,  # Resposta curta
          "min_length": 20,
          "do_sample": False
        }
      }

      response = requests.post(self.model_url, headers=self.headers, json=payload, timeout=45)
      response.raise_for_status()
      result = response.json()

      if isinstance(result, list) and len(result) > 0:
        text = result[0].get("generated_text", "").strip()
        email.suggested_response = text
        return email

      # Fallback
      fallback = FallbackResponseGenerator()
      return fallback.generate_response(email)
        
    except Exception as e:
      print(f"Erro na API Hugging Face: {e}")
      fallback = FallbackResponseGenerator()
      return fallback.generate_response(email)
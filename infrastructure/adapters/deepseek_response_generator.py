import requests
from core.entities.email import Email
from core.ports.response_generation import ResponseGenerator
from infrastructure.adapters.fallback_response_generator import FallbackResponseGenerator
from config.settings import DEEPSEEK_API_KEY

class DeepSeekResponseGenerator(ResponseGenerator):
  """Adaptador para geração de resposta usando API da DeepSeek"""

  def generate_response(self, email: Email) -> Email:
    try:
      API_URL = "https://api.deepseek.com/v1/chat/completions"
      headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
      }

      prompt = f"""
        Você é um assistente profissional de emails. Gere uma resposta curta, educada e objetiva em português para o seguinte email. 
        A resposta deve ter **no máximo 3 frases**, adequada ao contexto e ao tipo de email.

        Classificação do email: {email.classification} 
        Confiança da classificação: {email.confidence}

        Email: {email.content[:500]}

        Responda de forma direta e profissional:
        """

      data = {
        "model": "deepseek-chat",
        "messages": [
          {"role": "system", "content": "Você é um assistente profissional de email."},
          {"role": "user", "content": prompt}
        ],
        "max_tokens": 100,
        "temperature": 0.3
      }

      response = requests.post(API_URL, headers=headers, json=data)
      response.raise_for_status()
      email.suggested_response = response.json()['choices'][0]['message']['content'].strip()
      return email

    except Exception as e:
      fallback = FallbackResponseGenerator()
      return fallback.generate_response(email)

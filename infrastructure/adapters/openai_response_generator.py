import openai
from core.entities.email import Email
from core.ports.response_generation import ResponseGenerator
from infrastructure.adapters.fallback_response_generator import FallbackResponseGenerator
from config.settings import OPENAI_API_KEY

class OpenAIResponseGenerator(ResponseGenerator):
  """Adaptador para geração de resposta usando OpenAI"""
  
  def generate_response(self, email: Email) -> Email:
    try:
      openai.api_key = OPENAI_API_KEY
            
      prompt = f"""
      Você é um assistente profissional de emails. Gere uma resposta curta, educada e objetiva em português para o seguinte email. 
      A resposta deve ter **no máximo 3 frases**, adequada ao contexto e ao tipo de email.

      Classificação do email: {email.classification} 
      Confiança da classificação: {email.confidence}

      Email: {email.content[:500]}

      Responda de forma direta e profissional:"""
      
      response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "system", "content": "Você é um assistente profissional de email."},
          {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.3
      )
      
      email.suggested_response = response.choices[0].message.content.strip()
      return email
        
    except Exception as e:
      # Fallback para template
      fallback = FallbackResponseGenerator()
      return fallback.generate_response(email)
from typing import Literal
from infrastructure.adapters.deepseek_response_generator import DeepSeekResponseGenerator
from infrastructure.adapters.openai_response_generator import OpenAIResponseGenerator
from infrastructure.adapters.claude_response_generator import ClaudeResponseGenerator
from infrastructure.adapters.huggingface_response_generator import HuggingFaceResponseGenerator
from core.ports.response_generation import ResponseGenerator

def get_response_generator(provider: Literal["huggingface", "deepseek", "openai", "claude"] = "openai") -> ResponseGenerator:
  """
  Factory para obter diferentes implementações de gerador de resposta
  """
  if provider == "deepseek":
    return DeepSeekResponseGenerator()
  elif provider == "openai":
    return OpenAIResponseGenerator()
  elif provider == "claude":
    return ClaudeResponseGenerator()
  else:
    return HuggingFaceResponseGenerator()
from typing import Literal
from infrastructure.adapters.huggingface_classifier import HuggingFaceClassifier
from infrastructure.adapters.deepseek_classifier import DeepSeekClassifier
from infrastructure.adapters.openai_classifier import OpenAIClassifier
from infrastructure.adapters.claude_classifier import ClaudeClassifier
from core.ports.classification import EmailClassifier

def get_classifier(provider: Literal["huggingface", "deepseek", "openai", "claude"] = "huggingface") -> EmailClassifier:
  """
  Factory para obter diferentes implementações de classificadores
  """
  if provider == "deepseek":
    return DeepSeekClassifier()
  elif provider == "openai":
    return OpenAIClassifier()
  elif provider == "claude":
    return ClaudeClassifier()
  else:
    return HuggingFaceClassifier()
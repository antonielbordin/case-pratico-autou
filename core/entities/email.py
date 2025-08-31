from dataclasses import dataclass
from typing import Optional

@dataclass
class Email:
  """Entidade Email representando o domínio principal"""
  content: str
  classification: Optional[str] = None
  confidence: Optional[float] = None
  suggested_response: Optional[str] = None
  
  def is_productive(self) -> bool:
    return self.classification == "produtivo"
from core.entities.email import Email
from core.ports.classification import EmailClassifier

class ClassifyEmailUseCase:
  """Caso de uso para classificação de email"""
  
  def __init__(self, classifier: EmailClassifier):
    self.classifier = classifier
  
  def execute(self, email: Email) -> Email:
    return self.classifier.classify(email)
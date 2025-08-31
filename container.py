from dependency_injector import containers, providers
from core.ports.classification import EmailClassifier
from core.ports.response_generation import ResponseGenerator
from infrastructure.adapters.huggingface_classifier import HuggingFaceClassifier
from infrastructure.adapters.fallback_classifier import FallbackClassifier
from infrastructure.adapters.openai_response_generator import OpenAiResponseGenerator
from infrastructure.adapters.fallback_response_generator import FallbackResponseGenerator
from config.settings import DEFAULT_CLASSIFIER, DEFAULT_RESPONSE_GENERATOR

class Container(containers.DeclarativeContainer):
    """Container de injeção de dependência"""
    
    # Configuração
    config = providers.Configuration()
    
    # Adaptadores
    huggingface_classifier = providers.Factory(HuggingFaceClassifier)
    fallback_classifier = providers.Factory(FallbackClassifier)
    openai_response_generator = providers.Factory(OpenAiResponseGenerator)
    fallback_response_generator = providers.Factory(FallbackResponseGenerator)
    
    # Seleção dinâmica de implementações baseada na configuração
    classifier = providers.Selector(
        config.default_classifier,
        huggingface=huggingface_classifier,
        fallback=fallback_classifier
    )
    
    response_generator = providers.Selector(
        config.default_response_generator,
        openai=openai_response_generator,
        template=fallback_response_generator
    )
    
    # Configuração padrão
    config.default_classifier.from_value(DEFAULT_CLASSIFIER)
    config.default_response_generator.from_value(DEFAULT_RESPONSE_GENERATOR)
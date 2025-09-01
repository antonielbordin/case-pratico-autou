import os
from dotenv import load_dotenv

load_dotenv()

# Configurações da aplicação
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# API Keys
HF_API_KEY = os.getenv('HF_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')

# Configurações de modelo
DEFAULT_CLASSIFIER = os.getenv('DEFAULT_CLASSIFIER', 'huggingface')
DEFAULT_RESPONSE_GENERATOR = os.getenv('DEFAULT_RESPONSE_GENERATOR', 'openai')
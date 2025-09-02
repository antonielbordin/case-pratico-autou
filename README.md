# 📧 Case Prático AutoU - Sistema de Classificação de Emails

> **Simulação prática simplificada de um projeto real da AutoU**

Um sistema inteligente de classificação de emails que determina automaticamente se um email é **produtivo** (relacionado ao trabalho) ou **improdutivo** (pessoal/social), utilizando modelos de Machine Learning e técnicas de NLP.

## 🎯 **Objetivo do Projeto**

Este projeto implementa um sistema completo de classificação de emails usando **Arquitetura Limpa** (Clean Architecture) e **padrões de design**, demonstrando boas práticas de desenvolvimento de software aplicadas a problemas de **Inteligência Artificial**.

## ⚙️ **Funcionalidades**

- ✅ **Classificação Automática**: Determina se emails são produtivos ou improdutivos
- ✅ **Múltiplos Modelos**: Suporte a diferentes modelos de ML (BART, XLM-RoBERTa)
- ✅ **Processamento Inteligente**: Pré-processamento avançado de texto
- ✅ **Sistema de Fallback**: Classificação baseada em palavras-chave como backup
- ✅ **API RESTful**: Interface web para integração
- ✅ **Análise de Confiança**: Score de confiança para cada classificação
- ✅ **Arquitetura Limpa**: Separação clara de responsabilidades


## 🏗️ **Arquitetura do Sistema**

### Backend (Python/Flask)
- Endpoint de renderização do template html
- Endpoint de processamento do email

### Frontend (JavaScript/HTML/CSS)
- Interface responsiva para upload de arquivos e texto
- Exibição de resultados de classificação

```
📁 case-pratico-autou/
├── 🧠 core/                                    # Camada de domínio
│   ├── 📦 entities/
│   │   └── 📧 email.py                        # Entidade Email
│   ├── 🔌 ports/
│   │   ├── 🎯 classification.py               # Interface de classificação
│   │   ├── 📄 file_processor.py               # Interface de processamento de arquivos
│   │   └── ✨ response_generation.py          # Interface de geração de respostas
│   └── ⚙️ use_cases/
│       ├── 🎯 classification.py               # Casos de uso de classificação
│       └── ✨ response_generator.py           # Casos de uso de geração de respostas
│
├── 🏭 infrastructure/                          # Camada de infraestrutura
│   ├── 🔧 adapters/
│   │   ├── 🤖 openai_classifier.py            # Classificador OpenAI
│   │   ├── 🧪 deepseek_classifier.py          # Classificador DeepSeek
│   │   ├── 🎭 claude_classifier.py            # Classificador Claude
│   │   ├── 🤗 huggingface_classifier.py       # Classificador HuggingFace
│   │   ├── 🛡️ fallback_classifier.py          # Classificador de fallback
│   │   ├── 🤖 openai_response_generator.py    # Gerador de respostas OpenAI
│   │   ├── 🧪 deepseek_response_generator.py  # Gerador de respostas DeepSeek
│   │   ├── 🎭 claude_response_generator.py    # Gerador de respostas Claude
│   │   ├── 🤗 huggingface_response_generator.py # Gerador de respostas HuggingFace
│   │   ├── 🛡️ fallback_response_generator.py  # Gerador de respostas fallback
│   │   ├── 🏭 classifier_factory.py           # Factory de classificadores
│   │   ├── 🏭 response_generator_factory.py   # Factory de geradores de resposta
│   │   └── 📄 file_processor.py               # Processador de arquivos
│   └── ⚙️ config/
│       └── 🔑 keywords.json                   # Palavras-chave de configuração
│
├── 🌐 interfaces/                              # Camada de interface
│   └── 🕸️ web/
│       ├── 🎮 controllers/
│       │   └── 📧 email_controller.py         # Controlador de emails
│       ├── 🎨 static/
│       │   ├── 🎨 css/
│       │   │   └── 💅 style.css               # Estilos CSS
│       │   └── ⚡ js/
│       │       ├── 🔧 adapters/
│       │       │   └── 📧 emailProcessor.js   # Processador de email JS
│       │       ├── 🧠 core/
│       │       │   ├── 🎯 classifyEmail.js    # Classificação de email JS
│       │       │   └── ✨ generateResponse.js # Geração de resposta JS
│       │       ├── 🖼️ ui/
│       │       │   ├── 🎛️ domHandlers.js      # Manipuladores DOM
│       │       │   ├── 👂 eventListeners.js   # Event listeners
│       │       │   └── 📝 examplesHandlers.js # Manipuladores de exemplos
│       │       └── 🚀 index.js                # Arquivo principal JS
│       └── 📑 templates/
│           └── 🏠 index.html                  # Template principal
│
├── 🧪 tests/                                  # Camada de testes
│   ├── 🔗 integration/                       # Testes de integração
│   └── 🧩 unit/                              # Testes unitários
│
├── ⚙️ config/
│   └── 🔧 settings.py                        # Configurações da aplicação
│
├── 🚀 app.py                                 # Aplicação principal Flask
├── 📦 container.py                           # Container de dependências
├── 🐳 docker-compose.yml                     # Configuração Docker Compose
├── 🐳 Dockerfile                             # Configuração Docker
├── 📜 LICENSE                                # Licença do projeto
├── 📋 requirements.txt                       # Dependências Python
├── 🐍 runtime.txt                            # Versão do Python
├── 🔒 .env                                   # Variáveis de ambiente
├── 🙈 .gitignore                             # Arquivos ignorados pelo Git
├── 🎬 start.sh                               # Script de inicialização
└── 📄 README.md                              # Documentação do projeto
```

## 🚀 **Tecnologias Utilizadas**

### **Backend & API**
- **Python 3.8+**
- **Flask** - Framework web minimalista
- **Requests** - Cliente HTTP para APIs
- **PyPDF2** - Processamento de PDFs
- **OpenAI API** - Geração de respostas
- **Hugging Face Transformers** - Modelos de ML
- **Requests** - Cliente HTTP

### Frontend
- **HTML5/CSS3** - Estrutura e estilo
- **JavaScript ES6+** - Interatividade
- **Fetch API** - Comunicação com backend

### **Machine Learning & NLP**
- **HuggingFace Transformers** - Modelos de NLP
  - `facebook/bart-large-mnli` - Classificação zero-shot
  - `joeddav/xlm-roberta-large-xnli` - Classificação multilíngue
- **OpenAI GPT-3.5/4** - Geração de respostas
- **Deep Translator** - Tradução automática
- **Regex (re)** - Processamento de texto

### **Arquitetura & Padrões**
- **Clean Architecture** - Separação de camadas
- **Dependency Injection** - Inversão de dependências
- **Factory Pattern** - Criação de classificadores
- **Strategy Pattern** - Múltiplas estratégias de classificação

## 📦 **Instalação e Configuração**

### **Pré-requisitos**
- Python 3.8 ou superior
- Conta no HuggingFace (para API key)
- pip ou conda para gerenciamento de pacotes
- Git

### **1. Clonar o Repositório**
```bash
git clone https://github.com/antonielbordin/case-pratico-autou.git
cd case-pratico-autou
```

### **2. Criar Ambiente Virtual**
```bash
# Com venv
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Ou com conda
conda create -n autou-env python=3.8
conda activate autou-env
```

### **3. Instalar Dependências**
```bash
pip install -r requirements.txt
```

### **4. Configurar Variáveis de Ambiente**
Crie um arquivo `.env` na raiz do projeto:
```env
OPENAI_API_KEY=your_openai_api_key_here
HF_API_KEY=your_huggingface_api_key_here
FLASK_ENV=development
FLASK_DEBUG=True
```

### **5. Obter API Key do HuggingFace**
1. Acesse [HuggingFace](https://huggingface.co/)
2. Faça login/cadastro
3. Vá em Settings → Access Tokens
4. Gere um novo token
5. Adicione ao arquivo `.env`

## 🎯  **Como Usar**

### **Executar a Aplicação**
```bash
python app.py
```

### **Via Interface Web**

    Acesse http://localhost:5000

    Selecione um arquivo (PDF/TXT) ou digite texto diretamente

    Clique em "Processar Email"

    Visualize a classificação e resposta sugerida


### **Testar via API**
```bash
# Exemplo de requisição
curl -X POST http://localhost:5000/process-email \
  -H "Content-Type: application/json" \
  -d '{
    "content": "base64_encoded_content",
    "type": "file",
    "file_name": "document.pdf"
  }'
```

### **Resposta Esperada**
```json
{
  "classification": "produtivo",
  "confidence": 0.89,
  "suggestedResponse": "Agradeço seu contato. Analisarei sua solicitação..."
}
```

## 🧠 **Como Funciona**

### **1. Pré-processamento**
- Remove URLs, emails e números desnecessários
- Limita texto a ~400 palavras (limite de tokens)
- Normaliza caracteres especiais

### **2. Extração de Características**
- Identifica palavras-chave de trabalho: `projeto`, `cliente`, `prazo`, `meeting`, `deadline`
- Identifica palavras-chave pessoais: `família`, `férias`, `festa`, `family`, `vacation`

### **3. Classificação Inteligente**
- Usa modelos BART/XLM-RoBERTa via HuggingFace
- Labels descritivos para melhor contexto
- Ajuste de confiança baseado em palavras-chave

### **4. Sistema de Fallback**
- Se a API falhar, usa classificação baseada em regras
- Garante 100% de disponibilidade do serviço

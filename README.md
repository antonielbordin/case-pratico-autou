# 📧 Case Prático AutoU - Sistema de Classificação de Emails

> **Simulação prática simplificada de um projeto real da AutoU**

Um sistema inteligente de classificação de emails que determina automaticamente se um email é **produtivo** (relacionado ao trabalho) ou **improdutivo** (pessoal/social), utilizando modelos de Machine Learning e técnicas de NLP.

## 🎯 **Objetivo do Projeto**

Demonstrar um sistema completo de **classificação de e-mails** aplicando: 
- **Arquitetura Limpa** (Clean Architecture) 
- **Boas práticas de design de software**
- **Modelos de NLP (Machine Learning e APIs externas)**

## ⚙️ **Funcionalidades**

- ✅ **Classificação Automática**: Determina se emails são produtivos ou improdutivos
- ✅ **Múltiplos Modelos**: Suporte a diferentes modelos de ML (BART, XLM-RoBERTa)
- ✅ **Processamento Inteligente**: Pré-processamento avançado de texto
- ✅ **Sistema de Fallback**: Classificação baseada em palavras-chave como backup
- ✅ **API RESTful**: Interface web para integração
- ✅ **Análise de Confiança**: Score de confiança para cada classificação
- ✅ **Arquitetura Limpa**: Separação clara de responsabilidades


## 🏗️ **Arquitetura do Sistema**

A aplicação segue o padrão de **Clean Architecture**, separando responsabilidades em camadas:

- **Core** → Entidades, portas (interfaces) e casos de uso  
- **Infrastructure** → Adaptadores para IA (OpenAI, HuggingFace etc.), fallback e configuração  
- **Interfaces** → API Flask + frontend web em HTML/JS  
- **Tests** → Testes unitários e de integração

### Estrutura de pastas

```
📁 case-pratico-autou/
├── 🧠 core/   # Regras de negócio e domínio
│   ├── entities/ # Entidades (Email)
│   ├── ports/ # Interfaces (contratos)
│   └── use_cases/ # Casos de uso
│
├── 🏭 infrastructure/ # Implementações técnicas
│   ├── adapters/ # Classificadores, geradores de resposta, fábricas
│   └── config/ # Configurações (keywords.json, settings.py)
│
├── 🌐 interfaces/ # Camada de interface
│   └── web/ # API Flask + frontend (templates, static, controllers)
│
├── 🧪 tests/ # Testes unitários e de integração
│
├── app.py # Entrada principal Flask
├── container.py # Injeção de dependências
├── requirements.txt # Dependências Python
├── Dockerfile # Configuração Docker
├── docker-compose.yml # Orquestração de containers
├── .env # Variáveis de ambiente
└── README.md # Documentação

```

---

## 🧠 Como Funciona

1. **Recepção** → O usuário envia um e-mail (texto direto ou arquivo).  
2. **Pré-processamento** → O texto é limpo (remoção de URLs, emails, caracteres especiais).  
3. **Classificação**  
   - Tentativa com modelo de IA como BART/XLM-RoBERTa via HuggingFace e (OpenAI, DeepSeek, etc.)  
   - Se falhar ou a confiança for baixa, ativa o **fallback** por palavras-chave.  
4. **Análise de Confiança** → Cada classificação recebe um score de confiança.  
5. **Resposta** → Opcionalmente, um gerador de resposta automática é acionado.  
6. **Exibição** → O resultado é retornado via **API** ou mostrado na **interface web**.  

---

 

## 🔄 **Fluxo de Processamento**

  - Recepção: Upload de arquivo ou texto direto
  - Pré-processamento: Extração e limpeza de conteúdo
  - Classificação: Análise com múltiplos modelos de ML
  - Geração de Resposta: Criação de resposta contextual
  - Apresentação: Exibição dos resultados ao usuário

 
## 🚀 **Tecnologias Utilizadas**

### **Backend & API**
- **Python 3.8+**
- **Flask** - Framework web minimalista
- **Requests** - Cliente HTTP para APIs
- **PyPDF2** - Processamento de PDFs
- **OpenAI API** - Geração de respostas
- **Hugging Face Transformers** - Modelos de ML
- **Requests** - Cliente HTTP

### **Frontend**
- **HTML5/CSS3** - Estrutura e estilo
- **JavaScript ES6+** - Interatividade
- **Fetch API** - Comunicação com backend

### **IA & NLP**
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
- Python 3.8+
- Conta na OpenAI e/ou HuggingFace (API Key)
- pip para gerenciamento de pacotes
- Git

### **Etapas**

### **1. Clonar o Repositório**
```bash
git clone https://github.com/antonielbordin/case-pratico-autou.git
cd case-pratico-autou
```

### **2. Criar Ambiente Virtual**
```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
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

## 🔧 **Configurações Avançadas**

### **Alternar entre Modelos**
No arquivo `infrastructure/adapters/huggingface_classifier.py`:
```python
def classify(self, email: Email) -> Email:
    # Escolha o modelo desejado:
    return self._classifyBart(email)             # BART (padrão)
    # return self._classifyXLMR(email)           # XLM-RoBERTa
    # return self.classify_email_improved(email) # Versão otimizada
```

### **Personalizar Palavras-chave**
Edite as listas `work_keywords` e `personal_keywords` nos métodos de classificação.

## 🎯  **Como Usar**

### **Rodar a Aplicação**
```bash
python app.py
```

### **Via Interface Web**

 1. Acesse http://localhost:5000
 2. Selecione um arquivo (PDF/TXT) ou digite texto diretamente
 3. Clique em "Processar Email"
 4. Visualize a classificação e resposta sugerida
 5. Copie a resposta sugerida se nescessário

### **Via API**
```bash
# Exemplo de requisição com arquivo
curl -X POST http://localhost:5000/process-email \
  -H "Content-Type: application/json" \
  -d '{
    "content": "base64_encoded_content",
    "type": "file",
    "file_name": "document.pdf"
  }'

# Exemplo de requisição com texto
curl -X POST http://localhost:5000/process-email \
  -H "Content-Type: application/json" \
  -d '{
    "content": "seu texto aqui",
    "type": "text"
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

## 📚 **Recursos Adicionais**

- [HuggingFace Models](https://huggingface.co/models)
- [Clean Architecture em Python](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [BART Model Paper](https://arxiv.org/abs/1910.13461)
- [Email Classifier AI - Online](https://projects-autou.onrender.com/)

## 📄 **Licença**

Este projeto está sob a licença MIT. 
Veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📈 **Melhorias Futuras**
- Treinar modelos customizados
- Melhorar UI com Svelte ou Vue.js
- Documentação da API com Swagger/OpenAPI
- Monitoramento de métricas (Prometheus/Grafana)

## 👨‍💻 **Autor**

**Antoniel Bordin**
- GitHub: [@antonielbordin](https://github.com/antonielbordin)
- LinkedIn: [Antoniel Bordin](https://linkedin.com/in/antonielbordin)

## 🙏 **Agradecimentos**

- **AutoU** pela oportunidade de desenvolver este case prático
- **HuggingFace** pelos modelos de ML disponibilizados
- **Comunidade Python** pelas bibliotecas utilizadas

---

⭐ **Se este projeto foi útil para você, deixe uma estrela no GitHub!**
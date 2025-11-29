# Local AI Agent with Ollama

A simple Python AI agent project that runs language models locally using Ollama.

## 📋 Prerequisites

- Python 3.8+
- Ollama (https://ollama.ai)

## 🚀 Quick Start

### 1. Install Ollama
Download and install from [ollama.ai](https://ollama.ai)

### 2. Start Ollama Server
```bash
ollama serve
```

### 3. Pull a Model (in another terminal)
```bash
ollama pull mistral
```

Recommended models:
- `mistral` - Fast and efficient (7B)
- `llama2` - High quality (7B)
- `neural-chat` - Good for conversations (7B)
- `tinyllama` - Lightweight (1.1B)

### 4. Set Up Project

```bash
# Create .env file from example
cp .env.example .env

# Install dependencies
pip install -r requirements.txt
```

### 5. Run the Agent

```bash
# Interactive chat mode
python main.py

# Or use the agent in your code
python agent.py
```

## 📁 Project Structure

```
llm/
├── agent.py           # Core OllamaAgent class
├── main.py            # Interactive chat demo
├── requirements.txt   # Python dependencies
├── .env.example       # Environment variables template
└── README.md          # This file
```

## 💻 Usage

### Simple Generation
```python
from agent import OllamaAgent

agent = OllamaAgent()
response = agent.generate("What is AI?")
print(response)
```

### Chat Conversation
```python
messages = [
    {"role": "user", "content": "Hello!"},
]
response = agent.chat(messages)
messages.append({"role": "assistant", "content": response})

# Continue the conversation
messages.append({"role": "user", "content": "How are you?"})
response = agent.chat(messages)
```

## 🔧 Configuration

Edit `.env` file to customize:
```
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral
```

## 📚 Resources

- Ollama Documentation: https://github.com/ollama/ollama
- Available Models: https://ollama.ai/library
- API Reference: https://github.com/ollama/ollama/blob/main/docs/api.md

## ✅ Troubleshooting

- **"Connection refused"**: Make sure `ollama serve` is running
- **"Model not found"**: Run `ollama pull <model-name>`
- **Slow responses**: Use a smaller model like `tinyllama`
- **High memory usage**: Switch to a lighter model

Happy coding! 🎉

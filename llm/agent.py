import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")


class OllamaAgent:
    """Simple AI Agent using Ollama for local LLM inference"""

    def __init__(self, model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL):
        self.model = model
        self.base_url = base_url
        self.api_endpoint = f"{base_url}/api/generate"
        self.chat_endpoint = f"{base_url}/api/chat"

    def check_connection(self):
        """Check if Ollama server is running"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except Exception as e:
            print(f"Connection error: {e}")
            return False

    def generate(self, prompt, stream=False):
        """Generate text using the model"""
        if not self.check_connection():
            return "Error: Ollama server is not running. Please start Ollama first."

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream,
        }

        try:
            response = requests.post(self.api_endpoint, json=payload)
            response.raise_for_status()

            if stream:
                return response.text
            else:
                result = response.json()
                return result.get("response", "No response generated")

        except Exception as e:
            return f"Error: {str(e)}"

    def chat(self, messages, stream=False):
        """Chat with the model (conversational)"""
        if not self.check_connection():
            return "Error: Ollama server is not running. Please start Ollama first."

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": stream,
        }

        try:
            response = requests.post(self.chat_endpoint, json=payload)
            response.raise_for_status()

            if stream:
                return response.text
            else:
                result = response.json()
                return result.get("message", {}).get("content", "No response generated")

        except Exception as e:
            return f"Error: {str(e)}"


if __name__ == "__main__":
    # Example usage
    agent = OllamaAgent()

    print("🤖 Ollama AI Agent")
    print("-" * 40)

    if agent.check_connection():
        print(f"✅ Connected to Ollama on {OLLAMA_BASE_URL}")
        print(f"📦 Using model: {OLLAMA_MODEL}\n")

        # Example 1: Simple generation
        print("Example 1: Generate text")
        prompt = "What is artificial intelligence? Answer in one sentence."
        response = agent.generate(prompt)
        print(f"Prompt: {prompt}")
        print(f"Response: {response}\n")

        # Example 2: Chat
        print("Example 2: Chat conversation")
        messages = [
            {"role": "user", "content": "What is Python used for?"}
        ]
        response = agent.chat(messages)
        print(f"User: What is Python used for?")
        print(f"Agent: {response}\n")

    else:
        print("❌ Cannot connect to Ollama. Make sure it's running!")
        print("   Start Ollama with: ollama serve")

"""
Interactive AI Agent Demo
Run this script to interact with your local Ollama model
"""

from agent import OllamaAgent

def interactive_chat():
    """Interactive chat mode with the agent"""
    agent = OllamaAgent()

    if not agent.check_connection():
        print("❌ Ollama is not running!")
        print("📝 Instructions:")
        print("   1. Install Ollama: https://ollama.ai")
        print("   2. Run: ollama serve")
        print("   3. In another terminal, pull a model: ollama pull mistral")
        print("   4. Run this script again")
        return

    print("🤖 AI Agent - Chat Mode")
    print(f"Model: {agent.model}")
    print("Type 'exit' to quit\n")

    messages = []

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        print("Agent: ", end="", flush=True)
        response = agent.chat(messages)
        print(response)

        messages.append({"role": "assistant", "content": response})
        print()


if __name__ == "__main__":
    interactive_chat()

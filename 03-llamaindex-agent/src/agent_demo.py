"""
LlamaIndex Tool-calling Agent Demo
Tool: document retriever + numerical calculation
"""
from llama_index.agent.openai import OpenAIAgent

def main():
    print("==== LlamaIndex Agent Demo ====")
    # init tools: retrieval tool, calculator tool
    # build agent, run task planning & tool calling
    print("Agent run complete")

if __name__ == "__main__":
    main()

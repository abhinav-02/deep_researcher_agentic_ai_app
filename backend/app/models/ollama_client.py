from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gemma3:12b",
    temperature=0.8,
)
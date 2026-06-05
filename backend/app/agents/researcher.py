from app.models.ollama_client import llm


def summarize(content):

    prompt = f"""
    Summarize the following content.

    Focus on:
    - Facts
    - Metrics
    - Important findings

    Content:
    {content}
    """

    return llm.invoke(prompt).content
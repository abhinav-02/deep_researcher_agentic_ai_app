from app.models.ollama_client import llm


def create_plan(topic: str):

    prompt = f"""
    Create a research plan.

    Topic:
    {topic}

    Return:
    - Key areas to investigate
    - Questions to answer
    - Data sources needed
    """

    return llm.invoke(prompt).content
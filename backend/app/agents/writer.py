from app.models.ollama_client import llm


def write_report(notes):

    prompt = f"""
    Write a professional markdown report.

    Notes:
    {notes}

    Include:

    # Executive Summary

    # Findings

    # Analysis

    # Risks

    # Conclusion
    """

    return llm.invoke(prompt).content
from app.models.ollama_client import llm

def create_plan(topic: str):

    prompt = f"""
You are a search query generator.

Convert the user request into 4-5 SHORT search engine queries.

RULES:
- Each query must be 3–8 words max
- NO full sentences
- NO words like "research on", "how to", "I want"
- Must look like Google search queries

User request:
{topic}

Return ONLY a Python list of strings.

Example:
[
  "safe bond investing Europe",
  "European government bonds yield risk",
  "how to buy bonds DEGIRO Europe",
  "investment grade bonds Europe explained",
  "bond investing low risk strategy"
]
"""

    response = llm.invoke(prompt).content

    try:
        return eval(response)
    except:
        return [topic]
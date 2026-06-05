from fastapi import FastAPI

from app.agents.planner import create_plan

app = FastAPI()


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/research")
def research(payload: dict):

    topic = payload["query"]

    plan = create_plan(topic)

    return {
        "topic": topic,
        "plan": plan
    }
from fastapi import FastAPI, Response
from fastapi.responses import FileResponse

from app.agents.planner import create_plan
from app.agents.researcher import summarize
from app.agents.writer import write_report
from app.tools.search import search_web
from app.tools.url_utils import clean_urls
from app.tools.scrapper import scrape_url
from app.tools.exporter import export_docx, export_pdf

app = FastAPI()


@app.get("/")
def home():
    """Health check endpoint."""
    return {"status": "running"}


@app.post("/research")
def research(payload: dict):
    """Generate a research plan for a given topic."""
    topic = payload["query"]
    plan = create_plan(topic)
    return {"topic": topic, "plan": plan}


@app.post("/summarize")
def summarize_endpoint(payload: dict):
    """Summarize given content using the researcher agent."""
    content = payload.get("content", "")
    summary = summarize(content)
    return {"summary": summary}


@app.post("/write_report")
def write_report_endpoint(payload: dict):
    """Generate a markdown report from notes using the writer agent."""
    notes = payload.get("notes", "")
    report = write_report(notes)
    return {"report": report}




@app.post("/full_research")
def full_research_endpoint(payload: dict):

    topic = payload.get("query", "")

    if not topic:
        return {"error": "Query is required"}

    try:
        print("\n[1] Topic:", topic)

        # ✅ STEP 1: single plan generation (ONLY ONCE)
        plan = create_plan(topic)
        print("[2] Plan created")

        # If plan is bad, fallback
        if not isinstance(plan, list):
            plan = [topic]

        # ✅ STEP 2: LIMIT search calls (important for stability)
        urls = []

        for q in plan[:3]:   # LIMIT = key stability fix
            print("[3] searching:", q)

            try:
                results = search_web(q)
                urls.extend(results)
            except Exception as e:
                print("[SEARCH ERROR]", e)

        urls = list(set(urls))[:6]  # hard cap

        print("[4] URLs:", len(urls))

        # ✅ STEP 3: scraping (safe + bounded)
        raw_contents = []

        for i, u in enumerate(urls[:5]):
            print(f"[5] scraping {i+1}: {u}")

            try:
                content = scrape_url(u)

                if content and len(content) > 300:
                    raw_contents.append(content[:2000])

            except Exception as e:
                print("[SCRAPE ERROR]", e)

        if not raw_contents:
            return {
                "topic": topic,
                "plan": plan,
                "urls": urls,
                "error": "No usable content scraped"
            }

        print("[6] summarizing")

        # ✅ STEP 4: reduce LLM load (VERY IMPORTANT)
        notes = summarize("\n\n".join(raw_contents[:2]))

        print("[7] writing report")

        report = write_report(notes)

        print("[DONE]")

        return {
            "topic": topic,
            "plan": plan,
            "urls": urls,
            "notes": notes,
            "report": report,
        }
    except Exception as e:
        # Generic error handling for the full research pipeline
        return {
            "topic": topic,
            "plan": plan,
            "error": str(e),
        }

# Export endpoints – return files using FastAPI's FileResponse
@app.post("/export_docx")
def export_docx_endpoint(payload: dict):
    """Generate and return a DOCX file for the given report markdown."""
    report = payload.get("report", "")
    if not report:
        return {"error": "Report content is required"}
    path = export_docx(report)
    return FileResponse(
        path,
        filename="research_report.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )

@app.post("/export_pdf")
def export_pdf_endpoint(payload: dict):
    """Generate and return a PDF file for the given report markdown."""
    report = payload.get("report", "")
    if not report:
        return {"error": "Report content is required"}
    path = export_pdf(report)
    return FileResponse(
        path,
        filename="research_report.pdf",
        media_type="application/pdf",
    )

@app.post("/follow_up")
def follow_up(payload: dict):

    report = payload.get("report", "")
    question = payload.get("question", "")

    prompt = f"""
You are continuing an existing research project.

Existing report:

{report}

Follow-up question:

{question}

Answer specifically using the existing report as context.
Add any additional insights if needed.
"""

    answer = summarize(prompt)

    return {
        "answer": answer
    }
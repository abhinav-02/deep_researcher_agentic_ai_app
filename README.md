# 🔍 Deep Research Agentic AI App

An open-source multi-agent research assistant powered by Ollama and open-source LLMs.

The application performs autonomous research by:

* Creating a research plan
* Generating multiple search queries
* Searching the web
* Scraping relevant content
* Summarizing findings
* Generating structured reports
* Supporting follow-up research questions
* Exporting reports to Markdown, DOCX, and PDF

Built with:

* FastAPI
* Streamlit
* Ollama
* Gemma
* BeautifulSoup
* Python

---

# 🚀 Features

## Research Planning Agent

Breaks complex topics into focused research queries.

Example:

Input:

```text
How can I invest securely in European bonds?
```

Generated research plan:

```text
- European government bonds
- Bond investment risk analysis
- Investment-grade bonds Europe
- Bond yield comparison
- Safe fixed-income investing
```

---

## Search Agent

Searches the web using generated research queries.

Capabilities:

* Multi-query search
* URL filtering
* Duplicate removal
* Content-page prioritization

---

## Scraper Agent

Extracts meaningful content from discovered URLs.

Capabilities:

* HTML parsing
* Script/style removal
* Content cleaning
* Text extraction

---

## Researcher Agent

Creates concise summaries from scraped content.

Capabilities:

* Evidence extraction
* Key finding identification
* Topic summarization

---

## Writer Agent

Generates structured reports.

Report sections:

* Executive Summary
* Key Findings
* Risks
* Opportunities
* Recommendations

---

## Follow-up Research

Continue researching after the first report.

Examples:

```text
What are the main risks?

Compare this with ETFs.

Show tax implications for Dutch residents.
```

The system uses the existing report as context for deeper analysis.

---

## Export Reports

Supported formats:

* Markdown (.md)
* Microsoft Word (.docx)
* PDF (.pdf)

---

# 🏗 Architecture

```text
User Query
    │
    ▼
Planner Agent
    │
    ▼
Search Agent
    │
    ▼
Scraper Agent
    │
    ▼
Researcher Agent
    │
    ▼
Writer Agent
    │
    ▼
Research Report
    │
    ├── Follow-up Questions
    ├── Export PDF
    └── Export DOCX
```

---

# 📂 Project Structure

```text
deep_researcher_agentic_ai_app/

├── backend/
│   ├── app/
│   │   ├── agents/
│   │   │   ├── planner.py
│   │   │   ├── researcher.py
│   │   │   └── writer.py
│   │   │
│   │   ├── tools/
│   │   │   ├── search.py
│   │   │   ├── scrapper.py
│   │   │   └── exporter.py
│   │   │
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── streamlit_app.py
│   └── requirements.txt
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/abhinav-02/deep_researcher_agentic_ai_app.git

cd deep_researcher_agentic_ai_app
```

---

## 2. Install Ollama

Install Ollama:

```bash
https://ollama.com
```

Pull a model:

```bash
ollama pull gemma3:4b
```

or

```bash
ollama pull gemma3:12b
```

Start Ollama:

```bash
ollama serve
```

---

## 3. Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger API:

```text
http://127.0.0.1:8000/docs
```

---

## 4. Frontend Setup

```bash
cd frontend

python -m venv venv

source venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run streamlit_app.py
```

---

# API Endpoints

| Endpoint            | Purpose                    |
| ------------------- | -------------------------- |
| GET /               | Health Check               |
| POST /research      | Generate research plan     |
| POST /full_research | Execute complete pipeline  |
| POST /follow_up     | Continue existing research |
| POST /export_docx   | Export DOCX report         |
| POST /export_pdf    | Export PDF report          |

---

# Example Workflow

1. Enter research topic
2. Generate research plan
3. Search and scrape sources
4. Summarize findings
5. Generate report
6. Ask follow-up questions
7. Export report as DOCX or PDF

---

# Future Improvements

* LangGraph orchestration
* Async scraping
* Source citation tracking
* RAG memory
* Vector database integration
* Multi-model support
* Research history
* Deep research iterations
* Agent observability

---

# License

MIT License

---

# Author

Created by Abhinav Srivastava

GitHub:

https://github.com/abhinav-02

# Deep Researcher Agentic AI App

An AI-powered research assistant built using LangGraph, Ollama, FastAPI, and Streamlit.

The application performs autonomous research workflows by planning research tasks, gathering information from the web, summarizing findings, and generating structured reports.

## Features

* Local LLM inference using Ollama
* Research planning agent
* Web search integration
* Web content scraping
* AI-powered summarization
* Report generation
* FastAPI backend
* Streamlit frontend
* LangGraph workflow orchestration
* Fully local execution without paid APIs

## Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  ▼
FastAPI Backend
  │
  ▼
LangGraph Workflow
  │
  ├── Planner Agent
  ├── Search Agent
  ├── Scraper Agent
  ├── Summarizer Agent
  └── Report Writer Agent
  │
  ▼
Ollama + Gemma/Qwen Models
```

## Technology Stack

### Backend

* FastAPI
* LangGraph
* LangChain
* Ollama
* BeautifulSoup
* Requests
* DuckDuckGo Search

### Frontend

* Streamlit

### LLMs

* Gemma 3 12B (I have used it)
* Qwen3 14B
* Any Ollama-compatible model

## Project Structure

```text
deep-researcher-agentic-ai-app/

backend/
│
├── app/
│   ├── agents/
│   ├── models/
│   ├── tools/
│   ├── graph.py
│   └── main.py
│
└── requirements.txt

frontend/
│
├── streamlit_app.py
└── requirements.txt
```

## Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/deep-researcher-agentic-ai-app.git

cd deep-researcher-agentic-ai-app
```

### Install Ollama

https://ollama.com

Pull a model:

```bash
ollama pull gemma3:12b
```

or

```bash
ollama pull qwen3:14b
```

### Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

### Frontend Setup

```bash
cd frontend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Running the Application

### Start Ollama

```bash
ollama serve
```

### Start Backend

```bash
cd backend

source venv/bin/activate

uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

### Start Frontend

```bash
cd frontend

source venv/bin/activate

streamlit run streamlit_app.py
```

Frontend URL:

```text
http://localhost:8501
```

## Future Roadmap

* Multi-agent research workflows
* Citation support
* PDF report export
* Research memory
* Vector database integration
* RAG pipeline
* Job research assistant
* Financial research copilot
* Company intelligence reports
* Docker deployment
* Cloud deployment

## License

This project is licensed under the MIT License.

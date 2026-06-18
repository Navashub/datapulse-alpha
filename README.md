# DataPulse-alpha AI

An AI-powered document intelligence API built during the 
DataPulse internship program.

## What It Does
Upload documents. Ask questions. Get AI-powered answers.
Built with FastAPI, PostgreSQL, LanceDB, and OpenAI.

## Tech Stack
- FastAPI — API framework
- PostgreSQL — document metadata and query history
- LanceDB — vector database for semantic search
- OpenAI — embeddings and answer generation

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd datapulse-alpha
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment
```bash
cp .env.example .env
# Edit .env and add your credentials
```

### 5. Set up the database
```bash
# TODO: Add Alembic migration commands here
```

### 6. Run the API
```bash
uvicorn app.main:app --reload
```

### 7. Open API docs

http://localhost:8000/docs

## Running Tests
```bash
pytest tests/ -v
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |
| POST | /ingest | Upload a document |
| POST | /query | Ask a question |
| GET | /documents | List all documents |

## Team
<!-- TODO: Add your name and role here -->

## What I Learned
<!-- TODO: Fill this in at the end of the week -->
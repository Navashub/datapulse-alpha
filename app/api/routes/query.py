"""
Query Route.

POST /query

Accepts a question from the user.
Runs the RAG pipeline.
Returns an AI-generated answer grounded in ingested documents.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.crud import create_query_history
from app.core.rag_pipeline import run_rag_pipeline
from app.schemas.schemas import QueryRequest, QueryResponse

router = APIRouter()


@router.post("/query", response_model=QueryResponse, tags=["Query"])
async def query_documents(
    request: QueryRequest,
    db: Session = Depends(get_db)
):
    """
    Ask a question about your ingested documents.

    Returns an AI-generated answer with source references.

    TODO:
    Step 1 — Run the RAG pipeline
        result = run_rag_pipeline(
            question=request.question,
            top_k=request.top_k
        )

    Step 2 — Save to query history
        Use create_query_history() from app.db.crud
        Pass question, answer, and sources joined as string

    Step 3 — Return QueryResponse

    Error handling:
        Raise HTTPException(500) on failure
    """
    pass
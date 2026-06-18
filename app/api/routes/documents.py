"""
Documents Route.

GET /documents

Returns a list of all documents that have been ingested.
Reads from PostgreSQL (metadata only — not the vector store).
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.crud import get_all_documents
from app.schemas.schemas import DocumentResponse

router = APIRouter()


@router.get(
    "/documents",
    response_model=list[DocumentResponse],
    tags=["Documents"]
)
async def list_documents(db: Session = Depends(get_db)):
    """
    List all ingested documents.

    Returns metadata for every document stored in the system.

    TODO:
    1. Call get_all_documents(db) from crud
    2. Return the list
    3. Handle errors with HTTPException(500)
    """
    pass
"""
Document Ingestion Route.

POST /ingest

This endpoint handles the full ingestion pipeline:
  1. Receive an uploaded file
  2. Read its text content
  3. Chunk the text
  4. Embed each chunk
  5. Store chunks in LanceDB (vector store)
  6. Save document metadata to PostgreSQL
  7. Return a success response

This is the most complex route — it touches every layer of the system.
"""

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.crud import create_document
from app.core.chunker import chunk_text
from app.core.embeddings import embed_many
from app.core.vector_store import store_chunks
from app.schemas.schemas import IngestResponse
import uuid

router = APIRouter()


@router.post("/ingest", response_model=IngestResponse, tags=["Documents"])
async def ingest_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Upload and ingest a document into DataPulse AI.

    Accepts: .txt files (stretch goal: .pdf)
    Returns: Document ID, name, and chunk count

    TODO:
    Implement the ingestion pipeline:

    Step 1 — Read the file
        content = await file.read()
        text = content.decode("utf-8")

    Step 2 — Validate it's not empty
        Raise HTTPException(400) if text is empty

    Step 3 — Chunk the text
        Use chunk_text() from app.core.chunker

    Step 4 — Embed the chunks
        Use embed_many() from app.core.embeddings

    Step 5 — Store in LanceDB
        Generate a document_id = str(uuid.uuid4())
        Use store_chunks() from app.core.vector_store

    Step 6 — Save metadata to PostgreSQL
        Use create_document() from app.db.crud

    Step 7 — Return IngestResponse

    Error handling:
        Wrap everything in try/except
        Raise HTTPException(500) with detail on error
    """
    pass
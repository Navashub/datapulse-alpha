"""
Pydantic Schemas — Request and Response models.

Schemas define:
  - What data comes INTO the API (request bodies)
  - What data goes OUT of the API (response bodies)

They are separate from database models intentionally.
You don't always want to expose every database field to the API.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class IngestResponse(BaseModel):
    """Response returned after successfully ingesting a document."""

    # TODO 1:
    # Add these fields:
    # - message: str
    # - document_id: str
    # - document_name: str
    # - chunk_count: int
    pass


class QueryRequest(BaseModel):
    """Request body for asking a question."""

    # TODO 2:
    # Add these fields:
    # - question: str with a Field example="What is this document about?"
    # - top_k: optional int, default 3 (how many chunks to retrieve)
    pass


class QueryResponse(BaseModel):
    """Response returned after answering a question."""

    # TODO 3:
    # Add these fields:
    # - question: str
    # - answer: str
    # - sources: list[str] — chunk IDs used
    pass


class DocumentResponse(BaseModel):
    """Represents a single document in the documents list."""

    # TODO 4:
    # Add these fields matching the Document database model:
    # - id: str
    # - name: str
    # - content_type: str
    # - chunk_count: int
    # - created_at: datetime

    class Config:
        from_attributes = True
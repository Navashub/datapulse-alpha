"""
CRUD Operations — Create, Read, Update, Delete.

This file contains all database query functions.
Keeping database logic here (separate from routes) is
a clean architecture pattern used in production systems.

Routes should NEVER write raw SQL or SQLAlchemy queries.
They call these functions instead.
"""

from sqlalchemy.orm import Session
from typing import Optional
from app.db.models import Document, QueryHistory
import uuid


def create_document(
    db: Session,
    name: str,
    content_type: str,
    chunk_count: int
) -> Document:
    """
    Save a new document record to PostgreSQL.

    Args:
        db: Active database session
        name: Original filename of the document
        content_type: MIME type e.g. "text/plain"
        chunk_count: Number of chunks created during ingestion

    Returns:
        The saved Document object

    TODO 1:
    - Create a Document instance with the provided fields
    - Add it to the session (db.add)
    - Commit the session (db.commit)
    - Refresh to get the saved data back (db.refresh)
    - Return the document
    - Wrap in try/except — rollback on error
    """
    pass


def get_all_documents(db: Session) -> list[Document]:
    """
    Retrieve all documents from PostgreSQL.

    Args:
        db: Active database session

    Returns:
        List of all Document records

    TODO 2:
    - Query the Document table and return all records
    - Hint: db.query(Document).all()
    """
    pass


def create_query_history(
    db: Session,
    question: str,
    answer: str,
    sources: str
) -> QueryHistory:
    """
    Save a question and answer to query history.

    Args:
        db: Active database session
        question: The user's question
        answer: The AI generated answer
        sources: Comma-separated chunk IDs used as context

    Returns:
        The saved QueryHistory object

    TODO 3:
    - Create and save a QueryHistory record
    - Same pattern as create_document above
    """
    pass
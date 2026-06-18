"""
Database models.

Each class here maps to a table in PostgreSQL.
SQLAlchemy uses these classes to:
  - Create the tables (via Alembic migrations)
  - Query and insert records
"""

from sqlalchemy import Column, String, Text, DateTime, Integer
from sqlalchemy.sql import func
from app.db.database import Base
import uuid


class Document(Base):
    """
    Stores metadata about each ingested document.

    Note: The actual text content is stored in LanceDB (vector store).
    PostgreSQL stores the metadata — who, what, when.
    This is a common pattern in RAG systems.
    """

    __tablename__ = "documents"

    # TODO 1:
    # Add the following columns:
    # - id: String, primary key, default to str(uuid.uuid4())
    # - name: String(255), not nullable
    # - content_type: String(50) — e.g. "text/plain", "application/pdf"
    # - chunk_count: Integer, default 0 — how many chunks were created
    # - created_at: DateTime, default to current time (use server_default=func.now())
    #
    # Hint: Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    pass


class QueryHistory(Base):
    """
    Stores every question asked and the AI answer given.

    Useful for:
    - Analytics (what are users asking most?)
    - Debugging (why did the AI give a wrong answer?)
    - Audit trail
    """

    __tablename__ = "query_history"

    # TODO 2:
    # Add the following columns:
    # - id: String, primary key, default uuid
    # - question: Text, not nullable
    # - answer: Text, not nullable
    # - sources: Text — comma separated chunk IDs used to answer
    # - created_at: DateTime, server_default=func.now()
    pass
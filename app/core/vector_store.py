"""
Vector Store Interface using LanceDB.

LanceDB stores our text chunks as vectors (embeddings).
It lets us search for chunks by meaning, not keywords.

How it works:
  1. We embed each chunk → get a vector
  2. We store the vector + original text in LanceDB
  3. When a user asks a question:
     a. We embed the question
     b. LanceDB finds the vectors closest to the question vector
     c. We return those chunks as context for the AI

LanceDB stores data as files on disk — no separate server needed.
Data persists between app restarts automatically.
"""

import lancedb
import pyarrow as pa
from app.config import settings

# Table name in LanceDB
TABLE_NAME = "document_chunks"

# Embedding dimension for text-embedding-3-small
EMBEDDING_DIM = 1536


def get_table():
    """
    Connect to LanceDB and return the chunks table.
    Creates the table if it doesn't exist yet.

    Returns:
        LanceDB table object

    TODO:
    1. Connect to LanceDB using lancedb.connect(settings.lancedb_uri)
    2. Check if TABLE_NAME exists in db.table_names()
    3. If it exists: return db.open_table(TABLE_NAME)
    4. If not: create it with this schema:
       schema = pa.schema([
           pa.field("id", pa.string()),
           pa.field("document_id", pa.string()),
           pa.field("document_name", pa.string()),
           pa.field("text", pa.string()),
           pa.field("vector", pa.list_(pa.float32(), EMBEDDING_DIM)),
       ])
       return db.create_table(TABLE_NAME, schema=schema)
    """
    pass


def store_chunks(
    document_id: str,
    document_name: str,
    chunks: list[str],
    embeddings: list[list[float]]
) -> None:
    """
    Store text chunks and their embeddings in LanceDB.

    Args:
        document_id: UUID of the document from PostgreSQL
        document_name: Original filename
        chunks: List of text chunks
        embeddings: Corresponding embedding vectors

    TODO:
    1. Get the table using get_table()
    2. Build a list of dictionaries, one per chunk:
       {
         "id": f"{document_id}_chunk_{i}",
         "document_id": document_id,
         "document_name": document_name,
         "text": chunks[i],
         "vector": embeddings[i]
       }
    3. Add them to the table: table.add(records)
    """
    pass


def search_chunks(
    query_embedding: list[float],
    top_k: int = 3
) -> list[dict]:
    """
    Find the most semantically similar chunks to a query.

    Args:
        query_embedding: Embedding of the user's question
        top_k: Number of chunks to return

    Returns:
        List of matching chunks with text and metadata

    TODO:
    1. Get the table using get_table()
    2. Search using:
       results = table.search(query_embedding).limit(top_k).to_list()
    3. Return the results
    """
    pass
"""
Embedding Utility.

An embedding is a list of numbers (a vector) that represents
the meaning of a piece of text.

Similar texts → similar vectors → close together in vector space

Example:
  "How do I reset my password?" 
  → [0.12, -0.43, 0.87, ...] (1536 numbers)
  
  "Steps to change my login credentials"
  → [0.11, -0.41, 0.85, ...] (very similar numbers!)

This is how semantic search works — we don't match keywords,
we match meaning.

We use OpenAI's text-embedding-3-small model.
It's fast, cheap, and produces 1536-dimensional vectors.
"""

from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.openai_api_key)

EMBEDDING_MODEL = "text-embedding-3-small"


def embed_text(text: str) -> list[float]:
    """
    Generate an embedding vector for a single piece of text.

    Args:
        text: Any text string to embed

    Returns:
        A list of floats representing the embedding vector

    TODO:
    Call the OpenAI embeddings API.
    Steps:
    1. Call client.embeddings.create()
       with model=EMBEDDING_MODEL and input=text
    2. Return the embedding from the response
       Hint: response.data[0].embedding

    Note: Clean the text first — replace newlines with spaces.
    OpenAI recommends this for better embeddings.
    """
    pass


def embed_many(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings for multiple texts in one API call.

    More efficient than calling embed_text() in a loop
    because it sends one request instead of many.

    Args:
        texts: List of text strings to embed

    Returns:
        List of embedding vectors (same order as input)

    TODO:
    Call client.embeddings.create() with the full list as input.
    Return all embeddings.
    Hint: [item.embedding for item in response.data]
    """
    pass
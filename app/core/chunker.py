"""
Text Chunking Utility.

Before storing text in a vector database, we split it into
smaller pieces called "chunks". This is important because:

1. Embedding models have token limits
2. Smaller chunks = more precise retrieval
3. We can find the EXACT part of a document that answers a question

Example:
  A 10 page PDF becomes 50 chunks of ~200 words each.
  When a user asks a question, we find the 3 most relevant chunks
  and send those to the AI — not the whole document.
"""

from typing import Optional


def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50
) -> list[str]:
    """
    Split text into overlapping chunks.

    Overlap means the end of chunk 1 appears at the start of chunk 2.
    This preserves context across chunk boundaries.

    Example with chunk_size=10, overlap=3:
      Text:    "The quick brown fox jumps over the lazy dog"
      Chunk 1: "The quick b"
      Chunk 2: " brown fox "    ← starts 3 chars before chunk 1 ended
      Chunk 3: "fox jumps ov"

    Args:
        text: The full document text to split
        chunk_size: Maximum characters per chunk
        overlap: How many characters to repeat between chunks

    Returns:
        List of text chunks

    TODO:
    Implement this function.
    Steps:
    1. Strip and clean the input text
    2. Use a sliding window approach:
       - Start at position 0
       - Take chunk_size characters
       - Move forward by (chunk_size - overlap) characters
       - Repeat until end of text
    3. Skip empty chunks
    4. Return the list of chunks

    Hint:
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            ...
    """
    pass
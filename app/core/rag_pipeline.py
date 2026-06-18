"""
RAG Pipeline — Retrieval Augmented Generation.

This is the brain of DataPulse AI.

RAG works in two steps:
  STEP 1 — RETRIEVE:
    Take the user's question.
    Search the vector store for relevant chunks.
    Return the top matching chunks as context.

  STEP 2 — GENERATE:
    Send the question + retrieved chunks to the LLM.
    The LLM reads the context and answers the question.
    The answer is grounded in the actual documents.

Why RAG instead of just asking the LLM directly?
  - LLMs don't know YOUR documents
  - RAG gives the LLM the right information at the right time
  - Answers are traceable back to source chunks
  - No hallucination about document contents
"""

from openai import OpenAI
from app.config import settings
from app.core.embeddings import embed_text
from app.core.vector_store import search_chunks

client = OpenAI(api_key=settings.openai_api_key)

CHAT_MODEL = "gpt-4o-mini"

SYSTEM_PROMPT = """
You are DataPulse AI, an intelligent document assistant.
Answer questions using ONLY the context provided below.
If the context does not contain enough information to answer,
say "I don't have enough information in the documents to answer that."
Always be concise and cite which part of the context you used.
"""


def run_rag_pipeline(
    question: str,
    top_k: int = 3
) -> dict:
    """
    Run the full RAG pipeline for a user question.

    Args:
        question: The user's question
        top_k: Number of chunks to retrieve

    Returns:
        Dictionary with:
        - answer: str (the AI generated answer)
        - sources: list[str] (chunk IDs used)
        - context: list[str] (actual chunk texts used)

    TODO:
    Implement the two-step RAG pipeline:

    STEP 1 — RETRIEVE:
    1. Embed the question using embed_text()
    2. Search for relevant chunks using search_chunks()
    3. Extract the text and IDs from results

    STEP 2 — GENERATE:
    4. Build a context string from the retrieved chunks:
       Format each chunk as:
       "--- Chunk [chunk_id] ---\n{chunk_text}\n"
    5. Call client.chat.completions.create() with:
       - model=CHAT_MODEL
       - messages=[
           {"role": "system", "content": SYSTEM_PROMPT},
           {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
         ]
    6. Extract the answer from the response
    7. Return the answer, sources, and context

    Hint for extracting answer:
        response.choices[0].message.content
    """
    pass
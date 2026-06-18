"""
API Tests.

These tests verify that each endpoint behaves correctly.
Your job: make all these tests pass.

Run with: pytest tests/ -v
"""

from fastapi.testclient import TestClient
import io


def test_health_check(client):
    """
    Health endpoint should return 200 with status healthy.
    """
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "app" in data
    assert "version" in data


def test_list_documents_empty(client):
    """
    Documents endpoint should return empty list when nothing ingested.
    """
    response = client.get("/documents")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_ingest_document(client):
    """
    Ingest endpoint should accept a text file and return chunk count.
    """
    fake_file = io.BytesIO(b"DataPulse AI is a document intelligence platform. "
                            b"It uses RAG to answer questions about your documents.")
    response = client.post(
        "/ingest",
        files={"file": ("test.txt", fake_file, "text/plain")}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["chunk_count"] > 0
    assert data["document_name"] == "test.txt"
    assert "document_id" in data


def test_ingest_empty_file(client):
    """
    Ingest endpoint should reject empty files with 400 error.
    """
    empty_file = io.BytesIO(b"")
    response = client.post(
        "/ingest",
        files={"file": ("empty.txt", empty_file, "text/plain")}
    )
    assert response.status_code == 400


def test_query_after_ingest(client):
    """
    Query endpoint should return an answer after a document is ingested.
    """
    # First ingest
    fake_file = io.BytesIO(b"The DataPulse AI API was built using FastAPI and LanceDB.")
    client.post(
        "/ingest",
        files={"file": ("info.txt", fake_file, "text/plain")}
    )

    # Then query
    response = client.post(
        "/query",
        json={"question": "What was DataPulse AI built with?"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "sources" in data
    assert len(data["answer"]) > 0
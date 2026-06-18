"""
Pytest configuration and shared fixtures.

Fixtures are reusable setup functions for tests.
The TestClient lets us make HTTP requests to the API in tests
without running a real server.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """
    Provides a test client for making requests to the API.
    Use this in every test function.
    """
    return TestClient(app)
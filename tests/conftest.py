import pytest
from fastapi.testclient import TestClient

from agora_library_server.main import app


@pytest.fixture
def client():
    return TestClient(app)

import os

# Must be set before importing app.main
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_projects_endpoint_returns_response():
    response = client.get("/projects")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_future_endpoint_returns_response():
    response = client.get("/future")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
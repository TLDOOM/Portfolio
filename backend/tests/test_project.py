import os

os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from fastapi.testclient import TestClient
from app.core.db import Base, engine
from app.main import app

Base.metadata.create_all(bind=engine)


def test_projects_endpoint_returns_response():
    with TestClient(app) as client:
        response = client.get("/projects")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_future_endpoint_returns_response():
    with TestClient(app) as client:
        response = client.get("/future")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
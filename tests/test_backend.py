# tests/test_backend.py
import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from backend.app.main import app  # импорт safe, engine не нужен

client = TestClient(app)

def test_crud():
    response = client.post("/sources/", json={"name": "Test", "url": "https://test.com"})
    assert response.status_code == 200
    source_id = response.json()["id"]

    response = client.get("/sources/")
    assert any(s["id"] == source_id for s in response.json())

    response = client.put(f"/sources/{source_id}", json={"name": "Test2", "url": "https://test2.com"})
    assert response.json()["name"] == "Test2"

    response = client.delete(f"/sources/{source_id}")
    assert response.json()["ok"] == True
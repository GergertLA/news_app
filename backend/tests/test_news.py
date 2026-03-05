from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_news(client):
    response = client.get("/sources/")
    assert response.status_code == 200
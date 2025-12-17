from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={"x": 3})
    assert response.status_code == 200
    assert response.json()["result"] == 6

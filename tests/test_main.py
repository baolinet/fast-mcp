import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

# def test_read_root():
#     resp = client.get("/")
#     assert resp.status_code == 200
#     assert "msg" in resp.json()

# def test_ask_agent():
#     resp = client.get("/api/v1/agent/ask?q=你好")
#     assert resp.status_code == 200
#     data = resp.json()
#     assert data["question"] == "你好"
#     assert "answer" in data

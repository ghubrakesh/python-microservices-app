from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Enter the /search/<query> to search the pages or \n /wiki/<name> to get the summary of the page"
    }
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Enter the /search/<query> to search the pages or \n /wiki/<name> to get the summary of the page"
    }


def test_read_phrase():
    response = client.get("/phrase/wondder woman")
    assert response.status_code == 200
    assert response.json() == {
        "results": [
            "wonder woman",
            "american psychologist",
            "william moulton marston",
            "pen name",
            "charles moulton",
            "harry g. peter",
            "dc comics",
            "marston",
            "'s wife",
            "elizabeth",
            "life partner",
            "olive byrne",
            "character 's appearance.wonder",
            "woman",
            "american comic books",
            "dc comics",
            "justice league",
            "comics",
            "october",
            "sensation comics",
            "january",
            "wonder woman",
            "dc comics",
        ]
    }

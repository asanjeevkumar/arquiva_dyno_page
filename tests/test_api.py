from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "The saved string is dynamic string" in response.text

def test_update_string():
    new_string = "updated test string"
    response = client.post(
        "/update-string",
        json={"new_string": new_string}
    )
    assert response.status_code == 200
    assert response.json()["new_string"] == new_string

    # Verify the string was updated
    response = client.get("/")
    assert response.status_code == 200
    assert f"The saved string is {new_string}" in response.text 
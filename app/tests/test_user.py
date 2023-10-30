from app.tests.base import client
from app.tests.utils import generate_random_user

from httpx import Response


def create_user(random_user_data=None) -> Response:
    random_user_data = random_user_data or generate_random_user()
    response = client.post("/api/users", json=random_user_data)
    return response


def test_create_user():
    random_user_data = generate_random_user()
    response = create_user(random_user_data)
    assert response.status_code == 201, response.text
    assert response.json()["email"] == random_user_data["email"]
    assert response.json()["username"] == random_user_data["username"]
    assert response.json()["last_name"] == random_user_data["last_name"]
    assert response.json()["first_name"] == random_user_data["first_name"]


def test_retrieve_user():
    db_user = create_user().json()
    response = client.get(f"/api/users/{db_user['id']}")
    assert response.status_code == 200, response.text
    assert response.json()["email"] == db_user["email"]
    assert response.json()["username"] == db_user["username"]
    assert response.json()["last_name"] == db_user["last_name"]
    assert response.json()["first_name"] == db_user["first_name"]


def test_retrieve_user_list():
    [create_user() for _ in range(2)]
    response = client.get("/api/users")
    assert response.status_code == 200, response.text
    assert len(response.json()) >= 2

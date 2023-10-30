from app.tests.base import client
from app.tests.utils.asset import generate_random_asset

from httpx import Response


def create_asset(random_asset_data=None) -> Response:
    random_asset_data = random_asset_data or generate_random_asset()
    response = client.post("/api/assets", json=random_asset_data)
    return response


def test_create_asset():
    random_asset_data = generate_random_asset()
    response = create_asset(random_asset_data)
    assert response.status_code == 201, response.text
    assert response.json()["name"] == random_asset_data["name"]
    assert response.json()["symbol"] == random_asset_data["symbol"]
    assert (
        response.json()["pip_on_decimal"] ==
        random_asset_data["pip_on_decimal"]
    )


def test_retrieve_asset():
    db_asset = create_asset().json()
    response = client.get(f"/api/assets/{db_asset['symbol']}")
    assert response.status_code == 200, response.text
    assert response.json()["name"] == db_asset["name"]
    assert response.json()["symbol"] == db_asset["symbol"]
    assert response.json()["pip_on_decimal"] == db_asset["pip_on_decimal"]


def test_retrieve_asset_list():
    [create_asset() for _ in range(2)]
    response = client.get("/api/assets")
    assert response.status_code == 200, response.text
    assert len(response.json()) >= 2

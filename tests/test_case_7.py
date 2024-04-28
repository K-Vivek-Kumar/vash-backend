import json

from project import create_app


def test_user_login(client):
    login_data = {"email": "vash1@ret.in", "password": "vash"}
    response = client.post("/login", json=login_data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "access_token" in data
    assert isinstance(data["access_token"], str)


def test_retailer_login(client):
    app = create_app()
    with app.test_client() as client:
        response = client.post(
            "/retailer-login",
            json={"email": "vash4@ret.in", "password": "vash"},
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "access_token" in data
        assert isinstance(data["access_token"], str)
    print("Successful")
